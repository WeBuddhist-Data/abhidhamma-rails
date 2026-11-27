"""Pāli→Burmese keyword mapping for pi-2 (Vibhaṅga), chapter 18-dhammahadayavibhango only.

A copy of the approved sample script map_all.py (its tables, functions and verifier unchanged) plus the
chapter-18 table T_18, context functions f_dhatu / f_rupadhatu / f_rupa18 / f_satta and CTX; writes only
18-dhammahadayavibhango.mapped.md and map-table-18.md. The sample usage notes below still apply (map_18.py).

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


FUNCS = {"ajjhattam": f_ajjhattam, "rupa": f_rupa}
ALT = {}
CTX = {
}

# ---------------------------------------------------------------------------------------------------------
# chapter 18 (Dhammahadayavibhaṅga «သဘောတရားများ၏ နှလုံးသားကို ခွဲခြမ်းစိတ်ဖြာခြင်း»)
# ---------------------------------------------------------------------------------------------------------
UPK = "ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ၌"          # upapattikkhaṇe inside a phrase (its ၌ stays, rule 1)
T_18 = {
    # --- title and headings (the heading's own Burmese, pi-1 decision 4)
    "hadaya": "နှလုံးသား",                  # title «သဘောတရားများ၏ နှလုံးသားကို …» (pi-1 hadayaṃ = နှလုံးသား)
    "Dhamma": "သဘောတရား", "dhamma": "သဘောတရား",
    "vāro": "ဖော်ပြချက်",
    "Sabba": "အားလုံး", "sabba": "အားလုံး", "saṅgāhika": "စုစည်းသော",
    "ānuppatti": "ဖြစ်ပေါ်ခြင်း",             # fragment of anuppatti (rule 8: the positive part)
    "Uppattānuppattivāro": "ဖြစ်ပေါ်ခြင်း မဖြစ်ပေါ်ခြင်း ဖော်ပြချက်",
    "dassana": "ပြသသော", "dassanavāro": "ပြသသော ဖော်ပြချက်",
    "antara": "အသီးသီး", "Bhūmantaradassanavāro": "ဘုံ အသီးသီးကို ပြသသော ဖော်ပြချက်",
    "Uppādaka": "ဖြစ်ပေါ်စေသော", "Uppādakakamma": "ဖြစ်ပေါ်စေသော ကံ", "Uppādakakammaṃ": "ဖြစ်ပေါ်စေသော ကံ",
    "pamāṇa": "အတိုင်းအတာ", "pamāṇaṃ": "အတိုင်းအတာ",
    "āyuppamāṇa": "သက်တမ်း အတိုင်းအတာ", "āyuppamāṇaṃ": "သက်တမ်း အတိုင်းအတာ",
    "ādi": "စသည်",
    "Abhiññeyyādivāro": "ထူးကဲစွာ သိရမည့် သဘောတရား စသည်ကို ပြသသော ဖော်ပြချက်",
    "Sārammaṇānārammaṇavāro": "အာရုံ ရှိခြင်း မရှိခြင်း ဖော်ပြချက်",
    "ārammaṇa": "အာရုံ",
    "Diṭṭhasutādidassanavāro": "မြင်ရသော ကြားရသော စသည်တို့ကို ပြသသော ဖော်ပြချက်",
    "Tikādidassanavāro": "သုံးမျိုးတွဲ စသည်တို့ကို ပြသသော ဖော်ပြချက်",
    "Vipākattikaṃ": "ကံ၏ အကျိုး သုံးမျိုးတွဲ",
    "Upādinna": "ကံကြောင့် ဖြစ်သော", "upādinnā": "ကံကြောင့် ဖြစ်သော",   # pi-1 upādiṇṇa(ā)
    "Lokiya": "လောကနှင့် သက်ဆိုင်သော",
    "Asañña": "အသည", "sattā": "@satta",                    # loan အသညသတ် split as transliterated (pi-1 4 rule 19)
    # --- planes (dhātu = «ဘုံ» in Kāma- / Rūpa- / Arūpadhātu, «ဓာတ်» for the eighteen elements)
    "Kāmadhātu": "ကာမဘုံ", "kāmadhātu": "ကာမဘုံ", "Kāmadhātuyā": "ကာမဘုံ",
    "Rūpadhātu": "@rupadhatu", "rūpadhātu": "@rupadhatu",
    "Rūpadhātuyā": "သိမ်မွေ့သော ရုပ်ဘုံ", "rūpadhātuyā": "သိမ်မွေ့သော ရုပ်ဘုံ",
    "Arūpadhātu": "ရုပ်မရှိသော ဘုံ", "arūpadhātu": "ရုပ်မရှိသော ဘုံ",
    "Arūpadhātuyā": "ရုပ်မရှိသော ဘုံ", "arūpadhātuyā": "ရုပ်မရှိသော ဘုံ",
    "dhātuyā": "ဘုံ", "dhātu": "@dhatu", "Rūpa": "@rupa18", "rūpa": "@rupa18",
    "dhātuyo kāmadhātupariyāpannā": "ဓာတ် … ကာမဘုံ၌ အကျုံးဝင်သော",
    "dhātuyo pariyāpannā": "ဓာတ် … ဘဝဘုံတို့၌ အကျုံးဝင်သော",
    # --- the twelve lists (plurals and genitives = the noun, rule 1)
    "phassā": "တွေ့ထိမှု", "samphasso": "တွေ့ထိမှု", "indriyā": "စွမ်းရည်",
    "saccāni": "သစ္စာ", "saccā": "သစ္စာ", "saccānaṃ": "သစ္စာ", "cittānaṃ": "စိတ်", "dhammānaṃ": "သဘောတရား",
    "Samudaya": "ဖြစ်ပေါ်ခြင်း", "samudaya": "ဖြစ်ပေါ်ခြင်း",
    "Dukkha": "ဒုက္ခ", "dukkha": "ဒုက္ခ", "Dukkhasaccaṃ": "ဒုက္ခ သစ္စာ", "dukkhasaccaṃ": "ဒုက္ခ သစ္စာ",
    "sotaviññāṇadhātu": "နား သိစိတ် ဓာတ်", "ghānaviññāṇadhātu": "နှာခေါင်း သိစိတ် ဓာတ်",
    "jivhāviññāṇadhātu": "လျှာ သိစိတ် ဓာတ်",
    "manodhātusamphasso": "မနော ဓာတ်၏ တွေ့ထိမှု", "manodhātusamphassa": "မနော ဓာတ်၏ တွေ့ထိမှု",
    "manodhātusamphassajā": "မနော ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "Manoviññāṇadhātusamphassajā": "မနော သိစိတ် ဓာတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "aññātāvindriyaṃ": "အပြည့်အဝ သိမြင်ပြီးသူ၏ စွမ်းရည်",
    "rūpajīvitindriyaṃ": "ရုပ် အသက်၏ စွမ်းရည်",
    "kusalahetu": "ကုသိုလ် အမြစ်", "akusalahetu": "အကုသိုလ် အမြစ်",
    "kiriyābyākatesu": "ပြုရုံမျှသာ ဖြစ်သော ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "Kabaḷīkārāhāro": "လုတ်ပြု၍ စားရသော အာဟာရ", "phassāhāro": "တွေ့ထိမှု အာဟာရ",
    "manosañcetanāhāro": "မနော၏ စေ့ဆော်ခြင်း အာဟာရ", "viññāṇāhāro": "သိစိတ် အာဟာရ",
    # --- counts (pi-1 4 rule 18 / 5 rule 12: the text's count with «ပါး»; a keyword that contains a count keeps it)
    "aṭṭhārasa": "ဆယ့်ရှစ်ပါး", "aṭṭhārasa dhātuyo": "ဓာတ် ဆယ့်ရှစ်ပါး",
    "Aṭṭhārasannaṃ": "ဆယ့်ရှစ်ပါး", "Aṭṭhārasannaṃ dhātūnaṃ": "ဓာတ် ဆယ့်ရှစ်ပါး",
    "Dvādasannaṃ": "ဆယ့်နှစ်ပါး", "Dvādasannaṃ āyatanānaṃ": "အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး",
    "dvādasāyatanāni": "အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး", "ekādasāyatanāni": "အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး",
    "dasāyatanāni": "အာရုံခံ နယ်ပယ် ဆယ်ပါး", "Dasāyatanā": "အာရုံခံ နယ်ပယ် ဆယ်ပါး",
    "bāvīsatindriyāni": "စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး", "Bāvīsatindriyā": "စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး",
    "cuddasindriyāni": "စွမ်းရည် ဆယ့်လေးပါး", "Cuddasindriyā": "စွမ်းရည် ဆယ့်လေးပါး",
    "terasindriyāni": "စွမ်းရည် ဆယ့်သုံးပါး", "Terasindriyā": "စွမ်းရည် ဆယ့်သုံးပါး",
    "dvādasindriyāni": "စွမ်းရည် ဆယ့်နှစ်ပါး", "Dvādasindriyā": "စွမ်းရည် ဆယ့်နှစ်ပါး",
    "ekādasindriyāni": "စွမ်းရည် ဆယ့်တစ်ပါး", "Ekādasindriyā": "စွမ်းရည် ဆယ့်တစ်ပါး",
    "dasindriyāni": "စွမ်းရည် ဆယ်ပါး", "Dasindriyā": "စွမ်းရည် ဆယ်ပါး",
    "Soḷasa": "ဆယ့်ခြောက်ပါး", "Soḷasa dhātuyo": "ဓာတ် ဆယ့်ခြောက်ပါး",
    "Pannarasa": "ဆယ့်ငါးပါး", "Pannarasa dhātuyo": "ဓာတ် ဆယ့်ငါးပါး", "Terasa": "ဆယ့်သုံးပါး",
    "ekādasa dhātuyo": "ဓာတ် ဆယ့်တစ်ပါး", "dasa dhātuyo": "ဓာတ် ဆယ်ပါး", "Dasa dhātuyo": "ဓာတ် ဆယ်ပါး",
    # --- rebirth moment (Uppattānuppattivāra)
    "pātubhavanti": "ထင်ရှားလာသည်", "pātubhavati": "ထင်ရှားလာသည်",   # rule 4; plural ကြ dropped
    "khaṇe": "ခဏ", "upapattikkhaṇe": "ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ",
    "upapatti": "@alt",
    "upapattikkhaṇe ekādasāyatanāni": UPK + " အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး",
    "upapattikkhaṇe dasāyatanāni": UPK + " အာရုံခံ နယ်ပယ် ဆယ်ပါး",
    "upapattikkhaṇe ekādasa": UPK + " … ဆယ့်တစ်ပါး", "upapattikkhaṇe ekādasa dhātuyo": UPK + " ဓာတ် ဆယ့်တစ်ပါး",
    "upapattikkhaṇe dasa": UPK + " … ဆယ်ပါး", "upapattikkhaṇe dasa dhātuyo": UPK + " ဓာတ် ဆယ်ပါး",
    "upapattikkhaṇe dasindriyāni": UPK + " စွမ်းရည် ဆယ်ပါး",
    "upapattikkhaṇe terasindriyāni": UPK + " စွမ်းရည် ဆယ့်သုံးပါး",
    "devānaṃ": "နတ်", "devā": "နတ်", "Kāmāvacarānaṃ": "ကာမဘုံနှင့် ဆိုင်သော", "āvacarānaṃ": "ဘုံနှင့် ဆိုင်သော",
    "kappikānaṃ": "ကမ္ဘာဦး",                # fragment of paṭhamakappika: the text's one word (pi-1 4 rule 19)
    "manussānaṃ": "လူ", "Manussānaṃ": "လူ",
    "opapātikānaṃ": "အလိုအလျောက် ပေါ်လာသော",
    "petānaṃ": "ပြိတ္တာ", "asurānaṃ": "အသုရာ", "tiracchānagatānaṃ": "တိရစ္ဆာန်", "nerayikānaṃ": "ငရဲသား",
    "opapātikānaṃ petānaṃ": "အလိုအလျောက် ပေါ်လာသော ပြိတ္တာ",
    "opapātikānaṃ asurānaṃ": "အလိုအလျောက် ပေါ်လာသော အသုရာ",
    "opapātikānaṃ tiracchānagatānaṃ": "အလိုအလျောက် ပေါ်လာသော တိရစ္ဆာန်",
    "paripuṇṇāyatanānaṃ": "အာရုံခံ နယ်ပယ် ပြည့်စုံသူ",   # person nouns «…သူ» (pi-1 3 rule 18)
    "jaccandhānaṃ": "မွေးရာပါ မျက်စိ ကန်းသူ", "badhirānaṃ": "နား ပင်းသူ",
    "napuṃsakānaṃ": "လိင် မရှိသူ",
    "Gabbhaseyyakānaṃ": "အမိဝမ်းတွင်း၌ ဖြစ်သော", "gabbhaseyyakānaṃ": "အမိဝမ်းတွင်း၌ ဖြစ်သော",
    "sahetukānaṃ": "အမြစ် ရှိသော", "sampayuttānaṃ": "ယှဉ်တွဲသော", "vippayuttānaṃ": "ကင်းကွာသော",
    "ñāṇavippayuttānaṃ": "ဉာဏ်နှင့် ကင်းကွာသော",
    "Avasesānaṃ": "ကြွင်းသော",
    "asaññasattānaṃ": "အသညသတ်", "Asaññasattānaṃ": "အသညသတ်",
    "asaññasattānaṃ devānaṃ": "အသညသတ် နတ်", "Asaññasattānaṃ devānaṃ": "အသညသတ် နတ်",
    "aphassakā": "တွေ့ထိမှု မရှိသော", "avedanakā": "ခံစားမှု မရှိသော", "asaññakā": "မှတ်သိမှု မရှိသော",
    "acetanakā": "စေ့ဆော်မှု မရှိသော", "acittakā": "စိတ် မရှိသော", "anāhārā": "အာဟာရ မရှိသော",
    # --- the planes (Pariyāpanna / Dhammadassanavāra)
    "akaniṭṭhe deve": "အကနိဋ္ဌ နတ်",
    "paranimmitavasavattī": "ပရနိမ္မိတဝသဝတ္တီ", "paranimmitavasavattī deve": "ပရနိမ္မိတဝသဝတ္တီ နတ်",
    "deve antokaritvā": "နတ်တို့ကို အတွင်း ထည့်သွင်း၍",   # absolutive keeps ၍; the inner particles stay
    "uparito": "အထက်၌",                     # place adverb keeps its locative (as bahiddhā, pi-1 rule 11)
    "antare": "အကြား", "nirayaṃ": "ငရဲ",
    "āyatanūpage": "နယ်ပယ် ဘုံသို့ ရောက်သော",
    "ākāsānañcāyatanūpage": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ဘုံသို့ ရောက်သော",
    "nevasaññānāsaññāyatanūpage":
        "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ဘုံသို့ ရောက်သော",
    "sukhavihārissa": "သာယာစွာ နေထိုင်သော",
    "kusalākusalabyākatā": "ကုသိုလ် အကုသိုလ် … ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",   # N5
    # --- the kinds of deities (Uppādakakammaāyuppamāṇavāra); names = the loan, or its part (pi-1 4 rule 19)
    "sammuti": "သမုတ်ခြင်း", "visuddhi": "စင်ကြယ်ခြင်း",
    "rājāno": "ဘုရင်", "deviyo": "မိဖုရား", "kumārā": "မင်းသား", "arahanto": "ရဟန္တာ",
    "mahārājike": "မဟာရာဇ်", "mahārājikānaṃ": "မဟာရာဇ်", "tadupari": "ထိုအထက်",
    "Dānaṃ": "အလှူ", "sīlaṃ": "သီလ", "samādiyitvā": "ဆောက်တည်၍", "uposatha": "ဥပုသ်",
    "katvā": "စောင့်ထိန်း၍",                 # uposathakammaṃ katvā = «ဥပုသ်ကို စောင့်ထိန်း၍»
    "upapajjanti": "ပြန်လည် ဖြစ်ပေါ်သည်",
    "khattiya": "မင်းမျိုး", "brāhmaṇa": "ပုဏ္ဏားမျိုး", "gahapati": "သူကြွယ်မျိုး", "mahāsālānaṃ": "ကြွယ်ဝသော",
    "tāvatiṃsānaṃ": "တာဝတိံသာ", "yāmānaṃ devānaṃ": "ယာမာ နတ်",
    "tusitānaṃ": "တုသိတာ", "tusitānaṃ devānaṃ": "တုသိတာ နတ်",
    "nimmāna": "နိမ္မာန", "ratīnaṃ": "ရတီ", "nimmānaratīnaṃ devānaṃ": "နိမ္မာနရတီ နတ်",
    "vasavattīnaṃ": "ဝသဝတ္တီ", "paranimmitavasavattīnaṃ": "ပရနိမ္မိတဝသဝတ္တီ",
    "paranimmitavasavattīnaṃ devānaṃ": "ပရနိမ္မိတဝသဝတ္တီ နတ်",
    "sataṃ": "တစ်ရာ",
    # life-spans of the sense-sphere deities (^2-1023): the fused Burmese numeral goes to each Pāli part
    # that has no word of its own (pi-1 4 rule 19); first occurrence decides (one sense per segment)
    "mānusakāni": "လူ့", "mānusakaṃ vassasataṃ": "လူ့ နှစ် တစ်ရာ", "vassāni": "နှစ်",
    "paññāsa": "ငါးဆယ်", "rattindivo": "တစ်ရက်", "rattiyo": "ည", "tiṃsa": "သုံးဆယ်",
    "māso": "တစ်လ", "rattiyo māso": "ည … တစ်လ", "saṃvaccharo": "တစ်နှစ်",
    "dvādasamāsiyo saṃvaccharo": "ဆယ့်နှစ်လ … တစ်နှစ်",
    "dibbāni": "နတ်", "vassasatāni": "နှစ် ငါးရာ", "satāni": "ငါးရာ", "sahassaṃ": "တစ်ထောင်",
    "Manussānaṃ gaṇanāya": "လူတို့၏ ရေတွက်ပုံ", "gaṇanāya": "ရေတွက်ပုံ",
    "koṭiyo": "ကုဋေ", "soḷasa": "တစ်ထောင့်ခြောက်ရာ", "dvādasa": "ဆယ့်နှစ်", "aṭṭhavīsañca": "နှစ်ဆယ့်ရှစ်",
    "samiddhino": "ပြည့်စုံသော", "saṅkhāto": "ရေတွက်လျှင်", "pakāsitāti": "ဖော်ပြထားသော",
    # life-spans of the Brahmās (^2-1024 … ^2-1028)
    "bhāvetvā": "ပွားများ၍", "Kappassa": "ကမ္ဘာ", "kappā": "ကမ္ဘာ",
    "pārisajjānaṃ": "ပါရိသဇ္ဇ", "purohitānaṃ": "ပုရောဟိတ",
    "mahābrahmānaṃ": "မဟာဗြဟ္မာ", "mahābrahmānaṃ devānaṃ": "မဟာဗြဟ္မာ နတ်", "brahmānaṃ devānaṃ": "ဗြဟ္မာ နတ်",
    "ābhānaṃ": "ပရိတ္တာဘ",                   # the ā of -ābha fuses into the loan (ပရိတ္တာဘ): the whole loan
    "appamāṇābhānaṃ": "အပ္ပမာဏာဘ", "ābhassarānaṃ": "အာဘဿရ",
    "subhānaṃ": "သုဘ", "appamāṇa": "အပ္ပမာဏ", "kiṇhānaṃ": "ကိဏှ",
    "Bāttiṃsa": "သုံးဆယ့်နှစ်", "Catusaṭṭhi": "ခြောက်ဆယ့်လေး",
    "nānattatā": "ကွဲပြားခြင်း", "abhinīhāra": "ဦးတည် ပို့ဆောင်ခြင်း",
    "vehapphalānaṃ": "ဝေဟပ္ဖိုလ်", "vehapphalānaṃ devānaṃ": "ဝေဟပ္ဖိုလ် နတ်",
    "avihānaṃ": "အဝိဟာ", "avihānaṃ devānaṃ": "အဝိဟာ နတ်", "atappānaṃ": "အတပ္ပါ", "atappānaṃ devānaṃ": "အတပ္ပါ နတ်",
    "sudassānaṃ": "သုဒဿာ", "sudassānaṃ devānaṃ": "သုဒဿာ နတ်", "sudassīnaṃ devānaṃ": "သုဒဿီ နတ်",
    "akaniṭṭhānaṃ devānaṃ": "အကနိဋ္ဌ နတ်",
    "āyatanūpagānaṃ": "နယ်ပယ် ဘုံသို့ ရောက်သော",
    "ākāsānañcāyatanūpagānaṃ": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ် ဘုံသို့ ရောက်သော",
    "viññāṇañcāyatanūpagānaṃ": "အဆုံး မရှိသော သိစိတ် နယ်ပယ် ဘုံသို့ ရောက်သော",
    "ākiñcaññāyatanūpagānaṃ": "ဘာမျှ မရှိသော နယ်ပယ် ဘုံသို့ ရောက်သော",
    "nevasaññānāsaññāyatanūpagānaṃ":
        "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ် ဘုံသို့ ရောက်သော",
    "Kappasahassaṃ": "ကမ္ဘာ တစ်ထောင်",
    # --- the verse ^2-1029
    "Ukkhittā": "မြှောက်တင်ခံရသော", "puñña": "ကောင်းမှု", "tejena": "တန်ခိုး",
    "gatiṃ": "လားရာ", "gatā": "ရောက်သော", "Bhavaggatampi": "ဘဝ၏ ထိပ်ဆုံး",
    "punāgacchanti": "တဖန် ပြန်လာသည်", "duggatiṃ": "ဆိုးသော လားရာ",
    "dīghāyukā": "သက်တမ်း ရှည်သော", "cavanti": "စုတေသည်",
    "āyusaṅkhayā": "သက်တမ်း ကုန်ဆုံး", "saṅkhayā": "ကုန်ဆုံး",   # causal «…သဖြင့်» dropped (as «…ကြောင့်»)
    "koci": "တစ်စုံတစ်ရာ", "nicco": "မြဲသော", "mahesinā": "မြတ်စွာဘုရား",
    "Tasmā": "ထို့ကြောင့်", "dhīrā": "ပညာရှိသော", "nipakā": "ရင့်ကျက်သော", "nipuṇā": "လိမ္မာသော",
    "cintakā": "စဉ်းစားတတ်သူ",                # agent noun keeps «…သူ» (pi-1 4 rule 20)
    "Jarāmaraṇa": "အိုခြင်း သေခြင်း", "mokkhāya": "လွတ်မြောက်ရန်",   # purpose dative keeps ရန် (pi-1 4 rule 15)
    "bhāventi": "ပွားများသည်", "uttamaṃ": "အမြတ်ဆုံး",
    "Bhāvayitvā": "ပွားများ၍", "suciṃ": "စင်ကြယ်သော",
    "nibbānogadhagāminaṃ": "နိဗ္ဗာန်ထဲသို့ သက်ဝင် ရောက်ရှိစေသော",
    "āsave": "စိတ်အစွန်းအထင်း", "pariññāya": "ပိုင်းခြား သိ၍",
    "parinibbanti": "ပရိနိဗ္ဗာန် ပြုသည်", "anāsavāti": "စိတ်အစွန်းအထင်း မရှိသော",
    # --- Abhiññeyyādivāra … Tikādidassanavāra (gerundives «…ရမည့်», pi-1 pahātabbā)
    "abhiññeyyā": "ထူးကဲစွာ သိရမည့်", "abhiññeyyo": "ထူးကဲစွာ သိရမည့်", "Abhiññā": "ထူးကဲစွာ သိရမည့်",
    "pariññeyyā": "ပိုင်းခြား သိရမည့်", "pariññeyyo": "ပိုင်းခြား သိရမည့်",
    "bhāvetabbā": "ပွားများရမည့်", "bhāvetabbo": "ပွားများရမည့်",
    "sacchikātabbā": "မျက်မှောက်ပြုရမည့်", "sacchikātabbo": "မျက်မှောက်ပြုရမည့်",
    "sārammaṇārammaṇā": "အာရုံ ရှိသည်ကို အာရုံပြုသော", "anārammaṇārammaṇā": "အာရုံ မရှိသည်ကို အာရုံပြုသော",
    "sutā": "ကြားရသော", "suto": "ကြားရသော", "mutā": "နမ်း မြည်း ထိတွေ့ရသော", "muto": "နမ်း မြည်း ထိတွေ့ရသော",
    "viññātā": "သိရသော", "viññāto": "သိရသော",
    "nevavipākanavipākadhammadhammā":
        "ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား",
    "nevavipākanavipākadhammadhammo":           # the text renders the final -dhammo here (unlike N6)
        "ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား",
    "lokuttarā": "လောကကို ကျော်လွန်သော",
    "pakaraṇaṃ": "ကျမ်း", "Vibhaṅgapakaraṇaṃ": "ခွဲခြမ်းစိတ်ဖြာခြင်း ကျမ်း",
}
ALT["upapatti"] = ["ပြန်လည် ဖြစ်ပေါ်ခြင်း", "ပြန်လည် ဖြစ်ပေါ်သော"]   # noun where the text has one, else «…သည့်»


def _first(pat, pali):
    m = re.search(pat, pali)
    return m.group(0) if m else None


def _rupadhatu_plane(tok, pali):
    """rūpadhātu is the fine-material PLANE in the locative (-dhātuyā), in -dhātupariyāpanna and as a heading
    alone; it is the visible-object ELEMENT in the lists of the eighteen dhātus."""
    t = tok.lower()
    return t.startswith(("rūpadhātuy", "rūpadhātupariyāpann")) or pali.lstrip().startswith("#")


def f_dhatu(kw, pali, my):
    """dhātu, one sense per segment: the sense of the FIRST dhātu word of the Pāli segment: the plane «ဘုံ» in
    kāma- / arūpa- / (plane) rūpadhātu, the element «ဓာတ်» elsewhere (cakkhudhātu …, asaṅkhatā dhātu)."""
    # the keyword dhātu is the bare stem: the inflected dhātuyā / dhātuyo / dhātūnaṃ are other keywords
    tok = _first(r"[\wāīūṃṅñṭḍṇḷ]*dhātu(?![yū])[\wāīūṃṅñṭḍṇḷ]*", pali) or ""
    t = tok.lower()
    if t.startswith(("kāmadhātu", "arūpadhātu")) or (t.startswith("rūpadhātu") and _rupadhatu_plane(tok, pali)):
        return "ဘုံ"
    return "ဓာတ်"


def f_rupadhatu(kw, pali, my):
    tok = _first(r"(?<![\wāīūṃ])" + kw[0] + r"ūpadhātu(?!y)\w*", pali) or kw   # not the locative -dhātuyā
    return "သိမ်မွေ့သော ရုပ်ဘုံ" if _rupadhatu_plane(tok, pali) else "အဆင်းအရောင် ဓာတ်"


def f_rupa18(kw, pali, my):
    """rūpa, one sense per segment, read from the words of the keyword's own case (pi-1 3 rule 13): the FIRST
    rūpa compound decides: rūpāvacara and the plane rūpadhātu = «သိမ်မွေ့သော ရုပ်»; rūpāyatana / the element
    rūpadhātu = «အဆင်းအရောင်»; matter «ရုပ်» elsewhere (rūpakkhandho …)."""
    tok = _first(r"(?<![\wāīūṃ])" + kw[0] + r"ūp[aā]\w*", pali)
    if tok is None:
        return "ရုပ်"
    t = tok.lower()
    if t.startswith("rūpāvacar") or (t.startswith("rūpadhātu") and _rupadhatu_plane(tok, pali)):
        return "သိမ်မွေ့သော ရုပ်"
    if t.startswith(("rūpāyatana", "rūpadhātu", "rūpārammaṇ")):
        return "အဆင်းအရောင်"
    return "ရုပ်"


def f_satta(kw, pali, my):
    """sattā: «သတ္တဝါ» (pi-1) where the text has it; in the heading Asaññasattā the loan «အသညသတ်» (its part)."""
    return "သတ္တဝါ" if "သတ္တဝါ" in my else "သတ်"


FUNCS.update({"dhatu": f_dhatu, "rupadhatu": f_rupadhatu, "rupa18": f_rupa18, "satta": f_satta})

CTX.update({
    "2-1029": {"rūpa": "သိမ်မွေ့သော ရုပ်"},           # kāmarūpagatiṃ: the fine-material plane (text «… ရုပ်ဘုံ»)
    "2-1043": {"rūpā": "ရုပ်"},                       # «kati rūpā» = «ရုပ် ဖြစ်သော»: noun predicated (rule 2)
    "2-1022": {"Manussānaṃ": "လူ"},
    "2-1026": {"Soḷasa": "ဆယ့်ခြောက်"},              # «ဆယ့်ခြောက်ကမ္ဘာ»: kappa is the classifier
    "2-1027": {"Soḷasa": "တစ်သောင်းခြောက်ထောင်", "satāni": "ငါးရာ", "kappasahassāni": "ကမ္ဘာ နှစ်ထောင်"},
    "2-1028": {"kappasahassāni": "ကမ္ဘာ နှစ်သောင်း", "sahassāni": "နှစ်သောင်း", "Vīsati": "နှစ်သောင်း",
               "Cattārīsa": "လေးသောင်း", "Saṭṭhi": "ခြောက်သောင်း", "Caturāsīti": "ရှစ်သောင်းလေးထောင်"},
})

SECTIONS = {
    "preamble": T_PREAMBLE,
    "1-khandhavibhango": T_KHANDHA,
    "18-dhammahadayavibhango": T_18,
}
CHAPTERS = ["18-dhammahadayavibhango"]


# =====================================================================================================
# rules (written to map-table.md)
# =====================================================================================================
RULES = """## Rules

**Binding and unchanged:** the approved pi-2 sample (`map-table.md`: pi-1 rules 1–11 and N1–N11, the sample's
tables, compose rules, context functions and verifier, copied into map_18.py) and the agreed later pi-1 rules
(absolutives keep «…၍»; one sense per segment, the FIRST occurrence in the Pāli segment decides; no « / »
alternatives; numerals keep the text's count with «ပါး»; loans: a fragment of a transliterated name is its part of
the loan, pi-1 4 rule 19). Lookup: CTX -> this chapter's table T_18 -> the sample's tables -> the most frequent
final pi-1 value present in the segment -> compose. The sample's values are not changed.

Rules this chapter uses that pi-1 / the sample already had, applied to the Dhammahadaya's shapes:

- **The twelve lists** (pi-1 rule 1, 4 rule 18): plurals and genitives are the noun (phassā / samphasso =
  တွေ့ထိမှု, indriyā = စွမ်းရည်, saccāni / saccā / saccānaṃ = သစ္စာ, cittānaṃ = စိတ်); counted compounds keep the
  count with «ပါး» (dvādasāyatanāni = အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး, Soḷasa dhātuyo = ဓာတ် ဆယ့်ခြောက်ပါး,
  bāvīsatindriyāni = စွမ်းရည် နှစ်ဆယ့်နှစ်ပါး; bare Soḷasa / Pannarasa / Terasa = ဆယ့်ခြောက်ပါး …).
- **Headings** (pi-1 decision 4): the heading's own Burmese; a -vāro title compound = the heading whole
  (Uppattānuppattivāro, Bhūmantaradassanavāro, Abhiññeyyādivāro …); vāro = ဖော်ပြချက် (pi-1); dassana = ပြသသော,
  ādi = စသည်, Vipākattikaṃ = ကံ၏ အကျိုး သုံးမျိုးတွဲ.
- **Subject + predicate pairs** (pi-1 5 rule 21): dhātuyo kāmadhātupariyāpannā = ဓာတ် … ကာမဘုံ၌ အကျုံးဝင်သော
  (the count between is the gap).
- **Gerundives** «…ရမည့်» (pi-1 pahātabbā): abhiññeyyā = ထူးကဲစွာ သိရမည့်, pariññeyyā = ပိုင်းခြား သိရမည့်,
  bhāvetabbā = ပွားများရမည့်, sacchikātabbā = မျက်မှောက်ပြုရမည့်; the verse's abbreviation Abhiññā the same.
- **Verbs** (rule 4, plural ကြ dropped): pātubhavanti / pātubhavati = ထင်ရှားလာသည်, upapajjanti = ပြန်လည်
  ဖြစ်ပေါ်သည်, cavanti = စုတေသည်; absolutives keep «၍»: bhāvetvā = ပွားများ၍, samādiyitvā = ဆောက်တည်၍,
  katvā (uposathakammaṃ katvā «ဥပုသ်ကို စောင့်ထိန်း၍») = စောင့်ထိန်း၍, deve antokaritvā = နတ်တို့ကို အတွင်း
  ထည့်သွင်း၍ (inner particles stay, rule 1); purpose dative keeps ရန် (mokkhāya = လွတ်မြောက်ရန်).
- **Person nouns** «…သူ» (pi-1 3 rule 18 / 4 rule 20): paripuṇṇāyatanānaṃ = အာရုံခံ နယ်ပယ် ပြည့်စုံသူ,
  jaccandhānaṃ = မွေးရာပါ မျက်စိ ကန်းသူ, badhirānaṃ = နား ပင်းသူ, napuṃsakānaṃ = လိင် မရှိသူ, cintakā =
  စဉ်းစားတတ်သူ; adjectives the text builds as «…သူ» are «…သော» (sahetukānaṃ = အမြစ် ရှိသော, ñāṇavippayuttānaṃ =
  ဉာဏ်နှင့် ကင်းကွာသော, anāsavāti = စိတ်အစွန်းအထင်း မရှိသော).
- **Coordinated compound with the head between** (N5): kusalākusalabyākatā = ကုသိုလ် အကုသိုလ် … ကုသိုလ်လည်း
  မဟုတ် အကုသိုလ်လည်း မဟုတ်သော (text «… သဘောတရားနှင့် …»).
- **-dhamma forms** (N6): nevavipākanavipākadhammadhammo keeps «သဘောတရား» because the text renders it here
  («… မဟုတ်သော သဘောတရား ဖြစ်သည်»), the same value as the plural -dhammā.
- **Deity and plane names** (pi-1 4 rule 19): the loan or its part: paranimmitavasavattī = ပရနိမ္မိတဝသဝတ္တီ,
  vasavattīnaṃ = ဝသဝတ္တီ, nimmāna = နိမ္မာန, ratīnaṃ = ရတီ, mahārājike = မဟာရာဇ် (စာတုမဟာရာဇ်), subhānaṃ = သုဘ,
  kiṇhānaṃ = ကိဏှ, appamāṇa = အပ္ပမာဏ (in appamāṇasubha), Asañña = အသည and sattā = သတ် (heading «အသညသတ်များ»;
  sattā elsewhere = pi-1 သတ္တဝါ); the bigram «X devānaṃ» = the name + « နတ်». kappikānaṃ (paṭhamakappika) =
  ကမ္ဘာဦး, the text's one word for the compound.

## NEW rules (for the user's review)

C1. **dhātu by sense, one sense per segment**: the plane «ဘုံ» in Kāmadhātu / Rūpadhātu / Arūpadhātu (text
    «ကာမဘုံ», «သိမ်မွေ့သော ရုပ်ဘုံ», «ရုပ်မရှိသော ဘုံ»), the element «ဓာတ်» for the eighteen dhātus. The bare
    keyword dhātu takes the sense of its FIRST bare-stem occurrence in the Pāli segment (kāmadhātupariyāpanna …
    = ဘုံ in ^2-999 … ^2-1004 and the headings; cakkhudhātu / asaṅkhatā dhātu = ဓာတ် elsewhere); the locative
    dhātuyā (only in Kāma- / Rūpa- / Arūpadhātuyā) = ဘုံ. rūpadhātu = the plane «သိမ်မွေ့သော ရုပ်ဘုံ» in the
    locative, in -pariyāpanna and as a heading, the visible-object element «အဆင်းအရောင် ဓာတ်» (pi-1) in the lists;
    rūpa / Rūpa follow the first rūpa compound of their own case (sample f_rupa extended: the plane rūpadhātu =
    «သိမ်မွေ့သော ရုပ်»); in the verse kāmarūpagatiṃ (^2-1029) rūpa = «သိမ်မွေ့သော ရုပ်» (CTX).
C2. **upapatti** (rebirth) = «ပြန်လည် ဖြစ်ပေါ်ခြင်း» where the text has the noun (^2-1021 upapattidevā
    «ပြန်လည် ဖြစ်ပေါ်ခြင်းအားဖြင့် နတ်»), else «ပြန်လည် ဖြစ်ပေါ်သော» (the text's «ပြန်လည် ဖြစ်ပေါ်သည့် ခဏ»,
    N11's «…သည့်» ending; two forms of ONE sense, the ALT mechanism of the sample). upapattikkhaṇe = «ပြန်လည်
    ဖြစ်ပေါ်သည့် ခဏ» (rule 1: its locative goes); inside «upapattikkhaṇe X» the ၌ stays («… ခဏ၌ အာရုံခံ နယ်ပယ်
    ဆယ့်တစ်ပါး»; with only the count: «… ခဏ၌ … ဆယ့်တစ်ပါး», the noun ဓာတ် in the gap).
C3. **Fused Burmese numerals** (^2-1023, ^2-1027, ^2-1028): Burmese writes count × hundred / thousand / ten
    thousand as one word, so the fused numeral goes to each Pāli part that has no word of its own (pi-1 4 rule
    19), first occurrence deciding: vassasatāni (dibbāni pañca vassasatāni) = နှစ် ငါးရာ, satāni = ငါးရာ,
    sahassaṃ = တစ်ထောင်, soḷasa (soḷasa vassasatāni) = တစ်ထောင့်ခြောက်ရာ; ^2-1028 Vīsati and sahassāni =
    နှစ်သောင်း, Cattārīsa = လေးသောင်း, Saṭṭhi = ခြောက်သောင်း, Caturāsīti = ရှစ်သောင်းလေးထောင်; with kappa as the
    classifier the bare number (Soḷasa kappā = ဆယ့်ခြောက်, Bāttiṃsa = သုံးဆယ့်နှစ်). Time units keep the text's
    «တစ်» (māso = တစ်လ, saṃvaccharo = တစ်နှစ်, rattindivo = တစ်ရက်: «a month / a year / a day»).
C4. **Causal «…သဖြင့်»** (Pāli ablative āyusaṅkhayā «သက်တမ်း ကုန်ဆုံးသဖြင့်») is dropped like pi-1's «…ကြောင့်»
    (pi-1 2-02 rule 15): āyusaṅkhayā = သက်တမ်း ကုန်ဆုံး, saṅkhayā = ကုန်ဆုံး. The participle saṅkhāto
    (ekasaṅkhāto) keeps the text's conditional «ရေတွက်လျှင်» (the text builds no attributive for it).
C5. **Place adverb** uparito = «အထက်၌» (the locative is its meaning, as bahiddhā in pi-1 rule 11 and N10); the
    noun antare (etasmiṃ antare) = «အကြား» (rule 1).
C6. **Presence check, one more ending**: «Xသော» is accepted against the plural predicate «Xကြသည်»
    (samiddhino «ပြည့်စုံကြသည်»), as the sample accepts «Xသည်» and «Xကြသော».
C7. **hadaya** (title Dhammahadaya) = «နှလုံးသား», the title's word (pi-1 hadayaṃ = နှလုံးသား, 26 uses); pi-1's
    one «နှလုံး» is hadayaṅgamā «နှလုံးသို့».
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
    SRC[(sid, kw)] = src
    return v


# ---- presence check (the pi-1 checks: sample rules 3, 4, 8; 4-01 rule 12, 16; 5 rule 22) -----------------
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော", "၊", "သည့်", "ကြသည်")   # ch18 N-rule: the plural predicate «…ကြသည်» (samiddhino)
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
    "ajjhattaṃ": "pi-1 «မိမိ၌» is the jhāna adverb (ajjhattaṃ sampasādanaṃ); here the attributive qualifier of the "
                 "question / the ajjhatta list item (pi-1 ^1-1050 wording), one sense per segment",
    "vuccati rūpaṃ": "pi-1 «ရုပ်ပိုင်း» is the nāma-rūpa pair (^1-1317); here matter",
    "uppanno": "pi-1 «ဖြစ်ပေါ်သော» is «uppanno ca vicāro» (cittuppāda); here the Mātikā triad uppanna «ဖြစ်ပေါ်ပြီးသော» "
               "(pi-1 uppannā)",
    "hīno": "pi-1 «ယုတ်ညံ့သူ» is a person; here the quality of a feeling (Mātikā hīnā «ယုတ်ညံ့သော»)",
    "paccayā": "pi-1 «ကြောင့်» is the dependent-origination chain; here «X-samphassapaccayā» = «Xကို အကြောင်းပြု၍ ဖြစ်သော»",
    "bahiddhā": "pi-1 «သူတစ်ပါး၌ / ပြင်ပ၌ / အပြင်ဘက်» do not occur as the term: the pi-2 text's qualifier is «မိမိ၏ ပြင်ပ၌»",
    # chapter 18
    "hadaya": "pi-1 «နှလုံး» is hadayaṅgamā («နှလုံးသို့»); the title's word is «နှလုံးသား» (= pi-1 hadayaṃ, C7)",
    "dhātu": "the planes Kāma- / Rūpa- / Arūpadhātu: the text's «ဘုံ» (C1); the element keeps pi-1 «ဓာတ်»",
    "Rūpadhātu": "the fine-material plane (heading; text «သိမ်မွေ့သော ရုပ်ဘုံ», C1); the element keeps pi-1",
    "rūpadhātu": "the fine-material plane in rūpadhātupariyāpanna (text «သိမ်မွေ့သော ရုပ်ဘုံ၌», C1); the element "
                 "keeps pi-1",
    "samphasso": "pi-1 «ထိတွေ့ရ» is sukhasamphasso (the tangible, Rūpakaṇḍa); here contact «တွေ့ထိမှု» (the list noun)",
    "kusalahetu": "pi-1 «ကုသိုလ်၏ အမြစ်» does not occur: the text's «ကုသိုလ် အမြစ်» (as pi-1 kusalahetū)",
    "Abhiññā": "pi-1 «ထူးကဲစွာ သိ၍» is the absolutive abhiññāya; here the summary verse's abhiññeyyā «ထူးကဲစွာ သိရမည့်»",
    "antara": "pi-1 «ကြားညှပ်» is antarā (between); bhūmantara = the various planes «ဘုံ အသီးသီး»",
    "appamāṇa": "part of the deity name appamāṇasubha «အပ္ပမာဏသုဘ» (loan, pi-1 4 rule 19), not the quality",
    "gatā": "pi-1 «ရောက်ရှိသော» does not occur: the verse's «ရောက်ကြသည်»",
    "sattā": "heading Asaññasattā «အသညသတ်များ»: the part of the loan (pi-1 4 rule 19); pi-1 «သတ္တဝါ» in ^2-1029",
    "sutā": "pi-1 «အကြားအမြင်» is learning (sutaṃ); here «heard» (diṭṭha suta muta viññāta) «ကြားရသော»",
    "Vīsati": "pi-1 «နှစ်ဆယ်» is twenty; here «Vīsati kappasahassāni» = the fused numeral «နှစ်သောင်း» (C3)",
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
    with open(HERE / "map-table-18.md", "w", encoding="utf-8") as f:
        f.write("# pi-2 Burmese keyword mapping: rules and review table (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း», chapter: "
                + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_18.py (a copy of the approved sample's map_all.py). Burmese from the FINAL pi-2 text of this track only "
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
