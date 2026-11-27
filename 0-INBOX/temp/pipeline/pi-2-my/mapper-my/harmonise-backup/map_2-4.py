"""Pāli→Burmese keyword mapping for pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»). Chapters 2-ayatanavibhango, 3-dhatuvibhango, 4-saccavibhango
(copy of the approved sample script map_all.py: its tables, compose rules, context functions and verifier).

usage (python3 -I -X utf8, from any directory):
  map_2-4.py             writes <ch>.mapped.md for every chapter in CHAPTERS and map-table-2-4.md, then verifies them
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


def f_paritta(kw, pali, my):
    """parittā: the Mātikā «limited» «အကန့်အသတ် ရှိသော»; in the wind list «parittā vātā» the text's «အားနည်းသော»."""
    return "အားနည်းသော" if re.search(r"\bparittā vātā", pali) else "အကန့်အသတ် ရှိသော"


def f_avacara(kw, pali, my):
    """āvacarā: the plane in a Mātikā compound «ဘုံနှင့် ဆိုင်သော»; «etthāvacarā» (frequenting this range) =
    «ကျင်လည်သော» (text «ကျင်လည်ကြသော»), when that is the word's first occurrence."""
    m = re.search(r"(\w*)āvacarā", pali)
    return "ကျင်လည်သော" if m and m.group(1) == "etth" else "ဘုံနှင့် ဆိုင်သော"


FUNCS = {"ajjhattam": f_ajjhattam, "rupa": f_rupa, "parittā": f_paritta, "āvacarā": f_avacara}
ALT = {}
CTX = {
    # one sense per segment (pi-1 harmonise decision 3): the first occurrence decides
    "2-171": {"rūpā": "ရုပ်"},          # «Dasāyatanā rūpā» (matter), not the visible objects of the khandha list
    "2-173": {"hadayaṃ": "နှလုံး"},     # the organ in the body-part list (pi-1 «နှလုံးသား» is the mind word)
    "2-174": {"raso": "အရည်"},          # «mūlaraso khandharaso …» = «အမြစ် အရည်» (juice, not taste)
    "2-175": {"sammā": "ကောင်းစွာ"},    # «sammā pariṇāmaṃ gacchati» (properly digested)
    "2-182": {"rūpā": "ရုပ်"},          # «khandhadhātuāyatanā rūpā vedanā …» (matter)
    "2-184": {"rūpaṃ": "အဆင်းအရောင်"},  # first «Yaṃ rūpaṃ … vaṇṇanibhā» = the object seen (pi-1 3-02 decision 3)
    "2-188": {"rūpā": "ရုပ်"},          # «Dasa dhātuyo rūpā» (matter)
    "2-192": {"taca": "အရေ"},           # valittacatā «အရေတွန့်ခြင်း» (skin; pi-1 «အခေါက်» is bark)
    "2-194": {"dukkha": "ဆင်းရဲ"},      # first: dukkhadhammena «ဆင်းရဲဖွယ်ရာဖြင့်»
    "2-195": {"dukkha": "ဆင်းရဲ"},
    "2-198": {"dukkha": "ဆင်းရဲ"},
    "2-196": {"dukkhaṃ": "နာကျင်မှု"},  # kāyikaṃ dukkhaṃ (pi-1 value), as 3-dhatu ^2-180
    "2-197": {"dukkhaṃ": "နာကျင်မှု"},
    "2-201": {"Na": "မဟုတ်"},           # «Na kho panetaṃ icchāya pattabbaṃ» = «… ရနိုင်သည် မဟုတ်»
    "2-202": {"dukkhā": "ဒုက္ခ"},       # «pañcupādānakkhandhā dukkhā» (rule 2)
    "2-203": {"rūpaṃ": "သဘော ရှိသော"},  # only in piyarūpaṃ / sātarūpaṃ «… သဘော ရှိသော» (nature, not matter)
    "2-204": {"rūpaṃ": "သဘော ရှိသော"},
    "2-205": {"ajjhattaṃ": "မိမိ၌",     # jhāna «ajjhattaṃ sampasādanaṃ» (pi-1 value)
              "dukkha": "ဒုက္ခ",          # first: dukkhanirodhagāminī
              "aṭṭhaṅgiko maggo": "အင်္ဂါ ရှစ်ပါး ရှိသော … မဂ်"},   # «… ရှိသော ဤအရိယာ မဂ်»
    "2-217": {"Dukkha": "ဒုက္ခ"},       # first: Dukkhasaccaṃ (the truth), not the feeling «နာကျင်သော»
    "2-218": {"ajjhattaṃ": "မိမိ၌ ရှိသော"},  # «Dukkhasaccaṃ siyā ajjhattaṃ, siyā bāhiraṃ» (text «မိမိ၌ ရှိသော»)
}

# =====================================================================================================
# chapters 2-4 (this script)
# =====================================================================================================
T_AYATANA = {
    # the twelve bases with their count (pi-1: a keyword with a numeral keeps the count the text uses)
    "Dvādasāyatanāni": "အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး",
    "Dvādasannaṃ": "ဆယ့်နှစ်ပါး", "Dvādasannaṃ āyatanānaṃ": "အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး",
    "Ekādasāyatanā": "အာရုံခံ နယ်ပယ် ဆယ့်တစ်ပါး", "Dasāyatanā": "အာရုံခံ နယ်ပယ် ဆယ်ပါး",
    # «Cakkhuṃ aniccaṃ dukkhaṃ anattā vipariṇāmadhammaṃ» (rule 3: the attributive phrase as the text builds it)
    "dukkhaṃ": "ဒုက္ခ", "anattā": "အတ္တ မဟုတ်သော",       # dukkhaṃ: rule 2 (copula ဖြစ်သော not the keyword)
    "vipariṇāmadhammaṃ": "ဖောက်ပြန်ပြောင်းလဲတတ်သော သဘော ရှိသော",
    # the synonym lists of the sense bases (pi-1 3-01 ^1-596 …; fragments of «X-m-petaṃ», rule 8)
    "paṇḍara": "ကြည်လင်သောအရာ", "khetta": "လယ်ကွင်း", "netta": "လမ်းပြ", "tīra": "ကမ်း",
    "cakkhundriya": "မျက်စိ၏ စွမ်းရည်", "sotindriya": "နား၏ စွမ်းရည်", "ghānindriya": "နှာခေါင်း၏ စွမ်းရည်",
    "jīvhindriya": "လျှာ၏ စွမ်းရည်", "kāyindriya": "ကိုယ်၏ စွမ်းရည်",
    "sappaṭighena": "ထိခိုက်မှု ရှိသော", "sappaṭighāya": "ထိခိုက်မှု ရှိသော",
    "anidassanāya sappaṭighāya": "မမြင်နိုင်သော ထိခိုက်မှု ရှိသော",
    # the object lists (rūpa, sadda, gandha, rasa)
    "mutta": "ပုလဲ", "caturassaṃ": "လေးထောင့်ပုံ", "nigghosa": "ဆူညံ", "āma": "အစိမ်း",
    "lambikaṃ": "အချဉ်စူး", "asādu": "စားမကောင်းသော",
    "yaṃ vā pana": "ရှိသမျှလည်း", "yo vā pana": "ရှိသမျှလည်း",       # N2: ရှိသမျှ renders yaṃ … atthi
    # abhidhamma part
    "moha": "မောဟ", "dosa": "ဒေါသ",
    "bahuvidhena vedanākkhandho": "အမျိုးမျိုး … ခံစားမှု အစုအဝေး",                  # N4
    "bahuvidhena saññākkhandho": "အမျိုးမျိုး … မှတ်သိမှု အစုအဝေး",
    "bahuvidhena saṅkhārakkhandho": "အမျိုးမျိုး … ပြုပြင်ဖန်တီးမှု အစုအဝေး",
    "asaṅkhatā dhātu": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော ဓာတ်",
    # pañhāpucchaka: subject + predicate pairs (pi-1 5 rule 21; the count and «သည်» are the gap)
    "āyatanā siyā": "အာရုံခံ နယ်ပယ် … တစ်ခါတစ်ရံ",
    "āyatanā anidassana": "အာရုံခံ နယ်ပယ် … မမြင်နိုင်သော",
    "āyatanā anidassanā": "အာရုံခံ နယ်ပယ် … မမြင်နိုင်သော",
    "āyatanā sappaṭighā": "အာရုံခံ နယ်ပယ် … ထိခိုက်မှု ရှိသော",
    "Dasāyatanā sappaṭighā": "အာရုံခံ နယ်ပယ် ဆယ်ပါး … ထိခိုက်မှု ရှိသော",
    "sappaṭigha": "ထိခိုက်မှု ရှိသော",
    "nevavipākanavipākadhammadhammā": "ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား",
    "sahabhū": "အတူ တည်ရှိသော", "acetasikā": "စိတ်၏ အဖော် မဟုတ်သော", "arūpaṃ": "ရုပ် မဟုတ်သော",
    "saṃsaṭṭhaṃ": "ရောနှောသော", "cittasaṃsaṭṭhaṃ": "စိတ်နှင့် ရောနှောသော",
    "asaṅkhataṃ": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော",
    # «X ceva X-sampayuttañca» (neuter of the sample's CEVA strings, pi-1 rule 6)
    "hetu ceva hetusampayuttañca": "အမြစ်လည်း ဖြစ် အမြစ်နှင့်လည်း ယှဉ်တွဲသော",
    "āsavo ceva āsavasampayuttañca": "စိတ်အစွန်းအထင်းလည်း ဖြစ် စိတ်အစွန်းအထင်းနှင့်လည်း ယှဉ်တွဲသော",
    "saṃyojanañceva saṃyojanasampayuttañca": "နှောင်ကြိုးလည်း ဖြစ် နှောင်ကြိုးနှင့်လည်း ယှဉ်တွဲသော",
    "gantho ceva ganthasampayuttañca": "အထုံးလည်း ဖြစ် အထုံးနှင့်လည်း ယှဉ်တွဲသော",
    "nīvaraṇañceva nīvaraṇasampayuttañca": "အတားအဆီးလည်း ဖြစ် အတားအဆီးနှင့်လည်း ယှဉ်တွဲသော",
    "kileso ceva kilesasampayuttañca": "ကိလေသာလည်း ဖြစ် ကိလေသာနှင့်လည်း ယှဉ်တွဲသော",
}
T_DHATU = {
    # the elements: «X-dhātudvayaṃ – atthi ajjhattikā, atthi bāhirā» (text «Xဓာတ် နှစ်မျိုး»)
    "dhātudvayaṃ": "ဓာတ် နှစ်မျိုး", "dvayaṃ": "နှစ်မျိုး", "aññampi": "အခြား",   # aññampi: N2 frame «အခြား …»
    "seyyathidaṃ": "ဆိုလိုသည်မှာ",
    "ajjhattikā tejo": "အတွင်းပိုင်း မီး", "ajjhattikā tejodhātu": "အတွင်းပိုင်း မီးဓာတ်",
    "bāhirā tejo": "ပြင်ပ မီး", "bāhirā tejodhātu": "ပြင်ပ မီးဓာတ်",
    "ajjhattikā vāyo": "အတွင်းပိုင်း လေ", "ajjhattikā vāyodhātu": "အတွင်းပိုင်း လေဓာတ်",
    "bāhirā vāyo": "ပြင်ပ လေ", "bāhirā vāyodhātu": "ပြင်ပ လေဓာတ်",
    "ajjhattikā ākāsa": "အတွင်းပိုင်း ဟင်းလင်းပြင်", "ajjhattikā ākāsadhātu": "အတွင်းပိုင်း ဟင်းလင်းပြင် ဓာတ်",
    "bāhirā ākāsa": "ပြင်ပ ဟင်းလင်းပြင်", "bāhirā ākāsadhātu": "ပြင်ပ ဟင်းလင်းပြင် ဓာတ်",
    # «X-gataṃ» = «X သဘော ရှိသော» (text «X သဘော ရှိသောအရာ»: the head အရာ goes, rule 3, as kakkhaḷaṃ = ကြမ်းတမ်းသော)
    "kharigataṃ": "ခက်မာ သဘော ရှိသော", "āpogataṃ": "ရေ သဘော ရှိသော", "sinehagataṃ": "စေးကပ်မှု သဘော ရှိသော",
    "tejogataṃ": "မီး သဘော ရှိသော", "usmāgataṃ": "အပူ သဘော ရှိသော", "usumagataṃ": "အပူငွေ့ သဘော ရှိသော",
    "vāyogataṃ": "လေ သဘော ရှိသော", "ākāsagataṃ": "ဟင်းလင်းပြင် သဘော ရှိသော", "aghagataṃ": "ဗလာ သဘော ရှိသော",
    "vivaragataṃ": "အပေါက် သဘော ရှိသော", "ākāso": "ဟင်းလင်းပြင်", "rūpassa": "ရုပ်",
    # earth: the body parts and the outer things (one word each, as the text lists them)
    "kesā": "ဆံပင်", "lomā": "မွေးညင်း", "nakhā": "ခြေသည်းလက်သည်း", "dantā": "သွား", "taco": "အရေ",
    "nhāru": "အကြော", "aṭṭhi": "အရိုး", "miñjaṃ": "ခြင်ဆီ", "vakkaṃ": "ကျောက်ကပ်", "yakanaṃ": "အသည်း",
    "kilomakaṃ": "အမြှေး", "pihakaṃ": "သရက်ရွက်", "papphāsaṃ": "အဆုတ်", "antaṃ": "အူမ", "antaguṇaṃ": "အူသိမ်",
    "udariyaṃ": "အစာသစ်", "karīsaṃ": "အစာဟောင်း",
    "ayo": "သံ", "lohaṃ": "ကြေး", "tipu": "သံဖြူ", "sajjhaṃ": "ငွေဖြူ", "veḷuriyo": "ကြောင်မျက်ရွဲ",
    "saṅkho": "ခရုသင်း", "silā": "ကျောက်ဖျာ", "pavāḷaṃ": "သန္တာ", "rajataṃ": "ငွေ", "lohitaṅko": "ပတ္တမြား",
    "masāragallaṃ": "မြ", "tiṇaṃ": "မြက်", "kaṭṭhaṃ": "ထင်း", "sakkharā": "ကျောက်စရစ်", "kaṭhalaṃ": "အိုးခြမ်းကွဲ",
    "bhūmi": "မြေ", "pāsāṇo": "ကျောက်တုံး", "pabbato": "တောင်",
    # water
    "pittaṃ": "သည်းခြေ", "semhaṃ": "သလိပ်", "pubbo": "ပြည်", "lohitaṃ": "သွေး", "sedo": "ချွေး", "medo": "အဆီခဲ",
    "assu": "မျက်ရည်", "vasā": "အဆီကြည်", "kheḷo": "တံတွေး", "siṅghāṇikā": "နှပ်", "lasikā": "အစေး",
    "muttaṃ": "ကျင်ငယ်",
    "bhummāni": "မြေပေါ်ရှိ", "antalikkhāni": "ကောင်းကင်", "udakāni": "ရေ",
    # fire: verbs in «သည်» (rule 4; text «… ခြင်း», check «verb»)
    "santappati": "ပူနွေးသည်", "jīrīyati": "အိုမင်းသည်", "pariḍayhati": "ပူလောင်သည်",
    "pariṇāmaṃ gacchati": "ကြေကျက်သည်",
    "asita": "စားထားသော", "pīta": "သောက်ထားသော", "khāyita": "ခဲထားသော", "sāyitaṃ": "လျက်ထားသော",
    "sammā": "မှန်ကန်သော",                           # sammāsaṅkappo; «sammā pariṇāmaṃ» is CTX 2-175
    "kaṭṭhaggi": "ထင်း မီး", "palālaggi": "ကောက်ရိုး မီး", "tiṇaggi": "မြက် မီး", "gomayaggi": "နွားချေး မီး",
    "thusaggi": "ဖွဲ မီး", "saṅkāraggi": "အမှိုက် မီး", "indaggi": "မိုးကြိုး မီး", "sannicaya": "ပုံ",
    # air
    "uddhaṅgamā": "အထက်သို့ တက်သော", "adhogamā": "အောက်သို့ ဆင်းသော",
    "gamā": "တက်သော",                                   # fragment, first in uddhaṅgamā
    "kucchisayā": "ဝမ်းတွင်း၌ ရှိသော", "koṭṭhāsayā": "အူတွင်း၌ ရှိသော",
    "aṅgamaṅgānusārino": "ကိုယ်အင်္ဂါ အသီးသီးသို့ လှည့်လည်သွားသော", "ānusārino": "လှည့်လည်သွားသော",
    "satthaka": "ဓား", "khuraka": "သင်တုန်းဓား", "uppalaka": "ထိုးဖောက်သကဲ့သို့ ဖြစ်သော",
    "assāso": "ဝင်လေ", "vātā": "လေ",
    "puratthimā": "အရှေ့", "sarajā": "ဖုန်ပါသော", "arajā": "ဖုန်မပါသော", "sītā": "အေးသော", "uṇhā": "ပူသော",
    "parittā": "@parittā", "kāḷa": "မည်း", "verambha": "လေပွေ", "pakkha": "အတောင်", "supaṇṇa": "ဂဠုန်",
    "tālavaṇṭa": "ထန်းလက် ယပ်", "vidhūpana": "ယပ်တောင်",
    # space
    "lohitehi": "သွေး", "maṃsa": "အသား", "nāsa": "နှာခေါင်း", "dvāraṃ": "ပေါက်",
    "ajjhoharati": "မျိုချသည်", "santiṭṭhati": "တည်နေသည်", "nikkhamati": "ထွက်သည်",
    # consciousness elements, the feeling elements, the six of thought (pi-1 «X ဓာတ်» frame)
    "sotaviññāṇadhātu": "နား သိစိတ် ဓာတ်", "ghānaviññāṇadhātu": "နှာခေါင်း သိစိတ် ဓာတ်",
    "jivhāviññāṇadhātu": "လျှာ သိစိတ် ဓာတ်",
    "sukhadhātu": "သာယာမှု ဓာတ်", "dukkhadhātu": "နာကျင်မှု ဓာတ်", "somanassadhātu": "ဝမ်းမြောက်မှု ဓာတ်",
    "domanassadhātu": "စိတ်ဆင်းရဲမှု ဓာတ်", "upekkhādhātu": "ဥပေက္ခာ ဓာတ်", "avijjādhātu": "အမှန်ကို မသိမှု ဓာတ်",
    "dukkhaṃ": "နာကျင်မှု",                                  # kāyikaṃ dukkhaṃ (pi-1 value)
    "dukkhaṃ vedayitaṃ": "နာကျင်သော ခံစားရခြင်း",
    "cetasikaṃ asātaṃ": "စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ် မကောင်းမှု", "cetosamphassa": "စိတ်၏ တွေ့ထိမှု",
    "asaṅgāhaṇā": "စုစည်း၍ မယူနိုင်ခြင်း", "apariyogāhaṇā": "နက်နက်နဲနဲ မသက်ဝင်နိုင်ခြင်း",
    "ānusayo": "ကိန်းအောင်းခြင်း",
    "kāmadhātu": "ကာမ ဓာတ်", "byāpādadhātu": "ဖျက်ဆီးလိုစိတ် ဓာတ်", "vihiṃsādhātu": "ညှဉ်းပန်းမှု ဓာတ်",
    "nekkhammadhātu": "ကာမမှ ထွက်မြောက်ခြင်း ဓာတ်", "abyāpādadhātu": "ဖျက်ဆီးလိုစိတ် မရှိခြင်း ဓာတ်",
    "avihiṃsādhātu": "ညှဉ်းပန်းမှု မရှိခြင်း ဓာတ်",
    "nekkhamma": "ကာမမှ ထွက်မြောက်ခြင်း", "abyāpāda": "ဖျက်ဆီးလိုစိတ် မရှိခြင်း", "avihiṃsā": "ညှဉ်းပန်းမှု မရှိခြင်း",
    "paṭisaṃyutto": "စပ်ယှဉ်သော", "Kāmapaṭisaṃyutto": "ကာမနှင့် စပ်ယှဉ်သော",
    "byappanā": "အာရုံ၌ စိတ်ကို နစ်မြုပ်စွာ သွင်းခြင်း",
    "nirayaṃ": "ငရဲ", "pariyantaṃ": "အဆုံး", "uparito": "အထက်ဘက်", "vasavattī deve": "ဝသဝတ္တီ နတ်",
    "āvacarā": "@āvacarā",
    "Dasasu": "ဆယ်ပါး", "vatthūsu": "အကြောင်း", "manopadoso": "မနောဖြင့် ဒေါသထွက်ခြင်း",
    "byāpajjanā": "ဖောက်ပြန်နေခြင်း",
    "pāṇinā": "လက်", "leḍḍunā": "မြေစိုင်ခဲ", "daṇḍena": "တုတ်", "satthena": "လက်နက်", "rajjuyā": "ကြိုး",
    "aññataraññatarena": "တစ်ခုခုသော အရာ", "sattesu": "သတ္တဝါ", "viheṭheti": "ညှဉ်းဆဲသည်",
    "heṭhanā": "နှိပ်စက်ခြင်း", "viheṭhanā": "ညှဉ်းဆဲခြင်း", "hiṃsanā": "ထိခိုက်နာကျင်စေခြင်း",
    "vihiṃsanā": "ညှဉ်းပန်းခြင်း", "rosanā": "ဒေါသ ထွက်စေခြင်း", "parūpaghāto": "သူတစ်ပါးကို ထိပါးခြင်း",
    "ūpaghāto": "ထိပါးခြင်း",
    "mettācetovimutti": "မေတ္တာဖြင့် စိတ်လွတ်မြောက်မှု", "karuṇācetovimutti": "ကရုဏာဖြင့် စိတ်လွတ်မြောက်မှု",
    "cetovimutti": "စိတ်လွတ်မြောက်မှု", "karuṇāyitattaṃ": "ကရုဏာ ထားသော အဖြစ်",
    "aṭṭhārasa": "ဆယ့်ရှစ်ပါး", "aṭṭhārasa dhātuyo": "ဓာတ် ဆယ့်ရှစ်ပါး", "Aṭṭhārasa dhātuyo": "ဓာတ် ဆယ့်ရှစ်ပါး",
    # abhidhamma part
    "uppajjati cittaṃ": "စိတ် … ဖြစ်ပေါ်သည်", "paṭicca": "မှီ၍", "samanantarā": "အခြားမဲ့",
    "niruddha": "ချုပ်ပြီးသော", "dhātuyā": "ဓာတ်", "samannāhāro": "နှလုံးသွင်းခြင်း", "dhammesu": "သဘောတရား",
    "rūpe": "အဆင်းအရောင်", "sadde": "အသံ", "gandhe": "အနံ့", "rase": "အရသာ", "phoṭṭhabbe": "အထိအတွေ့",
    "gāmopeso": "ရွာ", "vā pana": "သို့မဟုတ်",
    # pañhāpucchaka: counts and subject + predicate pairs (pi-1 5 rule 21)
    "Pannarasa": "ဆယ့်ငါးပါး", "Sattarasa": "ဆယ့်ခုနစ်ပါး", "Soḷasa": "ဆယ့်ခြောက်ပါး",
    "Pannarasa dhātuyo": "ဓာတ် ဆယ့်ငါးပါး", "Sattarasa dhātuyo": "ဓာတ် ဆယ့်ခုနစ်ပါး",
    "Soḷasa dhātuyo": "ဓာတ် ဆယ့်ခြောက်ပါး", "Dasa dhātuyo": "ဓာတ် ဆယ်ပါး", "Ekādasa dhātuyo": "ဓာတ် ဆယ့်တစ်ပါး",
    "Dvādasa dhātuyo": "ဓာတ် ဆယ့်နှစ်ပါး",
    "dhātuyo siyā": "ဓာတ် … တစ်ခါတစ်ရံ", "dhātuyo hetuvippayuttā": "ဓာတ် … အမြစ်နှင့် ကင်းကွာသော",
    "dhātuyo pariyāpannā": "ဓာတ် … ဘဝဘုံတို့၌ အကျုံးဝင်သော", "dhātuyo sappaṭighā": "ဓာတ် … ထိခိုက်မှု ရှိသော",
    "anidassanaappaṭighā": "မမြင်နိုင် ထိခိုက်မှုလည်း မရှိသော",
}
T_SACCA = {
    # the truths (headings and the four-truth list)
    "Dukkhasaccaṃ": "ဒုက္ခ သစ္စာ", "Samudaya": "ဖြစ်ပေါ်ခြင်း",
    "dukkhaṃ": "ဒုက္ခ", "dukkho": "ဒုက္ခ",                    # rule 2 (predicate noun «ဒုက္ခ ဖြစ်သည်»)
    "ariyasaccaṃ": "အရိယာ သစ္စာ", "ariyasaccāni": "အရိယာ သစ္စာ", "ariyasaccānaṃ": "အရိယာ သစ္စာ",
    "saccāni": "သစ္စာ", "saccā": "သစ္စာ", "saccānaṃ": "သစ္စာ",
    "dukkhaṃ ariyasaccaṃ": "ဒုက္ခ အရိယာ သစ္စာ",
    "samudayaṃ": "ဖြစ်ပေါ်ခြင်း", "dukkhasamudayaṃ": "ဒုက္ခ ဖြစ်ပေါ်ခြင်း", "dukkhasamudayo": "ဒုက္ခ ဖြစ်ပေါ်ခြင်း",
    "dukkhasamudaye": "ဒုက္ခ ဖြစ်ပေါ်ခြင်း",
    "dukkhanirodhaṃ": "ဒုက္ခ ချုပ်ငြိမ်းခြင်း", "dukkhanirodho": "ဒုက္ခ ချုပ်ငြိမ်းခြင်း",
    "dukkhanirodha": "ဒုက္ခ ချုပ်ငြိမ်းရာ",                    # first in dukkhanirodhagāminī «… ချုပ်ငြိမ်းရာသို့»
    # dukkha ariyasacca
    "Jātipi": "မွေးဖွားခြင်း", "jarāpi": "အိုခြင်း", "maraṇampi": "သေခြင်း", "upāyāsāpi": "ပြင်းစွာ ပူပန်ခြင်း",
    "sokaparidevadukkhadomanassupāyāsāpi": "စိုးရိမ်ခြင်း ငိုကြွေးခြင်း ကိုယ်ဆင်းရဲခြင်း စိတ်ဆင်းရဲမှု ပြင်းစွာ ပူပန်ခြင်း",
    "sokaparidevadukkhadomanassupāyāsā": "စိုးရိမ်ခြင်း ငိုကြွေးခြင်း ကိုယ်ဆင်းရဲခြင်း စိတ်ဆင်းရဲမှု ပြင်းစွာ ပူပန်ခြင်း",
    "appiyehi": "မချစ်သော အရာ", "piyehi": "ချစ်သော အရာ", "vippayogo": "ကွေကွင်းရခြင်း",
    "picchaṃ": "အလိုရှိသည်", "labhati": "ရသည်", "saṃkhittena": "အကျဉ်း",
    "sañjāti": "ကောင်းစွာ မွေးဖွားခြင်း", "okkanti": "သက်ဆင်းခြင်း", "abhinibbatti": "ထင်ရှားစွာ ပေါ်ထွက်ခြင်း",
    "pātubhāvo": "ထင်ရှား လာခြင်း", "paṭilābho": "ရရှိခြင်း", "nikāye": "အမျိုးအစား", "nikāyā": "အမျိုးအစား",
    "vali": "တွန့်",
    "cuti": "စုတေခြင်း", "cavanatā": "ရွေ့လျောခြင်း", "maccu": "သေမင်း", "kālakiriyā": "ကွယ်လွန်ခြင်း",
    "kaḷevarassa": "ကိုယ်ခန္ဓာ", "nikkhepo": "စွန့်ပစ်ခြင်း", "upacchedo": "ပြတ်စဲခြင်း",
    "jīvitindriya": "အသက်၏ စွမ်းရည်", "jīvitindriyassupacchedo": "အသက်၏ စွမ်းရည် ပြတ်စဲခြင်း",
    # soka, parideva, upāyāsa
    "Ñāti": "ဆွေမျိုး", "bhoga": "စည်းစိမ်", "roga": "ကျန်းမာရေး", "byasanena": "ပျက်စီးခြင်း",
    "phuṭṭhassa": "ထိခိုက်ခံရသော", "byasanena vā phuṭṭhassa": "ပျက်စီးခြင်းဖြင့် ထိခိုက်ခံရသော",
    "samannāgatassa": "ကြုံတွေ့နေရသော", "dhammena": "ဖွယ်ရာ",
    "soko": "စိုးရိမ်ခြင်း", "socanā": "စိုးရိမ်နေခြင်း", "anto": "အတွင်း",
    "antoparisoko": "အတွင်း ပြင်းစွာ စိုးရိမ်ခြင်း", "parijjhāyanā": "လောင်မြိုက်ခြင်း", "sallaṃ": "ငြောင့်",
    "domanassaṃ": "စိတ်ဆင်းရဲမှု",
    "ādevo": "ငိုခြင်း", "paridevo": "ငိုကြွေးခြင်း", "ādevanā": "ငိုနေခြင်း", "palāpo": "ပေါက်ကရ ပြောခြင်း",
    "vippalāpo": "ကမောက်ကမ ပြောခြင်း", "lālappo": "မြည်တမ်းခြင်း",
    "āyāso": "ပူပန်ခြင်း", "upāyāso": "ပြင်းစွာ ပူပန်ခြင်း",
    # appiya / piya
    "yassa": "အကြင်သူ",                                        # the text writes the relative (pi-1 4-01 Yo «အကြင်»)
    "aniṭṭhā": "လိုလားဖွယ် မကောင်းသော", "akantā": "ချစ်ခင်ဖွယ် မကောင်းသော", "amanāpā": "စိတ်နှင့် မတွေ့သော",
    "iṭṭhā": "လိုလားဖွယ်ကောင်းသော", "kantā": "ချစ်ခင်ဖွယ်ကောင်းသော", "manāpā": "စိတ်နှင့် တွေ့သော",
    "ye vā panassa": "သို့မဟုတ် ထိုသူ", "kāmā": "လိုလားသော",
    "anattha": "အကျိုး မရှိခြင်း", "ahita": "အစီးအပွား မရှိခြင်း", "aphāsuka": "ချမ်းသာ မရှိခြင်း",
    "ayogakkhemakāmā": "ဘေးကင်းမှု မရှိခြင်းကို လိုလားသော", "phāsuka": "ချမ်းသာ", "yogakkhema": "ဘေးကင်းမှု",
    "samāgamo": "ဆုံဆည်းခြင်း", "samodhānaṃ": "ပေါင်းစည်းခြင်း", "missībhāvo": "ရောနှောခြင်း",
    "asamāgamo": "မဆုံဆည်းခြင်း", "asamodhānaṃ": "မပေါင်းစည်းခြင်း", "amissībhāvo": "မရောနှောခြင်း",
    "mātā": "မိခင်", "pitā": "ဖခင်", "bhātā": "ညီအစ်ကို", "bhaginī": "ညီအစ်မ", "mittā": "မိတ်ဆွေ",
    "amaccā": "အပေါင်းအဖော်", "ñātī": "ဆွေမျိုး", "sālohitā": "သွေးချင်း",
    "icchā": "ဆန္ဒ", "icchāya": "ဆန္ဒ", "pattabbaṃ": "ရနိုင်သော",
    "rūpupādānakkhandho": "စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော ရုပ် အစုအဝေး",
    "vedanupādānakkhandho": "စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော ခံစားမှု အစုအဝေး",
    "saññupādānakkhandho": "စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော မှတ်သိမှု အစုအဝေး",
    "saṅkhārupādānakkhandho": "စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော ပြုပြင်ဖန်တီးမှု အစုအဝေး",
    "viññāṇupādānakkhandho": "စွဲလမ်းမှု၏ အာရုံ ဖြစ်သော သိစိတ် အစုအဝေး",
    # samudaya, nirodha
    "ponobhavikā": "ဘဝသစ်ကို ဖြစ်စေတတ်သော", "nandi": "နှစ်သက်မှု", "ābhinandinī": "အလွန် နှစ်သက်တတ်သော",
    "kāmataṇhā": "ကာမကို တပ်မက်မှု", "bhavataṇhā": "ဘဝကို တပ်မက်မှု",
    "vibhavataṇhā": "ဘဝ ပျောက်ကွယ်ခြင်းကို တပ်မက်မှု", "phoṭṭhabbataṇhā": "အထိအတွေ့ကို တပ်မက်မှု",
    "taṇhā uppajjamānā uppajjati": "တပ်မက်မှု … ဖြစ်ပေါ်လျှင် ဖြစ်ပေါ်သည်", "nivisati": "တည်သည်",
    "taṇhā pahīyamānā pahīyati": "တပ်မက်မှု … ပျောက်ကင်းလျှင် ပျောက်ကင်းသည်",
    "pahīyati": "ပျောက်ကင်းသည်", "nirujjhati": "ချုပ်ငြိမ်းသည်",
    "piyarūpaṃ": "ချစ်ဖွယ် သဘော ရှိသော", "sātarūpaṃ": "နှစ်သက်ဖွယ်ကောင်းသော သဘော ရှိသော",
    "sañcetanā": "စေ့ဆော်မှု", "manosamphasso": "မနော၏ တွေ့ထိမှု",
    "asesa": "အကြွင်း မရှိ", "virāga": "ကင်းပြတ်", "cāgo": "စွန့်လွှတ်ခြင်း", "paṭinissaggo": "စွန့်ပစ်ခြင်း",
    "mutti": "လွတ်မြောက်ခြင်း", "anālayo": "မတွယ်တာခြင်း",
    # magga (suttanta): the eightfold path, the four exertions, satipaṭṭhāna, jhāna
    "aṭṭhaṅgiko maggo": "အင်္ဂါ ရှစ်ပါး ရှိသော မဂ်", "pañcaṅgiko maggo": "အင်္ဂါ ငါးပါး ရှိသော မဂ်",
    "Musā": "မုသား", "Musāvādā": "မုသား ပြောခြင်း", "pisuṇāya": "ကုန်းတိုက်သော", "pharusāya": "ကြမ်းတမ်းသော",
    "samphappalāpā": "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", "Pāṇātipātā": "သူ့အသက်ကို သတ်ခြင်း", "ātipātā": "သတ်ခြင်း",
    "ādānā": "ယူခြင်း", "micchācārā": "မှားယွင်းစွာ ကျင့်ခြင်း",
    "sāvako": "တပည့်", "pahāya": "ပယ်၍", "kappeti": "အသက်မွေးသည်",
    "anuppādāya": "မဖြစ်ပေါ်ရန်", "chandaṃ janeti": "ဆန္ဒကို ဖြစ်စေသည်",
    "kāye": "ကိုယ်", "Vedanāsu": "ခံစားမှု",
    "kāye kāyānupassī": "ကိုယ်၌ ကိုယ်ကို အဖန်ဖန် ရှုလျက်",                    # N-B (the text's «…လျက်»)
    "kāyānupassī viharati": "ကိုယ်ကို အဖန်ဖန် ရှုလျက် … နေသည်", "ānupassī": "အဖန်ဖန် ရှုလျက်",
    "ātāpī": "အားထုတ်သော", "satimā": "သတိ ရှိသော", "sukhavihārī": "သာယာစွာ နေသော",
    "vineyya": "ပယ်ဖျောက်လျက်",
    "viveka": "ကင်းဆိတ်ခြင်း", "savitakkaṃ savicāraṃ": "စတင်ကြံစည်မှု ရှိသော ဆက်လက်သုံးသပ်မှု ရှိသော",
    "pītisukhaṃ": "ပီတိနှင့် သာယာမှု ရှိသော",
    "Vitakkavicārānaṃ vūpasamā": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်း",
    # magga (abhidhamma)
    "pahānaṃ": "ပယ်ခြင်း", "Taṇhāya": "တပ်မက်မှု", "Taṇhāya pahānaṃ": "တပ်မက်မှုကို ပယ်ခြင်း",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "ကျင့်စဉ် ခက်ခဲသော ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    "ābhiññaṃ": "ထူးကဲစွာ သိခြင်း",
    "apacayagāmiṃ": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "dhammavicayasambojjhaṅgo": "သဘောတရားများကို စိစစ်ခြင်း ဗောဇ္ဈင်", "satisambojjhaṅgo": "သတိ ဗောဇ္ဈင်",
    "kāyaduccaritehi": "ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်", "vacīduccaritehi": "နှုတ်ဖြင့် ပြုသော ဒုစရိုက်",
    "akiriyā": "မပြုခြင်း", "akaraṇaṃ": "မပြုလုပ်ခြင်း", "anajjhāpatti": "မကျူးလွန်ခြင်း",
    "anatikkamo": "မကျော်လွန်ခြင်း",
    "Avasesā ca kilesā": "ကြွင်းကျန်သော ကိလေသာ", "avasesā ca kilesā": "ကြွင်းကျန်သော ကိလေသာ",
    "avasesā ca akusalā": "ကြွင်းကျန်သော အကုသိုလ်", "Avasesā ca akusalā": "ကြွင်းကျန်သော အကုသိုလ်",
    "sāsavāni": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော",
    "mūlāni sāsavāni": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော … အမြစ်",
    "kusalamūlāni sāsavāni": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ်၏ အမြစ်",
    "sāsavā kusalā dhammā": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ် သဘောတရား",
    "kusalākusalānaṃ": "ကုသိုလ်နှင့် အကုသိုလ်", "dhammānaṃ": "သဘောတရား",
    "kusalākusalānaṃ dhammānaṃ vipākā": "ကုသိုလ်နှင့် အကုသိုလ် သဘောတရားတို့၏ အကျိုး",
    "Sāsavā kusalākusalānaṃ dhammānaṃ": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ်နှင့် အကုသိုလ် သဘောတရား",
    "neva kusalā nākusalā": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်",
    # pañhāpucchaka
    "āsekkhā": "ကျင့်ကြံမှု ပြီးဆုံးသူ၏", "appaṭighā": "ထိခိုက်မှု မရှိသော", "arūpāni": "ရုပ် မဟုတ်သော",
    "saccā araṇā": "သစ္စာ … ပဋိပက္ခ မရှိသော", "saccāni appaṭighā": "သစ္စာ … ထိခိုက်မှု မရှိသော",
    "upādānañceva upādānasampayuttañca": "စွဲလမ်းမှုလည်း ဖြစ် စွဲလမ်းမှုနှင့်လည်း ယှဉ်တွဲသော",
}

SECTIONS = {
    "2-ayatanavibhango": T_AYATANA,
    "3-dhatuvibhango": T_DHATU,
    "4-saccavibhango": T_SACCA,
    "preamble": T_PREAMBLE,              # the approved sample tables, shared (looked up after the chapter's own)
    "1-khandhavibhango": T_KHANDHA,
}
CHAPTERS = ["2-ayatanavibhango", "3-dhatuvibhango", "4-saccavibhango"]


# =====================================================================================================
# rules (written to map-table.md)
# =====================================================================================================
RULES = """## Rules

**Binding and unchanged** (not repeated here): pi-1 `map-table.md` rules 1–11 and the agreed later pi-1 rules
(absolutives keep «…၍»; «samaye X» = «အချိန်၌ ရှိသော X»; relative pronouns = (no direct equivalent) where the text
builds the clause with «ရှိသော / ရှိသမျှ»; one sense per segment; no « / » alternatives), and the approved pi-2 sample
rules N1–N11 of `map-table.md` with its six deliberate differences from pi-1. This script is a copy of the sample's
`map_all.py` (tables, compose rules, context functions, verifier); the sample tables T_PREAMBLE / T_KHANDHA are kept
unchanged and shared, so every Mātikā / pañhāpucchaka value of chapters 2–4 is the sample's value. Lookup order:
CTX[segment] → the chapter's own table → the shared tables → the pi-1 mapping (the most frequent pi-1 value present in
the segment) → compose.

Approved rules applied to the new shapes of chapters 2–4 (no new principle):

- **Counts** (pi-1: a keyword with a numeral keeps the count): Dvādasāyatanāni = အာရုံခံ နယ်ပယ် ဆယ့်နှစ်ပါး,
  Dasāyatanā = အာရုံခံ နယ်ပယ် ဆယ်ပါး, Pannarasa dhātuyo = ဓာတ် ဆယ့်ငါးပါး, aṭṭhārasa dhātuyo = ဓာတ် ဆယ့်ရှစ်ပါး,
  dhātudvayaṃ = ဓာတ် နှစ်မျိုး.
- **Subject + predicate pairs of the pañhāpucchaka** (pi-1 5 rule 21, sample «khandhā siyā»): āyatanā siyā =
  အာရုံခံ နယ်ပယ် … တစ်ခါတစ်ရံ, dhātuyo siyā = ဓာတ် … တစ်ခါတစ်ရံ, Dasāyatanā sappaṭighā = အာရုံခံ နယ်ပယ် ဆယ်ပါး …
  ထိခိုက်မှု ရှိသော, saccā araṇā = သစ္စာ … ပဋိပက္ခ မရှိသော (the count and «သည်» fall in the gap).
- **The CEVA strings in the neuter** (pi-1 rule 6, sample CLUSTERS): hetu ceva hetusampayuttañca = အမြစ်လည်း ဖြစ်
  အမြစ်နှင့်လည်း ယှဉ်တွဲသော, and the same for āsava, saṃyojana, gantha, nīvaraṇa, kilesa, upādāna.
- **N4 with bahuvidhena**: bahuvidhena vedanākkhandho = အမျိုးမျိုး … ခံစားမှု အစုအဝေး.
- **Rule 3, the text's «…သူ» / «…သည့်» / «…၍» normalised to «…သော»**: ātāpī = အားထုတ်သော (text «အားထုတ်သူ»),
  satimā = သတိ ရှိသော, sukhavihārī = သာယာစွာ နေသော, phuṭṭhassa = ထိခိုက်ခံရသော, samannāgatassa = ကြုံတွေ့နေရသော,
  kāmā (-kāmā) = လိုလားသော, āvacarā in «etthāvacarā» = ကျင်လည်သော (text «ကျင်လည်ကြသော»), niruddha = ချုပ်ပြီးသော
  (text «ချုပ်ပြီးသည့်»), pattabbaṃ = ရနိုင်သော (text «ရနိုင်သည် မဟုတ်»).
- **Rule 3, the head noun «အရာ» goes**: the «-gataṃ» words = «X သဘော ရှိသော» (text «X သဘော ရှိသောအရာ»):
  kharigataṃ = ခက်မာ သဘော ရှိသော, āpogataṃ = ရေ သဘော ရှိသော, usmāgataṃ = အပူ သဘော ရှိသော, as pi-1 kakkhaḷaṃ =
  ကြမ်းတမ်းသော (text «ကြမ်းတမ်းသောအရာ»); paṇḍara = ကြည်လင်သောအရာ keeps it (the text's noun, pi-1 paṇḍaraṃ).
- **Rule 4, verbs in «သည်»** (text «…ခြင်း» / «…၏», check «verb»): santappati = ပူနွေးသည်, jīrīyati = အိုမင်းသည်,
  pariṇāmaṃ gacchati = ကြေကျက်သည်, ajjhoharati = မျိုချသည်, viheṭheti = ညှဉ်းဆဲသည်, kappeti = အသက်မွေးသည်,
  labhati = ရသည်, pahīyati = ပျောက်ကင်းသည်, nivisati = တည်သည်; with the subject in the keyword the Burmese order
  subject … verb: uppajjati cittaṃ = စိတ် … ဖြစ်ပေါ်သည်, kāyānupassī viharati = ကိုယ်ကို အဖန်ဖန် ရှုလျက် … နေသည်.
- **Absolutives** (decision 1): pahāya = ပယ်၍, paṭicca = မှီ၍ («Cakkhuñca paṭicca rūpe ca» = «…ကိုလည်းကောင်း
  …ကိုလည်းကောင်း မှီ၍»; the pi-1 «အကြောင်းတို့ကို မှီ၍» is paṭiccasamuppanna).
- **Rule 2, a noun predicated** (the copula is not the keyword): dukkhaṃ / dukkho / dukkhā = ဒုက္ခ («Jātipi dukkhā» =
  «မွေးဖွားခြင်းသည်လည်း ဒုက္ခ ဖြစ်သည်»; also «Cakkhuṃ aniccaṃ dukkhaṃ anattā» = «… ဒုက္ခ ဖြစ်သော …»); anattā keeps
  its negative (one word in Pāli): အတ္တ မဟုတ်သော.
- **Rule 8, fragments = the text's word for the part**: tīra = ကမ်း (orimaṃ tīraṃ «ဤဘက်ကမ်း»), nigghosa = ဆူညံ,
  āma = အစိမ်း, X-aggi = «X မီး», sannicaya = ပုံ, gamā (first in uddhaṅgamā) = တက်သော, vali / taca (valittacatā
  «အရေတွန့်ခြင်း») = တွန့် / အရေ, dukkha / dhammena (dukkhadhammena «ဆင်းရဲဖွယ်ရာဖြင့်») = ဆင်းရဲ / ဖွယ်ရာ,
  asesa / virāga (asesavirāganirodho «အကြွင်း မရှိ ကင်းပြတ်ချုပ်ငြိမ်းခြင်း») = အကြွင်း မရှိ / ကင်းပြတ်.
- **One sense per segment** (decision 3, the first occurrence decides): rūpā = ရုပ် in the pañhāpucchaka
  («Dasāyatanā rūpā», «Dasa dhātuyo rūpā») and in «khandhadhātuāyatanā rūpā vedanā …» (^2-182), the visible object
  «အဆင်းအရောင်» in the object lists; rūpaṃ in ^2-184 = အဆင်းအရောင် (first «Yaṃ rūpaṃ … vaṇṇanibhā», pi-1 3-02);
  rūpaṃ in ^2-203 / ^2-204 occurs only inside piyarūpaṃ / sātarūpaṃ = «သဘော ရှိသော» (nature); dukkha = ဒုက္ခ where
  the truth comes first, နာကျင်မှု where the faculty / element comes first (^2-161 dukkhindriya, ^2-179), ဆင်းရဲ in
  the soka / parideva / upāyāsa definitions (dukkhadhammena first); hadayaṃ = နှလုံး in the body-part list (^2-173),
  နှလုံးသား (pi-1) in the citta list; parittā = အားနည်းသော in the wind list (^2-176, context function), the Mātikā
  value elsewhere; sammā = ကောင်းစွာ in «sammā pariṇāmaṃ gacchati» (^2-175), မှန်ကန်သော (pi-1) in the path factors;
  raso = အရည် in the water list (^2-174), အရသာ (pi-1) in the taste list; ajjhattaṃ = မိမိ၌ (pi-1 jhāna adverb) in
  «ajjhattaṃ sampasādanaṃ» (^2-205), မိမိ၌ ရှိသော for the dyad item «siyā ajjhattaṃ, siyā bāhiraṃ» (^2-218, the
  text's word), မိမိ၏ အတွင်း၌ ဖြစ်သော (sample) in the element definitions.
- **«Na» as the text's free negative**: «Na kho panetaṃ icchāya pattabbaṃ» = «… ရနိုင်သည် မဟုတ်» gives Na = မဟုတ်
  (pi-1 rule 5 «na / no X» = «…သည် မဟုတ်»); the bound «na labhati» keeps «မ» (rule 9).

## NEW rules (for the user's review)

M1. **-pi nouns** (Jātipi, jarāpi, maraṇampi, upāyāsāpi, sokaparidevadukkhadomanassupāyāsāpi) = the noun alone:
    the text's «…သည်လည်း» is the case particle + the «also» of -pi, both after the noun (rule 1 strips particles at
    the end); the five-member compound is the five nouns without «၊» (rule 6).
M2. **The satipaṭṭhāna participle «…လျက်»** is kept as the text writes it, like the absolutives of decision 1:
    kāye kāyānupassī = ကိုယ်၌ ကိုယ်ကို အဖန်ဖန် ရှုလျက်, ānupassī = အဖန်ဖန် ရှုလျက်, vineyya = ပယ်ဖျောက်လျက်.
    No approved ending turns «လျက်» into «သော», so the value stays literal (no new presence rule).
M3. **The conditional present participle** «taṇhā uppajjamānā uppajjati» = «တပ်မက်မှု … ဖြစ်ပေါ်လျှင် ဖြစ်ပေါ်သည်»
    (text «ဤတပ်မက်မှုသည် ဖြစ်ပေါ်လျှင် ဖြစ်ပေါ်သည်»): the participle keeps the text's «…လျှင်», the finite verb is
    in «သည်» (rule 4), the demonstrative «ဤ» and «သည်» are the gap; the same for «taṇhā pahīyamānā pahīyati».
M4. **Relatives the text writes out**: yassa = အကြင်သူ (text «အကြင်သူအား»; as pi-1 4-01 Yo = «အကြင်» where the text
    writes it); ye vā panassa = သို့မဟုတ် ထိုသူ (text «သို့မဟုတ် ထိုသူ၏ …»: ye has no word, vā pana = သို့မဟုတ်,
    assa = ထိုသူ, ၏ dropped by rule 1); vā pana in «sabbadhammesu vā pana» = သို့မဟုတ်. yaṃ vā pana / yo vā pana
    (without aññampi in the keyword) = ရှိသမျှလည်း (N2: ရှိသမျှ renders yaṃ … atthi; aññampi = အခြား separately).
M5. **Juice and elements**: rūpassa = ရုပ် (genitive dropped, rule 1) in «bandhanattaṃ rūpassa»; seyyathidaṃ =
    ဆိုလိုသည်မှာ (the text's «that is», kept whole as a fixed phrase).

## Presence: notes on literal matches

- pitā: the pi-1 value «အဖ» occurred only inside «အပေါင်းအဖော်» (amaccā); the text's word «ဖခင်» is used instead.
- saṃkiliṭṭha (^2-170, ^2-187, ^2-217) and sanidassana (^2-170, ^2-217), pi-1 values: the chunk «ညစ်နွမ်းသော» /
  «မြင်နိုင်သော» is found literally only inside the negative «မညစ်နွမ်းသော်လည်း» / «မမြင်နိုင်သော်လည်း»; the
  positive term itself is in the text as «ကိလေသာဖြင့် ညစ်နွမ်း၍» / «မြင်နိုင်၍» (rule 3 normalises ၍ to သော).
- Every other chunk found literally starts at a word or is the text's compound member (e.g. «အတူ» in «…နှင့်အတူ»,
  «ကမ်း» in «ဤဘက်ကမ်း», «ပုံ» in «ထင်းပုံ», «ပေါက်» in «ခံတွင်းပေါက်», «ဝသဝတ္တီ» in «ပရနိမ္မိတဝသဝတ္တီ»).
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
    "ajjhattaṃ": "one sense per segment: the sample's «မိမိ၏ အတွင်း၌ ဖြစ်သော» in the element definitions («Yaṃ "
                 "ajjhattaṃ paccattaṃ …»); «မိမိ၌ ရှိသော» for the dyad item «siyā ajjhattaṃ, siyā bāhiraṃ» (^2-218, "
                 "the text's word); pi-1 «မိမိ၌» is kept for the jhāna adverb (^2-205)",
    "bahiddhā": "approved sample difference: the pi-2 text's qualifier is «မိမိ၏ ပြင်ပ၌»",
    "anuppādāya": "the pi-2 text has «မဖြစ်ပေါ်ရန်» (pi-1 «မဖြစ်ပေါ်စေရန်» does not occur)",
    "byāpajjanā": "the pi-2 text renders «byāpatti byāpajjanā» as «ဖောက်ပြန်ခြင်း၊ ဖောက်ပြန်နေခြင်း» (pi-1 "
                  "«ညှဉ်းဆဲလိုခြင်း» does not occur)",
    "cuti": "the text's word for cuti is «စုတေခြင်း»; pi-1 «သေခြင်း» renders maraṇa in the same segment",
    "dukkha": "dukkhadhammena «ဆင်းရဲဖွယ်ရာဖြင့်» is the first occurrence in the soka / parideva / upāyāsa "
              "definitions (one sense per segment); none of the pi-1 values carries it there",
    "dukkhaṃ": "rule 2: the truth / predicate noun «ဒုက္ခ ဖြစ်သည်» (pi-1 «နာကျင်မှု» is the feeling, kept where the "
               "text has it: kāyikaṃ dukkhaṃ ^2-180, ^2-196, ^2-197)",
    "gamā": "fragment; first in uddhaṅgamā «အထက်သို့ တက်သော» (pi-1 «ရောက်သော» does not occur)",
    "hadayaṃ": "the organ in the body-part list «နှလုံး» (^2-173); pi-1 «နှလုံးသား» kept in the citta list (^2-184)",
    "icchā": "the pi-2 text renders icchā here as «ဆန္ဒ» (pi-1 «အလိုရှိခြင်း» does not occur)",
    "kantā": "the pi-2 text's «ချစ်ခင်ဖွယ်ကောင်းသော» (as the sample's kantaṃ); pi-1 «နှစ်သက်သော» does not occur",
    "manāpā": "the pi-2 text's «စိတ်နှင့် တွေ့သော» (as the sample's manāpaṃ); pi-1 «စိတ်တွေ့သော» does not occur",
    "mātā": "the pi-2 text's «မိခင်» (pi-1 «အမိ» does not occur)",
    "Na": "«Na kho panetaṃ … pattabbaṃ» = «… ရနိုင်သည် မဟုတ်»: the text's free negative (pi-1 rule 5)",
    "parittā": "«parittā vātā» = «အားနည်းသော လေ» (wind list, ^2-176); the Mātikā value elsewhere",
    "pariyantaṃ": "the pi-2 text's «အဆုံး ပြု၍» (pi-1 «အဆုံးအစွန်» does not occur)",
    "paṭicca": "absolutive «မှီ၍» (decision 1) in «Cakkhuñca paṭicca rūpe ca»; pi-1 «အကြောင်းတို့ကို မှီ၍» is "
               "paṭiccasamuppanna",
    "pitā": "the text's «ဖခင်»; pi-1 «အဖ» occurs only inside «အပေါင်းအဖော်»",
    "pīta": "«asitapītakhāyitasāyitaṃ» = drunk «သောက်ထားသော» (pi-1 «အဝါ» is the colour)",
    "raso": "«mūlaraso …» in the water list = juice «အရည်» (^2-174); pi-1 «အရသာ» kept in the taste list",
    "rūpaṃ": "only inside piyarūpaṃ / sātarūpaṃ «… သဘော ရှိသော» (nature) in ^2-203 / ^2-204",
    "sammā": "«sammā pariṇāmaṃ gacchati» = «ကောင်းစွာ ကြေကျက်ခြင်း» (^2-175); pi-1 «မှန်ကန်သော» kept for the path",
    "sañcetanā": "the pi-2 text's «စေ့ဆော်မှု» (pi-1 «စေ့ဆော်ခြင်း» does not occur)",
    "taca": "valittacatā «အရေတွန့်ခြင်း» = skin (pi-1 «အခေါက်» is bark, kept in the smell / taste lists)",
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
    with open(HERE / "map-table-2-4.md", "w", encoding="utf-8") as f:
        f.write("# pi-2 Burmese keyword mapping: rules and review table (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း»: "
                + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_2-4.py (a copy of the approved sample script map_all.py). Burmese from the FINAL pi-2 text of this track only "
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


def compact(ch, only_open=False):
    """working aid: per segment, the mapping only (no texts); «??» = no value yet, with the pi-1 values."""
    my, pa, rows = load(ch)
    for sid, kws in rows:
        out = []
        for kw in [k.strip() for k in kws.split(", ")]:
            try:
                v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                if only_open:
                    continue
                ok = presence(v, my[sid])[0]
                out.append(f"{kw}={v}[{SRC[(sid, kw)][0]}{'' if ok else ' FAIL'}]")
            except KeyError:
                c = pi1_vals(kw)
                out.append(f"{kw}=??" + ("{" + " · ".join(f"{x}({m})" for x, m in c.most_common(3)) + "}" if c else ""))
        if out:
            print(f"== {sid} ({len(my[sid])} chars): " + " | ".join(out))


LEFT = set(" ၊။“‘”’–…([—-")


def bound_scan():
    """working aid: chunks found literally, but never at a word start (only inside another word): possible false
    positives of the substring presence check, listed for review."""
    for ch in CHAPTERS:
        my, pa, rows = load(ch)
        seen = set()
        for sid, kws in rows:
            for kw in [k.strip() for k in kws.split(", ")]:
                v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                if v == NONE:
                    continue
                for c in v.replace(" … ", " ").split():
                    t = my[sid]
                    if c not in t:
                        continue
                    if not any(i == 0 or t[i - 1] in LEFT for i in [m.start() for m in re.finditer(re.escape(c), t)]):
                        if (kw, v, c) not in seen:
                            seen.add((kw, v, c))
                            i = t.find(c)
                            print(f"{ch} {sid} {kw}={v} : «{c}» in …{t[max(0, i - 15):i + len(c) + 10]}…")


def grep(sid, *words):
    """working aid: the Burmese of segment sid around each word (or the Pāli, for a word in Latin script)."""
    for ch in CHAPTERS:
        my, pa, rows = load(ch)
        if sid not in my:
            continue
        for w in words:
            t = pa[sid] if w.isascii() or any("a" <= c <= "z" for c in w.lower()) else my[sid]
            for m in re.finditer(re.escape(w), t):
                print(f"{w}: …{t[max(0, m.start() - 80):m.end() + 80]}…")


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
                    c = pi1_vals(kw)
                    out.append(f"{kw}=??" + (" {pi-1: " + " · ".join(f"{x}({m})" for x, m in c.most_common(4)) + "}"
                                             if c else ""))
            print(" | ".join(out))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] in ("--cm", "--open"):
        CHAPTERS[:] = [args[1]]
        compact(args[1], args[0] == "--open")
        sys.exit()
    if args and args[0] == "--pi1":          # working aid: pi-1 values of keywords containing each argument
        for a in args[1:]:
            for k in sorted(k for k in PI1 if a in k)[:25]:
                print(f"{k}: " + " · ".join(f"{v} ({n})" for v, n in PI1[k].most_common(4)))
        sys.exit()
    if args and args[0] == "--bound":
        bound_scan()
        sys.exit()
    if args and args[0] == "--grep":
        grep(*args[1:])
        sys.exit()
    if args and args[0] == "--ch":           # working aid: every segment of one chapter
        CHAPTERS[:] = [args[1]]
        show([r[0] for r in load(args[1])[2]], pali=True)
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
