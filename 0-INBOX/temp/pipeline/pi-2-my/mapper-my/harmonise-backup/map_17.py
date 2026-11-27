"""Pāli→Burmese keyword mapping for pi-2 (Vibhaṅga, «ခွဲခြမ်းစိတ်ဖြာခြင်း»), chapter 17-khuddakavatthuvibhango.

usage (python3 -I -X utf8, from any directory):
  map_17.py             writes 17-khuddakavatthuvibhango.mapped.md and map-table-17.md, then verifies them
                        (keyword preservation, presence of every value chunk in its segment, no ", " / «၊» / « / »
                        in a value)
  map_17.py --report    writes nothing; lists unmapped keywords and presence failures
  map_17.py --seg ID    prints Pāli, Burmese, keywords and mapping of one segment

A copy (not an import) of the approved sample script map_all.py (pi-2; its tables T_PREAMBLE / T_KHANDHA, compose
rules, context functions and verifier are kept unchanged and used as shared tables), with this chapter's table
T_KHUDDAKA, its ALT variants and CTX overrides, the NEW rules N12-N22 (map-table-17.md) and four more accepted
endings in the presence check. The Burmese is the FINAL pi-2 text of this track
(AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters/17-khuddakavatthuvibhango.md). The list-item and
heading values in the first block of T_KHUDDAKA are this track's own Burmese for the Pāli word, read from the
zero-shot generator pi-2-my/make_ch17.py (ITEMS / NAME / headings: the words the text prints), each kept only where
it occurs in the segment. No other Burmese source is used.

Lookup order per keyword (as map_all.py):
  CTX[sid] -> T_KHUDDAKA -> the shared tables (sample) -> PI1: the final pi-1 mapping (the most frequent pi-1 value
  present in THIS segment) -> compose.
A value «@alt» = the first variant of ALT[kw] present in the segment (one sense per segment).
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
ALT = {
    "kula": ["ဒါယကာ အိမ်ဝန်း", "ကိုးကွယ်သော အိမ်"],
    "saṅgo": ["တွယ်ငြိမှု", "တွယ်ကပ်ခြင်း"],
    "adukkhamasukhaṃ": ["မနာကျင် မသာယာမှု", "မနာကျင် မသာယာသော"],
    "bhedā": ["ပြိုကွဲသောအခါ", "ပြိုကွဲ၍"],
    "carati": ["ပြုသည်", "ကျင့်သည်"],
    "sukhaṃ": ["သာယာမှု", "ချမ်းသာ"],
    "dukkha": ["ကိုယ်ဆင်းရဲခြင်း", "ဆင်းရဲ", "ဒုက္ခ"],
    "maggo": ["ခရီး", "မဂ်"],
    "iddhi": ["တန်ခိုး", "ဣဒ္ဓိ"],
    "saññī": ["မှတ်သိမှု ရှိသူ", "မှတ်သိမှု ရှိသော"],
    "sassato": ["ထာဝရ တည်မြဲသည်", "ထာဝရ တည်သော"],
    "saññīnāsaññī": ["မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သူ", "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သော"],
    "vādā": ["ဝါဒ", "ပြောခြင်း"],
    "paṭigha": ["ထိခိုက်မှု", "မုန်းတီးမှု"],
    "suta": ["အကြားအမြင်", "ကြားသော"],
    "pāripūriṃ": ["ကိုယ်အင်္ဂါ ပြည့်စုံခြင်း", "ပြည့်စုံမှု"],
    "sammā": ["အပြည့်အဝ", "မှန်ကန်စွာ", "ကောင်းစွာ"],
    "nānatta": ["အမျိုးမျိုးသော", "အမျိုးမျိုး ကွဲပြားမှု"],
    "sukha": ["ချမ်းသာသော", "သာယာမှု", "ချမ်းသာ"],
    "ābhogo": ["စိတ်ညွတ်ခြင်း", "ညွတ်ခြင်း"],
    "dukkhe": ["ဒုက္ခ", "ဆင်းရဲသော", "ဆင်းရဲ"],
    "uppajjati": ["ဖြစ်ပေါ်သည်", "ဖြစ်ပေါ်လာသည်"],
    "dhātu": ["ဓာတ်", "ဘုံ"],
    "jāti": ["ဇာတိ", "မွေးဖွားခြင်း"],
    "jātiṃ": ["ဇာတိ", "မွေးဖွားခြင်း"],
    "jātiṃ paṭicca": ["ဇာတိကို စွဲ၍", "မွေးဖွားခြင်းကို စွဲ၍"],
    "kata": ["ပြုပြီးသော", "ပြုခဲ့သော"],
    "doso": ["ဒေါသ", "အပြစ်"],
    "sīlabbatena": ["သီလနှင့် အကျင့်ဝတ်", "သီလ အကျင့်ဝတ်"],
    "jappā": ["စကား ပြောခြင်း", "တမ်းတခြင်း"],
    "paṭighāto": ["ထိခိုက်မှု", "ပြန်လည် ရန်ငြိုးဖွဲ့ခြင်း"],
    "adhamma": ["တရားနှင့် မညီသော", "မတရားသော"],
    "vibhava": ["ဘဝ ပျောက်ကွယ်ခြင်း", "ဘဝ ပျောက်ကွယ်သည်"],
    "saṃvattanikā": ["ဖြစ်စေတတ်သော", "ဖြစ်စေသော"],
    "āpajjati": ["ဝင်ရောက် ဆောင်ရွက်သည်", "ပြုသည်"],
    "bahiddhā": ["မိမိ၏ ပြင်ပ၌", "အပြင်ပိုင်း", "အပြင်ဘက်"],
    "pariḷāho": ["ပူလောင်ခြင်း", "ပူလောင်မှု"],
    "chando": ["ဆန္ဒ", "လိုလားမှု"],
    "ajjhosānaṃ": ["နစ်မွန်းခြင်း", "နစ်မွန်းမှု"],
    "ārabbha": ["အာရုံပြု၍", "အစွဲပြု၍"],
    "vivāda": ["အငြင်းပွားမှု", "အငြင်းပွားရာ", "အငြင်းပွားခြင်း"],
    "sakkāra": ["အပူဇော်ခံရခြင်း", "အရိုအသေ ပြုခံရမှု"],
    "garukāra": ["အလေးပြုခံရခြင်း", "လေးစားခံရမှု"],
    "vaṇṇa": ["အဆင်းလှခြင်း", "ဂုဏ်သတင်း", "ဂုဏ်ကျေးဇူး"],
    "paccaya": ["အထောက်အပံ့", "ပစ္စည်း"],
    "icchā": ["အလိုဆန္ဒ", "အလိုရှိခြင်း"],
    "kamyatā": ["ထူလိုခြင်း", "လိုခြင်း", "လိုချင်ခြင်း"],
    "jīvita": ["အသက်ရှင်ခြင်း", "အသက်"],
    "asaññi": ["မှတ်သိမှု မရှိသူ", "မှတ်သိမှု မရှိသော"],
    "nevasaññināsaññi": ["မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သူ", "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သော"],
    "uccheda": ["သေပြီးနောက် ပြတ်စဲသွားသည်", "ပြတ်စဲသွားသည်", "ပြတ်သည်"],
    "antavā": ["အဆုံး ရှိသူ", "အဆုံး ရှိသော"],
    "anantavā": ["အဆုံး မရှိသူ", "အဆုံး မရှိသော"],
    "ānudiṭṭhi": ["အဖန်ဖန် ရှုမြင်သော အယူ", "ပတ်သက်သော အယူ"],
    "vatthūni": ["အကြောင်းရင်း", "အကြောင်း"],
    "asaññī": ["မှတ်သိမှု မရှိသူ", "မှတ်သိမှု မရှိသော"],
    "nevasaññīnāsaññī": ["မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သူ", "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်သော"],
    "icchatā": ["လိုချင်ခြင်း", "လိုချင်မှု", "အလိုရှိခြင်း"],
    "Kāmadhātu": ['ကာမဘုံ', 'ကာမ ဓာတ်'],
    "esanā": ['ရှာမှီးမှု', 'ရှာမှီးခြင်း'],
    "rūpataṇhā": ['အဆင်းအရောင်ကို တပ်မက်မှု', 'သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု'],
}
CTX = {
    "2-17-0": { "vatthu": "အကြောင်းအရာ", },
    "2-17-3-18-0": { "bahiddhā": "အပြင်ပိုင်း", },
    "2-881": { "māno": "ထင်မှတ်မှု", },
    "2-916": { "Rūpa": "သိမ်မွေ့သော ရုပ်", },
    "2-932": { "dhammaṃ": "တရား", },
    "2-943": { "dukkhā": "ဆင်းရဲသော", },
    "2-953": { "uppanno": "ဖြစ်ပေါ်သော", "vatthu": "အကြောင်း", },
    "2-954": { "paṭivirodho": "ဆန့်ကျင်ခြင်း", },
    "2-977": { "sassata": "မြဲသည်", },
    "2-U10": { "aññataraññatarena": "တစ်ခုခုသော အရာ", },
    "2-974": { "sati": "ရှိသော", },
    "2-976": { "sati": "ရှိသော", },
    "2-U62": { "Rūpa": "အဆင်းအရောင်", },
    "2-U64": { "somanassa": "ဝမ်းမြောက်ဖွယ်", },
    "2-U65": { "domanassa": "စိတ်ဆင်းရဲဖွယ်", },
    "2-U66": { "upekkhā": "လျစ်လျူရှုဖွယ်", },
    "2-893": { "dhamma": "တရား", },
    "2-904": { "kodha": "အမျက်ဒေါသ", },
    "2-951": { "āyatanaṃ": "နယ်ပယ်", },
    "2-875": { "hīno": "ယုတ်ညံ့သူ", },
    "2-876": { "hīno": "ယုတ်ညံ့သူ", },
    "2-877": { "hīno": "ယုတ်ညံ့သူ", },
    "2-909": { "rūpataṇhā": "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု", "rūpa": "အဆင်းအရောင်", },
    "2-917": { "Rūpa": "သိမ်မွေ့သော ရုပ်", },
    "2-918": { "Rūpa": "သိမ်မွေ့သော ရုပ်", },
    "2-U49": { "Rūpa": "သိမ်မွေ့သော ရုပ်", },
    "2-948": { "evaṃdiṭṭhi": "ဤသို့ အယူ ရှိသော", },
    # @@CTX@@
}

T_KHUDDAKA = {
    # --- list items, names, headings: the zero-shot's own Burmese for the Pāli word (pi-2-my/make_ch17.py ITEMS / NAME)
    "Adhimāno": "လွန်ကဲစွာ ထင်မှတ်သော မာန",
    "Akkhanti": "မသည်းခံခြင်း",
    "Akusalaṃ kāyakammaṃ": "အကုသိုလ် ကိုယ်ဖြင့် ပြုသော ကံ",
    "Anajjavo": "မဖြောင့်မတ်မှု",
    "Antavādiṭṭhi": "လောကသည် အဆုံး ရှိသည်ဟူသော အယူ",
    "Arati": "မမွေ့လျော်မှု",
    "Asmimāno": "ငါ ရှိ၏ဟူသော မာန",
    "Atimāno": "အလွန် မာနထားမှု",
    "Atricchatā": "အလွန်အကျွံ လိုချင်ခြင်း",
    "Bhavadiṭṭhi": "ဘဝ ဆက်လက် တည်ရှိသည်ဟူသော အယူ",
    "Cetaso ca līnattaṃ": "စိတ်၏ တွန့်ဆုတ်နေမှု",
    "Chakkamātikā": "ခြောက်မျိုးတွဲ ခေါင်းစဉ်စာရင်း",
    "Cāpalyaṃ": "ပေါ့ပျက်မှု",
    "Dasakamātikā": "ဆယ်မျိုးတွဲ ခေါင်းစဉ်စာရင်း",
    "Dasavatthukā antaggāhikā diṭṭhi": "အကြောင်းအရာ ဆယ်ပါး ရှိသော အစွန်းကို စွဲကိုင်သော အယူ",
    "Dasavatthukā micchādiṭṭhi": "အကြောင်းအရာ ဆယ်ပါး ရှိသော မှားယွင်းသော အယူ",
    "Gotta": "အမျိုးအနွယ်",
    "Gottamadādī": "အမျိုးအနွယ်ကြောင့် မူးယစ်မှု စသည်",
    "Hīnassa": "ယုတ်ညံ့သူ ဖြစ်လျက်",
    "Janapadaṃ": "ဇနပုဒ်",
    "Jāti": "ဇာတိ",
    "Jātimado": "ဇာတိကြောင့် မူးယစ်မှု",
    "Kammārāmatā": "အလုပ်ကို နှစ်သက်ခြင်း",
    "Kuhanā": "လှည့်ဖြား ဟန်ဆောင်မှု",
    "Kāmadhātu": "@alt",
    "Kāmarāgānusayo": "ကာမရာဂ ကိန်းအောင်းခြင်း",
    "Kāmasaññā": "ကာမကို မှတ်သိမှု",
    "Kāmataṇhā": "ကာမကို တပ်မက်မှု",
    "Kāmavitakko": "ကာမကို စတင်ကြံစည်မှု",
    "Kāmesanā": "ကာမကို ရှာမှီးမှု",
    "Kāyaduccaritaṃ": "ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်",
    "Lapanā": "ချော့မော့ ပြောဆိုခြင်း",
    "Mado": "မူးယစ်မှု",
    "Mahicchatā": "လိုချင်မှု ကြီးခြင်း",
    "Makkho": "ကျေးဇူး ချေဖျက်မှု",
    "Micchāmāno": "မှားယွင်းသော မာန",
    "Musāvādo": "မုသား ပြောခြင်း",
    "Mānātimāno": "မာနနှင့် အလွန် မာနထားမှု",
    "Nemittikatā": "အရိပ်အမြွက် ပြတတ်ခြင်း",
    "Nippesikatā": "နှိပ်ကွပ် ပြောဆိုတတ်ခြင်း",
    "Omāno": "ယုတ်ညံ့ဟု ထင်မှတ်မှု",
    "Pamādo": "မေ့လျော့မှု",
    "Pāpicchatā": "ယုတ်မာသော အလိုရှိခြင်း",
    "Pāṇātipāto": "သူ့အသက်ကို သတ်ခြင်း",
    "Rāgaggi": "ရာဂ မီး",
    "Rūpataṇhā": "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်မှု",
    "Sadisassa": "တူညီသူ ဖြစ်လျက်",
    "Saññī": "မှတ်သိမှု ရှိသူ",
    "Siṅgaṃ": "ကြွားလုံး ထုတ်မှု",
    "Sārambho": "ပြိုင်ဆိုင်မှု",
    "Tandī": "ပျင်းရိငိုက်မျဉ်းမှု",
    "Taṇhaṃ": "တပ်မက်မှု",
    "Thambho": "တောင့်တင်းမှု",
    "Tintiṇaṃ": "ငမ်းငမ်းတက် မြည်တမ်းမှု",
    "Ucchedadiṭṭhi": "အတ္တသည် ပြတ်စဲသွားသည်ဟူသော အယူ",
    "Vijambhitā": "သမ်းဝေ ကိုင်းညွတ်မှု",
    "abahulīkammaṃ": "အဖန်ဖန် မပြုခြင်း",
    "abhāvanā": "မပွားများခြင်း",
    "accāsarā": "အပြစ်ကို ကျော်လွှားခြင်း",
    "acittīkāro": "အလေးမထားခြင်း",
    "adaṭṭhukamyatā": "မတွေ့မြင်လိုခြင်း",
    "adhammacariyā": "တရားနှင့် မညီသော အကျင့်",
    "adhimāno": "လွန်ကဲစွာ ထင်မှတ်သော မာန",
    "adhāraṇatā": "စွဲမှတ် မထားခြင်း",
    "adhāretukamyatā": "မဆောင်ထားလိုခြင်း",
    "agati": "အဂတိ",
    "agatigamanaṃ": "အဂတိ လိုက်ခြင်း",
    "aggī": "မီး",
    "agāravā": "မရိုသေမှု",
    "ajjhenena": "စာပေ သင်ယူမှု",
    "ajjhosānaṃ": "နစ်မွန်းခြင်း",
    "akkhamanatā": "မသည်းခံနိုင်သော အဖြစ်",
    "akkhanti": "မသည်းခံခြင်း",
    "akkosanā": "ဆဲရေးခြင်း",
    "akusaladhātuyo": "အကုသိုလ် ဓာတ်",
    "akusalasaññā": "အကုသိုလ် မှတ်သိမှု",
    "akusalavitakkā": "အကုသိုလ် စတင်ကြံစည်မှု",
    "akusalaṃ kāyakammaṃ": "အကုသိုလ် ကိုယ်ဖြင့် ပြုသော ကံ",
    "akusalaṃ manokammaṃ": "အကုသိုလ် မနောဖြင့် ပြုသော ကံ",
    "akusalaṃ vacīkammaṃ": "အကုသိုလ် နှုတ်ဖြင့် ပြုသော ကံ",
    "amaddavatā": "မနူးညံ့သော အဖြစ်",
    "amaddavo": "မနူးညံ့မှု",
    "amattaññutā": "အတိုင်းအရှည်ကို မသိခြင်း",
    "amudutā": "မနူးညံ့ခြင်း",
    "anabhiramaṇā": "မပျော်မွေ့နေခြင်း",
    "anabhirati": "မပျော်မွေ့ခြင်း",
    "anaddā": "အလေးဂရု မပြုခြင်း",
    "anaddāyanā": "အလေးဂရု မပြုနေခြင်း",
    "anadhivāsanatā": "သည်းမခံနိုင်ခြင်း",
    "anadhiṭṭhānaṃ": "မဆောက်တည်ခြင်း",
    "anajjavatā": "မဖြောင့်မတ်သော အဖြစ်",
    "anajjavo": "မဖြောင့်မတ်မှု",
    "anantavā": "အဆုံး မရှိသူ",
    "anantavādiṭṭhi": "လောကသည် အဆုံး မရှိဟူသော အယူ",
    "ananuyogo": "အားမထုတ်ခြင်း",
    "anavaññāta": "အထင်မသေးခံရခြင်း",
    "anaṭṭhitakiriyatā": "တည်တံ့စွာ မပြုခြင်း",
    "anokappanā": "သက်ဝင်၍ မယုံကြည်ခြင်း",
    "antaggāhikā diṭṭhi": "အစွန်းကို စွဲကိုင်သော အယူ",
    "antavā": "အဆုံး ရှိသူ",
    "antavādiṭṭhi": "လောကသည် အဆုံး ရှိသည်ဟူသော အယူ",
    "antānantikā": "အဆုံးနှင့် အဆုံးမဲ့ကို ဆိုသော ဝါဒ",
    "anuggahetukamyatā": "မသင်ယူလိုခြင်း",
    "anuppabandhanā": "ရန်ငြိုးကို ဆက်တိုက် ဖွဲ့ထားခြင်း",
    "anuppiyabhāṇitā": "နားဝင်ချိုအောင် ပြောခြင်း",
    "anupārambhanā": "အဖန်ဖန် အပြစ်ရှာခြင်း",
    "anupārambho": "အဖန်ဖန် အပြစ်ရှာမှု",
    "anusayā": "ကိန်းအောင်းခြင်း",
    "anusaṃsandanā": "ရန်ငြိုးကို ဆက်စပ်ထားခြင်း",
    "anuttānīkammaṃ": "ထင်ရှားအောင် မပြုခြင်း",
    "anādariyatā": "မလေးစားသော သဘော",
    "anāsevanā": "မမှီဝဲခြင်း",
    "anāvaṭṭanā": "အဖန်ဖန် လှည့်ခြင်း",
    "anāvikammaṃ": "ပေါ်လွင်အောင် မပြုခြင်း",
    "appatissavatā": "နာခံမှု မရှိခြင်း",
    "appaṭinissaggo": "မစွန့်လွှတ်ခြင်း",
    "appaṭisanthāro": "ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း မရှိခြင်း",
    "arati": "မမွေ့လျော်မှု",
    "aratitā": "မမွေ့လျော်သော အဖြစ်",
    "arūpī": "ရုပ် မရှိသူ",
    "asaddhammā": "သူတော်ကောင်း မဟုတ်သူတို့၏ တရား",
    "asakhilavācatā": "စကား မချိုမြိန်ခြင်း",
    "asakkaccakiriyatā": "ရိုရိုသေသေ မပြုခြင်း",
    "asampajaññatā": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိသော အဖြစ်",
    "asamāgantukamyatā": "မပေါင်းဆုံလိုခြင်း",
    "asantuṭṭhitā": "ရောင့်ရဲမှု မရှိခြင်း",
    "asavanakamyatā": "နားမထောင်လိုခြင်း",
    "asaññī": "မှတ်သိမှု မရှိသူ",
    "asaññīti naṃ paññapenti": "ထိုအတ္တကို မှတ်သိမှု မရှိသူဟု ပညတ်သည်",
    "asaṇhavācatā": "စကား မပြေပြစ်ခြင်း",
    "asoraccaṃ": "မယဉ်ကျေးခြင်း",
    "asotukamyatā": "မနာကြားလိုခြင်း",
    "assaddahanā": "မယုံကြည်ခြင်း",
    "assaddhiyaṃ": "ယုံကြည်မှု မရှိခြင်း",
    "assati": "သတိ မရှိခြင်း",
    "assādadiṭṭhi": "သာယာမှုဆိုင်ရာ အယူ",
    "asākhalyaṃ": "စကား မချိုသာခြင်း",
    "asātaccakiriyatā": "ထပ်ကာထပ်ကာ မပြုခြင်း",
    "asīlyaṃ": "ယဉ်ကျေးသော အလေ့ မရှိခြင်း",
    "atimāno": "အလွန် မာနထားမှု",
    "atricchatā": "အလွန်အကျွံ လိုချင်ခြင်း",
    "attaparibhavo": "မိမိကိုယ်ကို စော်ကားခြင်း",
    "attavaññā": "မိမိကိုယ်ကို လျစ်လျူရှုခြင်း",
    "attavādupādānaṃ": "အတ္တဟူသော ဝါဒ စွဲလမ်းမှု",
    "attuññā": "မိမိကိုယ်ကို အထင်သေးခြင်း",
    "attānudiṭṭhi": "အတ္တဟု အဖန်ဖန် ရှုမြင်သော အယူ",
    "avadaññutā": "ပေးကမ်းရန် မလိုလားခြင်း",
    "avaññā": "လျစ်လျူရှုခြင်း",
    "avijjānusayo": "အမှန်ကို မသိမှု ကိန်းအောင်းခြင်း",
    "ayoniso manasikāro": "မသင့်လျော်စွာ နှလုံးသွင်းခြင်း",
    "aṅgaṇaṃ": "အစွန်းအကွက်",
    "aṅgaṇāni": "အစွန်းအကွက်",
    "aṭhapanā": "ပြင်ဆင်ထားခြင်း",
    "aṭṭhapanā": "ခိုင်ခိုင်မြဲမြဲ တည်ထားခြင်း",
    "bhassārāmatā": "စကားပြောခြင်းကို နှစ်သက်ခြင်း",
    "bhavadiṭṭhi": "ဘဝ ဆက်လက် တည်ရှိသည်ဟူသော အယူ",
    "bhavataṇhā": "ဘဝကို တပ်မက်မှု",
    "bhavesanā": "ဘဝကို ရှာမှီးမှု",
    "bhayānakaṃ": "ကြောက်မက်ဖွယ် ဖြစ်ခြင်း",
    "bhayāni": "ဘေး",
    "bhoga": "စည်းစိမ်ဥစ္စာ",
    "bhojane amattaññutā": "အစားအစာ၌ အတိုင်းအရှည်ကို မသိခြင်း",
    "bhākuṭitā": "မျက်မှောင် ကြုတ်ခြင်း",
    "bhākuṭiyaṃ": "မျက်မှောင် ကြုတ်ထားသော အဖြစ်",
    "brahmacariyesanā": "မြတ်သော အကျင့်ကို ရှာမှီးမှု",
    "brāhmaṇo": "ပုဏ္ဏား",
    "byādhiyakaṃ": "ဖျားနာသကဲ့သို့ ဖြစ်ခြင်း",
    "byāpajjanā": "ဖောက်ပြန်နေခြင်း",
    "byāpādadhātu": "ဖျက်ဆီးလိုစိတ် ဓာတ်",
    "byāpādavitakko": "ဖျက်ဆီးလိုစိတ်ဆိုင်ရာ စတင်ကြံစည်မှု",
    "capalatā": "ပေါ့ပျက်ခြင်း",
    "cetaso ca līnattaṃ": "စိတ်၏ တွန့်ဆုတ်နေမှု",
    "cetaso utrāso": "စိတ်၏ ထိတ်လန့်ခြင်း",
    "cetaso vikkhepo": "စိတ်၏ ပျံ့လွင့်ခြင်း",
    "chadanaṃ": "ဖုံးအုပ်ခြင်း",
    "chambhitattaṃ": "တောင့်တင်းထားသော အဖြစ်",
    "chandarāgo": "လိုလားမှု ရာဂ",
    "chandarāgā": "လိုလားမှု ရာဂ",
    "chādanā": "ဖုံးခြင်း",
    "cittavipariyāso": "စိတ် ပြောင်းပြန်",
    "cāpalyaṃ": "ပေါ့ပျက်မှု",
    "cāturatā": "လိမ္မာဟန် ပြခြင်း",
    "cāturiyaṃ": "လိမ္မာဟန် ပြသော အဖြစ်",
    "cāṭukamyatā": "ဖားယားလိုခြင်း",
    "dasavatthukā antaggāhikā diṭṭhi": "အကြောင်းအရာ ဆယ်ပါး ရှိသော အစွန်းကို စွဲကိုင်သော အယူ",
    "dasavatthukā micchādiṭṭhi": "အကြောင်းအရာ ဆယ်ပါး ရှိသော မှားယွင်းသော အယူ",
    "devo": "နတ်",
    "dhanena": "ဥစ္စာ",
    "dhanāsā": "ဥစ္စာကို မျှော်လင့်ခြင်း",
    "diṭṭhivipariyāso": "အယူ ပြောင်းပြန်",
    "diṭṭhivipatti": "အယူ ပျက်စီးခြင်း",
    "diṭṭhiyo": "အယူ",
    "diṭṭhānusayo": "အယူ ကိန်းအောင်းခြင်း",
    "domanassupavicārā": "စိတ်ဆင်းရဲဖွယ်၌ စိတ် လှည့်လည်မှု",
    "dosaggi": "ဒေါသ မီး",
    "duccaritāni": "ဒုစရိုက်",
    "dukkhappabhavo": "ဒုက္ခ၏ ဖြစ်ပေါ်ရာ",
    "dussīlyaṃ": "သီလ ပျက်ခြင်း",
    "ekaccasassatikā": "အချို့ မြဲသည်ဟု ဆိုသော ဝါဒ",
    "esanā": "@alt",
    "gahaṭṭho": "လူဝတ်ကြောင်",
    "gandhāsā": "အနံ့ကို မျှော်လင့်ခြင်း",
    "garahaṇā": "ကဲ့ရဲ့ခြင်း",
    "garukāra": "အလေးပြုခံရခြင်း",
    "gehasitaṃ cetasikaṃ asātaṃ": "လောကီ အိမ်ရာကို မှီသော စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ် မကောင်းမှု",
    "gehasitaṃ cetasikaṃ sātaṃ": "လောကီ အိမ်ရာကို မှီသော စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ်ကောင်းမှု",
    "gehasitā upekkhā": "လောကီ အိမ်ရာကို မှီသော ဥပေက္ခာ",
    "gehasitāni domanassāni": "လောကီ အိမ်ရာကို မှီသော စိတ်ဆင်းရဲမှု",
    "gehasitāni somanassāni": "လောကီ အိမ်ရာကို မှီသော ဝမ်းမြောက်မှု",
    "giddhikatā": "မက်မောခြင်း",
    "gotta": "အမျိုးအနွယ်",
    "gottamado": "အမျိုးအနွယ်ကြောင့် မူးယစ်မှု",
    "gottena": "အမျိုးအနွယ်",
    "gūhanā": "ဝှက်ထားခြင်း",
    "heṭhanā": "နှိပ်စက်ခြင်း",
    "hiṃsanā": "ထိခိုက်နာကျင်စေခြင်း",
    "hīnassa": "ယုတ်ညံ့သူ ဖြစ်လျက်",
    "hīḷanā": "မိမိကိုယ်ကို နှိမ့်ချခြင်း",
    "icchāgatā": "အလိုရှိမှုသို့ ရောက်ခြင်း",
    "iddhi": "တန်ခိုး",
    "iriyāpatha": "ကိုယ်ဟန် အမူအရာ",
    "iñjitāni": "တုန်လှုပ်မှု",
    "jhāna": "ဈာန်",
    "jimhatā": "ကောက်ကျစ်သော အဖြစ်",
    "jātimado": "ဇာတိကြောင့် မူးယစ်မှု",
    "jātiyā": "ဇာတိ",
    "jīvitāsā": "အသက်ကို မျှော်လင့်ခြင်း",
    "kakkaratā": "ကောက်ကွေးခြင်း",
    "kakkariyaṃ": "ကောက်ကွေးသော အဖြစ်",
    "kakkhaḷiyaṃ": "ကြမ်းတမ်းခြင်း",
    "kammāyatanena": "အလုပ်အကိုင်",
    "kasāvā": "အမည်းအစက်",
    "kaṭhinatā": "မာကျောခြင်း",
    "keḷanā": "ကစားခြင်း",
    "khattiyo": "မင်းမျိုး",
    "khipanā": "ပစ်ချခြင်း",
    "kilesavatthūni": "ကိလေသာ အကြောင်းရင်း",
    "kiñcanaṃ": "တွယ်ငြိရာ",
    "kiñcanā": "တွယ်ငြိရာ",
    "kolaputtiyena": "အမျိုးကောင်းသား ဖြစ်ခြင်း",
    "kosajjaṃ": "ပျင်းရိမှု",
    "kuhanā": "လှည့်ဖြား ဟန်ဆောင်မှု",
    "kuhāyanā": "လှည့်ဖြား ဟန်ဆောင်ခြင်း",
    "kujjhitattaṃ": "အမျက်ဒေါသ ထွက်ထားသော အဖြစ်",
    "kusītavatthūni": "ပျင်းရိမှု၏ အကြောင်း",
    "kuṭilatā": "တွန့်လိမ်ခြင်း",
    "kāmataṇhā": "ကာမကို တပ်မက်မှု",
    "lapanā": "ချော့မော့ ပြောဆိုခြင်း",
    "lokadhammesu": "လောကဓံ",
    "lomahaṃso": "ကြက်သီးမွေးညင်း ထခြင်း",
    "līyitattaṃ": "အားပျော့ထားသော အဖြစ်",
    "macchariyaṃ": "ဝန်တိုမှု",
    "mado": "မူးယစ်မှု",
    "mahicchatā": "လိုချင်မှု ကြီးခြင်း",
    "majjanā": "မူးယစ်ခြင်း",
    "majjitattaṃ": "မူးယစ်ထားသော အဖြစ်",
    "makkho": "ကျေးဇူး ချေဖျက်မှု",
    "makkhāyanā": "ကျေးဇူး ချေဖျက်ခြင်း",
    "malaṃ": "အညစ်အကြေး",
    "malāni": "အညစ်အကြေး",
    "manasikāro": "နှလုံးသွင်းခြင်း",
    "manoduccaritaṃ": "မနောဖြင့် ပြုသော ဒုစရိုက်",
    "manopadoso": "မနောဖြင့် ဒေါသထွက်ခြင်း",
    "manovilekho": "မနောကို ခြစ်ကုတ်ခြင်း",
    "manusso": "လူ",
    "maññitāni": "ထင်မှတ်မှု",
    "maṇḍanā": "အလှဆင်ခြင်း",
    "micchattā": "မှားယွင်းမှု",
    "micchāmāno": "မှားယွင်းသော မာန",
    "mohaggi": "မောဟ မီး",
    "muggasūpyatā": "ပဲဟင်းကဲ့သို့ အမှန်အမှား ရောယှက် ပြောခြင်း",
    "musāvādo": "မုသား ပြောခြင်း",
    "muṭṭhassaccaṃ": "သတိလစ်ခြင်း",
    "mānā": "မာန",
    "mānānusayo": "မာန ကိန်းအောင်းခြင်း",
    "mānātimāno": "မာနနှင့် အလွန် မာနထားမှု",
    "māyāvitā": "လှည့်စားတတ်သော အဖြစ်",
    "nandirāgo": "နှစ်သက်မှု ရာဂ",
    "nemittikatā": "အရိပ်အမြွက် ပြတတ်ခြင်း",
    "nevasaññīnāsaññī": "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မရှိသည်လည်း မဟုတ်သူ",
    "nicca": "မြဲ၏",
    "niddārāmatā": "အိပ်ခြင်းကို နှစ်သက်ခြင်း",
    "nikati": "ကောက်ကျစ်ခြင်း",
    "nimittakammaṃ": "အရိပ်အမြွက် ပြုခြင်း",
    "nimittaṃ": "အရိပ်အမြွက် ပြခြင်း",
    "nippesikatā": "နှိပ်ကွပ် ပြောဆိုတတ်ခြင်း",
    "nirodhataṇhā": "ချုပ်ငြိမ်းခြင်းကို တပ်မက်မှု",
    "niṭṭhuriyakammaṃ": "ရက်စက်စွာ ပြုခြင်း",
    "niṭṭhuriyaṃ": "ရက်စက်ခြင်း",
    "nānattasaññā": "အမျိုးမျိုးသော မှတ်သိမှု",
    "obhāsakammaṃ": "သွယ်ဝိုက် ပြောဆိုမှု ပြုခြင်း",
    "obhāso": "သွယ်ဝိုက် ပြောခြင်း",
    "ohīḷanā": "မိမိကိုယ်ကို အလွန် နှိမ့်ချခြင်း",
    "omaññanā": "ယုတ်ညံ့ဟု ထင်မှတ်ခြင်း",
    "omaññitattaṃ": "ယုတ်ညံ့ဟု ထင်မှတ်ထားသော အဖြစ်",
    "omāno": "ယုတ်ညံ့ဟု ထင်မှတ်မှု",
    "pabbajito": "ရဟန်း",
    "pamajjanā": "မေ့လျော့ခြင်း",
    "pamādo": "မေ့လျော့မှု",
    "papañcitāni": "ချဲ့ထွင်မှု",
    "papañcārāmatā": "ချဲ့ထွင်ခြင်းကို နှစ်သက်ခြင်း",
    "parapiṭṭhimaṃsikatā": "ကွယ်ရာတွင် အတင်းပြောခြင်း",
    "paribhavo": "စော်ကားခြင်း",
    "parigedho": "အလွန် ငမ်းငမ်းတက် လိုချင်ခြင်း",
    "pariggaho": "သိမ်းပိုက်ခြင်း",
    "parigūhanā": "အနှံ့ ဝှက်ထားခြင်း",
    "pariharaṇā": "ရှောင်တိမ်းခြင်း",
    "parihāniyā dhammā": "ဆုတ်ယုတ်စေတတ်သော သဘောတရား",
    "parikathā": "ပတ်လည် စကား ပြောခြင်း",
    "parikkhattatā": "ကြော့ရှင်းဟန် ပြခြင်း",
    "paritassitā": "ပူပန်ခြင်း",
    "pariyuṭṭhānāni": "ထကြွခြင်း",
    "pariṇāha": "ကိုယ်လုံး ပြည့်ဖြိုးခြင်း",
    "parānuvādabhayaṃ": "သူတစ်ပါး အပြစ်တင်ခြင်း ဘေး",
    "parūpaghāto": "သူတစ်ပါးကို ထိပါးခြင်း",
    "paḷāso": "တုပြိုင်မှု",
    "paḷāsāhāro": "တုပြိုင်မှုကို ဆောင်ခြင်း",
    "paṭibhāna": "လျင်မြန်သော ဉာဏ်",
    "paṭibhānena": "လျင်မြန်သော ဉာဏ်",
    "paṭighānusayo": "မုန်းတီးမှု ကိန်းအောင်းခြင်း",
    "paṭisevanā": "ပြန်လည် ပေါင်းသင်းခြင်း",
    "paṭisārambhanā": "ပြန်လည် ပြိုင်ဆိုင်ခြင်း",
    "paṭisārambho": "ပြန်လည် ပြိုင်ဆိုင်မှု",
    "phanditāni": "လှုပ်ရှားမှု",
    "pharusavācatā": "စကား ကြမ်းတမ်းခြင်း",
    "phoṭṭhabbāsā": "အထိအတွေ့ကို မျှော်လင့်ခြင်း",
    "phārusiyaṃ": "ကြမ်းကြုတ်သော အဖြစ်",
    "piṇḍapātika": "ဆွမ်းခံ ဓုတင် ဆောင်ခြင်း",
    "puttāsā": "သားသမီးကို မျှော်လင့်ခြင်း",
    "pāpamittatā": "မိတ်ဆွေဆိုးနှင့် ပေါင်းသင်းခြင်း",
    "pāpanā": "အသရေဖျက်ခြင်း",
    "pāpicchatā": "ယုတ်မာသော အလိုရှိခြင်း",
    "pāribhaṭayatā": "ကလေးထိန်းသကဲ့သို့ ချော့မော့ခြင်း",
    "pāripūri": "ကိုယ်အင်္ဂါ ပြည့်စုံခြင်း",
    "pāripūrimado": "ကိုယ်အင်္ဂါ ပြည့်စုံခြင်းကြောင့် မူးယစ်မှု",
    "rasāsā": "အရသာကို မျှော်လင့်ခြင်း",
    "rattaññu": "ရဟန်းဝါ ကြာမြင့်ခြင်း",
    "rosanā": "ဒေါသ ထွက်စေခြင်း",
    "rūpataṇhā": "@alt",
    "rūpāsā": "အဆင်းအရောင်ကို မျှော်လင့်ခြင်း",
    "saddāsā": "အသံကို မျှော်လင့်ခြင်း",
    "sadisassa": "တူညီသူ ဖြစ်လျက်",
    "sakkāra": "အပူဇော်ခံရခြင်း",
    "sallapanā": "ရင်းနှီးစွာ ပြောဆိုခြင်း",
    "sallā": "ငြောင့်",
    "samannāhāro": "စိတ်ကို ဆောင်ခြင်း",
    "samphappalāpo": "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား",
    "sampāpanā": "အလွန် အသရေဖျက်ခြင်း",
    "samukkhepanā": "အလွန် မြှောက်ပင့်ခြင်း",
    "samullapanā": "အလွန် မြှောက်ပင့် ပြောဆိုခြင်း",
    "samunnahanā": "အလွန် ချည်နှောင်သကဲ့သို့ ပြောခြင်း",
    "sannamanā": "ကွေးညွတ်ခြင်း",
    "saññāvipariyāso": "မှတ်သိမှု ပြောင်းပြန်",
    "saññī": "မှတ်သိမှု ရှိသူ",
    "saṃsaggārāmatā": "ရောနှောခြင်းကို နှစ်သက်ခြင်း",
    "saṅgā": "တွယ်ငြိမှု",
    "saṅkhatāni": "ပြုပြင်ထားမှု",
    "saṅkhipanā": "အလွန် ပစ်ချခြင်း",
    "saṇṭhapanā": "ကောင်းစွာ တည်ထားခြင်း",
    "saṇṭhāna": "ကိုယ်ဟန် ပုံသဏ္ဌာန် လှပခြင်း",
    "saṭhaṃ": "စဉ်းလဲမှု",
    "sippa": "အတတ်ပညာ",
    "sippāyatanena": "အတတ်ပညာ",
    "siṅgaṃ": "ကြွားလုံး ထုတ်မှု",
    "siṅgāratā": "ကြွားလုံး ထုတ်ခြင်း",
    "somanassupavicārā": "ဝမ်းမြောက်ဖွယ်၌ စိတ် လှည့်လည်မှု",
    "sotaṃ": "ရေစီးကြောင်း",
    "subha": "တင့်တယ်၏",
    "suddo": "သူဆင်းရဲမျိုး",
    "sukha": "ချမ်းသာ၏",
    "suta": "အကြားအမြင်",
    "sutena": "အကြားအမြင်",
    "sāmantajappā": "အနီးအနား စကား ပြောခြင်း",
    "sārambhanā": "ပြိုင်ဆိုင်ခြင်း",
    "sārambho": "ပြိုင်ဆိုင်မှု",
    "sāṭheyyaṃ": "စဉ်းလဲသော အဖြစ်",
    "tamāni": "အမှောင်",
    "tandimanakatā": "ပျင်းရိငိုက်မျဉ်းသော စိတ် ရှိခြင်း",
    "tandiyanā": "ပျင်းရိငိုက်မျဉ်းခြင်း",
    "tandī": "ပျင်းရိငိုက်မျဉ်းမှု",
    "taṃsampavaṅkatā": "ထိုသူတို့ဘက်သို့ ညွတ်ကိုင်းခြင်း",
    "taṇhuppādā": "တပ်မက်မှု ဖြစ်ပေါ်ရာ",
    "taṇhāvicaritāni": "တပ်မက်မှု၏ ဖြစ်ပုံ",
    "thambho": "တောင့်တင်းမှု",
    "thīyanā": "ထိုင်းမှိုင်းခြင်း",
    "tintiṇaṃ": "ငမ်းငမ်းတက် မြည်တမ်းမှု",
    "tintiṇāyanā": "ငမ်းငမ်းတက် မြည်တမ်းခြင်း",
    "titthāyatanāni": "အယူဝါဒတို့၏ တည်ရာ",
    "ucchedadiṭṭhi": "အတ္တသည် ပြတ်စဲသွားသည်ဟူသော အယူ",
    "ujucittatā": "စိတ် ခေါင်းမာခြင်း",
    "ukkaṇṭhitā": "ငြီးငွေ့ခြင်း",
    "ukkhepanā": "မြှောက်ပင့်ခြင်း",
    "ukkācanā": "ချီးမွမ်း ပြောဆိုခြင်း",
    "unnahanā": "ချည်နှောင်သကဲ့သို့ ပြောခြင်း",
    "unnāmo": "ခေါင်းမော့ခြင်း",
    "upanayhanā": "ရန်ငြိုး သိုထားခြင်း",
    "upanāho": "ရန်ငြိုး သိုထားမှု",
    "upavicarati": "စိတ်ဖြင့် လှည့်လည် ချဉ်းကပ်သည်",
    "upekkhupavicārā": "လျစ်လျူရှုဖွယ်၌ စိတ် လှည့်လည်မှု",
    "upekkhāṭṭhāniyaṃ": "လျစ်လျူရှုဖွယ် ဖြစ်သော",
    "upārambhacittatā": "အပြစ်ရှာလိုသော စိတ် ရှိခြင်း",
    "upārambhanā": "အပြစ်ရှာခြင်း",
    "upārambho": "အပြစ်ရှာမှု",
    "uññā": "အထင်သေးခြင်း",
    "vacīduccaritaṃ": "နှုတ်ဖြင့် ပြုသော ဒုစရိုက်",
    "vambhanā": "နှိမ့်ချ ပြောခြင်း",
    "vañcanā": "လိမ်လည်ခြင်း",
    "vaṅkatā": "ကွေးကောက်ခြင်း",
    "vaṇṇa": "အဆင်းလှခြင်း",
    "vaṇṇapokkharatāya": "အဆင်းလှခြင်း",
    "verā": "ရန်",
    "vesso": "ကုန်သည်မျိုး",
    "vibhavadiṭṭhi": "ဘဝ ပျောက်ကွယ်သည်ဟူသော အယူ",
    "vibhavataṇhā": "ဘဝ ပျောက်ကွယ်ခြင်းကို တပ်မက်မှု",
    "vibhūsanā": "တန်ဆာဆင်ခြင်း",
    "vicikicchānusayo": "ယုံမှားမှု ကိန်းအောင်းခြင်း",
    "vidhā": "နှိုင်းယှဉ် ချိန်ဆမှု",
    "vihesā": "နှိပ်စက်မှု",
    "viheṭhanā": "ညှဉ်းဆဲခြင်း",
    "vihiṃsanā": "ညှဉ်းပန်းခြင်း",
    "vihiṃsādhātu": "ညှဉ်းပန်းမှု ဓာတ်",
    "vihiṃsāvitakko": "ညှဉ်းပန်းမှုဆိုင်ရာ စတင်ကြံစည်မှု",
    "vijambhitā": "သမ်းဝေ ကိုင်းညွတ်မှု",
    "vijjāṭṭhānena": "ပညာရပ်",
    "vikiraṇā": "ဖုံးကွယ်ရန် ဖြန့်ကြဲခြင်း",
    "vinamanā": "အမျိုးမျိုး ကိုင်းညွတ်ခြင်း",
    "vinicchayo": "ဆုံးဖြတ်ခြင်း",
    "vipariyāsā": "ပြောင်းပြန် ယူဆမှု",
    "virosanā": "အလွန် ဒေါသ ထွက်စေခြင်း",
    "visamaṃ": "ဖောက်ပြန်မှု",
    "visamāni": "ဖောက်ပြန်မှု",
    "vocchādanā": "ကောင်းစွာ ဖုံးအုပ်ခြင်း",
    "vossaggo": "လွှတ်ထားခြင်း",
    "yasa": "ကျော်ကြားမှု",
    "yobbana": "ပျိုရွယ်ခြင်း",
    "yugaggāho": "တန်းတူ ဆွဲကိုင်ခြင်း",
    "Ñātake": "ဆွေမျိုး",
    "ābhogo": "စိတ်ညွတ်ခြင်း",
    "ālapanā": "စကား စ၍ ပြောခြင်း",
    "ālasyaṃ": "ပျင်းရိခြင်း",
    "ālasyāyanā": "ပျင်းရိနေခြင်း",
    "ānamanā": "ကိုင်းညွတ်ခြင်း",
    "ārogya": "အနာကင်းခြင်း",
    "āroha": "အရပ်အမောင်း မြင့်ခြင်း",
    "āsīsanā": "တောင့်တခြင်း",
    "āvaṭṭanā": "လှည့်ခြင်း",
    "āyūhanī": "ကြိုးပမ်းစေတတ်သူ",
    "ṭhapanā": "တည်ထားခြင်း",
    # --- per keyword, read in the segments (this chapter)
    # headings
    "Khuddaka": "အသေးစား",
    "Ekaka": "တစ်မျိုးတွဲ",
    "Ekakaṃ": "တစ်မျိုးတွဲ",
    "Catukka": "လေးမျိုးတွဲ",
    "Catukkaṃ": "လေးမျိုးတွဲ",
    "Pañcaka": "ငါးမျိုးတွဲ",
    "Pañcakaṃ": "ငါးမျိုးတွဲ",
    "Chakka": "ခြောက်မျိုးတွဲ",
    "Chakkaṃ": "ခြောက်မျိုးတွဲ",
    "Sattaka": "ခုနစ်မျိုးတွဲ",
    "Sattakaṃ": "ခုနစ်မျိုးတွဲ",
    "Aṭṭhaka": "ရှစ်မျိုးတွဲ",
    "Aṭṭhakaṃ": "ရှစ်မျိုးတွဲ",
    "Navaka": "ကိုးမျိုးတွဲ",
    "Navakaṃ": "ကိုးမျိုးတွဲ",
    "Dasaka": "ဆယ်မျိုးတွဲ",
    "ādī": "စသည်",
    "ādi": "စသည်",
    "icchatā": "@alt",
    "vutti": "ဆက်ဆံမှု",
    "Asabhāga": "မလျော်ကန်သော",
    "asabhāga": "မလျော်ကန်သော",
    "sammado": "မူးမော့မှု",
    "Bhatta": "အစာ",
    "līnattaṃ": "တွန့်ဆုတ်နေမှု",
    "nijigīsanatā": "ရှာခြင်း",
    "lābhaṃ nijigīsanatā": "လာဘ်ကို ရှာခြင်း",
    "Sadisohamasmīti": "ငါသည် တူညီသူ ဖြစ်သည်",
    "Hīnohamasmīti": "ငါသည် ယုတ်ညံ့သူ ဖြစ်သည်",
    "ātimāno": "အလွန် မာနထားမှု",
    "Ñāti": "ဆွေမျိုး",
    "Janapada": "ဇာတိ ဇနပုဒ်",
    "Amara": "မသေခြင်း",
    "paṭisaṃyutto": "စပ်ယှဉ်သော",
    "Parānuddayatāpaṭisaṃyutto": "သူတစ်ပါးကို စာနာခြင်းနှင့် စပ်ယှဉ်သော",
    "ānuddayatā": "စာနာခြင်း",
    "paṭisaṃyutto vitakko": "စပ်ယှဉ်သော စတင်ကြံစည်မှု",
    "Anavaññatti": "အထင်မသေးခံရခြင်း",
    "macchariyañca": "ဝန်တိုမှု",
    "sāṭheyyañca": "စဉ်းလဲသော အဖြစ်",
    "Antavā": "@alt",
    "antavā": "@alt",
    "anantavā": "@alt",
    "Anantavā": "@alt",
    "ānudiṭṭhi": "@alt",
    "asoraccañca": "မယဉ်ကျေးခြင်း",
    "Asākhalyañca": "စကား မချိုသာခြင်း",
    "asākhalyañca": "စကား မချိုသာခြင်း",
    "aguttadvāratā": "တံခါးကို မစောင့်ထိန်းခြင်း",
    "Muṭṭhassaccañca": "သတိလစ်ခြင်း",
    "muṭṭhassaccañca": "သတိလစ်ခြင်း",
    "Ajjhatta": "အတွင်းပိုင်း",
    "ajjhatta": "အတွင်းပိုင်း",
    "saṃyojanañca": "နှောင်ကြိုး",
    "āyatanāni": "တည်ရာ",
    "assāda": "သာယာမှု",
    "cariyā": "အကျင့်",
    "adhamma": "တရားနှင့် မညီသော",
    "nānatta": "အမျိုးမျိုးသော",
    "kamyatā": "လိုခြင်း",
    "saddhammaṃ": "သူတော်ကောင်းတရား",
    "upārambha": "အပြစ်ရှာလိုသော",
    "magga": "လမ်း",
    "kummagga": "လမ်းမှား",
    "ganthādī": "အထုံး … စသည်",
    "uppādā": "ဖြစ်ပေါ်ရာ",
    "gamanāni": "လိုက်ခြင်း",
    "anariya": "အရိယာ မဟုတ်သူ",
    "vohārā": "ပြောဆိုမှု",
    "khilā": "ခက်ထန်မှု",
    "ceto": "စိတ်",
    "vinibandhā": "ချည်နှောင်ထားသော အရာ",
    "ānantarikāni": "ချက်ချင်း အကျိုးပေးသော",
    "ādīnavā": "အပြစ်",
    "akkhantiyā": "မသည်းခံခြင်း",
    "vādā": "ဝါဒ",
    "nibbānavādā": "နိဗ္ဗာန်ဟု ဆိုသော ဝါဒ",
    "vivāda": "အငြင်းပွားမှု",
    "vatthūni": "@alt",
    "virodha": "ဆန့်ကျင်မှု",
    "kāyā": "အစု",
    "parihāniyā": "ဆုတ်ယုတ်စေတတ်သော",
    "upavicārā": "စိတ် လှည့်လည်မှု",
    "gehasitāni": "လောကီ အိမ်ရာကို မှီသော",
    "gehasitā": "လောကီ အိမ်ရာကို မှီသော",
    "somanassāni": "ဝမ်းမြောက်မှု",
    "domanassāni": "စိတ်ဆင်းရဲမှု",
    "ānusayā": "ကိန်းအောင်းခြင်း",
    "kusīta": "ပျင်းရိမှု",
    "paṭighāto": "ထိခိုက်မှု",
    "dosā": "အပြစ်",
    "purisa": "လူ",
    "asaññī": "@alt",
    "nevasaññīnāsaññī": "@alt",
    "āghāta": "ရန်ငြိုးဖွဲ့ခြင်း",
    "Navavidhā": "ကိုးမျိုးသော",
    "navavidhā": "ကိုးမျိုးသော",
    "mūlakā": "အမြစ်ပြုသော",
    "maññitādīni": "ထင်မှတ်မှု … စသည်",
    "ādīni": "စသည်",
    "Dasa saṃyojanāni": "နှောင်ကြိုး ဆယ်ပါး",
    "dasa saṃyojanāni": "နှောင်ကြိုး ဆယ်ပါး",
    "Dasa micchattā": "မှားယွင်းမှု ဆယ်ပါး",
    "dasa micchattā": "မှားယွင်းမှု ဆယ်ပါး",
    "vatthukā": "အကြောင်းအရာ … ရှိသော",
    "Dasavatthukā": "အကြောင်းအရာ ဆယ်ပါး ရှိသော",
    "dasavatthukā": "အကြောင်းအရာ ဆယ်ပါး ရှိသော",
    "antaggāhikā": "အစွန်းကို စွဲကိုင်သော",
    "vicarita": "ဖြစ်ပုံ",
    "Taṇhāvicarita": "တပ်မက်မှု၏ ဖြစ်ပုံ",
    "Ajjhattikassa": "အတွင်း",
    "ajjhattikassa": "အတွင်း",
    "Bāhirassa": "အပြင်",
    "bāhirassa": "အပြင်",
    "Yā": "(no direct equivalent)",
    "yā": "(no direct equivalent)",
    "uccheda": "@alt",
    "siloka": "ကျော်စောမှု",
    "nevasaññināsaññi": "@alt",
    "asaññi": "@alt",
    "bhagavatā": "မြတ်စွာဘုရား",
    "veyyākaraṇe": "ဒေသနာ",
    "gatāni": "(no direct equivalent)",
    "sataṃ": "တစ်ရာ",
    "dvāsaṭṭhi": "ခြောက်ဆယ့်နှစ်ပါး",
    "vuttāni": "ဟောတော်မူခဲ့သော",
    "chattiṃsa": "သုံးဆယ့်ခြောက်ပါး",
    "vicaritāni": "ဖြစ်ပုံ",
    "Jātiṃ paṭicca": "ဇာတိကို စွဲ၍",
    "Jātiṃ": "ဇာတိ",
    "piṇḍapātikattaṃ": "ဆွမ်းခံ ဓုတင် ဆောင်ခြင်း",
    "vaṇṇaṃ": "အဆင်းလှခြင်း",
    "pariṇāhaṃ": "ကိုယ်လုံး ပြည့်ဖြိုးခြင်း",
    "Gottaṃ": "အမျိုးအနွယ်",
    "pāripūriṃ": "ကိုယ်အင်္ဂါ ပြည့်စုံခြင်း",
    "sippaṃ": "အတတ်ပညာ",
    "iriyāpathaṃ": "ကိုယ်ဟန် အမူအရာ",
    "anavaññātaṃ": "အထင်မသေးခံရခြင်း",
    "yasaṃ": "ကျော်ကြားမှု",
    "saṇṭhānaṃ": "ကိုယ်ဟန် ပုံသဏ္ဌာန် လှပခြင်း",
    "ārogyaṃ": "အနာကင်းခြင်း",
    "ārohaṃ": "အရပ်အမောင်း မြင့်ခြင်း",
    "sakkāraṃ": "အပူဇော်ခံရခြင်း",
    "sutaṃ": "အကြားအမြင်",
    "jīvitaṃ": "အသက်ရှင်ခြင်း",
    "jīvita": "@alt",
    "paṭibhānaṃ": "လျင်မြန်သော ဉာဏ်",
    "garukāraṃ": "အလေးပြုခံရခြင်း",
    "rattaññutaṃ": "ရဟန်းဝါ ကြာမြင့်ခြင်း",
    "iddhiṃ": "တန်ခိုး",
    "sīlaṃ": "သီလ",
    "bhogaṃ": "စည်းစိမ်ဥစ္စာ",
    "yobbanaṃ": "ပျိုရွယ်ခြင်း",
    "vuttitā": "အကျင့် ရှိခြင်း",
    "Kāyaduccarite": "ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်",
    "vacīduccarite": "နှုတ်ဖြင့် ပြုသော ဒုစရိုက်",
    "manoduccarite": "မနောဖြင့် ပြုသော ဒုစရိုက်",
    "duccarite": "ဒုစရိုက်",
    "anaṭṭhita": "တည်တံ့စွာ မပြုခြင်း",
    "cittassa vossaggo": "စိတ်ကို လွှတ်ထားခြင်း",
    "nikkhitta": "ချထားသော",
    "ānuppadānaṃ": "ထပ်ကာထပ်ကာ ပြုခြင်း",
    "guṇesu": "ဂုဏ်",
    "kāmaguṇesu": "ကာမဂုဏ်",
    "dhammānaṃ": "သဘောတရား",
    "kusalānaṃ vā dhammānaṃ": "ကုသိုလ် သဘောတရား",
    "piṇḍapāta": "ဆွမ်း",
    "asantuṭṭhassa": "ရောင့်ရဲမှု မရှိသူ",
    "senāsana": "ကျောင်းအိပ်ရာနေရာ",
    "bhesajja": "ဆေး",
    "cīvara": "သင်္ကန်း",
    "Cīvara": "သင်္ကန်း",
    "gilāna": "သူနာ",
    "guṇehi": "ဂုဏ်",
    "kāmaguṇehi": "ကာမဂုဏ်",
    "paccaya": "အထောက်အပံ့",
    "bhiyyokamyatā": "ပို၍ လိုချင်ခြင်း",
    "Itarītara": "ရရှိသမျှ",
    "dussīlo": "သီလ ပျက်သူ",
    "samāhitoti": "စိတ် တည်ကြည်သူ",
    "assaddho": "ယုံကြည်မှု မရှိသူ",
    "Assaddho": "ယုံကြည်မှု မရှိသူ",
    "ārāmo": "နှစ်သက်သူ",
    "akhīṇāsavo": "စိတ်အစွန်းအထင်း မကုန်သေးသူ",
    "āraddhavīriyoti": "ဝီရိယ အားထုတ်ထားသူ",
    "upaṭṭhitassatīti": "သတိ တည်ထားသူ",
    "muṭṭhassatī": "သတိ လစ်သူ",
    "jānātū": "သိသည်",
    "kusīto": "ပျင်းရိသူ",
    "bahussutoti": "အကြားအမြင် များသူ",
    "appassuto": "အကြားအမြင် နည်းသူ",
    "jano": "လူ",
    "pavivittoti": "ကင်းဆိတ်စွာ နေသူ",
    "asamāhito": "စိတ် မတည်ကြည်သူ",
    "sīlavāti": "သီလ ရှိသူ",
    "duppañño": "ပညာ နည်းသူ",
    "paññavāti": "ပညာ ရှိသူ",
    "icchati": "အလိုရှိသည်",
    "kamyatā": "@alt",
    "patta": "သပိတ်",
    "bāhirānaṃ": "ပြင်ပ",
    "pūti": "ပုပ်စပ်သော",
    "parikkhārānaṃ": "အသုံးအဆောင်",
    "bhātari": "ညီအစ်ကို",
    "buddhe": "ဘုရား",
    "sāvakesu": "တပည့်သာဝက",
    "jeṭṭhe": "အကြီးအကဲ",
    "pitari": "အဖ",
    "ggāhitā": "ယူခြင်း",
    "Mātari": "အမိ",
    "aññataraññataresu": "တစ်ဦးဦး",
    "ṭhāniyesu": "ထိုက်သော",
    "garu": "အလေးပြု",
    "upajjhāye": "ဥပဇ္ဈာယ်ဆရာ",
    "ācariyesu": "ဆရာ",
    "senāsanesu": "ကျောင်းအိပ်ရာနေရာ",
    "Pantesu": "ဆိတ်ငြိမ်ရာ",
    "dhammesu": "သဘောတရား",
    "jambhanā": "သမ်းဝေခြင်း",
    "pariḷāho": "ပူလောင်ခြင်း",
    "bhuttāvissa": "စားပြီးသူ",
    "duṭṭhullaṃ": "လေးလံခြင်း",
    "kilamatho": "ပင်ပန်းခြင်း",
    "akalyatā": "မကျန်းမာခြင်း",
    "iriyāpathassa": "ကိုယ်ဟန် အမူအရာ",
    "icchā": "@alt",
    "pāpicchassa": "ယုတ်မာသော အလိုရှိသော",
    "pāpiccho": "ယုတ်မာသော အလိုရှိသော",
    "pakatassa": "နှိပ်စက်ခံရသော",
    "pakato": "နှိပ်စက်ခံရသော",
    "icchāpakatassa": "အလိုဆန္ဒ နှိပ်စက်ခံရသော",
    "icchāpakato": "အလိုဆန္ဒ နှိပ်စက်ခံရသော",
    "saṅkhātena": "ဟူသော နည်း",
    "sannissitassa": "မှီသော",
    "sannissito": "မှီသော",
    "Lābhasakkārasilokasannissitassa": "လာဘ် အပူဇော်ခံရခြင်း ကျော်စောမှုကို မှီသော",
    "Lābhasakkārasilokasannissito": "လာဘ် အပူဇော်ခံရခြင်း ကျော်စောမှုကို မှီသော",
    "paccaya": "@alt",
    "sāmantajappitena": "အနီးအနား စကား ပြောခြင်း",
    "jappitena": "စကား ပြောခြင်း",
    "paresaṃ": "သူတစ်ပါး",
    "jappā": "စကား ပြောခြင်း",
    "hārikā": "ဆောင်ခြင်း",
    "avaṇṇa": "ကဲ့ရဲ့ သတင်း",
    "āharati": "ဆောင်သည်",
    "harati": "ဆောင်သည်",
    "pokkharatāya": "လှခြင်း",
    "ṭṭhānena": "(no direct equivalent)",
    "āyatanena": "(no direct equivalent)",
    "mānaṃ": "မာန",
    "vatthunā": "အကြောင်း",
    "jappeti": "ဖြစ်ပေါ်စေသည်",
    "mānaṃ jappeti": "မာနကို ဖြစ်ပေါ်စေသည်",
    "omānaṃ jappeti": "ယုတ်ညံ့ဟု ထင်မှတ်မှုကို ဖြစ်ပေါ်စေသည်",
    "attānaṃ": "မိမိကိုယ်",
    "parehi": "သူတစ်ပါး",
    "dahati": "ထားသည်",
    "sadisaṃ": "တူညီသူ",
    "atimaññati": "အလွန် မြင့်မြတ်သည်ဟု ထင်မှတ်သည်",
    "aparakālaṃ": "နောက်ပိုင်း အချိန်",
    "adhigata": "ရရှိသော",
    "kata": "ပြုပြီးသော",
    "sacchikata": "မျက်မှောက်ပြုပြီးသော",
    "chando": "ဆန္ဒ",
    "pāpakena": "ယုတ်မာသော",
    "pāpakena vā kammāyatanena": "ယုတ်မာသော အလုပ်အကိုင်",
    "vatena": "အကျင့်ဝတ်",
    "diṭṭhiyā": "အယူ",
    "sīlena": "သီလ",
    "sīlabbatena": "သီလ အကျင့်ဝတ်",
    "pariḷāho": "@alt",
    "chando": "@alt",
    "ajjhosānaṃ": "@alt",
    "ārabbha": "@alt",
    "gehasito": "လောကီ အိမ်ရာကို မှီသော",
    "geha": "လောကီ အိမ်ရာ",
    "Dukkara": "ပြုနိုင်ခဲသော အကျင့်",
    "kāritā": "ကျင့်ခြင်း",
    "gata": "(no direct equivalent)",
    "uppannesu": "ဖြစ်ပေါ်လာသော",
    "karaṇīyesu": "ပြုဖွယ်",
    "kicca": "ကိစ္စ",
    "yogaṃ": "(no direct equivalent)",
    "āpajjati": "ဝင်ရောက် ဆောင်ရွက်သည်",
    "sukhitesu": "ချမ်းသာသူ",
    "attanā": "မိမိကိုယ်တိုင်",
    "gihīhi": "လူဝတ်ကြောင်",
    "saṃsaṭṭho": "ရောနှောသော",
    "dukkhito": "ဆင်းရဲသော",
    "sahanandī": "အတူ ဝမ်းမြောက်သော",
    "sahasokī": "အတူ စိုးရိမ်သော",
    "avajāniṃsūti": "အထင်သေးသည်",
    "pare": "သူတစ်ပါး",
    "tattha": "ထိုတို့အနက်",
    "vivāda": "@alt",
    "sakkāra": "@alt",
    "garukāra": "@alt",
    "vaṇṇa": "@alt",
    "paṭicchādanahetuṃ": "ဖုံးကွယ်ရန် အလို့ငှာ",
    "caritvā": "ကျင့်၍",
    "pāpikaṃ": "ယုတ်မာသော",
    "paṇidahati": "ထားသည်",
    "saṅkappeti": "ကြံစည်သည်",
    "jaññā": "သိသည်",
    "bhāsati": "ပြောသည်",
    "vācāya": "နှုတ်",
    "parakkamati": "ကြိုးပမ်းသည်",
    "parisaṭho": "အလွန် စဉ်းလဲသူ",
    "saṭho": "စဉ်းလဲသူ",
    "icchaṃ": "အလို",
    "vācaṃ": "စကား",
    "ggāho": "စွဲကိုင်ခြင်း",
    "uppajjati": "ဖြစ်ပေါ်လာသည်",
    "uppajjati diṭṭhi": "ဖြစ်ပေါ်လာသော အယူ",
    "gataṃ": "(no direct equivalent)",
    "assaddhā": "ယုံကြည်မှု မရှိသော",
    "vippaṭikula": "ဆန့်ကျင်ဘက်",
    "appassutā": "အကြားအမြင် နည်းသော",
    "Kāyiko": "ကိုယ်ပိုင်းဆိုင်ရာ",
    "kāyiko": "ကိုယ်ပိုင်းဆိုင်ရာ",
    "vācasiko": "နှုတ်ပိုင်းဆိုင်ရာ",
    "kaṭukā": "ခါးသက်စေသော",
    "asamādhisaṃvattanikā": "သမာဓိ မဖြစ်စေတတ်သော",
    "saṃvattanikā": "@alt",
    "ābhisajjanī": "ထိခိုက်စေသော",
    "kaṇḍakā": "ဆူးကဲ့သို့ စူးသော",
    "appaṭisanthārako": "ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း မရှိသူ",
    "bhāsitā": "ပြောဆိုသူ",
    "abhijjhādomanassā": "သူ့ဥစ္စာကို လိုချင်ခြင်း စိတ်ဆင်းရဲမှု",
    "domanassā": "စိတ်ဆင်းရဲမှု",
    "indriyaṃ asaṃvutaṃ": "စွမ်းရည်ကို မစောင့်စည်းသော",
    "manindriyaṃ asaṃvutaṃ": "မနော၏ စွမ်းရည်ကို မစောင့်စည်းသော",
    "ggāhī": "စွဲယူသူ",
    "āpajjati": "@alt",
    "saṃvaraṃ āpajjati": "စောင့်စည်းမှု ပြုသည်",
    "pavedentī": "ဟောကြားသည်",
    "sayaṃ": "ကိုယ်တိုင်",
    "bahiddhā": "@alt",
    "piyassa": "ချစ်သော",
    "manāpassa": "နှစ်သက်သော",
    "appiyassa": "မချစ်သော",
    "amanāpassa": "မနှစ်သက်သော",
    "carati": "ပြုသည်",
    "anatthaṃ": "အကျိုးမဲ့",
    "jappā": "@alt",
    "paṭighāto": "@alt",
    "adhamma": "@alt",
    "vibhava": "@alt",
    "Kāmapaṭisaṃyutto": "ကာမနှင့် စပ်ယှဉ်သော",
    "Kāmapaṭisaṃyuttā": "ကာမနှင့် စပ်ယှဉ်သော",
    "paṭisaṃyuttā": "စပ်ယှဉ်သော",
    "pisuṇā": "ကုန်းတိုက်သော",
    "Musā": "မုသား",
    "musā": "မုသား",
    "pharusā": "ကြမ်းတမ်းသော",
    "ātipāto": "သတ်ခြင်း",
    "ādānaṃ": "ယူခြင်း",
    "saṅghe": "သံဃာတော်",
    "vicikicchati": "ယုံမှားသည်",
    "vantaṃ": "ရှိသော",
    "adassāvī": "မမြင်ဖူးသော",
    "rūpaṃ attato samanupassati": "ရုပ်ကို အတ္တဟု ရှုမြင်သည်",
    "dhātu": "ဘုံ",
    "paraṃ maraṇā": "သေပြီးနောက်",
    "ekaṭṭhaṃ": "တစ်နေရာတည်း တည်ရှိသော",
    "tadekaṭṭhaṃ": "ထိုနှင့် တစ်နေရာတည်း တည်ရှိသော",
    "sadisohamasmī": "ငါသည် တူညီသူ ဖြစ်သည်",
    "hīnohamasmī": "ငါသည် ယုတ်ညံ့သူ ဖြစ်သည်",
    "sīlabbatena": "@alt",
    "dhātu": "@alt",
    "Jāti": "@alt",
    "Jātiṃ": "@alt",
    "Jātiṃ paṭicca": "@alt",
    "utrāso": "ထိတ်လန့်ခြင်း",
    "sampasīdati": "ကြည်လင်သည်",
    "nādhimuccati": "မဆုံးဖြတ်နိုင်သည်",
    "samaṇo": "ရဟန်း",
    "ahetu": "အကြောင်း မရှိသော",
    "appaccayā": "အထောက်အပံ့ မရှိသော",
    "nimmāna": "ဖန်ဆင်းခြင်း",
    "kata": "@alt",
    "paṭisaṃvedeti": "ခံစားရသည်",
    "evaṃdiṭṭhī": "ဤသို့ အယူ ရှိသူ",
    "evaṃvādī": "ဤသို့ ဆိုလေ့ ရှိသူ",
    "adukkhamasukhaṃ": "မနာကျင် မသာယာမှု",
    "purisapuggalo": "ပုဂ္ဂိုလ်",
    "issara": "ဖန်ဆင်းရှင်",
    "diṭṭhī": "အယူ ရှိသော",
    "yaṃ kiñcāyaṃ": "ဤ … သမျှ",
    "doso": "@alt",
    "pātabyataṃ āpajjati": "သောက်သုံးသကဲ့သို့ နစ်မွန်းခြင်းသို့ ရောက်သည်",
    "buddhaṃ": "ဘုရား",
    "saddahati": "ယုံကြည်သည်",
    "saṅghaṃ": "သံဃာ",
    "bhavantattaṃ": "ယိမ်းထိုးနေသော အဖြစ်",
    "buddhā": "ဘုရားရှင်",
    "sāvakā": "တပည့်သာဝက",
    "vippaṭikulena": "ဆန့်ကျင်သော",
    "Anicce": "မမြဲသော",
    "dukkhe": "@alt",
    "asubhe": "မတင့်တယ်သော",
    "uppajjati": "@alt",
    "bhikkhuno": "ရဟန်း",
    "kupito": "အမျက်ထွက်သူ",
    "khilajāto": "ခက်ထန်သော စိတ် ဖြစ်ပေါ်သူ",
    "sabrahmacārīsu": "သီတင်းသုံးဖော်",
    "anattamano": "စိတ် မနှစ်သိမ့်သူ",
    "āhatacitto": "ထိခိုက်သော စိတ် ရှိသူ",
    "ṭṭhānā": "အကြောင်း",
    "pamāda": "မေ့လျော့ခြင်း",
    "surā": "သေရည်",
    "meraya": "သေရက်",
    "majja": "(no direct equivalent)",
    "micchācāro": "မှားယွင်းစွာ ကျင့်ခြင်း",
    "vādo": "ပြောခြင်း",
    "nicca": "မြဲသော",
    "subha": "တင့်တယ်သော",
    "sukha": "@alt",
    "aññathābhāvā": "တစ်မျိုးတစ်ဖုံ ဖြစ်ခြင်း",
    "paricāreti": "မွေ့လျော်သည်",
    "paññapenti": "ပညတ်သည်",
    "paramadiṭṭhadhammanibbānaṃ paññapenti": "မျက်မှောက်ဘဝ၌ အမြတ်ဆုံး နိဗ္ဗာန်ကို ပညတ်သည်",
    "uppilāvitaṃ": "ဖောင်းကြွခြင်း",
    "ābhogo": "@alt",
    "vicāritaṃ": "ဆက်လက်သုံးသပ်ခြင်း",
    "vitakkitaṃ": "စတင်ကြံစည်ခြင်း",
    "vitakkitaṃ vicāritaṃ": "စတင်ကြံစည်ခြင်း ဆက်လက်သုံးသပ်ခြင်း",
    "natthīti": "မရှိသည်",
    "sato": "ရှိနေသော",
    "ettāvatā": "ဤမျှဖြင့်",
    "paramadiṭṭhadhammanibbānappatto": "မျက်မှောက်ဘဝ၌ အမြတ်ဆုံး နိဗ္ဗာန်သို့ ရောက်သော",
    "samappito": "ပြည့်စုံသော",
    "sokaparidevadukkhadomanassupāyāsā": "စိုးရိမ်ခြင်း ငိုကြွေးခြင်း ကိုယ်ဆင်းရဲခြင်း စိတ်ဆင်းရဲမှု ပြင်းစွာ ပူပန်ခြင်း",
    "parama": "အမြတ်ဆုံး",
    "paramadiṭṭhadhammanibbāna": "မျက်မှောက်ဘဝ၌ အမြတ်ဆုံး နိဗ္ဗာန်",
    "evaṃdiṭṭhi": "ဤသို့ အယူ ရှိသူ",
    "aniccā": "မမြဲသော",
    "dukkha": "ကိုယ်ဆင်းရဲခြင်း",
    "Kāmā": "ကာမ",
    "samaṅgībhūto": "ယှဉ်သော",
    "akkhāyati": "ဆိုရသည်",
    "bho": "အချင်း",
    "vadesi": "ပြောသည်",
    "vitakkavicārānaṃ vūpasamā": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်း",
    "vipariṇāmadhammā": "ဖောက်ပြန်ခြင်း သဘော ရှိသော",
    "Yadeva": "(no direct equivalent)",
    "kissa hetu": "အဘယ်ကြောင့်",
    "sandiṭṭhi": "မိမိ အယူ",
    "appatisso": "နာခံမှု မရှိသော",
    "agāravo": "ရိုသေမှု မရှိသော",
    "agāravo viharati": "ရိုသေမှု မရှိ … နေသည်",
    "appamāde": "သတိ မလစ်ခြင်း",
    "paṭisanthāre": "ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း",
    "ārāmatā": "နှစ်သက်ခြင်း",
    "sātaṃ sukhaṃ": "နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော",
    "sātaṃ sukhaṃ vedayitaṃ": "နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော ခံစားရခြင်း",
    "sātā sukhā vedanā": "နှစ်သက်ဖွယ်ကောင်း၍ သာယာသော ခံစားမှု",
    "gehasitaṃ": "လောကီ အိမ်ရာကို မှီသော",
    "cetosamphassa": "စိတ်၏ တွေ့ထိမှု",
    "Manāpiyesu": "စိတ်နှင့် တွေ့သော",
    "rūpesu": "အဆင်းအရောင်",
    "gandhesu": "အနံ့",
    "saddesu": "အသံ",
    "phoṭṭhabbesu": "အထိအတွေ့",
    "rasesu": "အရသာ",
    "jāto": "မွေးဖွားသော",
    "thetato": "ခိုင်မြဲစွာ",
    "sassato": "ထာဝရ တည်သော",
    "nicco": "မြဲသော",
    "dhuvo": "ခိုင်မြဲသော",
    "avipariṇāmadhammo": "ဖောက်ပြန်ခြင်း မရှိသော သဘော ရှိသော",
    "paccanubhoti": "ခံစားသည်",
    "vedeyyo": "ခံစားတတ်သော",
    "vado": "ပြောဆိုတတ်သော",
    "me": "ငါ",
    "anattānaṃ": "အတ္တ မဟုတ်သော",
    "sañjānāmī": "သိသည်",
    "nāhosi": "မဖြစ်ခဲ့သည်",
    "saccato": "အမှန်အားဖြင့်",
    "saccato thetato": "အမှန်အားဖြင့် ခိုင်မြဲစွာ",
    "diṭṭhi uppajjati": "အယူ ဖြစ်ပေါ်သည်",
    "ānusayo": "ကိန်းအောင်းခြင်း",
    "anottappī": "ဒုစရိုက်ကို မကြောက်ရွံ့သူ",
    "ahiriko": "ဒုစရိုက်ကို မရှက်သူ",
    "amanasikārā": "နှလုံး မသွင်းခြင်း",
    "bhedā": "ပြိုကွဲသောအခါ",
    "sabbaṅgapaccaṅgī": "ကြီးငယ် အင်္ဂါ အားလုံး ပြည့်စုံသော",
    "sammā": "@alt",
    "sammā samucchinno": "ကောင်းစွာ ပြတ်စဲသော",
    "ucchedaṃ": "ပြတ်စဲခြင်း",
    "vināsaṃ": "ပျက်စီးခြင်း",
    "vibhavaṃ": "ဘဝ ပျောက်ကွယ်ခြင်း",
    "vinassati": "ပျက်စီးသည်",
    "nānatta": "@alt",
    "nānattasaññānaṃ": "အမျိုးမျိုး ကွဲပြားမှုဟု မှတ်သိမှု",
    "rūpasaññānaṃ": "ရုပ်ဟု မှတ်သိမှု",
    "paṭighasaññānaṃ": "ထိခိုက်မှုဟု မှတ်သိမှု",
    "paṭigha": "ထိခိုက်မှု",
    "dibbo": "နတ်၌ ဖြစ်သော",
    "mahābhūtiko": "မူလဓာတ်ကြီး … ဖြစ်သော",
    "bhūtiko": "မူလဓာတ် … ဖြစ်သော",
    "hoti paraṃ maraṇā": "သေပြီးနောက် ရှိသည်",
    "ettāvatā sammā": "ဤမျှဖြင့် ကောင်းစွာ",
    "ettāvatā sammā samucchinno": "ဤမျှဖြင့် ကောင်းစွာ ပြတ်စဲသော",
    "indriyo": "အာရုံခံ စွမ်းရည် ရှိသော",
    "ahīnindriyo": "မချို့ယွင်းသော အာရုံခံ စွမ်းရည် ရှိသော",
    "pettika": "အဖ",
    "sambhavo": "ဖြစ်ပေါ်လာသော",
    "bhakkho": "စားသော",
    "kabaḷīkāra": "လုတ်ပြု၍ စားရသော အစာ",
    "ākāsānañcāyatanaṃ": "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်",
    "ākiñcaññāyatanaṃ": "ဘာမျှ မရှိသော နယ်ပယ်",
    "ananto": "အဆုံး မရှိသော",
    "jānāsi": "သိသည်",
    "manomayo": "စိတ်ဖြင့် ဖြစ်သော",
    "nevasaññānāsaññāyatanūpago": "မှတ်သိမှု ရှိသည်လည်း မဟုတ် မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်သို့ ရောက်သော",
    "natthi kiñcīti": "ဘာမျှ မရှိသည်",
    "ākiñcaññāyatanūpago": "ဘာမျှ မရှိသော နယ်ပယ်သို့ ရောက်သော",
    "āyatanūpago": "နယ်ပယ်သို့ ရောက်သော",
    "ākāso": "ဟင်းလင်းပြင်",
    "piṇḍāya": "ဆွမ်း",
    "adhigamāya": "ရရှိရန်",
    "anadhigatassa adhigamāya": "မရရှိသေးသည်ကို ရရှိရန်",
    "anadhigatassa": "မရရှိသေးသော",
    "appattassa": "မရောက်သေးသော",
    "appattassa pattiyā": "မရောက်သေးသည်ကို ရောက်ရန်",
    "asacchikatassa": "မျက်မှောက် မပြုရသေးသော",
    "asacchikatassa sacchikiriyāya": "မျက်မှောက် မပြုရသေးသည်ကို မျက်မှောက်ပြုရန်",
    "māsācitaṃ": "ပဲတင်ထားသကဲ့သို့ လေးလံသော",
    "lūkhassa": "ကြမ်းတမ်းသော",
    "paṇītassa": "မွန်မြတ်သော",
    "bhojanassa": "အစာ",
    "karontassa": "ပြုနေသော",
    "kataṃ": "ပြုသော",
    "aṭṭhamaṃ": "အဋ္ဌမ",
    "sattamaṃ": "သတ္တမ",
    "chaṭṭhaṃ": "ဆဋ္ဌမ",
    "vīriyaṃ": "ဝီရိယ",
    "ārabhati": "အားထုတ်သည်",
    "vīriyaṃ ārabhati": "ဝီရိယကို အားထုတ်သည်",
    "kappo": "သင့်လျော်သည်",
    "pāripūriṃ": "@alt",
    "labhati": "ရသည်",
    "alatthaṃ": "ရခဲ့သည်",
    "kusītavatthu": "ပျင်းရိမှု၏ အကြောင်း",
    "kilanto": "ပင်ပန်းသော",
    "kilamissati": "ပင်ပန်းသည်",
    "ābādho": "အနာရောဂါ",
    "maggo": "ခရီး",
    "Handāhaṃ": "ယခု ငါ",
    "nipajjāmī": "လှဲလျောင်းသည်",
    "nipajjati": "လှဲလျောင်းသည်",
    "bhikkhunā": "ရဟန်း",
    "yāvadatthaṃ": "လိုသလောက်",
    "vuṭṭhito": "ထသော",
    "gelaññā": "ဖျားနာခြင်း",
    "appamattako": "အနည်းငယ်သော",
    "Tassa evaṃ hoti": "ထိုရဟန်းအား ဤသို့ အကြံ ဖြစ်သည်",
    "nigamaṃ": "နိဂုံး",
    "gāmaṃ": "ရွာ",
    "akammañño": "အလုပ်နှင့် မလျော်သော",
    "caranto": "လှည့်လည်သော",
    "piṇḍāya caranto": "ဆွမ်းခံ လှည့်လည်သော",
    "dubbalo": "အားနည်းသော",
    "nindāya": "ကဲ့ရဲ့ခြင်း",
    "ayase": "အခြံအရံ မရခြင်း",
    "yase": "အခြံအရံ ရခြင်း",
    "sukhe": "ချမ်းသာ",
    "pasaṃsāya": "ချီးမွမ်းခြင်း",
    "suta": "@alt",
    "viññāta": "သိသော",
    "muta": "ထိတွေ့သော",
    "paṭikarohī": "ကုစားသည်",
    "kopañca": "အမျက်",
    "paṭicarati": "လွှဲရှောင်သည်",
    "bāhā": "လက်",
    "vikkhepakaṃ": "ဝှေ့ယမ်းသော",
    "apanāmeti": "လွှဲသည်",
    "sāpattikova": "အာပတ် ရှိသော",
    "byāvaṭā": "ဂရုစိုက်နေသည်",
    "bhikkhuṃ": "ရဟန်း",
    "bhikkhū": "ရဟန်း",
    "codenti": "စောဒနာသည်",
    "codiyamāno": "စောဒနာခံရသော",
    "codakaṃyeva": "စောဒနာသူကိုသာ",
    "āpanno": "ရောက်ခဲ့သော",
    "pātukaroti": "ထင်ရှားစေသည်",
    "appaccayañca": "မနှစ်သက်မှု",
    "dosañca": "ဒေါသ",
    "anādiyitvā": "အလေးမထား၍",
    "aṭṭhamo": "အဋ္ဌမ",
    "pañcamo": "ပဉ္စမ",
    "sattamo": "သတ္တမ",
    "chaṭṭho": "ဆဋ္ဌမ",
    "nibbeṭheti": "ငြင်းဆိုသည်",
    "atibāḷhaṃ": "အလွန်အမင်း",
    "bālassa": "မိုက်မဲသော",
    "abyattassa": "မလိမ္မာသော",
    "assatiyāva": "သတိ မရှိဟန်ဖြင့်သာ",
    "pakkamati": "ထွက်သွားသည်",
    "hīnāyāvattissāmī": "လူဘောင်သို့ ပြန်လည်သည်",
    "āvattissāmī": "ပြန်လည်သည်",
    "āvattitvā": "ပြန်လည်ပြီး",
    "yenakāmaṃ": "အလိုရှိရာ",
    "majjhe": "အလယ်",
    "āpattiyā": "အာပတ်",
    "āyasmanto": "အသျှင်",
    "nāma": "ပင်လျှင်",
    "tuṇhībhūto": "ဆိတ်ဆိတ် နေသော",
    "sarāmi": "မှတ်မိသည်",
    "paccakkhāya": "စွန့်၍",
    "attamanā": "စိတ်ကျေနပ်သည်",
    "paṭippharati": "ပြန်လည် တိုက်ခိုက်သည်",
    "bhaṇitabbaṃ": "ပြောဆိုထိုက်သော",
    "bhaṇati": "ပြောဆိုသည်",
    "itthannāmaṃ": "ဤမည်သော",
    "bhaṇitena": "ပြောဆိုမှု",
    "aññenāññaṃ": "တစ်ခုဖြင့် တစ်ခု",
    "paccāropeti": "ပြန်လည် စွပ်စွဲသည်",
    "sikkhaṃ": "သိက္ခာ",
    "viheseti": "နှောင့်ယှက်သည်",
    "kiṃ nu kho": "အဘယ်",
    "arogo": "အနာကင်းသော",
    "arogo paraṃ maraṇā": "သေပြီးနောက် အနာကင်းသော",
    "nāsaññī": "မရှိသည်လည်း မဟုတ်သော",
    "saññīnāsaññī": "@alt",
    "tuvaṃtuvaṃ": "နင် ငါ ပြောဆိုခြင်း",
    "viggaha": "ငြင်းခုံ",
    "pesuñña": "ကုန်းတိုက်ခြင်း",
    "musāvādā": "မုသား ပြောခြင်း",
    "ādhikaraṇaṃ": "ကြောင့်",
    "kalaha": "ခိုက်ရန်ဖြစ်ခြင်း",
    "vādā": "@alt",
    "daṇḍādāna": "တုတ်ကိုင်ခြင်း",
    "ādāna": "ကိုင်ခြင်း",
    "satthādāna": "လက်နက်ကိုင်ခြင်း",
    "iñjitametaṃ": "ဤတုန်လှုပ်မှု",
    "saṅkhatametaṃ": "ဤပြုပြင်ထားမှု",
    "paṭigha": "@alt",
    "sammaggatā": "မှန်ကန်စွာ ရောက်ရှိသော",
    "sukata": "ကောင်းစွာ ပြုသော",
    "sarīra": "ကိုယ်ခန္ဓာ",
    "sassato": "@alt",
    "Sassato": "@alt",
    "aṭṭhārasa": "ဆယ့်ရှစ်ပါး",
    "asasmīti": "ငါ အမြဲ ရှိသည်",
    "aññathāsmīti": "ငါ အခြားတစ်မျိုး ဖြစ်သည်",
    "sātasmīti": "ငါ ပြတ်စဲသည်",
    "upanidhāya": "နှိုင်းယှဉ်၍",
    "vinassissāmi": "ငါ ပျက်စီးသည်",
    "niccosmi": "ငါ မြဲသည်",
    "dhuvosmi": "ငါ ခိုင်မြဲသည်",
    "sassatosmi": "ငါ ထာဝရ တည်သည်",
    "avipariṇāmadhammosmīti": "ငါ ဖောက်ပြန်ခြင်း မရှိသော သဘော ရှိသည်",
    "anavakāriṃ": "မခွဲခြားသော",
    "Kañci dhammaṃ anavakāriṃ": "တစ်စုံတစ်ခုသော သဘောတရားကို မခွဲခြားသော",
    "sati": "သတိ",
    "paṭilabhati": "ရသည်",
    "mānaṃ paṭilabhati": "မာနကို ရသည်",
    "chandaṃ paṭilabhati": "ဆန္ဒကို ရသည်",
    "diṭṭhiṃ paṭilabhati": "အယူကို ရသည်",
    "diṭṭhiṃ": "အယူ",
    "Parapuggalaṃ": "သူတစ်ပါး",
    "adhicca": "အကြောင်းမဲ့",
    "samuppannikā": "ဖြစ်ပေါ်သည်ဟု ဆိုသော",
    "amarā": "ငါးရှဉ့်",
    "vikkhepikā": "လှည့်ပတ် ပြောသော",
    "ānantikā": "အဆုံးမဲ့",
    "saññī": "@alt",
    "soḷasa": "ဆယ့်ခြောက်ပါး",
    "vatthu": "အကြောင်းအရာ",
    "satte": "သတ္တဝါ",
    "leḍḍunā": "မြေစိုင်ခဲ",
    "pāṇinā": "လက်",
    "viheṭheti": "ညှဉ်းဆဲသည်",
    "satthena": "လက်နက်",
    "rajjuyā": "ကြိုး",
    "daṇḍena": "တုတ်",
    "ūpaghāto": "ထိပါးခြင်း",
    "visamacariyā": "ဖောက်ပြန်သော အကျင့်",
    "bojjhaṅgā": "ဗောဇ္ဈင်",
    "pādā": "ပါဒ်",
    "iddhipādā": "ဣဒ္ဓိပါဒ်",
    "padhānā": "ကြိုးပမ်းအားထုတ်ခြင်း",
    "sammappadhānā": "မှန်ကန်သော ကြိုးပမ်းအားထုတ်ခြင်း",
    "aṭṭhaṅgiko maggo": "အင်္ဂါ ရှစ်ပါး ရှိသော … မဂ်",
    "paṭṭhānā": "ပဋ္ဌာန်",
    "satipaṭṭhānā": "သတိပဋ္ဌာန်",
    "ariyo": "အရိယာ",
    "maggo": "@alt",
    "iddhi": "@alt",
    "randha": "အပြစ်အနာအဆာ",
    "dukkhasamudaye": "ဒုက္ခ ဖြစ်ပေါ်ခြင်း",
    "attavādupādānañca": "အတ္တဟူသော ဝါဒ စွဲလမ်းမှု",
    "āgatiṃ": "အဂတိ",
    "mohāgatiṃ": "မောဟ အဂတိ",
    "Chandāgatiṃ": "ဆန္ဒ အဂတိ",
    "vāri": "ရေ",
    "vagga": "ဂိုဏ်းဖွဲ့၍",
    "bhayāgatiṃ": "ကြောက်ခြင်း အဂတိ",
    "gacchati": "လိုက်သည်",
    "dosāgatiṃ": "ဒေါသ အဂတိ",
    "vipariyāso": "ပြောင်းပြန်",
    "aviññātavāditā": "မသိဟု ပြောခြင်း",
    "amutavāditā": "မထိတွေ့ဟု ပြောခြင်း",
    "duggati": "ဆိုးသော လားရာ",
    "kumbhīla": "မိကျောင်း",
    "aggi": "မီး",
    "Rāja": "မင်း",
    "daṇḍa": "ဒဏ်ခတ်ခံရခြင်း",
    "ānuvāda": "အပြစ်တင်ခြင်း",
    "Attānuvāda": "မိမိကိုယ်ကို အပြစ်တင်ခြင်း",
    "susukā": "ငါးဆိုး",
    "cora": "ခိုးသူ",
    "Ūmi": "လှိုင်း",
    "āvaṭṭa": "ဝဲဂယက်",
    "samuppannaṃ": "ဖြစ်ပေါ်လာသော",
    "sukhadukkha": "ချမ်းသာ ဆင်းရဲ",
    "Sayaṅkataṃ": "မိမိ ပြုသော",
    "dukkha": "@alt",
    "kula": "@alt",
    "saṅgo": "@alt",
    "moha": "မောဟ",
    "dosa": "ဒေါသ",
    "sallaṃ": "ငြောင့်",
    "avigatapemo": "ချစ်ခင်မှု မကင်းသော",
    "paṇidhāya": "ဆုတောင်း၍",
    "tapena": "အကျင့်ခြိုးခြံမှု",
    "udarāvadehakaṃ": "ဝမ်းပြည့်အောင်",
    "kāye": "ကိုယ်",
    "avigatapariḷāho": "ပူလောင်မှု မကင်းသော",
    "avigatataṇho": "တပ်မက်မှု မကင်းသော",
    "avigatacchando": "ဆန္ဒ မကင်းသော",
    "anuyutto": "အားထုတ်သော",
    "bhuñjitvā": "စားပြီး၍",
    "rūpe": "ရုပ်",
    "deva": "နတ်",
    "nikāyaṃ": "အပေါင်း",
    "brahmacariyaṃ": "မြတ်သော အကျင့်",
    "carati": "@alt",
    "passasukhaṃ": "လှဲလျောင်းခြင်း၏ ချမ်းသာ",
    "seyyasukhaṃ": "အိပ်ခြင်း၏ ချမ်းသာ",
    "middhasukhaṃ": "ငိုက်မျဉ်းခြင်း၏ ချမ်းသာ",
    "sukhaṃ": "@alt",
    "avītarāgo": "ရာဂ မကင်းသော",
    "Kāme": "ကာမ",
    "avigatapipāso": "ငတ်မွတ်မှု မကင်းသော",
    "thinamiddha": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု",
    "uddhaccakukkucca": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု",
    "arahanto": "ရဟန္တာ",
    "lohitaṃ": "သွေး",
    "voropitā": "ချခံရသော",
    "jīvitā": "အသက်",
    "duṭṭhena": "ပြစ်မှားသော",
    "cittena": "စိတ်",
    "saṅgho": "သံဃာ",
    "uppāditaṃ": "ထွက်စေအပ်သော",
    "abhivadanti": "ကြွေးကြော်သည်",
    "diṭṭhadhammanibbānaṃ": "မျက်မှောက်ဘဝ၌ နိဗ္ဗာန်",
    "paññāpenti": "ပညတ်သည်",
    "roga": "ကျန်းမာရေး",
    "duggatiṃ": "ဆိုးသော လားရာ",
    "bhedā": "@alt",
    "sammūḷho": "တွေဝေသော",
    "kālaṅkaroti": "သေရသည်",
    "appiyo": "မချစ်အပ်သော",
    "amanāpo": "မနှစ်သက်အပ်သူ",
    "vajja": "အပြစ်",
    "nirayaṃ": "ငရဲ",
    "vera": "ရန်",
    "janassa": "လူ",
    "vinipātaṃ": "ပျက်စီး ကျရောက်ရာ",
    "upapajjati": "ရောက်ရသည်",
    "parisa": "ပရိသတ်",
    "asiloka": "အသရေပျက်ခြင်း",
    "Ājīvaka": "အသက်မွေးဝမ်းကျောင်းမှု",
    "sārajja": "ရွံ့ကြောက်ခြင်း",
    "kasāvo": "အမည်းအစက်",
    "Amanāpiyesu": "စိတ်နှင့် မတွေ့သော",
    "cetasikaṃ asātaṃ": "စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ် မကောင်းမှု",
    "dukkhaṃ vedayitaṃ": "နာကျင်သော ခံစားရခြင်း",
    "asātaṃ dukkhaṃ": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော",
    "asātaṃ dukkhaṃ vedayitaṃ": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားရခြင်း",
    "asātā dukkhā vedanā": "နှစ်သက်ဖွယ် မကောင်း၍ နာကျင်သော ခံစားမှု",
    "Upekkhāṭṭhāniyesu": "လျစ်လျူရှုဖွယ် ဖြစ်သော",
    "gehasitaṃ cetasikaṃ": "လောကီ အိမ်ရာကို မှီသော စိတ်ပိုင်းဆိုင်ရာ",
    "adukkhamasukhaṃ": "@alt",
    "nāsātaṃ": "နှစ်သက်ဖွယ် မကောင်းသည်လည်း မဟုတ်သော",
    # relative pronouns (approved pi-1 rule: no direct equivalent where the text builds the clause with ရှိသော / ရှိသမျှ)
    "Yo": "(no direct equivalent)",
    "yo": "(no direct equivalent)",
    "Yaṃ": "(no direct equivalent)",
    "yaṃ": "(no direct equivalent)",
    "dhuratā": "တာဝန်",


    # @@MANUAL@@
}

SECTIONS = {
    "preamble": T_PREAMBLE,
    "1-khandhavibhango": T_KHANDHA,
    "17-khuddakavatthuvibhango": T_KHUDDAKA,
}
CHAPTERS = ["17-khuddakavatthuvibhango"]


# =====================================================================================================
# rules (written to map-table.md)
# =====================================================================================================
RULES = """## Rules

The value is the word or phrase of THAT segment's Burmese (the FINAL pi-2 text) that carries the keyword, in the
dictionary form of the approved pi-1 Burmese mapping. **Binding and unchanged:** pi-1 `map-table.md` rules 1–11, the
agreed later pi-1 rules (absolutives keep «…၍»; relative pronouns Yo / Yā / Yaṃ = (no direct equivalent) where the
Burmese builds the clause with «ရှိသော / ရှိသမျှ»; one sense per segment; no « / » alternatives; caya-type fragments)
and the approved pi-2 sample rules N1–N11 (`map-table.md`). pi-1 values are reused for the same keyword in the same
kind of segment when they occur in the pi-2 segment (the script looks every keyword up in the final pi-1 mapping
after its own table); the cases where a pi-1 value occurs but another value was chosen are listed with the reason in
«Values that differ from pi-1».

## NEW rules (chapter 17, for the user's review)

N12. **Presence check, more accepted endings** (the same idea as pi-1 rule 3 and sample N11: only the ending
     differs). Adjective chunk «Xသော» also accepted before «ဟူ» («အဆုံး မရှိဟူသော»), «ကုန်» (plural predicate
     «မမြဲကုန်»), «လျက်» («လှည့်လည်လျက်») and the finite «၏» (a predicated adjective «X၏» → «Xသော»: «ထာဝရ တည်၏»).
     Verb chunk «Xသည်» also accepted before «ပါစေ» (optative), «သမျှ» («ခံစားရသမျှ»), «ဟု», «ကုန်», «အံ့», «လော့»
     and «မည်». New check «neg-verb»: «Xသည်» accepted against «…မX…» + a verb ending, because Burmese puts the
     negative inside the verb («မသိပါစေနှင့်», «ဝီရိယကို မအားထုတ်»), as pi-1 rule 8 does for compounds; used for
     verbs whose negative is a separate Pāli word (na / mā: jaññā = သိသည်, avajāniṃsūti = အထင်သေးသည်, ārabhati =
     အားထုတ်သည်, sampasīdati = ကြည်လင်သည်, jānāsi = သိသည်).
N13. **Persons**: where the text renders the Pāli adjective as a person noun predicated with «ဖြစ်» («X hoti», «X
     samāno»: «ယုံကြည်မှု မရှိသူ ဖြစ်လျက်», «အမျက်ထွက်သူ ဖြစ်၏») the value keeps «…သူ», as pi-1 sadiso = တူညီသူ,
     hīno = ယုတ်ညံ့သူ, janikā = မွေးဖွားပေးတတ်သူ (so hīno in «Idhekacco hīno hoti» = ယုတ်ညံ့သူ, sadisaṃ = တူညီသူ).
     Attributive adjectives in a modifier chain stay «…သော» (assaddhā … puggalā = ယုံကြည်မှု မရှိသော; pi-1 akovido /
     avinīto = «…သော» in the sakkāyadiṭṭhi formula, which also binds adassāvī = မမြင်ဖူးသော).
N14. **(no direct equivalent) for a compound member the text renders inside one word**, by analogy with the approved
     caya rule: gata / gataṃ / gatāni (diṭṭhigata = «အယူမှား»; pi-1 «သဘော ရှိသော» is ākāsagataṃ, another
     construction), ṭṭhānena (vijjāṭṭhāna = «ပညာရပ်»), āyatanena (kammāyatana = «အလုပ်အကိုင်», sippāyatana =
     «အတတ်ပညာ»), majja (surāmerayamajja = «သေရည်သေရက်»: surā = သေရည်, meraya = သေရက်), yogaṃ (yogaṃ āpajjati =
     «ဝင်ရောက် ဆောင်ရွက်၏», carried by āpajjati). Relative Yadeva = (no direct equivalent) (the «ရှိသမျှ» clause).
N15. **Synonym-list items and headings** take the zero-shot's own Burmese for that Pāli word (pi-2-my/make_ch17.py
     ITEMS / NAME), i.e. the item the text prints; inflected forms of an item keep its value (Jātiṃ, Gottaṃ, yasaṃ …
     = the noun, rule 1). Chapter headings: Ekaka … Dasaka = «Nမျိုးတွဲ» (pi-1 Duka = နှစ်မျိုးတွဲ); ādi / ādī /
     ādīni = «စသည်»; ganthādī = «အထုံး … စသည်» (the count belongs to the numeral).
N16. **Case meaning kept where the text renders it by a clause word** (as sample N7 paccayā): bhedā = «ပြိုကွဲသောအခါ»
     / «ပြိုကွဲ၍»; ādhikaraṇaṃ (ārakkhādhikaraṇaṃ) = «ကြောင့်»; ettāvatā = «ဤမျှဖြင့်»; saṅkhātena = «ဟူသော နည်း»;
     datives «…ရန်» (adhigamāya = ရရှိရန်, as pi-1 pattiyā = ရောက်ရန်); sati in «tasmiṃ sati» = «ရှိသော» (text
     «ရှိသော်», the concessive ending of rule 3).
N17. **Quoted views and «I am» clauses**: predicated adjectives = «…သော» (nicca = မြဲသော, nicco, dhuvo, arogo …),
     except where pi-1 binds (Sassato in «sassato loko» = ထာဝရ တည်မြဲသည်); the first-person «-smi / -āmi» forms keep
     «ငါ» and the verb in «…သည်» (niccosmi = ငါ မြဲသည်, asasmīti = ငါ အမြဲ ရှိသည်, vinassissāmi = ငါ ပျက်စီးသည်), as
     the māna names (Sadisohamasmīti = ငါသည် တူညီသူ ဖြစ်သည်, the quotative ဟူသော dropped, rule 4).
N18. **One keyword, several senses by compound** (one sense per segment: the sense of the first occurrence; ALT lists
     in map_17.py): vatthūni = အကြောင်းရင်း (kilesa-) / အကြောင်း (virodha-, kusīta-, āghāta-); kamyatā = ထူလိုခြင်း
     (ketukamyatā, pi-1) / လိုခြင်း / လိုချင်ခြင်း (sādhukamyatā); vaṇṇa = အဆင်းလှခြင်း (mada) / ဂုဏ်သတင်း /
     ဂုဏ်ကျေးဇူး (macchariya: the text has both); bahiddhā = မိမိ၏ ပြင်ပ၌ (sample) / အပြင်ပိုင်း (bahiddhāsaṃyojana) /
     အပြင်ဘက် («ito bahiddhā», pi-1 wording); rūpa follows pi-1 decision 3 with CTX where the first compound is a
     realm (rūpadhātu-, rūpataṇhā / rūparāga of the planes = «သိမ်မွေ့သော ရုပ်») or the visible object (rūpāsā,
     rūpataṇhā of the six objects = «အဆင်းအရောင်»); rūpataṇhā in the lobha list (twice: realm, then object) = the
     first, realm sense; also sammā, sukha, dukkha, dukkhe, uppajjati, āpajjati, paṭigha, doso, Jāti, dhātu, kata …
N19. **Counts**: a keyword that is a numeral keeps the text's count word (chattiṃsa = သုံးဆယ့်ခြောက်ပါး, aṭṭhārasa =
     ဆယ့်ရှစ်ပါး, dvāsaṭṭhi = ခြောက်ဆယ့်နှစ်ပါး, soḷasa = ဆယ့်ခြောက်ပါး; sataṃ = တစ်ရာ in «တစ်ရာ့ရှစ်ပါး»); «Dasa X»
     keywords keep the count after the noun (Dasa saṃyojanāni = နှောင်ကြိုး ဆယ်ပါး). Ordinals = the text's ordinals
     (aṭṭhamaṃ / aṭṭhamo = အဋ္ဌမ …).
N20. **Absolutives the text renders with «ပြီး»** keep the text's form (āvattitvā = ပြန်လည်ပြီး; bhuñjitvā = စားပြီး၍);
     the conjunctive «…ပြီး» of a participle is normalised to «…သော» by rule 3 (kataṃ in «ပြုပြီး ဖြစ်၏» = ပြုသော,
     vuṭṭhito = ထသော).
N21. **Keywords that include the negative** (nādhimuccati, nāhosi, nāsātaṃ, appiyo …) keep the text's negative form;
     the positive fragments of «na / mā + verb» keywords (sarāmi, saddahati, jaññā) take the positive verb (N12
     neg-verb).
N22. **Phrases of the Brahmajāla / suttanta frames** take the text's own words: bho = «အချင်း», kissa hetu =
     «အဘယ်ကြောင့်», kiṃ nu kho = «အဘယ်», nāma (tvampi nāma) = «ပင်လျှင်», yaṃ kiñcāyaṃ = «ဤ … သမျှ» (the text
     builds «yaṃ kiñci ayaṃ … paṭisaṃvedeti» as «ဤပုဂ္ဂိုလ်သည် … ခံစားရသမျှ»), Tassa evaṃ hoti = «ထိုရဟန်းအား ဤသို့
     အကြံ ဖြစ်သည်».
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
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော", "၊", "သည့်", "ဟူ", "ကုန်", "လျက်", "၏")
VERB_FROM = ("ပါ၏", "၏", "ပြီ", "သော", "၍", "ပြီး", "ခြင်း", "ရန်", "သည့်", "ကြ", "၊", "ဟူ", "လိမ့်မည်", "။", "ပါစေ", "သမျှ", "ဟု", "ကုန်", "အံ့", "လော့", "မည်")


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
    if c.endswith("သည်") and len(c) > 3:          # ch17 N13: infixed မ + verb ending («မ…ကြပါစေနှင့်»)
        st = c[:-3]
        for i in range(0, len(st)):
            if any(st[:i] + "မ" + st[i:] + e in text for e in VERB_FROM):
                return "neg-verb"
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
    "dhuratā": "the pi-2 text has «တာဝန်» (nikkhittadhuratā «တာဝန်ကို ချထားခြင်း»); pi-1 «ဝန်» occurs only inside that word",
    "gataṃ": "N14: pi-1 «သဘော ရှိသော» is ākāsagataṃ (another construction, ^1-637); in diṭṭhigataṃ the text has the one "
             "word «အယူမှား»; the «သဘော / ရှိသော» chunks here belong to evarūpā «ဤသို့ သဘောရှိသော»",
    "jīvita": "jīvitamado: the text's item is «အသက်ရှင်ခြင်း» (being alive); pi-1 «အသက်» (life faculty) occurs only "
              "inside it",
    "kamyatā": "2-834 (Mātikā): the kamyatā items are «…လိုခြင်း» (adassanakamyatā, asotukamyatā); pi-1 «လိုလားခြင်း» "
               "here belongs to avadaññutā «ပေးကမ်းရန် မလိုလားခြင်း»",
    "kodha": "kodhasāmantā: «အမျက်ဒေါသ» is kodha (pi-1 kodho); pi-1 «ဒေါသ» (dosa) occurs only inside it",
    "saṃvattanikā": "the text has «မဖြစ်စေတတ်သော» (asamādhisaṃvattanikā); pi-1 «ဖြစ်စေသော» is found only by an ending "
                    "rule, the exact text form is kept",
    "vibhava": "vibhavataṇhā: the text «ဘဝ ပျောက်ကွယ်ခြင်းကို» (pi-1 termbase vibhava = «ဘဝ ပျောက်ကွယ်ခြင်း»); pi-1 "
               "«ဘဝ ပျောက်ကွယ်သည်» is the view name (vibhavadiṭṭhi), kept there",
    "āyatanaṃ": "2-951 viññāṇañcāyatana: the text «… နယ်ပယ်»; pi-1 «အာရုံခံ နယ်ပယ်» matches only through «အာရုံခံ "
                "စွမ်းရည်» (ahīnindriyo) in the same segment",
}
AUTO_REASON = "no pi-1 value of the keyword occurs in the segment: the pi-2 text's own word for this compound / sense"


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
    with open(HERE / "map-table-17.md", "w", encoding="utf-8") as f:
        f.write("# pi-2 Burmese keyword mapping: rules and review table (Vibhaṅga «ခွဲခြမ်းစိတ်ဖြာခြင်း», chapter "
                + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_17.py (a copy of the approved sample map_all.py; sample rules and values binding). Burmese from the FINAL pi-2 text of this track only "
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
                            + f" | {REASONS.get(kw, AUTO_REASON)} |\n")
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
