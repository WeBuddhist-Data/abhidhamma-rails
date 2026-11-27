"""Pāli→Burmese keyword mapping for pi-1 (Dhammasaṅgaṇī), Rūpakaṇḍa chapters 3-01, 3-02, 3-03.

Copy of the approved sample mapper map_all.py (its tables, compose rules, context functions and verifier), with
the Rūpakaṇḍa table T_RUPA, the context functions f_rupa / f_rupam / f_rel / f_sukha / f_dukkha / f_bhedo, the
inflection variants (rule 12) and the multiword compose (rule 14). Writes only 3-0x-rupakandam.mapped.md and
map-table-3.md (the new rules 12-20 and the review table).

usage (python3 -I -X utf8):
  map_3.py               writes <ch>.mapped.md for every chapter in CHAPTERS and map-table-3.md, then verifies them
                         (keyword preservation, presence of every value chunk in its segment, no ", " / «၊» in a value)
  map_3.py --report    writes nothing; lists unmapped keywords and presence failures
  map_3.py --seg ID    prints Pāli, Burmese, keywords and mapping of one segment

Method (as the pi-1 Marathi mapper, brief burmese-mapper-brief.md): the Burmese is the FINAL text of this track
(AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters). No other Burmese source is used. Every keyword is
looked up in
  CTX[sid]       per-segment overrides (where the context changes the sense),
  T_<chapter>    the chapter's own table (keyword -> Burmese, dictionary form), then the tables of all chapters,
                 first letter case-insensitive; a value may be «@name» (a context function f(kw, pali, my)),
  compose()      «X dhammā» = T[X] + « သဘောတရား»; «no X dhammā» / «na X dhammā» = the negative attributive of T[X]
                 («…သော» -> «…သည် မဟုတ်သော», as the text builds it) + « သဘောတရား».
Adding a chapter: write its table T_<ch> (and CTX entries), register it in SECTIONS, add it to CHAPTERS.
The sample rules are in RULES (not rewritten here); the new rules are NEW_RULES (written to map-table-3.md).
"""
import re, sys, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-1_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")
NONE = "(no direct equivalent)"
DH = "သဘောတရား"


def low(w):
    return w[:1].lower() + w[1:]


# =====================================================================================================
# chapter tables
# =====================================================================================================
T_PREAMBLE = {
    "Abhidhamma": "အဘိဓမ္မာ",
    "Abhidhammapiṭake": "အဘိဓမ္မာပိဋက",
    "saṅgaṇī": "စုစည်းရေတွက်ခြင်း",
    "Dhammasaṅgaṇī": "သဘောတရားများကို စုစည်းရေတွက်ခြင်း",     # the book title, kept whole (rule 7)
    "Dhamma": DH,
    "Namo": "ရှိခိုးသည်",                                     # text «ရှိခိုးပါ၏» (rule 4)
    "bhagavato": "မြတ်စွာဘုရား",
    "arahato": "ရဟန္တာ",
    "sammā": "အပြည့်အဝ",
    "sambuddhassa": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်",
    "sammāsambuddhassa": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
}

T_MATIKA = {
    # --- headings, book frame
    "mātikā": "ခေါင်းစဉ်စာရင်း",
    "duka": "နှစ်မျိုးတွဲ",
    "dukaṃ": "နှစ်မျိုးတွဲ",
    "antara": "ကြားညှပ်",
    "antaradukaṃ": "ကြားညှပ် နှစ်မျိုးတွဲ",
    "piṭṭhi": "နောက်ဆုံး",
    "suttantika": "သုတ္တန်",
    "abhidhamma": "အဘိဓမ္မာ",
    "niṭṭhitā": "ပြီးဆုံးသော",                                  # text «ပြီးဆုံးပြီ» (rule 3)
    "dhammā": DH,
    # --- cluster nouns (nominative = the noun; «X ဖြစ်သော» = «that are X»: rule 2)
    "hetu": "အမြစ်", "hetū": "အမြစ်", "hetukā": "အမြစ်",
    "āsava": "စိတ်အစွန်းအထင်း", "āsavā": "စိတ်အစွန်းအထင်း",
    "saṃyojana": "နှောင်ကြိုး", "saṃyojanā": "နှောင်ကြိုး",
    "gantha": "အထုံး", "ganthā": "အထုံး",
    "ogha": "ရေအလျဉ်", "oghā": "ရေအလျဉ်",
    "yoga": "ထမ်းပိုး", "yogā": "ထမ်းပိုး",
    "nīvaraṇa": "အတားအဆီး", "nīvaraṇā": "အတားအဆီး",
    "parāmāsa": "မှားယွင်းသော ယူဆမှု", "parāmāsā": "မှားယွင်းသော ယူဆမှု",
    "upādāna": "စွဲလမ်းမှု", "upādānā": "စွဲလမ်းမှု",
    "kilesa": "ကိလေသာ", "kilesā": "ကိလေသာ",
    "citta": "စိတ်", "cittā": "စိတ်",
    "cetasikā": "စိတ်၏ အဖော်",
    "ārammaṇā": "အာရုံ",
    "adhipatino": "အကြီးအမှူး",
    "magga": "မဂ်",
    # --- triads
    "kusalā": "ကုသိုလ်", "akusalā": "အကုသိုလ်",
    "abyākatā": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "sampayuttā": "ယှဉ်တွဲသော", "vippayuttā": "ကင်းကွာသော",
    "vedanāya": "ခံစားမှု",
    "sukhāya": "သာယာသော", "sukhāya vedanāya": "သာယာသော ခံစားမှု",
    "dukkhāya": "နာကျင်သော", "dukkhāya vedanāya": "နာကျင်သော ခံစားမှု",
    "adukkhamasukhāya": "မနာကျင် မသာယာသော",
    "vipākadhamma": "အကျိုး ပေးတတ်သော",
    "vipākadhammadhammā": "အကျိုး ပေးတတ်သော သဘောတရား",
    "upādiṇṇa": "ကံကြောင့် ဖြစ်သော", "upādiṇṇā": "ကံကြောင့် ဖြစ်သော",
    "anupādiṇṇā": "ကံကြောင့် မဖြစ်သော",
    "upādāniyā": "စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော",
    "anupādāniyā": "စွဲလမ်းမှု၏ အာရုံ မဖြစ်နိုင်သော",
    "upādiṇṇupādāniyā": "ကံကြောင့် ဖြစ်၍ စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်သော",
    "anupādiṇṇupādāniyā": "ကံကြောင့် မဖြစ်သော်လည်း စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော",
    "anupādiṇṇaanupādāniyā": "ကံကြောင့်လည်း မဖြစ် စွဲလမ်းမှု၏ အာရုံလည်း မဖြစ်နိုင်သော",
    "saṃkiliṭṭha": "ကိလေသာဖြင့် ညစ်နွမ်းသော", "saṃkiliṭṭhā": "ကိလေသာဖြင့် ညစ်နွမ်းသော",
    "asaṃkiliṭṭha": "ကိလေသာဖြင့် မညစ်နွမ်းသော", "asaṃkiliṭṭhā": "ကိလေသာဖြင့် မညစ်နွမ်းသော",
    "saṃkilesikā": "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော",
    "asaṃkilesikā": "ကိလေသာ၏ အာရုံ မဖြစ်နိုင်သော",
    "vitakka": "စတင်ကြံစည်မှု", "vitakkā": "စတင်ကြံစည်မှု",
    "vicāra": "ဆက်လက်သုံးသပ်မှု", "vicārā": "ဆက်လက်သုံးသပ်မှု",
    "savitakkasavicārā": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော",
    "avitakkavicāramattā": "စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော",
    "savitakkā": "စတင်ကြံစည်မှု ရှိသော", "avitakkā": "စတင်ကြံစည်မှု မရှိသော",
    "savicārā": "ဆက်လက်သုံးသပ်မှု ရှိသော", "avicārā": "ဆက်လက်သုံးသပ်မှု မရှိသော",
    "pīti": "ပီတိ", "pītikā": "ပီတိ",
    "sappītikā": "ပီတိ ရှိသော", "appītikā": "ပီတိ မရှိသော",
    "sukha": "သာယာမှု", "upekkhā": "ဥပေက္ခာ",
    "sahagatā": "အတူ ဖြစ်သော",
    "pītisahagatā": "ပီတိနှင့်အတူ ဖြစ်သော",
    "sukhasahagatā": "သာယာမှုနှင့်အတူ ဖြစ်သော",
    "upekkhāsahagatā": "ဥပေက္ခာနှင့်အတူ ဖြစ်သော",
    "dassanena": "သစ္စာကို မြင်ခြင်း",
    "pahātabbā": "ပယ်ရမည့်", "pahātabba": "ပယ်ရမည့်",
    "bhāvanāya pahātabbā": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့်",
    "bhāvanāya pahātabba": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့်",
    "hetukā dhammā": "အမြစ် ရှိသော သဘောတရား",
    "ācaya": "စုပုံခြင်း", "apacaya": "လျော့ပါးခြင်း",
    "gāmino dhammā": "ဦးတည်သော သဘောတရား",
    "sekkhā": "ကျင့်ကြံဆဲသူ၏", "asekkhā": "ကျင့်ကြံမှု ပြီးဆုံးသူ၏",
    "parittā": "အကန့်အသတ် ရှိသော", "mahaggatā": "ကြီးမြတ်သော", "appamāṇā": "အတိုင်းအဆ မရှိသော",
    "paritta": "အကန့်အသတ် ရှိသော", "mahaggata": "ကြီးမြတ်သော", "appamāṇa": "အတိုင်းအဆ မရှိသော",   # text «… သည်ကို» (rule 3)
    "parittārammaṇā": "အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော",
    "mahaggatārammaṇā": "ကြီးမြတ်သည်ကို အာရုံပြုသော",
    "appamāṇārammaṇā": "အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော",
    "hīnā": "ယုတ်ညံ့သော", "majjhimā": "အလယ်အလတ်", "paṇītā": "မွန်မြတ်သော",
    "micchatta": "မှားယွင်းမှု", "sammatta": "မှန်ကန်မှု", "niyatā": "ကျိန်းသေသော",
    "uppannā": "ဖြစ်ပေါ်ပြီးသော", "uppādino": "ဖြစ်ပေါ်လာမည့်",
    "atītā": "အတိတ်", "anāgatā": "အနာဂတ်", "paccuppannā": "ပစ္စုပ္ပန်",
    "atītārammaṇā": "အတိတ်ကို အာရုံပြုသော",
    "anāgatārammaṇā": "အနာဂတ်ကို အာရုံပြုသော",
    "paccuppannārammaṇā": "ပစ္စုပ္ပန်ကို အာရုံပြုသော",
    "bahiddhā": "သူတစ်ပါး၌",
    "bahiddhā dhammā": "သူတစ်ပါး၌ ရှိသော သဘောတရား",
    "sanidassana": "မြင်နိုင်သော", "anidassana": "မမြင်နိုင်သော",
    "sanidassanā": "မြင်နိုင်သော", "anidassanā": "မမြင်နိုင်သော",
    "sappaṭighā": "ထိခိုက်မှု ရှိသော",
    # --- Abhidhamma dyads
    "sahetukā": "အမြစ် ရှိသော", "ahetukā": "အမြစ် မရှိသော",
    "appaccayā": "အကြောင်း မရှိသော",
    "saṅkhatā": "ပြုပြင်ဖန်တီးထားသော", "asaṅkhatā": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော",
    "rūpino": "ရုပ် ဖြစ်သော", "arūpino": "ရုပ် မဟုတ်သော",
    "lokiyā": "လောကနှင့် သက်ဆိုင်သော", "lokuttarā": "လောကကို ကျော်လွန်သော", "uttarā": "ကျော်လွန်သော",
    "na": "မ",                                                     # text «မသိနိုင်သော» (rule 9)
    "viññeyyā": "သိနိုင်သော",
    "sāsavā": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော",
    "anāsavā": "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော",
    "āsavavippayuttā": "စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော",
    "saṃyojaniyā": "နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော",
    "asaṃyojaniyā": "နှောင်ကြိုး၏ အာရုံ မဖြစ်နိုင်သော",
    "saṃyojanavippayuttā": "နှောင်ကြိုးနှင့် ကင်းကွာသော",
    "ganthaniyā": "အထုံး၏ အာရုံ ဖြစ်နိုင်သော",
    "aganthaniyā": "အထုံး၏ အာရုံ မဖြစ်နိုင်သော",
    "ganthavippayuttā": "အထုံးနှင့် ကင်းကွာသော",
    "oghaniyā": "ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်သော",
    "anoghaniyā": "ရေအလျဉ်၏ အာရုံ မဖြစ်နိုင်သော",
    "yoganiyā": "ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်သော",
    "ayoganiyā": "ထမ်းပိုး၏ အာရုံ မဖြစ်နိုင်သော",
    "nīvaraṇiyā": "အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော",
    "anīvaraṇiyā": "အတားအဆီး၏ အာရုံ မဖြစ်နိုင်သော",
    "nīvaraṇavippayuttā": "အတားအဆီးနှင့် ကင်းကွာသော",
    "parāmaṭṭhā": "မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော",
    "parāmāsavippayuttā": "မှားယွင်းသော ယူဆမှုနှင့် ကင်းကွာသော",
    "upādānavippayuttā": "စွဲလမ်းမှုနှင့် ကင်းကွာသော",
    "kilesavippayuttā": "ကိလေသာနှင့် ကင်းကွာသော",
    "cittavippayuttā": "စိတ်နှင့် ကင်းကွာသော",
    "saṃsaṭṭha": "ရောနှောသော", "saṃsaṭṭhā": "ရောနှောသော", "visaṃsaṭṭhā": "မရောနှောသော",
    "cittasaṃsaṭṭhā": "စိတ်နှင့် ရောနှောသော",
    "samuṭṭhāna": "ဖြစ်ပေါ်လာသော", "samuṭṭhānā": "ဖြစ်ပေါ်လာသော",
    "cittasamuṭṭhānā": "စိတ်မှ ဖြစ်ပေါ်လာသော",
    "sahabhuno": "အတူ တည်ရှိသော",
    "cittasahabhuno": "စိတ်နှင့်အတူ တည်ရှိသော",
    "anuparivattino": "နောက်သို့ လိုက်ပါသော",
    "cittānuparivattino": "စိတ်နောက်သို့ လိုက်ပါသော",
    "cittasaṃsaṭṭhasamuṭṭhānā": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော",
    "saṃsaṭṭhasamuṭṭhānā": "ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာသော",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhuno": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသော",
    "saṃsaṭṭhasamuṭṭhānasahabhuno": "ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နှင့်အတူ တည်ရှိသော",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino": "စိတ်နှင့် ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော",
    "saṃsaṭṭhasamuṭṭhānānuparivattino": "ရောနှော၍ စိတ်မှ ဖြစ်ပေါ်လာပြီး စိတ်နောက်သို့ လိုက်ပါသော",
    "ajjhattikā": "အတွင်းပိုင်း", "bāhirā": "ပြင်ပ",
    "upādā": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော",
    "kāma": "ကာမ", "rūpa": "@rupa", "arūpa": "ရုပ်မရှိသော",
    "avacarā": "ဘုံနှင့် ဆိုင်သော",
    "kāmāvacarā": "ကာမဘုံနှင့် ဆိုင်သော",
    "rūpāvacarā": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော",
    "arūpāvacarā": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော",
    "pariyāpannā": "ဘဝဘုံတို့၌ အကျုံးဝင်သော", "apariyāpannā": "ဘဝဘုံတို့၌ အကျုံးမဝင်သော",
    "niyyānikā": "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော",
    "sauttarā": "ထိုထက် သာလွန်သည် ရှိသေးသော", "anuttarā": "ထိုထက် သာလွန်သည် မရှိသော",
    "raṇā": "ပဋိပက္ခ", "saraṇā": "ပဋိပက္ခ ရှိသော", "araṇā": "ပဋိပက္ခ မရှိသော",
    # --- Suttanta dyads
    "vijjā": "အမှန်သိမြင်မှု", "avijjā": "အမှန်ကို မသိမှု",
    "bhāgino dhammā": "အစိတ်အပိုင်း ဖြစ်သော သဘောတရား",
    "vijju": "လျှပ်စီး", "vajira": "စိန်", "upamā": "တူသော",
    "vijjūpamā": "လျှပ်စီးနှင့် တူသော",
    "bālā": "မိုက်မဲသော", "paṇḍitā": "ပညာရှိသော",
    "kaṇhā": "မည်းနက်သော", "sukkā": "ဖြူစင်သော",
    "tapanīyā": "ပူပန်စေတတ်သော",
    "adhivacanā": "အမည်ခေါ်ဝေါ်မှု", "nirutti": "စကားဖြင့် ဖော်ပြမှု", "paññatti": "သတ်မှတ်ချက်",
    "pathā": "လမ်းကြောင်း",
    "nāmañca": "စိတ်ပိုင်း", "rūpañca": "ရုပ်ပိုင်း",
    "bhava": "ဘဝ", "taṇhā": "တပ်မက်မှု", "vibhava": "ဘဝ ပျောက်ကွယ်သည်",
    "diṭṭhi": "အယူ",
    "sassata": "ထာဝရ တည်မြဲသည်", "uccheda": "သေပြီးနောက် ပြတ်စဲသွားသည်",
    "sassatadiṭṭhi": "အတ္တသည် ထာဝရ တည်မြဲသည်ဟူသော အယူ",
    "ucchedadiṭṭhi": "အတ္တသည် သေပြီးနောက် ပြတ်စဲသွားသည်ဟူသော အယူ",
    "anudiṭṭhi": "ပတ်သက်သော အယူ",
    "ahirikañca": "ဒုစရိုက်ကို မရှက်မှု", "anottappañca": "ဒုစရိုက်ကို မကြောက်ရွံ့မှု",
    "hirī": "ဒုစရိုက်ကို ရှက်မှု", "ottappañca": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု",
    "dovacassatā": "သွန်သင်ချက်ကို နားမထောင်ခြင်း",
    "sovacassatā": "သွန်သင်ချက်ကို နားထောင်ခြင်း",
    "vacassatā": "သွန်သင်ချက်ကို နားထောင်ခြင်း",              # also from dovacassatā (rule 8)
    "pāpa": "ဆိုး",
    "mittatā": "မိတ်ဆွေ … ပေါင်းသင်းခြင်း",
    "āpatti": "အပြစ်", "vuṭṭhāna": "ထမြောက်ရာ", "kusalatā": "ကျွမ်းကျင်ခြင်း",
    "vuṭṭhānakusalatā": "ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း",
    "samāpatti": "ဈာန် ဝင်စားရာ",
    "dhātu": "ဓာတ်", "manasikāra": "နှလုံးသွင်းခြင်း",
    "manasikārakusalatā": "နှလုံးသွင်းခြင်း၌ ကျွမ်းကျင်ခြင်း",
    "āyatana": "အာရုံခံ နယ်ပယ်",
    "paṭicca": "အကြောင်းအကျိုး ဆက်စပ်", "samuppāda": "ဖြစ်ပေါ်ပုံ",
    "aṭṭhāna": "မဖြစ်နိုင်သည့်အရာ",
    "ajjavo": "ဖြောင့်မတ်ခြင်း", "maddavo": "နူးညံ့ခြင်း",
    "khanti": "သည်းခံခြင်း", "soraccañca": "ယဉ်ကျေးခြင်း",
    "sākhalyañca": "စကား ချိုသာခြင်း", "paṭisanthāro": "ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း",
    "indriyesu": "အာရုံခံ အင်္ဂါ", "dvāratā": "တံခါး", "gutta": "စောင့်ထိန်းသော",
    "bhojane": "အစားအစာ", "mattaññutā": "အတိုင်းအရှည်ကို သိခြင်း",
    "muṭṭhasaccañca": "သတိလစ်ခြင်း",
    "sampajaññañca": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း",
    "asampajaññañca": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိခြင်း",
    "sati": "သတိ",
    "paṭisaṅkhāna": "ပြန်လည် စဉ်းစားခြင်း", "balañca": "စွမ်းအား",
    "samatho": "စိတ်ငြိမ်သက်ခြင်း", "samatha": "စိတ်ငြိမ်သက်ခြင်း", "vipassanā": "ထိုးထွင်းသိမြင်ခြင်း",
    "paggāho": "စိတ်ကို မြှင့်တင်ခြင်း", "paggāha": "စိတ်ကို မြှင့်တင်ခြင်း",
    "nimittañca": "အမှတ်အသား",
    "avikkhepo": "စိတ် မပျံ့လွင့်ခြင်း",
    "sīla": "သီလ", "vipatti": "ပျက်စီးခြင်း", "sampadā": "ပြည့်စုံခြင်း", "visuddhi": "စင်ကြယ်ခြင်း",
    "yathā": "လျော်ညီသော",                                       # text «လျော်ညီသူ၏» (rule 3)
    "padhānaṃ": "ကြိုးပမ်းအားထုတ်ခြင်း", "padhānasmiṃ": "ကြိုးပမ်းအားထုတ်ခြင်း",
    "saṃvego": "သံဝေဂ ရခြင်း", "saṃvejaniyesu": "သံဝေဂ ရဖွယ်", "ṭhānesu": "အခြေအနေ",
    "saṃviggassa": "သံဝေဂ ရသော",                                 # text «သံဝေဂ ရသူ၏» (rule 3)
    "yoniso": "သင့်လျော်စွာ",
    "santuṭṭhitā": "ရောင့်ရဲမှု",
    "kusalesu": "ကုသိုလ်", "kusalesu dhammesu": "ကုသိုလ် သဘောတရား",
    "vimutti": "လွတ်မြောက်မှု",
    "khaye": "ကုန်ခန်းခြင်း", "anuppāde": "နောက်ထပ် မဖြစ်ပေါ်ခြင်း", "ñāṇaṃ": "ဉာဏ်",
}


# =====================================================================================================
# Rūpakaṇḍa (3-01, 3-02, 3-03): one table for the three chapters (T_RUPA, looked up before the sample tables),
# plus per-chapter tables for what differs.  Values from the FINAL Burmese of these chapters.
# =====================================================================================================
NOEQ = NONE
T_RUPA = {
    # --- headings, frame
    "kaṇḍaṃ": "အခန်း", "kaṇḍe": "အခန်း", "Rūpa": "ရုပ်",
    "Uddeso": "အကျဉ်း ဖော်ပြချက်", "niddeso": "အကျယ် ဖော်ပြချက်", "vibhatti": "ခွဲခြား ဖော်ပြချက်",
    "bhājanīyaṃ": "ခွဲခြမ်း ဖော်ပြချက်",
    "Dasakaṃ": "ဆယ်မျိုးတွဲ", "Ekādasakaṃ": "ဆယ့်တစ်မျိုးတွဲ", "Dukaṃ": "နှစ်မျိုးတွဲ", "Duka": "နှစ်မျိုးတွဲ",
    "Dasa": "ဆယ်", "dasa": "ဆယ်", "Ekādasa": "ဆယ့်တစ်", "ekādasa": "ဆယ့်တစ်", "Aṭṭhama": "အဋ္ဌမ",
    "Catubbidhena": "လေးမျိုး", "Chabbidhena": "ခြောက်မျိုး", "vidhena": "မျိုး",
    "saṅgaho": "စုစည်းခြင်း", "rūpasaṅgaho": "ရုပ်ကို … စုစည်းခြင်း",
    "bhāṇa": "ရွတ်ဖတ်ရန်", "vāro": "အပိုင်း",
    "Tattha": "ထိုတို့အနက်",
    # relative pronouns: Burmese builds a relative clause, no word (rule 15)
    "yaṃ": "@rel", "Yaṃ": "@rel", "yo": "@rel", "Yo": "@rel", "Yā": "@rel", "yā": "@rel",
    "eva": "ပင်",
    # --- 1-583 (abyākata), khandhas
    "khandho": "အစုအဝေး",
    "viññāṇakkhandho": "သိစိတ် အစုအဝေး", "vedanākkhandho": "ခံစားမှု အစုအဝေး",
    "saṅkhārakkhandho": "ပြုပြင်ဖန်တီးမှု အစုအဝေး", "saññākkhandho": "မှတ်သိမှု အစုအဝေး",
    "viññāṇa": "သိစိတ်", "vedanā": "ခံစားမှု", "saññā": "မှတ်သိမှု", "saṅkhāra": "ပြုပြင်ဖန်တီးမှု",
    "cetanā": "စေ့ဆော်မှု", "saññāya": "မှတ်သိမှု", "cetanāya": "စေ့ဆော်မှု",
    "kiriyā": "ပြုရုံမျှသာ ဖြစ်သော",
    "dhammā abyākatā": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား",
    "asaṅkhatā ca dhātu": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော ဓာတ်",
    "akusalānaṃ": "အကုသိုလ်", "akusalānaṃ dhammānaṃ": "အကုသိုလ် သဘောတရား",
    "Kusala": "ကုသိုလ်", "kusala": "ကုသိုလ်", "akusala": "အကုသိုလ်",
    "kusalā nākusalā": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်",
    "abyākata": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "kusalacittassa": "ကုသိုလ်စိတ်", "akusalacittassa": "အကုသိုလ်စိတ်", "cittassa": "စိတ်",
    # --- 1-584 / 1-594 (ekaka): the Mātikā terms, neuter (normalised to the Mātikā keys), plus
    "jarā": "အိုခြင်း", "abhibhūtaṃ": "လွှမ်းမိုးခံရသော", "aniccaṃ": "မမြဲသော",
    "viññāṇehi": "သိစိတ်", "upādāya": "မှီ၍", "upādāya rūpaṃ": "မှီ၍ ဖြစ်သော ရုပ်",
    "bhūtā": "မူလဓာတ်", "bhūtaṃ": "မူလဓာတ်", "bhūtānaṃ": "မူလဓာတ်", "bhūtehi": "မူလဓာတ်",
    "mahābhūtā": "မူလဓာတ်ကြီး", "mahābhūtaṃ": "မူလဓာတ်ကြီး", "mahābhūtānaṃ": "မူလဓာတ်ကြီး",
    "mahābhūtehi": "မူလဓာတ်ကြီး",
    "cetasikaṃ": "စိတ်၏ အဖော်", "āsavaṃ": "စိတ်အစွန်းအထင်း", "sekkha": "ကျင့်ကြံဆဲသူ၏",
    "asekkhaṃ": "ကျင့်ကြံမှု ပြီးဆုံးသူ၏", "gāmi": "ဦးတည်သော", "hetukaṃ": "အမြစ်", "ārammaṇaṃ": "အာရုံ",
    "ārammaṇo": "အာရုံ",
    "rūpaṃ": "@rupam", "rūpa": "@rupa",
    # --- sense organs, objects, bases, elements
    "cakkhu": "မျက်စိ", "Cakkhu": "မျက်စိ", "cakkhuṃ": "မျက်စိ", "cakkhunā": "မျက်စိ", "cakkhumhi": "မျက်စိ",
    "sota": "နား", "Sota": "နား", "sotaṃ": "နား", "sotena": "နား", "sotamhi": "နား",
    "ghāna": "နှာခေါင်း", "ghānaṃ": "နှာခေါင်း", "ghānena": "နှာခေါင်း", "ghānamhi": "နှာခေါင်း",
    "jivhā": "လျှာ", "jivhaṃ": "လျှာ", "jivhāya": "လျှာ",
    "kāya": "ကိုယ်", "Kāya": "ကိုယ်", "kāyo": "ကိုယ်", "kāyaṃ": "ကိုယ်", "kāyena": "ကိုယ်", "kāyamhi": "ကိုယ်",
    "kāyassa": "ကိုယ်", "mano": "မနော", "manasā": "မနော",
    "sadda": "အသံ", "Sadda": "အသံ", "saddo": "အသံ", "saddaṃ": "အသံ", "saddamhi": "အသံ",
    "gandha": "အနံ့", "gandho": "အနံ့", "gandhaṃ": "အနံ့", "gandhamhi": "အနံ့",
    "rasa": "အရသာ", "raso": "အရသာ", "rasaṃ": "အရသာ", "rasamhi": "အရသာ",
    "phoṭṭhabba": "အထိအတွေ့", "Phoṭṭhabba": "အထိအတွေ့", "phoṭṭhabbaṃ": "အထိအတွေ့", "phoṭṭhabbo": "အထိအတွေ့",
    "phoṭṭhabbamhi": "အထိအတွေ့",
    "rūpamhi": "အဆင်းအရောင်",
    "dhamma": DH, "dhammāyatana": "သဘောတရား အာရုံခံ နယ်ပယ်",
    "cakkhāyatanaṃ": "မျက်စိ အာရုံခံ နယ်ပယ်", "sotāyatanaṃ": "နား အာရုံခံ နယ်ပယ်",
    "ghānāyatanaṃ": "နှာခေါင်း အာရုံခံ နယ်ပယ်", "jivhāyatanaṃ": "လျှာ အာရုံခံ နယ်ပယ်",
    "kāyāyatanaṃ": "ကိုယ် အာရုံခံ နယ်ပယ်", "rūpāyatanaṃ": "အဆင်းအရောင် အာရုံခံ နယ်ပယ်",
    "saddāyatanaṃ": "အသံ အာရုံခံ နယ်ပယ်", "gandhāyatanaṃ": "အနံ့ အာရုံခံ နယ်ပယ်",
    "rasāyatanaṃ": "အရသာ အာရုံခံ နယ်ပယ်", "phoṭṭhabbāyatanaṃ": "အထိအတွေ့ အာရုံခံ နယ်ပယ်",
    "āyatanānaṃ": "အာရုံခံ နယ်ပယ်",
    "cakkhudhātu": "မျက်စိ ဓာတ်", "sotadhātu": "နား ဓာတ်", "ghānadhātu": "နှာခေါင်း ဓာတ်",
    "jivhādhātu": "လျှာ ဓာတ်", "kāyadhātu": "ကိုယ် ဓာတ်", "rūpadhātu": "အဆင်းအရောင် ဓာတ်",
    "saddadhātu": "အသံ ဓာတ်", "gandhadhātu": "အနံ့ ဓာတ်", "rasadhātu": "အရသာ ဓာတ်",
    "phoṭṭhabbadhātu": "အထိအတွေ့ ဓာတ်",
    "manodhātu": "မနော ဓာတ်", "manoviññāṇa": "မနော သိစိတ်", "manoviññāṇadhātu": "မနော သိစိတ် ဓာတ်",
    "cakkhuviññāṇassa": "မျက်စိ သိစိတ်", "kāyaviññāṇassa": "ကိုယ် သိစိတ်",
    "cakkhuviññāṇaṃ": "မျက်စိ သိစိတ်", "sotaviññāṇaṃ": "နား သိစိတ်", "ghānaviññāṇaṃ": "နှာခေါင်း သိစိတ်",
    "jivhāviññāṇaṃ": "လျှာ သိစိတ်", "kāyaviññāṇaṃ": "ကိုယ် သိစိတ်",
    "cakkhusamphassassa": "မျက်စိ၏ တွေ့ထိမှု", "sotasamphassassa": "နား၏ တွေ့ထိမှု",
    "ghānasamphassassa": "နှာခေါင်း၏ တွေ့ထိမှု", "jivhāsamphassassa": "လျှာ၏ တွေ့ထိမှု",
    "kāyasamphassassa": "ကိုယ်၏ တွေ့ထိမှု",
    "cakkhusamphasso": "မျက်စိ၏ တွေ့ထိမှု", "sotasamphasso": "နား၏ တွေ့ထိမှု",
    "ghānasamphasso": "နှာခေါင်း၏ တွေ့ထိမှု", "jivhāsamphasso": "လျှာ၏ တွေ့ထိမှု",
    "kāyasamphasso": "ကိုယ်၏ တွေ့ထိမှု",
    "samphassajāya": "တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "samphassajāya vedanāya": "တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု",
    "cakkhusamphassajāya": "မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "kāyasamphassajāya": "ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "cakkhusamphassajāya vedanāya": "မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု",
    "kāyasamphassajāya vedanāya": "ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု",
    "cakkhusamphassajā": "မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော", "sotasamphassajā": "နား၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "ghānasamphassajā": "နှာခေါင်း၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "jivhāsamphassajā": "လျှာ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော", "kāyasamphassajā": "ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "cakkhusamphassajā vedanā": "မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု",
    "sotasamphassajā vedanā": "နား၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု",
    "ghānasamphassajā vedanā": "နှာခေါင်း၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု",
    "jivhāsamphassajā vedanā": "လျှာ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု",
    "kāyasamphassajā vedanā": "ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော ခံစားမှု",
    "nissāya": "မှီ၍", "cakkhuṃ nissāya": "မျက်စိကို မှီ၍", "sotaṃ nissāya": "နားကို မှီ၍",
    "ghānaṃ nissāya": "နှာခေါင်းကို မှီ၍", "jivhaṃ nissāya": "လျှာကို မှီ၍", "kāyaṃ nissāya": "ကိုယ်ကို မှီ၍",
    "viññeyyaṃ rūpaṃ": "သိနိုင်သော ရုပ်",
    "āyatanaṃ cakkhuviññeyyaṃ rūpaṃ": "အာရုံခံ နယ်ပယ်သည် မျက်စိဖြင့် သိနိုင်သော ရုပ်",
    "āyatanaṃ manodhātuviññeyyaṃ rūpaṃ": "အာရုံခံ နယ်ပယ်တို့သည် မနော ဓာတ်ဖြင့် သိနိုင်သော ရုပ်",
    "rūpaṃ manoviññeyyaṃ rūpaṃ": "ရုပ် … မနောဖြင့် သိနိုင်သော ရုပ်",
    "rūpaṃ manoviññāṇadhātuviññeyyaṃ rūpaṃ": "ရုပ် … မနော သိစိတ် ဓာတ်ဖြင့် သိနိုင်သော ရုပ်",
    "viññātaṃ": "သိရသော", "sutaṃ": "ကြားရသော", "mutaṃ": "နမ်း မြည်း ထိတွေ့ရသော",
    "viññātaṃ rūpaṃ": "သိရသော ရုပ်",
    # --- faculties, intimation, space, water, qualities of matter, food
    "indriyaṃ": "စွမ်းရည်", "indriyānaṃ": "စွမ်းရည်",
    "itthi": "မိန်းမ", "Itthi": "မိန်းမ", "itthiyā": "မိန်းမ",
    "purisa": "ယောက်ျား", "purisassa": "ယောက်ျား", "jīvita": "အသက်",
    "itthindriyaṃ": "မိန်းမ၏ စွမ်းရည်", "Itthindriyaṃ": "မိန်းမ၏ စွမ်းရည်",
    "purisindriyaṃ": "ယောက်ျား၏ စွမ်းရည်", "jīvitindriyaṃ": "အသက်၏ စွမ်းရည်",
    "viññatti": "ထုတ်ဖော်ပြသမှု", "vacī": "နှုတ်",
    "kāyaviññatti": "ကိုယ်ဖြင့် ထုတ်ဖော်ပြသမှု", "Kāyaviññatti": "ကိုယ်ဖြင့် ထုတ်ဖော်ပြသမှု",
    "vacīviññatti": "နှုတ်ဖြင့် ထုတ်ဖော်ပြသမှု",
    "ākāsa": "ဟင်းလင်းပြင်", "ākāsadhātu": "ဟင်းလင်းပြင် ဓာတ်",
    "āpo": "ရေ", "Āpo": "ရေ", "āpodhātu": "ရေဓာတ်", "Āpodhātu": "ရေဓာတ်",
    "Pathavī": "မြေ", "pathavī": "မြေ", "Pathavīdhātu": "မြေဓာတ်", "pathavīdhātu": "မြေဓာတ်",
    "tejo": "မီး", "tejodhātu": "မီးဓာတ်", "vāyo": "လေ", "vāyodhātu": "လေဓာတ်",
    "lahutā": "ပေါ့ပါးခြင်း", "mudutā": "ပျော့ပျောင်းခြင်း", "kammaññatā": "အသုံးပြုရန် သင့်တော်ခြင်း",
    "upacayo": "တိုးပွားခြင်း", "santati": "ဆက်လက်ဖြစ်ပေါ်ခြင်း", "jaratā": "အိုမင်းခြင်း",
    "aniccatā": "မမြဲခြင်း",
    "rūpassa lahutā": "ရုပ်၏ ပေါ့ပါးခြင်း", "rūpassa mudutā": "ရုပ်၏ ပျော့ပျောင်းခြင်း",
    "rūpassa kammaññatā": "ရုပ်၏ အသုံးပြုရန် သင့်တော်ခြင်း", "rūpassa upacayo": "ရုပ်၏ တိုးပွားခြင်း",
    "rūpassa santati": "ရုပ်၏ ဆက်လက်ဖြစ်ပေါ်ခြင်း", "rūpassa jaratā": "ရုပ်၏ အိုမင်းခြင်း",
    "rūpassa aniccatā": "ရုပ်၏ မမြဲခြင်း",
    "rūpassa na lahutā": "ရုပ်၏ ပေါ့ပါးခြင်း မဟုတ်သော", "rūpassa na mudutā": "ရုပ်၏ ပျော့ပျောင်းခြင်း မဟုတ်သော",
    "rūpassa na kammaññatā": "ရုပ်၏ အသုံးပြုရန် သင့်တော်ခြင်း မဟုတ်သော",
    "rūpassa na upacayo": "ရုပ်၏ တိုးပွားခြင်း မဟုတ်သော",
    "rūpassa na santati": "ရုပ်၏ ဆက်လက်ဖြစ်ပေါ်ခြင်း မဟုတ်သော",
    "rūpassa na jaratā": "ရုပ်၏ အိုမင်းခြင်း မဟုတ်သော", "rūpassa na aniccatā": "ရုပ်၏ မမြဲခြင်း မဟုတ်သော",
    "kabaḷīkāro": "လုတ်ပြု၍ စားရသော", "āhāro": "အာဟာရ", "kabaḷīkāro āhāro": "လုတ်ပြု၍ စားရသော အာဟာရ",
    "oḷārikaṃ": "ရုန့်ရင်းသော", "sukhumaṃ": "နုညံ့သော",
    "cittasahabhu": "စိတ်နှင့်အတူ တည်ရှိသော", "anuparivatti": "နောက်သို့ လိုက်ပါသော",
    "cittānuparivatti": "စိတ်နောက်သို့ လိုက်ပါသော", "samuṭṭhānaṃ": "ဖြစ်ပေါ်လာသော",
    "cittajaṃ": "စိတ်မှ မွေးဖွားသော",
    "rūpaṃ cittānuparivatti": "စိတ်နောက်သို့ လိုက်ပါသော ရုပ်",
    "rūpaṃ cittasamuṭṭhānaṃ": "စိတ်မှ ဖြစ်ပေါ်လာသော ရုပ်",
    "rūpaṃ cittasahabhu": "စိတ်နှင့်အတူ တည်ရှိသော ရုပ်",
    "rūpaṃ sappaṭighaṃ": "ထိခိုက်မှု ရှိသော ရုပ်",
    "bāhiraṃ sappaṭighaṃ": "ပြင်ပ ဖြစ်သော ထိခိုက်မှု ရှိသော", "bāhiraṃ appaṭighaṃ": "ပြင်ပ ဖြစ်သော ထိခိုက်မှု မရှိသော", "rūpaṃ appaṭighaṃ": "ထိခိုက်မှု မရှိသော ရုပ်",
    "appaṭighaṃ": "ထိခိုက်မှု မရှိသော",
    "anidassanaappaṭighaṃ": "မမြင်နိုင် ထိခိုက်မှုလည်း မရှိသော",
    "anidassanasappaṭighaṃ": "မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော",
    "kammassa": "ကံ", "Kammassa": "ကံ",
    "kammassa katattā": "ပြုခဲ့သော ကံကြောင့်", "Kammassa katattā": "ပြုခဲ့သော ကံကြောင့်",
    # --- the sense-organ definitions (1-596 ff.)
    "pasādo": "အာရုံခံ ကြည်လင်မှု", "upādāya pasādo": "မှီ၍ ဖြစ်သော အာရုံခံ ကြည်လင်မှု",
    "attabhāva": "မိမိ ကိုယ်ခန္ဓာ",
    "dvārā": "တံခါး", "samuddo": "သမုဒ္ဒရာ", "paṇḍaraṃ": "ကြည်လင်သောအရာ", "khettaṃ": "လယ်ကွင်း",
    "nettaṃ": "လမ်းပြ", "nayanaṃ": "ခေါင်းဆောင်", "tīraṃ": "ကမ်း",
    "suñño": "ဆိတ်သုဉ်းသော", "gāmo": "ရွာ", "suñño gāmo": "ဆိတ်သုဉ်းသော ရွာ",
    "uppajji": "ဖြစ်ပေါ်ခဲ့သည်", "uppajjati": "ဖြစ်ပေါ်သည်", "uppajjissati": "ဖြစ်ပေါ်လိမ့်မည်",
    "paṭihaññi": "ထိခိုက်ခဲ့သည်", "paṭihaññati": "ထိခိုက်သည်", "paṭihaññissati": "ထိခိုက်လိမ့်မည်",
    "suṇi": "ကြားခဲ့သည်", "suṇāti": "ကြားသည်", "suṇissati": "ကြားလိမ့်မည်",
    "ghāyi": "နမ်းခဲ့သည်", "ghāyati": "နမ်းသည်", "ghāyissati": "နမ်းလိမ့်မည်",
    "sāyi": "မြည်းခဲ့သည်", "sāyati": "မြည်းသည်", "sāyissati": "မြည်းလိမ့်မည်",
    "phusi": "ထိခဲ့သည်", "phusati": "ထိသည်", "phusissati": "ထိလိမ့်မည်",
    "sappaṭighaṃ paṭihaññi": "ထိခိုက်မှု ရှိသော … ထိခိုက်ခဲ့သည်",
    "sappaṭigho paṭihaññi": "ထိခိုက်မှု ရှိသော … ထိခိုက်ခဲ့သည်",
    # --- visible object (1-616)
    "vaṇṇa": "အရောင်", "nibhā": "အသွေး", "vaṇṇanibhā": "အရောင်အသွေး",
    "upādāya vaṇṇanibhā": "မှီ၍ ဖြစ်သော အရောင်အသွေး",
    "maṇisaṅkhamuttāveḷuriyassa vaṇṇanibhā": "ကျောက်မျက် ခရုသင်း ပုလဲ ကြောင်မျက်ရွဲတို့၏ အရောင်အသွေး",
    "jātarūparajatassa vaṇṇanibhā": "ရွှေ ငွေတို့၏ အရောင်အသွေး",
    "maṇi": "ကျောက်မျက်", "saṅkha": "ခရုသင်း", "muttā": "ပုလဲ", "veḷuriyassa": "ကြောင်မျက်ရွဲ",
    "rajatassa": "ငွေ",
    "nīlaṃ": "အပြာ", "pītakaṃ": "အဝါ", "lohitakaṃ": "အနီ", "odātaṃ": "အဖြူ", "kāḷakaṃ": "အမည်း",
    "mañjiṭṭhakaṃ": "ကြက်သွေးရောင်", "hari": "အစိမ်း", "harivaṇṇaṃ": "အစိမ်းနှင့် တူသော အရောင်",
    "amba": "သရက်", "aṅkura": "ညွန့်", "ambaṅkuravaṇṇaṃ": "သရက်ညွန့် အရောင်",
    "vaṭṭaṃ": "အဝိုင်း", "parimaṇḍalaṃ": "စက်ဝိုင်းပုံ", "caturaṃsaṃ": "လေးထောင့်ပုံ",
    "chaḷaṃsaṃ": "ခြောက်ထောင့်ပုံ", "aṭṭhaṃsaṃ": "ရှစ်ထောင့်ပုံ", "soḷasaṃsaṃ": "ဆယ့်ခြောက်ထောင့်ပုံ",
    "chāyā": "အရိပ်", "ātapo": "နေရောင်", "āloko": "အလင်း", "andhakāro": "အမှောင်",
    "abbhā": "တိမ်", "mahikā": "မြူ", "dhūmo": "မီးခိုး", "rajo": "ဖုန်",
    "canda": "လ", "sūriya": "နေ", "maṇḍalassa": "ဝန်း", "tārakarūpānaṃ": "ကြယ်", "ādāsa": "မှန်",
    "sanidassanaṃ sappaṭighaṃ": "မြင်နိုင်သော ထိခိုက်မှု ရှိသော",
    "anidassanaṃ sappaṭighaṃ": "မမြင်နိုင်သော ထိခိုက်မှု ရှိသော",
    "anidassano sappaṭigho": "မမြင်နိုင်သော ထိခိုက်မှု ရှိသော",
    "anidassanena sappaṭighena": "မမြင်နိုင်သော ထိခိုက်မှု ရှိသော",
    "anidassanamhi sappaṭighamhi": "မမြင်နိုင်သော ထိခိုက်မှု ရှိသော",
    # --- sound (1-620)
    "bheri": "စည်ကြီး", "bherisaddo": "စည်ကြီးသံ", "mudiṅga": "ဗုံ", "mudiṅgasaddo": "ဗုံသံ",
    "saṅkhasaddo": "ခရုသင်းသံ", "paṇava": "စည်ငယ်", "paṇavasaddo": "စည်ငယ်သံ",
    "gīta": "သီချင်း", "gītasaddo": "သီချင်းသံ", "vādita": "တီးမှုတ်", "vāditasaddo": "တီးမှုတ်သံ",
    "samma": "လင်းကွင်း", "sammasaddo": "လင်းကွင်းသံ", "pāṇi": "လက်ခုပ်", "pāṇisaddo": "လက်ခုပ်သံ",
    "sattānaṃ": "သတ္တဝါ", "nigghosasaddo": "ဆူညံသံ",
    "dhātūnaṃ": "ဓာတ်", "sannighāta": "ရိုက်ခတ်", "dhātūnaṃ sannighātasaddo": "ဓာတ်တို့ ရိုက်ခတ်သံ",
    "vāta": "လေ", "vātasaddo": "လေတိုက်သံ", "udaka": "ရေ", "udakasaddo": "ရေသံ",
    "manussa": "လူ", "manussasaddo": "လူသံ", "amanussa": "လူ မဟုတ်သူ",
    "amanussasaddo": "လူ မဟုတ်သူတို့၏ အသံ",
    # --- smell (1-624), taste (1-628)
    "mūla": "အမြစ်", "sāra": "အနှစ်", "taca": "အခေါက်", "patta": "အရွက်", "puppha": "ပန်း",
    "phala": "အသီး", "āmaka": "အစိမ်း", "vissa": "ပုပ်သိုး", "khandha": "ပင်စည်",
    "mūlagandho": "အမြစ် အနံ့", "sāragandho": "အနှစ် အနံ့", "tacagandho": "အခေါက် အနံ့",
    "pattagandho": "အရွက် အနံ့", "pupphagandho": "ပန်း အနံ့", "phalagandho": "အသီး အနံ့",
    "āmakagandho": "အစိမ်း အနံ့", "vissagandho": "ပုပ်သိုး အနံ့",
    "sugandho": "မွှေးသော အနံ့", "duggandho": "နံစော်သော အနံ့",
    "mūlaraso": "အမြစ် အရသာ", "khandharaso": "ပင်စည် အရသာ", "tacaraso": "အခေါက် အရသာ",
    "pattaraso": "အရွက် အရသာ", "puppharaso": "ပန်း အရသာ", "phalaraso": "အသီး အရသာ",
    "ambilaṃ": "အချဉ်", "madhuraṃ": "အချို", "tittakaṃ": "အခါး", "kaṭukaṃ": "အစပ်", "loṇikaṃ": "အငန်",
    "khārikaṃ": "ပြာရည် အရသာ", "lambilaṃ": "အချဉ်စူး", "kasāvo": "အဖန်", "sādu": "စားကောင်းသော",
    # --- tangible (1-647), water (1-651), the four elements (1-967 ff.)
    "kakkhaḷaṃ": "ကြမ်းတမ်းသော", "mudukaṃ": "ပျော့ပျောင်းသော", "saṇhaṃ": "ချောမွေ့သော",
    "pharusaṃ": "ဖုထစ်သော", "garukaṃ": "လေးလံသော", "lahukaṃ": "ပေါ့ပါးသော",
    "samphassaṃ": "ထိတွေ့ရ", "samphasso": "ထိတွေ့ရ",
    "manāpiyo": "စိတ်နှင့် တွေ့သော", "amanāpiyo": "စိတ်နှင့် မတွေ့သော",
    "sineho": "စေးကပ်မှု", "gataṃ": "သဘော ရှိသော",
    "bandhanattaṃ": "ဖွဲ့စည်းချည်နှောင်ထားသော အဖြစ်",
    "bandhanattaṃ rūpassa": "ရုပ်၏ ဖွဲ့စည်းချည်နှောင်ထားသော အဖြစ်",
    "khara": "ခက်မာ", "kakkhaḷattaṃ": "ကြမ်းတမ်းသော အဖြစ်", "usmā": "အပူ", "usumaṃ": "အပူငွေ့",
    "thambhitattaṃ": "တောင့်တင်းထားသော အဖြစ်",
    # --- the femininity / masculinity / life faculties (1-632 ff.)
    "liṅgaṃ": "အသွင်သဏ္ဌာန်", "nimittaṃ": "အမှတ်အသား", "kuttaṃ": "အမူအရာ", "ākappo": "ဟန်ပန်",
    "rūpīnaṃ dhammānaṃ": "ရုပ် ဖြစ်သော သဘောတရား",
    "āyu": "သက်တမ်း", "ṭhiti": "တည်တံ့ခြင်း", "yapanā": "ဆက်လက် ဖြစ်နေခြင်း",
    "yāpanā": "ဆက်လက် ရှင်သန်စေခြင်း", "iriyanā": "လှုပ်ရှားခြင်း", "vattanā": "လည်ပတ်ခြင်း",
    "pālanā": "စောင့်ရှောက်ခြင်း",
    # --- intimation (1-635 / 1-636)
    "abhikkamantassa": "ရှေ့သို့ တိုးသွားသူ", "paṭikkamantassa": "နောက်သို့ ဆုတ်သူ",
    "ālokentassa": "ရှေ့တည့်တည့် ကြည့်သူ", "vilokentassa": "ဘေးဘီ ကြည့်သူ",
    "samiñjentassa": "ကွေးသူ", "pasārentassa": "ဆန့်သူ",
    "thambhanā": "တောင့်တင်းခြင်း", "santhambhitattaṃ": "ကောင်းစွာ တောင့်တင်းထားသော အဖြစ်",
    "viññāpanā": "ထုတ်ဖော်ပြသခြင်း",
    "vācā": "စကား", "girā": "စကားသံ", "byappatho": "ပြောဆိုပုံ", "udīraṇaṃ": "ရွတ်ဆိုခြင်း",
    "ghoso": "အသံဗလံ", "dhoso": "အသံဗလံ", "ghosakammaṃ": "အသံ ထုတ်ခြင်း", "bhedo": "@bhedo",
    # --- space (1-637), the qualities (1-638 ff.)
    "aghaṃ": "ဗလာ", "vivaro": "အပေါက်", "asamphuṭṭhaṃ": "မထိတွေ့သော",
    "lahupariṇāmatā": "လျင်မြန်စွာ ပြောင်းလဲနိုင်ခြင်း", "adandhanatā": "မနှေးကွေးခြင်း",
    "avitthanatā": "မတုံ့ဆိုင်းခြင်း", "dandhanatā": "နှေးကွေးခြင်း", "vitthanatā": "တုံ့ဆိုင်းခြင်း",
    "maddavatā": "နူးညံ့သော အဖြစ်", "akakkhaḷatā": "မကြမ်းတမ်းခြင်း", "akathinatā": "မမာကျောခြင်း",
    "kakkhaḷatā": "ကြမ်းတမ်းခြင်း", "kathinatā": "မာကျောခြင်း",
    "kammaññattaṃ": "အသုံးပြုရန် သင့်တော်သော အဖြစ်", "bhāvo": "သဘော",
    "ācayo": "စုပုံခြင်း",
    "jīraṇatā": "ဆွေးမြေ့ခြင်း", "khaṇḍiccaṃ": "သွားကျိုးခြင်း", "pāliccaṃ": "ဆံပင်ဖြူခြင်း",
    "valittacatā": "အရေတွန့်ခြင်း", "āyuno": "သက်တမ်း", "saṃhāni": "ယုတ်လျော့ခြင်း",
    "paripāko": "ရင့်ရော်ခြင်း",
    "khayo": "ကုန်ခန်းခြင်း", "vayo": "ပျက်ခြင်း", "paribhedo": "ကွဲကြေခြင်း",
    "antaradhānaṃ": "ကွယ်ပျောက်ခြင်း",
    # --- edible food (1-645)
    "Odano": "ထမင်း", "kummāso": "ဆန်ပြုတ်", "sattu": "မုယောမှုန့်", "maccho": "ငါး", "maṃsaṃ": "အသား",
    "khīraṃ": "နွားနို့", "dadhi": "နို့ချဉ်", "sappi": "ထောပတ်ကြည်", "navanītaṃ": "ထောပတ်",
    "madhu": "ပျားရည်", "phāṇitaṃ": "တင်လဲ",
    "mukha": "ခံတွင်း", "āsiyaṃ": "စားရသော", "danta": "သွား", "vikhādanaṃ": "ဝါးရသော",
    "gala": "လည်ချောင်း", "ajjhoharaṇīyaṃ": "မျိုချရသော", "kucchi": "ဝမ်း", "vitthambhanaṃ": "ပြည့်စေသော",
    "ojāya": "အဆီအနှစ်", "yāpenti": "အသက် ရှင်သန်သည်",
}
T_301 = {}
T_302 = {}
T_303 = {}


# =====================================================================================================
# context functions and per-segment overrides
# (Rūpakaṇḍa tables below)
#
# =====================================================================================================
RE_FINE = re.compile(r"(?<![aA])rūpāvacar|rūpūpapatti|rūparāga")
RE_VIS = re.compile(r"rūpāyatan|rūpadhātu|rūpārammaṇ")
RE_MAT = re.compile(r"rūpasaṅgah|rūpakaṇḍ|rūpavibhatt")
RE_VIS_RUPAM = re.compile(r"rūpaṃ (sanidassanaṃ|ārabbha|petaṃ|catunnaṃ mahābhūtānaṃ upādāya vaṇṇa)")


def f_rupa(kw, pali, my):
    """The fragment rūpa (sample rule 11, extended by rule 13), by the compounds of THAT segment it comes from:
    rūpāvacara = the fine-material plane «သိမ်မွေ့သော ရုပ်»; rūpāyatana / rūpadhātu / rūpārammaṇa = the visible
    object «အဆင်းအရောင်»; rūpasaṅgaha / Rūpakaṇḍa / Rūpavibhatti = matter «ရုပ်». Where the fragment comes from
    compounds of two senses, both are given as alternatives (plane, matter, visible object). The capitalised
    keyword «Rūpa» only looks at the capitalised words (a heading, or Rūpāyatanaṃ opening an answer)."""
    if kw[:1].isupper():
        pali = " ".join(w for w in pali.split() if w[:1] == "R").lower()
    senses = []
    if RE_FINE.search(pali):
        senses.append("သိမ်မွေ့သော ရုပ်")
    if RE_MAT.search(pali):
        senses.append("ရုပ်")
    if RE_VIS.search(pali):
        senses.append("အဆင်းအရောင်")
    return " / ".join(senses) or "ရုပ်"


def f_rupam(kw, pali, my):
    """rūpaṃ: matter «ရုပ်» («taṃ rūpaṃ», «sabbaṃ rūpaṃ»); where the same segment also has rūpaṃ as the visible
    object (rūpaṃ sanidassanaṃ … passati, rūpaṃ ārabbha, rūpaṃ petaṃ), both senses (rule 13)."""
    if RE_VIS_RUPAM.search(pali):
        return "ရုပ် / အဆင်းအရောင်"
    return "ရုပ်"


def f_sukha(kw, pali, my):
    """sukha in sukhasamphassa (pleasant to the touch) = «သာယာသော» (text «ထိတွေ့ရ သာယာသော»); else the sample's noun."""
    return "သာယာသော" if "sukhasamphass" in pali else "သာယာမှု"


def f_dukkha(kw, pali, my):
    return "နာကျင်သော" if "dukkhasamphass" in pali else "နာကျင်မှု"


def f_bhedo(kw, pali, my):
    """bhedo: in vacībhedo «နှုတ်မှ စကား ကွဲထွက်ခြင်း» = «ကွဲထွက်ခြင်း»; in the aniccatā list «ကွဲခြင်း»."""
    return "ကွဲထွက်ခြင်း" if "vacībhedo" in pali else "ကွဲခြင်း"


def f_rel(kw, pali, my):
    """Relative pronouns (rule 15): Burmese has none; the generalising «yaṃ / yo vā panaññampi atthi X» is rendered
    «အခြား X ရှိသမျှ» («whatever other X there is»), so there yaṃ / yo = «ရှိသမျှ»; elsewhere no direct equivalent."""
    return "ရှိသမျှ" if re.search(r"vā panaññ", pali) else NONE


FUNCS = {"rel": f_rel, "rupa": f_rupa, "rupam": f_rupam, "sukha": f_sukha, "dukkha": f_dukkha, "bhedo": f_bhedo}
T_RUPA.update({"sukha": "@sukha", "dukkha": "@dukkha", "Rūpa": "@rupa"})

CTX = {
    # sid: {keyword: value}
}

# chapter -> its own table (looked up first); every table is also shared with the other chapters
SECTIONS = {
    "preamble": T_PREAMBLE,
    "1-matika": T_MATIKA,
    "3-01-rupakandam": T_301,
    "3-02-rupakandam": T_302,
    "3-03-rupakandam": T_303,
}
CHAPTERS = ["3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam"]   # chapters written by this run (map_3.py)

SHARED = {}
for _t in SECTIONS.values():
    for _k, _v in _t.items():
        SHARED.setdefault(_k, _v)


# =====================================================================================================
# dictionary-form rules (written to map-table.md)
# =====================================================================================================
RULES = """## Dictionary-form rules (Burmese), proposed for review

The value is the word or phrase of THAT segment's Burmese that carries the keyword, reduced to one fixed form:

1. **Nouns** (a bare noun keyword in any case): the noun without the case particles and postpositions that follow it
   (၏ ကို ၌ တွင် နှင့် မှ ဖြင့် အား သို့ သည် က) and without the plural markers (များ တို့).
   dhammā = သဘောတရား; Abhidhammapiṭake (text «အဘိဓမ္မာပိဋကတွင်») = အဘိဓမ္မာပိဋက; indriyesu («အာရုံခံ
   အင်္ဂါတို့၏») = အာရုံခံ အင်္ဂါ; dassanena («သစ္စာကို မြင်ခြင်းဖြင့်») = သစ္စာကို မြင်ခြင်း; ṭhānesu
   («အခြေအနေတို့၌») = အခြေအနေ; kusalesu dhammesu («ကုသိုလ် သဘောတရားတို့၌») = ကုသိုလ် သဘောတရား.
   Only the particles at the END of the value go: inside a phrase the text's particles stay, because they belong to
   the term («စွဲလမ်းမှု၏ အာရုံ», «ကိလေသာဖြင့် ညစ်နွမ်းသော», «မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော»). Verbal nouns
   keep their noun ending: ခြင်း / မှု / ရာ (samatho = စိတ်ငြိမ်သက်ခြင်း, vuṭṭhāna = ထမြောက်ရာ).
2. **A noun predicated of dhammā** («X ဖြစ်သော / X မဟုတ်သော သဘောတရား» = «states that are / are not X») maps to the
   noun alone: the copula ဖြစ်သော / မဟုတ်သော is not the keyword. hetū = အမြစ်, āsavā = စိတ်အစွန်းအထင်း, cittā =
   စိတ်, cetasikā = စိတ်၏ အဖော် (the approved noun). A possessive fragment that lost its sa- / a- (hetukā, vitakkā,
   vicārā, pītikā, ārammaṇā, adhipatino) is likewise the noun it rests on, as the English mapping does:
   hetukā = အမြစ်, ārammaṇā = အာရုံ (also in -ārammaṇa compounds), adhipatino = အကြီးအမှူး.
3. **Adjectives and participles**: the attributive phrase as the text builds it, ending in the attributive marker
   «သော» (future / gerundive participles: «မည့်», as the text has it), WITHOUT the head noun သဘောတရား.
   sukhāya = သာယာသော; sampayuttā = ယှဉ်တွဲသော; hetusampayuttā-type compounds keep their object:
   āsavavippayuttā = စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော; pahātabbā = ပယ်ရမည့်; uppādino = ဖြစ်ပေါ်လာမည့်.
   A bare sampayuttā / sahagatā / anuparivattino drops the object's own postposition (နှင့် goes with the object):
   ယှဉ်တွဲသော, အတူ ဖြစ်သော, နောက်သို့ လိုက်ပါသော. An adjective the text builds without a marker keeps the text's
   form (majjhimā = အလယ်အလတ်, atītā = အတိတ်, bāhirā = ပြင်ပ); one the text builds as a genitive keeps ၏ as its
   attributive marker (sekkhā = ကျင့်ကြံဆဲသူ၏).
   Where the segment uses the same verb in another construction, only the ending is normalised to «သော»: the
   concessive «…သော်လည်း», the conjunctive «…၍» / «…ပြီး», the nominal «…သည်» (… သည်တို့ / သည်ကို), the verbal noun
   «…ခြင်း», the person noun «…သူ» and the finite «…ပြီ». upādiṇṇa (text «ကံကြောင့် ဖြစ်၍») = ကံကြောင့် ဖြစ်သော;
   anāsavā in «… မဖြစ်နိုင်သည်တို့လည်း» = … မဖြစ်နိုင်သော; mahaggata in «ကြီးမြတ်သည်ကို အာရုံပြုသော» =
   ကြီးမြတ်သော (as mahaggatā); saṃviggassa («သံဝေဂ ရသူ၏») = သံဝေဂ ရသော; gutta («စောင့်ထိန်းခြင်း») = စောင့်ထိန်းသော;
   niṭṭhitā («ပြီးဆုံးပြီ») = ပြီးဆုံးသော; yathā («လျော်ညီသူ၏») = လျော်ညီသော.
4. **Verbs**: the verb + «သည်» (one fixed form, whatever the text's ending: ပါ၏ / ၏ / ပြီ). The Mātikā has no
   finite Pāli verb; the one keyword the text renders by a finite verb is Namo («ရှိခိုးပါ၏») = ရှိခိုးသည်.
   A clause that renders a noun keyword keeps its own verb in «သည်» (vibhava = ဘဝ ပျောက်ကွယ်သည်, sassata =
   ထာဝရ တည်မြဲသည်), without the quotative ဟူသော.
5. **«X dhammā»** keywords = the attributive phrase + « သဘောတရား» (singular, plural marker dropped):
   kusalā dhammā = ကုသိုလ် သဘောတရား; sukhasahagatā dhammā = သာယာမှုနှင့်အတူ ဖြစ်သော သဘောတရား.
   «no / na X dhammā» = the negative the text builds, «…သည် မဟုတ်သော သဘောတရား» (no cittasamuṭṭhānā dhammā =
   စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော သဘောတရား). Privative a- / an- = the text's «မ…» or «… မရှိသော» form (asaṅkhatā =
   ပြုပြင်ဖန်တီးထားခြင်း မရှိသော, anāsavā = … မဖြစ်နိုင်သော).
6. **Sentence-final material** is dropped (။, ဖြစ်သည်, ပါ၏, the quotative ဟူသော before အယူ when only a part of the
   view is the keyword), and so is the «၊» inside a term: abyākatā = ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော
   (text «… မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော»). The «လည်း» of «neither … nor» stays: it is part of the term.
7. **Titles** keep the approved title whole: Dhammasaṅgaṇī = သဘောတရားများကို စုစည်းရေတွက်ခြင်း.
8. **Fragments** that lost a negative prefix map to the positive part: gutta (from aguttadvāratā) = စောင့်ထိန်းသော,
   mattaññutā (from amattaññutā) = အတိုင်းအရှည်ကို သိခြင်း, vacassatā (from dovacassatā) = သွန်သင်ချက်ကို
   နားထောင်ခြင်း, santuṭṭhitā (from asantuṭṭhitā) = ရောင့်ရဲမှု. Burmese puts the negative မ INSIDE a compound verb
   (နားမထောင်, အကျုံးမဝင်), so the check accepts the positive chunk with one infixed မ.
9. **Particles**: ca / pana / kho / eva have no Burmese word (none is a keyword here). The free negative na of
   «na viññeyyā» is the text's prefix «မ» (မသိနိုင်သော).
10. Discontinuous parts are joined with « … » (mittatā = မိတ်ဆွေ … ပေါင်းသင်းခြင်း); « / » only for genuine
    alternatives; never «, » or «၊» inside a value. Identical keywords in identical formulas get identical values;
    repeats inside a line get the same value.
11. **Sense by context**: rūpa in rūpāvacara = the fine-material plane «သိမ်မွေ့သော ရုပ်» (matter elsewhere = ရုပ်);
    bahiddhā in the Mātikā = «သူတစ်ပါး၌» (in others; the adverb keeps its locative ၌, which is its meaning).
"""


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
            out[m.group(1)] = " ".join(buf)
            buf = []
    return out


def resolve(v, kw, pali, my):
    if v is not None and v.startswith("@"):
        return FUNCS[v[1:]](kw, pali, my)
    return v


def table_get(tab, kw):
    for k in (kw, low(kw)):
        if k in tab:
            return tab[k]
    return None


def neg_attr(v):
    """«…သော» -> «…သည် မဟုတ်သော» (the negative attributive as the text builds it)."""
    if v.endswith("သော"):
        return v[:-3] + "သည် မဟုတ်သော"
    return None


def variants(kw):
    """Inflected forms of a Mātikā / table keyword (rule 12): -meva -> -ṃ (eva has its own keyword); neuter -ṃ,
    masculine -o, locative -mhi, instrumental -ena -> the plural -ā of the Mātikā key; -u / -i -> -uno / -ino."""
    k, out = low(kw), []
    if k.endswith("meva"):
        k = k[:-4] + "ṃ"
        out.append(k)
    if k.endswith("aṃ"):
        out += [k[:-2] + "ā", k[:-1]]
    if k.endswith("o"):
        out.append(k[:-1] + "ā")
    if k.endswith("amhi"):
        out.append(k[:-4] + "ā")
    if k.endswith("ena"):
        out.append(k[:-3] + "ā")
    if k.endswith(("u", "i")):
        out.append(k + "no")
    return out


def tables(ch, sid):
    return [CTX.get(sid, {}), SECTIONS.get(ch, {}), T_RUPA, SHARED]


def lookup1(ch, sid, kw):
    for tab in tables(ch, sid):
        v = table_get(tab, kw)
        if v is not None:
            return v
    for k2 in variants(kw):
        for tab in tables(ch, sid):
            v = table_get(tab, k2)
            if v is not None:
                return v
    return None


def lookup(ch, sid, kw, pali, my):
    v = lookup0(ch, sid, kw, pali, my)
    # rule 14: «rūpaṃ X» whose head noun the text separates from X («ထိခိုက်မှု ရှိသော၊ စွမ်းရည် ဖြစ်သော ရုပ်») is
    # discontinuous: «X … ရုပ်»
    flat = my.replace("၊ ", " ")
    if "rūpaṃ" in kw.split() and len(kw.split()) == 2 and v.endswith(" ရုပ်") and v not in flat:
        v = v[:-len(" ရုပ်")] + " … ရုပ်"
    return v


def lookup0(ch, sid, kw, pali, my):
    v = lookup1(ch, sid, kw)
    if v is not None:
        return resolve(v, kw, pali, my)
    ws = kw.split()
    if len(ws) >= 2 and ws[-1] == "dhammā":
        neg = ws[0] in ("no", "na")
        core = " ".join(ws[1:-1] if neg else ws[:-1])
        base = resolve(lookup1(ch, sid, core), core, pali, my)
        if base:
            if neg:
                base = neg_attr(base)
            if base:
                return base + " " + DH
    if len(ws) >= 2:
        # rule 14: a multiword keyword of attributes = the parts' values in the text's order, joined by a space
        # (the «၊» between them dropped, rule 6); a noun part rūpaṃ goes last, as the head noun «ရုပ်».
        parts = [w for w in ws if w != "rūpaṃ"] + [w for w in ws if w == "rūpaṃ"]
        vals = [resolve(lookup1(ch, sid, w), w, pali, my) for w in parts]
        if all(vals) and NONE not in vals:
            return " ".join(vals)
    raise KeyError(kw)


# ---- presence check --------------------------------------------------------------------------------
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "၊", "။", "သည့်")   # dictionary «Xသော» <- text «X»+one of these (rule 12: «၊» «။» «သည့်»)
VERB_FROM = ("ပါ၏", "၏", "ပြီ", "သော", "ကြ")                   # dictionary «Xသည်» <- text «X»+one of these («ကြ»: rule 16)


def chunk_present(c, text):
    """-> rule name ('exact', 'attr', 'verb', 'neg-infix') or None."""
    if c in text:
        return "exact"
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in ATTR_FROM):
            return "attr"
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in VERB_FROM):
            return "verb"
    for i in range(1, len(c)):
        if c[:i] + "မ" + c[i:] in text:
            return "neg-infix"
    return None


def presence(v, text):
    """-> (ok, [(chunk, rule) for every chunk not found literally])"""
    if v == NONE:
        return True, []
    rules = []
    for part in re.split(r" … | / ", v):
        for c in part.split():
            c = c.strip("“”‘’()")
            if not c:
                continue
            r = chunk_present(c, text)
            if r is None:
                return False, [(c, None)]
            if r != "exact":
                rules.append((c, r))
    return True, rules


def load(ch):
    my = segments(MY / f"{ch}.md")
    pa = segments(PI / f"{ch}.md")
    rows = [LINE.match(l).groups() for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()
            if LINE.match(l)]
    return my, pa, rows


def run(write=True):
    table = collections.defaultdict(collections.Counter)
    unmapped = collections.defaultdict(list)
    problems, summary = [], []
    for ch in CHAPTERS:
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
        if write and not unmapped:
            (HERE / f"{ch}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return table, unmapped, problems, summary


def verify(ch):
    """The three checks of the brief: keyword preservation, presence, no «, » / «၊» in a value."""
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
             if any(", " in v or "၊" in v for v in [kv.split("=", 1)[1] for kv in y.split(", ")])
             or y.count("=") != len(x.split(", "))]
    return len(a), bad, fails, punct, ruled


NEW_RULES = """## Rules

Rules 1–11 are the approved sample rules (map-table.md); they apply unchanged. The rules below are NEW for the
Rūpakaṇḍa (3-01, 3-02, 3-03) and are proposed for review.

12. **Inflected Mātikā terms** keep the Mātikā value: the neuter -aṃ of the Ekaka list and the matter definitions
    (saṅkhataṃ = ပြုပြင်ဖန်တီးထားသော, upādiṇṇaṃ = ကံကြောင့် ဖြစ်သော, bāhiraṃ = ပြင်ပ), the masculine -o
    (anidassano = မမြင်နိုင်သော), the locative -amhi and the instrumental -ena (sappaṭighamhi / sappaṭighena =
    ထိခိုက်မှု ရှိသော), -u / -i for -uno / -ino (cittasahabhu = စိတ်နှင့်အတူ တည်ရှိသော). «X-meva» (^1-594) = the
    value of X: eva has its own keyword there, «ပင်» (text «…သည်ပင်»). The Ekaka list uses the BARE predicate verb
    («ပြုပြင်ဖန်တီးထား၊», «မမြဲ၊», «ဖြစ်ပေါ်ပြီး၊», «ကာမဘုံနှင့် ဆိုင်၊») and the definitions «…သည့်»: the dictionary
    form is still the attributive «…သော» (rule 3); the presence check accepts the stem followed by «၊», «။» or «သည့်».
13. **rūpa by sense**: the fragment rūpa follows the compounds of THAT segment: rūpāvacara = «သိမ်မွေ့သော ရုပ်»
    (sample), rūpāyatana / rūpadhātu / rūpārammaṇa = the visible object «အဆင်းအရောင်», rūpasaṅgaha / Rūpakaṇḍa /
    Rūpavibhatti = matter «ရုပ်». A segment whose fragment comes from compounds of two senses gets both, as genuine
    alternatives («ရုပ် / အဆင်းအရောင်», ^1-585, 1-593, U1; «သိမ်မွေ့သော ရုပ် / ရုပ်», ^1-584, 1-594). The capitalised
    «Rūpa» is read from the capitalised word only (heading «ရုပ်», or the answer «Rūpāyatanaṃ» = «အဆင်းအရောင်»).
    rūpaṃ = matter «ရုပ်» (taṃ rūpaṃ, sabbaṃ rūpaṃ); where the same segment also has rūpaṃ as the object seen
    (rūpaṃ sanidassanaṃ … passati, rūpaṃ ārabbha, rūpaṃ petaṃ) = «ရုပ် / အဆင်းအရောင်»; rūpamhi (only the object)
    = «အဆင်းအရောင်».
14. **Multiword attribute keywords** = the text's phrase with the «၊» between the attributes dropped (rule 6), a noun
    rūpaṃ last as the head «ရုပ်»: upādā sappaṭighaṃ = မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော ထိခိုက်မှု ရှိသော;
    anidassano sappaṭigho = မမြင်နိုင်သော ထိခိုက်မှု ရှိသော; rūpaṃ cittasahabhu = စိတ်နှင့်အတူ တည်ရှိသော ရုပ်.
    In such a phrase bāhiraṃ keeps the text's «ပြင်ပ ဖြစ်သော» (bare bāhiraṃ stays the sample's «ပြင်ပ»). A
    compound the text builds concessively keeps the text, as the sample's anupādiṇṇupādāniyā: anidassanasappaṭighaṃ =
    မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော; anidassanaappaṭighaṃ = မမြင်နိုင် ထိခိုက်မှုလည်း မရှိသော (harmonise item 21).
    Fragments of a longer phrase keep the particles inside it (rule 1): «āyatanaṃ cakkhuviññeyyaṃ rūpaṃ» = အာရုံခံ
    နယ်ပယ်သည် မျက်စိဖြင့် သိနိုင်သော ရုပ်; «rūpaṃ manoviññeyyaṃ rūpaṃ» = ရုပ် … မနောဖြင့် သိနိုင်သော ရုပ် (the
    skipped «အားလုံးသည်» is sabbaṃ, not a keyword).
15. **Relative pronouns** yaṃ / yo / yā: Burmese has none (a relative clause, no word) = (no direct equivalent);
    in «yaṃ / yo vā panaññampi atthi X» the text says «အခြား X ရှိသမျှ» («whatever other X there is»), so there
    yaṃ / yo = «ရှိသမျှ».
16. **Finite verbs keep their tense** (rule 4's «သည်» form): aorist «…ခဲ့သည်» (uppajji, paṭihaññi, suṇi, ghāyi, sāyi,
    phusi), present «…သည်» (uppajjati …), future «…လိမ့်မည်» (uppajjissati …; the future has no သည်: text
    «…လိမ့်မည်ဖြစ်စေ»). «sappaṭighaṃ / sappaṭigho paṭihaññi» = ထိခိုက်မှု ရှိသော … ထိခိုက်ခဲ့သည် (discontinuous).
    yāpenti = အသက် ရှင်သန်သည် (text «အသက် ရှင်သန်ကြရာ»; the check accepts the plural «ကြ»).
17. **Absolutives** upādāya / nissāya = «မှီ၍», the conjunctive as the text has it (an absolutive is not a finite
    verb), with the object when the keyword has it (cakkhuṃ nissāya = မျက်စိကို မှီ၍); upādāya X = «မှီ၍ ဖြစ်သော X».
18. **Nouns of the matter chapters**: predicated nouns are the noun (rule 2): mahābhūtaṃ = မူလဓာတ်ကြီး, indriyaṃ =
    စွမ်းရည်, viññatti = ထုတ်ဖော်ပြသမှု; the fragment bhūta (of mahābhūta) = မူလဓာတ်. Numerals keep the count:
    Catubbidhena = လေးမျိုး, Dasa = ဆယ်; the fragment vidhena = မျိုး; rūpasaṅgaho = ရုပ်ကို … စုစည်းခြင်း (the
    count in between). The genitive of a compound member goes (rule 1): cakkhusamphassassa = မျက်စိ၏ တွေ့ထိမှု
    (the ၏ inside stays), cakkhuviññāṇassa = မျက်စိ သိစိတ်. Person nouns (abhikkamantassa …) = the noun «…သူ».
    Sound / smell / taste names keep the text's compound (bherisaddo = စည်ကြီးသံ, mūlagandho = အမြစ် အနံ့); a
    member alone is its noun (bheri = စည်ကြီး; pāṇi = လက်ခုပ်, as the text renders pāṇisadda).
19. **Sense by context** (as rule 11): sukha / dukkha in sukhasamphassa / dukkhasamphassa = သာယာသော / နာကျင်သော
    (text «ထိတွေ့ရ သာယာသော»; sukha elsewhere = the sample's သာယာမှု), samphassaṃ / samphasso = ထိတွေ့ရ; bhedo
    in vacībhedo = ကွဲထွက်ခြင်း, in the aniccatā list = ကွဲခြင်း. Adjectives the text builds with the head «အရာ»
    drop it as the head noun: kakkhaḷaṃ (text «ကြမ်းတမ်းသောအရာ») = ကြမ်းတမ်းသော, asamphuṭṭhaṃ = မထိတွေ့သော,
    gataṃ = သဘော ရှိသော.
20. **Source slip**: dhoso (^1-850) = ghoso = အသံဗလံ (harmonise item 15).
"""


def write_table(table, ruled_all):
    sample = set()
    for c in ("preamble", "1-matika"):
        for l in (HERE / f"{c}.mapped.md").read_text(encoding="utf-8").splitlines():
            for kv in l.split("] ", 1)[1].split(", "):
                sample.add(kv.split("=", 1)[0])
    with open(HERE / "map-table-3.md", "w", encoding="utf-8") as f:
        f.write("# pi-1 Burmese keyword mapping: Rūpakaṇḍa (" + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_3.py (a copy of the approved sample's map_all.py with the Rūpakaṇḍa tables). Burmese "
                "from the FINAL text of this track only (AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters).\n\n")
        f.write(NEW_RULES)
        f.write("\n## Presence: chunks matched by a dictionary-form rule (not literally in the segment)\n\n")
        f.write("Every other chunk of every value occurs literally in its segment's Burmese (particles that the "
                "rules strip follow the chunk in the text). attr = «…သော» from the text's «…သော်/၍/ပြီး/သည်/ခြင်း/သူ/ပြီ» or "
                "the bare predicate before «၊ / ။ / သည့်» (rule 12); verb = «…သည်» from «…ပါ၏/၏/ပြီ/သော/ကြ»; "
                "neg-infix = rule 8.\n\n| segment | keyword | chunk | rule |\n|---|---|---|---|\n")
        for sid, k, c, r in ruled_all:
            f.write(f"| {sid} | {k} | {c} | {r} |\n")
        f.write("\n## Keyword → Burmese (number of uses in 3-01, 3-02, 3-03)\n\n«new» = a keyword not in the approved "
                "sample outputs. Several values = the keyword reads differently by context.\n\n"
                "| Pāli keyword | Burmese (uses) | |\n|---|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            f.write(f"| {kw} | " + " / ".join(f"{v} ({n})" for v, n in table[kw].most_common())
                    + (" | new |\n" if kw not in sample else " | |\n"))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--seg":
        sid = args[1]
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            for s, kws in rows:
                if s == sid:
                    print(pa.get(sid), "\n", my[sid], "\n")
                    for kw in kws.split(", "):
                        try:
                            v = lookup(ch, sid, kw.strip(), pa.get(sid, ""), my[sid])
                            print(kw, "=", v, presence(v, my[sid]))
                        except KeyError:
                            print(kw, "= ??")
        sys.exit()
    report = bool(args and args[0] == "--report")
    table, unmapped, problems, summary = run(write=not report)
    if unmapped:
        print(f"UNMAPPED keywords: {len(unmapped)} distinct, {sum(len(v) for v in unmapped.values())} uses")
        for kw, where in sorted(unmapped.items(), key=lambda x: -len(x[1])):
            print(f"  {kw}\t{len(where)}\t{where[0][1]}")
    print(f"presence problems: {len(problems)}")
    for ch, sid, kw, v in problems:
        print(f"  {sid}\t{kw} = {v}")
    if report or unmapped:
        sys.exit()
    ruled_all, tot_nne = [], 0
    results = []
    for ch, n, nne in summary:
        ln, bad, fails, punct, ruled = verify(ch)
        ruled_all += ruled
        tot_nne += nne
        results.append((ch, ln, bad, fails, punct, ruled, nne))
    write_table(table, ruled_all)
    for ch, ln, bad, fails, punct, ruled, nne in results:
        print(f"{ch}: lines {ln} | keyword preservation bad {bad} | presence failures {len(fails)} "
              f"(rule-matched chunks {len(ruled)}) | comma/၊ {punct} | no-equivalent {nne}")
        for f_ in fails:
            print("   FAIL", f_)
    for sid, k, c, r in ruled_all:
        print(f"   rule {r:9} {sid:10} {k} : {c}")
    print("total no direct equivalent:", tot_nne, "| distinct keywords:", len(table))
