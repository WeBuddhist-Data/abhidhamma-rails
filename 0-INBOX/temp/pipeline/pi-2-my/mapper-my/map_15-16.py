"""Pāli→Burmese keyword mapping for pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»): chapters 15-patisambhidavibhango,
16-nanavibhango. A copy of the approved sample script map_15-16.py (tables, compose rules, context functions,
verifier) with this run's own tables T_PATI / T_NANA; it writes only these two chapters and map-table-15-16.md.

usage (python3 -I -X utf8, from any directory):
  map_15-16.py             writes <ch>.mapped.md for every chapter in CHAPTERS and map-table.md, then verifies them
                         (keyword preservation, presence of every value chunk in its segment, no ", " / «၊» / « / »
                         in a value)
  map_15-16.py --report    writes nothing; lists unmapped keywords and presence failures
  map_15-16.py --seg ID    prints Pāli, Burmese, keywords and mapping of one segment
  map_15-16.py --new [N]   prints the first N segments that hold a keyword without a value (working aid)

Method: a copy (not an import) of the approved pi-1 Burmese mapper (pi-1-my/mapper-my/map_15-16.py and the later
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
ALT = {"nānā": ["အသီးသီး ကွဲပြားသော", "အမျိုးမျိုး"],
       "tattha": ["ထိုတို့အနက်", "ထို၌"],
       "paccavekkhaṇā": ["ပြန်လည် ဆင်ခြင်ခြင်း", "ပြန်လည် ဆင်ခြင်သော"]}   # pi-1 value where the text has it   # «tattha katamā» first; only «yā tattha paññā» (^2-827) = «ထို၌ ရှိသော»   # nānāvatthukā «အသီးသီး ကွဲပြားသော» / nānādhātu «အမျိုးမျိုး»
CTX = {
    # ^2-745: the text renders «manoviññāṇadhātu uppannā hoti … upasampajja viharati» with one verb (ဝင်စား၍ နေသော
    # အချိန်၌); «uppannā» has no word of its own there
    "2-745": {"uppannā": NONE, "dhātu uppannā": "ဓာတ်"},
    "2-753": {"dhammā": NONE},          # only in -dhammadhammā paññā: the final -dhammā has no word (sample N6)
    "2-754": {"Dhamme": "တရား"},        # «Dhamme ñāṇaṃ» = «တရားကို သိသော ဉာဏ်» (the dhamma of the four kinds of knowledge)
    "2-762": {"vatthu": "မှီရာ"},       # first vatthu: uppannavatthukā (the physical basis), not ñāṇavatthu
    "2-800": {"dhamma": "တရား", "dhamme": "တရား", "attha": "အကျိုးအနက်", "Atthe": "အကျိုးအနက်"},  # the four paṭisambhidā
    "2-808": {"nirodha": "ချုပ်ငြိမ်းရာ"},   # saññāvedayitanirodhasamāpatti «… ချုပ်ငြိမ်းရာ ဈာန် ဝင်စားရာ»
    "2-811": {"gāmī": "ရောက်စေသော"},    # nirayagāmī «ငရဲသို့ ရောက်စေသော» (not the Mātikā «ဦးတည်သော»)
    "2-816": {"rūpaṃ": "သဘော"},         # first rūpa: piyarūpaṃ «ချစ်ဖွယ် သဘော» (nature, not matter)
    "2-823": {"ānusayā": "ကိန်းအောင်းခြင်း ရှိသော"},   # pāpānusayā (attribute of the beings), not the noun
    "2-828": {"amanasikārā": "နှလုံး မသွင်းခြင်း", "Ajjhattaṃ": "မိမိ၌", "kusalo": "ကျွမ်းကျင်သော",
              "rūpāni": "အဆင်းအရောင်"},   # «rūpāni passati» = «အဆင်းအရောင်တို့ကို မြင်၏»
    # ^2-828: «nānattasaññānaṃ amanasikārā» (ablative «ကြောင့်» dropped); the vimokkha adverb (pi-1 jhāna «မိမိ၌»);
    # samādhikusalo «ကျွမ်းကျင်၏» (skilled, not the Mātikā kusala)
    "2-798": {"hoti": NONE},             # the copula of «vītarāgo hoti» «ရာဂ ကင်း၏» has no word
    "2-809": {"hetū": "အကြောင်းရင်း", "sammā": "အပြည့်အဝ"},
    # ^2-809: «hetū paccayā» = «အကြောင်းရင်း၊ အကြောင်း» (notes-ch15-16); the first sammā is sammāsambuddha (preamble)
    "2-806": {"paccayā": "ကြောင့်", "rūpa": "ရုပ်ပိုင်း"},   # nāmarūpa «စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း»
    "2-831": {"anāsavaṃ": "စိတ်အစွန်းအထင်း မရှိသော"},   # cetovimutti «free of taints» (notes-ch15-16), not the Mātikā
    "2-796": {"pajānāti": "ကွဲပြားစွာ သိသည်"},   # (bhikkhu) pajānāti, harmonise-notes 13 (not the Tathāgata's)
    "2-766": {"mattā": "ရုံမျှ", "ṭhānaṃ": "ရပ်ခြင်း"},   # abhinipātamattā «ကျရောက်ရုံမျှ»; the posture «standing»
}

T_PATI = {
    # --- headings (rule 7: the heading's own Burmese; notes-ch15-16 «New strings»)
    "Paṭisambhidā": "ပိုင်းခြားသိသော ဉာဏ်",
    "Saṅgaha": "အကျဉ်းချုပ်", "saṅgaha": "အကျဉ်းချုပ်",
    "Saṅgahavāro": "အကျဉ်းချုပ် ဖော်ပြချက်", "saṅgahavāro": "အကျဉ်းချုပ် ဖော်ပြချက်",
    "Saccavāro": "သစ္စာအလိုက် ဖော်ပြချက်", "saccavāro": "သစ္စာအလိုက် ဖော်ပြချက်",
    "Hetu": "အကြောင်းရင်း",                     # Hetuvāra: the cause (not the Mātikā root «အမြစ်»)
    "Dhamma": "သဘောတရား",                      # Dhammavāra «သဘောတရားအလိုက်»
    "Dhammavāro": "သဘောတရားအလိုက် ဖော်ပြချက်", "dhammavāro": "သဘောတရားအလိုက် ဖော်ပြချက်",
    "samuppādavāro": "ဖြစ်ပေါ်ပုံအလိုက် ဖော်ပြချက်",
    "Pariyatti": "ပရိယတ္တိ", "pariyatti": "ပရိယတ္တိ",
    "Pariyattivāro": "ပရိယတ္တိအလိုက် ဖော်ပြချက်", "pariyattivāro": "ပရိယတ္တိအလိုက် ဖော်ပြချက်",
    "Kusala": "ကုသိုလ်", "Akusala": "အကုသိုလ်",
    "Kiriya": "ပြုရုံမျှသာ ဖြစ်သော",            # pi-1 kiriya (5 rule 18), present in the heading
    "Dukaṃ": "နှစ်မျိုးတွဲ",
    # --- the four paṭisambhidā (notes-ch15-16)
    "paṭisambhidā": "ပိုင်းခြားသိသော ဉာဏ်", "paṭisambhidānaṃ": "ပိုင်းခြားသိသော ဉာဏ်",
    "atthapaṭisambhidā": "အကျိုးအနက်ကို ပိုင်းခြားသိသော ဉာဏ်",
    "dhammapaṭisambhidā": "တရားကို ပိုင်းခြားသိသော ဉာဏ်",
    "niruttipaṭisambhidā": "စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်",
    "Niruttipaṭisambhidā": "စကားဖြင့် ဖော်ပြမှုကို ပိုင်းခြားသိသော ဉာဏ်",
    "paṭibhānapaṭisambhidā": "ဉာဏ်ပေါ်မှုကို ပိုင်းခြားသိသော ဉာဏ်",
    "attha": "အကျိုးအနက်", "Atthe": "အကျိုးအနက်", "atthaṃ": "အကျိုးအနက်",
    "dhamma": "တရား", "dhamme": "တရား", "dhammaṃ": "တရား",   # the dhamma of dhammapaṭisambhidā (first in every segment)
    "nirutti": "စကားဖြင့် ဖော်ပြမှု", "Nirutti": "စကားဖြင့် ဖော်ပြမှု", "niruttiyā": "စကားဖြင့် ဖော်ပြမှု",
    "paṭibhāna": "ဉာဏ်ပေါ်မှု",
    "ābhilāpe": "ခေါ်ဆိုခြင်း",                 # fragment of dhammaniruttābhilāpe «… ဖော်ပြမှုကို ခေါ်ဆိုခြင်း»
    "ñāṇaṃ": "ဉာဏ်", "ñāṇesu": "ဉာဏ်", "Ñāṇesu": "ဉာဏ်",
    "jotakānī": "ထင်ရှားစေသော", "idamatthajotakānī": "ဤအကျိုးအနက်ကို ထင်ရှားစေသော",
    "ñāṇāni idamatthajotakānī": "ဉာဏ် … ဤအကျိုးအနက်ကို ထင်ရှားစေသော",
    "dhammānaṃ paññatti": "သဘောတရားတို့၏ သတ်မှတ်ချက်",
    "jānāti": "သိသည်",
    # --- the objects of knowledge «X-e ñāṇaṃ» (pi-1 Dukkhe ñāṇaṃ = ဒုက္ခကို သိသော ဉာဏ်)
    "dukkhasamudaye": "ဒုက္ခ ဖြစ်ပေါ်ခြင်း",
    "Hetumhi": "အကြောင်းရင်း", "phale": "အကျိုး",
    "Jarāmaraṇe": "အိုခြင်းနှင့် သေခြင်း", "maraṇe": "သေခြင်း",
    "jarāmaraṇanirodhe": "အိုခြင်းနှင့် သေခြင်း ချုပ်ငြိမ်းခြင်း",
    "Jarāmaraṇe ñāṇaṃ": "အိုခြင်းနှင့် သေခြင်းကို သိသော ဉာဏ်",
    "Jātiyā": "မွေးဖွားခြင်း", "bhave": "ဘဝ", "upādāne": "စွဲလမ်းမှု", "taṇhāya": "တပ်မက်မှု",
    "phasse": "တွေ့ထိမှု", "āyatane": "အာရုံခံ နယ်ပယ်", "nāmarūpe": "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း", "rūpe": "ရုပ်ပိုင်း",
    "viññāṇe": "သိစိတ်", "viññāṇe ñāṇaṃ": "သိစိတ်ကို သိသော ဉာဏ်",
    "saṅkhāresu": "ပြုပြင်ဖန်တီးမှု", "saṅkhāresu ñāṇaṃ": "ပြုပြင်ဖန်တီးမှုများကို သိသော ဉာဏ်",
    "saṅkhāranirodhe": "ပြုပြင်ဖန်တီးမှုများ ချုပ်ငြိမ်းခြင်း",
    # --- the pariyatti list (the nine aṅgas, names)
    "suttaṃ": "သုတ်", "geyyaṃ": "ဂေယျ", "veyyākaraṇaṃ": "ဝေယျာကရဏ", "gāthaṃ": "ဂါထာ", "udānaṃ": "ဥဒါန်း",
    "itivuttakaṃ": "ဣတိဝုတ်", "jātakaṃ": "ဇာတ်", "abbhutadhammaṃ": "အဗ္ဘုတဓမ္မ", "abbhuta": "အဗ္ဘုတ",
    "vedallaṃ": "ဝေဒလ္လ", "bhāsitassa": "ဟောပြောချက်",
    # --- the cittuppāda openings (abhidhamma part)
    "rūpārammaṇaṃ": "အဆင်းအရောင်ကို အာရုံပြုသော", "sasaṅkhārena": "တိုက်တွန်းမှုဖြင့်",
    "pathavīkasiṇaṃ": "မြေ ကသိုဏ်း",
    "rūpūpapattiyā": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်ပေါ်ရန်",
    "rūpūpapattiyā maggaṃ": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်း",
    "arūpūpapattiyā": "ရုပ်မရှိသော ဘုံ၌ ဖြစ်ပေါ်ရန်",
    "arūpūpapattiyā maggaṃ": "ရုပ်မရှိသော ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်း",
    "ūpapattiyā": "ဖြစ်ပေါ်ရန်",
    "āyatanaṃ": "နယ်ပယ်", "ākiñcaññāyatanaṃ": "ဘာမျှ မရှိသော နယ်ပယ်",
    "nevasaññānāsaññāyatanasaññāsahagataṃ": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်ဟု "
                                             "မှတ်သိမှုနှင့်အတူ ဖြစ်သော",
    "ābhiññaṃ": "ထူးကဲစွာ သိခြင်း", "apacayagāmiṃ": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "ကျင့်စဉ် ခက်ခဲသော ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    "vipākaṃ": "ကံ၏ အကျိုး ဖြစ်သော",           # «vipākaṃ cakkhuviññāṇaṃ» = «ကံ၏ အကျိုး ဖြစ်သော မျက်စိ သိစိတ်» (pi-1 vipākā)
    "kāmāvacarassa kusalassa": "ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်",
    "rūpāvacarassa": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော", "āvacarassa": "ဘုံနှင့် ဆိုင်သော",
    "ye vā pana": "ရှိသမျှလည်း",                 # pi-1 2-01 rule 12: ye = ရှိသမျှ; vā pana = the text's «လည်း»
    "saddārammaṇaṃ": "အသံကို အာရုံပြုသော", "gandhārammaṇaṃ": "အနံ့ကို အာရုံပြုသော",
    "rasārammaṇaṃ": "အရသာကို အာရုံပြုသော", "phoṭṭhabbārammaṇaṃ": "အထိအတွေ့ကို အာရုံပြုသော",
    "rūpārammaṇā": "အဆင်းအရောင်ကို အာရုံပြုသော", "phoṭṭhabbārammaṇā": "အထိအတွေ့ကို အာရုံပြုသော",
    "dhammārammaṇā": "သဘောတရားကို အာရုံပြုသော",
    "dhātu uppannā": "ဓာတ် … ဖြစ်ပေါ်ပြီးသော",     # subject + predicate (pi-1 5 rule 21), the text's «သည်» between
    "ākusalā": "အကုသိုလ်",                       # fragment of nākusalā without the negative (rule 8)
    "neva kusalā nākusalā": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်",
    "arūpāvacaraṃ jhānaṃ": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ဈာန်",
    "sampayuttesu": "ယှဉ်တွဲသော", "phalesu": "ဖိုလ်", "maggesu": "မဂ်",
    # --- pañhāpucchaka
    "paṭisambhidā aniyatā": "ပိုင်းခြားသိသော ဉာဏ် … မကျိန်းသေသော",   # «Tisso» = the count «သုံးပါး» in the gap
    "nevavipākanavipākadhammadhammā": "ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား",
    "ācayagāmino": "စုပုံခြင်းဆီသို့ ဦးတည်သော", "apacayagāminī": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "Anidassanaapaṭighā": "မမြင်နိုင် ထိခိုက်မှုလည်း မရှိသော",       # pi-1 anidassanaappaṭighaṃ
    "apaṭighā": "ထိခိုက်မှု မရှိသော", "appaṭighā": "ထိခိုက်မှု မရှိသော",
    "na hetū": "အမြစ် မဟုတ်သော",
}

T_NANA = {
    # --- headings (rule 7)
    "Ñāṇa": "ဉာဏ်", "mātikā": "ခေါင်းစဉ်စာရင်း", "Mātikā": "ခေါင်းစဉ်စာရင်း", "niddeso": "အကျယ် ဖော်ပြချက်",
    "Ekaka": "တစ်မျိုးတွဲ", "Duka": "နှစ်မျိုးတွဲ", "Tika": "သုံးမျိုးတွဲ", "Catukka": "လေးမျိုးတွဲ",
    "Pañcaka": "ငါးမျိုးတွဲ", "Chakka": "ခြောက်မျိုးတွဲ", "Sattaka": "ခုနစ်မျိုးတွဲ", "Aṭṭhaka": "ရှစ်မျိုးတွဲ",
    "Navaka": "ကိုးမျိုးတွဲ", "Dasaka": "ဆယ်မျိုးတွဲ",
    "Chakkamātikā": "ခြောက်မျိုးတွဲ ခေါင်းစဉ်စာရင်း", "Dasakamātikā": "ဆယ်မျိုးတွဲ ခေါင်းစဉ်စာရင်း",
    # --- the frame «Nvidhena ñāṇavatthu» (notes-ch15-16: ñāṇavatthu = ဉာဏ် အခြေခံ)
    "ñāṇavatthu": "ဉာဏ် အခြေခံ", "vatthu": "အခြေခံ",
    "dhamma": "သဘောတရား", "dhammaṃ": "သဘောတရား", "dhamme": "သဘောတရား",
    # --- the ekaka list of the five consciousnesses (^2-751)
    "viññāṇā": "သိစိတ်", "acetasikā": "စိတ်၏ အဖော် မဟုတ်သော", "āsekkhā": "ကျင့်ကြံမှု ပြီးဆုံးသူ၏",
    "Uppanna": "ဖြစ်ပေါ်ပြီးသော", "uppannārammaṇā": "ဖြစ်ပေါ်ပြီးသော အာရုံ ရှိသော",
    "purejātārammaṇā": "ရှေးဦးစွာ ဖြစ်ပေါ်ပြီးသော အာရုံ ရှိသော",
    "Ajjhattika": "အတွင်းပိုင်း", "Ajjhattikavatthukā": "အတွင်းပိုင်း မှီရာ ရှိသော",
    "bāhirārammaṇā": "ပြင်ပ အာရုံ ရှိသော", "Asambhinna": "မပျက်စီးသေးသော", "Nānā": "@alt", "nānā": "@alt",
    "gocara": "ကျက်စားရာ", "gocaravisayaṃ": "ကျက်စားရာ နယ်ပယ်", "paccanubhonti": "ခံစားသည်",
    "asamannāhārā": "အာရုံသို့ စိတ်ညွတ်ခြင်း မရှိဘဲ", "amanasikārā": "နှလုံး မသွင်းဘဲ",
    "abbokiṇṇā": "ကြားမပြတ် ဆက်တိုက်", "apubbaṃ": "ရှေ့ မရှိဘဲ", "acarimaṃ": "နောက် မရှိဘဲ",
    "samanantarā": "ချက်ချင်း နောက်၌", "anābhogā": "ဆင်ခြင်ခြင်း မရှိသော",
    "aññatra": "လွဲ၍", "abhinipāta": "အာရုံ ကျရောက်",
    "paṭivijānāti": "ပိုင်းခြား၍ သိသည်", "iriyāpathaṃ": "ဣရိယာပုထ်", "kappeti": "ပြုလုပ်သည်",
    "paṭṭhapeti": "ဖြစ်စေသည်", "kusalākusalaṃ": "ကုသိုလ် အကုသိုလ်", "ākusalaṃ": "အကုသိုလ်",
    "kusalākusalaṃ dhammaṃ": "ကုသိုလ် အကုသိုလ် သဘောတရား",
    "samāpajjati": "ဝင်စားသည်", "vuṭṭhāti": "ထမြောက်သည်", "cavati": "သေသည်",
    "supati": "အိပ်သည်", "paṭibujjhati": "နိုးသည်", "supinaṃ": "အိပ်မက်",
    "yāthāvaka": "ဟုတ်မှန်သည့်အတိုင်း", "vibhāvanā": "ထင်ရှားစေသော", "vibhāvanā paññā": "ထင်ရှားစေသော ပညာ",
    # --- the duka list (^2-752)
    "Atthajāpikā": "အကျိုးကို ဖြစ်စေတတ်သော", "jāpikā": "ဖြစ်စေတတ်သော",
    "jāpitatthā": "အကျိုးကို ဖြစ်စေပြီးသော", "jāpita": "ဖြစ်စေပြီးသော",
    "Sappītikā": "ပီတိ ရှိသော", "appītikā": "ပီတိ မရှိသော", "Savitakkā": "စတင်ကြံစည်မှု ရှိသော",
    # --- the tika list (^2-753): «-dhammadhammā paññā», the head is paññā (sample N6: the final -dhamma has no word)
    "vipākadhammadhammā": "အကျိုး ပေးတတ်သော",
    "nevavipākanavipākadhammadhammā": "ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော",
    "Cintāmayā": "စဉ်းစားခြင်းမှ ဖြစ်သော", "sutamayā": "ကြားနာခြင်းမှ ဖြစ်သော", "suta": "ကြားနာခြင်း",
    "bhāvanāmayā": "ဘာဝနာ ပွားများခြင်းမှ ဖြစ်သော", "bhāvanā": "ဘာဝနာ ပွားများခြင်း",
    "Dānamayā": "ပေးလှူခြင်းမှ ဖြစ်သော", "Dāna": "ပေးလှူခြင်း", "sīlamayā": "သီလမှ ဖြစ်သော",
    "Adhisīle": "လွန်မြတ်သော သီလ", "adhicitte": "လွန်မြတ်သော စိတ်", "citte": "စိတ်",
    "adhipaññāya": "လွန်မြတ်သော ပညာ",
    "Adhisīle paññā": "လွန်မြတ်သော သီလ၌ ရှိသော ပညာ", "adhicitte paññā": "လွန်မြတ်သော စိတ်၌ ရှိသော ပညာ",
    "adhipaññāya paññā": "လွန်မြတ်သော ပညာ၌ ရှိသော ပညာ",
    "upāya": "နည်းလမ်း",
    "uppādinī": "ဖြစ်ပေါ်လာမည့်", "anuppannā": "မဖြစ်ပေါ်သေးသော", "ādhipatinī": "အကြီးအမှူး",
    "ācayagāminī": "စုပုံခြင်းဆီသို့ ဦးတည်သော",
    # --- the catukka list (^2-754)
    "saccānulomikaṃ": "သစ္စာနှင့် လျော်ညီသော", "ānulomikaṃ": "လျော်ညီသော",
    "anvaye": "ဆက်စပ်၍", "anvaye ñāṇaṃ": "ဆက်စပ်၍ သိသော ဉာဏ်", "pariye": "စိတ်ကို ပိုင်းခြား၍", "sammuti": "သမုတ်",
    "ācayāya": "စုပုံခြင်းအတွက်", "apacayāya": "လျော့ပါးခြင်းအတွက်",        # dative of purpose: «အတွက်» kept
    "nibbidāya": "ငြီးငွေ့ခြင်းအတွက်", "paṭivedhāya": "ထိုးဖောက်၍ သိခြင်းအတွက်",  # (as pi-1 keeps «ရန်», N7)
    "paññā ācayāya": "စုပုံခြင်းအတွက် … ပညာ", "paññā apacayāya": "လျော့ပါးခြင်းအတွက် … ပညာ",
    "paññā nibbidāya": "ငြီးငွေ့ခြင်းအတွက် … ပညာ",
    "Hānabhāginī": "ဆုတ်ယုတ်ခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော", "ṭhitibhāginī": "တည်တံ့ခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော",
    "visesabhāginī": "ထူးခြားခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော", "nibbedhabhāginī": "ဖောက်ထွင်းခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော",
    "visesa": "ထူးခြားခြင်း", "nibbedha": "ဖောက်ထွင်းခြင်း",
    # --- pañcaka … navaka (^2-755 … ^2-759)
    "sammā": "မှန်ကန်သော", "pañcañāṇiko": "ဉာဏ် ငါးပါး ရှိသော", "abhiññāsu": "ထူးကဲစွာ သိခြင်း",
    "Sattasattati": "ခုနစ်ဆယ့်ခုနစ်ပါး", "samāpattīsu": "ဈာန် ဝင်စားရာ", "vihāra": "နေထိုင်ရာ",
    "anupubba": "အစဉ်အတိုင်း",
    # --- the ten powers of the Tathāgata (^2-760; the honorific «…တော်မူ» is the text's verb)
    "tathāgato": "မြတ်စွာဘုရား", "tathāgatabalāni": "ဘုရားဆိုင်ရာ စွမ်းအား", "samannāgato": "ပြည့်စုံသော",
    "āsabhaṃ": "အမြတ်ဆုံး", "ṭhānaṃ": "နေရာ", "paṭijānāti": "ဝန်ခံတော်မူသည်",
    "ṭhānaṃ paṭijānāti": "နေရာကို ဝန်ခံတော်မူသည်",
    "parisāsu": "ပရိသတ်", "sīha": "ခြင်္သေ့", "nādaṃ": "ဟိန်းသံ", "nadati": "ဟိန်းတော်မူသည်",
    "sīhanādaṃ nadati": "ခြင်္သေ့ဟိန်းသံကို ဟိန်းတော်မူသည်",
    "cakkaṃ": "တရားစက်", "brahmacakkaṃ": "မြတ်သော တရားစက်", "pavatteti": "လည်စေတော်မူသည်",
    "brahmacakkaṃ pavatteti": "မြတ်သော တရားစက်ကို လည်စေတော်မူသည်",
    "pajānāti": "သိတော်မူသည်", "yathābhūtaṃ": "ဟုတ်မှန်သည့်အတိုင်း",
    "aṭṭhānato": "မဖြစ်နိုင်သော အကြောင်း",       # «…အဖြစ်» (as) dropped (pi-1 5 rule 15)
    "balaṃ āgamma tathāgato": "စွမ်းအားကို မှီ၍ မြတ်စွာဘုရား", "āgamma": "မှီ၍",
    "samādānānaṃ": "ဆောက်တည်မှု", "kammasamādānānaṃ": "ကံ ဆောက်တည်မှု",
    "ṭhānaso": "ဖြစ်ရာ အခြေအနေ", "hetuso": "အကြောင်းရင်း",   # «…အားဖြင့်» (by) dropped (rule 1)
    "sabbattha": "ဘုံ အားလုံး", "gāminiṃ": "ရောက်စေသော",
    "ādhimuttikataṃ": "စိတ်ညွတ်ရာ",
    "jhāna": "ဈာန်", "vimokkha": "လွတ်မြောက်ခြင်း", "samāpattīnaṃ": "ဈာန် ဝင်စားရာ",
    "saṃkilesaṃ": "ညစ်နွမ်းခြင်း", "vodānaṃ": "စင်ကြယ်ခြင်း", "vuṭṭhānaṃ": "ထမြောက်ခြင်း",
    "pubbenivāsānussatiṃ": "ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့ခြင်း", "ānussatiṃ": "အဖန်ဖန် အောက်မေ့ခြင်း",
    "cutūpapātaṃ": "သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်း", "ūpapātaṃ": "ဖြစ်ပေါ်ခြင်း", "khayaṃ": "ကုန်ခန်းခြင်း",
    # --- the ekaka exposition (^2-761 … ^2-766)
    "āsekkha": "ကျင့်ကြံမှု ပြီးဆုံးသူ၏", "hetumeva": "အမြစ်", "vicārameva": "ဆက်လက်သုံးသပ်မှု",
    "arūpameva": "ရုပ် မဟုတ်သော", "acetasikameva": "စိတ်၏ အဖော် မဟုတ်သော",
    "ābhibhūtameva": "လွှမ်းမိုးခံရသော", "āvacarameva": "ဘုံနှင့် ဆိုင်သော", "aniyatameva": "မကျိန်းသေသော",
    "uppannasmiṃ": "ဖြစ်ပေါ်ပြီးသော", "asambhinnasmiṃ": "မပျက်စီးသေးသော", "vatthukā": "မှီရာ ရှိသော",
    "ārammaṇe": "အာရုံ", "aññaṃ": "တခြား",
    "sotaviññāṇassa": "နား သိစိတ်", "ghānaviññāṇassa": "နှာခေါင်း သိစိတ်", "jivhāviññāṇassa": "လျှာ သိစိတ်",
    "paccanubhoti": "ခံစားသည်", "gocaravisayaṃ paccanubhontī": "ကျက်စားရာ နယ်ပယ်ကို ခံစားသည်",
    "kāyaviññāṇaṃ na paccanubhoti": "ကိုယ် သိစိတ် … မခံစား",
    "cakkhuviññāṇaṃ na paccanubhoti": "မျက်စိ သိစိတ် … မခံစား",
    "kāyaviññāṇassa gocaravisayaṃ": "ကိုယ် သိစိတ်၏ ကျက်စားရာ နယ်ပယ်",
    "cakkhuviññāṇassa gocaravisayaṃ": "မျက်စိ သိစိတ်၏ ကျက်စားရာ နယ်ပယ်",
    "samannāharantassa": "အာရုံသို့ စိတ်ညွတ်သူ", "manasikarontassa": "နှလုံးသွင်းသူ",
    "paṭipāṭiyā": "အစဉ်အတိုင်း ဆက်တိုက်", "khaṇe": "ခဏ", "ekakkhaṇe": "တစ်ခဏတည်း",
    "kāyaviññāṇassa uppannasamanantarā": "ကိုယ် သိစိတ် ဖြစ်ပေါ်ပြီး၍ ချက်ချင်း နောက်၌",
    "cakkhuviññāṇassa uppannasamanantarā": "မျက်စိ သိစိတ် ဖြစ်ပေါ်ပြီး၍ ချက်ချင်း နောက်၌",
    "kāyaviññāṇaṃ na uppajjati": "ကိုယ် သိစိတ် မဖြစ်ပေါ်", "cakkhuviññāṇaṃ na uppajjati": "မျက်စိ သိစိတ် မဖြစ်ပေါ်",
    "āvaṭṭanā": "စိတ်ကို လှည့်ဆောင်ခြင်း", "ābhogo": "ဆင်ခြင်ခြင်း", "samannāhāro": "အာရုံသို့ စိတ်ညွတ်ခြင်း",
    "manasikāro": "နှလုံးသွင်းခြင်း", "āpāta": "အာရုံ ရှေ့သို့ ရောက်လာ",
    "manodhātuyā": "မနော ဓာတ်", "dhātuyā": "ဓာတ်",
    "gamanaṃ": "သွားခြင်း", "nisajjaṃ": "ထိုင်ခြင်း", "seyyaṃ": "လျောင်းခြင်း",
    "Ekakaṃ": "တစ်မျိုးတွဲ",
    # --- the duka exposition (^2-767 …): the locative substantives; the text adds the head «သဘောတရား»
    #     (NEW 15-16 rule N4, as pi-1 5 rule 18 adds «စိတ်»)
    "kusale": "ကုသိုလ် သဘောတရား", "vipāke": "ကံ၏ အကျိုး ဖြစ်သော သဘောတရား",
    "ābyākate": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား",
    "kusalābyākate": "ကုသိုလ် သဘောတရားနှင့် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား",
    "kiriyābyākate": "ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား",
    "Kāmāvacarakusalābyākate": "ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ် သဘောတရားနှင့် ကုသိုလ်လည်း မဟုတ် "
                               "အကုသိုလ်လည်း မဟုတ်သော သဘောတရား",
    "attha": "အကျိုး", "Attha": "အကျိုး",     # ch16: the attha of atthajāpikā «အကျိုးကို ဖြစ်စေတတ်သော»
    "samāpattiṃ": "ဈာန် ဝင်စားရာ", "uppādentassa": "ဖြစ်စေသော", "uppannāya": "ဖြစ်ပေါ်ပြီးသော",
    "phalesu paññā": "ဖိုလ် … ရှိသော ပညာ", "maggesu paññā": "မဂ် … ရှိသော ပညာ",   # «လေးပါးတို့၌» = catūsu: the gap
    # --- the tika exposition (^2-768 …)
    "tattha": "@alt", "sammādiṭṭhi": "မှန်ကန်သော အယူ", "yaṃ": NONE,   # relative pronoun (pi-1 rule)
    "yoga": "ပညာရှိ", "vihitesu": "စီမံထားသော", "āyatanesu": "အလုပ်အကိုင်", "sippāyatanesu": "အတတ်ပညာ",
    "vijjā": "အသိပညာ", "ṭṭhānesu": "ဌာန", "kammassakataṃ": "ကံသာ မိမိ၏ ဥစ္စာ ဖြစ်ကြောင်း",
    "anicca": "မမြဲသော", "evarūpiṃ": "ဤသို့ သဘောရှိသော", "anulomikaṃ": "လျော်ညီသော",
    "khantiṃ": "သည်းခံ လက်ခံမှု", "diṭṭhiṃ": "အယူ", "ruciṃ": "နှစ်သက်မှု", "mudiṃ": "ကြည်နူးမှု",
    "pekkhaṃ": "ရှုကြည့်မှု", "nijjhāna": "ဆင်ခြင်၍", "sutvā": "ကြားနာ၍", "paṭilabhati": "ရရှိသည်",
    "Dānaṃ": "ပေးလှူခြင်း", "Sīlaṃ": "သီလ", "ādhigaccha": "ရရှိ၍", "sīle": "သီလ",
    "Pātimokkha": "ပါတိမောက်", "saṃvaraṃ": "စောင့်စည်းမှု", "saṃvarantassa": "စောင့်စည်းသူ",
    "Rūpāvacarārūpāvacarasamāpattiṃ": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ဈာန် ဝင်စားရာ",
    "ārūpāvacara": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော", "samāpajjantassa": "ဝင်စားသူ",
    "manasikaroto": "နှလုံးသွင်းသူ", "pahīyanti": "ပျောက်ကင်းသည်", "nirujjhanti": "ချုပ်ငြိမ်းသည်",
    "tatrupāyā": "ထိုအရာ၌ နည်းလမ်း ဖြစ်သော",
    "vitakkavicāra": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု",
    "vitakkavicārasampayuttā": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့နှင့် ယှဉ်တွဲသော",
    "vitakkavicāravippayuttā": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့နှင့် ကင်းကွာသော",
    "arahatta": "အရဟတ္တ", "upariṭṭhimā": "အမြင့်ဆုံး ဖြစ်သော",
    "rūpāvacarārūpāvacarakusalābyākate": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ကုသိုလ် "
                                         "သဘောတရားနှင့် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား",
    "āvacara": "ဘုံနှင့် ဆိုင်သော",
    "Paritte": "အကန့်အသတ် ရှိသော", "Mahaggate": "ကြီးမြတ်သော", "Appamāṇe": "အတိုင်းအဆ မရှိသော",
    "adhipatiṃ": "အကြီးအမှူး",
    "bahiddhā paññā": "မိမိ၏ ပြင်ပ၌ ရှိသော ပညာ", "samāpannassa paññā": "ဈာန် ဝင်စားသူ၏ ပညာ",
    "Ajjhatte": "မိမိ၌ ရှိသော", "Ajjhatte dhamme": "မိမိ၌ ရှိသော သဘောတရား", "Ajjhatta": "မိမိ၌",
    "Bahiddhādhamme": "မိမိ၏ ပြင်ပ၌ ရှိသော သဘောတရား",
    # --- the catukka exposition (^2-793 …)
    "sukata": "ကောင်းစွာ ပြုသော", "sammaggatā": "မှန်ကန်စွာ ရောက်ရှိသော", "sayaṃ": "ကိုယ်တိုင်",
    "pavedentī": "ဟောကြားသည်", "yā": NONE,
    "anulomikā": "လျော်ညီသော", "khanti": "သည်းခံ လက်ခံမှု", "ruci": "နှစ်သက်မှု", "pekkhā": "ရှုကြည့်မှု",
    "dukkhe": "ဒုက္ခ",
    "ñātena": "သိပြီးသော", "viditena": "ထင်ရှားစွာ သိပြီးသော", "pariyogāḷhena": "နက်နက်နဲနဲ သက်ဝင်ပြီးသော",
    "nayaṃ": "နည်း", "neti": "ဆောင်သည်", "Ye hi keci": "အကြင်သူ", "samaṇā": "ရဟန်း",
    "dukkhaṃ": "ဒုက္ခ", "samudayaṃ": "ဖြစ်ပေါ်ခြင်း", "dukkhasamudayaṃ": "ဒုက္ခ ဖြစ်ပေါ်ခြင်း",
    "nirodhaṃ": "ချုပ်ငြိမ်းခြင်း", "dukkhanirodhaṃ": "ဒုက္ခ ချုပ်ငြိမ်းခြင်း",
    "abbhaññaṃsu": "ထူးကဲစွာ သိခဲ့သည်", "dukkhaṃ abbhaññaṃsu": "ဒုက္ခကို ထူးကဲစွာ သိခဲ့သည်",
    "abhijānissanti": "ထူးကဲစွာ သိလိမ့်မည်",
    "pariye ñāṇaṃ": "စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်", "ceto": "စိတ်", "paricca": "ပိုင်းခြား၍",
    "sarāgaṃ": "ရာဂ ရှိသော", "vītarāgaṃ": "ရာဂ ကင်းသော", "sadosaṃ": "ဒေါသ ရှိသော", "vītadosaṃ": "ဒေါသ ကင်းသော",
    "samohaṃ": "မောဟ ရှိသော", "vītamohaṃ": "မောဟ ကင်းသော", "saṃkhittaṃ": "တွန့်ဆုတ်နေသော",
    "vikkhittaṃ": "ပျံ့လွင့်နေသော", "mahaggataṃ": "ကြီးမြတ်သော", "amahaggataṃ": "မကြီးမြတ်သော",
    "sauttaraṃ": "ထိုထက် သာလွန်သည် ရှိသေးသော", "anuttaraṃ": "ထိုထက် သာလွန်သည် မရှိသော",
    "samāhitaṃ": "တည်ကြည်သော", "asamāhitaṃ": "မတည်ကြည်သော", "vimuttaṃ": "လွတ်မြောက်သော",
    "avimuttaṃ": "မလွတ်မြောက်သော",
    "avasesā": "ကြွင်းသော", "avasesā paññā": "ကြွင်းသော ပညာ",
    "rūpāvacarārūpāvacarakusale": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ကုသိုလ် သဘောတရား",
    "vītarāgo": "ရာဂ ကင်းသော", "abhiññāyo": "ထူးကဲစွာ သိခြင်း", "paṭivijjhati": "ထိုးဖောက်၍ သိသည်",
    "saccāni": "သစ္စာ",
    # --- hānabhāginī … (^2-799)
    "manasikārā": "နှလုံးသွင်းခြင်း", "pāpa": "ယုတ်မာသော",
    "lābhiṃ": "ရသူ", "saññāmanasikārā": "မှတ်သိမှုနှင့် နှလုံးသွင်းခြင်း",
    "kāmasahagatā saññāmanasikārā": "ကာမနှင့်အတူ ဖြစ်သော မှတ်သိမှုနှင့် နှလုံးသွင်းခြင်း",
    "samudācaranti": "ထကြွလာသည်", "santiṭṭhati": "တည်တံ့သည်",
    "anudhammatā": "လျော်ညီသော", "tadanudhammatā sati": "ထိုဈာန်နှင့် လျော်ညီသော သတိ",
    "tadanudhammatā sati santiṭṭhati": "ထိုဈာန်နှင့် လျော်ညီသော သတိ တည်တံ့သည်",
    "avitakka": "စတင်ကြံစည်မှု မရှိခြင်း", "nibbidā": "ငြီးငွေ့ခြင်း",
    "nibbidāsahagatā": "ငြီးငွေ့ခြင်းနှင့်အတူ ဖြစ်သော", "ūpasañhitā": "စပ်သော",
    "virāgūpasañhitā": "ရာဂ ကင်းခြင်းနှင့် စပ်သော",
    "pītisukha": "ပီတိနှင့် သာယာမှု", "pītisukhasahagatā": "ပီတိနှင့် သာယာမှုနှင့်အတူ ဖြစ်သော",
    "Adukkhamasukha": "မနာကျင် မသာယာမှု", "āyatana": "နယ်ပယ်",
    "Ākāsānañcāyatanassa": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်",
    "Viññāṇañcāyatanassa": "အဆုံး မရှိသော သိစိတ် နယ်ပယ်", "Ākiñcaññāyatanassa": "ဘာမျှ မရှိသော နယ်ပယ်",
    "samādhiṃ": "သမာဓိ", "Samādhissa": "သမာဓိ", "Kicchena": "ခက်ခဲစွာ", "kasirena": "ပင်ပန်းစွာ",
    "dukkhapaṭipadā": "ကျင့်စဉ် ခက်ခဲသော", "sukhapaṭipadā": "ကျင့်စဉ် လွယ်ကူသော",
    "ābhiññā": "ထူးကဲစွာ သိခြင်း", "dandhābhiññā": "ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    "khippābhiññā": "ထူးကဲစွာ သိခြင်း လျင်မြန်သော",
    "dukkhapaṭipadā dandhābhiññā": "ကျင့်စဉ် ခက်ခဲသော ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    "dukkhapaṭipadā khippābhiññā": "ကျင့်စဉ် ခက်ခဲသော ထူးကဲစွာ သိခြင်း လျင်မြန်သော",
    "abhijānantassa": "ထူးကဲစွာ သိသူ", "khippaṃ": "လျင်မြန်စွာ", "dandhaṃ": "နှေးကွေးစွာ",
    "nikāma": "စိတ်တိုင်းကျ", "lābhissa": "ရ၍", "pharantassa": "ပျံ့နှံ့စေသူ", "vipulaṃ": "ကျယ်ပြန့်စွာ",
    "samudaya": "ဖြစ်ပေါ်ခြင်း", "saṅkhāranirodhaṃ": "ပြုပြင်ဖန်တီးမှုများ ချုပ်ငြိမ်းခြင်း",
    "viññāṇepetaṃ ñāṇaṃ": "သိစိတ်ကို သိသော ဉာဏ်လည်း", "Catukkaṃ": "လေးမျိုးတွဲ",
    # --- pañcaka / chakka (^2-804, ^2-805)
    "jhānesu": "ဈာန်", "pharaṇatā": "ပျံ့နှံ့ခြင်း", "āloka": "အလင်း", "Paracitte": "အခြားသူ၏ စိတ်",
    "paracitte": "အခြားသူ၏ စိတ်", "Dibba": "နတ်", "vuṭṭhitassa": "ထမြောက်သူ",
    "paccavekkhaṇāñāṇaṃ": "ပြန်လည် ဆင်ခြင်သော ဉာဏ်", "sukho": "သာယာသော", "paccattaññeva": "မိမိ၌ပင်",
    "ñāṇaṃ uppajjati": "ဉာဏ် ဖြစ်ပေါ်သည်", "ariyo": "အရိယာ", "nirāmiso": "လောကီ အာမိသ မရှိသော",
    "akāpurisasevito": "သူယုတ်မာတို့ မမှီဝဲသော", "sevito": "မှီဝဲသော", "santo": "ငြိမ်သက်သော",
    "paṭippassaddha": "ငြိမ်းအေးခြင်း", "laddho": "ရအပ်သော",
    "ekodibhāvādhigato": "စိတ်ကို စုစည်း တည်ငြိမ်ခြင်းသို့ ရောက်သော", "ādhigato": "ရောက်သော",
    "sasaṅkhāraniggayhavāritagato": "တိုက်တွန်းမှုဖြင့် နှိပ်ကွပ် တားမြစ်ရသော",   # the keyword lost na (rule 8)
    "sasaṅkhāra": "တိုက်တွန်းမှု", "niggayha": "နှိပ်ကွပ်", "vārita": "တားမြစ်ရသော",
    "samāpajjāmi": "ဝင်စားသည်", "vuṭṭhahāmī": "ထမြောက်သည်", "Pañcakaṃ": "ငါးမျိုးတွဲ",
    "Iddhi": "တန်ခိုး", "vidhe": "အမျိုးမျိုး", "visuddhiyā": "စင်ကြယ်သော",
    "pubbenivāsānussatiyā": "ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့နိုင်သော", "ānussatiyā": "အဖန်ဖန် အောက်မေ့နိုင်သော",
    "cutūpapāte": "သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်း", "ūpapāte": "ဖြစ်ပေါ်ခြင်း", "Chakkaṃ": "ခြောက်မျိုးတွဲ",
    # --- sattaka (^2-806): «X-paccayā Y-nti ñāṇaṃ» = «Xကြောင့် Y ဖြစ်ပေါ်သည်ဟု သိသော ဉာဏ်» (pi-1 ^1-1343 «ကြောင့်»)
    "jātipaccayā": "မွေးဖွားခြင်းကြောင့်", "bhavapaccayā": "ဘဝကြောင့်", "upādānapaccayā": "စွဲလမ်းမှုကြောင့်",
    "taṇhāpaccayā": "တပ်မက်မှုကြောင့်", "vedanāpaccayā": "ခံစားမှုကြောင့်", "phassapaccayā": "တွေ့ထိမှုကြောင့်",
    "saḷāyatanapaccayā": "အာရုံခံ နယ်ပယ် ခြောက်ပါးကြောင့်", "nāmarūpapaccayā": "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်းကြောင့်",
    "viññāṇapaccayā": "သိစိတ်ကြောင့်", "saṅkhārapaccayā": "ပြုပြင်ဖန်တီးမှုများကြောင့်",
    "avijjāpaccayā": "အမှန်ကို မသိမှုကြောင့်", "jarāmaraṇa": "အိုခြင်းနှင့် သေခြင်း",
    "nāmarūpa": "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း", "ṭṭhiti": "တည်ရှိပုံ", "tampi": "ထိုဉာဏ် … လည်း",
    "khaya": "ကုန်ခန်း", "vaya": "ပျက်စီး", "virāga": "ကင်းပြတ်", "nirodha": "ချုပ်ငြိမ်း",   # stems of «…တတ်သော သဘော»
    "Sattakaṃ": "ခုနစ်မျိုးတွဲ",
    # --- aṭṭhaka / navaka (^2-807, ^2-808)
    "phale": "ဖိုလ်", "Sotāpatti": "သောတာပတ္တိ", "sakadāgāmi": "သကဒါဂါမိ", "anāgāmi": "အနာဂါမိ",
    "Aṭṭhakaṃ": "ရှစ်မျိုးတွဲ", "Navakaṃ": "ကိုးမျိုးတွဲ", "samāpattiyā": "ဈာန် ဝင်စားရာ",
    "catutthajjhāna": "စတုတ္ထ ဈာန်", "ākāsānañcāyatana": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်",
    "ākāsānañcāyatanasamāpattiyā": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ဝင်စားရာ",
    "viññāṇañcāyatanasamāpattiyā": "အဆုံး မရှိသော သိစိတ် နယ်ပယ် ဝင်စားရာ",
    "ākiñcaññāyatanasamāpattiyā": "ဘာမျှ မရှိသော နယ်ပယ် ဝင်စားရာ",
    "nevasaññānāsaññāyatanasamāpattiyā": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ဝင်စားရာ",
    "vedayita": "ခံစားမှု", "paccavekkhaṇā": "@alt",
    # --- the first power: ṭhāna / aṭṭhāna (^2-809)
    "Aṭṭhānametaṃ": "မဖြစ်နိုင်သော အကြောင်း", "anavakāso": "အခွင့်အလမ်း မရှိ",
    "sampanno": "ပြည့်စုံသော", "diṭṭhisampanno": "အယူ ပြည့်စုံသော", "puggalo": "ပုဂ္ဂိုလ်",
    "diṭṭhisampanno puggalo": "အယူ ပြည့်စုံသော ပုဂ္ဂိုလ်", "saṅkhāraṃ": "ပြုပြင်ဖန်တီးမှု",
    "niccato": "မြဲသော", "sukhato": "သာယာသော", "atthato": "အနှစ်သာရ ရှိသော",   # «…သည်ဟု ယူဆရာ၏» (-to = as)
    "mātaraṃ": "အမိ", "pitaraṃ": "အဖ", "jīvitā": "အသက်", "voropeyya": "သတ်သည်",
    "paduṭṭhena": "ပြစ်မှားလိုသော", "cittena": "စိတ်", "lohitaṃ": "သွေး", "uppādeyya": "ထွက်စေသည်",
    "saṅghaṃ": "သံဃာ", "satthāraṃ": "ဆရာ", "uddiseyya": "ကိုးကွယ်သည်", "aṭṭhamaṃ": "ရှစ်ကြိမ်မြောက်",
    "bhavaṃ": "ဘဝ", "nibbatteyya": "ဖြစ်စေသည်", "lokadhātuyā": "လောကဓာတ်",
    "arahanto": "ရဟန္တာ", "arahaṃ": "ရဟန္တာ", "uppajjeyyuṃ": "ဖြစ်ပေါ်သည်",
    "sambuddho": "အမှန်ကို ကိုယ်တိုင် … သိမြင်တော်မူသော ဘုရား",
    "sammāsambuddho": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရား",
    "sammāsambuddhā": "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရား",
    "rājāno": "မင်း", "rājā": "မင်း", "cakkavattī": "စကြဝတေး", "itthī": "အမျိုးသမီး", "puriso": "အမျိုးသား",
    "sakkattaṃ": "သိကြားမင်း အဖြစ်", "kareyya": "ပြုသည်",
    "kāyaduccarita": "ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်", "vacīduccarita": "နှုတ်ဖြင့် ပြုသော ဒုစရိုက်",
    "manoduccarita": "မနောဖြင့် ပြုသော ဒုစရိုက်", "duccarita": "ဒုစရိုက်",
    "kāyasucarita": "ကိုယ်ဖြင့် ပြုသော သုစရိုက်", "vacīsucarita": "နှုတ်ဖြင့် ပြုသော သုစရိုက်",
    "manosucarita": "မနောဖြင့် ပြုသော သုစရိုက်", "sucarita": "သုစရိုက်",
    "iṭṭho": "လိုလားဖွယ်ကောင်းသော", "aniṭṭho": "လိုလားဖွယ် မကောင်းသော", "kanto": "ချစ်ခင်ဖွယ်ကောင်းသော",
    "akanto": "ချစ်ခင်ဖွယ် မကောင်းသော", "manāpo": "စိတ်နှင့် တွေ့သော", "amanāpo": "စိတ်နှင့် မတွေ့သော",
    "manāpo vipāko": "စိတ်နှင့် တွေ့သော အကျိုး", "amanāpo vipāko": "စိတ်နှင့် မတွေ့သော အကျိုး",
    "bhedā": "ပြိုကွဲ၍", "paraṃ maraṇā": "သေပြီးနောက်", "upapajjeyya": "ရောက်သည်",
    "sugatiṃ": "ကောင်းသော လားရာ", "saggaṃ": "နတ်ပြည်", "saggaṃ lokaṃ": "နတ်ပြည် လောက", "gatiṃ": "လားရာ",
    "duggatiṃ": "ဆိုးသော လားရာ", "vinipātaṃ": "ပျက်စီး ကျရောက်ရာ", "nirayaṃ": "ငရဲ",
    # --- powers 2 … 5 (^2-810 … ^2-813)
    "kammasamādānāni": "ကံ ဆောက်တည်မှု", "samādānāni": "ဆောက်တည်မှု", "pāpakāni": "ယုတ်မာသော",
    "pāpakāni kammasamādānāni": "ယုတ်မာသော ကံ ဆောက်တည်မှု",
    "kalyāṇāni kammasamādānāni": "ကောင်းမြတ်သော ကံ ဆောက်တည်မှု",
    "gati": "လားရာ ဘဝ", "upadhi": "ခန္ဓာကိုယ်", "payoga": "ကြိုးစား အားထုတ်မှု", "sampatti": "ပြည့်စုံမှု",
    "vipattiṃ": "ချို့ယွင်းမှု", "paṭibāḷhāni": "တားဆီးခံရသော", "vipaccanti": "အကျိုး ပေးသည်",
    "niraya": "ငရဲ", "tiracchāna": "တိရစ္ဆာန်", "yoni": "ဘဝ", "petti": "ပြိတ္တာ", "visaya": "ဘုံ", "deva": "နတ်",
    "nānattaṃ": "ကွဲပြားမှု",
    "hīnādhimuttikā": "ယုတ်ညံ့သော စိတ်ညွတ်ရာ ရှိသော", "paṇītādhimuttikā": "မွန်မြတ်သော စိတ်ညွတ်ရာ ရှိသော",
    "ādhimuttikā": "စိတ်ညွတ်ရာ ရှိသော",
    "sevanti": "မှီဝဲသည်", "bhajanti": "ပေါင်းဖော်သည်", "payirupāsanti": "ဆည်းကပ်သည်",
    "seviṃsu": "မှီဝဲခဲ့သည်", "bhajiṃsu": "ပေါင်းဖော်ခဲ့သည်", "payirupāsiṃsu": "ဆည်းကပ်ခဲ့သည်",
    "sevissanti": "မှီဝဲလိမ့်မည်", "bhajissanti": "ပေါင်းဖော်လိမ့်မည်", "payirupāsissanti": "ဆည်းကပ်လိမ့်မည်",
    # --- power 6: indriyaparopariyatta (^2-814 … ^2-825)
    "āsayaṃ": "စိတ်သဘောထား", "āsayo": "စိတ်သဘောထား", "anusayaṃ": "ကိန်းအောင်းခြင်း", "adhimuttiṃ": "စိတ်ညွတ်ရာ",
    "rajakkhe": "ကိလေသာ မြူ", "akkhe": NONE,     # rajakkha «ကိလေသာ မြူ»: the text has no word for akkha (eye)
    "tikkhindriye": "စွမ်းရည် ထက်မြက်သော", "mudindriye": "စွမ်းရည် နုံ့သော", "indriye": "စွမ်းရည်",
    "svākāre": "အခြင်းအရာ ကောင်းသော", "dvākāre": "အခြင်းအရာ ဆိုးသော", "ākāre": "အခြင်းအရာ",
    "suviññāpaye": "သိအောင် ပြောပြရ လွယ်သော", "duviññāpaye": "သိအောင် ပြောပြရ ခက်သော",
    "viññāpaye": "သိအောင် ပြောပြရ",
    "bhabbābhabbe": "ထိုက်တန်သော မထိုက်တန်သော", "ābhabbe": "မထိုက်တန်သော",   # ā = the a- of abhabbe
    "antavā": "အဆုံး ရှိသော", "anantavā": "အဆုံး မရှိသော", "sarīra": "ကိုယ်ခန္ဓာ",
    "bhavadiṭṭhi": "ဘဝ ဆက်လက် တည်ရှိသည်ဟူသော အယူ", "vibhavadiṭṭhi": "ဘဝ ပျောက်ကွယ်သည်ဟူသော အယူ",
    "sannissitā": "မှီသော", "ante": "အစွန်း", "anupagamma": "မကပ်ရောက်ဘဲ",
    "paccayatā": "ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ", "dhammesu": "သဘောတရား", "paṭiladdhā": "ရရှိထားသော",
    "ānusayā": "ကိန်းအောင်းခြင်း", "rāgānusayo": "ရာဂ ကိန်းအောင်းခြင်း",
    "paṭighānusayo": "မုန်းတီးမှု ကိန်းအောင်းခြင်း", "anuseti": "ကိန်းအောင်းသည်",
    "piyarūpaṃ": "ချစ်ဖွယ် သဘော", "sātarūpaṃ": "နှစ်သက်ဖွယ် သဘော", "appiyarūpaṃ": "မချစ်ဖွယ် သဘော",
    "asātarūpaṃ": "မနှစ်သက်ဖွယ် သဘော", "ānupatitā": "လိုက်ပါ ကျရောက်သော",
    "Tadekaṭṭho": "ထိုအရာနှင့် တစ်နေရာတည်း တည်ရှိသော", "ekaṭṭho": "တစ်နေရာတည်း တည်ရှိသော",
    "Puññābhisaṅkhāro": "ကောင်းမှုကို ပြုပြင်ဖန်တီးမှု", "apuññābhisaṅkhāro": "မကောင်းမှုကို ပြုပြင်ဖန်တီးမှု",
    "āneñjābhisaṅkhāro": "မတုန်လှုပ်ခြင်းကို ပြုပြင်ဖန်တီးမှု", "ābhisaṅkhāro": "ပြုပြင်ဖန်တီးမှု",
    "bhūmako": "ဘုံနှင့် ဆိုင်သော",
    "adhimutti": "စိတ်ညွတ်ရာ", "rajakkhā": "ကိလေသာ မြူ", "akkhā": NONE,
    "kilesavatthūni": "ကိလေသာ အခြေခံ", "Dasa kilesavatthūni": "ကိလေသာ အခြေခံ ဆယ်ပါး",
    "āsevitāni": "မှီဝဲအပ်ပြီးသော", "bhāvitāni": "ပွားများအပ်ပြီးသော", "bahulīkatāni": "အဖန်ဖန် ပြုအပ်ပြီးသော",
    "ussadagatāni": "ထူထပ်နေသော", "anāsevitāni": "မမှီဝဲအပ်သော", "abhāvitāni": "မပွားများအပ်သော",
    "abahulīkatāni": "အဖန်ဖန် မပြုအပ်သော", "anussadagatāni": "မထူထပ်သော",
    "mudindriyā": "စွမ်းရည် နုံ့သော", "tikkhindriyā": "စွမ်းရည် ထက်မြက်သော", "indriyā": "စွမ်းရည်",
    "dvākārā": "အခြင်းအရာ ဆိုးသော", "svākārā": "အခြင်းအရာ ကောင်းသော", "ākārā": "အခြင်းအရာ",
    "āsayā": "စိတ်သဘောထား ရှိသော", "caritā": "စရိုက် ရှိသော",
    "kalyāṇacaritā": "ကောင်းမြတ်သော စရိုက် ရှိသော", "kalyāṇādhimuttikā": "ကောင်းမြတ်သော စိတ်ညွတ်ရာ ရှိသော",
    "suviññāpayā": "သိအောင် ပြောပြရ လွယ်သော", "duviññāpayā": "သိအောင် ပြောပြရ ခက်သော",
    "viññāpayā": "သိအောင် ပြောပြရ",
    "kammāvaraṇena": "ကံ အဟန့်အတား", "kilesāvaraṇena": "ကိလေသာ အဟန့်အတား", "āvaraṇena": "အဟန့်အတား",
    "samannāgatā": "ပြည့်စုံသော", "āvaraṇena samannāgatā": "အဟန့်အတားနှင့် ပြည့်စုံသော",
    "assaddhā": "ယုံကြည်မှု မရှိသော", "acchandikā": "ဆန္ဒ မရှိသော", "chandikā": "ဆန္ဒ ရှိသော",
    "abhabbā": "မထိုက်တန်သော", "bhabbā": "ထိုက်တန်သော", "niyāmaṃ": "သေချာသော လမ်းကြောင်း",
    "okkamituṃ": "သက်ဆင်းရန်", "sammattaṃ": "မှန်ကန်မှု",
    # --- power 7: jhāna, vimokkha, samādhi, samāpatti (^2-828)
    "jhāyī": "ဈာန်ဝင်စားသူ", "samānaṃ": NONE,      # «sampattiyeva samānaṃ»: the participle «being» has no word
    "vipatti": "ချို့ယွင်းမှု", "pacceti": "ထင်မှတ်သည်",
    "khippaṃ samāpajjati": "လျင်မြန်စွာ ဝင်စားသည်", "dandhaṃ samāpajjati": "နှေးကွေးစွာ ဝင်စားသည်",
    "samādhismiṃ samādhi": "သမာဓိ၌ သမာဓိ", "samādhismiṃ samāpatti": "သမာဓိ၌ ဝင်စားခြင်း", "samādhī": "သမာဓိ",
    "vimokkho": "လွတ်မြောက်ခြင်း", "vimokkhā": "လွတ်မြောက်ခြင်း", "saññī": "မှတ်သိမှု ရှိသူ",
    "Subhanteva": "တင့်တယ်သည်ဟုသာ", "adhimutto": "စိတ်ညွတ်သော",
    "rūpasaññānaṃ": "ရုပ်ဟု မှတ်သိမှု", "paṭighasaññānaṃ": "ထိခိုက်မှုဟု မှတ်သိမှု", "paṭigha": "ထိခိုက်မှု",
    "nānattasaññānaṃ": "အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှု", "ananto": "အဆုံး မရှိသော", "ākāso": "ဟင်းလင်းပြင်",
    "ākāsānañcāyatanaṃ": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်", "natthi kiñci": "ဘာမျှ မရှိ",
    "nevasaññānāsaññāyatanaṃ": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်",
    "pañcamo": "ပဉ္စမ", "chaṭṭho": "ဆဋ္ဌမ", "sattamo": "သတ္တမ", "aṭṭhamo": "အဋ္ဌမ",
    "Saṃkilesa": "ညစ်နွမ်းခြင်း", "Vodāna": "စင်ကြယ်ခြင်း", "Vuṭṭhāna": "ထမြောက်ခြင်း",
    "vuṭṭhānampi": "ထမြောက်ခြင်း … လည်း",
    "hānabhāgiyo": "ဆုတ်ယုတ်ခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော", "visesabhāgiyo": "ထူးခြားခြင်း၏ အစိတ်အပိုင်း ဖြစ်သော",
    # --- power 8: pubbenivāsa (^2-829)
    "anekavihitaṃ": "အမျိုးမျိုးသော", "pubbenivāsaṃ": "ရှေးဘဝ", "anussarati": "အဖန်ဖန် အောက်မေ့တော်မူသည်",
    "ānussati": "အဖန်ဖန် အောက်မေ့ခြင်း", "jātiṃ": "ဘဝ", "jātiyo": "ဘဝ",
    "dasapi": "ဆယ်", "dasapi jātiyo": "ဆယ်ဘဝ", "vīsampi": "နှစ်ဆယ်", "tiṃsampi": "သုံးဆယ်",
    "cattālīsampi": "လေးဆယ်", "paññāsampi": "ငါးဆယ်", "satampi": "တစ်ရာ", "sahassampi": "တစ်ထောင်",
    "kappe": "ကမ္ဘာ", "saṃvaṭṭa": "ပျက်ခြင်း", "vivaṭṭa": "တည်ခြင်း", "amutra": "အခြားဘဝ",
    "nāmo": "အမည်", "gotto": "အနွယ်", "vaṇṇo": "အဆင်း", "āhāro": "အစာ", "paṭisaṃvedī": "ခံစားခဲ့သော",
    "āyu": "အသက်", "pariyanto": "အပိုင်းအခြား", "cuto": "သေသော", "udapādiṃ": "ဖြစ်ပေါ်ခဲ့သည်",
    "ūpapanno": "ဖြစ်ပေါ်လာသော", "sākāraṃ": "အခြင်းအရာနှင့် တကွ",
    # --- power 9: cutūpapāta (^2-830)
    "dibbena": "နတ်", "visuddhena": "စင်ကြယ်သော", "atikkanta": "ကျော်လွန်သော", "mānusakena": "လူ၏ မျက်စိ",
    "cavamāne": "သေဆဲ", "hīne": "ယုတ်ညံ့သော", "paṇīte": "မွန်မြတ်သော", "suvaṇṇe": "အဆင်း လှသော",
    "dubbaṇṇe": "အဆင်း ဆိုးသော", "sugate": "ကောင်းသော လားရာ ရှိသော", "duggate": "ဆိုးသော လားရာ ရှိသော",
    "yathākammūpage": "ကံအားလျော်စွာ ရောက်သွားသော", "ūpage": "ရောက်သွားသော", "vata": NONE,  # emphatic particle
    "kāyaduccaritena": "ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်", "vacīduccaritena": "နှုတ်ဖြင့် ပြုသော ဒုစရိုက်",
    "manoduccaritena": "မနောဖြင့် ပြုသော ဒုစရိုက်", "duccaritena": "ဒုစရိုက်",
    "kāyasucaritena": "ကိုယ်ဖြင့် ပြုသော သုစရိုက်", "vacīsucaritena": "နှုတ်ဖြင့် ပြုသော သုစရိုက်",
    "manosucaritena": "မနောဖြင့် ပြုသော သုစရိုက်", "sucaritena": "သုစရိုက်",
    "upavādakā": "စွပ်စွဲ ပြောဆိုသော", "micchādiṭṭhikā": "မှားယွင်းသော အယူ ရှိသော", "samādānā": "ဆောက်တည်သော",
    "upapannā": "ရောက်သော",
    # --- power 10 (^2-831)
    "vimuttiṃ": "လွတ်မြောက်ခြင်း", "cetovimuttiṃ": "စိတ်၏ လွတ်မြောက်ခြင်း", "diṭṭheva dhamme": "မျက်မှောက်ဘဝ၌ပင်",
    "viharatī": "နေတော်မူသည်", "upasampajja viharatī": "ဝင်စား၍ နေတော်မူသည်",
    "Nevasaññānāsaññāyatanasahagatā": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်နှင့်အတူ ဖြစ်သော",
}
# the same senses in chapter 16 as in chapter 15 (the paṭisambhidā list ^2-800, the objects of knowledge «X-e ñāṇaṃ»)
for _k in ("paṭisambhidā", "atthapaṭisambhidā", "dhammapaṭisambhidā", "niruttipaṭisambhidā", "paṭibhānapaṭisambhidā",
           "nirutti", "paṭibhāna", "ābhilāpe", "ñāṇaṃ", "ñāṇesu", "Atthe", "jānāti",
           "dukkhasamudaye", "Jarāmaraṇe", "maraṇe", "jarāmaraṇanirodhe", "Jarāmaraṇe ñāṇaṃ", "Jātiyā", "bhave",
           "upādāne", "taṇhāya", "phasse", "āyatane", "nāmarūpe", "rūpe", "viññāṇe", "viññāṇe ñāṇaṃ", "saṅkhāresu",
           "saṅkhāresu ñāṇaṃ", "saṅkhāranirodhe", "phalesu", "maggesu", "apacayagāminī", "ācayagāmino",
           "kāmāvacarassa kusalassa", "rūpārammaṇaṃ", "sasaṅkhārena", "āyatanaṃ", "ākiñcaññāyatanaṃ"):
    T_NANA.setdefault(_k, T_PATI[_k])
for _st, _n in (("vitakka", "စတင်ကြံစည်မှု"), ("vicāra", "ဆက်လက်သုံးသပ်မှု"), ("pīti", "ပီတိ"),
                 ("sukha", "သာယာမှု"), ("upekkhā", "ဥပေက္ခာ"), ("vitakkavicāra", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု")):
    T_NANA.setdefault(_st + "sampayuttā", _n + "နှင့် ယှဉ်တွဲသော")
    T_NANA.setdefault(_st + "vippayuttā", _n + "နှင့် ကင်းကွာသော")

SECTIONS = {
    "15-patisambhidavibhango": T_PATI,
    "16-nanavibhango": T_NANA,
    # the approved sample's tables (shared fallbacks, never written here)
    "preamble": T_PREAMBLE,
    "1-khandhavibhango": T_KHANDHA,
}
CHAPTERS = ["15-patisambhidavibhango", "16-nanavibhango"]


# =====================================================================================================
# rules (written to map-table.md)
# =====================================================================================================
RULES = """## Rules

**Binding and unchanged:** the approved pi-1 rules (pi-1 `map-table.md` rules 1–11, the agreed later pi-1 rules in
`map-table-2-01 … -5.md` and `map-harmonise-notes.md`) and the approved pi-2 sample (`map-table.md`, N1–N11, the
values of `preamble.mapped.md` / `1-khandhavibhango.mapped.md`). This script is a copy of the sample's `map_all.py`
(its tables T_PREAMBLE / T_KHANDHA, cluster compounds, compose rules, context functions and verifier) with this run's
tables T_PATI (ch. 15) and T_NANA (ch. 16); the two new tables do not leak into each other. Lookup: CTX → own chapter
table → the sample's tables → the final pi-1 mapping (the most frequent pi-1 value present in THAT segment) → compose.
The Burmese is the FINAL pi-2 text; the Burmese forms follow `notes-ch15-16.md` («New strings») and
`harmonise-notes.md`.

Approved rules used as they stand: nouns without final case particle / plural (rule 1); attributes in «…သော» without
the head (rule 3); verbs «…သည်» (rule 4); «na X» = «…သည် မဟုတ်သော» (rule 5); discontinuous « … » (rule 10); fragments
(rule 8, ākusalā = အကုသိုလ်, ābhabbe = မထိုက်တန်သော: the vowel ā keeps the a- of the member); absolutives keep «၍»;
«X-meva» = the Mātikā value of X (pi-1 3, ^1-594); relative pronouns yaṃ / yā / Yaṃ = (no direct equivalent) (pi-1
2-01 rule 12) but «ye vā pana» = «ရှိသမျှလည်း» and Ye = «ရှိသမျှ» (pi-1); «samaye» = အချိန်; sense by context, one
sense per segment (rūpa, dhamma, attha, vatthu, nānā, ṭhāna, mattā, see the CTX table); the time-list «uppanna» =
«ဖြစ်ပေါ်ပြီးသော» (sample); bahiddhā = «မိမိ၏ ပြင်ပ၌» (sample N10); vipākadhammadhammā = «အကျိုး ပေးတတ်သော
သဘောတရား» where the plural stands alone (^2-749) and «အကျိုး ပေးတတ်သော» where paññā is the head (^2-753, sample N6).

## NEW rules (for the user's review)

M1. **The four paṭisambhidā** (notes-ch15-16): paṭisambhidā = «ပိုင်းခြားသိသော ဉာဏ်»; attha = «အကျိုးအနက်» in ch. 15
    and in the paṭisambhidā list of ch. 16 (^2-800) (harmonise: one compound for result and meaning), but «အကျိုး» in
    ch. 16 atthajāpikā / jāpitattha (^2-752, ^2-767); the dhamma of dhammapaṭisambhidā / Dhamme ñāṇaṃ = «တရား»
    (ch. 15, ^2-754, ^2-800), the phenomenon «သဘောတရား» elsewhere; ābhilāpe (fragment of dhammaniruttābhilāpe) =
    «ခေါ်ဆိုခြင်း»; jotakānī / idamatthajotakānī = «(ဤအကျိုးအနက်ကို) ထင်ရှားစေသော»; the headings «X-vāro» = the
    heading whole («အကျဉ်းချုပ် ဖော်ပြချက်» …), Hetu (Hetuvāra) = «အကြောင်းရင်း» (cause, not the Mātikā root).
M2. **«X-e ñāṇaṃ»** = «Xကို သိသော ဉာဏ်» (pi-1 Dukkhe ñāṇaṃ); the bare locative X-e = X without «ကို» (rule 1):
    Jarāmaraṇe = «အိုခြင်းနှင့် သေခြင်း», saṅkhāresu = «ပြုပြင်ဖန်တီးမှု» (the plural «များ» stays inside a phrase:
    saṅkhāresu ñāṇaṃ = «ပြုပြင်ဖန်တီးမှုများကို သိသော ဉာဏ်»); «Xpetaṃ ñāṇaṃ» = «Xကို သိသော ဉာဏ်လည်း» (pi = လည်း; etaṃ
    has no word); anvaye / pariye = «ဆက်စပ်၍ / စိတ်ကို ပိုင်းခြား၍» (the text's own words).
M3. **«X paññā»** (ch. 16) = the attribute(s) + «ပညာ» (the «၊» between two attributes dropped, rule 6):
    «Āsavavippayuttā sāsavā paññā» = «စိတ်အစွန်းအထင်းနှင့် ကင်းကွာသော စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ပညာ»;
    «(bhūmīsu) X-e paññā» = «(ဘုံ … ဖြစ်သော) X၌ ရှိသော ပညာ» (the count of tīsu / catūsu is the gap, pi-1 5 rule 15;
    the locative «၌» stays inside the phrase); «maggesu / phalesu paññā» = «မဂ် / ဖိုလ် … ရှိသော ပညာ» («လေးပါးတို့၌»
    is the gap); «adhisīle paññā» = «လွန်မြတ်သော သီလ၌ ရှိသော ပညာ»; «samāpannassa paññā» = «ဈာန် ဝင်စားသူ၏ ပညာ»
    (genitive part of the term). «X citta»(nti) of the sixteen states of mind = «X စိတ်».
M4. **Locative substantives** kusale / vipāke / ābyākate / kusalābyākate / kiriyābyākate / (rūpāvacarārūpāvacara)kusale
    = the text's noun with the head «သဘောတရား» it adds («ကုသိုလ် သဘောတရား», «ကံ၏ အကျိုး ဖြစ်သော သဘောတရား» …), as pi-1
    5 rule 18 maps kusalaṃ to «ကုသိုလ်စိတ်» where the text adds «စိတ်».
M5. **Subject + predicate keywords** (pi-1 5 rule 21, the particles between are the gap): «ñāṇāni idamatthajotakānī» =
    «ဉာဏ် … ဤအကျိုးအနက်ကို ထင်ရှားစေသော»; «paṭisambhidā aniyatā» = «ပိုင်းခြားသိသော ဉာဏ် … မကျိန်းသေသော»;
    «dhātu uppannā» = «ဓာတ် … ဖြစ်ပေါ်ပြီးသော» (the pi-2 uppanna, sample); «paññā ācayāya» = «စုပုံခြင်းအတွက် … ပညာ»
    (Burmese order); «kāyaviññāṇaṃ na paccanubhoti» = «ကိုယ် သိစိတ် … မခံစား».
M6. **Negated verbs**: a keyword that contains na takes the Burmese negative «မV» (Burmese has no «…သည်» after a
    negated verb): «cakkhuviññāṇaṃ na uppajjati» = «မျက်စိ သိစိတ် မဖြစ်ပေါ်»; a verb keyword without na whose verb the
    text negates keeps the positive dictionary form (rule 8): kappeti = «ပြုလုပ်သည်» (text «မပြုလုပ်», check P2).
M7. **Verb forms**: the aorist keeps the text's past «ခဲ့» (abbhaññaṃsu = «ထူးကဲစွာ သိခဲ့သည်», seviṃsu =
    «မှီဝဲခဲ့သည်»), the future its «လိမ့်မည်» (abhijānissanti = «ထူးကဲစွာ သိလိမ့်မည်», sevissanti = «မှီဝဲလိမ့်မည်»):
    the tense is the keyword's form, so bhajanti / bhajiṃsu / bhajissanti stay apart; the plural «ကြ» goes (check P4).
    The optative -eyya = verb + «သည်» (voropeyya = «သတ်သည်», text «သတ်ရာ၏», check P6). The Tathāgata's honorific
    «…တော်မူ» is the text's verb (harmonise 13): pajānāti = «သိတော်မူသည်», paṭijānāti = «ဝန်ခံတော်မူသည်»; the monk's
    pajānāti (^2-796) = «ကွဲပြားစွာ သိသည်»; jānāti = «သိသည်».
M8. **Datives of purpose keep «အတွက်»** (ācayāya = «စုပုံခြင်းအတွက်», nibbidāya = «ငြီးငွေ့ခြင်းအတွက်»): the case
    meaning, as pi-1 keeps «ရန်» for datives (sample N7). The X-paccayā links of ^2-806 = «Xကြောင့်» (pi-1 ^1-1343).
    The adverbs keep their word: samanantarā = «ချက်ချင်း နောက်၌», diṭṭheva dhamme = «မျက်မှောက်ဘဝ၌ပင်», hetuso /
    ṭhānaso = «အကြောင်းရင်း / ဖြစ်ရာ အခြေအနေ» (the «…အားဖြင့်» = by, a postposition, goes, rule 1), aṭṭhānato =
    «မဖြစ်နိုင်သော အကြောင်း» (the «အဖြစ်» = as goes, pi-1 5 rule 15); niccato / sukhato / atthato = «မြဲသော / သာယာသော /
    အနှစ်သာရ ရှိသော» (the text's «…သည်ဟု ယူဆရာ၏»).
M9. **Numbers and «-pi»**: dasapi / vīsampi … sahassampi = the text's number («ဆယ်», «နှစ်ဆယ်» … «တစ်ထောင်»; the pi is the
    text's «…ကိုလည်းကောင်း»); Sattasattati = «ခုနစ်ဆယ့်ခုနစ်ပါး» (pi-1 5 rule 12); «Xampi» = X + «လည်း» across the
    text's subject particle: tampi = «ထိုဉာဏ် … လည်း» (the text names the pronoun's noun, sample N9), vuṭṭhānampi =
    «ထမြောက်ခြင်း … လည်း».
M10. **(no direct equivalent)** (13 uses): uppannā ^2-745 (the text has one verb for «uppannā hoti … upasampajja
    viharati»); dhammā ^2-753 (only in «-dhammadhammā paññā», sample N6); akkhe / akkhā (rajakkha = «ကိလေသာ မြူ»: no word
    for the eye); vata (emphatic), samānaṃ (the participle «being», ^2-828), hoti (the copula of «vītarāgo hoti», ^2-798);
    yaṃ / yā / Yaṃ (relative pronouns, pi-1 rule).
M11. **Variants of one sense picked by the segment (@alt)**: nānā = «အသီးသီး ကွဲပြားသော» (nānāvatthukā) / «အမျိုးမျိုး»
    (nānādhātu, nānādhimuttikatā); tattha = «ထိုတို့အနက်» («tattha katamā …?») / «ထို၌» (only «yā tattha paññā»,
    ^2-827); paccavekkhaṇā = the pi-1 «ပြန်လည် ဆင်ခြင်ခြင်း» where the text has it (^2-804), «ပြန်လည် ဆင်ခြင်သော»
    (^2-808).

**Presence check, NEW ending rules** (the approved «attr», «verb», «attr-fut», «neg-infix», «neg-attr», «fut» and the
sample's «သည့်» stay):
P1. «attr»: a chunk «Xသော» is also accepted against the text's predicate «Xကြ…» (plural), «Xဟု / Xဟူ» (quotative) and
    «X၏» (literary statement ending): rule 3's «…သည်» → «…သော» with the other statement endings of the text.
P2. «neg-verb»: a chunk «Xသည်» against the text's negated bare verb «မX» (the keyword has no na; rule 8).
P3. The text's quotation marks “ ” ‘ ’ are ignored by the check (anicca in «“ရုပ်သည် မမြဲ”ဟူ၍»).
P4. «plural»: «Xလိမ့်မည်» / «Xခဲ့သည်» against the text's «Xကြလိမ့်မည်» / «Xခဲ့ကြ…» (the plural «ကြ» before the tense).
P5. «verb» also from the conditional «Xလျှင်» (^2-799: «samudācaranti …» = «… ထကြွလာလျှင်»).
P6. «verb» also from the optative «Xရာ(၏)» (pi-1 5 rule 22 «ကြရာ»; ^2-809).
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
for _t in (T_PREAMBLE, T_KHANDHA):    # the approved sample's tables only: T_PATI and T_NANA do not leak into each other
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
    if v is not None:
        return resolve(v, kw, pali, my), "table"
    v = table_get(SHARED, kw)
    if v is not None:
        return resolve(v, kw, pali, my), "sample"
    v = pi1_get(kw, my)
    if v is not None:
        return v, "pi1"
    return None, None


# heads of the attributive pairs «rūpaṃ atītaṃ», «Sāsavā vedanā», «cakkhusamphassajā saññā» (Burmese: attr + head)
HEADS = {"rūpaṃ", "vedanā", "saññā", "saṅkhārā", "viññāṇaṃ", "cetanā"}
# subjects of the subject + predicate pairs «Rūpakkhandho hetuvippayutto», «khandhā cittasaṃsaṭṭhā»,
# «dasavidhena vedanākkhandho» (pi-1 5 rule 21: the text's particles between go, « … » marks the gap)
SUBJ = re.compile(r"^(Rūpakkhandho|Vedanākkhandho|Saññākkhandho|Saṅkhārakkhandho|Viññāṇakkhandho|khandhā|"
                  r"dasavidhena) (.+)$")


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
    if ws[-1] == "citta" and len(ws) == 2:   # «X citta»(nti) of the sixteen states of mind = «X စိတ်»
        return lookup(ch, sid, ws[0], pali, my) + " စိတ်"
    if ws[-1] == "paññā" and ws[-2].endswith(("e", "su")):
        # NEW (15-16 rule N3b): «(bhūmīsu) X-e paññā» = «(ဘုံ … ဖြစ်သော) X၌ ရှိသော ပညာ» (notes-ch15-16 X-e paññā);
        # the count of «tīsu / catūsu bhūmīsu» is not in the keyword: it is the gap « … »
        pre = ""
        if ws[0] == "bhūmīsu":
            pre, ws = "ဘုံ … ဖြစ်သော ", ws[1:]
        return pre + lookup(ch, sid, " ".join(ws[:-1]), pali, my) + "၌ ရှိသော ပညာ"
    if ws[-1] == "paññā":               # NEW (15-16 rule N3a): «X paññā» = the attribute(s) + «ပညာ»
        rest = " ".join(ws[:-1])
        try:
            b = lookup(ch, sid, rest, pali, my)
        except KeyError:
            b = " ".join(lookup(ch, sid, w, pali, my) for w in ws[:-1])
        return b + " ပညာ"
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
    h = harmonise_rules.apply(kw, sid, v, my)      # map-harmonise: book-wide alignments (harmonise_rules.py)
    if h != v:
        v, src = h, "harmonise"
    SRC[(sid, kw)] = src
    return v


# ---- presence check: the ONE check shared by all pi-2 mapping scripts (presence_check.py; map-harmonise
# decision 3: the merged, documented ending list). Imported, not copied, so every script uses the same form.
sys.path.insert(0, str(HERE))
from presence_check import ATTR_FROM, VERB_FROM, chunk_present, presence  # noqa: E402,F401
import harmonise_rules  # noqa: E402  (map-harmonise: the book-wide alignments, applied in lookup())


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
    "bahiddhā": "pi-1 «သူတစ်ပါး၌ / ပြင်ပ၌ / အပြင်ဘက်» do not occur as the term: the pi-2 text's qualifier is «မိမိ၏ ပြင်ပ၌» (sample N10)",
    "adhimutti": "the disposition of beings «စိတ်ညွတ်ရာ» (^2-818); pi-1 «အလွန် လွတ်မြောက်မှု» is another sense and not in the segment",
    "arahatta": "the path / fruit name «အရဟတ္တ(ဖိုလ်)»; pi-1 «ရဟန္တာ» (the person) does not occur",
    "avasesā": "the text's word «ကြွင်းသော»; pi-1 «ကြွင်းကျန်သော» does not occur",
    "aññaṃ": "the text's word «တခြား» (^2-762); pi-1 «တခြားစီ» does not occur in the segment",
    "catukka": "heading «group of four» (Catukkamātikā / -niddeso); pi-1 «ဈာန် လေးပါး» is the jhāna method",
    "pañcaka": "heading «group of five»; pi-1 «ဈာန် ငါးပါး» is the jhāna method",
    "dhammaṃ": "the dhamma of the paṭisambhidā / pariyatti «တရား» (M1, ^2-724)",
    "dhamme": "the dhamma of dhammapaṭisambhidā «တရား» (M1); pi-1 «တရားတော်» does not occur",
    "dhammā": "^2-753: only inside «-dhammadhammā paññā», no word (sample N6, M10)",
    "dhātu uppannā": "the pi-2 text's uppanna «ဖြစ်ပေါ်ပြီးသော» (sample) with the subject particle as the gap (M5); ^2-745 has no verb (M10)",
    "dukkhaṃ": "the noble truth «ဒုက္ခ» (pi-1 Dukkhe = ဒုက္ခ); pi-1 «နာကျင်မှု» is the feeling",
    "hetu": "Hetuvāra: the cause «အကြောင်းရင်း» (notes-ch15-16), not the Mātikā root «အမြစ်»",
    "hetū": "^2-809 «hetū paccayā» = «အကြောင်းရင်း၊ အကြောင်း»: hetu = «အကြောင်းရင်း» (notes-ch15-16)",
    "hoti": "^2-798: the copula of «vītarāgo hoti» has no word (M10)",
    "iddhi": "the text's «တန်ခိုး» (iddhividha); pi-1 «ဣဒ္ဓိ» does not occur",
    "khanti": "acceptance «သည်းခံ လက်ခံမှု» (notes-ch15-16); pi-1 «သည်းခံခြင်း» does not occur",
    "manasikārā": "the pi-2 text writes «နှလုံးသွင်းခြင်း» as one word; pi-1 «နှလုံး သွင်းခြင်း» (with a space) is not the text's form",
    "nirodha": "fragment of nirodhadhamma «ချုပ်ငြိမ်းတတ်သော» (^2-806) and saññāvedayitanirodha «ချုပ်ငြိမ်းရာ» (^2-808): the text's stem",
    "paccavekkhaṇā": "^2-808: «paccavekkhaṇāñāṇaṃ» = «ပြန်လည် ဆင်ခြင်သော ဉာဏ်», the pi-1 noun does not occur (M11)",
    "paṭigha": "the jhāna paṭighasaññā «ထိခိုက်မှုဟု မှတ်သိမှု» (impact); pi-1 «မုန်းတီးမှု» is aversion",
    "pāpa": "pāpāsayā … «ယုတ်မာသော»; pi-1 «ဆိုး» occurs in ^2-823 only as the word of dvākārā",
    "rūpa": "^2-806 nāmarūpa «ရုပ်ပိုင်း» (pi-1 nāma-rūpa, ^1-1317)",
    "rūpaṃ": "^2-816 piyarūpaṃ «ချစ်ဖွယ် သဘော» (nature), not matter",
    "rūpāni": "^2-828 «rūpāni passati» = «အဆင်းအရောင်တို့ကို မြင်၏» (visible forms)",
    "samāpattiyā": "the attainment «ဈာန် ဝင်စားရာ» (notes-ch15-16); pi-1 «ကျူးလွန်ခြင်း» is āpatti (offence)",
    "saññī": "arūpasaññī «… မှတ်သိမှု မရှိသူ»: the fragment's positive «မှတ်သိမှု ရှိသူ» (rule 8); pi-1 «မှတ်သိသော» does not occur",
    "suttaṃ": "the aṅga name «သုတ်»; pi-1 «ချည်ကြိုး» (thread) is another sense",
    "sutvā": "the text's «ကြားနာ၍»; pi-1 «ကြား၍» does not occur",
    "uppannā": "^2-745: no word of its own (M10)",
    "vata": "the emphatic particle has no word (M10); pi-1 «အကျင့်ဝတ်» is vata (observance)",
    "vihāra": "anupubbavihāra «နေထိုင်ရာ»; pi-1 «ဗြဟ္မစိုရ်» is brahmavihāra",
    "vijjā": "vijjāṭṭhāna «အသိပညာ ဌာန» (field of learning); pi-1 «အမှန်သိမြင်မှု» is true knowledge",
    "vipatti": "the text's «ချို့ယွင်းမှု» (^2-828); pi-1 «ပျက်စီးခြင်း» does not occur",
    "vipākadhammadhammā": "^2-753 «vipākadhammadhammā paññā»: the head is paññā, the final -dhamma has no word (sample N6)",
    "vuṭṭhāna": "the text's «ထမြောက်ခြင်း» (^2-828); pi-1 «ထမြောက်ရာ» does not occur",
    "yoga": "yogavihita «ပညာရှိတို့ စီမံထားသော» (notes-ch15-16); pi-1 «ထမ်းပိုး» is the bond",
    "āhāro": "the text's «အစာ» (^2-829); pi-1 «အာဟာရ» does not occur",
    "āyatana": "the jhāna sphere «နယ်ပယ်» (ākāsānañcāyatana …); pi-1 «အာရုံခံ နယ်ပယ်» is the sense base",
    "āyatanaṃ": "the jhāna sphere «နယ်ပယ်» (ākiñcaññāyatanaṃ); pi-1 «အာရုံခံ နယ်ပယ်» is the sense base",
    "āyu": "the text's «အသက်» (^2-829); pi-1 «သက်တမ်း» does not occur",
}

for _k, _r in harmonise_rules.REASONS.items():
    REASONS.setdefault(_k, _r)


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
    with open(HERE / "map-table-15-16.md", "w", encoding="utf-8") as f:
        f.write("# pi-2 Burmese keyword mapping: rules and review table (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း»: "
                + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_15-16.py (a copy of the approved sample map_all.py). Burmese from the FINAL pi-2 text of this track only "
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
                            + f" | {REASONS.get(kw) or REASONS.get(kw.lower(), 'UNEXPLAINED')} |\n")
        f.write("\n")
        f.write(RULES)
        f.write("\n## Per-segment overrides (CTX; the reasons are the comments in map_15-16.py)\n\n"
                "| segment | keyword | value |\n|---|---|---|\n")
        for sid, d in CTX.items():
            for k, v in d.items():
                f.write(f"| {sid} | {k} | {v} |\n")
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
    if args and args[0] in ("--seg", "--segb"):
        show(args[1:], pali=args[0] == "--seg")
        sys.exit()
    if args and args[0] == "--srcs":
        want = set(args[1:]) or {"pi1", "sample"}
        agg = collections.defaultdict(list)
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            for sid, kws in rows:
                for kw in [k.strip() for k in kws.split(", ")]:
                    v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                    if SRC[(sid, kw)] in want:
                        agg[(SRC[(sid, kw)], kw, v)].append(sid)
        for (src, kw, v), sids in sorted(agg.items()):
            print(f"{src}\t{kw}\t{v}\t{len(sids)}\t{' '.join(sids[:4])}")
        sys.exit()
    if args and args[0] == "--kw":
        for ch in CHAPTERS:
            for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
                sid, rest = LINE.match(l).groups()
                for kv in rest.split(", "):
                    k, v = kv.split("=", 1)
                    if k in args[1:]:
                        print(f"{sid}\t{k}\t{v}")
        sys.exit()
    if args and args[0] == "--pi1":
        for kw in args[1:]:
            print(kw, "=>", " · ".join(f"{v} ({n})" for v, n in pi1_vals(kw).most_common(6)))
        sys.exit()
    if args and args[0] == "--new":
        n = int(args[1]) if len(args) > 1 else 5
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            for sid, kws in rows:
                if n <= 0:
                    break
                miss, have = [], []
                for kw in [k.strip() for k in kws.split(", ")]:
                    try:
                        v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                        if not presence(v, my[sid])[0]:
                            have.append(f"{kw}={v} FAIL")
                    except KeyError:
                        miss.append(kw)
                if miss or any(h.endswith(" FAIL") for h in have):
                    n -= 1
                    print("==", sid)
                    print(pa.get(sid))
                    print(my[sid])
                    print("FAIL:", " | ".join(have))
                    print("MISS:", ", ".join(miss))
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
