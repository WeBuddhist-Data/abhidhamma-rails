"""Pāli→Burmese keyword mapping for pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»): chapters 5, 7, 8, 9, 10, 11.

A copy of the approved sample script map_all.py (its tables T_PREAMBLE, T_KHANDHA, compose rules, context functions
and verifier unchanged, used as shared tables) with the tables of these six chapters added. It writes only
<ch>.mapped.md of these chapters and map-table-5-7-11.md. Extra working aids: --pi1 KW…, --todo CH, --dump CH,
--grep CH SID|all REGEX [p].

usage (python3 -I -X utf8, from any directory):
  map_5-7-11.py          writes <ch>.mapped.md for every chapter in CHAPTERS and map-table-5-7-11.md, then verifies them
                         (keyword preservation, presence of every value chunk in its segment, no ", " / «၊» / « / »
                         in a value)
  map_all.py --report    writes nothing; lists unmapped keywords and presence failures
  map_all.py --seg ID    prints Pāli, Burmese, keywords and mapping of one segment
  map_all.py --new [N]   prints the first N segments that hold a keyword without a value (working aid)

Method: a copy (not an import) of the approved pi-1 Burmese mapper (pi-1-my/mapper-my/map_all.py and the later
pi-1 scripts map_2-01 … map_5): tables keyword -> Burmese in dictionary form, per-segment overrides CTX, context
functions, compose rules and the presence verifier. The Burmese is the FINAL pi-2 text of this track
(AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters). No other Burmese source is used.

Lookup order per keyword:
  CTX[sid] -> the chapter's own table T_<ch> -> the shared tables of the other pi-2 chapters
  -> PI1: the final pi-1 mapping (AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md), the most
     frequent pi-1 value of that keyword that is present in THIS segment (pi-1 values are binding for the same
     keyword in the same kind of segment; the pi-2 text reuses pi-1's Burmese for identical Pāli)
  -> compose: «X dhammā» = T[X] + « သဘောတရား»; «vuccati X» = T[X] + «ဟု ခေါ်သည်».
A value «@name» is a context function f(kw, pali, my); «@alt» = the first variant of ALT[kw] present in the segment
(variants of ONE sense: the endings the text uses in that segment).
Adding a chapter: write its table T_<ch> (and CTX entries), register it in SECTIONS, add it to CHAPTERS.
"""
import re, sys, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-2_split_chapters"
PI1MAP = ROOT / "AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md"
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
    # pi-1 preamble values (approved sample), unchanged
    "Abhidhamma": "အဘိဓမ္မာ",
    "Abhidhammapiṭake": "အဘိဓမ္မာပိဋက",
    "Namo": "ရှိခိုးသည်",
    "bhagavato": "မြတ်စွာဘုရား",
    "arahato": "ရဟန္တာ",
    "sammā": "အပြည့်အဝ",
    "sambuddhassa": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရားရှင်",
    "sammāsambuddhassa": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်",
    # the pi-2 book title (rule 7: the approved title whole)
    "Vibhaṅgapāḷi": "ခွဲခြမ်းစိတ်ဖြာခြင်း",
    "Vibhaṅga": "ခွဲခြမ်းစိတ်ဖြာခြင်း",
    "pāḷi": NONE,                                             # «the canonical text»: the title has no word for it
}

T_KHANDHA = {
    # --- headings and colophons (the heading's own Burmese, pi-1 decision 4)
    "vibhaṅgo": "ခွဲခြမ်းစိတ်ဖြာခြင်း",
    "Suttanta": "သုတ္တန်",
    "Pañhā": "မေးခွန်း",
    "Pañhāpucchakaṃ": "မေးခွန်းများဖြင့် ဖော်ပြချက်",
    "Tikaṃ": "သုံးမျိုးတွဲ", "Tika": "သုံးမျိုးတွဲ", "tike": "သုံးမျိုးတွဲ", "tikā": "သုံးမျိုးတွဲ",
    "mūlakaṃ": "အခြေခံသော",                 # pi-1 mūlaka; the text's head «ခွဲနည်း» is not the keyword (rule 3)
    "Ubhato": "နှစ်ဘက်စလုံး", "vaḍḍhakaṃ": "တိုးပွားသော",
    "vitthāro": "အကျယ်",
    "vibhattaṃ": "ခွဲခြားထားသော",            # text «ခွဲခြားထားသည့်အတိုင်း» (rule 3, ending «သည့်»)
    # --- suttanta frame
    "Yaṃ kiñci": "မည်သည့် … မဆို", "Yā kāci": "မည်သည့် … မဆို", "Ye keci": "မည်သည့် … မဆို",
    "tadekajjhaṃ": "ထိုအားလုံးကို တစ်စုတည်း",
    "abhisaññūhitvā": "ပေါင်းစု၍", "abhisaṅkhipitvā": "အကျဉ်းချုံ့၍",      # absolutives keep «၍»
    "vuccati": "ခေါ်သည်", "vuccanti": "ခေါ်သည်",
    "vuccanti saṅkhārā": "ပြုပြင်ဖန်တီးမှုများဟု ခေါ်သည်",   # the text keeps the plural inside the phrase
    "upādāyupādāya": "နှိုင်းယှဉ်၍",
    "daṭṭhabbaṃ": "မှတ်ယူရမည့်", "daṭṭhabbā": "မှတ်ယူရမည့်",              # gerundive as pahātabbā (attr-fut)
    "yaṃ vā panaññampi": "အခြား … ရှိသမျှလည်း",
    "parapuggalānaṃ": "အခြား ပုဂ္ဂိုလ်",
    "pāṭipuggalikaṃ": "ပုဂ္ဂိုလ်တစ်ဦးချင်းစီ၏ ဖြစ်သော",
    "upādāyarūpaṃ": "မှီ၍ ဖြစ်သော ရုပ်",
    "ajjhattaṃ": "@ajjhattam",
    "rūpa": "@rupa",
    # the three time lists (pi-1 1-1044 … 1-1046; the arisen list «…ပြီးသော», pi-1 4-01 rule 16)
    "atītaṃ": "အတိတ်", "anāgataṃ": "အနာဂတ်", "paccuppannaṃ": "ပစ္စုပ္ပန်",
    "atītā": "အတိတ်", "anāgatā": "အနာဂတ်", "paccuppannā": "ပစ္စုပ္ပန်",
    "niruddhaṃ": "ချုပ်ငြိမ်းပြီးသော", "vigataṃ": "ကင်းပျောက်ပြီးသော",
    "vipariṇataṃ": "ဖောက်ပြန် ပြောင်းလဲပြီးသော", "abbhatthaṅgataṃ": "လုံးဝ ကွယ်ပျောက်ပြီးသော",
    "atītaṃsena": "အတိတ် အပိုင်း",
    "saṅgahitaṃ": "အကျုံးဝင်သော", "saṅgahitā": "အကျုံးဝင်သော",
    "atītaṃsena saṅgahitaṃ": "အတိတ် အပိုင်း၌ အကျုံးဝင်သော",
    "atītaṃsena saṅgahitā": "အတိတ် အပိုင်း၌ အကျုံးဝင်သော",
    "jātaṃ": "မွေးဖွားပြီးသော", "nibbattaṃ": "ပေါ်ထွက်ပြီးသော",
    "abhinibbattaṃ": "ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော", "pātubhūtaṃ": "ထင်ရှားလာပြီးသော",
    "uppannaṃ": "ဖြစ်ပေါ်ပြီးသော", "uppannā": "ဖြစ်ပေါ်ပြီးသော", "uppanno": "ဖြစ်ပေါ်ပြီးသော",
    "uṭṭhitaṃ": "ထပေါ်ပြီးသော", "samuṭṭhitaṃ": "ကောင်းစွာ ထပေါ်ပြီးသော",
    # the hīna / paṇīta lists (my2-zeroshot-terms, new in pi-2)
    "uññātaṃ": "အထင်သေးထားသော", "avaññātaṃ": "လျစ်လျူရှုထားသော", "hīḷitaṃ": "ကဲ့ရဲ့ထားသော",
    "paribhūtaṃ": "စော်ကားထားသော", "acittīkataṃ": "အလေးမထားသော", "cittīkataṃ": "အလေးထားသော",
    "hīnamataṃ": "ယုတ်ညံ့သည်ဟု ယူဆထားသော",
    "aniṭṭhaṃ": "လိုလားဖွယ် မကောင်းသော", "iṭṭhaṃ": "လိုလားဖွယ်ကောင်းသော",
    "akantaṃ": "ချစ်ခင်ဖွယ် မကောင်းသော", "kantaṃ": "ချစ်ခင်ဖွယ်ကောင်းသော",
    "amanāpaṃ": "စိတ်နှင့် မတွေ့သော", "manāpaṃ": "စိတ်နှင့် တွေ့သော",
    "rūpā": "အဆင်းအရောင်", "saddā": "အသံ", "gandhā": "အနံ့", "rasā": "အရသာ", "phoṭṭhabbā": "အထိအတွေ့",
    "upakaṭṭhe": "အနားကပ်သော",              # fragment of anupakaṭṭhe (rule 8); the positive item is in the text
    # the eleven qualifiers, predicated («Xသည် ရုန့်ရင်းသည်»: rule 3 normalises «…သည်» to «…သော»)
    "oḷārikā": "ရုန့်ရင်းသော", "sukhumā": "နုညံ့သော",
    "bahiddhā": "မိမိ၏ ပြင်ပ၌",            # the adverb keeps its locative (rule 11); pi-2 text form
    # kinds of feeling / perception etc. (statement qualifiers)
    "dukkhā": "နာကျင်သော", "Dukkhā": "နာကျင်သော", "adukkhamasukhā": "မနာကျင် မသာယာသော",
    "kusalābyākatā": "ကုသိုလ် … ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "kusalākusalā": "ကုသိုလ် … အကုသိုလ်",
    "sukhadukkhā": "သာယာသော … နာကျင်သော", "sukhadukkhāhi": "သာယာသော … နာကျင်သော",
    "vedanāhi": "ခံစားမှု", "saññāhi": "မှတ်သိမှု",
    "ābyākatāhi vedanāhi": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော ခံစားမှု",
    "ābyākatāhi saññāhi": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော မှတ်သိမှု",
    "akusalābyākatāhi saññāhi": "အကုသိုလ် … ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော မှတ်သိမှု",
    "dukkhāhi vedanāhi": "နာကျင်သော ခံစားမှု",
    "sampayuttāhi saññāhi": "ယှဉ်တွဲသော မှတ်သိမှု",
    "vedanāya sampayuttā": "ခံစားမှုနှင့် ယှဉ်တွဲသော",
    "anāsavaṃ": "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော",
    "Paṭighasamphassa": "ထိခိုက်မှု၏ တွေ့ထိမှု", "Paṭighasamphassajā": "ထိခိုက်မှု၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "adhivacanasamphassa": "အမည်ခေါ်ဝေါ်မှု၏ တွေ့ထိမှု",
    "adhivacanasamphassajā": "အမည်ခေါ်ဝေါ်မှု၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "manosamphassajā": "မနော၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "manoviññāṇaṃ": "မနော သိစိတ်", "viññāṇadhātu": "သိစိတ် ဓာတ်",
    "khandhānaṃ": "အစုအဝေး",
    # --- abhidhamma part: numbers of kinds (rule 1: «…မျိုးဖြင့်» without ဖြင့်; pi-1 vidhena = မျိုး)
    "Ekavidhena": "တစ်မျိုး", "Duvidhena": "နှစ်မျိုး", "Tividhena": "သုံးမျိုး", "Catubbidhena": "လေးမျိုး",
    "Pañcavidhena": "ငါးမျိုး", "Chabbidhena": "ခြောက်မျိုး", "Sattavidhena": "ခုနစ်မျိုး",
    "Aṭṭhavidhena": "ရှစ်မျိုး", "Navavidhena": "ကိုးမျိုး", "Dasavidhena": "ဆယ်မျိုး",
    "Ekādasavidhena": "ဆယ့်တစ်မျိုး", "Catuvīsatividhena": "နှစ်ဆယ့်လေးမျိုး",
    "Tiṃsatividhena": "သုံးဆယ်မျိုး", "Tiṃsavidhena": "သုံးဆယ်မျိုး", "Bahuvidhena": "အမျိုးမျိုး",
    "paccayā": "အကြောင်းပြု၍",                # «X-samphassapaccayā» = «Xကို အကြောင်းပြု၍ ဖြစ်သော»
    "cakkhusamphassa": "မျက်စိ၏ တွေ့ထိမှု", "sotasamphassa": "နား၏ တွေ့ထိမှု",
    "ghānasamphassa": "နှာခေါင်း၏ တွေ့ထိမှု", "jivhāsamphassa": "လျှာ၏ တွေ့ထိမှု",
    "manosamphassa": "မနော၏ တွေ့ထိမှု",
    "sukhindriya": "သာယာမှု၏ စွမ်းရည်", "dukkhindriya": "နာကျင်မှု၏ စွမ်းရည်",
    "somanassindriya": "ဝမ်းမြောက်မှု၏ စွမ်းရည်", "domanassindriya": "စိတ်ဆင်းရဲမှု၏ စွမ်းရည်",
    "upekkhindriya": "ဥပေက္ခာ၏ စွမ်းရည်",
    "sukhindriyaṃ": "သာယာမှု၏ စွမ်းရည်", "domanassindriyaṃ": "စိတ်ဆင်းရဲမှု၏ စွမ်းရည်",
    "cakkhundriyaṃ": "မျက်စိ၏ စွမ်းရည်", "sotindriyaṃ": "နား၏ စွမ်းရည်", "ghānindriyaṃ": "နှာခေါင်း၏ စွမ်းရည်",
    "jivhindriyaṃ": "လျှာ၏ စွမ်းရည်", "kāyindriyaṃ": "ကိုယ်၏ စွမ်းရည်",
    "cakkhuviññeyyaṃ": "မျက်စိဖြင့် သိနိုင်သော", "sotaviññeyyaṃ": "နားဖြင့် သိနိုင်သော",
    "ghānaviññeyyaṃ": "နှာခေါင်းဖြင့် သိနိုင်သော", "jivhāviññeyyaṃ": "လျှာဖြင့် သိနိုင်သော",
    "kāyaviññeyyaṃ": "ကိုယ်ဖြင့် သိနိုင်သော",
    "rūpaṃ upādā": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော ရုပ်",
    "jarābhibhūtaṃ": "အိုခြင်း လွှမ်းမိုးခံရသော", "ābhibhūtaṃ": "လွှမ်းမိုးခံရသော",
    "mattaṃ": "သာ", "matto": "သာ",
    "saha": "အတူ", "sahabhu": "အတူ တည်ရှိသော", "ānuparivatti": "နောက်သို့ လိုက်ပါသော",
    "ānuparivattino": "နောက်သို့ လိုက်ပါသော",
    "āsekkhaṃ": "ကျင့်ကြံမှု ပြီးဆုံးသူ၏", "āpacaya": "လျော့ပါးခြင်း", "gāmī": "ဦးတည်သော",
    "ādhipati": "အကြီးအမှူး", "ādhipatino": "အကြီးအမှူး",
    "bhāvanāya": "ဘာဝနာ ပွားများခြင်း",
    "kenaci": "တစ်စုံတစ်ခုသော စိတ်",
    "kenaci viññeyyo": "တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော",
    "kenaci na viññeyyo": "တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော",
    "viññeyyo": "သိနိုင်သော",
    "uttaro": "ကျော်လွန်သော",               # first occurrence: lokuttaro (pi-1 uttarā)
    "arūpā": "ရုပ် မဟုတ်သော",
    "khandhā siyā": "အစုအဝေး … တစ်ခါတစ်ရံ",
    "anidassanasappaṭigho": "မမြင်နိုင်သော်လည်း ထိခိုက်မှု ရှိသော",
    "sanidassano": "မြင်နိုင်သော",
    # Mātikā items in the masculine (-o), the neuter (-aṃ) and the plural (-ā): the Mātikā value (pi-1 3 rule 12)
    "phassasampayutto": "တွေ့ထိမှုနှင့် ယှဉ်တွဲသော", "cittasampayutto": "စိတ်နှင့် ယှဉ်တွဲသော",
    "sukhāya vedanāya sampayutto": "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော",
    "dukkhāya vedanāya sampayutto": "နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော",
    "Dukkhāya vedanāya sampayutto": "နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော",
    "vedanāya sampayutto": "ခံစားမှုနှင့် ယှဉ်တွဲသော",
    "vippayutto": "ကင်းကွာသော",
    "hetuko": "အမြစ်", "sahetuko": "အမြစ် ရှိသော", "ahetuko": "အမြစ် မရှိသော",
    "kusalo": "ကုသိုလ်", "akusalo": "အကုသိုလ်",
    "abyākato": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "kāmāvacaro": "ကာမဘုံနှင့် ဆိုင်သော", "rūpāvacaro": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော",
    "arūpāvacaro": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော", "āvacaro": "ဘုံနှင့် ဆိုင်သော",
    "pariyāpanno": "ဘဝဘုံတို့၌ အကျုံးဝင်သော", "apariyāpanno": "ဘဝဘုံတို့၌ အကျုံးမဝင်သော",
    "sukhindriyasampayutto": "သာယာမှု၏ စွမ်းရည်နှင့် ယှဉ်တွဲသော",
    "vipākadhammadhammo": "အကျိုး ပေးတတ်သော",              # head = the aggregate; -dhammo has no word
    "vipākadhammadhammā": "အကျိုး ပေးတတ်သော သဘောတရား",     # pi-1 Mātikā value (pañhāpucchaka, rule 5)
    "upādāniyo": "စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော",
    "saṃkiliṭṭho": "ကိလေသာဖြင့် ညစ်နွမ်းသော", "asaṃkiliṭṭho": "ကိလေသာဖြင့် မညစ်နွမ်းသော",
    "asaṃkiliṭṭhasaṃkilesiko": "ကိလေသာဖြင့် မညစ်နွမ်းသော်လည်း ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော",
    "asaṃkiliṭṭhaasaṃkilesiko": "ကိလေသာဖြင့်လည်း မညစ်နွမ်း ကိလေသာ၏ အာရုံလည်း မဖြစ်နိုင်သော",
    "savitakkasavicāro": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော",
    "avitakkavicāramatto": "စတင်ကြံစည်မှု မရှိဘဲ ဆက်လက်သုံးသပ်မှုသာ ရှိသော",
    "avitakko": "စတင်ကြံစည်မှု မရှိသော", "savicāro": "ဆက်လက်သုံးသပ်မှု ရှိသော",
    "avicāro": "ဆက်လက်သုံးသပ်မှု မရှိသော",
    "pītisahagato": "ပီတိနှင့်အတူ ဖြစ်သော", "sukhasahagato": "သာယာမှုနှင့်အတူ ဖြစ်သော",
    "upekkhāsahagato": "ဥပေက္ခာနှင့်အတူ ဖြစ်သော",
    "pahātabbo": "ပယ်ရမည့်", "pahātabbahetuko": "ပယ်ရမည့် အမြစ် ရှိသော",
    "ācayagāmī": "စုပုံခြင်းဆီသို့ ဦးတည်သော", "apacayagāmī": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "sekkho": "ကျင့်ကြံဆဲသူ၏", "asekkho": "ကျင့်ကြံမှု ပြီးဆုံးသူ၏",
    "paritto": "အကန့်အသတ် ရှိသော", "mahaggato": "ကြီးမြတ်သော", "appamāṇo": "အတိုင်းအဆ မရှိသော",
    "parittārammaṇo": "အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော",
    "mahaggatārammaṇo": "ကြီးမြတ်သည်ကို အာရုံပြုသော",
    "appamāṇārammaṇo": "အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော",
    "hīno": "ယုတ်ညံ့သော", "majjhimo": "အလယ်အလတ်", "paṇīto": "မွန်မြတ်သော",
    "micchattaniyato": "မှားယွင်းမှု၌ ကျိန်းသေသော", "niyato": "ကျိန်းသေသော", "aniyato": "မကျိန်းသေသော",
    "uppādī": "ဖြစ်ပေါ်လာမည့်",
    "atīto": "အတိတ်", "anāgato": "အနာဂတ်", "paccuppanno": "ပစ္စုပ္ပန်",
    "atītārammaṇo": "အတိတ်ကို အာရုံပြုသော", "anāgatārammaṇo": "အနာဂတ်ကို အာရုံပြုသော",
    "paccuppannārammaṇo": "ပစ္စုပ္ပန်ကို အာရုံပြုသော",
    "ajjhatto": "မိမိ၌ ရှိသော", "bahiddho": "မိမိ၏ ပြင်ပ၌ ရှိသော",
    "ajjhattabahiddho": "မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော",
    "ajjhattārammaṇo": "မိမိ၌ ရှိသည်ကို အာရုံပြုသော",
    "bahiddhārammaṇo": "မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော",
    "ajjhattabahiddhārammaṇo": "မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသည်ကို အာရုံပြုသော",
    "lokiyo": "လောကနှင့် သက်ဆိုင်သော",
    "niyyāniko": "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော",
    "sauttaro": "ထိုထက် သာလွန်သည် ရှိသေးသော",
    "saraṇo": "ပဋိပက္ခ ရှိသော", "araṇo": "ပဋိပက္ခ မရှိသော",
    "anārammaṇo": "အာရုံ မရှိသော", "sārammaṇā": "အာရုံ ရှိသော",
    "sappaccayaṃ": "အကြောင်း ရှိသော", "acetasikaṃ": "စိတ်၏ အဖော် မဟုတ်သော",
    "ajjhattiko": "အတွင်းပိုင်း",
}

# the ten clusters: «X-sampayutto / -vippayutto», «X-vippayutta-Y-iyo» (pi-1 4 rule 14) and «X ceva X-sampayutto»
CLUSTERS = [  # stem, Burmese noun, iya positive / negative, nominatives used in «X ceva …»
    ("hetu", "အမြစ်", None, None, ("hetu", "hetū")),
    ("āsava", "စိတ်အစွန်းအထင်း", "sāsavo", "anāsavo", ("āsavo", "āsavā")),
    ("saṃyojana", "နှောင်ကြိုး", "saṃyojaniyo", "asaṃyojaniyo", ("saṃyojanañ", "saṃyojanā")),
    ("gantha", "အထုံး", "ganthaniyo", "aganthaniyo", ("gantho", "ganthā")),
    ("ogha", "ရေအလျဉ်", "oghaniyo", "anoghaniyo", ("ogho", "oghā")),
    ("yoga", "ထမ်းပိုး", "yoganiyo", "ayoganiyo", ("yogo", "yogā")),
    ("nīvaraṇa", "အတားအဆီး", "nīvaraṇiyo", "anīvaraṇiyo", ("nīvaraṇañ", "nīvaraṇā")),
    ("parāmāsa", "မှားယွင်းသော ယူဆမှု", "parāmaṭṭho", "aparāmaṭṭho", ("parāmāso", "parāmāsā")),
    ("upādāna", "စွဲလမ်းမှု", "upādāniyo", "anupādāniyo", ("upādānañ", "upādānā")),
    ("kilesa", "ကိလေသာ", "saṃkilesiko", "asaṃkilesiko", ("kileso", "kilesā")),
]
for _st, _n, _pos, _neg, _noms in CLUSTERS:
    T_KHANDHA.setdefault(_st + "sampayutto", _n + "နှင့် ယှဉ်တွဲသော")
    T_KHANDHA.setdefault(_st + "vippayutto", _n + "နှင့် ကင်းကွာသော")
    if _pos:
        T_KHANDHA.setdefault(_pos, _n + "၏ အာရုံ ဖြစ်နိုင်သော")
        T_KHANDHA.setdefault(_neg, _n + "၏ အာရုံ မဖြစ်နိုင်သော")
        T_KHANDHA.setdefault(_st + "vippayutta" + _pos, _n + "နှင့် ကင်းကွာသော … " + _n + "၏ အာရုံ ဖြစ်နိုင်သော")
        T_KHANDHA.setdefault(_st + "vippayutta" + _neg, _n + "နှင့် ကင်းကွာသော … " + _n + "၏ အာရုံ မဖြစ်နိုင်သော")
    for _nom, _end in zip(_noms, ("o", "ā")):
        _k = (_nom + "ceva " if _nom.endswith("ñ") else _nom + " ceva ") + _st + "sampayutt" + _end
        T_KHANDHA.setdefault(_k, _n + "လည်း ဖြစ် " + _n + "နှင့်လည်း ယှဉ်တွဲသော")

# the neuter -aṃ and plural -ā of every masculine -o entry (inflected Mātikā items keep the Mātikā value)
for _k, _v in list(T_KHANDHA.items()):
    if _k.endswith("o"):
        T_KHANDHA.setdefault(_k[:-1] + "aṃ", _v)
        T_KHANDHA.setdefault(_k[:-1] + "ā", _v)


def f_ajjhattam(kw, pali, my):
    """ajjhattaṃ: the qualifier of the question «rūpaṃ / viññāṇaṃ ajjhattaṃ?» = «မိမိ၌ ရှိသော» when that is the
    word's first occurrence in the segment; the item of the ajjhatta list «tesaṃ tesaṃ sattānaṃ ajjhattaṃ
    paccattaṃ …» = «မိမိ၏ အတွင်း၌ ဖြစ်သော» (pi-1 ^1-1050) when the list comes first (one sense per segment)."""
    m = re.search(r"\bajjhattaṃ\b(.)?", pali)
    if m and m.group(1) == "?":
        return "မိမိ၌ ရှိသော"
    return "မိမိ၏ အတွင်း၌ ဖြစ်သော"


def f_rupa(kw, pali, my):
    """rūpa, one sense per segment (pi-1 harmonise decision 3): the sense of the FIRST rūpa compound of the Pāli
    segment (a-rūpa compounds are skipped, they carry the keyword arūpa): rūpāvacara = the fine-material plane
    «သိမ်မွေ့သော ရုပ်», rūpāyatana / rūpadhātu = the visible object «အဆင်းအရောင်», matter «ရုပ်» elsewhere."""
    m = re.search(r"(?<![\wā])[Rr]ūp([aā]\w*)", pali)
    if m:
        rest = m.group(1)
        if rest.startswith("āvacar"):
            return "သိမ်မွေ့သော ရုပ်"
        if rest.startswith(("āyatana", "adhātu")):
            return "အဆင်းအရောင်"
    return "ရုပ်"


FUNCS = {"ajjhattam": f_ajjhattam, "rupa": f_rupa}
ALT = {}
CTX = {
}

# numbers of indriyas (pi-1 harmonise 5: a numeral keeps the text's count with its classifier «ပါး»)
NUMS = {"Eka": "တစ်", "Dvi": "နှစ်", "Dasa": "ဆယ်", "Ekādasa": "ဆယ့်တစ်", "Dvādasa": "ဆယ့်နှစ်", "Terasa": "ဆယ့်သုံး",
        "Cuddasa": "ဆယ့်လေး", "Pannarasa": "ဆယ့်ငါး", "Soḷasa": "ဆယ့်ခြောက်", "Sattarasa": "ဆယ့်ခုနစ်",
        "Aṭṭhārasa": "ဆယ့်ရှစ်", "Ekavīsati": "နှစ်ဆယ့်တစ်", "Bāvīsati": "နှစ်ဆယ့်နှစ်"}

T_5 = {
    # --- 2-219 / 2-221 list and 2-220 definitions (the indriya names: pi-1 values; the new ones the text's)
    "Bāvīsatindriyāni": "စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး",
    "Bāvīsatīnaṃ": "နှစ်ဆယ့်နှစ်ပါး", "Bāvīsatīnaṃ indriyānaṃ": "စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး",
    "aññātāvindriyaṃ": "အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည်",
    "rūpajīvitindriyaṃ": "ရုပ် ဖြစ်သော အသက်၏ စွမ်းရည်",
    "arūpajīvitindriyaṃ": "ရုပ် မဟုတ်သော အသက်၏ စွမ်းရည်",
    "jīvitaṃ": "အသက်",
    "rūpīnaṃ": "ရုပ် ဖြစ်သော",                       # «rūpīnaṃ dhammānaṃ» = «ရုပ် ဖြစ်သော သဘောတရားတို့၏»
    "itthattaṃ": "မိန်းမ ဖြစ်သော အဖြစ်", "purisattaṃ": "ယောက်ျား ဖြစ်သော အဖြစ်",
    "cetosamphassa": "စိတ်၏ တွေ့ထိမှု",
    "cetasikaṃ asātaṃ": "စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ် မကောင်းမှု",
    "dukkhaṃ vedayitaṃ": "နာကျင်သော ခံစားရခြင်း",
    "apilāpanatā": "အပေါ်ယံ မပေါ်လောခြင်း", "asammussanatā": "မမေ့လျော့ခြင်း",
    "asithilaparakkamatā": "မလျော့ရဲဘဲ ကြိုးစားခြင်း",
    "anikkhitta": "လက်မလွှတ်သော",                  # first in anikkhittachandatā «ဆန္ဒကို လက်မလွှတ်ခြင်း» (one sense)
    "dhura": "ဝန်",                                   # anikkhittadhuratā / dhurasampaggāho «ဝန်ကို …»
    "gāmopeso": "ရွာ",                                # «suñño gāmopeso» = «ဆိတ်သုဉ်းသော ရွာလည်း ဤသည်ပင်» (pi-1 gāmo)
    "dhammavicayasambojjhaṅgo": "သဘောတရားများကို စိစစ်ခြင်း ဗောဇ္ဈင်",
    "sammā": "@alt",                                   # pi-1 «မှန်ကန်သော» (sammāsati …), not the preamble's «အပြည့်အဝ»
    # --- 2-222 … 2-224 pañhāpucchaka
    "indriyā": "စွမ်းရည်",
    "No": "မဟုတ်",                                    # «No upādānā» = «စွဲလမ်းမှု မဟုတ်သော» (rule 9: the text's negative)
    "rūpā": "ရုပ်",                                   # «Sattindriyā rūpā» = «… ရုပ် ဖြစ်သော» (rule 2), not the object seen
    "sahabhū": "အတူ တည်ရှိသော",                     # as pi-1 sahabhuno (cittasahabhū «စိတ်နှင့်အတူ တည်ရှိသော»)
    "nevavipākanavipākadhammadhammā": "ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား",
    "kileso ceva kilesasampayuttañcā": "ကိလေသာလည်း ဖြစ် ကိလေသာနှင့်လည်း ယှဉ်တွဲသော",
    "āsavo ceva āsavasampayuttañcā": "စိတ်အစွန်းအထင်းလည်း ဖြစ် စိတ်အစွန်းအထင်းနှင့်လည်း ယှဉ်တွဲသော",
    "saṃyojanañceva saṃyojanasampayuttañcā": "နှောင်ကြိုးလည်း ဖြစ် နှောင်ကြိုးနှင့်လည်း ယှဉ်တွဲသော",
    "nīvaraṇañceva nīvaraṇasampayuttañcā": "အတားအဆီးလည်း ဖြစ် အတားအဆီးနှင့်လည်း ယှဉ်တွဲသော",
    "gantho ceva ganthasampayutta": "အထုံးလည်း ဖြစ် အထုံးနှင့်လည်း ယှဉ်တွဲသော",
}
for _k, _v in NUMS.items():
    T_5.setdefault(_k + "ndriyā", "စွမ်းရည် " + _v + "ပါး")
    T_5.setdefault(_k[:-1] + "indriyā", "စွမ်းရည် " + _v + "ပါး")
ALT["sammā"] = ["မှန်ကန်သော", "မှန်ကန်စွာ", "အပြည့်အဝ"]

# ---- shared by chapters 7-11 (merged into each chapter table; the chapter's own entry wins) ----------------
T_COMMON = {
    "sammā": "@alt",
    "Tena": "ထို့ကြောင့်",                            # «Tena vuccati "X"ti» = «ထို့ကြောင့် "X"ဟု ဆိုသည်»
    "ajjhattaṃ": "မိမိ၌ ရှိသော",                     # «ajjhattaṃ kāye / dhammesu» = «မိမိ၌ ရှိသော ကိုယ်၌» (as ^2-4)
    # the «upeto hoti …» list: predicate adjectives, the text's person noun «…သူ» normalised to «…သော» (rule 3,
    # as pi-1 sampajāno = ကောင်းစွာ ဆင်ခြင်သိမြင်သော)
    "upeto": "ယှဉ်သော", "samupeto": "ကောင်းစွာ ယှဉ်သော", "upapanno": "ရောက်ရှိသော", "sampanno": "ပြည့်စုံသော",
    "samannāgato": "@alt",
    # verbs (rule 4) and absolutives («…၍»)
    "āsevati": "အလေ့အကျင့် ပြုသည်", "bahulīkaroti": "အကြိမ်ကြိမ် ပြုသည်",
    "vavatthapeti": "ပိုင်းခြား သတ်မှတ်သည်", "upasaṃharati": "ညွှတ်ဆောင်သည်",
    "cittaṃ upasaṃharati": "စိတ်ကို ညွှတ်ဆောင်သည်",
    "āsevitvā": "အလေ့အကျင့် ပြု၍", "bhāvetvā": "ပွားများ၍", "bahulīkaritvā": "အကြိမ်ကြိမ် ပြု၍",
    "vavatthapetvā": "ပိုင်းခြား သတ်မှတ်၍",
    "taṃ nimittaṃ āsevati": "ထိုအမှတ်အသားကို အလေ့အကျင့် ပြုသည်",
    "taṃ nimittaṃ āsevitvā": "ထိုအမှတ်အသားကို အလေ့အကျင့် ပြု၍",
    "pajānāti": "ကွဲပြားစွာ သိသည်", "viharatīti": "နေသည်",
    # the satipaṭṭhāna formula
    "ātāpī": "ထက်သန်သော လုံ့လ ရှိသော", "ātāpo": "ထက်သန်သော လုံ့လ", "satimā": "သတိ ရှိသော",
    "vineyya": "ပယ်ဖျောက်၍", "loke": "လောက", "domanassaṃ": "စိတ်ဆင်းရဲမှု",
    "abhijjhādomanassaṃ": "သူ့ဥစ္စာကို လိုချင်ခြင်းနှင့် စိတ်ဆင်းရဲမှု",
    "abhijjhādomanassa": "သူ့ဥစ္စာကို လိုချင်ခြင်းနှင့် စိတ်ဆင်းရဲမှု",
    "loke abhijjhādomanassaṃ": "လောက၌ သူ့ဥစ္စာကို လိုချင်ခြင်းနှင့် စိတ်ဆင်းရဲမှု",
    "loke abhijjhādomanassa": "လောက၌ သူ့ဥစ္စာကို လိုချင်ခြင်းနှင့် စိတ်ဆင်းရဲမှု",
    "ānupassī": "အဖန်ဖန် ရှုသော", "anupassī": "အဖန်ဖန် ရှုသော",
    "ānupassanā": "အဖန်ဖန် ရှုခြင်း", "anupassanā": "အဖန်ဖန် ရှုခြင်း",
    "niddeso": "ဖွင့်ဆိုချက်", "ānupassanāniddeso": "အဖန်ဖန် ရှုခြင်းကို ဖွင့်ဆိုချက်",
    "paṭṭhāna": "ပဋ္ဌာန်", "paṭṭhānā": "ပဋ္ဌာန်", "paṭṭhānānaṃ": "ပဋ္ဌာန်", "paṭṭhānaṃ": "ပဋ္ဌာန်",
    "Satipaṭṭhāna": "သတိပဋ္ဌာန်", "satipaṭṭhānā": "သတိပဋ္ဌာန်", "satipaṭṭhānānaṃ": "သတိပဋ္ဌာန်",
    "satipaṭṭhānaṃ": "သတိပဋ္ဌာန်",
    # the nīvaraṇas and the bojjhaṅgas (2-367; the bojjhaṅga names below for every case)
    "santaṃ": "ရှိနေသော", "kāmacchandaṃ": "ကာမကို လိုလားမှု",
    "byāpādaṃ": "ဖျက်ဆီးလိုစိတ်", "thinamiddhaṃ": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု",
    "uddhaccakukkuccaṃ": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု", "vicikicchaṃ": "ယုံမှားမှု",
    "uppādo": "ဖြစ်ပေါ်ခြင်း", "anuppādo": "မဖြစ်ပေါ်ခြင်း", "pāripūrī": "ပြည့်စုံခြင်း",
    "anuppannassa": "မဖြစ်ပေါ်သေးသော", "uppannassa": "ဖြစ်ပေါ်ပြီးသော", "pahīnassa": "ပယ်ပြီးသော",
    "vicaya": "စိစစ်ခြင်း", "dhammavicaya": "သဘောတရားများကို စိစစ်ခြင်း",
    # the abhidhamma frame (2-375 …: the pi-1 jhāna formula; pi-1 values where the text has them)
    "ābhiññaṃ": "ထူးကဲစွာ သိခြင်း",                   # fragment of dandhābhiññaṃ (pi-1 abhiññaṃ)
    "paṭipadaṃ dandhābhiññaṃ": "ကျင့်စဉ် … ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "ကျင့်စဉ် ခက်ခဲသော ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    "apacayagāmiṃ": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော", "apacayagāmino": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "Avasesā": "ကြွင်းသော",                           # text «ကြွင်းသော သဘောတရားများ» (pi-1 «ကြွင်းကျန်သော» not here)
    "Anidassanaappaṭighā": "မမြင်နိုင် ထိခိုက်မှုလည်း မရှိသော",   # text «မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော» (rule 6)
    "appaṭighā": "ထိခိုက်မှု မရှိသော",
}
ALT["samannāgato"] = ["အပြည့်အဝ ပြည့်စုံသော", "ပြည့်စုံသော"]
BOJJH = {"sati": "သတိ", "dhammavicaya": "သဘောတရားများကို စိစစ်ခြင်း", "vīriya": "ဝီရိယ", "pīti": "ပီတိ",
         "passaddhi": "ငြိမ်းအေးခြင်း", "samādhi": "သမာဓိ", "upekkhā": "ဥပေက္ခာ"}
for _st, _v in BOJJH.items():
    for _end in ("o", "aṃ", "a", "assa", "ā"):
        T_COMMON.setdefault(_st + "sambojjhaṅg" + _end, _v + " ဗောဇ္ဈင်")
for _end in ("o", "aṃ", "a", "assa", "ā"):
    T_COMMON.setdefault("sambojjhaṅg" + _end, "ဗောဇ္ဈင်")
# the three «X / anuppanna- / uppanna- / pahīna- X», «X uppādo» shapes of 2-367
for _kw, _v in (("kāmacchandassa", "ကာမကို လိုလားမှု"), ("vicikicchāya", "ယုံမှားမှု"),
                ("satisambojjhaṅgassa", "သတိ ဗောဇ္ဈင်"), ("upekkhāsambojjhaṅgassa", "ဥပေက္ခာ ဗောဇ္ဈင်")):
    _f = _kw.endswith("āya")
    T_COMMON[("anuppannāya " if _f else "anuppannassa ") + _kw] = "မဖြစ်ပေါ်သေးသော " + _v
    T_COMMON[("uppannāya " if _f else "uppannassa ") + _kw] = "ဖြစ်ပေါ်ပြီးသော " + _v
    T_COMMON[("pahīnāya " if _f else "pahīnassa ") + _kw] = "ပယ်ပြီးသော " + _v
    T_COMMON[_kw + " uppādo"] = _v + "၏ ဖြစ်ပေါ်ခြင်း"
T_COMMON["anuppannāya vicikicchāya uppādo"] = "မဖြစ်ပေါ်သေးသော ယုံမှားမှု၏ ဖြစ်ပေါ်ခြင်း"
T_COMMON["satisambojjhaṅgassa bhāvanāya pāripūrī"] = "သတိ ဗောဇ္ဈင်၏ ပွားများခြင်းဖြင့် ပြည့်စုံခြင်း"
# the four objects, each with the three qualifiers (2-355 …): «ajjhattaṃ kāye» = «မိမိ၌ ရှိသော ကိုယ်»
for _o, _v, _a in (("kāye", "ကိုယ်", "kāyā"), ("vedanāsu", "ခံစားမှု", "vedanā"), ("citte", "စိတ်", "cittā"),
                   ("dhammesu", "သဘောတရား", "dhammā")):
    T_COMMON[_o] = _v
    T_COMMON["ajjhattaṃ " + _o] = "မိမိ၌ ရှိသော " + _v
    T_COMMON["bahiddhā " + _o] = "မိမိ၏ ပြင်ပ၌ ရှိသော " + _v
    T_COMMON["ajjhattabahiddhā " + _o] = "မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော " + _v
    _n = _a
    T_COMMON[_n + "nupassī"] = _v + "ကို အဖန်ဖန် ရှုသော"
    T_COMMON[_n + "nupassī viharati"] = _v + "ကို အဖန်ဖန် ရှုသူ ဖြစ်လျက် နေသည်"
    T_COMMON[(_n + "nupassanā").capitalize()] = _v + "ကို အဖန်ဖန် ရှုခြင်း"
    T_COMMON[(_n + "nupassanāniddeso").capitalize()] = _v + "ကို အဖန်ဖန် ရှုခြင်းကို ဖွင့်ဆိုချက်"
T_COMMON["vedanāsu vedanānupassī"] = "ခံစားမှုတို့၌ ခံစားမှုကို အဖန်ဖန် ရှုသော"
T_COMMON["vedanāsu cittaṃ"] = "ခံစားမှုတို့၌ စိတ်"

T_7 = {
    "chandaṃ": "လိုလားမှု",                         # fragment of kāmacchandaṃ «ကာမကို လိုလားမှု» (2-367)
    # headings (the heading's own Burmese, pi-1 decision 4)
    "Satipaṭṭhānavibhaṅgo": "သတိပဋ္ဌာန်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း",
    # 2-356 the parts of the body (the text's list; mutta has no word in it)
    "pāda": "ခြေ", "talā": "ဖဝါး", "kesamatthakā": "ဆံပင်ဖျား", "matthakā": "ဖျား",
    "pariyantaṃ": "ဝန်းရံထားသော",                  # tacapariyantaṃ «အရေဖြင့် ဝန်းရံထားသော»
    "pakārassa": "အမျိုး",                           # nānappakārassa «အမျိုးမျိုးသော»
    "asucino": "မစင်ကြယ်သည့်အရာ", "paccavekkhati": "ဆင်ခြင်သည်",
    "atthissa": "ထိုသူ၏ … ရှိသည်",                  # «atthissa kāye …» = «ထိုသူ၏ ကိုယ်၌ … ရှိ၏»
    "kāye kesā": "ကိုယ်၌ ဆံပင်",
    "kesā": "ဆံပင်", "lomā": "မွေးညင်း", "nakhā": "ခြေသည်းလက်သည်း", "dantā": "သွား", "taco": "အရေ",
    "nhāru": "အကြော", "aṭṭhi": "အရိုး", "miñjaṃ": "ခြင်ဆီ", "vakkaṃ": "ကျောက်ကပ်", "hadayaṃ": "နှလုံး",
    "yakanaṃ": "အသည်း", "kilomakaṃ": "အမြှေး", "pihakaṃ": "အဖျဉ်း", "papphāsaṃ": "အဆုတ်", "antaṃ": "အူမ",
    "antaguṇaṃ": "အူသိမ်", "udariyaṃ": "အစာသစ်", "karīsaṃ": "အစာဟောင်း", "pittaṃ": "သည်းခြေ",
    "semhaṃ": "သလိပ်", "pubbo": "ပြည်", "lohitaṃ": "သွေး", "sedo": "ချွေး", "medo": "အဆီခဲ", "assu": "မျက်ရည်",
    "vasā": "အဆီကြည်", "kheḷo": "တံတွေး", "siṅghāṇikā": "နှပ်", "lasikā": "အစေး",
    "mutta": NONE,                                  # the text's list ends «… နှပ်၊ အစေး ရှိ၏»: no word for urine
    # 2-357 … 2-362 word commentary
    "Iriyati": "လှုပ်ရှားသည်", "vattati": "လည်ပတ်သည်", "pāleti": "စောင့်ရှောက်သည်", "yapeti": "ဆက်လက် ဖြစ်နေသည်",
    "yāpeti": "ဆက်လက် ရှင်သန်စေသည်", "carati": "ကျင်လည်သည်",
    "vīriyārambho": "ဝီရိယ စတင်ခြင်း",
    "paṭivinītā": "လုံးဝ ပယ်ဖျောက်ပြီးသော", "santā": "ငြိမ်းပြီးသော", "samitā": "ငြိမ်သက်ပြီးသော",
    "vūpasantā": "ကောင်းစွာ ငြိမ်သက်ပြီးသော", "atthaṅgatā": "ကွယ်ပျောက်ပြီးသော",
    "appitā": "ချုပ်ငြိမ်းစေပြီးသော", "byappitā": "အပြီးတိုင် ချုပ်ငြိမ်းစေပြီးသော",
    "sositā": "ခြောက်ခန်းစေပြီးသော", "visositā": "လုံးဝ ခြောက်ခန်းစေပြီးသော", "byantīkatā": "အဆုံးသတ်ပြီးသော",
    "asātaṃ dukkhaṃ": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော",
    "asātaṃ dukkhaṃ vedayitaṃ": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားရခြင်း",
    "asātā dukkhā vedanā": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားမှု",
    # 2-363 feelings
    "vedayamāno": "ခံစားရလျှင်", "vedayāmī": "ငါ ခံစားရသည်", "vedayatī": "ခံစားသည်",
    "sāmisaṃ": "ကာမဂုဏ်နှင့် စပ်သော", "nirāmisaṃ": "ကာမဂုဏ်နှင့် မစပ်သော",
    # 2-365 minds
    "rāgaṃ": "ရာဂ", "dosaṃ": "ဒေါသ",
    "samāhitaṃ": "တည်ကြည်သော", "asamāhitaṃ": "မတည်ကြည်သော", "saṃkhittaṃ": "တွန့်ဆုတ်နေသော",
    "vikkhittaṃ": "ပျံ့လွင့်နေသော", "amahaggataṃ": "မကြီးမြတ်သော", "vimuttaṃ": "လွတ်မြောက်သော",
    "avimuttaṃ": "မလွတ်မြောက်သော", "anuttaraṃ": "ထိုထက် သာလွန်သည် မရှိသော",
}
# 2-363 «(sāmisaṃ / nirāmisaṃ) sukhaṃ / dukkhaṃ (vedanaṃ)»
for _q, _qv in (("", ""), ("sāmisaṃ ", "ကာမဂုဏ်နှင့် စပ်သော "), ("nirāmisaṃ ", "ကာမဂုဏ်နှင့် မစပ်သော ")):
    for _f, _fv in (("sukhaṃ", "သာယာသော"), ("dukkhaṃ", "နာကျင်သော")):
        if _q:
            T_7[_q + _f] = _qv + _fv
        T_7[_q + _f + " vedanaṃ"] = _qv + _fv + " ခံစားမှု"
# 2-365 «X vā cittaṃ» = «X စိတ်ကိုဖြစ်စေ» (vā = the text's «ဖြစ်စေ»)
for _q, _qv in (("sarāgaṃ", "ရာဂ ရှိသော"), ("vītarāgaṃ", "ရာဂ ကင်းသော"), ("sadosaṃ", "ဒေါသ ရှိသော"),
                ("vītadosaṃ", "ဒေါသ ကင်းသော"), ("samohaṃ", "မောဟ ရှိသော"), ("vītamohaṃ", "မောဟ ကင်းသော"),
                ("saṃkhittaṃ", "တွန့်ဆုတ်နေသော"), ("vikkhittaṃ", "ပျံ့လွင့်နေသော"), ("mahaggataṃ", "ကြီးမြတ်သော"),
                ("amahaggataṃ", "မကြီးမြတ်သော"), ("sauttaraṃ", "ထိုထက် သာလွန်သည် ရှိသေးသော"),
                ("anuttaraṃ", "ထိုထက် သာလွန်သည် မရှိသော"), ("samāhitaṃ", "တည်ကြည်သော"),
                ("asamāhitaṃ", "မတည်ကြည်သော"), ("vimuttaṃ", "လွတ်မြောက်သော"), ("avimuttaṃ", "မလွတ်မြောက်သော")):
    T_7[_q + " vā cittaṃ"] = _qv + " စိတ်ကိုဖြစ်စေ"
CTX["2-363"] = {"sukhaṃ": "သာယာသော", "dukkhaṃ": "နာကျင်သော"}     # adjectives of vedanaṃ here (one sense)
T_8 = {
    "Sammappadhānavibhaṅgo": "မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်းများကို ခွဲခြမ်းစိတ်ဖြာခြင်း",
    "padhāna": "ကြိုးပမ်းအားထုတ်ခြင်း", "padhānā": "ကြိုးပမ်းအားထုတ်ခြင်း",
    "padhānānaṃ": "ကြိုးပမ်းအားထုတ်ခြင်း",
    "sammappadhānā": "မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း", "sammappadhānaṃ": "မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း",
    "sammappadhānānaṃ": "မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း",
    "anuppannānaṃ": "မဖြစ်ပေါ်သေးသော", "anuppādāya": "မဖြစ်ပေါ်ရန်", "dhammānaṃ": "သဘောတရား",
    "chandaṃ": "ဆန္ဒ", "chando": "ဆန္ဒ", "chandikatā": "ဆန္ဒ ပြုခြင်း",
    "kattu": "ပြုလုပ်", "kamyatā": "လိုခြင်း",       # kattukamyatā «ပြုလုပ်လိုခြင်း» (one word: its two parts)
    "kusalo dhammacchando": "ကုသိုလ် သဘောတရားကို လိုလားသော ဆန္ဒ",
    "chandaṃ janeti": "ဆန္ဒကို ဖြစ်စေသည်", "Imaṃ chandaṃ janeti": "ဤဆန္ဒကို ဖြစ်စေသည်",
    "sañjaneti": "ကောင်းစွာ ဖြစ်စေသည်", "samuṭṭhapeti": "ကောင်းစွာ ထပေါ်စေသည်", "nibbatteti": "ပေါ်ထွက်စေသည်",
    "vīriyaṃ ārabhati": "ဝီရိယကို စတင်သည်", "Imaṃ vīriyaṃ ārabhati": "ဤဝီရိယကို စတင်သည်",
    "samārabhati": "ကောင်းစွာ စတင်သည်",
    "Imaṃ cittaṃ paggaṇhāti": "ဤစိတ်ကို မြှင့်တင်သည်", "sampaggaṇhāti": "ကောင်းစွာ မြှင့်တင်သည်",
    "upatthambheti": "ထောက်ပံ့သည်", "paccupatthambheti": "အထပ်ထပ် ထောက်ပံ့သည်",
    # the quoted verbs «X-tīti» = the verb (rule 4; text «X၏ ဟူသည်»), as viharatīti
    "Vāyamatīti": "အားထုတ်သည်", "Padahatīti": "ကြိုးပမ်းသည်", "paggaṇhātīti": "မြှင့်တင်သည်",
    "cittaṃ paggaṇhātīti": "စိတ်ကို မြှင့်တင်သည်", "janetīti": "ဖြစ်စေသည်", "Chandaṃ janetīti": "ဆန္ဒကို ဖြစ်စေသည်",
    "ārabhatīti": "စတင်သည်", "vīriyaṃ ārabhatīti": "ဝီရိယကို စတင်သည်",
    "vepullaṃ": "ပြန့်ပြောခြင်း", "asammoso": "မပျောက်ပျက်ခြင်း",
}
T_9 = {
    "Iddhipāda": "ဣဒ္ဓိပါဒ်", "pāda": "ပါဒ်", "pādā": "ပါဒ်", "pādānaṃ": "ပါဒ်",    # «ဣဒ္ဓိပါဒ်» (one word)
    "iddhipādo": "ဣဒ္ဓိပါဒ်", "iddhipādā": "ဣဒ္ဓိပါဒ်", "iddhipādaṃ": "ဣဒ္ဓိပါဒ်", "iddhipādānaṃ": "ဣဒ္ဓိပါဒ်",
    "Chandiddhipādo": "ဆန္ဒ ဣဒ္ဓိပါဒ်", "Vīriyiddhipādo": "ဝီရိယ ဣဒ္ဓိပါဒ်", "Cittiddhipādo": "စိတ် ဣဒ္ဓိပါဒ်",
    "Vīmaṃsiddhipādo": "စုံစမ်းဆင်ခြင်မှု ဣဒ္ဓိပါဒ်",
    "chandasamādhi": "ဆန္ဒ သမာဓိ", "vīriyasamādhi": "ဝီရိယ သမာဓိ", "cittasamādhi": "စိတ် သမာဓိ",
    "vīmaṃsāsamādhi": "စုံစမ်းဆင်ခြင်မှု သမာဓိ", "Vīmaṃsaṃ": "စုံစမ်းဆင်ခြင်မှု",
    "padhānasaṅkhāra": "ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှု",
    "padhānasaṅkhāro": "ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှု",
    "padhānasaṅkhārā": "ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှု", "saṅkhāro": "ပြုပြင်ဖန်တီးမှု",
    "samannāgataṃ": "အပြည့်အဝ ပြည့်စုံသော",
    "samādhipadhānasaṅkhārasamannāgataṃ": "သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှုတို့ဖြင့် အပြည့်အဝ ပြည့်စုံသော",
    "samādhipadhānasaṅkhārasamannāgato": "သမာဓိနှင့် ကြိုးပမ်းအားထုတ်ခြင်း ပြုပြင်ဖန်တီးမှုတို့ဖြင့် အပြည့်အဝ ပြည့်စုံသော",
    "samannāgataṃ iddhipādaṃ": "အပြည့်အဝ ပြည့်စုံသော ဣဒ္ဓိပါဒ်",
    "iddhipādaṃ bhāveti": "ဣဒ္ဓိပါဒ်ကို ပွားများသည်", "iddhipādaṃ bhāvetī": "ဣဒ္ဓိပါဒ်ကို ပွားများသည်",
    "adhipatiṃ": "အကြီးအမှူး", "samādhiṃ": "သမာဓိ", "labhati": "ရသည်", "labhati samādhiṃ": "သမာဓိကို ရသည်",
    "ekaggataṃ": "စူးစိုက်မှု", "cittassekaggataṃ": "စိတ်၏ စူးစိုက်မှု",          # pi-1 ekaggatā
    "abhisaññahitvā": "ပေါင်းစု၍",                    # = abhisaññūhitvā (sample)
    "ekajjhaṃ": "တစ်စုတည်း",                          # fragment of tadekajjhaṃ
    "saṅkhyaṃ": "အမည်", "gacchati": "ရသည်", "saṅkhyaṃ gacchati": "အမည် ရသည်",   # text «… ဟူ၍သာ အမည် ရ၏»
    "tveva": "ဟူ၍သာ",                                 # (i)ti + eva
    # 2-434 the synonyms of iddhi
    "samiddhi": "ကောင်းစွာ ပြည့်စုံခြင်း", "ijjhanā": "ပြီးမြောက်ခြင်း", "samijjhanā": "ကောင်းစွာ ပြီးမြောက်ခြင်း",
    "paṭilābho": "ထပ်မံ ရခြင်း", "patti": "ရောက်ခြင်း", "sampatti": "ကောင်းစွာ ရောက်ခြင်း",
    "sacchikiriyā": "မျက်မှောက်ပြုခြင်း", "upasampadā": "ပြည့်စုံစွာ ရရှိခြင်း",
    "viññāṇakhandho": "သိစိတ် အစုအဝေး",
    # 2-465 pañhāpucchaka
    "na hetu": "အမြစ် မဟုတ်သော", "acetasiko": "စိတ်၏ အဖော် မဟုတ်သော", "visaṃsaṭṭho": "မရောနှောသော",
}
for _st, _v in (("chand", "ဆန္ဒ"), ("vīriy", "ဝီရိယ"), ("citt", "စိတ်"), ("vīmaṃs", "စုံစမ်းဆင်ခြင်မှု")):
    T_9[_st + "iddhipādo"] = _v + " ဣဒ္ဓိပါဒ်"
T_10 = {
    "Bojjhaṅga": "ဗောဇ္ဈင်", "bojjhaṅgā": "ဗောဇ္ဈင်", "bojjhaṅgānaṃ": "ဗောဇ္ဈင်",   # the text's term (pi-1 ^1-? once
                                                                                    # «သိမြင်ခြင်း၏ အင်္ဂါ», not here)
    # 2-467 the sutta definitions
    "paramena": "အမြတ်ဆုံးသော", "nepakkena": "ရင့်ကျက်သော ဉာဏ်",   # «paramena satinepakkena» = «အမြတ်ဆုံးသော
                                                                    # သတိနှင့် ရင့်ကျက်သော ဉာဏ်ဖြင့်»
    "cirakatampi": "ကြာမြင့်စွာ ပြုခဲ့သည်ကိုလည်း",   # -pi = the text's «လည်း»
    "saritā": "အောက်မေ့သော", "anussaritā": "အဖန်ဖန် အောက်မေ့သော",   # agent nouns, «…သူ» → «…သော» (rule 3)
    "viharanto": "နေစဉ်",                             # present participle = the text's temporal clause
    "paññāya": "ပညာ",
    "pavicinati": "သေချာစွာ စိစစ်သည်", "pavicarati": "သေချာစွာ သုံးသပ်သည်",
    "parivīmaṃsamāpajjati": "ပတ်လည် စူးစမ်းဆန်းစစ်ခြင်းသို့ ရောက်သည်", "āpajjati": "ရောက်သည်",
    "āraddhaṃ": "စတင်ပြီးသော",                        # «… ဝီရိယကို စတင်ပြီး ဖြစ်၏»
    "asallīnaṃ": "မတွန့်ဆုတ်သော", "nirāmisā": "ကာမဂုဏ်နှင့် မစပ်သော",
    "Pītimanassa": "ပီတိ ရှိသော စိတ် ရှိသော",         # «ပီတိ ရှိသော စိတ် ရှိသူ၏»
    "kāyopi": "ကိုယ်လည်း", "passambhati": "ငြိမ်းအေးသည်", "sukhino": "သာယာမှု ရှိသော",
    "ajjhupekkhitā": "ဥပေက္ခာဖြင့် လွန်စွာ ရှုသော",
    # 2-469
    "abhiññāya": "ထူးကဲစွာ သိခြင်း", "sambodhāya": "ကောင်းစွာ သိမြင်ခြင်း",
    "saṃvattati": "အတွက် ဖြစ်သည်",                   # «… နိဗ္ဗာန်အတွက် ဖြစ်၏» (conduces to)
    "tadapi": "အရာသည်လည်း",                          # «yadapi … tadapi» = «… ဖြစ်သည့်အရာသည်လည်း»
    # 2-471
    "sambojjhaṅgaṃ bhāveti": "ဗောဇ္ဈင်ကို ပွားများသည်",
    "viveka": "ကင်းဆိတ်ခြင်း", "virāga": "ပြယ်ပျောက်ခြင်း", "vossagga": "စွန့်လွှတ်ခြင်း", "pariṇāmiṃ": "ညွတ်သော",
    # 2-474 …
    "paṭippassambhanā": "လုံးဝ အေးချမ်းခြင်း", "paṭippassambhitattaṃ": "လုံးဝ အေးချမ်းသွားသော အဖြစ်",
    "upekkhanā": "ဥပေက္ခာဖြင့် ရှုခြင်း", "ajjhupekkhanā": "ဥပေက္ခာဖြင့် လွန်စွာ ရှုခြင်း",
    "majjhattatā": "အလယ်အလတ်၌ တည်ခြင်း",
    # 2-485
    "Lokuttarā": "လောကကို ကျော်လွန်သော", "na hetū": "အမြစ် မဟုတ်သော",
}
def f_maggo(kw, pali, my):
    """aṭṭhaṅgiko / pañcaṅgiko maggo = «အင်္ဂါ ရှစ်ပါး / ငါးပါး ရှိသော မဂ်»; where Ariyo stands between
    («… ရှိသော အရိယာ မဂ်», ^2-486 / 2-488 / 2-504) the gap is marked « … » (pi-1 rule 10)."""
    n = "ရှစ်ပါး" if low(kw).startswith("aṭṭh") else "ငါးပါး"
    v = "အင်္ဂါ " + n + " ရှိသော"
    return v + " မဂ်" if v + " မဂ်" in my else v + " … မဂ်"


FUNCS["maggo"] = f_maggo
T_11 = {
    "Maggaṅga": "မဂ်၏ အင်္ဂါ", "maggaṅgā": "မဂ်၏ အင်္ဂါ", "maggaṅgānaṃ": "မဂ်၏ အင်္ဂါ", "aṅga": "အင်္ဂါ",
    "aṅgānaṃ": "အင်္ဂါ",
    "aṭṭhaṅgiko maggo": "@maggo", "pañcaṅgiko maggo": "@maggo",
    "seyyathidaṃ": "ဆိုလိုသည်မှာ", "Ariyo": "အရိယာ",
    # 2-487 the definitions of the eight factors
    "Nekkhamma": "ကာမမှ ထွက်မြောက်ခြင်း", "abyāpāda": "ဖျက်ဆီးလိုစိတ် မရှိခြင်း", "avihiṃsā": "ညှဉ်းပန်းမှု မရှိခြင်း",
    "dukkhasamudaye": "ဒုက္ခ ဖြစ်ပေါ်ခြင်း",
    "Musā": "မုသား", "Musāvādā": "မုသား ပြောခြင်း", "Musāvādā veramaṇī": "မုသား ပြောခြင်းမှ ကင်းဝေးခြင်း",
    "pisuṇāya": "ကုန်းတိုက်သော", "pharusāya": "ကြမ်းတမ်းသော",
    "samphappalāpā": "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား",
    "Pāṇātipātā": "သူ့အသက်ကို သတ်ခြင်း", "ātipātā": "သတ်ခြင်း",
    "Pāṇātipātā veramaṇī": "သူ့အသက်ကို သတ်ခြင်းမှ ကင်းဝေးခြင်း",
    "ādānā": "ယူခြင်း", "adinnādānā veramaṇī": "မပေးသည်ကို ယူခြင်းမှ ကင်းဝေးခြင်း",
    "micchācārā": "မှားယွင်းစွာ ကျင့်ခြင်း",
    "kāmesumicchācārā veramaṇī": "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းမှ ကင်းဝေးခြင်း",
    "sāvako": "တပည့်", "pahāya": "ပယ်၍",
    "jīvikaṃ": "အသက်", "kappeti": "မွေးသည်",       # «jīvikaṃ kappeti» = «အသက်မွေး၏» (one verb: its two parts)
    "dhammesu dhammānupassī": "သဘောတရားတို့၌ သဘောတရားကို အဖန်ဖန် ရှုသော",
    "pītisukhaṃ": "ပီတိနှင့် သာယာမှု ရှိသော",        # jhāna «… ပီတိနှင့် သာယာမှု ရှိသော ပထမ ဈာန်»
    "sukhavihārī": "သာယာစွာ နေသော",
    "vitakkavicārānaṃ": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု",
    "vitakkavicārānaṃ vūpasamā": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်း",
    # 2-489
    "diṭṭhiṃ": "အယူ", "saṅkappaṃ": "ကြံစည်မှု", "vācaṃ": "စကား", "ājīvaṃ": "အသက်မွေးမှု", "vāyāmaṃ": "အားထုတ်မှု",
    "satiṃ": "သတိ",
    # 2-492 …
    "kāyaduccaritehi": "ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်", "vacīduccaritehi": "နှုတ်ဖြင့် ပြုသော ဒုစရိုက်",
    "akiriyā": "မပြုခြင်း", "akaraṇaṃ": "မပြုလုပ်ခြင်း", "anajjhāpatti": "မကျူးလွန်ခြင်း",
    "anatikkamo": "မကျော်လွန်ခြင်း",
    "vāyāmena": "အားထုတ်မှု", "saṅkappena": "ကြံစည်မှု", "satiyā": "သတိ",
    "Araṇāti": "ပဋိပက္ခ မရှိသော",
}
CTX["2-487"] = {"ajjhattaṃ": "မိမိ၌"}             # the jhāna adverb «ajjhattaṃ sampasādanaṃ» (pi-1 value)

for _t in (T_9, T_10, T_11):                  # the sammappadhāna formula recurs in 9-11
    for _k, _v in T_8.items():
        if not _k.endswith("vibhaṅgo"):
            _t.setdefault(_k, _v)
for _t in (T_7, T_8, T_9, T_10, T_11):
    for _k, _v in T_COMMON.items():
        _t.setdefault(_k, _v)
T_5.setdefault("sammā", "@alt")

SECTIONS = {
    "preamble": T_PREAMBLE,                 # approved sample tables (copied unchanged; shared lookup)
    "1-khandhavibhango": T_KHANDHA,
    "5-indriyavibhango": T_5,
    "7-satipatthanavibhango": T_7,
    "8-sammappadhanavibhango": T_8,
    "9-iddhipadavibhango": T_9,
    "10-bojjhangavibhango": T_10,
    "11-maggangavibhango": T_11,
}
CHAPTERS = ["5-indriyavibhango", "7-satipatthanavibhango", "8-sammappadhanavibhango", "9-iddhipadavibhango",
            "10-bojjhangavibhango", "11-maggangavibhango"]


# =====================================================================================================
# rules (written to map-table.md)
# =====================================================================================================
RULES = """## Rules

**Binding and unchanged:** the approved pi-1 Burmese mapping rules (pi-1 `map-table.md` rules 1–11 and the agreed
later rules: absolutives keep «…၍»; «samaye X» = «အချိန်၌ ရှိသော X»; bare relatives = (no direct equivalent) where the
text builds the clause with «ရှိသော / ရှိသမျှ»; one sense per segment; no « / » alternatives) and the approved pi-2
sample (`map-table.md`, N1–N11, the six deliberate differences). The sample's tables T_PREAMBLE / T_KHANDHA, its compose
rules, context functions and verifier are copied unchanged; pi-1 values are reused where they occur in the segment.
The value is always the word or phrase of THAT segment's final pi-2 Burmese.

## NEW rules in chapters 5, 7–11 (for the user's review)

M1. **Counts of indriyas** (pi-1 harmonise 5, the text's count with «ပါး»): Dasindriyā … Ekavīsatindriyā,
    Bāvīsatindriyāni = «စွမ်းရည် Nပါး» (Dasindriyā = စွမ်းရည် ဆယ်ပါး); Bāvīsatīnaṃ = နှစ်ဆယ့်နှစ်ပါး; bare indriyā =
    စွမ်းရည်. The sample's subject + predicate compose (pi-1 5 rule 21) is extended to indriyā: indriyā siyā =
    «စွမ်းရည် … တစ်ခါတစ်ရံ», indriyā hetū = «စွမ်းရည် … အမြစ်», indriyā sappaṭighā = «စွမ်းရည် … ထိခိုက်မှု ရှိသော».
M2. **Bare negatives**: No («No upādānā» = «စွဲလမ်းမှု မဟုတ်သော») = «မဟုတ်», the text's negative word (na keeps pi-1
    «မ»); na hetu / na hetū = «အမြစ် မဟုတ်သော» (rule 5 negative attributive). CEVA strings in -o / -añcā
    (kileso ceva kilesasampayuttañcā …) take the sample's CEVA value «Xလည်း ဖြစ် Xနှင့်လည်း ယှဉ်တွဲသော».
M3. **Predicate adjectives the text builds as person nouns «…သူ»** (upeto, samupeto, upapanno, sampanno, samannāgato,
    ātāpī, satimā, (k)anupassī, saritā, anussaritā, sukhavihārī, Pītimanassa, sukhino, ajjhupekkhitā,
    samādhipadhānasaṅkhārasamannāgato) = «…သော» (pi-1 rule 3, as pi-1 sampajāno = ကောင်းစွာ ဆင်ခြင်သိမြင်သော).
    A phrase with viharati keeps the text's form inside and normalises only the verb ending (rule 1 / rule 4):
    kāyānupassī viharati = «ကိုယ်ကို အဖန်ဖန် ရှုသူ ဖြစ်လျက် နေသည်».
M4. **Quoted verbs and Tena**: «X-tīti» (viharatīti, Vāyamatīti, Padahatīti, janetīti, paggaṇhātīti, ārabhatīti …)
    = the verb in «သည်» (rule 4; text «X၏ ဟူသည်»); Tena («Tena vuccati») = «ထို့ကြောင့်».
M5. **Present participles** with no attributive form in the text keep its temporal clause: vedayamāno = «ခံစားရလျှင်»,
    viharanto = «နေစဉ်». vedayāmī keeps its subject: «ငါ ခံစားရသည်».
M6. **ajjhattaṃ with an object** (ajjhattaṃ kāye / vedanāsu / citte / dhammesu, 7 and 10) = «မိမိ၌ ရှိသော» (the
    sample's question value), the pairs = «မိမိ၌ ရှိသော ကိုယ်», «မိမိ၏ ပြင်ပ၌ ရှိသော ကိုယ်», «မိမိ၌နှင့် မိမိ၏ ပြင်ပ၌ ရှိသော
    ကိုယ်»; the jhāna adverb «ajjhattaṃ sampasādanaṃ» (^2-487) keeps pi-1 «မိမိ၌» (CTX).
M7. **vā and -pi**: «X vā cittaṃ» = «X စိတ်ကိုဖြစ်စေ» (vā = the text's «ဖြစ်စေ», kept like the sample's «လည်း» in
    yaṃ vā panaññampi); -pi = «လည်း» (cirakatampi = ကြာမြင့်စွာ ပြုခဲ့သည်ကိုလည်း, kāyopi = ကိုယ်လည်း, tadapi =
    အရာသည်လည်း, the correlative of «… ဖြစ်သည့်အရာသည်လည်း»).
M8. **A fragment inside one Burmese word** = that part of the word (as pi-1 rule 8 fragments): paṭṭhāna / paṭṭhānā =
    ပဋ္ဌာန် (သတိပဋ္ဌာန်), pāda / pādā = ပါဒ် (ဣဒ္ဓိပါဒ်), kattu / kamyatā = ပြုလုပ် / လိုခြင်း (ပြုလုပ်လိုခြင်း), jīvikaṃ /
    kappeti = အသက် / မွေးသည် (အသက်မွေး၏), miñjaṃ = ခြင်ဆီ (ရိုးတွင်းခြင်ဆီ), matthakā = ဖျား (ဆံပင်ဖျား), pāda / talā
    = ခြေ / ဖဝါး (ခြေဖဝါး, ch. 7), ātipātā = သတ်ခြင်း, ādānā = ယူခြင်း, ābhiññaṃ = ထူးကဲစွာ သိခြင်း (pi-1 abhiññaṃ).
M9. **Perfect participle lists** (vinītā … byantīkatā, ^2-362 / 364 / 366 / 373) = «…ပြီးသော» (pi-1 abbhatthaṅgatā =
    လုံးဝ ကွယ်ပျောက်ပြီးသော). Presence check, one more ending: «Xပြီးသော» is accepted against the text's predicate
    «Xပြီး ဖြစ်ကြ၏» (check «perf-pred», used only for byantīkatā, the last item of the list, 4×).
M10. **Ariyo between attribute and head**: aṭṭhaṅgiko maggo = «အင်္ဂါ ရှစ်ပါး ရှိသော မဂ်»; where the text puts အရိယာ
    between (^2-486, 2-488, 2-504) the gap is marked: «အင်္ဂါ ရှစ်ပါး ရှိသော … မဂ်» (pi-1 rule 10).
M11. **mutta = (no direct equivalent)** (^2-356): the text's list of the body parts has 30 words for the 31 Pāli items;
    urine has no word («… တံတွေး၊ နှပ်၊ အစေး ရှိ၏», three times). Translation not edited: reported.
M12. **sammā** = pi-1 «မှန်ကန်သော» (sammādiṭṭhi / -sati / -vāyāma …, ALT: the first of မှန်ကန်သော / မှန်ကန်စွာ /
    အပြည့်အဝ present), not the preamble table's «အပြည့်အဝ» (sammāsambuddha), which the shared lookup would give and
    which occurs in these segments only as samannāgato «အပြည့်အဝ ပြည့်စုံသူ».
M13. **Sense by context, one sense per segment** (new keywords): chandaṃ = «လိုလားမှု» only in ^2-367 (kāmacchandaṃ),
    «ဆန္ဒ» in 8–11; sukhaṃ / dukkhaṃ = «သာယာသော / နာကျင်သော» only in ^2-363 (adjectives of vedanaṃ, CTX);
    anikkhitta = «လက်မလွှတ်သော» (first in anikkhittachandatā, as the pi-1 nikkhitta decision); rūpā in ^2-224
    («Sattindriyā rūpā») = «ရုပ်» (rule 2), not the sample's object-seen value.
M14. **Headings** whole, as the sample: Satipaṭṭhānavibhaṅgo = «သတိပဋ္ဌာန်များကို ခွဲခြမ်းစိတ်ဖြာခြင်း»,
    Sammappadhānavibhaṅgo = «မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်းများကို ခွဲခြမ်းစိတ်ဖြာခြင်း»; the niddesa headings
    «X-ānupassanāniddeso» = «Xကို အဖန်ဖန် ရှုခြင်းကို ဖွင့်ဆိုချက်», niddeso = ဖွင့်ဆိုချက်.

Genuinely unclear (kept, for review): tadapi = «အရာသည်လည်း» (the Burmese fuses yadapi … tadapi); saṃvattati =
«အတွက် ဖြစ်သည်» (the dative «အတွက်» stands once after the three nouns); pakārassa = «အမျိုး» (nānappakārassa
«အမျိုးမျိုးသော»); gāmopeso = «ရွာ» (the text's «ဤသည်ပင်» is the frame); saṅkhyaṃ gacchati = «အမည် ရသည်», tveva =
«ဟူ၍သာ».
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


def load_pi1():
    d = collections.defaultdict(collections.Counter)
    for l in PI1MAP.read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if not m:
            continue
        for kv in m.group(2).split(", "):
            if "=" in kv:
                k, v = kv.split("=", 1)
                d[k][v] += 1
    return d


PI1 = load_pi1()

SHARED = {}
for _t in SECTIONS.values():
    for _k, _v in _t.items():
        SHARED.setdefault(_k, _v)


def f_alt(kw, pali, my):
    cands = ALT.get(kw) or ALT[low(kw)]
    for c in cands:
        if presence(c, my)[0]:
            return c
    return cands[0]


FUNCS["alt"] = f_alt


def resolve(v, kw, pali, my):
    if v is not None and v.startswith("@"):
        return FUNCS[v[1:]](kw, pali, my)
    return v


def table_get(tab, kw):
    for k in (kw, low(kw), kw[:1].upper() + kw[1:]):
        if k in tab:
            return tab[k]
    return None


def pi1_get(kw, my):
    """the most frequent pi-1 value of kw (or of its lower-case form) present in this segment: first the values
    whose every chunk is in the text literally, then those matched by an ending rule."""
    c = collections.Counter()
    for k in {kw, low(kw)}:
        c.update(PI1.get(k, {}))
    ranked = [v for v, _ in c.most_common() if v != NONE]
    for strict in (True, False):
        for v in ranked:
            ok, rules = presence(v, my)
            if ok and (not strict or not rules):
                return v
    return None


SRC = {}   # (sid, kw) -> source of the value: ctx / table / pi1 / compose


def base_get(ch, sid, kw, pali, my):
    v = table_get(CTX.get(sid, {}), kw)
    if v is not None:
        return resolve(v, kw, pali, my), "ctx"
    v = table_get(SECTIONS.get(ch, {}), kw)
    if v is None:
        v = table_get(SHARED, kw)
    if v is not None:
        return resolve(v, kw, pali, my), "table"
    v = pi1_get(kw, my)
    if v is not None:
        return v, "pi1"
    return None, None


# heads of the attributive pairs «rūpaṃ atītaṃ», «Sāsavā vedanā», «cakkhusamphassajā saññā» (Burmese: attr + head)
HEADS = {"rūpaṃ", "vedanā", "saññā", "saṅkhārā", "viññāṇaṃ", "cetanā"}
# subjects of the subject + predicate pairs «Rūpakkhandho hetuvippayutto», «khandhā cittasaṃsaṭṭhā»,
# «dasavidhena vedanākkhandho» (pi-1 5 rule 21: the text's particles between go, « … » marks the gap)
SUBJ = re.compile(r"^(Rūpakkhandho|Vedanākkhandho|Saññākkhandho|Saṅkhārakkhandho|Viññāṇakkhandho|khandhā|"
                  r"dasavidhena|indriyā) (.+)$")


def compose(ch, sid, kw, pali, my):
    ws = kw.split()
    if len(ws) < 2:
        return None
    if ws[-1] == "dhammā":
        b = lookup(ch, sid, " ".join(ws[:-1]), pali, my)
        return b + " " + DH
    if ws[0] in ("vuccati", "vuccanti"):
        return lookup(ch, sid, " ".join(ws[1:]), pali, my) + "ဟု ခေါ်သည်"
    if ws[0] in ("na", "no") and len(ws) == 2:
        b = lookup(ch, sid, ws[1], pali, my)
        return b[:-3] + "သည် မဟုတ်သော" if b.endswith("သော") else None
    m = SUBJ.match(kw)
    if m:
        return lookup(ch, sid, m.group(1), pali, my) + " … " + lookup(ch, sid, m.group(2), pali, my)
    if len(ws) == 2 and ws[0] in HEADS:
        return lookup(ch, sid, ws[1], pali, my) + " " + lookup(ch, sid, ws[0], pali, my)
    if len(ws) == 2 and ws[1] in HEADS:
        return lookup(ch, sid, ws[0], pali, my) + " " + lookup(ch, sid, ws[1], pali, my)
    return None


def lookup(ch, sid, kw, pali, my):
    v, src = base_get(ch, sid, kw, pali, my)
    if v is None:
        v, src = compose(ch, sid, kw, pali, my), "compose"
    if v is None:
        raise KeyError(kw)
    SRC[(sid, kw)] = src
    return v


# ---- presence check (the pi-1 checks: sample rules 3, 4, 8; 4-01 rule 12, 16; 5 rule 22) -----------------
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော", "၊", "သည့်")
VERB_FROM = ("ပါ၏", "၏", "ပြီ", "သော", "၍", "ပြီး", "ခြင်း", "ရန်", "သည့်", "ကြ", "၊", "ဟူ", "လိမ့်မည်", "။")


def chunk_present(c, text):
    """-> rule name ('exact', 'attr', 'verb', 'attr-fut', 'neg-infix', 'neg-attr') or None."""
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
    if c.endswith("ည့်") and c[:-3] + "ည်" in text:
        return "attr-fut"
    if c.endswith("ပြီးသော") and c[:-3] + " ဖြစ်" in text:      # NEW (5-7-11): «Xပြီး ဖြစ်ကြ၏» (predicate)
        return "perf-pred"
    for i in range(1, len(c)):
        if c[:i] + "မ" + c[i:] in text or c[:i] + " မ" + c[i:] in text:
            return "neg-infix"
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        for i in range(0, len(st)):
            if any((st[:i] + "မ" + st[i:]) + e in text for e in ATTR_FROM):
                return "neg-attr"
    return None


def presence(v, text):
    """-> (ok, [(chunk, rule) for every chunk not found literally])"""
    if v == NONE:
        return True, []
    rules = []
    for part in re.split(r" … ", v):
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
    """The three checks of the brief: keyword preservation, presence, no «, » / «၊» / « / » in a value."""
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


# values that differ from the pi-1 value(s) of the same keyword, with the reason (written to map-table.md)
REASONS = {
    "ajjhattaṃ": "the qualifier with an object «ajjhattaṃ kāye / vedanāsu / citte / dhammesu» = «မိမိ၌ ရှိသော ကိုယ်၌ …» "
                 "(the sample's question value); pi-1 «မိမိ၌» (jhāna adverb) is kept where it is that adverb (^2-487)",
    "bahiddhā": "pi-1 «သူတစ်ပါး၌ / ပြင်ပ၌ / အပြင်ဘက်» do not occur as the term: the pi-2 text's qualifier is «မိမိ၏ ပြင်ပ၌» "
                "(approved sample N10)",
    "anuppādāya": "pi-1 «မဖြစ်ပေါ်စေရန်» is not in these segments: the text has «… သဘောတရားတို့ မဖြစ်ပေါ်ရန်»",
    "Avasesā": "pi-1 «ကြွင်းကျန်သော» is not in these segments: the text has «ကြွင်းသော သဘောတရားများ»",
    "bojjhaṅgā": "pi-1 «သိမြင်ခြင်း၏ အင်္ဂါ» (one use) is not in the text: the Vibhaṅga text's term is «ဗောဇ္ဈင်»",
    "chandaṃ": "^2-367 the fragment of kāmacchandaṃ «ကာမကို လိုလားမှု»; «ဆန္ဒ» (pi-1) does not occur there; in chapters "
               "8-11 chandaṃ keeps pi-1 «ဆန္ဒ»",
    "chando": "pi-1 «လိုလားမှု» is the hindrance kāmacchando; here the wholesome chanda of kattukamyatā, text «ဆန္ဒ»",
    "dukkhaṃ": "^2-363 the adjective of vedanaṃ («နာကျင်သော ခံစားမှု»); pi-1 «နာကျင်မှု» is the noun (kept elsewhere)",
    "sukhaṃ": "^2-363 the adjective of vedanaṃ («သာယာသော ခံစားမှု»); pi-1 «သာယာမှု» is the noun (kept elsewhere)",
    "hadayaṃ": "the body part of the 31-part list, text «နှလုံး»; pi-1 «နှလုံးသား» (heart as mind) is not in the segment",
    "kamyatā": "fragment of kattukamyatā, text «ပြုလုပ်လိုခြင်း» (one word): pi-1 «လိုချင်ခြင်း / ထူလိုခြင်း / "
               "လိုလားခြင်း» are not in the segment",
    "niddeso": "the section heading word of this text «… ဖွင့်ဆိုချက်»; pi-1 «အကျယ် ဖော်ပြချက်» is not in these headings",
    "pariyantaṃ": "«tacapariyantaṃ» = «အရေဖြင့် ဝန်းရံထားသော» (bounded); pi-1 «အဆုံးအစွန်» (limit) is another word",
    "saritā": "agent noun of sarati «remember» (text «အောက်မေ့သူ»); pi-1 «စီးဆင်းတတ်သူ» is saritā «flowing» (taṇhā)",
    "uppādo": "text «… ၏ ဖြစ်ပေါ်ခြင်း»; pi-1 «ဖြစ်ပေါ်မှု» is not in the segment",
    "āpajjati": "fragment of parivīmaṃsamāpajjati «… စူးစမ်းဆန်းစစ်ခြင်းသို့ ရောက်၏»; pi-1 «ပြုသည်» is another construction",
}


def pi1_vals(kw):
    c = collections.Counter()
    for k in {kw, low(kw)}:
        c.update(PI1.get(k, {}))
    return c


def write_table(table, ruled_all, results):
    same_uses = sum(n for kw, c in table.items() for v, n in c.items() if v in pi1_vals(kw))
    same_kv = sum(1 for kw, c in table.items() for v in c if v in pi1_vals(kw))
    known = [kw for kw in table if pi1_vals(kw)]
    total = sum(sum(c.values()) for c in table.values())
    with open(HERE / "map-table-5-7-11.md", "w", encoding="utf-8") as f:
        f.write("# pi-2 Burmese keyword mapping: rules and review table (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း», chapters "
                + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_5-7-11.py (a copy of the approved sample map_all.py; its tables and rules unchanged). Burmese from the FINAL pi-2 text of this track only "
                "(AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters); pi-1 values from "
                "AI_translation/burmese/pi-1-keywords-by-reference-pali-burmese-plain.md. No other Burmese source.\n\n")
        f.write("## Verification\n\n| chapter | lines | keyword preservation | presence failures | comma / ၊ / « / » "
                "| rule-matched chunks | (no direct equivalent) |\n|---|---|---|---|---|---|---|\n")
        for ch, ln, bad, fails, punct, ruled, nne in results:
            f.write(f"| {ch} | {ln} | bad {bad} | {len(fails)} | {punct} | {len(ruled)} | {nne} |\n")
        f.write(f"\n## Reuse of pi-1\n\n- Keyword uses: {total}; distinct keywords: {len(table)}.\n"
                f"- Keywords that pi-1 also has: {len(known)} distinct; their values taken **unchanged from pi-1**: "
                f"{same_kv} distinct keyword-value pairs, {same_uses} uses.\n"
                f"- Keywords new in pi-2 (not in the pi-1 mapping): {len(table) - len(known)} distinct.\n\n")
        f.write("### Values that differ from pi-1 for the same keyword\n\n| keyword | pi-2 value (uses) | pi-1 value(s) "
                "| reason |\n|---|---|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            p1 = pi1_vals(kw)
            if not p1:
                continue
            for v, n in table[kw].items():
                if v not in p1:
                    f.write(f"| {kw} | {v} ({n}) | " + " · ".join(f"{x} ({m})" for x, m in p1.most_common())
                            + f" | {REASONS.get(kw, 'UNEXPLAINED')} |\n")
        f.write("\n")
        f.write(RULES)
        f.write("\n## Presence: chunks matched by an ending rule (not literally in the segment)\n\n"
                "Every other chunk of every value occurs literally in its segment's Burmese.\n\n"
                "| segment | keyword | chunk | rule |\n|---|---|---|---|\n")
        for sid, k, c, r in ruled_all:
            f.write(f"| {sid} | {k} | {c} | {r} |\n")
        f.write("\n## Keyword → Burmese (uses)\n\n«pi-1» = the value is a pi-1 value of the same keyword. Several "
                "values = the keyword reads differently by context.\n\n| Pāli keyword | Burmese (uses) |\n|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            p1 = pi1_vals(kw)
            f.write(f"| {kw} | " + " · ".join(f"{v} ({n}{', pi-1' if v in p1 else ''})"
                                               for v, n in table[kw].most_common()) + " |\n")


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
                    v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                    ok = presence(v, my[sid])[0]
                    out.append(f"{kw}={v}[{SRC[(sid, kw)]}{'' if ok else ' FAIL'}]")
                except KeyError:
                    out.append(f"{kw}=??")
            print(" | ".join(out))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--pi1":          # working aid: the pi-1 values of keywords
        for kw in args[1:]:
            print(kw, "\t", " · ".join(f"{v} ({n})" for v, n in pi1_vals(kw).most_common()) or "-")
        sys.exit()
    if args and args[0] == "--grep":         # working aid: --grep CH SID|all REGEX [pali]: matches with context
        my, pa, rows = load(args[1])
        src = pa if len(args) > 4 else my
        for sid, t in src.items():
            if args[2] in ("all", sid):
                for m in re.finditer(args[3], t):
                    print(sid, "…" + t[max(0, m.start() - 70):m.end() + 90] + "…")
        sys.exit()
    if args and args[0] == "--dump":         # working aid: distinct keyword = value [source] (uses, first segment)
        my, pa, rows = load(args[1])
        seen = collections.OrderedDict()
        for sid, kws in rows:
            for kw in [k.strip() for k in kws.split(", ")]:
                try:
                    v = lookup(args[1], sid, kw, pa.get(sid, ""), my[sid])
                except KeyError:
                    v = "??"
                key = (kw, v, SRC.get((sid, kw), "-"))
                seen.setdefault(key, [0, sid])[0] += 1
        for (kw, v, s), (n, sid) in seen.items():
            if len(args) < 3 or s in args[2:]:
                print(f"{kw}={v} [{s}] {n} {sid}")
        sys.exit()
    if args and args[0] == "--todo":         # working aid: per segment of a chapter, the keywords without a value
        my, pa, rows = load(args[1])
        for sid, kws in rows:
            miss = []
            for kw in [k.strip() for k in kws.split(", ")]:
                try:
                    lookup(args[1], sid, kw, pa.get(sid, ""), my[sid])
                except KeyError:
                    miss.append(kw)
            if miss:
                print(sid, "|", ", ".join(miss))
        sys.exit()
    if args and args[0] in ("--seg", "--segb"):
        show(args[1:], pali=args[0] == "--seg")
        sys.exit()
    if args and args[0] == "--report":
        table, unmapped, problems, summary = run(write=False)
        print(f"UNMAPPED keywords: {len(unmapped)} distinct, {sum(len(v) for v in unmapped.values())} uses")
        for kw, where in sorted(unmapped.items(), key=lambda x: -len(x[1])):
            print(f"  {kw}\t{len(where)}\t{where[0][1]}")
        print(f"presence problems: {len(problems)}")
        for ch, sid, kw, v in problems:
            print(f"  {sid}\t{kw} = {v}")
        sys.exit()
    table, unmapped, problems, summary = run(write=True)
    if unmapped or problems:
        print("UNMAPPED", dict(unmapped), "PROBLEMS", problems)
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
    for sid, k, c, r in ruled_all:
        print(f"   rule {r:9} {sid:10} {k} : {c}")
