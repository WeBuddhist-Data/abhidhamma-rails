"""Pāli→Burmese keyword mapping for pi-1 chapter 5 (Aṭṭhakathākaṇḍa) of «သဘောတရားများကို စုစည်းရေတွက်ခြင်း».

usage (python3 -I -X utf8):
  map_5.py             writes 5-atthakathakandam.mapped.md and map-table-5.md, then verifies the chapter
                       (keyword preservation, presence of every value chunk in its segment, no ", " / «၊» in a value)
  map_5.py --report    writes nothing; lists unmapped keywords and presence failures
  map_5.py --seg ID    prints Pāli, Burmese, keywords and mapping of one segment

Method: the approved sample mapper map_all.py (brief burmese-mapper-brief.md, «Approved sample»), COPIED here, not
imported: its tables T_PREAMBLE / T_MATIKA (unchanged: Mātikā items quoted in this chapter keep the 1-matika
values), its compose rules, its context function and its verifier. This chapter adds
  T_ATTHA        the chapter table (keyword -> Burmese, dictionary form), looked up before the sample tables,
  CTX            per-segment overrides,
  @functions     context functions (rūpa / ākāsa sense, the -ato forms, coordinated pairs, jhāna-method groups),
  compose()      also «dhammā X» (the keyword order of this chapter) = T[X] + « သဘောတရား»,
  presence()     three more ending rules (NEW_RULES, written to map-table-5.md).
The Burmese is the FINAL text of this track (AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters);
no other Burmese source is used.
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
# sample tables (copied unchanged from map_all.py, approved 2026-11-17)
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
# chapter 5 table (Aṭṭhakathākaṇḍa)
# =====================================================================================================
KUS, AKUS, CIT = "ကုသိုလ်", "အကုသိုလ်", "စိတ်"
ABY = "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော"      # = T_MATIKA abyākatā (sample rule 6: no «၊»)
KIR = "ပြုရုံမျှသာ ဖြစ်သော"
KAMA = "ကာမဘုံနှင့် ဆိုင်သော"
RUPAV = "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော"
LOKUT = "လောကကို ကျော်လွန်သော"
SAHA = "နှင့်အတူ ဖြစ်သော"
VAT = "ခေါ်ဆို၍ ရ"                                    # vattabba: «ခေါ်ဆို၍ မရ» without its negative (new rule 14)

T_ATTHA = {
    # --- headings, colophons
    "kaṇḍaṃ": "အခန်း", "Aṭṭhakathā": "အနက်ဖွင့်", "atthuddhāro": "အနက် ထုတ်ဖော်ချက်",
    "niṭṭhito": "ပြီးဆုံးသော",                               # text «ပြီးဆုံးပြီ» (sample rule 3, as niṭṭhitā)
    # --- the kinds of mind (neuter nouns of the lists: the text adds «စိတ်», minor clarification)
    "kusalaṃ": KUS + CIT, "akusalaṃ": AKUS + CIT,
    "kusala": KUS, "akusala": AKUS, "kusalassa": KUS, "akusalassa": AKUS,
    "akusalacitta": AKUS + CIT,
    "kusalesu": KUS + CIT, "akusalesu": AKUS + CIT,          # «… စိတ်တို့၌» (not the Mātikā «kusalesu dhammesu»)
    "kiriyā": KIR, "kiriya": KIR, "kiriyesu": KIR + " " + CIT,
    "kiriyābyākataṃ": KIR + " " + ABY + " " + CIT,
    "abyākataṃ": ABY, "abyākata": ABY,
    "akusalābyākatā": AKUS + " " + ABY,                      # «ကုသိုလ်၊ အကုသိုလ်၊ ABY» (rule 6)
    "vipāka": "ကံ၏ အကျိုး",                    # the noun without the copula ဖြစ်သော (sample rule 2), as the 2-04 / 2-05 headings (harmonise)
    "kusalato": "@ato", "akusalato": "@ato", "kiriyato": "@ato", "vipākato": "@ato",
    "kusalato ca vipākato": "@coord", "vipākato ca kiriyato": "@coord",
    "bhūmīsu": "ဘုံ",
    "citta": CIT, "Cittañca": CIT, "cittā": CIT,
    "uppādā": "ဖြစ်ပေါ်မှု", "uppādo": "ဖြစ်ပေါ်မှု", "uppāde": "ဖြစ်ပေါ်မှု", "uppādesu": "ဖြစ်ပေါ်မှု",
    "cittuppādā": "စိတ် ဖြစ်ပေါ်မှု", "cittuppādo": "စိတ် ဖြစ်ပေါ်မှု", "cittuppāde": "စိတ် ဖြစ်ပေါ်မှု",
    "cittuppādesu": "စိတ် ဖြစ်ပေါ်မှု",
    # --- numbers (the count as the text gives it, with its classifier «ပါး»: rule 12, harmonise decision 5)
    "Dvādasa": "ဆယ့်နှစ်ပါး", "ekādasa": "ဆယ့်တစ်ပါး", "dasa": "ဆယ်ပါး",
    # --- planes, jhānas
    "Kāma": "ကာမ", "Kāmāvacara": KAMA, "Kāmāvacaraṃ": KAMA, "kāmāvacara": KAMA, "kāmāvacarassa": KAMA,
    "avacara": "ဘုံနှင့် ဆိုင်သော", "avacaraṃ": "ဘုံနှင့် ဆိုင်သော", "avacarassa": "ဘုံနှင့် ဆိုင်သော",
    "rūpāvacara": RUPAV, "rūpāvacaraṃ": RUPAV,
    "lokuttara": LOKUT, "lokuttaraṃ": LOKUT,
    "jhānā": "ဈာန်", "jhānaṃ": "ဈာန်", "jhāne": "ဈာန်", "jhānassa": "ဈာန်",
    "catutthaṃ jhānaṃ": "စတုတ္ထ ဈာန်", "catutthassa jhānassa": "စတုတ္ထ ဈာန်",
    "lokuttaraṃ catutthaṃ jhānaṃ": LOKUT + " စတုတ္ထ ဈာန်",
    "lokuttaraṃ paṭhamaṃ jhānaṃ": LOKUT + " ပထမ ဈာန်",
    "lokuttarapañcakanaye dutiyaṃ jhānaṃ": LOKUT + " ဈာန် ငါးပါး ခွဲနည်းအရ ဒုတိယ ဈာန်",
    "pañcaka": "ဈာန် ငါးပါး", "naye": "ခွဲနည်း", "pañcakanaye": "ဈာန် ငါးပါး ခွဲနည်း",
    "lokuttaratikacatukkajjhānā": "@jh", "lokuttaratikatikajjhānā": "@jh", "lokuttaradukatikajjhānā": "@jh",
    "lokuttaradukadukajjhānā": "@jh", "lokuttaraekakadukajjhānā": "@jh",
    "āruppā": "ရုပ်မရှိသော ဈာန်",
    # --- qualifiers of cittuppāda
    "sahagata": "အတူ ဖြစ်သော", "sahagato": "အတူ ဖြစ်သော", "sahagataṃ": "အတူ ဖြစ်သော",
    "sahagatesu": "အတူ ဖြစ်သော",
    "sahagatacitta": "အတူ ဖြစ်သော စိတ်", "sahagato citta": "အတူ ဖြစ်သော စိတ်",
    "sahagatesu citta": "အတူ ဖြစ်သော စိတ်",
    "somanassa": "ဝမ်းမြောက်မှု", "somanassasahagata": "ဝမ်းမြောက်မှု" + SAHA,
    "somanassasahagatā": "ဝမ်းမြောက်မှု" + SAHA,
    "domanassa": "စိတ်ဆင်းရဲမှု", "domanassasahagata": "စိတ်ဆင်းရဲမှု" + SAHA,
    "domanassasahagatesu": "စိတ်ဆင်းရဲမှု" + SAHA,
    "upekkhāsahagata": "ဥပေက္ခာ" + SAHA,
    "lobha": "လောဘ", "lobhasahagata": "လောဘ" + SAHA, "lobhasahagatesu": "လောဘ" + SAHA,
    "vicikicchā": "ယုံမှားမှု", "vicikicchāsahagato": "ယုံမှားမှု" + SAHA,
    "vicikicchāsahagataṃ": "ယုံမှားမှု" + SAHA, "vicikicchāsahagatesu": "ယုံမှားမှု" + SAHA,
    "uddhacca": "ယောက်ယက်ခတ်မှု", "uddhaccasahagato": "ယောက်ယက်ခတ်မှု" + SAHA,
    "uddhaccasahagataṃ": "ယောက်ယက်ခတ်မှု" + SAHA, "uddhaccasahagatesu": "ယောက်ယက်ခတ်မှု" + SAHA,
    "uddhaccaṃ": "ယောက်ယက်ခတ်မှု",
    "diṭṭhigata": "အယူမှား",
    "diṭṭhigatavippayutta": "အယူမှားနှင့် ကင်းကွာသော", "diṭṭhigatavippayuttā": "အယူမှားနှင့် ကင်းကွာသော",
    "vippayuttalobha": "ကင်းကွာသော လောဘ", "vippayuttā lobha": "ကင်းကွာသော လောဘ",   # text «…ကင်းကွာသော၊ လောဘ…»
    "sampayutta": "ယှဉ်တွဲသော", "sampayutte": "ယှဉ်တွဲသော", "sampayutto": "ယှဉ်တွဲသော",
    "vippayutta": "ကင်းကွာသော", "vippayutte": "ကင်းကွာသော",
    "ñāṇa": "ဉာဏ်", "ñāṇavippayutta": "ဉာဏ်နှင့် ကင်းကွာသော", "ñāṇavippayutte": "ဉာဏ်နှင့် ကင်းကွာသော",
    "vippayuttacitta": "ကင်းကွာသော စိတ်", "vippayutte citta": "ကင်းကွာသော စိတ်",
    "ahetuke citta": "အမြစ် မရှိသော စိတ်",
    "hetuka": "အမြစ်", "hetukaṃ": "အမြစ်",                   # sample rule 2 (hetukā = အမြစ်)
    "sasaṅkhārikesu": "တိုက်တွန်းမှုဖြင့် ဖြစ်သော",
    # --- feelings, factors
    "dukkha": "နာကျင်မှု", "vedanā": "ခံစားမှု", "Vedanā": "ခံစားမှု",
    "kāyaviññāṇaṃ": "ကိုယ် သိစိတ်",
    "uppanno": "ဖြစ်ပေါ်သော", "uppannaṃ": "ဖြစ်ပေါ်သော", "uppanne": "ဖြစ်ပေါ်သော",
    "uppannaṃ vicāraṃ": "ဖြစ်ပေါ်သော ဆက်လက်သုံးသပ်မှု", "uppannaṃ vitakkaṃ": "ဖြစ်ပေါ်သော စတင်ကြံစည်မှု",
    "uppanne vitakkavicāre": "ဖြစ်ပေါ်သော စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု",
    "uppanno ca vicāro": "ဖြစ်ပေါ်သော ဆက်လက်သုံးသပ်မှု",
    "uppanne hetū": "ဖြစ်ပေါ်သော အမြစ်",
    "sahajāto": "အတူတကွ ဖြစ်ပေါ်သော",
    "savitakkasavicāro": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော",
    "ṭhapetvā": "ချန်ထား၍",                                   # absolutive = the preposition «except» (rule 13)
    "moho": "မောဟ", "mohaṃ": "မောဟ", "sahagato moho": "အတူ ဖြစ်သော မောဟ",
    "sahagataṃ mohaṃ": "အတူ ဖြစ်သော မောဟ",
    "sahagataṃ uddhaccasahagataṃ mohaṃ": "အတူ ဖြစ်သော ယောက်ယက်ခတ်မှု" + SAHA + " မောဟ",
    "siyā": "တစ်ခါတစ်ရံ",
    # --- «na vattabbā» (rule 14)
    "vattabbā": VAT, "vattabbo": VAT, "vattabbaṃ": VAT,
    "vattabbo savitakkasavicāro": "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှု ရှိသော … " + VAT,
    "vattabbaṃ pītisahagatanti": "ပီတိနှင့်အတူ ဖြစ်သော … " + VAT,
    "vattabbā parittārammaṇā": "အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော … " + VAT,
    "vattabbā maggārammaṇā": "မဂ်ကို အာရုံပြုသော … " + VAT,
    "vattabbā anuppannā": "မဖြစ်ပေါ်သေးသော … " + VAT,
    "vattabbā atītārammaṇā": "အတိတ်ကို အာရုံပြုသော … " + VAT,
    "vattabbaṃ ajjhattārammaṇanti": "မိမိ၌ ရှိသည်ကို အာရုံပြုသော … " + VAT,
    # --- matter, nibbāna, paths and fruits
    "rūpañca": "ရုပ်", "Rūpañca": "ရုပ်", "rūpaṃ": "ရုပ်", "Rūpaṃ": "ရုပ်",
    "rūpañca nibbānañca": "@coord", "rūpaṃ nibbānañca": "@coord", "sāmaññaphalāni nibbānañca": "@coord",
    "indriyabaddharūpañca nibbānañca": "စွမ်းရည်တို့နှင့် ဆက်စပ်သော ရုပ်နှင့် နိဗ္ဗာန်",   # an- dropped (rule 8)
    "nibbānañca anārammaṇā": "နိဗ္ဗာန်သည် အာရုံ မရှိသော",
    "indriya": "စွမ်းရည်", "baddha": "ဆက်စပ်သော",
    "kammassa": "ကံ", "kammassa katattā": "ကံကို ပြုခဲ့ခြင်းကြောင့်",   # ကြောင့် is the causal meaning of katattā, not a rule-1 particle (as 3 and 4; harmonise)
    "yañca": "ရှိသမျှ", "yaṃ": "ရှိသမျှ",
    "maggā": "မဂ်", "maggā apariyāpannā": "ဘဝဘုံတို့၌ အကျုံးမဝင်သော မဂ်", "ariya": "အရိယာ",
    "sāmañña": "ရဟန်းအဖြစ်", "phalāni": "ဖိုလ်", "phalaṃ": "ဖိုလ်",
    "arahatta": "ရဟန္တာ", "Upariṭṭhimaṃ": "အမြင့်ဆုံး",
    "sekkha": "ကျင့်ကြံဆဲသူ၏",                                 # as T_MATIKA sekkhā (nevasekkhanāsekkhā)
    "avasesaṃ": "ကြွင်းကျန်သော", "avasesañca": "ကြွင်းကျန်သော",
    "avasesaṃ akusalaṃ": "ကြွင်းကျန်သော " + AKUS + CIT, "avasesañca rūpaṃ": "ကြွင်းကျန်သော ရုပ်",
    "sabbaṃ": "အားလုံး",
    "upādāya": "မှီ၍", "upādāya rūpaṃ": "မှီ၍ ဖြစ်သော ရုပ်", "bhūtā": "မူလဓာတ်", "mahābhūtā": "မူလဓာတ်ကြီး",
    "Niyogā": "အမြဲတမ်း",
    # --- mind, consciousness, aggregates, bases
    "mano": "မနော", "manodhātu": "မနော ဓာတ်", "manodhātuyo": "မနော ဓာတ်", "dhātuyo": "ဓာတ်",
    "manoviññāṇa": "မနော သိစိတ်", "manoviññāṇadhātu": "မနော သိစိတ် ဓာတ်",
    "kiriyāmano": KIR + " မနော", "kiriyāmanodhātu": KIR + " မနော ဓာတ်",
    "kiriyāhetukamanoviññāṇa": KIR + " အမြစ် မရှိသော … မနော သိစိတ်",
    "kiriyāhetukamanoviññāṇadhātu": KIR + " အမြစ် မရှိသော … မနော သိစိတ် ဓာတ်",
    "dhātu upekkhāsahagatā": "ဥပေက္ခာ" + SAHA + " … ဓာတ်",
    "manoviññāṇadhātu upekkhāsahagatā": "ဥပေက္ခာ" + SAHA + " မနော သိစိတ် ဓာတ်",
    "viññāṇāni": "သိစိတ်", "pañcaviññāṇāni": "ငါးပါးစီ ရှိသော သိစိတ်",
    "Cakkhuviññāṇaṃ": "မျက်စိ သိစိတ်", "sotaviññāṇaṃ": "နား သိစိတ်", "ghānaviññāṇaṃ": "နှာခေါင်း သိစိတ်",
    "jivhāviññāṇaṃ": "လျှာ သိစိတ်",
    "khandho": "အစုအဝေး", "Vedanākkhandho": "ခံစားမှု အစုအဝေး", "saññākkhandho": "မှတ်သိမှု အစုအဝေး",
    "saṅkhārakkhandho": "ပြုပြင်ဖန်တီးမှု အစုအဝေး", "saṅkhāra": "ပြုပြင်ဖန်တီးမှု", "saññā": "မှတ်သိမှု",
    "asaññā": "မှတ်သိမှု မရှိသော",                           # nevasaññānāsañña: attributive as 2-04 / 2-05 / 4-02 (harmonise 5)
    "Viññāṇañcāyatanaṃ": "အဆုံး မရှိသော သိစိတ် နယ်ပယ်",
    "ānañca": "အဆုံး မရှိသော", "ānañcāyatanaṃ": "အဆုံး မရှိသော … နယ်ပယ်",
    "ākāsa": "@akasa", "ākiñcañña": "ဘာမျှ မရှိသော",
    "Cakkhu": "မျက်စိ", "Cakkhāyatanaṃ": "မျက်စိ အာရုံခံ နယ်ပယ်",
    "Rūpāyatanaṃ": "အဆင်းအရောင် အာရုံခံ နယ်ပယ်", "rūpāyatanaṃ": "အဆင်းအရောင် အာရုံခံ နယ်ပယ်",
    "sadda": "အသံ", "saddāyatanaṃ": "အသံ အာရုံခံ နယ်ပယ်", "gandha": "အနံ့", "gandhāyatanaṃ": "အနံ့ အာရုံခံ နယ်ပယ်",
    "rasa": "အရသာ", "rasāyatanaṃ": "အရသာ အာရုံခံ နယ်ပယ်",
    "phoṭṭhabba": "အထိအတွေ့", "phoṭṭhabbāyatanaṃ": "အထိအတွေ့ အာရုံခံ နယ်ပယ်",
    "manāyatanaṃ": "မနော အာရုံခံ နယ်ပယ်", "dhammāyatanaṃ": "သဘောတရား အာရုံခံ နယ်ပယ်",
    "dhammāyatana": "သဘောတရား အာရုံခံ နယ်ပယ်", "dhamma": DH,
    "anidassanaṃ": "မမြင်နိုင်သော", "appaṭighaṃ": "ထိခိုက်မှု မရှိသော",
    "kāya": "ကိုယ်", "vacī": "နှုတ်", "viññatti": "ထုတ်ဖော်ပြသမှု",
    "kāyaviññatti": "ကိုယ်ဖြင့် ထုတ်ဖော်ပြသမှု", "vacīviññatti": "နှုတ်ဖြင့် ထုတ်ဖော်ပြသမှု",
    "cittajaṃ": "စိတ်မှ မွေးဖွားသော",
    "santati": "ဆက်လက်ဖြစ်ပေါ်ခြင်း", "rūpassa santati": "ရုပ်၏ ဆက်လက်ဖြစ်ပေါ်ခြင်း",
    "lahutā": "ပေါ့ပါးခြင်း", "rūpassa lahutā": "ရုပ်၏ ပေါ့ပါးခြင်း",
    "mudutā": "ပျော့ပျောင်းခြင်း", "rūpassa mudutā": "ရုပ်၏ ပျော့ပျောင်းခြင်း",
    "kammaññatā": "အသုံးပြုရန် သင့်တော်ခြင်း", "rūpassa kammaññatā": "ရုပ်၏ အသုံးပြုရန် သင့်တော်ခြင်း",
    "rūpassa upacayo": "ရုပ်၏ တိုးပွားခြင်း",
    "kabaḷīkāro": "လုတ်ပြု၍ စားရသော", "āhāro": "အာဟာရ", "kabaḷīkāro āhāro": "လုတ်ပြု၍ စားရသော အာဟာရ",
    "āpo": "ရေ", "āpodhātu": "ရေဓာတ်", "ākāsadhātu": "ဟင်းလင်းပြင် ဓာတ်",
    # --- roots (Hetugocchaka)
    "hetū ekato uppajjanti": "အမြစ် … တစ်ပြိုင်နက် ဖြစ်ပေါ်သည်", "ekato": "တစ်ပြိုင်နက်",
    "uppajjati": "ဖြစ်ပေါ်သည်", "uppajjanti": "ဖြစ်ပေါ်သည်",     # one verb form (rule 4; plural ကြ dropped)
    "Lobho": "လောဘ", "lobho": "လောဘ", "Doso": "ဒေါသ", "doso": "ဒေါသ",
    "Alobho": "လောဘ မရှိခြင်း", "adoso": "ဒေါသ မရှိခြင်း", "Amoho": "မောဟ မရှိခြင်း",
    "kusalahetu": KUS + "၏ အမြစ်", "kusalahetū": KUS + "၏ အမြစ်", "akusalahetū": AKUS + "၏ အမြစ်",
    "abyākatahetū": ABY + " သဘောတရားတို့၏ အမြစ်",
    "vipākahetu": "ကံ၏ အကျိုး ဖြစ်သော စိတ်၏ အမြစ်", "kiriyahetu": KIR + " စိတ်၏ အမြစ်",
    # --- clusters (the cluster nouns are the sample values; members as the text names them)
    "āsavo": "စိတ်အစွန်းအထင်း", "kāmāsavo": "ကာမ စိတ်အစွန်းအထင်း", "bhavāsavo": "ဘဝ စိတ်အစွန်းအထင်း",
    "diṭṭhāsavo": "အယူ စိတ်အစွန်းအထင်း", "avijjāsavo": "အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း",
    "saṃyojanaṃ": "နှောင်ကြိုး", "kāmarāgasaṃyojanaṃ": "ကာမရာဂ နှောင်ကြိုး",
    "paṭighasaṃyojanaṃ": "မုန်းတီးမှု နှောင်ကြိုး", "mānasaṃyojanaṃ": "မာန နှောင်ကြိုး",
    "diṭṭhisaṃyojanaṃ": "အယူ နှောင်ကြိုး", "vicikicchāsaṃyojanaṃ": "ယုံမှားမှု နှောင်ကြိုး",
    "parāmāsasaṃyojanaṃ": "မှားယွင်းသော ယူဆမှု နှောင်ကြိုး", "rāgasaṃyojanaṃ": "ရာဂ နှောင်ကြိုး",
    "issāsaṃyojanaṃ": "ငြူစူမှု နှောင်ကြိုး", "macchariyasaṃyojanaṃ": "ဝန်တိုမှု နှောင်ကြိုး",
    "avijjāsaṃyojanaṃ": "အမှန်ကို မသိမှု နှောင်ကြိုး",
    "paṭigha": "မုန်းတီးမှု", "paṭighaṃ": "မုန်းတီးမှု",       # aversion (harmonise item 11), not the Mātikā impact
    "māna": "မာန", "māno": "မာန", "issā": "ငြူစူမှု", "macchariya": "ဝန်တိုမှု",
    "rāga": "ရာဂ", "kāmarāga": "ကာမရာဂ",
    "sīlabbata": "သီလ အကျင့်ဝတ်", "vata": "အကျင့်ဝတ်",
    "sīlabbataparāmāsa": "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု",
    "sīlabbataparāmāso": "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု",
    "parāmāso": "မှားယွင်းသော ယူဆမှု", "parāmāsaṃ": "မှားယွင်းသော ယူဆမှု",
    "Diṭṭhiparāmāso": "အယူဆိုင်ရာ မှားယွင်းသော ယူဆမှု",
    "gantho": "အထုံး", "kāyagantho": "ကိုယ် အထုံး",
    "abhijjhā": "သူ့ဥစ္စာကို လိုချင်ခြင်း", "abhijjhākāyagantho": "သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် အထုံး",
    "byāpādo": "ဖျက်ဆီးလိုစိတ်", "byāpādo kāyagantho": "ဖျက်ဆီးလိုစိတ်ဟူသော ကိုယ် အထုံး",
    "parāmāso kāyagantho": "မှားယွင်းသော ယူဆမှုဟူသော ကိုယ် အထုံး",
    "abhiniveso": "သက်ဝင်ယုံကြည်ခြင်း", "abhiniveso kāyagantho": "သက်ဝင်ယုံကြည်ခြင်းဟူသော ကိုယ် အထုံး",
    "sacca": "အမှန်",
    "nīvaraṇaṃ": "အတားအဆီး", "kāmacchandanīvaraṇaṃ": "ကာမကို လိုလားမှု အတားအဆီး",
    "byāpādanīvaraṇaṃ": "ဖျက်ဆီးလိုစိတ် အတားအဆီး",
    "thinamiddhanīvaraṇaṃ": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု အတားအဆီး",
    "uddhaccakukkuccanīvaraṇaṃ": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု အတားအဆီး",
    "kukkuccanīvaraṇaṃ": "နောင်တ ပူပန်မှု အတားအဆီး", "vicikicchānīvaraṇaṃ": "ယုံမှားမှု အတားအဆီး",
    "avijjānīvaraṇaṃ": "အမှန်ကို မသိမှု အတားအဆီး",
    "chanda": "လိုလားမှု", "kāmacchanda": "ကာမကို လိုလားမှု", "byāpāda": "ဖျက်ဆီးလိုစိတ်",
    "thina": "ထိုင်းမှိုင်းမှု", "thinaṃ": "ထိုင်းမှိုင်းမှု", "middha": "ငိုက်မျဉ်းမှု", "kukkucca": "နောင်တ ပူပန်မှု",
    "kāmupādānaṃ": "ကာမ စွဲလမ်းမှု", "diṭṭhupādānaṃ": "အယူ စွဲလမ်းမှု", "sīlabbatupādānaṃ": "သီလ အကျင့်ဝတ် စွဲလမ်းမှု",
    "vāda": "ဝါဒ", "atta": "အတ္တ",
    "vatthūni": "အခြေခံ", "Dasa": "ဆယ်ပါး",
    "ahirikaṃ": "ဒုစရိုက်ကို မရှက်မှု", "anottappaṃ": "ဒုစရိုက်ကို မကြောက်ရွံ့မှု",
    # «Teva / Tāneva X X ceva …» (subject + the first word of the predicate)
    "saṃyojanāni saṃyojanā": "နှောင်ကြိုး … နှောင်ကြိုး", "nīvaraṇāni nīvaraṇā": "အတားအဆီး … အတားအဆီး",
    "upādānāni upādānā": "စွဲလမ်းမှု … စွဲလမ်းမှု", "kilesā kilesā": "ကိလေသာ … ကိလေသာ",
    # «X ceva Y» (the Mātikā CEVA strings, «၊» dropped: sample rule 6)
    "saṃyojanā ceva saṃyojaniyā": "နှောင်ကြိုးလည်း ဖြစ် နှောင်ကြိုး၏ အာရုံလည်း ဖြစ်နိုင်သော",
    "ganthā ceva ganthaniyā": "အထုံးလည်း ဖြစ် အထုံး၏ အာရုံလည်း ဖြစ်နိုင်သော",
    "nīvaraṇā ceva nīvaraṇiyā": "အတားအဆီးလည်း ဖြစ် အတားအဆီး၏ အာရုံလည်း ဖြစ်နိုင်သော",
    "upādānā ceva upādāniyā": "စွဲလမ်းမှုလည်း ဖြစ် စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်သော",
    # «X-vippayuttā Y» (the «kho pana» pair: «X သဘောတရားများအနက် Y», the «သဘောတရားများအနက်» not in the keyword)
    "saṃyojanavippayuttā saṃyojaniyā": "နှောင်ကြိုးနှင့် ကင်းကွာသော … နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော",
    "ganthavippayuttā ganthaniyā": "အထုံးနှင့် ကင်းကွာသော … အထုံး၏ အာရုံ ဖြစ်နိုင်သော",
    "nīvaraṇavippayuttā nīvaraṇiyā": "အတားအဆီးနှင့် ကင်းကွာသော … အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော",
    "upādānavippayuttā upādāniyā": "စွဲလမ်းမှုနှင့် ကင်းကွာသော … စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော",
    "kilesavippayuttā saṃkilesikā": "ကိလေသာနှင့် ကင်းကွာသော … ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော",
    # --- Mātikā terms not in the sample table (the approved Mātikā strings of the text, «၊» dropped)
    "ācayagāmino": "စုပုံခြင်းဆီသို့ ဦးတည်သော", "apacayagāmino": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "nevācayagāmināpacayagāmino": "စုပုံခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ် လျော့ပါးခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်သော",
    "micchattaniyatā": "မှားယွင်းမှု၌ ကျိန်းသေသော", "sammattaniyatā": "မှန်ကန်မှု၌ ကျိန်းသေသော",
    "pahātabbahetukā": "ပယ်ရမည့် အမြစ် ရှိသော",
    "dassanena pahātabbahetukā": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော",
    "bhāvanāya pahātabbahetukā": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော",
    "avitakkaavicārā": "စတင်ကြံစည်မှုလည်း မရှိ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော",
    "hetuvippayuttā": "အမြစ်နှင့် ကင်းကွာသော",
    "kenaci viññeyyā": "တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော",
    "cittavisaṃsaṭṭhā": "စိတ်နှင့် မရောနှောသော",
    "appaṭighā": "ထိခိုက်မှု မရှိသော",
}


# =====================================================================================================
# context functions and per-segment overrides
# =====================================================================================================
def f_rupa(kw, pali, my):
    """rūpa in rūpāvacara = the fine-material plane «သိမ်မွေ့သော ရုပ်» (sample); in rūpāyatana = the visible object
    «အဆင်းအရောင်» (sample rule 11); elsewhere matter «ရုပ်»."""
    if re.search(r"(?<![aA])rūpāvacar|rūpūpapatti|rūparāga", pali, re.I):
        return "သိမ်မွေ့သော ရုပ်"
    if re.search(r"rūpāyatan", pali, re.I):
        return "အဆင်းအရောင်"
    return "ရုပ်"


def f_akasa(kw, pali, my):
    """ākāsa: in ākāsadhātu (the space element) «ဟင်းလင်းပြင်»; in ākāsānañcāyatana «ကောင်းကင်»."""
    return "ဟင်းလင်းပြင်" if "ākāsadhātu" in pali else "ကောင်းကင်"


WB = r"(?![a-zāīūṃṅñṭḍṇḷ])"
AS_RE = re.compile(r"(?<![a-zāīūṃṅñṭḍṇḷ])kusalato ca (?:vipākato ca(?: kiriyato ca)?|kiriyato ca)")


def ato_use(kw, pali):
    """-> ('as' | 'among', position) for the FIRST occurrence of the keyword in the Pāli segment.
    'as' = inside «kusalato ca vipākato ca [kiriyato ca]» after a jhāna (text «X-အဖြစ်လည်းကောင်း»);
    'among' = with a number or «ahetuke» (text «X-အနက်»)."""
    p = pali.lower()
    spans = [m.span() for m in AS_RE.finditer(p)]
    m = re.search(re.escape(kw.lower()) + WB, p)
    if not m:
        raise KeyError(kw)
    return ("as" if any(a <= m.start() < b for a, b in spans) else "among"), m.start()


ATO_AS = {"kusalato": KUS, "vipākato": "ကံ၏ အကျိုး", "kiriyato": "ပြုရုံမျှသာ"}
ATO_AMONG = {"kusalato": KUS + CIT, "akusalato": AKUS + CIT, "kiriyato": KIR + " " + CIT}


def f_ato(kw, pali, my):
    """The -ato forms (rule 15): the kind of mind without the ablative marker «အနက်» (from among) / «အဖြစ်»
    (as) and without «လည်းကောင်း»."""
    use, pos = ato_use(kw, pali)
    k = low(kw)
    if use == "as":
        return ATO_AS[k]
    if k == "vipākato":
        before = pali.lower()[:pos]
        return "အကျိုး ဖြစ်သော စိတ်" if before.endswith("kusalassa ") else "ကံ၏ အကျိုး ဖြစ်သော စိတ်"
    return ATO_AMONG[k]


COORD = {   # keyword -> (A, B): the two members as the text names them
    "kusalato ca vipākato": (KUS, "ကံ၏ အကျိုး"),
    "vipākato ca kiriyato": ("ကံ၏ အကျိုး", "ပြုရုံမျှသာ"),
    "rūpañca nibbānañca": ("ရုပ်", "နိဗ္ဗာန်"),
    "rūpaṃ nibbānañca": ("ရုပ်", "နိဗ္ဗာန်"),
    "sāmaññaphalāni nibbānañca": ("ရဟန်းအဖြစ်၏ ဖိုလ်", "နိဗ္ဗာန်"),
}


def f_coord(kw, pali, my):
    """Coordinated keywords «A ca B» (rule 16): the text's own coordination, its «၊» dropped:
    «Aနှင့် B»; «Aလည်း၊ Bလည်း» -> «Aလည်း Bလည်း»; «Aအဖြစ်လည်းကောင်း၊ Bအဖြစ်လည်းကောင်း» (the -ato pair after a jhāna)
    -> «Aအဖြစ်လည်းကောင်း Bအဖြစ်လည်းကောင်း»; anything else between A and B (a count) -> «A … B»."""
    k = low(kw)
    a, b = COORD[k]
    if k == "vipākato ca kiriyato" and ato_use(kw, pali)[0] == "among":
        return "အကျိုး ဖြစ်သော စိတ်အနက်လည်းကောင်း " + KIR + " စိတ်အနက်လည်းကောင်း"
    for sep, x in (("နှင့် ", ""),):
        if a + sep + b in my:
            return a + sep + b
    for x in ("အဖြစ်လည်းကောင်း", "လည်း"):
        if f"{a}{x}၊ {b}{x}" in my or f"{a}{x} {b}{x}" in my:
            return f"{a}{x} {b}{x}"
    return f"{a} … {b}"


JNUM = {"ekaka": 1, "duka": 2, "tika": 3, "catukka": 4, "pañcaka": 5}
NUMW = {1: "တစ်", 2: "နှစ်", 3: "သုံး", 4: "လေး", 5: "ငါး"}
JPL = {"rūpāvacara": RUPAV, "lokuttara": LOKUT}


def f_jh(kw, pali, my):
    """Jhāna-method groups «lokuttara-tika-catukka-jjhānā» = the three jhānas of the fourfold and the four of the
    fivefold method, as the text builds them (rule 17)."""
    m = re.fullmatch(r"(rūpāvacara|lokuttara)(ekaka|duka|tika|catukka)(duka|tika|catukka|pañcaka)jjhānā", low(kw))
    pl, a, b = JPL[m[1]], JNUM[m[2]], JNUM[m[3]]
    return (f"{pl} ဈာန် လေးပါး ခွဲနည်းအရ ဈာန် {NUMW[a]}ပါးနှင့် ဈာန် ငါးပါး ခွဲနည်းအရ ဈာန် {NUMW[b]}ပါး")


FUNCS = {"rupa": f_rupa, "akasa": f_akasa, "ato": f_ato, "coord": f_coord, "jh": f_jh}

CTX = {
    # sid: {keyword: value}
    # «Katame dhammā asekkhā?»: the fragment sekkhā rests on «ကျင့်ကြံမှု» of «ကျင့်ကြံမှု ပြီးဆုံးသူ၏» (rule 8);
    # the sample's «ကျင့်ကြံဆဲသူ၏» (trainee) is not in this segment.
    "1-1415": {"sekkhā": "ကျင့်ကြံမှု"},
    # «apacayagāmino»: caya (accumulation) has no Burmese word in «လျော့ပါးခြင်းဆီသို့ ဦးတည်သော».
    "1-1412": {"caya": NONE},
}

# chapter -> its own table (looked up first); every table is also shared with the other chapters
SECTIONS = {
    "preamble": T_PREAMBLE,
    "1-matika": T_MATIKA,
    "5-atthakathakandam": T_ATTHA,
}
CHAPTERS = ["5-atthakathakandam"]   # chapters written by this run

SHARED = {}
for _t in SECTIONS.values():
    for _k, _v in _t.items():
        SHARED.setdefault(_k, _v)
SAMPLE_KEYS = set(T_PREAMBLE) | set(T_MATIKA)


# =====================================================================================================
# new rules (written to map-table-5.md); the sample rules 1-11 of map-table.md apply unchanged
# =====================================================================================================
NEW_RULES = """## New rules for chapter 5 (rules 1–11 of map-table.md apply unchanged)

12. **Numbers**: a bare numeral keyword keeps the count the text uses, with its classifier «ပါး» (harmonise
    decision 5, as 2-04, 4-01 rule 18 and 4-03: Dvādasa = ဆယ့်နှစ်ပါး, ekādasa = ဆယ့်တစ်ပါး, dasa / Dasa = ဆယ်ပါး);
    only where the text counts with «မျိုး» (dasavidhena = ဆယ်မျိုးဖြင့်, 3-01 / 3-03) is the number word bare, because
    vidha has its own word there. A keyword that contains a count keeps it (pañcaviññāṇāni =
    ငါးပါးစီ ရှိသော သိစိတ်; the jhāna-method groups, rule 17).
13. **ṭhapetvā / Ṭhapetvā** (absolutive used as the preposition «except») = the text's «ချန်ထား၍», kept in the
    conjunctive form because that form is the preposition; upādāya (absolutive «depending on») likewise = «မှီ၍».
14. **na vattabbā / vattabbo / vattabbaṃ**: the keyword lost the free negative na (rule 8): «ခေါ်ဆို၍ မရ» (cannot be
    called) without its negative = «ခေါ်ဆို၍ ရ». A keyword «vattabbā X» / «vattabbaṃ Xnti» = the Mātikā string of X
    + « … ခေါ်ဆို၍ ရ» (Burmese order: the term, then the verb; the plural «သဘောတရားများ», the quotative «ဟု(လည်းကောင်း)»
    and the other terms between are not in the keyword).
15. **The -ato forms** (kusalato, akusalato, kiriyato, vipākato) = the kind of mind without the ablative markers
    «အနက်» (from among) / «အဖြစ်» (as) and without «လည်းကောင်း» (case markers, rule 1). The text builds two
    constructions; the FIRST occurrence of the keyword in the Pāli segment decides:
    with a number («kāmāvacarakusalato cattāro», «akusalato cha», «kiriyato cha», «kāmāvacarassa vipākato») = the
    list noun «ကုသိုလ်စိတ် / အကုသိုလ်စိတ် / ပြုရုံမျှသာ ဖြစ်သော စိတ် / ကံ၏ အကျိုး ဖြစ်သော စိတ်» (after
    «kusalassa / akusalassa»: «အကျိုး ဖြစ်သော စိတ်», since the text says «ကုသိုလ်၏ အကျိုး …»);
    after a jhāna («kusalato ca vipākato ca kiriyato ca») = «ကုသိုလ် / ကံ၏ အကျိုး / ပြုရုံမျှသာ».
16. **Coordinated keywords** «A ca B» / «Añca Bñca» (rūpañca nibbānañca, rūpaṃ nibbānañca, sāmaññaphalāni
    nibbānañca, kusalato ca vipākato, vipākato ca kiriyato) = the text's own coordination, «၊» dropped (rule 6):
    «ရုပ်နှင့် နိဗ္ဗာန်» where the Pāli has no comma; «ရုပ်လည်း နိဗ္ဗာန်လည်း» where it has «rūpañca, nibbānañca»;
    «ကုသိုလ်အဖြစ်လည်းကောင်း ကံ၏ အကျိုးအဖြစ်လည်းကောင်း» after a jhāna; a count between the members (ဖိုလ်
    လေးပါးလည်း) gives «A … B». The connectors stay because they carry the ca. A single «X ca» keeps no «လည်း»
    (rūpañca = ရုပ်, uppanno ca vicāro = ဖြစ်ပေါ်သော ဆက်လက်သုံးသပ်မှု).
17. **Jhāna-method groups** (lokuttaratikacatukkajjhānā …) = the text's phrase in full: «PLANE ဈာန် လေးပါး ခွဲနည်းအရ
    ဈာန် A-ပါးနှင့် ဈာန် ငါးပါး ခွဲနည်းအရ ဈာန် B-ပါး» (its «နှင့်» joins the two methods and stays).
    Fragments: pañcaka = ဈာန် ငါးပါး, naye = ခွဲနည်း, pañcakanaye = ဈာန် ငါးပါး ခွဲနည်း (the «အရ» = according to,
    a postposition, goes).
18. **Kinds of mind**: the neuter list nouns kusalaṃ / akusalaṃ, the locatives kusalesu / akusalesu / kiriyesu and
    kiriyābyākataṃ map to the text's noun with «စိတ်» (ကုသိုလ်စိတ်, … ပြုရုံမျှသာ ဖြစ်သော ABY စိတ်): the text adds
    «စိတ်» to every such noun (notes-ch5: bare ကုသိုလ် reads «merit»). The compound fragments kusala / akusala /
    kusalassa keep the bare term (ကုသိုလ် / အကုသိုလ်), kiriyā / kiriya the attributive «ပြုရုံမျှသာ ဖြစ်သော».
    kusalesu here is «ကုသိုလ်စိတ်» (the Mātikā «kusalesu dhammesu» = ကုသိုလ် stays in its own segments).
19. **«dhammā X»** (the keyword order of this chapter: «Katame dhammā X?») = the value of «X dhammā» (sample rule 5):
    dhammā kusalā = ကုသိုလ် သဘောတရား; dhammā no cittasamuṭṭhānā = စိတ်မှ ဖြစ်ပေါ်လာသည် မဟုတ်သော သဘောတရား.
    Mātikā terms that the sample table lacks take the approved Mātikā string of the text, «၊» dropped.
20. **Sense by context** (rule 11 continued): rūpa / rūpañca / rūpaṃ = matter «ရုပ်» (the sample's rūpañca
    «ရုပ်ပိုင်း» is the nāma-rūpa dyad), but rūpa in rūpāvacara = «သိမ်မွေ့သော ရုပ်» and in rūpāyatana = the visible
    object «အဆင်းအရောင်»; ākāsa = «ကောင်းကင်» in ākāsānañcāyatana, «ဟင်းလင်းပြင်» in ākāsadhātu; paṭigha = aversion
    «မုန်းတီးမှု» (harmonise item 11), not the Mātikā impact «ထိခိုက်မှု».
21. **Two-word frames**: «Tāneva saṃyojanāni saṃyojanā ceva …» gives the keyword «saṃyojanāni saṃyojanā» (subject +
    predicate noun) = «နှောင်ကြိုး … နှောင်ကြိုး» (the «များသည်ပင်» between is particles); «X-vippayuttā Y» (the
    «kho pana» pair) = «X-string … Y-string» (the «သဘောတရားများအနက်» between is not in the keyword); «X ceva Y» =
    the Mātikā CEVA string, «၊» dropped.
22. **Presence, three more ending rules** (the check accepts, besides the sample's «attr», «verb» and «neg-infix»):
    «fut»: a chunk ending in «မည့်» against the text's «မည်» of the negative «… ပယ်ရမည် မဟုတ်သော»;
    «attr» also before «၊» (the coordinated predicate «မမြင်နိုင်၊ ထိခိုက်မှုလည်း မရှိသော»: one «သော» serves both);
    «verb» also from «ကြသည်» / «ကြရာ» (the plural verb, ကြ dropped as a plural marker).
"""


# =====================================================================================================
# engine (copied from map_all.py; lookup() extended by «dhammā X», presence() by rule 22)
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


def lookup(ch, sid, kw, pali, my):
    o = CTX.get(sid, {})
    v = table_get(o, kw)
    if v is None:
        v = table_get(SECTIONS.get(ch, {}), kw)
    if v is None:
        v = table_get(SHARED, kw)
    if v is not None:
        return resolve(v, kw, pali, my)
    ws = kw.split()
    core = None
    if len(ws) >= 2 and ws[-1] == "dhammā":
        core = ws[:-1]
    elif len(ws) >= 2 and ws[0] == "dhammā":
        core = ws[1:]
    if core:
        neg = core[0] in ("no", "na") and len(core) > 1
        c = " ".join(core[1:] if neg else core)
        base = table_get(SECTIONS.get(ch, {}), c) or table_get(SHARED, c)
        base = resolve(base, c, pali, my)
        if base:
            if neg:
                base = neg_attr(base)
            if base:
                return base + " " + DH
    raise KeyError(kw)


# ---- presence check --------------------------------------------------------------------------------
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "၊")   # dictionary «Xသော» <- text «X»+one of these
VERB_FROM = ("ပါ၏", "၏", "ပြီ", "သော", "ကြသည်", "ကြရာ")              # dictionary «Xသည်» <- text «X»+one of these


def chunk_present(c, text):
    """-> rule name ('exact', 'attr', 'verb', 'fut', 'neg-infix') or None."""
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
    if c.endswith("မည့်") and c[:-4] + "မည်" in text:
        return "fut"
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


def sample_value(kw):
    """The sample's value for a keyword (None if the sample tables lack it), for the review table; «X dhammā» /
    «dhammā X» built from a sample value (rules 5, 19) count as the sample's."""
    for t in (T_PREAMBLE, T_MATIKA):
        v = table_get(t, kw)
        if v is not None:
            return v
    ws = kw.split()
    core = ws[:-1] if len(ws) >= 2 and ws[-1] == "dhammā" else ws[1:] if len(ws) >= 2 and ws[0] == "dhammā" else None
    if core:
        neg = core[0] in ("no", "na") and len(core) > 1
        c = " ".join(core[1:] if neg else core)
        base = table_get(T_MATIKA, c)
        if base and not base.startswith("@"):
            base = neg_attr(base) if neg else base
            if base:
                return base + " " + DH
    return None


def write_table(table, ruled_all, summary):
    with open(HERE / "map-table-5.md", "w", encoding="utf-8") as f:
        f.write("# pi-1 Burmese keyword mapping, chapter 5 (Aṭṭhakathākaṇḍa): new rules and review table\n\n")
        f.write("Written by map_5.py. Burmese from the FINAL text of this track only "
                "(AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters). The approved rules 1–11 and the "
                "values of map-table.md (preamble, 1-matika) apply unchanged; Mātikā items quoted in this chapter keep "
                "the 1-matika values.\n\n")
        for ch, n, nne in summary:
            f.write(f"- {ch}: {n} lines, {nne} × (no direct equivalent)\n")
        f.write("\n" + NEW_RULES)
        f.write("\n## Per-segment overrides (CTX)\n\n| segment | keyword | value | reason |\n|---|---|---|---|\n")
        f.write("| 1-1415 | sekkhā | ကျင့်ကြံမှု | fragment of asekkhā; the segment has only «ကျင့်ကြံမှု ပြီးဆုံးသူ၏» "
                "(rule 8) |\n")
        f.write("| 1-1412 | caya | (no direct equivalent) | fragment of apacaya; «လျော့ပါးခြင်း» (decrease) has no "
                "word for caya (accumulation) |\n")
        f.write("\n## Presence: chunks matched by a dictionary-form rule (not literally in the segment)\n\n")
        f.write("Every other chunk of every value occurs literally in its segment's Burmese (particles that the "
                "rules strip follow the chunk in the text).\n\n| segment | keyword | chunk | rule |\n|---|---|---|---|\n")
        for sid, k, c, r in ruled_all:
            f.write(f"| {sid} | {k} | {c} | {r} |\n")
        f.write("\n## Keyword → Burmese in this chapter (number of uses)\n\n«sample» = the value of map-table.md "
                "(unchanged); «NEW» = a keyword the sample tables lack; «≠ sample» = a sense or form this chapter "
                "needs (rules 18, 20). Several values = the keyword reads differently by context.\n\n"
                "| Pāli keyword | Burmese (uses) | |\n|---|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            sv = sample_value(kw)
            vals = list(table[kw])
            if sv is None:
                tag = "NEW"
            elif not sv.startswith("@") and any(v != sv for v in vals):
                tag = "≠ sample"
            else:
                tag = "sample"
            f.write(f"| {kw} | " + " / ".join(f"{v} ({n})" for v, n in table[kw].most_common()) + f" | {tag} |\n")


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
    write_table(table, ruled_all, summary)
    for ch, ln, bad, fails, punct, ruled, nne in results:
        print(f"{ch}: lines {ln} | keyword preservation bad {bad} | presence failures {len(fails)} "
              f"(rule-matched chunks {len(ruled)}) | comma/၊ {punct} | no-equivalent {nne}")
        for f_ in fails:
            print("   FAIL", f_)
    for sid, k, c, r in ruled_all:
        print(f"   rule {r:9} {sid:10} {k} : {c}")
    print("total no direct equivalent:", tot_nne, "| distinct keywords:", len(table))
