"""Pāli→Burmese keyword mapping for pi-1 chapter 2-01-cittuppadakandam (Dhammasaṅgaṇī, Cittuppādakaṇḍa).

usage (python3 -I -X utf8):
  map_2-01.py             writes 2-01-cittuppadakandam.mapped.md and map-table-2-01.md, then verifies
                          (keyword preservation, presence of every value chunk in its segment, no ", " / «၊»)
  map_2-01.py --report    writes nothing; lists unmapped keywords, presence failures, values from the sample tables
  map_2-01.py --seg ID    prints Pāli, Burmese, keywords and mapping of one segment

A copy (not an import) of the approved sample mapper map_all.py: its tables T_PREAMBLE / T_MATIKA, compose rules,
context functions and verifier, plus this chapter's table T_CU and the new rules 12-22 (RULES below). Burmese from the
FINAL text of this track only (AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters); no other Burmese
source. map_all.py, map-table.md and the sample outputs are not touched.
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
# 2-01 Cittuppādakaṇḍa (the eight kāmāvacara kusala cittas): values from THIS chapter's Burmese
# =====================================================================================================
_KAYA = "စိတ်၏ အဖော်တို့"          # kāya- (the mental body; approved term kept whole, rule 18)
_SAMAYE = "အချိန်၌ ရှိသော"          # «samaye X» bigrams (rule 13)

T_CU = {
    # --- headings, colophons
    "uppāda": "ဖြစ်ပေါ်ခြင်း", "cittuppāda": "စိတ် ဖြစ်ပေါ်ခြင်း", "kaṇḍaṃ": "အခန်း", "citta": "စိတ်",
    "kusalaṃ": "ကုသိုလ်", "kāma": "ကာမ", "kāmāvacara": "ကာမဘုံနှင့် ဆိုင်သော", "avacara": "ဘုံနှင့် ဆိုင်သော",
    "bhājanī": "ခွဲခြမ်း ဖော်ပြချက်", "bhājanīyaṃ": "ခွဲခြမ်း ဖော်ပြချက်",
    "koṭṭhāsa": "အစုအပိုင်း", "suññata": "ဆိတ်သုဉ်းကြောင်း", "vāro": "@vara", "bhāṇa": "ရွတ်ဖတ်ရန်",
    "pañcamaṃ": "ပဉ္စမ", "chaṭṭhaṃ": "ဆဋ္ဌမ", "sattamaṃ": "သတ္တမ", "aṭṭhamaṃ": "အဋ္ဌမ",
    "cittāni": "စိတ်",
    # --- the opening «Katame dhammā kusalā? Yasmiṃ samaye …»
    "dhammā kusalā": "ကုသိုလ် သဘောတရား", "kusalā": "ကုသိုလ်",
    "kāmāvacaraṃ": "ကာမဘုံနှင့် ဆိုင်သော", "avacaraṃ": "ဘုံနှင့် ဆိုင်သော",
    "kusalaṃ cittaṃ": "ကုသိုလ်စိတ်", "uppannaṃ": "ဖြစ်ပေါ်လာသော",
    "sahagataṃ": "အတူ ဖြစ်သော", "somanassasahagataṃ": "ဝမ်းမြောက်မှုနှင့်အတူ ဖြစ်သော",
    "upekkhāsahagataṃ": "ဥပေက္ခာနှင့်အတူ ဖြစ်သော",
    "sampayuttaṃ": "ယှဉ်တွဲသော", "vippayuttaṃ": "ကင်းကွာသော", "ñāṇavippayuttaṃ": "ဉာဏ်နှင့် ကင်းကွာသော",
    "ñāṇa": "ဉာဏ်", "somanassa": "ဝမ်းမြောက်မှု", "upekkhā": "ဥပေက္ခာ",
    "saṅkhārena": "တိုက်တွန်းမှု",
    "rūpa": "@rupa", "sadda": "အသံ", "gandha": "အနံ့", "rasa": "အရသာ", "phoṭṭhabba": "အထိအတွေ့",
    "dhamma": DH, "ārammaṇaṃ": "အာရုံ", "yaṃ yaṃ": "မည်သည့်အရာ", "ārabbha": "အာရုံပြု၍",
    # --- «ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā» (rule 20)
    "ye": "ရှိသမျှ", "paṭicca": "အကြောင်းတို့ကို မှီ၍", "samuppannā": "ဖြစ်ပေါ်လာသော",
    "paṭiccasamuppannā": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော",
    "paṭiccasamuppannā arūpino": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော",
    "samuppannā arūpino": "ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော",
    "samuppannā arūpino dhammā": "ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော … " + DH,
    "arūpino": "ရုပ် မဟုတ်သော", "arūpino dhammā": "ရုပ် မဟုတ်သော … " + DH,
    "arūpīnaṃ": "ရုပ် မဟုတ်သော", "arūpīnaṃ dhammānaṃ": "ရုပ် မဟုတ်သော " + DH,
    "ṭhapetvā": "ချန်ထား၍",
    # --- relative pronouns of the definitions (rule 12)
    "yo": NONE, "yā": NONE, "yaṃ": NONE,
    # --- factor names (the 1-1 list), dictionary form
    "phasso": "တွေ့ထိမှု", "phassa": "တွေ့ထိမှု", "vedanā": "ခံစားမှု", "saññā": "မှတ်သိမှု",
    "cetanā": "စေ့ဆော်မှု", "cittaṃ": "စိတ်", "cittassa": "စိတ်",
    "vitakko": "စတင်ကြံစည်မှု", "vicāro": "ဆက်လက်သုံးသပ်မှု", "pīti": "ပီတိ", "sukhaṃ": "သာယာမှု",
    "ekaggatā": "စူးစိုက်မှု", "cittassekaggatā": "စိတ်၏ စူးစိုက်မှု",
    "indriyaṃ": "စွမ်းရည်", "indriyāni": "စွမ်းရည်", "balaṃ": "စွမ်းအား", "balāni": "စွမ်းအား",
    "saddhā": "ယုံကြည်မှု", "sati": "သတိ", "samādhi": "သမာဓိ", "paññā": "ပညာ", "mana": "မနော", "mano": "မနော",
    "jīvita": "အသက်", "hiri": "ဒုစရိုက်ကို ရှက်မှု", "hirī": "ဒုစရိုက်ကို ရှက်မှု",
    "ottappa": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု", "ottappaṃ": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု",
    "saddhindriyaṃ": "ယုံကြည်မှု၏ စွမ်းရည်", "vīriyindriyaṃ": "ဝီရိယ၏ စွမ်းရည်", "satindriyaṃ": "သတိ၏ စွမ်းရည်",
    "samādhindriyaṃ": "သမာဓိ၏ စွမ်းရည်", "paññindriyaṃ": "ပညာ၏ စွမ်းရည်", "manindriyaṃ": "မနော၏ စွမ်းရည်",
    "somanassindriyaṃ": "ဝမ်းမြောက်မှု၏ စွမ်းရည်", "jīvitindriyaṃ": "အသက်၏ စွမ်းရည်",
    "upekkhindriyaṃ": "ဥပေက္ခာ၏ စွမ်းရည်",
    "sammā": "မှန်ကန်သော", "diṭṭhi": "အယူ", "saṅkappo": "ကြံစည်မှု", "vāyāmo": "အားထုတ်မှု",
    "saddhābalaṃ": "ယုံကြည်မှု၏ စွမ်းအား", "vīriyabalaṃ": "ဝီရိယ၏ စွမ်းအား", "satibalaṃ": "သတိ၏ စွမ်းအား",
    "samādhibalaṃ": "သမာဓိ၏ စွမ်းအား", "paññābalaṃ": "ပညာ၏ စွမ်းအား",
    "hiribalaṃ": "ဒုစရိုက်ကို ရှက်မှု၏ စွမ်းအား", "ottappabalaṃ": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု၏ စွမ်းအား",
    "alobho": "လောဘ မရှိခြင်း", "adoso": "ဒေါသ မရှိခြင်း", "amoho": "မောဟ မရှိခြင်း",
    "anabhijjhā": "သူ့ဥစ္စာကို မလိုချင်ခြင်း", "abyāpādo": "ဖျက်ဆီးလိုစိတ် မရှိခြင်း",
    "kāya": _KAYA,
    "passaddhi": "ငြိမ်းအေးခြင်း", "cittapassaddhi": "စိတ် ငြိမ်းအေးခြင်း",
    "lahutā": "ပေါ့ပါးခြင်း", "cittalahutā": "စိတ် ပေါ့ပါးခြင်း",
    "mudutā": "ပျော့ပျောင်းခြင်း", "cittamudutā": "စိတ် ပျော့ပျောင်းခြင်း",
    "kammaññatā": "အသုံးပြုရန် သင့်တော်ခြင်း", "cittakammaññatā": "စိတ် အသုံးပြုရန် သင့်တော်ခြင်း",
    "pāguññatā": "ကျင့်သားရခြင်း", "cittapāguññatā": "စိတ် ကျင့်သားရခြင်း",
    "ujukatā": "ဖြောင့်တန်းခြင်း", "cittujukatā": "စိတ် ဖြောင့်တန်းခြင်း",
    "sampajaññaṃ": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း", "samatho": "စိတ်ငြိမ်သက်ခြင်း",
    "vipassanā": "ထိုးထွင်းသိမြင်ခြင်း", "paggāho": "စိတ်ကို မြှင့်တင်ခြင်း", "avikkhepo": "စိတ် မပျံ့လွင့်ခြင်း",
    # --- phassa, vedanā, saññā, cetanā (1-2 … 1-5, 1-10, 1-152 …)
    "phusanā": "ထိခြင်း", "saṃphusanā": "တွေ့ထိခြင်း",
    "tajjā": "သက်ဆိုင်ရာ", "dhātu": "ဓာတ်", "dhātuyo": "ဓာတ်",
    "manoviññāṇa": "မနော သိစိတ်", "manoviññāṇadhātu": "မနော သိစိတ် ဓာတ်",
    "samphassajaṃ": "တွေ့ထိမှုမှ ဖြစ်ပေါ်သော", "samphassajā": "တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "cetosamphassajaṃ": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော", "cetosamphassajā": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "cetasikaṃ": "စိတ်ပိုင်းဆိုင်ရာ", "sātaṃ": "@sata", "asātaṃ": "နှစ်သက်ဖွယ် မကောင်းသော",
    "cetasikaṃ sātaṃ": "စိတ်ပိုင်းဆိုင်ရာ နှစ်သက်ဖွယ်ကောင်းမှု", "cetasikaṃ sukhaṃ": "စိတ်ပိုင်းဆိုင်ရာ သာယာမှု",
    "vedayitaṃ": "ခံစားရခြင်း", "sukhā": "သာယာသော",
    "sukhaṃ vedayitaṃ": "သာယာသော ခံစားရခြင်း", "sukhā vedanā": "သာယာသော ခံစားမှု",
    "adukkhamasukhaṃ": "မနာကျင် မသာယာသော",
    "cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မနာကျင် မသာယာသော ခံစားရခြင်း",
    "cetosamphassajā adukkhamasukhā vedanā": "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော မနာကျင် မသာယာသော ခံစားမှု",
    "sañjānanā": "မှတ်သိခြင်း", "sañjānitattaṃ": "မှတ်သိထားသော အဖြစ်",
    "sañcetanā": "စေ့ဆော်ခြင်း", "cetayitattaṃ": "စေ့ဆော်ထားသော အဖြစ်",
    # --- citta (1-6 …)
    "mānasaṃ": "စိတ်နှလုံး", "hadayaṃ": "နှလုံးသား", "paṇḍaraṃ": "ကြည်လင်သောအရာ",
    "manāyatanaṃ": "မနော အာရုံခံ နယ်ပယ်", "viññāṇaṃ": "သိစိတ်", "viññāṇa": "သိစိတ်",
    "khandho": "အစုအဝေး", "khandhā": "အစုအဝေး", "khandhassa": "အစုအဝေး",
    "viññāṇakkhandho": "သိစိတ် အစုအဝေး", "viññāṇakkhandhaṃ": "သိစိတ် အစုအဝေး", "viññāṇakkhandhassa": "သိစိတ် အစုအဝေး",
    "vedanākkhandho": "ခံစားမှု အစုအဝေး", "vedanākkhandhaṃ": "ခံစားမှု အစုအဝေး", "vedanākkhandhassa": "ခံစားမှု အစုအဝေး",
    "saññākkhandho": "မှတ်သိမှု အစုအဝေး", "saññākkhandhaṃ": "မှတ်သိမှု အစုအဝေး", "saññākkhandhassa": "မှတ်သိမှု အစုအဝေး",
    "saṅkhāra": "ပြုပြင်ဖန်တီးမှု", "saṅkhārakkhandho": "ပြုပြင်ဖန်တီးမှု အစုအဝေး",
    "saṅkhārakkhandhassa": "ပြုပြင်ဖန်တီးမှု အစုအဝေး",
    # --- vitakka, vicāra, pīti (1-7 … 1-9)
    "takko": "တွေးတောခြင်း", "appanā": "အာရုံ၌ စိတ်ကို သွင်းခြင်း", "cetaso": "စိတ်",
    "abhiniropanā": "အာရုံသို့ တင်ပို့ခြင်း",
    "cāro": "သုံးသပ်ခြင်း", "anusandhānatā": "အာရုံနှင့် ဆက်စပ်ထားခြင်း",
    "anupekkhanatā": "အာရုံကို စေ့စေ့ ရှုကြည့်ခြင်း",
    "pāmojjaṃ": "ရွှင်လန်းခြင်း", "āmodanā": "ဝမ်းသာခြင်း", "pamodanā": "အလွန် ဝမ်းသာခြင်း",
    "hāso": "ပြုံးရွှင်ခြင်း", "pahāso": "အလွန် ပြုံးရွှင်ခြင်း", "vitti": "ကျေနပ်ခြင်း",
    "odagyaṃ": "စိတ်တက်ကြွခြင်း", "attamanatā": "နှစ်သိမ့်ခြင်း",
    # --- ekaggatā / samādhi (1-11 …)
    "ṭhiti": "တည်တံ့ခြင်း", "cittassa ṭhiti": "စိတ်၏ တည်တံ့ခြင်း", "saṇṭhiti": "ကောင်းစွာ တည်တံ့ခြင်း",
    "avaṭṭhiti": "ခိုင်မြဲစွာ တည်တံ့ခြင်း", "avisāhāro": "မပြန့်ကျဲခြင်း", "avisāhaṭa": "မပြန့်ကျဲသော",
    "mānasatā": "စိတ် … အဖြစ်", "avisāhaṭamānasatā": "စိတ် မပြန့်ကျဲသော အဖြစ်",
    # --- saddhā (1-12 …)
    "saddahanā": "ယုံကြည်ခြင်း", "okappanā": "စိတ်ချ အားကိုးခြင်း", "abhippasādo": "ကြည်ညိုလေးစားခြင်း",
    # --- vīriya (1-13 …)
    "cetasiko": "စိတ်ပိုင်းဆိုင်ရာ", "cetasiko vīriyārambho": "စိတ်ပိုင်းဆိုင်ရာ ဝီရိယ စတင်ခြင်း",
    "ārambho": "စတင်ခြင်း", "nikkamo": "ရှေ့သို့ တိုးထွက်ခြင်း", "parakkamo": "ရဲရင့်စွာ ကြိုးစားခြင်း",
    "uyyāmo": "ထကြွ ကြိုးစားခြင်း", "ussāho": "စိတ်အားထက်သန်မှု", "ussoḷhī": "ပြင်းပြသော အားမာန်",
    "thāmo": "ခွန်အား", "dhiti": "ဇွဲ", "asithila": "မလျော့ရဲသော",
    "nikkhitta": "လက်လွှတ်သော / ချထားသော", "chandatā": "ဆန္ဒ", "dhuratā": "ဝန်",
    "sampaggāho": "ခိုင်မြဲစွာ ထမ်းဆောင်ခြင်း",
    # --- sati (1-14 …)
    "anussati": "အဖန်ဖန် အောက်မေ့ခြင်း", "paṭissati": "ပြန်လည် အောက်မေ့ခြင်း", "saraṇatā": "မှတ်မိခြင်း",
    "dhāraṇatā": "စွဲမှတ်ထားခြင်း", "pilāpanatā": "အပေါ်ယံ ပေါ်လောခြင်း", "sammussanatā": "မေ့လျော့ခြင်း",
    # --- paññā (1-16 …)
    "pajānanā": "ကွဲပြားစွာ သိခြင်း", "vicayo": "စိစစ်ခြင်း", "pavicayo": "သေချာစွာ စိစစ်ခြင်း",
    "dhammavicayo": "သဘောတရားများကို စိစစ်ခြင်း",
    "sallakkhaṇā": "လက္ခဏာကို ကောင်းစွာ ခွဲခြားခြင်း", "upalakkhaṇā": "လက္ခဏာကို အနီးကပ် ခွဲခြားခြင်း",
    "paccupalakkhaṇā": "လက္ခဏာကို အသီးသီး ခွဲခြားခြင်း",
    "paṇḍiccaṃ": "လိမ္မာခြင်း", "kosallaṃ": "ကျွမ်းကျင်ခြင်း", "nepuññaṃ": "နက်နဲသိမ်မွေ့ခြင်း",
    "vebhabyā": "ခွဲခြမ်းစိတ်ဖြာခြင်း", "cintā": "စဉ်းစားခြင်း", "upaparikkhā": "စူးစမ်းဆန်းစစ်ခြင်း",
    "bhūrī": "ကျယ်ပြန့်ခြင်း", "medhā": "ဉာဏ်ထက်မြက်ခြင်း", "pariṇāyikā": "လမ်းပြခြင်း", "patodo": "နှင်တံ",
    "satthaṃ": "ဓား", "paññāsatthaṃ": "ပညာ ဓား", "pāsādo": "ပြာသာဒ်", "paññāpāsādo": "ပညာ ပြာသာဒ်",
    "āloko": "အလင်း", "paññāāloko": "ပညာ အလင်း", "obhāso": "အရောင်အဝါ", "paññāobhāso": "ပညာ အရောင်အဝါ",
    "pajjoto": "မီးအိမ်", "paññāpajjoto": "ပညာ မီးအိမ်", "ratanaṃ": "ရတနာ", "paññāratanaṃ": "ပညာ ရတနာ",
    # --- jīvita (1-19 …)
    "āyu": "သက်တမ်း", "yapanā": "ဆက်လက် ဖြစ်နေခြင်း", "yāpanā": "ဆက်လက် ရှင်သန်စေခြင်း",
    "iriyanā": "လှုပ်ရှားခြင်း", "vattanā": "လည်ပတ်ခြင်း", "pālanā": "စောင့်ရှောက်ခြင်း",
    # --- hiri, ottappa (1-30 …)
    "hirīyati": "ရှက်သည်", "ottappati": "ကြောက်ရွံ့သည်",
    "pāpakānaṃ": "ယုတ်မာသော", "akusalānaṃ": "အကုသိုလ်", "akusalānaṃ dhammānaṃ": "အကုသိုလ် " + DH,
    "samāpattiyā": "ကျူးလွန်ခြင်း",
    # --- alobha, adosa (1-32 …)
    "lubbhanā": "မက်မောခြင်း", "asārāgo": "မတပ်မက်ခြင်း", "sārajjanā": "စွဲမက်ခြင်း",
    "kusala": "ကုသိုလ်", "mūlaṃ": "အမြစ်", "kusalamūlaṃ": "ကုသိုလ်၏ အမြစ်",
    "dussanā": "စိတ်ဆိုးခြင်း", "abyāpajjo": "မညှဉ်းဆဲလိုခြင်း", "byāpajjo": "ညှဉ်းဆဲလိုခြင်း",
    # --- the six pairs (1-40 … 1-51)
    "passambhanā": "အေးချမ်းခြင်း", "passambhitattaṃ": "အေးချမ်းသွားသော အဖြစ်",
    "paṭipassambhitattaṃ": "လုံးဝ အေးချမ်းသွားသော အဖြစ်",
    "lahu": "လျင်မြန်စွာ", "adandhanatā": "မနှေးကွေးခြင်း", "dandhanatā": "နှေးကွေးခြင်း",
    "vitthanatā": "တုံ့ဆိုင်းခြင်း",
    "maddavatā": "နူးညံ့သော အဖြစ်", "akakkhaḷatā": "မကြမ်းတမ်းခြင်း", "kakkhaḷatā": "ကြမ်းတမ်းခြင်း",
    "kathinatā": "မာကျောခြင်း",
    "kammaññattaṃ": "အသုံးပြုရန် သင့်တော်သော အဖြစ်", "bhāvo": "သဘော",
    "paguṇattaṃ": "ကျင့်သားရသော အဖြစ်",
    "ujutā": "ဖြောင့်ခြင်း", "ajimhatā": "မကောက်ကွေးခြင်း", "jimhatā": "ကောက်ကွေးခြင်း",
    "vaṅkatā": "ကွေးညွှတ်ခြင်း", "kuṭilatā": "လိမ်ကောက်ခြင်း",
    # --- Koṭṭhāsavāra / Suññatavāra (1-58 …)
    "āyatanāni": "အာရုံခံ နယ်ပယ်", "dhammāyatanaṃ": DH + " အာရုံခံ နယ်ပယ်", "dhammadhātu": DH + " ဓာတ်",
    "āhāro": "အာဟာရ", "āhārā": "အာဟာရ", "manosañcetanā": "မနော၏ စေ့ဆော်ခြင်း",
    "jhānaṃ": "ဈာန်", "maggo": "မဂ်", "hetū": "အမြစ်",
    "pañcaṅgikaṃ": "အင်္ဂါ ငါးပါး ရှိသော", "pañcaṅgiko": "အင်္ဂါ ငါးပါး ရှိသော",
    "caturaṅgikaṃ": "အင်္ဂါ လေးပါး ရှိသော", "caturaṅgiko": "အင်္ဂါ လေးပါး ရှိသော",
    "caturaṅgiko maggo": "အင်္ဂါ လေးပါး ရှိသော မဂ်",
}


# =====================================================================================================
# context functions and per-segment overrides
# =====================================================================================================
def f_rupa(kw, pali, my):
    """rūpa in rūpāvacara = the fine-material plane «သိမ်မွေ့သော ရုပ်» (sample); in rūpārammaṇa = the visible
    object «အဆင်းအရောင်» (2-01); elsewhere matter «ရုပ်»."""
    if re.search(r"(?<![aA])rūpāvacar|rūpūpapatti|rūparāga", pali):
        return "သိမ်မွေ့သော ရုပ်"
    if "rūpārammaṇ" in pali:
        return "အဆင်းအရောင်"
    return "ရုပ်"


def f_vara(kw, pali, my):
    """-vāra: «bhāṇavāro» = recitation section «အပိုင်း»; Koṭṭhāsa- / Suññatavāro = exposition «ဖော်ပြချက်»."""
    if "bhāṇavāro" in pali and not re.search(r"(Koṭṭhāsa|Suññata)vāro", pali):
        return "အပိုင်း"
    return "ဖော်ပြချက်"


def f_sata(kw, pali, my):
    """sātaṃ: the noun «နှစ်သက်ဖွယ်ကောင်းမှု» of «cetasikaṃ sātaṃ» (sukha lists); in «neva sātaṃ nāsātaṃ» the
    text builds the attributive «နှစ်သက်ဖွယ်ကောင်းသည်လည်း မဟုတ်» -> «နှစ်သက်ဖွယ်ကောင်းသော»."""
    if "neva sātaṃ" in pali:
        return "နှစ်သက်ဖွယ်ကောင်းသော"
    return "နှစ်သက်ဖွယ်ကောင်းမှု"


FUNCS = {"rupa": f_rupa, "vara": f_vara, "sata": f_sata}

CTX = {
    # sid: {keyword: value}   (none needed: every 2-01 segment type is covered by T_CU and the functions)
}

# chapter -> its own table (looked up first); every table is also shared with the other chapters
SECTIONS = {
    "preamble": T_PREAMBLE,
    "1-matika": T_MATIKA,
    "2-01-cittuppadakandam": T_CU,
}
CHAPTERS = ["2-01-cittuppadakandam"]   # chapters written by this script

SHARED = {}
for _t in SECTIONS.values():
    for _k, _v in _t.items():
        SHARED.setdefault(_k, _v)


# =====================================================================================================
# new dictionary-form rules for 2-01 (written to map-table-2-01.md; rules 1-11 of map-table.md apply)
# =====================================================================================================
RULES = """## New dictionary-form rules for 2-01 (rules 1–11 of map-table.md, approved, apply unchanged)

12. **Relative pronouns** of the definitions («Yo / Yā / Yaṃ tasmiṃ samaye A B C –»): Burmese has no relative
    pronoun; the text builds the relative clause with the attributive «ထိုအချိန်၌ ရှိသော A၊ B၊ C», so Yo / Yā / Yaṃ =
    (no direct equivalent). **ye / Ye** of «ye vā pana tasmiṃ samaye aññepi atthi …» is rendered by a word: the text's
    «… သဘောတရားများ ရှိသမျှလည်း» («whatever there are»), so ye = ရှိသမျှ («လည်း» = vā pana is not the keyword).
    yaṃ yaṃ (of «yaṃ yaṃ vā panārabbha») = မည်သည့်အရာ (text «မည်သည့်အရာကို»).
13. **«samaye X» bigrams** (from «tasmiṃ samaye X»: samaye phasso, samaye cittaṃ, samaye paññā …) = «အချိန်၌ ရှိသော X»:
    the time adverb keeps its locative ၌ (its meaning, as bahiddhā in rule 11), the attributive ရှိသော with which the
    text joins it to X stays (inside the value, rule 1), and ထို (tasmiṃ, not in the keyword) goes. X has its own value.
14. **Absolutives** (indeclinable gerunds) keep the text's conjunctive «၍»: ārabbha = အာရုံပြု၍, ṭhapetvā =
    ချန်ထား၍, paṭicca = အကြောင်းတို့ကို မှီ၍ (with the object «အကြောင်းတို့ကို» by which the text renders
    «depending [on conditions]»).
15. **Finite verbs** that the text renders by a verbal noun keep rule 4 (verb + «သည်»): hirīyati («ရှက်ခြင်း») =
    ရှက်သည်, ottappati («ကြောက်ရွံ့ခြင်း») = ကြောက်ရွံ့သည်. The check accepts «…ခြင်း» for «…သည်».
16. **Synonym lists**: each Pāli synonym = the Burmese item at its position in the definition line (as the 2-01
    synonym table of my_formulas.py places them), in the form the text gives it (…ခြင်း / …မှု / …သော အဖြစ် /
    …သော သဘော / noun). A keyword that is a part of a compound item = the part of the item that renders it:
    ārambho (vīriyārambho) = စတင်ခြင်း, chandatā = ဆန္ဒ, dhuratā = ဝန်, sampaggāho (dhurasampaggāho) = ခိုင်မြဲစွာ
    ထမ်းဆောင်ခြင်း, satthaṃ / pāsādo / āloko / obhāso / pajjoto / ratanaṃ (paññā-X) = ဓား / ပြာသာဒ် / အလင်း /
    အရောင်အဝါ / မီးအိမ် / ရတနာ, bhāvo (kammañña- / paguṇabhāvo) = သဘော, lahu (lahupariṇāmatā) = လျင်မြန်စွာ (the
    adverb as the text builds it), passambhitattaṃ (paṭipassambhitattaṃ) = အေးချမ်းသွားသော အဖြစ်, abhiniropanā
    (cetaso abhiniropanā) = အာရုံသို့ တင်ပို့ခြင်း (cetaso = စိတ်, its ကို goes with it), anusandhānatā (cittassa
    anusandhānatā) = အာရုံနှင့် ဆက်စပ်ထားခြင်း, attamanatā (attamanatā cittassa) = နှစ်သိမ့်ခြင်း; mānasatā
    (avisāhaṭamānasatā = «စိတ် မပြန့်ကျဲသော အဖြစ်») is discontinuous: စိတ် … အဖြစ်. cittassa alone = စိတ် (rule 1).
17. **Fragments without their negative prefix** (rule 8 extended) = the positive part: lubbhanā = မက်မောခြင်း
    (alubbhanā), sārajjanā = စွဲမက်ခြင်း, dussanā = စိတ်ဆိုးခြင်း (adussanā «စိတ်မဆိုးခြင်း»: infixed မ), byāpajjo =
    ညှဉ်းဆဲလိုခြင်း, dandhanatā = နှေးကွေးခြင်း, vitthanatā = တုံ့ဆိုင်းခြင်း, kakkhaḷatā = ကြမ်းတမ်းခြင်း, kathinatā =
    မာကျောခြင်း, jimhatā = ကောက်ကွေးခြင်း, vaṅkatā = ကွေးညွှတ်ခြင်း, kuṭilatā = လိမ်ကောက်ခြင်း, pilāpanatā =
    အပေါ်ယံ ပေါ်လောခြင်း, sammussanatā = မေ့လျော့ခြင်း. The participle **nikkhitta** (anikkhitta-chandatā /
    -dhuratā: «ဆန္ဒကို လက်မလွှတ်ခြင်း», «ဝန်ကို မချထားခြင်း») = လက်လွှတ်သော / ချထားသော (two compounds, two
    Burmese verbs: genuine alternatives, rule 3 «…သော»); **asithila** («မလျော့ရဲဘဲ ကြိုးစားခြင်း») = မလျော့ရဲသော
    (the negative conjunctive «…ဘဲ» normalised to «…သော», as «…၍» in rule 3). The check accepts «ဘဲ» among the
    attributive sources and an infixed မ inside an attributive stem.
18. **kāya** (kāyapassaddhi … kāyujukatā) = စိတ်၏ အဖော်တို့: the approved term for the mental «body» (the feeling,
    perception and formation aggregates, as the text defines it) kept whole; its «တို့» marks the group and keeps it
    apart from cetasika «စိတ်၏ အဖော်» (the one exception to rule 1's dropped plural marker; for review).
19. **Sense by context** (rule 11 extended): rūpa in rūpārammaṇa = the visible object «အဆင်းအရောင်» (sadda / gandha /
    rasa / phoṭṭhabba = အသံ / အနံ့ / အရသာ / အထိအတွေ့; dhamma(-ārammaṇa / -āyatana / -dhātu) = သဘောတရား);
    sātaṃ = the noun «နှစ်သက်ဖွယ်ကောင်းမှု» in the sukha lists («cetasikaṃ sātaṃ»), the attributive
    «နှစ်သက်ဖွယ်ကောင်းသော» in «neva sātaṃ nāsātaṃ» (text «…ကောင်းသည်လည်း မဟုတ်»; asātaṃ = နှစ်သက်ဖွယ်
    မကောင်းသော); -vāro = «ဖော်ပြချက်» (Koṭṭhāsa- / Suññatavāro: exposition) but «အပိုင်း» in bhāṇavāro (recitation
    section; bhāṇa = ရွတ်ဖတ်ရန်); sammā- = မှန်ကန်သော (right: sammādiṭṭhi …; the preamble's «အပြည့်အဝ» belongs to
    sammāsambuddha).
20. **«ye vā pana … aññepi atthi paṭiccasamuppannā arūpino dhammā»**: the text puts «အခြား» (aññe, not a keyword)
    between the attributes and the noun, so arūpino dhammā = ရုပ် မဟုတ်သော … သဘောတရား and samuppannā arūpino dhammā =
    ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော … သဘောတရား (rule 10); arūpino = ရုပ် မဟုတ်သော (the Mātikā value); the contiguous
    arūpīnaṃ dhammānaṃ («ထို ရုပ် မဟုတ်သော သဘောတရားတို့၏») = ရုပ် မဟုတ်သော သဘောတရား (the Mātikā value).
21. **Counts and ordinals**: a keyword with a numeral keeps the text's count (pañcaṅgikaṃ = အင်္ဂါ ငါးပါး ရှိသော,
    caturaṅgiko maggo = အင်္ဂါ လေးပါး ရှိသော မဂ်); a plural without numeral is the bare noun (khandhā, indriyāni,
    balāni, āhārā, dhātuyo, āyatanāni, cittāni); ordinals as the text: Pañcamaṃ … Aṭṭhamaṃ = ပဉ္စမ … အဋ္ဌမ.
22. **Headings**: uppāda = ဖြစ်ပေါ်ခြင်း, Cittuppāda = စိတ် ဖြစ်ပေါ်ခြင်း, kaṇḍaṃ = အခန်း; bhājanī / bhājanīyaṃ
    (Padabhājanī) = ခွဲခြမ်း ဖော်ပြချက် (pada «ပုဒ်အလိုက်» is not in the keyword); Koṭṭhāsa = အစုအပိုင်း (the
    postposition «အလိုက်», «by», goes: rule 1); Suññata = ဆိတ်သုဉ်းကြောင်း (the text's nominal form).
"""


# =====================================================================================================
# engine (copied from map_all.py; lookup adds the «samaye X» compose, presence adds rules 15 and 17)
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


SOURCE = {}   # (ch, kw) -> where the value came from: ctx / own / samaye / shared / dhammā


def lookup(ch, sid, kw, pali, my):
    o = CTX.get(sid, {})
    v, src = table_get(o, kw), "ctx"
    if v is None:
        v, src = table_get(SECTIONS.get(ch, {}), kw), "own"
    ws = kw.split()
    if v is None and len(ws) == 2 and ws[0] == "samaye":          # rule 13
        base = table_get(SECTIONS.get(ch, {}), ws[1])
        base = resolve(base, ws[1], pali, my)
        if base and base != NONE:
            v, src = _SAMAYE + " " + base, "samaye"
    if v is None:
        v, src = table_get(SHARED, kw), "shared"
    if v is not None:
        SOURCE[(ch, kw)] = src
        return resolve(v, kw, pali, my)
    if len(ws) >= 2 and ws[-1] == "dhammā":
        neg = ws[0] in ("no", "na")
        core = " ".join(ws[1:-1] if neg else ws[:-1])
        base = table_get(SECTIONS.get(ch, {}), core) or table_get(SHARED, core)
        base = resolve(base, core, pali, my)
        if base:
            if neg:
                base = neg_attr(base)
            if base:
                SOURCE[(ch, kw)] = "dhammā"
                return base + " " + DH
    raise KeyError(kw)


# ---- presence check --------------------------------------------------------------------------------
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ဘဲ")   # «Xသော» <- text «X»+one of these (+ဘဲ: rule 17)
VERB_FROM = ("ပါ၏", "၏", "ပြီ", "သော", "ခြင်း")                       # «Xသည်» <- text «X»+one of these (+ခြင်း: rule 15)


def chunk_present(c, text):
    """-> rule name ('exact', 'attr', 'verb', 'neg-infix', 'neg-infix+attr') or None."""
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
    if c.endswith("သော") and len(c) > 3:
        st = c[:-3]
        for i in range(1, len(st)):
            if any(st[:i] + "မ" + st[i:] + e in text for e in ATTR_FROM):
                return "neg-infix+attr"
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
    # repeats: one keyword = one value inside a line
    rep = []
    for (i, x), (_, y) in zip(a, b):
        seen = {}
        for kv in y.split(", "):
            k, v = kv.split("=", 1)
            if seen.setdefault(k, v) != v:
                rep.append((i, k))
    return len(a), bad, fails, punct, ruled, rep


def write_table(table, ruled_all):
    with open(HERE / "map-table-2-01.md", "w", encoding="utf-8") as f:
        f.write("# pi-1 Burmese keyword mapping: 2-01 Cittuppādakaṇḍa (new rules and review table)\n\n")
        f.write("Written by map_2-01.py. Burmese from the FINAL text of this track only "
                "(AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters/2-01-cittuppadakandam.md). "
                "The approved sample rules 1–11 and values (map-table.md, preamble / 1-matika) are kept; only what is "
                "new is listed here.\n\n")
        f.write(RULES)
        f.write("\n## Presence: chunks matched by a dictionary-form rule (not literally in the segment)\n\n")
        f.write("Every other chunk of every value occurs literally in its segment's Burmese (particles that the "
                "rules strip follow the chunk in the text). Rule-matched chunks, one row per keyword and chunk "
                "(segments listed):\n\n| keyword | chunk | rule | segments |\n|---|---|---|---|\n")
        grp = collections.OrderedDict()
        for sid, k, c, r in ruled_all:
            grp.setdefault((k, c, r), []).append(sid)
        for (k, c, r), sids in grp.items():
            f.write(f"| {k} | {c} | {r} | {' '.join(sids)} |\n")
        f.write("\n## Keyword → Burmese (number of uses)\n\nSource: own = the 2-01 table T_CU, samaye = rule 13, "
                "shared = the approved sample tables. Several values = the keyword reads differently by "
                "context.\n\n| Pāli keyword | Burmese (uses) | source |\n|---|---|---|\n")
        for kw in sorted(table, key=lambda x: (low(x).lower(), x)):
            src = SOURCE.get((CHAPTERS[0], kw), "")
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
    report = bool(args and args[0] == "--report")
    table, unmapped, problems, summary = run(write=not report)
    if unmapped:
        print(f"UNMAPPED keywords: {len(unmapped)} distinct, {sum(len(v) for v in unmapped.values())} uses")
        for kw, where in sorted(unmapped.items(), key=lambda x: -len(x[1])):
            print(f"  {kw}\t{len(where)}\t{where[0][1]}")
    print(f"presence problems: {len(problems)}")
    for ch, sid, kw, v in problems:
        print(f"  {sid}\t{kw} = {v}")
    if report:
        print("values from the shared sample tables:",
              sorted({k for (c, k), s in SOURCE.items() if s in ("shared", "dhammā")}))
    if report or unmapped:
        sys.exit()
    ruled_all, tot_nne = [], 0
    results = []
    for ch, n, nne in summary:
        ln, bad, fails, punct, ruled, rep = verify(ch)
        ruled_all += ruled
        tot_nne += nne
        results.append((ch, ln, bad, fails, punct, ruled, rep, nne))
    write_table(table, ruled_all)
    for ch, ln, bad, fails, punct, ruled, rep, nne in results:
        print(f"{ch}: lines {ln} | keyword preservation bad {bad} | presence failures {len(fails)} "
              f"(rule-matched chunks {len(ruled)}) | comma/၊ {punct} | repeat conflicts {rep} | no-equivalent {nne}")
        for f_ in fails:
            print("   FAIL", f_)
    for k in sorted({(k, c, r) for _, k, c, r in ruled_all}):
        print("   rule", k)
    print("total no direct equivalent:", tot_nne, "| distinct keywords:", len(table))
