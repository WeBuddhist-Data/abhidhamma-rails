"""Shared Burmese (Myanmar) formulas for pi-1 (Dhammasaṅgaṇī, «သဘောတရားများကို စုစည်းရေတွက်ခြင်း»), plain audience.

First Burmese text in the vault (sample: preamble + 1-matika, 2026-11-16). Every later Burmese generator imports this
module, so that identical Pāli always gets identical Burmese. Writes no files at import. It holds:
  * the book frame (NAMO, ABHI, TITLE, NITTHITA, PE) and the word for dhamma = phenomenon (DHAMMA);
  * headings and colophon sentences (HEAD, COLO);
  * variant readings (SIGLA, PATHA / LEKHANA labels, VAR_KIND, var_my);
  * item letters (LABEL) and number words (NUM, ORD, TIKA, DUKA: proposed for later chapters);
  * the mātikā tables: TERMS (triad / dyad term, Pāli nominative plural surface without «dhammā» -> Burmese
    attributive phrase, normally ending in «သော»), the gocchaka FAMILY pattern that builds the six dyads of each
    cluster and its «ceva» forms (CEVA, CEVANO), KHO_PANA, nominal() for the «-pi» members, SUT (suttantika
    «X ca» / «Xñca» items), MFIXED (suttantika lines that are phrases);
  * the engine: translate() -> line_my() -> heading / mātikā line / colophon. Any line no rule matches raises Miss:
    nothing is ever guessed.

Negation rule (checked by check_sample.py): a free Pāli «na / no / neva» that negates a whole term becomes
«… မဟုတ်» («not (being) …», built with no_()); a privative «a- / an-» becomes «မ» before the verb («မရှိ», «မဖြစ်»,
«မမြင်နိုင်»). «vippayutta» is not a negation: «နှင့် ကင်းကွာသော» (separated from).
Later chapters: import this module, add their own entries to HEAD / COLO / TERMS / SUT / VAR_KIND …, or add
(regex, function) pairs to EXTRA_RULES. Do not change existing strings without the user's approval.
"""
import re


class Miss(Exception):
    """A Pāli line or fragment that no rule or table entry matches."""


# ===================================================================================== book frame
NAMO = "ထိုမြတ်စွာဘုရား၊ ရဟန္တာ၊ အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်အား ရှိခိုးပါ၏"
#      Namo tassa bhagavato arahato sammāsambuddhassa (no full stop, as in the Pāli)
ABHI = "အဘိဓမ္မာပိဋကတွင်"                       # Abhidhammapiṭake ("in the Abhidhamma Piṭaka")
TITLE = "သဘောတရားများကို စုစည်းရေတွက်ခြင်း"       # Dhammasaṅgaṇīpāḷi (book title, Burmese only)
NITTHITA = "ပြီးဆုံးပြီ"                           # niṭṭhitā / niṭṭhitaṃ
PE = "…"                                        # …pe… and …Pe… = one «…»
END = "။"                                       # full stop of a statement / list item
COMMA = "၊"

# dhamma = phenomenon / state (not «the Teaching»): «သဘောတရား»; rejected: bare «တရား» (reads as the Teaching,
# a sermon), «ဓမ္မ» (Pāli), «ဖြစ်စဉ်» (event / process), «အရာ» (any thing)
DHAMMA = "သဘောတရား"
DHAMMA_PL = "သဘောတရားများ"                      # dhammā after a mātikā term
DHAMMA_AMONG = "သဘောတရားများအနက်"              # «X kho pana dhammā …» = among the X phenomena
DHAMMA_LOC = "သဘောတရားတို့၌"                    # dhammesu

# ===================================================================================== numbers (proposed)
TIKA, DUKA = "သုံးမျိုးတွဲ", "နှစ်မျိုးတွဲ"            # tika (triad) / duka (dyad)
NUM = {"eka": "တစ်", "dvi": "နှစ်", "ti": "သုံး", "catu": "လေး", "pañca": "ငါး", "cha": "ခြောက်",
       "satta": "ခုနစ်", "aṭṭha": "ရှစ်", "nava": "ကိုး", "dasa": "ဆယ်"}
ORD = {"paṭhama": "ပထမ", "dutiya": "ဒုတိယ", "tatiya": "တတိယ", "catuttha": "စတုတ္ထ", "pañcama": "ပဉ္စမ",
       "chaṭṭha": "ဆဋ္ဌမ", "sattama": "သတ္တမ", "aṭṭhama": "အဋ္ဌမ"}

# ===================================================================================== item letters
LABEL = {"(Ka)": "(က)", "(Kha)": "(ခ)", "(Ga)": "(ဂ)", "(Gha)": "(ဃ)", "(Ṅa)": "(င)"}

# ===================================================================================== variant readings
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "pī.": "Pī.", "kaṃ.": "Kaṃ.", "?": "?"}
PATHA, LEKHANA = "ပါဌ်ကွဲ", "စာလုံးပေါင်းကွဲ"       # a different word / spelling only
VAR_KIND = {
    "upādinnupādāniyā": LEKHANA, "anupādinnānupādāniyā": LEKHANA, "asaṃkiliṭṭhāsaṃkilesikā": LEKHANA,
    "avitakkāvicārā": LEKHANA, "nevācayagāmino nāpacayagāmino": LEKHANA, "nevasekkhānāsekkhā": LEKHANA,
    "anidassanāppaṭighā": LEKHANA, "upādinnā": LEKHANA, "paṭisandhāro ca": LEKHANA,
    "suttantamātikā": PATHA,
}
VAR_RE = re.compile(r"\[(?P<t>[^\[\]()]+?) \((?P<s>[^()]+)\)\]")


def var_my(br):
    """«[upādinnā (sī. syā.)]» -> «[စာလုံးပေါင်းကွဲ (Sī., Syā.): upādinnā]»."""
    m = VAR_RE.fullmatch(br)
    if not m or m["t"] not in VAR_KIND:
        raise Miss("variant: " + br)
    sig = ", ".join(SIGLA[s] for s in m["s"].split())
    return f"[{VAR_KIND[m['t']]} ({sig}): {m['t']}]"


# ===================================================================================== mātikā building blocks
SAMP = "နှင့် ယှဉ်တွဲသော"       # -sampayutta (N + «နှင့် ယှဉ်တွဲသော» = conjoined with N)
VIPP = "နှင့် ကင်းကွာသော"        # -vippayutta (separated from N; not a negation)
OBJ = "၏ အာရုံ ဖြစ်နိုင်သော"     # -iya / sa- of a cluster (sāsava, saṃyojaniya …) = can be the object of N
NOBJ = "၏ အာရုံ မဖြစ်နိုင်သော"   # a-…-iya / an-āsava = cannot be the object of N
OBJ_HI = "၏ အာရုံလည်း ဖြစ်နိုင်သော"
SAMP_HI = "နှင့်လည်း ယှဉ်တွဲသော"
IS, ISNOT = " ဖြစ်သော", " မဟုတ်သော"   # X dhammā (N itself) / no X, na X
TOGETHER = "နှင့်အတူ ဖြစ်သော"   # -sahagata
DASS = "သစ္စာကို မြင်ခြင်းဖြင့်"   # dassanena (by seeing the truth)
BHAV = "ဘာဝနာ ပွားများခြင်းဖြင့်"   # bhāvanāya (by developing the mind)
PAH = "ပယ်ရမည့်"                  # pahātabba (to be abandoned), attributive
PAH_S = "ပယ်ရမည်"                 # pahātabba, before «မဟုတ်»
ROOT = "အမြစ်"                    # hetu (root)
VIT, VIC = "စတင်ကြံစည်မှု", "ဆက်လက်သုံးသပ်မှု"   # vitakka (initial thinking) / vicāra (continued examining)
SUKHA, DUKKHA = "သာယာ", "နာကျင်"               # sukha / dukkha (adjective stems)
FEEL = "ခံစားမှု"                                # vedanā
KAMMA_BORN = "ကံကြောင့် ဖြစ်"                    # upādiṇṇa (produced by kamma), verb stem
UPA = "စွဲလမ်းမှု"                              # upādāna (clinging)
KIL = "ကိလေသာ"                                 # kilesa (defilement)
KIL_SOIL = "ကိလေသာဖြင့် ညစ်နွမ်း"                # saṃkiliṭṭha, verb stem
SEE, IMPACT = "မြင်နိုင်", "ထိခိုက်မှု"            # sanidassana (visible) / paṭigha (impact)
MIND = "စိတ်"                                   # citta
TAKES = "ကို အာရုံပြုသော"                        # -ārammaṇa (taking … as object)


def no_(x):
    """Free «na / no» before a verb-phrase term: «… သော» -> «… သည် မဟုတ်သော» (not (being) …)."""
    if not x.endswith("သော"):
        raise Miss("no_: " + x)
    return x[:-3] + "သည် မဟုတ်သော"


def nominal(x):
    """Attributive «… သော» -> nominal «… သည်တို့» (those that …), for the «-pi» members."""
    if not x.endswith("သော"):
        raise Miss("nominal: " + x)
    return x[:-3] + "သည်တို့"


# ===================================================================================== mātikā terms
TERMS = {
    # ---- triads
    "kusalā": "ကုသိုလ်", "akusalā": "အကုသိုလ်",
    "abyākatā": "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော",
    "sukhāya vedanāya sampayuttā": f"{SUKHA}သော {FEEL}{SAMP}",
    "dukkhāya vedanāya sampayuttā": f"{DUKKHA}သော {FEEL}{SAMP}",
    "adukkhamasukhāya vedanāya sampayuttā": f"မ{DUKKHA} မ{SUKHA}သော {FEEL}{SAMP}",
    "vipākā": "ကံ၏ အကျိုး ဖြစ်သော", "vipākadhammadhammā": "အကျိုး ပေးတတ်သော",
    "nevavipākanavipākadhammadhammā": "ကံ၏ အကျိုးလည်း မဟုတ်၊ အကျိုး ပေးတတ်သည်လည်း မဟုတ်သော",
    "upādiṇṇupādāniyā": f"{KAMMA_BORN}၍ {UPA}{OBJ_HI}",
    "anupādiṇṇupādāniyā": f"{KAMMA_BORN.replace(' ဖြစ်', ' မဖြစ်')}သော်လည်း {UPA}{OBJ}",
    "anupādiṇṇaanupādāniyā": f"ကံကြောင့်လည်း မဖြစ်၊ {UPA}၏ အာရုံလည်း မဖြစ်နိုင်သော",
    "saṃkiliṭṭhasaṃkilesikā": f"{KIL_SOIL}၍ {KIL}{OBJ_HI}",
    "asaṃkiliṭṭhasaṃkilesikā": f"{KIL}ဖြင့် မညစ်နွမ်းသော်လည်း {KIL}{OBJ}",
    "asaṃkiliṭṭhaasaṃkilesikā": f"{KIL}ဖြင့်လည်း မညစ်နွမ်း၊ {KIL}၏ အာရုံလည်း မဖြစ်နိုင်သော",
    "savitakkasavicārā": f"{VIT}နှင့် {VIC} ရှိသော",
    "avitakkavicāramattā": f"{VIT} မရှိဘဲ {VIC}သာ ရှိသော",
    "avitakkaavicārā": f"{VIT}လည်း မရှိ၊ {VIC}လည်း မရှိသော",
    "pītisahagatā": f"ပီတိ{TOGETHER}", "sukhasahagatā": f"{SUKHA}မှု{TOGETHER}",
    "upekkhāsahagatā": f"ဥပေက္ခာ{TOGETHER}",
    "dassanena pahātabbā": f"{DASS} {PAH}", "bhāvanāya pahātabbā": f"{BHAV} {PAH}",
    "neva dassanena na bhāvanāya pahātabbā":
        f"{DASS}လည်း {PAH_S} မဟုတ်၊ {BHAV}လည်း {PAH_S} မဟုတ်သော",
    "dassanena pahātabbahetukā": f"{DASS} {PAH} {ROOT} ရှိသော",
    "bhāvanāya pahātabbahetukā": f"{BHAV} {PAH} {ROOT} ရှိသော",
    "neva dassanena na bhāvanāya pahātabbahetukā":
        f"{DASS}လည်း {PAH} {ROOT} ရှိသည် မဟုတ်၊ {BHAV}လည်း {PAH} {ROOT} ရှိသည် မဟုတ်သော",
    "ācayagāmino": "စုပုံခြင်းဆီသို့ ဦးတည်သော", "apacayagāmino": "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော",
    "nevācayagāmināpacayagāmino":
        "စုပုံခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်သော",
    "sekkhā": "ကျင့်ကြံဆဲသူ၏", "asekkhā": "ကျင့်ကြံမှု ပြီးဆုံးသူ၏",
    "nevasekkhanāsekkhā": "ကျင့်ကြံဆဲသူ၏လည်း မဟုတ်၊ ကျင့်ကြံမှု ပြီးဆုံးသူ၏လည်း မဟုတ်သော",
    "parittā": "အကန့်အသတ် ရှိသော", "mahaggatā": "ကြီးမြတ်သော", "appamāṇā": "အတိုင်းအဆ မရှိသော",
    "parittārammaṇā": f"အကန့်အသတ် ရှိသည်{TAKES}", "mahaggatārammaṇā": f"ကြီးမြတ်သည်{TAKES}",
    "appamāṇārammaṇā": f"အတိုင်းအဆ မရှိသည်{TAKES}",
    "hīnā": "ယုတ်ညံ့သော", "majjhimā": "အလယ်အလတ်", "paṇītā": "မွန်မြတ်သော",
    "micchattaniyatā": "မှားယွင်းမှု၌ ကျိန်းသေသော", "sammattaniyatā": "မှန်ကန်မှု၌ ကျိန်းသေသော",
    "aniyatā": "မကျိန်းသေသော",
    "maggārammaṇā": f"မဂ်{TAKES}", "maggahetukā": "မဂ်ကို အမြစ်ပြုသော",
    "maggādhipatino": "မဂ်ကို အကြီးအမှူးပြုသော",
    "uppannā": "ဖြစ်ပေါ်ပြီးသော", "anuppannā": "မဖြစ်ပေါ်သေးသော", "uppādino": "ဖြစ်ပေါ်လာမည့်",
    "atītā": "အတိတ်", "anāgatā": "အနာဂတ်", "paccuppannā": "ပစ္စုပ္ပန်",
    "atītārammaṇā": f"အတိတ်{TAKES}", "anāgatārammaṇā": f"အနာဂတ်{TAKES}",
    "paccuppannārammaṇā": f"ပစ္စုပ္ပန်{TAKES}",
    "ajjhattā": "မိမိ၌ ရှိသော", "bahiddhā": "သူတစ်ပါး၌ ရှိသော",
    "ajjhattabahiddhā": "မိမိ၌နှင့် သူတစ်ပါး၌ ရှိသော",
    "ajjhattārammaṇā": f"မိမိ၌ ရှိသည်{TAKES}", "bahiddhārammaṇā": f"သူတစ်ပါး၌ ရှိသည်{TAKES}",
    "ajjhattabahiddhārammaṇā": f"မိမိ၌နှင့် သူတစ်ပါး၌ ရှိသည်{TAKES}",
    "sanidassanasappaṭighā": f"{SEE}၍ {IMPACT}လည်း ရှိသော",
    "anidassanasappaṭighā": f"မ{SEE}သော်လည်း {IMPACT} ရှိသော",
    "anidassanaappaṭighā": f"မ{SEE}၊ {IMPACT}လည်း မရှိသော",
    # ---- hetu cluster (the cluster frame of FAMILY with «hetu» = root, special Y = sahetuka)
    "hetū": f"{ROOT}{IS}", "na hetū": f"{ROOT}{ISNOT}",
    "sahetukā": f"{ROOT} ရှိသော", "ahetukā": f"{ROOT} မရှိသော",
    "hetusampayuttā": f"{ROOT}{SAMP}", "hetuvippayuttā": f"{ROOT}{VIPP}",
    # ---- cūḷantara
    "sappaccayā": "အကြောင်း ရှိသော", "appaccayā": "အကြောင်း မရှိသော",
    "saṅkhatā": "ပြုပြင်ဖန်တီးထားသော", "asaṅkhatā": "ပြုပြင်ဖန်တီးထားခြင်း မရှိသော",
    "sanidassanā": f"{SEE}သော", "anidassanā": f"မ{SEE}သော",
    "sappaṭighā": f"{IMPACT} ရှိသော", "appaṭighā": f"{IMPACT} မရှိသော",
    "rūpino": "ရုပ်" + IS, "arūpino": "ရုပ်" + ISNOT,
    "lokiyā": "လောကနှင့် သက်ဆိုင်သော", "lokuttarā": "လောကကို ကျော်လွန်သော",
    "kenaci viññeyyā": "တစ်စုံတစ်ခုသော စိတ်ဖြင့် သိနိုင်သော",
    "kenaci na viññeyyā": "တစ်စုံတစ်ခုသော စိတ်ဖြင့် မသိနိုင်သော",
    # ---- mahantara
    "sārammaṇā": "အာရုံ ရှိသော", "anārammaṇā": "အာရုံ မရှိသော",
    "cittā": MIND + IS, "no cittā": MIND + ISNOT,
    "cetasikā": f"{MIND}၏ အဖော်{IS}", "acetasikā": f"{MIND}၏ အဖော်{ISNOT}",
    "cittasampayuttā": MIND + SAMP, "cittavippayuttā": MIND + VIPP,
    "cittasaṃsaṭṭhā": f"{MIND}နှင့် ရောနှောသော", "cittavisaṃsaṭṭhā": f"{MIND}နှင့် မရောနှောသော",
    "cittasamuṭṭhānā": f"{MIND}မှ ဖြစ်ပေါ်လာသော",
    "cittasahabhuno": f"{MIND}နှင့်အတူ တည်ရှိသော",
    "cittānuparivattino": f"{MIND}နောက်သို့ လိုက်ပါသော",
    "cittasaṃsaṭṭhasamuṭṭhānā": f"{MIND}နှင့် ရောနှော၍ {MIND}မှ ဖြစ်ပေါ်လာသော",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhuno":
        f"{MIND}နှင့် ရောနှော၍ {MIND}မှ ဖြစ်ပေါ်လာပြီး {MIND}နှင့်အတူ တည်ရှိသော",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivattino":
        f"{MIND}နှင့် ရောနှော၍ {MIND}မှ ဖြစ်ပေါ်လာပြီး {MIND}နောက်သို့ လိုက်ပါသော",
    "ajjhattikā": "အတွင်းပိုင်း", "bāhirā": "ပြင်ပ",
    "upādā": "မူလဓာတ်ကြီးများကို မှီ၍ ဖြစ်သော",
    "upādiṇṇā": f"{KAMMA_BORN}သော", "anupādiṇṇā": "ကံကြောင့် မဖြစ်သော",
    # ---- kilesa cluster (FAMILY frame plus saṃkiliṭṭha)
    "saṃkiliṭṭhā": f"{KIL_SOIL}သော", "asaṃkiliṭṭhā": f"{KIL}ဖြင့် မညစ်နွမ်းသော",
    # ---- piṭṭhiduka
    "savitakkā": f"{VIT} ရှိသော", "avitakkā": f"{VIT} မရှိသော",
    "savicārā": f"{VIC} ရှိသော", "avicārā": f"{VIC} မရှိသော",
    "sappītikā": "ပီတိ ရှိသော", "appītikā": "ပီတိ မရှိသော",
    "kāmāvacarā": "ကာမဘုံနှင့် ဆိုင်သော", "rūpāvacarā": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော",
    "arūpāvacarā": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော",
    "pariyāpannā": "ဘဝဘုံတို့၌ အကျုံးဝင်သော", "apariyāpannā": "ဘဝဘုံတို့၌ အကျုံးမဝင်သော",
    "niyyānikā": "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော", "aniyyānikā": "လွတ်မြောက်ရာသို့ မပို့ဆောင်သော",
    "niyatā": "ကျိန်းသေသော",
    "sauttarā": "ထိုထက် သာလွန်သည် ရှိသေးသော", "anuttarā": "ထိုထက် သာလွန်သည် မရှိသော",
    "saraṇā": "ပဋိပက္ခ ရှိသော", "araṇā": "ပဋိပက္ခ မရှိသော",
    # ---- suttantika dyads with «dhammā»
    "vijjābhāgino": "အမှန်သိမြင်မှု၏ အစိတ်အပိုင်း ဖြစ်သော",
    "avijjābhāgino": "အမှန်ကို မသိမှု၏ အစိတ်အပိုင်း ဖြစ်သော",
    "vijjūpamā": "လျှပ်စီးနှင့် တူသော", "vajirūpamā": "စိန်နှင့် တူသော",
    "bālā": "မိုက်မဲသော", "paṇḍitā": "ပညာရှိသော", "kaṇhā": "မည်းနက်သော", "sukkā": "ဖြူစင်သော",
    "tapanīyā": "ပူပန်စေတတ်သော", "atapanīyā": "မပူပန်စေတတ်သော",
    "adhivacanā": "အမည်ခေါ်ဝေါ်မှု ဖြစ်သော", "adhivacanapathā": "အမည်ခေါ်ဝေါ်မှု၏ လမ်းကြောင်း ဖြစ်သော",
    "nirutti": "စကားဖြင့် ဖော်ပြမှု ဖြစ်သော", "niruttipathā": "စကားဖြင့် ဖော်ပြမှု၏ လမ်းကြောင်း ဖြစ်သော",
    "paññatti": "သတ်မှတ်ချက် ဖြစ်သော", "paññattipathā": "သတ်မှတ်ချက်၏ လမ်းကြောင်း ဖြစ်သော",
}
# free «na / no» before a whole verb-phrase term: «… သည် မဟုတ်သော»
for _k in ["cittasamuṭṭhānā", "cittasahabhuno", "cittānuparivattino", "cittasaṃsaṭṭhasamuṭṭhānā",
           "cittasaṃsaṭṭhasamuṭṭhānasahabhuno", "cittasaṃsaṭṭhasamuṭṭhānānuparivattino", "upādā"]:
    TERMS["no " + _k] = no_(TERMS[_k])
for _k in ["dassanena pahātabbahetukā", "bhāvanāya pahātabbahetukā", "pītisahagatā", "sukhasahagatā",
           "upekkhāsahagatā", "kāmāvacarā", "rūpāvacarā", "arūpāvacarā"]:
    TERMS["na " + _k] = no_(TERMS[_k])
TERMS["na dassanena pahātabbā"] = f"{DASS} {PAH_S} မဟုတ်သော"     # «ပယ်ရမည့်» is not a «သော» form
TERMS["na bhāvanāya pahātabbā"] = f"{BHAV} {PAH_S} မဟုတ်သော"

# the gocchaka clusters: Pāli stem -> Burmese noun N, and the Pāli of the «object of N» word and its negative
# (sāsava / anāsava, saṃyojaniya / asaṃyojaniya …; parāmaṭṭha / aparāmaṭṭha; saṃkilesika / asaṃkilesika)
FAMILY = {
    "āsava": dict(N="စိတ်အစွန်းအထင်း", y="sāsavā", ny="anāsavā"),
    "saṃyojana": dict(N="နှောင်ကြိုး", y="saṃyojaniyā", ny="asaṃyojaniyā"),
    "gantha": dict(N="အထုံး", y="ganthaniyā", ny="aganthaniyā"),
    "ogha": dict(N="ရေအလျဉ်", y="oghaniyā", ny="anoghaniyā"),
    "yoga": dict(N="ထမ်းပိုး", y="yoganiyā", ny="ayoganiyā"),
    "nīvaraṇa": dict(N="အတားအဆီး", y="nīvaraṇiyā", ny="anīvaraṇiyā"),
    "parāmāsa": dict(N="မှားယွင်းသော ယူဆမှု", y="parāmaṭṭhā", ny="aparāmaṭṭhā"),
    "upādāna": dict(N=UPA, y="upādāniyā", ny="anupādāniyā"),
    "kilesa": dict(N=KIL, y="saṃkilesikā", ny="asaṃkilesikā"),
}
CEVA = {}        # (X, Y) of «X ceva dhammā Y ca» -> Burmese (both X and Y)
CEVANO = {}      # (Y, X) of «Y ceva dhammā no / na ca X» -> Burmese (Y but not X)


def _families():
    for st, d in FAMILY.items():
        N = d["N"]
        x = st[:-1] + "ā"
        sp, vp = st + "sampayuttā", st + "vippayuttā"
        TERMS.update({x: N + IS, "no " + x: N + ISNOT, d["y"]: N + OBJ, d["ny"]: N + NOBJ,
                      sp: N + SAMP, vp: N + VIPP})
        CEVA[(x, d["y"])] = f"{N}လည်း ဖြစ်၊ {N}{OBJ_HI}"
        CEVANO[(d["y"], x)] = f"{N}၏ အာရုံ ဖြစ်နိုင်သော်လည်း {N}{ISNOT}"
        CEVA[(x, sp)] = f"{N}လည်း ဖြစ်၊ {N}{SAMP_HI}"
        CEVANO[(sp, x)] = f"{N}နှင့် ယှဉ်တွဲသော်လည်း {N}{ISNOT}"


_families()
CEVA.update({
    ("hetū", "sahetukā"): f"{ROOT}လည်း ဖြစ်၊ {ROOT}လည်း ရှိသော",
    ("hetū", "hetusampayuttā"): f"{ROOT}လည်း ဖြစ်၊ {ROOT}{SAMP_HI}",
    ("kilesā", "saṃkiliṭṭhā"): f"{KIL}လည်း ဖြစ်၊ {KIL}ဖြင့်လည်း ညစ်နွမ်းသော",
})
CEVANO.update({
    ("sahetukā", "hetū"): f"{ROOT} ရှိသော်လည်း {ROOT}{ISNOT}",
    ("hetusampayuttā", "hetū"): f"{ROOT}နှင့် ယှဉ်တွဲသော်လည်း {ROOT}{ISNOT}",
    ("saṃkiliṭṭhā", "kilesā"): f"{KIL_SOIL}သော်လည်း {KIL}{ISNOT}",
})
KHO_PANA = "ထို့ပြင်"          # «X kho pana dhammā Ypi.» = «ထို့ပြင် X သဘောတရားများအနက် Y-သည်တို့လည်း။»
PI = "လည်း"                  # -pi (also) on a mātikā member

# suttantika «X ca» / «Xñca» items: Pāli X (without «ca» / «ñca») -> Burmese; the listing «ca» is not rendered
SUT = {
    "nāma": "စိတ်ပိုင်း", "rūpa": "ရုပ်ပိုင်း", "avijjā": "အမှန်ကို မသိမှု", "bhavataṇhā": "ဘဝကို တပ်မက်မှု",
    "bhavadiṭṭhi": "ဘဝ ဆက်လက် တည်ရှိသည်ဟူသော အယူ", "vibhavadiṭṭhi": "ဘဝ ပျောက်ကွယ်သည်ဟူသော အယူ",
    "sassatadiṭṭhi": "အတ္တသည် ထာဝရ တည်မြဲသည်ဟူသော အယူ",
    "ucchedadiṭṭhi": "အတ္တသည် သေပြီးနောက် ပြတ်စဲသွားသည်ဟူသော အယူ",
    "antavā diṭṭhi": "လောကသည် အဆုံး ရှိသည်ဟူသော အယူ", "anantavā diṭṭhi": "လောကသည် အဆုံး မရှိဟူသော အယူ",
    "pubbantānudiṭṭhi": "အတိတ်နှင့် ပတ်သက်သော အယူ", "aparantānudiṭṭhi": "အနာဂတ်နှင့် ပတ်သက်သော အယူ",
    "ahirika": "ဒုစရိုက်ကို မရှက်မှု", "anottappa": "ဒုစရိုက်ကို မကြောက်ရွံ့မှု",
    "hirī": "ဒုစရိုက်ကို ရှက်မှု", "ottappa": "ဒုစရိုက်ကို ကြောက်ရွံ့မှု",
    "dovacassatā": "သွန်သင်ချက်ကို နားမထောင်ခြင်း", "pāpamittatā": "မိတ်ဆွေဆိုးနှင့် ပေါင်းသင်းခြင်း",
    "sovacassatā": "သွန်သင်ချက်ကို နားထောင်ခြင်း", "kalyāṇamittatā": "မိတ်ဆွေကောင်းနှင့် ပေါင်းသင်းခြင်း",
    "āpattikusalatā": "အပြစ်တို့၌ ကျွမ်းကျင်ခြင်း",
    "āpattivuṭṭhānakusalatā": "အပြစ်မှ ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း",
    "samāpattikusalatā": "ဈာန် ဝင်စားရာ၌ ကျွမ်းကျင်ခြင်း",
    "samāpattivuṭṭhānakusalatā": "ဈာန်မှ ထမြောက်ရာ၌ ကျွမ်းကျင်ခြင်း",
    "dhātukusalatā": "ဓာတ်တို့၌ ကျွမ်းကျင်ခြင်း", "manasikārakusalatā": "နှလုံးသွင်းခြင်း၌ ကျွမ်းကျင်ခြင်း",
    "āyatanakusalatā": "အာရုံခံ နယ်ပယ်တို့၌ ကျွမ်းကျင်ခြင်း",
    "paṭiccasamuppādakusalatā": "အကြောင်းအကျိုး ဆက်စပ်ဖြစ်ပေါ်ပုံ၌ ကျွမ်းကျင်ခြင်း",
    "ṭhānakusalatā": "ဖြစ်နိုင်သည့်အရာ၌ ကျွမ်းကျင်ခြင်း", "aṭṭhānakusalatā": "မဖြစ်နိုင်သည့်အရာ၌ ကျွမ်းကျင်ခြင်း",
    "ajjavo": "ဖြောင့်မတ်ခြင်း", "maddavo": "နူးညံ့ခြင်း", "khanti": "သည်းခံခြင်း", "soracca": "ယဉ်ကျေးခြင်း",
    "sākhalya": "စကား ချိုသာခြင်း", "paṭisanthāro": "ဖော်ဖော်ရွေရွေ ကြိုဆိုဆက်ဆံခြင်း",
    "indriyesu aguttadvāratā": "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို မစောင့်ထိန်းခြင်း",
    "bhojane amattaññutā": "အစားအစာ၌ အတိုင်းအရှည်ကို မသိခြင်း",
    "indriyesu guttadvāratā": "အာရုံခံ အင်္ဂါတို့၏ တံခါးကို စောင့်ထိန်းခြင်း",
    "bhojane mattaññutā": "အစားအစာ၌ အတိုင်းအရှည်ကို သိခြင်း",
    "muṭṭhasacca": "သတိလစ်ခြင်း", "asampajañña": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း မရှိခြင်း",
    "sati": "သတိ", "sampajañña": "ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း",
    "paṭisaṅkhānabala": "ပြန်လည် စဉ်းစားခြင်း၏ စွမ်းအား", "bhāvanābala": "ဘာဝနာ ပွားများခြင်း၏ စွမ်းအား",
    "samatho": "စိတ်ငြိမ်သက်ခြင်း", "vipassanā": "ထိုးထွင်းသိမြင်ခြင်း",
    "samathanimitta": "စိတ်ငြိမ်သက်ခြင်း၏ အမှတ်အသား", "paggāhanimitta": "စိတ်ကို မြှင့်တင်ခြင်း၏ အမှတ်အသား",
    "paggāho": "စိတ်ကို မြှင့်တင်ခြင်း", "avikkhepo": "စိတ် မပျံ့လွင့်ခြင်း",
    "sīlavipatti": "သီလ ပျက်စီးခြင်း", "diṭṭhivipatti": "အယူ ပျက်စီးခြင်း",
    "sīlasampadā": "သီလ ပြည့်စုံခြင်း", "diṭṭhisampadā": "အယူ ပြည့်စုံခြင်း",
    "sīlavisuddhi": "သီလ စင်ကြယ်ခြင်း", "diṭṭhivisuddhi": "အယူ စင်ကြယ်ခြင်း",
    "vijjā": "အမှန်သိမြင်မှု", "vimutti": "လွတ်မြောက်မှု",
}
PADHANA = "ကြိုးပမ်းအားထုတ်ခြင်း"    # padhāna (striving; kept apart from paggāha = «စိတ်ကို မြှင့်တင်ခြင်း»)
SAMVEGA = "သံဝေဂ"                     # saṃvega (ordinary Burmese word for spiritual urgency)
# whole suttantika lines that are phrases (after the label)
MFIXED = {
    "diṭṭhivisuddhi kho pana.": f"{KHO_PANA} {SUT['diṭṭhivisuddhi']}{END}",
    "yathādiṭṭhissa ca padhānaṃ.": f"အယူနှင့် လျော်ညီသူ၏ {PADHANA}{END}",
    "saṃvego ca saṃvejaniyesu ṭhānesu.": f"{SAMVEGA} ရဖွယ် အခြေအနေတို့၌ {SAMVEGA} ရခြင်း{END}",
    "saṃviggassa ca yoniso padhānaṃ.": f"{SAMVEGA} ရသူ၏ သင့်လျော်စွာ {PADHANA}{END}",
    "asantuṭṭhitā ca kusalesu dhammesu.": f"{TERMS['kusalā']} {DHAMMA_LOC} ရောင့်ရဲမှု မရှိခြင်း{END}",
    "appaṭivānitā ca padhānasmiṃ.": f"{PADHANA}၌ နောက်မဆုတ်ခြင်း{END}",
    "khaye ñāṇaṃ.": f"ကုန်ခန်းခြင်းကို သိသော ဉာဏ်{END}",
    "anuppāde ñāṇanti.": f"နောက်ထပ် မဖြစ်ပေါ်ခြင်းကို သိသော ဉာဏ်{END}",
}

# ===================================================================================== headings, colophons
MATIKA = "ခေါင်းစဉ်စာရင်း"            # mātikā (list of headings; not «မာတိကာ» = table of contents)
HEAD = {
    "Mātikā": MATIKA,
    "Tikamātikā": f"{TIKA} {MATIKA}",
    "Dukamātikā": f"{DUKA} {MATIKA}",
    "Hetugocchakaṃ": f"{ROOT}တို့၏ အစု",
    "Cūḷantaradukaṃ": f"ကြားညှပ် {DUKA} အစုငယ်",
    "Mahantaradukaṃ": f"ကြားညှပ် {DUKA} အစုကြီး",
    "Piṭṭhidukaṃ": f"နောက်ဆုံး {DUKA}များ",
    "Suttantikadukamātikā": f"သုတ္တန် {DUKA} {MATIKA}",
}
for _st, _d in FAMILY.items():                      # Āsavagocchakaṃ … Kilesagocchakaṃ = «N-တို့၏ အစု»
    HEAD[_st[0].upper() + _st[1:] + "gocchakaṃ"] = f"{_d['N']}တို့၏ အစု"
COLO = dict(HEAD)                                   # colophon sentences (without the full stop)
COLO.update({
    "Abhidhammadukamātikā": f"အဘိဓမ္မာ {DUKA} {MATIKA}",
    "Mātikā niṭṭhitā": f"“{MATIKA}” {NITTHITA}",
})

# ===================================================================================== the engine
EXTRA_RULES = []      # later chapters: (compiled regex on the line body, function(match) -> Burmese) tried first
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
HEAD_RE = re.compile(r"(?P<h>#+) (?P<t>.+)$")
LABEL_RE = re.compile(r"(?P<l>\((?:Ka|Kha|Ga|Gha|Ṅa)\)) (?P<r>.+)$")
COLO_RE = re.compile(r"(?P<t>[^\[\]]+?)(?: (?P<v>\[[^\]]+\]))?\.")


def _t(key):
    if key not in TERMS:
        raise Miss("mātikā term: " + key)
    return TERMS[key]


def _v(v):
    return " " + var_my(v) if v else ""


def matika_my(rest):
    """One mātikā member (the text after the «(Ka)» label)."""
    if rest in MFIXED:
        return MFIXED[rest]
    m = re.fullmatch(r"(?P<x>.+?) ceva dhammā (?P<y>.+?) ca\.", rest)
    if m:
        k = (m["x"], m["y"])
        if k not in CEVA:
            raise Miss("ceva: " + rest)
        return f"{CEVA[k]} {DHAMMA_PL}{END}"
    m = re.fullmatch(r"(?P<y>.+?) ceva dhammā (?:na|no) ca (?P<x>.+?)\.", rest)
    if m:
        k = (m["y"], m["x"])
        if k not in CEVANO:
            raise Miss("ceva no: " + rest)
        return f"{CEVANO[k]} {DHAMMA_PL}{END}"
    m = re.fullmatch(r"(?P<x>.+?) kho pana dhammā (?P<y>.+?)pi\.", rest)
    if m:
        return f"{KHO_PANA} {_t(m['x'])} {DHAMMA_AMONG} {nominal(_t(m['y']))}{PI}{END}"
    m = re.fullmatch(r"(?P<t>.+?)(?: (?P<v>\[[^\]]+\]))? dhammā\.", rest)
    if m:
        return f"{_t(m['t'])}{_v(m['v'])} {DHAMMA_PL}{END}"
    m = re.fullmatch(r"(?P<t>\S+dhammadhammā)\.", rest)          # the noun «dhamma» inside the term
    if m:
        return f"{_t(m['t'])} {DHAMMA_PL}{END}"
    m = re.fullmatch(r"(?P<y>\S+)pi\.", rest)
    if m:
        return f"{nominal(_t(m['y']))}{PI}{END}"
    m = re.fullmatch(r"(?P<x>.+?)(?: ca|ñca)(?: (?P<v>\[[^\]]+\]))?\.", rest)
    if m:
        if m["x"] not in SUT:
            raise Miss("suttantika: " + rest)
        return f"{SUT[m['x']]}{_v(m['v'])}{END}"
    raise Miss("mātikā: " + rest)


def line_my(body):
    for rx, fn in EXTRA_RULES:
        m = rx.fullmatch(body)
        if m:
            return fn(m)
    m = HEAD_RE.fullmatch(body)
    if m:
        if m["t"] not in HEAD:
            raise Miss("heading: " + body)
        return f"{m['h']} {HEAD[m['t']]}"
    m = LABEL_RE.fullmatch(body)
    if m:
        return LABEL[m["l"]] + " " + matika_my(m["r"])
    m = COLO_RE.fullmatch(body)
    if m and m["t"] in COLO:
        return f"{COLO[m['t']]}{_v(m['v'])}{END}"
    raise Miss("line: " + body)


def translate(text):
    out = []
    for line in text.splitlines():
        if not line.strip():
            out.append("")
            continue
        m = ID_RE.search(line)
        body = line[:m.start()] if m else line
        out.append(line_my(body) + (" " + m.group(1) if m else ""))
    return "\n".join(out).rstrip("\n") + "\n"


# #####################################################################################################################
# Cittuppāda (2-01, 2026-11-16): ADDITIVE section. Nothing above this line was changed; the Mātikā sample regenerates
# byte for byte. Model for 2-02 … 5: import this module, add your own NAMES / SYN / GEN / BODY / CITTA_KIND / QUAL /
# HEAD / COLO / VAR_KIND entries in memory (never change a value given here), call rebuild_cu(), then translate_cu().
# Frames (Pāli -> Burmese):
#   Katame dhammā kusalā?                      -> «ကုသိုလ် သဘောတရားများ ဟူသည် အဘယ်တို့နည်း» + «။»
#   Yasmiṃ samaye KIND uppannaṃ hoti QUAL… OBJ vā … yaṃ yaṃ vā panārabbha
#                                              -> «OBJ-ကို အာရုံပြု၍ဖြစ်စေ၊ … မည်သည့်အရာကို အာရုံပြု၍ဖြစ်စေ QUAL၊ QUAL KIND-သည်
#                                                 [တိုက်တွန်းမှုဖြင့်] ဖြစ်ပေါ်လာသော အချိန်၌»
#   tasmiṃ samaye X hoti / honti               -> «ထိုအချိန်၌ X ရှိသည် / ရှိကြသည်»
#   Katamo … tasmiṃ samaye X hoti?             -> «ထိုအချိန်၌ ရှိသော X ဟူသည် အဘယ်နည်း» (plural: ရှိကြသော … အဘယ်တို့နည်း)
#   Yo / Yā / Yaṃ tasmiṃ samaye [GEN] A B C –  -> «ထိုအချိန်၌ ရှိသော [GEN] A၊ B၊ C –»
#   ayaṃ / idaṃ tasmiṃ samaye X hoti           -> «ဤသည်မှာ ထိုအချိန်၌ ရှိသော X ဖြစ်သည်»
#   ime / imāni / imā tasmiṃ samaye X honti    -> «ဤသည်တို့မှာ ထိုအချိန်၌ ရှိကြသော X ဖြစ်ကြသည်»
#   ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā
#                                              -> «ထိုအချိန်၌ အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော ရုပ် မဟုတ်သော အခြား
#                                                 သဘောတရားများ ရှိသမျှလည်း» (with ṭhapetvā: «A-ကို ချန်ထား၍၊ B-ကို … C-ကို
#                                                 ချန်ထား၍» before it)
#   ime dhammā kusalā                          -> «ဤသဘောတရားများသည် ကုသိုလ် ဖြစ်ကြသည်»
#   Tasmiṃ kho pana samaye                     -> «ထို့ပြင် ထိုအချိန်၌»
# Separators: «, » and «; » -> «၊ »; «?» and «.» -> «။»; « – » kept; «…pe…» -> «…».
# Numbers: «eko / ekā / ekaṃ X» -> «X တစ်ပါး»; counted groups «X N-ပါး» (classifier ပါး throughout).
# Every synonym of a list must differ from the others in Burmese unless the Pāli repeats it (list_items raises Miss).
# #####################################################################################################################

# ------------------------------------------------------------------------------------------- time words, frame words
YASMIM = "အချိန်၌"                  # yasmiṃ samaye «…ဖြစ်ပေါ်လာသော အချိန်၌» (at the time when …)
TASMIM = "ထိုအချိန်၌"                # tasmiṃ samaye (at that time)
KHO_PANA_SAMAYE = f"{KHO_PANA} {TASMIM}"   # Tasmiṃ kho pana samaye («ထို့ပြင်» = the sample's kho pana)
CU_HOTI = {"sg": "ရှိသည်", "pl": "ရှိကြသည်"}            # X hoti / honti (there is / there are)
CU_REL = {"sg": "ရှိသော", "pl": "ရှိကြသော"}             # «… tasmiṃ samaye X» inside a question / closer
CU_Q = {"sg": "ဟူသည် အဘယ်နည်း", "pl": "ဟူသည် အဘယ်တို့နည်း"}   # Katamo … ? (which is …?)
CU_DEM = {"sg": "ဤသည်မှာ", "pl": "ဤသည်တို့မှာ"}         # ayaṃ / idaṃ ; ime / imāni / imā (this is / these are)
CU_COP = {"sg": "ဖြစ်သည်", "pl": "ဖြစ်ကြသည်"}           # closing copula
CL = "ပါး"                                            # classifier for counted factors (ငါးပါးသီလ style)
KAYA = f"{MIND}၏ အဖော်တို့"     # kāya- in kāyapassaddhi …: the mental «body» = the companions of the mind (the text
#                                 defines it by the feeling, perception and formation aggregates); not the physical body
KANDA = "အခန်း"                  # kaṇḍa (chapter / book part)
VARA = "ဖော်ပြချက်"              # -vāra (exposition section: Koṭṭhāsavāra, Suññatavāra) and Padabhājanī
BHANAVARA = "ရွတ်ဖတ်ရန် အပိုင်း"   # bhāṇavāra (recitation section)
SAMMA = "မှန်ကန်သော"             # sammā- (right), cf. sammattaniyatā = မှန်ကန်မှု၌ …
INDRIYA = "စွမ်းရည်"             # -indriya (faculty); kept apart from bala = «စွမ်းအား»
BALA = "စွမ်းအား"                # -bala (power), as the sample's paṭisaṅkhānabala «…၏ စွမ်းအား»
KHANDHA = "အစုအဝေး"             # khandha (aggregate, heap); kept apart from gocchaka «အစု»
VINNANA = "သိစိတ်"                # viññāṇa (consciousness); not ဝိညာဉ် (popular «soul»)
MANO = "မနော"                    # mano (mind, everyday Burmese word); NOTE for checkers: «မနော» is not a negation
SANNA = "မှတ်သိမှု"                # saññā (perception)
CETANA = "စေ့ဆော်မှု"              # cetanā (intention); not စေတနာ (everyday «goodwill»)
PHASSA = "တွေ့ထိမှု"               # phassa (contact)
SANKHARA = "ပြုပြင်ဖန်တီးမှု"       # saṅkhāra (formation), one root with saṅkhatā «ပြုပြင်ဖန်တီးထားသော»
AHARA = "အာဟာရ"                  # āhāra (nutriment)
JHANA = "ဈာန်"                   # jhāna
MAGGA = "မဂ်"                     # magga (path)
SOMANASSA = "ဝမ်းမြောက်မှု"        # somanassa (mental joy)


def _ix(x, mod):
    """Burmese «X၏ <faculty / power>» for -indriya / -bala names."""
    return f"{x}၏ {mod}"


# ------------------------------------------------------------------------------------------- synonym table
# Pāli surface (one word or a fixed phrase) -> Burmese. Items that are also factor NAMES are looked up in NAMES.
# Endings: -nā / -ā action noun = «…ခြင်း»; -ttaṃ = «…သော / ထားသော အဖြစ်»; -bhāvo = «…သော သဘော»; privative a- = «မ».
_SATA = "နှစ်သက်ဖွယ်ကောင်း"           # sāta (agreeable), verb stem; kept apart from sukha = «သာယာ»
CSJ = f"{MIND}၏ {PHASSA}မှ ဖြစ်ပေါ်သော"   # cetosamphassaja- (born of mind-contact)
CETASIKA_ADJ = "စိတ်ပိုင်းဆိုင်ရာ"          # cetasika (adjective «mental», as nāma = စိတ်ပိုင်း); the noun cetasika
#                                          stays the sample's «စိတ်၏ အဖော်»
SYN = {
    # phassa
    "phusanā": "ထိခြင်း", "saṃphusanā": "တွေ့ထိခြင်း", "saṃphusitattaṃ": "တွေ့ထိထားသော အဖြစ်",
    # vedanā (joyful and neutral forms)
    "cetasikaṃ sātaṃ": f"{CETASIKA_ADJ} {_SATA}မှု",
    "cetasikaṃ sukhaṃ": f"{CETASIKA_ADJ} {SUKHA}မှု",
    "cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ": f"{CSJ} {_SATA}၍ {SUKHA}သော ခံစားရခြင်း",
    "cetosamphassajā sātā sukhā vedanā": f"{CSJ} {_SATA}၍ {SUKHA}သော {FEEL}",
    "cetasikaṃ neva sātaṃ nāsātaṃ":
        f"{CETASIKA_ADJ} {_SATA}သည်လည်း မဟုတ်၊ နှစ်သက်ဖွယ် မကောင်းသည်လည်း မဟုတ်သော အဖြစ်",
    "cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ": f"{CSJ} မ{DUKKHA} မ{SUKHA}သော ခံစားရခြင်း",
    "cetosamphassajā adukkhamasukhā vedanā": f"{CSJ} မ{DUKKHA} မ{SUKHA}သော {FEEL}",
    # saññā, cetanā
    "sañjānanā": "မှတ်သိခြင်း", "sañjānitattaṃ": "မှတ်သိထားသော အဖြစ်",
    "sañcetanā": "စေ့ဆော်ခြင်း", "cetayitattaṃ": "စေ့ဆော်ထားသော အဖြစ်",
    # citta
    "mano": MANO, "mānasaṃ": "စိတ်နှလုံး", "hadayaṃ": "နှလုံးသား", "paṇḍaraṃ": "ကြည်လင်သောအရာ",
    "viññāṇaṃ": VINNANA, "tajjāmanoviññāṇadhātu": f"သက်ဆိုင်ရာ {MANO} {VINNANA} ဓာတ်",
    # vitakka, vicāra
    "takko": "တွေးတောခြင်း", "saṅkappo": "ကြံစည်မှု", "appanā": "အာရုံ၌ စိတ်ကို သွင်းခြင်း",
    "byappanā": "အာရုံ၌ စိတ်ကို နစ်မြုပ်စွာ သွင်းခြင်း", "cetaso abhiniropanā": "စိတ်ကို အာရုံသို့ တင်ပို့ခြင်း",
    "cāro": "သုံးသပ်ခြင်း", "anuvicāro": "ထပ်ကာထပ်ကာ သုံးသပ်ခြင်း", "upavicāro": "အနီးကပ် သုံးသပ်ခြင်း",
    "cittassa anusandhānatā": "စိတ်ကို အာရုံနှင့် ဆက်စပ်ထားခြင်း", "anupekkhanatā": "အာရုံကို စေ့စေ့ ရှုကြည့်ခြင်း",
    # pīti
    "pāmojjaṃ": "ရွှင်လန်းခြင်း", "āmodanā": "ဝမ်းသာခြင်း", "pamodanā": "အလွန် ဝမ်းသာခြင်း",
    "hāso": "ပြုံးရွှင်ခြင်း", "pahāso": "အလွန် ပြုံးရွှင်ခြင်း", "vitti": "ကျေနပ်ခြင်း",
    "odagyaṃ": "စိတ်တက်ကြွခြင်း", "attamanatā cittassa": "စိတ်၏ နှစ်သိမ့်ခြင်း",
    # ekaggatā / samādhi
    "ṭhiti": "တည်တံ့ခြင်း", "saṇṭhiti": "ကောင်းစွာ တည်တံ့ခြင်း", "avaṭṭhiti": "ခိုင်မြဲစွာ တည်တံ့ခြင်း",
    "avisāhāro": "မပြန့်ကျဲခြင်း", "avisāhaṭamānasatā": "စိတ် မပြန့်ကျဲသော အဖြစ်",
    # saddhā
    "saddhā": "ယုံကြည်မှု", "saddahanā": "ယုံကြည်ခြင်း", "okappanā": "စိတ်ချ အားကိုးခြင်း",
    "abhippasādo": "ကြည်ညိုလေးစားခြင်း",
    # vīriya
    "cetasiko vīriyārambho": f"{CETASIKA_ADJ} ဝီရိယ စတင်ခြင်း", "nikkamo": "ရှေ့သို့ တိုးထွက်ခြင်း",
    "parakkamo": "ရဲရင့်စွာ ကြိုးစားခြင်း", "uyyāmo": "ထကြွ ကြိုးစားခြင်း", "vāyāmo": "အားထုတ်မှု",
    "ussāho": "စိတ်အားထက်သန်မှု", "ussoḷhī": "ပြင်းပြသော အားမာန်", "thāmo": "ခွန်အား", "dhiti": "ဇွဲ",
    "asithilaparakkamatā": "မလျော့ရဲဘဲ ကြိုးစားခြင်း", "anikkhittachandatā": "ဆန္ဒကို လက်မလွှတ်ခြင်း",
    "anikkhittadhuratā": "ဝန်ကို မချထားခြင်း", "dhurasampaggāho": "ဝန်ကို ခိုင်မြဲစွာ ထမ်းဆောင်ခြင်း",
    "vīriyaṃ": "ဝီရိယ",
    # sati
    "anussati": "အဖန်ဖန် အောက်မေ့ခြင်း", "paṭissati": "ပြန်လည် အောက်မေ့ခြင်း", "saraṇatā": "မှတ်မိခြင်း",
    "dhāraṇatā": "စွဲမှတ်ထားခြင်း", "apilāpanatā": "အပေါ်ယံ မပေါ်လောခြင်း", "asammussanatā": "မမေ့လျော့ခြင်း",
    # paññā
    "paññā": "ပညာ", "pajānanā": "ကွဲပြားစွာ သိခြင်း", "vicayo": "စိစစ်ခြင်း", "pavicayo": "သေချာစွာ စိစစ်ခြင်း",
    "dhammavicayo": f"{DHAMMA_PL}ကို စိစစ်ခြင်း", "sallakkhaṇā": "လက္ခဏာကို ကောင်းစွာ ခွဲခြားခြင်း",
    "upalakkhaṇā": "လက္ခဏာကို အနီးကပ် ခွဲခြားခြင်း", "paccupalakkhaṇā": "လက္ခဏာကို အသီးသီး ခွဲခြားခြင်း",
    "paṇḍiccaṃ": "လိမ္မာခြင်း", "kosallaṃ": "ကျွမ်းကျင်ခြင်း", "nepuññaṃ": "နက်နဲသိမ်မွေ့ခြင်း",
    "vebhabyā": "ခွဲခြမ်းစိတ်ဖြာခြင်း", "cintā": "စဉ်းစားခြင်း", "upaparikkhā": "စူးစမ်းဆန်းစစ်ခြင်း",
    "bhūrī": "ကျယ်ပြန့်ခြင်း", "medhā": "ဉာဏ်ထက်မြက်ခြင်း", "pariṇāyikā": "လမ်းပြခြင်း", "patodo": "နှင်တံ",
    "paññāsatthaṃ": "ပညာ ဓား", "paññāpāsādo": "ပညာ ပြာသာဒ်", "paññāāloko": "ပညာ အလင်း",
    "paññāobhāso": "ပညာ အရောင်အဝါ", "paññāpajjoto": "ပညာ မီးအိမ်", "paññāratanaṃ": "ပညာ ရတနာ",
    # jīvita
    "āyu": "သက်တမ်း", "yapanā": "ဆက်လက် ဖြစ်နေခြင်း", "yāpanā": "ဆက်လက် ရှင်သန်စေခြင်း",
    "iriyanā": "လှုပ်ရှားခြင်း", "vattanā": "လည်ပတ်ခြင်း", "pālanā": "စောင့်ရှောက်ခြင်း", "jīvitaṃ": "အသက်",
    # alobha, adosa
    "alubbhanā": "မမက်မောခြင်း", "alubbhitattaṃ": "မမက်မောသော အဖြစ်", "asārāgo": "မတပ်မက်ခြင်း",
    "asārajjanā": "မစွဲမက်ခြင်း", "asārajjitattaṃ": "မစွဲမက်သော အဖြစ်", "kusalamūlaṃ": f"{TERMS['kusalā']}၏ {ROOT}",
    "adussanā": "စိတ်မဆိုးခြင်း", "adussitattaṃ": "စိတ်မဆိုးသော အဖြစ်", "abyāpajjo": "မညှဉ်းဆဲလိုခြင်း",
    # passaddhi, lahutā, mudutā, kammaññatā, pāguññatā, ujukatā
    "passaddhi": "ငြိမ်းအေးခြင်း", "paṭipassaddhi": "လုံးဝ ငြိမ်းအေးခြင်း", "passambhanā": "အေးချမ်းခြင်း",
    "paṭipassambhanā": "လုံးဝ အေးချမ်းခြင်း", "paṭipassambhitattaṃ": "လုံးဝ အေးချမ်းသွားသော အဖြစ်",
    "lahutā": "ပေါ့ပါးခြင်း", "lahupariṇāmatā": "လျင်မြန်စွာ ပြောင်းလဲနိုင်ခြင်း", "adandhanatā": "မနှေးကွေးခြင်း",
    "avitthanatā": "မတုံ့ဆိုင်းခြင်း",
    "mudutā": "ပျော့ပျောင်းခြင်း", "maddavatā": "နူးညံ့သော အဖြစ်", "akakkhaḷatā": "မကြမ်းတမ်းခြင်း",
    "akathinatā": "မမာကျောခြင်း",
    "kammaññatā": "အသုံးပြုရန် သင့်တော်ခြင်း", "kammaññattaṃ": "အသုံးပြုရန် သင့်တော်သော အဖြစ်",
    "kammaññabhāvo": "အသုံးပြုရန် သင့်တော်သော သဘော",
    "paguṇatā": "ကျင့်သားရခြင်း", "paguṇattaṃ": "ကျင့်သားရသော အဖြစ်", "paguṇabhāvo": "ကျင့်သားရသော သဘော",
    "ujutā": "ဖြောင့်ခြင်း", "ujukatā": "ဖြောင့်တန်းခြင်း", "ajimhatā": "မကောက်ကွေးခြင်း",
    "avaṅkatā": "မကွေးညွှတ်ခြင်း", "akuṭilatā": "မလိမ်ကောက်ခြင်း",
}
SYN["cittassa ṭhiti"] = f"{MIND}၏ {SYN['ṭhiti']}"
SYN_MAXLEN = 6        # longest phrase key in words

# ------------------------------------------------------------------------------------------- factor names
NAMES = {
    "phasso": PHASSA, "vedanā": FEEL, "saññā": SANNA, "cetanā": CETANA, "cittaṃ": MIND,
    "vitakko": VIT, "vicāro": VIC, "pīti": "ပီတိ", "sukhaṃ": SUKHA + "မှု", "upekkhā": "ဥပေက္ခာ",
    "cittassekaggatā": f"{MIND}၏ စူးစိုက်မှု",
    "saddhindriyaṃ": _ix(SYN["saddhā"], INDRIYA), "vīriyindriyaṃ": _ix(SYN["vīriyaṃ"], INDRIYA),
    "satindriyaṃ": _ix(SUT["sati"], INDRIYA), "samādhindriyaṃ": _ix("သမာဓိ", INDRIYA),
    "paññindriyaṃ": _ix(SYN["paññā"], INDRIYA), "manindriyaṃ": _ix(MANO, INDRIYA),
    "somanassindriyaṃ": _ix(SOMANASSA, INDRIYA), "upekkhindriyaṃ": _ix("ဥပေက္ခာ", INDRIYA),
    "jīvitindriyaṃ": _ix(SYN["jīvitaṃ"], INDRIYA),
    "sammādiṭṭhi": f"{SAMMA} အယူ", "sammāsaṅkappo": f"{SAMMA} {SYN['saṅkappo']}",
    "sammāvāyāmo": f"{SAMMA} {SYN['vāyāmo']}", "sammāsati": f"{SAMMA} {SUT['sati']}",
    "sammāsamādhi": f"{SAMMA} သမာဓိ",
    "saddhābalaṃ": _ix(SYN["saddhā"], BALA), "vīriyabalaṃ": _ix(SYN["vīriyaṃ"], BALA),
    "satibalaṃ": _ix(SUT["sati"], BALA), "samādhibalaṃ": _ix("သမာဓိ", BALA), "paññābalaṃ": _ix(SYN["paññā"], BALA),
    "hiribalaṃ": _ix(SUT["hirī"], BALA), "ottappabalaṃ": _ix(SUT["ottappa"], BALA),
    "alobho": "လောဘ မရှိခြင်း", "adoso": "ဒေါသ မရှိခြင်း", "amoho": "မောဟ မရှိခြင်း",
    "anabhijjhā": "သူ့ဥစ္စာကို မလိုချင်ခြင်း", "abyāpādo": "ဖျက်ဆီးလိုစိတ် မရှိခြင်း",
    "hirī": SUT["hirī"], "ottappaṃ": SUT["ottappa"],
    "sati": SUT["sati"], "sampajaññaṃ": SUT["sampajañña"], "samatho": SUT["samatho"],
    "vipassanā": SUT["vipassanā"], "paggāho": SUT["paggāho"], "avikkhepo": SUT["avikkhepo"],
    # aggregates, bases, elements, nutriments
    "vedanākkhandho": f"{FEEL} {KHANDHA}", "saññākkhandho": f"{SANNA} {KHANDHA}",
    "saṅkhārakkhandho": f"{SANKHARA} {KHANDHA}", "viññāṇakkhandho": f"{VINNANA} {KHANDHA}",
    "manāyatanaṃ": f"{MANO} အာရုံခံ နယ်ပယ်", "dhammāyatanaṃ": f"{DHAMMA} အာရုံခံ နယ်ပယ်",
    "manoviññāṇadhātu": f"{MANO} {VINNANA} ဓာတ်", "dhammadhātu": f"{DHAMMA} ဓာတ်",
    "phassāhāro": f"{PHASSA} {AHARA}", "manosañcetanāhāro": f"{MANO}၏ {SYN['sañcetanā']} {AHARA}",
    "viññāṇāhāro": f"{VINNANA} {AHARA}",
    # group nouns (Suññatavāra) and the jhāna / path
    "dhammā": DHAMMA_PL, "khandhā": f"{KHANDHA}များ", "āyatanāni": "အာရုံခံ နယ်ပယ်များ", "dhātuyo": "ဓာတ်များ",
    "āhārā": f"{AHARA}များ", "indriyāni": f"{INDRIYA}များ", "jhānaṃ": JHANA, "maggo": MAGGA,
    "balāni": f"{BALA}များ", "hetū": f"{ROOT}များ",
}
# the six pairs: kāya- (the mental companions) / citta- (the mind)
CU_PAIRS = {"passaddhi": "passaddhi", "lahutā": "lahutā", "mudutā": "mudutā", "kammaññatā": "kammaññatā",
            "pāguññatā": "paguṇatā", "ujukatā": "ujukatā"}
for _p, _s in CU_PAIRS.items():
    NAMES["kāyujukatā" if _p == "ujukatā" else "kāya" + _p] = f"{KAYA} {SYN[_s]}"
    NAMES["cittujukatā" if _p == "ujukatā" else "citta" + _p] = f"{MIND} {SYN[_s]}"


# counted groups: Pāli number word -> NUM stem; «X N-ပါး»
CU_NUM = {"eko": "eka", "ekā": "eka", "ekaṃ": "eka", "dve": "dvi", "tayo": "ti", "cattāro": "catu",
          "pañca": "pañca", "cha": "cha", "satta": "satta", "aṭṭha": "aṭṭha"}


def count_my(x, stem):
    """«X» + Pāli number stem -> «X N-ပါး»."""
    return f"{x} {NUM[stem]}{CL}"


_ANGA = "အင်္ဂါ"
NAMES.update({
    "cattāro khandhā": count_my(KHANDHA, "catu"), "dvāyatanāni": count_my("အာရုံခံ နယ်ပယ်", "dvi"),
    "dve dhātuyo": count_my("ဓာတ်", "dvi"), "tayo āhārā": count_my(AHARA, "ti"),
    "aṭṭhindriyāni": count_my(INDRIYA, "aṭṭha"), "sattindriyāni": count_my(INDRIYA, "satta"),
    "pañcaṅgikaṃ jhānaṃ": f"{count_my(_ANGA, 'pañca')} ရှိသော {JHANA}",
    "caturaṅgikaṃ jhānaṃ": f"{count_my(_ANGA, 'catu')} ရှိသော {JHANA}",
    "pañcaṅgiko maggo": f"{count_my(_ANGA, 'pañca')} ရှိသော {MAGGA}",
    "caturaṅgiko maggo": f"{count_my(_ANGA, 'catu')} ရှိသော {MAGGA}",
    "satta balāni": count_my(BALA, "satta"), "cha balāni": count_my(BALA, "cha"),
    "tayo hetū": count_my(ROOT, "ti"), "dve hetū": count_my(ROOT, "dvi"),
})

# genitive / qualifying heads of a synonym list (between «Yo/Yā/Yaṃ [tasmiṃ samaye]» and the items)
GEN = {
    "vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa":
        f"{NAMES['vedanākkhandho']}၊ {NAMES['saññākkhandho']}နှင့် {NAMES['saṅkhārakkhandho']}တို့၏",
    "viññāṇakkhandhassa": f"{NAMES['viññāṇakkhandho']}၏",
    "tesaṃ arūpīnaṃ dhammānaṃ": f"ထို {TERMS['arūpino']} {DHAMMA}တို့၏",
    "tajjāmanoviññāṇadhātusamphassajaṃ": f"{SYN['tajjāmanoviññāṇadhātu']}၏ {PHASSA}မှ ဖြစ်ပေါ်သော",
    "tajjāmanoviññāṇadhātusamphassajā": f"{SYN['tajjāmanoviññāṇadhātu']}၏ {PHASSA}မှ ဖြစ်ပေါ်သော",
}

# definitions that are sentences, not synonym lists (from «Yaṃ» up to the dash)
_PAPA = f"ယုတ်မာသော {TERMS['akusalā']} {DHAMMA}တို့ကို ကျူးလွန်ခြင်းကို"   # pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā
BODY = {
    "Yaṃ tasmiṃ samaye hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        f"{TASMIM} ရှက်ထိုက်သည့်အရာကို ရှက်ခြင်း၊ {_PAPA} ရှက်ခြင်း",
    "Yaṃ tasmiṃ samaye ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        f"{TASMIM} ကြောက်ရွံ့ထိုက်သည့်အရာကို ကြောက်ရွံ့ခြင်း၊ {_PAPA} ကြောက်ရွံ့ခြင်း",
}

# ------------------------------------------------------------------------------------------- the citta opening
CITTA_KIND = {"kāmāvacaraṃ kusalaṃ cittaṃ": f"{TERMS['kāmāvacarā']} {TERMS['kusalā']}{MIND}"}
QUAL = {
    "somanassasahagataṃ": SOMANASSA + TOGETHER, "upekkhāsahagataṃ": TERMS["upekkhāsahagatā"],
    "ñāṇasampayuttaṃ": "ဉာဏ်" + SAMP, "ñāṇavippayuttaṃ": "ဉာဏ်" + VIPP,
}
QUAL_ADV = {"sasaṅkhārena": "တိုက်တွန်းမှုဖြင့်"}     # adverbs of the arising (with prompting)
ARAMMANA = {   # «X-ārammaṇaṃ vā» -> «X-ကို အာရုံပြု၍ဖြစ်စေ»
    "rūpārammaṇaṃ": "အဆင်းအရောင်", "saddārammaṇaṃ": "အသံ", "gandhārammaṇaṃ": "အနံ့",
    "rasārammaṇaṃ": "အရသာ", "phoṭṭhabbārammaṇaṃ": "အထိအတွေ့", "dhammārammaṇaṃ": DHAMMA,
}
ARAMMANA_VA = "ကို အာရုံပြု၍ဖြစ်စေ"
YAM_YAM = "မည်သည့်အရာ" + ARAMMANA_VA             # yaṃ yaṃ vā panārabbha
UPPANNA = "ဖြစ်ပေါ်လာသော"                         # uppannaṃ hoti (before «အချိန်၌»)
YEVA = (f"{TASMIM} အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်လာသော {TERMS['arūpino']} အခြား {DHAMMA_PL} ရှိသမျှလည်း")
#        ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā
THAPETVA = "ကို ချန်ထား၍"                           # ṭhapetvā X-ṃ = «X-ကို ချန်ထား၍»
IME_KUSALA = f"ဤ{DHAMMA_PL}သည် {TERMS['kusalā']} {CU_COP['pl']}"     # ime dhammā kusalā
KATAME_KUSALA = f"{TERMS['kusalā']} {DHAMMA_PL} {CU_Q['pl']}"        # Katame dhammā kusalā

# ------------------------------------------------------------------------------------------- headings, colophons
_CU_TITLES = {
    "Cittuppādakaṇḍaṃ": f"{MIND} ဖြစ်ပေါ်ခြင်း {KANDA}",
    "Kāmāvacarakusalaṃ": f"{TERMS['kāmāvacarā']} {TERMS['kusalā']}",
    "Padabhājanī": f"ပုဒ်အလိုက် ခွဲခြမ်း {VARA}",
    "Padabhājanīyaṃ": f"ပုဒ်အလိုက် ခွဲခြမ်း {VARA}",
    "Koṭṭhāsavāro": f"အစုအပိုင်းအလိုက် {VARA}",
    "Suññatavāro": f"ဆိတ်သုဉ်းကြောင်း {VARA}",
    "Aṭṭha kāmāvacaramahākusalacittāni":
        f"{TERMS['kāmāvacarā']} ကြီးကျယ်သော {TERMS['kusalā']}{MIND} {NUM['aṭṭha']}{CL}",
}
for _o, _om in ORD.items():          # Paṭhamaṃ cittaṃ … Aṭṭhamaṃ cittaṃ; Paṭhamabhāṇavāro …
    _cap = _o[0].upper() + _o[1:]
    _CU_TITLES[f"{_cap}ṃ cittaṃ"] = f"{_om} {MIND}"
    _CU_TITLES[f"{_cap}bhāṇavāro"] = f"{_om} {BHANAVARA}"
for _k2, _v2 in _CU_TITLES.items():
    HEAD.setdefault(_k2, _v2)
    COLO.setdefault(_k2, _v2)

# ------------------------------------------------------------------------------------------- variant readings
for _k2, _v2 in {
    "viriyindriyaṃ": LEKHANA, "viriyabalaṃ": LEKHANA, "kāyappassaddhi": LEKHANA, "cittappassaddhi": LEKHANA,
    "kāyujjukatā": LEKHANA, "cittujjukatā": LEKHANA, "sañcetayitattaṃ": PATHA, "viriyārambho": LEKHANA,
    "ussoḷhi": LEKHANA, "irīyanā": LEKHANA, "adūsanā adūsitattaṃ": LEKHANA, "paṭippassaddhi": LEKHANA,
    "paṭippassambhanā": LEKHANA, "paṭippassambhitattaṃ": LEKHANA, "thapetvā": LEKHANA,
}.items():
    VAR_KIND.setdefault(_k2, _v2)


# ------------------------------------------------------------------------------------------- the clause engine
_WC = "A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ"
NA = rf"(?![{_WC}])"                  # no word character after


def _alt(keys):
    """Regex alternation of Pāli keys, longest first; the first letter matches either case."""
    return "(?:" + "|".join(f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:])
                            for k in sorted(keys, key=len, reverse=True)) + ")"


def _name(p):
    k = p[0].lower() + p[1:]
    if k not in NAMES:
        raise Miss("name: " + p)
    return NAMES[k]


def _nm(m):
    """Name with an optional «eko / ekā / ekaṃ» -> «X တစ်ပါး»."""
    x = _name(m["name"])
    return count_my(x, CU_NUM[m["num"]]) if m["num"] else x


def _n(v):
    return "pl" if v == "honti" else "sg"


def r_katame(m):
    return KATAME_KUSALA


def r_defq(m):
    n = _n(m["v"])
    return f"{TASMIM} {CU_REL[n]} {_nm(m)} {CU_Q[n]}"


def r_close(m):
    n = _n(m["v"])
    return f"{CU_DEM[n]} {TASMIM} {CU_REL[n]} {_nm(m)} {CU_COP[n]}"


def r_item(m):
    v = " " + var_my(m["var"]) if m["var"] else ""
    return f"{_nm(m)}{v} {CU_HOTI[_n(m['v'])]}"


def r_nameseq(m):
    return (COMMA + " ").join(_name(p) for p in m[0].split(" "))


def r_name(m):
    return _name(m[0])


def r_open(m):
    """«Yasmiṃ samaye KIND uppannaṃ hoti QUAL… [sasaṅkhārena] OBJ vā … yaṃ yaṃ vā panārabbha»."""
    quals, advs = [], []
    for q in m["q"].split(" "):
        if q in QUAL:
            quals.append(QUAL[q])
        elif q in QUAL_ADV:
            advs.append(QUAL_ADV[q])
        else:
            raise Miss("qualifier: " + q)
    objs = re.findall(r"(\S+ārammaṇaṃ) vā(…pe…)?", m["obj"])
    if not objs or "".join(o + " vā" + (pe + " " if pe else " ") for o, pe in objs).rstrip() != m["obj"].rstrip():
        raise Miss("objects: " + m["obj"])
    s = ""
    for i, (o, pe) in enumerate(objs):
        if o not in ARAMMANA:
            raise Miss("object: " + o)
        s += ARAMMANA[o] + ARAMMANA_VA
        s += (PE + " ") if pe else (COMMA + " ")
    adv = " ".join(advs) + " " if advs else ""
    return (f"{s}{YAM_YAM} {(COMMA + ' ').join(quals)} {CITTA_KIND[m['kind']]}သည် {adv}{UPPANNA} {YASMIM}")


def r_yeva(m):
    if not m["th"]:
        return YEVA
    v = " " + var_my(m["v"]) if m["v"] else ""
    a, b, c = (NAMES[k] for k in ("vedanākkhandho", "saññākkhandho", "viññāṇakkhandho"))
    return f"{a}{THAPETVA}{v}{COMMA} {b}{THAPETVA}{COMMA} {c}{THAPETVA} {YEVA}"


def r_body(m):
    return BODY[m[0]]


def r_colo(m):
    return COLO[m[0]]


def r_var(m):
    return var_my(m[0])


def _syn(key):
    if key in SYN:
        return SYN[key]
    if key in NAMES:
        return NAMES[key]
    return None


def list_items(text):
    """Split a synonym list into items: [pāli, burmese, variant_burmese, pe_after]. Raises Miss on an unknown word
    and on two different Pāli items of one list with the same Burmese."""
    toks = re.findall(r"\[[^\]]*\]|…pe…|[^\s\[…]+", text)
    items, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t.startswith("["):
            if not items:
                raise Miss("variant before item: " + text)
            items[-1][2] = var_my(t)
            i += 1
            continue
        if t == "…pe…":
            if not items:
                raise Miss("pe before item: " + text)
            items[-1][3] = True
            i += 1
            continue
        for k in range(SYN_MAXLEN, 0, -1):
            words = toks[i:i + k]
            if len(words) < k or any(w.startswith("[") or w == "…pe…" for w in words):
                continue
            val = _syn(" ".join(words))
            if val is not None:
                items.append([" ".join(words), val, "", False])
                i += k
                break
        else:
            raise Miss("synonym: " + t + "  in: " + text[:120])
    seen = {}
    for p, my, _, _ in items:
        if my in seen and seen[my] != p:
            raise Miss(f"two synonyms share «{my}»: {seen[my]} / {p}")
        seen[my] = p
    return items


def items_my(items):
    out = ""
    for j, (p, my, v, pe) in enumerate(items):
        out += my + (" " + v if v else "")
        if j < len(items) - 1:
            out += (PE + " ") if pe else (COMMA + " ")
        elif pe:
            out += PE
    return out


CU_REL_RE = None


def r_rel(s, pos):
    """«Yo / Yā / Yaṃ [tasmiṃ samaye] [GEN] LIST» up to « – »: returns (Burmese, new pos) or None."""
    m = CU_REL_RE.match(s, pos)
    if not m:
        return None
    end = s.find(" – ", m.end())
    if end < 0:
        raise Miss("list without dash: " + s[pos:pos + 80])
    parts = []
    if m["ts"]:
        parts += [TASMIM, CU_REL["sg"]]
    if m["gen"]:
        parts.append(GEN[m["gen"]])
    parts.append(items_my(list_items(s[m.end():end])))
    return " ".join(parts), end


CU_SEP = [("…pe…. ", PE + END + " "), ("…pe….", PE + END), ("…pe…", PE), ("? ", END + " "), ("?", END),
          ("; ", COMMA + " "), (", ", COMMA + " "), (" – ", " – "), (". ", END + " "), (".", END), (" ", " ")]
CU_RULES = []
CU_EXTRA_RULES = []   # later chapters: (compiled regex, function(match) -> Burmese) pairs tried before the built-ins


def rebuild_cu():
    """(Re)compile the clause rules from the tables (call after adding entries)."""
    global CU_REL_RE
    names = _alt(NAMES)
    num = r"(?:(?P<num>eko|ekā|ekaṃ) )?"
    var = r"(?: (?P<var>\[[^\]]+\]))?"
    CU_REL_RE = re.compile(r"(?:Yo|Yā|Yaṃ)(?P<ts> tasmiṃ samaye)? (?:(?P<gen>" + _alt(GEN) + r") )?")
    rules = [
        (r"Katame dhammā kusalā", r_katame),
        (r"Katam(?:o|ā|aṃ|e|āni) tasmiṃ samaye " + num + r"(?P<name>" + names + r") (?P<v>hoti|honti)" + NA,
         r_defq),
        (r"Yasmiṃ samaye (?P<kind>" + _alt(CITTA_KIND) + r") uppannaṃ hoti (?P<q>(?:" + _alt({**QUAL, **QUAL_ADV})
         + r")(?: " + _alt({**QUAL, **QUAL_ADV}) + r")*) (?P<obj>\S+ārammaṇaṃ vā.*?)(?= yaṃ yaṃ vā panārabbha)"
         r" yaṃ yaṃ vā panārabbha", r_open),
        (_alt(BODY), r_body),
        ("REL", None),
        (r"(?:[Aa]yaṃ|[Ii]daṃ|[Ii]me|[Ii]māni|[Ii]mā) tasmiṃ samaye " + num + r"(?P<name>" + names
         + r") (?P<v>hoti|honti)" + NA, r_close),
        (r"[Yy]e vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā(?P<th> ṭhapetvā(?: (?P<v>\[[^\]]+\]))?"
         r" vedanākkhandhaṃ ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ)?", r_yeva),
        (r"ime dhammā kusalā", lambda m: IME_KUSALA),
        (r"Tasmiṃ kho pana samaye", lambda m: KHO_PANA_SAMAYE),
        (r"tasmiṃ samaye", lambda m: TASMIM),
        (_alt(COLO) + NA, r_colo),
        (num + r"(?P<name>" + names + r")" + var + r" (?P<v>hoti|honti)" + NA, r_item),
        (names + r"(?: " + names + r")+" + NA, r_nameseq),
        (names + NA, r_name),
        (r"\[[^\]]+\]", r_var),
    ]
    CU_RULES[:] = [(p if p == "REL" else re.compile(p), f) for p, f in list(CU_EXTRA_RULES) + rules]


def clauses_my(s):
    pos, out = 0, []
    while pos < len(s):
        for p, my in CU_SEP:
            if s.startswith(p, pos):
                out.append(my)
                pos += len(p)
                break
        else:
            for rx, f in CU_RULES:
                if rx == "REL":
                    r = r_rel(s, pos)
                    if r:
                        out.append(r[0])
                        pos = r[1]
                        break
                    continue
                m = rx.match(s, pos)
                if m:
                    out.append(f(m))
                    pos = m.end()
                    break
            else:
                raise Miss("no frame: " + s[pos:pos + 100])
    return "".join(out)


def line_cu(body):
    m = HEAD_RE.fullmatch(body)
    if m:
        if m["t"] not in HEAD:
            raise Miss("heading: " + body)
        return f"{m['h']} {HEAD[m['t']]}"
    if LABEL_RE.fullmatch(body):
        return line_my(body)            # a mātikā member: the sample's engine
    return clauses_my(body)


def translate_cu(text):
    if not CU_RULES:
        rebuild_cu()
    out = []
    for line in text.splitlines():
        if not line.strip():
            out.append("")
            continue
        m = ID_RE.search(line)
        body = line[:m.start()] if m else line
        out.append(line_cu(body) + (" " + m.group(1) if m else ""))
    return "\n".join(out).rstrip("\n") + "\n"


rebuild_cu()
