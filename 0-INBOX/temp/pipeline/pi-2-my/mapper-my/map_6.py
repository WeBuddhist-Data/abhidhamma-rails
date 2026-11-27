"""Pāli→Burmese keyword mapping for pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»), chapter 6-paticcasamuppadavibhango.

A copy of the approved sample script map_all.py (tables, compose rules, context functions, verifier unchanged; the
sample tables T_PREAMBLE / T_KHANDHA stay as shared tables) with the chapter table T_PATICCA, the context functions
f_rupa6 / f_dukkha, ALT / CTX entries, the working aid --kwin, and map-table-6.md as its table file. It writes only
6-paticcasamuppadavibhango.mapped.md and map-table-6.md.

usage (python3 -I -X utf8, from any directory):
  map_all.py             writes <ch>.mapped.md for every chapter in CHAPTERS and map-table.md, then verifies them
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


T_PATICCA = {
    # --- headings (the heading's own Burmese, pi-1 decision 4; my2-zeroshot-terms ch6)
    "catukkaṃ": "လေးမျိုးတွဲ",
    "Paccayacatukkaṃ": "အကြောင်း လေးမျိုးတွဲ",
    "Hetu": "အကြောင်းပြုခြင်း",                     # Hetucatukkaṃ «အကြောင်းပြုခြင်း လေးမျိုးတွဲ»
    "Sampayuttacatukkaṃ": "ယှဉ်တွဲခြင်း လေးမျိုးတွဲ",
    "Aññamañña": "အချင်းချင်း အကြောင်းဖြစ်ခြင်း",
    "Aññamaññacatukkaṃ": "အချင်းချင်း အကြောင်းဖြစ်ခြင်း လေးမျိုးတွဲ",
    "vipākaniddeso": "ကံ၏ အကျိုးကို အကျယ် ဖော်ပြချက်",
    "mūlakavipāka": "အခြေခံသော ကံ၏ အကျိုး",
    # --- the twelve links (pi-1 ^1-1343: paccayā = ကြောင့်; «Xpaccayā» = «Xကြောင့်», the ablative is the keyword's
    #     meaning, as N7 of the sample keeps «အကြောင်းပြု၍»)
    "paccayā": "ကြောင့်",
    "Avijjāpaccayā": "အမှန်ကို မသိမှုကြောင့်", "avijjāpaccayā": "အမှန်ကို မသိမှုကြောင့်",
    "saṅkhārapaccayā": "@alt", "Saṅkhārapaccayā": "@alt",
    "viññāṇapaccayā": "သိစိတ်ကြောင့်",
    "nāmarūpaṃ": "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း", "nāmarūpa": "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း",
    "rūpapaccayā": "ရုပ်ပိုင်းကြောင့်",                # fragment of nāmarūpapaccayā
    "nāmapaccayā": "စိတ်ပိုင်းကြောင့်", "Nāmapaccayā": "စိတ်ပိုင်းကြောင့်",
    "saḷāyatanaṃ": "အာရုံခံ နယ်ပယ် ခြောက်ပါး", "saḷāyatana": "အာရုံခံ နယ်ပယ် ခြောက်ပါး",
    "saḷāyatanapaccayā": "အာရုံခံ နယ်ပယ် ခြောက်ပါးကြောင့်",
    "chaṭṭhāyatanaṃ": "ဆဋ္ဌမ အာရုံခံ နယ်ပယ်", "chaṭṭhāyatana": "ဆဋ္ဌမ အာရုံခံ နယ်ပယ်",
    "āyatanapaccayā": "အာရုံခံ နယ်ပယ်ကြောင့်",       # fragment of chaṭṭhāyatanapaccayā
    "phassapaccayā": "တွေ့ထိမှုကြောင့်", "vedanāpaccayā": "ခံစားမှုကြောင့်", "taṇhāpaccayā": "တပ်မက်မှုကြောင့်",
    "upādānapaccayā": "စွဲလမ်းမှုကြောင့်", "bhavapaccayā": "ဘဝကြောင့်", "jātipaccayā": "မွေးဖွားခြင်းကြောင့်",
    "jarāmaraṇaṃ": "@alt",
    "domanassupāyāsā": "စိတ်ဆင်းရဲမှု ပြင်းစွာ ပူပန်ခြင်း",   # list «…၊ …» (rule 6: «၊» dropped)
    "saṅkhāro": "ပြုပြင်ဖန်တီးမှု",
    "dukkhakkhandhassa": "ဒုက္ခ အစုအဝေး",
    "kevalassa dukkhakkhandhassa": "ဒုက္ခ အစုအဝေး အားလုံး",
    # --- the Suttanta definitions (the forms of THIS text, harmonised)
    "Puññābhisaṅkhāro": "ကောင်းမှု ဖြစ်စေသော ပြုပြင်ဖန်တီးမှု",
    "apuññābhisaṅkhāro": "မကောင်းမှု ဖြစ်စေသော ပြုပြင်ဖန်တီးမှု",
    "āneñjābhisaṅkhāro": "မတုန်လှုပ်သော ပြုပြင်ဖန်တီးမှု",
    "ābhisaṅkhāro": "ပြုပြင်ဖန်တီးမှု",                 # fragment (head of the three abhisaṅkhāra)
    "kāyasaṅkhāro": "ကိုယ် ပြုပြင်ဖန်တီးမှု",
    "dāna": "ဒါန", "bhāvanā": "ဘာဝနာ",
    "dukkhasamudaye": "ဒုက္ခ ဖြစ်ပေါ်ခြင်း",
    "attavādupādānaṃ": "အတ္တဟူသော ဝါဒ စွဲလမ်းမှု",
    "kammabhavo": "ကံ ဘဝ", "upapattibhavo": "ပြန်လည် ဖြစ်ပေါ်ခြင်း ဘဝ",
    "ekavokāra": "အစုအဝေး တစ်ပါး ရှိသော", "catuvokāra": "အစုအဝေး လေးပါး ရှိသော",
    "pañcavokāra": "အစုအဝေး ငါးပါး ရှိသော",
    "nevasaññānāsaññā": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော",
    "pātubhāvo": "ထင်ရှား လာခြင်း", "sañjāti": "ကောင်းစွာ မွေးဖွားခြင်း", "okkanti": "သက်ဆင်းခြင်း",
    "abhinibbatti": "ထင်ရှားစွာ ပေါ်ထွက်ခြင်း", "nikāye": "အမျိုးအစား", "paṭilābho": "ရရှိခြင်း",
    "cuti": "စုတေခြင်း", "maccu": "သေမင်း", "kālakiriyā": "ကွယ်လွန်ခြင်း", "kaḷevarassa": "ကိုယ်ခန္ဓာ",
    "nikkhepo": "စွန့်ပစ်ခြင်း", "jīvitindriya": "အသက်၏ စွမ်းရည်", "upacchedo": "ပြတ်စဲခြင်း",
    "taca": "အရေ", "vali": "တွန့်ခြင်း",              # valittacatā «အရေတွန့်ခြင်း»
    "soko": "စိုးရိမ်ခြင်း", "socanā": "စိုးရိမ်နေခြင်း", "anto": "အတွင်း", "parisoko": "ပြင်းစွာ စိုးရိမ်ခြင်း",
    "parijjhāyanā": "လောင်မြိုက်ခြင်း", "domanassaṃ": "စိတ်ဆင်းရဲမှု", "sallaṃ": "ငြောင့်",
    "Ñāti": "ဆွေမျိုး", "bhoga": "စည်းစိမ်", "roga": "ကျန်းမာရေး", "byasanena": "ပျက်စီးခြင်း",
    "phuṭṭhassa": "ထိခိုက်ခံရသူ", "byasanena vā phuṭṭhassa": "ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ",
    "samannāgatassa": "ကြုံတွေ့နေရသူ", "dukkha": "@dukkha", "dhammena": "ဖွယ်ရာ",
    "ādevo": "ငိုခြင်း", "paridevo": "ငိုကြွေးခြင်း", "ādevanā": "ငိုနေခြင်း", "palāpo": "ပေါက်ကရ ပြောခြင်း",
    "vippalāpo": "ကမောက်ကမ ပြောခြင်း", "lālappo": "မြည်တမ်းခြင်း",
    "āyāso": "ပူပန်ခြင်း", "upāyāso": "ပြင်းစွာ ပူပန်ခြင်း",
    "asātaṃ dukkhaṃ": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော",
    "asātaṃ dukkhaṃ vedayitaṃ": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားရခြင်း",
    "dukkhaṃ vedayitaṃ": "နာကျင်သော ခံစားရခြင်း",
    "asātā dukkhā vedanā": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားမှု",
    "cetasikaṃ asātaṃ": "စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ် မကောင်းမှု",
    "cetosamphassa": "စိတ်၏ တွေ့ထိမှု",
    "saṅgati": "စုဝေးခြင်း", "samāgamo": "ဆုံဆည်းခြင်း", "samodhānaṃ": "ပေါင်းစည်းခြင်း",
    "Tena": "ထို့ကြောင့်",
    "rūpa": "@rupa6", "Rūpa": "@rupa6", "rūpaṃ": "@rupa6",
    "sammā": "မှန်ကန်သော",                          # sammādiṭṭhi (pi-1), not the preamble's sammāsambuddha
    # --- the Abhidhamma tetrads: hetuka = «Xကို အကြောင်းပြုသော» (pi-1 cittahetukaṃ), qualifier + noun (N3)
    "hetuko": "အကြောင်းပြုသော", "hetukaṃ": "အကြောင်းပြုသော", "hetukā": "အကြောင်းပြုသော",
    "saṅkhāro avijjāhetuko": "အမှန်ကို မသိမှုကို အကြောင်းပြုသော ပြုပြင်ဖန်တီးမှု",
    "vedanā phassahetukā": "တွေ့ထိမှုကို အကြောင်းပြုသော ခံစားမှု",
    "taṇhā vedanāhetukā": "ခံစားမှုကို အကြောင်းပြုသော တပ်မက်မှု",
    "upādānaṃ taṇhāhetukaṃ": "တပ်မက်မှုကို အကြောင်းပြုသော စွဲလမ်းမှု",
    # --- the Abhidhamma definitions
    "sañcetayitattaṃ": "စေ့ဆော်ထားသော အဖြစ်",
    "sātaṃ sukhaṃ": "နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော",
    "sātaṃ sukhaṃ vedayitaṃ": "နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော ခံစားရခြင်း",
    "sātā sukhā vedanā": "နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော ခံစားမှု",
    "nāsātaṃ": "နှစ်သက်ဖွယ် မကောင်းသည်လည်း မဟုတ်သော",   # «neva sātaṃ nāsātaṃ» (rule 5 negative attributive)
    "titthāyatanaṃ": "အယူဝါဒတို့၏ တည်ရာ",
    "nibbatti": "ပေါ်ထွက်ခြင်း", "abhinibbati": "ထင်ရှားစွာ ပေါ်ထွက်ခြင်း",
    "nandirāgo": "နှစ်သက်မှု ရာဂ",
    "sasaṅkhārena": "တိုက်တွန်းမှုဖြင့်",              # sa- «with» = ဖြင့် (the instrumental is the keyword's meaning)
    "adhimokkhapaccayā": "ဆုံးဖြတ်မှုကြောင့်", "adhimuccanā": "ဆုံးဖြတ်ခြင်း",
    "tadadhimuttatā": "ထိုအာရုံ၌ ဆုံးဖြတ်ထားသော အဖြစ်",
    "paṭighapaccayā": "မုန်းတီးမှုကြောင့်", "vicikicchāpaccayā": "ယုံမှားမှုကြောင့်",
    "uddhaccapaccayā": "ယောက်ယက်ခတ်မှုကြောင့်",
    "dvidhāpatho": "လမ်း နှစ်ခွ", "apariyogāhaṇā": "နက်နက်နဲနဲ မသက်ဝင်နိုင်ခြင်း",
    "chambhitattaṃ": "တောင့်တင်းနေသော အဖြစ်",
    "anekaṃsa": "တစ်ထစ်ချ",       # anekaṃsaggāho «တစ်ထစ်ချ မယူနိုင်ခြင်း»: gāho = ယူနိုင်ခြင်း (pi-1); the an- is the
                                 # မ infixed in the verb (rule 8), so the fragment keeps the adverb only
    "cetaso vikkhepo": "စိတ်၏ ပျံ့လွင့်ခြင်း",
    "pasādo": "ကြည်ညိုမှု", "pasādapaccayā": "ကြည်ညိုမှုကြောင့်",   # confidence (ch6), not pi-1 sense-sensitivity
    "mūlapaccayā": "အမြစ်များကြောင့်",                 # fragment of (a)kusalamūlapaccayā («…၏ အမြစ်များကြောင့်»)
    "kusalamūla": "ကုသိုလ်၏ အမြစ်", "akusalamūla": "အကုသိုလ်၏ အမြစ်",
    "mūlā": "အမြစ်", "kusalamūlā": "ကုသိုလ်၏ အမြစ်",
    "alubbhanā": "မမက်မောခြင်း", "adussanā": "စိတ်မဆိုးခြင်း",
    "Cakkhāyatanassa": "မျက်စိ အာရုံခံ နယ်ပယ်", "sotāyatanassa": "နား အာရုံခံ နယ်ပယ်",
    "ghānāyatanassa": "နှာခေါင်း အာရုံခံ နယ်ပယ်", "jivhāyatanassa": "လျှာ အာရုံခံ နယ်ပယ်",
    "kāyāyatanassa": "ကိုယ် အာရုံခံ နယ်ပယ်",
    "rūpaṃ nissāya": "မှီ၍ … ရုပ်",                   # «Yaṃ rūpaṃ nissāya … vattati» = «… မှီ၍ ဖြစ်ပေါ်ရာ ရုပ်»
    "vattati": "ဖြစ်ပေါ်သည်",                          # «… မှီ၍ ဖြစ်ပေါ်ရာ» (rule 4)
    "manosamphasso": "မနော၏ တွေ့ထိမှု",
    # --- cittuppāda openings (pi-1 values of the jhāna / path openings)
    "rūpārammaṇaṃ": "အဆင်းအရောင်ကို အာရုံပြုသော", "saddārammaṇaṃ": "အသံကို အာရုံပြုသော",
    "gandhārammaṇaṃ": "အနံ့ကို အာရုံပြုသော", "rasārammaṇaṃ": "အရသာကို အာရုံပြုသော",
    "phoṭṭhabbārammaṇaṃ": "အထိအတွေ့ကို အာရုံပြုသော",
    "rūpārammaṇā": "အဆင်းအရောင်ကို အာရုံပြုသော", "saddārammaṇā": "အသံကို အာရုံပြုသော",
    "gandhārammaṇā": "အနံ့ကို အာရုံပြုသော", "rasārammaṇā": "အရသာကို အာရုံပြုသော",
    "phoṭṭhabbārammaṇā": "အထိအတွေ့ကို အာရုံပြုသော",
    "ūpapattiyā maggaṃ": "ဖြစ်ပေါ်ရန် လမ်း", "ūpapattiyā": "ဖြစ်ပေါ်ရန်",
    "rūpūpapattiyā": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်ပေါ်ရန်", "arūpūpapattiyā": "ရုပ်မရှိသော ဘုံ၌ ဖြစ်ပေါ်ရန်",
    "pathavīkasiṇaṃ": "မြေ ကသိုဏ်း",
    "ākiñcaññāyatanaṃ": "ဘာမျှ မရှိသော နယ်ပယ်",
    "nevasaññānāsaññāyatana": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်",
    "ābhiññaṃ": "ထူးကဲစွာ သိခြင်း",
    "paṭipadaṃ dandhābhiññaṃ": "ကျင့်စဉ် … ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    "apacayagāmiṃ": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "maggapariyāpannaṃ": "မဂ်၌ အကျုံးဝင်သော",
    "dhammānaṃ": "သဘောတရား",
    "kāmāvacarassa kusalassa": "ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်",
    "āvacarassa": "ဘုံနှင့် ဆိုင်သော",
    "vipākaṃ": "@alt",
    "dhātu uppannā": "ဓာတ် … ဖြစ်ပေါ်ပြီးသော",
    "ākusalā": "အကုသိုလ်", "ākusalaṃ": "အကုသိုလ်",      # fragments of nākusalā / nākusalaṃ (rule 8)
    "arūpāvacaraṃ jhānaṃ": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ဈာန်",
}


def f_dukkha(kw, pali, my):
    """dukkha, one sense per segment (its FIRST free-standing compound in the Pāli segment): «dukkhadhammena»
    (the soka / parideva / upāyāsa frame) = the text's «ဆင်းရဲဖွယ်ရာ» → ဆင်းရဲ (dhammena = ဖွယ်ရာ);
    dukkhapaṭipadaṃ = ခက်ခဲသော; elsewhere the pi-1 value ဒုက္ခ (dukkhakkhandha, ^1-1343)."""
    m = re.search(r"(?<![\wā])[Dd]ukkh(\w*)", pali)
    rest = m.group(1) if m else ""
    if rest.startswith("adhammena"):
        return "ဆင်းရဲ"
    if rest.startswith("apaṭipad"):
        return "ခက်ခဲသော"                               # dukkhapaṭipadaṃ (pi-1 «ကျင့်စဉ် ခက်ခဲသော»)
    return "ဒုက္ခ"


def f_rupa6(kw, pali, my):
    """rūpa in ch6, one sense per segment: the sense of the keyword's FIRST occurrence in the Pāli segment
    (a-rūpa skipped): inside nāmarūpa = the nāma-rūpa member «ရုပ်ပိုင်း»; rūpāvacara / rūpabhava /
    rūpūpapatti = the fine-material plane «သိမ်မွေ့သော ရုပ်»; rūpataṇhā / rūpārammaṇa / rūpāyatana / rūpadhātu
    = the visible object «အဆင်းအရောင်»; matter «ရုပ်» elsewhere."""
    for m in re.finditer(r"[Rr]ūp([aāū]\w*)", pali):
        before = pali[max(0, m.start() - 4):m.start()]
        if before.endswith("a") and not before.endswith("nāma"):
            continue                                       # arūpa
        rest = m.group(1)
        if before.endswith("nāma"):
            return "ရုပ်ပိုင်း"
        if rest.startswith(("āvacar", "abhav", "ūpapatt")):
            return "သိမ်မွေ့သော ရုပ်"
        if rest.startswith(("ataṇh", "ārammaṇ", "āyatana", "adhātu", "asaññ", "asañcetan")):
            return "အဆင်းအရောင်"
        return "ရုပ်"
    return "ရုပ်"


FUNCS = {"ajjhattam": f_ajjhattam, "rupa": f_rupa, "rupa6": f_rupa6, "dukkha": f_dukkha}
ALT = {
    "saṅkhārapaccayā": ["ပြုပြင်ဖန်တီးမှုများကြောင့်", "ပြုပြင်ဖန်တီးမှုကြောင့်"],
    "jarāmaraṇaṃ": ["အိုခြင်းနှင့် သေခြင်း", "အိုခြင်း သေခြင်း"],
    "vipākaṃ": ["ကံ၏ အကျိုး ဖြစ်သော", "ကံ၏ အကျိုး"],
}
CTX = {
    "2-236": {"indriyānaṃ": "အာရုံခံ အင်္ဂါ"},      # «indriyānaṃ paripāko» = «အာရုံခံ အင်္ဂါတို့ ရင့်ရော်ခြင်း»
}

SECTIONS = {
    "preamble": T_PREAMBLE,
    "1-khandhavibhango": T_KHANDHA,
    "6-paticcasamuppadavibhango": T_PATICCA,
}
CHAPTERS = ["6-paticcasamuppadavibhango"]


# =====================================================================================================
# rules (written to map-table.md)
# =====================================================================================================
RULES = """## Rules

**Binding and unchanged:** pi-1 `map-table.md` rules 1–11, the agreed later pi-1 rules, and the approved pi-2 sample
rules N1–N11 (`map-table.md`); the sample's values are reused for the same keyword in the same kind of segment, and
the final pi-1 mapping is looked up for every keyword the chapter table does not set (the most frequent pi-1 value
present in the segment). No keyword of this chapter is (no direct equivalent).

## NEW rules and values in ch6 (for the user's review)

C1. **paccayā and «X-paccayā»** (the links of the chain): paccayā = «ကြောင့်» (pi-1 ^1-1343; the sample's «အကြောင်းပြု၍»
    belongs to X-samphassapaccayā, which ch6 does not have). The compound keyword «X-paccayā» = «Xကြောင့်» with the
    ablative kept, because «because of» is the keyword's meaning (as sample N7 keeps «အကြောင်းပြု၍»):
    avijjāpaccayā = အမှန်ကို မသိမှုကြောင့်, nāmapaccayā = စိတ်ပိုင်းကြောင့်, adhimokkhapaccayā = ဆုံးဖြတ်မှုကြောင့် …
    The text's plural inside the compound stays (rule 1 strips only at the end): saṅkhārapaccayā =
    «ပြုပြင်ဖန်တီးမှုများကြောင့်» in the Suttanta part (^2-225, ^2-227: plural saṅkhārā) and «ပြုပြင်ဖန်တီးမှုကြောင့်»
    in the Abhidhamma part (singular saṅkhāro); mūlapaccayā (from kusala- / akusalamūlapaccayā) = «အမြစ်များကြောင့်».
    Fragments: rūpapaccayā (from nāmarūpapaccayā) = ရုပ်ပိုင်းကြောင့်; āyatanapaccayā (from chaṭṭhāyatanapaccayā) =
    အာရုံခံ နယ်ပယ်ကြောင့်.
C2. **hetuka in the Hetucatukka** = «(Xကို) အကြောင်းပြုသော» (the text's word, as pi-1 cittahetukaṃ «စိတ်ကို
    အကြောင်းပြုသော»), not the Mātikā root «အမြစ်» (the sample's hetuko): hetuko / hetukaṃ = အကြောင်းပြုသော; the pairs
    = qualifier + noun (N3): saṅkhāro avijjāhetuko = အမှန်ကို မသိမှုကို အကြောင်းပြုသော ပြုပြင်ဖန်တီးမှု. Hetu (from
    Hetucatukkaṃ) = the heading's «အကြောင်းပြုခြင်း». The four tetrad headings keep the heading whole (pi-1 decision 4):
    catukkaṃ = လေးမျိုးတွဲ, Aññamañña = အချင်းချင်း အကြောင်းဖြစ်ခြင်း.
C3. **rūpa, one sense per segment (f_rupa6)**: the sense of the first rūpa compound of the Pāli segment (a-rūpa
    skipped): inside nāmarūpa = the pair member «ရုပ်ပိုင်း» (a pi-1 value, ^1-1317); rūpabhavo / rūpāvacara /
    rūpūpapatti = «သိမ်မွေ့သော ရုပ်»; rūpataṇhā / rūpārammaṇa = «အဆင်းအရောင်»; matter «ရုပ်» elsewhere. This gives rūpaṃ
    = ရုပ်ပိုင်း also in ^2-225, where the pi-1 mapping of the same chain (^1-1343) has «ရုပ်» (a substring of the
    text's «ရုပ်ပိုင်း»): the keyword there is the nāma-rūpa member, as nāma = စိတ်ပိုင်း in the same pi-1 line.
    rūpaṃ nissāya («Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati» = «… မှီ၍ ဖြစ်ပေါ်ရာ ရုပ်») = «မှီ၍ … ရုပ်»;
    nāmarūpaṃ / nāmarūpa = စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း.
C4. **Compounds the text renders as a list** (rule 6, «၊» dropped): jarāmaraṇaṃ in ^2-225 («အိုခြင်း၊ သေခြင်း၊ …») =
    «အိုခြင်း သေခြင်း», elsewhere «အိုခြင်းနှင့် သေခြင်း» (the text's pair); domanassupāyāsā = «စိတ်ဆင်းရဲမှု ပြင်းစွာ
    ပူပန်ခြင်း».
C5. **The byasana frame** of soka / parideva / upāyāsa (^2-237, ^2-238, ^2-241): Ñāti / bhoga / roga = ဆွေမျိုး /
    စည်းစိမ် / ကျန်းမာရေး (the text renders rogabyasana as «loss of health»); byasanena = ပျက်စီးခြင်း; phuṭṭhassa =
    ထိခိုက်ခံရသူ, samannāgatassa = ကြုံတွေ့နေရသူ (rule 1: ၏ goes, the person noun «သူ» stays); «byasanena vā phuṭṭhassa»
    = «ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသူ၏ဖြစ်စေ» (vā = ဖြစ်စေ; the particles inside the phrase stay); in «dukkhadhammena»
    (text «ဆင်းရဲဖွယ်ရာဖြင့်») dukkha = ဆင်းရဲ and dhammena = ဖွယ်ရာ (f_dukkha; elsewhere dukkha = pi-1 ဒုက္ခ, and
    ခက်ခဲသော in dukkhapaṭipadaṃ).
C6. **Feeling phrases** (^2-239, ^2-240, ^2-249, ^2-283 …): «sātaṃ sukhaṃ (vedayitaṃ)» / «asātaṃ dukkhaṃ (vedayitaṃ)» /
    «sātā sukhā vedanā» = the text's «နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော (ခံစားရခြင်း / ခံစားမှု)» (the «၍» inside the phrase
    stays); nāsātaṃ (in «neva sātaṃ nāsātaṃ») = «နှစ်သက်ဖွယ် မကောင်းသည်လည်း မဟုတ်သော» (rule 5 negative attributive with
    the «neither … nor» လည်း of rule 6).
C7. **sasaṅkhārena** = «တိုက်တွန်းမှုဖြင့်»: sa- (with) is rendered by ဖြင့်, so the instrumental stays (as N7).
C8. **Fragments** (rule 8): ābhisaṅkhāro = ပြုပြင်ဖန်တီးမှု (head of the three abhisaṅkhāra); ūpapattiyā (maggaṃ) from
    rūpūpapattiyā = the pi-1 «ဖြစ်ပေါ်ရန် (လမ်း)»; ākusalā / ākusalaṃ (from nākusalā / nākusalaṃ) = အကုသိုလ်; anekaṃsa
    (from anekaṃsaggāho «တစ်ထစ်ချ မယူနိုင်ခြင်း») = «တစ်ထစ်ချ», gāho = the pi-1 «ယူနိုင်ခြင်း» (the an- is the infixed
    မ, rule 8); taca / vali (valittacatā «အရေတွန့်ခြင်း») = အရေ / တွန့်ခြင်း; nikāye (sattanikāye) = အမျိုးအစား;
    abhinibbati (spelling of abhinibbatti, ^2-273) = ထင်ရှားစွာ ပေါ်ထွက်ခြင်း.
C9. **Cittuppāda openings**: «manodhātu uppannā hoti» → dhātu uppannā = «ဓာတ် … ဖြစ်ပေါ်ပြီးသော» (sample uppanna, the
    subject + predicate gap of pi-1 5 rule 21; the text «… ဓာတ်သည် ဖြစ်ပေါ်ပြီးသော အချိန်၌»); vipākaṃ (adjectival,
    «vipākaṃ cakkhuviññāṇaṃ») = the pi-1 vipākā «ကံ၏ အကျိုး ဖြစ်သော»; X-ārammaṇaṃ / -ā = «Xကို အာရုံပြုသော» (pi-1
    dhammārammaṇaṃ; text «…ကို အာရုံပြု၍ဖြစ်စေ», attr rule); kāmāvacarassa kusalassa = ကာမဘုံနှင့် ဆိုင်သော ကုသိုလ်.
C10. **Other values**: sammā (sammādiṭṭhi) = the pi-1 «မှန်ကန်သော», not the preamble's «အပြည့်အဝ» (sammāsambuddha);
    Tena / tena (tena vuccati) = ထို့ကြောင့်; vattati = ဖြစ်ပေါ်သည် (rule 4; the text's form is «ဖြစ်ပေါ်ရာ», the chunk
    also occurs literally in the segment); pasādo = ကြည်ညိုမှု (confidence, see the differences table); indriyānaṃ in
    «indriyānaṃ paripāko» (^2-236, CTX) = «အာရုံခံ အင်္ဂါ» (pi-1 indriyesu), the pi-1 «စွမ်းရည်» stays for jīvitindriya.
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
    "cuti": "pi-1 «သေခြင်း» is cuti in cutūpapātañāṇa (^1-1380); in the maraṇa list (^2-236) «သေခြင်း» is maraṇaṃ "
            "and the text has «စုတေခြင်း» for cuti (pi-2 harmonise-notes: one form)",
    "dhātu uppannā": "pi-1 «ဓာတ် ဖြစ်ပေါ်လာသည်» (finite) is not in the pi-2 text; the cittuppāda opening is "
                     "«… ဓာတ်သည် ဖြစ်ပေါ်ပြီးသော အချိန်၌» (sample uppanna = ဖြစ်ပေါ်ပြီးသော; rule C9)",
    "dukkha": "«dukkhadhammena» = «ဆင်းရဲဖွယ်ရာဖြင့်» (rule C5); the pi-1 values occur elsewhere in ch6 (ဒုက္ခ, ခက်ခဲသော)",
    "Hetu": "pi-1 «အမြစ်» is the root (hetu dhammā); here the heading Hetucatukkaṃ «အကြောင်းပြုခြင်း လေးမျိုးတွဲ» (rule C2)",
    "hetukaṃ": "pi-1 «အမြစ်» is the root fragment of sahetuka; here X-hetukaṃ «Xကို အကြောင်းပြုသော» (rule C2)",
    "pasādo": "pi-1 «အာရုံခံ ကြည်လင်မှု» is the sensitivity of a sense organ (rūpa); here confidence in the kusala "
              "chain «vedanāpaccayā pasādo» (my2-zeroshot-terms: pasādo (confidence) = ကြည်ညိုမှု)",
    "rūpa": "the fragment of nāmarūpapaccayā (^2-229) is the nāma-rūpa member «ရုပ်ပိုင်း» (rule C3); the pi-1 values "
            "are used for the other senses",
    "taca": "pi-1 «အခေါက်» is bark (tacasāra); here the skin of valittacatā «အရေတွန့်ခြင်း»",
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
    with open(HERE / "map-table-6.md", "w", encoding="utf-8") as f:
        f.write("# pi-2 Burmese keyword mapping: NEW rules and values of chapter (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း»): "
                + ", ".join(CHAPTERS) + "\n\n")
        f.write("Written by map_6.py (a copy of the approved sample map_all.py). Burmese from the FINAL pi-2 text of this track only "
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
    if args and args[0] in ("--seg", "--segb"):
        show(args[1:], pali=args[0] == "--seg")
        sys.exit()
    if args and args[0] == "--kwin":
        # working aid: for each keyword (args, or every unmapped / failing one) its first segment, a Pāli window
        # around it and the Burmese window at the proportional position
        _, unmapped, problems, _ = run(write=False)
        W = 110
        want = args[1:] or list(unmapped) + sorted({p[2] for p in problems})
        firsts = {kw: w[0][1] for kw, w in unmapped.items()}
        for p in problems:
            firsts.setdefault(p[2], p[1])
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            for kw in want:
                sid = firsts.get(kw) or next((s for s, k in rows if kw in [x.strip() for x in k.split(", ")]), None)
                if not sid:
                    continue
                pali, mt = pa.get(sid, ""), my[sid]
                i = pali.find(kw.split()[0])
                if i < 0:
                    i = pali.lower().find(kw.split()[0].lower())
                j = int(len(mt) * max(i, 0) / max(len(pali), 1))
                print(f"== {kw} [{sid}]\n  PI: {pali[max(0, i - 60):i + 90]}\n  MY: {mt[max(0, j - W):j + W]}")
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
