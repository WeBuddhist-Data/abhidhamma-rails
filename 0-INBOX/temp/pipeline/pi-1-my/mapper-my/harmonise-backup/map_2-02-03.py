"""Pāli→Burmese keyword mapping for pi-1 chapters 2-02 and 2-03 (Cittuppādakaṇḍa: fine-material, immaterial,
three-plane and world-transcending wholesome cittas). A COPY of map_all.py (the approved sample's tables T_PREAMBLE /
T_MATIKA, compose rules, context function and verifier, copied unchanged), plus the table T_CU2 of these two chapters,
the context functions they need and the new rules 12-20 (RULES_NEW, written to map-table-2-02-03.md).
It writes only 2-02-cittuppadakandam.mapped.md, 2-03-cittuppadakandam.mapped.md and map-table-2-02-03.md.

usage (python3 -I -X utf8):
  map_2-02-03.py             writes <ch>.mapped.md for the two chapters and map-table-2-02-03.md, then verifies them
                             (keyword preservation, presence of every value chunk in its segment, no ", " / «၊»)
  map_2-02-03.py --report    writes nothing; lists unmapped keywords and presence failures
  map_2-02-03.py --seg ID    prints Pāli, Burmese, keywords and mapping of one segment
  map_2-02-03.py --show N ID …   prints Pāli, Burmese and keywords of segments, cut to N characters

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


# =====================================================================================================
# chapters 2-02 / 2-03 (one table for both: the same jhāna / path formulas and factor lists)
# =====================================================================================================
_KAYA = "စိတ်၏ အဖော်တို့"         # kāya- of kāyapassaddhi …: kept whole with တို့ (apart from cetasika «စိတ်၏ အဖော်»), as 2-01
T_CU2 = {
    # --- headings, colophons
    "rūpāvacara": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော", "arūpāvacara": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော",
    "kāmāvacara": "ကာမဘုံနှင့် ဆိုင်သော", "avacara": "ဘုံနှင့် ဆိုင်သော",
    "kāmāvacaraṃ": "ကာမဘုံနှင့် ဆိုင်သော", "avacaraṃ": "ဘုံနှင့် ဆိုင်သော",
    "kusalaṃ": "ကုသိုလ်", "kusala": "ကုသိုလ်",
    "bhūmaka": "ဘုံ … နှင့် ဆိုင်သော",                          # Tebhūmaka «ဘုံ သုံးပါးနှင့် ဆိုင်သော» (rule 10)
    "lokuttara": "လောကကို ကျော်လွန်သော", "lokuttarakusalaṃ": "လောကကို ကျော်လွန်သော ကုသိုလ်",
    "lokuttaraṃ": "လောကကို ကျော်လွန်သော", "lokuttaraṃ cittaṃ": "လောကကို ကျော်လွန်သော စိတ်",
    "catukka": "ဈာန် လေးပါး", "catukkanayo": "ဈာန် လေးပါး နည်း",
    "pañcaka": "ဈာန် ငါးပါး", "pañcakanayo": "ဈာန် ငါးပါး နည်း",
    "nayo": "နည်း", "nayā": "နည်း", "vīsati": "နှစ်ဆယ်",
    "soḷasakkhattukaṃ": "တစ်ဆယ့်ခြောက်ကြိမ် နည်း", "soḷasakkhattukāni": "တစ်ဆယ့်ခြောက်ကြိမ် နည်း",
    "aṭṭhakkhattukaṃ": "ရှစ်ကြိမ် နည်း",
    "paṭipadā": "ကျင့်စဉ်", "ārammaṇāni": "အာရုံ",
    "abhibhāyatanāni": "လွှမ်းမိုးရာ နယ်ပယ်", "abhibhu": "လွှမ်းမိုးရာ",
    "āyatanāni": "@ayatanani",
    "vimokkhāni": "လွတ်မြောက်ခြင်း",
    "brahma": "ဗြဟ္မစိုရ်", "vihāra": "ဗြဟ္မစိုရ်",               # one Burmese word for brahmavihāra (unclear)
    "jhānāni": "ဈာန်", "asubha": "မတင့်တယ်ခြင်း",
    "suddhika": "သက်သက်", "suddhikapaṭipadā": "ကျင့်စဉ် သက်သက်",
    "suññata": "ဆိတ်သုဉ်းခြင်း", "appaṇihita": "တောင့်တမှု မရှိခြင်း",
    "mūlaka": "အခြေခံသော", "mūlakapaṭipadā": "အခြေခံသော ကျင့်စဉ်",   # text «…ကို အခြေခံသော» (rule 3)
    "adhipati": "အကြီးအမှူး",
    "maggo": "မဂ်",
    # --- the jhāna opening
    "rūpa": "@rupa2", "arūpa": "ရုပ်မရှိသော",
    "upapattiyā": "ဖြစ်ပေါ်ရန်", "maggaṃ": "@maggam", "upapattiyā maggaṃ": "ဖြစ်ပေါ်ရန် လမ်း",
    "bhāveti": "ပွားများသည်", "maggaṃ bhāveti": "လမ်းကို ပွားများသည်",
    "upasampajja": "ဝင်စား၍", "viharati": "နေသည်", "upasampajja viharati": "ဝင်စား၍ နေသည်",
    "jhānaṃ": "ဈာန်", "pañcamaṃ": "ပဉ္စမ", "catutthaṃ jhānaṃ": "စတုတ္ထ ဈာန်",
    "kāmehi": "ကာမ", "vivicca": "ကင်းဆိတ်၍", "vivicceva": "ကင်းဆိတ်၍သာ", "eva": "သာ",
    "vivicceva kāmehi": "ကာမတို့မှ ကင်းဆိတ်၍သာ",
    "akusalehi": "အကုသိုလ်", "akusalehi dhammehi": "အကုသိုလ် သဘောတရား",
    "vitakkaṃ": "စတင်ကြံစည်မှု", "vicāraṃ": "ဆက်လက်သုံးသပ်မှု",
    "vivekajaṃ": "ကင်းဆိတ်ခြင်းမှ ဖြစ်ပေါ်သော", "samādhijaṃ": "သမာဓိမှ ဖြစ်ပေါ်သော",
    "sukhaṃ": "သာယာမှု", "sukhañca": "သာယာမှု", "sukhassa": "သာယာမှု", "sukha": "@sukha",
    "dukkha": "@dukkha", "dukkhassa": "နာကျင်မှု",
    "vitakka": "စတင်ကြံစည်မှု", "vicārānaṃ": "ဆက်လက်သုံးသပ်မှု", "vūpasamā": "ငြိမ်းသွားခြင်း",
    "ajjhattaṃ": "မိမိ၌", "sampasādanaṃ": "ကြည်လင်မှု", "cetaso": "စိတ်",
    "ekodibhāvaṃ": "စုစည်း တည်ငြိမ်စေသော",
    "pītiyā": "ပီတိ", "virāgā": "ပြယ်ပျောက်သွားခြင်း",
    "upekkhako": "ဥပေက္ခာ ရှိသော", "upekkhako ca viharati": "ဥပေက္ခာ ရှိလျက်လည်း နေသည်",
    "sato": "သတိ ရှိသော", "sampajāno": "ကောင်းစွာ ဆင်ခြင်သိမြင်သော",
    "kāyena": _KAYA, "paṭisaṃvedeti": "ခံစားသည်", "ariyā": "အရိယာ", "ācikkhanti": "ပြောကြားသည်",
    "pahānā": "ပယ်ခြင်း", "sukhassa ca pahānā": "သာယာမှုကိုလည်း ပယ်ခြင်း",
    "atthaṅgamā": "ချုပ်ငြိမ်းသွားခြင်း", "domanassānaṃ": "စိတ်ဆင်းရဲမှု",
    "adukkhamasukhaṃ": "မနာကျင် မသာယာသော", "pārisuddhiṃ": "စင်ကြယ်သော",
    "kasiṇaṃ": "ကသိုဏ်း", "pathavī": "မြေ", "āpo": "ရေ", "tejo": "မီး", "vāyo": "လေ",
    "nīla": "အပြာ", "pīta": "အဝါ", "lohita": "အနီ", "odāta": "အဖြူ",
    "abhiññaṃ": "ထူးကဲစွာ သိခြင်း", "paṭipadaṃ": "ကျင့်စဉ်",
    "dukkhapaṭipadaṃ": "ကျင့်စဉ် ခက်ခဲသော", "sukhapaṭipadaṃ": "ကျင့်စဉ် လွယ်ကူသော",
    "dandha": "နှေးကွေးသော", "dandhābhiññaṃ": "ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    "khippa": "လျင်မြန်သော", "khippābhiññaṃ": "ထူးကဲစွာ သိခြင်း လျင်မြန်သော",
    "paṭipadaṃ dandha": "ကျင့်စဉ် … နှေးကွေးသော", "paṭipadaṃ khippa": "ကျင့်စဉ် … လျင်မြန်သော",
    "parittaṃ": "အကန့်အသတ် ရှိသော", "parittāni": "အကန့်အသတ် ရှိသော",
    "appamāṇaṃ": "အတိုင်းအဆ မရှိသော", "appamāṇāni": "အတိုင်းအဆ မရှိသော",
    "ārammaṇaṃ": "အာရုံ",
    "parittārammaṇaṃ": "အကန့်အသတ် ရှိသည်ကို အာရုံပြုသော",
    "appamāṇārammaṇaṃ": "အတိုင်းအဆ မရှိသည်ကို အာရုံပြုသော",
    # --- abhibhāyatana, vimokkha, brahmavihāra, asubha
    "ajjhattaṃ arūpa": "မိမိ၌ ရုပ်ဟု မမှတ်သိသော",          # the a- of arūpa- is the text's «မ» of «မမှတ်သိဘဲ»
    "saññī": "မှတ်သိသော", "rūpasaññī": "ရုပ်ဟု မှတ်သိသော",       # fragments of arūpasaññī (rule 8)
    "bahiddhā": "ပြင်ပ၌",                                        # outside (harmonise-notes item 9), rule 11
    "rūpāni": "ရုပ်", "abhibhuyya": "လွှမ်းမိုး၍", "jānāmi": "သိသည်", "passāmīti": "မြင်သည်",
    "suvaṇṇa": "အဆင်း လှသော", "dubbaṇṇāni": "အဆင်း ဆိုးသော",
    "nīlāni": "ပြာသော", "pītāni": "ဝါသော", "lohitakāni": "နီသော", "odātāni": "ဖြူသော",
    "vaṇṇāni": "အဆင်း", "nidassanāni": "မြင်ရသော", "nibhāsāni": "တောက်ပသော",
    "rūpī": "ရုပ် ရှိသော", "subhanti": "တင့်တယ်သည်",
    "sahagataṃ": "အတူ ဖြစ်သော", "mettā": "မေတ္တာ", "karuṇā": "ကရုဏာ", "muditā": "မုဒိတာ",
    "mettāsahagataṃ": "မေတ္တာနှင့်အတူ ဖြစ်သော", "upekkhāsahagataṃ": "ဥပေက္ခာနှင့်အတူ ဖြစ်သော",
    "uddhumātaka": "ဖူးရောင်နေသော အလောင်း", "vinīlaka": "ညိုမည်းနေသော အလောင်း",
    "vipubbaka": "ပြည်ယိုနေသော အလောင်း", "vicchiddaka": "ပြတ်ထွက်နေသော အလောင်း",
    "vikkhāyitaka": "ကိုက်စားခံရသော အလောင်း", "vikkhittaka": "ပြန့်ကျဲနေသော အလောင်း",
    "hata": "ခုတ်ထစ်သော", "lohitaka": "သွေးစွန်းနေသော အလောင်း",
    "puḷavaka": "ပိုးလောက်တက်နေသော အလောင်း", "aṭṭhika": "အရိုးစု",
    # --- immaterial
    "sabbaso": "အလုံးစုံ", "samatikkamā": "ကျော်လွန်ခြင်း", "samatikkamma": "ကျော်လွန်၍",
    "nānatta": "အမျိုးမျိုး ကွဲပြားမှု", "saññānaṃ": "မှတ်သိမှု", "manasikārā": "နှလုံး သွင်းခြင်း",
    "ākāsa": "ကောင်းကင်", "ānañca": "အဆုံး မရှိသော",
    "ānañcāyatana": "အဆုံး မရှိသော … နယ်ပယ်", "ānañcāyatanaṃ": "အဆုံး မရှိသော … နယ်ပယ်",
    "viññāṇañca": "အဆုံး မရှိသော သိစိတ်", "viññāṇañcāyatanaṃ": "အဆုံး မရှိသော သိစိတ် နယ်ပယ်",
    "ākiñcañña": "ဘာမျှ မရှိသော", "nāsaññā": "မှတ်သိမှု မရှိသည် မဟုတ်သော",
    # --- the kāmāvacara opening (tebhūmaka)
    "kāma": "ကာမ", "kusalaṃ cittaṃ": "ကုသိုလ်စိတ်", "uppannaṃ": "ဖြစ်ပေါ်လာသော",
    "somanassasahagataṃ": "ဝမ်းမြောက်မှုနှင့်အတူ ဖြစ်သော", "ñāṇa": "ဉာဏ်",
    "sampayuttaṃ": "ယှဉ်တွဲသော", "vippayuttaṃ": "ကင်းကွာသော", "ñāṇavippayuttaṃ": "ဉာဏ်နှင့် ကင်းကွာသော",
    "saṅkhārena": "တိုက်တွန်းမှု",
    "hīnaṃ": "ယုတ်ညံ့သော", "majjhimaṃ": "အလယ်အလတ်", "paṇītaṃ": "မွန်မြတ်သော",
    "chanda": "ဆန္ဒ", "vīmaṃsā": "စုံစမ်းဆင်ခြင်မှု",
    "adhipateyyaṃ": "အကြီးအမှူးပြုသော", "ādhipateyyaṃ": "အကြီးအမှူးပြုသော",
    # --- the lokuttara opening
    "lokuttaraṃ jhānaṃ": "လောကကို ကျော်လွန်သော ဈာန်",
    "lokuttaraṃ jhānaṃ bhāveti": "လောကကို ကျော်လွန်သော ဈာန်ကို ပွားများသည်",
    "niyyānikaṃ": "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော", "gāmiṃ": "ဦးတည်သော", "caya": NONE,
    "niyyānikaṃ apacayagāmiṃ": "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "diṭṭhigatānaṃ": "အယူမှား", "pahānāya": "ပယ်ရန်", "diṭṭhigatānaṃ pahānāya": "အယူမှားတို့ကို ပယ်ရန်",
    "bhūmiyā": "အဆင့်", "pattiyā": "ရောက်ရန်",
    "kāmarāga": "ကာမရာဂ", "rāga": "ရာဂ", "byāpādānaṃ": "ဖျက်ဆီးလိုစိတ်", "tanubhāvāya": "ပါးလျစေရန်",
    "avasesa": "အကြွင်းအကျန်",                                     # fragment of anavasesa (rule 8)
    "māna": "မာန", "uddhacca": "ယောက်ယက်ခတ်မှု", "avijjāya": "အမှန်ကို မသိမှု",
    "suññataṃ": "ဆိတ်သုဉ်းသော", "appaṇihitaṃ": "တောင့်တမှု မရှိသော",
    # lokuttaraṃ X bhāveti (^1-357)
    "khandhaṃ": "အစုအဝေး", "bojjhaṅgaṃ": "ဗောဇ္ဈင်", "samathaṃ": "စိတ်ငြိမ်သက်ခြင်း", "phassaṃ": "တွေ့ထိမှု",
    "dhātuṃ": "ဓာတ်", "vedanaṃ": "ခံစားမှု", "cetanaṃ": "စေ့ဆော်မှု", "saññaṃ": "မှတ်သိမှု",
    "āhāraṃ": "အာဟာရ", "āyatanaṃ": "အာရုံခံ နယ်ပယ်", "saccaṃ": "သစ္စာ", "indriyaṃ": "စွမ်းရည်",
    "balaṃ": "စွမ်းအား", "dhammaṃ": DH, "padhānaṃ": "ကြိုးပမ်းအားထုတ်ခြင်း",
    "paṭṭhānaṃ": "ပဋ္ဌာန်", "iddhi": "ဣဒ္ဓိ",                            # inside the loans သတိပဋ္ဌာန် / ဣဒ္ဓိပါဒ်
    # --- the factor lists (the 2-01 names, as these chapters' Burmese has them)
    "phasso": "တွေ့ထိမှု", "vedanā": "ခံစားမှု", "saññā": "မှတ်သိမှု", "cetanā": "စေ့ဆော်မှု", "cittaṃ": "စိတ်",
    "cittassa": "စိတ်", "vitakko": "စတင်ကြံစည်မှု", "vicāro": "ဆက်လက်သုံးသပ်မှု",
    "ekaggatā": "စူးစိုက်မှု", "cittassekaggatā": "စိတ်၏ စူးစိုက်မှု",
    "indriyāni": "စွမ်းရည်", "saddhā": "ယုံကြည်မှု", "samādhi": "သမာဓိ", "jīvita": "အသက်",
    "somanassa": "ဝမ်းမြောက်မှု", "mana": "မနော", "upekkhindriyaṃ": "ဥပေက္ခာ၏ စွမ်းရည်",
    "saddhindriyaṃ": "ယုံကြည်မှု၏ စွမ်းရည်", "vīriyindriyaṃ": "ဝီရိယ၏ စွမ်းရည်",
    "satindriyaṃ": "သတိ၏ စွမ်းရည်", "samādhindriyaṃ": "သမာဓိ၏ စွမ်းရည်", "paññindriyaṃ": "ပညာ၏ စွမ်းရည်",
    "manindriyaṃ": "မနော၏ စွမ်းရည်", "somanassindriyaṃ": "ဝမ်းမြောက်မှု၏ စွမ်းရည်",
    "jīvitindriyaṃ": "အသက်၏ စွမ်းရည်",
    "anaññātaññassāmītindriyaṃ": "မသိရသေးသည်ကို သိရတော့မည်ဟူသော စွမ်းရည်",
    "aññāta": "သိသော",                                             # fragment of anaññāta (rule 8)
    "aññindriyaṃ": "အပြည့်အဝ သိမြင်ခြင်း၏ စွမ်းရည်", "aññā": "အပြည့်အဝ သိမြင်ခြင်း",
    "sammā": "မှန်ကန်သော", "diṭṭhi": "အယူ", "vāyāmo": "အားထုတ်မှု", "saṅkappo": "ကြံစည်မှု",
    "vācā": "စကား", "ājīvo": "အသက်မွေးမှု",
    "saddhābalaṃ": "ယုံကြည်မှု၏ စွမ်းအား", "vīriyabalaṃ": "ဝီရိယ၏ စွမ်းအား", "satibalaṃ": "သတိ၏ စွမ်းအား",
    "samādhibalaṃ": "သမာဓိ၏ စွမ်းအား", "paññābalaṃ": "ပညာ၏ စွမ်းအား",
    "hiri": "ဒုစရိုက်ကို ရှက်မှု", "ottappa": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု", "ottappaṃ": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု",
    "hiribalaṃ": "ဒုစရိုက်ကို ရှက်မှု၏ စွမ်းအား", "ottappabalaṃ": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု၏ စွမ်းအား",
    "alobho": "လောဘ မရှိခြင်း", "adoso": "ဒေါသ မရှိခြင်း", "amoho": "မောဟ မရှိခြင်း",
    "anabhijjhā": "သူ့ဥစ္စာကို မလိုချင်ခြင်း", "abyāpādo": "ဖျက်ဆီးလိုစိတ် မရှိခြင်း",
    "kāya": "@kaya",
    "passaddhi": "ငြိမ်းအေးခြင်း", "lahutā": "ပေါ့ပါးခြင်း", "mudutā": "ပျော့ပျောင်းခြင်း",
    "kammaññatā": "အသုံးပြုရန် သင့်တော်ခြင်း", "pāguññatā": "ကျင့်သားရခြင်း", "ujukatā": "ဖြောင့်တန်းခြင်း",
    "cittapassaddhi": "စိတ် ငြိမ်းအေးခြင်း", "cittalahutā": "စိတ် ပေါ့ပါးခြင်း",
    "cittamudutā": "စိတ် ပျော့ပျောင်းခြင်း", "cittakammaññatā": "စိတ် အသုံးပြုရန် သင့်တော်ခြင်း",
    "cittapāguññatā": "စိတ် ကျင့်သားရခြင်း", "cittujukatā": "စိတ် ဖြောင့်တန်းခြင်း",
    "sati": "သတိ", "sampajaññaṃ": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း",
    "samatho": "စိတ်ငြိမ်သက်ခြင်း", "vipassanā": "ထိုးထွင်းသိမြင်ခြင်း",
    "paggāho": "စိတ်ကို မြှင့်တင်ခြင်း", "avikkhepo": "စိတ် မပျံ့လွင့်ခြင်း",
    "ye": "ရှိသမျှ",                                               # ye … atthi = «… ရှိသမျှ»
    "samuppannā": "ဖြစ်ပေါ်လာသော", "paṭicca": "အကြောင်းတို့ကို မှီ၍",   # paṭiccasamuppanna, not the doctrine
    "paṭiccasamuppannā": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော",
    "paṭiccasamuppannā arūpino": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော",
    "samuppannā arūpino": "ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော",
    "samuppannā arūpino dhammā": "ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော … သဘောတရား",
    "arūpino dhammā": "ရုပ် မဟုတ်သော … သဘောတရား",                   # «… အခြား သဘောတရားများ»
    "dhammā kusalā": "ကုသိုလ် သဘောတရား",
    # --- the summary (Tasmiṃ kho pana samaye …)
    "khandhā": "အစုအဝေး", "khandho": "အစုအဝေး", "khandhassa": "အစုအဝေး",
    "dhātu": "ဓာတ်", "dhātuyo": "ဓာတ်", "āhārā": "အာဟာရ", "balāni": "စွမ်းအား",
    "tivaṅgikaṃ": "အင်္ဂါ သုံးပါး ရှိသော", "duvaṅgikaṃ": "အင်္ဂါ နှစ်ပါး ရှိသော",
    "duvaṅgikaṃ jhānaṃ": "အင်္ဂါ နှစ်ပါး ရှိသော ဈာန်",
    "caturaṅgiko": "အင်္ဂါ လေးပါး ရှိသော", "caturaṅgikaṃ": "အင်္ဂါ လေးပါး ရှိသော",
    "caturaṅgiko maggo": "အင်္ဂါ လေးပါး ရှိသော မဂ်",
    "pañcaṅgikaṃ": "အင်္ဂါ ငါးပါး ရှိသော", "aṭṭhaṅgiko": "အင်္ဂါ ရှစ်ပါး ရှိသော",
    "dhamma": DH, "dhammāyatanaṃ": "သဘောတရား အာရုံခံ နယ်ပယ်", "dhammadhātu": "သဘောတရား ဓာတ်",
    "manāyatanaṃ": "မနော အာရုံခံ နယ်ပယ်", "manoviññāṇa": "မနော သိစိတ်",
    "manoviññāṇadhātu": "မနော သိစိတ် ဓာတ်", "viññāṇa": "သိစိတ်", "saṅkhāra": "ပြုပြင်ဖန်တီးမှု",
    "vedanākkhandho": "ခံစားမှု အစုအဝေး", "saññākkhandho": "မှတ်သိမှု အစုအဝေး",
    "saṅkhārakkhandho": "ပြုပြင်ဖန်တီးမှု အစုအဝေး", "viññāṇakkhandho": "သိစိတ် အစုအဝေး",
    "vedanākkhandhaṃ": "ခံစားမှု အစုအဝေး", "saññākkhandhaṃ": "မှတ်သိမှု အစုအဝေး",
    "viññāṇakkhandhaṃ": "သိစိတ် အစုအဝေး",
    "vedanākkhandhassa": "ခံစားမှု အစုအဝေး", "saññākkhandhassa": "မှတ်သိမှု အစုအဝေး",
    "saṅkhārakkhandhassa": "ပြုပြင်ဖန်တီးမှု အစုအဝေး", "viññāṇakkhandhassa": "သိစိတ် အစုအဝေး",
    "ṭhapetvā": "ချန်ထား၍",
    # --- the definitions (synonym lists)
    "yā": NONE, "yo": NONE, "yaṃ": NONE,                            # relative pronoun: no Burmese word
    "samaye": "အချိန်",
    "samaye phasso": "အချိန်၌ ရှိသော တွေ့ထိမှု", "samaye cittaṃ": "အချိန်၌ ရှိသော စိတ်",
    "samaye takko": "အချိန်၌ ရှိသော တွေးတောခြင်း", "samaye cāro": "အချိန်၌ ရှိသော သုံးသပ်ခြင်း",
    "samaye cetasikaṃ": "အချိန်၌ ရှိသော စိတ်ပိုင်းဆိုင်ရာ", "samaye saddhā": "အချိန်၌ ရှိသော ယုံကြည်မှု",
    "samaye sati": "အချိန်၌ ရှိသော သတိ", "samaye paññā": "အချိန်၌ ရှိသော ပညာ",
    "samaye alobho": "အချိန်၌ ရှိသော လောဘ မရှိခြင်း", "samaye adoso": "အချိန်၌ ရှိသော ဒေါသ မရှိခြင်း",
    "samaye micchāājīvā ārati": "အချိန်၌ ရှိသော မှားယွင်းသော အသက်မွေးမှုမှ ရှောင်ခြင်း",
    "phusanā": "ထိခြင်း", "saṃphusanā": "တွေ့ထိခြင်း",
    "tajjā": "သက်ဆိုင်ရာ", "samphassajā": "တွေ့ထိမှုမှ ဖြစ်ပေါ်သော", "samphassajaṃ": "တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "cetosamphassajaṃ": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော", "cetosamphassajā": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "cetasikaṃ": "စိတ်ပိုင်းဆိုင်ရာ", "sātaṃ": "နှစ်သက်ဖွယ်ကောင်းမှု",
    "cetasikaṃ sātaṃ": "စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ်ကောင်းမှု", "cetasikaṃ sukhaṃ": "စိတ်ပိုင်းဆိုင်ရာ သာယာမှု",
    "vedayitaṃ": "ခံစားရခြင်း", "sukhaṃ vedayitaṃ": "သာယာသော ခံစားရခြင်း",
    "sukhā": "သာယာသော", "sukhā vedanā": "သာယာသော ခံစားမှု",
    "sañjānanā": "မှတ်သိခြင်း", "sañjānitattaṃ": "မှတ်သိထားသော အဖြစ်",
    "sañcetanā": "စေ့ဆော်ခြင်း", "cetayitattaṃ": "စေ့ဆော်ထားသော အဖြစ်",
    "mano": "မနော", "mānasaṃ": "စိတ်နှလုံး", "hadayaṃ": "နှလုံးသား", "paṇḍaraṃ": "ကြည်လင်သောအရာ",
    "viññāṇaṃ": "သိစိတ်",
    "takko": "တွေးတောခြင်း", "appanā": "အာရုံ၌ စိတ်ကို သွင်းခြင်း", "abhiniropanā": "အာရုံသို့ တင်ပို့ခြင်း",
    "maggaṅgaṃ": "မဂ်၏ အင်္ဂါ", "aṅgaṃ": "အင်္ဂါ", "magga": "မဂ်",
    "cāro": "သုံးသပ်ခြင်း", "anusandhānatā": "အာရုံနှင့် ဆက်စပ်ထားခြင်း",
    "anupekkhanatā": "အာရုံကို စေ့စေ့ ရှုကြည့်ခြင်း",
    "pāmojjaṃ": "ရွှင်လန်းခြင်း", "āmodanā": "ဝမ်းသာခြင်း", "pamodanā": "အလွန် ဝမ်းသာခြင်း",
    "hāso": "ပြုံးရွှင်ခြင်း", "pahāso": "အလွန် ပြုံးရွှင်ခြင်း", "vitti": "ကျေနပ်ခြင်း",
    "odagyaṃ": "စိတ်တက်ကြွခြင်း", "attamanatā": "နှစ်သိမ့်ခြင်း",
    "sambojjhaṅgo": "ဗောဇ္ဈင်", "samādhisambojjhaṅgo": "သမာဓိ ဗောဇ္ဈင်", "vīriyasambojjhaṅgo": "ဝီရိယ ဗောဇ္ဈင်",
    "vicayasambojjhaṅgo": "စိစစ်ခြင်း ဗောဇ္ဈင်",                       # fragment of dhammavicayasambojjhaṅgo
    "ṭhiti": "တည်တံ့ခြင်း", "cittassa ṭhiti": "စိတ်၏ တည်တံ့ခြင်း", "saṇṭhiti": "ကောင်းစွာ တည်တံ့ခြင်း",
    "avaṭṭhiti": "ခိုင်မြဲစွာ တည်တံ့ခြင်း", "avisāhāro": "မပြန့်ကျဲခြင်း",
    "avisāhaṭa": "မပြန့်ကျဲသော", "mānasatā": "စိတ် … အဖြစ်", "avisāhaṭamānasatā": "စိတ် မပြန့်ကျဲသော အဖြစ်",
    "saddahanā": "ယုံကြည်ခြင်း", "okappanā": "စိတ်ချ အားကိုးခြင်း", "abhippasādo": "ကြည်ညိုလေးစားခြင်း",
    "cetasiko": "စိတ်ပိုင်းဆိုင်ရာ", "ārambho": "စတင်ခြင်း",
    "cetasiko vīriyārambho": "စိတ်ပိုင်းဆိုင်ရာ ဝီရိယ စတင်ခြင်း",
    "nikkamo": "ရှေ့သို့ တိုးထွက်ခြင်း", "parakkamo": "ရဲရင့်စွာ ကြိုးစားခြင်း", "uyyāmo": "ထကြွ ကြိုးစားခြင်း",
    "ussāho": "စိတ်အားထက်သန်မှု", "ussoḷhī": "ပြင်းပြသော အားမာန်", "thāmo": "ခွန်အား", "dhiti": "ဇွဲ",
    "asithila": "မလျော့ရဲသော", "nikkhitta": "လက်လွှတ်သော / ချထားသော",   # anikkhitta-chandatā / -dhuratā: two verbs (as 2-01)
    "chandatā": "ဆန္ဒ", "dhuratā": "ဝန်", "sampaggāho": "ခိုင်မြဲစွာ ထမ်းဆောင်ခြင်း",
    "anussati": "အဖန်ဖန် အောက်မေ့ခြင်း", "paṭissati": "ပြန်လည် အောက်မေ့ခြင်း", "saraṇatā": "မှတ်မိခြင်း",
    "dhāraṇatā": "စွဲမှတ်ထားခြင်း", "pilāpanatā": "အပေါ်ယံ ပေါ်လောခြင်း", "sammussanatā": "မေ့လျော့ခြင်း",
    "paññā": "ပညာ", "pajānanā": "ကွဲပြားစွာ သိခြင်း", "vicayo": "စိစစ်ခြင်း", "pavicayo": "သေချာစွာ စိစစ်ခြင်း",
    "dhammavicayo": "သဘောတရားများကို စိစစ်ခြင်း",                       # «သဘောတရားများကို» inside the term (rule 1)
    "sallakkhaṇā": "လက္ခဏာကို ကောင်းစွာ ခွဲခြားခြင်း", "upalakkhaṇā": "လက္ခဏာကို အနီးကပ် ခွဲခြားခြင်း",
    "paccupalakkhaṇā": "လက္ခဏာကို အသီးသီး ခွဲခြားခြင်း", "paṇḍiccaṃ": "လိမ္မာခြင်း", "kosallaṃ": "ကျွမ်းကျင်ခြင်း",
    "nepuññaṃ": "နက်နဲသိမ်မွေ့ခြင်း", "vebhabyā": "ခွဲခြမ်းစိတ်ဖြာခြင်း", "cintā": "စဉ်းစားခြင်း",
    "upaparikkhā": "စူးစမ်းဆန်းစစ်ခြင်း", "bhūrī": "ကျယ်ပြန့်ခြင်း", "medhā": "ဉာဏ်ထက်မြက်ခြင်း",
    "pariṇāyikā": "လမ်းပြခြင်း", "patodo": "နှင်တံ",
    "satthaṃ": "ဓား", "paññāsatthaṃ": "ပညာ ဓား", "pāsādo": "ပြာသာဒ်", "paññāpāsādo": "ပညာ ပြာသာဒ်",
    "āloko": "အလင်း", "paññāāloko": "ပညာ အလင်း", "obhāso": "အရောင်အဝါ", "paññāobhāso": "ပညာ အရောင်အဝါ",
    "pajjoto": "မီးအိမ်", "paññāpajjoto": "ပညာ မီးအိမ်", "ratanaṃ": "ရတနာ", "paññāratanaṃ": "ပညာ ရတနာ",
    "viditānaṃ": "တွေ့ရှိသော", "sacchikatānaṃ": "မျက်မှောက် ပြုသော", "ñātānaṃ": "သိသော",
    "sacchikiriyāya": "မျက်မှောက်ပြုရန်",
    "āyu": "သက်တမ်း", "yapanā": "ဆက်လက် ဖြစ်နေခြင်း", "yāpanā": "ဆက်လက် ရှင်သန်စေခြင်း",
    "iriyanā": "လှုပ်ရှားခြင်း", "vattanā": "လည်ပတ်ခြင်း", "pālanā": "စောင့်ရှောက်ခြင်း",
    "arūpīnaṃ": "ရုပ် မဟုတ်သော", "arūpīnaṃ dhammānaṃ": "ရုပ် မဟုတ်သော သဘောတရား",
    "vacī": "နှုတ်", "duccaritehi": "ဒုစရိုက်", "micchā": "မှားယွင်းသော",
    "ārati": "ရှောင်ခြင်း", "virati": "ရှောင်ကြဉ်ခြင်း", "paṭivirati": "ပြန်လှည့် ရှောင်ကြဉ်ခြင်း",
    "veramaṇī": "ကင်းဝေးခြင်း", "kiriyā": "ပြုခြင်း", "karaṇaṃ": "ပြုလုပ်ခြင်း", "ajjhāpatti": "ကျူးလွန်ခြင်း",
    "velā": "နယ်နိမိတ်", "atikkamo": "ကျော်လွန်ခြင်း", "setu": "တံတား", "ghāto": "ဖြိုဖျက်ခြင်း",
    "hirīyati": "ရှက်သည်", "ottappati": "ကြောက်ရွံ့သည်", "pāpakānaṃ": "ယုတ်မာသော",
    "akusalānaṃ": "အကုသိုလ်", "akusalānaṃ dhammānaṃ": "အကုသိုလ် သဘောတရား", "samāpattiyā": "ကျူးလွန်ခြင်း",
    "mūlaṃ": "အမြစ်", "kusalamūlaṃ": "ကုသိုလ်၏ အမြစ်",
    "lubbhanā": "မက်မောခြင်း", "sārajjanā": "စွဲမက်ခြင်း", "asārāgo": "မတပ်မက်ခြင်း",
    "dussanā": "စိတ်ဆိုးခြင်း", "abyāpajjo": "မညှဉ်းဆဲလိုခြင်း", "byāpajjo": "ညှဉ်းဆဲလိုခြင်း",
    "passambhanā": "အေးချမ်းခြင်း", "passambhitattaṃ": "အေးချမ်းသွားသော အဖြစ်",
    "paṭipassambhitattaṃ": "လုံးဝ အေးချမ်းသွားသော အဖြစ်",
    "lahu": "လျင်မြန်စွာ", "adandhanatā": "မနှေးကွေးခြင်း", "dandhanatā": "နှေးကွေးခြင်း",
    "vitthanatā": "တုံ့ဆိုင်းခြင်း",
    "maddavatā": "နူးညံ့သော အဖြစ်", "akakkhaḷatā": "မကြမ်းတမ်းခြင်း", "kakkhaḷatā": "ကြမ်းတမ်းခြင်း",
    "kathinatā": "မာကျောခြင်း",
    "kammaññattaṃ": "အသုံးပြုရန် သင့်တော်သော အဖြစ်", "bhāvo": "သဘော", "paguṇattaṃ": "ကျင့်သားရသော အဖြစ်",
    "ujutā": "ဖြောင့်ခြင်း", "ajimhatā": "မကောက်ကွေးခြင်း", "jimhatā": "ကောက်ကွေးခြင်း",
    "vaṅkatā": "ကွေးညွှတ်ခြင်း", "kuṭilatā": "လိမ်ကောက်ခြင်း",
}
# «lokuttaraṃ X» / «lokuttaraṃ X bhāveti» (^1-357 and the openings): the object as the text builds it
_LOKX = {"jhānaṃ": "ဈာန်", "maggaṃ": "မဂ်", "satipaṭṭhānaṃ": "သတိပဋ္ဌာန်", "iddhipādaṃ": "ဣဒ္ဓိပါဒ်",
         "indriyaṃ": "စွမ်းရည်", "balaṃ": "စွမ်းအား", "bojjhaṅgaṃ": "ဗောဇ္ဈင်", "saccaṃ": "သစ္စာ",
         "samathaṃ": "စိတ်ငြိမ်သက်ခြင်း", "dhammaṃ": DH, "khandhaṃ": "အစုအဝေး", "āyatanaṃ": "အာရုံခံ နယ်ပယ်",
         "dhātuṃ": "ဓာတ်", "āhāraṃ": "အာဟာရ", "phassaṃ": "တွေ့ထိမှု", "vedanaṃ": "ခံစားမှု",
         "saññaṃ": "မှတ်သိမှု", "cetanaṃ": "စေ့ဆော်မှု", "cittaṃ": "စိတ်"}
for _x, _m in _LOKX.items():
    T_CU2[f"lokuttaraṃ {_x}"] = f"{T_CU2['lokuttaraṃ']} {_m}"
    T_CU2[f"lokuttaraṃ {_x} bhāveti"] = f"{T_CU2['lokuttaraṃ']} {_m}ကို ပွားများသည်"


def f_rupa2(kw, pali, my):
    """2-02 / 2-03: rūpa of rūpūpapatti / rūpāvacara / rūparāga = the fine-material plane «သိမ်မွေ့သော ရုပ်»
    (as the sample's f_rupa, also for the capitalised heading «Rūpāvacara…»); in the immaterial openings
    («arūpūpapattiyā … rūpasaññānaṃ») = matter «ရုပ်» (rūpasaññā = «ရုပ်ဟု မှတ်သိမှု»)."""
    if "arūpūpapatti" in pali:
        return "ရုပ်"
    if re.search(r"(?<![aA])(?:[rR]ūpāvacar|rūpūpapatti|rūparāga)", pali):
        return "သိမ်မွေ့သော ရုပ်"
    return "ရုပ်"


def f_sukha(kw, pali, my):
    """sukha- of sukhapaṭipadā = easy «လွယ်ကူသော» (rule 11); elsewhere pleasant feeling «သာယာမှု»."""
    return "လွယ်ကူသော" if "sukhapaṭipad" in pali else "သာယာမှု"


def f_dukkha(kw, pali, my):
    """dukkha- of dukkhapaṭipadā = difficult «ခက်ခဲသော» (rule 11); elsewhere painful feeling «နာကျင်မှု»."""
    return "ခက်ခဲသော" if "dukkhapaṭipad" in pali else "နာကျင်မှု"


def f_maggam(kw, pali, my):
    """maggaṃ of «rūpūpapattiyā maggaṃ» = the way «လမ်း»; «lokuttaraṃ maggaṃ» = the path «မဂ်» (rule 11)."""
    return "မဂ်" if "lokuttaraṃ maggaṃ" in pali else "လမ်း"


def f_ayatanani(kw, pali, my):
    """āyatanāni of abhibhāyatanāni (headings, colophon) = «နယ်ပယ်»; of dvāyatanāni = «အာရုံခံ နယ်ပယ်»."""
    if re.search(r"[aA]bhibhāyatanāni", pali) and "dvāyatanāni" not in pali:
        return "နယ်ပယ်"
    return "အာရုံခံ နယ်ပယ်"


def f_kaya(kw, pali, my):
    """kāya of kāyaduccarita = the body «ကိုယ်»; of kāyapassaddhi … = the mental body «စိတ်၏ အဖော်» (rule 11)."""
    return "ကိုယ်" if "kāyaduccarit" in pali else _KAYA


FUNCS = {"rupa": f_rupa, "rupa2": f_rupa2, "sukha": f_sukha, "dukkha": f_dukkha, "maggam": f_maggam,
         "ayatanani": f_ayatanani, "kaya": f_kaya}

CTX = {
    # sid: {keyword: value}
}

# chapter -> its own table (looked up first); every table is also shared with the other chapters
SECTIONS = {
    "preamble": T_PREAMBLE,
    "1-matika": T_MATIKA,
    "2-02-cittuppadakandam": T_CU2,
    "2-03-cittuppadakandam": T_CU2,
}
CHAPTERS = ["2-02-cittuppadakandam", "2-03-cittuppadakandam"]

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

RULES_NEW = """## New rules for 2-02 / 2-03 (proposed for review; rules 1-11 of map-table.md apply unchanged)

Kept from the sample: every keyword the sample already has keeps its value in the same kind of segment (kusalā =
ကုသိုလ်, arūpino = ရုပ် မဟုတ်သော, hetū = အမြစ်, pīti = ပီတိ, upekkhā = ဥပေက္ခာ, apacaya = လျော့ပါးခြင်း, paritta =
အကန့်အသတ် ရှိသော, appamāṇa = အတိုင်းအဆ မရှိသော …). Factor names and synonym items are the forms of THESE chapters'
Burmese (the 2-01 tables of my_formulas.py were used only to locate them).

12. **Attributives from «…လျက်» and «…ဘဲ»** are normalised to «…သော» like the endings of rule 3: sampajāno (text
    «ကောင်းစွာ ဆင်ခြင်သိမြင်လျက်») = ကောင်းစွာ ဆင်ခြင်သိမြင်သော; upekkhako («ဥပေက္ခာ ရှိလျက်») = ဥပေက္ခာ ရှိသော;
    sato = သတိ ရှိသော; asithila («မလျော့ရဲဘဲ») = မလျော့ရဲသော; saññī / rūpasaññī (fragments of arūpasaññī, text
    «ရုပ်ဟု မမှတ်သိဘဲ») = မှတ်သိသော / ရုပ်ဟု မှတ်သိသော.
13. **Finite verbs** (rule 4, verb + «သည်») also from the conjunctive «…၍», the plural «…ကြသော» and the verbal
    noun «…ခြင်း»: bhāveti («ပွားများ၍») = ပွားများသည်; viharati = နေသည်; paṭisaṃvedeti («ခံစား၍») = ခံစားသည်;
    ācikkhanti («ပြောကြားကြသော») = ပြောကြားသည် (the plural agreement ကြ goes, as the noun plural markers of rule 1);
    hirīyati / ottappati («ရှက်ခြင်း» / «ကြောက်ရွံ့ခြင်း») = ရှက်သည် / ကြောက်ရွံ့သည်; jānāmi / passāmīti («သိ၏၊
    မြင်၏ဟု») = သိသည် / မြင်သည် (quotative ဟု dropped, rule 4); subhanti («တင့်တယ်၏ဟု») = တင့်တယ်သည်. A verb phrase
    keeps its inner ၍: upasampajja viharati = ဝင်စား၍ နေသည်; maggaṃ bhāveti = လမ်းကို ပွားများသည်.
    **Absolutives** (indeclinable gerunds) are not finite verbs: they keep the text's conjunctive «…၍», as the
    parallel mappings of 2-01 (its rule 14) and 2-04 / 2-05 (its rule 12) decided, because 2-04 / 2-05 repeat these
    openings word for word: upasampajja = ဝင်စား၍; vivicca = ကင်းဆိတ်၍ (vivicceva = ကင်းဆိတ်၍သာ, eva = သာ);
    samatikkamma = ကျော်လွန်၍; ṭhapetvā = ချန်ထား၍; abhibhuyya = လွှမ်းမိုး၍; paṭicca = အကြောင်းတို့ကို မှီ၍ (with
    the object by which the text renders «depending [on conditions]»).
14. **Fragments that lost a negative prefix** (rule 8) also where the text's negative is the leading «မ» of a verb or
    sits inside a verbal noun: aññāta (anaññāta «မသိရသေး») = သိသော; viditānaṃ (avidita «မတွေ့ရှိရသေး», ^1-364
    «တွေ့ရှိပြီး») = တွေ့ရှိသော; sacchikatānaṃ = မျက်မှောက် ပြုသော; nikkhitta (anikkhitta-chandatā / -dhuratā:
    «ဆန္ဒကို လက်မလွှတ်ခြင်း», «ဝန်ကို မချထားခြင်း») = လက်လွှတ်သော / ချထားသော (two compounds, two Burmese verbs:
    genuine alternatives, as 2-01); lubbhanā
    («မမက်မောခြင်း») = မက်မောခြင်း; sārajjanā = စွဲမက်ခြင်း; dussanā («စိတ်မဆိုးခြင်း») = စိတ်ဆိုးခြင်း; byāpajjo =
    ညှဉ်းဆဲလိုခြင်း; pilāpanatā («အပေါ်ယံ မပေါ်လောခြင်း») = အပေါ်ယံ ပေါ်လောခြင်း; sammussanatā = မေ့လျော့ခြင်း;
    kiriyā = ပြုခြင်း; karaṇaṃ = ပြုလုပ်ခြင်း; ajjhāpatti = ကျူးလွန်ခြင်း; atikkamo = ကျော်လွန်ခြင်း; dandhanatā,
    vitthanatā, kakkhaḷatā, kathinatā, jimhatā, vaṅkatā, kuṭilatā likewise; manasikārā («နှလုံး မသွင်းခြင်း») =
    နှလုံး သွင်းခြင်း (spelt with the text's space); avasesa (anavasesa «အကြွင်းအကျန် မရှိအောင်») = အကြွင်းအကျန်;
    passambhitattaṃ (inside paṭipassambhitattaṃ) = အေးချမ်းသွားသော အဖြစ်; vicayasambojjhaṅgo (inside
    dhammavicayasambojjhaṅgo) = စိစစ်ခြင်း ဗောဇ္ဈင်. The privative keywords that keep their a- keep the text's «မ»
    (asithila, avisāhaṭa, adandhanatā …). ajjhattaṃ arūpa (= the arūpa- of arūpasaññī) = မိမိ၌ ရုပ်ဟု မမှတ်သိသော:
    the text puts the a- into the verb of -saññī, so the negative and «မှတ်သိ» cannot be separated.
15. **The causal ending «…ကြောင့်»** (the Pāli ablative -ā: vūpasamā, virāgā, pahānā, atthaṅgamā, samatikkamā,
    amanasikārā) is a postposition like those of rule 1 and is dropped: vūpasamā = ငြိမ်းသွားခြင်း; sukhassa ca
    pahānā = သာယာမှုကိုလည်း ပယ်ခြင်း (ca = the text's လည်း inside the phrase, as in rule 6).
16. **Frame words**: Yā / Yo / Yaṃ opening a synonym list have no Burmese word = (no direct equivalent); ye (ye vā
    pana … atthi) = ရှိသမျှ (the text's relative-indefinite); «samaye X» = «အချိန်၌ ရှိသော X» (the text's «ထိုအချိန်၌
    ရှိသော X»; tasmiṃ's ထို is not in the keyword); samaye alone = အချိန်; eva = သာ; caya (fragment of apacaya) =
    (no direct equivalent): the text renders apacaya by one word «လျော့ပါးခြင်း» (decrease) and has no word for
    «accumulation».
17. **Sense by context** (rule 11 extended; context functions in map_2-02-03.py): rūpa = သိမ်မွေ့သော ရုပ် in
    rūpūpapatti / the Rūpāvacara headings / rūparāga, ရုပ် in the immaterial openings (rūpasaññā «ရုပ်ဟု မှတ်သိမှု»);
    maggaṃ = လမ်း in «rūpūpapattiyā maggaṃ» (the way to rebirth), မဂ် in «lokuttaraṃ maggaṃ»; sukha / dukkha =
    လွယ်ကူသော / ခက်ခဲသော in sukha- / dukkhapaṭipadā, otherwise the feeling သာယာမှု / နာကျင်မှု; āyatanāni =
    နယ်ပယ် in abhibhāyatanāni, အာရုံခံ နယ်ပယ် in dvāyatanāni; kāya = စိတ်၏ အဖော်တို့ in kāyapassaddhi … and kāyena
    (harmonise-notes item 10; kept whole with its တို့, which keeps it apart from cetasika «စိတ်၏ အဖော်», as 2-01's
    rule 18: the one exception to the dropped plural marker), ကိုယ် in kāyaduccarita; bahiddhā = ပြင်ပ၌ (outside:
    the forms of the bases of mastery, harmonise-notes item 9), not the Mātikā's သူတစ်ပါး၌; sammā = မှန်ကန်သော
    (right: sammādiṭṭhi …), not the preamble's အပြည့်အဝ (sammāsambuddha); paṭicca = အကြောင်းတို့ကို မှီ၍ (of
    paṭiccasamuppannā dhammā, rule 13), not the Mātikā's paṭiccasamuppāda «အကြောင်းအကျိုး ဆက်စပ်».
18. **Discontinuous values** where the text puts a word between the parts (rule 10): paṭipadaṃ dandha / khippa =
    ကျင့်စဉ် … နှေးကွေးသော / လျင်မြန်သော; (samuppannā) arūpino dhammā = (ဖြစ်ပေါ်လာသော) ရုပ် မဟုတ်သော … သဘောတရား
    (text «… အခြား သဘောတရားများ»: aññe = အခြား is not in the keyword); ānañcāyatana(ṃ) = အဆုံး မရှိသော … နယ်ပယ်
    (ākāsa = ကောင်းကင် between); bhūmaka (Tebhūmaka) = ဘုံ … နှင့် ဆိုင်သော; mānasatā = စိတ် … အဖြစ်. Comma series
    lose their «၊» (rule 6): niyyānikaṃ apacayagāmiṃ = လွတ်မြောက်ရာသို့ ပို့ဆောင်သော လျော့ပါးခြင်းဆီသို့ ဦးတည်သော.
19. **Loanwords** that one Pāli fragment cannot split: the fragment = the part of the loan that renders it:
    paṭṭhānaṃ = ပဋ္ဌာန် (သတိပဋ္ဌာန်), iddhi = ဣဒ္ဓိ (ဣဒ္ဓိပါဒ်); brahma and vihāra both = ဗြဟ္မစိုရ် (one word for
    brahmavihāra, no Burmese part for either alone).
20. **Headings with counts**: Catukka / Pañcaka = ဈာန် လေးပါး / ဈာန် ငါးပါး (the text names the jhāna with its count);
    soḷasakkhattuka- = တစ်ဆယ့်ခြောက်ကြိမ် နည်း and aṭṭhakkhattuka- = ရှစ်ကြိမ် နည်း (the text's head နည်း kept: the
    -ka noun is «the sixteenfold [method]»); nayo / nayā (Catukkanayo, mahānayā) = နည်း. Titles keep the attributive
    form: Suññataṃ = ဆိတ်သုဉ်းသော, Appaṇihitaṃ = တောင့်တမှု မရှိသော (the heading adds ဈာန်); Suññata- /
    Appaṇihita- of the mūlaka titles = the text's verbal nouns ဆိတ်သုဉ်းခြင်း / တောင့်တမှု မရှိခြင်း; mūlaka =
    အခြေခံသော (text «…ကို အခြေခံသော», rule 3).
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
    # ---- rules 12-14 (2-02 / 2-03, map-table-2-02-03.md)
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in ATTR_FROM_NEW):
            return "attr-new"
    if c.endswith("သည်") and len(c) > 3:
        st = c[:-3]
        if any(st + e in text for e in VERB_FROM_NEW):
            return "verb-new"
    if c[-3:] in ("သော", "သည်") and len(c) > 3 and "မ" + c[:-3] in text:
        return "neg-prefix"
    if c.endswith("သော") and len(c) > 3:          # rule 14: infixed မ inside an attributive stem + a rule-3 ending
        st = c[:-3]
        for i in range(1, len(st)):
            if any(st[:i] + "မ" + st[i:] + e in text for e in ATTR_FROM):
                return "neg-infix-attr"
    return None


ATTR_FROM_NEW = ("လျက်", "ဘဲ")              # rule 12: «Xသော» <- text «Xလျက်» (while X) / «Xဘဲ» (without X-ing)
VERB_FROM_NEW = ("၍", "ကြသော", "ကြသည်", "ခြင်း")   # rule 13: «Xသည်» <- text «X၍» / «Xကြသော» / «Xခြင်း»


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


def write_table(table, ruled_all, results):
    with open(HERE / "map-table-2-02-03.md", "w", encoding="utf-8") as f:
        f.write("# pi-1 Burmese keyword mapping: chapters 2-02 and 2-03 (new rules and review table)\n\n")
        f.write("Written by map_2-02-03.py. Burmese from the FINAL text of this track only "
                "(AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters). The approved rules 1-11 of "
                "map-table.md and the sample values (preamble, 1-matika) apply unchanged; below are only the NEW "
                "rules these chapters need, then the presence exceptions and the full keyword table.\n\n")
        f.write("Verification: " + "; ".join(
            f"{ch}: lines {ln}, keyword preservation bad {bad}, presence failures {len(fails)}, comma/၊ {punct}, "
            f"(no direct equivalent) {nne}" for ch, ln, bad, fails, punct, ruled, nne in results) + ".\n\n")
        f.write(RULES_NEW)
        f.write("\n## Presence: chunks matched by a dictionary-form rule (not literally in the segment)\n\n")
        f.write("Every other chunk of every value occurs literally in its segment's Burmese. Rule names: attr / verb "
                "/ neg-infix = approved rules 3 / 4 / 8; attr-new = rule 12, verb-new = rule 13, neg-prefix and neg-infix-attr = rule "
                "14.\n\n| keyword | chunk | rule | uses | first segment |\n|---|---|---|---|---|\n")
        agg = collections.OrderedDict()
        for sid, k, c, r in ruled_all:
            agg.setdefault((k, c, r), [0, sid])[0] += 1
        for (k, c, r), (n, sid) in agg.items():
            f.write(f"| {k} | {c} | {r} | {n} | {sid} |\n")
        f.write("\n## Keyword → Burmese (number of uses)\n\nSeveral values = the keyword reads differently by "
                "context.\n\n| Pāli keyword | Burmese (uses) |\n|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            f.write(f"| {kw} | " + " / ".join(f"{v} ({n})" for v, n in table[kw].most_common()) + " |\n")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--show":       # --show N ID ID ...: Pāli and Burmese of segments, cut to N characters
        n = int(args[1])
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            for s, kws in rows:
                if s in args[2:]:
                    print("===", s, "\nPI:", pa.get(s, "")[:n], "\nMY:", my[s][:n], "\nKW:", kws[:n])
        sys.exit()
    if args and args[0] == "--src":        # keywords whose value comes from the sample tables (not T_CU2 / CTX)
        seen = collections.Counter()
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            for s, kws in rows:
                for kw in [k.strip() for k in kws.split(", ")]:
                    if table_get(T_CU2, kw) is None and table_get(CTX.get(s, {}), kw) is None:
                        seen[(kw, lookup(ch, s, kw, pa.get(s, ""), my[s]))] += 1
        for (kw, v), n in sorted(seen.items()):
            print(f"{kw} = {v} ({n})")
        sys.exit()
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
    write_table(table, ruled_all, results)
    for ch, ln, bad, fails, punct, ruled, nne in results:
        print(f"{ch}: lines {ln} | keyword preservation bad {bad} | presence failures {len(fails)} "
              f"(rule-matched chunks {len(ruled)}) | comma/၊ {punct} | no-equivalent {nne}")
        for f_ in fails:
            print("   FAIL", f_)
    for (k, c, r), n in collections.Counter((k, c, r) for _, k, c, r in ruled_all).items():
        print(f"   rule {r:9} {n:4}  {k} : {c}")
    print("total no direct equivalent:", tot_nne, "| distinct keywords:", len(table))
