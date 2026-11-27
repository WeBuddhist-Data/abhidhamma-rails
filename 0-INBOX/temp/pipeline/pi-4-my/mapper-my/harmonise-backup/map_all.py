"""Pāli→Burmese keyword mapping for pi-4 (Puggalapaññatti, «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း»), the WHOLE book.

usage (/opt/homebrew/Caskroom/miniconda/base/bin/python3 -I -X utf8, from any directory):
  map_all.py             writes <ch>.mapped.md for every chapter and map-table.md, then verifies them
  map_all.py --report    writes nothing; lists unmapped keywords and presence failures
  map_all.py --seg ID..  prints Pāli, Burmese, keywords and mapping (with the source of each value)
  map_all.py --dump CH   prints the mapping of every segment of a chapter with the source of each value

Method: a copy (not an import) of the approved pi-3 Burmese mapper (pi-3-my/mapper-my/map_all.py, itself the pi-3
version of pi-2's and pi-1's): tables keyword -> Burmese in dictionary form, per-segment overrides CTX, context
functions, compose rules and the presence verifier (presence_check.py, a copy of pi-3's ONE shared check). The
Burmese is the FINAL pi-4 text of this track (AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters).
No other Burmese source is used.

Lookup order per keyword:
  CTX[sid] -> the chapter's own table T_<ch> -> the shared tables of the other chapters
  -> TERMS: the approved pi-4 forms of my4-zeroshot-terms.md (person-type names, titles, list items), when present
  -> a pi-1 / pi-2 / pi-3 multiword value that the text has as a phrase
  -> compose rules (X dhammā / X puggalo / na X / numbers)
  -> PRIOR: the final pi-2, then pi-3, then pi-1 mapping, the most frequent value of that keyword present in THIS
     segment (literal contiguous presence first, then presence by an ending rule)
A value «@name» is a context function f(kw, pali, my).
"""
import re, sys, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-4_split_chapters"
MAPS = {t: ROOT / f"AI_translation/burmese/{t}-keywords-by-reference-pali-burmese-plain.md" for t in ("pi-1", "pi-2", "pi-3")}
TERMS_FILE = HERE.parent / "my4-zeroshot-terms.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
NONE = "(no direct equivalent)"
PUG = "ပုဂ္ဂိုလ်"

sys.path.insert(0, str(HERE))
from presence_check import ATTR_FROM, VERB_FROM, chunk_present, presence  # noqa: E402,F401


def low(w):
    return w[:1].lower() + w[1:]


# =====================================================================================================
# chapter tables
# =====================================================================================================
# ---- TABLES-BEGIN
# ---------------------------------------------------------------------------------------------- preamble
T_PREAMBLE = {
    # pi-1 / pi-2 / pi-3 preamble values (approved samples), unchanged
    "abhidhamma": "အဘိဓမ္မာ", "Abhidhammapiṭake": "အဘိဓမ္မာပိဋက",
    "namo": "ရှိခိုးသည်", "bhagavato": "မြတ်စွာဘုရား", "arahato": "ရဟန္တာ",
    "sammāsambuddhassa": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
    "sambuddha": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်",
    # the pi-4 book title (rule 7: the approved title whole) and its members (my4-zeroshot-terms «Book title»)
    "paññatti": "@pannatti", "puggala": "ပုဂ္ဂိုလ်", "puggalapaññatti": "@puggalapannatti",
}

# ---------------------------------------------------------------------------------------------- 1-matika
T_MATIKA = {
    # --- the six designations (^4-M-1 … ^4-M-6; my4-zeroshot-terms «The six designations»)
    "paññattiyo": "သတ်မှတ်ချက်",
    "Kittāvatā": "အဘယ်မျှ", "Yāvatā": "ရှိသမျှ", "ettāvatā": "ဤမျှ",
    "Kittāvatā khandhānaṃ": "@kittavata", "Kittāvatā āyatanānaṃ": "@kittavata", "Kittāvatā dhātūnaṃ": "@kittavata",
    "Kittāvatā saccānaṃ": "@kittavata", "Kittāvatā indriyānaṃ": "@kittavata", "Kittāvatā puggalānaṃ": "@kittavata",
    "ettāvatā khandhānaṃ": "@ettavata", "ettāvatā āyatanānaṃ": "@ettavata", "ettāvatā dhātūnaṃ": "@ettavata",
    "ettāvatā saccānaṃ": "@ettavata", "ettāvatā indriyānaṃ": "@ettavata", "ettāvatā puggalānaṃ": "@ettavata",
    "dukkha": "@dukkha", "sukha": "@sukha", "rūpa": "@rupa", "hoti": "@hoti", "sammā": "@samma", "saṅkhāra": "@sankhara", "sota": "@sota",
    "puthu": "@puthu", "vaṇṇa": "@vanna", "dhamma": "@dhamma", "gāmī": "@gami", "phala": "@phala", "ṭhita": "@thita", "eka": "@eka",
    # --- fragments of the person-type names (rule 8 / P2: the part of the NAME that carries the fragment;
    #     participles and -ī adjectives in the attributive «…သော», pi-1 rule 3; the first compound decides)
    "bhabba": "@bhabba", "abhabba": "မထိုက်တန်သော", "āgamano": "ရှေ့သို့ တိုးတက်ရန်",
    "cetanā": "စေတနာ", "anurakkhaṇā": "စောင့်ရှောက်ခြင်း",
    "kappī": "ကမ္ဘာ", "ṭhito": "@thito",
    "upahacca": "သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ", "antarā": "သက်တမ်း၏ အလယ်သို့ မရောက်မီ",
    "parinibbāyī": "ပရိနိဗ္ဗာန် ပြုသော",
    "patto": "ရောက်သော", "dhammo": "သဘော ရှိသော",
    "kuppa": "ပျက်ယွင်းတတ်သော", "akuppa": "မပျက်ယွင်းတတ်သော", "parihāna": "ဆုတ်ယုတ်တတ်သော",
    "sīsī": "ကုန်ဆုံးသော", "sama": "@sama",
    "gotra": "အရိယာ အနွယ်", "bhū": "ပြောင်းသော",
    "kola": "အမျိုး", "bījī": "မျိုးစေ့ … ရှိသော",
    "anusārī": "အစဉ်လိုက်သော",
    "sotāpattiphala": "သောတာပတ္တိဖိုလ်", "phalasacchikiriyāya": "ဖိုလ်ကို မျက်မှောက်ပြုရန်",
    "sacchikiriyāya paṭipanno": "မျက်မှောက်ပြုရန် ကျင့်ကြံသော", "paṭipanno": "@patipanno",
    "akaniṭṭha": "အကနိဋ္ဌ ဘုံ", "uddhaṃsoto": "အထက်သို့ စီးဆင်း၍",
    "vijjo": "အမှန်သိမြင်မှု … ရှိသော", "vimutto": "လွတ်မြောက်သော", "jano": NONE,   # puthujjana = one word ပုထုဇဉ်
    "paccekabuddho": NONE,                  # the variant in Roman script inside the text's bracket (pi-1)
    "phalesu": NONE,                        # the variant in Roman script inside the text's bracket (^4-M-12)
    "uparato": "ရှောင်ကြဉ်သော", "pacceka": "ပစ္စေကဗုဒ္ဓါ", "samaya": "အချိန်အလိုက်",
    "bhāga": "နှစ်ဖက်စလုံး",                 # ubhatobhāga «နှစ်ဖက်စလုံးမှ» (the ablative goes, rule 1)
    # --- ^4-M-8 (twos)
    "hiriko": "ဒုစရိုက်ကို ရှက်သော", "vaco": "သွန်သင်ချက်ကို နားထောင်သော", "upaṭṭhita": "တည်နေသော",
    "paṇīta": "မွန်မြတ်သော", "vipanno": "ပျက်စီးသော", "saṃyojano": "နှောင်ကြိုး ရှိသော",
    "mitto": "မိတ်ဆွေ … ပေါင်းသင်းသော", "vaḍḍhanti": "တိုးပွားသည်",
    "guttadvāro": "တံခါးကို စောင့်ထိန်းသော", "ññū": "သိသော", "matta": "အတိုင်းအရှည်",
    "puggalā dullabhā": "ရခဲသော ပုဂ္ဂိုလ်", "dullabhā": "ရခဲသော", "tappayā": "ရောင့်ရဲစေရန်",
    # --- ^4-M-9 (threes)
    "sevitabbo": "ပေါင်းသင်းအပ်", "bhajitabbo": "ဆည်းကပ်အပ်", "payirupāsitabbo": "ချဉ်းကပ် ခစားအပ်",
    "jigucchitabbo": "စက်ဆုပ်အပ်", "ajjhupekkhitabbo": "လျစ်လျူရှုအပ်",
    "sakkatvā": "ရိုသေ၍", "garuṃ katvā": "လေးစားကာ",
    "potthaka": "လျှော်ပိတ်စ", "kāsika": "ကာသိ", "kāsikavattha": "ကာသိ ပိတ်စ",
    "samādhismiṃ": "သမာဓိ", "samādhismiṃ paññāya": "သမာဓိ … ပညာ",
    "gūtha": "မစင်", "bhāṇī": "စကားပြောသော",
    "pathavi": "မြေ", "pāsāṇa": "ကျောက်", "lekhā": "အရေးအကြောင်း",
    "bhavesu": "ဘဝ", "sīlesu": "သီလ",
    "paripūrakārī": "ပြည့်စုံစွာ ကျင့်သော", "sīlesu paripūrakārī": "သီလတို့ကို ပြည့်စုံစွာ ကျင့်သော",
    "puggalo paripūrakārī": "ပုဂ္ဂိုလ် … ပြည့်စုံစွာ ကျင့်သော", "kārī": "@kari",
    "āso": "မျှော်လင့်ချက် ရှိသော", "vigata": "@vigata",
    "ucchaṅga": "ပေါင်ခွင်", "avakujja": "မှောက်ထားသော အိုး", "pañño": "ပညာ ရှိသော",
    "pameyyo": "@pameyyo", "citto": "စိတ် ရှိသော", "citto puggalo": "စိတ် ရှိသော ပုဂ္ဂိုလ်",
    "pañño puggalo": "ပညာ ရှိသော ပုဂ္ဂိုလ်",
    "gilāna": "@gilana", "aruka": "အနာ", "satthāro": "ဆရာ",
    # --- ^4-M-10 (fours)
    "tacchaṃ": "ဟုတ်တိုင်း", "bhūtaṃ": "အမှန်အတိုင်း",
    "yutta": "သင့်လျော်သော", "mutta": "@mutta", "paṭibhāno": "ဉာဏ်ပေါ်မှု ရှိသော",
    "samaṇesu": "ရဟန်း",
    "avaṇṇaṃ bhāsitā": "ကဲ့ရဲ့ ပြောဆိုသော", "vaṇṇaṃ bhāsitā": "ချီးမွမ်း ပြောဆိုသော",
    "balībadda": "နွားလား", "valāhaka": "မိုးတိမ်", "mūsika": "ကြွက်", "kumbha": "အိုး",
    "udakarahada": "ရေကန်", "āsīvisa": "မြွေဆိုး",
    "samathassa": "စိတ်ငြိမ်သက်ခြင်း", "cetosamathassa": "စိတ်ငြိမ်သက်ခြင်း",
    "sītībhūto": "အေးမြသော", "nibbuto": "ငြိမ်းအေးသော", "nicchāto": "ဆာလောင်မှု ကင်းသော", "chāto": "ဆာလောင်မှု",
    "Tamo": "မှောင်မိုက်", "joti": "အလင်း", "parāyano": "ရှေးရှုသော",
    "arahassa": "ထိုက်သော", "avaṇṇārahassa": "ကဲ့ရဲ့ထိုက်သော", "vaṇṇārahassa": "ချီးမွမ်းထိုက်သော",
    "appasādaṃ": "မကြည်ညိုမှု", "upadaṃsitā": "ပြသသော", "pasādaṃ upadaṃsitā": "ကြည်ညိုမှုကို ပြသသော",
    "pasādanīye ṭhāne pasādaṃ": "ကြည်ညိုထိုက်သော အရာ၌ ကြည်ညိုမှု",
    "uṭṭhāna": "ကြိုးစားအားထုတ်မှု", "upajīvī": "အသက်မွေးသော",
    "anuvicca": "စုံစမ်း", "pariyogāhetvā": "@pariyogahetva",
    "paṭisaṃvedī": "ခံစားသော", "vipañcita": "အကျယ် ရှင်းပြမှ", "ugghaṭita": "အကျဉ်းကို ကြားရုံဖြင့်",
    "pada": "@pada", "lābhī": "ရရှိသော",
    "adhipaññā": "လွန်ကဲသော ပညာ", "adhipaññādhamma": "လွန်ကဲသော ပညာဖြင့် သဘောတရား",
    "vipassanāya": "ထိုးထွင်းသိမြင်ခြင်း", "dhammavipassanāya": "သဘောတရားတို့ကို ထိုးထွင်းသိမြင်ခြင်း",
    "brahma": "မြင့်မြတ်သော", "pamāṇo": "အတိုင်းအတာ ထား၍", "pasanno": "ကြည်ညိုသော",
    "lūkha": "ကြမ်းတမ်းခြင်း", "ghosa": "အသံဗလံ",
    "suto": "အကြားအမြင်", "upapanno": "@upapanno", "sutena upapanno": "အကြားအမြင်နှင့် ပြည့်စုံသော",
    "puriso": "သူတော်ကောင်း", "asappurisataro": "သူတော်ကောင်း မဟုတ်သူထက် ပို၍ သူတော်ကောင်း မဟုတ်သူ",
    "puggalo attantapo": "ပုဂ္ဂိုလ် … မိမိကိုယ်ကို ပူပန်စေသော", "puggalo paṭipanno": "ပုဂ္ဂိုလ် … ကျင့်ကြံသော",
    "dhammakathikā puggalā": "တရား ဟောပြောသော ပုဂ္ဂိုလ်", "dhammakathikā": "တရား ဟောပြောသော",
    "kathikā": "ဟောပြောသော",
    "anuyoga": NONE,           # P4: «anuyogam anuyutto» = the one verb «… အားထုတ်သူ» (anuyutto), as pi-1 caya
    "paritāpanānuyoga": "ပူပန်စေခြင်း", "paritāpana": "ပူပန်စေခြင်း",
    "atta": "မိမိ", "attanā": "@attana", "tapo": "ပူပန်စေသော",
    "padumo": "ကြာနီ", "puṇḍarīko": "ကြာဖြူ", "sukhumālo": "နူးညံ့သိမ်မွေ့သော", "acalo": "မတုန်လှုပ်သော",
    "pāraṅgato": "ကမ်းတစ်ဖက်သို့ ရောက်သော", "thale": "ကုန်းပေါ်", "oṇato": "နိမ့်ရာ",
    # --- ^4-M-11 (fives): the ascetic practices are person nouns (group names «Pañca X»: the NAME «…သူ»)
    "abbhokāsikā": "လွင်တီးခေါင်၌ နေသူ", "piṇḍa": "ဆွမ်း", "piṇḍapātikā": "ဆွမ်းခံ၍သာ စားသူ",
    "sosānikā": "သုသာန်၌ နေသူ", "mūlikā": "ရင်း၌ နေသူ", "āraññikā": "တော၌ နေသူ",
    "nesajjikā": "မလျောင်းဘဲ ထိုင်၍သာ နေသူ", "bhattikā": "နောက်မှ ကပ်သော ဆွမ်းကို မစားသူ",
    "khalu": NONE,             # khalupacchābhattika: the refusal is the negative inside «… မစားသူ» (bhattikā)
    "santhatikā": "ခင်းထားသည့်အတိုင်း နေရာ၌ နေသူ", "yathā": "@yatha",
    "paṃsukūlikā": "ပံ့သကူ သင်္ကန်းကိုသာ ဝတ်သူ", "cīvarikā": "သင်္ကန်း … ဆောင်သူ", "āsanikā": "တစ်ထိုင်တည်းသာ စားသူ",
    "momūho": "အလွန် တွေဝေသော", "mando": "ထုံထိုင်းသော",
    "Datvā": "ပေးပြီးနောက်", "avajānāti": "အထင်သေးသည်", "saṃvāsena": "အတူ နေခြင်း",
    "paññāvimuttiṃ": "ပညာဖြင့် လွတ်မြောက်ခြင်း", "parisesā": "အကြွင်းအကျန် ရှိသော",
    "vippaṭisārī": "နောင်တ ရသော", "ārabhati": "မှားယွင်းစွာ ပြုမူသည်", "yodhājīva": "စစ်သည်",
    # --- ^4-M-12 (sixes)
    "sabbaññutaṃ": "အလုံးစုံကို သိသော ဉာဏ်", "pāpuṇāti": "ရောက်သည်", "abhisambujjhati": "အပြည့်အဝ သိမြင်သည်",
    "sāmaṃ": "ကိုယ်တိုင်", "āgantā": "ပြန်လာမည့်", "āgāmī": "ပြန်လာသော",
    "sāvaka": "တပည့်", "pāramiṃ": "ပါရမီ",
    "dukkhassantakaro": "ဒုက္ခ၏ အဆုံးကို ပြုသော", "karo": "ပြုသော", "dukkhassa": "@dukkhassa",
    "anussutesu": "ကြားဖူးသော", "ananussutesu dhammesu": "မကြားဖူးသော တရား", "dhammesu": "@dhammesu",
    "diṭṭhe dhamme": "မျက်မှောက်ဘဝ", "vasībhāvaṃ": "နိုင်နင်းခြင်း", "balesu": "စွမ်းအား",
    # --- ^4-M-13 (sevens)
    "Sakiṃ": "တစ်ကြိမ်", "nimuggo": "နစ်နေသော", "ummujjitvā": "ပေါ်လာပြီး",
    "viloketi": "ပတ်ဝန်းကျင်ကို ကြည့်သည်", "patarati": "ကူးခတ်သည်", "paṭigādha": "ခြေကုပ်ရာ",
    "tiṭṭhati": "ရပ်တည်နေသည်",
    # --- ^4-M-14 … ^4-M-16
    "samaṅgino puggalā": "ပြည့်စုံသော ပုဂ္ဂိုလ်", "samaṅgino": "ပြည့်စုံသော",
    "niṭṭhā": "ပြီးမြောက်ခြင်း", "vihāya": "စွန့်ခွာပြီးမှ",
}

# numbers of persons (my4-zeroshot-terms «persons are counted «ပုဂ္ဂိုလ် Nယောက်»»; pi-1 harmonise decision 5: the
# count keeps the text's classifier)
NUM_MY = {"eka": "တစ်", "ekaṃ": "တစ်", "dve": "နှစ်", "dvinnaṃ": "နှစ်", "tayo": "သုံး", "tiṇṇaṃ": "သုံး",
          "cattāro": "လေး", "catunnaṃ": "လေး", "pañca": "ငါး", "pañcannaṃ": "ငါး", "cha": "ခြောက်", "channaṃ": "ခြောက်",
          "satta": "ခုနစ်", "sattannaṃ": "ခုနစ်", "aṭṭha": "ရှစ်", "aṭṭhannaṃ": "ရှစ်", "nava": "ကိုး",
          "navannaṃ": "ကိုး", "dasa": "ဆယ်", "dasannaṃ": "ဆယ်"}
T_EKAKA = {
    # --- the definition frame (my4-zeroshot-terms «The definition frame»): «X ဟူသည် အဘယ် ပုဂ္ဂိုလ်နည်း»
    "Katamo": "အဘယ်", "Katamo puggalo": "အဘယ် ပုဂ္ဂိုလ်",
    # --- ^4-1 … ^4-8
    "samayena": "အချိန်အလိုက်", "vimokkhe": "လွတ်မြောက်ခြင်း", "parikkhīṇā": "ကုန်ခန်းသော",
    "ariyapuggalā": "အရိယာ ပုဂ္ဂိုလ်",
    "sahagatānaṃ": "အတူ ဖြစ်သော", "rūpasahagatānaṃ": "သိမ်မွေ့သော ရုပ်ဘုံနှင့်အတူ ဖြစ်သော",
    "kasira": "@kasira", "kiccha": "ခက်ခဲ",
    "lābhī samāpattīnaṃ": "ဈာန် ဝင်စားရာ … ရရှိသော", "puggalo lābhī": "ပုဂ္ဂိုလ် … ရရှိသော",
    "yatthicchakaṃ": "အလိုရှိရာ", "yadicchakaṃ": "အလိုရှိသည်", "icchakaṃ": "အလိုရှိသမျှ",
    "pamādaṃ": "မေ့လျော့မှု", "Aṭṭhānaṃ": "မဖြစ်နိုင်သော အကြောင်း",
    "parihāyati": "ဆုတ်ယုတ်သည်", "anusañceteti": "အဖန်ဖန် စေတနာ ထားသည်", "anurakkhati": "စောင့်ရှောက်သည်",
    # --- ^4-9 … ^4-23
    "pahīnāni": "@pahina", "pahīnā": "@pahina", "avakkanti": "သက်ဆင်းခြင်း",
    "janā": NONE,                        # puthujjanā = the one word «ပုထုဇဉ်» (as jano, pi-2 harmonise decision 4)
    "uparatā": "ရှောင်ကြဉ်သော", "kamma": "ကံ", "eḷā": "နုံအသော",
    "ānantarikā": "ချက်ချင်း အကျိုးပေးသော ကံ ရှိသော", "diṭṭhikā": "အယူ ရှိသော", "ṭhitā": "တည်နေသော",
    "uḍḍayhana": "မီးလောင်ရမည့်", "sacchikaroti": "မျက်မှောက် ပြုသည်", "abhiñño": "ထူးကဲစွာ သိခြင်း … ရှိသော",
    "sambuddho": "@sambuddho",
    # --- ^4-24 … ^4-30
    "nirodho": "ချုပ်ငြိမ်းခြင်း", "vodiṭṭhā": "ကောင်းစွာ မြင်ပြီးသော", "vocaritā": "ကောင်းစွာ ဆင်ခြင်ပြီးသော",
    "gāminī paṭipadā": "ရောက်စေသော ကျင့်စဉ်", "paveditā": "ဟောကြားထားသော", "dhammā": "@dhamma_pl",
    "paveditā dhammā": "ဟောကြားထားသော တရား", "pattassa": "ရောက်သော",
    "vāhiṃ": "ဆောင်သော", "puggalassa paṭipannassa": "ကျင့်ကြံသော … ပုဂ္ဂိုလ်", "paṭipannassa": "ကျင့်ကြံသော",
    "sacchikiriyāya paṭipannassa": "မျက်မှောက်ပြုရန် ကျင့်ကြံသော", "adhimattaṃ": "လွန်ကဲသော",
    # --- ^4-31 … ^4-44
    "saṃyojanānaṃ": "နှောင်ကြိုး", "parikkhayā": "ကုန်ခန်းခြင်း", "dukkhassantaṃ": "ဒုက္ခ၏ အဆုံး",
    "sambodhi": "အပြည့်အဝ သိမြင်ခြင်း", "vinipātadhammo": "အပါယ်သို့ ကျတတ်သော သဘော ရှိသော",
    "mānuse": "လူ", "khattuṃ": "ကြိမ်", "sandhāvitvā": "ကူးသွား", "saṃsaritvā": "ကျင်လည်ပြီး",
    "mānusakaṃ": "လူ့", "nibbattetvā": "ပေါ်ထွက်စေ၍",
    "āgantvā": "ပြန်လာ၍", "mohānaṃ": "မောဟ", "tanuttā": "ပါးလျခြင်း", "sakiṃ": "တစ်ကြိမ်",
    "āvattidhammo": "ပြန်လာတတ်သော သဘော ရှိသော", "āvatti": "ပြန်လာတတ်သော",
    "orambhāgiyānaṃ saṃyojanānaṃ": "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး", "opapātiko": "အလိုအလျောက် ပေါ်လာသော",
    "sañjaneti": "ဖြစ်ပေါ်စေသည်", "upariṭṭhimānaṃ saṃyojanānaṃ": "အထက်ပိုင်း နှောင်ကြိုး",
    "vemajjhaṃ": "အလယ်", "pattaṃ": "ရောက်", "kālakiriyaṃ": "ကွယ်လွန်ခြင်း", "atikkamitvā": "ကျော်လွန်၍",
    "atappaṃ": "အတပ္ပါ ဘုံ", "avihā": "အဝိဟာ ဘုံ", "sudassaṃ": "သုဒဿာ ဘုံ",
    "tanubhūtā": "ပါးလျသော", "avasesa": "@avasesa", "sekkhā": "ကျင့်ကြံဆဲသူ",
}
T_DUKA = {
    # --- ^4-45 … ^4-52: the synonym lists (pi-1 / pi-2 rails text; each synonym its own word)
    "pahīno": "@pahina", "pahīnaṃ": "@pahina",
    "kammaṃ": "@kammam", "byāpajjitattaṃ": "ဖောက်ပြန်ထားသော အဖြစ်", "daḷhīkammaṃ": "ခိုင်မြဲအောင် ပြုခြင်း",
    "vibha": "ခွဲခြမ်းစိတ်ဖြာခြင်း",        # the reference «vibha. 891» = «“ခွဲခြမ်းစိတ်ဖြာခြင်း” 891» (a translated note, pi-3 M9)
    "niṭṭhuriya": "ရက်စက်ခြင်း", "ṭhānaṃ": "@thanam", "āhāro": "@aharo",
    "issāyitattaṃ": "ငြူစူထားသော အဖြစ်", "usūyitattaṃ": "သဝန်တိုထားသော အဖြစ်",
    "maccharāyitattaṃ": "ဝန်တိုထားသော အဖြစ်",
    "pārikkhattiyaṃ": "ကြော့ရှင်းဟန် ပြသော အဖြစ်", "parikkhattattā": "ကြော့ရှင်းဟန် ပြခြင်း", "pari": "အလွန်",
    "evaṃ": "@evam",
    "paṭicchādana": "ဖုံးကွယ်ရန်", "hetu": "@hetu", "āvi": "ပေါ်လွင်အောင်", "uttānī": "ထင်ရှားအောင်",
    "pāpakiriyā": "ယုတ်မာသော အမှုကို ပြုခြင်း",
    # --- ^4-55 … ^4-62
    "saha": "လျော်စွာ", "dhammike": "တရား", "patissavatā": "နာခံမှု ရှိခြင်း", "ādariyatā": "လေးစားသော အဖြစ်",
    "anādariyatā": "မလေးစားသော အဖြစ်", "gāravatā": "ရိုသေမှု ရှိခြင်း", "ādariyaṃ": "လေးစားခြင်း",
    "sambhatti": "ကောင်းစွာ ကိုးကွယ်ခြင်း", "sīlā": "သီလ",
    "aguttadvāratāya": "တံခါးကို မစောင့်ထိန်းခြင်း", "ññutā": "သိခြင်း", "dhāraṇatā": "@dharanata",
    "saṅgāhaṇā": "စုစည်း၍ ယူနိုင်ခြင်း", "pekkhaṇā": "ရှုမြင်ခြင်း", "paccakkha": "ကိုယ်တိုင် ထင်ထင်ရှားရှား",
    "pariyogāhaṇā": "နက်နက်နဲနဲ သက်ဝင်နိုင်ခြင်း", "abhisamayo": "@abhisamayo",
    "paṭivedho": "ထိုးဖောက်၍ သိခြင်း",
    "sīlavipatti": "သီလ ပျက်စီးခြင်း", "āyatanaṃ": "@ayatanam", "cintetabbā": "စဉ်းစားရမည့်", "siddhi": "ဖြစ်ပုံ",
    "sabbattha": NONE,               # the sigla «(sabbattha)» kept in Roman script inside the bracket (pi-1)
    "paṭiggāho": "လက်ခံ စွဲကိုင်ခြင်း", "ku": "မှား",
    "sammāpaṭipannā": "@sammapatipanna", "pavedenti": "ဟောကြားသည်",
    # --- ^4-63 … ^4-90
    "orambhāgiyāni saṃyojanāni": "အောက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး",
    "uddhambhāgiyāni saṃyojanāni": "အထက်ပိုင်း ဘုံနှင့် ဆိုင်သော နှောင်ကြိုး",
    "Katamo pugalo": "အဘယ် ပုဂ္ဂိုလ်", "pugalo": PUG,      # the Pāli misprint pugalo (^4-70) = puggalo
    "cariya": "အကျင့်", "purāṇaṃ": "ဟောင်းသော",
    "sīlasampadā": "သီလ ပြည့်စုံခြင်း", "diṭṭhisampadā": "အယူ ပြည့်စုံခြင်း",
    "vedī": "ဆပ်သော", "kata": "ကျေးဇူး", "kataññū": "ကျေးဇူးကို သိသော",
    "duttappayā": "ရောင့်ရဲစေရန် ခက်ခဲသော", "sutappayā": "ရောင့်ရဲစေရန် လွယ်ကူသော",
    "nikkhipati": "သိုမှီးထားသည်", "vissajjeti": "စွန့်ကြဲသည်", "laddhaṃ": "ရတိုင်း", "laddhaṃ laddhaṃ": "ရတိုင်း ရတိုင်း",
    "kukkuccāyitabbaṃ": "နောင်တ ပူပန်ရန် ထိုက်သော", "kukkuccāyati": "နောင်တ ပူပန်သည်", "bhajati": "ဆည်းကပ်သည်",
    "sambuddhā": "@sambuddho", "sāvakā": "တပည့်", "vuccati": "@vuccati",
    "sevati": "ပေါင်းသင်းသည်",      # sevati bhajati payirupāsati = ပေါင်းသင်း / ဆည်းကပ် / ချဉ်းကပ် ခစား (as sevitabbo …)
    "gataṃ": "@gatam",               # diṭṭhigataṃ «အယူမှား» (diṭṭhi = အယူ)
    "ñāṇaṃ": "@nanam",
}
T_TIKA = {
    # --- ^4-91 … ^4-93 (nirāso, āsaṃso, vigatāso)
    "asuci": "စင်ကြယ်မှု မရှိသော", "saṅkassara": "သံသယဖြင့် အောက်မေ့ရသော", "samācāro": "အကျင့် ရှိသော",
    "paṭicchanna": "ဖုံးကွယ်ထားသော", "kammanto": "အမှု ရှိသော", "paṭiñño": "ဝန်ခံသော",
    "brahmacārī": "မြင့်မြတ်သော အကျင့်ကို ကျင့်သော", "cārī": "ကျင့်သော", "pūti": "ပုပ်သိုးသော",
    "avassuto": "ကိလေသာ စိုစွတ်သော", "kasambu": "အမှိုက်သရိုက်",
    "suṇāti": "@sunati3", "kira": "သတတ်", "nāmo": "မည်သော", "itthaṃ": "ဤ", "khayā": "ကုန်ခန်းခြင်း",
    "viharissāmi": "နေရပါသည်", "paṭippassaddhā": "ငြိမ်းသွားသော", "vimuttassa": "လွတ်မြောက်သော",
    # --- ^4-94 (the sick)
    "savaṇāya": "နာကြားရန်", "anuññātaṃ": "ခွင့်ပြုတော်မူသော", "paveditaṃ": "ဟောကြားထားသော",
    "paveditaṃ vinayaṃ": "ဟောကြားထားသော … ဝိနည်း", "vinayaṃ": "ဝိနည်း", "dhammavinayaṃ": "တရားနှင့် ဝိနည်း",
    "dhamma savaṇāya": "တရား … နာကြားရန်", "okkamati": "သက်ဆင်းသည်", "puggalo okkamati": "ပုဂ္ဂိုလ် … သက်ဆင်းသည်",
    "bhojanāni": "အစားအစာ", "sappāyāni": "သင့်လျော်သော", "sappāyāni bhojanāni": "သင့်လျော်သော အစားအစာ",
    "sappāyāni bhesajjāni": "သင့်လျော်သော ဆေးဝါး", "bhesajjāni": "ဆေးဝါး", "ābādhā": "အနာရောဂါ",
    "upaṭṭhākaṃ": "လုပ်ကျွေးပြုစုသူ", "patirūpaṃ": "လျောက်ပတ်သော", "patirūpaṃ upaṭṭhākaṃ": "လျောက်ပတ်သော လုပ်ကျွေးပြုစုသူ",
    "upaṭṭhātabbā": "လုပ်ကျွေးပြုစုရမည့်", "upaṭṭhāko": "လုပ်ကျွေးပြုစုသူ", "aññesaṃ": "အခြားသူ",
    "gilāno": "လူနာ", "vuṭṭhāti": "@vutthati", "gilāno vuṭṭhāti": "လူနာ … ပျောက်ကင်းသည်", "desetabbo": "ဟောကြားရမည့်",
    "gilāna": "@gilana",
    # --- ^4-98 … ^4-104
    "kula": "@kula", "sampajāna": "သိလျက်", "pūga": "အသင်းအပင်း", "jānaṃ": "သိလျက်", "passaṃ": "မြင်လျက်",
    "puṭṭho": "မေးမြန်းခံရသော", "sakkhi": "သက်သေ", "abhinīto": "ခေါ်ဆောင်ခံရသော", "vadehi": "ပြောသည်",
    "ehi": "လာသည်", "musāvādī": "မုသား ပြောသော", "musāvādaṃ": "မုသား ပြောခြင်း", "paṭivirato": "ရှောင်ကြဉ်သော",
    "hetu": "@hetu", "pemaniyā": "ချစ်ခင်ဖွယ်ကောင်းသော", "nelā": "အပြစ်ကင်းသော",
    "upama": "တူသော", "upamo": "တူသော",
    "upāyāsa": "ပြင်းစွာ ပူပန်ခြင်း", "bahulo": "များသော", "abhisajjati": "ငြိုငြင်သည်", "kuppati": "အမျက်ထွက်သည်",
    "byāpajjati": "@byapajjati", "patitthīyati": "ခိုင်ခိုင်မာမာ ဆန့်ကျင်သည်", "kopaṃ": "အမျက်ထွက်ခြင်း",
    "appaccayaṃ": "မနှစ်သက်မှု", "duṭṭha": "ပြည်တည်နေသော", "kaṭṭhena": "သစ်သားချောင်း", "kaṭhalāya": "အိုးခြမ်းကွဲ",
    "ghaṭṭito": "ထိခိုက်မိသော", "āsavaṃ deti": "ပြည်ယိုသည်", "bhiyyoso": "ပို၍ ပို၍",
    "assavanoti": NONE, "kathalena": NONE,          # the variants in Roman script inside the text's bracket
    "aṭṭhakathā": "အဋ္ဌကထာ",                       # the translated sigla «(အဋ္ဌကထာ)»
    "cakkhumā": "မျက်စိ ကောင်းသော", "ratta": "ညဉ့်အခါ", "andhakāra": "မှောင်မိုက်", "timisāya": "ထူထပ်စဉ်",
    "antarikāya": "ခဏ",
    "natthi kiñci": "တစ်စုံတစ်ရာမျှ မရှိသည်", "abhejjaṃ": "မဖောက်ထွင်းနိုင်သော", "maṇi": "ပတ္တမြား", "pāsāṇo": "ကျောက်",
    "tathārūpaṃ cakkhu": "ထိုသို့ သဘောရှိသော မျက်စိ", "jāneyya": "သိသည်", "adhigataṃ": "ရပြီးသော",
    "anavajje": "အပြစ် မရှိသော", "anavajje dhamme": "အပြစ် မရှိသော သဘောတရား", "sāvajja": "အပြစ် ရှိသော",
    "sukka": "ဖြူစင်သော", "sukka dhamme": "ဖြူစင်သော … သဘောတရား", "kaṇha": "မည်းနက်သော",
    "paṭibhāge": "ဆန့်ကျင်ဘက် ရှိသော", "akusale": "အကုသိုလ်", "akusale dhamme": "အကုသိုလ် သဘောတရား",
    # --- ^4-107 … ^4-110 (the inverted pot, the lap)
    "ārāmaṃ": "ကျောင်း", "gantā": "သွားသော", "gato": NONE,        # gato: the variant [gato (sī.)] in Roman script
    "abhikkhaṇaṃ": "ခဏခဏ", "dhammassavaṇāya": "တရား နာကြားရန်", "ārāmaṃ savaṇāya": "နာကြားရန် … ကျောင်း",
    "majjhekalyāṇaṃ": "အလယ်၌ ကောင်းသော", "atthaṃ": "@attham", "byañjanaṃ": "@byanjanam", "kevala": "အလုံးစုံ",
    "paripuṇṇaṃ": "ပြည့်စုံသော", "paripuṇṇaṃ parisuddhaṃ": "ပြည့်စုံသော … စင်ကြယ်သော", "parisuddhaṃ": "စင်ကြယ်သော",
    "cariyaṃ": "အကျင့်", "brahmacariyaṃ pakāsenti": "မြင့်မြတ်သော အကျင့်ကို ထုတ်ဖော် ပြသည်",
    "pakāsenti": "ထုတ်ဖော် ပြသည်", "āsane": "နေရာ", "nisinno": "ထိုင်နေသော", "kathāya": "တရားစကား",
    "manasi": "@manasi", "neva manasi karoti": "နှလုံး မသွင်းသည်",
    "kumbho": "အိုး", "nikkujjo": "မှောက်ထားသော", "nikujjo": NONE, "tatra": "@tatra",
    "udakaṃ": "ရေ", "āsittaṃ": "လောင်းထည့်သော", "vivaṭṭati": "စီးကျသွားသည်", "saṇṭhāti": "တည်နေသည်",
    "khajjakāni": "စားဖွယ်", "ākiṇṇāni": "ပြန့်ကျဲ ထည့်ထားသော", "tilā": "နှမ်း", "taṇḍulā": "ဆန်",
    "modakā": "မုန့်လုံး", "badarā": "ဆီးသီး", "vuṭṭhahanto": "ထသော", "satisammosā": "သတိလစ်၍",
    "pakireyya": "ဖိတ်ကျစေသည်", "ukkujjo": "လှန်ထားသော",
    "sotāpanna": "သောတာပန်", "sakadāgāmino": "သကဒါဂါမ်", "vītarāgo": "ရာဂ ကင်းသော",
    # --- ^4-113 … ^4-115 (the writing on rock, earth, water)
    "abhiṇhaṃ": "ခဏခဏ", "kujjhati": "အမျက်ဒေါသ ထွက်သည်", "assa": "ထိုသူ",
    "ciraṃ dīgharattaṃ": "ကြာမြင့်စွာ ရှည်လျားသော ကာလပတ်လုံး", "dīgharattaṃ": "@digharattam",
    "lujjati": "ပျက်သည်", "vātena": "လေ", "udakena": "ရေ", "ṭhitikā": "တည်သော",
    "vuccamāno": "ပြောဆိုခံရသော", "pharusena": "ကြမ်းတမ်းစွာ", "amanāpena": "မနှစ်မြို့ဖွယ်",
    "saṃsandati": "ညီညွတ်စွာ ပေါင်းစည်းသည်", "sandhiyati": "ပြန်လည် ဆက်စပ်သည်",
    "sammodati": "ဝမ်းမြောက်စွာ ဆက်ဆံသည်", "ceva": NONE,       # the variant «… ceva (syā.)» in Roman script
    # --- ^4-116 / ^4-117 (the bark cloth, the Kāsi cloth)
    "diṭṭha": "အမြင်", "anugatiṃ": "အတုယူ လိုက်နာ", "paṭiggaṇhāti": "လက်ခံသည်", "sevanti": "ပေါင်းသင်းသည်",
    "bhajanti": "ဆည်းကပ်သည်", "ānisaṃsaṃ": "အာနိသင်", "thero": "ထေရ်", "phalaṃ": "@phalam",
    "bhikkhūsu": "ရဟန်း", "Navo": "ဝါငယ်", "saṅgha": "သံဃာ", "parikkhāraṃ": "အသုံးအဆောင်",
    "chaḍḍenti": "စွန့်ပစ်သည်", "potthakā": "လျှော်ပိတ်စ", "anattamano": "စိတ်မနှစ်သိမ့်သော",
    "ahitāya": "အစီးအပွား မရှိခြင်း", "saṅkāra": "အမှိုက်", "kūṭe": "ပုံ", "jiṇṇo": "ဟောင်းနွမ်းသော",
    "ukkhali": "အိုး", "parimajjanaṃ": "သုတ်ဝတ်", "dukkhasamphassatāya": "ထိတွေ့ရ နာကျင်ခြင်း",
    "ukkhipati": "နှင်ထုတ်သည်", "dubbaṇṇatāya": "အဆင်း ညှိုးခြင်း", "dubbaṇṇo": "@dubbanno",
    "nicchāreti": "ထုတ်ဖော် ပြောဆိုသည်",
    "sameti": "ညီသည်", "vaṇṇavantaṃ": "အဆင်း လှသော", "suvaṇṇatāya": "အဆင်း လှခြင်း", "karaṇḍake": "ဘူး",
    "gandha": "@gandha", "vattha": "ပိတ်စ", "ādheyyaṃ": "လက်ခံ မှတ်သားထိုက်သော", "ratana": "ရတနာ",
    "nikkhipanti": "ထည့်ထားသည်", "kho": NONE, "pana": NONE,     # «yesaṃ kho pana» only in the Roman-script variant
    "jiṇṇaṃ": "ဟောင်းနွမ်းသော", "sukhasamphassatāya": "ထိတွေ့ရ သာယာခြင်း", "appasaddā": "အသံ ငြိမ်သော",
    "ṭīkāya": "ဋီကာ", "hitāya": "အစီးအပွား", "vacanaṃ": "စကား", "paliveṭhanaṃ": "ထုပ်ရာ အဝတ်",
    # --- ^4-118 … ^4-123
    "capalo": "ပေါ့ပျက်သော", "vikiṇṇa": "ရှုပ်ပွေစွာ", "unnaḷo": "@unnalo", "uddhato": "ယောက်ယက်ခတ်သော",
    "indriyo": "အာရုံခံ အင်္ဂါ", "vāco": "@vaco_", "mukharo": "@mukharo", "pākaṭa": "ပွင့်ဟနေသော",
    "vibbhanta": "ပျံ့လွင့်သော", "samāhito": "တည်ကြည်သော", "saṃvuta": "စောင့်စည်းသော",
    "ekagga": "တစ်ခုတည်း၌ စူးစိုက်သော",
    "samādhinā": "သမာဓိ", "samādhinā paññāya": "သမာဓိ … ပညာ", "anuddayā": "သနားကြင်နာခြင်း",
    "phāsu": "@phasu", "saṃvijjamānā": "ထင်ရှား ရှိသော", "pavattinī": "ဆက်လက် ဖြစ်ပွားနေသော", "kathā": "စကား",
    "paripūressāmi": "ပြည့်စုံအောင် ပြုသည်", "Aparipūraṃ": "မပြည့်စုံသေးသော", "adhiko": "သာလွန်သော",
    # --- ^4-124 … ^4-131
    "sahāyo": "အပေါင်းအဖော် … ရှိသော", "sampavaṅko": "ညွတ်ကိုင်းသော", "kittisaddo": "သတင်းစကား",
    "abbhuggacchati": "ပျံ့နှံ့သည်", "ḍaṃsati": "ကိုက်သည်", "makkheti": "ပေကျံစေသည်", "ahi": "မြွေ",
    "paribhāseyya": "ကဲ့ရဲ့ ပြောဆိုသည်", "Akkoseyya": "ဆဲရေးသည်", "alātaṃ": "မီးစ", "tinduka": "တည်သား",
    "gūthakūpo": "မစင်တွင်း", "ciṭiciṭāyati": "တဖွားဖွား မီးပွင့်သည်", "cicciṭāyati": "တဖျစ်ဖျစ် မြည်သည်",
    "duggandho": "အနံ့ ဆိုးသော", "aruko": "အနာ",
    "paripūrakārino": "ပြည့်စုံစွာ ကျင့်သော", "kārino": "ကျင့်သော",
    "vedanānaṃ": "ခံစားမှု", "rūpānaṃ": "ရုပ်", "pariññaṃ": "ပိုင်းခြား သိခြင်း", "kāmānaṃ": "ကာမ",
    "satthā": "ဆရာ", "satthā paññapeti": "ဆရာ … ပညတ်သည်", "pariññaṃ paññapeti": "ပိုင်းခြား သိခြင်းကို ပညတ်သည်",
    "paññapeti": "ပညတ်သည်", "vedanānaṃ pariññaṃ": "ခံစားမှုတို့ကို ပိုင်းခြား သိခြင်း",
    "rūpānaṃ pariññaṃ": "ရုပ်တို့ကို ပိုင်းခြား သိခြင်း", "kāmānaṃ pariññaṃ": "ကာမတို့ကို ပိုင်းခြား သိခြင်း",
    "ucchedavādo": "ပြတ်စဲသွားသည်ဟု ဆိုသော ဝါဒ ရှိသော", "sassatavādo": "ထာဝရ တည်မြဲသည်ဟု ဆိုသော ဝါဒ ရှိသော",
    "attānaṃ": "အတ္တ", "dhamme": "@dhamme",
    # rule 3 (the person noun «…သူ» -> «…သော» for an adjective), as pi-1 sīlavanto / pi-2 dussīla
    "dussīlo": "သီလ ပျက်သော", "sīlavā": "သီလ ရှိသော",
    "brahmacariyaṃ": "မြင့်မြတ်သော အကျင့်",   # pi-1 brahmacariya (pi-2 «မြတ်သော» is only a substring of «မြင့်မြတ်သော»)
    "payirupāsanti": "ချဉ်းကပ် ခစားသည်", "desenti": "ဟောကြားသည်",
    "purisa": "@purisa", "purisapuggalo": "လူ ပုဂ္ဂိုလ်", "dukkhāya": "@dukkhaya", "sukhāya": "@sukhaya",
}
T_CATUKKA = {
    # --- ^4-132 … ^4-143: the five precepts / ten courses (attributive «…သော», rule 3; the verbal nouns «…ခြင်း»)
    "pāṇa": "@pana_", "atipātī": "သတ်သော", "pāṇātipātī": "သူ့အသက်ကို သတ်သော",
    "puggalo pāṇātipātī": "ပုဂ္ဂိုလ် … သူ့အသက်ကို သတ်သော", "ādāyī": "ယူသော", "micchācārī": "မှားယွင်းစွာ ကျင့်သော",
    "kāmesumicchācārī": "ကာမတို့၌ မှားယွင်းစွာ ကျင့်သော", "ṭhāyī": "မှီဝဲသော", "vādī": "ပြောသော",
    "asappurisena": "သူတော်ကောင်း မဟုတ်သူ", "samādapeti": "ဆောက်တည်စေသည်", "cāre": "ကျင့်ခြင်း", "ṭhāne": "အကြောင်း",
    "atipāte": "သတ်ခြင်း", "pāṇātipāte": "သူ့အသက်ကို သတ်ခြင်း", "paraṃ": "သူတစ်ပါး", "vāde": "ပြောခြင်း",
    "atipātā": "သတ်ခြင်း", "kāmesumicchācārā": "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း",
    "kāmesumicchācārā paṭivirato": "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းမှ ရှောင်ကြဉ်သော",
    "adinnādānā paṭivirato": "မပေးသည်ကို ယူခြင်းမှ ရှောင်ကြဉ်သော",
    "sappurisena": "သူတော်ကောင်း", "veramaṇiyā": "ကင်းဝေးခြင်း",
    "pāṇātipātā veramaṇiyā": "သူ့အသက်ကို သတ်ခြင်းမှ ကင်းဝေးခြင်း",
    "adinnādānā veramaṇiyā": "မပေးသည်ကို ယူခြင်းမှ ကင်းဝေးခြင်း", "musāvādā veramaṇiyā": "မုသား ပြောခြင်းမှ ကင်းဝေးခြင်း",
    "palāpī": "ပြိန်ဖျင်းသော စကားကို ပြောသော", "palāpā": "ပြိန်ဖျင်းသော စကား", "sampha": "အကျိုးမဲ့",
    "pisuṇa": "ကုန်းတိုက်သော", "pharusa": "ကြမ်းတမ်းသော", "abhijjhālu": "သူ့ဥစ္စာကို လိုချင်သော",
    "byāpanna": "ဖျက်ဆီးလိုစိတ် ရှိသော", "abyāpanna": "ဖျက်ဆီးလိုစိတ် မရှိသော",
    "anabhijjhāya": "သူ့ဥစ္စာကို မလိုချင်ခြင်း", "vācāya": "@vacaya",
    "pāpataro": "ပို၍ ယုတ်မာသူ", "pāpadhammena": "ယုတ်မာသော သဘော ရှိသူ",
    "pāpadhammataro": "ပို၍ ယုတ်မာသော သဘော ရှိသူ", "samā": "မှန်ကန်သော",
    # --- ^4-145 … ^4-155
    "anavajjena": "အပြစ် မရှိသော", "sāvajjena": "အပြစ် ရှိသော", "bahulaṃ": "များစွာ", "vajjo": "အပြစ်",
    "velāya": "ခဏ", "puggalassa abhisamayo": "ပုဂ္ဂိုလ် … ထိုးဖောက် သိမြင်ခြင်း", "udāhaṭa": "ပြောကြားလိုက်သော",
    "vitthārena": "အကျယ်အားဖြင့်", "vibhajiyamāne": "ခွဲခြား ပြသသော", "atthe": "အနက်",
    "paripucchato": "မေးမြန်းခြင်း", "sevato": "ပေါင်းသင်းခြင်း", "payirupāsato": "ချဉ်းကပ် ခစားခြင်း",
    "mitte": "မိတ်ဆွေ", "kalyāṇamitte": "မိတ်ဆွေကောင်း", "anupubbena": "အစဉ်အတိုင်း", "bhajato": "ဆည်းကပ်ခြင်း",
    "uddesato": "သင်ယူခြင်း", "karoto": "နှလုံးသွင်းခြင်း",
    "suṇato": "ကြားနာသော", "jātiyā": "ဘဝ", "dhārayato": "ဆောင်ထားသော", "vācayato": "ပို့ချသော",
    "vadati": "ဖြေဆိုသည်", "yuttaṃ": "သင့်လျော်စွာ", "pañhaṃ": "ပြဿနာ", "sīghaṃ": "လျင်မြန်စွာ",
    # --- ^4-156 … ^4-163 (preachers, clouds, mice, mangoes, pots, lakes, bulls, snakes)
    "parisā": "ပရိသတ်", "parisaṃ": "ပရိသတ်", "sahita": "အနက် ဆက်စပ်သော", "sahitaṃ": "အနက် ဆက်စပ်သော",
    "asahitassa": "အနက် မဆက်စပ်သော", "asahitaṃ": "အနက် မဆက်စပ်သော", "saṅkhaṃ gacchati": "အမည် ရသည်",
    "kusalā": "ကျွမ်းကျင်သော", "kathiko": "ဟောပြောသူ", "dhammakathiko bhāsati": "တရား ဟောပြောသူ … ဟောပြောသည်",
    "valāhako": "မိုးတိမ်", "kattā": "@katta", "gajjitā": "မိုး ချုန်းသူ", "vassitā": "မိုး ရွာသူ",
    "puggalo gajjitā": "ပုဂ္ဂိုလ် … မိုး ချုန်းသူ", "puggalo vassitā": "ပုဂ္ဂိုလ် … မိုး ရွာသူ",
    "gādhaṃ": "တွင်း", "gādhaṃ kattā": "တွင်း တူးသူ", "pariyāpuṇāti": "သင်ယူသည်",
    "dhammaṃ pariyāpuṇāti": "တရားကို သင်ယူသည်", "vasitā": "နေသူ", "mūsikā": "ကြွက်",
    "puggalo kattā": "ပုဂ္ဂိုလ် … တူးသူ", "puggalo pariyāpuṇāti": "ပုဂ္ဂိုလ် … သင်ယူသည်", "puggalo vasitā": "ပုဂ္ဂိုလ် … နေသူ",
    "ālokitaṃ": "ရှေ့သို့ ကြည့်ခြင်း", "samiñjitaṃ": "ကွေးခြင်း", "pasāritaṃ": "ဆန့်ခြင်း",
    "samiñjitaṃ pasāritaṃ": "ကွေးခြင်း … ဆန့်ခြင်း", "dhāraṇaṃ": "ဆောင်ခြင်း", "patta dhāraṇaṃ": "သပိတ် … ဆောင်ခြင်း",
    "saṅghāṭi dhāraṇaṃ": "ဒုကုဋ် … ဆောင်ခြင်း", "cīvaradhāraṇaṃ": "သင်္ကန်းကို ဆောင်ခြင်း",
    "paṭikkantaṃ": "နောက်သို့ ဆုတ်ခြင်း", "abhikkantaṃ": "ရှေ့သို့ တိုးခြင်း", "pāsādikaṃ": "ကြည်ညိုဖွယ်",
    "vaṇṇī": "အဆင်း ရှိသော", "vaṇṇi": "အဆင်း ရှိသော", "ambaṃ": "သရက်သီး", "pakka": "မှည့်သော", "āmaṃ": "စိမ်းသော",
    "puggalo pakko": "ပုဂ္ဂိုလ် … မှည့်သော", "puggalo āmo": "ပုဂ္ဂိုလ် … စိမ်းသော",
    "pihito": "အဖုံး ပိတ်ထားသော", "vivaṭo": "အဖုံး ဖွင့်ထားသော", "tuccho": "ဗလာ ဖြစ်သော",
    "puggalo tuccho": "ပုဂ္ဂိုလ် … ဗလာ ဖြစ်သော", "puggalo pūro": "ပုဂ္ဂိုလ် … ပြည့်သော",
    "gambhīra": "နက်", "udakarahado": "ရေကန်", "obhāso": "@obhaso", "uttāno": "တိမ်သော",
    "puggalo gambhīro": "ပုဂ္ဂိုလ် … နက်သော", "puggalo uttāno": "ပုဂ္ဂိုလ် … တိမ်သော",
    "balībaddo": "နွားလား", "caṇḍo": "ကြမ်းကြုတ်သော", "gava": "@gava", "ubbejitā": "ထိတ်လန့်စေသူ",
    "puggalo caṇḍo": "ပုဂ္ဂိုလ် … ကြမ်းကြုတ်သော", "puggalo ubbejitā": "ပုဂ္ဂိုလ် … ထိတ်လန့်စေသူ",
    "āgata": "လျင်မြန်စွာ တက်သော", "ghora": "ပြင်းသော", "viso": "အဆိပ်", "āgataviso": "အဆိပ် လျင်မြန်စွာ တက်သော",
    "āsīviso": "မြွေဆိုး", "āsīvisā": "မြွေဆိုး", "neva": "@neva",
    # --- ^4-164 … ^4-173
    "duppaṭipadāya": "ဆိုးသော ကျင့်စဉ်", "duppaṭipannānaṃ": "ဆိုးစွာ ကျင့်သော", "avaṇṇa": "ကဲ့ရဲ့",
    "buddhānaṃ": "ဘုရားရှင်", "sāvakānaṃ": "တပည့်", "titthiyānaṃ": "တိတ္ထိ",
    "avaṇṇaṃ bhāsati": "ကဲ့ရဲ့ ပြောဆိုသည်", "vaṇṇaṃ bhāsati": "ချီးမွမ်း ပြောဆိုသည်",
    "pasādaṃ janeti": "ကြည်ညိုမှုကို ဖြစ်စေသည်",
    "puggalo avaṇṇaṃ bhāsati": "ပုဂ္ဂိုလ် … ကဲ့ရဲ့ ပြောဆိုသည်", "puggalo vaṇṇaṃ bhāsati": "ပုဂ္ဂိုလ် … ချီးမွမ်း ပြောဆိုသည်",
    "puggalo pasādaṃ janeti": "ပုဂ္ဂိုလ် … ကြည်ညိုမှုကို ဖြစ်စေသည်",
    "puggalo titthiyānaṃ vaṇṇaṃ bhāsati": "ပုဂ္ဂိုလ် … တိတ္ထိ … ချီးမွမ်း ပြောဆိုသည်",
    "paṭipadāya": "ကျင့်စဉ်", "paṭipannānaṃ": "ကျင့်သော", "micchāpaṭipannānaṃ": "မှားယွင်းစွာ ကျင့်သော",
    "sammāpaṭipannānaṃ": "မှန်ကန်စွာ ကျင့်သော",
    "veyyākaraṇāya": "ဖြေဆိုရန်", "pañhassa": "ပြဿနာ",
    "Nerayikā": "ငရဲသား", "abhinibbattati": "ဖြစ်ပေါ်သည်", "uṭṭhahato": "ထကြွ၍", "ghaṭato": "ကြိုးပမ်း၍",
    "vāyamato": "အားထုတ်၍", "upajīvino": "အသက်မွေးသော", "puggalassa ājīvo": "ပုဂ္ဂိုလ် … အသက်မွေးမှု",
    "paranimmitavasavattideve": NONE,      # the variant in Roman script inside the text's bracket
    "vattī": "ဝတ္တီ", "vasa": "ဝသ",      # as pi-2 para «ပရ» / nimmita «နိမ္မိတ» (the name's syllables)
    "vena": "ဝါးရက်သမား", "rathakāra": "ရထားလုပ်သမား", "nesāda": "မုဆိုး", "caṇḍāla": "စဏ္ဍာလ",
    "pukkusa": "အမှိုက်သိမ်းသမား", "kule": "အမျိုး", "paccājāto": "ပြန်လည် မွေးဖွားသော",
    "puggalo paccājāto": "ပုဂ္ဂိုလ် … ပြန်လည် မွေးဖွားသော", "dalidde": "ဆင်းရဲသော", "vuttike": "အသက်မွေးရ",
    "kasirena": "ခက်ခဲစွာ", "acchādo": "အဝတ်", "seyyā": "အိပ်ရာ", "āvasatha": "နေအိမ်", "padīpeyyassa": "ဆီမီး",
    "anna": "အစာ", "pāna": "အဖျော်", "mālā": "ပန်း", "vilepanassa": "နံ့သာပျောင်း", "yānassa": "ယာဉ်",
    "kāṇo": "မျက်စိ ကွယ်သော", "kuṇī": "လက် ကောက်သော", "khañjo": "ခြေ ဆွံ့သော", "pakkhahato": "လေဖြတ်သော",
    "pakkha": NONE,                       # pakkhahata = the one word «လေဖြတ်»
    "bahu": "များသော", "ābādho": "ရောဂါ", "okoṭimako": "ပုကွသော", "duddasiko": "ကြည့်ရ ဆိုးသော",
    "aḍḍhe": "ချမ်းသာသော", "dhane": "ဥစ္စာ", "bhoge": "စည်းစိမ်", "rajate": "ငွေ", "pahūta": "ပေါများသော",
    "upakaraṇe": "အသုံးအဆောင်", "mahāsāla": "ကြွယ်ဝသော", "dassanīyo": "ရှုချင်ဖွယ် ဖြစ်သော",
    "pāsādiko": "ကြည်ညိုဖွယ် ဖြစ်သော", "abhirūpo": "ရုပ်ချောသော", "paramāya": "အလွန်",
    "vaṇṇapokkharatāya": "လှပသော အဆင်း",
    "kalyāṇadhammā": "ကောင်းမွန်သော သဘော ရှိသော", "sīlavatī": "သီလ ရှိသော",
    "sāraparivāro": "အနှစ် အခြံအရံ ရှိသော", "phegguparivāro": "အကာ အခြံအရံ ရှိသော", "sāro": "အနှစ်", "pheggu": "အကာ",
    "parivāro": "အခြံအရံ ရှိသော", "sāro parivāro": "အနှစ် … အခြံအရံ ရှိသော", "pheggu parivāro": "အကာ … အခြံအရံ ရှိသော",
    "puggalo sāro": "ပုဂ္ဂိုလ် … အနှစ်", "puggalo pheggu": "ပုဂ္ဂိုလ် … အကာ",
    "puggalo sāro parivāro": "ပုဂ္ဂိုလ် … အနှစ် … အခြံအရံ ရှိသော",
    "puggalo pheggu parivāro": "ပုဂ္ဂိုလ် … အကာ … အခြံအရံ ရှိသော", "rukkho": "သစ်ပင်",
    "vaṇṇanāya": "ချီးမွမ်းစကား", "thomanāya": "ချီးကျူးစကား", "pasaṃsanāya": "ထောမနာစကား",
    "vaṇṇahārikāya": "ဂုဏ်သတင်း ဆောင်ယူချက်", "pariṇāhaṃ": "လုံးပတ်", "ārohaṃ": "အရပ် အမြင့်",
    "saṇṭhānaṃ": "ပုံသဏ္ဌာန်", "passitvā": "မြင်၍", "gahetvā": "ထား၍",
    "dukkara": "ပြုရခက်သော", "senāsana": "@senasana", "kārikaṃ": "အကျင့်", "vividhaṃ": "အမျိုးမျိုးသော",
    "paññaṃ": "ပညာ",
    "samādhisampanno": "သမာဓိ ပြည့်စုံသော", "vimuttisampanno": "လွတ်မြောက်မှု ပြည့်စုံသော",
    "paññāsampanno": "ပညာ ပြည့်စုံသော", "sampadāya": "ပြည့်စုံခြင်း", "sīlasampadāya": "သီလ ပြည့်စုံခြင်း",
    "samādhisampadāya": "သမာဓိ ပြည့်စုံခြင်း", "paññāsampadāya": "ပညာ ပြည့်စုံခြင်း",
    "vimuttisampadāya": "လွတ်မြောက်မှု ပြည့်စုံခြင်း", "ñāṇadassana": "သိမြင်သော ဉာဏ်", "dassana": "သိမြင်သော",
    "vimuttiñāṇadassana": "လွတ်မြောက်မှုကို သိမြင်သော ဉာဏ်",
    # --- ^4-174 (tormenting oneself): the generator's lists (make_ch5.py _FOODS / _CLOTH), word by word
    "acelako": "အဝတ် မဝတ်သော", "ācāro": "ကျင့်ဝတ်", "hattha": "လက်", "apalekhano": "လျက်သော",
    "tiṭṭha": "ရပ်သည်", "abhihaṭaṃ": "ယူဆောင်လာသော", "uddissa": "ရည်ရွယ်၍", "nimantanaṃ": "ပင့်ဖိတ်ခြင်း",
    "sādiyati": "သာယာသည်", "kumbhi": "အိုး", "mukhā": "@mukha", "kaḷopi": "ဒယ်အိုး", "eḷaka": "တံခါးခုံ",
    "antaraṃ": "ကြားခံ၍", "daṇḍa": "@danda", "musala": "ကျည်ပွေ့", "bhuñjamānānaṃ": "စားနေသော",
    "gabbhiniyā": "ကိုယ်ဝန် ရှိသော", "pāyamānāya": "နို့တိုက်နေသော",
    "saṅkittīsu": "ငတ်မွတ်ချိန်၌ စုဆောင်းထားသော ဆွမ်း", "sā": "ခွေး", "upaṭṭhito": "ရပ်စောင့်နေသော",
    "makkhikā": "ယင်ကောင်", "saṇḍasaṇḍacārinī": "အုပ်လိုက် ပျံဝဲနေသော", "macchaṃ": "ငါး", "suraṃ": "သေရည်",
    "merayaṃ": "အရက်", "thusodakaṃ": "ဖွဲရေ", "pivati": "သောက်သည်",
    "āgāriko": "အိမ်", "ālopiko": "လုတ်", "dattiyā": "ခွက်", "dattīhi": "ခွက်", "yāpeti": "မျှတသည်",
    "ekāhikaṃ": "တစ်ရက်ခြား", "pariyāya": "အလှည့်ကျ",
    "sāka": "ဟင်းရွက်", "sāmāka": "ဆပ်", "nīvāra": "တောစပါး", "daddula": "သားရေ အပိုင်းအစ", "haṭa": "ရေညှိ",
    "kaṇa": "ဖွဲနု", "ācāma": "ထမင်းရည်ချ", "piññāka": "နှမ်းဖတ်", "tiṇa": "မြက်", "go": "နွား", "maya": "ချေး",
    "vana": "တော", "pavatta": "ကြွေကျသော",
    "sāṇāni": "လျှော် အဝတ်", "masāṇāni": "လျှော် ရောသော အဝတ်", "chava": "အလောင်း", "dussāni": "အဝတ်",
    "paṃsukūlāni": "ပံ့သကူ အဝတ်", "paṃsu": "ပံ့သကူ", "kūlāni": "အဝတ်", "tirīṭāni": "သစ်ခေါက် အဝတ်",
    "ajinaṃ": "@ajinam", "khipaṃ": "အစ", "kusa": "ကုသမြက်", "vāka": "သစ်ခေါက် အမျှင်", "phalaka": "ပျဉ်ပြား",
    "kesa": "ဆံပင်", "kambalaṃ": "ကမ္ဗလာ", "vāḷa": "တိရစ္ဆာန် အမွေး", "ulūka": "ဇီးကွက်", "pakkhaṃ": "အတောင်",
    "ulukapakkhampi": NONE,               # the variant in Roman script inside the text's bracket
    "dhāreti": "ဝတ်သည်", "massu": "မုတ်ဆိတ်", "locako": "နုတ်သော", "locana": "နုတ်ခြင်း",
    "ubbhaṭṭhako": "မတ်တတ် ရပ်သော", "āsana": "ထိုင်ခုံ", "paṭikkhitto": "ပယ်သော",
    "ukkuṭiko": "ခြောင်းကြောင့်ချ ထိုင်သော", "ukkuṭika": "ခြောင်းကြောင့်ချ ထိုင်၍", "padhāna": "ကြိုးစားခြင်း",
    "kaṇṭaka": "ဆူး", "apassayiko": "လျောင်းသော", "sāya": "ညနေ", "tatiyakaṃ": "သုံးကြိမ်",
    "orohana": "ဆင်းခြင်း", "vihitaṃ": "အမျိုးမျိုးသော",
    # --- ^4-175 / ^4-176 (tormenting others; the king's sacrifice): agent nouns «…သူ» (the text's nouns)
    "orabbhiko": "သိုး သတ်သူ", "sūkariko": "ဝက် သတ်သူ", "sākuṇiko": "ငှက် ဖမ်းသူ", "māgaviko": "သားကောင် ဖမ်းသူ",
    "luddo": "မုဆိုး", "macchaghātako": "ငါး သတ်သူ", "ghātako": "သတ်သူ", "coro": "သူခိုး", "cora": "သူခိုး",
    "bandhanāgāriko": "ထောင်စောင့်", "kurūra": "ကြမ်းကြုတ်သော", "kammantā": "အလုပ် ရှိသော",
    "muddhāvasitto": "ဘိသိက်ခံ", "puratthimena": "အရှေ့ဘက်", "narassa": "လူ", "sandha": NONE,
    "āgāraṃ": "အဆောင်", "kārāpetvā": "ဆောက်စေ၍", "massuṃ": "မုတ်ဆိတ်", "ohāretvā": "ရိတ်၍", "khara": "ကြမ်းသော",
    "sappi": "@sappi", "miga": "သမင်", "visāṇena": "ချို", "pavisati": "ဝင်သည်", "mahesiyā": "မိဖုရား",
    "brāhmaṇena purohitena": "ပုဏ္ဏား ပုရောဟိတ်", "purohitena": "ပုရောဟိတ်",
    "anantarahitāya": "အခင်း မခင်းထားသော", "harita": "စိမ်းစိုသော", "bhūmiyā": "မြေ", "seyyaṃ kappeti": "အိပ်ရာ ပြုသည်",
    "gāviyā": "နွားမ", "vacchāya": "နွားသငယ် ရှိသော", "purohito yāpeti": "ပုရောဟိတ် … မျှတသည်", "aggiṃ": "မီး",
    "avasesena": "ကြွင်းကျန်သော", "usabhā": "နွားထီး", "vacchatarā": "နွားထီးပေါက်", "vacchatariyo": "နွားမပေါက်",
    "ajā": "ဆိတ်", "urabbhā": "သိုး", "assā": "မြင်း", "yañña": "ယဇ်", "yūpa": "ယဇ်တိုင်", "dabbhā": "မြက်",
    "tajjitā": "ခြိမ်းခြောက်ခံရသော",
    "pāṇātipātā paṭivirato": "သူ့အသက်ကို သတ်ခြင်းမှ ရှောင်ကြဉ်သော",
    "musāvādā paṭivirato": "မုသား ပြောခြင်းမှ ရှောင်ကြဉ်သော",
    "Yo": NONE,          # pi-1 agreed rule: the relative pronoun, the clause built with «… ရှိသမျှ» (^4-166)
    # Paranimmitavasavattī «ပရနိမ္မိတဝသဝတ္တီ»: para / nimmita keep the pi-2 values (the name's syllables), vasa and
    # vattī are given the name's remaining syllables in the same way

    "sutte": "@sutte", "carati": "@carati", "samannāgato": "@samannagato",
    "evaṃ hoti": "ဤသို့ … ဖြစ်သည်",
    # --- ^4-176 (rest; the editors' note is translated, pi-3 M9)
    "kandaraka": "ကန္ဒရက", "kandarakasutte": "ကန္ဒရကသုတ်", "majjhima": "မဇ္ဈိမ", "majjhimanikāye": "မဇ္ဈိမနိကာယ်",
    "potthake": "ပေစာမူ", "sīhaḷa": "သီဟိုဠ်", "attantapa": "အတ္တန္တပ",
    "kaṇḍuvamāno": "ကုတ်သော", "pessā": "စေခိုင်းရသူ", "haññantu": "သတ်သည်", "dāsā": "ကျွန်",
    "abbhañjitvā": "လိမ်း၍", "barihisa": "ယဇ်ခင်း", "upalittāya": "လိမ်းကျံထားသော", "parikammāni": "အလုပ်",
    "thane": "နို့သီး", "saddhiṃ": "အတူ", "rukkhā": "သစ်ပင်", "mahāsālo": "ကြွယ်ဝသော", "rudamānā": "ငိုကြွေးသော",
    "rudamāno": "ငိုကြွေးသော", "kammakarā": "အလုပ်သမား", "puggalo parantapo": "ပုဂ္ဂိုလ် … သူတစ်ပါးကို ပူပန်စေသော",
    # --- ^4-177 (the Tathāgata; going forth)
    "uppajjati": "ပွင့်ထွန်းတော်မူသည်", "bhagavā": "ဘုန်းတော်ရှင်", "brāhmaṇiṃ": "ပုဏ္ဏား",
    "parivaṭṭaṃ": "အပေါင်း", "caraṇa": "အကျင့်", "sambādho": "ကျဉ်းကျပ်သော", "raja": "@raja",
    "sukaraṃ": "လွယ်ကူသော", "saddhaṃ": "ယုံကြည်မှု", "pabbajjā": "ရဟန်း ပြုခြင်း",
    "bhogakkhandhaṃ": "စည်းစိမ် အစု", "pajaṃ": "သတ္တဝါ အပေါင်း", "sārathi": "ဆုံးမရာ", "damma": "ဆုံးမထိုက်သော",
    "anuttaro": "အတုမရှိသော", "agāraṃ": "အိမ်ရာ", "ajjhāvasatā": "နေသူ", "ghara": "အိမ်ရာ",
    "anagāriyaṃ": "အိမ်ရာ မရှိသော ရဟန်းအဖြစ်", "gahapati": "@gahapati", "putto": "သား", "vidū": "သိတော်မူသော",
    "pavedeti": "ဟောကြားတော်မူသည်", "deseti": "ဟောတော်မူသည်", "pakāseti": "ထင်ရှားပြတော်မူသည်",
    "kāsāyāni": "ဖန်ရည်စွန်းသော", "vatthāni": "သင်္ကန်း", "likhitaṃ": "ပွတ်ထားသော", "paṭisañcikkhati": "ဆင်ခြင်သည်",
    "āpatho": "တက်ရာ လမ်း", "ekanta": "@ekanta", "sugato": "ကောင်းသော လားရာသို့ ကြွတော်မူသော",
    # --- ^4-178 / ^4-179 (the virtues)
    "ārā": "ဝေးကွာစွာ", "nihita": "ချထားသော", "daṇḍo": "တုတ်", "sattho": "လက်နက်", "lajjī": "ရှက်တတ်သော",
    "dayāpanno": "သနားကြင်နာမှု ရှိသော", "anukampī": "စာနာသော", "bhūta": "@bhuta",
    "pāṭikaṅkhī": "မျှော်လင့်သော", "athenena": "ခိုးဝှက်ခြင်း မရှိသော", "sucibhūtena": "စင်ကြယ်သော",
    "abrahmacariyaṃ": "မြင့်မြတ်သော အကျင့် မဟုတ်သည်", "gāma": "ရွာသား", "methunā": "မေထုန်",
    "atipātaṃ": "သတ်ခြင်း", "pāṇātipātaṃ": "သူ့အသက်ကို သတ်ခြင်း", "ājīva": "အသက်မွေးမှု",
    "theto": "တည်ကြည်သော", "paccayiko": "ယုံကြည်ထိုက်သော", "visaṃvādako": "လှည့်ဖြားသော",
    "pisuṇaṃ": "ကုန်းတိုက်သော စကား", "pharusaṃ": "ကြမ်းတမ်းသော စကား", "palāpaṃ": "ပြိန်ဖျင်းသော စကား",
    "bhedāya": "ကွဲစေရန်", "akkhātā": "ပြောကြားသော", "bhinnānaṃ": "ကွဲပြားနေသော", "sandhātā": "ပြန်လည် စည်းလုံးစေသော",
    "samagga": "ညီညွတ်ခြင်း", "rato": "ပျော်ပိုက်သော", "nandī": "နှစ်သက်သော", "karaṇiṃ": "ညီညွတ်စေသော",
    "vinaya": "ဝိနည်း", "nidhānavatiṃ": "မှတ်သားထိုက်သော", "sāpadesaṃ": "အကြောင်း ပြချက်နှင့် တကွ ဖြစ်သော",
    "pariyantavatiṃ": "အပိုင်းအခြား ရှိသော",
    "bīja": "မျိုးစေ့", "samārambhā": "ဖျက်ဆီးခြင်း", "bhattiko": "စားသော", "ratti": "ညစာ", "virato": "ကင်းဝေးသော",
    "vikāla": "အချိန်လွန်", "bhojanā": "စားခြင်း", "nacca": "ကခြင်း",
    "visūka": "ကုသိုလ်ကို ဆန့်ကျင်သော ပွဲသဘင်", "dassanā": "ကြည့်ခြင်း", "vilepana": "နံ့သာပျောင်း",
    "dhāraṇa": "ဆောင်ခြင်း", "maṇḍana": "အလှပြင်ခြင်း", "vibhūsana": "တန်ဆာဆင်ခြင်း", "mahā": "မြတ်သော",
    "sayanā": "အိပ်ရာ", "rajata": "ငွေ", "paṭiggahaṇā": "လက်ခံခြင်း", "paṭiggahaṇā paṭivirato": "လက်ခံခြင်းမှ ရှောင်ကြဉ်သော",
    "kumārikā": "မိန်းကလေး", "dāsi": "ကျွန်မ", "dāsa": "ကျွန်ယောက်ျား", "aja": "ဆိတ်", "eḷaka": "@elaka",
    "kukkuṭa": "ကြက်", "sūkara": "ဝက်", "hatthi": "ဆင်", "vaḷava": "မြင်းမ", "khetta": "လယ်",
    "dūteyya": "တမန် လုပ်ခြင်း", "pahiṇa": "စေခိုင်းရာ", "gamana": "သွားခြင်း", "tulā": "ချိန်ခွင်",
    "kūṭa": "လိမ်ခြင်း", "kaṃsa": "ကြေးခွက်", "ukkoṭana": "တံစိုး ယူခြင်း", "vañcana": "လှည့်ဖြားခြင်း",
    "nikati": "@nikati", "sāci": "ကောက်ကျစ်သော", "yogā": "နည်းလမ်း", "chedana": "ဖြတ်ခြင်း", "vadha": "သတ်ခြင်း",
    "bandhana": "နှောင်ဖွဲ့ခြင်း", "viparāmosa": "ခိုးဆိုးခြင်း", "ālopa": "လုယက်ခြင်း",
    "sahasākārā": "အနိုင်အထက် ပြုခြင်း",
    # --- ^4-180 … ^4-185 (contentment, restraint, the jhānas, the three knowledges)
    "santuṭṭho": "ရောင့်ရဲသော", "parihārikena": "စောင့်ရှောက်ရုံ", "cīvarena": "သင်္ကန်း", "piṇḍapātena": "ဆွမ်း",
    "yena yeneva": "အရပ်တိုင်း", "samādāya": "ယူဆောင်၍", "sakuṇo": "ငှက်", "ḍeti": "ပျံသည်",
    "patta": "@patta", "bhāro": "ဝန်", "ariyena sīlakkhandhena": "အရိယာ သီလ အစုအဝေး",
    "iminā ariyena samannāgato": "ဤအရိယာ … အပြည့်အဝ ပြည့်စုံသော", "anavajja": "အပြစ် မရှိသော",
    "abyāseka": "ကိလေသာ မရောနှောသော", "santuṭṭhiyā": "ရောင့်ရဲမှု", "giri": "တောင်ဂူ",
    "bhāve": "ဆိတ်ဆိတ်နေရာ", "cīvaradhāraṇe": "သင်္ကန်းကို ဆောင်ရာ", "bhattaṃ": "ဆွမ်းစား",
    "paṭikkanto": "ပြန်လာသော", "saṃvarena": "စောင့်စည်းမှု", "indriya": "@indriya",
    "vigatathinamiddho viharati": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု ကင်းသော … နေသည်",
    "vūpasantacitto": "ကောင်းစွာ ငြိမ်သက်ပြီးသော စိတ် ရှိသော", "kathaṃkathī": "တွေးတောသော",
    "jaṃ": "ဖြစ်ပေါ်သော", "vihārī": "နေသော", "samāhite": "တည်ကြည်သော", "samāhite citte": "စိတ်သည် တည်ကြည်သော",
    "parisuddhe": "စင်ကြယ်သော", "pariyodāte": "ဖြူစင်သော", "anaṅgaṇe": "အမည်းအစက် မရှိသော",
    "mudubhūte": "နူးညံ့သော", "kammaniye": "အသုံးပြုရန် သင့်တော်သော", "ṭhite": "@thite",
    "āneñja": "မတုန်လှုပ်ခြင်း", "ñāṇāya": "ဉာဏ်", "abhininnāmeti": "ညွတ်စေသည်",
    "pubbenivāsa": "ရှေးဘဝ", "anussarati": "အဖန်ဖန် အောက်မေ့သည်", "vīsaṃ": "နှစ်ဆယ်", "tiṃsaṃ": "သုံးဆယ်",
    "cattālīsaṃ": "လေးဆယ်", "paññāsaṃ": "ငါးဆယ်", "uddesaṃ": "ညွှန်ပြချက်",
    "upapāta": "ဖြစ်ပေါ်ခြင်း", "upapajjamāne": "ဖြစ်ပေါ်ဆဲ", "caritena": "ဒုစရိုက်", "gate": "@gate",
    "upage": "ရောက်သွားသော", "jānato": "သိသော", "vimuccati": "လွတ်မြောက်သည်", "vusitaṃ": "ကျင့်ပြီးသော",
    "nāparaṃ": "နောက်ထပ်",
    # --- ^4-187 … ^4-190
    "phalassa": "ဖိုလ်", "maggassa": "မဂ်", "lokuttaramaggassa": "လောကကို ကျော်လွန်သော မဂ်",
    "pāpaṃ": "ယုတ်မာသော", "paṭisevati": "မှီဝဲသည်", "puggalo paṭisevati": "ပုဂ္ဂိုလ် … မှီဝဲသည်",
    "dukkhena": "နာကျင်မှု", "mukhena": "မျက်ရည် စီးသော",
    "aññāya": "သိ၍", "attha": "@attha", "puggalassa sutaṃ": "ပုဂ္ဂိုလ် … အကြားအမြင်", "sakid": "တစ်ကြိမ်",
}
T_PANCAKA = {
    # --- ^4-191 / ^4-192
    "jā": "ဖြစ်သော", "ārambhajā": "မှားယွင်းစွာ ပြုမူခြင်းမှ ဖြစ်သော", "vippaṭisārajā": "နောင်တ ရခြင်းမှ ဖြစ်သော",
    "ārambhajā āsavā": "မှားယွင်းစွာ ပြုမူခြင်းမှ ဖြစ်သော … စိတ်အစွန်းအထင်း", "ārambha": "မှားယွင်းစွာ ပြုမူခြင်း",
    "āyasmato": "အသျှင်", "saṃvijjanti": "ရှိသည်", "pavaḍḍhanti": "ပို၍ ပို၍ တိုးပွားသည်",
    "paṭivinodetvā": "ဖယ်ရှားပြီး", "bhāvetu": "ပွားများသည်", "pañcamena": "ပဉ္စမ", "samasamo": "တန်းတူ ဖြစ်သော",
    "ovadiyamānā": "ဆုံးမခံရသော", "anusāsiyamānā": "သွန်သင်ခံရသော", "pāpuṇanti": "ရောက်သည်",
    "deti": "ပေးသည်", "puggalo deti": "ပုဂ္ဂိုလ် … ပေးသည်", "puggalo deti cīvara": "ပုဂ္ဂိုလ် … သင်္ကန်း … ပေးသည်",
    "saṃvasati": "အတူ နေသည်", "puggalo saṃvasati": "ပုဂ္ဂိုလ် … အတူ နေသည်", "parassa": "သူတစ်ပါး",
    "vaṇṇe": "ချီးမွမ်း", "avaṇṇe": "ကဲ့ရဲ့", "adhimuccitā": "ယုံကြည်လိုက်သူ", "ittara": "ခဏတာသာ",
    "saddho": "ယုံကြည်မှု ရှိသော", "bhattī": "ကိုးကွယ်ခြင်း ရှိသော", "pemo": "ချစ်ခင်မှု ရှိသော",
    "hīna": "ယုတ်ညံ့သော",
    # --- ^4-193 … ^4-198 (the five warriors and the five monks)
    "yodhājīvo": "စစ်သည်", "rajaggaṃ": "ဖုန်လုံး", "raja": "@raja", "dhaja": "အလံ",
    "aggaṃ": "@aggam",              # dhajaggaṃ «အလံဖျား» (in rajaggaṃ «ဖုန်လုံး» the tip has no word of its own)
    "Puna": "တစ်ဖန်", "saṅgāmaṃ": "စစ်ပွဲ", "sahati": "သည်းခံနိုင်သည်", "saṃvijjamāno": "ထင်ရှား ရှိသော",
    "sahati rajaggaṃ": "ဖုန်လုံးကို သည်းခံနိုင်သည်", "sahati dhajaggaṃ": "အလံဖျားကို သည်းခံနိုင်သည်",
    "sahati ussāraṇaṃ": "ကြွေးကြော်သံကို သည်းခံနိုင်သည်",
    "sahati sampahāraṃ": "ထိပ်တိုက် တိုက်ခိုက်ခြင်းကို သည်းခံနိုင်သည်",
    "yodhājīvo sahati": "စစ်သည် … သည်းခံနိုင်သည်", "bhikkhu sahati": "ရဟန်း … သည်းခံနိုင်သည်",
    "ussāraṇaṃ": "ကြွေးကြော်သံ", "saṃsīdati": "စိတ်ဓာတ် ကျဆင်းသည်", "visīdati": "အားလျော့သည်",
    "santhambhati": "ခိုင်ခိုင်မာမာ ရပ်တည်နိုင်သည်", "satthambhati": NONE,   # the variant in Roman script
    "sampahāre": "ထိပ်တိုက် တိုက်ခိုက်ခြင်း", "sampahāraṃ": "ထိပ်တိုက် တိုက်ခိုက်ခြင်း",
    "haññati": "အသတ်ခံရသည်", "abhivijinitvā": "အောင်နိုင်၍", "vijitasaṅgāmo": "စစ်ပွဲကို အောင်ပြီးသော",
    "sīsaṃ": "ရှေ့တန်း", "ajjhāvasati": "အုပ်စိုး နေသည်",
    "sandhāretuṃ": "ဆက်လက် ထိန်းသိမ်းနိုင်", "dubbalyaṃ": "အားနည်းချက်", "āvikatvā": "@avikatva",
    "dubbalyaṃ āvikatvā": "@dubbalyam_avikatva", "hīnāya": "လူဘောင်", "āvattati": "ပြန်လည်သည်",
    "sikkhaṃ āvattati": "သိက္ခာကို … ပြန်လည်သည်", "paccakkhāya": "@paccakkhaya",
    "asukasmiṃ": "ဤမည်သော", "gāme": "ရွာ", "nigame": "နိဂုံး", "itthī": "မိန်းမ", "kumārī": "အပျို",
    "abhirūpā": "အဆင်းလှသော", "dassanīyā": "ရှုချင်ဖွယ် ကောင်းသော", "pāsādikā": "ကြည်ညိုဖွယ် ကောင်းသော",
    "suñña": "ဆိတ်ငြိမ်ရာ", "mātugāmo": "အမျိုးသမီး", "upasaṅkamitvā": "ချဉ်းကပ်၍",
    "ūhasati": "ပြုံးရယ်သည်", "ullapati": "စကား ပြောဆို ချော့မော့သည်", "ujjagghati": "ကျယ်လောင်စွာ ရယ်မောသည်",
    "uppaṇḍeti": "ကျီစယ် ပြက်ရယ်ပြုသည်", "ūhasiyamāno": "ပြုံးရယ်ခြင်း",
    "ullapiyamāno": "စကား ပြောဆို ချော့မော့ခြင်း", "ujjagghiyamāno": "ကျယ်လောင်စွာ ရယ်မောခြင်း",
    "uppaṇḍiyamāno": "ကျီစယ် ပြက်ရယ်ပြုခြင်း", "uhasati": NONE,     # the variant in Roman script
    "abhinisīdati": "အနီး၌ ထိုင်သည်", "abhinipajjati": "အနီး၌ လှဲလျောင်းသည်", "ajjhottharati": "ဖိ၍ အုပ်မိုးသည်",
    "methunaṃ": "မေထုန်", "catuttho puggalo": "စတုတ္ထ … ပုဂ္ဂိုလ်",
    "viniveṭhetvā": "ရုန်းထွက်၍", "vinimocetvā": "လွတ်မြောက်အောင် ပြုပြီး", "vijayasmiṃ": "အောင်နိုင်ခြင်း",
    "yena": NONE, "kāmaṃ": "အလိုရှိရာ",       # yena kāmaṃ «အလိုရှိရာသို့» (one phrase)
    # --- ^4-199 … ^4-201 (the five alms-food eaters)
    "mandattā": "ထုံထိုင်းခြင်း", "momūhattā": "အလွန် တွေဝေခြင်း", "iccho": "အလိုရှိသော", "ummādā": "ရူးသွပ်ခြင်း",
    "vikkhepā": "ပျံ့လွင့်ခြင်း", "vaṇṇitaṃ": "ချီးမွမ်းထားသော", "buddhehi": "ဘုရားရှင်", "appa": "နည်းခြင်း",
    "santuṭṭhiṃ": "ရောင့်ရဲမှု", "sallekhaṃ": "ခြိုးခြံခြင်း", "santuṭṭhiṃ nissāya": "ရောင့်ရဲမှုကိုသာ မှီ၍",
    "sallekhaṃ nissāya": "ခြိုးခြံခြင်းကိုသာ မှီ၍", "seṭṭho": "အကောင်းဆုံး", "uttamo": "အထွတ်အထိပ်",
    "pavaro": "အမွန်မြတ်ဆုံး", "mokkho": NONE, "gavā": "နွား", "maṇḍo": "အနှစ်",
    "eva piṇḍapātiko": "ဆွမ်းခံ၍သာ စားသူ", "eva sosāniko": "သုသာန်၌ နေသူ", "sosāniko": "သုသာန်၌ နေသူ",
}
T_REST = {       # chakka, sattaka, aṭṭhaka, navaka, dasaka
    "arahantā": "ရဟန္တာ", "dukkhassanta": "ဒုက္ခ၏ အဆုံး", "daṭṭhabbo": "သိမှတ်ရမည့်", "karoti": "@karoti",
    "kāḷakehi": "မည်းနက်သော", "ummujjati": "ပေါ်လာသည်", "hāyati": "ယုတ်လျော့သည်", "vaḍḍhati": "တိုးပွားသည်",
    "hāyati no vaḍḍhati": "ယုတ်လျော့သည် … တိုးပွားသည်", "tiṭṭhati no vaḍḍhati": "တည်တံ့သည် … တိုးပွားသည်",
    "patigādha": "ခြေကုပ်ရာ", "ṭhānesu": "နေရာ", "sāhu dhammesu": "သဘောတရား … ကောင်းသော", "tassa": "ထိုသူ",
    "parinibbāyissa": "ပရိနိဗ္ဗာန် ပြုသော", "gāmino": "ရောက်သော", "sakadāgāmissa": "သကဒါဂါမ်",
    "bījissa": "မျိုးစေ့ … ရှိသော", "uddhaṃsotassa": "အထက်သို့ စီးဆင်း၍",
}
CTX = {
    "4-M-10": {"dhamma": "တရား"},   # dhammappamāṇo / dhammappasanno «တရား…» (dhammo, dhammakathikā, adhipaññādhamma
                                    # are keywords of their own in this list)
    "4-176": {"rūpa": "အဆင်း", "evameva": "ဤနည်းတူ"},   # sarūpavacchā «မိခင်နှင့် အဆင်းတူသော»; the note «… evameva»
}
# ---- TABLES-END
SECTIONS = {"preamble": T_PREAMBLE, "1-matika": T_MATIKA, "2-ekakapuggalapannatti": T_EKAKA,
            "3-dukapuggalapannatti": T_DUKA, "4-tikapuggalapannatti": T_TIKA, "5-catukkapuggalapannatti": T_CATUKKA,
            "6-pancakapuggalapannatti": T_PANCAKA, "7-chakkapuggalapannatti": T_REST,
            "8-sattakapuggalapannatti": T_REST, "9-atthakapuggalapannatti": T_REST,
            "10-navakapuggalapannatti": T_REST, "11-dasakapuggalapannatti": T_REST}

CHAPTERS = ["preamble", "1-matika", "2-ekakapuggalapannatti", "3-dukapuggalapannatti", "4-tikapuggalapannatti",
            "5-catukkapuggalapannatti", "6-pancakapuggalapannatti", "7-chakkapuggalapannatti",
            "8-sattakapuggalapannatti", "9-atthakapuggalapannatti", "10-navakapuggalapannatti",
            "11-dasakapuggalapannatti"]
ONLY = None   # set by --only CH,CH (staged runs: preamble, 1-matika, 2-ekaka first)


# =====================================================================================================
# engine
# =====================================================================================================
def segments(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip():
            continue
        buf.append(l)
        m = ID.search(l)
        if m:
            out[m.group(1)] = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", " ".join(buf))
            buf = []
    return out


def load_map(path):
    d = collections.defaultdict(collections.Counter)
    for l in path.read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if not m:
            continue
        for kv in m.group(2).split(", "):
            if "=" in kv:
                k, v = kv.split("=", 1)
                d[low(k)][v] += 1
    return d


PRIOR = {t: load_map(p) for t, p in MAPS.items()}
PRIOR_ORDER = ("pi-2", "pi-3", "pi-1")     # pi-2 first where they differ (brief), then pi-3, then pi-1


def load_terms(names_only):
    """my4-zeroshot-terms.md lines «Pāli = Burmese (note)» -> {low(pāli): burmese}; names_only: the sections
    «Person-type names of the mātikā» and «Group names» (and the plural forms line), else the other sections."""
    t = {}
    sec = ""
    for l in TERMS_FILE.read_text(encoding="utf-8").split("## Variant readings")[0].splitlines():
        if l.startswith("## "):
            sec = l
            continue
        is_name = sec.startswith(("## Person-type names", "## Group names"))
        if is_name != names_only:
            continue
        if " = " not in l or l.startswith("#"):
            continue
        p, b = l.strip().split(" = ", 1)
        p = re.sub(r"\s*\((?:book title|heading[^)]*|chapter heading[^)]*)\)$", "", p).strip().rstrip(".?").strip()
        b = re.sub(r"\s*\((?=[^)]*[A-Za-z])[^()]*\)\s*$", "", b.strip())
        b = b.split(";")[0].strip().rstrip("။").strip()
        if "⟦" in b or not b or "၊" in b or len(p.split()) > 4:
            continue
        t.setdefault(low(p), b)
    for l in TERMS_FILE.read_text(encoding="utf-8").splitlines():      # «Plural forms of the definitions: a = A; …»
        if l.startswith("Plural forms of the definitions:"):
            for pair in l.split(":", 1)[1].split(";"):
                if " = " in pair:
                    p, b = pair.strip().split(" = ", 1)
                    t.setdefault(low(p.strip()), b.strip().rstrip("။"))
    return t


NAMES = load_terms(True)
TERMS = load_terms(False)
TERMS.update({k: v for k, v in NAMES.items()})      # for the helpers / compose: every pi-4 form

SHARED = {}
for _t in SECTIONS.values():
    for _k, _v in _t.items():
        SHARED.setdefault(low(_k), _v)


END_PARTICLES = ("တို့၌", "တို့ကို", "တို့၏", "တို့", "များ")


def strip_particles(t):
    """rule 1 for a terms-file value: a final plural + case particle goes (kusalesu dhammesu «…တို့၌»)."""
    for e in END_PARTICLES:
        if t.endswith(e) and len(t) > len(e) + 1:
            return t[: -len(e)]
    return t


def resolve(v, kw, pali, my, sid=None):
    if v is not None and v.startswith("@"):
        v = FUNCS[v[1:]](kw, pali, my)
        if v == "@prior":
            v = pi_get(kw, my)[0]
            if v is None:
                raise KeyError(kw)
    return v


def table_get(tab, kw):
    for k in (kw, low(kw), kw[:1].upper() + kw[1:]):
        if k in tab:
            return tab[k]
    return None


def prev_vals(kw, tag=None):
    c = collections.Counter()
    for t in ([tag] if tag else PRIOR_ORDER):
        c.update(PRIOR[t].get(low(kw), {}))
    return c


def contiguous(v, my):
    parts = v.split(" … ")
    if not all(p in my for p in parts):
        return False
    return len(parts) == 1 or v.replace(" … ", " ") not in my


def contiguous_rule(v, my):
    """every « … »-part of the value occurs as a whole phrase in the text, its final «သော» standing for one of the
    attributive endings of the presence check (e.g. «ရာဂ ကင်းသော» against «ရာဂ ကင်းသူ»)."""
    for part in v.split(" … "):
        if part in my:
            continue
        if not part.endswith("သော") or not any(part[:-3] + e in my for e in ATTR_FROM):
            return False
    return True


def pi_get(kw, my, tiers=("contig", "literal", "rule")):
    """the most frequent pi-2 (then pi-3, pi-1) value of the keyword present in the segment, by tier: a value whose
    parts occur contiguously in the text, then one whose every chunk is literally in the text, then (VERBS only,
    a value ending in «သည်») one matched by an ending rule. Non-verb values matched only by an ending rule are not
    taken automatically (they can sit anywhere in a long segment): those keywords are in the tables."""
    ranked = [(t, [v for v, _ in prev_vals(kw, t).most_common() if v != NONE]) for t in PRIOR_ORDER]
    for tier in tiers:
        for tag, vals in ranked:
            for v in vals:
                if tier == "rule" and not (v.endswith("သည်") or contiguous_rule(v, my)):
                    continue
                ok, rules = presence(v, my)
                if not ok:
                    continue
                if (tier == "contig" and contiguous(v, my)) or (tier == "literal" and not rules) or tier == "rule":
                    return v, tag
    return None, None


SRC = {}


def first_compound(pali, stems):
    best = None
    for st, val in stems:
        for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])" + st, pali, flags=re.I):
            if best is None or m.start() < best[0]:
                best = (m.start(), val)
            break
    return best[1] if best else None


# ---- FUNCS-BEGIN
GEN = {"khandhānaṃ": "အစုအဝေး", "āyatanānaṃ": "အာရုံခံ နယ်ပယ်", "dhātūnaṃ": "ဓာတ်", "saccānaṃ": "သစ္စာ",
       "indriyānaṃ": "စွမ်းရည်", "puggalānaṃ": PUG}


def by_first(stems, default):
    """one sense per segment (pi-1 harmonise decision 3): the sense of the FIRST of the stems in the Pāli segment."""
    def f(kw, pali, my):
        v = first_compound(pali, stems)
        return v if v is not None else default
    return f


def pref(a, b):
    """the value a where the segment's text has it (presence check), else b (the same keyword in another
    construction of the text: one sense per segment, the text's own word)."""
    def f(kw, pali, my):
        return a if presence(a, my)[0] else b
    return f


def by_sub(stems, default):
    """as by_first, but the stem may stand inside a compound (the first one by position in the Pāli)."""
    def f(kw, pali, my):
        best = None
        for st, val in stems:
            i = pali.find(st)
            if i >= 0 and (best is None or i < best[0]):
                best = (i, val)
        return best[1] if best else default
    return f


def f_pannatti(kw, pali, my):
    """paññatti = «သတ်မှတ်ချက်» (pi-1 ^1-M2-108); in the book title alone = the title's «သတ်မှတ်ဖော်ပြခြင်း»."""
    return "သတ်မှတ်ချက်" if "သတ်မှတ်ချက်" in my else "သတ်မှတ်ဖော်ပြခြင်း"


def f_puggalapannatti(kw, pali, my):
    """the book title «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း» (rule 7) where the text has it, else the designation
    «ပုဂ္ဂိုလ် သတ်မှတ်ချက်» (my4-zeroshot-terms «The six designations»)."""
    t = "ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း"
    return t if t in my else "ပုဂ္ဂိုလ် သတ်မှတ်ချက်"


def f_kittavata(kw, pali, my):
    """«Kittāvatā Xānaṃ» (question «Xတို့၏ X သတ်မှတ်ချက်သည် အဘယ်မျှ ရှိသနည်း»): X … အဘယ်မျှ (text order)."""
    return GEN[kw.split()[1]] + " … အဘယ်မျှ"


def f_ettavata(kw, pali, my):
    """«ettāvatā Xānaṃ» («ဤမျှသည် Xတို့၏ …»): the phrase with its inner «သည်» (pi-1 rule 1), the genitive goes."""
    return "ဤမျှသည် " + GEN[kw.split()[1]]


def f_dhammesu(kw, pali, my):
    return "တရား" if "တရားတို့၌" in my and "သဘောတရားတို့၌" not in my else "သဘောတရား"


def f_pahina(kw, pali, my):
    """pahīna: «ပယ်ပြီးသော» (text «ပယ်ပြီး ဖြစ်၏», perf-pred), the fragment of appahīna «ပယ်ရသော» («မပယ်ရသေး»)."""
    return "ပယ်ပြီးသော" if "ပယ်ပြီး" in my else "ပယ်ရသော"


def f_thito(kw, pali, my):
    return "တည်နေသော" if "တည်နေ" in my else "တည်သော"


def f_avasesa(kw, pali, my):
    return "ကြွင်းကျန်သော" if "ကြွင်းကျန်သော" in my else "အကြွင်း"


def f_dhamma_pl(kw, pali, my):
    """dhammā: the teachings «တရား» (Tathāgatappaveditā dhammā, ananussutesu dhammesu), else «သဘောတရား»."""
    return "တရား" if re.search(r"(?<!သဘော)တရားတို့", my) and "pavedit" in pali else "သဘောတရား"


def f_samma(kw, pali, my):
    """sammā: the homage «Sammāsambuddha» = «အပြည့်အဝ» (pi-1 / pi-2 / pi-3 preamble), elsewhere «မှန်ကန်သော», the
    adverb «မှန်ကန်စွာ» where the text has only that (sammāpaṭipanna, sammaggata)."""
    v = first_compound(pali, [("sammāsambuddh", "အပြည့်အဝ"), ("samm", "မှန်ကန်သော")]) or "မှန်ကန်သော"
    if v == "မှန်ကန်သော" and not presence(v, my)[0] and "မှန်ကန်စွာ" in my:
        return "မှန်ကန်စွာ"
    return v


def f_vuccati(kw, pali, my):
    """vuccati = «ခေါ်သည်»; where the Pāli has it only inside a Roman-script variant (^4-90) = (no direct equivalent)."""
    return "ခေါ်သည်" if re.search(r"\bvuccat", re.sub(r"\[[^\]]*\]", "", pali)) else NONE


def f_hoti(kw, pali, my):
    """hoti: the copula «ဖြစ်သည်» (text «… ဖြစ်၏»); existence «ရှိသည်» (pi-2) where the text has no «ဖြစ်»."""
    return "ဖြစ်သည်" if "ဖြစ်" in my else "ရှိသည်"


def f_phasu(kw, pali, my):
    return "ချမ်းသာစွာ" if "ချမ်းသာစွာ" in my else "ချမ်းသာ"


def f_digharattam(kw, pali, my):
    """dīgharattaṃ «for a long time»: «ရှည်လျားသော ကာလပတ်လုံး» where the text has it (after ciraṃ «ကြာမြင့်စွာ»),
    else the text's «ကြာမြင့်စွာ» (^4-116 / ^4-117: a different rendering, listed for the rails step)."""
    return "ရှည်လျားသော ကာလပတ်လုံး" if "ရှည်လျားသော ကာလပတ်လုံး" in my else "ကြာမြင့်စွာ"


def f_hetu(kw, pali, my):
    """hetu: «… အလို့ငှာ» (paṭicchādanahetu), «အကြောင်း» (atta- / para- / āmisahetu «…၏ အကြောင်းကြောင့်»)."""
    if "အလို့ငှာ" in my:
        return "အလို့ငှာ"
    return "အကြောင်း" if "အကြောင်းကြောင့်" in my else "ကြောင့်"


FUNCS = {
    # dhamma (fragment), one sense per segment: the teaching «တရား» / the phenomenon «သဘောတရား» by the first compound
    # that is not a keyword of its own in that list (dhammakathikā, adhipaññādhamma … are)
    "bhuta": by_sub([("pāṇabhūt", NONE), ("bhūtagām", "အပင်"), ("bhūtavād", "အမှန်")], "@prior"),
    "vaco_": pref("ပြောတတ်သော", "စကားကို ပြောသော"),
    "abhisamayo": pref("ထင်ထင်ရှားရှား သိမြင်ခြင်း", "ထိုးဖောက် သိမြင်ခြင်း"),
    "pariyogahetva": pref("စိစစ်၍", "စိစစ်"),
    "sammapatipanna": pref("မှန်ကန်စွာ ကျင့်ကြံသော", "မှန်ကန်စွာ ကျင့်သော"),
    "kasira": pref("ပင်ပန်း", "ခက်ခဲသော"),
    "dubbanno": pref("အဆင်း ညှိုးသော", "အဆင်း ဆိုးသော"),
    "mutta": by_first([("muttācār", "စွန့်လွှတ်သော"), ("muttappaṭibhān", "လျင်မြန်သော")], "လျင်မြန်သော"),
    "ajinam": pref("သမင်သားရေ", "သားရေ"),
    "mukha": pref("နှုတ်ခမ်း", "မျက်ရည် စီးသော"),
    "danda": pref("တုတ်", "ဒဏ်"),
    "sunati": pref("ကြားရသည်", "ကြားနာသည်"),
    "attham": pref("အနက်အဓိပ္ပာယ်", "အနက်"),
    "byanjanam": lambda kw, pali, my: "စကားလုံး" if "စကားလုံးနှင့် ပြည့်စုံ" in my else "သဒ္ဒါ",
    "attha": by_sub([("atthavād", "အကျိုး"), ("atthasaṃhit", "အကျိုး"), ("atthamaññ", "အနက်")], "အနက်"),
    "kari": by_sub([("sampajānakār", "ပြုလေ့ရှိသော")], "ကျင့်သော"),
    "vigata": pref("ကင်းပြီးသော", "ကင်းသော"),
    "pana_": pref("သူ့အသက်", "သတ္တဝါ"),
    "dharanata": pref("စွဲမှတ်ထားခြင်း", "စွဲမှတ် ထားခြင်း"),
    "attana": pref("မိမိကိုယ်တိုင်", "မိမိကိုယ်"),
    "manasi": pref("နှလုံးသွင်းခြင်း", "နှလုံး"),
    "sappi": lambda kw, pali, my: "ထောပတ်ကြည်" if "sappimaṇḍ" in pali else "ထောပတ်",
    "gahapati": pref("သူကြွယ်မျိုး", "သူကြွယ်"),
    "thite": pref("တည်တံ့သော", "ရပ်ရာ"),
    "gate": pref("လားရာ ရှိသော", "သွားရာ"),
    "aharo": pref("ဆောင်ခြင်း", "အစာ"),
    "dukkhassa": pref("ဒုက္ခ", "နာကျင်မှု"),
    "upapanno": pref("ပြည့်စုံသော", "ဖြစ်ပေါ်လာသော"),
    "kammam": pref("ပြုခြင်း", "ကံ"),
    "patipanno": pref("ကျင့်ကြံသော", "ကျင့်သော"),
    "elaka": by_first([("eḷakamantar", "တံခါးခုံ"), ("ajeḷak", "သိုး")], "တံခါးခုံ"),
    "nikati": lambda kw, pali, my: "ကောက်ကျစ်ခြင်း" if "ကောက်ကျစ်ခြင်း" in my else "စဉ်းလဲခြင်း",
    "patta": by_first([("sapattabhār", "အတောင်")], "သပိတ်"),
    "indriya": lambda kw, pali, my: "အာရုံခံ အင်္ဂါ" if "အာရုံခံ အင်္ဂါ" in my else "စွမ်းရည်",
    "raja": pref("မြူမှုန်", "ဖုန်လုံး"),
    "sutte": by_sub([("kandarakasutt", "သုတ်"), ("attantapasutt", "သုတ်"), ("sutte jāgar", "အိပ်ရာ")], "အိပ်ရာ"),
    "carati": pref("ကျင့်သည်", "ပြုသည်"),
    "samannagato": pref("အပြည့်အဝ ပြည့်စုံသော", "ပြည့်စုံသော"),
    "byapajjati": pref("ဖောက်ပြန်သည်", "ဒဏ်ရာ ရသည်"),
    "gatam": pref("မှား", "ရောက်သော"),
    "sunati3": lambda kw, pali, my: next((v for v in ("ကြားရသည်", "ကြားနာသည်", "ကြားသည်") if presence(v, my)[0]), "ကြားသည်"),
    "karoti": lambda kw, pali, my: NONE if not re.search(r"\bkaroti\b", re.sub(r"\[[^\]]*\]", "", pali)) else "ပြုသည်",
    # diṭṭhe (ceva) dhamme = «မျက်မှောက်ဘဝ»: dhamme = «ဘဝ» (^4-M-12 diṭṭhe dhamme)
    "dhamme": lambda kw, pali, my: "ဘဝ" if re.search(r"diṭṭhe(va| ceva)? dhamme", pali) and "မျက်မှောက်ဘဝ" in my
        else (pi_get(kw, my)[0] or "သဘောတရား"),
    "katta": lambda kw, pali, my: "ပြုလုပ်သူ" if "ပြုလုပ်သူ" in my else "တူးသူ",
    "obhaso": lambda kw, pali, my: "ဟန် ထင်ရသော" if "ဟန် ထင်ရ" in my else "အရောင်အဝါ",
    "gava": lambda kw, pali, my: "နွား",
    "neva": lambda kw, pali, my: NONE if re.search(r"\[[^\]]*\bneva\b", pali) and not re.search(
        r"\bneva\b", re.sub(r"\[[^\]]*\]", "", pali)) else (pi_get(kw, my)[0] or "မ"),
    "senasana": lambda kw, pali, my: "ကျောင်းအိပ်ရာနေရာ" if "ကျောင်းအိပ်ရာနေရာ" in my else "အိပ်ရာ နေရာ",
    "vacaya": lambda kw, pali, my: "နှုတ်" if "နှုတ်" in my else "စကား",
    "dhamma": by_first([("pāpadhamm", "သဘော"), ("kalyāṇadhamm", "သဘော"), ("dhammavinay", "တရား"), ("dhammadesan", "တရား"), ("dhammassavan", "တရား"),
                        ("dhammassavaṇ", "တရား"), ("dhammānusār", "တရား"), ("dhammamacchariy", "တရား"),
                        ("dhammappam", "တရား"), ("dhammappas", "တရား"), ("dhammāyatan", "သဘောတရား"),
                        ("dhammadhāt", "သဘောတရား"), ("dhammavicay", "သဘောတရား")], "@prior"),
    "purisa": lambda kw, pali, my: "ယောက်ျား" if "ယောက်ျား" in my else "လူ",
    "dukkhaya": lambda kw, pali, my: "ဆင်းရဲခြင်း" if "ဆင်းရဲခြင်းငှာ" in my else "နာကျင်သော",
    "sukhaya": lambda kw, pali, my: "ချမ်းသာခြင်း" if "ချမ်းသာခြင်းငှာ" in my else "သာယာသော",
    "phasu": f_phasu, "digharattam": f_digharattam, "hetu": f_hetu,
    "vutthati": by_first([("vuṭṭhāti tamhā ābādh", "ပျောက်ကင်းသည်")], "ထမြောက်သည်"),
    "gilana": lambda kw, pali, my: "သူနာ" if "gilānapaccay" in pali else "လူနာ",
    "unnalo": lambda kw, pali, my: "ဘဝင်မြင့်သော" if "ဘဝင်မြင့်" in my else "ဘဝင် မြင့်သော",
    "mukharo": lambda kw, pali, my: "စကားများသော" if "စကားများ" in my else "စကား များသော",
    "pameyyo": lambda kw, pali, my: "ချိန်ဆရ" if "ချိန်ဆရ" in my else "ချိန်ဆ၍ ရနိုင်သော",
    "kula": by_first([("rājakul", "မင်းမျိုးမင်းနွယ်"), ("kulamacchariy", "ကိုးကွယ်သော အိမ်")], "အမျိုး"),
    "tatra": by_first([("tatra udak", NONE), ("tatra yvāy", NONE)], NONE),
    "phalam": by_first([("phalaṃ vipāk", "အသီးအပွင့်")], "အကျိုး"),
    "gandha": lambda kw, pali, my: "နံ့သာ" if re.search(r"gandhakaraṇḍ|mālāgandh", pali) else pi_get(kw, my)[0],
    "nanam": by_first([("aññāṇ", "သိခြင်း"), ("ñāṇ", "ဉာဏ်")], "ဉာဏ်"),
    "hoti": f_hoti, "vuccati": f_vuccati,
    "pada": by_first([("padaparam", "စကားလုံး"), ("padasiddh", "ပုဒ်")], "စကားလုံး"),
    "thanam": by_first([("vivādaṭṭhān", "အကြောင်း")], "အကြောင်း"),
    "evam": lambda kw, pali, my: (lambda v: v if presence(v, my)[0] else "ဤနည်းတူ")(
        by_first([("evaṃ khudd", "ဤနည်းတူ"), ("evamuparipi", "ဤနည်းတူ")], "ဤသို့")(kw, pali, my)),
    "aggam": lambda kw, pali, my: "ဖျား" if "အလံဖျား" in my else NONE,
    "avikatva": pref("ထုတ်ဖော်၍", "ထုတ်ဖော်"),
    "dubbalyam_avikatva": pref("အားနည်းချက်ကို ထုတ်ဖော်၍", "အားနည်းချက်ကို ထုတ်ဖော်"),
    "paccakkhaya": pref("စွန့်၍", "စွန့်"),
    "ekanta": pref("စင်စစ်", "လုံးဝ"),
    "ayatanam": by_first([("titthāyatan", "တည်ရာ")], "အာရုံခံ နယ်ပယ်"),
    "pannatti": f_pannatti, "pahina": f_pahina, "thito": f_thito, "avasesa": f_avasesa, "dhamma_pl": f_dhamma_pl,
    "bhabba": by_first([("cetanābhabb", "ထိန်းနိုင်သော"), ("anurakkhaṇābhabb", "ထိန်းနိုင်သော"),
                        ("bhabbāgaman", "ထိုက်တန်သော"), ("abhabbāgaman", "ထိုက်တန်သော")], "ထိုက်တန်သော"),
    "sambuddho": lambda kw, pali, my: by_first(
        [("sammāsambuddh" + kw[-1], "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရား"), ("paccekasambuddh" + kw[-1], NONE)],
        "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရား")(kw, pali, my), "puggalapannatti": f_puggalapannatti, "kittavata": f_kittavata, "ettavata": f_ettavata, "dhammesu": f_dhammesu,
    # pi-3 f_dukkha / f_sukha (approved), with the pi-4 compounds
    "dukkha": lambda kw, pali, my: (lambda v: v if presence(v, my)[0] else "နာကျင်မှု")(by_first([("adukkhamasukh", "နာကျင်"), ("dukkhasacc", "ဒုက္ခ"), ("dukkhindriy", "နာကျင်မှု"),
                        ("dukkhāya", "နာကျင်သော"), ("dukkhaṃ", "ဒုက္ခ"), ("dukkhassa", "ဒုက္ခ")], "ဒုက္ခ")(kw, pali, my)),
    "sukha": by_first([("sukhindriy", "သာယာမှု"), ("sukhasahagat", "သာယာမှု"), ("sukhāya", "သာယာသော"),
                       ("sukhappaṭisaṃvedī", "သာယာမှု")], "သာယာမှု"),
    # sammā: the homage «Sammāsambuddha» = «အပြည့်အဝ» (pi-1 / pi-2 / pi-3 preamble), elsewhere «မှန်ကန်သော»
    "samma": f_samma,
    "sankhara": by_first([("asaṅkhār", "တိုက်တွန်းမှု"), ("sasaṅkhār", "တိုက်တွန်းမှု"),
                          ("saṅkhārakkhandh", "ပြုပြင်ဖန်တီးမှု")], "ပြုပြင်ဖန်တီးမှု"),
    "sota": by_first([("anusota", "ရေစီး"), ("paṭisota", "ရေစီး"), ("sotāyatan", "နား"), ("sotadhāt", "နား"),
                      ("sotaviññāṇ", "နား"), ("sotindriy", "နား")], "နား"),
    "puthu": by_first([("puthujjan", "ပုထုဇဉ်"), ("puthupañ", "ကျယ်ပြန့်သော")], "ပုထုဇဉ်"),
    "gami": by_first([("uddhaṃsotoakaniṭṭhagām", "ရောက်သော"), ("anusotagām", "လိုက်သွားသော"),
                      ("paṭisotagām", "သွားသော")], NONE),
    "phala": by_first([("uṭṭhānaphal", "အကျိုး"), ("puññaphal", "အကျိုး"), ("vanamūlaphal", "အသီး")], "ဖိုလ်"),
    "thita": by_first([("ṭhitakapp", "တည်နေစေသော"), ("ṭhitatt", "တည်ငြိမ်သော")], "တည်နေသော"),
    "sama": by_first([("samasīs", "တပြိုင်နက်"), ("asamapekkh", "ညီညီညွတ်ညွတ်"), ("samapekkh", "ညီညီညွတ်ညွတ်")],
                     "တပြိုင်နက်"),
    "eka": by_first([("ekabīj", "တစ်စေ့"), ("ekāsanik", "တစ်ထိုင်")], "တစ်"),
    "vanna": by_first([("vaṇṇamacchariy", "ဂုဏ်သတင်း"), ("vaṇṇapokkhar", "အသားအရေ"), ("avaṇṇārah", "ချီးမွမ်း"), ("vaṇṇārah", "ချီးမွမ်း"), ("vaṇṇaṃ", "ချီးမွမ်း"),
                       ("avaṇṇaṃ", "ချီးမွမ်း"), ("vaṇṇo", "ချီးမွမ်းဖွယ်")], "အဆင်းအရောင်"),
    # rūpa (pi-3 f_rupa, approved): the fine-material plane «သိမ်မွေ့သော ရုပ်» (rūpāvacara, rūpabhava, and now
    # rūpasahagata / rūparāga «သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်ဘဝ»), the visible object «အဆင်းအရောင်», matter «ရုပ်»
    "rupa": by_first([("rūpāvacar", "သိမ်မွေ့သော ရုပ်"), ("rūpabhav", "သိမ်မွေ့သော ရုပ်"),
                      ("rūpasahagat", "သိမ်မွေ့သော ရုပ်"), ("rūparāg", "သိမ်မွေ့သော ရုပ်"),
                      ("rūpāyatan", "အဆင်းအရောင်"), ("rūpadhāt", "အဆင်းအရောင်"), ("rūpappam", "အဆင်းအရောင်"),
                      ("rūpappas", "အဆင်းအရောင်"), ("rūpakkhandh", "ရုပ်"), ("rūpa", "@prior")], "@prior"),
    "yatha": by_first([("yathāsanthatik", "အတိုင်း")], "အတိုင်း"),
}
# ---- FUNCS-END


def compose(ch, sid, kw, pali, my):
    try:
        return _compose(ch, sid, kw, pali, my)
    except KeyError:
        return None


NEG_PREFIX = ("na ", "no ", "neva ")


def number(kw, my):
    """P5: a count of persons keeps the text's classifier «ယောက်», of things «ပါး» (pi-1 harmonise decision 5)."""
    n = NUM_MY.get(low(kw))
    if n is None:
        return None
    for c in ("ယောက်", "ပါး", "မျိုး", ""):
        if n + c in my:
            return n + c
    return None


def _compose(ch, sid, kw, pali, my):
    ws = kw.split()
    if len(ws) == 1:
        return number(kw, my)
    # P1: «NAME puggalo» (mātikā) = the NAME's attributive form + «ပုဂ္ဂိုလ်» (text «…သော ပုဂ္ဂိုလ်»)
    if len(ws) == 2 and low(ws[1]) in ("puggalo", "puggalā"):
        t = TERMS.get(low(ws[0]))
        if t and t.endswith("သူ") and t[:-2] + "သော " + PUG in my:
            return t[:-2] + "သော " + PUG
        n = number(ws[0], my)
        if n and f"{PUG} {n}" in my:
            return f"{PUG} {n}"
    if low(ws[0]) in ("na", "no", "neva"):
        return None
    # a multiword keyword: its members' values joined in TEXT order, « … » where they are not adjacent (rule 10)
    if len(ws) == 2 and low(ws[0]) in ("vuccati", "vuccanti") and low(ws[1]) not in ("puggalo", "puggalā"):
        b = lookup(ch, sid, ws[1], pali, my, inner=True)       # pi-2 «vuccati rūpaṃ = ရုပ်ဟု ခေါ်သည်»
        if b + "ဟု ခေါ်သည်" in my:
            return b + "ဟု ခေါ်သည်"
    if len(ws) == 2:
        a, b = (lookup(ch, sid, w, pali, my, inner=True) for w in ws)
        for x, y in ((a, b), (b, a)):
            if NONE not in (x, y) and f"{x} {y}" in my:
                return f"{x} {y}"
    if len(ws) > 2:
        for a_, b_ in ((" ".join(ws[:-1]), ws[-1]), (ws[0], " ".join(ws[1:]))):
            multi = a_ if " " in a_ else b_
            if table_get(SHARED, multi) is not None or prev_vals(multi):
                try:
                    x, y = lookup(ch, sid, a_, pali, my, inner=True), lookup(ch, sid, b_, pali, my, inner=True)
                except KeyError:
                    continue
                px, py = find_pos(x, my), find_pos(y, my)
                (x, y) = (x, y) if px <= py else (y, x)
                return x + (" " if f"{x.split(' … ')[-1]} {y.split(' … ')[0]}" in my else " … ") + y
    vals = []
    for w in ws:
        v = lookup(ch, sid, w, pali, my, inner=True)
        if v == NONE:
            continue
        vals.append(v)
    if not vals:
        return NONE
    pos = [find_pos(v, my) for v in vals]
    order = [v for _, v in sorted(zip(pos, vals), key=lambda x: x[0])]
    out = order[0]
    for v in order[1:]:
        if v in out:
            continue
        out = out + (" " if (out.split(" … ")[-1] + " " + v.split(" … ")[0]) in my else " … ") + v
    return out


def find_pos(v, my):
    """position of a value in the text: its first part, else that part without its final «သော / သည်» (the text's
    ending differs), else its first chunk (likewise)."""
    first = v.split(" … ")[0]
    for c in (first, first[:-3] if first.endswith(("သော", "သည်")) else None, first.split()[0],
              first.split()[0][:-3] if first.split()[0].endswith(("သော", "သည်")) else None):
        if c:
            p = my.find(c)
            if p < 0 and c.startswith("မ"):
                p = my.find(c[1:])
            if p >= 0:
                return p
    return 10 ** 6


def lookup(ch, sid, kw, pali, my, inner=False):
    v = table_get(CTX.get(sid, {}), kw)
    if v is not None:
        SRC[(sid, kw)] = "ctx"
        return resolve(v, kw, pali, my)
    v = table_get(SECTIONS.get(ch, {}), kw)
    if v is None:
        v = table_get(SHARED, kw)
    if v is not None:
        SRC[(sid, kw)] = "table"
        return resolve(v, kw, pali, my)
    t = NAMES.get(low(kw))                    # P1: the approved person-type NAME
    if t is not None and presence(t, my)[0]:
        SRC[(sid, kw)] = "name"
        return t
    v, tag = pi_get(kw, my, tiers=("contig",))   # a pi-2 / pi-3 / pi-1 value the text has as a phrase
    if v is not None:
        SRC[(sid, kw)] = tag
        return v
    t = TERMS.get(low(kw))
    if t is not None:
        t = strip_particles(t)
        if presence(t, my)[0]:
            SRC[(sid, kw)] = "terms"
            return t
    if " " in kw:
        v = compose(ch, sid, kw, pali, my)
        if v is not None and presence(v, my)[0]:
            SRC[(sid, kw)] = "compose"
            return v
    v = number(kw, my)
    if v is not None:
        SRC[(sid, kw)] = "compose"
        return v
    v, tag = pi_get(kw, my)
    if v is not None:
        SRC[(sid, kw)] = tag
        return v
    raise KeyError(kw)


def load(ch):
    my = segments(MY / f"{ch}.md")
    pa = segments(PI / f"{ch}.md")
    rows = [LINE.match(l).groups() for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()
            if LINE.match(l)]
    return my, pa, rows


def chapters():
    return [c for c in CHAPTERS if ONLY is None or c in ONLY]


def run(write=True):
    table = collections.defaultdict(collections.Counter)
    unmapped = collections.defaultdict(list)
    problems, summary = [], []
    for ch in chapters():
        my, pa, rows = load(ch)
        lines, nne = [], 0
        for sid, kws in rows:
            pairs = []
            for kw in [k.strip() for k in kws.split(", ")]:
                try:
                    v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                except KeyError:
                    unmapped[kw].append((ch, sid))
                    v = "?"
                else:
                    ok, _ = presence(v, my[sid])
                    if not ok:
                        problems.append((ch, sid, kw, v))
                pairs.append(f"{kw}={v}")
                table[kw][v] += 1
                nne += v == NONE
            lines.append(f"[{sid}] " + ", ".join(pairs))
        summary.append((ch, len(lines), nne))
        if write and not unmapped and not problems:
            (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return table, unmapped, problems, summary


def verify(ch):
    a = [l.split("] ", 1) for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    my, _, _ = load(ch)
    fails, ruled = [], []
    for (i, x), (_, y) in zip(a, b):
        for kv in y.split(", "):
            k, v = kv.split("=", 1)
            ok, rules = presence(v, my[i[1:]])
            if not ok:
                fails.append((i, k, v))
                continue
            for c, r in rules:
                ruled.append((i[1:], k, c, r))
    punct = [i for (i, x), (_, y) in zip(a, b)
             if any(", " in v or "၊" in v or " / " in v for v in [kv.split("=", 1)[1] for kv in y.split(", ")])
             or y.count("=") != len(x.split(", "))]
    return len(a), bad, fails, punct, ruled


# =====================================================================================================
# rules and reasons (written to map-table.md)
# =====================================================================================================
RULES = """## Rules

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-4 text) that carries the keyword, in the
dictionary form of the approved pi-1 / pi-2 / pi-3 Burmese mappings. **Binding and unchanged:** pi-1 `map-table.md`
rules 1–11 and the agreed later pi-1 rules (absolutives keep «…၍»; relative pronouns = (no direct equivalent) where the
Burmese builds the clause with «ရှိသော / ရှိသမျှ» (^4-166 Yo); one sense per segment; no « / » alternatives), pi-2
N1–N11 and harmonise decisions (compound members inside one Burmese word = (no direct equivalent); «vuccati X» =
«Xဟု ခေါ်သည်»), pi-3 M1–M9 (the « … » gap; a translated editors' note gets values, a Roman-script variant = (no direct
equivalent); the shared presence check). pi-2, pi-3 and pi-1 values are reused for the same keyword where they occur in
the pi-4 segment: the script looks every keyword not in its own tables up in the final pi-2, then pi-3, then pi-1 mapping
(the most frequent value that the segment's text has as a phrase; a value matched only by an ending rule is taken
automatically only when it is a verb «…သည်» or its whole phrase stands in the text with another attributive ending).

How the approved rules apply to the Puggalapaññatti's shapes:

- **Nouns** (rule 1): no case particle / plural at the end (ekaccassa puggalassa «…ပုဂ္ဂိုလ်၏» = ပုဂ္ဂိုလ်); inner particles
  of a phrase stay (sīlesu paripūrakārī = သီလတို့ကို ပြည့်စုံစွာ ကျင့်သော; ettāvatā khandhānaṃ = ဤမျှသည် အစုအဝေး).
- **Adjectives / participles / -ī adjectives** (rule 3): «…သော», the text's person noun «…သူ» normalised (vimutto =
  လွတ်မြောက်သော, parinibbāyī = ပရိနိဗ္ဗာန် ပြုသော, pāṇātipātī = သူ့အသက်ကို သတ်သော); gerundives as the text builds
  them («…အပ်»: sevitabbo = ပေါင်းသင်းအပ်; «…ရမည့်»: upaṭṭhātabbā = လုပ်ကျွေးပြုစုရမည့်).
- **Verbs** (rule 4): verb + «သည်» whatever the text's ending (viharati = နေသည်, kujjhati = အမျက်ဒေါသ ထွက်သည်);
  a negated verb gives the positive verb (rule 8: santhambhati «မရပ်တည်နိုင်» = ခိုင်ခိုင်မာမာ ရပ်တည်နိုင်သည်).
- **The definition frame** (my4-zeroshot-terms «The definition frame»): Katamo = အဘယ်, Katamo puggalo = အဘယ် ပုဂ္ဂိုလ်,
  vuccati puggalo = ပုဂ္ဂိုလ် … ခေါ်သည် (text «ဤပုဂ္ဂိုလ်ကို “X”ဟု ခေါ်သည်»), vuccati X = Xဟု ခေါ်သည် (pi-2
  vuccati rūpaṃ), Kittāvatā Xānaṃ = X … အဘယ်မျှ, ettāvatā Xānaṃ = ဤမျှသည် X, Yāvatā = ရှိသမျှ.
- **Sense by context, one sense per segment** (pi-1 decision 3): the pi-3 functions f_rupa / f_dukkha / f_sukha (rūpa
  in rūpasahagata / rūparāga = the fine-material plane «သိမ်မွေ့သော ရုပ်»), sammā (homage «အပြည့်အဝ» / «မှန်ကန်သော» /
  adverb «မှန်ကန်စွာ»), and for pi-4: dhamma (teaching «တရား» / phenomenon «သဘောတရား» / pāpadhamma «သဘော»),
  saṅkhāra (asaṅkhāra «တိုက်တွန်းမှု»), sota (anusota «ရေစီး»), puthu (puthujjana / puthupañña), phala (fruit /
  path-fruit «ဖိုလ်» / result «အကျိုး»), vaṇṇa (praise / reputation / complexion), hetu, kula, gilāna (lūna «လူနာ» /
  gilānapaccaya «သူနာ»), raja (dust cloud «ဖုန်လုံး»), and others: the first compound of the Pāli segment that is not
  a keyword of its own decides (functions in the script, each with its stems).

## NEW rules (beyond pi-1 / pi-2 / pi-3)

P1. **Person-type names** (brief rule 2): the keyword of a person type = the approved NAME of my4-zeroshot-terms
    «Person-type names» / «Group names» (also its plural, sekkhā = ကျင့်ကြံဆဲသူ), the same value in mātikā, heading and
    definition. Where the mātikā builds the name before «puggalo» as an adjective, the presence check accepts the NAME
    «Xသူ» against the text's «Xသော ပုဂ္ဂိုလ်» (rule «name-attr»), and «NAME puggalo» = «Xသော ပုဂ္ဂိုလ်».
P2. **Fragments of names** (rule 8 applied to compounds): a fragment keyword = the part of its compound's NAME that
    carries it, by the compound the fragment belongs to (one sense per segment): kuppa = ပျက်ယွင်းတတ်သော, dhammo =
    သဘော ရှိသော, gotra = အရိယာ အနွယ်, bhū = ပြောင်းသော, kappī = ကမ္ဘာ, ṭhita = တည်နေစေသော (Ṭhitakappī),
    akaniṭṭha = အကနိဋ္ဌ ဘုံ, gāmī = ရောက်သော (Uddhaṃsotoakaniṭṭhagāmī, whose members are the neighbouring keywords).
    A name that is one Burmese word gives its word to one member, the other = (no direct equivalent) (pi-2 decision 4:
    puthu = ပုထုဇဉ်, jano = (no direct equivalent); pacceka = ပစ္စေကဗုဒ္ဓါ, sambuddho in paccekasambuddho = (no direct
    equivalent); pakkhahata «လေဖြတ်», pakkha = (no direct equivalent)).
P3. **Presence check, more endings** (presence_check.py, each marked «pi-4»): «Xသော» also against «Xလည်း / Xကား /
    Xသေး / Xလျှင် / Xစဉ် / Xလိမ့်မည် / Xသကဲ့သို့ / Xသဖြင့်», «Xသည်» also against «Xလည်း / Xကား / Xသူ / Xဘဲ / Xကာ /
    Xသတတ် / Xသကဲ့သို့»; a variant bracket «[…]» is not a word boundary («ပြည်ယို [ပါဌ်ကွဲ …]သကဲ့သို့»).
P4. **Cognate object** «X-anuyogam anuyutto» («…ကို အားထုတ်သူ», one verb): anuyoga = (no direct equivalent), as pi-1
    caya (one Burmese word for apacaya); khalu (khalupacchābhattika «… ဆွမ်းကို မစားသူ») likewise.
P5. **Counts of persons**: the text's classifier «ယောက်» (Dasa puggalā = ပုဂ္ဂိုလ် ဆယ်ယောက်), of things «ပါး», of kinds
    «မျိုး» (pi-1 harmonise decision 5).
P6. **Agent nouns in -tar and the -ika practitioners / occupations** stay nouns «…သူ» as the text has them (bhāsitā =
    ပြောဆိုသူ, pi-2; kattā, vassitā, gajjitā, ubbejitā; piṇḍapātiko / sosāniko … = the group NAMES; orabbhiko = သိုး
    သတ်သူ …): they are person nouns, not attributive participles.
P7. **Comparatives** «X-ena Xtaro»: the instrumental = the standard «X» (asappurisena = သူတော်ကောင်း မဟုတ်သူ, the
    «ထက်» of comparison goes, rule 1), Xtaro = «ပို၍ X» (asappurisataro = ပို၍ သူတော်ကောင်း မဟုတ်သူ).
P8. **The mātikā predicates «atthekacco puggalo P»**: puggalo P = «ပုဂ္ဂိုလ် … P» in text order (puggalo attantapo =
    ပုဂ္ဂိုလ် … မိမိကိုယ်ကို ပူပန်စေသော); multiword keywords compose their members' values in TEXT order with « … »
    for a gap (rule 10), a contiguous pair first (paṭipanno puggalo = ကျင့်ကြံသော ပုဂ္ဂိုလ်).
"""

REASONS = {
    "sammāsambuddho": "P1: the approved NAME «…ဘုရားရှင်» (pi-2 «…ဘုရား» is only its substring)",
    "eka": "^4-M-7: the fragment of Ekabījī «မျိုးစေ့ တစ်စေ့သာ» (Ekakaṃ «တစ်မျိုးတွဲ» is a keyword of its own)",
    "bhāga": "ubhatobhāga «နှစ်ဖက်စလုံးမှ» (pi-3 «သဘော» is sabhāga «like nature», another word)",
    "vaṇṇa": "the sense of the segment (praise «ချီးမွမ်း», reputation «ဂုဏ်သတင်း», complexion «အသားအရေ»); pi-2 «အရောင်» is "
             "only a substring of «အဆင်းအရောင်»",
    "sekkhā": "P1: the plural of the NAME sekkho «ကျင့်ကြံဆဲသူ» (pi-1 «ကျင့်ကြံဆဲသူ၏» is a genitive, pi-2 «ကျင့်ကြံမှု» a noun)",
    "saṭho": "P1: the approved NAME «စဉ်းလဲသူ»",
    "brahmacariyaṃ": "pi-1 brahmacariya «မြင့်မြတ်သော အကျင့်» (pi-2 «မြတ်သော» is only a substring of «မြင့်မြတ်သော»)",
    "purisapuggalo": "the text renders both members «ဤလူ ပုဂ္ဂိုလ်» (pi-2 «ပုဂ္ဂိုလ်» = the head only)",
    "sutte": "^4-176 the note «kandarakasutte» «ကန္ဒရကသုတ်» (pi-2 «အိပ်ရာ» = sutte «asleep», which is elsewhere in the segment)",
    "pāṇa": "pāṇātipāta «သူ့အသက်ကို သတ်ခြင်း» (the first pāṇa compound of ^4-178); in pāṇabhūta the pi-2 «သတ္တဝါ» is kept",
    "indriya": "indriyasaṃvara «အာရုံခံ အင်္ဂါ စောင့်စည်းမှု» (pi-1 indriyesu); «စွမ်းရည်» belongs to cakkhundriya, a keyword of its own",
    "dhamme": "diṭṭhe (ceva) dhamme «မျက်မှောက်ဘဝ» (^4-M-12 diṭṭhe dhamme), dhamme = «ဘဝ»",
}
AUTO_REASON = "the pi-1 / pi-2 / pi-3 value is not in this segment's Burmese: the pi-4 text words it differently"


def write_table(table, ruled_all, results):
    total = sum(sum(c.values()) for c in table.values())
    known = [kw for kw in table if prev_vals(kw)]
    same = [(kw, v, n) for kw, c in table.items() for v, n in c.items() if v in prev_vals(kw)]
    by = {t: [x for x in same if x[1] in prev_vals(x[0], t)] for t in PRIOR_ORDER}
    with open(HERE / "map-table.md", "w", encoding="utf-8") as f:
        f.write("# pi-4 Burmese keyword mapping: rules and review table (Puggalapaññatti «ပုဂ္ဂိုလ်များကို သတ်မှတ်ဖော်ပြခြင်း», "
                "the whole book)\n\n")
        f.write("Written by map_all.py. Burmese from the FINAL pi-4 text of this track only "
                "(AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters); approved pi-4 forms from "
                "my4-zeroshot-terms.md; pi-1 / pi-2 / pi-3 values from AI_translation/burmese/pi-{1,2,3}-keywords-by-"
                "reference-pali-burmese-plain.md. No other Burmese source.\n\n")
        f.write("## Verification\n\n| chapter | lines | keyword preservation | presence failures | comma / ၊ / « / » "
                "| rule-matched chunks | (no direct equivalent) |\n|---|---|---|---|---|---|---|\n")
        for ch, ln, bad, fails, punct, ruled, nne in results:
            f.write(f"| {ch} | {ln} | bad {bad} | {len(fails)} | {punct} | {len(ruled)} | {nne} |\n")
        f.write(f"\n## Reuse of pi-1 / pi-2 / pi-3\n\n- Keyword uses: {total}; distinct keywords: {len(table)}.\n"
                f"- Keywords that pi-1, pi-2 or pi-3 also has: {len(known)} distinct; their values taken **unchanged from "
                f"pi-1 / pi-2 / pi-3**: {len(same)} distinct keyword-value pairs, {sum(x[2] for x in same)} uses ("
                + "; ".join(f"a {t} value: {len(by[t])} pairs, {sum(x[2] for x in by[t])} uses" for t in PRIOR_ORDER)
                + ").\n"
                f"- Keywords new in pi-4 (in none of the three mappings): {len(table) - len(known)} distinct.\n\n")
        f.write("### Values that differ from pi-1 / pi-2 / pi-3 for the same keyword\n\n| keyword | pi-4 value (uses) | "
                "pi-2 / pi-3 / pi-1 value(s) | reason |\n|---|---|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            pa = prev_vals(kw)
            if not pa:
                continue
            for v, n in table[kw].items():
                if v not in pa:
                    f.write(f"| {kw} | {v} ({n}) | " + " · ".join(f"{x} ({m})" for x, m in pa.most_common(3))
                            + f" | {REASONS.get(low(kw), REASONS.get(kw, AUTO_REASON))} |\n")
        f.write("\n" + RULES)
        f.write("\n## Presence: chunks matched by an ending rule (not literally in the segment)\n\n"
                "Every other chunk of every value occurs literally in its segment's Burmese.\n\n"
                "| segment | keyword | chunk | rule |\n|---|---|---|---|\n")
        for sid, k, c, r in ruled_all:
            f.write(f"| {sid} | {k} | {c} | {r} |\n")
        f.write("\n## Keyword → Burmese (uses)\n\n«pi-2» / «pi-3» / «pi-1» = the value is a value of the same keyword "
                "there. Several values = the keyword reads differently by context.\n\n"
                "| Pāli keyword | Burmese (uses) |\n|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            f.write(f"| {kw} | " + " · ".join(
                f"{v} ({n}" + next((f", {t}" for t in PRIOR_ORDER if v in prev_vals(kw, t)), "") + ")"
                for v, n in table[kw].most_common()) + " |\n")



def fmt(sid, kw, v, my):
    ok = presence(v, my)[0]
    return f"{kw}={v}[{SRC.get((sid, kw), '?')}{'' if ok else ' FAIL'}]"


def show(sids, pali=True):
    for ch in CHAPTERS:
        my, pa, rows = load(ch)
        R = dict(rows)
        for sid in sids:
            if sid not in R:
                continue
            print("==", sid)
            if pali:
                print(pa.get(sid))
            print(my[sid])
            out = []
            for kw in [k.strip() for k in R[sid].split(", ")]:
                try:
                    out.append(fmt(sid, kw, lookup(ch, sid, kw, pa.get(sid, ""), my[sid]), my[sid]))
                except KeyError:
                    out.append(f"{kw}=??")
            print(" | ".join(out))


def dump(ch, only_src=None):
    my, pa, rows = load(ch)
    for sid, kws in rows:
        out = []
        for kw in [k.strip() for k in kws.split(", ")]:
            try:
                v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                if only_src and SRC.get((sid, kw)) not in only_src:
                    continue
                out.append(fmt(sid, kw, v, my[sid]))
            except KeyError:
                out.append(f"{kw}=??")
        if out:
            print(f"[{sid}] " + " | ".join(out))


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--only" in args:
        i = args.index("--only"); ONLY = set(args[i + 1].split(",")); del args[i:i + 2]
    if args and args[0] == "--seg":
        show(args[1:]); sys.exit()
    if args and args[0] == "--dump":
        dump(args[1], set(args[2].split(",")) if len(args) > 2 else None); sys.exit()
    if args and args[0] == "--report":
        table, unmapped, problems, summary = run(write=False)
        print(f"UNMAPPED keywords: {len(unmapped)} distinct, {sum(len(v) for v in unmapped.values())} uses")
        for kw, where in sorted(unmapped.items(), key=lambda x: (x[1][0][0], -len(x[1]))):
            print(f"  {kw}\t{len(where)}\t{where[0][1]}")
        print(f"presence problems: {len(problems)}")
        for ch, sid, kw, v in problems:
            print(f"  {sid}\t{kw} = {v}")
        sys.exit()
    table, unmapped, problems, summary = run(write=True)
    if unmapped or problems:
        print("UNMAPPED", len(unmapped), "PROBLEMS", problems[:20])
        sys.exit(1)
    ruled_all, results = [], []
    for ch, n, nne in summary:
        ln, bad, fails, punct, ruled = verify(ch)
        ruled_all += ruled
        results.append((ch, ln, bad, fails, punct, ruled, nne))
    write_table(table, ruled_all, results)
    for ch, ln, bad, fails, punct, ruled, nne in results:
        print(f"{ch}: lines {ln} | keyword preservation bad {bad} | presence failures {len(fails)} "
              f"(rule-matched chunks {len(ruled)}) | comma/၊// {punct} | no-equivalent {nne}")
        for f_ in fails:
            print("   FAIL", f_)
