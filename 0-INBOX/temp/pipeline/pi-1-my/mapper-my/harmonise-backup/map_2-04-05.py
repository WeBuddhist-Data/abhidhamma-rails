"""Pāli→Burmese keyword mapping for pi-1 chapters 2-04 and 2-05 (Cittuppādakaṇḍa: the twelve unwholesome cittas,
the resultants and the functional cittas).

usage (python3 -I -X utf8):
  map_2-04-05.py             writes <ch>.mapped.md for 2-04 / 2-05 and map-table-2-04-05.md, then verifies them
                             (keyword preservation, presence of every value chunk in its segment, no ", " / «၊»)
  map_2-04-05.py --report    writes nothing; lists unmapped keywords and presence failures
  map_2-04-05.py --seg ID    prints Pāli, Burmese, keywords and mapping of one segment

Method: a COPY of the approved sample mapper map_all.py (its tables T_PREAMBLE / T_MATIKA, the compose rule for
«X dhammā», the context function for rūpa, the presence check and the verifier), not an import. map_all.py,
map-table.md and the sample outputs are not touched. The Burmese is the FINAL text of this track
(AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters); no other Burmese source is used.
Lookup order per keyword: CTX[sid] (per-segment overrides) -> T_CU (this file's table for 2-04 / 2-05) -> the sample
tables (first letter case-insensitive) -> compose(). New here (map-table-2-04-05.md, rules 12-20):
  * a value may be a LIST of candidates (one sense or one shape per entry); the first one found in the segment wins:
    literally, then as two literal pieces in text order joined with « … » (discontinuous), then by the dictionary-form
    endings of the presence check;
  * «samaye X» = «အချိန်၌ ရှိသော X» (as 2-01); «Yo / Yā / Yaṃ» (relative pronoun) = (no direct equivalent).
  --loose lists the values found only chunk by chunk (for a manual review); --compare FILE… lists keywords whose
  values differ from other chapters' mapped files (read-only).
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
TABLE_OUT = HERE / "map-table-2-04-05.md"


def low(w):
    return w[:1].lower() + w[1:]


# ---- copied verbatim from map_all.py (approved sample tables) ----
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
# 2-04 / 2-05: building blocks (strings of the chapter text)
# =====================================================================================================
ABY = "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်သော"         # abyākata (sample value, «၊» dropped: rule 6)
KIR = "ပြုရုံမျှသာ ဖြစ်သော"                               # kiriya / kiriyā
VIP = "ကံ၏ အကျိုး"                                        # vipāka (noun)
VIPA = "ကံ၏ အကျိုး ဖြစ်သော"                               # vipāka before the citta
MVD = "မနော သိစိတ် ဓာတ်"                                   # manoviññāṇadhātu
MD = "မနော ဓာတ်"                                          # manodhātu
SOM = "ဝမ်းမြောက်မှု"                                      # somanassa
UPE = "ဥပေက္ခာ"
CSJ = "စိတ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော"                      # cetosamphassaja
KSJ = "ကိုယ်၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော"                     # kāyasamphassaja
SATA = "နှစ်သက်ဖွယ်ကောင်း"
ASATA = "နှစ်သက်ဖွယ် မကောင်း"
AHIRI = "ဒုစရိုက်ကို မရှက်မှု"
ANOTT = "ဒုစရိုက်ကို မကြောက်ရွံ့မှု"
MICCHA = "မှားယွင်းသော"
IND = "စွမ်းရည်"                                          # -indriya
BAL = "စွမ်းအား"                                           # -bala
SANNA = "မှတ်သိမှု"
VINN = "သိစိတ်"
ANNA = "အပြည့်အဝ သိမြင်ခြင်း"
ANG = "အင်္ဂါ"
LOK = "လောကကို ကျော်လွန်သော"
RUPAV = "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော"
ARUPAV = "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော"
KAMAV = "ကာမဘုံနှင့် ဆိုင်သော"

T_CU = {
    # --- frames, particles
    "Yo": NONE, "Yā": NONE, "Yaṃ": NONE,              # relative pronoun: Burmese builds the clause with «…သော» (rule 13)
    "ye": "ရှိသမျှ",                                   # ye vā pana … aññepi atthi … dhammā = «… သဘောတရားများ ရှိသမျှလည်း»
    "yaṃ yaṃ": "မည်သည့်အရာ",
    "ārabbha": "အာရုံပြု၍",                            # absolutive (rule 12)
    "eva": "သာ",                                       # vivicceva = «ကင်းဆိတ်၍သာ» (rule 14)
    "ṭhapetvā": "ချန်ထား၍",
    "dhammā akusalā": "အကုသိုလ် သဘောတရား", "dhammā abyākatā": ABY + " " + DH, "dhammā kusalā": "ကုသိုလ် သဘောတရား",
    "akusalā": "အကုသိုလ်", "akusalaṃ": "အကုသိုလ်", "akusala": "အကုသိုလ်", "akusalassa": "အကုသိုလ်",
    "akusalānaṃ": "အကုသိုလ်", "akusalānaṃ dhammānaṃ": "အကုသိုလ် သဘောတရား", "akusalāni": "အကုသိုလ်",
    "kusalā": "ကုသိုလ်", "kusalaṃ": "ကုသိုလ်", "kusalassa": "ကုသိုလ်", "Kusala": "ကုသိုလ်",
    "abyākatā": ABY, "abyākataṃ": ABY, "Abyākata": ABY,
    "kusalā nākusalā": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်",      # neva kusalā nākusalā (… မဟုတ်၊ … ကံ၏ အကျိုးလည်း)
    "kusalaṃ nākusalaṃ": "ကုသိုလ်လည်း မဟုတ် အကုသိုလ်လည်း မဟုတ်",
    "kammavipākā": VIP, "kammavipākaṃ": VIP,          # na ca kammavipākā: the positive part (rule 8)
    # --- the citta opening
    "akusalaṃ cittaṃ": "အကုသိုလ်စိတ်",
    "cittaṃ uppannaṃ": "စိတ် ဖြစ်ပေါ်လာသည်",           # clause (rule 4): text «… စိတ်သည် ဖြစ်ပေါ်လာသော»
    "dhātu uppannā": "ဓာတ် ဖြစ်ပေါ်လာသည်",
    "uppannaṃ": "ဖြစ်ပေါ်လာသော", "uppannā": "ဖြစ်ပေါ်လာသော",
    "sahagataṃ": "အတူ ဖြစ်သော", "sahagatā": "အတူ ဖြစ်သော",
    "somanassasahagataṃ": SOM + "နှင့်အတူ ဖြစ်သော", "somanassasahagatā": SOM + "နှင့်အတူ ဖြစ်သော",
    "upekkhāsahagataṃ": UPE + "နှင့်အတူ ဖြစ်သော", "upekkhāsahagatā": UPE + "နှင့်အတူ ဖြစ်သော",
    "domanassasahagataṃ": "စိတ်ဆင်းရဲမှုနှင့်အတူ ဖြစ်သော",
    "sampayuttaṃ": "ယှဉ်တွဲသော", "sampayuttā": "ယှဉ်တွဲသော",
    "vippayuttaṃ": "ကင်းကွာသော", "vippayuttā": "ကင်းကွာသော",
    "diṭṭhigatavippayuttaṃ": "အယူမှားနှင့် ကင်းကွာသော",
    "ñāṇavippayuttā": "ဉာဏ်နှင့် ကင်းကွာသော", "ñāṇa": "ဉာဏ်",
    "diṭṭhigata": "အယူမှား",
    "saṅkhārena": "တိုက်တွန်းမှု",                       # sasaṅkhārena «တိုက်တွန်းမှုဖြင့်»
    "ārammaṇaṃ": "အာရုံ", "ārammaṇā": "အာရုံ",          # sample rule 2 (also in -ārammaṇa compounds)
    "dhammārammaṇaṃ": "သဘောတရားကို အာရုံပြုသော", "dhammārammaṇā": "သဘောတရားကို အာရုံပြုသော",
    "dhamma": DH,
    "sadda": "အသံ", "gandha": "အနံ့", "rasa": "အရသာ", "phoṭṭhabba": "အထိအတွေ့",
    "rūpa": "@rupa", "Rūpa": "@rupa",
    "paṭigha": "မုန်းတီးမှု",                            # aversion (paṭighasampayutta), harmonise-notes item 11
    # --- factor names
    "phasso": "တွေ့ထိမှု", "Phasso": "တွေ့ထိမှု", "vedanā": "ခံစားမှု", "saññā": SANNA, "cetanā": "စေ့ဆော်မှု",
    "cittaṃ": "စိတ်", "vitakko": "စတင်ကြံစည်မှု", "vicāro": "ဆက်လက်သုံးသပ်မှု", "pīti": "ပီတိ",
    "sukhaṃ": "သာယာမှု", "ekaggatā": "စူးစိုက်မှု", "cittassekaggatā": "စိတ်၏ စူးစိုက်မှု",
    "indriyaṃ": IND, "indriyāni": IND,
    "vīriyindriyaṃ": "ဝီရိယ၏ " + IND, "samādhindriyaṃ": "သမာဓိ၏ " + IND, "manindriyaṃ": "မနော၏ " + IND,
    "somanassindriyaṃ": SOM + "၏ " + IND, "jīvitindriyaṃ": "အသက်၏ " + IND, "upekkhindriyaṃ": UPE + "၏ " + IND,
    "dukkhindriyaṃ": "နာကျင်မှု၏ " + IND, "paññindriyaṃ": "ပညာ၏ " + IND, "aññindriyaṃ": ANNA + "၏ " + IND,
    "balaṃ": BAL, "balāni": BAL,
    "vīriyabalaṃ": "ဝီရိယ၏ " + BAL, "samādhibalaṃ": "သမာဓိ၏ " + BAL, "paññābalaṃ": "ပညာ၏ " + BAL,
    "ahirikabalaṃ": AHIRI + "၏ " + BAL, "anottappabalaṃ": ANOTT + "၏ " + BAL,
    "ahirika": AHIRI, "ahirikaṃ": AHIRI, "anottappa": ANOTT, "anottappaṃ": ANOTT,
    "micchā": MICCHA, "micchādiṭṭhi": MICCHA + " အယူ", "micchāsaṅkappo": MICCHA + " ကြံစည်မှု",
    "micchāvāyāmo": MICCHA + " အားထုတ်မှု", "micchāsamādhi": MICCHA + " သမာဓိ",
    "micchāpatho": MICCHA + " လမ်းကြောင်း", "micchattaṃ": "မှားယွင်းမှု",
    "diṭṭhi": "အယူ", "samādhi": "သမာဓိ", "vāyāmo": "အားထုတ်မှု", "saṅkappo": "ကြံစည်မှု",
    "lobho": "လောဘ", "moho": "မောဟ", "doso": "ဒေါသ", "abhijjhā": "သူ့ဥစ္စာကို လိုချင်ခြင်း",
    "byāpādo": "ဖျက်ဆီးလိုစိတ်", "samatho": "စိတ်ငြိမ်သက်ခြင်း", "paggāho": "စိတ်ကို မြှင့်တင်ခြင်း",
    "avikkhepo": "စိတ် မပျံ့လွင့်ခြင်း",
    "vicikicchā": "ယုံမှားမှု", "uddhaccaṃ": "ယောက်ယက်ခတ်မှု", "uddhacca": "ယောက်ယက်ခတ်မှု",
    "alobho": "လောဘ မရှိခြင်း", "adoso": "ဒေါသ မရှိခြင်း", "amoho": "မောဟ မရှိခြင်း",
    "abyākatamūlaṃ": ABY + " အမြစ်", "mūlaṃ": "အမြစ်", "akusalamūlaṃ": "အကုသိုလ်၏ အမြစ်",
    "somanassa": SOM, "upekkhā": UPE, "domanassa": "စိတ်ဆင်းရဲမှု",
    "dukkhaṃ": "နာကျင်မှု", "dukkha": "@dukkha", "sukha": "@sukha",
    "jīvita": "အသက်", "mana": "မနော", "mano": "မနော",
    # --- groups (Tasmiṃ kho pana samaye …): the count follows the text (rule 15)
    "khandhā": "အစုအဝေး", "khandho": "အစုအဝေး", "āyatanāni": "အာရုံခံ နယ်ပယ်", "dhātuyo": "ဓာတ်", "dhātu": "ဓာတ်",
    "āhārā": "အာဟာရ", "jhānaṃ": "ဈာန်", "maggo": "မဂ်", "hetū": "အမြစ်", "hetu": "အမြစ်",
    "pañcaṅgikaṃ": ANG + " ငါးပါး ရှိသော", "caturaṅgikaṃ": ANG + " လေးပါး ရှိသော",
    "caturaṅgiko": ANG + " လေးပါး ရှိသော", "tivaṅgiko": ANG + " သုံးပါး ရှိသော", "duvaṅgiko": ANG + " နှစ်ပါး ရှိသော",
    "caturaṅgiko maggo": ANG + " လေးပါး ရှိသော မဂ်",
    "dhammāyatanaṃ": DH + " အာရုံခံ နယ်ပယ်", "dhammadhātu": DH + " ဓာတ်",
    # --- the «ye vā pana» clause
    "paṭicca": "အကြောင်းတို့ကို မှီ၍",
    "samuppannā": "ဖြစ်ပေါ်လာသော",
    "paṭiccasamuppannā": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော",
    "arūpino": "ရုပ် မဟုတ်သော", "arūpīnaṃ": "ရုပ် မဟုတ်သော",
    "arūpino dhammā": "ရုပ် မဟုတ်သော " + DH, "arūpīnaṃ dhammānaṃ": "ရုပ် မဟုတ်သော " + DH,
    "samuppannā arūpino": "ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော",
    "samuppannā arūpino dhammā": "ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော " + DH,
    "paṭiccasamuppannā arūpino": "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော",
    # --- aggregates (saṅkhārakkhandha)
    "viññāṇakkhandhaṃ": VINN + " အစုအဝေး", "viññāṇakkhandho": VINN + " အစုအဝေး",
    "vedanākkhandhaṃ": "ခံစားမှု အစုအဝေး", "saññākkhandhaṃ": SANNA + " အစုအဝေး",
    "saṅkhārakkhandho": "ပြုပြင်ဖန်တီးမှု အစုအဝေး", "saṅkhāra": "ပြုပြင်ဖန်တီးမှု",
    "viññāṇa": VINN, "viññāṇaṃ": VINN,
    # --- phassa, vedanā
    "phusanā": "ထိခြင်း", "saṃphusanā": "တွေ့ထိခြင်း",
    "samphassajaṃ": "တွေ့ထိမှုမှ ဖြစ်ပေါ်သော", "samphassajā": "တွေ့ထိမှုမှ ဖြစ်ပေါ်သော",
    "cetosamphassajaṃ": CSJ, "cetosamphassajā": CSJ,
    "kāyasamphassajaṃ": KSJ, "kāyasamphassajā": KSJ, "kāyasamphassa": "ကိုယ်၏ တွေ့ထိမှု", "samphassa": "တွေ့ထိမှု",
    "sātaṃ": [SATA + "မှု", SATA + "သော"], "asātaṃ": [ASATA + "မှု", ASATA + "သော"],
    "tajjā": "သက်ဆိုင်ရာ", "vedayitaṃ": "ခံစားရခြင်း",
    "cetasikaṃ": "စိတ်ပိုင်းဆိုင်ရာ", "kāyikaṃ": "ကိုယ်ပိုင်းဆိုင်ရာ",
    "cetasikaṃ sātaṃ": "စိတ်ပိုင်းဆိုင်ရာ " + SATA + "မှု", "cetasikaṃ sukhaṃ": "စိတ်ပိုင်းဆိုင်ရာ သာယာမှု",
    "cetasikaṃ dukkhaṃ": "စိတ်ပိုင်းဆိုင်ရာ နာကျင်မှု",
    "manoviññāṇa": "မနော " + VINN, "manoviññāṇadhātu": MVD, "manodhātu": MD,
    "cakkhuviññāṇa": "မျက်စိ " + VINN, "cakkhuviññāṇadhātu": "မျက်စိ " + VINN + " ဓာတ်",
    "kāyaviññāṇa": "ကိုယ် " + VINN, "kāyaviññāṇadhātu": "ကိုယ် " + VINN + " ဓာတ်",
    "cakkhuviññāṇaṃ": "မျက်စိ " + VINN, "sotaviññāṇaṃ": "နား " + VINN, "ghānaviññāṇaṃ": "နှာခေါင်း " + VINN,
    "jivhāviññāṇaṃ": "လျှာ " + VINN, "kāyaviññāṇaṃ": "ကိုယ် " + VINN,
    "sukhaṃ vedayitaṃ": "သာယာသော ခံစားရခြင်း", "sukhā vedanā": "သာယာသော ခံစားမှု", "sukhā": "သာယာသော",
    "dukkhā vedanā": "နာကျင်သော ခံစားမှု",
    "adukkhamasukhaṃ": "မနာကျင် မသာယာသော",
    "cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ": CSJ + " မနာကျင် မသာယာသော ခံစားရခြင်း",
    "cetosamphassajā adukkhamasukhā vedanā": CSJ + " မနာကျင် မသာယာသော ခံစားမှု",
    # --- saññā, cetanā, citta
    "sañjānanā": "မှတ်သိခြင်း", "sañjānitattaṃ": "မှတ်သိထားသော အဖြစ်",
    "sañcetanā": "စေ့ဆော်ခြင်း", "cetayitattaṃ": "စေ့ဆော်ထားသော အဖြစ်",
    "mānasaṃ": "စိတ်နှလုံး", "hadayaṃ": "နှလုံးသား", "paṇḍaraṃ": "ကြည်လင်သောအရာ",
    "manāyatanaṃ": "မနော အာရုံခံ နယ်ပယ်",
    # --- vitakka, vicāra
    "takko": "တွေးတောခြင်း", "appanā": "အာရုံ၌ စိတ်ကို သွင်းခြင်း", "cetaso": "စိတ်",
    "abhiniropanā": "အာရုံသို့ တင်ပို့ခြင်း",
    "cāro": "သုံးသပ်ခြင်း", "cittassa": "စိတ်", "anusandhānatā": "အာရုံနှင့် ဆက်စပ်ထားခြင်း",
    "anupekkhanatā": "အာရုံကို စေ့စေ့ ရှုကြည့်ခြင်း",
    # --- pīti
    "attamanatā": "နှစ်သိမ့်ခြင်း", "anattamanatā": "မနှစ်သိမ့်ခြင်း",
    "āmodanā": "ဝမ်းသာခြင်း", "odagyaṃ": "စိတ်တက်ကြွခြင်း", "pāmojjaṃ": "ရွှင်လန်းခြင်း",
    "pahāso": "အလွန် ပြုံးရွှင်ခြင်း", "hāso": "ပြုံးရွှင်ခြင်း", "pamodanā": "အလွန် ဝမ်းသာခြင်း",
    "vitti": "ကျေနပ်ခြင်း",
    # --- ekaggatā / samādhi
    "ṭhiti": "တည်တံ့ခြင်း", "cittassa ṭhiti": "စိတ်၏ တည်တံ့ခြင်း", "saṇṭhiti": "ကောင်းစွာ တည်တံ့ခြင်း",
    "avaṭṭhiti": "ခိုင်မြဲစွာ တည်တံ့ခြင်း", "avisāhāro": "မပြန့်ကျဲခြင်း",
    "avisāhaṭa": "မပြန့်ကျဲသော", "avisāhaṭamānasatā": "စိတ် မပြန့်ကျဲသော အဖြစ်", "mānasatā": "စိတ် … အဖြစ်",
    # --- vīriya
    "cetasiko": "စိတ်ပိုင်းဆိုင်ရာ", "cetasiko vīriyārambho": "စိတ်ပိုင်းဆိုင်ရာ ဝီရိယ စတင်ခြင်း",
    "ārambho": "စတင်ခြင်း", "nikkamo": "ရှေ့သို့ တိုးထွက်ခြင်း", "parakkamo": "ရဲရင့်စွာ ကြိုးစားခြင်း",
    "uyyāmo": "ထကြွ ကြိုးစားခြင်း", "ussāho": "စိတ်အားထက်သန်မှု", "ussoḷhī": "ပြင်းပြသော အားမာန်",
    "thāmo": "ခွန်အား", "dhiti": "ဇွဲ", "asithila": "မလျော့ရဲသော",
    "chandatā": "ဆန္ဒ", "dhuratā": "ဝန်",
    "nikkhitta": "လက်လွှတ်သော / ချထားသော",           # two compounds, two Burmese verbs (as the 2-01 mapping)
    "sampaggāho": "ခိုင်မြဲစွာ ထမ်းဆောင်ခြင်း",
    # --- jīvita
    "āyu": "သက်တမ်း", "yapanā": "ဆက်လက် ဖြစ်နေခြင်း", "yāpanā": "ဆက်လက် ရှင်သန်စေခြင်း",
    "iriyanā": "လှုပ်ရှားခြင်း", "vattanā": "လည်ပတ်ခြင်း", "pālanā": "စောင့်ရှောက်ခြင်း",
    # --- micchādiṭṭhi
    "diṭṭhigataṃ": "အယူမှား", "gahanaṃ": "တောအုပ်", "kantāro": "ကန္တာရ",
    "visūkāyikaṃ": "ကောက်ကွေးမှု", "vipphanditaṃ": "တုန်လှုပ်မှု",
    "saṃyojanaṃ": "နှောင်ကြိုး", "diṭṭhisaṃyojanaṃ": "အယူ နှောင်ကြိုး",
    "gāho": "စွဲကိုင်ခြင်း", "patiṭṭhāho": "ခိုင်မြဲစွာ စွဲကိုင်ခြင်း", "abhiniveso": "သက်ဝင်ယုံကြည်ခြင်း",
    "parāmāso": "မှားယွင်းသော ယူဆမှု", "kummaggo": "လမ်းမှား", "patho": ["လမ်းကြောင်း", "လမ်း"],
    "tittha": "အယူဝါဒ", "vipariyāsa": "ပြောင်းပြန်", "vipariyāsaggāho": "ပြောင်းပြန် စွဲကိုင်ခြင်း",
    # --- ahirika, anottappa
    "hirīyati": "ရှက်သည်", "ottappati": "ကြောက်ရွံ့သည်", "ottappitabbena": "ကြောက်ရွံ့ထိုက်သည့်အရာ",
    "pāpakānaṃ": "ယုတ်မာသော", "samāpattiyā": "ကျူးလွန်ခြင်း",
    # --- lobha
    "lubbhanā": "မက်မောခြင်း", "sārāgo": "တပ်မက်ခြင်း", "sārajjanā": "စွဲမက်ခြင်း",
    # --- moha (fragments that lost a- / an- map to the positive part: sample rule 8)
    "ñāṇaṃ": "သိခြင်း", "aññāṇaṃ": "မသိခြင်း", "dassanaṃ": "မြင်ခြင်း", "anabhisamayo": "ထင်ထင်ရှားရှား မသိမြင်ခြင်း",
    "anubodho": "လိုက်၍ နားလည်ခြင်း", "sambodho": "ကောင်းစွာ နားလည်ခြင်း", "appaṭivedho": "ထိုးဖောက်၍ မသိခြင်း",
    "asaṃgāhanā": "စုစည်း၍ မယူနိုင်ခြင်း", "pariyogāhanā": "နက်နက်နဲနဲ သက်ဝင်နိုင်ခြင်း",
    "samapekkhanā": "ညီညီညွတ်ညွတ် ရှုမြင်ခြင်း", "paccavekkhanā": "ပြန်လည် ဆင်ခြင်ခြင်း",
    "paccakkhakammaṃ": "ကိုယ်တိုင် ထင်ထင်ရှားရှား ပြုခြင်း", "dummejjhaṃ": "ဉာဏ်နုံခြင်း", "bālyaṃ": "မိုက်မဲခြင်း",
    "sampajaññaṃ": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း", "pamoho": "အလွန် တွေဝေခြင်း", "sammoho": "လုံးဝ တွေဝေခြင်း",
    "avijjā": "အမှန်ကို မသိမှု", "ogho": "ရေအလျဉ်", "yogo": "ထမ်းပိုး", "anusayo": "ကိန်းအောင်းခြင်း",
    "pariyuṭṭhānaṃ": "ထကြွခြင်း", "laṅgī": "တံခါးကန့်လန့်",
    # --- dosa
    "dussanā": "စိတ်ဆိုးခြင်း", "dussitattaṃ": "စိတ်ဆိုးထားသော အဖြစ်", "byāpatti": "ဖောက်ပြန်ခြင်း",
    "byāpajjanā": "ညှဉ်းဆဲလိုခြင်း", "virodho": "ဆန့်ကျင်ခြင်း", "paṭivirodho": "ပြန်လည် ဆန့်ကျင်ခြင်း",
    "caṇḍikkaṃ": "ကြမ်းကြုတ်ခြင်း", "asuropo": "စကား ကြမ်းခြင်း",
    # --- vicikicchā
    "kaṅkhā": "သံသယ", "kaṅkhāyanā": "သံသယ ဖြစ်ခြင်း", "vimati": "စိတ်ရှုပ်ထွေးခြင်း",
    "dveḷhakaṃ": "စိတ် နှစ်ခွ ဖြစ်ခြင်း", "dvedhā": "နှစ်ခွ", "saṃsayo": "ဒွိဟ ဖြစ်ခြင်း",
    "anekaṃsaggāho": "တစ်ထစ်ချ မယူနိုင်ခြင်း", "ekaṃsa": "တစ်ထစ်ချ",
    "āsappanā": "ယိမ်းယိုင်ခြင်း", "parisappanā": "ပတ်ချာလည် ယိမ်းယိုင်ခြင်း",
    "thambhitattaṃ": "တောင့်တင်းနေသော အဖြစ်", "vilekho": "ခြစ်ကုတ်ခြင်း",
    # --- uddhacca
    "avūpasamo": "မငြိမ်ဝပ်ခြင်း", "vikkhepo": "ပျံ့လွင့်ခြင်း", "bhantattaṃ": "ယိမ်းထိုးနေသော အဖြစ်",
    # --- paññā (aññātāvindriya)
    "aññā": ANNA, "aññātāvī": "အပြည့်အဝ သိမြင်ပြီးသူ", "paññā": "ပညာ", "pajānanā": "ကွဲပြားစွာ သိခြင်း",
    "vicayo": "စိစစ်ခြင်း", "pavicayo": "သေချာစွာ စိစစ်ခြင်း", "dhammavicayo": "သဘောတရားများကို စိစစ်ခြင်း",
    "sallakkhaṇā": "လက္ခဏာကို ကောင်းစွာ ခွဲခြားခြင်း", "upalakkhaṇā": "လက္ခဏာကို အနီးကပ် ခွဲခြားခြင်း",
    "paccupalakkhaṇā": "လက္ခဏာကို အသီးသီး ခွဲခြားခြင်း", "paṇḍiccaṃ": "လိမ္မာခြင်း", "kosallaṃ": "ကျွမ်းကျင်ခြင်း",
    "nepuññaṃ": "နက်နဲသိမ်မွေ့ခြင်း", "vebhabyā": "ခွဲခြမ်းစိတ်ဖြာခြင်း", "cintā": "စဉ်းစားခြင်း",
    "upaparikkhā": "စူးစမ်းဆန်းစစ်ခြင်း", "bhūrī": "ကျယ်ပြန့်ခြင်း", "medhā": "ဉာဏ်ထက်မြက်ခြင်း",
    "pariṇāyikā": "လမ်းပြခြင်း", "vipassanā": "ထိုးထွင်းသိမြင်ခြင်း", "patodo": "နှင်တံ",
    "satthaṃ": "ဓား", "paññāsatthaṃ": "ပညာ ဓား", "pāsādo": "ပြာသာဒ်", "paññāpāsādo": "ပညာ ပြာသာဒ်",
    "āloko": "အလင်း", "paññāāloko": "ပညာ အလင်း", "obhāso": "အရောင်အဝါ", "paññāobhāso": "ပညာ အရောင်အဝါ",
    "pajjoto": "မီးအိမ်", "paññāpajjoto": "ပညာ မီးအိမ်", "ratanaṃ": "ရတနာ", "paññāratanaṃ": "ပညာ ရတနာ",
    "sammā": "မှန်ကန်သော", "magga": "မဂ်", "maggaṅgaṃ": "မဂ်၏ " + ANG,
    "sambojjhaṅgo": "ဗောဇ္ဈင်", "vicayasambojjhaṅgo": "စိစစ်ခြင်း ဗောဇ္ဈင်",
    # --- resultants, functional (openings)
    "kāmāvacarassa": KAMAV, "rūpāvacarassa": RUPAV, "arūpāvacarassa": ARUPAV, "avacarassa": "ဘုံနှင့် ဆိုင်သော",
    "rūpāvacaraṃ": RUPAV, "arūpāvacaraṃ": ARUPAV, "avacaraṃ": "ဘုံနှင့် ဆိုင်သော",
    "kāmāvacara": KAMAV, "Rūpāvacara": RUPAV, "Arūpāvacara": ARUPAV, "avacara": "ဘုံနှင့် ဆိုင်သော",
    "kāma": "ကာမ", "arūpa": "ရုပ်မရှိသော", "Arūpa": "ရုပ်မရှိသော",
    "kusalassa kammassa": "ကုသိုလ်ကံ", "akusalassa kammassa": "အကုသိုလ်ကံ",
    "katattā": "ပြုခဲ့သော", "upacitattā": "ဆည်းပူးခဲ့သော", "bhāvitattā": "ပွားများခဲ့သော",   # rule 16
    "kiriyā": KIR, "kiriyaṃ": KIR, "Kiriyā": KIR,
    "vihāraṃ": "နေထိုင်ရန်",                          # diṭṭhadhammasukhavihāraṃ «… သာယာစွာ နေထိုင်ရန် ဖြစ်သော»
    "hetukā": "အမြစ်", "hetuka": "အမြစ်",              # sample rule 2 (sahetuka / ahetuka)
    # --- jhāna, path openings
    "jhānaṃ bhāveti": "ဈာန်ကို ပွားများသည်", "bhāveti": "ပွားများသည်",
    "lokuttaraṃ": LOK, "lokuttaraṃ jhānaṃ": LOK + " ဈာန်", "lokuttaraṃ jhānaṃ bhāveti": LOK + " ဈာန်ကို ပွားများသည်",
    "niyyānikaṃ": "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော", "gāmiṃ": "ဦးတည်သော", "apacaya": "လျော့ပါးခြင်း",
    "caya": NONE,                                      # apacaya «လျော့ပါးခြင်း»: no word for accumulation (rule 8)
    "niyyānikaṃ apacayagāmiṃ": "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "diṭṭhigatānaṃ": "အယူမှား", "pahānāya": "ပယ်ရန်", "diṭṭhigatānaṃ pahānāya": "အယူမှားတို့ကို ပယ်ရန်",
    "bhūmiyā": "အဆင့်", "pattiyā": "ရောက်ရန်", "tanubhāvāya": "ပါးလျစေရန်",
    "kāmarāga": "ကာမရာဂ", "rāga": "ရာဂ", "māna": "မာန", "avijjāya": "အမှန်ကို မသိမှု",
    "byāpādānaṃ": "ဖျက်ဆီးလိုစိတ်", "avasesa": "အကြွင်းအကျန်",
    "vivicca": "ကင်းဆိတ်၍", "kāmehi": "ကာမ", "vivicceva kāmehi": "ကာမတို့မှ ကင်းဆိတ်၍သာ",
    "upasampajja": "ဝင်စား၍", "viharati": "နေသည်", "upasampajja viharati": "ဝင်စား၍ နေသည်",
    "paṭipadaṃ": "ကျင့်စဉ်", "paṭipadā": "ကျင့်စဉ်", "dukkhapaṭipadaṃ": "ကျင့်စဉ် ခက်ခဲသော",
    "sukhapaṭipadaṃ": "ကျင့်စဉ် လွယ်ကူသော",
    "abhiññaṃ": "ထူးကဲစွာ သိခြင်း", "abhiññanti": "ထူးကဲစွာ သိခြင်း",
    "dandha": "နှေးကွေးသော", "khippa": "လျင်မြန်သော",
    "dandhābhiññaṃ": "ထူးကဲစွာ သိခြင်း နှေးကွေးသော", "dandhābhiññanti": "ထူးကဲစွာ သိခြင်း နှေးကွေးသော",
    "khippābhiññaṃ": "ထူးကဲစွာ သိခြင်း လျင်မြန်သော",
    "paṭipadaṃ dandha": "ကျင့်စဉ် နှေးကွေးသော", "paṭipadaṃ khippa": "ကျင့်စဉ် လျင်မြန်သော",
    "suññataṃ": ["ဆိတ်သုဉ်းသော", "ဆိတ်သုဉ်းခြင်း"], "suññatanti": "ဆိတ်သုဉ်းသော", "suññatā": "ဆိတ်သုဉ်းခြင်း",
    "Suññata": "ဆိတ်သုဉ်းခြင်း",
    "animittaṃ": "အမှတ်အသား မရှိသော", "animittanti": "အမှတ်အသား မရှိသော",
    "appaṇihitaṃ": ["တောင့်တမှု မရှိသော", "တောင့်တမှု မရှိခြင်း"], "appaṇihitanti": "တောင့်တမှု မရှိသော",
    "Appaṇihita": "တောင့်တမှု မရှိခြင်း",
    "chanda": "ဆန္ဒ", "Chanda": "ဆန္ဒ",
    "adhipateyyaṃ": "အကြီးအမှူးပြုသော", "adhipateyyanti": "အကြီးအမှူးပြုသော", "adhipateyya": "အကြီးအမှူးပြုသော",
    "pañcamaṃ": "ပဉ္စမ", "catutthaṃ jhānaṃ": "စတုတ္ထ ဈာန်",
    "kusalassa jhānassa": "ကုသိုလ် ဈာန်", "lokuttarassa kusalassa": LOK + " ကုသိုလ်",
    "lokuttarassa kusalassa jhānassa": LOK + " ကုသိုလ် ဈာန်",
    "maggaṃ": "@maggam", "maggaṃ bhāveti": "လမ်းကို ပွားများသည်",
    "upapattiyā": "ဖြစ်ပေါ်ရန်", "upapattiyā maggaṃ": "ဖြစ်ပေါ်ရန် လမ်း",
    "pathavī": "မြေ", "kasiṇaṃ": "ကသိုဏ်း",
    "vitakka": "စတင်ကြံစည်မှု", "vicārānaṃ": "ဆက်လက်သုံးသပ်မှု", "vūpasamā": "ငြိမ်းသွားခြင်း",
    "sukhassa": "သာယာမှု", "pahānā": "ပယ်ခြင်း", "sukhassa ca pahānā": "သာယာမှုကိုလည်း ပယ်ခြင်း",
    "sabbaso": "အလုံးစုံ", "samatikkamā": "ကျော်လွန်ခြင်း", "samatikkamma": "ကျော်လွန်၍",
    "atthaṅgamā": "ချုပ်ငြိမ်းသွားခြင်း", "nānatta": "အမျိုးမျိုး ကွဲပြားမှု", "manasikārā": "နှလုံး သွင်းခြင်း",
    "saññānaṃ": SANNA,
    "ākāsa": "ကောင်းကင်", "ānañca": "အဆုံး မရှိသော",
    "ānañcāyatana": "အဆုံး မရှိသော နယ်ပယ်", "ānañcāyatanaṃ": "အဆုံး မရှိသော နယ်ပယ်",
    "viññāṇañca": "အဆုံး မရှိသော " + VINN, "viññāṇañcāyatanaṃ": "အဆုံး မရှိသော " + VINN + " နယ်ပယ်",
    "ākiñcañña": "ဘာမျှ မရှိသော", "asaññā": SANNA + " မရှိသော",
    # lokuttaraṃ X bhāveti (the 2-03 list, repeated in 2-05)
    "lokuttaraṃ satipaṭṭhānaṃ bhāveti": LOK + " သတိပဋ္ဌာန်ကို ပွားများသည်",
    "lokuttaraṃ satipaṭṭhānaṃ": LOK + " သတိပဋ္ဌာန်", "paṭṭhānaṃ": "ပဋ္ဌာန်", "sati": "သတိ",
    "padhānaṃ": "ကြိုးပမ်းအားထုတ်ခြင်း", "iddhi": "ဣဒ္ဓိ",
    "lokuttaraṃ iddhipādaṃ": LOK + " ဣဒ္ဓိပါဒ်", "lokuttaraṃ indriyaṃ": LOK + " " + IND,
    "lokuttaraṃ balaṃ": LOK + " " + BAL, "lokuttaraṃ bojjhaṅgaṃ": LOK + " ဗောဇ္ဈင်", "bojjhaṅgaṃ": "ဗောဇ္ဈင်",
    "lokuttaraṃ maggaṃ": LOK + " မဂ်", "lokuttaraṃ saccaṃ": LOK + " သစ္စာ", "saccaṃ": "သစ္စာ",
    "lokuttaraṃ samathaṃ": LOK + " စိတ်ငြိမ်သက်ခြင်း", "samathaṃ": "စိတ်ငြိမ်သက်ခြင်း",
    "lokuttaraṃ dhammaṃ": LOK + " " + DH, "lokuttaraṃ khandhaṃ": LOK + " အစုအဝေး", "khandhaṃ": "အစုအဝေး",
    "lokuttaraṃ āyatanaṃ": LOK + " အာရုံခံ နယ်ပယ်", "āyatanaṃ": "အာရုံခံ နယ်ပယ်",
    "lokuttaraṃ dhātuṃ": LOK + " ဓာတ်", "dhātuṃ": "ဓာတ်",
    "lokuttaraṃ āhāraṃ": LOK + " အာဟာရ", "āhāraṃ": "အာဟာရ",
    "lokuttaraṃ phassaṃ": LOK + " တွေ့ထိမှု", "phassaṃ": "တွေ့ထိမှု",
    "lokuttaraṃ vedanaṃ": LOK + " ခံစားမှု", "vedanaṃ": "ခံစားမှု",
    "lokuttaraṃ saññaṃ": LOK + " " + SANNA, "saññaṃ": SANNA,
    "lokuttaraṃ cetanaṃ": LOK + " စေ့ဆော်မှု", "cetanaṃ": "စေ့ဆော်မှု",
    "lokuttaraṃ cittaṃ": LOK + " စိတ်",
    "vīmaṃsā": "စုံစမ်းဆင်ခြင်မှု", "sukhasahagataṃ": "သာယာမှုနှင့်အတူ ဖြစ်သော",
    # --- headings, colophons
    "Dvādasa": "ဆယ့်နှစ်ပါး", "akusalacittāni": "အကုသိုလ်စိတ်",
    "Abyākatavipāko": ABY + " " + VIP,
    "viññāṇāni": VINN, "vipāka": VIP, "vipākā": VIPA, "Kusalavipāka": "ကုသိုလ်ကံ၏ အကျိုး",
    "Kusalavipākā": "ကုသိုလ်ကံ၏ အကျိုး", "Kusalavipākāni": "ကုသိုလ်ကံ၏ အကျိုး",
    "vipākāni": VIPA, "vipākāni pañcaviññāṇāni": VIPA + " " + VINN + " ငါးပါး",
    "vipākapañcaviññāṇāni": VIPA + " " + VINN + " ငါးပါး",
    "vipākamanodhātu": VIPA + " " + MD, "vipākā manodhātu": VIPA + " " + MD,
    "vipākamanoviññāṇadhātu": [VIPA + " " + MVD, VIPA + " … " + MVD],          # heading «…ဖြစ်သော၊ Q … ဓာတ်»
    "vipākā manoviññāṇadhātu": [VIPA + " " + MVD, VIPA + " … " + MVD],
    "vipākā upekkhāsahagatā manoviññāṇadhātu": VIPA + " " + UPE + "နှင့်အတူ ဖြစ်သော " + MVD,
    "mahāvipākā": "ကြီးကျယ်သော " + VIP,
    "manoviññāṇadhātusomanassasahagatā": SOM + "နှင့်အတူ ဖြစ်သော " + MVD,
    "manoviññāṇadhātu somanassasahagatā": SOM + "နှင့်အတူ ဖြစ်သော " + MVD,
    "manoviññāṇadhātuupekkhāsahagatā": UPE + "နှင့်အတူ ဖြစ်သော " + MVD,
    "manoviññāṇadhātu upekkhāsahagatā": UPE + "နှင့်အတူ ဖြစ်သော " + MVD,
    "dhātusomanassasahagatā": SOM + "နှင့်အတူ ဖြစ်သော ဓာတ်", "dhātu somanassasahagatā": SOM + "နှင့်အတူ ဖြစ်သော ဓာတ်",
    "dhātuupekkhāsahagatā": UPE + "နှင့်အတူ ဖြစ်သော ဓာတ်", "dhātu upekkhāsahagatā": UPE + "နှင့်အတူ ဖြစ်သော ဓာတ်",
    "Lokuttara": LOK, "Suddhika": "သက်သက်", "suddhika": "သက်သက်",
    "Suddhikapaṭipadā": "ကျင့်စဉ် သက်သက်", "suddhikapaṭipadā": "ကျင့်စဉ် သက်သက်",
    "Suddhikaappaṇihitaṃ": "တောင့်တမှု မရှိခြင်း သက်သက်",
    "nayā": "နည်း", "Vīsati": "နှစ်ဆယ်",
    "Akusala": "အကုသိုလ်", "vipākaabyākataṃ": [ABY + " " + VIP, ABY + " … " + VIP],   # «ABY အကုသိုလ်ကံ၏ အကျိုး»
    "kiriyāabyākataṃ": KIR + " " + ABY, "Kiriyā abyākatā": KIR + " " + ABY, "kiriyā abyākatā": KIR + " " + ABY,
    "Kiriyāmano": KIR + " မနော", "Kiriyā mano": KIR + " မနော",
    "Kiriyāmanodhātu": KIR + " " + MD, "Kiriyā manodhātu": KIR + " " + MD,
    "Kiriyāmanoviññāṇa": KIR + " မနော " + VINN, "Kiriyā manoviññāṇa": KIR + " မနော " + VINN,
    "Kiriyāmanoviññāṇadhātu": KIR + " " + MVD, "Kiriyā manoviññāṇadhātu": KIR + " " + MVD,
    "Vipākā abyākatā": VIPA + " " + ABY,
    "Cittuppāda": "စိတ် ဖြစ်ပေါ်ခြင်း", "uppāda": "ဖြစ်ပေါ်ခြင်း", "Citta": "စိတ်", "cittāni": "စိတ်",
    "kaṇḍaṃ": "အခန်း", "niṭṭhitaṃ": "ပြီးဆုံးသော",
}


# =====================================================================================================
# context functions (copied from the sample and extended) and per-segment overrides
# =====================================================================================================
def f_rupa(kw, pali, my):
    """rūpa in rūpāvacara / rūpūpapatti = the fine-material plane «သိမ်မွေ့သော ရုပ်» (sample); as the visible
    object (rūpārammaṇa) = «အဆင်းအရောင်»; elsewhere matter «ရုပ်» (rūpasaññā «ရုပ်ဟု မှတ်သိမှု»). The sample's
    pattern is tightened so that arūpūpapatti / Rūpāvacara (heading, capital R) are read correctly."""
    if re.search(r"(?<![aA])[rR]ūpāvacar|(?<![aA])[rR]ūpūpapatti|(?<![aA])rūparāga", pali):
        return "သိမ်မွေ့သော ရုပ်"
    if re.search(r"rūpārammaṇ", pali):
        return "အဆင်းအရောင်"
    return "ရုပ်"


def f_dukkha(kw, pali, my):
    """dukkha in dukkhapaṭipadā = «ခက်ခဲသော» (difficult progress); elsewhere the painful feeling «နာကျင်မှု»."""
    if "dukkhapaṭipad" in pali:
        return ["ခက်ခဲသော"]
    return ["နာကျင်မှု", "နာကျင်သော"]


def f_sukha(kw, pali, my):
    """sukha in sukhapaṭipadā = «လွယ်ကူသော»; in diṭṭhadhammasukhavihāra = «သာယာစွာ»; elsewhere «သာယာမှု»."""
    if "sukhapaṭipad" in pali:
        return ["လွယ်ကူသော"]
    if "sukhavihār" in pali:
        return ["သာယာစွာ"]
    return ["သာယာမှု", "သာယာသော"]


def f_maggam(kw, pali, my):
    """maggaṃ in «rūpūpapattiyā maggaṃ bhāveti» = the way «လမ်း»; the supramundane path = «မဂ်»."""
    if re.search(r"[uū]papattiyā maggaṃ", pali):
        return "လမ်း"
    return "မဂ်"


FUNCS = {"rupa": f_rupa, "dukkha": f_dukkha, "sukha": f_sukha, "maggam": f_maggam}

CTX = {
    # sid: {keyword: value}
}

# chapter -> its own table (looked up first); the sample tables are the shared fallback
SECTIONS = {
    "2-04-cittuppadakandam": T_CU,
    "2-05-cittuppadakandam": T_CU,
}
CHAPTERS = ["2-04-cittuppadakandam", "2-05-cittuppadakandam"]

SHARED = {}
for _t in (T_PREAMBLE, T_MATIKA):
    for _k, _v in _t.items():
        SHARED.setdefault(_k, _v)


# =====================================================================================================
# dictionary-form rules: the sample's rules 1-11 (approved, copied unchanged) + the new rules of 2-04 / 2-05
# =====================================================================================================
# ---- copied verbatim from map_all.py (approved sample rules 1-11) ----
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


NEW_RULES = """
### New rules for 2-04 / 2-05 (proposed for review)

12. **Absolutives (gerunds) keep the text's «…၍»**: ārabbha = အာရုံပြု၍, paṭicca = အကြောင်းတို့ကို မှီ၍ (with the
    object the text supplies), ṭhapetvā = ချန်ထား၍, upasampajja = ဝင်စား၍, vivicca = ကင်းဆိတ်၍, samatikkamma =
    ကျော်လွန်၍. (The sample normalises «…၍» to «…သော» only for participles, rule 3; an absolutive is not one.)
13. **Relative pronouns** Yo / Yā / Yaṃ = (no direct equivalent): Burmese has no relative pronoun, the clause is built
    by the attributive verb («ထိုအချိန်၌ ရှိသော X»). The correlative **ye** of «ye vā pana … aññepi atthi … dhammā» =
    «ရှိသမျှ» (whatever there are), which carries it; **yaṃ yaṃ** = «မည်သည့်အရာ».
14. **eva** (vivicceva kāmehi) = the text's emphatic suffix «သာ» («ကင်းဆိတ်၍သာ»); **ca** inside a keyword stays as
    the text's «လည်း» (sukhassa ca pahānā = သာယာမှုကိုလည်း ပယ်ခြင်း).
15. **Counts and groups**: a group noun drops the plural and the count the keyword does not have (khandhā = အစုအဝေး,
    āyatanāni = အာရုံခံ နယ်ပယ်, balāni = စွမ်းအား); a keyword with a numeral keeps the text's count (pañcaṅgikaṃ =
    အင်္ဂါ ငါးပါး ရှိသော, tivaṅgiko = အင်္ဂါ သုံးပါး ရှိသော, Dvādasa = ဆယ့်နှစ်ပါး, vipākapañcaviññāṇāni = ကံ၏ အကျိုး
    ဖြစ်သော သိစိတ် ငါးပါး).
16. **Causal ablatives** (-ttā, -ā «because of») drop the postposition «ကြောင့်» like a case particle; the verb keeps
    the participle form of rule 3: katattā = ပြုခဲ့သော (text «ပြုခဲ့၍»), upacitattā = ဆည်းပူးခဲ့သော, bhāvitattā =
    ပွားများခဲ့သော (text «…ခဲ့သောကြောင့်»); samatikkamā = ကျော်လွန်ခြင်း, atthaṅgamā = ချုပ်ငြိမ်းသွားခြင်း,
    vūpasamā = ငြိမ်းသွားခြင်း, pahānā = ပယ်ခြင်း (text «…ခြင်းကြောင့်»).
17. **Purpose datives** keep the text's purpose form «…ရန်»: pahānāya = ပယ်ရန်, pattiyā = ရောက်ရန်, upapattiyā =
    ဖြစ်ပေါ်ရန်, tanubhāvāya = ပါးလျစေရန်, vihāraṃ (diṭṭhadhammasukhavihāraṃ, «… နေထိုင်ရန် ဖြစ်သော») = နေထိုင်ရန်.
18. **Verbs** (rule 4) also come from the text's conjunctive «…၍» and verbal noun «…ခြင်း» (the check accepts them):
    bhāveti = ပွားများသည် (text «ပွားများ၍»), hirīyati = ရှက်သည် (text «မရှက်ခြင်း»: na hirīyati, the positive verb),
    ottappati = ကြောက်ရွံ့သည်; «cittaṃ uppannaṃ» / «dhātu uppannā» are clauses: စိတ် / ဓာတ် ဖြစ်ပေါ်လာသည် (text «…သည်
    ဖြစ်ပေါ်လာသော»). asithila (text «မလျော့ရဲဘဲ») = မလျော့ရဲသော: the negative conjunctive «…ဘဲ» is normalised to
    «…သော» like the endings of rule 3.
19. **«samaye X»** (from «tasmiṃ samaye X») = «အချိန်၌ ရှိသော X», as the 2-01 mapping (its rule 13): the time adverb
    keeps its locative ၌ (rule 11), the attributive ရှိသော by which the text joins it to X stays inside the value,
    ထို (tasmiṃ) goes: samaye phasso = အချိန်၌ ရှိသော တွေ့ထိမှု.
    **nikkhitta** (anikkhittachandatā «ဆန္ဒကို လက်မလွှတ်ခြင်း», anikkhittadhuratā «ဝန်ကို မချထားခြင်း») = လက်လွှတ်သော /
    ချထားသော (two compounds, two Burmese verbs; positive part, rule 8; as 2-01); the check accepts the infixed မ inside
    an attributive stem.
20. **Candidates and discontinuity** (method): where one keyword has two shapes in these chapters, the table lists both
    and the first one found in the segment is taken: literally (a «၊ » of the text counts as a space, rule 6); else by
    the dictionary endings of the presence check; else as two literal pieces at word boundaries, in text order, inside
    one sentence and at most 60 characters apart, joined with « … » (e.g. samuppannā arūpino dhammā = ဖြစ်ပေါ်လာသော ရုပ်
    မဟုတ်သော … သဘောတရား, because the text has «… ရုပ် မဟုတ်သော အခြား သဘောတရားများ»: aññe «အခြား» is not part of the
    keyword; Kiriyāmanoviññāṇadhātu = ပြုရုံမျှသာ ဖြစ်သော … မနော သိစိတ် ဓာတ် in «ပြုရုံမျှသာ ဖြစ်သော၊ ဝမ်းမြောက်မှုနှင့်အတူ
    ဖြစ်သော မနော သိစိတ် ဓာတ်»). Sense by context (rule 11) adds: rūpa as the visible
    object (rūpārammaṇa) = အဆင်းအရောင်, rūpa in rūpasaññā / rūpa- of matter = ရုပ်; dukkha / sukha in dukkha- /
    sukhapaṭipadā = ခက်ခဲသော / လွယ်ကူသော (progress), sukha in diṭṭhadhammasukhavihāra = သာယာစွာ, elsewhere the feeling
    နာကျင်မှု / သာယာမှု; maggaṃ in «rūpūpapattiyā maggaṃ» = လမ်း (the way to rebirth), the supramundane path = မဂ်;
    sātaṃ / asātaṃ = the noun «…မှု» in «cetasikaṃ sātaṃ», the attributive «…သော» in «neva sātaṃ nāsātaṃ» (text
    «… ကောင်းသည်လည်း မဟုတ်»); paṭigha = aversion «မုန်းတီးမှု» (harmonise-notes item 11); suññataṃ / appaṇihitaṃ =
    «…သော» as a jhāna qualifier, «…ခြင်း» in the headings (text «ဆိတ်သုဉ်းခြင်း သက်သက်»).
21. **No direct equivalent** here: the relative pronouns (rule 13) and caya (the fragment of apacaya: the text renders
    apacaya by «လျော့ပါးခြင်း», diminishing, with no word for the accumulation).
"""


# =====================================================================================================
# engine (copied from the sample; lookup extended with candidate lists, «samaye X» and discontinuity)
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
    """-> list of candidates."""
    if v is None:
        return []
    if isinstance(v, list):
        out = []
        for x in v:
            out += resolve(x, kw, pali, my)
        return out
    if v.startswith("@"):
        r = FUNCS[v[1:]](kw, pali, my)
        return [r] if isinstance(r, str) else list(r)
    return [v]


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


def candidates(ch, sid, kw, pali, my):
    o = CTX.get(sid, {})
    for tab in (o, SECTIONS.get(ch, {}), SHARED):
        v = table_get(tab, kw)
        if v is not None:
            return resolve(v, kw, pali, my)
    ws = kw.split()
    if len(ws) >= 2 and low(ws[0]) == "samaye":                       # rule 19
        rest = " ".join(ws[1:])
        cs = candidates(ch, sid, rest, pali, my)
        return [f"အချိန်၌ ရှိသော {c}" for c in cs] + [f"အချိန်၌ … {c}" for c in cs]
    if len(ws) >= 2 and ws[-1] == "dhammā":                           # sample compose (rule 5)
        neg = ws[0] in ("no", "na")
        core = " ".join(ws[1:-1] if neg else ws[:-1])
        out = []
        for base in candidates(ch, sid, core, pali, my):
            if neg:
                base = neg_attr(base)
            if base:
                out.append(base + " " + DH)
        return out
    raise KeyError(kw)


# ---- presence check (sample) + the endings of rule 18 ------------------------------------------------
ATTR_FROM = ("သော်", "၍", "ပြီး", "သည်", "ခြင်း", "သူ", "ပြီ", "ဘဲ")   # dictionary «Xသော» <- text «X»+one of these
VERB_FROM = ("ပါ၏", "၏", "ပြီ", "သော", "၍", "ခြင်း")                 # dictionary «Xသည်» <- text «X»+one of these


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
    if c.endswith("သော") and len(c) > 3:            # infixed မ inside an attributive stem (လက်လွှတ်သော <- လက်မလွှတ်ခြင်း)
        st = c[:-3]
        for i in range(1, len(st)):
            if any(st[:i] + "မ" + st[i:] + e in text for e in ATTR_FROM):
                return "neg-infix"
    return None


def parts(v):
    return [p for p in re.split(r" … | / ", v) if p]


def presence(v, text):
    """-> (ok, [(chunk, rule) for every chunk not found literally])"""
    if v == NONE:
        return True, []
    rules = []
    for part in parts(v):
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


def flat(text):
    """the segment with «၊ » read as a space (rule 6: the «၊» inside a term is dropped)."""
    return text.replace("၊ ", " ")


def literal(v, text):
    t = flat(text)
    return v == NONE or all(p in t for p in parts(v))


def by_endings(v, text):
    """every part present literally or with the dictionary ending of its last word (rules 3, 4, 18)."""
    if v == NONE:
        return True
    text = flat(text)
    for p in parts(v):
        if p in text:
            continue
        if p.endswith("သော") and any(p[:-3] + e in text for e in ATTR_FROM):
            continue
        if p.endswith("သည်") and any(p[:-3] + e in text for e in VERB_FROM):
            continue
        return False
    return True


BOUND = " ၊။–…“”‘’()["


PARTICLES = ("၏", "ကို", "၌", "နှင့်", "မှ", "ဖြင့်", "သည်", "တို့", "များ")
MAXGAP = 60


def auto_split(v, text):
    """a value not found whole -> «A … B» when A and B are found in that order at word boundaries, inside one
    sentence (no «။» between) and at most MAXGAP characters apart; the nearest pair wins, on a tie the longer A."""
    if v == NONE or " … " in v or " / " in v:
        return None
    t = flat(text)
    w = v.split()
    best = None
    for k in range(1, len(w)):
        a, b = " ".join(w[:k]), " ".join(w[k:])
        for m in re.finditer(re.escape(a), t):
            e = m.end()
            if m.start() > 0 and t[m.start() - 1] not in BOUND:
                continue
            if e < len(t) and t[e] not in BOUND and not t[e:].startswith(PARTICLES):
                continue
            j = t.find(b, e + 1)
            while j >= 0 and t[j - 1] != " ":
                j = t.find(b, j + 1)
            if j < 0 or "။" in t[e:j] or j - e > MAXGAP:
                continue
            key = (j - e, -k)
            if best is None or key < best[0]:
                best = (key, f"{a} … {b}")
    return best[1] if best else None


def choose(cs, text):
    for c in cs:
        if literal(c, text):
            return c
    for c in cs:
        if by_endings(c, text):
            return c
    for c in cs:
        s = auto_split(c, text)
        if s:
            return s
    for c in cs:
        if presence(c, text)[0]:
            return c
    return cs[0]


def lookup(ch, sid, kw, pali, my):
    cs = candidates(ch, sid, kw, pali, my)
    if not cs:
        raise KeyError(kw)
    return choose(cs, my)


def load(ch):
    my = segments(MY / f"{ch}.md")
    pa = segments(PI / f"{ch}.md")
    rows = [LINE.match(l).groups() for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()
            if LINE.match(l)]
    return my, pa, rows


def map_line(ch, sid, kws, pa, my, unmapped=None, problems=None):
    pairs, vals = [], {}
    for kw in [k.strip() for k in kws.split(", ")]:
        if kw in vals:                          # repeats inside a line get the same value
            v = vals[kw]
        else:
            try:
                v = lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
            except KeyError:
                if unmapped is not None:
                    unmapped[kw].append((ch, sid))
                v = "?"
            else:
                ok, _ = presence(v, my[sid])
                if not ok and problems is not None:
                    problems.append((ch, sid, kw, v))
            vals[kw] = v
        pairs.append((kw, v))
    return pairs


def run(write=True):
    table = collections.defaultdict(collections.Counter)
    unmapped = collections.defaultdict(list)
    problems, summary = [], []
    for ch in CHAPTERS:
        my, pa, rows = load(ch)
        lines, nne = [], 0
        for sid, kws in rows:
            pairs = map_line(ch, sid, kws, pa, my, unmapped, problems)
            for kw, v in pairs:
                table[kw][v] += 1
                nne += v == NONE
            lines.append(f"[{sid}] " + ", ".join(f"{k}={v}" for k, v in pairs))
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
    # repeats: the same keyword inside one line has one value
    rep = []
    for i, y in b:
        d = {}
        for kv in y.split(", "):
            k, v = kv.split("=", 1)
            if d.setdefault(k, v) != v:
                rep.append((i, k))
    return len(a), bad, fails, punct, ruled, rep


def write_table(table, ruled_all):
    with open(TABLE_OUT, "w", encoding="utf-8") as f:
        f.write("# pi-1 Burmese keyword mapping: rules and review table, chapters 2-04 / 2-05 (Cittuppādakaṇḍa)\n\n")
        f.write("Written by map_2-04-05.py (a copy of the sample mapper map_all.py with the tables of these chapters). "
                "Burmese from the FINAL text of this track only "
                "(AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters).\n\n")
        f.write("Rules 1-11 are the approved sample rules (map-table.md, unchanged); rules 12-21 are new.\n\n")
        f.write(RULES)
        f.write(NEW_RULES)
        f.write("\n## Presence: chunks matched by a dictionary-form rule (not literally in the segment)\n\n")
        f.write("Every other chunk of every value occurs literally in its segment's Burmese (particles that the "
                "rules strip follow the chunk in the text). Grouped by keyword and chunk.\n\n"
                "| keyword | chunk | rule | segments |\n|---|---|---|---|\n")
        grp = collections.OrderedDict()
        for sid, k, c, r in ruled_all:
            grp.setdefault((k, c, r), []).append(sid)
        for (k, c, r), sids in grp.items():
            sh = ", ".join(sids[:4]) + (f" … ({len(sids)})" if len(sids) > 4 else "")
            f.write(f"| {k} | {c} | {r} | {sh} |\n")
        f.write("\n## Keyword → Burmese (number of uses), 2-04 and 2-05\n\nSeveral values = the keyword reads "
                "differently by context (or is discontinuous in some segments).\n\n"
                "| Pāli keyword | Burmese (uses) |\n|---|---|\n")
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
                    for kw, v in map_line(ch, sid, kws, pa, my):
                        print(kw, "=", v, presence(v, my[sid]) if v != "?" else "??")
        sys.exit()
    if args and args[0] == "--loose":
        # values whose parts are not found whole in the segment (only chunk by chunk): listed for a manual review
        seen = collections.Counter()
        for ch in CHAPTERS:
            my, pa, rows = load(ch)
            for sid, kws in rows:
                for kw, v in map_line(ch, sid, kws, pa, my):
                    if v != NONE and not by_endings(v, my[sid]):
                        seen[(kw, v)] += 1
        for (kw, v), n in sorted(seen.items()):
            print(f"{kw} = {v}  ({n})")
        sys.exit()
    if args and args[0] == "--compare":
        # read-only: keywords shared with other chapters' mapped files (args[1:]) whose values differ
        def vals(names):
            d = collections.defaultdict(collections.Counter)
            for n in names:
                p = HERE / n
                if not p.exists():
                    continue
                for l in p.read_text(encoding="utf-8").splitlines():
                    m = LINE.match(l)
                    if m:
                        for kv in m.group(2).split(", "):
                            k, v = kv.split("=", 1)
                            d[k][v] += 1
            return d
        mine = vals(f"{c}.mapped.md" for c in CHAPTERS)
        other = vals(args[1:])
        for k in sorted(set(mine) & set(other)):
            if set(mine[k]) != set(other[k]):
                print(f"{k}\n   here : {dict(mine[k])}\n   other: {dict(other[k])}")
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
    ruled_all, tot_nne, results = [], 0, []
    for ch, n, nne in summary:
        ln, bad, fails, punct, ruled, rep = verify(ch)
        ruled_all += ruled
        tot_nne += nne
        results.append((ch, ln, bad, fails, punct, ruled, nne, rep))
    write_table(table, ruled_all)
    for ch, ln, bad, fails, punct, ruled, nne, rep in results:
        print(f"{ch}: lines {ln} | keyword preservation bad {bad} | presence failures {len(fails)} "
              f"(rule-matched chunks {len(ruled)}) | comma/၊ {punct} | repeats differing {rep} | no-equivalent {nne}")
        for f_ in fails:
            print("   FAIL", f_)
    print("total no direct equivalent:", tot_nne, "| distinct keywords:", len(table))
