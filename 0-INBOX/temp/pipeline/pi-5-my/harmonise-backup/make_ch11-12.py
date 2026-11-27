"""Burmese zero-shot of pi-5 (Kathāvatthu, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»), chapters 11-12:
11-tatiyavaggo, 12-catutthavaggo.

usage: python3 -I -X utf8 make_ch11-12.py [chapter ...] [--misses] [--units]
Model: the approved sample. Every line is generated from the Pāli by my5_formulas.translate_line() through the
frames, rules and tables of my5_formulas.py, make_sample.py and make_ch6-10.py (all imported READ ONLY: they install
their tables at import and write nothing; their __main__ never runs) and the tables of THIS script, which extends
them IN MEMORY only (nothing in my5_formulas.py / make_sample.py / make_ch6-10.py / my5-zeroshot-terms.md changes).
Strings of make_ch2-5.py (not importable together with make_ch6-10.py) are copied verbatim and checked against the
ch2-5 output files by check_ch11-12.py.
  * PROP_X (propositions), QUOTE_X (sutta quotations), SENT_X (unique sentences), LINES_X (verses, uddāna),
    HEAD_X / COLO_X (headings, colophons); productive propositions are built from small tables;
  * NEW: every new recurring term or phrase (Pāli = Burmese), copied into notes-ch11-12.md.
A unit no frame / rule / table matches stops the run (Miss): nothing is guessed.
"""
import importlib.util
import pathlib
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location("make_ch6_10", HERE / "make_ch6-10.py")
P6 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P6)          # installs make_sample + make_ch6-10 tables; writes nothing
MS = P6.MS
F = P6.F
from my5_formulas import V, FR, Cl, C, END, PE  # noqa: E402

PALI = MS.PALI
OUT = MS.OUT
NAMES_OUT = ["11-tatiyavaggo.md", "12-catutthavaggo.md"]
W = P6.W
PROP_X, QUOTE_X, SENT_X, LINES_X, HEAD_X, COLO_X, ANCHOR_X = {}, {}, {}, {}, {}, {}, {}
VAR_X, REF_X, REF_NOTE_X, BR_X = {}, {}, {}, {}
NEW = {}


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


def section(pali, my):
    HEAD_X[pali] = my
    COLO_X[f"{pali} niṭṭhitā"] = F.DONE.format(my)
    new(pali, my)
    return my


KATHA = F.KATHA_W
EXIST, NEXIST = P6.EXIST, P6.NEXIST

QCH = '"‘’“”'


def key(p):
    """A Pāli proposition / sentence as the engine looks it up: no quotes, no brackets, «…pe…» as «…»."""
    return F.norm_pe(F.BR_RE.sub("", p).translate({ord(c): None for c in QCH}).strip())


def P(pali, cl):
    """A proposition (canonical form: first letter small, quotes / brackets out)."""
    k = key(pali)
    PROP_X[k[:1].lower() + k[1:]] = cl
    return cl


def S(pali, my):
    """A whole sentence (as cut by the engine) -> Burmese with its end mark."""
    SENT_X[key(pali)] = my
    return my


def Q(pali, my):
    """A sutta quotation (without its final «ti») -> Burmese (inner quotes written ‹…›)."""
    QUOTE_X[key(pali)] = my
    return my


def VV(pre, verb, neg=False, post=""):
    return Cl(pre, verb, "မ" + verb, neg, post)


def NSAY(pre, quote_my, neg=True):
    """«S na vattabbaṃ – "Q"» inside a proposition: «S ဤသို့ မဆိုသင့် – “Q”» (Q quoted one level down)."""
    return Cl(f"{pre} ဤသို့".strip(), "ဆိုသင့်", "မဆိုသင့်", neg=neg, post=f" – {quote_my}")


class Fut2(Cl):
    """uppajjissati / nuppajjissati: «ဖြစ်ပေါ်လိမ့်မည်» / «ဖြစ်ပေါ်လိမ့်မည် မဟုတ်»."""

    def __init__(self, pre, neg=False):
        super().__init__(pre, "ဖြစ်ပေါ်လိမ့်မည်", "ဖြစ်ပေါ်လိမ့်မည် မဟုတ်", neg)

    def f(self, form, depth=0):
        v = self.nv if self.neg else self.v
        tail = {"stmt": "", "q": "လော" if not self.neg else "လော", "bare": "", "cond": "ဆိုလျှင်" if not self.neg else "လျှင်",
                "nanu": " မဟုတ်လော", "rel": "သော"}[form]
        if self.neg and form == "q":
            tail = "လော"
        return F.q_set((self.pre + " " if self.pre else "") + v + tail, depth)


# ===================================================================================== shared vocabulary
BUDDHA = F.BHAGAVA                                                   # tathāgato (pi-2 ^2-760 «မြတ်စွာဘုရား»)
TB = W("2", "^2-760", "tathāgatabalaṃ hoti", "ဘုရားဆိုင်ရာ စွမ်းအား")    # tathāgatabala
SAV = W("2", "^2-487", "ariyasāvako", "တပည့်")                         # sāvaka
SB = new("sāvakabalaṃ", f"{SAV}၏ စွမ်းအား")
SADH = new("sāvakasādhāraṇa / sāvakaasādhāraṇa", ("တပည့်တို့နှင့် ဆက်ဆံ", "တပည့်တို့နှင့် မဆက်ဆံ"))
KNOWN = "ဟုတ်မှန်သည့်အတိုင်း သိသော ဉာဏ်"                             # yathābhūtaṃ ñāṇaṃ (pi-2 ^2-809 …)
W("2", "^2-809", "yathābhūtaṃ ñāṇaṃ", KNOWN)
ARIYA_N = new("ariya (noble, of a knowledge)", "အရိယာ အရာ")
SATIP = P6.SATIPATTHANA
GRP11 = {"satipaṭṭhānā": SATIP, "sammappadhānā": P6._SP, "sammappadhānaṃ": P6._SP, "iddhipādā": P6._ID,
         "indriyā": F.INDRIYA_W, "balā": "စွမ်းအား", "bojjhaṅgā": P6._BJW}
for _k in ("sammappadhānā", "sammappadhānaṃ"):      # elided series heads (the others keep the ch8 forms)
    PROP_X.setdefault(_k, FR(GRP11[_k]))
SAKKAYA = W("1", "^1-1006", "sakkāyadiṭṭhi", "ကိုယ်ကို အတ္တဟု ယူဆသော အယူ")
VICI = W("1", "^1-1006", "vicikicchā", "ယုံမှားမှု")
SILAB = W("1", "^1-1006", "sīlabbataparāmāso", "သီလ အကျင့်ဝတ်ဆိုင်ရာ မှားယွင်းသော ယူဆမှု")
DITTHI = W("2", "^2-816", "diṭṭhānusayo", "အယူ")
ANUSAYA = W("2", "^2-816", "anusayo", "ကိန်းအောင်းခြင်း")
PARIYUTTH = W("2", "^2-U70", "pariyuṭṭhānāni", "ထကြွခြင်း")
NIYY = W("1", "^1-343", "niyyānikaṃ", "လွတ်မြောက်ရာသို့ ပို့ဆောင်သော")
MAT = {  # the Mātikā adjectives (pi-1 dyads «X၏ အာရုံ ဖြစ်နိုင်သော» …)
    "lokiya": W("1", "^1-M2-12", "lokiyā dhammā", "လောကနှင့် သက်ဆိုင်သော"),
    "sāsava": "စိတ်အစွန်းအထင်း၏ အာရုံ ဖြစ်နိုင်သော",
    "saṃyojaniya": W("1", "^1-M2-21", "saṃyojaniyā dhammā", "နှောင်ကြိုး၏ အာရုံ ဖြစ်နိုင်သော"),
    "ganthaniya": W("1", "^1-M2-27", "ganthaniyā dhammā", "အထုံး၏ အာရုံ ဖြစ်နိုင်သော"),
    "oghaniya": W("1", "^1-M2-33", "oghaniyā dhammā", "ရေအလျဉ်၏ အာရုံ ဖြစ်နိုင်သော"),
    "yoganiya": W("1", "^1-M2-39", "yoganiyā dhammā", "ထမ်းပိုး၏ အာရုံ ဖြစ်နိုင်သော"),
    "nīvaraṇiya": W("1", "^1-M2-45", "nīvaraṇiyā dhammā", "အတားအဆီး၏ အာရုံ ဖြစ်နိုင်သော"),
    "parāmaṭṭha": W("1", "^1-M2-51", "parāmaṭṭhā dhammā", "မှားယွင်းသော ယူဆမှု၏ အာရုံ ဖြစ်နိုင်သော"),
    "upādāniya": W("1", "^1-M2-70", "upādāniyā dhammā", "စွဲလမ်းမှု၏ အာရုံ ဖြစ်နိုင်သော"),
    "saṃkilesiya": W("1", "^1-M2-76", "saṃkilesikā dhammā", "ကိလေသာ၏ အာရုံ ဖြစ်နိုင်သော"),
}
W("1", "^1-M2-15", "sāsavā dhammā", MAT["sāsava"])
MAT_ALL = "၊ ".join(MAT[k] for k in ("lokiya", "sāsava", "saṃyojaniya", "ganthaniya", "oghaniya", "yoganiya",
                                      "nīvaraṇiya", "parāmaṭṭha", "upādāniya", "saṃkilesiya"))
PAHINA, BHAVITA = P6.PAHINA, P6.BHAVITA                              # («ပယ်ပြီး», «မပယ်ရသေး»), («ပွားများပြီး», …)
SARIPUTTA = "သာရိပုတ္တရာ"                                           # Sāriputta (make_ch2-5 THERA, copied)
AYASMA = "အသျှင်"                                                    # āyasmā (ch5 «အသျှင် ဖဂ္ဂုန»)
DEVA_PL = f"{F.DEVA}တို့"
MANASI = W("2", "^2-604", "na manasi karoti", "နှလုံး မသွင်း")            # manasi karoti «နှလုံးသွင်း»
MK = ("နှလုံးသွင်း", "နှလုံး မသွင်း")
NOTSAY_Q = "ဤသို့ မဆိုသင့်ပါ"

# ===================================================================================== 21. Balakathā
section("Tatiyavaggo", f"{F.ORD_MY[3]} {F.VAGGA_W}")
COLO_X["Tatiyavaggo"] = HEAD_X["Tatiyavaggo"]
section("(21) 1. Balakathā", f"(21) 1. စွမ်းအားအကြောင်း {KATHA}")
section("Balakathā", f"စွမ်းအားအကြောင်း {KATHA}")
OBJ = {  # the objects of the ten powers (pi-2 ^2-760 wording, with «ကို»)
    "ṭhānāṭhān": W("2", "^2-760", "ṭhānañca ṭhānato aṭṭhānañca", "ဖြစ်နိုင်သော အကြောင်း") + "နှင့် မဖြစ်နိုင်သော အကြောင်းကို",
    "kamma": W("2", "^2-760", "kammasamādānānaṃ ṭhānaso hetuso vipākaṃ",
               "အတိတ်၊ အနာဂတ်၊ ပစ္စုပ္ပန် ကံ ဆောက်တည်မှုတို့၏ အကျိုးကို ဖြစ်ရာ အခြေအနေအားဖြင့်၊ အကြောင်းရင်းအားဖြင့်"),
    "sabbattha": W("2", "^2-760", "sabbatthagāminiṃ paṭipadaṃ", "ဘုံ အားလုံးသို့ ရောက်စေသော ကျင့်စဉ်") + "ကို",
    "aneka": W("2", "^2-760", "anekadhātu nānādhātulokaṃ", "ဓာတ် များပြား၍ ဓာတ် အမျိုးမျိုး ရှိသော လောက") + "ကို",
    "adhimutti": W("2", "^2-760", "sattānaṃ nānādhimuttikataṃ", "သတ္တဝါတို့၏ စိတ်ညွတ်ရာ အမျိုးမျိုး ကွဲပြားခြင်း") + "ကို",
    "indriya": W("2", "^2-760", "indriyaparopariyattaṃ", "စွမ်းရည်တို့ မြင့်မြတ်ခြင်း နိမ့်ကျခြင်း") + "ကို",
    "jhāna": W("2", "^2-760", "jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ vuṭṭhānaṃ",
               "ဈာန်၊ လွတ်မြောက်ခြင်း၊ သမာဓိ၊ ဈာန် ဝင်စားရာတို့၏ ညစ်နွမ်းခြင်း၊ စင်ကြယ်ခြင်း၊ ထမြောက်ခြင်း") + "ကို",
    "pubbe": W("2", "^2-760", "pubbenivāsānussatiṃ", "ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့ခြင်း") + "ကို",
    "cutu": W("2", "^2-760", "sattānaṃ cutūpapātaṃ", "သတ္တဝါတို့၏ သေခြင်းနှင့် ဖြစ်ပေါ်ခြင်း") + "ကို",
    "āsava": W("2", "^2-760", "āsavānaṃ khayaṃ", "စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်း") + "ကို",
}
OBJ_PI = {  # Pāli forms -> OBJ key (the accusative after jānāti and the forms before «yathābhūtaṃ ñāṇaṃ»)
    "ṭhānāṭhānaṃ": "ṭhānāṭhān", "ṭhānāṭhāne": "ṭhānāṭhān",
    "atītānāgatapaccuppannānaṃ kammasamādānānaṃ ṭhānaso hetuso vipākaṃ": "kamma",
    "sabbatthagāminiṃ paṭipadaṃ": "sabbattha", "anekadhātuṃ nānādhātuṃ lokaṃ": "aneka",
    "sattānaṃ nānādhimuttikataṃ": "adhimutti", "indriyaparopariyattaṃ": "indriya",
    "jhānavimokkhasamādhisamāpattīnaṃ saṃkilesaṃ vodānaṃ vuṭṭhānaṃ": "jhāna",
    "pubbenivāsānussatiṃ": "pubbe", "pubbenivāsānussati": "pubbe",
    "sattānaṃ cutūpapātaṃ": "cutu", "sattānaṃ cutūpapāte": "cutu", "āsavānaṃ khaye": "āsava",
}
TBK = {}         # Pāli «X yathābhūtaṃ ñāṇaṃ tathāgatabalaṃ» -> Burmese subject
for _p, _k in OBJ_PI.items():
    _n = f"{OBJ[_k]} {KNOWN}ဟူသော {TB}"
    TBK[f"{_p} yathābhūtaṃ ñāṇaṃ tathāgatabalaṃ"] = _n
    P(f"sāvako {_p} jānāti", VV(f"{SAV}သည် {OBJ[_k]}", "သိ"))
for _s, _n in TBK.items():
    P(f"{_s} sāvakasādhāraṇaṃ", Cl(f"{_n}သည် တပည့်တို့နှင့်", "ဆက်ဆံ", "မဆက်ဆံ"))
    P(f"{_s} sāvakaasādhāraṇaṃ", Cl(f"{_n}သည် တပည့်တို့နှင့်", "ဆက်ဆံ", "မဆက်ဆံ", neg=True))
new("X yathābhūtaṃ ñāṇaṃ tathāgatabalaṃ", f"Xကို {KNOWN}ဟူသော {TB}")
P("tathāgatabalaṃ sāvakasādhāraṇaṃ", Cl(f"{TB}သည် တပည့်တို့နှင့်", "ဆက်ဆံ", "မဆက်ဆံ"))
P("tathāgatabalaṃ sāvakabalaṃ, sāvakabalaṃ tathāgatabalaṃ", V(f"{TB}သည် {SB} ဖြစ်၍ {SB}သည် {TB}"))
P("taññeva tathāgatabalaṃ taṃ sāvakabalaṃ, taññeva sāvakabalaṃ taṃ tathāgatabalaṃ",
  V(f"ထို{TB}ပင် ထို{SB} ဖြစ်၍ ထို{SB}ပင် ထို{TB}"))
LIKE = "ကဲ့သို့ပင် {}သည် ထိုနည်းတူ"                                   # yādisaṃ A tādisaṃ B
P("yādisaṃ tathāgatabalaṃ tādisaṃ sāvakabalaṃ, yādisaṃ sāvakabalaṃ tādisaṃ tathāgatabalaṃ",
  V(f"{TB}{LIKE.format(SB)} ဖြစ်၍ {SB}{LIKE.format(TB)}"))
new("yādisaṃ A tādisaṃ B", "Aကဲ့သို့ပင် Bသည် ထိုနည်းတူ ဖြစ်")


def PY(who):     # who pubbayogo pubbacariyā dhammakkhānaṃ dhammadesanā
    return f"{who}၏ ရှေးကာလ အားထုတ်မှု၊ ရှေးကာလ ကျင့်ကြံမှု၊ တရားကို ပြောကြားခြင်း၊ တရားကို ဟောကြားခြင်း"


new("pubbayogo pubbacariyā dhammakkhānaṃ dhammadesanā", PY("X")[len("X၏ "):])
P("yādiso tathāgatassa pubbayogo pubbacariyā dhammakkhānaṃ dhammadesanā tādiso sāvakassa pubbayogo pubbacariyā "
  "dhammakkhānaṃ dhammadesanā", V(f"{PY(BUDDHA)}{LIKE.format(PY(SAV))}"))
EPI11 = new("jino satthā sammāsambuddho sabbaññū sabbadassāvī dhammassāmī dhammappaṭisaraṇo",
            "အောင်နိုင်သူ၊ ဆရာ၊ " + W("1", "^T-1", "sammāsambuddhassa",
                                      "အမှန်ကို ကိုယ်တိုင် အပြည့်အဝ သိမြင်တော်မူသော ဘုရားရှင်")
            + "၊ အလုံးစုံကို သိသူ၊ အလုံးစုံကို မြင်သူ၊ တရား၏ အရှင်၊ တရား၏ ကိုးကွယ်ရာ")
SABBANNU = "အလုံးစုံကို သိသူ၊ အလုံးစုံကို မြင်သူ"
MAGGA_EPI = new("anuppannassa maggassa uppādetā … maggakovido",
                "မဖြစ်ပေါ်သေးသော မဂ်ကို ဖြစ်ပေါ်စေသူ၊ မပေါ်ပေါက်သေးသော မဂ်ကို ပေါ်ပေါက်စေသူ၊ မဟောကြားရသေးသော "
                "မဂ်ကို ဟောကြားသူ၊ မဂ်ကို သိသူ၊ မဂ်ကို နားလည်သူ၊ မဂ်၌ ကျွမ်းကျင်သူ")
for _s, _sm in (("tathāgato", BUDDHA), ("sāvako", SAV)):
    P(f"{_s} jino satthā sammāsambuddho sabbaññū sabbadassāvī dhammassāmī dhammappaṭisaraṇo", V(f"{_sm}သည် {EPI11}"))
    P(f"{_s} anuppannassa maggassa uppādetā asañjātassa maggassa sañjanetā anakkhātassa maggassa akkhātā maggaññū "
      "maggavidū maggakovido", V(f"{_sm}သည် {MAGGA_EPI}"))
P("sāvako sabbaññū sabbadassāvī", V(f"{SAV}သည် {SABBANNU}"))
P("nanu tathāgatassāpi āsavā khīṇā sāvakassāpi āsavā khīṇā",
  V(f"{BUDDHA}၏လည်း စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းပြီး ဖြစ်၍ {SAV}၏လည်း စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းပြီး"))
P("tathāgatassāpi āsavā khīṇā sāvakassāpi āsavā khīṇā",
  V(f"{BUDDHA}၏လည်း စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းပြီး ဖြစ်၍ {SAV}၏လည်း စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းပြီး"))
DIFF = (f"{BUDDHA}၏ဖြစ်စေ {SAV}၏ဖြစ်စေ စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်းနှင့် စိတ်အစွန်းအထင်းတို့ ကုန်ခန်းခြင်း၌ဖြစ်စေ၊ "
        "လွတ်မြောက်ခြင်းနှင့် လွတ်မြောက်ခြင်း၌ဖြစ်စေ တစ်စုံတစ်ရာ ကွဲပြားမှု")
for _n, _neg in (("", False), ("n", True)):
    P(f"{_n}atthi kiñci nānākaraṇaṃ tathāgatassa vā sāvakassa vā āsavakkhayena vā āsavakkhayaṃ vimuttiyā vā vimutti",
      V(DIFF, EXIST, neg=_neg))
S("Natthi.", f"{NEXIST}ပါ{END}")
new("Natthi. (answer)", f"{NEXIST}ပါ{END}")
BR_X["[ayamettha sādhāraṇapakkhaṃ sandhāya paṭikkhepo (ṭīkā oloketabbā)]"] = (
    "[ဤနေရာ၌ ဤငြင်းပယ်ချက်သည် ဆက်ဆံသော ဘက်ကို ရည်ရွယ်၍ ဖြစ်သည် (ဋီကာကို ကြည့်ပါ)]")

# ===================================================================================== 22. Ariyantikathā
section("(22) 2. Ariyantikathā", f"(22) 2. အရိယာ ဟူသော {KATHA}")
section("Ariyantikathā", f"အရိယာ ဟူသော {KATHA}")
SUNNATA = W("1", "^1-1-5-2-0", "Suññataṃ", "ဆိတ်သုဉ်းသော")
APPAN = W("1", "^1-1-5-4-0", "Appaṇihitaṃ", "တောင့်တမှု မရှိသော")
ARAMM = {  # -ārammaṇa (has … as its object)
    "suññat": "ဆိတ်သုဉ်းခြင်းကို", "suññāt": "ဆိတ်သုဉ်းခြင်းကို", "animitt": "အမှတ်အသား မရှိခြင်းကို",
    "appaṇihit": "တောင့်တမှု မရှိခြင်းကို", "appapaṇihit": "တောင့်တမှု မရှိခြင်းကို",
}
AR_V = ("အာရုံပြု", "အာရုံ မပြု")
for _k in ("suññat", "animitt", "appaṇihit"):
    new(f"{_k}ārammaṇa", f"{ARAMM[_k]} {AR_V[0]}သော")


def ar_cl(stem, pre=""):
    return Cl(f"{pre}{ARAMM[stem]}", *AR_V)


for _k in ARAMM:
    for _e in ("aṃ", "ā"):
        P(f"{_k}ārammaṇ{_e}", ar_cl(_k))
ARSUBJ = dict(TBK)
ARSUBJ.update({"satipaṭṭhānā": f"{SATIP}တို့", "bojjhaṅgā": f"{P6._BJW}တို့",
               "sammappadhānā, iddhipādā, indriyā, balā, bojjhaṅgā":
                   f"{P6._SP}၊ {P6._ID}၊ {F.INDRIYA_W}၊ စွမ်းအား၊ {P6._BJW}တို့"})
_AR_RX = r"(?:suññat|suññāt|animitt|appaṇihit|appapaṇihit)ārammaṇ(?:aṃ|ā)"


@F.rule(r"(?P<s>.+?) (?P<a>ariyaṃ|ariyā)(?P<na> na vattabb(?:aṃ|ā) –)? (?P<l>" + _AR_RX + r"(?:… " + _AR_RX + r")*)")
def _r_ariya_ar(m):
    """S ariyaṃ (na vattabbaṃ –) X-ārammaṇaṃ(… Y-ārammaṇaṃ): «Sသည် အရိယာ အရာ ဖြစ်၍ (ဤသို့ မဆိုသင့် – “…”) …»."""
    if m["s"] not in ARSUBJ:
        return None
    items = m["l"].split("… ")
    stems = [re.match(r"(.+?)ārammaṇ", x)[1] for x in items]
    pre = f"{ARSUBJ[m['s']]}သည် {ARIYA_N} ဖြစ်၍"
    if m["na"]:
        if len(items) == 1:
            return NSAY(pre, f"«{ar_cl(stems[0]).f('stmt')}»")
        body = "… ".join(ar_cl(s).f("bare") for s in stems[:-1]) + "… " + ar_cl(stems[-1]).f("stmt")
        return NSAY(pre, body)
    if len(items) == 1:
        return ar_cl(stems[0], pre + " ")
    return Cl(pre + " " + "… ".join(ar_cl(s).f("bare") for s in stems[:-1]) + "… " + ARAMM[stems[-1]], *AR_V)


for _s, _n in TBK.items():
    P(f"{_s} ariyaṃ", V(f"{_n}သည် {ARIYA_N}"))
    P(f"{_s} na vattabbaṃ – ariyaṃ", NSAY(f"{_n}ကို", f"«{ARIYA_N}»ဟု"))
new("X na vattabbaṃ – ariyaṃ", f"Xကို ဤသို့ မဆိုသင့် – “{ARIYA_N}”ဟု")
for _k, _m in (("ṭhānāṭhānañca", OBJ["ṭhānāṭhān"]), ("sattānaṃ cutūpapātañca", OBJ["cutu"]),
               ("suññatañca", "ဆိတ်သုဉ်းခြင်းကို"), ("appaṇihitañca", "တောင့်တမှု မရှိခြင်းကို"),
               ("yathākammūpagatañca", "ကံအားလျော်စွာ ရောက်သွားခြင်းကို")):
    P(f"{_k} manasi karoti", Cl(_m[:-len("ကို")] + "ကိုလည်း", *MK))
new("X-ñca manasi karoti", "Xကိုလည်း နှလုံးသွင်း")
SAMODH = new("dvinnaṃ phassānaṃ dvinnaṃ cittānaṃ samodhānaṃ hoti",
             "တွေ့ထိမှု နှစ်ပါး၊ စိတ် နှစ်ပါးတို့၏ ပေါင်းဆုံခြင်း")
P("dvinnaṃ phassānaṃ dvinnaṃ cittānaṃ samodhānaṃ hoti", V(SAMODH))
_MPN = "မဂ်၊ ဖိုလ်၊ နိဗ္ဗာန်၊ သောတာပတ္တိမဂ်၊ သောတာပတ္တိဖိုလ်"
P("maggo phalaṃ nibbānaṃ, sotāpattimaggo sotāpattiphalaṃ…pe… bojjhaṅgo", V(f"{_MPN}… {P6._BJW}"))
P("animittārammaṇaṃ appaṇihitārammaṇaṃ", Cl(f"{ARAMM['animitt']} {AR_V[0]}၍ {ARAMM['appaṇihit']}", *AR_V))

# ===================================================================================== 23. Vimuttikathā
section("(23) 3. Vimuttikathā", f"(23) 3. လွတ်မြောက်ခြင်းအကြောင်း {KATHA}")
section("Vimuttikathā", f"လွတ်မြောက်ခြင်းအကြောင်း {KATHA}")
VIM = ("လွတ်မြောက်", "မလွတ်မြောက်")
VIMS = ("လွတ်မြောက်ကြ", "မလွတ်မြောက်ကြ")
CITTA = "စိတ်"
SA = {  # sa-X (citta with X), pi-2 ^2-796 «ရာဂ ရှိသော စိတ်»
    "sarāgaṃ": "ရာဂ ရှိသော", "sadosaṃ": "ဒေါသ ရှိသော", "samohaṃ": "မောဟ ရှိသော", "saphassaṃ": "တွေ့ထိမှု ရှိသော",
    "savedanaṃ": "ခံစားမှု ရှိသော", "sasaññaṃ": "မှတ်သိမှု ရှိသော", "sacetanaṃ": "စေ့ဆော်မှု ရှိသော",
    "sapaññaṃ": "ပညာ ရှိသော",
}
W("2", "^2-796", "Sarāgaṃ vā cittaṃ", "ရာဂ ရှိသော စိတ်")
W("2", "^2-796", "sadosaṃ vā cittaṃ", "ဒေါသ ရှိသော စိတ်")
W("2", "^2-796", "samohaṃ vā cittaṃ", "မောဟ ရှိသော စိတ်")
for _k, _m in SA.items():
    new(f"{_k} cittaṃ", f"{_m} {CITTA}")
    P(_k, FR(_m))
    P(f"{_k} cittaṃ vimuccati", Cl(f"{_m} {CITTA}သည်", *VIM))
    for _b in ("sarāgaṃ", "sadosaṃ", "samohaṃ"):
        if _k in ("sarāgaṃ", "sadosaṃ", "samohaṃ"):
            continue
        _bm = SA[_b]
        P(f"{_k} {_b}", FR(f"{_m[:-len('သော')]}၍ {_bm}"))
        P(f"{_k} {_b} cittaṃ vimuccati", Cl(f"{_m[:-len('သော')]}၍ {_bm} {CITTA}သည်", *VIM))
P("sarāgaṃ sadosaṃ samohaṃ cittaṃ vimuccati", Cl(f"ရာဂ ရှိ၍ ဒေါသ ရှိ၍ မောဟ ရှိသော {CITTA}သည်", *VIM))
P("vītarāgaṃ vītadosaṃ vītamohaṃ nikkilesaṃ cittaṃ vimuccati",
  Cl(f"ရာဂ ကင်း၍ ဒေါသ ကင်း၍ မောဟ ကင်း၍ ကိလေသာ ကင်းသော {CITTA}သည်", *VIM))
W("2", "^2-796", "vītarāgaṃ vā cittaṃ", "ရာဂ ကင်းသော စိတ်")
for _k, _m in (("phasso", "တွေ့ထိမှု"), ("paññā", "ပညာ"), ("rāgo", "ရာဂ"), ("doso", "ဒေါသ"), ("moho", "မောဟ")):
    P(f"{_k} ca cittañca ubho vimuccanti", Cl(f"{_m}နှင့် {CITTA} နှစ်ပါးစလုံး", *VIMS))
new("X ca cittañca ubho vimuccanti", f"Xနှင့် {CITTA} နှစ်ပါးစလုံး {VIMS[0]}")
SAHA = {  # X-sahagata … X-anuparivatti (pi-1 dyad words)
    "sahagataṃ": "နှင့်အတူ ဖြစ်သော", "sahajātaṃ": "နှင့်အတူ ပေါ်ပေါက်သော", "saṃsaṭṭhaṃ": "နှင့် ရောနှောသော",
    "sampayuttaṃ": "နှင့် ယှဉ်တွဲသော", "sahabhu": "နှင့်အတူ တည်ရှိသော", "anuparivatti": "နောက်သို့ လိုက်ပါသော",
}
W("1", "^1-M2-59", "cittasaṃsaṭṭhā", "စိတ်နှင့် ရောနှောသော")
W("1", "^1-M2-58", "cittasampayuttā", "စိတ်နှင့် ယှဉ်တွဲသော")
W("1", "^1-M2-61", "cittasahabhuno", "စိတ်နှင့်အတူ တည်ရှိသော")
W("1", "^1-M2-62", "cittānuparivattino", "စိတ်နောက်သို့ လိုက်ပါသော")
new("X-sahajāta", "Xနှင့်အတူ ပေါ်ပေါက်သော")
for _k, _m in (("rāga", "ရာဂ"), ("dosa", "ဒေါသ"), ("moha", "မောဟ")):
    _w = "၊ ".join(f"{_m}{SAHA[s]}" for s in SAHA)
    _pi = (f"{_k}sahagataṃ {_k}sahajātaṃ {_k}saṃsaṭṭhaṃ {_k}sampayuttaṃ {_k}sahabhu {_k[:-1]}ānuparivatti "
           "akusalaṃ lokiyaṃ sāsavaṃ")
    P(_pi, FR(f"{_w}၊ အကုသိုလ် ဖြစ်သော၊ {MAT['lokiya']}၊ {MAT['sāsava']}"))
    P(_pi + " saṃyojaniyaṃ ganthaniyaṃ oghaniyaṃ yoganiyaṃ nīvaraṇiyaṃ parāmaṭṭhaṃ upādāniyaṃ saṃkilesiyaṃ cittaṃ "
      "vimuccati", Cl(f"{_w}၊ အကုသိုလ် ဖြစ်သော၊ {MAT_ALL} {CITTA}သည်", *VIM))
P("saṃkilesiyaṃ cittaṃ vimuccati", Cl(f"{MAT['saṃkilesiya']} {CITTA}သည်", *VIM))
VAR_X["sasaññaṃ"] = F.PATHA

# ===================================================================================== 24. Vimuccamānakathā
section("(24) 4. Vimuccamānakathā", f"(24) 4. လွတ်မြောက်ဆဲ အရာအကြောင်း {KATHA}")
section("Vimuccamānakathā", f"လွတ်မြောက်ဆဲ အရာအကြောင်း {KATHA}")
VIMUTTA = "လွတ်မြောက်ပြီးသော အရာ"
P("vimuttaṃ vimuccamānaṃ", V(f"{VIMUTTA}သည် လွတ်မြောက်ဆဲ အရာ"))
new("vimuttaṃ vimuccamānaṃ", f"{VIMUTTA}သည် လွတ်မြောက်ဆဲ အရာ ဖြစ်")
EK = "တစ်စိတ်တစ်ဒေသ"                                                 # ekadesaṃ (ch2-5 / ch6-10)
P("ekadesaṃ vimuttaṃ, ekadesaṃ avimuttaṃ",
  Cl(f"{EK} လွတ်မြောက်ပြီး၍ {EK}", "လွတ်မြောက်ပြီး", "မလွတ်မြောက်သေး", neg=True))
_FP = P6._FP.replace(P6.CATU, EK)


def ek_head(p_my, phal_my):
    return f"{EK} {p_my} ဖြစ်၍ {EK} {p_my} မဟုတ်၊ {EK} {phal_my}သို့ {_FP}"


_EK_SOT = (f"{ek_head(F.SOTAPANNA, P6.PAT['sotāpattiphala'])}၏၊ {EK} အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ၊ "
           "အမျိုးမှ အမျိုးသို့ ကူးသူ၊ မျိုးစေ့ တစ်စေ့သာ ရှိသူ၊ ဘုရားရှင်၌ မတုန်မလှုပ်သော ကြည်ညိုမှုနှင့် ပြည့်စုံသူ၊ "
           f"တရားတော်၌… သံဃာတော်၌… အရိယာတို့ နှစ်သက်သော သီလတို့နှင့် ပြည့်စုံ၍ {EK} အရိယာတို့ နှစ်သက်သော သီလတို့နှင့်")
assert _EK_SOT.replace(EK, P6.CATU) == P6._SOT
P("ekadesaṃ sotāpanno, ekadesaṃ na sotāpanno, ekadesaṃ sotāpattiphalappatto paṭiladdho adhigato sacchikato "
  "upasampajja viharati, kāyena phusitvā viharati, ekadesaṃ na kāyena phusitvā viharati, ekadesaṃ sattakkhattuparamo "
  "kolaṅkolo ekabījī buddhe aveccappasādena samannāgato dhamme…pe… saṅghe…pe… ariyakantehi sīlehi samannāgato, "
  "ekadesaṃ ariyakantehi sīlehi na samannāgato", Cl(_EK_SOT, "ပြည့်စုံ", "မပြည့်စုံ", neg=True))
P("ekadesaṃ sakadāgāmī, ekadesaṃ na sakadāgāmī, ekadesaṃ sakadāgāmiphalappatto paṭiladdho adhigato sacchikato "
  "upasampajja viharati, kāyena phusitvā viharati, ekadesaṃ na kāyena phusitvā viharati",
  Cl(ek_head(F.SAKADAGAMI, P6.PAT["sakadāgāmiphala"])[:-len(" နေ")], "နေ", "မနေ"))
_PT4 = P6._PT4
_EK_ANA = (f"{ek_head(F.ANAGAMI, P6.PAT['anāgāmiphala'])}၏၊ {EK} {_PT4['antarāparinibbāyī']}၊ "
           f"{_PT4['upahaccaparinibbāyī']}၊ {_PT4['asaṅkhāraparinibbāyī']}၊ {_PT4['sasaṅkhāraparinibbāyī']}၊ {P6._UDH}၊ "
           f"{EK} {P6._UDH}")
P("ekadesaṃ anāgāmī, ekadesaṃ na anāgāmī, ekadesaṃ anāgāmiphalappatto paṭiladdho adhigato sacchikato upasampajja "
  "viharati, kāyena phusitvā viharati, ekadesaṃ na kāyena phusitvā viharati, ekadesaṃ antarāparinibbāyī, "
  "upahaccaparinibbāyī, asaṅkhāraparinibbāyī, sasaṅkhāraparinibbāyī, uddhaṃsotoakaniṭṭhagāmī, ekadesaṃ na "
  "uddhaṃsotoakaniṭṭhagāmī", Cl(_EK_ANA, "ဖြစ်", "မဟုတ်", neg=True))
_EPI = P6.EPI
_EK_ARH = (f"{ek_head(F.ARAHA, P6.PAT['arahatta'])}၏၊ {EK} {_EPI[0][1]}၊ {_EPI[1][1]}၊ {_EPI[2][1]}… "
           f"{EK} မျက်မှောက်ပြုရမည့် အရာကို မျက်မှောက်ပြုပြီး၍ {EK} မျက်မှောက်ပြုရမည့် အရာကို")
P("ekadesaṃ arahā ekadesaṃ na arahā, ekadesaṃ arahattappatto paṭiladdho adhigato sacchikato upasampajja viharati, "
  "kāyena phusitvā viharati, ekadesaṃ na kāyena phusitvā viharati, ekadesaṃ vītarāgo vītadoso vītamoho…pe… ekadesaṃ "
  "sacchikātabbaṃ sacchikataṃ, ekadesaṃ sacchikātabbaṃ na sacchikataṃ",
  Cl(_EK_ARH, P6.SACCHI[0], "မျက်မှောက် မပြုရသေး", neg=True))
P("uppādakkhaṇe vimuttaṃ, bhaṅgakkhaṇe vimuccamānaṃ",
  V("ဖြစ်ခြင်း ခဏ၌ လွတ်မြောက်ပြီး၍ ပြိုပျက်ခြင်း ခဏ၌ လွတ်မြောက်ဆဲ အရာ"))
new("bhaṅgakkhaṇo", "ပြိုပျက်ခြင်း ခဏ")
_TASSA = F.strip_id(F.FINAL.seg("4", "^4-185")[2][0])
_i = _TASSA.index("ဤသို့ သိသော၊ ဤသို့ မြင်သော")
Q("tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati, bhavāsavāpi cittaṃ vimuccati, avijjāsavāpi cittaṃ "
  "vimuccati", _TASSA[_i:_TASSA.index("။", _i)])
F.WITNESS.setdefault("tassa evaṃ jānato evaṃ passato … vimuccati", ("4", "^4-185", QUOTE_X[key(
    "tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati, bhavāsavāpi cittaṃ vimuccati, avijjāsavāpi cittaṃ "
    "vimuccati")]))
_SO = _TASSA.split("။")[0] if False else F.strip_id(F.FINAL.seg("4", "^4-185")[2][0]).split("။")[0]
assert _SO.startswith("ထိုသူသည် ဤသို့ စိတ်သည် တည်ကြည်၍") and _SO.endswith("စိတ်ကို ညွတ်စေ၏")
Q("so evaṃ samāhite citte parisuddhe pariyodāte anaṅgaṇe vigatūpakkilese mudubhūte kammaniye ṭhite āneñjappatte "
  "āsavānaṃ khayañāṇāya cittaṃ abhininnāmeti", _SO)
F.WITNESS.setdefault("so evaṃ samāhite citte … āsavānaṃ khayañāṇāya cittaṃ abhininnāmeti", ("4", "^4-185", _SO))
BR_X["[dī. ni. 1.248 ādayo]"] = "[“ဒီဃနိကာယ်” 1.248 စသည်]"
VAR_X["tena hi"] = F.PATHA
VAR_X["tena hi na vattabbaṃ"] = F.PATHA
P("atthi cittaṃ vimuccamānaṃ", V("လွတ်မြောက်ဆဲ စိတ်", EXIST))
P("atthi cittaṃ rajjamānaṃ dussamānaṃ muyhamānaṃ kilissamānaṃ",
  V("တပ်မက်ဆဲ၊ ဒေါသ ဖြစ်ဆဲ၊ တွေဝေဆဲ၊ ညစ်နွမ်းဆဲ စိတ်", EXIST))
_BOTH = ("တပ်မက်ပြီးသည်လည်း ဖြစ်၍ မတပ်မက်သည်လည်း ဖြစ်၊ ဒေါသ ဖြစ်ပြီးသည်လည်း ဖြစ်၍ ဒေါသ မဖြစ်သည်လည်း ဖြစ်၊ "
         "တွေဝေပြီးသည်လည်း ဖြစ်၍ မတွေဝေသည်လည်း ဖြစ်၊ ဖြတ်ပြီးသည်လည်း ဖြစ်၍ မဖြတ်ရသေးသည်လည်း ဖြစ်၊ "
         "ခွဲပြီးသည်လည်း ဖြစ်၍ မခွဲရသေးသည်လည်း ဖြစ်၊ ပြုပြီးသည်လည်း ဖြစ်၍ မပြုရသေးသည်လည်း")
P("rattañceva arattañca, duṭṭhañceva aduṭṭhañca, mūḷhañceva amūḷhañca, chinnañceva achinnañca, bhinnañceva "
  "abhinnañca, katañceva akatañca", V(f"ထိုစိတ်သည် {_BOTH}"))


@F.frame(r"nanu (?P<p>.+?)ti\?")
def _f_nanu_small(m):
    """…pe… nanu P-ti? (a small letter after «…pe… »)."""
    return F.pq(m["p"], "nanu") + END


def before_generic():
    """Move the frame just registered before the generic «P-ti?» / «P-ti.» frames."""
    fr = F.FRAMES.pop()
    F.FRAMES.insert(next(i for i, (_, fn) in enumerate(F.FRAMES) if fn is F._f_q), fr)


before_generic()

# ===================================================================================== 25. Aṭṭhamakakathā
section("(25) 5. Aṭṭhamakakathā", f"(25) 5. အဋ္ဌမ ပုဂ္ဂိုလ်အကြောင်း {KATHA}")
section("Aṭṭhamakakathā", f"အဋ္ဌမ ပုဂ္ဂိုလ်အကြောင်း {KATHA}")
AP = new("aṭṭhamako puggalo (the eighth person)", f"{F.ORD_MY[8]} {F.PUGGALA}")
GOTRA = W("4", "^4-M-7", "Gotrabhū", "အရိယာ အနွယ်သို့ ပြောင်းသူ")
GP = new("gotrabhū puggalo", "အရိယာ အနွယ်သို့ ပြောင်းသော ပုဂ္ဂိုလ်")
KX = {  # kilesa objects of «… pahīnaṃ» (Pāli nominative -> (Burmese, neuter?))
    "diṭṭhipariyuṭṭhānaṃ": f"{DITTHI} {PARIYUTTH}", "vicikicchāpariyuṭṭhānaṃ": f"{VICI} {PARIYUTTH}",
    "diṭṭhānusayo": f"{DITTHI} {ANUSAYA}", "vicikicchānusayo": f"{VICI} {ANUSAYA}", "sīlabbataparāmāso": SILAB,
}
new("diṭṭhipariyuṭṭhānaṃ", KX["diṭṭhipariyuṭṭhānaṃ"])
new("diṭṭhānusayo / vicikicchānusayo", f"{KX['diṭṭhānusayo']} / {KX['vicikicchānusayo']}")
_PH = {"diṭṭhipariyuṭṭhānaṃ": ("pahīnaṃ", "appahīnaṃ"), "vicikicchāpariyuṭṭhānaṃ": ("pahīnaṃ", "appahīnaṃ"),
       "diṭṭhānusayo": ("pahīno", "appahīno"), "vicikicchānusayo": ("pahīno", "appahīno"),
       "sīlabbataparāmāso": ("pahīno", "appahīno")}
for _sp, _sm in (("aṭṭhamakassa puggalassa ", f"{AP}သည် "), ("gotrabhuno puggalassa ", f"{GP}သည် "), ("", "")):
    if _sp:
        P(_sp.strip(), FR(_sm.strip()[:-len("သည်")] + "၌"))
    for _k, _km in KX.items():
        _p, _a = _PH[_k]
        if _sp:
            P(f"{_sp}{_k}", FR(f"{_sm}{_km}"))
        P(f"{_sp}{_k} {_p}", Cl(f"{_sm}{_km}ကို", *PAHINA))
        P(f"{_sp}{_k} {_a}", Cl(f"{_sm}{_km}ကို", *PAHINA, neg=True))
        P(f"{_sp}{_k} nuppajjissatīti katvā {_p}",
          Cl(f"{_sm}{_km} ဖြစ်ပေါ်လိမ့်မည် မဟုတ်{F.KATVA} ထိုအရာကို", *PAHINA))
        if _k.endswith("pariyuṭṭhānaṃ"):
            _st = _k[:-1]
            P(f"{_sp}{_st}pahānāya maggo bhāvito", Cl(f"{_sm}{_km}ကို ပယ်ရန် မဂ်ကို", *BHAVITA))
            P(f"{_sp}{_st}pahānāya maggo abhāvito", Cl(f"{_sm}{_km}ကို ပယ်ရန် မဂ်ကို", *BHAVITA, neg=True))
            for _g in ("satipaṭṭhānā", "bojjhaṅgā"):
                P(f"{_sp}{_st}pahānāya {_g} bhāvitā", Cl(f"{_sm}{_km}ကို ပယ်ရန် {GRP11[_g]}ကို", *BHAVITA))
                P(f"{_sp}{_st}pahānāya {_g} abhāvitā",
                  Cl(f"{_sm}{_km}ကို ပယ်ရန် {GRP11[_g]}ကို", *BHAVITA, neg=True))
                P(f"{_sp}{_st}pahānāya {_g}", FR(f"{_sm}{_km}ကို ပယ်ရန် {GRP11[_g]}"))
            P(f"{_sp}{_st}pahānāya maggo bhāvito", Cl(f"{_sm}{_km}ကို ပယ်ရန် မဂ်ကို", *BHAVITA))
for _g in ("satipaṭṭhānā", "bojjhaṅgā"):
    P(f"{_g} abhāvitā", Cl(f"{GRP11[_g]}ကို", *BHAVITA, neg=True))
_VKM = KX["vicikicchāpariyuṭṭhānaṃ"]
P("aṭṭhamakassa puggalassa vicikicchāpariyuṭṭhānapahānāya maggo abhāvito…pe… satipaṭṭhānā…pe… bojjhaṅgā abhāvitā",
  Cl(f"{AP}သည် {_VKM}ကို ပယ်ရန် မဂ်ကို {BHAVITA[1]}… {SATIP}ကို… {P6._BJW}ကို", *BHAVITA, neg=True))
_SOT_FP = f"{F.SOTAPANNA} ဖြစ်၍ {P6.PAT['sotāpattiphala']}သို့ ရောက်၍ ရ၍ ပြည့်မီ၍ မျက်မှောက်ပြု၍ ပြည့်စုံစေလျက် နေ၏၊ ကိုယ်ဖြင့် တွေ့ထိ၍"
P("aṭṭhamako puggalo sotāpanno sotāpattiphalappatto paṭiladdho adhigato sacchikato upasampajja viharati, kāyena "
  "phusitvā viharati", Cl(f"{AP}သည် {_SOT_FP}", "နေ", "မနေ"))
P("aṭṭhamako puggalo sotāpanno sotāpattiphalappatto…pe… kāyena phusitvā viharati",
  Cl(f"{AP}သည် {F.SOTAPANNA} ဖြစ်၍ {P6.PAT['sotāpattiphala']}သို့ ရောက်၍… ကိုယ်ဖြင့် တွေ့ထိ၍", "နေ", "မနေ"))
AMAGGA = (f"မဂ် မဟုတ်သော၊ {MAT['lokiya']}၊ {MAT['sāsava']}… {MAT['saṃkilesiya']} အရာဖြင့်")
P("amaggena pahīnaṃ lokiyena sāsavena…pe… saṃkilesiyena", Cl(AMAGGA, *PAHINA))
new("amaggena pahīnaṃ lokiyena sāsavena… saṃkilesiyena", f"{AMAGGA} {PAHINA[0]}")
S("Uppajjissatīti?", f"ဖြစ်ပေါ်လိမ့်မည်လော{END}")
S("Nuppajjissati.", f"ဖြစ်ပေါ်လိမ့်မည် မဟုတ်ပါ{END}")
P("nuppajjissati", Fut2("", neg=True))
new("uppajjissati / nuppajjissati", "ဖြစ်ပေါ်လိမ့်မည် / ဖြစ်ပေါ်လိမ့်မည် မဟုတ်")

# ===================================================================================== 26. Aṭṭhamakassa indriyakathā
section("(26) 6. Aṭṭhamakassaindriyakathā", f"(26) 6. အဋ္ဌမ ပုဂ္ဂိုလ်၏ စွမ်းရည်အကြောင်း {KATHA}")
section("Aṭṭhamakassa indriyakathā", f"အဋ္ဌမ ပုဂ္ဂိုလ်၏ စွမ်းရည်အကြောင်း {KATHA}")
_IN = {k: v.my for k, (v, r) in F.NOUN.items() if k.endswith("indriyaṃ")}
IND = {"saddhā": W("1", "^1-95", "Saddhābalaṃ", "ယုံကြည်မှု"), "vīriyaṃ": "ဝီရိယ", "sati": "သတိ",
       "samādhi": "သမာဓိ", "paññā": "ပညာ", "mano": "မနော", "somanassaṃ": "ဝမ်းမြောက်မှု", "jīvitaṃ": "အသက်",
       "pañcindriyāni": f"{F.INDRIYA_W} {F.NUM_MY[5]}{F.CL}"}
for _k in ("saddhindriyaṃ", "vīriyindriyaṃ", "satindriyaṃ", "samādhindriyaṃ", "paññindriyaṃ", "manindriyaṃ",
           "somanassindriyaṃ", "jīvitindriyaṃ"):
    IND[_k] = _IN[_k]
for _k, _m in IND.items():
    P6.LST.setdefault(_k, _m)
    P(f"atthi {_k}", V(_m, EXIST))
    P(f"natthi {_k}", V(_m, EXIST, neg=True))
AP_LOC = f"{AP}၌"
P6.GEN.update({"aṭṭhamakassa puggalassa": AP_LOC, "tattha": "ထို၌", "devesu": f"{DEVA_PL}၌",
               "manussesu": f"{F.MANUSSA}တို့၌"})
PAT_GEN = {"sakadāgāmiphalasacchikiriyāya paṭipannassa puggalassa": "sakadāgāmiphala",
           "anāgāmiphalasacchikiriyāya paṭipannassa puggalassa": "anāgāmiphala",
           "arahattasacchikiriyāya paṭipannassa puggalassa": "arahatta"}
for _g, _f in PAT_GEN.items():
    P6.GEN[_g] = f"{P6.PAT[_f]}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော {F.PUGGALA}၌"
    P(_g, FR(P6.GEN[_g]))
for _k, _m in (("assaddho", W("2", "^2-851", "assaddho samāno", "ယုံကြည်မှု မရှိသူ")),
               ("kusīto hīnavīriyo", W("2", "^2-851", "kusīto samāno", "ပျင်းရိသူ")[:-len("သူ")] + "၍ ဝီရိယ ယုတ်လျော့သူ"),
               ("muṭṭhassati asampajāno", W("2", "^2-851", "muṭṭhassatī samāno", "သတိ လစ်သူ")[:-len("သူ")]
                + "၍ ကောင်းစွာ ဆင်ခြင်သိမြင်ခြင်း ကင်းသူ"),
               ("asamāhito vibbhantacitto", W("2", "^2-851", "asamāhito samāno", "စိတ် မတည်ကြည်သူ")[:-len("သူ")]
                + "၍ စိတ် ပျံ့လွင့်သူ"),
               ("duppañño elamūgo", W("2", "^2-851", "duppañño samāno", "ပညာ နည်းသူ")[:-len("သူ")] + "၍ နုံအ ထုံထိုင်းသူ"),
               ("bāhiro puthujjanapakkhe ṭhito", f"သာသနာပ {P6.PUTHU} ဘက်၌ တည်သူ")):
    new(_k, _m)
    P(f"aṭṭhamako puggalo {_k}", V(f"{AP}သည် {_m}"))
_NIY = {"saddhā": ("sā ca saddhā niyyānikā", "ထိုယုံကြည်မှုသည်လည်း"), "vīriyaṃ": ("tañca vīriyaṃ niyyānikaṃ", "ထိုဝီရိယသည်လည်း"),
        "sati": ("sā ca sati niyyānikā", "ထိုသတိသည်လည်း"), "samādhi": ("so ca samādhi niyyāniko", "ထိုသမာဓိသည်လည်း"),
        "paññā": ("sā ca paññā niyyānikā", "ထိုပညာသည်လည်း")}
for _k, (_p, _m) in _NIY.items():
    P(_p, V(f"{_m} {NIYY} အရာ"))
    P(f"atthi {_k}, {_p}", V(f"{IND[_k]} ရှိ၍ {_m} {NIYY} အရာ"))
new("sā ca saddhā niyyānikā", f"ထိုယုံကြည်မှုသည်လည်း {NIYY} အရာ ဖြစ်")
S('Nanu vuttaṃ bhagavatā – "pañcimāni, bhikkhave, indriyāni! Katamāni pañca? Saddhindriyaṃ, vīriyindriyaṃ, '
  'satindriyaṃ, samādhindriyaṃ, paññindriyaṃ – imāni kho, bhikkhave, pañcindriyāni. Imesaṃ kho, bhikkhave, pañcannaṃ '
  'indriyānaṃ samattā paripūrattā arahā hoti. Tato mudutarehi arahattasacchikiriyāya paṭipanno hoti, tato mudutarehi '
  'anāgāmī hoti, tato mudutarehi anāgāmiphalasacchikiriyāya paṭipanno hoti, tato mudutarehi sakadāgāmī hoti, tato '
  'mudutarehi sakadāgāmiphalasacchikiriyāya paṭipanno hoti, tato mudutarehi sotāpanno hoti, tato mudutarehi '
  'sotāpattiphalasacchikiriyāya paṭipanno hoti. Yassa kho, bhikkhave, imāni pañcindriyāni sabbena sabbaṃ sabbathā '
  'sabbaṃ natthi, tamahaṃ ‘bāhiro puthujjanapakkhe ṭhito’ti vadāmī"ti [saṃ. ni. 5.488].',
  f"{BUDDHA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “ရဟန်းတို့၊ ဤ{F.INDRIYA_W} ငါးပါးတို့ ရှိကုန်၏၊ အဘယ် ငါးပါးတို့နည်း။ "
  f"{IND['saddhindriyaṃ']}၊ {IND['vīriyindriyaṃ']}၊ {IND['satindriyaṃ']}၊ {IND['samādhindriyaṃ']}၊ "
  f"{IND['paññindriyaṃ']} – ရဟန်းတို့၊ ဤသည်တို့ကား {F.INDRIYA_W} ငါးပါးတို့ ဖြစ်ကုန်၏။ ရဟန်းတို့၊ ဤ{F.INDRIYA_W} "
  f"ငါးပါးတို့ ပြည့်စုံခြင်း၊ ပြည့်ဝခြင်းကြောင့် {F.ARAHA} ဖြစ်၏။ ထိုထက် နုံ့သော {F.INDRIYA_W}တို့ကြောင့် "
  f"{P6.PAT['arahatta']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသူ ဖြစ်၏၊ ထိုထက် နုံ့သော {F.INDRIYA_W}တို့ကြောင့် {F.ANAGAMI} "
  f"ဖြစ်၏၊ ထိုထက် နုံ့သော {F.INDRIYA_W}တို့ကြောင့် {P6.PAT['anāgāmiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသူ ဖြစ်၏၊ "
  f"ထိုထက် နုံ့သော {F.INDRIYA_W}တို့ကြောင့် {F.SAKADAGAMI} ဖြစ်၏၊ ထိုထက် နုံ့သော {F.INDRIYA_W}တို့ကြောင့် "
  f"{P6.PAT['sakadāgāmiphala']}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသူ ဖြစ်၏၊ ထိုထက် နုံ့သော {F.INDRIYA_W}တို့ကြောင့် "
  f"{F.SOTAPANNA} ဖြစ်၏၊ ထိုထက် နုံ့သော {F.INDRIYA_W}တို့ကြောင့် {P6.PAT['sotāpattiphala']}ကို မျက်မှောက်ပြုရန် "
  f"ကျင့်ကြံသူ ဖြစ်၏။ ရဟန်းတို့၊ အကြင်သူ၌ ဤ{F.INDRIYA_W} ငါးပါးတို့သည် အလုံးစုံ လုံးဝ မရှိကုန်၊ ထိုသူကို "
  f"‘သာသနာပ {P6.PUTHU} ဘက်၌ တည်သူ’ဟု ငါ ဆို၏”ဟူ၍{END}")
W("2", "^2-814", "indriyaparopariyattaṃ", "စွမ်းရည် ထက်မြက်သော၊ စွမ်းရည် နုံ့သော")

# ===================================================================================== 27-28. Dibbacakkhu / Dibbasota
section("(27) 7. Dibbacakkhukathā", f"(27) 7. နတ်မျက်စိအကြောင်း {KATHA}")
section("Dibbacakkhukathā", f"နတ်မျက်စိအကြောင်း {KATHA}")
section("(28) 8. Dibbasotakathā", f"(28) 8. နတ်နားအကြောင်း {KATHA}")
section("Dibbasotakathā", f"နတ်နားအကြောင်း {KATHA}")
DC = W("4", "^4-184", "dibbena cakkhunā", "နတ်မျက်စိ")                  # dibbacakkhu
MC = new("maṃsacakkhu", "ပကတိ မျက်စိ")
PC = new("paññācakkhu", "ပညာမျက်စိ")
DS = new("dibbasota", "နတ်နား")
MS_ = new("maṃsasota", "ပကတိ နား")
DHUP = new("dhammupatthaddha", "တရား၏ ထောက်ပံ့မှုကို ရသော")
BEC = ("ဖြစ်လာ", "မဖြစ်လာ")                                         # hoti (becomes)
EYE = {"maṃsacakkhuṃ": MC, "dibbacakkhuṃ": DC, "paññācakkhuṃ": PC, "maṃsasotaṃ": MS_, "dibbasotaṃ": DS}
for _a, _am in EYE.items():
    for _b, _bm in EYE.items():
        if _a == _b or (_a.endswith("sotaṃ") != _b.endswith("sotaṃ")):
            continue
        P(f"{_a} dhammupatthaddhaṃ {_b} hoti", Cl(f"{DHUP} {_am}သည် {_bm}", *BEC))
        P(f"{_a} {_b}, {_b} {_a}", V(f"{_am}သည် {_bm} ဖြစ်၍ {_bm}သည် {_am}"))
        P(f"yādisaṃ {_a} tādisaṃ {_b}, yādisaṃ {_b} tādisaṃ {_a}", V(f"{_am}{LIKE.format(_bm)} ဖြစ်၍ {_bm}{LIKE.format(_am)}"))
        P(f"taññeva {_a} taṃ {_b}, taṃ {_b} taṃ {_a}", V(f"ထို{_am}ပင် ထို{_bm} ဖြစ်၍ ထို{_bm}ပင် ထို{_am}"))
VIS = "နယ်ပယ်၊ အစွမ်း၊ ကျက်စားရာ"                                    # visayo ānubhāvo gocaro
new("visayo ānubhāvo gocaro", VIS)
for _a, _am, _b, _bm in (("maṃsacakkhussa", MC, "dibbassa cakkhussa", DC), ("maṃsasotassa", MS_, "dibbassa sotassa", DS)):
    P(f"yādiso {_a} visayo ānubhāvo gocaro tādiso {_b} visayo ānubhāvo gocaro",
      V(f"{_am}၏ {VIS}{LIKE.format(_bm + '၏ ' + VIS)}"))
KAMA_AV = W("1", "^1-M2-93", "kāmāvacarā dhammā", "ကာမဘုံနှင့် ဆိုင်သော")
RUPA_AV = W("1", "^1-M2-94", "rūpāvacarā dhammā", "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော")
ARUPA_AV = W("1", "^1-M2-95", "arūpāvacarā dhammā", "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော")
PARIY = W("1", "^1-M2-96", "pariyāpannā dhammā", "ဘဝဘုံတို့၌ အကျုံးဝင်သော")
APARIY = W("1", "^1-M2-96", "apariyāpannā dhammā", "ဘဝဘုံတို့၌ အကျုံးမဝင်သော")
UPAD = W("1", "^1-M1-4", "upādiṇṇupādāniyā", "ကံကြောင့် ဖြစ်")
HUTVA = {"upādiṇṇaṃ": f"{UPAD}သော", "anupādiṇṇaṃ": "ကံကြောင့် မဖြစ်သော", "kāmāvacaraṃ": KAMA_AV,
         "rūpāvacaraṃ": RUPA_AV, "arūpāvacaraṃ": ARUPA_AV, "pariyāpannaṃ": PARIY, "apariyāpannaṃ": APARIY}
for _a, _b in (("upādiṇṇaṃ", "anupādiṇṇaṃ"), ("kāmāvacaraṃ", "rūpāvacaraṃ"), ("rūpāvacaraṃ", "arūpāvacaraṃ"),
               ("pariyāpannaṃ", "apariyāpannaṃ")):
    P(f"{_a} hutvā {_b} hoti", Cl(f"{HUTVA[_a]} အရာ ဖြစ်ပြီးမှ {HUTVA[_b]} အရာ", *BEC))
new("X hutvā Y hoti", "X ဖြစ်ပြီးမှ Y ဖြစ်လာ")
VAR_X["upādinnaṃ"] = F.LEKHANA
P("dveva cakkhūni", V(f"မျက်စိ {F.NUM_MY[2]}{F.CL}သာ", EXIST))
for _k in ("ekaṃyeva sotaṃ", "ekaññeva sotaṃ"):
    P(_k, V(f"နား {F.NUM_MY[1]}{F.CL}တည်းသာ", EXIST))
for _k in ("tīṇi cakkhūni vuttāni bhagavatā – maṃsacakkhuṃ, dibbacakkhuṃ, paññācakkhuṃ", ):
    P(_k, Cl(f"မျက်စိ {F.NUM_MY[3]}{F.CL}တို့ကို {BUDDHA}", "ဟောတော်မူ", "မဟောတော်မူ", post=f" – {MC}၊ {DC}၊ {PC}"))
P("dve sotāni vuttāni bhagavatā – maṃsasotaṃ, dibbasotaṃ",
  Cl(f"နား {F.NUM_MY[2]}{F.CL}တို့ကို {BUDDHA}", "ဟောတော်မူ", "မဟောတော်မူ", post=f" – {MS_}၊ {DS}"))
S('Nanu dve sotāni vuttāni bhagavatā – "maṃsasotaṃ, dibbasota"nti?',
  f"နား {F.NUM_MY[2]}{F.CL}တို့ကို {BUDDHA} ဟောတော်မူသည် မဟုတ်လော – “{MS_}၊ {DS}”{END}")
Q("tīṇimāni, bhikkhave, cakkhūni! Katamāni tīṇi? Maṃsacakkhuṃ, dibbacakkhuṃ, paññācakkhunti – imāni kho, bhikkhave, "
  "tīṇi cakkhūni", f"ရဟန်းတို့၊ ဤမျက်စိ {F.NUM_MY[3]}{F.CL}တို့ ရှိကုန်၏၊ အဘယ် {F.NUM_MY[3]}{F.CL}တို့နည်း။ {MC}၊ {DC}၊ "
  f"{PC}ဟူ၍ – ရဟန်းတို့၊ ဤသည်တို့ကား မျက်စိ {F.NUM_MY[3]}{F.CL}တို့ ဖြစ်ကုန်၏")
LINES_X[key('"Maṃsacakkhuṃ dibbacakkhuṃ, paññācakkhuṃ anuttaraṃ;')] = f"“{MC}၊ {DC}၊ အမြတ်ဆုံး {PC}၊"
LINES_X[key("Etāni tīṇi cakkhūni, akkhāsi purisuttamo.")] = (
    f"ဤမျက်စိ {F.NUM_MY[3]}{F.CL}တို့ကို လူတို့တွင် အမြတ်ဆုံးသူသည် ဟောကြားတော်မူခဲ့၏{END}")
LINES_X[key('"Maṃsacakkhussa uppādo, maggo dibbassa cakkhuno;')] = f"“{MC}၏ ဖြစ်ပေါ်ခြင်း၊ {DC}၏ လမ်း၊"
LINES_X[key("Yadā ca ñāṇaṃ udapādi, paññācakkhuṃ anuttaraṃ;")] = f"အကြင်အခါ၌ အမြတ်ဆုံး {PC}ဟူသော ဉာဏ် ဖြစ်ပေါ်လာ၏၊"
LINES_X[key('Tassa cakkhussa paṭilābhā, sabbadukkhā pamuccatī"ti [itivu. 61 itivuttake].')] = (
    "ထိုမျက်စိကို ရခြင်းကြောင့် ဒုက္ခ အားလုံးမှ လွတ်မြောက်၏”ဟူ၍ ⟦0⟧။")
REF_NOTE_X["itivuttake"] = f"{F.REF['itivu.']}၌"

# ===================================================================================== 29. Yathākammūpagatañāṇakathā
section("(29) 9. Yathākammūpagatañāṇakathā", f"(29) 9. ကံအားလျော်စွာ ရောက်သွားခြင်းကို သိသော ဉာဏ်အကြောင်း {KATHA}")
section("Yathākammūpagatañāṇakathā", f"ကံအားလျော်စွာ ရောက်သွားခြင်းကို သိသော ဉာဏ်အကြောင်း {KATHA}")
YK = new("yathākammūpagata", "ကံအားလျော်စွာ ရောက်သွားခြင်း")
YKN = new("yathākammūpagataṃ ñāṇaṃ", f"{YK}ကို သိသော ဉာဏ်")
VAR_X["yathākammūpagatañāṇaṃ"] = F.LEKHANA
P("yathākammūpagataṃ ñāṇaṃ dibbacakkhuṃ", V(f"{YKN}သည် {DC}"))
SEE = f"{DC}ဖြင့် အဆင်းအရောင်ကို"                               # dibbena cakkhunā rūpaṃ passati (ch10 / pi-1 ^1-1352 rūpa)
new("dibbena cakkhunā rūpaṃ passati (after «manasi karoti»)", f"{SEE} မြင်")


@F.rule(r"(?P<l>.+?manasi karoti), dibbena cakkhunā rūpaṃ passati")
def _r_see(m):
    """… manasi karoti, dibbena cakkhunā rūpaṃ passati (the sample's «… ရုပ်ကို မြင်သူ» is an agent in a series)."""
    try:
        pre = F.prop_my(m["l"], "stmt")
    except F.Miss:
        return None
    return VV(f"{pre}{C} {SEE}", "မြင်")
_D4 = F.strip_id(F.FINAL.seg("4", "^4-184")[2][0])
THOUGHT = {  # «X"ti ca manasi karoti»: the thoughts of the divine-eye passage (pi-4 ^4-184 wording)
    "ime vata bhonto sattā": "အချင်းတို့၊ ဤသတ္တဝါတို့သည်",
    "kāyaduccaritena samannāgatā": "ကိုယ်ဖြင့် ပြုသော ဒုစရိုက်နှင့် အပြည့်အဝ ပြည့်စုံကြ၏",
    "vacīduccaritena samannāgatā": "နှုတ်ဖြင့် ပြုသော ဒုစရိုက်နှင့် အပြည့်အဝ ပြည့်စုံကြ၏",
    "manoduccaritena samannāgatā": "မနောဖြင့် ပြုသော ဒုစရိုက်နှင့် အပြည့်အဝ ပြည့်စုံကြ၏",
    "ariyānaṃ upavādakā": "အရိယာတို့ကို စွပ်စွဲ ပြောဆိုကြ၏",
    "micchādiṭṭhikā": "မှားယွင်းသော အယူ ရှိကြ၏",
    "micchādiṭṭhikammasamādānā": "မှားယွင်းသော အယူကြောင့် ဖြစ်သော ကံကို ဆောက်တည်ကြ၏",
    "te kāyassa bhedā paraṃ maraṇā apāyaṃ duggatiṃ vinipātaṃ nirayaṃ upapannā":
        "ထိုသူတို့သည် ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက် အပါယ်၊ ဆိုးသော လားရာ၊ ပျက်စီး ကျရောက်ရာ၊ ငရဲ၌ ပြန်လည် ဖြစ်ပေါ်ကြပြီ",
    "ime vā pana bhonto sattā": "သို့မဟုတ် အချင်းတို့၊ ဤသတ္တဝါတို့သည်",
    "kāyasucaritena samannāgatā": "ကိုယ်ဖြင့် ပြုသော သုစရိုက်နှင့် အပြည့်အဝ ပြည့်စုံကြ၏",
    "vacīsucaritena samannāgatā": "နှုတ်ဖြင့် ပြုသော သုစရိုက်နှင့် အပြည့်အဝ ပြည့်စုံကြ၏",
    "manosucaritena samannāgatā": "မနောဖြင့် ပြုသော သုစရိုက်နှင့် အပြည့်အဝ ပြည့်စုံကြ၏",
    "ariyānaṃ anupavādakā": "အရိယာတို့ကို မစွပ်စွဲကြ",
    "sammādiṭṭhikā": "မှန်ကန်သော အယူ ရှိကြ၏",
    "sammādiṭṭhikammasamādānā": "မှန်ကန်သော အယူကြောင့် ဖြစ်သော ကံကို ဆောက်တည်ကြ၏",
    "sammādiṭṭhikammasammādānā": "မှန်ကန်သော အယူကြောင့် ဖြစ်သော ကံကို ဆောက်တည်ကြ၏",
    "te kāyassa bhedā paraṃ maraṇā sugatiṃ saggaṃ lokaṃ upapannā":
        "ထိုသူတို့သည် ခန္ဓာကိုယ် ပြိုကွဲ၍ သေပြီးနောက် ကောင်းသော လားရာ၊ နတ်ပြည် လောက၌ ပြန်လည် ဖြစ်ပေါ်ကြပြီ",
}
for _k, _m in THOUGHT.items():
    assert _m.replace("သို့မဟုတ် ", "") in _D4, _k
    F.WITNESS.setdefault(_k, ("4", "^4-184", _m))


@F.rule(r"(?P<q>.+?)ti ca manasi karoti")
def _r_thought(m):
    """"X"ti ca manasi karoti: «“X”ဟုလည်း နှလုံးသွင်း» (X from the divine-eye passage)."""
    if m["q"] not in THOUGHT:
        return None
    return Cl(f"«{THOUGHT[m['q']]}»ဟုလည်း", *MK)


P("atthi koci adibbacakkhuko dibbacakkhuṃ appaṭiladdho anadhigato asacchikato yathākammūpagataṃ jānāti",
  V(f"{DC} မရှိသော၊ {DC}ကို မရသေးသော၊ မရောက်သေးသော၊ မျက်မှောက် မပြုရသေးသော၊ {YK}ကို သိသော "
    "တစ်စုံတစ်ယောက်", EXIST))
SARI = f"{AYASMA} {SARIPUTTA}"
P("āyasmā sāriputto yathākammūpagataṃ ñāṇaṃ jānāti", VV(f"{SARI}သည် {YKN}ကို", "သိ"))
P("atthāyasmato sāriputtassa dibbacakkhuṃ", V(f"{SARI}၌ {DC}", EXIST))
S("Nanu āyasmā sāriputto etadavoca –", f"{SARI}သည် ဤသို့ ပြောခဲ့သည် မဟုတ်လော –")
LINES_X[key('"Neva pubbenivāsāya, napi dibbassa cakkhuno;')] = (
    "“ရှေးဘဝများကို အဖန်ဖန် အောက်မေ့ခြင်းအတွက်လည်း မဟုတ်၊ နတ်မျက်စိအတွက်လည်း မဟုတ်၊")
LINES_X[key("Cetopariyāya iddhiyā, sotadhātuvisuddhiyā;")] = (
    "သူတစ်ပါး စိတ်ကို ပိုင်းခြား သိခြင်း၊ ဣဒ္ဓိ၊ နား ဓာတ် စင်ကြယ်ခြင်း၊")
LINES_X[key('Cutiyā upapattiyā, paṇidhi me na vijjatī"ti [theragā. 996 theragāthāyaṃ].')] = (
    "စုတေခြင်း၊ ပြန်လည် ဖြစ်ပေါ်ခြင်းတို့အတွက် ငါ၌ ဆုတောင်းမှု မရှိ”ဟူ၍ ⟦0⟧။")
REF_X["theragā."] = "“ထေရဂါထာ”"
REF_NOTE_X["theragāthāyaṃ"] = "“ထေရဂါထာ”၌"

# ===================================================================================== 30. Saṃvarakathā
section("(30) 10. Saṃvarakathā", f"(30) 10. စောင့်စည်းမှုအကြောင်း {KATHA}")
section("Saṃvarakathā", f"စောင့်စည်းမှုအကြောင်း {KATHA}")
SV, ASV = new("saṃvaro / asaṃvaro", ("စောင့်စည်းမှု", "မစောင့်စည်းမှု"))
_D5 = F.strip_id(F.FINAL.seg("2", "^2-703")[2][0])
PANA_V = W("2", "^2-703", "pāṇātipātā veramaṇī", "သူ့အသက်ကို သတ်ခြင်းမှ ကင်းဝေးခြင်း")
SURA = W("2", "^2-703", "surāmerayamajjapamādaṭṭhānā veramaṇī", "သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့ခြင်း၏ အကြောင်း")
SURA_V = W("2", "^2-703", "surāmerayamajjapamādaṭṭhānā veramaṇī", f"{SURA}မှ ကင်းဝေးခြင်း")
for _k, _m in (("saṃvaro", SV), ("asaṃvaro", ASV), ("pāṇātipātā veramaṇī", PANA_V), ("pāṇātipātā veramaṇi", PANA_V),
               ("pāṇātipāto", F.PANATIPATA), ("surāmerayamajjapamādaṭṭhānā veramaṇī", SURA_V),
               ("surāmerayamajjapamādaṭṭhānā veramaṇi", SURA_V), ("surāmerayamajjapamādaṭṭhānaṃ", SURA),
               ("saññā", F.SANNA.my)):
    P6.LST.setdefault(_k, _m)
SILA_SV = f"{ASV}မှ {SV}သည် သီလ"
P("asaṃvarā saṃvaro sīlaṃ", V(SILA_SV))
new("asaṃvarā saṃvaro sīlaṃ", f"{SILA_SV} ဖြစ်")
P("atthi devesu asaṃvaro, yamhā asaṃvarā saṃvaro sīlaṃ",
  V(f"{DEVA_PL}၌ အကြင် {ASV}မှ {SV}သည် သီလ ဖြစ်၏၊ ထို{ASV}", EXIST))


@F.frame(r"Yaṃ tattha vadesi – vattabbe kho (?P<p>[^–]+?), no ca vattabbe – (?P<q>.+?)ti micchā\.")
def _f_yam_nodash(m):
    """Yaṃ tattha vadesi – "vattabbe kho ‘P,’ no ca vattabbe – ‘Q’"ti micchā. (no dash after «kho», ^5-379)"""
    return (f"ထိုအရာ၌ သင်ပြောသော စကား – “{F.SAY} ‘{F.pq(m['p'], 'stmt', 2)}’{C} {F.NOT_SAY} – "
            f"‘{F.pq(m['q'], 'stmt', 2)}’”{F.WRONG}{END}")


before_generic()
P("sabbe devā pāṇātipātino adinnādāyino kāmesumicchācārino musāvādino surāmerayamajjapamādaṭṭhāyino",
  V(f"{F.DEVA} အားလုံးတို့သည် " + W("4", "^4-132", "pāṇātipātī hoti",
                                    "သူ့အသက်ကို သတ်သူ ဖြစ်၏၊ မပေးသည်ကို ယူသူ ဖြစ်၏၊ ကာမတို့၌ မှားယွင်းစွာ ကျင့်သူ ဖြစ်၏၊ "
                                    "မုသား ပြောသူ ဖြစ်၏၊ သေရည် အရက် မူးယစ်ဖွယ်ဟူသော မေ့လျော့မှု၏ အကြောင်းကို မှီဝဲသူ")
    .replace(" ဖြစ်၏၊", "၊")))

# ===================================================================================== 31. Asaññakathā
section("(31) 11. Asaññakathā", f"(31) 11. အသညသတ်အကြောင်း {KATHA}")
section("Asaññakathā", f"အသညသတ်အကြောင်း {KATHA}")
ASAT = W("2", "^2-1015", "asaññasattānaṃ devānaṃ", "အသညသတ်")
SANNA = F.SANNA.my
_SR, _ASR = f"{SANNA} ရှိသော", f"{SANNA} မရှိသော"
TOK = {  # the words of the existence lists
    "gati": "လားရာ", "sattāvāso": "သတ္တဝါတို့ နေရာ ဘုံ", "saṃsāro": "သံသရာ", "yoni": "မွေးဖွားရာ အမျိုးအစား",
    "attabhāvapaṭilābho": "ကိုယ်ခန္ဓာ ရရှိခြင်း",
    "pañcavokārabhavo": W("2", "^2-234", "pañcavokārabhavo", "အစုအဝေး ငါးပါး ရှိသော ဘဝ"),
    "ekavokārabhavo": W("2", "^2-234", "ekavokārabhavo", "အစုအဝေး တစ်ပါး ရှိသော ဘဝ"),
    "catuvokārabhavo": W("2", "^2-234", "catuvokārabhavo", "အစုအဝေး လေးပါး ရှိသော ဘဝ"),
}
W("2", "^2-U58", "duggatiṃ", "လားရာ")
for _w in ("bhavo", "gati", "sattāvāso", "saṃsāro", "yoni"):
    _base = TOK.get(_w, "ဘဝ")
    TOK[f"saññā{_w}"] = f"{_SR} {_base}"
    TOK[f"asañña{_w}"] = f"{_ASR} {_base}"
TOK["saññabhavo"], TOK["asaññabhavo"] = f"{_SR} ဘဝ", f"{_ASR} ဘဝ"
TOK["saññattabhāvapaṭilābho"] = f"{_SR} {TOK['attabhāvapaṭilābho']}"
TOK["asaññattabhāvapaṭilābho"] = f"{_ASR} {TOK['attabhāvapaṭilābho']}"
for _k in ("gati", "sattāvāso", "saṃsāro", "yoni", "attabhāvapaṭilābho", "saññābhavo", "asaññabhavo"):
    new(_k, TOK[_k])
_TSEP = re.compile(r"(… | )")


@F.rule(r"(?P<so>so ca )?(?P<l>[^,;–]+)")
def _r_exist_list(m):
    """An existence list «saññābhavo saññāgati…pe… saññattabhāvapaṭilābho» (so ca …): «ထိုဘဝသည်လည်း A၊ B… C»."""
    parts = _TSEP.split(m["l"])
    toks, seps = parts[0::2], parts[1::2]
    if len(toks) < 2 or any(t not in TOK for t in toks):
        return None
    out = TOK[toks[0]]
    for sp, t in zip(seps, toks[1:]):
        out += ("… " if "…" in sp else f"{C} ") + TOK[t]
    pre = "ထိုဘဝသည်လည်း " if m["so"] == "so ca " else ""
    return V(pre + out)


new("so ca X (the existence)", "ထိုဘဝသည်လည်း X ဖြစ်")
for _g, _gm in (("asaññasattesu", f"{ASAT}တို့၌"), ("manussesu", f"{F.MANUSSA}တို့၌")):
    P(f"{_g} saññā atthi", V(f"{_gm} {SANNA}", EXIST))
    P(f"{_g} saññā atthi, tāya saññāya saññākaraṇīyaṃ karoti",
      VV(f"{_gm} {SANNA} ရှိ၍ ထို{SANNA}ဖြင့် {SANNA}၏ ပြုဖွယ် ကိစ္စကို", "ပြု"))
    P(f"{_g} saññā atthi, na ca tāya saññāya saññākaraṇīyaṃ karoti",
      VV(f"{_gm} {SANNA} ရှိ၍ ထို{SANNA}ဖြင့် {SANNA}၏ ပြုဖွယ် ကိစ္စကို", "ပြု", neg=True))
P("tāya saññāya saññākaraṇīyaṃ karoti", VV(f"ထို{SANNA}ဖြင့် {SANNA}၏ ပြုဖွယ် ကိစ္စကို", "ပြု"))
new("tāya saññāya saññākaraṇīyaṃ karoti", f"ထို{SANNA}ဖြင့် {SANNA}၏ ပြုဖွယ် ကိစ္စကို ပြု")
Q("santi, bhikkhave, asaññasattā nāma devā; saññuppādā ca pana te devā tamhā kāyā cavanti",
  f"ရဟန်းတို့၊ {ASAT} မည်သော {F.DEVA}တို့ ရှိကုန်၏၊ ထို{F.DEVA}တို့သည် {SANNA} ဖြစ်ပေါ်ခြင်းကြောင့် ထိုဘုံမှ စုတေကုန်၏")
SOME = "အချို့ အချိန်၌"                                               # kiñci kāle
new("kiñci kāle", SOME)
S("Kiñci kāle atthi, kiñci kāle natthīti.", f"{SOME} ရှိ၍ {SOME} {NEXIST}{END}")
VAR_X["kañci"] = F.LEKHANA
P("asaññasattesu saññā kiñci kāle atthi, kiñci kāle natthi",
  Cl(f"{ASAT}တို့၌ {SANNA}သည် {SOME} ရှိ၍ {SOME}", EXIST, NEXIST, neg=True))
P("kiñci kāle saññasattā kiñci kāle asaññasattā, kiñci kāle saññabhavo kiñci kāle asaññabhavo, kiñci kāle "
  "pañcavokārabhavo kiñci kāle ekavokārabhavo",
  V(f"{SOME} {_SR} သတ္တဝါ ဖြစ်၍ {SOME} {ASAT} ဖြစ်၊ {SOME} {TOK['saññabhavo']} ဖြစ်၍ {SOME} {TOK['asaññabhavo']} "
    f"ဖြစ်၊ {SOME} {TOK['pañcavokārabhavo']} ဖြစ်၍ {SOME} {TOK['ekavokārabhavo']}"))
S("Kaṃ kālaṃ atthi, kaṃ kālaṃ natthīti?", f"အဘယ် အချိန်၌ ရှိ၍ အဘယ် အချိန်၌ {NEXIST}သနည်း{END}")
CUTI, UPAP, THITI = "စုတေသည့် အချိန်၌", "ပြန်လည် ဖြစ်ပေါ်သည့် အချိန်၌", "တည်နေသည့် အချိန်၌"
new("cutikāle / upapattikāle / ṭhitikāle", f"{CUTI} / {UPAP} / {THITI}")
S("Cutikāle upapattikāle atthi, ṭhitikāle natthīti.", f"{CUTI}၊ {UPAP} ရှိ၍ {THITI} {NEXIST}{END}")
P("cutikāle upapattikāle saññasattā, ṭhitikāle asaññasattā; cutikāle upapattikāle saññabhavo, ṭhitikāle "
  "asaññabhavo; cutikāle upapattikāle pañcavokārabhavo, ṭhitikāle ekavokārabhavo",
  V(f"{CUTI}၊ {UPAP} {_SR} သတ္တဝါ ဖြစ်၍ {THITI} {ASAT} ဖြစ်၊ {CUTI}၊ {UPAP} {TOK['saññabhavo']} ဖြစ်၍ {THITI} "
    f"{TOK['asaññabhavo']} ဖြစ်၊ {CUTI}၊ {UPAP} {TOK['pañcavokārabhavo']} ဖြစ်၍ {THITI} {TOK['ekavokārabhavo']}"))

# ===================================================================================== 32. Nevasaññānāsaññāyatanakathā
NSN = W("1", "^1-1421", "nevasaññānāsaññāyatanaṃ",
        "မှတ်သိမှု ရှိသည်လည်း မဟုတ်၊ မှတ်သိမှု မရှိသည်လည်း မဟုတ်သော နယ်ပယ်")
section("(32) 12. Nevasaññānāsaññāyatanakathā", f"(32) 12. {NSN}အကြောင်း {KATHA}")
section("Nevasaññānāsaññāyatanakathā", f"{NSN}အကြောင်း {KATHA}")
ARUPA = {"nevasaññānāsaññāyatan": NSN,
         "ākāsānañcāyatan": W("1", "^1-266", "ākāsānañcāyatanaṃ", "အဆုံး မရှိသော ဟင်းလင်းပြင် နယ်ပယ်"),
         "viññāṇañcāyatan": W("1", "^1-266", "viññāṇañcāyatanasaññāsahagataṃ", "အဆုံး မရှိသော သိစိတ် နယ်ပယ်"),
         "ākiñcaññāyatan": W("1", "^1-267", "ākiñcaññāyatanasaññāsahagataṃ", "ဘာမျှ မရှိသော နယ်ပယ်")}
CATUV = TOK["catuvokārabhavo"]
SAY_S = f"«{SANNA} ရှိသည်»"                                           # "saññā atthī"ti
SAY_SN = f"«{SANNA} ရှိသည်»ဟူ၍ဖြစ်စေ၊ «{NEXIST}»ဟူ၍ဖြစ်စေ"            # "saññā atthī"ti vā "natthī"ti vā
for _k, _m in ARUPA.items():
    P(f"{_k}aṃ", FR(_m))
    P(f"{_k}aṃ catuvokārabhavo", V(f"{_m}သည် {CATUV}"))
    for _tail, _q in (("saññā atthi", SAY_S), ("saññā atthīti vā natthīti vā", SAY_SN)):
        P(f"{_k}e na vattabbaṃ – {_tail}", NSAY(f"{_m}၌", _q))
        P(f"{_k}aṃ catuvokārabhavo {_k}e na vattabbaṃ – {_tail}", NSAY(f"{_m}သည် {CATUV} ဖြစ်၍ {_m}၌", _q))
P("asaññasattesu na vattabbaṃ – saññā atthi", NSAY(f"{ASAT}တို့၌", SAY_S))
new('X-e na vattabbaṃ – "saññā atthī"ti', f"X၌ ဤသို့ မဆိုသင့် – “{SANNA} ရှိသည်”")
P("nevasaññānāsaññāyatanaṃ", V(f"ထိုအရာသည် {NSN}"))
P("nevasaññānāsaññāyatananti katvā nevasaññānāsaññāyatane na vattabbaṃ – saññā atthīti vā natthīti vā",
  NSAY(f"{NSN}{F.KATVA} {NSN}၌", SAY_SN))
ADKM = W("1", "^1-M1-2", "adukkhamasukhāya vedanāya", "မနာကျင် မသာယာ")
P("adukkhamasukhā vedanāti katvā adukkhamasukhāya vedanāya na vattabbaṃ – vedanāti vā avedanāti vā",
  NSAY(f"{ADKM}သော {F.VEDANA.my}{F.KATVA} {ADKM}သော {F.VEDANA.my}ကို",
       f"«{F.VEDANA.my}»ဟူ၍ဖြစ်စေ၊ «{F.VEDANA.my} မဟုတ်»ဟူ၍ဖြစ်စေ"))
VAR_X["nevasaññānāsaññāyatane vattabbaṃ"] = F.PATHA
VAR_X["adukkhamasukhā vedanā"] = F.PATHA
LINES_X["Tassuddānaṃ –"] = F.LINES.get("Tassuddānaṃ –", "ထို၏ အကျဉ်းချုပ် –")
LINES_X[key("Balaṃ sādhāraṇaṃ ariyaṃ, sarāgaṃ cittaṃ vimuccati;")] = (
    f"စွမ်းအား၊ ဆက်ဆံခြင်း၊ {ARIYA_N}၊ {SA['sarāgaṃ']} {CITTA} လွတ်မြောက်ခြင်း၊")
LINES_X[key("Vimuttaṃ vimuccamānaṃ, atthi cittaṃ vimuccamānaṃ.")] = (
    f"{VIMUTTA} လွတ်မြောက်ဆဲ ဖြစ်ခြင်း၊ လွတ်မြောက်ဆဲ စိတ် ရှိခြင်း{END}")
LINES_X[key("Aṭṭhamakassa puggalassa, diṭṭhipariyuṭṭhānaṃ pahīnaṃ;")] = (
    f"{AP}သည် {KX['diṭṭhipariyuṭṭhānaṃ']}ကို ပယ်ပြီးခြင်း၊")
LINES_X[key("Aṭṭhamakassa puggalassa, natthi pañcindriyāni cakkhuṃ.")] = (
    f"{AP_LOC} {IND['pañcindriyāni']} {NEXIST}ခြင်း၊ မျက်စိ{END}")
LINES_X[key("Sotaṃ dhammupatthaddhaṃ, yathākammūpagataṃ ñāṇaṃ;")] = f"{DHUP} နား၊ {YKN}၊"
LINES_X[key("Devesu saṃvaro asañña-sattesu saññā evameva bhavagganti.")] = (
    f"{DEVA_PL}၌ {SV}၊ {ASAT}တို့၌ {SANNA}၊ ထို့အတူပင် ဘဝ၏ အထွတ်အထိပ်{END}")

# ===================================================================================== 12. Catutthavaggo: shared parts
section("Catutthavaggo", f"{F.ORD_MY[4]} {F.VAGGA_W}")
COLO_X["Catutthavaggo"] = HEAD_X["Catutthavaggo"]
ARAHA = F.ARAHA
ARAHATTA_N = "ရဟန္တာ အဖြစ်"                                          # arahatta (make_ch2-5 ARAHATTA_N, copied)
GIHI = W("2", "^2-888", "gihīhi saṃsaṭṭho", "လူဝတ်ကြောင်")             # gihī
PUTHU = P6.PUTHU
ANAS = W("1", "^1-M2-15", "anāsavā dhammā", "စိတ်အစွန်းအထင်း၏ အာရုံ မဖြစ်နိုင်သော")
SAS = MAT["sāsava"]
SAMANN = ("ပြည့်စုံ", "မပြည့်စုံ")                                    # samannāgato
PH = {"sotāpatti": P6.PAT["sotāpattiphala"], "sakadāgāmi": P6.PAT["sakadāgāmiphala"],
      "anāgāmi": P6.PAT["anāgāmiphala"]}
MG = {"sotāpatti": "သောတာပတ္တိမဂ်", "sakadāgāmi": "သကဒါဂါမိမဂ်", "anāgāmi": "အနာဂါမိမဂ်", "arahatta": "ရဟန္တာ မဂ်"}
W("2", "^2-807", "Sotāpattimagge", "သောတာပတ္တိမဂ်")
PATP = {k: f"{P6.PAT[v]}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော {F.PUGGALA}" for k, v in
        (("arahattasacchikiriyāya paṭipanno puggalo", "arahatta"),
         ("anāgāmiphalasacchikiriyāya paṭipanno puggalo", "anāgāmiphala"),
         ("sakadāgāmiphalasacchikiriyāya paṭipanno puggalo", "sakadāgāmiphala"))}
PERS = {"arahā": ARAHA, "anāgāmī": F.ANAGAMI, "sakadāgāmī": F.SAKADAGAMI, "sotāpanno": F.SOTAPANNA}
PERS.update(PATP)
INS = {"arahatā": ARAHA, "anāgāminā": F.ANAGAMI, "sakadāgāminā": F.SAKADAGAMI}
INS.update({k.replace("paṭipanno puggalo", "paṭipannena puggalena"): v for k, v in PATP.items()})
NUMI = {"catūhi": F.NUM_MY[4], "tīhi": F.NUM_MY[3], "dvīhi": F.NUM_MY[2], "chahi": F.NUM_MY[6]}
NUMA = {"cattāri": F.NUM_MY[4], "tīṇi": F.NUM_MY[3], "dve": F.NUM_MY[2], "cattāro": F.NUM_MY[4], "tayo": F.NUM_MY[3]}
SOT_TYPES = (f"{F.SOTAPANNA}၊ " + "၊ ".join(W("4", "^4-M-7", k, m) for k, m in (
    ("Sattakkhattuparamo", "အများဆုံး ခုနစ်ကြိမ်သာ ပြန်လည် ဖြစ်ပေါ်သူ"), ("Kolaṅkolo", "အမျိုးမှ အမျိုးသို့ ကူးသူ"),
    ("Ekabījī", "မျိုးစေ့ တစ်စေ့သာ ရှိသူ"))))
ANA_TYPES = (f"{F.ANAGAMI}၊ " + "၊ ".join(P6._PT4[k] for k in ("antarāparinibbāyī", "upahaccaparinibbāyī",
                                                           "asaṅkhāraparinibbāyī", "sasaṅkhāraparinibbāyī"))
             + f"၊ {P6._UDH}")
DK = {  # dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti (ch5 wording, copied)
    "dukkhaṃ parijānāti": Cl("ဒုက္ခကို", "ပိုင်းခြား သိ", "ပိုင်းခြား မသိ"),
    "samudayaṃ pajahati": VV("ဒုက္ခ ဖြစ်ပေါ်ခြင်းကို", "ပယ်"),
    "nirodhaṃ sacchikaroti": Cl("ဒုက္ခ ချုပ်ငြိမ်းခြင်းကို", "မျက်မှောက်ပြု", "မျက်မှောက် မပြု"),
    "maggaṃ bhāveti": VV("မဂ်ကို", "ပွားများ"),
}
for _k, _c in DK.items():
    P(_k, _c)
DK_ALL = "dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti"
DK_ALL_MY = "ဒုက္ခကို ပိုင်းခြား သိသည်၊ ဒုက္ခ ဖြစ်ပေါ်ခြင်းကို ပယ်သည်၊ ဒုက္ခ ချုပ်ငြိမ်းခြင်းကို မျက်မှောက်ပြုသည်၊ မဂ်ကို ပွားများ"
new(DK_ALL, DK_ALL_MY)
KIL12 = {  # kilesa lists (commas normalised away) -> Burmese
    "sakkāyadiṭṭhiṃ vicikicchaṃ sīlabbataparāmāsaṃ": f"{SAKKAYA}၊ {VICI}၊ {SILAB}",
    "sakkāyadiṭṭhiṃ vicikicchaṃ sīlabbataparāmāsaṃ apāyagamanīyaṃ rāgaṃ apāyagamanīyaṃ dosaṃ apāyagamanīyaṃ mohaṃ":
        f"{SAKKAYA}၊ {VICI}၊ {SILAB}၊ အပါယ်သို့ ရောက်စေတတ်သော ရာဂ၊ အပါယ်သို့ ရောက်စေတတ်သော ဒေါသ၊ "
        "အပါယ်သို့ ရောက်စေတတ်သော မောဟ",
    "sakkāyadiṭṭhiṃ… apāyagamanīyaṃ mohaṃ": f"{SAKKAYA}… အပါယ်သို့ ရောက်စေတတ်သော မောဟ",
    "oḷārikaṃ kāmarāgaṃ oḷārikaṃ byāpādaṃ": "ရုန့်ရင်းသော ကာမရာဂ၊ ရုန့်ရင်းသော ဖျက်ဆီးလိုစိတ်",
    "aṇusahagataṃ kāmarāgaṃ aṇusahagataṃ byāpādaṃ": "သိမ်မွေ့သော ကာမရာဂ၊ သိမ်မွေ့သော ဖျက်ဆီးလိုစိတ်",
}
new("apāyagamanīya (make_ch2-5, copied)", "အပါယ်သို့ ရောက်စေတတ်သော")
VIT = ("ကျော်လွန်ပြီး", "မကျော်လွန်ရသေး")                               # vītivatto

# ===================================================================================== 33. Gihissa arahātikathā
section("(33) 1. Gihissa arahātikathā", f"(33) 1. {GIHI} {ARAHA} ဖြစ်နိုင်သည်ဟူသော {KATHA}")
section("Gihissa arahātikathā", f"{GIHI} {ARAHA} ဖြစ်နိုင်သည်ဟူသော {KATHA}")
P("gihissa arahā", Cl(f"{GIHI}သည် {ARAHA}", "ဖြစ်နိုင်", "မဖြစ်နိုင်"))
new("gihissa arahā", f"{GIHI}သည် {ARAHA} ဖြစ်နိုင်")
GSY = new("gihisaṃyojanaṃ", f"{GIHI}၏ နှောင်ကြိုး")
P6.LST.setdefault("gihisaṃyojanaṃ", GSY)
P("arahato gihisaṃyojanaṃ pahīnaṃ ucchinnamūlaṃ tālāvatthukataṃ anabhāvaṅkataṃ āyatiṃ anuppādadhammaṃ",
  V(f"{ARAHA}သည် {GSY}ကို ပယ်ပြီး၊ {P6.UCCH_MY}"))
_DE = W("4", "^4-131", "diṭṭhe ceva dhamme", "မျက်မှောက်ဘဝ၌ပင်")
_BHEDA = W("4", "^4-184", "kāyassa bhedā", "ခန္ဓာကိုယ် ပြိုကွဲ၍")
for _n, _neg in (("", False), ("n", True)):
    P(f"{_n}atthi koci gihī gihisaṃyojanaṃ appahāya diṭṭheva dhamme dukkhassantakaro",
      V(f"{GSY}ကို မပယ်ဘဲ {_DE} {F.DUKKHA_END}သော {GIHI} တစ်စုံတစ်ယောက်", EXIST, neg=_neg))
S('Nanu vacchagotto paribbājako bhagavantaṃ etadavoca – "atthi nu kho, bho gotama, koci gihī gihisaṃyojanaṃ '
  'appahāya kāyassa bhedā dukkhassantakaro"ti?',
  f"ဝစ္ဆဂေါတ္တ ပရိဗိုဇ်သည် {BUDDHA}ကို ဤသို့ လျှောက်ခဲ့သည် မဟုတ်လော – “အသျှင် ဂေါတမ၊ {GSY}ကို မပယ်ဘဲ "
  f"{_BHEDA} {F.DUKKHA_END}သော {GIHI} တစ်စုံတစ်ယောက် ရှိပါသလော”{END}")
S('"Natthi kho, vaccha, koci gihī gihisaṃyojanaṃ appahāya kāyassa bhedā dukkhassantakaro"ti.',
  f"“ဝစ္ဆ၊ {GSY}ကို မပယ်ဘဲ {_BHEDA} {F.DUKKHA_END}သော {GIHI} တစ်စုံတစ်ယောက်မျှ {NEXIST}”ဟူ၍{END}")
P6.ACTS.update({
    "ajeḷakaṃ paṭiggaṇheyya": ("ဆိတ်နှင့် သိုးကို", "ခံယူရာ"), "kukkuṭasūkaraṃ paṭiggaṇheyya": ("ကြက်နှင့် ဝက်ကို", "ခံယူရာ"),
    "hatthigavassavaḷavaṃ paṭiggaṇheyya": ("ဆင်၊ နွား၊ မြင်း၊ မြင်းမတို့ကို", "ခံယူရာ"),
    "tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya": ("ခါ၊ ငုံး၊ ဒေါင်း၊ ငှက်ကြီးတို့ကို", "ခံယူရာ"),
    "cittavaṇḍavālamoḷiṃ dhāreyya": ("အရောင်စုံ ဆံထုံးကို", "ဆောင်ရာ"),
    "odātāni vatthāni dīghadasāni dhāreyya": ("အနားစ ရှည်သော အဖြူ အဝတ်တို့ကို", "ဝတ်ဆင်ရာ"),
    "yāvajīvaṃ agāriyabhūto assa": ("အသက်ထက်ဆုံး လူ့ဘောင်၌ နေသူ", "ဖြစ်ရာ"),
})
for _k in ("ajeḷakaṃ paṭiggaṇheyya", "kukkuṭasūkaraṃ paṭiggaṇheyya", "hatthigavassavaḷavaṃ paṭiggaṇheyya",
           "tittiravaṭṭakamorakapiñjaraṃ paṭiggaṇheyya", "cittavaṇḍavālamoḷiṃ dhāreyya",
           "odātāni vatthāni dīghadasāni dhāreyya", "yāvajīvaṃ agāriyabhūto assa"):
    new(_k, " ".join(P6.ACTS[_k]))
ANCHOR_X["tittiravaṭṭakamorakapiñjaraṃ"] = "ငှက်ကြီးတို့ကို"
ANCHOR_X["cittavaṇḍavālamoḷiṃ"] = "အရောင်စုံ ဆံထုံးကို"
VAR_X["… kapiñjalaṃ"] = F.PATHA
VAR_X["pītavaṇṭavālamoḷikaṃ"] = F.PATHA
_YASO = "ယသ အမျိုးကောင်းသား၊ ဥတ္တိယ သူကြွယ်၊ သေတု လုလင်တို့သည် လူဝတ်ကြောင် အသွင်ဖြင့် ရဟန္တာ အဖြစ်သို့"
P("yaso kulaputto, uttiyo gahapati, setu māṇavo, gihibyañjanena arahattaṃ patto", VV(_YASO, "ရောက်ပြီး"))

# ===================================================================================== 34. Upapattikathā
section("(34) 2. Upapattikathā", f"(34) 2. ပြန်လည် ဖြစ်ပေါ်ခြင်းအကြောင်း {KATHA}")
section("Upapattikathā", f"ပြန်လည် ဖြစ်ပေါ်ခြင်းအကြောင်း {KATHA}")
SAHA_U = new("saha upapattiyā", "ပြန်လည် ဖြစ်ပေါ်သည်နှင့် တစ်ပြိုင်နက်")
P("saha upapattiyā arahā", V(f"{SAHA_U} {ARAHA}"))
for _k, _m in (("sotāpanno", F.SOTAPANNA), ("sakadāgāmī", F.SAKADAGAMI), ("anāgāmī", F.ANAGAMI)):
    P(f"saha upapattiyā {_k} hoti", VV(f"{SAHA_U} {_m}", "ဖြစ်"))
    P(f"saha upapattiyā {_k} na hoti", VV(f"{SAHA_U} {_m}", "ဖြစ်", neg=True))
THERA = {"sāriputto": SARIPUTTA, "mahāmoggallāno": "မဟာမောဂ္ဂလ္လာန်", "mahākassapo": "မဟာကဿပ",
         "mahākaccāno": "မဟာကစ္စာယန", "mahākoṭṭhiko": "မဟာကောဋ္ဌိက", "mahāpanthako": "မဟာပန္ထက"}
for _k, _m in THERA.items():
    P(f"{_k} thero", FR(f"{_m} မထေရ်"))
    P(f"{_k} thero saha upapattiyā arahā", V(f"{_m} မထေရ်သည် {SAHA_U} {ARAHA}"))
    P(f"{_k} thero na saha upapattiyā arahā", V(f"{_m} မထေရ်သည် {SAHA_U} {ARAHA}", neg=True))
UPC = new("upapattesiyaṃ cittaṃ", "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော စိတ်")
P("upapattesiyena cittena arahattaṃ sacchikaroti lokiyena sāsavena…pe… saṃkilesiyena",
  Cl(f"{MAT['lokiya']}၊ {SAS}… {MAT['saṃkilesiya']} {UPC}ဖြင့် {ARAHATTA_N}ကို", "မျက်မှောက်ပြု", "မျက်မှောက် မပြု"))
_GAMI = ("ကုန်ခန်းခြင်းဆီသို့", "ဗောဓိဆီသို့", "လျော့ပါးခြင်းဆီသို့")
P("upapattesiyaṃ cittaṃ niyyānikaṃ khayagāmī bodhagāmī apacayagāmī anāsavaṃ…pe… asaṃkilesiyaṃ",
  V(f"{UPC}သည် {NIYY}၊ " + "၊ ".join(f"{g} ဦးတည်သော" for g in _GAMI)
    + f"၊ {ANAS}… {MAT['saṃkilesiya'].replace(' ဖြစ်နိုင်', ' မဖြစ်နိုင်')} အရာ"))
_NOTG = f"{UPC}သည် လွတ်မြောက်ရာသို့ မပို့ဆောင်သော၊ " + "၊ ".join(f"{g} ဦးမတည်သော" for g in _GAMI)
P("upapattesiyaṃ cittaṃ aniyyānikaṃ na khayagāmi na bodhagāmi na apacayagāmi sāsavaṃ…pe… saṃkilesiyaṃ",
  V(f"{_NOTG}၊ {SAS}… {MAT['saṃkilesiya']} အရာ"))
P("upapattesiyena cittena rāgaṃ pajahati, dosaṃ pajahati, mohaṃ pajahati, anottappaṃ pajahati",
  VV(f"{UPC}ဖြင့် ရာဂကို ပယ်သည်၊ ဒေါသကို ပယ်သည်၊ မောဟကို ပယ်သည်၊ {P6.KIL['anottappaṃ']}ကို", "ပယ်"))
P("upapattesiyaṃ cittaṃ maggo… satipaṭṭhānaṃ…pe… sammappadhānaṃ… iddhipādo… indriyaṃ… balaṃ… bojjhaṅgo",
  V(f"{UPC}သည် မဂ်… {SATIP}… {P6._SP}… {P6._ID}… {F.INDRIYA_W}… စွမ်းအား… {P6._BJW}"))
P("upapattesiyena cittena dukkhaṃ parijānāti", Cl(f"{UPC}ဖြင့် ဒုက္ခကို", "ပိုင်းခြား သိ", "ပိုင်းခြား မသိ"))
P("cuticittaṃ maggacittaṃ upapattesiyaṃ cittaṃ phalacittaṃ",
  V(f"စုတိ စိတ်သည် မဂ် စိတ် ဖြစ်၍ {UPC}သည် ဖိုလ် စိတ်"))

# ===================================================================================== 35. Anāsavakathā
section("(35) 3. Anāsavakathā", f"(35) 3. {ANAS} အရာအကြောင်း {KATHA}")
section("Anāsavakathā", f"{ANAS} အရာအကြောင်း {KATHA}")
P("arahato sabbe dhammā anāsavā", V(f"{ARAHA}၏ {P6.ALL_DH}တို့သည် {ANAS} အရာ"))
ORG = {"cakkhuṃ": "မျက်စိ", "sotaṃ": "နား", "ghānaṃ": "နှာခေါင်း", "jivhā": "လျှာ", "kāyo": F.KAYA}
for _k, _m in ORG.items():
    P(f"arahato {_k}", FR(f"{ARAHA}၏ {_m}"))
    P(f"arahato {_k} {'anāsavo' if _k == 'kāyo' else 'anāsavaṃ'}", V(f"{ARAHA}၏ {_m}သည် {ANAS} အရာ"))
_KAYA_A = (f"ချီးမြှောက်ခြင်း နှိပ်ကွပ်ခြင်းကို ခံရနိုင်သော၊ ဖြတ်ခြင်း ခွဲခြင်းကို ခံရနိုင်သော၊ ကျီး၊ လင်းတ၊ "
           "စွန်တို့နှင့် ဆက်ဆံသော အရာ")
ANAS_DH = f"{ANAS} သဘောတရား"
for _s, _sm in (("arahato kāyo", f"{ARAHA}၏ {F.KAYA}"), ("anāsavo dhammo", ANAS_DH)):
    P(f"{_s} paggahaniggahupago chedanabhedanupago kākehi gijjhehi kulalehi sādhāraṇo", V(f"{_sm}သည် {_KAYA_A}"))
for _s, _sm in (("arahato kāye", f"{ARAHA}၏ {F.KAYA}၌"), ("anāsave dhamme", f"{ANAS_DH}၌")):
    P(f"{_s} visaṃ kameyya, satthaṃ kameyya, aggi kameyya",
      VV(f"{_sm} အဆိပ် တိုးဝင်ရာ၏၊ လက်နက် တိုးဝင်ရာ၏၊ မီး", "တိုးဝင်ရာ"))
BAND = "အနှောင်အဖွဲ့"                                                  # bandhana (kept apart from saṃyojana)
new("bandhana", BAND)
_B1 = [("addu", "ခြေချင်း"), ("rajju", "ကြိုး"), ("saṅkhalika", "သံကြိုး")]
_B2 = [("gāma", "ရွာ"), ("nigama", "နိဂုံး"), ("nagara", "မြို့"), ("janapada", "ဇနပုဒ်")]
_KP = f"လည်ပင်း ပါဝင်သော ပဉ္စမ ပြည့် {BAND}တို့ဖြင့် ချည်နှောင်ရန်"


def _band(items):
    return "၊ ".join(f"{m} {BAND}ဖြင့် ချည်နှောင်ရန်" for _, m in items)


P("labbhā arahato kāyo addubandhanena bandhituṃ, rajjubandhanena bandhituṃ, saṅkhalikabandhanena bandhituṃ, "
  "gāmabandhanena bandhituṃ, nigamabandhanena bandhituṃ, nagarabandhanena bandhituṃ, janapadabandhanena bandhituṃ, "
  "kaṇṭhapañcamehi bandhanehi bandhituṃ",
  Cl(f"{ARAHA}၏ {F.KAYA}ကို {_band(_B1 + _B2)}၊ {_KP}", "ဖြစ်နိုင်", "မဖြစ်နိုင်"))
P("labbhā anāsavo dhammo addubandhanena bandhituṃ, rajjubandhanena bandhituṃ, saṅkhalikabandhanena bandhituṃ, "
  "gāmanigamanagarajanapadabandhanena bandhituṃ, kaṇṭhapañcamehi bandhanehi bandhituṃ",
  Cl(f"{ANAS_DH}ကို {_band(_B1)}၊ ရွာ၊ နိဂုံး၊ မြို့၊ ဇနပုဒ် {BAND}ဖြင့် ချည်နှောင်ရန်၊ {_KP}", "ဖြစ်နိုင်",
     "မဖြစ်နိုင်"))
REQ = {"cīvaraṃ": "သင်္ကန်း", "piṇḍapātaṃ": "ဆွမ်း", "senāsanaṃ": "ကျောင်းအိပ်ရာနေရာ",
       "gilānapaccayabhesajjaparikkhāraṃ": "သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်"}
W("2", "^2-929", "cīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhārehi", "ကျောင်းအိပ်ရာနေရာ")
_GIVE = {"arahā puthujjanassa": (f"{ARAHA}သည် {PUTHU}အား", (ANAS, SAS)),
         "puthujjano arahato": (f"{PUTHU}သည် {ARAHA}အား", (SAS, ANAS))}
for _g, (_gm, (_a, _b)) in _GIVE.items():
    _ab = "anāsav" if _a == ANAS else "sāsav"
    _bb = "sāsav" if _a == ANAS else "anāsav"
    for _e in ("aṃ", "o"):
        _turn = Cl(f"{_a} အရာ ဖြစ်ပြီးမှ {_b} အရာ", *BEC)
        P(f"{_ab}{_e} hutvā {_bb}{_e} hoti", _turn)
    P(f"yadi {_g} cīvaraṃ deti, {_ab}aṃ hutvā {_bb}aṃ hoti",
      Cl(f"အကယ်၍ {_gm} {REQ['cīvaraṃ']}ကို ပေးလျှင် ထိုအရာသည် {_a} အရာ ဖြစ်ပြီးမှ {_b} အရာ", *BEC))
    P(f"yadi {_g} piṇḍapātaṃ deti, senāsanaṃ deti, gilānapaccayabhesajjaparikkhāraṃ deti, {_ab}o hutvā {_bb}o hoti",
      Cl(f"အကယ်၍ {_gm} {REQ['piṇḍapātaṃ']}ကို ပေး၏၊ {REQ['senāsanaṃ']}ကို ပေး၏၊ "
         f"{REQ['gilānapaccayabhesajjaparikkhāraṃ']}ကို ပေးလျှင် ထိုအရာသည် {_a} အရာ ဖြစ်ပြီးမှ {_b} အရာ", *BEC))
    P(f"taññeva {_ab}aṃ taṃ {_bb}aṃ", V(f"ထို{_a} အရာပင် ထို{_b} အရာ"))
P("maggo anāsavo hutvā sāsavo hoti", Cl(f"မဂ်သည် {ANAS} အရာ ဖြစ်ပြီးမှ {SAS} အရာ", *BEC))
P("phalaṃ… satipaṭṭhānaṃ… sammappadhānaṃ… iddhipādo… indriyaṃ… balaṃ… bojjhaṅgo anāsavo hutvā sāsavo hoti",
  Cl(f"ဖိုလ်… {SATIP}… {P6._SP}… {P6._ID}… {F.INDRIYA_W}… စွမ်းအား… {P6._BJW}သည် {ANAS} အရာ ဖြစ်ပြီးမှ "
     f"{SAS} အရာ", *BEC))
P("rāgo sāsavo hutvā anāsavo hoti", Cl(f"ရာဂသည် {SAS} အရာ ဖြစ်ပြီးမှ {ANAS} အရာ", *BEC))
P("doso…pe… moho…pe… anottappaṃ sāsavaṃ hutvā anāsavaṃ hoti",
  Cl(f"ဒေါသ… မောဟ… {P6.KIL['anottappaṃ']}သည် {SAS} အရာ ဖြစ်ပြီးမှ {ANAS} အရာ", *BEC))
P("nanu arahā anāsavo", V(f"{ARAHA}သည် စိတ်အစွန်းအထင်း ကင်းသူ"))
P("arahā anāsavo", V(f"{ARAHA}သည် စိတ်အစွန်းအထင်း ကင်းသူ"))
new("arahā anāsavo", f"{ARAHA}သည် စိတ်အစွန်းအထင်း ကင်းသူ ဖြစ်")

# ===================================================================================== 36 / 41. Samannāgata, Aparāpi samannāgata
section("(36) 4. Samannāgatakathā", f"(36) 4. ပြည့်စုံခြင်းအကြောင်း {KATHA}")
section("Samannāgatakathā", f"ပြည့်စုံခြင်းအကြောင်း {KATHA}")
section("(41) 9. Aparāpi samannāgatakathā", f"(41) 9. နောက်ထပ် ပြည့်စုံခြင်းအကြောင်း {KATHA}")
section("Aparāpi samannāgatakathā", f"နောက်ထပ် ပြည့်စုံခြင်းအကြောင်း {KATHA}")
MENT = {"phassehi": "တွေ့ထိမှု", "vedanāhi": F.VEDANA.my, "saññāhi": SANNA, "cetanāhi": "စေ့ဆော်မှု",
        "cittehi": CITTA, "saddhāhi": IND["saddhā"], "vīriyehi": "ဝီရိယ", "satīhi": "သတိ", "samādhīhi": "သမာဓိ",
        "paññāhi": "ပညာ", "phalehi": "ဖိုလ်", "maggehi": "မဂ်", "upekkhāhi": "ဥပေက္ခာ", "bodhīhi": "ဗောဓိ"}
_MSEP = re.compile(r"(, |… | )")


def ment_list(l):
    """«catūhi phassehi catūhi vedanāhi…pe… catūhi paññāhi» -> «တွေ့ထိမှု လေးပါး၊ ခံစားမှု လေးပါး… ပညာ လေးပါး»."""
    parts = _MSEP.split(l.strip())
    toks, seps = parts[0::2], parts[1::2]
    if len(toks) % 2:
        return None
    out = ""
    for i in range(0, len(toks), 2):
        n, w = toks[i], toks[i + 1]
        if n not in NUMI or w not in MENT or (i and seps[i - 1] == " " and False):
            return None
        if i:
            out += "… " if "…" in seps[i - 1] else f"{C} "
        out += f"{MENT[w]} {NUMI[n]}{F.CL}"
    return out + "တို့"


@F.rule(r"(?P<s>.+?) (?P<l>(?:catūhi|tīhi|dvīhi|chahi) .+?) samannāgato")
def _r_samann(m):
    """S catūhi phassehi … samannāgato: «Sသည် တွေ့ထိမှု လေးပါး၊ … တို့နှင့် ပြည့်စုံ»."""
    if m["s"] not in PERS:
        return None
    lm = ment_list(m["l"])
    if lm is None:
        return None
    return Cl(f"{PERS[m['s']]}သည် {lm}နှင့်", *SAMANN)


for _s, _sm in PERS.items():
    for _f, _fm in PH.items():
        P(f"{_s} {_f}phalena samannāgato", Cl(f"{_sm}သည် {_fm}နှင့်", *SAMANN))
        P(f"{_s} {_f}phalaṃ vītivatto", Cl(f"{_sm}သည် {_fm}ကို", *VIT))
        P(f"nanu {_s} {_f}phalaṃ vītivatto", Cl(f"{_sm}သည် {_fm}ကို", *VIT))
        for _c in ("", ","):
            P(f"{_s} {_f}phalaṃ vītivatto{_c} tena samannāgato",
              Cl(f"{_sm}သည် {_fm}ကို {VIT[0]}၍ ထိုဖိုလ်နှင့်", *SAMANN))
    P(f"sveva {_s}, so sotāpanno", V(f"ထို{_sm}ပင် {F.SOTAPANNA}"))
    P(f"sveva {_s}, so sakadāgāmī", V(f"ထို{_sm}ပင် {F.SAKADAGAMI}"))
    P(f"sveva {_s}, so anāgāmī", V(f"ထို{_sm}ပင် {F.ANAGAMI}"))
    P(f"{_s} sotāpanno sattakkhattuparamo, kolaṅkolo, ekabījī", V(f"{_sm}သည် {SOT_TYPES}"))
    P(f"{_s} sakadāgāmī", V(f"{_sm}သည် {F.SAKADAGAMI}"))
    for _c in (", ", " "):
        P(f"{_s} anāgāmī{_c}antarāparinibbāyī, upahaccaparinibbāyī, asaṅkhāraparinibbāyī, sasaṅkhāraparinibbāyī, "
          "uddhaṃsoto akaniṭṭhagāmī", V(f"{_sm}သည် {ANA_TYPES}"))


@F.rule(r"(?P<s>.+?) (?P<m>sotāpatti|sakadāgāmi|anāgāmi)maggaṃ vītivatto, (?P<k>.+?) vītivatto,? tena samannāgato")
def _r_vitivatta(m):
    """S Mmaggaṃ vītivatto, KILESAS vītivatto(,) tena samannāgato."""
    k = m["k"].replace(",", "")
    if m["s"] not in PERS or k not in KIL12:
        return None
    return Cl(f"{PERS[m['s']]}သည် {MG[m['m']]}ကို {VIT[0]}၍ {KIL12[k]}ကို {VIT[0]}၍ ထိုမဂ်နှင့်", *SAMANN)


for _s, _sm in INS.items():
    for _n, _nm in (("cattāri", "လေး"), ("tīṇi", "သုံး"), ("dve", "နှစ်")):
        for _o, _om in (("phalāni paṭiladdhāni", "ဖိုလ်"),):
            for _c in ("", ","):
                P(f"{_s} {_n} {_o}{_c} tehi ca aparihīno",
                  VV(f"{_sm}သည် {_om} {_nm}ပါးတို့ကို ရပြီး ဖြစ်၍ ထို{_om}တို့မှလည်း", "ဆုတ်ယုတ်", neg=True))
            P(f"{_s} {_n} {_o}", VV(f"{_sm}သည် {_om} {_nm}ပါးတို့ကို", "ရပြီး"))
    for _n, _nm in (("cattāro", "လေး"), ("tayo", "သုံး"), ("dve", "နှစ်")):
        for _c in ("", ","):
            P(f"{_s} {_n} maggā paṭiladdhā{_c} tehi ca aparihīno",
              VV(f"{_sm}သည် မဂ် {_nm}ပါးတို့ကို ရပြီး ဖြစ်၍ ထိုမဂ်တို့မှလည်း", "ဆုတ်ယုတ်", neg=True))
    for _c in ("", ","):
        P(f"{_s} sotāpattiphalaṃ paṭiladdhaṃ{_c} tena ca aparihīno",
          VV(f"{_sm}သည် {PH['sotāpatti']}ကို ရပြီး ဖြစ်၍ ထိုဖိုလ်မှလည်း", "ဆုတ်ယုတ်", neg=True))
    P(f"{_s} sotāpattiphalaṃ paṭiladdhaṃ", VV(f"{_sm}သည် {PH['sotāpatti']}ကို", "ရပြီး"))
P("tehi ca aparihīno", VV("ထိုဖိုလ်တို့မှလည်း", "ဆုတ်ယုတ်", neg=True))
P("tena ca aparihīno", VV("ထိုဖိုလ်မှလည်း", "ဆုတ်ယုတ်", neg=True))
for _s, _sm in PERS.items():
    for _n in NUMI:
        for _w in ("phalehi", "maggehi"):
            P(f"{_s} {_n} {_w} samannāgato", Cl(f"{_sm}သည် {MENT[_w]} {NUMI[_n]}{F.CL}တို့နှင့်", *SAMANN))
for _f, _p, _fm in (("sotāpatti", "sotāpanno", F.SOTAPANNA), ("sakadāgāmi", "sakadāgāmī", F.SAKADAGAMI),
                    ("anāgāmi", "anāgāmī", F.ANAGAMI)):
    P(f"{_f}phalena samannāgato {_p}ti vattabbo",
      Cl(f"{PH[_f]}နှင့် ပြည့်စုံသူကို «{_fm}»ဟု", "ဆိုသင့်", "မဆိုသင့်"))
new("X-phalena samannāgato «Y»ti vattabbo", "Xနှင့် ပြည့်စုံသူကို “Y”ဟု ဆိုသင့်")

# ===================================================================================== 37. Upekkhāsamannāgatakathā
section("(37) 5. Upekkhāsamannāgatakathā", f"(37) 5. ဥပေက္ခာနှင့် ပြည့်စုံခြင်းအကြောင်း {KATHA}")
section("Upekkhāsamannāgatakathā", f"ဥပေက္ခာနှင့် ပြည့်စုံခြင်းအကြောင်း {KATHA}")
W("1", "^1-M1-7", "upekkhāsahagatā dhammā", "ဥပေက္ခာ")
SENSE = [("cakkhunā rūpaṃ", "မျက်စိဖြင့် အဆင်းအရောင်ကို", "မြင်"), ("sotena saddaṃ", "နားဖြင့် အသံကို", "ကြား"),
         ("ghānena gandhaṃ", "နှာခေါင်းဖြင့် အနံ့ကို", "နမ်း"), ("jivhāya rasaṃ", "လျှာဖြင့် အရသာကို", "လျက်"),
         ("kāyena phoṭṭhabbaṃ", f"{F.KAYA}ဖြင့် အတွေ့အထိကို", "ထိ"), ("manasā dhammaṃ", "မနောဖြင့် သဘောတရားကို", "သိ")]
_S5 = "၊ ".join(f"{o} {v}၏" for _, o, v in SENSE[1:])
_S5b = "၊ ".join(f"{o} {v}၏" for _, o, v in SENSE[:5])
P("arahā cakkhunā rūpaṃ passanto sotena saddaṃ suṇāti, ghānena gandhaṃ ghāyati, jivhāya rasaṃ sāyati, kāyena "
  "phoṭṭhabbaṃ phusati, manasā dhammaṃ vijānāti…pe… manasā dhammaṃ vijānanto cakkhunā rūpaṃ passati, sotena saddaṃ "
  "suṇāti, ghānena gandhaṃ ghāyati, jivhāya rasaṃ sāyati, kāyena phoṭṭhabbaṃ phusati",
  VV(f"{ARAHA}သည် {SENSE[0][1]} မြင်နေစဉ် {_S5}… {SENSE[5][1]} သိနေစဉ် {_S5b[:-len('ထိ၏')]}".rstrip(), "ထိ"))
SATATA = new("satataṃ samitaṃ abbokiṇṇaṃ", "အမြဲတမ်း၊ အစဉ်တစိုက်၊ ကြားမလပ်ဘဲ")
for _k, _m, _n, _nm in (("chahi upekkhāhi", "ဥပေက္ခာ", "cha upekkhāyo", F.NUM_MY[6]),
                        ("tīhi bodhīhi", "ဗောဓိ", "tisso bodhiyo", F.NUM_MY[3])):
    P(f"satataṃ samitaṃ abbokiṇṇaṃ {_k} samannāgato samohito, {_n} paccupaṭṭhitā",
      Cl(f"{SATATA} {_m} {_nm}{F.CL}တို့နှင့် ပြည့်စုံ၍ ယှဉ်တွဲလျက် {_m} {_nm}{F.CL}တို့",
         "ထင်ရှား တည်နေကြ", "ထင်ရှား မတည်နေကြ"))
VAR_X["samāhito"] = F.PATHA
P("nanu arahā chaḷaṅgupekkho", V(f"{ARAHA}သည် အင်္ဂါ ခြောက်ပါးနှင့် ပြည့်စုံသော ဥပေက္ခာ ရှိသူ"))
P("arahā chaḷaṅgupekkho", V(f"{ARAHA}သည် အင်္ဂါ ခြောက်ပါးနှင့် ပြည့်စုံသော ဥပေက္ခာ ရှိသူ"))
new("chaḷaṅgupekkho", "အင်္ဂါ ခြောက်ပါးနှင့် ပြည့်စုံသော ဥပေက္ခာ ရှိသူ")


@F.frame(r"(?P<h>[Hh])añci (?P<p>.+?)[,;] (?P<neg>tena|no ca) vata re vattabbe – (?P<q>.+?)ti…\.?")
def _f_if_pe(m):
    """Hañci P, tena vata re vattabbe – "Q"ti…pe…. (^5-397)"""
    return F.if_my(m["p"], m["q"], neg=m["neg"] == "no ca") + PE


before_generic()

# ===================================================================================== 38. Bodhiyā buddhotikathā
section("(38) 6. Bodhiyā buddhotikathā", f"(38) 6. ဗောဓိဖြင့် ဘုရား ဖြစ်သည်ဟူသော {KATHA}")
section("Bodhiyā buddhotikathā", f"ဗောဓိဖြင့် ဘုရား ဖြစ်သည်ဟူသော {KATHA}")
BODHI = "ဗောဓိ"                                                        # bodhi (ch8 bodhagāmī «ဗောဓိဆီသို့»)
new("bodhi (awakening)", BODHI)
BUD = "ဘုရား"                                                         # buddho
BT = {"": "", "atītāya ": f"{P6.ATITA} ", "anāgatāya ": f"{P6.ANAGATA} ", "paccuppannāya ": f"{P6.PACCUP} "}
for _t, _tm in BT.items():
    P(f"{_t}bodhiyā buddho", V(f"{_tm}{BODHI}ဖြင့် {BUD}"))
P("bodhiyā niruddhāya vigatāya paṭipassaddhāya abuddho hoti",
  Cl(f"{BODHI} ချုပ်ငြိမ်း၍ ကင်းပျောက်၍ ငြိမ်းအေးသွားသောအခါ {BUD} မဟုတ်သူ", *BEC))
for _pre, _pm in (("tāya bodhiyā", f"ထို{BODHI}ဖြင့်"), ("na ca tāya bodhiyā", f"ထို{BODHI}ဖြင့်")):
    _neg = _pre.startswith("na ca")
    P(f"{_pre} bodhikaraṇīyaṃ karoti", VV(f"{_pm} {BODHI}၏ ပြုဖွယ် ကိစ္စကို", "ပြု", neg=_neg))
    P(f"{_pre} dukkhaṃ parijānāti", Cl(f"{_pm} ဒုက္ခကို", "ပိုင်းခြား သိ", "ပိုင်းခြား မသိ", neg=_neg))
P("tīhi bodhīhi buddho", V(f"{BODHI} {F.NUM_MY[3]}{F.CL}ဖြင့် {BUD}"))
P("bodhipaṭilābhā buddho", V(f"{BODHI}ကို ရခြင်းကြောင့် {BUD}"))
P("bodhipaṭilābhā bodhi", V(f"{BODHI}ကို ရခြင်းသည် {BODHI}"))
P("atītāya bodhiyā buddho, anāgatāya bodhiyā buddho, paccuppannāya bodhiyā buddho",
  V(f"{P6.ATITA} {BODHI}ဖြင့် {BUD} ဖြစ်၍ {P6.ANAGATA} {BODHI}ဖြင့် {BUD} ဖြစ်၍ {P6.PACCUP} {BODHI}ဖြင့် {BUD}"))

# ===================================================================================== 39. Lakkhaṇakathā
section("(39) 7. Lakkhaṇakathā", f"(39) 7. လက္ခဏာအကြောင်း {KATHA}")
section("Lakkhaṇakathā", f"လက္ခဏာအကြောင်း {KATHA}")
BS = new("bodhisatto", "ဘုရားလောင်း")
CVS = new("cakkavattisatto", "စကြဝတေး မင်းလောင်း")
LK = "လက္ခဏာ"
P("lakkhaṇasamannāgato bodhisatto", V(f"{LK}တို့နှင့် ပြည့်စုံသူသည် {BS}"))
for _k, _m in (("padesa", "အချို့"), ("tibhāga", "သုံးပုံတစ်ပုံ"), ("upaḍḍha", "တစ်ဝက်")):
    P(f"{_k}lakkhaṇehi samannāgato {_k}bodhisatto", V(f"{LK} {_m}တို့နှင့် ပြည့်စုံသူသည် {_m} {BS}"))
P("cakkavattisatto lakkhaṇasamannāgato, cakkavattisatto bodhisatto",
  V(f"{CVS}သည် {LK}တို့နှင့် ပြည့်စုံ၍ {CVS}သည် {BS}"))
P("yādiso bodhisattassa pubbayogo pubbacariyā dhammakkhānaṃ dhammadesanā, tādiso cakkavattisattassa pubbayogo "
  "pubbacariyā dhammakkhānaṃ dhammadesanā", V(f"{PY(BS)}{LIKE.format(PY(CVS))}"))
EVAM = W("4", "^4-94", "Evamevaṃ", "ထို့အတူပင်")
MARV = [  # «Yathā A, evamevaṃ B?»: A with bodhisatta, B the same with cakkavattisatta ({X} = the person)
    ("bodhisattassa jāyamānassa devā paṭhamaṃ paṭiggaṇhanti pacchā manussā",
     "{X} မွေးဖွားနေစဉ် နတ်တို့က ရှေးဦးစွာ ခံယူကြပြီး နောက်မှ လူတို့က ခံယူကြ"),
    ("bodhisattassa jāyamānassa cattāro naṃ devaputtā paṭiggahetvā mātu purato ṭhapenti – attamanā, devi, hohi! "
     "Mahesakkho te putto uppannoti",
     "{X} မွေးဖွားနေစဉ် နတ်သား လေးယောက်တို့သည် ထိုသူကို ခံယူ၍ မယ်တော်၏ ရှေ့၌ ထားကြ၏ – «မိဖုရား၊ "
     "ဝမ်းမြောက်ပါလော့၊ တန်ခိုးကြီးသော သားတော် ဖွားမြင်ပါပြီ»ဟု ပြောကြ"),
    ("bodhisattassa jāyamānassa dve udakassa dhārā antalikkhā pātubhavanti – ekā sītassa, ekā uṇhassa – yena "
     "bodhisattassa udakakiccaṃ karonti mātu ca",
     "{X} မွေးဖွားနေစဉ် ကောင်းကင်မှ ရေ အလျဉ် နှစ်သွယ် ထင်ရှားလာကြ၏ – တစ်သွယ်က အေးသော ရေ၊ တစ်သွယ်က ပူသော ရေ – "
     "ထိုရေဖြင့် {X}အားလည်း မယ်တော်အားလည်း ရေ၏ ကိစ္စကို ပြုကြ"),
    ("sampatijāto bodhisatto samehi pādehi patiṭṭhahitvā uttarena abhimukho sattapadavītihārena gacchati setamhi "
     "chatte anudhāriyamāne, sabbā ca disā viloketi, āsabhiñca vācaṃ bhāsati – aggohamasmi lokassa, jeṭṭhohamasmi "
     "lokassa, seṭṭhohamasmi lokassa, ayamantimā jāti, natthi dāni punabbhavoti",
     "မွေးဖွားပြီးခါစ {X}သည် ခြေ နှစ်ဖက်ဖြင့် ညီညာစွာ ရပ်၍ မြောက်အရပ်သို့ မျက်နှာမူလျက် ထီးဖြူကို မိုးထားစဉ် "
     "ခုနစ်လှမ်း လှမ်း၍ သွား၏၊ အရပ် အားလုံးကိုလည်း ကြည့်၏၊ အမြတ်ဆုံး စကားကိုလည်း ဆို၏ – «ငါသည် လောက၏ "
     "ထိပ်ဆုံး ဖြစ်၏၊ ငါသည် လောက၏ အကြီးဆုံး ဖြစ်၏၊ ငါသည် လောက၏ အမြတ်ဆုံး ဖြစ်၏၊ ဤသည်ကား နောက်ဆုံး ဘဝ "
     "ဖြစ်၏၊ ယခုအခါ ဘဝသစ် " + NEXIST + "တော့»ဟု ကြွေးကြော်"),
    ("bodhisattassa jāyamānassa mahato ālokassa mahato obhāsassa mahato bhūmicālassa pātubhāvo hoti",
     "{X} မွေးဖွားနေစဉ် ကြီးမားသော အလင်း၊ ကြီးမားသော အရောင်၊ ကြီးမားသော မြေငလျင်တို့ ထင်ရှား ပေါ်ပေါက်"),
    ("bodhisattassa pakatikāyo samantā byāmaṃ obhāsati", "{X}၏ ပကတိ ကိုယ်သည် ပတ်လည် တစ်လံ ထွန်းလင်း"),
    ("bodhisatto mahāsupinaṃ passati", "{X}သည် အိပ်မက်ကြီးကို မြင်"),
]
new("punabbhava (make_ch2-5, copied)", "ဘဝသစ်")
MARV_D = {}
for _a, _m in MARV:
    MARV_D[_a] = (_m, "bodhisatt")
    MARV_D[_a.replace("bodhisatt", "cakkavattisatt")] = (_m, "cakkavattisatt")


def _marv(x):
    for c, _ in F._cands(x):
        if c in MARV_D:
            m, who = MARV_D[c]
            return F.q_set(m.replace("{X}", BS if who == "bodhisatt" else CVS), 0)
    raise F.Miss("marvel: " + x)


@F.frame(r"Yathā (?P<a>.+?), evamevaṃ (?P<b>.+?)\?")
def _f_yatha(m):
    """Yathā A, evamevaṃ B? = «Aသကဲ့သို့ ထို့အတူပင် Bသလော»."""
    return f"{_marv(m['a'])}သကဲ့သို့ {EVAM} {_marv(m['b'])}သလော{END}"


before_generic()
REF_NOTE_X["vuttaṃ dissāya pucchati"] = "ဟောတော်မူချက်ကို ကြည့်၍ မေးသည်"
REF_NOTE_X["ghaṭikārasuttaṃ nissāya pucchati"] = "“ဃဋီကာရ သုတ်”ကို မှီ၍ မေးသည်"
CAKKA = P6._CK                                                       # rājā cakkavattī (ch8)
_RT = ["စက်", "ဆင်", "မြင်း", "ပတ္တမြား", "မိန်းမ", "သူကြွယ်"]
S('Nanu vuttaṃ bhagavatā – "dvattiṃsimāni, bhikkhave, mahāpurisassa mahāpurisalakkhaṇāni, yehi samannāgatassa '
  'mahāpurisassa dveva gatiyo bhavanti anaññā! Sace agāraṃ ajjhāvasati, rājā hoti cakkavattī dhammiko dhammarājā '
  'cāturanto vijitāvī janapadatthāvariyappatto sattaratanasamannāgato. Tassimāni satta ratanāni bhavanti, seyyathidaṃ '
  '– cakkaratanaṃ, hatthiratanaṃ, assaratanaṃ, maṇiratanaṃ, itthiratanaṃ, gahapatiratanaṃ, pariṇāyakaratanameva '
  'sattamaṃ. Parosahassaṃ kho panassa puttā bhavanti sūrā vīraṅgarūpā parasenappamaddanā. So imaṃ pathaviṃ '
  'sāgarapariyantaṃ adaṇḍena asatthena dhammena abhivijiya ajjhāvasati. Sace kho pana agārasmā anagāriyaṃ pabbajati, '
  'arahaṃ hoti sammāsambuddho loke vivaṭṭacchado"ti.',
  f"{BUDDHA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “ရဟန်းတို့၊ ယောကျ်ားမြတ်၏ ယောကျ်ားမြတ် {LK} သုံးဆယ့်နှစ်ပါးတို့သည် "
  f"ဤသည်တို့ပင် ဖြစ်ကုန်၏၊ အကြင် {LK}တို့နှင့် ပြည့်စုံသော ယောကျ်ားမြတ်အား လားရာ နှစ်ပါးသာ ဖြစ်ကုန်၏၊ အခြား "
  "မဟုတ် ⟦b⟧။ အကယ်၍ လူ့ဘောင်၌ နေလျှင် တရားနှင့် လျော်သော၊ တရားမင်း ဖြစ်သော၊ လေးဘက် သမုဒ္ဒရာ အဆုံးရှိ မြေကို "
  "အစိုးရသော၊ စစ်အောင်နိုင်သော၊ တိုင်းနိုင်ငံကို တည်တံ့ခိုင်မြဲစေသော၊ ရတနာ ခုနစ်ပါးနှင့် ပြည့်စုံသော "
  f"{CAKKA} ဖြစ်၏။ ထိုမင်း၌ ဤရတနာ ခုနစ်ပါးတို့ ဖြစ်ကုန်၏၊ ဆိုလိုသည်မှာ – "
  + "၊ ".join(f"{r} ရတနာ" for r in _RT) + "၊ ခုနစ်ခုမြောက် ခေါင်းဆောင် ရတနာ။ ထိုမင်း၏ သားတော်တို့သည် "
  "တစ်ထောင်ကျော် ရှိကုန်၏၊ ရဲရင့်ကုန်၏၊ သူရဲကောင်း ရုပ်သွင် ရှိကုန်၏၊ ရန်သူ့ စစ်တပ်ကို နှိမ်နင်းနိုင်ကုန်၏။ "
  "ထိုမင်းသည် သမုဒ္ဒရာ အဆုံးရှိ ဤမြေကို ဒဏ်ဖြင့် မဟုတ်၊ လက်နက်ဖြင့် မဟုတ်၊ တရားဖြင့် အောင်နိုင်၍ အုပ်ချုပ်၏။ "
  "အကယ်၍ လူ့ဘောင်မှ ထွက်၍ ရဟန်း ပြုလျှင် လောက၌ ကိလေသာ အဖုံးအကာကို ဖွင့်လှစ်ပြီးသော ရဟန္တာ၊ "
  f"{EPI11.split('၊ ')[2]} ဖြစ်၏”ဟူ၍{END}")
VAR_X["na aññā"] = F.PATHA

# ===================================================================================== 40. Niyāmokkantikathā
section("(40) 8. Niyāmokkantikathā", f"(40) 8. သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းခြင်းအကြောင်း {KATHA}")
section("Niyāmokkantikathā", f"သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းခြင်းအကြောင်း {KATHA}")
W("4", "^4-13", "niyāmaṃ okkamituṃ", "သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းရန်")
OKK = new("pāvacane okkantaniyāmo caritabrahmacariyo",
          "သာသနာ၌ သေချာသော လမ်းကြောင်းသို့ သက်ဆင်းပြီး၍ မြင့်မြတ်သော အကျင့်ကို ကျင့်ပြီးသူ")
W("2", "^2-509", "imasmiṃ brahmacariye", "မြင့်မြတ်သော အကျင့်")
MASTER = {"kassapassa bhagavato": f"ကဿပ {BUDDHA}", "bhagavato": BUDDHA}
WHO = {"bodhisatto": BS, "āyasmā ānando": f"{AYASMA} အာနန္ဒာ",
       "citto gahapati hatthako āḷavako": "စိတ္တ သူကြွယ်၊ ဟတ္ထက အာဠဝက"}
for _w, _wm in WHO.items():
    for _ms, _mm in MASTER.items():
        P(f"{_w} {_ms} pāvacane okkantaniyāmo caritabrahmacariyo", V(f"{_wm}သည် {_mm}၏ {OKK}"))
        P(f"{_w} {_ms} sāvako", V(f"{_wm}သည် {_mm}၏ {SAV}"))
for _ms, _mm in MASTER.items():
    P(f"na ca {_ms} sāvako", V(f"{_mm}၏ {SAV}လည်း", neg=True))
P("sāvako hutvā buddho hoti", Cl(f"{SAV} ဖြစ်ပြီးမှ {BUD}", *BEC))
P("anussaviyo", V("သူတစ်ပါးထံမှ ကြားနာ၍ သိသူ"))
P("bhagavā sayambhū", V(f"{BUDDHA}သည် ကိုယ်တိုင် အလိုလို သိတော်မူသူ"))
new("anussaviyo / sayambhū", "သူတစ်ပါးထံမှ ကြားနာ၍ သိသူ / ကိုယ်တိုင် အလိုလို သိတော်မူသူ")
SAMANNA = "ရဟန်း၏ အကျိုး"                                            # sāmaññaphala
for _n, _nm in (("tīṇeva", f"{F.NUM_MY[3]}{F.CL}တို့ကိုသာ"), ("cattāri", f"{F.NUM_MY[4]}{F.CL}တို့ကို")):
    P(f"bhagavatā bodhiyā mūle {_n} sāmaññaphalāni abhisambuddhāni",
      Cl(f"{BUDDHA}သည် ဗောဓိပင်ရင်း၌ {SAMANNA} {_nm}", "ထိုးထွင်း သိတော်မူခဲ့", "ထိုးထွင်း မသိတော်မူခဲ့"))
DKK = W("4", "^4-172", "dukkarakārikaṃ", "ပြုရခက်သော အကျင့်")
DSP = new("dassanasampanno puggalo", f"မှန်ကန်သော အမြင်နှင့် ပြည့်စုံသော {F.PUGGALA}")
P("bodhisatto dukkarakāriyaṃ akāsi", Cl(f"{BS}သည် {DKK}ကို", "ကျင့်ခဲ့", "မကျင့်ခဲ့"))
P("dassanasampanno puggalo dukkarakāriyaṃ kareyya", Cl(f"{DSP}သည် {DKK}ကို", "ကျင့်ရာ", "မကျင့်ရာ"))
P("bodhisatto aparantapaṃ akāsi, aññaṃ satthāraṃ uddisi",
  Cl(f"{BS}သည် အခြားသော ခြိုးခြံသော အကျင့်ကို ကျင့်ခဲ့၍ အခြား ဆရာကို", "ညွှန်ပြခဲ့", "မညွှန်ပြခဲ့"))
ANCHOR_X["aparantapaṃ"] = "ခြိုးခြံသော အကျင့်ကို"
VAR_X["amaraṃ tapaṃ"] = F.PATHA
P("dassanasampanno puggalo aññaṃ satthāraṃ uddiseyya", Cl(f"{DSP}သည် အခြား ဆရာကို", "ညွှန်ပြရာ", "မညွှန်ပြရာ"))
P("sāvako jātiṃ vītivatto asāvako hoti", Cl(f"{SAV}သည် ဘဝ တစ်ခုကို ကျော်လွန်ပြီးသောအခါ {SAV} မဟုတ်သူ", *BEC))
Q("kassape ahaṃ, ānanda, bhagavati brahmacariyaṃ acariṃ āyatiṃ sambodhāya",
  f"အာနန္ဒာ၊ ငါသည် ကဿပ {BUDDHA} ထံ၌ နောင်အခါ အမှန်ကို သိခြင်းအတွက် မြင့်မြတ်သော အကျင့်ကို ကျင့်ခဲ့၏")
UPAKA = [
    ('"Sabbābhibhū sabbavidūhamasmi,', "“ငါသည် အရာအားလုံးကို လွှမ်းမိုးသူ၊ အရာအားလုံးကို သိသူ ဖြစ်၏၊"),
    ("Sabbesu dhammesu anupalitto;", "သဘောတရား အားလုံးတို့၌ မလိမ်းကျံ၊"),
    ("Sabbañjaho taṇhakkhaye vimutto,", "အရာအားလုံးကို စွန့်ပယ်ပြီး တပ်မက်မှု ကုန်ခန်းရာ၌ လွတ်မြောက်ပြီ၊"),
    ("Sayaṃ abhiññāya kamuddiseyyaṃ.", "ကိုယ်တိုင် ထူးကဲစွာ သိ၍ အဘယ်သူကို ဆရာဟု ညွှန်ပြရအံ့နည်း။"),
    ('"Na me ācariyo atthi, sadiso me na vijjati;', f"“ငါ့အား ဆရာ {NEXIST}၊ ငါနှင့် တူသူ {NEXIST}၊"),
    ("Sadevakasmiṃ lokasmiṃ, natthi me paṭipuggalo.", f"နတ်နှင့်တကွသော လောက၌ ငါ့အား ပြိုင်ဘက် ပုဂ္ဂိုလ် {NEXIST}။"),
    ('"Ahañhi arahā loke, ahaṃ satthā anuttaro;', f"“ငါသည် လောက၌ {ARAHA} ဖြစ်၏၊ ငါသည် အမြတ်ဆုံး ဆရာ ဖြစ်၏၊"),
    ("Ekomhi sammāsambuddho, sītibhūtosmi nibbuto.",
     f"ငါသည် တစ်ဆူတည်းသော {EPI11.split('၊ ')[2]} ဖြစ်၏၊ ငါသည် အေးငြိမ်း၍ ငြိမ်းချမ်းပြီ။"),
    ('"Dhammacakkaṃ pavattetuṃ, gacchāmi kāsinaṃ puraṃ;', "“တရားစက်ကို လည်စေရန် ကာသိ မြို့သို့ ငါ သွားမည်၊"),
    ('Andhībhūtasmiṃ [andhabhūtasmiṃ (sī. syā. kaṃ. pī.)] lokasmiṃ, āhañchaṃ [āhaññiṃ (ka.)] amatadundubhi"nti '
     '[dudrabhinti (ka.)].', "ကန်းနေသော ⟦0⟧ လောက၌ အမြိုက် စည်ကို ⟦1⟧ တီးမည်”ဟူ၍ ⟦2⟧။"),
    ('"Yathā kho tvaṃ, āvuso, paṭijānāsi, arahasi anantajino"ti?',
     "“ငါ့ရှင်၊ သင် ဝန်ခံသည့်အတိုင်း သင်သည် အဆုံးမဲ့ အောင်နိုင်သူ ဖြစ်ထိုက်သလော”။"),
    ('"Mādisā ve jinā honti, ye pattā āsavakkhayaṃ;',
     "“စိတ်အစွန်းအထင်း ကုန်ခန်းခြင်းသို့ ရောက်ပြီးသူတို့သည် ငါကဲ့သို့သော အောင်နိုင်သူတို့ ဖြစ်ကုန်၏၊"),
    ('Jitā me pāpakā dhammā, tasmāhaṃ upaka jino"ti [mahāva. 11; ma. ni. 1.285; 2.341].',
     "ငါသည် ယုတ်မာသော သဘောတရားတို့ကို အောင်နိုင်ပြီ၊ ဥပက၊ ထို့ကြောင့် ငါသည် အောင်နိုင်သူ ဖြစ်၏”ဟူ၍ ⟦0⟧။"),
]
for _p, _m in UPAKA:
    LINES_X[key(_p)] = _m
VAR_X.update({"andhabhūtasmiṃ": F.LEKHANA, "āhaññiṃ": F.PATHA, "dudrabhinti": F.LEKHANA})
BR_X["[mahāva. 11; ma. ni. 1.285; 2.341]"] = "[“မဟာဝဂ်” 11၊ “မဇ္ဈိမနိကာယ်” 1.285၊ 2.341]"
REF_X["paṭi. ma."] = "“ပဋိသမ္ဘိဒါမဂ်”"
_AS = W("2", "^2-189", "dukkhaṃ ariyasaccaṃ", "အရိယာ သစ္စာ")
_TR = {"dukkhaṃ": "ဒုက္ခ", "dukkhasamudayaṃ": "ဒုက္ခ ဖြစ်ပေါ်ခြင်း", "dukkhanirodhaṃ": "ဒုက္ခ ချုပ်ငြိမ်းခြင်း",
       "dukkhanirodhagāminī paṭipadā": W("2", "^2-189", "dukkhanirodhagāminī paṭipadā ariyasaccaṃ",
                                         "ဒုက္ခ ချုပ်ငြိမ်းရာသို့ ရောက်စေသော ကျင့်စဉ်")}
_EYE5 = "မျက်စိ ဖြစ်ပေါ်၏၊ ဉာဏ် ဖြစ်ပေါ်၏၊ ပညာ ဖြစ်ပေါ်၏၊ အမှန်သိမြင်မှု ဖြစ်ပေါ်၏၊ အလင်း ဖြစ်ပေါ်၏"
_ANAN = "ယခင်က မကြားဖူးသော တရားတို့၌"
W("4", "^4-M-12", "pubbe ananussutesu dhammesu", _ANAN)
_R = "ရဟန်းတို့၊"
S('Nanu vuttaṃ bhagavatā – "‘idaṃ dukkhaṃ ariyasacca’nti me, bhikkhave, pubbe ananussutesu dhammesu cakkhuṃ '
  'udapādi, ñāṇaṃ udapādi, paññā udapādi, vijjā udapādi, āloko udapādi. ‘Taṃ kho panidaṃ dukkhaṃ ariyasaccaṃ '
  'pariññeyya’nti me, bhikkhave…pe… pariññātanti me, bhikkhave, pubbe ananussutesu dhammesu cakkhuṃ udapādi…pe… '
  'āloko udapādi. ‘Idaṃ dukkhasamudayaṃ ariyasacca’nti me, bhikkhave…pe… ‘taṃ kho panidaṃ dukkhasamudayaṃ '
  '[dukkhasamudayo (syā. kaṃ.)] ariyasaccaṃ pahātabba’nti me, bhikkhave…pe… pahīnanti me, bhikkhave…pe… ‘idaṃ '
  'dukkhanirodhaṃ [dukkhanirodho (syā. kaṃ.)] ariyasacca’nti me, bhikkhave…pe… ‘taṃ kho panidaṃ dukkhanirodhaṃ '
  'ariyasaccaṃ sacchikātabba’nti me, bhikkhave…pe… sacchikatanti me, bhikkhave…pe… ‘idaṃ dukkhanirodhagāminī '
  'paṭipadā ariyasacca’nti me, bhikkhave…pe… ‘taṃ kho panidaṃ dukkhanirodhagāminī paṭipadā ariyasaccaṃ '
  'bhāvetabba’nti me, bhikkhave…pe… bhāvitanti me, bhikkhave, pubbe ananussutesu dhammesu cakkhuṃ udapādi, ñāṇaṃ '
  'udapādi, paññā udapādi, vijjā udapādi, āloko udapādī"ti [mahāva. 15; saṃ. ni. 5.1081; paṭi. ma. 2.30].',
  f"{BUDDHA} ဤသို့ ဟောတော်မူသည် မဟုတ်လော – “{_R} ‘ဤသည်ကား {_TR['dukkhaṃ']} {_AS}’ဟု {_ANAN} ငါ့အား {_EYE5}။ "
  f"{_R} ‘ထို{_TR['dukkhaṃ']} {_AS}ကို ပိုင်းခြား သိရမည်’ဟု ငါ့အား… {_R} ပိုင်းခြား သိပြီးပြီဟု {_ANAN} ငါ့အား "
  f"မျက်စိ ဖြစ်ပေါ်၏… အလင်း ဖြစ်ပေါ်၏။ {_R} ‘ဤသည်ကား {_TR['dukkhasamudayaṃ']} {_AS}’ဟု ငါ့အား… {_R} "
  f"‘ထို{_TR['dukkhasamudayaṃ']} ⟦b⟧ {_AS}ကို ပယ်ရမည်’ဟု ငါ့အား… {_R} ပယ်ပြီးပြီဟု ငါ့အား… {_R} ‘ဤသည်ကား "
  f"{_TR['dukkhanirodhaṃ']} ⟦b⟧ {_AS}’ဟု ငါ့အား… {_R} ‘ထို{_TR['dukkhanirodhaṃ']} {_AS}ကို မျက်မှောက်ပြုရမည်’ဟု "
  f"ငါ့အား… {_R} မျက်မှောက်ပြုပြီးပြီဟု ငါ့အား… {_R} ‘ဤသည်ကား {_TR['dukkhanirodhagāminī paṭipadā']} {_AS}’ဟု ငါ့အား… "
  f"{_R} ‘ထို{_TR['dukkhanirodhagāminī paṭipadā']} {_AS}ကို ပွားများရမည်’ဟု ငါ့အား… {_R} ပွားများပြီးပြီဟု {_ANAN} "
  f"ငါ့အား {_EYE5}”ဟူ၍{END}")
VAR_X.update({"dukkhasamudayo": F.LEKHANA, "dukkhanirodho": F.LEKHANA})

# ===================================================================================== 42. Sabbasaṃyojanappahānakathā
SSP = new("sabbasaṃyojanānaṃ pahānaṃ", "နှောင်ကြိုး အားလုံးတို့ကို ပယ်ခြင်း")
section("(42) 10. Sabbasaṃyojanappahānakathā", f"(42) 10. {SSP}အကြောင်း {KATHA}")
section("Sabbasaṃyojanappahānakathā", f"{SSP}အကြောင်း {KATHA}")
P("sabbasaṃyojanānaṃ pahānaṃ arahattaṃ", V(f"{SSP}သည် {ARAHATTA_N}"))
P("arahattamaggena sabbe saṃyojanā pahīyanti",
  Cl(f"{MG['arahatta']}ဖြင့် နှောင်ကြိုး အားလုံးတို့", "ပယ်ခံရကြ", "ပယ်ခံ မရကြ"))
for _k, _m in KIL12.items():
    P(f"arahattamaggena {_k} pajahati", VV(f"{MG['arahatta']}ဖြင့် {_m}ကို", "ပယ်"))
_SAID = ("ဟောတော်မူ", "မဟောတော်မူ")
for _k, _m in (("tiṇṇaṃ saṃyojanānaṃ pahānaṃ sotāpattiphalaṃ", f"နှောင်ကြိုး {F.NUM_MY[3]}{F.CL}တို့ကို ပယ်ခြင်းကို "
                                                             f"{PH['sotāpatti']}"),
               ("kāmarāgabyāpādānaṃ tanubhāvaṃ sakadāgāmiphalaṃ",
                f"ကာမရာဂနှင့် ဖျက်ဆီးလိုစိတ်တို့ ပါးလျခြင်းကို {PH['sakadāgāmi']}"),
               ("kāmarāgabyāpādānaṃ anavasesappahānaṃ anāgāmiphalaṃ",
                f"ကာမရာဂနှင့် ဖျက်ဆီးလိုစိတ်တို့ကို အကြွင်းမဲ့ ပယ်ခြင်းကို {PH['anāgāmi']}"),
               ("rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānaṃ arahattaṃ",
                W("2", "^2-U49", "Rūparāgo", "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ") + "၊ "
                + W("2", "^2-U49", "arūparāgo", "ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ") + "၊ မာန၊ "
                + W("2", "^2-U49", "uddhaccaṃ", "ယောက်ယက်ခတ်မှု") + "၊ "
                + W("2", "^2-U49", "avijjā", "အမှန်ကို မသိမှု") + f"တို့ကို အကြွင်းမဲ့ ပယ်ခြင်းကို {ARAHATTA_N}")):
    P(f"{_k} vuttaṃ bhagavatā", Cl(f"{_m}ဟု {BUDDHA}", *_SAID))
new("anavasesa (make_ch2-5, copied)", "အကြွင်းမဲ့")
P("arahato sabbe saṃyojanā pahīnā", Cl(f"{ARAHA}သည် နှောင်ကြိုး အားလုံးတို့ကို", *PAHINA))
LINES_X[key("Gihissa arahā, saha upapattiyā arahā, arahato sabbe dhammā anāsavā, arahā catūhi phalehi samannāgato, "
            "evamevaṃ chahi upekkhāhi, bodhiyā buddho, salakkhaṇasamannāgato, bodhisatto okkantaniyāmo "
            "caritabrahmacariyo, paṭipannako phalena samannāgato, sabbasaṃyojanānaṃ pahānaṃ arahattanti.")] = (
    f"{GIHI} {ARAHA}၊ {SAHA_U} {ARAHA}၊ {ARAHA}၏ {P6.ALL_DH}တို့သည် {ANAS} အရာ ဖြစ်ခြင်း၊ {ARAHA}သည် ဖိုလ် "
    f"{F.NUM_MY[4]}{F.CL}နှင့် ပြည့်စုံခြင်း၊ {EVAM} ဥပေက္ခာ {F.NUM_MY[6]}{F.CL}၊ {BODHI}ဖြင့် {BUD}၊ {LK}နှင့် "
    f"ပြည့်စုံသူ၊ {BS}သည် သေချာသော လမ်းကြောင်းသို့ သက်ဆင်း၍ မြင့်မြတ်သော အကျင့်ကို ကျင့်ပြီးသူ၊ ကျင့်ကြံဆဲသူ "
    f"ဖိုလ်နှင့် ပြည့်စုံခြင်း၊ {SSP}သည် {ARAHATTA_N}{END}")


# ===================================================================================== run
def install():
    F.VAR_KIND.update(VAR_X)
    F.REF.update(REF_X)
    F.REF_NOTE.update(REF_NOTE_X)
    F._REF_RE = re.compile(r"(?P<r>" + "|".join(re.escape(k) for k in sorted(F.REF, key=len, reverse=True))
                           + r") (?P<n>[\d.\-]+)")
    F.BR_TABLE.update(BR_X)
    F.PROP.update(PROP_X)
    F.QUOTE.update(QUOTE_X)
    F.SENT.update(SENT_X)
    F.LINES.update(LINES_X)
    F.ANCHOR.update(ANCHOR_X)
    F.HEAD.update(HEAD_X)
    F.COLO.update(COLO_X)


install()


def run(name, misses=False):
    return P6.run(name, misses)


def main():
    args = sys.argv[1:]
    misses = "--misses" in args
    names = [a for a in args if not a.startswith("--")] or NAMES_OUT
    if "--units" in args:
        for name in names:
            P6.units(name)
        return
    total = 0
    for name in names:
        text, bad = run(name, misses)
        total += bad
        if not misses and not bad:
            assert "\n\n\n" not in text
            (OUT / name).write_text(text, encoding="utf-8")
            print(f"wrote {name}")
    if misses:
        print(f"{total} misses")


if __name__ == "__main__":
    main()
