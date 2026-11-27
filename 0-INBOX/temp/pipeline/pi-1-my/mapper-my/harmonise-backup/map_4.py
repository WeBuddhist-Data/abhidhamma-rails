"""Pāli→Burmese keyword mapping for pi-1 chapters 4-01, 4-02, 4-03 (Nikkhepakaṇḍa «အကျဉ်း ဖော်ပြချက် အခန်း»).

A copy of the approved sample mapper map_all.py (its tables T_PREAMBLE / T_MATIKA, compose rules, context function
and verifier copied unchanged, not imported), with the Nikkhepa table T_4, more context functions, CTX overrides and
the new dictionary-form rules NEW_RULES (rules 12-22, written to map-table-4.md after the approved rules 1-11).

usage (python3 -I -X utf8, from any directory):
  map_4.py               writes 4-01/4-02/4-03 <ch>.mapped.md and map-table-4.md, then verifies them
                         (keyword preservation, presence of every value chunk in its segment, no ", " / «၊» in a value)
  map_4.py --report      writes nothing; lists unmapped keywords and presence failures
  map_4.py --seg ID      prints Pāli, Burmese, keywords and mapping of one segment
  map_4.py --new [N]     prints the first N segments that hold a keyword without a value (working aid)
  map_4.py --review IDs  prints the Burmese and the written mapping of the listed segments

Lookup order per keyword: CTX[sid] -> T_4 (own chapter table) -> the shared tables (sample first, so Mātikā items keep
the 1-matika values) -> compose: «vuccati X» = T[X] + «ဟု ခေါ်သည်»; «dhammā X» = «X dhammā»; «X dhammā» =
T[X] + « သဘောတရား»; «no / na X dhammā» = negative attributive + « သဘောတရား». A value «@name» is a context function
f(kw, pali, my); «@alt» takes the first variant in ALT that is present in the segment (variants of ONE sense only).
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


def f_rupa4(kw, pali, my):
    """rūpa in the Nikkhepa: the fine-material plane in rūpāvacara (as the sample); the visible object
    «အဆင်းအရောင်» in rūpāyatana / rūpadhātu / rūpārammaṇa (rule 11: by context); matter «ရုပ်» elsewhere."""
    if re.search(r"(?<![aA])[rR]ūpāvacar|rūpūpapatti|rūparāga", pali):
        return "သိမ်မွေ့သော ရုပ်"
    if re.search(r"[rR]ūpāyatan|rūpadhātu|[rR]ūpārammaṇ", pali) and "အဆင်းအရောင်" in my:
        return "အဆင်းအရောင်"
    return "ရုပ်"


def f_maggo(kw, pali, my):
    """maggo in «kummaggo» (the view list) = road «လမ်း»; the path elsewhere = «မဂ်»."""
    return "လမ်း" if "kummagg" in pali and "လမ်းမှား" in my else "မဂ်"


def f_dhamme(kw, pali, my):
    """dhamme: the Teaching in the doubt list («dhamme kaṅkhati» = «တရားတော်အပေါ်»); states elsewhere."""
    return "တရားတော်" if "dhamme kaṅkhati" in pali else DH


def f_bahiddha(kw, pali, my):
    """bahiddhā «in others» (the Mātikā sense, rule 11) / «outside» in «ito bahiddhā» (outside this dispensation)."""
    if "Ito bahiddhā" in pali or "ito bahiddhā" in pali:
        return "အပြင်ဘက်"
    return "သူတစ်ပါး၌"


def f_paticca(kw, pali, my):
    """paṭicca in «paṭiccasamuppannesu» (depending on conditions) = «အကြောင်းတို့ကို မှီသည်»; in
    paṭiccasamuppāda (the sample) = «အကြောင်းအကျိုး ဆက်စပ်»."""
    if "paṭiccasamuppann" in pali and "အကြောင်းတို့ကို မှီ" in my:
        return "အကြောင်းတို့ကို မှီသည်"
    return "အကြောင်းအကျိုး ဆက်စပ်"


def f_bhuta(kw, pali, my):
    """bhūtā: «ဖြစ်ပြီးသော» (has become) in the uppanna list; the fragment of mahābhūtā = «မူလဓာတ်»."""
    return "မူလဓာတ်" if "mahābhūt" in pali and "မူလဓာတ်" in my else "ဖြစ်ပြီးသော"


def f_samma(kw, pali, my):
    """sammā: «မှန်ကန်သော» in sammādiṭṭhi / sammāsaṅkappa … (the right path factors), «မှန်ကန်စွာ» in
    sammaggatā / sammāpaṭipannā, «ကောင်းစွာ» where the text renders it so; the sample's «အပြည့်အဝ»
    (sammāsambuddha) elsewhere."""
    if "sammāsambuddh" in pali:
        return "အပြည့်အဝ"
    if re.search(r"sammaggat|sammāpaṭipann", pali) and "မှန်ကန်စွာ" in my:
        return "မှန်ကန်စွာ"
    if "မှန်ကန်သော" in my:
        return "မှန်ကန်သော"
    return "အပြည့်အဝ"


def f_sukha(kw, pali, my):
    """sukha: the feeling «သာယာမှု» (sample); in diṭṭhadhammasukhavihāra the adverb «သာယာစွာ»."""
    return "သာယာစွာ" if "sukhavihār" in pali and "သာယာစွာ" in my else "သာယာမှု"


def f_namam(kw, pali, my):
    """nāmaṃ: the name «အမည်» in the adhivacana list; mentality «စိတ်ပိုင်း» in «katamaṃ nāmaṃ» (as the sample's nāmañca)."""
    return "စိတ်ပိုင်း" if "katamaṃ nāmaṃ" in pali else "အမည်"


def f_saddha(kw, pali, my):
    """saddhā: the fragment of assaddhā = the positive noun «ယုံကြည်မှု» (rule 8); the adjective «ယုံကြည်မှု ရှိသော»."""
    return "ယုံကြည်မှု" if "assaddhā" in pali else "ယုံကြည်မှု ရှိသော"


def f_paccaya(kw, pali, my):
    """paccayā: in the dependent-origination chain «X-paccayā» = «ကြောင့်» (because of); «hetū paccayā» = «အထောက်အပံ့»."""
    return "ကြောင့်" if "Avijjāpaccayā" in pali else "အထောက်အပံ့"


def f_samvaro(kw, pali, my):
    """saṃvaro: «စောင့်စည်းမှု» in sīlasaṃvaro; «စောင့်စည်းခြင်း» in the guarded-doors list."""
    return "စောင့်စည်းမှု" if "sīlasaṃvaro" in pali else "စောင့်စည်းခြင်း"


def f_rupam(kw, pali, my):
    """rūpaṃ: the visible object «အဆင်းအရောင်» in «cakkhunā rūpaṃ disvā» (rule 11); matter «ရုပ်» elsewhere."""
    return "အဆင်းအရောင်" if "cakkhunā rūpaṃ" in pali else "ရုပ်"


def f_kayassa(kw, pali, my):
    """kāyassa: the bodily body «ကိုယ်ခန္ဓာ» in «imassa kāyassa ṭhitiyā»; the mental body «စိတ်၏ အဖော်» in the
    middha definition (as harmonise item 10)."""
    return "ကိုယ်ခန္ဓာ" if "imassa kāyassa" in pali else "စိတ်၏ အဖော်"


# morphological variants of ONE sense: the first one present in the segment is taken (rule 13)
ALT = {
    "sineho": ["ချစ်ခင်ခြင်း", "ချစ်ခင်မှု"], "nandī": ["နှစ်သက်ခြင်း", "နှစ်သက်မှု"],
    "mucchā": ["မိန်းမောခြင်း", "မိန်းမောမှု"],
    "kamyatā": ["လိုချင်ခြင်း", "ထူလိုခြင်း", "လိုလားခြင်း"],
    "patho": ["လမ်းကြောင်း", "လမ်း"], "gāho": ["စွဲကိုင်ခြင်း", "ယူနိုင်ခြင်း"],
    "phalaṃ": ["ဖိုလ်", "အသီးအပွင့်"], "dhamma": [DH, "တရား"], "ñāṇaṃ": ["ဉာဏ်", "သိခြင်း"],
    "khandhā": ["အစုအဝေး", "အစု"], "sacca": ["အမှန်", "သစ္စာ"], "uppādāya": ["ဖြစ်ပေါ်ရန်", "ဖြစ်ပေါ်စေရန်"],
    "anussati": ["အဖန်ဖန် အောက်မေ့ခြင်း", "အောက်မေ့နိုင်သော"], "para": ["သူတစ်ပါး", "ပရ"],
    "ākāsa": ["ဟင်းလင်းပြင်", "ကောင်းကင်"],
    "akusalābyākatā": ["အကုသိုလ်နှင့် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
                       "အကုသိုလ် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော"],
}


def f_alt(kw, pali, my):
    cands = ALT[low(kw)]
    for c in cands:
        if presence(c, my)[0]:
            return c
    return cands[0]


def f_niyata(kw, pali, my):
    """niyatā: «ကျိန်းသေသော» (fixed, the Mātikā); in the ajjhatta list «ajjhattaṃ paccattaṃ niyatā» = «သီးသန့် ဖြစ်သော»
    (harmonise: kept)."""
    return "သီးသန့် ဖြစ်သော" if "paccattaṃ niyatā" in pali else "ကျိန်းသေသော"


def f_vibhava(kw, pali, my):
    """vibhava: the sample's «ဘဝ ပျောက်ကွယ်သည်» (the view); in vibhavataṇhā the text's «ဘဝ ပြတ်စဲခြင်း»."""
    return "ဘဝ ပြတ်စဲခြင်း" if "vibhavataṇh" in pali and "ဘဝ ပြတ်စဲခြင်း" in my else "ဘဝ ပျောက်ကွယ်သည်"


FUNCS = {"alt": f_alt, "niyata": f_niyata, "vibhava": f_vibhava, "samvaro": f_samvaro, "rupam": f_rupam, "kayassa": f_kayassa, "saddha": f_saddha, "paccaya": f_paccaya, "namam": f_namam, "samma": f_samma, "sukha": f_sukha, "bhuta": f_bhuta, "rupa": f_rupa, "rupa4": f_rupa4, "maggo": f_maggo, "dhamme": f_dhamme, "bahiddha": f_bahiddha,
         "paticca": f_paticca}

# =====================================================================================================
# Nikkhepakaṇḍa (4-01, 4-02, 4-03): new values (the Mātikā values above stay binding)
# =====================================================================================================
T_4 = {
    # --- headings
    "kaṇḍaṃ": "အခန်း", "nikkhepa": "အကျဉ်း ဖော်ပြချက်", "nikkhepaṃ": "အကျဉ်း ဖော်ပြချက်",
    # --- the aggregates, roots, kamma (the 4-0x answer lists)
    "khandho": "အစုအဝေး", "khandhā": "@alt", "khandha": "အစုအဝေး",
    "rūpakkhandho": "ရုပ် အစုအဝေး", "vedanākkhandho": "ခံစားမှု အစုအဝေး", "saññākkhandho": "မှတ်သိမှု အစုအဝေး",
    "saṅkhārakkhandho": "ပြုပြင်ဖန်တီးမှု အစုအဝေး", "viññāṇakkhandho": "သိစိတ် အစုအဝေး",
    "vedanā": "ခံစားမှု", "saññā": "မှတ်သိမှု", "saṅkhāra": "ပြုပြင်ဖန်တီးမှု", "viññāṇa": "သိစိတ်",
    "sampayutto": "ယှဉ်တွဲသော", "samuṭṭhānaṃ": "ဖြစ်ပေါ်လာသော",
    "kāya": "ကိုယ်", "vacī": "နှုတ်", "mano": "မနော",
    "kāyakammaṃ": "ကိုယ်ဖြင့် ပြုသော ကံ", "vacīkammaṃ": "နှုတ်ဖြင့် ပြုသော ကံ", "manokammaṃ": "မနောဖြင့် ပြုသော ကံ",
    "samuṭṭhānaṃ kāyakammaṃ": "ဖြစ်ပေါ်လာသော ကိုယ်ဖြင့် ပြုသော ကံ",
    "vacīkammaṃ manokammaṃ": "နှုတ်ဖြင့် ပြုသော ကံ မနောဖြင့် ပြုသော ကံ",     # «၊» dropped (rule 6)
    "mūlāni": "အမြစ်", "kusalamūlāni": "ကုသိုလ်၏ အမြစ်", "akusalamūlāni": "အကုသိုလ်၏ အမြစ်",
    "alobho": "လောဘ မရှိခြင်း", "adoso": "ဒေါသ မရှိခြင်း", "amoho": "မောဟ မရှိခြင်း",
    "lobho": "လောဘ", "doso": "ဒေါသ", "moho": "မောဟ",
    "ekaṭṭhā": "တစ်နေရာတည်း တည်ရှိသော", "ekaṭṭhā ca kilesā": "တစ်နေရာတည်း တည်ရှိသော ကိလေသာ",
    # --- abyākata frame
    "kusala": "ကုသိုလ်", "akusala": "အကုသိုလ်",
    "akusalānaṃ": "အကုသိုလ်", "akusalānaṃ dhammānaṃ": "အကုသိုလ် သဘောတရား",
    "kusalā nākusalā": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်",               # «၊» dropped (rule 6)
    "kiriyā": "ပြုရုံမျှသာ ဖြစ်သော", "kiriya": "ပြုရုံမျှသာ ဖြစ်သော",
    "dhātu": "ဓာတ်", "rūpaṃ": "@rupam",
    "asaṅkhatā ca dhātu": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော ဓာတ်",
    "kāmāvacare": "ကာမဘုံနှင့် ဆိုင်သော", "rūpāvacare": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော",
    "arūpāvacare": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော", "avacare": "ဘုံနှင့် ဆိုင်သော",
    "bhūmiyaṃ": "အဆင့်",
    "ṭhapetvā": "ချန်ထားသည်",                                                  # text «ချန်ထား၍» (rule 4, new rule 12)
    "kammassa katattā": "ကံကို ပြုခဲ့ခြင်းကြောင့်",
    "yañca": "ရှိသမျှ",
    "sāsavā kusalākusalā dhammā": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ်နှင့် အကုသိုလ် သဘောတရား",
    "maggā": "မဂ်", "phalāni": "ဖိုလ်",
    "apariyāpannā maggā": "ဘဝဘုံတို့၌ အကျုံးမဝင်သော မဂ်",
    "maggā apariyāpannā": "ဘဝဘုံတို့၌ အကျုံးမဝင်သော မဂ်",
    "bhāvanāya pahātabbahetukā": "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော",
    "dassanena pahātabbahetukā": "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော",
    "pahātabbahetukā": "ပယ်ရမည့် အမြစ် ရှိသော",
    "avasesā": "ကြွင်းကျန်သော", "avaseso": "ကြွင်းကျန်သော", "avasesā kusala": "ကြွင်းကျန်သော ကုသိုလ်",
    "akusalābyākatā": "@alt",
    "ācayagāmino": "စုပုံခြင်းဆီသို့ ဦးတည်သော", "apacayagāmino": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "caya": NONE,                                     # fragment of apacaya: the text has only «လျော့ပါးခြင်း»
    "dhammā neva ācayagāmi": "စုပုံခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ် … သဘောတရား",
    "sāmañña": "ရဟန်းအဖြစ်", "arahatta": "ရဟန္တာ", "phalaṃ": "@alt", "upariṭṭhimaṃ": "အမြင့်ဆုံး",
    "uppajjanti": "ဖြစ်ပေါ်သည်", "ārabbha": "အာရုံပြုသည်",
    "ārabbha ye uppajjanti": "အာရုံပြု၍ ဖြစ်ပေါ်သည်",
    "cittacetasikā": "စိတ်နှင့် စိတ်၏ အဖော်",
    "uppajjanti cittacetasikā": "ဖြစ်ပေါ်သော စိတ်နှင့် စိတ်၏ အဖော်",
    "paritte dhamme": "အကန့်အသတ် ရှိသော သဘောတရား",
    "paritte dhamme ārabbha": "အကန့်အသတ် ရှိသော သဘောတရားတို့ကို အာရုံပြုသည်",
    "mahaggate dhamme": "ကြီးမြတ်သော သဘောတရား",
    "mahaggate dhamme ārabbha": "ကြီးမြတ်သော သဘောတရားတို့ကို အာရုံပြုသည်",
    "appamāṇe dhamme": "အတိုင်းအဆ မရှိသော သဘောတရား",
    "appamāṇe dhamme ārabbha": "အတိုင်းအဆ မရှိသော သဘောတရားတို့ကို အာရုံပြုသည်",
    "atīte dhamme": "အတိတ် သဘောတရား", "atīte dhamme ārabbha": "အတိတ် သဘောတရားတို့ကို အာရုံပြုသည်",
    "anāgate dhamme": "အနာဂတ် သဘောတရား", "anāgate dhamme ārabbha": "အနာဂတ် သဘောတရားတို့ကို အာရုံပြုသည်",
    "paccuppanne dhamme": "ပစ္စုပ္ပန် သဘောတရား",
    "paccuppanne dhamme ārabbha": "ပစ္စုပ္ပန် သဘောတရားတို့ကို အာရုံပြုသည်",
    "kammāni": "ကံ", "kammassa": "ကံ", "ānantarikāni": "နောက်ဘဝ၌ ချက်ချင်း အကျိုးပေးသော",
    "micchādiṭṭhi": "မှားယွင်းသော အယူ",
    "micchattaniyatā": "မှားယွင်းမှု၌ ကျိန်းသေသော", "sammattaniyatā": "မှန်ကန်မှု၌ ကျိန်းသေသော",
    "ariya": "အရိယာ", "ariyamaggaṃ": "အရိယာ မဂ်", "ariyamagga": "အရိယာ မဂ်",
    "maggahetū": "မဂ်၏ အမြစ်", "aṅgāni": "အင်္ဂါ", "samaṅgissa": "ပြည့်စုံသော",
    "bhāvayantassa": "ပွားများနေသော", "maggaṃ bhāvayantassa": "မဂ်ကို ပွားများနေသော",
    "vīmaṃsā": "စုံစမ်းဆင်ခြင်မှု",
    "jātā": "မွေးဖွားပြီးသော", "sañjātā": "ကောင်းစွာ မွေးဖွားပြီးသော", "nibbattā": "ပေါ်ထွက်ပြီးသော",
    "abhinibbattā": "ထင်ရှားစွာ ပေါ်ထွက်ပြီးသော", "pātubhūtā": "ထင်ရှားလာပြီးသော",
    "samuppannā": "ကောင်းစွာ ဖြစ်ပေါ်ပြီးသော", "uṭṭhitā": "ထပေါ်ပြီးသော", "samuṭṭhitā": "ကောင်းစွာ ထပေါ်ပြီးသော",
    "aṃsena": "အပိုင်း", "saṅkhārā": "ပြုပြင်ဖန်တီးမှု", "viññāṇaṃ": "သိစိတ်",
    "avipakkavipākānaṃ": "အကျိုး မရင့်ကျက်သေးသော",
    "uppajjitvā": "ဖြစ်ပေါ်သည်", "niruddhā": "ချုပ်ငြိမ်းပြီးသော", "vigatā": "ကင်းပျောက်ပြီးသော",
    "vipariṇatā": "ဖောက်ပြန် ပြောင်းလဲပြီးသော", "abbhatthaṅgatā": "လုံးဝ ကွယ်ပျောက်ပြီးသော",
    "tesaṃ tesaṃ": "ထိုထို", "paccattaṃ": "ကိုယ်စီ ဖြစ်သော", "pāṭipuggalikā": "ပုဂ္ဂိုလ်တစ်ဦးချင်းစီ၏ ဖြစ်သော",
    "niyatā": "@niyata", "vibhava": "@vibhava", "ñāṇaṃ": "@alt",
    "rūpa": "@rupa4", "maggo": "@maggo", "dhamme": "@dhamme", "bahiddhā": "@bahiddha", "paṭicca": "@paticca",
    "sāsavā kusalābyākatā dhammā": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ်နှင့် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား",
    "avitakkaavicārā": "စတင်ကြံစည်မှုလည်း မရှိ ဆက်လက်သုံးသပ်မှုလည်း မရှိသော",
    # --- the view, doubt and rite lists (HSYN forms)
    "vicikicchā": "ယုံမှားမှု", "saṃyojanāni": "နှောင်ကြိုး", "saṃyojanaṃ": "နှောင်ကြိုး",
    "sakkāyadiṭṭhi": "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ", "sakkāya": "ကိုယ်",
    "parāmāso": "မှားယွင်းသော ယူဆမှု", "sīlabbataparāmāso": "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု",
    "sīlabbata": "သီလ အကျင့်ဝတ်", "vata": "အကျင့်ဝတ်",
    "tattha": "ထိုတို့အနက်", "assutavā": "အကြားအမြင် မရှိသော", "puthujjano": "ပုထုဇဉ်", "ariyānaṃ": "အရိယာ",
    "akovido": "မကျွမ်းကျင်သော", "avinīto": "မလေ့ကျင့်ထားသော", "dhammassa": "တရား",
    "sappurisānaṃ": "သူတော်ကောင်း", "purisānaṃ": "သူတော်ကောင်း",
    "attato": "အတ္တဟု", "samanupassati": "ရှုမြင်သည်", "rūpavantaṃ": "ရုပ် ရှိသော",
    "vedanaṃ": "ခံစားမှု", "saññaṃ": "မှတ်သိမှု", "saṅkhāre": "ပြုပြင်ဖန်တီးမှု",
    "yā": NONE, "evarūpā": "ဤသို့ သဘောရှိသော",
    "diṭṭhigataṃ": "အယူမှား", "gahanaṃ": "တောအုပ်", "kantāro": "ကန္တာရ", "visūkāyikaṃ": "ကောက်ကွေးမှု",
    "vipphanditaṃ": "တုန်လှုပ်မှု", "diṭṭhisaṃyojanaṃ": "အယူ နှောင်ကြိုး", "gāho": "@alt",
    "paṭiggāho": "ခိုင်မြဲစွာ စွဲကိုင်ခြင်း", "abhiniveso": "သက်ဝင်ယုံကြည်ခြင်း", "kummaggo": "လမ်းမှား",
    "micchāpatho": "မှားယွင်းသော လမ်းကြောင်း", "micchā": "မှားယွင်းသော", "patho": "@alt",
    "micchattaṃ": "မှားယွင်းမှု", "tittha": "အယူဝါဒ",
    "vipariyāsaggāho": "ပြောင်းပြန် စွဲကိုင်ခြင်း", "vipariyāsa": "ပြောင်းပြန်",
    "satthari": "ဘုရားရှင်", "kaṅkhati": "သံသယ ဖြစ်သည်", "sikkhāya": "ကျင့်စဉ်",
    "idappaccayatā": "ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ",
    "paṭiccasamuppannesu": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော",
    "paṭiccasamuppannesu dhammesu": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော သဘောတရား",
    "samuppannesu": "ဖြစ်ပေါ်လာသော", "samuppannesu dhammesu": "ဖြစ်ပေါ်လာသော သဘောတရား",
    "kaṅkhā": "သံသယ", "vimati": "စိတ်ရှုပ်ထွေးခြင်း", "dveḷhakaṃ": "စိတ် နှစ်ခွ ဖြစ်ခြင်း",
    "dvedhāpatho": "လမ်း နှစ်ခွ", "saṃsayo": "ဒွိဟ ဖြစ်ခြင်း", "anekaṃsaggāho": "တစ်ထစ်ချ မယူနိုင်ခြင်း",
    "ekaṃsa": "တစ်ထစ်ချ", "āsappanā": "ယိမ်းယိုင်ခြင်း", "parisappanā": "ပတ်ချာလည် ယိမ်းယိုင်ခြင်း",
    "apariyogāhanā": "နက်နက်နဲနဲ မသက်ဝင်နိုင်ခြင်း", "pariyogāhanā": "နက်နက်နဲနဲ သက်ဝင်နိုင်ခြင်း",
    "thambhitattaṃ": "တောင့်တင်းနေသော အဖြစ်", "cittassa": "စိတ်", "vilekho": "ခြစ်ကုတ်ခြင်း",
    "ito": "ဤသာသနာ", "samaṇa": "ရဟန်း", "brāhmaṇānaṃ": "ပုဏ္ဏား", "suddhi": "စင်ကြယ်ခြင်း",
    "puggalānaṃ": "ပုဂ္ဂိုလ်",
    "bahiddhā dhamme ārabbha": "သူတစ်ပါး၌ ရှိသော သဘောတရားတို့ကို အာရုံပြုသည်",
    "dhamme ārabbha": "သဘောတရားတို့ကို အာရုံပြုသည်",
    "rūpāyatanaṃ": "အဆင်းအရောင် အာရုံခံ နယ်ပယ်",
    # --- āyatana (1-1057)
    "cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "jivhā": "လျှာ",
    "sadda": "အသံ", "gandha": "အနံ့", "rasa": "အရသာ", "phoṭṭhabba": "အထိအတွေ့",
    "cakkhāyatanaṃ": "မျက်စိ အာရုံခံ နယ်ပယ်", "sotāyatanaṃ": "နား အာရုံခံ နယ်ပယ်",
    "ghānāyatanaṃ": "နှာခေါင်း အာရုံခံ နယ်ပယ်", "jivhāyatanaṃ": "လျှာ အာရုံခံ နယ်ပယ်",
    "kāyāyatanaṃ": "ကိုယ် အာရုံခံ နယ်ပယ်", "saddāyatanaṃ": "အသံ အာရုံခံ နယ်ပယ်",
    "gandhāyatanaṃ": "အနံ့ အာရုံခံ နယ်ပယ်", "rasāyatanaṃ": "အရသာ အာရုံခံ နယ်ပယ်",
    "phoṭṭhabbāyatanaṃ": "အထိအတွေ့ အာရုံခံ နယ်ပယ်",
    "appaṭighaṃ": "ထိခိုက်မှု မရှိသော", "anidassanaṃ": "မမြင်နိုင်သော",
    "dhamma": "@alt", "dhammāyatana": "သဘောတရား အာရုံခံ နယ်ပယ်",
    # --- the roots (1-1059 ff.)
    "kusalahetū": "ကုသိုလ် အမြစ်", "akusalahetū": "အကုသိုလ် အမြစ်",
    "abyākata": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော",
    "abyākatahetū": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော အမြစ်",
    "kāmāvacarahetū": "ကာမဘုံနှင့် ဆိုင်သော အမြစ်", "rūpāvacarahetū": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော အမြစ်",
    "arūpāvacarahetū": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော အမြစ်", "apariyāpannahetū": "ဘဝဘုံတို့၌ အကျုံးမဝင်သော အမြစ်",
    "avacara": "ဘုံနှင့် ဆိုင်သော", "rūpāvacara": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော",
    "arūpāvacara": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော",
    "yo": NONE, "yaṃ": NONE, "evarūpo": "ဤသို့ သဘောရှိသော", "evarūpaṃ": "ဤသို့ သဘောရှိသော",
    "mūlaṃ": "အမြစ်", "kusalamūlaṃ": "ကုသိုလ်၏ အမြစ်", "akusalamūlaṃ": "အကုသိုလ်၏ အမြစ်",
    # alobha / adosa
    "lubbhanā": "မက်မောခြင်း", "sārajjanā": "စွဲမက်ခြင်း", "asārāgo": "မတပ်မက်ခြင်း",
    "anabhijjhā": "သူ့ဥစ္စာကို မလိုချင်ခြင်း", "abhijjhā": "သူ့ဥစ္စာကို လိုချင်ခြင်း",
    "dussanā": "စိတ်ဆိုးခြင်း", "dussitattaṃ": "စိတ်ဆိုးထားသော အဖြစ်",
    "metti": "မေတ္တာ", "mettāyanā": "မေတ္တာ ထားခြင်း",
    "anuddā": "သနားကြင်နာခြင်း", "anuddāyanā": "သနားကြင်နာနေခြင်း",
    "hitesitā": "အကျိုးကို လိုလားခြင်း", "hita": "အကျိုး", "anukampā": "စာနာ ထောက်ထားခြင်း",
    "abyāpādo": "ဖျက်ဆီးလိုစိတ် မရှိခြင်း", "abyāpajjo": "မညှဉ်းဆဲလိုခြင်း", "byāpajjo": "ညှဉ်းဆဲလိုခြင်း",
    # amoha (paññā list)
    "dukkhe": "ဒုက္ခ", "dukkhe ñāṇaṃ": "ဒုက္ခကို သိသော ဉာဏ်", "samudaye": "ဖြစ်ပေါ်ခြင်း",
    "nirodhe": "ချုပ်ငြိမ်းခြင်း", "dukkhanirodhe": "ဒုက္ခ ချုပ်ငြိမ်းခြင်း",
    "paññā": "ပညာ", "pajānanā": "ကွဲပြားစွာ သိခြင်း", "vicayo": "စိစစ်ခြင်း", "pavicayo": "သေချာစွာ စိစစ်ခြင်း",
    "dhammavicayo": "သဘောတရားများကို စိစစ်ခြင်း",
    "sallakkhaṇā": "လက္ခဏာကို ကောင်းစွာ ခွဲခြားခြင်း", "upalakkhaṇā": "လက္ခဏာကို အနီးကပ် ခွဲခြားခြင်း",
    "paccupalakkhaṇā": "လက္ခဏာကို အသီးသီး ခွဲခြားခြင်း",
    "paṇḍiccaṃ": "လိမ္မာခြင်း", "kosallaṃ": "ကျွမ်းကျင်ခြင်း", "nepuññaṃ": "နက်နဲသိမ်မွေ့ခြင်း",
    "vebhabyā": "ခွဲခြမ်းစိတ်ဖြာခြင်း", "cintā": "စဉ်းစားခြင်း", "upaparikkhā": "စူးစမ်းဆန်းစစ်ခြင်း",
    "bhūrī": "ကျယ်ပြန့်ခြင်း", "medhā": "ဉာဏ်ထက်မြက်ခြင်း", "pariṇāyikā": "လမ်းပြခြင်း",
    "sampajaññaṃ": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း", "patodo": "နှင်တံ",
    "indriyaṃ": "စွမ်းရည်", "paññindriyaṃ": "ပညာ၏ စွမ်းရည်", "balaṃ": "စွမ်းအား", "paññābalaṃ": "ပညာ၏ စွမ်းအား",
    "satthaṃ": "ဓား", "paññāsatthaṃ": "ပညာ ဓား", "pāsādo": "ပြာသာဒ်", "paññāpāsādo": "ပညာ ပြာသာဒ်",
    "āloko": "အလင်း", "paññāāloko": "ပညာ အလင်း", "obhāso": "အရောင်အဝါ", "paññāobhāso": "ပညာ အရောင်အဝါ",
    "pajjoto": "မီးအိမ်", "paññāpajjoto": "ပညာ မီးအိမ်", "ratanaṃ": "ရတနာ", "paññāratanaṃ": "ပညာ ရတနာ",
    # lobha list (1-1065)
    "rāgo": "ရာဂ", "sārāgo": "တပ်မက်ခြင်း", "anunayo": "လိုက်လျောခြင်း", "anurodho": "သဘောတူ လိုက်ပါခြင်း",
    "nandī": "@alt", "icchā": "အလိုရှိခြင်း", "mucchā": "@alt",
    "gedho": "ငမ်းငမ်းတက် လိုချင်ခြင်း", "paligedho": "အလွန် ငမ်းငမ်းတက် လိုချင်ခြင်း",
    "saṅgo": "တွယ်ကပ်ခြင်း", "paṅko": "ရွှံ့ညွန်", "ejā": "တုန်လှုပ်ခြင်း", "māyā": "လှည့်စားတတ်ခြင်း",
    "janikā": "မွေးဖွားပေးတတ်သူ", "sañjananī": "ကောင်းစွာ မွေးဖွားပေးတတ်သူ", "sibbinī": "ချုပ်လုပ်တတ်သူ",
    "jālinī": "ပိုက်ကွန်ကဲ့သို့ ဖြစ်သူ", "saritā": "စီးဆင်းတတ်သူ", "visattikā": "ပျံ့နှံ့ တွယ်ကပ်တတ်သူ",
    "suttaṃ": "ချည်ကြိုး", "visaṭā": "ပျံ့နှံ့ခြင်း", "āyūhinī": "ကြိုးပမ်းစေတတ်သူ", "dutiyā": "အဖော်",
    "paṇidhi": "စိတ်ညွှတ်ခြင်း", "netti": "ဆွဲဆောင်သော ကြိုး", "vanaṃ": "တော", "vanatho": "တောအုပ်",
    "santhavo": "ရင်းနှီးခြင်း", "sineho": "@alt", "apekkhā": "ငဲ့ကွက်ခြင်း", "paṭibandhu": "ဆွေမျိုး",
    "āsā": "မျှော်လင့်ခြင်း", "āsisanā": "တောင့်တခြင်း",
    "dhana": "ဥစ္စာ", "putta": "သားသမီး", "jīvita": "အသက်",
    "jappā": "တမ်းတခြင်း", "pajappā": "အလွန် တမ်းတခြင်း", "abhijappā": "ထူးထူးခြားခြား တမ်းတခြင်း",
    "jappanā": "တမ်းတနေခြင်း", "loluppaṃ": "လိုချင်လွန်းခြင်း", "loluppāyanā": "လိုချင်လွန်းနေခြင်း",
    "pucchañjikatā": "အမြီး ခါ၍ ချော့မော့ခြင်း", "sādhu": "ကောင်းသည်ထက် ကောင်းသည်", "kamyatā": "@alt",
    "adhamma": "မတရားသော", "visama": "ဖောက်ပြန်သော",
    "nikanti": "စွဲလန်းခြင်း", "nikāmanā": "အလွန် လိုလားခြင်း", "patthanā": "ဆုတောင်းခြင်း",
    "pihanā": "အားကျ လိုချင်ခြင်း", "sampatthanā": "ကောင်းစွာ ဆုတောင်းခြင်း", "nirodha": "ချုပ်ငြိမ်းခြင်း",
    "ogho": "ရေအလျဉ်", "yogo": "ထမ်းပိုး", "gantho": "အထုံး", "upādānaṃ": "စွဲလမ်းမှု",
    "āvaraṇaṃ": "ပိတ်ဆို့ခြင်း", "nīvaraṇaṃ": "အတားအဆီး", "chādanaṃ": "ဖုံးအုပ်ခြင်း", "bandhanaṃ": "အချည်အနှောင်",
    "upakkileso": "ညစ်နွမ်းစေတတ်သော အညစ်အကြေး", "anusayo": "ကိန်းအောင်းခြင်း", "pariyuṭṭhānaṃ": "ထကြွခြင်း",
    "latā": "နွယ်ပင်", "vevicchaṃ": "တစ်ကိုယ်ကောင်းဆန်ခြင်း", "dukkha": "ဒုက္ခ", "nidānaṃ": "ဇာစ်မြစ်",
    "pabhavo": "ဖြစ်ပေါ်ရာ", "pāso": "ကျော့ကွင်း", "baḷisaṃ": "ငါးမျှားချိတ်", "visayo": "နယ်ပယ်",
    "nadī": "မြစ်", "gaddulaṃ": "ကြိုးသိုင်း", "samuddo": "သမုဒ္ဒရာ",
    # dosa list (1-1066)
    "anatthaṃ": "မကောင်းမှု", "acarīti": "ပြုခဲ့သည်", "acarī": "ပြုခဲ့သည်", "caratīti": "ပြုနေသည်",
    "āghāto": "ရန်ငြိုးဖွဲ့ခြင်း", "jāyati": "ဖြစ်ပေါ်သည်", "āghāto jāyati": "ရန်ငြိုးဖွဲ့ခြင်း ဖြစ်ပေါ်သည်",
    "piyassa": "ချစ်ခင်သော", "manāpassa": "နှစ်လိုဖွယ်ကောင်းသော", "aṭṭhāne": "အကြောင်း မရှိဘဲ",
    "paṭighāto": "ပြန်လည် ရန်ငြိုးဖွဲ့ခြင်း", "paṭighaṃ": "မုန်းတီးမှု", "paṭivirodho": "ပြန်လည် ဆန့်ကျင်ခြင်း",
    "kopo": "အမျက်ထွက်ခြင်း", "pakopo": "အလွန် အမျက်ထွက်ခြင်း", "sampakopo": "ပြင်းစွာ အမျက်ထွက်ခြင်း",
    "padoso": "အလွန် ဒေါသထွက်ခြင်း", "sampadoso": "ပြင်းစွာ ဒေါသထွက်ခြင်း", "byāpatti": "ဖောက်ပြန်ခြင်း",
    "kodho": "အမျက်ဒေါသ", "kujjhanā": "အမျက်ဒေါသ ထွက်ခြင်း", "byāpajjanā": "ညှဉ်းဆဲလိုခြင်း",
    "virodho": "ဆန့်ကျင်ခြင်း", "caṇḍikkaṃ": "ကြမ်းကြုတ်ခြင်း", "asuropo": "စကား ကြမ်းခြင်း",
    "anattamanatā": "မနှစ်သိမ့်ခြင်း",
    # moha list (1-1067)
    "aññāṇaṃ": "မသိခြင်း", "dukkhe aññāṇaṃ": "ဒုက္ခကို မသိခြင်း", "adassanaṃ": "မမြင်ခြင်း", "dassanaṃ": "မြင်ခြင်း",
    "anabhisamayo": "ထင်ထင်ရှားရှား မသိမြင်ခြင်း", "ananubodho": "လိုက်၍ မနားလည်ခြင်း",
    "anubodho": "လိုက်၍ နားလည်ခြင်း", "asambodho": "ကောင်းစွာ မနားလည်ခြင်း", "sambodho": "ကောင်းစွာ နားလည်ခြင်း",
    "appaṭivedho": "ထိုးဖောက်၍ မသိခြင်း", "asaṃgāhanā": "စုစည်း၍ မယူနိုင်ခြင်း",
    "asamapekkhanā": "ညီညီညွတ်ညွတ် မရှုမြင်ခြင်း", "samapekkhanā": "ညီညီညွတ်ညွတ် ရှုမြင်ခြင်း",
    "apaccavekkhaṇā": "ပြန်လည် မဆင်ခြင်ခြင်း", "paccavekkhaṇā": "ပြန်လည် ဆင်ခြင်ခြင်း",
    "apaccakkhakammaṃ": "ကိုယ်တိုင် ထင်ထင်ရှားရှား မပြုခြင်း", "paccakkhakammaṃ": "ကိုယ်တိုင် ထင်ထင်ရှားရှား ပြုခြင်း",
    "dummejjhaṃ": "ဉာဏ်နုံခြင်း", "bālyaṃ": "မိုက်မဲခြင်း",
    "asampajaññaṃ": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိခြင်း",
    "pamoho": "အလွန် တွေဝေခြင်း", "sammoho": "လုံးဝ တွေဝေခြင်း", "laṅgī": "တံခါးကန့်လန့်",
    "vipākato": "အကျိုး အဖြစ်", "kusalānaṃ": "ကုသိုလ်", "kusalānaṃ vā dhammānaṃ": "ကုသိုလ် သဘောတရား",
    "kusalānaṃ dhammānaṃ": "ကုသိုလ် သဘောတရား",
    "abyākatesu vā dhammesu": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား",
    "sambojjha": "ဗောဇ္ဈင်", "aṅgo": NONE,           # aṅga is inside the loan ဗောဇ္ဈင်
    "maggaṅgaṃ": "မဂ်၏ အင်္ဂါ",
    "tehi dhammehi": "ထိုသဘောတရား", "hetuvippayuttā": "အမြစ်နှင့် ကင်းကွာသော",
    "hetusampayuttā": "အမြစ်နှင့် ယှဉ်တွဲသော", "mohena": "မောဟ",
    "asaṅkhatā dhātu": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော ဓာတ်", "yeva": "အကြင်",
    "appaṭighā": "ထိခိုက်မှု မရှိသော",
    "upādāya": "မှီ၍ ဖြစ်သော", "upādāya rūpaṃ": "မှီ၍ ဖြစ်သော ရုပ်",
    "mahābhūtā": "မူလဓာတ်ကြီး", "bhūtā": "@bhuta",
    "sāsavā kusalākusalābyākatā dhammā": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ် အကုသိုလ်နှင့် ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော သဘောတရား",
    "āsavo": "စိတ်အစွန်းအထင်း", "kāmāsavo": "ကာမ စိတ်အစွန်းအထင်း", "bhavāsavo": "ဘဝ စိတ်အစွန်းအထင်း",
    "diṭṭhāsavo": "အယူ စိတ်အစွန်းအထင်း", "avijjāsavo": "အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း",
    "kāmesu": "ကာမ", "chando": "လိုလားမှု", "pariḷāho": "ပူလောင်မှု", "kāmarāgo": "ကာမရာဂ",
    "sassato": "ထာဝရ တည်မြဲသည်", "jīvaṃ": "အသက်", "sarīranti": "ကိုယ်ခန္ဓာ", "hoti": "ရှိသည်",
    "hoti tathāgato": "မြတ်စွာဘုရား … ရှိသည်", "maraṇāti": "သေပြီးနောက်", "aññaṃ": "တခြားစီ",
    "avasesā sāsavā kusala": "ကြွင်းကျန်သော စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော ကုသိုလ်",
    "avijjāsavena": "အမှန်ကို မသိမှု စိတ်အစွန်းအထင်း",
    "kaṇḍe": "အခန်း", "bhāṇa": "ရွတ်ဖတ်ရန်", "vāro": "အပိုင်း",
    # --- fetters (1-1118 ff.)
    "dasa": "ဆယ်ပါး", "paṭigha": "မုန်းတီးမှု", "māna": "မာန", "māno": "မာန", "issā": "ငြူစူမှု",
    "macchariya": "ဝန်တိုမှု", "rāga": "ရာဂ", "kāmarāga": "ကာမရာဂ",
    "sīlabbataparāmāsa": "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု",
    "kāmarāgasaṃyojanaṃ": "ကာမရာဂ နှောင်ကြိုး", "paṭighasaṃyojanaṃ": "မုန်းတီးမှု နှောင်ကြိုး",
    "mānasaṃyojanaṃ": "မာန နှောင်ကြိုး", "vicikicchāsaṃyojanaṃ": "ယုံမှားမှု နှောင်ကြိုး",
    "sīlabbataparāmāsasaṃyojanaṃ": "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု နှောင်ကြိုး",
    "bhavarāgasaṃyojanaṃ": "ဘဝရာဂ နှောင်ကြိုး", "issāsaṃyojanaṃ": "ငြူစူမှု နှောင်ကြိုး",
    "macchariyasaṃyojanaṃ": "ဝန်တိုမှု နှောင်ကြိုး", "avijjāsaṃyojanaṃ": "အမှန်ကို မသိမှု နှောင်ကြိုး",
    "kāmacchando": "ကာမကို လိုလားမှု",
    "sadiso": "တူညီသူ", "hīno": "ယုတ်ညံ့သူ", "maññanā": "ထင်မှတ်ခြင်း", "maññitattaṃ": "ထင်မှတ်ထားသော အဖြစ်",
    "unnati": "စိတ် မြင့်တက်ခြင်း", "unnamo": "ခေါင်းမော့ခြင်း", "dhajo": "အလံ", "ketu": "အလံ",
    "sampaggāho": "အလွန် မြှင့်တင်ခြင်း", "ketukamyatā": "အလံ ထူလိုခြင်း",
    "patiṭṭhāho": "ခိုင်မြဲစွာ စွဲကိုင်ခြင်း",                 # source slip for paṭiggāho (harmonise item 15)
    "para": "@alt", "issāyanā": "ငြူစူခြင်း", "usūyā": "သဝန်တိုမှု", "usūyanā": "သဝန်တိုခြင်း",
    "sakkāra": "အရိုအသေ ပြုခံရမှု", "garukāra": "လေးစားခံရမှု", "mānana": "ချီးမြှောက်ခံရမှု",
    "vandana": "ရှိခိုးခံရမှု", "pūjanāsu": "ပူဇော်ခံရမှု",
    "macchariyāni": "ဝန်တိုမှု", "āvāsa": "နေရာထိုင်ခင်း", "kula": "ကိုးကွယ်သော အိမ်", "vaṇṇa": "ဂုဏ်သတင်း",
    "maccharāyanā": "ဝန်တိုနေခြင်း", "kadariyaṃ": "ကပ်စေးနည်းခြင်း", "kaṭukañcukatā": "တွန့်တိုခြင်း",
    "aggahitattaṃ": "တင်းတင်း ဆုပ်ကိုင်ထားသော အဖြစ်",
    "saṃyojanā ceva saṃyojaniyā": "နှောင်ကြိုးလည်း ဖြစ် နှောင်ကြိုး၏ အာရုံလည်း ဖြစ်နိုင်သော",
    "avijjāsaṃyojanena": "အမှန်ကို မသိမှု နှောင်ကြိုး",
    "saṃyojanavippayuttā saṃyojaniyā": "နှောင်ကြိုးနှင့် ကင်းကွာသော … နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော",
    # --- knots (1-1140 ff.)
    "kāyagantho": "ကိုယ် အထုံး", "byāpādo": "ဖျက်ဆီးလိုစိတ်", "sacca": "@alt",
    "abhijjhā kāyagantho": "သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် အထုံး",
    "byāpādo kāyagantho": "ဖျက်ဆီးလိုစိတ်ဟူသော ကိုယ် အထုံး",
    "sīlabbataparāmāso kāyagantho": "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှုဟူသော ကိုယ် အထုံး",
    "idaṃ saccābhiniveso kāyagantho": "ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်းဟူသော ကိုယ် အထုံး",
    "idaṃsaccābhiniveso kāyagantho": "ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်းဟူသော ကိုယ် အထုံး",
    "vuccati abhijjhā kāya": "သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် … ဟု ခေါ်သည်",
    "vuccati byāpādo kāya": "ဖျက်ဆီးလိုစိတ်ဟူသော ကိုယ် … ဟု ခေါ်သည်",
    "vuccati sīlabbataparāmāso kāya": "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှုဟူသော ကိုယ် … ဟု ခေါ်သည်",
    "vuccati idaṃsaccābhiniveso kāya": "ဤအရာသာ အမှန်ဟု သက်ဝင်ယုံကြည်ခြင်းဟူသော ကိုယ် … ဟု ခေါ်သည်",
    "moghamaññanti": "အခြားအရာသည် အချည်းနှီး ဖြစ်သည်", "sarīraṃ": "ကိုယ်ခန္ဓာ", "maraṇā": "သေပြီးနောက်",
    "sīlabbataparāmāsaṃ": "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု",
    "sīlabbataparāmāsaṃ kāyaganthaṃ": "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှုဟူသော ကိုယ် အထုံး",
    "ganthā ceva ganthaniyā": "အထုံးလည်း ဖြစ် အထုံး၏ အာရုံလည်း ဖြစ်နိုင်သော",
    "abhijjhākāyaganthena": "သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် အထုံး",
    "ganthavippayuttā ganthaniyā": "အထုံးနှင့် ကင်းကွာသော … အထုံး၏ အာရုံ ဖြစ်နိုင်သော",
    "oghavippayuttā": "ရေအလျဉ်နှင့် ကင်းကွာသော", "yogavippayuttā": "ထမ်းပိုးနှင့် ကင်းကွာသော",
    # --- hindrances (1-1158 ff.)
    "chanda": "လိုလားမှု", "kāmacchanda": "ကာမကို လိုလားမှု", "byāpāda": "ဖျက်ဆီးလိုစိတ်",
    "thina": "ထိုင်းမှိုင်းမှု", "middha": "ငိုက်မျဉ်းမှု", "uddhacca": "ယောက်ယက်ခတ်မှု", "kukkucca": "နောင်တ ပူပန်မှု",
    "kāmacchandanīvaraṇaṃ": "ကာမကို လိုလားမှု အတားအဆီး", "byāpādanīvaraṇaṃ": "ဖျက်ဆီးလိုစိတ် အတားအဆီး",
    "thinamiddhanīvaraṇaṃ": "ထိုင်းမှိုင်းမှုနှင့် ငိုက်မျဉ်းမှု အတားအဆီး",
    "uddhaccakukkuccanīvaraṇaṃ": "ယောက်ယက်ခတ်မှုနှင့် နောင်တ ပူပန်မှု အတားအဆီး",
    "vicikicchānīvaraṇaṃ": "ယုံမှားမှု အတားအဆီး", "avijjānīvaraṇaṃ": "အမှန်ကို မသိမှု အတားအဆီး",
    "akallatā": "မကျန်းမာခြင်း", "akammaññatā": "အသုံးပြုရန် မသင့်တော်ခြင်း", "olīyanā": "တွန့်ဆုတ်ခြင်း",
    "sallīyanā": "လုံးဝ တွန့်ဆုတ်ခြင်း", "līnaṃ": "အားပျော့ခြင်း", "līyanā": "အားပျော့နေခြင်း",
    "thinaṃ": "ထိုင်းမှိုင်းမှု", "thiyanā": "ထိုင်းမှိုင်းခြင်း", "thiyitattaṃ": "ထိုင်းမှိုင်းထားသော အဖြစ်",
    "kāyassa": "@kayassa",
    "onāho": "ပိတ်ဖုံးခံရခြင်း", "antosamorodho": "အတွင်း၌ ပိတ်ဆို့ခံရခြင်း", "middhaṃ": "ငိုက်မျဉ်းမှု",
    "soppaṃ": "အိပ်ငိုက်ခြင်း", "pacalāyikā": "ငိုက်ဆင်းခြင်း", "supanā": "အိပ်ပျော်ခြင်း",
    "supitattaṃ": "အိပ်ပျော်ထားသော အဖြစ်",
    "uddhaccaṃ": "ယောက်ယက်ခတ်မှု", "avūpasamo": "မငြိမ်ဝပ်ခြင်း", "cetaso": "စိတ်", "vikkhepo": "ပျံ့လွင့်ခြင်း",
    "bhantattaṃ": "ယိမ်းထိုးနေသော အဖြစ်",
    "kappiye": "အပ်စပ်သည်", "avajje": "အပြစ်မရှိသည်", "vajja": "အပြစ်ရှိသည်", "saññitā": "မှတ်ထင်ခြင်း",
    "kukkuccaṃ": "နောင်တ ပူပန်မှု", "kukkuccāyanā": "နောင်တ ပူပန်ခြင်း", "vippaṭisāro": "နောင်တ ရခြင်း",
    "nīvaraṇā ceva nīvaraṇiyā": "အတားအဆီးလည်း ဖြစ် အတားအဆီး၏ အာရုံလည်း ဖြစ်နိုင်သော",
    "nīvaraṇāni": "အတားအဆီး", "avijjānīvaraṇena": "အမှန်ကို မသိမှု အတားအဆီး",
    "kukkuccanīvaraṇaṃ": "နောင်တ ပူပန်မှု အတားအဆီး", "uddhaccanīvaraṇaṃ": "ယောက်ယက်ခတ်မှု အတားအဆီး",
    "nīvaraṇavippayuttā nīvaraṇiyā": "အတားအဆီးနှင့် ကင်းကွာသော … အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော",
    # --- citta, rūpa (1-1193 ff.)
    "cakkhuviññāṇaṃ": "မျက်စိ သိစိတ်", "sotaviññāṇaṃ": "နား သိစိတ်", "ghānaviññāṇaṃ": "နှာခေါင်း သိစိတ်",
    "jivhāviññāṇaṃ": "လျှာ သိစိတ်", "kāyaviññāṇaṃ": "ကိုယ် သိစိတ်", "manodhātu": "မနော ဓာတ်",
    "manoviññāṇa": "မနော သိစိတ်", "manoviññāṇadhātu": "မနော သိစိတ် ဓာတ်",
    "cittañca": "စိတ်", "sampayuttanti": "ယှဉ်တွဲသော", "vattabbaṃ": "ခေါ်ဆိုသည်",
    "cittavisaṃsaṭṭhā": "စိတ်နှင့် မရောနှောသော",
    "kāyaviññatti": "ကိုယ်ဖြင့် ထုတ်ဖော်ပြသမှု", "vacīviññatti": "နှုတ်ဖြင့် ထုတ်ဖော်ပြသမှု",
    "viññatti": "ထုတ်ဖော်ပြသမှု", "cittajaṃ": "စိတ်မှ မွေးဖွားသော", "cittahetukaṃ": "စိတ်ကို အမြစ်ပြုသော",
    "santati": "ဆက်လက်ဖြစ်ပေါ်ခြင်း", "rūpassa santati": "ရုပ်၏ ဆက်လက်ဖြစ်ပေါ်ခြင်း",
    "rūpassa upacayo": "ရုပ်၏ တိုးပွားခြင်း", "lahutā": "ပေါ့ပါးခြင်း", "rūpassa lahutā": "ရုပ်၏ ပေါ့ပါးခြင်း",
    "mudutā": "ပျော့ပျောင်းခြင်း", "rūpassa mudutā": "ရုပ်၏ ပျော့ပျောင်းခြင်း",
    "kammaññatā": "အသုံးပြုရန် သင့်တော်ခြင်း", "rūpassa kammaññatā": "ရုပ်၏ အသုံးပြုရန် သင့်တော်ခြင်း",
    "ākāsa": "@alt", "ākāsadhātu": "ဟင်းလင်းပြင် ဓာတ်", "āpo": "ရေ", "āpodhātu": "ရေဓာတ်",
    "kabaḷīkāro": "လုတ်ပြု၍ စားရသော", "āhāro": "အာဟာရ", "kabaḷīkāro āhāro": "လုတ်ပြု၍ စားရသော အာဟာရ",
    "avasesañca": "ကြွင်းကျန်သော", "avasesañca rūpaṃ": "ကြွင်းကျန်သော ရုပ်",
    "manāyatanaṃ": "မနော အာရုံခံ နယ်ပယ်", "dhammāyatanaṃ": "သဘောတရား အာရုံခံ နယ်ပယ်",
    # --- clingings (1-1219 ff.)
    "kāmupādānaṃ": "ကာမ စွဲလမ်းမှု", "diṭṭhupādānaṃ": "အယူ စွဲလမ်းမှု",
    "sīlabbatupādānaṃ": "သီလ အကျင့်ဝတ် စွဲလမ်းမှု", "attavādupādānaṃ": "အတ္တဟူသော ဝါဒ စွဲလမ်းမှု",
    "vāda": "ဝါဒ", "atta": "အတ္တ",
    "sammā": "@samma", "sukha": "@sukha",
    "natthi": "မရှိသည်", "kammānaṃ": "ကံ", "dukkaṭānaṃ": "ဆိုးစွာ ပြုသော", "sattā": "သတ္တဝါ",
    "brāhmaṇā": "ပုဏ္ဏား", "abhiññā": "ထူးကဲစွာ သိသည်", "pitā": "အဖ", "mātā": "အမိ",
    "gatā": "ရောက်ရှိသော", "paṭipannā": "ကျင့်ကြံသော", "sacchikatvā": "မျက်မှောက်ပြုသည်",
    "pavedentīti": "ဟောကြားသည်", "opapātikā": "အလိုအလျောက် ပေါ်လာသော", "hutaṃ": "ပူဇော်သကာ ဆက်ကပ်ခြင်း",
    "sīlabbatupādānañca": "သီလ အကျင့်ဝတ် စွဲလမ်းမှု",
    "upādānā ceva upādāniyā": "စွဲလမ်းမှုလည်း ဖြစ် စွဲလမ်းမှု၏ အာရုံလည်း ဖြစ်နိုင်သော",
    "upādānāni": "စွဲလမ်းမှု", "kāmupādānena": "ကာမ စွဲလမ်းမှု", "upādānañceva": "စွဲလမ်းမှု",
    "kāmupādānaṃ diṭṭhupādānena": "ကာမ စွဲလမ်းမှုသည် အယူ စွဲလမ်းမှု",
    "upādānavippayuttā upādāniyā": "စွဲလမ်းမှုနှင့် ကင်းကွာသော … စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော",
    # --- defilements (1-1235 ff.)
    "vatthūni": "ဖြစ်ရာ အခြေခံ", "ahirīkaṃ": "ဒုစရိုက်ကို မရှက်မှု", "ahirikaṃ": "ဒုစရိုက်ကို မရှက်မှု",
    "anottappaṃ": "ဒုစရိုက်ကို မကြောက်ရွံ့မှု",
    "hirīyati": "ရှက်သည်", "pāpakānaṃ": "ယုတ်မာသော", "samāpattiyā": "ကျူးလွန်ခြင်း",
    "ottappati": "ကြောက်ရွံ့သည်", "ottappitabbena": "ကြောက်ရွံ့ထိုက်သည့်အရာ",
    "kileso": "ကိလေသာ",
    "uddhaccaṃ anottappena": "ယောက်ယက်ခတ်မှုသည် ဒုစရိုက်ကို မကြောက်ရွံ့မှု",
    "uddhaccaṃ ahirikena": "ယောက်ယက်ခတ်မှုသည် ဒုစရိုက်ကို မရှက်မှု",
    "ahirikaṃ anottappena": "ဒုစရိုက်ကို မရှက်မှုသည် ဒုစရိုက်ကို မကြောက်ရွံ့မှု",
    "ahirikaṃ uddhaccena": "ဒုစရိုက်ကို မရှက်မှုသည် ယောက်ယက်ခတ်မှု",
    "anottappaṃ uddhaccena": "ဒုစရိုက်ကို မကြောက်ရွံ့မှုသည် ယောက်ယက်ခတ်မှု",
    "anottappaṃ ahirikena": "ဒုစရိုက်ကို မကြောက်ရွံ့မှုသည် ဒုစရိုက်ကို မရှက်မှု",
    "kilesavippayuttā saṃkilesikā": "ကိလေသာနှင့် ကင်းကွာသော … ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော",
    # --- planes (1-1287 ff.)
    "avicinirayaṃ": "အဝီစိ ငရဲ", "pariyantaṃ": "အဆုံးအစွန်", "karitvā": "ပြုသည်",
    "nimmita": "နိမ္မိတ", "vasavattī": "ဝသဝတ္တီ",       # parts of the loan name «ပရနိမ္မိတဝသဝတ္တီ»
    "deve": "နတ်", "āyatanā": "အာရုံခံ နယ်ပယ်",
    "brahma": "ဗြဟ္မာ့", "samāpannassa": "ဈာန် ဝင်စားသော", "upapannassa": "ထိုဘုံ၌ ဖြစ်ပေါ်သော",
    "diṭṭhadhamma": "မျက်မှောက်ဘဝ", "vihārissa": "နေထိုင်သော",
    "ānañca": "အဆုံး မရှိသော", "ānañcāyatana": "အဆုံး မရှိသော … နယ်ပယ်", "asaññā": "မှတ်သိမှု မရှိသော",
    "sampayuttakā": "ယှဉ်တွဲသော",
    "vijjābhāgino": "အမှန်သိမြင်မှု၏ အစိတ်အပိုင်း ဖြစ်သော",
    "avijjābhāgino": "အမှန်ကို မသိမှု၏ အစိတ်အပိုင်း ဖြစ်သော",
    "maggesu": "မဂ်", "magge": "မဂ်", "upariṭṭhime": "အမြင့်ဆုံး",
    "ahirīkañca": "ဒုစရိုက်ကို မရှက်မှု", "duccaritaṃ": "ဒုစရိုက်", "caritaṃ": "စရိုက်",   # part of the loan သုစရိုက်
    "atapanīyā": "မပူပန်စေတတ်သော",
    "saṅkhā": "ရေတွက် ခေါ်ဝေါ်ခြင်း", "samaññā": "အများ သမုတ်ခြင်း", "vohāro": "ပြောဆို သုံးနှုန်းခြင်း",
    "nāmaṃ": "@namam", "nāmakammaṃ": "အမည်ပေးခြင်း", "nāmadheyyaṃ": "အမည်နာမ", "abhilāpo": "ခေါ်ဆိုခြင်း",
    "adhivacanapathā": "အမည်ခေါ်ဝေါ်မှု၏ လမ်းကြောင်း ဖြစ်သော",
    "niruttipathā": "စကားဖြင့် ဖော်ပြမှု၏ လမ်းကြောင်း ဖြစ်သော",
    "paññattipathā": "သတ်မှတ်ချက်၏ လမ်းကြောင်း ဖြစ်သော",
    "bhavadiṭṭhi": "ဘဝ ဆက်လက် တည်ရှိသည်ဟူသော အယူ", "vibhavadiṭṭhi": "ဘဝ ပျောက်ကွယ်သည်ဟူသော အယူ",
    "bhavissati": "ဆက်လက် တည်ရှိသည်", "attā": "အတ္တ", "ucchijjissati": "ပြတ်စဲသွားသည်",
    "antavā diṭṭhi": "လောကသည် အဆုံး ရှိသည်ဟူသော အယူ", "anantavā diṭṭhi": "လောကသည် အဆုံး မရှိဟူသော အယူ",
    "pubbantānudiṭṭhi": "အတိတ်နှင့် ပတ်သက်သော အယူ", "aparantānudiṭṭhi": "အနာဂတ်နှင့် ပတ်သက်သော အယူ",
    "uppajjati": "ဖြစ်ပေါ်သည်", "uppajjati diṭṭhi": "ဖြစ်ပေါ်သော အယူ",
    "ottappaṃ": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု",
    "sahadhammike": "တရားနှင့် လျော်စွာ", "vuccamāne": "သွန်သင် ပြောဆိုသော",
    "dovacassāyaṃ": "စကား နားမထောင်ခြင်း", "dovacassiyaṃ": "စကား နားမထောင်သော အဖြစ်",
    "vippaṭikūla": "ဆန့်ကျင်ဘက်", "gāhitā": "ယူခြင်း", "vipaccanīka": "ဆန့်ကျင်ခြင်း", "sātatā": "နှစ်သက်ခြင်း",
    "anādariyaṃ": "မလေးစားခြင်း", "anādaratā": "မလေးစားသော အဖြစ်", "agāravatā": "ရိုသေမှု မရှိခြင်း",
    "appaṭissavatā": "နာခံမှု မရှိခြင်း", "paṭissavatā": "နာခံမှု",
    "puggalā": "ပုဂ္ဂိုလ်", "saddhā": "@saddha", "dussīlā": "သီလ ပျက်သော", "sutā": "အကြားအမြင်",
    "maccharino": "ဝန်တိုသော", "duppaññā": "ပညာ နည်းသော",
    "sevanā": "ပေါင်းသင်းခြင်း", "nisevanā": "နီးကပ်စွာ ပေါင်းသင်းခြင်း", "saṃsevanā": "ကောင်းစွာ ပေါင်းသင်းခြင်း",
    "bhajanā": "ဆည်းကပ်ခြင်း", "sambhajanā": "ကောင်းစွာ ဆည်းကပ်ခြင်း", "bhatti": "ကိုးကွယ်ခြင်း",
    "sampavaṅkatā": "ညွတ်ကိုင်းခြင်း",
    "sovacassāyaṃ": "စကား နားထောင်ခြင်း", "sovacassiyaṃ": "စကား နားထောင်သော အဖြစ်", "paṭikūla": "ဆန့်ကျင်ဘက်",
    "sagāravatā": "ရိုသေမှု ရှိခြင်း", "sādariyaṃ": "လေးစားခြင်း", "sādaratā": "လေးစားသော အဖြစ်",
    "sappaṭissavatā": "နာခံမှု ရှိခြင်း",
    "sīlavanto": "သီလ ရှိသော", "cāgavanto": "စွန့်ကြဲမှု ရှိသော", "paññavanto": "ပညာ ရှိသော",
    "āpattikusalatā": "အပြစ်တို့၌ ကျွမ်းကျင်ခြင်း", "āpattivuṭṭhānakusalatā": "အပြစ်မှ ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း",
    "samāpattikusalatā": "ဈာန် ဝင်စားရာ၌ ကျွမ်းကျင်ခြင်း",
    "samāpattivuṭṭhānakusalatā": "ဈာန်မှ ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း",
    "dhātukusalatā": "ဓာတ်တို့၌ ကျွမ်းကျင်ခြင်း", "āyatanakusalatā": "အာရုံခံ နယ်ပယ်တို့၌ ကျွမ်းကျင်ခြင်း",
    "paṭiccasamuppādakusalatā": "အကြောင်းအကျိုး ဆက်စပ်ဖြစ်ပေါ်ပုံ၌ ကျွမ်းကျင်ခြင်း",
    "ṭhānakusalatā": "ဖြစ်နိုင်သည့်အရာ၌ ကျွမ်းကျင်ခြင်း", "aṭṭhānakusalatā": "မဖြစ်နိုင်သည့်အရာ၌ ကျွမ်းကျင်ခြင်း",
    "aṭṭhārasa": "ဆယ့်ရှစ်ပါး", "dvādasa": "ဆယ့်နှစ်ပါး", "dhātūnaṃ": "ဓာတ်",
    "cakkhudhātu": "မျက်စိ ဓာတ်", "sotadhātu": "နား ဓာတ်", "ghānadhātu": "နှာခေါင်း ဓာတ်", "jivhādhātu": "လျှာ ဓာတ်",
    "kāyadhātu": "ကိုယ် ဓာတ်", "rūpadhātu": "အဆင်းအရောင် ဓာတ်", "saddadhātu": "အသံ ဓာတ်", "gandhadhātu": "အနံ့ ဓာတ်",
    "rasadhātu": "အရသာ ဓာတ်", "phoṭṭhabbadhātu": "အထိအတွေ့ ဓာတ်",
    "cakkhuviññāṇa": "မျက်စိ သိစိတ်", "sotaviññāṇa": "နား သိစိတ်", "ghānaviññāṇa": "နှာခေါင်း သိစိတ်",
    "jivhāviññāṇa": "လျှာ သိစိတ်", "kāyaviññāṇa": "ကိုယ် သိစိတ်",
    "cakkhuviññāṇadhātu": "မျက်စိ သိစိတ် ဓာတ်", "kāyaviññāṇadhātu": "ကိုယ် သိစိတ် ဓာတ်",
    # dependent origination (1-1343)
    "paccayā": "@paccaya", "jarā": "အိုခြင်း", "maraṇaṃ": "သေခြင်း", "soka": "စိုးရိမ်ခြင်း",
    "parideva": "ငိုကြွေးခြင်း", "domanassa": "စိတ်ဆင်းရဲခြင်း", "upāyāsā": "ပြင်းစွာ ပူပန်ခြင်း",
    "bhavo": "ဘဝ", "jāti": "မွေးဖွားခြင်း", "phasso": "တွေ့ထိမှု", "āyatanaṃ": "အာရုံခံ နယ်ပယ်", "nāma": "စိတ်ပိုင်း",
    "samudayo": "ဖြစ်ပေါ်ခြင်း", "khandhassa": "အစုအဝေး", "kevalassa": "အားလုံး",
    "uppādāya": "@alt", "taṃ taṃ": "ထိုထို", "ye ye": "အကြင် အကြင်",
    "ajimhatā": "မကောက်ကွေးခြင်း", "jimhatā": "ကောက်ကွေးခြင်း", "avaṅkatā": "မကွေးညွှတ်ခြင်း",
    "vaṅkatā": "ကွေးညွှတ်ခြင်း", "akuṭilatā": "မလိမ်ကောက်ခြင်း", "kuṭilatā": "လိမ်ကောက်ခြင်း",
    "maddavatā": "နူးညံ့သော အဖြစ်", "akakkhaḷatā": "မကြမ်းတမ်းခြင်း", "kakkhaḷatā": "ကြမ်းတမ်းခြင်း",
    "akathinatā": "မမာကျောခြင်း", "kathinatā": "မာကျောခြင်း", "nīca": "နှိမ့်ချခြင်း", "cittatā": "စိတ်",
    "khamanatā": "ခွင့်လွှတ်ခြင်း", "adhivāsanatā": "လက်ခံ သည်းညည်းခံခြင်း", "acaṇḍikkaṃ": "မကြမ်းကြုတ်ခြင်း",
    "anasuropo": "စကား မကြမ်းခြင်း", "attamanatā": "နှစ်သိမ့်ခြင်း",
    "kāyiko": "ကိုယ်ဖြင့်", "vācasiko": "နှုတ်ဖြင့်", "avītikkamo": "မကျူးလွန်ခြင်း", "soraccaṃ": "ယဉ်ကျေးခြင်း",
    "saṃvaro": "@samvaro",
    # speech (1-1350)
    "vācā": "စကား", "aṇḍakā": "ခက်ထန်သော", "kakkasā": "ကြမ်းတမ်းသော", "kaṭukā": "နာကျင်စေသော",
    "abhisajjanī": "ထိခိုက်စေသော", "kodha": "ဒေါသ", "sāmantā": "နီးစပ်သော", "samādhi": "သမာဓိ",
    "saṃvattanikā": "ဖြစ်စေသော", "tathārūpiṃ": "ထိုသို့သော", "neḷā": "အပြစ်ကင်းသော", "kaṇṇa": "နား",
    "sukhā": "ချိုသော", "pemanīyā": "ချစ်ခင်ဖွယ်ကောင်းသော", "hadaya": "နှလုံး", "gamā": "ရောက်သော",
    "porī": "ယဉ်ယဉ်ကျေးကျေး ရှိသော", "kantā": "နှစ်သက်သော", "manāpā": "စိတ်တွေ့သော",
    "bhāsitā hoti": "ပြောဆိုသူ ဖြစ်သည်", "saṇha": "ချောမွေ့သော", "sakhila": "ချိုသာသော",
    "apharusa": "မကြမ်းတမ်းသော", "sākhalyaṃ": "စကား ချိုသာခြင်း",
    "paṭisanthārā": "ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း", "āmisa": "ပစ္စည်း",
    "paṭisanthārako": "ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံသူ", "ekacco": "အချို့သော သူ",
    # guarding the doors (1-1352 ff.)
    "cakkhunā": "မျက်စိ", "disvā": "မြင်သည်", "nimitta": "အမှတ်အသား", "gāhī": "စွဲယူသူ",
    "viharantaṃ": "နေသော", "asaṃvutaṃ": "မစောင့်စည်းသော",
    "abhijjhādomanassā": "သူ့ဥစ္စာကို လိုချင်ခြင်း စိတ်ဆင်းရဲခြင်း", "domanassā": "စိတ်ဆင်းရဲခြင်း",
    "pāpakā": "ယုတ်မာသော", "anvāssaveyyuṃ": "စီးဝင်လာနိုင်သည်", "saṃvarāya": "စောင့်စည်းရန်",
    "paṭipajjati": "ကျင့်ကြံသည်", "rakkhati": "စောင့်ရှောက်သည်", "āpajjati": "ပြုသည်",
    "sotena": "နား", "sutvā": "ကြားသည်", "saddaṃ": "အသံ", "ghānena": "နှာခေါင်း", "gandhaṃ": "အနံ့",
    "ghāyitvā": "နမ်းသည်", "jivhāya": "လျှာ", "rasaṃ": "အရသာ", "sāyitvā": "လျက်သည်", "kāyena": "ကိုယ်",
    "phoṭṭhabbaṃ": "အထိအတွေ့", "phusitvā": "ထိသည်", "manasā": "မနော", "dhammaṃ": "သဘောတရား",
    "viññāya": "သိသည်", "manindriyaṃ": "မနော၏ စွမ်းရည်", "indriyānaṃ": "အာရုံခံ အင်္ဂါ",
    "agutti": "မစောင့်ထိန်းခြင်း", "agopanā": "မကာကွယ်ခြင်း", "anārakkho": "မစောင့်ရှောက်ခြင်း",
    "asaṃvaro": "မစောင့်စည်းခြင်း", "gopanā": "ကာကွယ်ခြင်း", "ārakkho": "စောင့်ရှောက်ခြင်း",
    # food (1-1353, 1-1355)
    "appaṭisaṅkhā": "ပြန်လည် မဆင်ခြင်ခြင်း", "paṭisaṅkhā": "ပြန်လည် ဆင်ခြင်ခြင်း", "ayoniso": "မသင့်လျော်စွာ",
    "āhāraṃ": "အစာ", "āhāreti": "စားသုံးသည်",
    "davāya": "ကစားရန်", "madāya": "မာန်ယစ်ရန်", "maṇḍanāya": "အလှပြင်ရန်", "vibhūsanāya": "တန်ဆာဆင်ရန်",
    "ṭhitiyā": "တည်တံ့ရန်", "yāpanāya": "ဆက်လက် ရှင်သန်ရန်", "vihiṃsā": "ညှဉ်းပန်းမှု",
    "brahmacariya": "မြင့်မြတ်သော အကျင့်", "anuggahāya": "ထောက်ပံ့ရန်", "purāṇañca": "ဟောင်းသော",
    "yātrā": "အသက်မွေးမှု", "anavajjatā": "အပြစ် မရှိမှု", "phāsu": "ချမ်းသာစွာ", "vihāro": "နေထိုင်မှု",
    "cāti": NONE,
    # mindfulness (1-1356 ff.)
    "muṭṭhasaccaṃ": "သတိလစ်ခြင်း", "asati": "သတိ မရှိခြင်း", "ananussati": "အဖန်ဖန် မအောက်မေ့ခြင်း",
    "anussati": "@alt", "appaṭissati": "ပြန်လည် မအောက်မေ့ခြင်း",
    "paṭissati": "ပြန်လည် အောက်မေ့ခြင်း", "saraṇatā": "မှတ်မိခြင်း", "dhāraṇatā": "စွဲမှတ်ထားခြင်း",
    "pilāpanatā": "အပေါ်ယံ ပေါ်လောခြင်း", "sammusanatā": "မေ့လျော့ခြင်း",
    "satindriyaṃ": "သတိ၏ စွမ်းရည်", "satibalaṃ": "သတိ၏ စွမ်းအား",
    "āsevanā": "အလေ့အကျင့် ပြုခြင်း", "bahulīkammaṃ": "အကြိမ်ကြိမ် ပြုခြင်း",
    "bojjhaṅgā": "သိမြင်ခြင်း၏ အင်္ဂါ",
    "ṭhiti": "တည်တံ့ခြင်း", "cittassa ṭhiti": "စိတ်၏ တည်တံ့ခြင်း", "nimittaṃ": "အမှတ်အသား",
    "cetasiko": "စိတ်ပိုင်းဆိုင်ရာ", "ārambho": "စတင်ခြင်း", "vāyāmo": "အားထုတ်မှု",
    "cetasiko vīriyārambho": "စိတ်ပိုင်းဆိုင်ရာ ဝီရိယ စတင်ခြင်း",
    "vītikkamo": "ကျူးလွန်ခြင်း", "dussilyaṃ": "သီလ ဖောက်ဖျက်မှု", "atthi": "ရှိသည်",
    "kammassakata": "ကံသာ မိမိ၏ ဥစ္စာ ဖြစ်ကြောင်း", "anulomika": "လျော်ညီသော", "phala": "ဖိုလ်",
    "padhānanti": "ကြိုးပမ်းအားထုတ်ခြင်း", "diṭṭhissa": "အယူ",
    "bhayaṃ": "ဘေး", "byādhi": "နာခြင်း", "maraṇa": "သေခြင်း", "saṃvejaniyaṃ": "သံဝေဂ ရဖွယ်", "ṭhānanti": "အခြေအနေ",
    "bhikkhu": "ရဟန်း", "uppannānaṃ": "ဖြစ်ပေါ်ပြီးသော", "anuppādāya": "မဖြစ်ပေါ်စေရန်",
    "chandaṃ": "ဆန္ဒ", "janeti": "ဖြစ်စေသည်", "vāyamati": "အားထုတ်သည်", "ārabhati": "စတင်သည်",
    "cittaṃ": "စိတ်", "paggaṇhāti": "မြှင့်တင်သည်", "cittaṃ paggaṇhāti": "စိတ်ကို မြှင့်တင်သည်",
    "padahati": "ကြိုးပမ်းသည်", "cittaṃ paggaṇhāti padahati": "စိတ်ကို မြှင့်တင်သည် ကြိုးပမ်းသည်",
    "pahānāya": "ပယ်ရန်", "asammosāya": "မပျောက်ပျက်ရန်", "vepullāya": "ပြန့်ပြောရန်", "pāripūriyā": "ပြည့်စုံရန်",
    "kusalesu dhammesūti": "ကုသိုလ် သဘောတရား",
    "kiriyatā": "ပြုခြင်း", "sakkacca": "ရိုသေစွာ", "sātacca": "အစဉ်တစိုက်", "ṭhita": "ရပ်တန့်ခြင်း",
    "olīna": "တွန့်ဆုတ်သော", "nikkhitta": "လက်လွှတ်သော", "chandatā": "ဆန္ဒ", "dhuratā": "ဝန်",
    "padhānasminti": "ကြိုးပမ်းအားထုတ်ခြင်း",
    "nivāsa": "ဘဝ", "sattānaṃ": "သတ္တဝါ", "cuti": "သေခြင်း", "upapāte": "ဖြစ်ပေါ်ခြင်း",
    "āsavānaṃ": "စိတ်အစွန်းအထင်း",
    "vimuttīti": "လွတ်မြောက်မှု", "vimuttiyo": "လွတ်မြောက်မှု", "adhimutti": "အလွန် လွတ်မြောက်မှု",
    "ñāṇanti": "ဉာဏ်", "niṭṭhitaṃ": "ပြီးဆုံးသော",
    # @END
}

NOT_YET = {   # a-X «not (yet) X» lists: the positive stem + «သော» (text «မ…သေးသော»; rule 8)
    "jātā": "မွေးဖွားသော", "bhūtā": "ဖြစ်သော", "sañjātā": "ကောင်းစွာ မွေးဖွားသော", "nibbattā": "ပေါ်ထွက်သော",
    "abhinibbattā": "ထင်ရှားစွာ ပေါ်ထွက်သော", "pātubhūtā": "ထင်ရှား လာသော", "uppannā": "ဖြစ်ပေါ်သော",
    "samuppannā": "ကောင်းစွာ ဖြစ်ပေါ်သော", "uṭṭhitā": "ထပေါ်သော", "samuṭṭhitā": "ကောင်းစွာ ထပေါ်သော",
}
CTX = {
    # sid: {keyword: value}
    "1-1042": NOT_YET, "1-1045": NOT_YET,
    "1-1024": {"sekkhā": "ကျင့်ကြံမှု"},                 # fragment of asekkhā «ကျင့်ကြံမှု ပြီးဆုံးသူ၏» (rule 8)
    "1-1043": {"yañca": NONE},                          # «yañca rūpaṃ … uppajjissati» = «… ဖြစ်ပေါ်လာမည့် ရုပ်လည်း»
    "1-1317": {"rūpaṃ": "ရုပ်ပိုင်း", "vuccati rūpaṃ": "ရုပ်ပိုင်းဟု ခေါ်သည်"},   # nāma / rūpa (sample rūpañca)
    "1-1376": {"saṃvego": "သံဝေဂ"},
    "1-1092": {"yo": "အကြင်"},                          # «Yo eva so dhammo» = «အကြင် သဘောတရားသည်» (as Yeva, 1-1091)
    "1-1101": {"na": "မဟုတ်",                           # «… သိနိုင်သည် မဟုတ်ကြ» (free na = «မဟုတ်», style rule)
               "dhammā cakkhu": "သဘောတရား … မျက်စိ", "dhammā sota": "သဘောတရား … နား",
               "dhammā ghāna": "သဘောတရား … နှာခေါင်း", "dhammā jivhā": "သဘောတရား … လျှာ",
               "dhammā kāya": "သဘောတရား … ကိုယ်"},     # «ye … dhammā cakkhuviññeyyā» = «သဘောတရားများသည် မျက်စိဖြင့် …»                     # the heading word «Saṃvegoti» = «သံဝေဂ ဟူသည်»
    "1-1355": {"santuṭṭhitā": "ရောင့်ရဲခြင်း"},          # positive noun of the text (1-1353 has «ရောင့်ရဲမှု မရှိခြင်း»)
    "1-1339": {"samāpatti": "ဈာန် ဝင်စားမှု"},          # «samāpattīhi» = «ဈာန် ဝင်စားမှုတို့မှ»
    "1-1344": {"hetū": "အကြောင်း"},                     # «hetū paccayā» = «အကြောင်း၊ အထောက်အပံ့»
    "1-1345": {"hetū": "အကြောင်း"},
}

# chapter -> its own table (looked up first); every table is also shared with the other chapters
SECTIONS = {
    "preamble": T_PREAMBLE,
    "1-matika": T_MATIKA,
    "4-01-nikkhepakandam": T_4,
    "4-02-nikkhepakandam": T_4,
    "4-03-nikkhepakandam": T_4,
}
CHAPTERS = ["4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam"]   # chapters written by this run

SAMPLE = dict(T_MATIKA)
SAMPLE.update(T_PREAMBLE)
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


NEW_RULES = """## New rules for the Nikkhepakaṇḍa (4-01, 4-02, 4-03), proposed for review

Rules 1-11 above are the approved sample rules, unchanged. The Nikkhepa answers bring constructions the Mātikā did
not have; each new rule says what it adds.

12. **Verbs other than finite** (absolutives, gerundives, finite verbs inside definitions): one form, verb + «သည်»
    (rule 4 extended to every verb keyword): ṭhapetvā (text «ချန်ထား၍») = ချန်ထားသည်; ārabbha («အာရုံပြု၍») =
    အာရုံပြုသည်; disvā = မြင်သည်; karitvā = ပြုသည်; uppajjanti («ဖြစ်ပေါ်ကြသော») = ဖြစ်ပေါ်သည်; Bhavissati
    («ဆက်လက် တည်ရှိလိမ့်မည်») = ဆက်လက် တည်ရှိသည်; two verbs in one keyword each take «သည်» (cittaṃ paggaṇhāti
    padahati = စိတ်ကို မြှင့်တင်သည် ကြိုးပမ်းသည်). A verb object inside the keyword keeps its text particle
    (Paritte dhamme ārabbha = အကန့်အသတ် ရှိသော သဘောတရားတို့ကို အာရုံပြုသည်). The check accepts «Xသည်» for the text's
    «X» + ၍ / ပြီး / ခြင်း / ရန် / သည့် / ကြ / ၊ / ဟူ / လိမ့်မည် / ။ (also after the negative: natthi, rakkhati in
    «မစောင့်ရှောက်၊» = the positive verb, rule 8).
13. **«vuccati X»** = «Xဟု ခေါ်သည်», the text's «ဤသည်ကို Xဟု ခေါ်သည်» without the frame's «ဤသည်ကို» (vuccati
    kāmāsavo = ကာမ စိတ်အစွန်းအထင်းဟု ခေါ်သည်). A keyword the extractor cut inside a compound keeps the cut:
    «vuccati abhijjhā kāya» = သူ့ဥစ္စာကို လိုချင်ခြင်းဟူသော ကိုယ် … ဟု ခေါ်သည်.
14. **Question frames**: «dhammā X» (the order of «Katame dhammā X?») = «X dhammā» (rule 5): dhammā kusalā = ကုသိုလ်
    သဘောတရား. «X-vippayuttā Y-iyā» without dhammā = «Xနှင့် ကင်းကွာသော … X၏ အာရုံ ဖြစ်နိုင်သော»: the text's «…
    သဘောတရားများအနက်» belongs to the left-out dhammā, so « … » marks the gap. «X ceva Y» (ca not in the keyword) =
    «Xလည်း ဖြစ် Yလည်း ဖြစ်နိုင်သော» (both … and: «၊» dropped, «လည်း» kept, as rule 6). «dhammā neva ācayagāmi» (cut
    before «na apacayagāmino») = စုပုံခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ် … သဘောတရား.
15. **Purpose datives** (-āya / -iyā: saṃvarāya, davāya, madāya, pahānāya, uppādāya, ṭhitiyā, pāripūriyā …) keep the
    text's purpose ending «…ရန်» (saṃvarāya = စောင့်စည်းရန်): the ending is the case meaning, as bahiddhā keeps ၌
    (rule 11); they are not nouns of rule 1.
16. **Attributive endings normalised to «သော»** (rule 3 extended): the verbal plural «…ကြသော» (uppajjanti
    cittacetasikā = ဖြစ်ပေါ်သော စိတ်နှင့် စိတ်၏ အဖော်), the negative conjunctive «မX-ဘဲ» (asaṃvutaṃ = မစောင့်စည်းသော),
    the coordinated clause «neither X၊ nor Y-သော» where X has no marker of its own (asaṃkiliṭṭha in 1-999, upādiṇṇa in
    1-996, rule 8: the positive part). The «not yet» list (1-1042 anuppannā, 1-1045 anāgatā: «မ…သေးသော») gives the
    fragments of ajātā … asamuṭṭhitā the positive stem + «သော» (jātā = မွေးဖွားသော); the same keywords in the «arisen»
    lists (1-1041, 1-1046) keep the text's «…ပြီးသော» (jātā = မွေးဖွားပြီးသော). The negative gerundive «ပယ်ရမည်
    မဟုတ်» counts for the approved «ပယ်ရမည့်» (check «attr-fut»).
17. **Relative pronouns** yo / yā / yaṃ / ye (any case) = (no direct equivalent): the Burmese builds the relative
    clause without a word for them. Where the text writes «အကြင်» that is the value (Yeva 1-1091, Yo 1-1092 =
    အကြင်; Ye ye 1-1344 = အကြင် အကြင်). Particles cāti = (no direct equivalent).
18. **Numerals** that are keywords keep the text's count: Dasa = ဆယ်ပါး, Dvādasa = ဆယ့်နှစ်ပါး, Aṭṭhārasa =
    ဆယ့်ရှစ်ပါး (as brief: «a keyword with a numeral keeps the count the text uses»).
19. **Loans and fragments without a Burmese part**: a fragment of a transliterated name is its part of the loan
    (paranimmitavasavattī: para = ပရ, nimmita = နိမ္မိတ, vasavattī = ဝသဝတ္တီ; sucaritaṃ: caritaṃ = စရိုက်); a fragment
    with nothing of its own in the text = (no direct equivalent): aṅgo (inside the loan ဗောဇ္ဈင်), caya (from
    apacaya; the text has only «လျော့ပါးခြင်း»). A Pāli word the text renders as one Burmese compound gives the
    compound to each part that has no separate word (sappurisānaṃ / purisānaṃ = သူတော်ကောင်း).
20. **Synonym lists** (lobha, dosa, moha, paññā, doubt, view, sati …): each keyword = its own item of the text's
    list, with the text's ending (ခြင်း / မှု / အဖြစ်); agent nouns keep «…သူ» (janikā = မွေးဖွားပေးတတ်သူ). The same
    sense with another ending of the same word in another list follows the segment: sineho ချစ်ခင်ခြင်း (lobha list) /
    ချစ်ခင်မှု (kāma and bhava lists); likewise nandī, mucchā, kamyatā (လိုချင်ခြင်း / ထူလိုခြင်း / လိုလားခြင်း),
    uppādāya (ဖြစ်ပေါ်ရန် / ဖြစ်ပေါ်စေရန်), khandhā (အစုအဝေး / အစု) (script: ALT, the first variant present).
21. **Sense by context** (rule 11 extended): rūpa / rūpaṃ = «အဆင်းအရောင်» (the visible object) in rūpāyatana,
    rūpadhātu and «cakkhunā rūpaṃ disvā», «ရုပ်ပိုင်း» in the nāma / rūpa pair (1-1317), «သိမ်မွေ့သော ရုပ်» in
    rūpāvacara also when capitalised (Rūpāvacarā), «ရုပ်» (matter) elsewhere; bahiddhā = «အပြင်ဘက်» in «ito bahiddhā»
    (outside this dispensation), «သူတစ်ပါး၌» elsewhere; dhamme = «တရားတော်» in the doubt list; dhamma = «တရား» in
    dhammamacchariya / dhammapaṭisanthāra; nāmaṃ = «အမည်» (adhivacana list) / «စိတ်ပိုင်း» (1-1316); kāyassa =
    «စိတ်၏ အဖော်» in the middha definition (the mental body, harmonise item 10) / «ကိုယ်ခန္ဓာ» in «imassa kāyassa»;
    kāyena = «ကိုယ်» (the body door); paṭigha = «မုန်းတီးမှု» (aversion: the fetter); sammā = «မှန်ကန်သော» in the right
    path factors, «မှန်ကန်စွာ» in sammaggatā / sammāpaṭipannā (sammāsambuddha keeps the sample's «အပြည့်အဝ»);
    sukha = «သာယာစွာ» in diṭṭhadhammasukhavihāra; niyatā = «သီးသန့် ဖြစ်သော» in the ajjhatta list (harmonise:
    kept); vibhava = «ဘဝ ပြတ်စဲခြင်း» in vibhavataṇhā; paccayā = «ကြောင့်» in the dependent-origination chain /
    «အထောက်အပံ့» in «hetū paccayā», where hetū = «အကြောင်း»; saddhā = «ယုံကြည်မှု» (fragment of assaddhā) /
    «ယုံကြည်မှု ရှိသော»; maggo = «လမ်း» in kummaggo; bhūtā = «မူလဓာတ်» (fragment of mahābhūtā) / «ဖြစ်ပြီးသော»;
    sacca = «အမှန်» (idaṃsaccābhinivesa) / «သစ္စာ» (saccānulomika); patho = «လမ်း» in dvedhāpatho; gāho =
    «ယူနိုင်ခြင်း» (fragment of anekaṃsaggāho); phalaṃ = «အသီးအပွင့်» in «kammānaṃ phalaṃ»; ñāṇaṃ = «သိခြင်း»
    (fragment of aññāṇaṃ); samāpatti = «ဈာန် ဝင်စားမှု» in 1-1339 (samāpattīhi); anussati = «အောက်မေ့နိုင်သော» in
    pubbenivāsānussati (1-1380); sekkhā (fragment of asekkhā, 1-1024) = «ကျင့်ကြံမှု».
22. **A free na the text renders by «မဟုတ်»** (1-1101: «… သိနိုင်သည် မဟုတ်ကြ») = «မဟုတ်» (style rule: free na =
    «… မဟုတ်»); the sample's prefix «မ» stays where the text has «မသိနိုင်သော». «dhammā cakkhu» (the cut of «dhammā
    cakkhuviññeyyā») = «သဘောတရား … မျက်စိ» (the subject and its sense door). The negative-infix check (rule 8) also
    accepts «X မY» with a space (dhāraṇatā in «စွဲမှတ် မထားခြင်း»).
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
    if len(ws) >= 2 and ws[0] == "vuccati":                            # «vuccati X» = «Xဟု ခေါ်သည်» (rule 4)
        base = lookup(ch, sid, " ".join(ws[1:]), pali, my)
        return base + "ဟု ခေါ်သည်"
    if len(ws) >= 2 and ws[0] == "dhammā" and ws[-1] != "dhammā":      # «dhammā X» (the 4-0x question order)
        ws = ws[1:] + ["dhammā"]
        k2 = " ".join(ws)
        v = table_get(SECTIONS.get(ch, {}), k2) or table_get(SHARED, k2)
        if v is not None:
            return resolve(v, k2, pali, my)
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
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ကြသော", "ဘဲ", "သေးသော")   # dictionary «Xသော» <- text «X»+one of these
VERB_FROM = ("ပါ၏", "၏", "ပြီ", "သော", "၍", "ပြီး", "ခြင်း", "ရန်", "သည့်", "ကြ", "၏။", "၊", "ဟူ", "လိမ့်မည်", "။")  # «Xသည်» <- text «X»+one of these


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
    if c.endswith("ည့်") and c[:-3] + "ည်" in text:     # «ပယ်ရမည့်» <- the negative «ပယ်ရမည် မဟုတ်»
        return "attr-fut"
    for i in range(1, len(c)):
        if c[:i] + "မ" + c[i:] in text or c[:i] + " မ" + c[i:] in text:
            return "neg-infix"
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        if st + "၊" in text:                       # «neither X၊ nor Y-သော»: X's marker comes after the last clause
            return "attr-clause"
        for i in range(0, len(st)):
            if (st[:i] + "မ" + st[i:]) + "၊" in text or any((st[:i] + "မ" + st[i:]) + e in text for e in ATTR_FROM):
                return "neg-attr"
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
    with open(HERE / "map-table-4.md", "w", encoding="utf-8") as f:
        f.write("# pi-1 Burmese keyword mapping: rules and review table (Dhammasaṅgaṇī, chapters "
                + ", ".join(CHAPTERS) + ")\n\n")
        f.write("Written by map_4.py. Burmese from the FINAL text of this track only "
                "(AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters). The approved sample rules 1-11 "
                "are repeated for reference; the new rules are 12-22.\n\n")
        f.write(RULES.replace("proposed for review", "approved with the sample (2026-11-17)"))
        f.write("\n" + NEW_RULES)
        f.write("\n## Presence: chunks matched by a dictionary-form rule (not literally in the segment)\n\n")
        f.write("Every other chunk of every value occurs literally in its segment's Burmese (particles that the "
                "rules strip follow the chunk in the text).\n\n| segment | keyword | chunk | rule |\n|---|---|---|---|\n")
        for sid, k, c, r in ruled_all:
            f.write(f"| {sid} | {k} | {c} | {r} |\n")
        f.write("\n## Keyword → Burmese (number of uses)\n\nSeveral values = the keyword reads differently by "
                "context. Source: «sample» = the approved preamble / 1-matika value (the same keyword keeps it), «new» = "
                "this table T_4 or a context rule, «composed» = rules 5 / 13 / 14 built from table values.\n\n"
                "| Pāli keyword | Burmese (uses) | source |\n|---|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            if table_get(T_4, kw) is not None:
                src = "new"
            elif table_get(SAMPLE, kw) is not None:
                src = "sample"
            else:
                src = "composed"
            f.write(f"| {kw} | " + " / ".join(f"{v} ({n})" for v, n in table[kw].most_common()) + f" | {src} |\n")


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
    if args and args[0] == "--review":
        # sid MY and mapping for the listed sids
        want = set(args[1:])
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            mapped = dict(l.split("] ", 1) for l in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines())
            for sid, kws in rows:
                if sid in want:
                    print(f"=== {sid}\nMY: {my[sid][:900]}\nMAP: {mapped['[' + sid]}\n")
        sys.exit()
    if args and args[0] == "--new":
        # print the segments (in order) that hold a keyword not mapped yet; each such keyword shown once
        seen = set()
        lim = int(args[1]) if len(args) > 1 else 40
        n = 0
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            for sid, kws in rows:
                new = []
                for kw in [k.strip() for k in kws.split(", ")]:
                    try:
                        lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                    except KeyError:
                        if kw not in seen:
                            new.append(kw)
                            seen.add(kw)
                if new:
                    print(f"=== {sid}\nPI: {pa.get(sid, '')}\nMY: {my[sid]}\nNEW: {', '.join(new)}\n")
                    n += 1
                    if n >= lim:
                        sys.exit()
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
