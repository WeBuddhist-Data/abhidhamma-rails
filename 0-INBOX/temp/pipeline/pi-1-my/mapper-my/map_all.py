"""Pāli→Burmese keyword mapping for pi-1 (Dhammasaṅgaṇī, «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»).

usage (python3 -I -X utf8):
  map_all.py             writes <ch>.mapped.md for every chapter in CHAPTERS and map-table.md, then verifies them
                         (keyword preservation, presence of every value chunk in its segment, no ", " / «၊» in a value)
  map_all.py --report    writes nothing; lists unmapped keywords and presence failures
  map_all.py --seg ID    prints Pāli, Burmese, keywords and mapping of one segment

Method (as the pi-1 Marathi mapper, brief burmese-mapper-brief.md): the Burmese is the FINAL text of this track
(AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters). No other Burmese source is used. Every keyword is
looked up in
  CTX[sid]       per-segment overrides (where the context changes the sense),
  T_<chapter>    the chapter's own table (keyword -> Burmese, dictionary form), then the tables of all chapters,
                 first letter case-insensitive; a value may be «@name» (a context function f(kw, pali, my)),
  compose()      «X dhammā» = T[X] + « သဘောတရား»; «no X dhammā» / «na X dhammā» = the negative attributive of T[X]
                 («…သော» -> «…သည် မဟုတ်သော», as the text builds it) + « သဘောတရား».
Adding a chapter: write its table T_<ch> (and CTX entries), register it in SECTIONS, add it to CHAPTERS.
The dictionary-form rules are in RULES (written to the top of map-table.md).
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
# context functions and per-segment overrides
# =====================================================================================================
def f_rupa(kw, pali, my):
    """rūpa in rūpāvacara = the fine-material plane «သိမ်မွေ့သော ရုပ်»; elsewhere matter «ရုပ်» (the visible
    object «အဆင်းအရောင်» is added with the chapters that use it)."""
    if re.search(r"(?<![aA])rūpāvacar|rūpūpapatti|rūparāga", pali):
        return "သိမ်မွေ့သော ရုပ်"
    return "ရုပ်"


FUNCS = {"rupa": f_rupa}

CTX = {
    # sid: {keyword: value}
}

# chapter -> its own table (looked up first); every table is also shared with the other chapters
SECTIONS = {
    "preamble": T_PREAMBLE,
    "1-matika": T_MATIKA,
}
CHAPTERS = ["preamble", "1-matika"]   # chapters written by this run (append the next ones here)

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
    if len(ws) >= 2 and ws[-1] == "dhammā":
        neg = ws[0] in ("no", "na")
        core = " ".join(ws[1:-1] if neg else ws[:-1])
        base = table_get(SECTIONS.get(ch, {}), core) or table_get(SHARED, core)
        base = resolve(base, core, pali, my)
        if base:
            if neg:
                base = neg_attr(base)
            if base:
                return base + " " + DH
    raise KeyError(kw)


# ---- presence check --------------------------------------------------------------------------------
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ")   # dictionary «Xသော» <- text «X»+one of these
VERB_FROM = ("ပါ၏", "၏", "ပြီ", "သော")                         # dictionary «Xသည်» <- text «X»+one of these


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


def write_table(table, ruled_all):
    with open(HERE / "map-table.md", "w", encoding="utf-8") as f:
        f.write("# pi-1 Burmese keyword mapping: rules and review table (Dhammasaṅgaṇī, sample: "
                + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_all.py. Burmese from the FINAL text of this track only "
                "(AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters).\n\n")
        f.write(RULES)
        f.write("\n## Presence: chunks matched by a dictionary-form rule (not literally in the segment)\n\n")
        f.write("Every other chunk of every value occurs literally in its segment's Burmese (particles that the "
                "rules strip follow the chunk in the text).\n\n| segment | keyword | chunk | rule |\n|---|---|---|---|\n")
        for sid, k, c, r in ruled_all:
            f.write(f"| {sid} | {k} | {c} | {r} |\n")
        f.write("\n## Keyword → Burmese (number of uses)\n\nSeveral values = the keyword reads differently by "
                "context.\n\n| Pāli keyword | Burmese (uses) |\n|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            f.write(f"| {kw} | " + " / ".join(f"{v} ({n})" for v, n in table[kw].most_common()) + " |\n")


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
