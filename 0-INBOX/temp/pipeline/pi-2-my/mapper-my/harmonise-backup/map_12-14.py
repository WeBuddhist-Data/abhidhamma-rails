"""Pāli→Burmese keyword mapping for pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»), chapters 12-jhanavibhango,
13-appamannavibhango, 14-sikkhapadavibhango. A copy of the approved sample's map_all.py (tables, compose rules, context
functions, verifier); writes only these three chapters and map-table-12-14.md. Working aid: --todo ID … (Pāli, Burmese
and the keywords still without a value).

usage (python3 -I -X utf8, from any directory):
  map_12-14.py           writes <ch>.mapped.md for every chapter in CHAPTERS and map-table-12-14.md, then verifies them
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


def f_pahana(kw, pali, my):
    """pahānā: the verbal noun «ပယ်ခြင်း» (pi-1) where the text has it; the causal clause «ပယ်ပြီးသောကြောင့်» of the
    bhikkhu glosses (^2-510) = «ပယ်ပြီးသော» (ablative ကြောင့် dropped, as pi-1 vūpasamā)."""
    return "ပယ်ခြင်း" if "ပယ်ခြင်း" in my else "ပယ်ပြီးသော"


def f_ayatanam(kw, pali, my):
    """āyatanaṃ: the sense base «အာရုံခံ နယ်ပယ်» (pi-1) in manāyatanaṃ (the citta list); the jhāna sphere
    (ākāsānañcāyatana …) = «နယ်ပယ်» elsewhere in these chapters (one sense per segment)."""
    return "အာရုံခံ နယ်ပယ်" if "manāyatana" in pali else "နယ်ပယ်"


FUNCS = {"ajjhattam": f_ajjhattam, "rupa": f_rupa, "pahana": f_pahana, "ayatanam": f_ayatanam}
ALT = {}
CTX = {
    "2-510": {"sekkho": "ကျင့်ကြံဆဲသူ", "asekkho": "ကျင့်ကြံမှု ပြီးဆုံးသူ"},   # apposition «ကျင့်ကြံဆဲသူ ရဟန်း», no ၏
    "2-511": {"sampanno": "ပြည့်ဝသော"},                                    # the «endowed» list: ပြည့်ဝ၏
    "2-513": {"patta": "သစ်ရွက်"},                                          # pattadāna: a gift of leaves
    "2-514": {"bhajati": "ဆည်းကပ်သည်"},                                     # sevati bhajati payirupāsati
    "2-515": {"saṃvara": "စောင့်စည်းခြင်း"},                                # saṃvarakaraṇīyāni
    "2-516": {"vattati": "ကျင့်သည်"},
    "2-519": {"kappeti": "ပြုသည်"},
    "2-528": {"sevati": "ဆည်းကပ်သည်"},
    "2-673": {"ekaṃ disaṃ pharitvā": "အရပ် တစ်မျက်နှာကို … ပျံ့နှံ့စေ၍"},    # the question «… အဘယ်သို့ ပျံ့နှံ့စေ၍»
    "2-663": {"ekaṃ disaṃ pharitvā": "အရပ် တစ်မျက်နှာကို … ပျံ့နှံ့စေ၍"},    # the question «… အဘယ်သို့ ပျံ့နှံ့စေ၍»
    "2-653": {"ekaṃ disaṃ pharitvā": "အရပ် တစ်မျက်နှာကို … ပျံ့နှံ့စေ၍"},    # the question «… အဘယ်သို့ ပျံ့နှံ့စေ၍»
    "2-643": {"ekaṃ disaṃ pharitvā": "အရပ် တစ်မျက်နှာကို … ပျံ့နှံ့စေ၍"},    # the question «… အဘယ်သို့ ပျံ့နှံ့စေ၍»
    "2-536": {"kāyo": "ကိုယ်"},
    "2-552": {"yaṃ": NONE},                    # relative pronoun: the clause closes with ရှိသမျှ (agreed pi-1 rule)
    "2-640": {"appaṭighā": "ထိခိုက်မှုလည်း မရှိသော"},  # fragment of anidassanaappaṭighā («… လည်း မရှိသော»)
    "2-701": {"appaṭighā": "ထိခိုက်မှုလည်း မရှိသော"},
    "2-716": {"appaṭighā": "ထိခိုက်မှုလည်း မရှိသော"},                                             # ujuko hoti kāyo: the body
    "2-619": {"saññī": "မှတ်သိမှု ရှိသော"},                                 # fragment of nevasaññī                                      # bhajati sambhajati sevati …                                         # sīhaseyyaṃ kappeti                                       # samādāya vattati = ဆောက်တည်၍ ကျင့်၏
}

T_JHANA = {
    # --- headings
    "Jhāna": "ဈာန်",
    # --- ^2-508 the suttanta summary (the gradual training); every word as the text renders it
    "pahāya": "ပယ်၍", "pahāyā": "ပယ်၍",
    "Vicikicchaṃ pahāya": "ယုံမှားမှုကို ပယ်၍", "Vicikicchaṃ pahāyā": "ယုံမှားမှုကို ပယ်၍",
    "Thinamiddhaṃ pahāya": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှုကို ပယ်၍",
    "Thinamiddhaṃ pahāyā": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှုကို ပယ်၍",
    "Uddhaccakukkuccaṃ pahāya": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှုကို ပယ်၍",
    "Uddhaccakukkuccaṃ pahāyā": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှုကို ပယ်၍",
    "Vicikicchaṃ": "ယုံမှားမှု", "Thinamiddhaṃ": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု",
    "Uddhaccakukkuccaṃ": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု",
    "sampajānakārī": "ကောင်းစွာ ဆင်ခြင်သိမြင်လျက် ပြုလေ့ရှိသော",
    "sampajāna": "ကောင်းစွာ ဆင်ခြင်သိမြင်သော",
    "abhikkante": "ရှေ့သို့ တိုးရာ", "paṭikkante": "နောက်သို့ ဆုတ်ရာ",
    "ālokite": "ရှေ့သို့ ကြည့်ရာ", "vilokite": "ဘေးသို့ ကြည့်ရာ",
    "samiñjite": "ကွေးရာ", "pasārite": "ဆန့်ရာ",
    "saṅghāṭi": "ဒုကုဋ်", "patta": "သပိတ်", "cīvara": "သင်္ကန်း", "dhāraṇe": "ဆောင်ရာ",
    "asite": "စားရာ", "pīte": "သောက်ရာ", "khāyite": "ခဲရာ", "sāyite": "လျက်ရာ",
    "uccāra": "ကျင်ကြီး", "passāva": "ကျင်ငယ်",
    "gate": "သွားရာ", "ṭhite": "ရပ်ရာ", "nisinne": "ထိုင်ရာ", "sutte": "အိပ်ရာ", "jāgarite": "နိုးရာ",
    "bhāsite": "ပြောဆိုရာ", "tuṇhībhāve": "ဆိတ်ဆိတ်နေရာ", "tuṇhī": "ဆိတ်ဆိတ်",
    "abbhokāsaṃ": "လွင်တီးခေါင်", "araññaṃ": "တော", "rukkha": "သစ်ပင်", "mūlaṃ": "ရင်း",
    "pabbataṃ": "တောင်", "kandaraṃ": "ချောက်", "guhaṃ": "ဂူ", "susānaṃ": "သုသာန်",
    "vanapatthaṃ": "တောအုပ်ကြီး", "patthaṃ": "တောအုပ်ကြီး",          # the text renders vanapattha with one word
    "palāla": "ကောက်ရိုး", "puñjaṃ": "ပုံ",
    "nigghosaṃ": "ဆူညံသံ",                                          # fragment of appanigghosaṃ (rule 8)
    "vijanavātaṃ": "လူသူ ကင်းသော", "vātaṃ": NONE,                    # the text has no word for «wind»
    "rāhasseyyakaṃ": "လျှို့ဝှက်စွာ နေရာ ဖြစ်သော",
    "paṭisallāna": "တစ်ယောက်တည်း ကိန်းအောင်းရန်", "sāruppaṃ": "သင့်လျော်သော",
    "vivittaṃ": "ဆိတ်ငြိမ်သော", "senāsanaṃ": "အိပ်ရာ နေရာ", "vivittaṃ senāsanaṃ": "ဆိတ်ငြိမ်သော အိပ်ရာ နေရာ",
    "bhajati": "မှီဝဲသည်",
    "amanasikārā": "နှလုံး မသွင်းခြင်း",
    "bodhi": "ဗောဓိ", "pakkhikānaṃ": "ပက္ခိယ", "bodhipakkhikānaṃ": "ဗောဓိပက္ခိယ",
    "dhammānaṃ": "သဘောတရား", "bodhipakkhikānaṃ dhammānaṃ": "ဗောဓိပက္ခိယ သဘောတရား",
    "pāṇa": "သတ္တဝါ", "bhūta": NONE,          # pāṇabhūta = one word «သတ္တဝါ» (as caya where apacaya is one word)
    "hitānukampī": "အကျိုးကို စာနာသော", "ānukampī": "စာနာသော",
    "nepakkaṃ": "ပညာ ရင့်ကျက်ခြင်း", "sātaccaṃ": "အစဉ်တစိုက် ဖြစ်ခြင်း",
    "ācāra": "အကျင့်", "gocara": "ကျက်စားရာ", "sampanno": "ပြည့်စုံသော",
    "upakkilese": "အညစ်အကြေး", "nīvaraṇe": "အတားအဆီး",
    "abhijjhaṃ": "သူ့ဥစ္စာကို လိုချင်ခြင်း", "loke": "လောက",
    "vigatābhijjhena": "သူ့ဥစ္စာကို လိုချင်ခြင်း ကင်းသော", "cetasā": "စိတ်",
    "vigatābhijjhena cetasā": "သူ့ဥစ္စာကို လိုချင်ခြင်း ကင်းသော စိတ်",
    "tiṇṇa": "ကူးမြောက်သော", "padosaṃ": "အလွန် ဒေါသထွက်ခြင်း",
    "pallaṅkaṃ": "ထက်ဝယ်", "ābhujitvā": "ဖွဲ့ခွေ၍", "ujuṃ": "ဖြောင့်မတ်စွာ", "parimukhaṃ": "ရှေ့မှောက်",
    "satiṃ": "သတိ", "upaṭṭhapetvā": "ထင်စေ၍", "nisīdati": "ထိုင်သည်",
    "bhaya": "ဘေး", "dassāvī": "မြင်လေ့ရှိသော",
    "aṇumattesu": "အနည်းငယ်မျှသော", "vajjesu": "အပြစ်", "aṇumattesu vajjesu": "အနည်းငယ်မျှသော အပြစ်",
    "anuyutto": "အားထုတ်သော", "jāgariyānuyogamanuyutto": "နိုးကြားမှုကို အားထုတ်သော",
    "pubbarattāpararattaṃ": "ညဉ့်ဦးယံ ညဉ့်နောက်ယံ",
    "dvāro": "တံခါး", "pātimokkha": "ပါတိမောက်", "saṃvara": "စောင့်စည်းမှု", "saṃvuto": "စောင့်စည်းသော",
    "sikkhā": "သိက္ခာ", "padesu": "ပုဒ်", "sikkhati": "ကျင့်သည်", "samādāya": "ဆောက်တည်၍",
    "mattaññū": "အတိုင်းအရှည်ကို သိသော", "bhojane mattaññū": "အစားအစာ၌ အတိုင်းအရှည်ကို သိသော",
    "sukhavihārī": "သာယာစွာ နေသော",
    "suññāgāragato": "ဆိတ်ငြိမ်ရာ အိမ်သို့ ရောက်သော", "gato": "ရောက်သော", "āgāra": "အိမ်",
    "āloka": "အလင်း", "saññī": "မှတ်သိသော",
    "anuddhato": "မယောက်ယက်ခတ်သော", "vūpasanta": "ကောင်းစွာ ငြိမ်သက်သော",
    "akathaṃkathī": "‘အဘယ်သို့နည်း’ဟု မတွေးတောသော",
    "dubbalīkaraṇe": "အားနည်းစေတတ်သော", "paññāya": "ပညာ",
    "parisodheti": "အကြွင်းမဲ့ သန့်စင်စေသည်", "cittaṃ parisodheti": "စိတ်ကို အကြွင်းမဲ့ သန့်စင်စေသည်",
    "viveka": "ကင်းဆိတ်ခြင်း", "pītisukhaṃ": "ပီတိနှင့် သာယာမှု",
    "vitakkavicārānaṃ": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု",
    "vitakkavicārānaṃ vūpasamā": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်း",
    "rūpasaññānaṃ": "ရုပ်ဟု မှတ်သိမှု", "paṭighasaññānaṃ": "ထိခိုက်မှုဟု မှတ်သိမှု", "paṭigha": "ထိခိုက်မှု",
    "nānattasaññānaṃ": "အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှု",
    "ananto": "အဆုံး မရှိသော", "ākāso": "ဟင်းလင်းပြင်", "natthi kiñcī": "ဘာမျှ မရှိသည်",
    "ākāsānañcāyatanaṃ": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်",
    "ākiñcaññāyatanaṃ": "ဘာမျှ မရှိသော နယ်ပယ်",
    "nevasaññānāsaññāyatanaṃ": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်",
    "āyatanaṃ": "@ayatanam",
    "dhammā kusalā": "သဘောတရား … ကုသိုလ်",   # «Ime dhammā kusalā» = «ဤသဘောတရားများသည် ကုသိုလ် ဖြစ်ကြသည်»
    "samāpattiyā": "ရောက်ရှိရန်",             # kusalānaṃ dhammānaṃ samāpattiyā (dative, sample N7)
    # --- ^2-509 «idha»
    "Tena": "ထို့ကြောင့်", "diṭṭhiyā": "အယူ", "khantiyā": "လက်ခံမှု", "ruciyā": "နှစ်သက်မှု",
    "ādāye": "ယူဆောင်ထားမှု", "dhamme": "တရား", "vinaye": "ဝိနည်း", "dhammavinaye": "တရားနှင့် ဝိနည်း",
    "pāvacane": "ဒေသနာတော်", "brahmacariye": "မြင့်မြတ်သော အကျင့်", "cariye": "အကျင့်",
    "satthu": "ဆရာ", "sāsane": "အဆုံးအမ",
    # --- ^2-510 «bhikkhu»
    "samaññāya": "အမည်", "paṭiññāya": "ဝန်ခံခြင်း", "bhikkhatīti": "တောင်းခံသည်", "bhikkhakoti": "တောင်းခံသူ",
    "bhikkhā": "ဆွမ်းခံ", "cariyaṃ": "ကျင့်ဝတ်", "bhinna": "ကွဲပြဲသော", "paṭa": "အဝတ်", "dharoti": "ဆောင်သူ",
    "bhindati": "ဖြိုခွဲသည်", "bhinnattā": "ကွဲပြီးသော", "odhiso": "အပိုင်းအခြားဖြင့်",
    "anodhiso": "အပိုင်းအခြား မရှိ", "kilesānaṃ": "ကိလေသာ", "pahānā": "@pahana",
    "aggo": "အမြတ်ဆုံး", "bhadro": "ကောင်းမြတ်သော", "sāro": "အနှစ်သာရ",
    "saṅghena": "သံဃာ", "samaggena saṅghena": "ညီညွတ်သော သံဃာ", "ñatti": "ဉတ်",
    "ñatticatutthena": "ဉတ်လေးကြိမ်မြောက်", "kammena": "ကံ", "akuppena": "မပျက်စီးသော",
    "ṭhānārahena": "အကြောင်းနှင့် လျော်သော", "ārahena": "လျော်သော", "upasampanno": "ပဉ္စင်းခံပြီးသော",
    # --- ^2-511 «pātimokkha», ^2-513 ācāra
    "sīlaṃ": "သီလ", "patiṭṭhā": "တည်ရာ", "ādi": "အစ", "caraṇaṃ": "အကျင့်", "saṃyamo": "ထိန်းချုပ်မှု",
    "mokkhaṃ": "မျက်နှာ", "pāmokkhaṃ": "အထွတ်အထိပ်",
    "Kāyiko": "ကိုယ်ပိုင်းဆိုင်ရာ", "kāyiko": "ကိုယ်ပိုင်းဆိုင်ရာ", "vācasiko": "နှုတ်ပိုင်းဆိုင်ရာ",
    "Kāyiko avītikkamo": "ကိုယ်ပိုင်းဆိုင်ရာ မကျူးလွန်ခြင်း", "Kāyiko vītikkamo": "ကိုယ်ပိုင်းဆိုင်ရာ ကျူးလွန်ခြင်း",
    "Saṃvutoti": "စောင့်စည်းသော",
    "upeto": "ပြည့်စုံသော", "samupeto": "ကောင်းစွာ ပြည့်စုံသော", "upāgato": "ရောက်ရှိသော",
    "samupāgato": "ကောင်းစွာ ရောက်ရှိသော", "upapanno": "ရရှိသော", "samannāgato": "အညီအညွတ် ပြည့်စုံသော",
    "Viharatī": "နေသည်", "viharatī": "နေသည်",
    "iriyati": "ဣရိယာပုထ်ကို ပြုသည်", "vattati": "လည်ပတ်သည်", "pāleti": "စောင့်ရှောက်သည်",
    "yapeti": "မျှတသည်", "yāpeti": "မျှတစေသည်", "carati": "ကျင့်လည်သည်",
    "ācāro": "အကျင့်", "anācāro": "မသင့်တော်သော အကျင့်", "dussīlyaṃ": "သီလ ပျက်ခြင်း",
    "veḷu": "ဝါး", "dānena": "ပေးခြင်း", "phala": "သစ်သီး", "sināna": "ရေချိုးမှုန့်", "dantakaṭṭha": "ဒန်ပူ",
    "cāṭukamyatāya": "ချော့မော့ ပြောဆိုခြင်း",
    "muggasūpyatāya": "ပဲဟင်းကဲ့သို့ အမှန်အမှား ရောနှော ပြောဆိုခြင်း",
    "pāribhaṭayatāya": "ကလေးထိန်းကဲ့သို့ ပြုစုခြင်း", "jaṅgha": "ခြေလျင်", "pesanikena": "စေခိုင်းမှုကို ခံခြင်း",
    "buddha": "မြတ်စွာဘုရား", "paṭikuṭṭhena": "ကဲ့ရဲ့တော်မူအပ်သော", "ājīvena": "အသက်မွေးမှု",
    "jīvikaṃ": "အသက်", "kappeti": "မွေးသည်",
    # --- ^2-514 gocara
    "gocaro": "ကျက်စားရာ", "agocaro": "မကျက်စားသင့်ရာ", "gocarena": "ကျက်စားရာ", "ācārena": "အကျင့်",
    "vesiyā": "ပြည့်တန်ဆာ", "vidhavā": "ခင်ပွန်း သေဆုံးသူ", "kumāri": "အပျို", "thulla": "ကြီး",
    "paṇḍaka": "ပဏ္ဍုက်", "pānāgāra": "သေရည်ဆိုင်", "saṃsaṭṭho": "ရောနှောသော",
    "rāja": "ဘုရင်", "rājūhi": "ဘုရင်", "mahāmattehi": "အမတ်ကြီး", "titthiyehi": "အယူဝါဒ ခြားနားသူ",
    "sāvakehi": "တပည့်", "ananulomikena": "လျော်ညီမှု မရှိသော",
    "kulāni": "အမျိုး", "saddhāni": "ယုံကြည်မှု ရှိသော", "bhūtāni": "ဖြစ်သော",
    "akkosaka": "ဆဲရေး", "paribhāsakāni": "ပုတ်ခတ်တတ်သော", "kāmāni": "လိုလားသော",
    "anattha": "အကျိုး မရှိခြင်း", "ahita": "စီးပွား မဖြစ်ခြင်း", "phāsuka": "ချမ်းသာ",
    "aphāsuka": "ချမ်းသာ မရှိခြင်း", "khema": "ဘေးကင်းရာ", "yoga": NONE,   # yogakkhema = one word ဘေးကင်းရာ
    "kāsāva": "ဖန်ရည်စွန်း သင်္ကန်း", "pajjotāni": "ထိန်လင်းသော", "isi": "ရသေ့",
    "paṭivātāni": "လေ တိုက်ခတ်ရာ ဖြစ်သော",
    "bhikkhūnaṃ": "ရဟန်း", "bhikkhunīnaṃ": "ဘိက္ခုနီ", "upāsakānaṃ": "ဥပါသကာ", "upāsikānaṃ": "ဥပါသိကာ",
    "sevati": "မှီဝဲသည်", "payirupāsati": "ချဉ်းကပ် ခစားသည်",
    # --- ^2-515 aṇumatta vajja
    "tattha": "ထိုတို့အနက်",
    "appamattakāni": "အလွန် နည်းသော", "oramattakāni": "အနည်းငယ်မျှ ဖြစ်သော", "lahusāni": "ပေါ့သော",
    "sammatāni": "သတ်မှတ်ထားသော", "karaṇīyāni": "ပြုပြင်ရမည့်", "saṃyama": "ထိန်းချုပ်ခြင်း",
    "cittuppādakaraṇīyāni": "စိတ် ဖြစ်ပေါ်ခြင်းဖြင့် ပြုပြင်ရမည့်", "paṭibaddhāni": "ဆက်စပ်သော",
    "vajja": "အပြစ်", "ādīnava": "အပြစ်ဒဏ်", "nissaraṇa": "ထွက်မြောက်ရာ",
    # --- ^2-516 sikkhā
    "sabbena sabbaṃ": "အားလုံးကို အားလုံးဖြင့်", "sabbathā": "အလုံးစုံဖြင့်", "asesaṃ": "အကြွင်းအကျန် မရှိ",
    "nissesaṃ": "အကုန်အစင်", "padesū": "ပုဒ်", "sikkhāyo": "သိက္ခာ",
    # --- ^2-517 guttadvāra
    "abhijjhādomanassā": "သူ့ဥစ္စာကို လိုချင်ခြင်း စိတ်ဆင်းရဲမှု", "domanassā": "စိတ်ဆင်းရဲမှု",
    "cakkhundriyaṃ asaṃvutaṃ": "မျက်စိ၏ စွမ်းရည်ကို မစောင့်စည်းသော",
    "manindriyaṃ asaṃvutaṃ": "မနော၏ စွမ်းရည်ကို မစောင့်စည်းသော",
    "gutti": "စောင့်ထိန်းခြင်း", "guttadvāratā": "တံခါးကို စောင့်ထိန်းခြင်း",
    "saṃvaraṃ āpajjati": "စောင့်စည်းမှု ပြုသည်",
    # --- ^2-518 bhojane mattaññutā (datives keep «ရန်», sample N7)
    "vihiṃsūparatiyā": "ညှဉ်းပန်းမှု ငြိမ်းရန်", "brahmacariyānuggahāya": "မြင့်မြတ်သော အကျင့်ကို ထောက်ပံ့ရန်",
    "ānuggahāya": "ထောက်ပံ့ရန်", "asantuṭṭhitā": "ရောင့်ရဲမှု မရှိခြင်း",
    "bhojane mattaññutā": "အစားအစာ၌ အတိုင်းအရှည်ကို သိခြင်း", "iti": "ဤသို့",
    # --- ^2-519 jāgariyānuyoga
    "caṅkamena": "စင်္ကြံ လျှောက်ခြင်း", "nisajjāya": "ထိုင်ခြင်း", "dhammehi": "သဘောတရား",
    "āvaraṇīyehi": "ပိတ်ပင်တတ်သော", "āvaraṇīyehi dhammehi": "ပိတ်ပင်တတ်သော သဘောတရား",
    "āvaraṇīyehi dhammehi cittaṃ": "ပိတ်ပင်တတ်သော သဘောတရားတို့မှ စိတ်",
    "rattiyā": "ညဉ့်", "majjhima": "သန်းခေါင်", "yāmaṃ": "ယံ",          # X-yāma = one word «…ယံ»
    "dakkhiṇena": "ညာဘက်", "passena": "နံပါး", "sīha": "ခြင်္သေ့", "seyyaṃ": "အိပ်ခြင်း",
    "pāde": "ခြေတစ်ဖက်", "accādhāya": "ထပ်၍", "manasikaritvā": "နှလုံးသွင်း၍", "paccuṭṭhāya": "ထ၍",
    # --- ^2-520 … ^2-522
    "vīriyārambho": "ဝီရိယ စတင်ခြင်း", "Nepakka": "ပညာ ရင့်ကျက်ခြင်း",
    "bojjhaṅgā": "ဗောဇ္ဈင်", "aṅgo": NONE, "aṅgā": NONE,       # sambojjhaṅga = one word ဗောဇ္ဈင် (pi-1 aṅgo)
    "satisambojjhaṅgo": "သတိ ဗောဇ္ဈင်", "dhammavicayasambojjhaṅgo": "သဘောတရားများကို စိစစ်ခြင်း ဗောဇ္ဈင်",
    "pītisambojjhaṅgo": "ပီတိ ဗောဇ္ဈင်", "passaddhisambojjhaṅgo": "ငြိမ်းအေးခြင်း ဗောဇ္ဈင်",
    "upekkhāsambojjhaṅgo": "ဥပေက္ခာ ဗောဇ္ဈင်", "vicaya": "စိစစ်ခြင်း", "dhammavicaya": "သဘောတရားများကို စိစစ်ခြင်း",
    "āsevati": "မှီဝဲသည်", "bahulīkaroti": "အဖန်ဖန် ပြုသည်",
    # --- ^2-523 … ^2-530
    "sato sampajānakārī": "သတိ ရှိလျက် ကောင်းစွာ ဆင်ခြင်သိမြင်လျက် ပြုလေ့ရှိသော",
    "abhikkamati": "ရှေ့သို့ တိုးသည်", "paṭikkamati": "နောက်သို့ ဆုတ်သည်", "āloketi": "ရှေ့သို့ ကြည့်သည်",
    "viloketi": "ဘေးသို့ ကြည့်သည်", "samiñjeti": "ကွေးသည်", "pasāreti": "ဆန့်သည်",
    "apilāpanatā": "အပေါ်ယံ မပေါ်လောခြင်း", "asammusanatā": "မမေ့လျော့ခြင်း",
    "bhūrī": "ကျယ်ပြန့်သော", "satiyā": "သတိ",
    "santike": "အနီး", "Dūre": "အဝေး", "anākiṇṇaṃ": "မပြည့်ကျပ်သော", "gahaṭṭhehi": "လူဝတ်ကြောင်",
    "pabbajitehi": "ရဟန်းအဖြစ် ထွက်သူ",
    "mañcopi": "ညောင်စောင်း", "pīṭhampi": "ခုံ", "bhisipi": "မွေ့ရာ", "bibbohanampi": "ခေါင်းအုံး",
    "vihāropi": "ကျောင်း", "aḍḍhayogopi": "တစ်ခြမ်းမိုး ကျောင်း", "pāsādopi": "ပြာသာဒ်", "aṭṭopi": "ရဲတိုက်",
    "māḷopi": "ဝန်းဝိုင်း အဆောင်", "leṇampi": "လှိုဏ်ဂူ", "guhāpi": "ဂူ", "mūlampi": "ရင်း", "gumbopi": "ရုံ",
    "bhikkhū": "ရဟန်း", "paṭikkamanti": "ဆုတ်နားသည်", "Yattha vā pana": "သို့မဟုတ် … မည်သည့်နေရာမဆို",
    "sambhajati": "ကောင်းစွာ မှီဝဲသည်", "nisevati": "အမြဲ ဆည်းကပ်သည်", "saṃsevati": "ကောင်းစွာ ဆည်းကပ်သည်",
    "nikkhamitvā": "ထွက်ပြီး", "bahi": "အပြင်", "indakhīlā": "မြို့တံခါး တိုင်ကြီး",
    "pabbato": "တောင်", "kandarā": "ချောက်", "guhā": "ဂူ", "abbhokāso": "လွင်တီးခေါင်", "puñjo": "ပုံ",
    # --- ^2-531 vanapattha («…ametaṃ» = «ဤသည်မှာ …»: etaṃ is part of the keyword)
    "Vanapattha": "တောအုပ်ကြီး", "pattha": "တောအုပ်ကြီး",
    "adhivacanaṃ": "အမည်", "senāsanānaṃ": "အိပ်ရာ နေရာ", "senāsanānaṃ adhivacanaṃ": "အိပ်ရာ နေရာတို့၏ အမည်",
    "dūrānametaṃ": "ဤသည်မှာ ဝေးကွာသော", "dūrānametaṃ senāsanānaṃ": "ဤသည်မှာ ဝေးကွာသော အိပ်ရာ နေရာ",
    "vanasaṇḍānametaṃ": "ဤသည်မှာ တောအုပ်တို့ဖြင့် ဖုံးလွှမ်းသော",
    "bhīsanakānametaṃ": "ဤသည်မှာ ကြောက်မက်ဖွယ်ကောင်းသော",
    "salomahaṃsānametaṃ": "ဤသည်မှာ ကြက်သီး ထဖွယ်ကောင်းသော",
    "salomahaṃsānametaṃ senāsanānaṃ": "ဤသည်မှာ ကြက်သီး ထဖွယ်ကောင်းသော အိပ်ရာ နေရာ",
    "pariyantānametaṃ": "ဤသည်မှာ အစွန်အဖျား၌ ရှိသော",
    "pariyantānametaṃ senāsanānaṃ": "ဤသည်မှာ အစွန်အဖျား၌ ရှိသော အိပ်ရာ နေရာ",
    "manussūpacārānametaṃ": "ဤသည်မှာ လူတို့ ကျက်စားရာ",     # without its na (rule 8)
    "ūpacārānametaṃ": "ဤသည်မှာ … ကျက်စားရာ",
    "durabhisambhavānametaṃ": "ဤသည်မှာ ရောက်ရန် ခဲယဉ်းသော",
    "durabhisambhavānametaṃ senāsanānaṃ": "ဤသည်မှာ ရောက်ရန် ခဲယဉ်းသော အိပ်ရာ နေရာ",
    # --- ^2-534 … ^2-537
    "mūla": "ရင်း", "arañña": "တော", "nisinno": "ထိုင်နေသော",
    "ujuko": "ဖြောင့်မတ်သော", "ṭhito": "တည်ငြိမ်သော", "paṇihito": "ကောင်းစွာ ထားအပ်သော",
    "nāsikagge": "နှာသီးဖျား", "agge": "ဖျား", "mukha": "နှုတ်ခမ်းအထက်", "nimitte": "အမှတ်",
    # --- ^2-538 the «calmed» list (predicated participles: «…သွားသည်» -> «…သွားသော», rule 3)
    "santā": "ငြိမ်သက်သွားသော", "samitā": "ငြိမ်းသွားသော", "vūpasantā": "ကောင်းစွာ ငြိမ်သက်သွားသော",
    "atthaṅgatā": "ကွယ်ပျောက်သွားသော", "abbhatthaṅgatā": "လုံးဝ ကွယ်ပျောက်သွားသော",
    "appitā": "ဆုံးခန်းတိုင်သွားသော", "byappitā": "လုံးဝ ဆုံးခန်းတိုင်သွားသော",
    "sositā": "ခြောက်ခန်းသွားသော", "visositā": "လုံးဝ ခြောက်ခန်းသွားသော", "byantīkatā": "အဆုံးသတ်သွားသော",
    # --- ^2-539 … ^2-547 the hindrances
    "ābhijjhena": "သူ့ဥစ္စာကို လိုချင်ခြင်း", "abhijjhāya": "သူ့ဥစ္စာကို လိုချင်ခြင်း",
    "sodheti": "သန့်စင်စေသည်", "visodheti": "အထူး သန့်စင်စေသည်", "parisodhetī": "အကြွင်းမဲ့ သန့်စင်စေသည်",
    "cittaṃ parisodhetī": "စိတ်ကို အကြွင်းမဲ့ သန့်စင်စေသည်",
    "moceti": "လွတ်စေသည်", "vimoceti": "အထူး လွတ်စေသည်", "parimoceti": "အကြွင်းမဲ့ လွတ်စေသည်",
    "byāpajjanā": "ဖောက်ပြန်နေခြင်း", "kujjhitattaṃ": "အမျက်ဒေါသ ထွက်ထားသော အဖြစ်",
    "abyāpannaṃ": "ဖျက်ဆီးလိုစိတ် မရှိသော", "Abyāpannacitto": "ဖျက်ဆီးလိုစိတ် မရှိသော စိတ် ရှိသော",
    "akalyatā": "မကျန်းမာခြင်း", "līyitattaṃ": "အားပျော့ထားသော အဖြစ်",
    "pariyonāho": "အပြည့် ပိတ်ဖုံးခံရခြင်း", "anto": "အတွင်း", "samorodho": "ပိတ်ဆို့ခံရခြင်း",
    "suppaṃ": "အိပ်ငိုက်ခြင်း", "suppanā": "အိပ်ပျော်ခြင်း",
    "thinamiddhassa": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု", "middhassa": "ငိုက်မျဉ်းမှု", "Vigata": "ကင်းသော",
    "vantattā": "အန်ထုတ်ပြီးသော", "muttattā": "လွှတ်ပြီးသော", "pahīnattā": "ပယ်ပြီးသော",
    "paṭinissaṭṭhattā": "ပြန်လည် စွန့်လွှတ်ပြီးသော",
    # --- ^2-549 … ^2-559
    "ālokā": "အလင်း", "parisuddhā": "စင်ကြယ်သော", "pariyodātā": "ဖြူစင်သော",
    "thinamiddhā": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု",
    "Akappiye": "မအပ်စပ်သည်", "vajje": "အပြစ်ရှိသည်",   # as pi-1 kappiye / avajje
    "vilekhā": "ခြစ်ကုတ်ခြင်း",
    "cetaso vikkhepo": "စိတ်၏ ပျံ့လွင့်ခြင်း", "kukkuccassa": "နောင်တ ပူပန်မှု",
    "uddhaccakukkuccassa": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု",
    "uddhaccakukkuccā": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု",
    "Vūpasantacitto": "ကောင်းစွာ ငြိမ်သက်သော စိတ် ရှိသော", "samitaṃ": "ငြိမ်းသော",
    "vūpasantaṃ": "ကောင်းစွာ ငြိမ်သက်သော",
    "dvidhāpatho": "လမ်း နှစ်ခွ", "apariyogāhaṇā": "နက်နက်နဲနဲ မသက်ဝင်နိုင်ခြင်း",
    "chambhitattaṃ": "တောင့်တင်းနေသော အဖြစ်",              # = pi-1 thambhitattaṃ
    "anekaṃsa": "တစ်ထစ်ချ မယူနိုင်ခြင်း",                   # = pi-1 anekaṃsaggāho (the text's negative)
    "tiṇṇo": "ကူးမြောက်သော", "nittiṇṇo": "လုံးဝ ကူးမြောက်သော", "pāra": "တစ်ဖက်ကမ်း",
    "vicikicchāya": "ယုံမှားမှု", "dhammesu": "သဘောတရား", "vicikicchati": "ယုံမှားသည်",
    "nikkathaṃkathī": "တွေးတောမှု ကင်းသော", "vikathaṃkatho": "တွေးတောမှု ပြတ်သော",
    # --- ^2-563 … ^2-568 the first jhāna
    "nirujjhati": "ချုပ်ပျောက်သည်", "nīvaraṇehi": "အတားအဆီး",
    "chandarāgo": "ဆန္ဒရာဂ", "saṅkapparāgo": "ကြံစည်မှု ရာဂ", "kāmo": "ကာမ",
    "anusandhanatā": "အာရုံနှင့် ဆက်စပ်ထားခြင်း", "upavicāro": "အနီးကပ် သုံးသပ်ခြင်း",
    "viveke": "ကင်းဆိတ်ခြင်း", "jātā": "မွေးဖွားသော", "sañjātā": "ကောင်းစွာ မွေးဖွားသော",
    "nibbattā": "ပေါ်ထွက်သော", "pātubhūtā": "ထင်ရှားလာသော",
    "Pītisukha": "ပီတိနှင့် သာယာမှု", "sahajātaṃ": "အတူ ဖြစ်ပေါ်သော", "saṃsaṭṭhaṃ": "ရောနှောသော",
    "cetosamphassa": "စိတ်၏ တွေ့ထိမှု", "sātaṃ sukhaṃ": "နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော",
    "sātaṃ sukhaṃ vedayitaṃ": "နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော ခံစားရခြင်း",
    "sātā sukhā vedanā": "နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော ခံစားမှု",
    "gaṇanānupubbatā": "ရေတွက်ခြင်း၏ အစဉ်", "ānupubbatā": "အစဉ်", "samāpajjatīti": "ဝင်စားသည်",
    # --- ^2-570 … ^2-577
    "lābho": "ရခြင်း", "paṭilābho": "ပြန်လည် ရခြင်း", "patti": "ရောက်ခြင်း", "sampatti": "ကောင်းစွာ ရောက်ခြင်း",
    "phusanā": "ထိတွေ့ခြင်း", "sacchikiriyā": "မျက်မှောက် ပြုခြင်း", "upasampadā": "ဝင်စားခြင်း",
    "Upasampajjā": "ဝင်စား၍", "Ajjhatta": "မိမိ၌", "Sampasādana": "ကြည်လင်မှု",
    "ekodibhāva": "စုစည်း တည်ငြိမ်စေသော", "anucāro": "လိုက်၍ သုံးသပ်ခြင်း",
    "samādhimhi": "သမာဓိ", "sampasādo": "ကြည်လင်မှု",
    # --- ^2-584 … ^2-589 the third jhāna
    "upekkhanā": "တည်ငြိမ်စွာ ရှုခြင်း", "ajjhupekkhanā": "အလွန် တည်ငြိမ်စွာ ရှုခြင်း",
    "majjhattatā": "အလယ်၌ တည်ခြင်း",
    "kāyo": "စိတ်၏ အဖော်တို့",                 # the mental body (pi-1 kāyena «စိတ်၏ အဖော်တို့»)
    "paṭisaṃvedetī": "ခံစားသည်",
    "buddhā": "ဘုရားရှင်", "sāvakā": "တပည့်သာဝက", "desenti": "ဟောသည်", "paññapenti": "သိစေသည်",
    "paṭṭhapenti": "ထူထောင်သည်", "vivaranti": "ဖွင့်လှစ်သည်", "vibhajanti": "ခွဲခြားပြသည်",
    "uttāniṃ": "ပေါ်လွင်အောင်", "pakāsenti": "ထင်ရှားစေသည်", "satimā": "သတိ ရှိသော",
    # --- ^2-594 … ^2-602 the fourth jhāna, the formless
    "dukkhaṃ vedayitaṃ": "နာကျင်သော ခံစားရခြင်း",
    "asātaṃ dukkhaṃ": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော",
    "asātaṃ dukkhaṃ vedayitaṃ": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားရခြင်း",
    "asātā dukkhā vedanā": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားမှု",
    "domanassaṃ": "စိတ်ဆင်းရဲမှု", "somanassaṃ": "ဝမ်းမြောက်မှု",
    "cetasikaṃ asātaṃ": "စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ် မကောင်းမှု",
    "nāsātaṃ": "နှစ်သက်ဖွယ် မကောင်းသည်လည်း မဟုတ်သော",
    "vivaṭā": "ပွင့်လင်းသော", "pārisuddhi": "စင်ကြယ်သော",
    "samāpattiṃ": "ဈာန်", "sukhavihārissa": "သာယာစွာ နေထိုင်သော",
    "atikkanto": "ကျော်လွန်သော", "vītikkanto": "လွန်မြောက်သော", "samatikkanto": "ကောင်းစွာ ကျော်လွန်သော",
    # --- ^2-603 … ^2-611
    "vuccanti paṭighasaññāyo": "ထိခိုက်မှုဟု မှတ်သိမှုတို့ဟု ခေါ်သည်",
    "Asamāpannassa": "ဈာန် မဝင်စားသော", "samāpannassa": "ဝင်စားသော", "manasi karoti": "နှလုံး သွင်းသည်",
    "Ananto": "အဆုံး မရှိသော", "Anantaṃ": "အဆုံး မရှိသော",
    "pharati": "ပျံ့နှံ့စေသည်", "ṭhapeti": "ထားသည်", "saṇṭhapeti": "ကောင်းစွာ ထားသည်",
    "āyatanassa": "နယ်ပယ်", "ākāsānañcāyatanassa": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်",
    "samatikkammā": "ကျော်လွန်၍", "ākāsaṃ": "ဟင်းလင်းပြင်", "phuṭṭhaṃ": "ပျံ့နှံ့သော",
    # --- ^2-612 … ^2-621
    "viññāṇañcāyatanassa": "အဆုံး မရှိသော သိစိတ် နယ်ပယ်", "ākiñcaññāyatanassa": "ဘာမျှ မရှိသော နယ်ပယ်",
    "nevasaññānāsaññāyatanassa": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်",
    "Natthi kiñcī": "ဘာမျှ မရှိသည်", "vibhāveti": "ပျောက်ကွယ်စေသည်",
    "santato": "ငြိမ်သက်သည်ဟု",
    "saṅkhārāvasesasamāpattiṃ": "ပြုပြင်ဖန်တီးမှု အကြွင်းအကျန်သာ ရှိသော ဈာန်", "āvasesa": "အကြွင်းအကျန်",
    "Nevasaññīnāsaññī": "မှတ်သိမှု ရှိသူလည်း မဟုတ် မှတ်သိမှု မရှိသူလည်း မဟုတ်သော",
    "nāsaññī": "မှတ်သိမှု မရှိသူလည်း မဟုတ်သော",
    # --- abhidhamma part: the jhāna openings (pi-1 upapattiyā = ဖြစ်ပေါ်ရန်)
    "ūpapattiyā": "ဖြစ်ပေါ်ရန်", "ūpapattiyā maggaṃ": "ဖြစ်ပေါ်ရန် လမ်း",
    "rūpūpapattiyā": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်ပေါ်ရန်",
    "rūpūpapattiyā maggaṃ": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်း",
    "arūpūpapattiyā": "ရုပ်မရှိသော ဘုံ၌ ဖြစ်ပေါ်ရန်",
    "arūpūpapattiyā maggaṃ": "ရုပ်မရှိသော ဘုံ၌ ဖြစ်ပေါ်ရန် လမ်း",
    "pathavīkasiṇaṃ": "မြေ ကသိုဏ်းကို အာရုံပြုသော",
    "pañcaṅgikaṃ jhānaṃ": "အင်္ဂါ ငါးပါး ရှိသော ဈာန်", "caturaṅgikaṃ jhānaṃ": "အင်္ဂါ လေးပါး ရှိသော ဈာန်",
    "tivaṅgikaṃ jhānaṃ": "အင်္ဂါ သုံးပါး ရှိသော ဈာန်",
    "nevasaññānāsaññāyatana": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်",
    "ābhiññaṃ": "ထူးကဲစွာ သိခြင်း", "apacayagāmiṃ": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "ကျင့်စဉ် ခက်ခဲသော ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    # --- headings, the pañhāpucchaka (ch12)
    "Rūpārūpāvacarakiriyā": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံတို့နှင့် ဆိုင်သော ပြုရုံမျှသာ ဖြစ်သော စိတ်",
    "ārūpāvacara": "ရုပ်မရှိသော ဘုံတို့နှင့် ဆိုင်သော",
    "sukhavihāraṃ": "သာယာစွာ နေထိုင်ရန် ဖြစ်သော",
    "nākusalaṃ": "အကုသိုလ်လည်း မဟုတ်သော", "neva kusalaṃ nākusalaṃ": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "arūpāvacaraṃ jhānaṃ": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော ဈာန်", "jhānānaṃ": "ဈာန်",
    "ācayagāmino": "စုပုံခြင်းဆီသို့ ဦးတည်သော", "apacayagāmino": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "etthuppannaṃ": "ယင်း၌ ဖြစ်ပေါ်ပြီးသော",
    "etthuppannaṃ upekkhaṃ": "ယင်း၌ ဖြစ်ပေါ်ပြီးသော ဥပေက္ခာ", "upekkhaṃ": "ဥပေက္ခာ",
    "etthuppannaṃ pītiṃ": "ယင်း၌ ဖြစ်ပေါ်ပြီးသော ပီတိ", "pītiṃ": "ပီတိ",
    "etthuppannaṃ sukhaṃ": "ယင်း၌ ဖြစ်ပေါ်ပြီးသော သာယာမှု",
    "etthuppannaṃ vicāraṃ": "ယင်း၌ ဖြစ်ပေါ်ပြီးသော ဆက်လက်သုံးသပ်မှု",
    "etthuppanne vitakkavicāre": "ယင်း၌ ဖြစ်ပေါ်ပြီးသော စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု",
    "vitakkavicāre": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု", "vicāre": "ဆက်လက်သုံးသပ်မှု",
    "sukhaṃ vedanaṃ": "သာယာသော ခံစားမှု",
    "nevavipākanavipākadhammadhammā": "ကံ၏ အကျိုးလည်း မဟုတ် အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော သဘောတရား",
    "Anidassanaappaṭighā": "မမြင်နိုင် ထိခိုက်မှုလည်း မရှိသော", "appaṭighā": "ထိခိုက်မှု မရှိသော",
    "lokuttarā": "လောကကို ကျော်လွန်သော", "araṇāti": "ပဋိပက္ခ မရှိသော",
}

T_APPAMANNA = {
    # --- headings, the four appamaññā (my2-zeroshot-terms: appamaññā = အပ္ပမညာ)
    "Appamaññā": "အပ္ပမညာ", "appamaññāyo": "အပ္ပမညာ", "appamaññānaṃ": "အပ္ပမညာ",
    "sahagatena": "အတူ ဖြစ်သော",
    "mettāsahagatena": "မေတ္တာနှင့်အတူ ဖြစ်သော", "karuṇāsahagatena": "ကရုဏာနှင့်အတူ ဖြစ်သော",
    "muditāsahagatena": "မုဒိတာနှင့်အတူ ဖြစ်သော", "upekkhāsahagatena": "ဥပေက္ခာနှင့်အတူ ဖြစ်သော",
    "mettāsahagatena cetasā": "မေတ္တာနှင့်အတူ ဖြစ်သော စိတ်",
    "karuṇāsahagatena cetasā": "ကရုဏာနှင့်အတူ ဖြစ်သော စိတ်",
    "muditāsahagatena cetasā": "မုဒိတာနှင့်အတူ ဖြစ်သော စိတ်",
    "upekkhāsahagatena cetasā": "ဥပေက္ခာနှင့်အတူ ဖြစ်သော စိတ်",
    "karuṇāsahagataṃ": "ကရုဏာနှင့်အတူ ဖြစ်သော", "muditāsahagataṃ": "မုဒိတာနှင့်အတူ ဖြစ်သော",
    "disaṃ": "အရပ်", "ekaṃ disaṃ pharitvā": "အရပ် တစ်မျက်နှာကို ပျံ့နှံ့စေ၍", "pharitvā": "ပျံ့နှံ့စေ၍",
    "pharitvā viharati": "ပျံ့နှံ့စေ၍ နေသည်", "tathā": "ထို့အတူ", "tathā catutthaṃ": "ထို့အတူ စတုတ္ထ",
    "tiriyaṃ": "ဖီလာ", "sabbadhi": "နေရာတိုင်း၌", "sabbattatāya": "ခပ်သိမ်းသော သဘော",
    "sabbāvantaṃ": "အားလုံး ပါဝင်သော", "sabbāvantaṃ lokaṃ": "အားလုံး ပါဝင်သော လောက",
    "sabbāvantaṃ loka": "အားလုံး ပါဝင်သော လောက",
    "vipulena": "ပြန့်ပြောသော", "mahaggatena": "ကြီးမြတ်သော", "appamāṇena": "အတိုင်းအဆ မရှိသော",
    "averena": "ရန်ငြိုး မရှိသော", "abyāpajjena": "ညှဉ်းဆဲလိုမှု မရှိသော",
    "vipulaṃ": "ပြန့်ပြောသော", "avero": "ရန်ငြိုး မရှိသော", "abyāpajjo": "ညှဉ်းဆဲလိုမှု မရှိသော",
    "puggalaṃ": "ပုဂ္ဂိုလ်", "piyaṃ": "ချစ်ရသော", "duggataṃ": "ဆင်းရဲ ဒုက္ခရောက်နေသော", "durūpetaṃ": "ကံဆိုးသော",
    "mettāyeyya": "မေတ္တာ ထားသည်", "karuṇāyeyya": "ကရုဏာ ထားသည်", "mudito": "မုဒိတာ ရှိသော",
    "sattesu": "သတ္တဝါ", "jātaṃ": "ဖြစ်ပေါ်သော",            # sahajātaṃ «အတူ ဖြစ်ပေါ်၏» (not the time list)
    "ceto": "စိတ်", "cetovimutti": "စိတ်လွတ်မြောက်မှု",
    "mettācetovimutti": "မေတ္တာဖြင့် စိတ်လွတ်မြောက်မှု", "mettāyitattaṃ": "မေတ္တာ ထားသော အဖြစ်",
    "karuṇāyanā": "ကရုဏာ ထားခြင်း", "karuṇāyitattaṃ": "ကရုဏာ ထားသော အဖြစ်",
    "karuṇācetovimutti": "ကရုဏာဖြင့် စိတ်လွတ်မြောက်မှု",
    "muditāyanā": "မုဒိတာ ထားခြင်း", "muditāyitattaṃ": "မုဒိတာ ထားသော အဖြစ်",
    "muditācetovimutti": "မုဒိတာဖြင့် စိတ်လွတ်မြောက်မှု",
    "upekkhāyanā": "ဥပေက္ခာ ထားခြင်း", "upekkhāyitattaṃ": "ဥပေက္ခာ ထားသော အဖြစ်",
    "upekkhācetovimutti": "ဥပေက္ခာဖြင့် စိတ်လွတ်မြောက်မှု",
    "puratthimaṃ": "အရှေ့", "dakkhiṇaṃ": "တောင်", "uttaraṃ": "မြောက်", "vidisaṃ": "အရပ်ကြား",
    "puratthimaṃ vā disaṃ": "အရှေ့ အရပ်", "pacchimaṃ vā disaṃ": "အနောက် အရပ်",
    "uttaraṃ vā disaṃ": "မြောက် အရပ်", "dakkhiṇaṃ vā disaṃ": "တောင် အရပ်", "catutthaṃ disaṃ": "စတုတ္ထ အရပ်",
    "adhimuccitvā": "စိတ်ကို ညွတ်စေ၍", "pharitvā adhimuccitvā": "ပျံ့နှံ့စေ၍ စိတ်ကို ညွတ်စေ၍",
    "Pariyādāya": "အကုန် သိမ်းကျုံး၍", "vacana": "စကား",
    "āvacarassa": "ဘုံနှင့် ဆိုင်သော", "ākusalaṃ": "အကုသိုလ်",     # fragment of nākusalaṃ (rule 8)
    "āsekkhā": "ကျင့်ကြံမှု ပြီးဆုံးသူ၏", "na hetu": "အမြစ် မဟုတ်သော",
}

T_SIKKHA = {
    # --- heading, the five precepts (the text's final forms; inside a phrase «…မှ» stays)
    "Sikkhāpada": "သိက္ခာပုဒ်", "pada": "ပုဒ်", "sikkhāpadaṃ": "သိက္ခာပုဒ်", "padaṃ": "ပုဒ်",
    "sikkhāpadāni": "သိက္ခာပုဒ်", "padāni": "ပုဒ်", "sikkhāpadānaṃ": "သိက္ခာပုဒ်", "padānaṃ": "ပုဒ်",
    "veramaṇī sikkhāpadaṃ": "ကင်းဝေးခြင်း သိက္ခာပုဒ်",
    "pāṇātipātā": "သူ့အသက်ကို သတ်ခြင်း", "ātipātā": "သတ်ခြင်း",
    "pāṇātipātā veramaṇī": "သူ့အသက်ကို သတ်ခြင်းမှ ကင်းဝေးခြင်း",
    "ādānā": "ယူခြင်း", "adinnādānā veramaṇī": "မပေးသည်ကို ယူခြင်းမှ ကင်းဝေးခြင်း",
    "micchācārā": "မှားယွင်းစွာ ကျင့်ခြင်း",
    "kāmesumicchācārā veramaṇī": "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းမှ ကင်းဝေးခြင်း",
    "musā": "မုသား", "vādā": "ပြောခြင်း", "musāvādā": "မုသား ပြောခြင်း",
    "musāvādā veramaṇī": "မုသား ပြောခြင်းမှ ကင်းဝေးခြင်း",
    "surā": "သေရည်", "meraya": "အရက်", "majja": "မူးယစ်ဖွယ်", "pamāda": "မေ့လျော့ခြင်း", "ṭṭhānā": "အကြောင်း",
    "surāmerayamajjapamādaṭṭhānā veramaṇī": "သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့ခြင်း၏ အကြောင်းမှ ကင်းဝေးခြင်း",
    "akiriyā": "မပြုခြင်း", "akaraṇaṃ": "မပြုလုပ်ခြင်း", "anajjhāpatti": "မကျူးလွန်ခြင်း",
    "anatikkamo": "မကျော်လွန်ခြင်း", "sañcetayitattaṃ": "စေ့ဆော်ထားသော အဖြစ်",
    "sasaṅkhārena": "တိုက်တွန်းမှုဖြင့်",          # the adverb «with prompting» keeps its instrumental
    "chandādhipateyyaṃ": "ဆန္ဒကို အကြီးအမှူးပြုသော",
    "vīmaṃsādhipateyyaṃ": "စုံစမ်းဆင်ခြင်မှုကို အကြီးအမှူးပြုသော",
    "kāmāvacare": "ကာမဘုံ", "āvacare": "ဘုံ",       # the slip kāmāvacare (for -raṃ): text «ကာမဘုံ၌»
    "rūpārammaṇaṃ": "အဆင်းအရောင်ကို အာရုံပြုသော", "yaṃ yaṃ vā panārabbha": "မည်သည့်အရာကို အာရုံပြု၍",
    "dhammā sikkhā": "သိက္ခာ ဖြစ်သော သဘောတရား", "Kusalāyeva": "ကုသိုလ် … သာ",
}

SECTIONS = {
    "12-jhanavibhango": T_JHANA,
    "13-appamannavibhango": T_APPAMANNA,
    "14-sikkhapadavibhango": T_SIKKHA,
    # the approved sample's tables (shared fallbacks, never written here)
    "preamble": T_PREAMBLE,
    "1-khandhavibhango": T_KHANDHA,
}
CHAPTERS = ["12-jhanavibhango", "13-appamannavibhango", "14-sikkhapadavibhango"]


# =====================================================================================================
# rules (written to map-table.md)
# =====================================================================================================
RULES = """## Rules

Binding and unchanged: the approved sample `map-table.md` (pi-1 rules 1–11, the agreed later pi-1 rules, N1–N11) and
its values; the sample's tables are copied into this script and used as fallbacks for the same keyword. The value is
the word or phrase of THAT segment's Burmese (the FINAL pi-2 text) that carries the keyword, in pi-1 dictionary form
(nouns without final particles and plural; adjectives / participles in «…သော»; verbs in «…သည်»; absolutives keep
«…၍»; datives keep «…ရန်»; « … » for gaps; «၊» dropped inside a value). Lookup order: CTX[segment] → this chapter's
table → the other chapters' tables (incl. the sample's) → the final pi-1 mapping (most frequent pi-1 value present in
the segment) → compose rules.

## NEW rules (for the user's review)

M1. **Presence check, more endings** (same normalisation as pi-1 rules 3 / 4, longer list): a chunk «Xသော» is accepted
    against the text's «Xလျက်» (participle «while …»: sato = သတိ ရှိသော, sampajāno, hitānukampī, tiṇṇa), «Xကုန်သော»
    (literary plural: dubbalīkaraṇe), «Xကြသည် / Xကြ၏ / X၏ / X။» (a participle predicated with a finite ending:
    sampayuttā in «… ယှဉ်တွဲကြသည်», upeto «ပြည့်စုံ၏», anākiṇṇaṃ «မပြည့်ကျပ်။») and «X”» (an adjective ending a
    quotation: Ananto «“ဟင်းလင်းပြင်သည် အဆုံး မရှိ”»); a chunk «Xသည်» against «Xရာ» (verb of a «where …» clause:
    paṭikkamanti «ဆုတ်နားရာ»), «X”» and «Xသနည်း» (question: viharati «… နေသနည်း»).
M2. **A value of another chapter's table that is not in THIS segment gives way to the pi-1 value that is** (pi-1 values
    are binding): sammā = pi-1 «မှန်ကန်သော» (not the preamble's «အပြည့်အဝ»); ajjhattaṃ (the jhāna adverb) = pi-1
    «မိမိ၌» (not the sample's list item, which stays where the text has it, ^2-573).
M3. **Predicated participles rendered by a finite verb** keep the attributive «…သော» (pi-1 rule 3, the sample's
    oḷārikā): the endowed list upeto … samannāgato «ပြည့်စုံ၏ …» = ပြည့်စုံသော …; the «calmed» list santā … byantīkatā
    «ငြိမ်သက်သွားသည် …» = ငြိမ်သက်သွားသော …; jātā honti … pātubhūtā «မွေးဖွားကြ၏ …» = မွေးဖွားသော …; atikkanto /
    vītikkanto / samatikkanto «ကျော်လွန်ပြီး ဖြစ်၏» = ကျော်လွန်သော (the conjunctive ပြီး normalised, rule 3).
M4. **Causal ablatives** rendered «…ပြီးသောကြောင့်» = «…ပြီးသော» (ကြောင့် dropped, as pi-1 vūpasamā): bhinnattā,
    vantattā, muttattā, pahīnattā, paṭinissaṭṭhattā; pahānā = ပယ်ပြီးသော in the bhikkhu glosses ^2-510 only
    (function f_pahana; pi-1 «ပယ်ခြင်း» wherever the text has it).
M5. **The situations of clear comprehension** abhikkante … tuṇhībhāve = «…ရာ» (ရာ kept as the noun ending, ၌ dropped):
    abhikkante = ရှေ့သို့ တိုးရာ, asite = စားရာ, gate = သွားရာ …
M6. **A compound the text renders with one word**: a member without a word of its own = (no direct equivalent), as pi-1
    caya / aṅgo: bhūta (pāṇabhūta = သတ္တဝါ), vātaṃ (vijanavāta = လူသူ ကင်းသော), yoga (yogakkhema = ဘေးကင်းရာ), aṅgo /
    aṅgā (sambojjhaṅga = ဗောဇ္ဈင်). A member that is a visible part of the one word keeps that part: guhaṃ = ဂူ
    (တောင်ဂူ), gumbopi = ရုံ (ဝါးရုံ), mūlaṃ = ရင်း (သစ်ပင်ရင်း), majjhima = သန်းခေါင် and yāmaṃ = ယံ (သန်းခေါင်ယံ),
    rattiyā = ညဉ့် (ညဉ့်ဦးယံ), thulla = ကြီး (အပျိုကြီး), agge = ဖျား (နှာသီးဖျား); vanapattha is one word
    «တောအုပ်ကြီး», so patthaṃ / pattha = တောအုပ်ကြီး.
M7. **«…ametaṃ» keywords** (dūrānametaṃ … durabhisambhavānametaṃ) include etaṃ = «ဤသည်မှာ …» (the text's word for it);
    the fragment of na manussūpacārānaṃ drops na (rule 8): manussūpacārānametaṃ = ဤသည်မှာ လူတို့ ကျက်စားရာ.
M8. **Adverbs keep their case particle** (as pi-1 rule 11 bahiddhā; nouns still drop it, rule 1): sabbadhi =
    နေရာတိုင်း၌, sabbathā = အလုံးစုံဖြင့်, sabbena sabbaṃ = အားလုံးကို အားလုံးဖြင့်, odhiso = အပိုင်းအခြားဖြင့်,
    sasaṅkhārena = တိုက်တွန်းမှုဖြင့်, santato = ငြိမ်သက်သည်ဟု; but dānena = ပေးခြင်း, sabbattatāya = ခပ်သိမ်းသော သဘော.
M9. **Quoted lemmas** («"Viharatī"ti», «"Saṃvuto"ti», «"Natthi kiñcī"ti») take the dictionary form of the word
    (Viharatī = နေသည်; Saṃvutoti = စောင့်စည်းသော; Natthi kiñcī = ဘာမျှ မရှိသည်, rule 4 for a clause).
M10. **Frames with vā**: Yattha vā pana = «သို့မဟုတ် … မည်သည့်နေရာမဆို» (as N2 Yaṃ kiñci); X vā disaṃ = «X အရပ်» (the
    «ဖြစ်စေ» of vā is the frame); yaṃ yaṃ vā panārabbha = မည်သည့်အရာကို အာရုံပြု၍ (absolutive).
M11. **Predicate sentences**: «Ime dhammā kusalā» = «သဘောတရား … ကုသိုလ်» (text «ဤသဘောတရားများသည် ကုသိုလ် ဖြစ်ကြသည်»;
    subject … predicate as pi-1 5 rule 21; the pi-1 attributive «ကုသိုလ် သဘောတရား» is not in the text);
    dhammā sikkhā = «သိက္ခာ ဖြစ်သော သဘောတရား» (the text's phrase); Kusalāyeva = «ကုသိုလ် … သာ» (eva = သာ).
M12. **Sense by context, one sense per segment**: kāyo / kāyena = ကိုယ် (the body: ^2-536, the sense door) or
    «စိတ်၏ အဖော်တို့» (the mental body, ^2-587, pi-1); patta = သပိတ် (saṅghāṭipatta) or သစ်ရွက် (pattadāna ^2-513);
    paṭigha in paṭighasaññā = ထိခိုက်မှု (impact; pi-1 «မုန်းတီးမှု» = aversion stays for paṭighaṃ ^2-542);
    āyatanaṃ = နယ်ပယ် (the jhāna sphere) or အာရုံခံ နယ်ပယ် (manāyatana, f_ayatanam); sevati / bhajati by their place in
    the synonym list (^2-514, ^2-528); vattati = ကျင့်သည် in «samādāya vattati» (^2-516); kappeti = မွေးသည် (jīvikaṃ
    kappeti) or ပြုသည် (sīhaseyyaṃ kappeti, ^2-519); sampanno = ပြည့်ဝသော in the endowed list (^2-511); sekkho /
    asekkho without ၏ where the text has the apposition «ကျင့်ကြံဆဲသူ ရဟန်း» (^2-510); saññī (fragment of nevasaññī)
    = မှတ်သိမှု ရှိသော (^2-619); uttaraṃ = မြောက် (the north, ch13); jātaṃ (of sahajātaṃ) = ဖြစ်ပေါ်သော (ch13), not
    the sample's time-list value; samāpattiyā = ရောက်ရှိရန် (^2-511, «for the attainment of»).
M13. **Relative pronoun yaṃ** (^2-552, the clause closes with «ရှိသမျှ») = (no direct equivalent), the agreed pi-1 rule
    (written explicitly: the pi-1 lookup skips (no direct equivalent)).
M14. **The precepts**: «X-ā veramaṇī» = «Xမှ ကင်းဝေးခြင်း» (the ablative inside the phrase stays, rule 1);
    veramaṇī sikkhāpadaṃ = ကင်းဝေးခြင်း သိက္ခာပုဒ်; each member of surāmerayamajjapamādaṭṭhāna has its word (surā =
    သေရည်, meraya = အရက်, majja = မူးယစ်ဖွယ်, pamāda = မေ့လျော့ခြင်း, ṭṭhānā = အကြောင်း).
M15. **Discontinuity by the question word**: in «Kathañca … ekaṃ disaṃ pharitvā viharati?» the text puts «အဘယ်သို့»
    inside: ekaṃ disaṃ pharitvā = «အရပ် တစ်မျက်နှာကို … ပျံ့နှံ့စေ၍» (^2-643, ^2-653, ^2-663, ^2-673).
M16. **Fragments of «na X»** keep «…လည်း မဟုတ်သော» as the text builds the pair: nākusalaṃ = အကုသိုလ်လည်း မဟုတ်သော,
    nāsātaṃ = နှစ်သက်ဖွယ် မကောင်းသည်လည်း မဟုတ်သော, nāsaññī = မှတ်သိမှု မရှိသူလည်း မဟုတ်သော; appaṭighā inside
    anidassanaappaṭighā = ထိခိုက်မှုလည်း မရှိသော; the fragment ākusalaṃ (from nākusalaṃ) = အကုသိုလ် (rule 8).

## Genuinely unclear (for the user)

- thulla = ကြီး, majjhima = သန်းခေါင်, yāmaṃ = ယံ, rattiyā = ညဉ့်, agge = ဖျား, gumbopi = ရုံ: parts of one Burmese word
  (M6); (no direct equivalent) would also be defensible.
- paṭisallāna = «တစ်ယောက်တည်း ကိန်းအောင်းရန်» (the text has the purpose form only, «… ကိန်းအောင်းရန် သင့်လျော်သော»).
- pāde (pāde pādaṃ accādhāya) = «ခြေတစ်ဖက်» (text «ခြေတစ်ဖက်ပေါ်၌»); mukha (mukhanimitte) = «နှုတ်ခမ်းအထက်».
- anekaṃsa = «တစ်ထစ်ချ မယူနိုင်ခြင်း» (= pi-1 anekaṃsaggāho; the negative is on the verb).
- sukhavihāraṃ (diṭṭhadhammasukhavihāraṃ) = «သာယာစွာ နေထိုင်ရန် ဖြစ်သော» (the text's attribute of the jhāna).
- kāmāvacare (^2-711, a source slip for kāmāvacaraṃ) = «ကာမဘုံ» (the text «ကာမဘုံ၌»).
- manasi karoti = «နှလုံး သွင်းသည်»: the text writes «နှလုံး မသွင်း» (^2-604) and «နှလုံးသွင်း၏» (^2-610), so the value
  is spaced to match both.
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
    if v is not None:
        return resolve(v, kw, pali, my), "table"
    v = table_get(SHARED, kw)
    if v is not None:
        v = resolve(v, kw, pali, my)
        if presence(v, my)[0]:
            return v, "table"
        # 12-14 rule M2: a value of another chapter's table that is not in THIS segment gives way to the pi-1 value
        # of the keyword that is (pi-1 values are binding for the same keyword in the same kind of segment)
        p = pi1_get(kw, my)
        return (p, "pi1") if p is not None else (v, "table")
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
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော", "၊", "သည့်",
             "လျက်", "ကုန်သော", "ကြသည်", "၏", "ကြ၏", "။", "”")   # 12-14: NEW endings (map-table-12-14.md, rule M1)
VERB_FROM = ("ပါ၏", "၏", "ပြီ", "သော", "၍", "ပြီး", "ခြင်း", "ရန်", "သည့်", "ကြ", "၊", "ဟူ", "လိမ့်မည်", "။",
             "ရာ", "”", "သနည်း")   # 12-14: NEW ending, the verb of a «where …» clause (map-table-12-14.md, rule M1)


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
    "ajjhattaṃ": "the sample's list-item value where the text glosses ajjhatta as «မိမိ၏ အတွင်း၌ ဖြစ်သော» (^2-573); "
                 "the jhāna adverb keeps pi-1 «မိမိ၌» (M2)",
    "bahiddhā": "the approved sample value (Vibhaṅga qualifier «မိမိ၏ ပြင်ပ၌»)",
    "abbhatthaṅgatā": "the text's «calmed» list «လုံးဝ ကွယ်ပျောက်သွားသည်» (no «ပြီး»), M3",
    "pātubhūtā": "the text writes «ထင်ရှားလာကြ၏» (one word, no «ပြီး»), M3",
    "abhijjhādomanassā": "the text has «စိတ်ဆင်းရဲမှု», not pi-1 «စိတ်ဆင်းရဲခြင်း»",
    "domanassā": "the text has «စိတ်ဆင်းရဲမှု», not pi-1 «စိတ်ဆင်းရဲခြင်း»",
    "abyāpajjo": "the text «ညှဉ်းဆဲလိုမှု မရှိ» (pi-1's «မညှဉ်းဆဲလိုခြင်း» is not in the segment)",
    "byāpajjanā": "the byāpāda list: «byāpatti byāpajjanā byāpajjitattaṃ» = «ဖောက်ပြန်ခြင်း၊ ဖောက်ပြန်နေခြင်း၊ …»",
    "bhūrī": "the attributive of bhūrīmedhā «ကျယ်ပြန့်သော ဉာဏ်ထက်မြက်ခြင်း» (Vb one word); pi-1 «ကျယ်ပြန့်ခြင်း» not in the text",
    "bojjhaṅgā": "the text «ဗောဇ္ဈင် ခုနစ်ပါး» (pi-1's gloss «သိမြင်ခြင်း၏ အင်္ဂါ» not in the segment; = pi-1 sambojjhaṅgo)",
    "dhamme": "«imasmiṃ dhamme» = «ဤတရား၌» (pi-1 «တရားတော်» not in the segment)",
    "dhammā kusalā": "predicate sentence «ဤသဘောတရားများသည် ကုသိုလ် ဖြစ်ကြသည်» (M11)",
    "kāmāvacare": "source slip for kāmāvacaraṃ; the text «ကာမဘုံ၌» (unclear list)",
    "Kāyiko": "the text's final term «ကိုယ်ပိုင်းဆိုင်ရာ» (pi-1 «ကိုယ်ဖြင့်» not in the segment)",
    "vācasiko": "the text's final term «နှုတ်ပိုင်းဆိုင်ရာ» (pi-1 «နှုတ်ဖြင့်» not in the segment)",
    "kāyo": "the mental body in ^2-587 «စိတ်၏ အဖော်တို့» (pi-1 kāyena), the body «ကိုယ်» in ^2-536 (M12)",
    "mukha": "mukhanimitta = «နှုတ်ခမ်းအထက် အမှတ်» (pi-1 «ခံတွင်း» not in the segment)",
    "mūla": "rukkhamūla = «သစ်ပင်ရင်း» (pi-1 «အမြစ်» is the root cause)",
    "mūlaṃ": "rukkhamūla = «သစ်ပင်ရင်း» (pi-1 «အမြစ်» is the root cause)",
    "pahānā": "the bhikkhu glosses «ပယ်ပြီးသောကြောင့်» (M4); pi-1 «ပယ်ခြင်း» elsewhere",
    "patta": "the bowl «သပိတ်» (saṅghāṭipattacīvara) / the leaf «သစ်ရွက်» (pattadāna); pi-1 «အရွက်» not in the text (M12)",
    "Paṭigha": "paṭighasaññā = impact «ထိခိုက်မှု» (pi-1 «မုန်းတီးမှု» = aversion), M12",
    "paṭigha": "paṭighasaññā = impact «ထိခိုက်မှု» (pi-1 «မုန်းတီးမှု» = aversion), M12",
    "phala": "phaladāna = «သစ်သီးကို ပေးခြင်း» (pi-1 «အသီး / ဖိုလ်» not in the segment)",
    "phusanā": "the attainment list «ထိတွေ့ခြင်း» (pi-1 «ထိခြင်း» not in the segment)",
    "samāpannassa": "«X samāpannassa» = «Xကို ဝင်စားသူ၏»: the object ဈာန် has its own keyword (samāpattiṃ)",
    "samāpattiyā": "«kusalānaṃ dhammānaṃ samāpattiyā» = «… ရောက်ရှိရန်» (pi-1 «ကျူးလွန်ခြင်း» is āpatti), M12",
    "saññī": "fragment of nevasaññī «မှတ်သိမှု ရှိသူ» (^2-619), M12",
    "vajja": "vajjadassāvī = «အပြစ်ဟု မြင်လေ့ရှိသူ»: the noun (pi-1 «အပြစ်ရှိသည်» is the predicate of vajjasaññitā)",
    "yoga": "yogakkhema = one word «ဘေးကင်းရာ» (M6)",
    "āyatanaṃ": "the jhāna sphere «နယ်ပယ်» (ākāsānañcāyatana …); pi-1 «အာရုံခံ နယ်ပယ်» = the sense base (M12)",
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
    with open(HERE / "map-table-12-14.md", "w", encoding="utf-8") as f:
        f.write("# pi-2 Burmese keyword mapping: rules and review table (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း», chapters: "
                + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_12-14.py (a copy of the approved sample's map_all.py). Burmese from the FINAL pi-2 text of this track only "
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


def todo(sids):
    """working aid: Pāli, Burmese and only the keywords without a value / failing presence"""
    for ch in CHAPTERS:
        my, pa, rows = load(ch)
        R = dict(rows)
        for sid in sids:
            if sid not in R:
                continue
            out = []
            for kw in dict.fromkeys(k.strip() for k in R[sid].split(", ")):
                try:
                    v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                    if not presence(v, my[sid])[0]:
                        out.append(f"{kw}=FAIL:{v}")
                except KeyError:
                    out.append(kw)
            if not out:
                continue
            print("==", sid)
            print(pa.get(sid))
            print(my[sid])
            print("TODO:", " | ".join(out))


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
    if args and args[0] == "--todo":
        todo(args[1:])
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
