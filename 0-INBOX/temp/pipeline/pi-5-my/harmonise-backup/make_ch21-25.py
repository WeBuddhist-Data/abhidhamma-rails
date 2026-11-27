"""Burmese zero-shot of pi-5 (Kathāvatthu, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»), chapters 21-25:
21-terasamavaggo, 22-cuddasamavaggo, 23-pannarasamavaggo, 24-solasamavaggo, 25-sattarasamavaggo.

usage: python3 -I -X utf8 make_ch21-25.py [chapter ...] [--misses] [--units]
Model: the approved sample. Every line is generated from the Pāli by my5_formulas.translate_line() through the
frames, rules and tables of my5_formulas.py, make_sample.py, make_ch6-10.py and make_ch11-12.py (all imported READ
ONLY: they install their tables at import and write nothing; their __main__ never runs) and the tables of THIS
script, which extends them IN MEMORY only (nothing in my5_formulas.py / make_*.py / my5-zeroshot-terms.md changes).
  * PROP_X (propositions), QUOTE_X (sutta quotations), SENT_X (unique sentences), LINES_X (verses, uddāna),
    HEAD_X / COLO_X (headings, colophons); productive propositions are built from small tables;
  * NEW: every new recurring term or phrase (Pāli = Burmese), copied into notes-ch21-25.md.
A unit no frame / rule / table matches stops the run (Miss): nothing is guessed.
"""
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
_spec = importlib.util.spec_from_file_location("make_ch11_12", HERE / "make_ch11-12.py")
P11 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P11)         # installs make_sample + make_ch6-10 + make_ch11-12 tables; writes nothing
P6 = P11.P6
MS = P11.MS
F = P11.F
from my5_formulas import V, FR, Cl, C, END, PE  # noqa: E402,F401

PALI = MS.PALI
OUT = MS.OUT
NAMES_OUT = ["21-terasamavaggo.md", "22-cuddasamavaggo.md", "23-pannarasamavaggo.md", "24-solasamavaggo.md",
             "25-sattarasamavaggo.md"]
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
key = P11.key


def _same(a, b):
    return all(a.f(x) == b.f(x) for x in ("stmt", "q", "bare", "cond", "nanu"))


def P(pali, cl):
    """A proposition (canonical form). An entry the imported tables already have must give the same Burmese."""
    k = key(pali)
    k = k[:1].lower() + k[1:]
    old = F.PROP.get(k) or PROP_X.get(k)
    if old is not None and not _same(old, cl):
        raise SystemExit(f"P: «{k}» already has another Burmese: {old.f('stmt')} / {cl.f('stmt')}")
    PROP_X[k] = cl
    return cl


def S(pali, my):
    SENT_X[key(pali)] = my
    return my


def Q(pali, my):
    QUOTE_X[key(pali)] = my
    return my


VV = P11.VV
NSAY = P11.NSAY


def before_generic():
    """Move the frame just registered before the generic «P-ti?» / «P-ti.» frames."""
    fr = F.FRAMES.pop()
    F.FRAMES.insert(next(i for i, (_, fn) in enumerate(F.FRAMES) if fn is F._f_q), fr)


# ===================================================================================== shared vocabulary
BUDDHA = F.BHAGAVA                                                    # bhagavā / tathāgato (pi-2 «မြတ်စွာဘုရား»)
SAID = ("ဟောတော်မူ", "မဟောတော်မူ")                                   # vutto bhagavatā (ch11-12 _SAID)
BHAVITA, PAHINA = P6.BHAVITA, P6.PAHINA
SATIP, SP, ID, BJW = P6.SATIPATTHANA, P6._SP, P6._ID, P6._BJW
INDRIYA, BALA = F.INDRIYA_W, "စွမ်းအား"
RUPA_AV, ARUPA_AV, KAMA_AV = P11.RUPA_AV, P11.ARUPA_AV, P11.KAMA_AV
LOKIYA, LOKUTTARA = P6.LOKIYA, P6.LOKUTTARA
ABY = MS.ABY                                                          # abyākata (core term)
CITTA = P11.CITTA
ARAHA, PUTHU, BS = P11.ARAHA, P11.PUTHU, P11.BS
MG, PH = P11.MG, P11.PH
JAHATI = "စွန့်ပယ်"                                                   # jahati (make_ch2-5 JAHATI, copied)
NIBBANA = F.NIBBANA
KUSALA, AKUSALA = "ကုသိုလ်", "အကုသိုလ်"
THING = "အရာ"
EXN = ("ရှိ", "မရှိ")                                                  # atthi / natthi as verb stems
MK11 = P11.MK                                                           # manasi karoti «နှလုံးသွင်း» (ch11-12)
ORD_X = {13: "တေရသမ", 14: "စုဒ္ဒသမ", 15: "ပန္နရသမ", 16: "သောဠသမ", 17: "သတ္တရသမ"}   # vagga ordinals 13-17
for _n, _v in ((13, "Terasamavaggo"), (14, "Cuddasamavaggo"), (15, "Pannarasamavaggo"), (16, "Soḷasamavaggo"),
               (17, "Sattarasamavaggo")):
    HEAD_X[_v] = new(_v, f"{ORD_X[_n]} {F.VAGGA_W}")
    COLO_X[_v] = HEAD_X[_v]
AY_N = {k[:-len("āyatanaṃ")]: v.my for k, (v, r) in F.NOUN.items() if k.endswith("āyatanaṃ") and "nom" in r}
TAN = {"rūpa": "အဆင်းအရောင်", "sadda": "အသံ", "gandha": "အနံ့", "rasa": "အရသာ", "phoṭṭhabba": "အထိအတွေ့",
       "dhamma": "သဘောတရား"}                                          # the six cravings (pi-2 ^2-U62)
_U62 = W("2", "^2-U62", "Rūpataṇhā, saddataṇhā, gandhataṇhā, rasataṇhā, phoṭṭhabbataṇhā, dhammataṇhā",
         "၊ ".join(f"{v}ကို တပ်မက်မှု" for v in TAN.values()))
TANHA = W("2", "^2-U62", "taṇhākāyā", "တပ်မက်မှု")
TN = {k: f"{v}ကို {TANHA}" for k, v in TAN.items()}                   # rūpataṇhā …
LOBHA = W("1", "^1-1065", "Tattha katamo lobho", "လောဘ")
DUKKHASAM = P11._TR["dukkhasamudayaṃ"]                                # dukkhasamudaya «ဒုက္ခ ဖြစ်ပေါ်ခြင်း» (pi-2 ^2-189)
KSA_PI = "kusalākusalā sāvajjānavajjā hīnapaṇītā kaṇhasukkasappaṭibhāgā dhammā"
KSA = (W("4", "^4-104", "kusalākusale dhamme", "ကုသိုလ် အကုသိုလ်") + "၊ "
       + W("4", "^4-104", "sāvajjānavajje dhamme", "အပြစ် ရှိသော အပြစ် မရှိသော") + "၊ "
       + W("4", "^4-104", "hīnappaṇīte dhamme", "ယုတ်ညံ့သော မွန်မြတ်သော") + "၊ "
       + W("4", "^4-104", "kaṇhasukkasappaṭibhāge dhamme", "မည်းနက်သော ဖြူစင်သော ဆန့်ကျင်ဘက် ရှိသော")
       + " သဘောတရားတို့")
FACE = ("မျက်နှာချင်းဆိုင် ဖြစ်လာကြ", "မျက်နှာချင်းဆိုင် မဖြစ်လာကြ")   # sammukhībhāvaṃ āgacchanti
new("sammukhībhāvaṃ āgacchanti", FACE[0])
P(f"{KSA_PI} sammukhībhāvaṃ āgacchanti", Cl(f"{KSA}သည်", *FACE))
P("kusalākusalā…pe… sammukhībhāvaṃ āgacchanti", Cl("ကုသိုလ် အကုသိုလ်… သဘောတရားတို့သည်", *FACE))
SAMP = W("1", "^1-M2-58", "cittasampayuttā", "စိတ်နှင့် ယှဉ်တွဲသော")
P("dvinnaṃ phassānaṃ…pe… dvinnaṃ cittānaṃ samodhānaṃ hoti", V("တွေ့ထိမှု နှစ်ပါး… စိတ် နှစ်ပါးတို့၏ ပေါင်းဆုံခြင်း"))
_ARY = ("rūpaṃ nibbānaṃ cakkhāyatanaṃ…pe… phoṭṭhabbāyatanaṃ",
        f"{F.RUPA.my}၊ {NIBBANA}၊ {AY_N['cakkh']}… {AY_N['phoṭṭhabb']}")
P(_ARY[0], V(_ARY[1]))
VIPABY = f"{W('1', '^1-1386', 'Catūsu bhūmīsu vipāko', 'ကံ၏ အကျိုး ဖြစ်သော')} {ABY} အရာ"      # vipākābyākata
KIRABY = f"{W('1', '^1-1386', 'kiriyābyākataṃ', 'ပြုရုံမျှသာ ဖြစ်သော')} {ABY} အရာ"          # kiriyābyākata
for _e in ("ā", "aṃ"):
    P(f"vipākābyākat{_e} kiriyābyākat{_e} {_ARY[0]}", V(f"{VIPABY}၊ {KIRABY}၊ {_ARY[1]}"))
new("vipākābyākata / kiriyābyākata", f"{VIPABY} / {KIRABY}")
_SO_PE = P11._SO[:P11._SO.index("တည်ကြည်၍၊") + len("တည်ကြည်၍")] + "… " + P11._SO[P11._SO.index("စိတ်အစွန်းအထင်းတို့ ကုန်ခန်း"):]
Q("so evaṃ samāhite citte…pe… āsavānaṃ khayañāṇāya cittaṃ abhininnāmeti", _SO_PE)
_TS = P11.QUOTE_X[key("tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati, bhavāsavāpi cittaṃ vimuccati, "
                      "avijjāsavāpi cittaṃ vimuccati")].split("၏၊ ")
assert len(_TS) == 3
Q("tassa evaṃ jānato evaṃ passato kāmāsavāpi cittaṃ vimuccati…pe… avijjāsavāpi cittaṃ vimuccati",
  f"{_TS[0]}၏… {_TS[2]}")

# ===================================================================================== 126. Kappaṭṭhakathā
KAPPA = "ကမ္ဘာ"                                                       # kappa (aeon)
KT = new("kappaṭṭho", f"{KAPPA} ပတ်လုံး တည်ရမည့်သူ")
KTP = f"{KAPPA} ပတ်လုံး တည်ရမည့် {F.PUGGALA}"                         # kappaṭṭho puggalo
KTK = new("kappaṭṭhiyaṃ kammaṃ", f"{KAPPA} ပတ်လုံး တည်စေသော {F.KAMMA}")
STAY = ("တည်ရာ", "မတည်ရာ")
section("(126) 1. Kappaṭṭhakathā", f"(126) 1. {KT}အကြောင်း {KATHA}")
section("Kappaṭṭhakathā", f"{KT}အကြောင်း {KATHA}")
P("kappaṭṭho kappaṃ tiṭṭheyya", Cl(f"{KT}သည် {KAPPA} ပတ်လုံး", *STAY))
_KS = f"{KAPPA}လည်း တည်နေ၍"                                            # kappo ca saṇṭhāti
P("kappo ca saṇṭhāti buddho ca loke uppajjati", Cl(f"{_KS} ဘုရားလည်း လောက၌", "ပွင့်ထွန်းတော်မူ", "မပွင့်ထွန်းတော်မူ"))
W("4", "^4-177", "tathāgato loke uppajjati", "ပွင့်ထွန်းတော်မူ")
P("kappo ca saṇṭhāti saṅgho ca bhijjati", Cl(f"{_KS} {F.SANGHA}လည်း", "ကွဲပြား", "မကွဲပြား"))
P("kappo ca saṇṭhāti kappaṭṭho ca kappaṭṭhiyaṃ kammaṃ karoti", Cl(f"{_KS} {KT}သည်လည်း {KTK}ကို", "ပြု", "မပြု"))
P("kappo ca saṇṭhāti kappaṭṭho ca puggalo kālaṃ karoti", Cl(f"{_KS} {KTP}သည်လည်း", "သေ", "မသေ"))
P("atītaṃ kappaṃ tiṭṭheyya, anāgataṃ kappaṃ tiṭṭheyya",
  Cl(f"{P6.ATITA} {KAPPA} ပတ်လုံး တည်ရာ၍ {P6.ANAGATA} {KAPPA} ပတ်လုံး", *STAY))
for _n, _k in (("dve", 2), ("tayo", 3), ("cattāro", 4)):
    P(f"{_n} kappe tiṭṭheyya", Cl(f"{KAPPA} {F.NUM_MY[_k]}{KAPPA} ပတ်လုံး", *STAY))
S("Kappaṭṭho kappe ḍayhante kattha gacchatīti?", f"{KAPPA} မီးလောင်သောအခါ {KT}သည် အဘယ်သို့ သွားသနည်း{END}")
S("Aññaṃ lokadhātuṃ gacchatīti.", f"အခြား စကြဝဠာသို့ သွားပါသည်{END}")
S("Mato gacchati, vehāsaṃ gacchatīti?", f"သေ၍ သွားသလော၊ ကောင်းကင်ဖြင့် သွားသလော{END}")
S("Mato gacchatīti.", f"သေ၍ သွားပါသည်{END}")
P("kappaṭṭhiyaṃ kammaṃ aparāpariyavepakkaṃ", V(f"{KTK}သည် နောက်ဘဝ အဆက်ဆက်၌ အကျိုးပေးသော {F.KAMMA}"))
P("vehāsaṃ gacchati", VV("ကောင်းကင်ဖြင့်", "သွား"))
BR_X["[vehāsaṃ gacchatīti (?) ayaṃ hi paravādissa paṭiññāyeva, kathā. 621-623 navamapantiyaṃ viya]"] = (
    f"[ကောင်းကင်ဖြင့် သွားသည်ဟူသည် (မသေချာ) ဤသည်ကား {F.PARAVADI}၏ ဝန်ခံချက်သာ ဖြစ်သည်၊ {KATHA} 621-623 ၏ "
    "နဝမ စာကြောင်း၌ကဲ့သို့]")
P("kappaṭṭho iddhimā", V(f"{KT}သည် {F.IDDHI} ရှိသူ"))
_IDP = [W("2", "^2-9-1-1-0", "Chandiddhipādo", "ဆန္ဒ ဣဒ္ဓိပါဒ်"), W("2", "^2-9-1-2-0", "Vīriyiddhipādo", "ဝီရိယ ဣဒ္ဓိပါဒ်"),
        W("2", "^2-9-1-3-0", "Cittiddhipādo", "စိတ် ဣဒ္ဓိပါဒ်"),
        W("2", "^2-9-1-4-0", "Vīmaṃsiddhipādo", "စုံစမ်းဆင်ခြင်မှု ဣဒ္ဓိပါဒ်")]
P("kappaṭṭhena chandiddhipādo bhāvito vīriyiddhipādo bhāvito cittiddhipādo bhāvito vīmaṃsiddhipādo bhāvito",
  Cl(f"{KT}သည် " + "၊ ".join(f"{x}ကို {BHAVITA[0]}" for x in _IDP[:3]) + f"၊ {_IDP[3]}ကို", *BHAVITA))
LINES_X[key('"Āpāyiko nerayiko, kappaṭṭho saṅghabhedako;')] = (
    f"“{F.SANGHA}ကို ခွဲသူသည် အပါယ်သို့ ရောက်သူ၊ ငရဲ၌ ကျသူ၊ {KT} ဖြစ်၏၊")
LINES_X[key("Vaggarato adhammaṭṭho, yogakkhemā padhaṃsati;")] = (
    "အသင်းကွဲခြင်း၌ မွေ့လျော်သူ၊ တရား မဟုတ်သည်၌ တည်သူသည် ထမ်းပိုးမှ လွတ်ငြိမ်းရာမှ ပျက်စီး၏၊")
LINES_X[key('Saṅghaṃ samaggaṃ bhetvāna [bhinditvā (sī. ka.)], kappaṃ nirayamhi paccatī"ti '
            '[cūḷava. 354; a. ni. 10.39; itivu. 18].')] = (
    f"ညီညွတ်သော {F.SANGHA}ကို ခွဲ၍ ⟦0⟧ {KAPPA} ပတ်လုံး ငရဲ၌ ပူလောင်ရ၏”ဟူ၍ ⟦1⟧{END}")
VAR_X["bhinditvā"] = F.PATHA
new("yogakkhema", "ထမ်းပိုးမှ လွတ်ငြိမ်းရာ")

# ===================================================================================== 127. Kusalapaṭilābhakathā
section("(127) 2. Kusalapaṭilābhakathā", f"(127) 2. {KUSALA}ကို ရခြင်းအကြောင်း {KATHA}")
section("Kusalapaṭilābhakathā", f"{KUSALA}ကို ရခြင်းအကြောင်း {KATHA}")
GET = ("ရရာ", "မရရာ")
for _n, _neg in (("", False), ("na ", True)):
    P(f"kappaṭṭho kusalaṃ cittaṃ {_n}paṭilabheyya", Cl(f"{KT}သည် {KUSALA} {CITTA}ကို", *GET, neg=_neg))
GIVE = ("လှူရာ", "မလှူရာ")
P("kappaṭṭho dānaṃ dadeyya", Cl(f"{KT}သည် ဒါန", "ပြုရာ", "မပြုရာ"))
new("dānaṃ dadeyya", "ဒါန ပြုရာ")
_GL = W("2", "^2-849", "gilānappaccayabhesajjaparikkhārehi", "သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်")
DANA_I = {"cīvaraṃ": W("2", "^2-849", "Itarītaracīvara", "သင်္ကန်း"), "piṇḍapātaṃ": W("2", "^2-849", "piṇḍapāta", "ဆွမ်း"),
          "senāsanaṃ": W("2", "^2-849", "senāsana", "ကျောင်းအိပ်ရာနေရာ"), "gilānapaccayabhesajjaparikkhāraṃ": _GL,
          "khādanīyaṃ": "ခဲဖွယ်", "bhojanīyaṃ": "ဘောဇဉ်", "pānīyaṃ": "သောက်ရေ"}
for _k, _m in DANA_I.items():
    P(f"kappaṭṭho {_k} dadeyya", Cl(f"{KT}သည် {_m}ကို", *GIVE))
    P(f"{_k} dadeyya", Cl(f"{_m}ကို", *GIVE))
CETIYA = new("cetiya", "စေတီ")
P("cetiyaṃ vandeyya", Cl(f"{CETIYA}ကို", "ရှိခိုးရာ", "မရှိခိုးရာ"))
P("cetiye mālaṃ āropeyya", Cl(f"{CETIYA}၌ ပန်းကို", "တင်လှူရာ", "မတင်လှူရာ"))
W("4", "^4-168", "mālāgandhavilepanassa", "ပန်း နံ့သာ နံ့သာပျောင်း")
P("gandhaṃ āropeyya", Cl("နံ့သာကို", "တင်လှူရာ", "မတင်လှူရာ"))
P("vilepanaṃ āropeyya", Cl("နံ့သာပျောင်းကို", "တင်လှူရာ", "မတင်လှူရာ"))
for _s, _sm in (("", ""), ("kappaṭṭho ", f"{KT}သည် ")):
    P(f"{_s}cetiyaṃ abhidakkhiṇaṃ kareyya", Cl(f"{_sm}{CETIYA}ကို လက်ယာရစ်", "လှည့်ပတ်ရာ", "မလှည့်ပတ်ရာ"))
ANCHOR_X["abhidakkhiṇaṃ"] = "လက်ယာရစ်"
VAR_X["padakkhiṇaṃ"] = F.PATHA
P("tato vuṭṭhānaṃ kusalaṃ cittaṃ paṭilabheyya", Cl(f"ထိုမှ ထမြောက်ရန် {KUSALA} {CITTA}ကို", *GET))
P("rūpāvacaraṃ", FR(RUPA_AV))
P("arūpāvacaraṃ", FR(ARUPA_AV))
P("lokuttaraṃ kusalaṃ cittaṃ paṭilabheyya", Cl(f"{LOKUTTARA} {KUSALA} {CITTA}ကို", *GET))

# ===================================================================================== 128. Anantarāpayuttakathā
NIYAMA = "သေချာသော လမ်းကြောင်း"                                      # niyāma (pi-4 ^4-13)
W("4", "^4-13", "niyāmaṃ okkamituṃ", f"{NIYAMA}သို့ သက်ဆင်းရန်")
SNM = new("sammattaniyāma", f"မှန်ကန်မှု၌ {NIYAMA}")                  # pi-1 sammattaniyata «မှန်ကန်မှု၌ ကျိန်းသေသော»
MNM = new("micchattaniyāma", f"မှားယွင်းမှု၌ {NIYAMA}")
W("1", "^1-M1-15", "micchattaniyatā dhammā", "မှားယွင်းမှု၌ ကျိန်းသေသော")
ANP = new("anantarāpayutto puggalo", f"ချက်ချင်း အကျိုးပေးသော {F.KAMMA}ကို ပြုခဲ့သော {F.PUGGALA}")
W("2", "^2-U55", "kammāni ānantarikāni", "ချက်ချင်း အကျိုးပေးသော ကံ")
section("(128) 3. Anantarāpayuttakathā", f"(128) 3. {ANP}အကြောင်း {KATHA}")
section("Anantarāpayuttakathā", f"{ANP}အကြောင်း {KATHA}")
OKKR = ("သက်ဆင်းရာ", "မသက်ဆင်းရာ")
OKK = ("သက်ဆင်း", "မသက်ဆင်း")
P("anantarāpayutto puggalo sammattaniyāmaṃ okkameyya", Cl(f"{ANP}သည် {SNM}သို့", *OKKR))
P("micchattaniyāmañca sammattaniyāmañca ubho okkameyya", Cl(f"{MNM}နှင့် {SNM} နှစ်ပါးစလုံးသို့", *OKKR))
KUKK = W("1", "^1-1164", "kukkuccaṃ", "နောင်တ ပူပန်မှု")
VIPP = new("vippaṭisāriya", "စိတ် ပူလောင်မှု")
P("taṃ kammaṃ payuttaṃ kukkuccaṃ uppāditaṃ vippaṭisāriyaṃ janitaṃ",
  Cl(f"ထို{F.KAMMA}ကို ပြုခဲ့ပြီး၍ {KUKK}ကို ဖြစ်ပေါ်စေခဲ့ပြီး၍ {VIPP}ကို", "ဖြစ်စေခဲ့ပြီး", "မဖြစ်စေရသေး"))
ABH_OKK = ("သက်ဆင်းနိုင်", "မသက်ဆင်းနိုင်")                          # (a)bhabbo … okkamituṃ (make_ch2-5)
P("anantarāpayutto puggalo abhabbo sammattaniyāmaṃ okkamituṃ", Cl(f"{ANP}သည် {SNM}သို့", *ABH_OKK, neg=True))
_U55 = {"mātā jīvitā voropitā": W("2", "^2-U55", "Mātā jīvitā voropitā hoti", "အမိသည် အသက်မှ ချခံရ"),
        "pitā jīvitā voropito": W("2", "^2-U55", "pitā jīvitā voropito hoti", "အဖသည် အသက်မှ ချခံရ"),
        "arahā jīvitā voropito": W("2", "^2-U55", "arahanto jīvitā voropito hoti", "ရဟန္တာသည် အသက်မှ ချခံရ"),
        "duṭṭhena cittena tathāgatassa lohitaṃ uppāditaṃ":
            W("2", "^2-U55", "duṭṭhena cittena tathāgatassa lohitaṃ uppāditaṃ hoti",
              "ပြစ်မှားသော စိတ်ဖြင့် မြတ်စွာဘုရား၏ သွေးကို ထွက်စေအပ်"),
        "saṅgho bhinno": W("2", "^2-U55", "saṅgho bhinno hoti", "သံဃာသည် ကွဲပြားစေခံရ")}
for _k, _m in _U55.items():
    _pre, _v = _m.rsplit(" ", 1)
    P(_k, Cl(_pre, _v, "မ" + _v if not _v.startswith("ချ") else "ချ မခံရ"))
_PAT = f"ထို{F.KAMMA}ကို ပြန်ရုပ်သိမ်း၍ {KUKK}ကို ပယ်ဖျောက်၍ {VIPP}ကို ဖယ်ရှား၍"
P("anantarāpayutto puggalo taṃ kammaṃ paṭisaṃharitvā kukkuccaṃ paṭivinodetvā vippaṭisāriyaṃ paṭivinetvā abhabbo "
  "sammattaniyāmaṃ okkamituṃ", Cl(f"{ANP}သည် {_PAT} {SNM}သို့", *ABH_OKK, neg=True))
ANCHOR_X["paṭivinetvā"] = "ဖယ်ရှား၍"
VAR_X["paṭivinodetvā"] = F.PATHA
P("taṃ kammaṃ paṭisaṃhaṭaṃ kukkuccaṃ paṭivinoditaṃ vippaṭisāriyaṃ paṭivinītaṃ",
  Cl(f"ထို{F.KAMMA}ကို ပြန်ရုပ်သိမ်းပြီး၍ {KUKK}ကို ပယ်ဖျောက်ပြီး၍ {VIPP}ကို", "ဖယ်ရှားပြီး", "မဖယ်ရှားရသေး"))
P("taṃ kammaṃ payutto āsi", Cl(f"ထို{F.KAMMA}ကို", "ပြုခဲ့", "မပြုခဲ့"))

# ===================================================================================== 129. Niyatassa niyāmakathā
NIYATO = new("niyato (a person)", "လမ်းကြောင်း သေချာပြီးသူ")
MNY = new("micchattaniyato", f"မှားယွင်းမှု၌ {NIYATO}")
SNY = new("sammattaniyato", f"မှန်ကန်မှု၌ {NIYATO}")
section("(129) 4. Niyatassa niyāmakathā", f"(129) 4. {NIYATO}၏ {NIYAMA}အကြောင်း {KATHA}")
section("Niyatassa niyāmakathā", f"{NIYATO}၏ {NIYAMA}အကြောင်း {KATHA}")
P("niyato niyāmaṃ okkamati", Cl(f"{NIYATO}သည် {NIYAMA}သို့", *OKK))
P("micchattaniyato sammattaniyāmaṃ okkamati, sammattaniyato micchattaniyāmaṃ okkamati",
  Cl(f"{MNY}သည် {SNM}သို့ သက်ဆင်း၍ {SNY}သည် {MNM}သို့", *OKK))
PUBBE = "အရင်"                                                        # pubbe … pacchā
P("pubbe maggaṃ bhāvetvā pacchā niyāmaṃ okkamati", Cl(f"{PUBBE} မဂ်ကို ပွားများ၍ နောက်မှ {NIYAMA}သို့", *OKK))
P("pubbe sotāpattimaggaṃ bhāvetvā pacchā sotāpattiniyāmaṃ okkamati",
  Cl(f"{PUBBE} {MG['sotāpatti']}ကို ပွားများ၍ နောက်မှ သောတာပတ္တိ {NIYAMA}သို့", *OKK))
P("pubbe sakadāgāmi", FR(f"{PUBBE} သကဒါဂါမိ"))
P("anāgāmi", FR("အနာဂါမိ"))
P("arahattamaggaṃ bhāvetvā pacchā arahattaniyāmaṃ okkamati",
  Cl(f"{MG['arahatta']}ကို ပွားများ၍ နောက်မှ ရဟန္တာ {NIYAMA}သို့", *OKK))
P("pubbe satipaṭṭhānaṃ", FR(f"{PUBBE} {SATIP}"))
for _k, _m in (("iddhipādaṃ", ID), ("indriyaṃ", INDRIYA), ("balaṃ", BALA)):
    P(_k, FR(_m))
P("bojjhaṅgaṃ bhāvetvā pacchā niyāmaṃ okkamati", Cl(f"{BJW}ကို ပွားများ၍ နောက်မှ {NIYAMA}သို့", *OKK))
P("bhabbo bodhisatto tāya jātiyā dhammaṃ nābhisametuṃ",
  Cl(f"{BS}သည် ထိုဘဝ၌ တရားကို ထိုးထွင်း မသိဘဲ", "ရှိနိုင်", "ရှိ၍ မဖြစ်နိုင်"))

# ===================================================================================== 130. Nivutakathā / 131. Sammukhībhūtakathā
NIVUTO = new("nivuto", "အတားအဆီး ဖုံးလွှမ်းထားသူ")
NIVARANA = W("1", "^1-1158", "Cha nīvaraṇā", "အတားအဆီး")
section("(130) 5. Nivutakathā", f"(130) 5. {NIVUTO}အကြောင်း {KATHA}")
section("Nivutakathā", f"{NIVUTO}အကြောင်း {KATHA}")
P("nivuto nīvaraṇaṃ jahati", VV(f"{NIVUTO}သည် {NIVARANA}ကို", JAHATI))
SAMMUKHI = new("sammukhībhūto", "နှောင်ကြိုးနှင့် မျက်နှာချင်းဆိုင် ဖြစ်နေသူ")
section("(131) 6. Sammukhībhūtakathā", f"(131) 6. {SAMMUKHI}အကြောင်း {KATHA}")
section("Sammukhībhūtakathā", f"{SAMMUKHI}အကြောင်း {KATHA}")
P("sammukhībhūto saṃyojanaṃ jahati", VV(f"{SAMMUKHI}သည် နှောင်ကြိုးကို", JAHATI))
P("ratto rāgaṃ jahati, duṭṭho dosaṃ jahati, mūḷho mohaṃ jahati, kiliṭṭho kilese jahati",
  VV(f"တပ်မက်နေသူသည် ရာဂကို {JAHATI}၍ ဒေါသ ဖြစ်နေသူသည် ဒေါသကို {JAHATI}၍ တွေဝေနေသူသည် မောဟကို {JAHATI}၍ "
     "ညစ်နွမ်းနေသူသည် ကိလေသာတို့ကို", JAHATI))
P("rāgena rāgaṃ jahati, dosena dosaṃ jahati, mohena mohaṃ jahati, kilesehi kilese jahati",
  VV(f"ရာဂဖြင့် ရာဂကို {JAHATI}၍ ဒေါသဖြင့် ဒေါသကို {JAHATI}၍ မောဟဖြင့် မောဟကို {JAHATI}၍ ကိလေသာတို့ဖြင့် "
     "ကိလေသာတို့ကို", JAHATI))
P("rāgo cittasampayutto, maggo cittasampayutto", V(f"ရာဂသည် {SAMP} {THING} ဖြစ်၍ မဂ်သည် {SAMP} {THING}"))
P("rāgo akusalo, maggo kusalo", V(f"ရာဂသည် {AKUSALA} ဖြစ်၍ မဂ်သည် {KUSALA}"))
_R = "ရဟန်းတို့၊"
Q("cattārimāni, bhikkhave, suvidūravidūrāni! Katamāni cattāri? Nabhañca, bhikkhave, pathavī ca – idaṃ paṭhamaṃ "
  "suvidūravidūraṃ…pe… tasmā sataṃ dhammo asabbhi ārakā",
  f"{_R} အလွန် ဝေးကွာသော ဤအရာ {F.NUM_MY[4]}{F.CL}တို့ ရှိကုန်၏။ အဘယ် {F.NUM_MY[4]}{F.CL}တို့နည်း။ {_R} ကောင်းကင်နှင့် "
  "မြေ – ဤသည်ကား ပထမ အလွန် ဝေးကွာသော အရာ ဖြစ်၏… ထို့ကြောင့် သူတော်ကောင်းတို့၏ တရားသည် သူယုတ်မာတို့မှ ဝေးကွာ၏")

# ===================================================================================== 132. Samāpanno assādetikathā
SAMAP = P6.SAMAP                                                      # samāpanno «သမာပတ်ကို ဝင်စားနေသူ»
NIK = W("1", "^1-1065", "nikanti", "စွဲလန်းခြင်း")
JN = new("jhānanikanti", f"{P6.JH}ကို {NIK}")
section("(132) 7. Samāpanno assādetikathā", f"(132) 7. {SAMAP} သာယာသည်ဟူသော {KATHA}")
section("Samāpanno assādetikathā", f"{SAMAP} သာယာသည်ဟူသော {KATHA}")
P("samāpanno assādeti, jhānanikanti jhānārammaṇā",
  V(f"{SAMAP}သည် သာယာ၍ {JN}သည် {P6.JH}ကို အာရုံပြုသော {THING}"))
P("taṃ jhānaṃ tassa jhānassa ārammaṇaṃ", V(f"ထို{P6.JH}သည် ထို{P6.JH}၏ အာရုံ"))
_SELF = [("tena phassena taṃ phassaṃ phusati", "တွေ့ထိမှု", "တွေ့ထိ"), ("tāya vedanāya taṃ vedanaṃ vedeti", "ခံစားမှု", "ခံစား"),
         ("tāya saññāya taṃ saññaṃ sañjānāti", "မှတ်သိမှု", "မှတ်သိ"),
         ("tāya cetanāya taṃ cetanaṃ ceteti", "စေ့ဆော်မှု", "စေ့ဆော်"), ("tena cittena taṃ cittaṃ cinteti", "စိတ်", "ကြံ"),
         ("tena vitakkena taṃ vitakkaṃ vitakketi", "စတင်ကြံစည်မှု", "စတင်ကြံစည်"),
         ("tena vicārena taṃ vicāraṃ vicāreti", "ဆက်လက်သုံးသပ်မှု", "ဆက်လက်သုံးသပ်"),
         ("tāya pītiyā taṃ pīti piyāyati", "ပီတိ", "နှစ်သက်"), ("tāya satiyā taṃ satiṃ sarati", "သတိ", "အောက်မေ့"),
         ("tāya paññāya taṃ paññaṃ pajānāti", "ပညာ", "သိ")]
P(", ".join(x[0] for x in _SELF),
  VV(" ".join(f"ထို{n}ဖြင့် ထို{n}ကို {v}၍" for _, n, v in _SELF[:-1]) + f" ထို{_SELF[-1][1]}ဖြင့် ထို{_SELF[-1][1]}ကို",
     _SELF[-1][2]))
P("jhānanikanti cittasampayuttā, jhānaṃ cittasampayuttaṃ", V(f"{JN}သည် {SAMP} {THING} ဖြစ်၍ {P6.JH}သည် {SAMP} {THING}"))
P("jhānanikanti akusalaṃ, jhānaṃ kusalaṃ", V(f"{JN}သည် {AKUSALA} ဖြစ်၍ {P6.JH}သည် {KUSALA}"))
_VIV = W("1", "^1-160", "vivicceva kāmehi vivicca akusalehi dhammehi",
         "ကာမတို့မှ ကင်းဆိတ်၍သာ၊ အကုသိုလ် သဘောတရားတို့မှ ကင်းဆိတ်၍")
_VUP = W("1", "^1-161", "vitakkavicārānaṃ vūpasamā", "စတင်ကြံစည်မှုနှင့် ဆက်လက်သုံးသပ်မှုတို့ ငြိမ်းသွားခြင်းကြောင့်")
_ASS = "ထိုသူသည် ထိုဈာန်ကို သာယာ၏၊ ထိုဈာန်ကို နှစ်သက်တောင့်တ၏၊ ထိုဈာန်ဖြင့်လည်း နှစ်သိမ့်မှုသို့ ရောက်၏"
Q("idha, bhikkhave, bhikkhu vivicceva kāmehi vivicca akusalehi dhammehi paṭhamaṃ jhānaṃ upasampajja viharati, so taṃ "
  "assādeti taṃ nikāmeti tena ca vittiṃ āpajjati; vitakkavicārānaṃ vūpasamā…pe… dutiyaṃ jhānaṃ…pe… tatiyaṃ "
  "jhānaṃ…pe… catutthaṃ jhānaṃ upasampajja viharati, so taṃ assādeti taṃ nikāmeti tena ca vittiṃ āpajjati",
  f"{_R} ဤသာသနာ၌ ရဟန်းသည် {_VIV} ပထမ ဈာန်ကို ဝင်စား၍ နေ၏၊ {_ASS}၊ {_VUP}… ဒုတိယ ဈာန်ကို… တတိယ ဈာန်ကို… "
  f"စတုတ္ထ ဈာန်ကို ဝင်စား၍ နေ၏၊ {_ASS}")
new("so taṃ assādeti taṃ nikāmeti tena ca vittiṃ āpajjati", _ASS)

# ===================================================================================== 133. Asātarāgakathā
ASATA = new("asātarāgo", "မသာယာဖွယ်ကို တပ်မက်မှု")
section("(133) 8. Asātarāgakathā", f"(133) 8. {ASATA}အကြောင်း {KATHA}")
section("Asātarāgakathā", f"{ASATA}အကြောင်း {KATHA}")
P("atthi asātarāgo", V(ASATA, EXIST))
for _k, _m in (("dukkh", "ဒုက္ခ"), ("sukh", "သုခ")):
    _p = (f"{_k}ābhinandino sattā, atthi keci {_k}aṃ patthenti pihenti esanti gavesanti pariyesanti, {_k}aṃ ajjhosāya "
          "tiṭṭhanti")
    P(_p, V(f"{F.SATTA}တို့သည် {_m}ကို နှစ်သက်ကြ၍ {_m}ကို တောင့်တကြ၊ အားကျ လိုချင်ကြ၊ ရှာကြ၊ ရှာဖွေကြ၊ စုံစမ်းရှာဖွေကြပြီး "
            f"{_m}ကို စွဲလမ်း၍ နေကြသော အချို့သူတို့", EXIST))
VD = {"dukkhāya": W("1", "^1-M1-2", "dukkhāya vedanāya sampayuttā", "နာကျင်သော ခံစားမှု"),
      "sukhāya": "သာယာသော ခံစားမှု"}
W("1", "^1-M1-2", "sukhāya vedanāya sampayuttā", VD["sukhāya"])
RAGAN = "ရာဂ ကိန်းအောင်းခြင်း"                                        # rāgānusaya (pi-2 ^2-816 «ကာမရာဂ ကိန်းအောင်းခြင်း»)
PATIGHAN = W("2", "^2-816", "paṭighānusayo", "မုန်းတီးမှု ကိန်းအောင်းခြင်း")
for _a, _b in (("dukkhāya", "sukhāya"), ("sukhāya", "dukkhāya")):
    P(f"{_a} vedanāya rāgānusayo anuseti, {_b} vedanāya paṭighānusayo anuseti",
      VV(f"{VD[_a]}၌ {RAGAN} ကိန်းအောင်း၍ {VD[_b]}၌ {PATIGHAN}", "ကိန်းအောင်း"))
ADUKKHA = W("1", "^1-M1-2", "adukkhamasukhāya vedanāya sampayuttā", "မနာကျင် မသာယာသော")
Q("so evaṃ anurodhavirodhaṃ samāpanno yaṃ kiñci vedanaṃ vedayati sukhaṃ vā dukkhaṃ vā adukkhamasukhaṃ vā, so taṃ "
  "vedanaṃ abhinandati abhivadati ajjhosāya tiṭṭhati",
  "ထိုသူသည် ဤသို့ လိုက်လျောခြင်း ဆန့်ကျင်ခြင်းသို့ ရောက်လျက် သာယာသော ခံစားမှုဖြစ်စေ၊ နာကျင်သော ခံစားမှုဖြစ်စေ၊ "
  f"{ADUKKHA} ခံစားမှုဖြစ်စေ အကြင် ခံစားမှုကို ခံစား၏၊ ထိုသူသည် ထိုခံစားမှုကို အလွန် နှစ်သက်၏၊ ချီးမွမ်း၏၊ "
  "စွဲလမ်း၍ နေ၏")
W("1", "^1-1065", "anurodho", "လိုက်လျောခြင်း")
BR_X["[ma. ni. 3.409 mahātaṇhāsaṅkhaye]"] = f"[{F.REF['ma. ni.']} 3.409 မဟာတဏှာသင်္ခယ သုတ်၌]"

# ===================================================================================== 134. / 135. Dhammataṇhā
DT = TN["dhamma"]
section("(134) 9. Dhammataṇhā abyākatātikathā", f"(134) 9. {DT}သည် {ABY} {THING} ဖြစ်သည်ဟူသော {KATHA}")
section("Dhammataṇhā abyākatātikathā", f"{DT}သည် {ABY} {THING} ဖြစ်သည်ဟူသော {KATHA}")
section("(135) 10. Dhammataṇhā na dukkhasamudayotikathā", f"(135) 10. {DT}သည် {DUKKHASAM} မဟုတ်ဟူသော {KATHA}")
section("Dhammataṇhā na dukkhasamudayotikathā", f"{DT}သည် {DUKKHASAM} မဟုတ်ဟူသော {KATHA}")
for _k, _m in TN.items():
    P(f"{_k}taṇhā", FR(_m))
    P(f"{_k}taṇhā abyākatā", V(f"{_m}သည် {ABY} {THING}"))
    P(f"{_k}taṇhā akusalā", V(f"{_m}သည် {AKUSALA}"))
    P(f"{_k}taṇhā lobho abyākato", V(f"{_m} ဟူသော {LOBHA}သည် {ABY} {THING}"))
    P(f"{_k}taṇhā lobho akusalo", V(f"{_m} ဟူသော {LOBHA}သည် {AKUSALA}"))
    P(f"{_k}taṇhā dukkhasamudayo", V(f"{_m}သည် {DUKKHASAM}"))
    P(f"{_k}taṇhā na dukkhasamudayo", V(f"{_m}သည် {DUKKHASAM}", neg=True))
    P(f"{_k}taṇhā lobho dukkhasamudayo", V(f"{_m} ဟူသော {LOBHA}သည် {DUKKHASAM}"))
    P(f"{_k}taṇhā lobho, na dukkhasamudayo", V(f"{_m}သည် {LOBHA} ဖြစ်၍ {DUKKHASAM}", neg=True))
for _k in ("sadda", "gandha", "rasa"):
    P(f"{_k}taṇhā", FR(TN[_k]))
P("taṇhā akusalā vuttā bhagavatā", Cl(f"{TANHA}ကို {AKUSALA}ဟု {BUDDHA}", *SAID))
P("taṇhā dukkhasamudayo vutto bhagavatā", Cl(f"{TANHA}ကို {DUKKHASAM}ဟု {BUDDHA}", *SAID))
for _p, _m in (("akusalo", AKUSALA), ("dukkhasamudayo", DUKKHASAM)):
    P(f"lobho {_p} vutto bhagavatā, dhammataṇhā lobho", V(f"{LOBHA}ကို {_m}ဟု {BUDDHA} ဟောတော်မူ၍ {DT}သည် {LOBHA}"))
P("sā dhammataṇhā", V(f"ထို{TANHA}သည် {DT}"))
_203 = F.novar(F.strip_id(F.FINAL.seg("2", "^2-203")[2][0]))
_203 = _203[_203.index("ဘဝသစ်ကို ဖြစ်စေတတ်သော"):]
_203 = _203[:_203.index("။")]
assert _203.startswith("ဘဝသစ်ကို ဖြစ်စေတတ်သော၊ ") and _203.endswith("ဘဝ ပျောက်ကွယ်ခြင်းကို တပ်မက်မှု"), _203
Q("yāyaṃ taṇhā ponobbhavikā nandīrāgasahagatā tatratatrābhinandinī, seyyathidaṃ – kāmataṇhā, bhavataṇhā, vibhavataṇhā",
  _203)
F.WITNESS.setdefault("yāyaṃ taṇhā ponobbhavikā … vibhavataṇhā", ("2", "^2-203", _203))
BR_X["[mahāva. 14; dī. ni. 2.400]"] = f"[“မဟာဝဂ်” 14၊ {F.REF['dī. ni.']} 2.400]"
LINES_X[key("Kappaṭṭho kappaṃ tiṭṭheyya, kappaṭṭho kusalaṃ cittaṃ na paṭilabheyya, anantarāpayutto puggalo "
            "sammattaniyāmaṃ okkameyya, niyato niyāmaṃ okkamati, nivuto nīvaraṇaṃ jahati, sammukhībhūto saṃyojanaṃ "
            "jahati, jhānanikanti, asātarāgo, dhammataṇhā abyākatā, dhammataṇhā na dukkhasamudayoti.")] = (
    f"{KT}သည် {KAPPA} ပတ်လုံး တည်ခြင်း၊ {KT}သည် {KUSALA} {CITTA}ကို မရခြင်း၊ {ANP}သည် {SNM}သို့ "
    f"{OKK[0]}ခြင်း၊ {NIYATO}သည် {NIYAMA}သို့ {OKK[0]}ခြင်း၊ {NIVUTO}သည် {NIVARANA}ကို {JAHATI}ခြင်း၊ {SAMMUKHI}သည် "
    f"နှောင်ကြိုးကို {JAHATI}ခြင်း၊ {JN}၊ {ASATA}၊ {DT}သည် {ABY} {THING} ဖြစ်ခြင်း၊ {DT}သည် {DUKKHASAM} "
    f"မဟုတ်ခြင်း{END}")


# ===================================================================================== 136. Kusalākusalapaṭisandahanakathā
section("(136) 1. Kusalākusalapaṭisandahanakathā", f"(136) 1. {KUSALA} {AKUSALA} ဆက်စပ်ခြင်းအကြောင်း {KATHA}")
section("Kusalākusalapaṭisandahanakathā", f"{KUSALA} {AKUSALA} ဆက်စပ်ခြင်းအကြောင်း {KATHA}")
KM = W("2", "^2-834", "akusalamūlāni", "အကုသိုလ်၏ အမြစ်")[len("အ"):]                     # kusalamūla «ကုသိုလ်၏ အမြစ်»
AKM = f"{AKUSALA}၏ အမြစ်"
LINK = ("ဆက်စပ်", "မဆက်စပ်")
for _a, _am, _b, _bm in (("akusala", AKM, "kusala", KM), ("kusala", KM, "akusala", AKM)):
    P(f"{_a}mūlaṃ paṭisandahati {_b}mūlaṃ", Cl(f"{_am}သည် {_bm}နှင့်", *LINK))
P("akusalamūlaṃ paṭisandahati kusalamūlaṃ, kusalamūlaṃ paṭisandahati akusalamūlaṃ",
  Cl(f"{AKM}သည် {KM}နှင့် ဆက်စပ်၍ {KM}သည် {AKM}နှင့်", *LINK))
AVT = W("2", "^2-766", "āvaṭṭanā vā", "စိတ်ကို လှည့်ဆောင်ခြင်း")                         # āvaṭṭanā
PANIDHI = new("paṇidhi", "စိတ်ကို ထားရှိခြင်း")
VIN = {"cakkhu": "မျက်စိ", "sota": "နား", "ghāna": "နှာခေါင်း", "jivhā": "လျှာ", "kāya": "ကိုယ်"}
VINN = {k: f"{v} သိစိတ်" for k, v in VIN.items()}                                          # cakkhuviññāṇa …
W("1", "^1-433", "cakkhuviññāṇadhātu", "မျက်စိ သိစိတ် ဓာတ်")
SUBJ_U = {"kusalassa": KUSALA, "akusalassa": AKUSALA}
SUBJ_U.update({f"{k}viññāṇassa": v for k, v in VINN.items()})
for _a, _b in (("akusalassa", "kusalassa"), ("kusalassa", "akusalassa"), ("cakkhuviññāṇassa", "sotaviññāṇassa"),
               ("jivhāviññāṇassa", "kāyaviññāṇassa")):
    P(f"yā {_a} uppādāya āvaṭṭanā…pe… paṇidhi, sāva {_b} uppādāya āvaṭṭanā…pe… paṇidhi",
      V(f"{SUBJ_U[_a]} ဖြစ်ပေါ်ရန် {AVT}… {PANIDHI} ဟူသမျှသည်ပင် {SUBJ_U[_b]} ဖြစ်ပေါ်ရန် {AVT}… {PANIDHI}"))
ARISE = ("ဖြစ်ပေါ်", "မဖြစ်ပေါ်")
SUBJ_N = {"kusalaṃ": KUSALA, "akusalaṃ": AKUSALA, "akusalamūlaṃ": AKM, "kusalamūlaṃ": KM}
SUBJ_N.update({f"{k}viññāṇaṃ": v for k, v in VINN.items()})
for _s, _sm in SUBJ_N.items():
    P(f"{_s} anāvaṭṭentassa uppajjati", Cl(f"{_sm}သည် စိတ်ကို မလှည့်ဆောင်သူအား", *ARISE))
    P(f"{_s} āvaṭṭentassa uppajjati", Cl(f"{_sm}သည် စိတ်ကို လှည့်ဆောင်သူအား", *ARISE))
    P(f"{_s} yoniso manasikaroto uppajjati", Cl(f"{_sm}သည် သင့်လျော်စွာ နှလုံးသွင်းသူအား", *ARISE))
    P(f"{_s} ayoniso manasikaroto uppajjati", Cl(f"{_sm}သည် မသင့်လျော်စွာ နှလုံးသွင်းသူအား", *ARISE))
P("appaṇidahantassa uppajjati", Cl("စိတ်ကို မထားရှိသူအား", *ARISE))
P("paṇidahantassa uppajjati", Cl("စိတ်ကို ထားရှိသူအား", *ARISE))
ANCHOR_X["anāvaṭṭentassa"] = "မလှည့်ဆောင်သူအား"
VAR_X.update({"anāvaṭṭantassa": F.LEKHANA, "anāvajjantassa": F.PATHA})
new("yoniso / ayoniso manasikaroto", "သင့်လျော်စွာ / မသင့်လျော်စွာ နှလုံးသွင်းသူအား")
SN = {"kāma": W("2", "^2-911", "Kāmasaññā", "ကာမကို မှတ်သိမှု"),
      "byāpāda": W("2", "^2-911", "byāpādasaññā", "ဖျက်ဆီးလိုစိတ်ဆိုင်ရာ မှတ်သိမှု"),
      "vihiṃsā": W("2", "^2-911", "vihiṃsāsaññā", "ညှဉ်းပန်းမှုဆိုင်ရာ မှတ်သိမှု"),
      "nekkhamma": "ကာမမှ ထွက်မြောက်ခြင်းဆိုင်ရာ မှတ်သိမှု", "abyāpāda": "မဖျက်ဆီးလိုခြင်းဆိုင်ရာ မှတ်သိမှု",
      "avihiṃsā": "မညှဉ်းပန်းခြင်းဆိုင်ရာ မှတ်သိမှု"}
new("nekkhamma- / abyāpāda- / avihiṃsāsaññā", f"{SN['nekkhamma']} / {SN['abyāpāda']} / {SN['avihiṃsā']}")
_BY = W("1", "^1-1158", "byāpādanīvaraṇaṃ", "ဖျက်ဆီးလိုစိတ်")
_VH = W("2", "^2-912", "vihiṃsādhātu", "ညှဉ်းပန်းမှု")
_MK = dict(zip(("mettā", "karuṇā", "muditā", "upekkhā"), W("2", "^2-683", "mettā, karuṇā, muditā, upekkhā",
                                                            "မေတ္တာ၊ ကရုဏာ၊ မုဒိတာ၊ ဥပေက္ခာ").split("၊ ")))
ARATI = new("arati", "မမွေ့လျော်မှု")
NEXT = "၏ ချက်ချင်း နောက်၌"                                           # X-assa anantarā
new("X-assa anantarā", f"X{NEXT}")
_P1 = [(SN["kāma"], SN["nekkhamma"]), (SN["byāpāda"], SN["abyāpāda"]), (SN["vihiṃsā"], SN["avihiṃsā"]),
       (_BY, _MK["mettā"]), (_VH, _MK["karuṇā"]), (ARATI, _MK["muditā"]), (PATIGHAN.split()[0], _MK["upekkhā"])]
P("kāmasaññāya anantarā nekkhammasaññā uppajjati, byāpādasaññāya anantarā abyāpādasaññā uppajjati, vihiṃsāsaññāya "
  "anantarā avihiṃsāsaññā uppajjati, byāpādassa anantarā mettā uppajjati, vihiṃsāya anantarā karuṇā uppajjati, "
  "aratiyā anantarā muditā uppajjati, paṭighassa anantarā upekkhā uppajjati",
  Cl(" ".join(f"{a}{NEXT} {b} ဖြစ်ပေါ်၍" for a, b in _P1[:-1]) + f" {_P1[-1][0]}{NEXT} {_P1[-1][1]}", *ARISE))
P("nekkhammasaññāya anantarā kāmasaññā uppajjati, abyāpādasaññāya anantarā byāpādasaññā uppajjati, "
  "avihiṃsāsaññāya anantarā vihiṃsāsaññā uppajjati, mettāya anantarā byāpādo uppajjati, karuṇāya anantarā vihiṃsā "
  "uppajjati, muditāya anantarā arati uppajjati, upekkhāya anantarā paṭighaṃ uppajjati",
  Cl(" ".join(f"{b}{NEXT} {a} ဖြစ်ပေါ်၍" for a, b in _P1[:-1]) + f" {_P1[-1][1]}{NEXT} {_P1[-1][0]}", *ARISE))
for _y in ("yasmiṃyeva", "yasmiññeva"):
    P(f"{_y} vatthusmiṃ rajjati tasmiññeva vatthusmiṃ virajjati, {_y} vatthusmiṃ virajjati tasmiññeva vatthusmiṃ "
      "rajjati", Cl("အကြင် အရာဝတ္ထု၌ပင် တပ်မက်လျှင် ထိုအရာဝတ္ထု၌ပင် တပ်မက်မှု ကင်း၍ အကြင် အရာဝတ္ထု၌ပင် "
                     "တပ်မက်မှု ကင်းလျှင် ထိုအရာဝတ္ထု၌ပင်", "တပ်မက်", "မတပ်မက်"))


@F.frame(r"(?P<p>[^–]+?), na vattabbaṃ – (?P<q>.+?)ti\?")
def _f_p_navatt(m):
    """P, na vattabbaṃ – "Q"ti? = «P-သည်၊ ဤသို့ မဆိုသင့်သလော – “Q”» (^5-686 …)."""
    return f"{F.pq(m['p'], 'stmt')}{C} ဤသို့ မဆိုသင့်သလော – “{F.pq(m['q'], 'stmt', 1)}”{END}"


before_generic()

# ===================================================================================== 137. Saḷāyatanuppattikathā
SALAY = W("1", "^1-1343", "nāmarūpapaccayā saḷāyatanaṃ", "အာရုံခံ နယ်ပယ် ခြောက်ပါး")
section("(137) 2. Saḷāyatanuppattikathā", f"(137) 2. {SALAY} ဖြစ်ပေါ်ခြင်းအကြောင်း {KATHA}")
section("Saḷāyatanuppattikathā", f"{SALAY} ဖြစ်ပေါ်ခြင်းအကြောင်း {KATHA}")
WOMB = "အမိဝမ်း"
P("saḷāyatanaṃ apubbaṃ acarimaṃ mātukucchismiṃ saṇṭhāti",
  Cl(f"{SALAY}သည် ရှေ့ မကျ နောက် မကျ {WOMB}၌ တစ်ပြိုင်နက်", "တည်", "မတည်"))
_SAB = W("2", "^2-951", "sabbaṅgapaccaṅgī ahīnindriyo",
         "ကြီးငယ် အင်္ဂါ အားလုံး ပြည့်စုံသော၊ မချို့ယွင်းသော အာရုံခံ စွမ်းရည် ရှိသော")
P("sabbaṅgapaccaṅgī ahīnindriyo mātukucchismiṃ okkamati",
  Cl(f"ကြီးငယ် အင်္ဂါ အားလုံး ပြည့်စုံ၍ မချို့ယွင်းသော အာရုံခံ စွမ်းရည် ရှိသူ ဖြစ်လျက် {WOMB}သို့", *OKK))
UPS = "ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော"                                # upapattesiya (ch11-12 «… စိတ်»)
UPC = f"{UPS} {CITTA}ဖြင့်"
P("upapattesiyena cittena cakkhāyatanaṃ saṇṭhāti", Cl(f"{UPC} {AY_N['cakkh']}", "တည်", "မတည်"))
P("upapattesiyena cittena sotāyatanaṃ…pe… ghānāyatanaṃ…pe… jivhāyatanaṃ saṇṭhāti",
  Cl(f"{UPC} {AY_N['sot']}… {AY_N['ghān']}… {AY_N['jivh']}", "တည်", "မတည်"))
_BODY = [("hatthā saṇṭhanti", "လက်တို့"), ("pādā saṇṭhanti", "ခြေတို့"), ("sīsaṃ saṇṭhāti", "ဦးခေါင်း"),
         ("kaṇṇo saṇṭhāti", "နား"), ("nāsikā saṇṭhāti", "နှာခေါင်း"), ("mukhaṃ saṇṭhāti", "ပါးစပ်"),
         ("dantā saṇṭhanti", "သွားတို့")]
P("upapattesiyena cittena " + ", ".join(x for x, _ in _BODY),
  Cl(f"{UPC} " + " ".join(f"{m} တည်၍" for _, m in _BODY[:-1]) + f" {_BODY[-1][1]}", "တည်", "မတည်"))
MKG = "အမိဝမ်း၌ ရောက်ပြီးသူ၏ နောက်မှ"                                  # mātukucchigatassa pacchā
P("mātukucchigatassa pacchā cakkhāyatanaṃ uppajjati", Cl(f"{MKG} {AY_N['cakkh']}", *ARISE))
P("mātukucchigatassa pacchā sotāyatanaṃ…pe… ghānāyatanaṃ…pe… jivhāyatanaṃ uppajjati",
  Cl(f"{MKG} {AY_N['sot']}… {AY_N['ghān']}… {AY_N['jivh']}", *ARISE))
_KL = [W("2", "^2-173", "kesā lomā nakhā dantā", x) for x in ("ဆံပင်", "မွေးညင်း", "ခြေသည်းလက်သည်း", "သွား")]
_AT = W("2", "^2-173", "aṭṭhi aṭṭhimiñjaṃ", "အရိုး")
P("mātukucchigatassa pacchā kesā lomā nakhā dantā aṭṭhī uppajjanti",
  Cl(f"{MKG} {'၊ '.join(_KL)}၊ {_AT}တို့", "ဖြစ်ပေါ်ကြ", "မဖြစ်ပေါ်ကြ"))
for _k, _m in (("cakkhu", "မျက်စိ"), ("jivhā", "လျှာ"), ("aṭṭhi", _AT)):
    P(f"mātukucchismiṃ {_k}paṭilābhāya kammaṃ karoti", Cl(f"{WOMB}၌ {_m} ရရှိရန် {F.KAMMA}ကို", "ပြု", "မပြု"))
for _p, _m in (('"Paṭhamaṃ kalalaṃ hoti, kalalā hoti abbudaṃ;', "“ပထမ အရည်ကြည် ဖြစ်၏၊ အရည်ကြည်မှ အမြှုပ် ဖြစ်၏၊"),
               ("Abbudā jāyate pesi [pesī (syā. kaṃ. pī.)], pesi nibbattate [nibbattatī (sī. syā., saṃ. ni. 1.235), "
                "nibbattati (pī. ka.)] ghano;", "အမြှုပ်မှ အသားစ ⟦0⟧ ဖြစ်ပေါ်၏၊ အသားစမှ အခဲ ဖြစ်လာ၏ ⟦1⟧၊"),
               ("Ghanā pasākhā jāyanti, kesā lomā nakhāpi ca.",
                f"အခဲမှ အကိုင်းအခက်တို့ ဖြစ်ပေါ်ကြ၏၊ {_KL[0]}၊ {_KL[1]}၊ {_KL[2]}တို့လည်း ဖြစ်ပေါ်ကြ၏။"),
               ('"Yañcassa bhuñjati mātā, annaṃ pānañca bhojanaṃ;',
                "“ထိုသူ၏ အမိသည် အစာ၊ အဖျော်၊ ဘောဇဉ် ဟူသော အကြင် အရာကို စား၏၊"),
               ('Tena so tattha yāpeti, mātukucchigato naro"ti [saṃ. ni. 1.235].',
                f"ထိုအရာဖြင့် {WOMB}၌ ရောက်နေသော ထိုလူသည် ထို၌ အသက် မွေး၏”ဟူ၍ ⟦0⟧{END}")):
    LINES_X[key(_p)] = _m
VAR_X["pesī"] = F.LEKHANA
BR_X["[nibbattatī (sī. syā., saṃ. ni. 1.235), nibbattati (pī. ka.)]"] = (
    f"[{F.LEKHANA} (Sī., Syā., {F.REF['saṃ. ni.']} 1.235): nibbattatī၊ (Pī., Ka.): nibbattati]")
W("4", "^4-168", "annassa pānassa", "အစာ၊ အဖျော်")

# ===================================================================================== 138. Anantarapaccayakathā
section("(138) 3. Anantarapaccayakathā", f"(138) 3. ချက်ချင်း နောက်၌ ဖြစ်စေသော အကြောင်းအကြောင်း {KATHA}")
section("Anantarapaccayakathā", f"ချက်ချင်း နောက်၌ ဖြစ်စေသော အကြောင်းအကြောင်း {KATHA}")
_ORDV = ["cakkhu", "sota", "ghāna", "jivhā", "kāya"]
for _a, _b in zip(_ORDV, _ORDV[1:]):
    P(f"{_a}viññāṇassa anantarā {_b}viññāṇaṃ uppajjati", Cl(f"{VINN[_a]}{NEXT} {VINN[_b]}", *ARISE))
for _s in ("cakkhu", "sota", "jivhā", "kāya"):
    for _o, _om in (("rūpa", TAN["rūpa"]), ("rasa", TAN["rasa"])):
        P(f"{_s}viññāṇaṃ {_o}nimittaṃ manasikaroto uppajjati",
          Cl(f"{VINN[_s]}သည် {_om}၏ {F.NIMITTA}ကို နှလုံးသွင်းသူအား", *ARISE))
        P(f"{_s}viññāṇaṃ {_o[:-1]}ārammaṇaññeva na aññārammaṇaṃ",
          Cl(f"{VINN[_s]}သည် {_om}ကိုသာ အာရုံပြု၍ အခြားကို", "အာရုံ မပြု", "အာရုံပြု"))
_PAT2 = {"cakkhu": ("cakkhuñca paṭicca rūpe ca", f"{VIN['cakkhu']}ကိုလည်းကောင်း၊ {TAN['rūpa']}တို့ကိုလည်းကောင်း မှီ၍"),
         "jivhā": ("jivhañca paṭicca rase ca", f"{VIN['jivhā']}ကိုလည်းကောင်း၊ {TAN['rasa']}တို့ကိုလည်းကောင်း မှီ၍")}
W("2", "^2-184", "Cakkhuñca paṭicca rūpe ca", _PAT2["cakkhu"][1])
SUTTA_IS = f"ဤသို့သော {F.SUTTANTA} အမှန်ပင်"
for _s, (_pp, _pm) in _PAT2.items():
    for _v in ("cakkhu", "sota", "jivhā", "kāya"):
        P(f"{_pp} uppajjati {_v}viññāṇaṃ", Cl(f"{_pm} {VINN[_v]}", *ARISE))
        P(f"{_pp} uppajjati {_v}viññāṇanti – attheva suttanto",
          Cl(f"«{_pm} {VINN[_v]} {ARISE[0]}» – {SUTTA_IS}", EXIST, NEXIST))
for _a, _b in (("cakkhu", "sota"), ("jivhā", "kāya")):
    P(f"taññeva {_a}viññāṇaṃ taṃ {_b}viññāṇaṃ", V(f"ထို{VINN[_a]}ပင် ထို{VINN[_b]}"))


@F.frame(r"(?P<p>[^–]+?)ti – attheva suttantoti\?")
def _f_p_attheva(m):
    """"P"ti – attheva suttantoti? = «“P” – ဤသို့သော သုတ္တန် အမှန်ပင် ရှိသလော» (^5-694)."""
    return f"“{F.pq(m['p'], 'stmt', 1)}” – {SUTTA_IS} {EXIST}သလော{END}"


before_generic()
P("pañcaviññāṇā aññamaññassa samanantarā uppajjanti",
  Cl(f"{W('2', '^2-766', 'Pañca viññāṇā', 'သိစိတ် ငါးပါး')}တို့သည် အချင်းချင်း{NEXT}", "ဖြစ်ပေါ်ကြ", "မဖြစ်ပေါ်ကြ"))
_DANCE = ("က၊ သီဆို၊ တီးမှုတ်နေရင်း အဆင်းအရောင်ကိုလည်း မြင်၊ အသံကိုလည်း ကြား၊ အနံ့ကိုလည်း ခံ၊ အရသာကိုလည်း ခံ၊ "
          f"အထိအတွေ့ကိုလည်း ထိသော {MS.KOCI}")
P("atthi koci naccati gāyati vādeti, rūpañca passati, saddañca suṇāti, gandhañca ghāyati, rasañca sāyati, "
  "phoṭṭhabbañca phusati", V(_DANCE, EXIST))
# ^5-693: the quotation «"yā … paṇidhīti» is never closed in the Pāli (source slip): units cut by hand
OPEN_Q_X = {
    'Cakkhuviññāṇassa anantarā sotaviññāṇaṃ uppajjati, na vattabbaṃ – yā cakkhuviññāṇassa uppādāya āvaṭṭanā… '
    'paṇidhi, sāva sotaviññāṇassa uppādāya āvaṭṭanā… paṇidhīti? Āmantā. Sotaviññāṇaṃ anāvaṭṭentassa uppajjati… '
    'appaṇidahantassa uppajjatīti? Na hevaṃ vattabbe…. Nanu sotaviññāṇaṃ āvaṭṭentassa uppajjati… paṇidahantassa '
    'uppajjatīti, āmantā. Hañci sotaviññāṇaṃ āvaṭṭentassa uppajjati… paṇidahantassa uppajjati, no ca vata re '
    'vattabbe – cakkhuviññāṇassa anantarā sotaviññāṇaṃ uppajjatīti.': [
        "Cakkhuviññāṇassa anantarā sotaviññāṇaṃ uppajjati, na vattabbaṃ – yā cakkhuviññāṇassa uppādāya āvaṭṭanā… "
        "paṇidhi, sāva sotaviññāṇassa uppādāya āvaṭṭanā… paṇidhīti?", "Āmantā.",
        "Sotaviññāṇaṃ anāvaṭṭentassa uppajjati… appaṇidahantassa uppajjatīti?", "Na hevaṃ vattabbe….",
        "Nanu sotaviññāṇaṃ āvaṭṭentassa uppajjati… paṇidahantassa uppajjatīti, āmantā.",
        "Hañci sotaviññāṇaṃ āvaṭṭentassa uppajjati… paṇidahantassa uppajjati, no ca vata re vattabbe – "
        "cakkhuviññāṇassa anantarā sotaviññāṇaṃ uppajjatīti."],
}
S("Nanu sotaviññāṇaṃ āvaṭṭentassa uppajjati… paṇidahantassa uppajjatīti, āmantā.",
  f"{VINN['sota']}သည် စိတ်ကို လှည့်ဆောင်သူအား ဖြစ်ပေါ်သလော… စိတ်ကို ထားရှိသူအား ဖြစ်ပေါ်သည် မဟုတ်လော၊ "
  f"{F.YES}{END}")

# ===================================================================================== 139. Ariyarūpakathā
MAHAB = W("1", "^1-584", "Cattāro ca mahābhūtā", "မူလဓာတ်ကြီး")
ARR = new("ariyarūpaṃ", "အရိယာ ရုပ်")
section("(139) 4. Ariyarūpakathā", f"(139) 4. {ARR}အကြောင်း {KATHA}")
section("Ariyarūpakathā", f"{ARR}အကြောင်း {KATHA}")
_UPR = W("1", "^1-584", "catunnañca mahābhūtānaṃ upādāya rūpaṃ", "မူလဓာတ်ကြီး လေးပါးကို မှီ၍ ဖြစ်သော ရုပ်")
P("ariyarūpaṃ mahābhūtānaṃ upādāya", V(f"{ARR}သည် {MAHAB}တို့ကို မှီ၍ ဖြစ်သော {THING}"))
for _s, _sm in (("ariyarūpaṃ", ARR), ("mahābhūtā", f"{MAHAB}တို့")):
    for _e, _m in (("kusal", KUSALA), ("abyākat", f"{ABY} {THING}")):
        P(f"{_s} {_e}aṃ" if _s.endswith("ṃ") else f"{_s} {_e}ā", V(f"{_sm}သည် {_m}"))
_ANAS = ["anāsav", "asaṃyojaniy", "aganthaniy", "anoghaniy", "ayoganiy", "anīvaraṇiy", "aparāmaṭṭh", "anupādāniy",
         "asaṃkilesiy"]
_ANAS_MY = [P6.SAT_W[x + "ā"] for x in _ANAS[:-1]] + [P6.SAT_W["asaṃkilesikā"]]
_SAS_MY = [P11.MAT[k] for k in ("sāsava", "saṃyojaniya", "ganthaniya", "oghaniya", "yoganiya", "nīvaraṇiya",
                                "parāmaṭṭha", "upādāniya", "saṃkilesiya")]
P("ariyarūpaṃ " + " ".join(f"{x}aṃ" for x in _ANAS), V(f"{ARR}သည် {'၊ '.join(_ANAS_MY)} {THING}"))
P("mahābhūtā anāsavā…pe… asaṃkilesiyā", V(f"{MAHAB}တို့သည် {_ANAS_MY[0]}… {_ANAS_MY[-1]} {THING}"))
P("mahābhūtā sāsavā saṃyojaniyā…pe… saṃkilesiyā", V(f"{MAHAB}တို့သည် {_SAS_MY[0]}၊ {_SAS_MY[1]}… {_SAS_MY[-1]} {THING}"))
P("ariyarūpaṃ sāsavaṃ saṃyojaniyaṃ…pe… saṃkilesiyaṃ", V(f"{ARR}သည် {_SAS_MY[0]}၊ {_SAS_MY[1]}… {_SAS_MY[-1]} {THING}"))
Q("yaṃ kiñci, bhikkhave, rūpaṃ cattāri mahābhūtāni catunnañca mahābhūtānaṃ upādāyarūpaṃ",
  f"{_R} ရုပ် ဟူသမျှသည် {MAHAB} {F.NUM_MY[4]}{F.CL}နှင့် {_UPR} ဖြစ်၏")
BR_X["[ma. ni. 1.347; a. ni. 11.15]"] = f"[{F.REF['ma. ni.']} 1.347၊ {F.REF['a. ni.']} 11.15]"

# ===================================================================================== 140. Añño anusayotikathā
section("(140) 5. Añño anusayotikathā", f"(140) 5. {P11.ANUSAYA}သည် တခြား ဖြစ်သည်ဟူသော {KATHA}")
section("Añño anusayotikathā", f"{P11.ANUSAYA}သည် တခြား ဖြစ်သည်ဟူသော {KATHA}")
ANU, PAR = P11.ANUSAYA, P11.PARIYUTTH
_KR = W("2", "^2-816", "kāmarāgānusayo", "ကာမရာဂ ကိန်းအောင်းခြင်း").split()[0]
KIL7 = {  # stem: (Burmese, «añño X» form, «sveva X» form)
    "kāmarāga": (_KR, "añño kāmarāgo", "sveva kāmarāgo"), "paṭigha": (PATIGHAN.split()[0], "aññaṃ paṭighaṃ",
                                                                     "taññeva paṭighaṃ"),
    "māna": ("မာန", "añño māno", "sveva māno"), "diṭṭhi": (P11.DITTHI, "aññā diṭṭhi", "sāva diṭṭhi"),
    "vicikicchā": (P11.VICI, "aññā vicikicchā", "sāva vicikicchā"),
    "bhavarāga": ("ဘဝရာဂ", "añño bhavarāgo", "sveva bhavarāgo"),
    "avijjā": (W("2", "^2-816", "avijjānusayo", "အမှန်ကို မသိမှု"), "aññā avijjā", "sāva avijjā")}
W("2", "^2-816", "bhavarāgānusayo", "ဘဝရာဂ ကိန်းအောင်းခြင်း")
W("2", "^2-816", "mānānusayo", "မာန ကိန်းအောင်းခြင်း")
for _k, (_m, _an, _sv) in KIL7.items():
    _anu = {"diṭṭhi": "diṭṭhānusayo"}.get(_k, _k[:-1] + "ānusayo")
    _par = f"{_k}pariyuṭṭhānaṃ"
    P(f"añño {_anu} aññaṃ {_par}", V(f"{_m} {ANU}နှင့် {_m} {PAR}သည် {F.OTHER}"))
    P(f"{_an} aññaṃ {_par}", V(f"{_m}နှင့် {_m} {PAR}သည် {F.OTHER}"))
    P(f"{_sv} taṃ {_par}", V(f"ထို{_m}ပင် ထို{_m} {PAR}"))
    P(f"sveva {_anu} taṃ {_par}", V(f"ထို{_m} {ANU}ပင် ထို{_m} {PAR}"))
P("añño anusayo aññaṃ pariyuṭṭhānaṃ", V(f"{ANU}နှင့် {PAR}သည် {F.OTHER}"))
P("añño rāgo aññaṃ pariyuṭṭhānaṃ", V(f"ရာဂနှင့် {PAR}သည် {F.OTHER}"))
SAY_V = ("ဆိုသင့်", "မဆိုသင့်")
_KBC = f"{KUSALA} {CITTA} သို့မဟုတ် {ABY} {CITTA} ဖြစ်နေစဉ်"           # kusalābyākate citte vattamāne
for _k, _m in (("sānusayo", f"{ANU} ရှိသူ"), ("sarāgo", "ရာဂ ရှိသူ")):
    P(f"puthujjano kusalābyākate citte vattamāne {_k}ti vattabbo", Cl(f"{PUTHU}ကို {_KBC} «{_m}»ဟု", *SAY_V))
P("pariyuṭṭhitoti vattabbo", Cl(f"«{PAR} ရှိသူ»ဟု", *SAY_V))

# ===================================================================================== 141. Pariyuṭṭhānaṃ cittavippayuttantikathā
VIPP_C = W("1", "^1-M2-58", "cittavippayuttā", "စိတ်နှင့် ကင်းကွာသော")
section("(141) 6. Pariyuṭṭhānaṃ cittavippayuttantikathā", f"(141) 6. {PAR}သည် {VIPP_C} {THING} ဖြစ်သည်ဟူသော {KATHA}")
section("Pariyuṭṭhānaṃ cittavippayuttantikathā", f"{PAR}သည် {VIPP_C} {THING} ဖြစ်သည်ဟူသော {KATHA}")
P("pariyuṭṭhānaṃ cittavippayuttaṃ", V(f"{PAR}သည် {VIPP_C} {THING}"))
SKC = W("1", "^1-M1-5", "saṃkiliṭṭhasaṃkilesikā dhammā", "ကိလေသာဖြင့် ညစ်နွမ်း") + "သော"
_SCT = (f"{P11.SA['sarāgaṃ']} {CITTA}၊ {P11.SA['sadosaṃ']} {CITTA}၊ {P11.SA['samohaṃ']} {CITTA}… {AKUSALA} {CITTA}၊ "
        f"{SKC} {CITTA}")
for _n, _neg in (("", False), ("n", True)):
    P(f"{_n}atthi sarāgaṃ cittaṃ sadosaṃ cittaṃ samohaṃ cittaṃ…pe… akusalaṃ cittaṃ saṃkiliṭṭhaṃ cittaṃ",
      V(_SCT, EXIST, neg=_neg))

# ===================================================================================== 142. Pariyāpannakathā
section("(142) 7. Pariyāpannakathā", f"(142) 7. {P11.PARIY} {THING}အကြောင်း {KATHA}")
section("Pariyāpannakathā", f"{P11.PARIY} {THING}အကြောင်း {KATHA}")
_RR = W("2", "^2-U49", "Rūparāgo", "သိမ်မွေ့သော ရုပ်ဘဝကို တပ်မက်သော ရာဂ")
_ARR = W("2", "^2-U49", "arūparāgo", "ရုပ်မရှိသော ဘဝကို တပ်မက်သော ရာဂ")
RG = {"rūpa": _RR, "arūpa": _ARR, "kāma": _KR}
DHX = {"rūpa": "သိမ်မွေ့သော ရုပ် ဓာတ်", "arūpa": "ရုပ်မရှိသော ဓာတ်", "kāma": W("2", "^2-912", "Kāmadhātu", "ကာမ ဓာတ်")}
new("rūpadhātu / arūpadhātu (realms)", f"{DHX['rūpa']} / {DHX['arūpa']}")
for _k in ("sadda", "gandha", "rasa", "phoṭṭhabba"):
    RG[_k] = f"{TAN[_k]}ကို တပ်မက်သော ရာဂ"
    DHX[_k] = W("1", "^1-U1", f"{_k}dhātu", f"{TAN[_k]} ဓာတ်")
SINK = ("ကိန်းအောင်း", "မကိန်းအောင်း")
INC = ("အကျုံးဝင်", "အကျုံးမဝင်")
for _k in RG:
    _a = f"{_k}rāgo {_k}dhātuṃ anuseti"
    _am = f"{RG[_k]}သည် {DHX[_k]}၌"
    P(_a, Cl(_am, *SINK))
    P(f"{_a}, {_k}dhātupariyāpanno", Cl(f"{_am} ကိန်းအောင်း၍ {DHX[_k]}၌", *INC))
    P(f"{_a} {_k}dhātupariyāpanno", Cl(f"{_am} ကိန်းအောင်း၍ {DHX[_k]}၌", *INC))
    P(f"{_k}dhātupariyāpanno", Cl(f"{DHX[_k]}၌", *INC))
    P(f"{_k}rāgo", FR(RG[_k]))
P("rūparāgo rūpadhātuṃ anuseti rūpadhātupariyāpanno, arūparāgo arūpadhātuṃ anuseti arūpadhātupariyāpanno",
  Cl(f"{RG['rūpa']}သည် {DHX['rūpa']}၌ ကိန်းအောင်း၍ {DHX['rūpa']}၌ အကျုံးဝင်၍ {RG['arūpa']}သည် {DHX['arūpa']}၌ "
     f"ကိန်းအောင်း၍ {DHX['arūpa']}၌", *INC))
P("gandharāgo…pe… rasarāgo…pe… phoṭṭhabbarāgo phoṭṭhabbadhātuṃ anuseti, phoṭṭhabbadhātupariyāpanno",
  Cl(f"{RG['gandha']}… {RG['rasa']}… {RG['phoṭṭhabba']}သည် {DHX['phoṭṭhabba']}၌ ကိန်းအောင်း၍ {DHX['phoṭṭhabba']}၌",
     *INC))
P("gandharāgo…pe… rasarāgo…pe… phoṭṭhabbarāgo phoṭṭhabbadhātuṃ anuseti",
  Cl(f"{RG['gandha']}… {RG['rasa']}… {RG['phoṭṭhabba']}သည် {DHX['phoṭṭhabba']}၌", *SINK))
SMS = new("samāpattesiya", "သမာပတ်ကို ရှာသော")
DDS = new("diṭṭhadhammasukhavihāra", "ယခုဘဝ၌ ချမ်းသာစွာ နေခြင်း ဖြစ်သော")
_SH = "အတူ ဖြစ်သော၊ အတူ ပေါ်ပေါက်သော၊ ရောနှောသော၊ ယှဉ်တွဲသော၊ အတူ ဖြစ်ပေါ်သော၊ အတူ ချုပ်သော၊ မှီရာ တူသော၊ အာရုံ တူသော"
new("sahagato sahajāto saṃsaṭṭho sampayutto ekuppādo ekanirodho ekavatthuko ekārammaṇo", _SH)
_SH_E = "အာရုံ တူသော"
P("samāpattesiyo upapattesiyo diṭṭhadhammasukhavihāro, samāpattesiyena cittena upapattesiyena cittena "
  "diṭṭhadhammasukhavihārena cittena sahagato sahajāto saṃsaṭṭho sampayutto ekuppādo ekanirodho ekavatthuko "
  "ekārammaṇo", V(f"{SMS}၊ {UPS}၊ {DDS} {THING} ဖြစ်၍ {SMS} {CITTA}၊ {UPS} {CITTA}၊ {DDS} {CITTA}တို့နှင့်{_SH} {THING}"))
_N3 = f"{SMS} {THING} မဟုတ်၊ {UPS} {THING} မဟုတ်၊ {DDS} {THING} မဟုတ်"
_N3C = f"{SMS} {CITTA}နှင့် မဟုတ်၊ {UPS} {CITTA}နှင့် မဟုတ်၊ {DDS} {CITTA}နှင့် မဟုတ်ဘဲ"
P("na samāpattesiyo na upapattesiyo na diṭṭhadhammasukhavihāro, na samāpattesiyena cittena na upapattesiyena cittena "
  "na diṭṭhadhammasukhavihārena cittena sahagato sahajāto saṃsaṭṭho sampayutto ekuppādo ekanirodho ekavatthuko "
  "ekārammaṇo", V(f"{_N3}၍ {_N3C} {_SH} {THING}"))
P("na samāpattesiyo na upapattesiyo na diṭṭhadhammasukhavihāro…pe… ekārammaṇo", V(f"{_N3}… {_SH_E} {THING}"))
P("na samāpattesiyo na upapattesiyo na diṭṭhadhammasukhavihāro, na samāpattesiyena cittena…pe… ekārammaṇo",
  V(f"{_N3}၍ {SMS} {CITTA}နှင့် မဟုတ်… {_SH_E} {THING}"))
P("na samāpattesiyo na upapattesiyo…pe… ekārammaṇo", V(f"{SMS} {THING} မဟုတ်၊ {UPS} {THING} မဟုတ်… {_SH_E} {THING}"))
S('Arūparāgo arūpadhātuṃ anuseti, na vattabbaṃ – "arūpadhātupariyāpanno"ti, na hevaṃ vattabbe…pe…',
  f"{RG['arūpa']}သည် {DHX['arūpa']}၌ ကိန်းအောင်းသည်{C} ဤသို့ မဆိုသင့် – “{DHX['arūpa']}၌ အကျုံးဝင်သည်”{C} "
  f"{F.NO_SAY}{PE}")

# ===================================================================================== 143. Abyākatakathā
DG = W("1", "^1-1105", "diṭṭhigataṃ", "အယူမှား")
section("(143) 8. Abyākatakathā", f"(143) 8. {ABY} {THING}အကြောင်း {KATHA}")
section("Abyākatakathā", f"{ABY} {THING}အကြောင်း {KATHA}")
for _e, _m in (("abyākataṃ", f"{ABY} {THING}"), ("akusalaṃ", AKUSALA), ("apariyāpannaṃ", f"{P11.APARIY} {THING}")):
    P(f"diṭṭhigataṃ {_e}", V(f"{DG}သည် {_m}"))
DGS = f"{DG}နှင့် ယှဉ်တွဲသော"
for _e, _m in (("abyākato", f"{ABY} {THING}"), ("akusalo", AKUSALA)):
    P(f"diṭṭhigatasampayutto phasso {_e}", V(f"{DGS} တွေ့ထိမှုသည် {_m}"))
P("diṭṭhigatasampayuttā vedanā…pe… saññā…pe… cetanā…pe… cittaṃ abyākataṃ",
  V(f"{DGS} ခံစားမှု… မှတ်သိမှု… စေ့ဆော်မှု… {CITTA}သည် {ABY} {THING}"))
P("diṭṭhigatasampayuttā vedanā saññā cetanā cittaṃ akusalaṃ",
  V(f"{DGS} ခံစားမှု၊ မှတ်သိမှု၊ စေ့ဆော်မှု၊ {CITTA}သည် {AKUSALA}"))
PHALA = "အကျိုး"
VIPAKA_N = "ကံ၏ အကျိုး"
P("aphalaṃ avipākaṃ", V(f"{PHALA} မရှိ၍ {VIPAKA_N} မရှိသော {THING}"))
P("saphalaṃ savipākaṃ", V(f"{PHALA} ရှိ၍ {VIPAKA_N} ရှိသော {THING}"))
MD = W("1", "^1-365", "micchādiṭṭhi hoti", "မှားယွင်းသော အယူ")
P("micchādiṭṭhiparamāni vajjāni vuttāni bhagavatā", Cl(f"{MD}ကို အကြီးဆုံး အပြစ်ဟု {BUDDHA}", *SAID))
ANCHOR_X["vajjāni"] = "အကြီးဆုံး အပြစ်ဟု"
BR_X["[aṅguttaranikāye]"] = f"[{F.REF['a. ni.']}၌]"
Q("micchādiṭṭhi kho, vaccha, akusalā, sammādiṭṭhi kusalā",
  f"ဝစ္ဆ၊ {MD}သည် {AKUSALA} ဖြစ်၏ ⟦b⟧၊ {F.SAMMADITTHI}သည် {KUSALA} ဖြစ်၏ ⟦b⟧")
VAR_X.update({"akusalaṃ": F.PATHA, "kusalaṃ": F.PATHA})
Q("micchādiṭṭhissa kho ahaṃ, puṇṇa, dvinnaṃ gatīnaṃ aññataraṃ gatiṃ vadāmi – nirayaṃ vā tiracchānayoniṃ vā",
  f"ပုဏ္ဏ၊ {MD} ရှိသူအား ငါသည် {W('2', '^2-U58', 'duggatiṃ', 'လားရာ')} {F.NUM_MY[2]}{F.CL}တို့အနက် တစ်ပါးပါးသော "
  f"လားရာကို ဟော၏ – ငရဲကိုဖြစ်စေ၊ {F.TIRACCHANA} ဘုံကိုဖြစ်စေ")
_V10 = W("1", "^1-1105", "Sassato lokoti vā", "လောကသည် ထာဝရ တည်မြဲသည်ဟူ၍ဖြစ်စေ၊ လောကသည် ထာဝရ မတည်မြဲဟူ၍ဖြစ်စေ၊ "
         "လောကသည် အဆုံး ရှိသည်ဟူ၍ဖြစ်စေ၊ လောကသည် အဆုံး မရှိဟူ၍ဖြစ်စေ၊ အသက်သည် ကိုယ်ခန္ဓာပင် ဖြစ်သည်ဟူ၍ဖြစ်စေ၊ "
         "အသက်နှင့် ကိုယ်ခန္ဓာသည် တခြားစီ ဖြစ်သည်ဟူ၍ဖြစ်စေ၊ မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်ဟူ၍ဖြစ်စေ၊ "
         "မြတ်စွာဘုရားသည် သေပြီးနောက် မရှိဟူ၍ဖြစ်စေ၊ မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်လည်း ဖြစ် မရှိသည်လည်း "
         "ဖြစ်သည်ဟူ၍ဖြစ်စေ၊ မြတ်စွာဘုရားသည် သေပြီးနောက် ရှိသည်လည်း မဟုတ် မရှိသည်လည်း မဟုတ်ဟူ၍ဖြစ်စေ")
_V10 = [x[:-len("ဟူ၍ဖြစ်စေ")] for x in _V10.split("၊ ")]
assert len(_V10) == 10
UND = new("abyākatametaṃ (undeclared)", "ဤသည်ကို မဖြေကြားအပ်")
_VC = "ဝစ္ဆ"
_VQ = [f"‹{x}›ဟူ၍ {_VC}၊ {UND}" for x in _V10[:3]] + [f"‹{x}›ဟူ၍ {_VC}…" for x in _V10[3:9]]
Q("sassato lokoti kho, vaccha, abyākatametaṃ, asassato lokoti kho, vaccha, abyākatametaṃ, antavā lokoti kho, vaccha, "
  "abyākatametaṃ, anantavā lokoti kho, vaccha…pe… taṃ jīvaṃ taṃ sarīranti kho, vaccha…pe… aññaṃ jīvaṃ aññaṃ "
  "sarīranti kho, vaccha…pe… hoti tathāgato paraṃ maraṇāti kho, vaccha…pe… na hoti tathāgato paraṃ maraṇāti kho, "
  "vaccha…pe… hoti ca na ca hoti tathāgato paraṃ maraṇāti kho, vaccha…pe… neva hoti na na hoti tathāgato paraṃ "
  "maraṇāti kho, vaccha, abyākatametaṃ",
  "၊ ".join(_VQ[:3]) + "၊ " + " ".join(_VQ[3:]) + f" ‹{_V10[9]}›ဟူ၍ {_VC}၊ {UND}")
REF_NOTE_X["thokaṃ pana visadisaṃ"] = "သို့သော် အနည်းငယ် ကွဲပြားသည်"
Q("micchādiṭṭhikassa, bhikkhave, purisapuggalassa yañceva kāyakammaṃ yathādiṭṭhisamattaṃ samādinnaṃ, yañca "
  "vacīkammaṃ…pe… yañca manokammaṃ, yā ca cetanā, yā ca patthanā, yo ca paṇidhi, ye ca saṅkhārā, sabbe te dhammā "
  "aniṭṭhāya akantāya amanāpāya ahitāya dukkhāya saṃvattanti",
  f"{_R} {MD} ရှိသော ယောက်ျား ပုဂ္ဂိုလ်၏ အယူအတိုင်း ပြည့်စုံစွာ ဆောက်တည်ထားသော ကာယကံ၊ ဝစီကံ… မနောကံ၊ "
  f"စေ့ဆော်မှု၊ ဆုတောင်းခြင်း၊ {PANIDHI}၊ ပြုပြင်ဖန်တီးမှုတို့ ဟူသမျှ၊ ထိုသဘောတရား အားလုံးတို့သည် "
  "မလိုလားဖွယ်ရာ၊ မနှစ်သက်ဖွယ်ရာ၊ စိတ် မတွေ့ဖွယ်ရာ၊ အစီးအပွား မဖြစ်ဖွယ်ရာ၊ ဆင်းရဲဖွယ်ရာ အဖြစ်သို့ ရောက်စေကုန်၏")
W("1", "^1-1065", "patthanā", "ဆုတောင်းခြင်း")

# ===================================================================================== 144. Apariyāpannakathā
section("(144) 9. Apariyāpannakathā", f"(144) 9. {P11.APARIY} {THING}အကြောင်း {KATHA}")
section("Apariyāpannakathā", f"{P11.APARIY} {THING}အကြောင်း {KATHA}")
P("puthujjano kāmesu vītarāgoti vattabbo", Cl(f"{PUTHU}ကို «ကာမတို့၌ ရာဂ ကင်းသူ»ဟု", *SAY_V))
P("vigatadiṭṭhiyoti vattabbo", Cl(f"«{DG} ကင်းသူ»ဟု", *SAY_V))
LINES_X[key("Akusalamūlaṃ paṭisandahati kusalamūlaṃ, kusalamūlaṃ paṭisandahati akusalamūlaṃ, saḷāyatanaṃ "
            "chaviññāṇakāyā, ariyarūpaṃ mahābhūtānaṃ upādāya, sveva anusayo taṃ pariyuṭṭhānaṃ, pariyuṭṭhānaṃ "
            "cittavippayuttaṃ, yathādhātu taññeva anuseti, diṭṭhigataṃ abyākataṃ, diṭṭhigataṃ apariyāpannanti.")] = (
    f"{AKM}သည် {KM}နှင့် ဆက်စပ်ခြင်း၊ {KM}သည် {AKM}နှင့် ဆက်စပ်ခြင်း၊ {SALAY}၊ သိစိတ် အစု ခြောက်ပါး၊ {ARR}သည် "
    f"{MAHAB}တို့ကို မှီ၍ ဖြစ်ခြင်း၊ ထို{ANU}ပင် ထို{PAR} ဖြစ်ခြင်း၊ {PAR}သည် {VIPP_C} {THING} ဖြစ်ခြင်း၊ "
    f"ဓာတ်အလိုက် ထိုဓာတ်၌ပင် ကိန်းအောင်းခြင်း၊ {DG}သည် {ABY} {THING} ဖြစ်ခြင်း၊ {DG}သည် {P11.APARIY} {THING} "
    f"ဖြစ်ခြင်း{END}")


def open_q(line, protect=(), slot=None):
    """A Pāli line whose quotation is never closed (source slip): cut into sentences with the quotes ignored
    (protected sub-strings, e.g. a whole sutta quotation, are kept in one piece); registered in OPEN_Q_X.
    slot: (unit index, «⟦0⟧»): a bracket placeholder put before the end mark of that unit."""
    k = key(line)
    tmp = k
    for i, p in enumerate(protect):
        tmp = tmp.replace(key(p), f"Qzz{i}zzQ{key(p)[-1]}")
    units = [tmp[a:b].strip() for a, b in F.split_sents(tmp)]
    for i, p in enumerate(protect):
        units = [u.replace(f"Qzz{i}zzQ{key(p)[-1]}", key(p)) for u in units]
    OPEN_Q_X[k] = units
    if slot:
        SLOT_X[k] = slot


SLOT_X = {}

# ===================================================================================== 145. Paccayatākathā
PCT = new("paccayatā", "အကြောင်းဖြစ်ပုံ")
VAV = ("ပိုင်းခြား သတ်မှတ်ပြီး", "ပိုင်းခြား မသတ်မှတ်ရသေး")
section("(145) 1. Paccayatākathā", f"(145) 1. {PCT}အကြောင်း {KATHA}")
section("Paccayatākathā", f"{PCT}အကြောင်း {KATHA}")
P("paccayatā vavatthitā", Cl(f"{PCT}သည်", *VAV))
ADH = W("3", "^3-98", "maggādhipatino dhammā", "အကြီးအမှူး")                      # adhipati
SAHAJ = P11.SAHA["sahajātaṃ"].strip()                                                 # «နှင့်အတူ ပေါ်ပေါက်သော»
PCN = {"hetu": "အမြစ်", "adhipati": ADH, "sahajāta": "အတူ ပေါ်ပေါက်ခြင်း", "indriya": INDRIYA, "magga": "မဂ်",
       "āhāra": "အာဟာရ", "ārammaṇa": "အာရုံ", "anantara": "ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း",
       "samanantara": "ကောင်းစွာ ချက်ချင်း နောက်၌ ဖြစ်စေခြင်း",
       "āsevana": W("1", "^1-1361", "āsevanā bhāvanā", "အလေ့အကျင့် ပြုခြင်း")}
PCY = {k: f"{v}ဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်" for k, v in PCN.items()}              # X-paccayena paccayo
new("X-paccayena paccayo", "Xဟူသော အကြောင်းဖြင့် အကြောင်း ဖြစ်")
for _a, _b in (("hetu", "adhipati"), ("adhipati", "sahajāta"), ("adhipati", "indriya"), ("adhipati", "magga"),
               ("adhipati", "āhāra"), ("adhipati", "ārammaṇa"), ("anantara", "āsevana")):
    P(f"{_a}paccayena paccayo, {_b}paccayena paccayo", V(f"{PCY[_a]}၍ {PCY[_b][:-len(' ဖြစ်')]}"))
P("hetupaccayena paccayo hoti, ārammaṇapaccayena paccayo hoti, anantarapaccayena paccayo hoti, "
  "samanantarapaccayena paccayo hoti",
  V("၍ ".join(PCY[x] for x in ("hetu", "ārammaṇa", "anantara")) + f"၍ {PCY['samanantara'][:-len(' ဖြစ်')]}"))
VIMAMSA = _IDP[3].split()[0]                                                           # «စုံစမ်းဆင်ခြင်မှု»
P("vīmaṃsā hetu, so ca adhipati", V(f"{VIMAMSA}သည် အမြစ် ဖြစ်၍ ထိုအမြစ်သည်လည်း {ADH}"))
SDA = f"အတူ ပေါ်ပေါက်သော {P6.DH_PL}၏ {ADH}"                                          # sahajātānaṃ dhammānaṃ adhipati
for _k, _m in (("chanda", "ဆန္ဒ"), ("vīriya", "ဝီရိယ"), ("citta", CITTA), ("vīmaṃsā", VIMAMSA)):
    _pk = f"{_k[:-1]}ādhipati sahajātānaṃ dhammānaṃ adhipati"
    _sub = f"{_m} {ADH}သည် {SDA}"
    P(_pk, V(_sub))
    P(f"{_pk}, tañca indriyaṃ", V(f"{_sub} ဖြစ်၍ ထိုအရာသည်လည်း {INDRIYA}"))
    P(f"{_pk}, tañca maggaṅgaṃ", V(f"{_sub} ဖြစ်၍ ထိုအရာသည်လည်း မဂ်၏ အင်္ဂါ"))
    P(f"{_pk}, so ca āhāro", V(f"{_sub} ဖြစ်၍ ထိုအရာသည်လည်း အာဟာရ"))
P("ariyaṃ dhammaṃ garuṃ katvā uppajjati paccavekkhaṇā, tañcārammaṇaṃ",
  V(f"အရိယာ တရားကို လေးစားဖွယ်ရာ ပြု၍ ပြန်လည် ဆင်ခြင်ခြင်း ဖြစ်ပေါ်၍ ထိုအရာသည်လည်း အာရုံ"))
W("2", "^2-808", "paccavekkhaṇāñāṇaṃ", "ပြန်လည် ဆင်ခြင်")
for _k, _m in (("kusalā", KUSALA), ("akusalā", AKUSALA), ("kiriyābyākatā", KIRABY[:-len(" အရာ")])):
    _g = _k[:-1] + "ānaṃ"
    P(f"purimā purimā {_k} dhammā pacchimānaṃ pacchimānaṃ {_g} dhammānaṃ anantarapaccayena paccayo, sā ca āsevanā",
      V(f"ရှေးရှေး {_m} {P6.DH_PL}သည် နောက်နောက် {_m} {P6.DH_PL}အား {PCY['anantara']}၍ ထိုအရာသည်လည်း "
        f"{PCN['āsevana']}"))

# ===================================================================================== 146. Aññamaññapaccayakathā
section("(146) 2. Aññamaññapaccayakathā", f"(146) 2. အချင်းချင်း အကြောင်း ဖြစ်ခြင်းအကြောင်း {KATHA}")
section("Aññamaññapaccayakathā", f"အချင်းချင်း အကြောင်း ဖြစ်ခြင်းအကြောင်း {KATHA}")
PS = {"avijjā": W("1", "^1-1343", "Avijjāpaccayā saṅkhārā", "အမှန်ကို မသိမှု"), "saṅkhārā": "ပြုပြင်ဖန်တီးမှုများ",
      "taṇhā": TANHA, "upādānaṃ": W("1", "^1-1343", "taṇhāpaccayā upādānaṃ", "စွဲလမ်းမှု"),
      "viññāṇaṃ": "သိစိတ်", "nāmarūpaṃ": W("1", "^1-1343", "viññāṇapaccayā nāmarūpaṃ", "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း"),
      "jarāmaraṇa": "အိုခြင်း၊ သေခြင်း", "jāti": W("1", "^1-1343", "bhavapaccayā jāti", "မွေးဖွားခြင်း"),
      "bhavo": "ဘဝ"}
_PS_ABL = {"avijjā": "avijjā", "saṅkhāra": "saṅkhārā", "taṇhā": "taṇhā", "upādāna": "upādānaṃ",
           "viññāṇa": "viññāṇaṃ", "nāmarūpa": "nāmarūpaṃ", "jarāmaraṇa": "jarāmaraṇa", "jāti": "jāti"}
for _a, _b, _e in (("avijjā", "saṅkhārā", "va"), ("taṇhā", "upādānaṃ", "va"), ("saṅkhāra", "avijjā", "pi"),
                   ("upādāna", "taṇhā", "pi"), ("avijjā", "saṅkhārā", "pi"), ("taṇhā", "upādānaṃ", "pi"),
                   ("nāmarūpa", "viññāṇaṃ", "pi")):
    _em = "သာ" if _e == "va" else "လည်း"
    P(f"{_a}paccayā{_e} {_b}", Cl(f"{PS[_PS_ABL[_a]]}ကြောင့်{_em} {PS[_b]}", *ARISE))
P("avijjāpaccayāpi saṅkhārā, saṅkhārapaccayāpi avijjā; taṇhāpaccayāpi upādānaṃ, upādānapaccayāpi taṇhā",
  Cl(f"{PS['avijjā']}ကြောင့်လည်း {PS['saṅkhārā']} ဖြစ်ပေါ်၍ {PS['saṅkhārā']}ကြောင့်လည်း {PS['avijjā']} ဖြစ်ပေါ်၏၊ "
     f"{TANHA}ကြောင့်လည်း {PS['upādānaṃ']} ဖြစ်ပေါ်၍ {PS['upādānaṃ']}ကြောင့်လည်း {TANHA}", *ARISE))
P("avijjā saṅkhārena sahajātā", V(f"{PS['avijjā']}သည် ပြုပြင်ဖန်တီးမှု{SAHAJ} {THING}"))
P("taṇhā upādānena sahajātā", V(f"{TANHA}သည် {PS['upādānaṃ']}{SAHAJ} {THING}"))
P("jarāmaraṇapaccayā, bhikkhave, jāti, jātipaccayā bhavo",
  Cl(f"{_R} {PS['jarāmaraṇa']}ကြောင့် {PS['jāti']} ဖြစ်ပေါ်၏၊ {PS['jāti']}ကြောင့် {PS['bhavo']}", *ARISE))
P("viññāṇapaccayā, bhikkhave, nāmarūpaṃ, nāmarūpapaccayāpi viññāṇaṃ",
  Cl(f"{_R} {PS['viññāṇaṃ']}ကြောင့် {PS['nāmarūpaṃ']} ဖြစ်ပေါ်၏၊ {PS['nāmarūpaṃ']}ကြောင့်လည်း {PS['viññāṇaṃ']}", *ARISE))
REF_NOTE_X["thokaṃ pana visadisaṃ"] = "သို့သော် အနည်းငယ် ကွဲပြားသည်"


@F.frame(r"(?P<t>Tena hi )?(?P<p>[^–]+?), na vattabbaṃ – (?P<q>.+?)ti\.")
def _f_tenahi_p_navatt(m):
    """Tena hi P, na vattabbaṃ – "Q"ti. (^5-719)"""
    pre = f"{F.TENA_HI} " if m["t"] else ""
    return f"{pre}{F.pq(m['p'], 'stmt')}{C} ဤသို့ မဆိုသင့် – “{F.pq(m['q'], 'stmt', 1)}”{END}"


before_generic()

# ===================================================================================== 147. Addhākathā / 148. Khaṇalayamuhuttakathā
ADDHA = new("addhā", "ကာလ")
PARIN = ("အမှန်တကယ် ဖြစ်ပေါ်ပြီး", "အမှန်တကယ် မဖြစ်ပေါ်ရသေး")                       # parinipphanna
new("parinipphanna", "အမှန်တကယ် ဖြစ်ပေါ်ပြီးသော")
section("(147) 3. Addhākathā", f"(147) 3. {ADDHA}အကြောင်း {KATHA}")
section("Addhākathā", f"{ADDHA}အကြောင်း {KATHA}")
TIME3 = {"atīt": P6.ATITA, "anāgat": P6.ANAGATA, "paccuppann": P6.PACCUP}
P("addhā parinipphanno", Cl(f"{ADDHA}သည်", *PARIN))
for _k, _m in TIME3.items():
    P(f"{_k}o addhā parinipphanno", Cl(f"{_m} {ADDHA}သည်", *PARIN))
    P(f"{_k}aṃ rūpaṃ vedanā saññā saṅkhārā viññāṇaṃ {_k}o addhā",
      V(f"{_m} {F.RUPA.my}၊ {F.VEDANA.my}၊ {F.SANNA.my}၊ {F.SANKHARA.my}၊ {F.VINNANA.my}သည် {_m} {ADDHA}"))
    P(f"{_k}ā pañcaddhā", V(f"{_m} {ADDHA} {F.NUM_MY[5]}{F.CL}"))
S("Rūpanti?", f"{F.RUPA.my} ဖြစ်သလော{END}")                                       # the subject elided
S("vedanā…pe… saññā…pe… saṅkhārā…pe… viññāṇanti?",
  f"{F.VEDANA.my}… {F.SANNA.my}… {F.SANKHARA.my}… {F.VINNANA.my} ဖြစ်သလော{END}")
_KH5 = f"{F.KHANDHA_W} {F.NUM_MY[5]}{F.CL}"
_AY12 = f"{F.AYATANA_W} {F.NUM_MY[12]}{F.CL}"
_DH18 = f"{F.DHATU_W} {F.NUM_MY[18]}{F.CL}"
_IN22 = f"{F.INDRIYA_W} {F.NUM_MY[22]}{F.CL}"
for _pi, _set, _n, _nm in ((("atītā", "anāgatā", "paccuppannā"), "pañcakkhandhā", "pannarasaddhā", "ဆယ့်ငါး"),
                           (("atītāni", "anāgatāni", "paccuppannāni"), "dvādasāyatanāni", "chattiṃsa addhā",
                            "သုံးဆယ့်ခြောက်"),
                           (("atītā", "anāgatā", "paccuppannā"), "aṭṭhārasa dhātuyo", "catupaññāsa addhā", "ငါးဆယ့်လေး"),
                           (("atītāni", "anāgatāni", "paccuppannāni"), "bāvīsatindriyāni", "chasaṭṭhi addhā",
                            "ခြောက်ဆယ့်ခြောက်")):
    _sm = {"pañcakkhandhā": _KH5, "dvādasāyatanāni": _AY12, "aṭṭhārasa dhātuyo": _DH18, "bāvīsatindriyāni": _IN22}[_set]
    _ad = ("atīto", "anāgato", "paccuppanno")
    P(", ".join(f"{a} {_set} {b} addhā" for a, b in zip(_pi, _ad)),
      V("၍ ".join(f"{m} {_sm}သည် {m} {ADDHA} ဖြစ်" for m in TIME3.values())[:-len(" ဖြစ်")]))
    P(_n, V(f"{ADDHA} {_nm}{F.CL}"))
KATHAV = "စကားပြောရာ အကြောင်းအရာ"                                                    # kathāvatthu (topic of talk)
_KTH = "အကြောင်းပြု၍ စကား ပြောရာ၏"
Q("tīṇimāni, bhikkhave, kathāvatthūni! Katamāni tīṇi? Atītaṃ vā, bhikkhave, addhānaṃ ārabbha kathaṃ katheyya – evaṃ "
  "ahosi atītamaddhānanti; anāgataṃ vā, bhikkhave, addhānaṃ ārabbha kathaṃ katheyya – evaṃ bhavissati "
  "anāgatamaddhānanti; etarahi vā, bhikkhave, paccuppannaṃ addhānaṃ ārabbha kathaṃ katheyya – evaṃ hoti etarahi "
  "paccuppannanti. Imāni kho, bhikkhave, tīṇi kathāvatthūni",
  f"{_R} {KATHAV} {F.NUM_MY[3]}{F.CL}တို့သည် ဤသည်တို့ပင်တည်း။ အဘယ် {F.NUM_MY[3]}{F.CL}တို့နည်း။ {_R} {P6.ATITA} "
  f"{ADDHA}ကိုဖြစ်စေ {_KTH} – ‹{P6.ATITA} {ADDHA}၌ ဤသို့ ဖြစ်ခဲ့၏›ဟူ၍၊ {_R} {P6.ANAGATA} {ADDHA}ကိုဖြစ်စေ {_KTH} – "
  f"‹{P6.ANAGATA} {ADDHA}၌ ဤသို့ ဖြစ်လိမ့်မည်›ဟူ၍၊ {_R} ယခု {P6.PACCUP} {ADDHA}ကိုဖြစ်စေ {_KTH} – ‹ယခု {P6.PACCUP}၌ "
  f"ဤသို့ ဖြစ်၏›ဟူ၍။ {_R} ဤသည်တို့ကား {KATHAV} {F.NUM_MY[3]}{F.CL}တို့ ဖြစ်ကုန်၏")
_TQ = ('Nanu vuttaṃ bhagavatā – "tīṇimāni, bhikkhave, kathāvatthūni! Katamāni tīṇi? Atītaṃ vā, bhikkhave, addhānaṃ '
       'ārabbha kathaṃ katheyya – ‘evaṃ ahosi atītamaddhāna’nti; anāgataṃ vā, bhikkhave, addhānaṃ ārabbha kathaṃ '
       'katheyya – ‘evaṃ bhavissati anāgatamaddhāna’nti; etarahi vā, bhikkhave, paccuppannaṃ addhānaṃ ārabbha kathaṃ '
       'katheyya – ‘evaṃ hoti etarahi paccuppanna’nti. Imāni kho, bhikkhave, tīṇi kathāvatthūnī"ti.')
open_q('Na vattabbaṃ – "addhā parinipphannoti? Āmantā. ' + _TQ + ' Attheva suttantoti? Āmantā. Tena hi addhā '
       'parinipphannoti.', protect=[_TQ], slot=(2, "⟦0⟧"))
KLM = {"khaṇo": "ခဏ", "layo": "အခိုက်အတန့်", "muhuttaṃ": "မုဟုတ်ကာလ"}
new("khaṇo / layo / muhuttaṃ", " / ".join(KLM.values()))
section("(148) 4. Khaṇalayamuhuttakathā", f"(148) 4. {KLM['khaṇo']}၊ {KLM['layo']}၊ {KLM['muhuttaṃ']}အကြောင်း {KATHA}")
section("Khaṇalayamuhuttakathā", f"{KLM['khaṇo']}၊ {KLM['layo']}၊ {KLM['muhuttaṃ']}အကြောင်း {KATHA}")
P("khaṇo parinipphanno, layo parinipphanno, muhuttaṃ parinipphannaṃ",
  Cl(f"{KLM['khaṇo']}သည် {PARIN[0]}၍ {KLM['layo']}သည် {PARIN[0]}၍ {KLM['muhuttaṃ']}သည်", *PARIN))
P("muhuttaṃ parinipphannaṃ", Cl(f"{KLM['muhuttaṃ']}သည်", *PARIN))
open_q('Na vattabbaṃ – "muhuttaṃ parinipphannanti? Āmantā. ' + _TQ + ' Attheva suttantoti? Āmantā. Tena hi muhuttaṃ '
       'parinipphannanti.', protect=[_TQ])

# ===================================================================================== 149. Āsavakathā
section("(149) 5. Āsavakathā", f"(149) 5. စိတ်အစွန်းအထင်းအကြောင်း {KATHA}")
section("Āsavakathā", f"စိတ်အစွန်းအထင်းအကြောင်း {KATHA}")
_AS4 = W("1", "^1-1102", "Cattāro āsavā", f"စိတ်အစွန်းအထင်း {F.NUM_MY[4]}{F.CL}")
P("cattāro āsavā anāsavā", V(f"{_AS4}တို့သည် {_ANAS_MY[0]} {THING}"))
P("atthaññeva āsavā yehi āsavehi te āsavā sāsavā honti",
  Cl(f"ထိုစိတ်အစွန်းအထင်းတို့ကို {_SAS_MY[0]} {THING} ဖြစ်စေသည့် အခြား စိတ်အစွန်းအထင်းတို့", "ရှိသေး", "မရှိတော့"))
open_q('Na vattabbaṃ – "cattāro āsavā anāsavāti? Āmantā. Atthaññeva āsavā yehi āsavehi te āsavā sāsavā hontīti? Na '
       'hevaṃ vattabbe. Tena hi cattāro āsavā anāsavāti.')

# ===================================================================================== 150. Jarāmaraṇakathā
JM = PS["jarāmaraṇa"].replace("၊ ", " ")                                                 # «အိုခြင်း သေခြင်း»
section("(150) 6. Jarāmaraṇakathā", f"(150) 6. {JM}အကြောင်း {KATHA}")
section("Jarāmaraṇakathā", f"{JM}အကြောင်း {KATHA}")
P("lokuttarānaṃ dhammānaṃ jarāmaraṇaṃ lokuttaraṃ", V(f"{LOKUTTARA} {P6.DH_PL}၏ {JM}သည် {LOKUTTARA} {THING}"))
_MP = {"sotāpattimagg": MG["sotāpatti"], "sotāpattiphal": PH["sotāpatti"], "sakadāgāmimagg": MG["sakadāgāmi"],
       "sakadāgāmiphal": PH["sakadāgāmi"], "anāgāmimagg": MG["anāgāmi"], "anāgāmiphal": PH["anāgāmi"],
       "arahattamagg": MG["arahatta"], "arahattaphal": P6.PAT["arahatta"]}
for _k, _m in _MP.items():
    _nom = f"{_k}o" if _k.endswith("magg") else f"{_k}aṃ"
    P(f"{_k}assa jarāmaraṇaṃ {_nom}", V(f"{_m}၏ {JM}သည် {_m}"))
    P(f"{_k}assa", FR(f"{_m}၏"))
for _k, _m in (("satipaṭṭhānānaṃ", SATIP), ("sammappadhānānaṃ", SP), ("iddhipādānaṃ", ID), ("indriyānaṃ", INDRIYA),
               ("balānaṃ", BALA)):
    P(_k, FR(f"{_m}တို့၏"))
P("bojjhaṅgānaṃ jarāmaraṇaṃ bojjhaṅgo", V(f"{BJW}တို့၏ {JM}သည် {BJW}"))
P("lokiyaṃ", V(f"{LOKIYA} {THING}"))
P("lokuttaraṃ", V(f"{LOKUTTARA} {THING}"))
open_q('Na vattabbaṃ – "lokuttarānaṃ dhammānaṃ jarāmaraṇaṃ lokuttaranti? Āmantā. Lokiyanti? Na hevaṃ vattabbe. Tena hi '
       'lokuttaranti.')

# ===================================================================================== 151-153. Saññāvedayitakathā
SVN = W("2", "^2-808", "saññāvedayitanirodhasamāpattiyā", "မှတ်သိမှုနှင့် ခံစားရခြင်း ချုပ်ငြိမ်းရာ ဈာန်")
SVS = new("saññāvedayitanirodhasamāpatti", f"{SVN} ဝင်စားခြင်း")
SVP = new("saññāvedayitanirodhaṃ samāpanno", f"{SVN}ကို ဝင်စားနေသူ")
for _n, _h in (("(151) 7. ", "Saññāvedayitakathā"), ("(152) 8. ", "Dutiyasaññāvedayitakathā"),
               ("(153) 9. ", "Tatiyasaññāvedayitakathā")):
    _o = {"Saññāvedayitakathā": "", "Dutiyasaññāvedayitakathā": f"{F.ORD_MY[2]} ",
          "Tatiyasaññāvedayitakathā": f"{F.ORD_MY[3]} "}[_h]
    section(_n + _h, f"{_n}{_o}{SVN}အကြောင်း {KATHA}")
    section(_h, f"{_o}{SVN}အကြောင်း {KATHA}")
for _k, _m in (("lokuttarā", LOKUTTARA), ("lokiyā", LOKIYA)):
    P(f"saññāvedayitanirodhasamāpatti {_k}", V(f"{SVS}သည် {_m} {THING}"))
    P(_k, V(f"{_m} {THING}"))
for _k, _m in (("kāmāvacarā", KAMA_AV), ("rūpāvacarā", RUPA_AV), ("arūpāvacarā", ARUPA_AV)):
    P(_k, V(f"{_m} {THING}"))
for _p in ("saññāvedayitanirodhasamāpatti lokuttarā", "saññāvedayitanirodhasamāpatti lokiyā"):
    _o = "lokiyā" if _p.endswith("lokuttarā") else "lokuttarā"
    _O = _o[:1].upper() + _o[1:]
    _t = _p.split()[-1]
    open_q(f'Na vattabbaṃ – "{_p}ti? Āmantā. {_O}ti? Na hevaṃ vattabbe. Tena hi {_t}ti.')
KALA = ("သေရာ", "မသေရာ")
for _n, _neg in (("", False), ("na ", True)):
    P(f"saññāvedayitanirodhaṃ samāpanno {_n}kālaṃ kareyya", Cl(f"{SVP}သည်", *KALA, neg=_neg))
    P(f"cakkhuviññāṇasamaṅgī {_n}kālaṃ kareyya", Cl(f"{VINN['cakkhu']}နှင့် ပြည့်စုံနေသူသည်", *KALA, neg=_neg))
SVPL = f"{SVP}၌"
MRT = "သေခါနီး"                                                                       # māraṇantiya
new("māraṇantiya", MRT)
_FIVE = ["တွေ့ထိမှု", F.VEDANA.my, F.SANNA.my, "စေ့ဆော်မှု", CITTA]
for _n, _neg in (("", False), ("n", True)):
    P(f"{_n}atthi saññāvedayitanirodhaṃ samāpannassa māraṇantiyo phasso, māraṇantiyā vedanā, māraṇantiyā saññā, "
      "māraṇantiyā cetanā, māraṇantiyaṃ cittaṃ", V(f"{SVPL} " + "၊ ".join(f"{MRT} {x}" for x in _FIVE), EXIST, neg=_neg))
    P(f"{_n}atthi saññāvedayitanirodhaṃ samāpannassa phasso vedanā saññā cetanā cittaṃ",
      V(f"{SVPL} " + "၊ ".join(_FIVE), EXIST, neg=_neg))
DEATH = "သေခြင်း"
for _a, _am in (("a", "မရှိ"), ("sa", "ရှိ")):
    P(f"{_a}phassakassa kālaṃ kiriyā, {_a}vedanakassa kālaṃ kiriyā…pe… {_a}cittakassa kālaṃ kiriyā",
      V(f"တွေ့ထိမှု {_am}သူ၏ {DEATH}၊ ခံစားမှု {_am}သူ၏ {DEATH}… စိတ် {_am}သူ၏ {DEATH}"))
    P(f"{_a}phassakassa maggabhāvanā…pe… {_a}cittakassa maggabhāvanā",
      V(f"တွေ့ထိမှု {_am}သူ၏ မဂ်ကို ပွားများခြင်း… စိတ် {_am}သူ၏ မဂ်ကို ပွားများခြင်း"))
P("saphassakassa kālaṃ kiriyā…pe… sacittakassa kālaṃ kiriyā", V(f"တွေ့ထိမှု ရှိသူ၏ {DEATH}… စိတ် ရှိသူ၏ {DEATH}"))
P("saphassakassa maggabhāvanā…pe… sacittakassa maggabhāvanā",
  V("တွေ့ထိမှု ရှိသူ၏ မဂ်ကို ပွားများခြင်း… စိတ် ရှိသူ၏ မဂ်ကို ပွားများခြင်း"))
HIT = ("တိုးဝင်ရာ", "မတိုးဝင်ရာ")                                         # kameyya (ch11-12 «… တိုးဝင်ရာ»)


def hit_cl(pre, neg):
    """X kāye visaṃ (na) kameyya, satthaṃ (na) kameyya, aggi (na) kameyya (ch11-12 ^5-391 wording)."""
    if not neg:
        return VV(f"{pre} အဆိပ် တိုးဝင်ရာ၏၊ လက်နက် တိုးဝင်ရာ၏၊ မီး", HIT[0])
    return Cl(f"{pre} အဆိပ် မတိုးဝင်ရာ၊ လက်နက် မတိုးဝင်ရာ၊ မီး", *HIT, neg=True)


for _n, _neg in (("", False), ("na ", True)):
    P(f"saññāvedayitanirodhaṃ samāpannassa kāye visaṃ {_n}kameyya, satthaṃ {_n}kameyya, aggi {_n}kameyya",
      hit_cl(f"{SVP}၏ {F.KAYA}၌", _neg))
P("na nirodhaṃ samāpanno", V("ချုပ်ငြိမ်းရာ ဈာန်ကို ဝင်စားနေသူ", neg=True))
RULE_N = "စည်းမျဉ်း"                                                                    # niyāma (a fixed law)
new("so niyāmo yena niyāmena niyato (a fixed law)", f"အကြင် {RULE_N}ဖြင့် သတ်မှတ်ထားသောကြောင့် …၊ ထို{RULE_N}")
for _n, _neg in (("", False), ("n", True)):
    for _s, _sm in (("saññāvedayitanirodhaṃ samāpanno", SVP), ("cakkhuviññāṇasamaṅgī", f"{VINN['cakkhu']}နှင့် ပြည့်စုံနေသူ")):
        P(f"{_n}atthi so niyāmo yena niyāmena niyato {_s} na kālaṃ kareyya",
          V(f"အကြင် {RULE_N}ဖြင့် သတ်မှတ်ထားသောကြောင့် {_sm} {KALA[1]}၊ ထို{RULE_N}", EXIST, neg=_neg))

# ===================================================================================== 154. Asaññasattupikakathā
ASP = new("asaññasattupika", f"{W('2', '^2-1015', 'asaññasattānaṃ devānaṃ', 'အသညသတ်')} ဘုံသို့ ရောက်စေတတ်သော")
section("(154) 10. Asaññasattupikakathā", f"(154) 10. {ASP} အရာအကြောင်း {KATHA}")
section("Asaññasattupikakathā", f"{ASP} အရာအကြောင်း {KATHA}")
P("saññāvedayitanirodhasamāpatti asaññasattupikā", V(f"{SVS}သည် {ASP} {THING}"))
_ALB = [W("1", "^1-32", "alobho kusalamūlaṃ", "လောဘ မရှိခြင်း"), W("1", "^1-33", "adoso kusalamūlaṃ", "ဒေါသ မရှိခြင်း"),
        "မောဟ မရှိခြင်း"]
_ALB = [f"{x} ဟူသော {KM}" for x in _ALB]
_5B = "ယုံကြည်မှု၊ ဝီရိယ၊ သတိ၊ သမာဓိ၊ ပညာ"
for _n, _neg in (("", False), ("n", True)):
    P(f"{_n}atthi saññāvedayitanirodhaṃ samāpannassa alobho kusalamūlaṃ, adoso kusalamūlaṃ, amoho kusalamūlaṃ, "
      "saddhā vīriyaṃ sati samādhi paññā", V(f"{SVPL} {'၊ '.join(_ALB)}၊ {_5B}", EXIST, neg=_neg))
P("natthi saññāvedayitanirodhaṃ samāpannassa alobho kusalamūlaṃ, adoso kusalamūlaṃ…pe… paññā",
  V(f"{SVPL} {_ALB[0]}၊ {_ALB[1]}… ပညာ", EXIST, neg=True))
P("ye keci saññāvedayitanirodhaṃ samāpajjanti, sabbe te asaññasattupikā",
  V(f"{SVN}ကို ဝင်စားကြသူ ဟူသမျှ၊ ထိုသူ အားလုံးတို့သည် {ASP[:-len('စေတတ်သော')]}ကြမည့်သူတို့"))
P("idhāpi asaññī tatrāpi asaññī", V("ဤနေရာ၌လည်း မှတ်သိမှု မရှိသူ ဖြစ်၍ ထိုနေရာ၌လည်း မှတ်သိမှု မရှိသူ"))

# ===================================================================================== 155. Kammūpacayakathā
KU = new("kammūpacayo", f"{F.KAMMA}၏ စုဆောင်းမှု")
section("(155) 11. Kammūpacayakathā", f"(155) 11. {KU}အကြောင်း {KATHA}")
section("Kammūpacayakathā", f"{KU}အကြောင်း {KATHA}")
for _sep in (" ", ", "):
    P(f"aññaṃ kammaṃ{_sep}añño kammūpacayo", V(f"{F.KAMMA}နှင့် {KU}သည် {F.OTHER}"))
_UP = [("añño phasso, añño phassūpacayo", "တွေ့ထိမှု"), ("aññā vedanā, añño vedanūpacayo", F.VEDANA.my),
       ("aññā saññā, añño saññūpacayo", F.SANNA.my), ("aññā cetanā, añño cetanūpacayo", "စေ့ဆော်မှု"),
       ("aññaṃ cittaṃ, añño cittūpacayo", CITTA), ("aññā saddhā, añño saddhūpacayo", "ယုံကြည်မှု"),
       ("aññaṃ vīriyaṃ, añño vīriyūpacayo", "ဝီရိယ"), ("aññā sati, añño satūpacayo", "သတိ"),
       ("añño samādhi, añño samādhūpacayo", "သမာဓိ"), ("aññā paññā, añño paññūpacayo", "ပညာ"),
       ("añño rāgo, añño rāgūpacayo", "ရာဂ")]
_ANOT = P6.KIL["anottappaṃ"]
P("; ".join(x for x, _ in _UP) + "…pe… aññaṃ anottappaṃ, añño anottappūpacayo",
  V("၊ ".join(f"{m}နှင့် {m}၏ စုဆောင်းမှုသည် {F.OTHER} ဖြစ်" for _, m in _UP)
    + f"… {_ANOT}နှင့် {_ANOT}၏ စုဆောင်းမှုသည် {F.OTHER}"))
P("kammūpacayo kammena sahajāto", V(f"{KU}သည် {F.KAMMA}{SAHAJ} {THING}"))
for _k, _m in (("kusal", KUSALA), ("akusal", AKUSALA)):
    P(f"{_k}ena kammena sahajāto kammūpacayo {_k}o", V(f"{_m} {F.KAMMA}{SAHAJ} {KU}သည် {_m}"))
_VS = {"sukhāya": VD["sukhāya"], "dukkhāya": VD["dukkhāya"], "adukkhamasukhāya": f"{ADUKKHA} ခံစားမှု"}
for _k, _m in _VS.items():
    P(f"{_k} vedanāya sampayuttena kammena sahajāto kammūpacayo {_k} vedanāya sampayutto",
      V(f"{_m}နှင့် ယှဉ်တွဲသော {F.KAMMA}{SAHAJ} {KU}သည် {_m}နှင့် ယှဉ်တွဲသော {THING}"))
    P(f"{_k} vedanāya", FR(_m))
S("Kammūpacayo kammena sahajātoti, āmantā.", f"{KU}သည် {F.KAMMA}{SAHAJ} {THING} ဖြစ်သလော၊ {F.YES}{END}")
S("Kusalena kammena sahajāto kammūpacayo kusaloti, na hevaṃ vattabbe…pe….",
  f"{KUSALA} {F.KAMMA}{SAHAJ} {KU}သည် {KUSALA} ဖြစ်သလော၊ {F.NO_SAY}{PE}")
S("Aññaṃ kammaṃ añño kammūpacayoti, āmantā.", f"{F.KAMMA}နှင့် {KU}သည် {F.OTHER} ဖြစ်သလော၊ {F.YES}{END}")
SARAMM = W("1", "^1-M2-55", "sārammaṇā dhammā", "အာရုံ ရှိသော")
ANARAMM = W("1", "^1-M2-55", "anārammaṇā dhammā", "အာရုံ မရှိသော")
for _s, _sm, _sj in (("kammaṃ", F.KAMMA, "sahajātaṃ"), ("kammūpacayo", KU, "sahajāto")):
    _e = "aṃ" if _s == "kammaṃ" else "o"
    for _a, _am in (("sār", SARAMM), ("anār", ANARAMM)):
        P(f"{_s} cittena {_sj}, {_s} {_a}ammaṇ{_e}",
          V(f"{_sm}သည် {CITTA}{SAHAJ} {THING} ဖြစ်၍ {_sm}သည် {_am} {THING}"))
    for _n, _neg in (("", False), ("na ", True)):
        P(f"{_s} cittena {_sj}, cittaṃ bhijjamānaṃ {_s} {_n}bhijjati",
          Cl(f"{_sm}သည် {CITTA}{SAHAJ} {THING} ဖြစ်၍ {CITTA} ပျက်သည်ရှိသော် {_sm}", "ပျက်", "မပျက်", neg=_neg))
for _s, _sm in (("kammūpacayo", KU), ("vipāko", VIPAKA_N)):
    for _a, _am in (("sār", SARAMM), ("anār", ANARAMM)):
        P(f"{_s} {_a}ammaṇo", V(f"{_sm}သည် {_am} {THING}"))
P("kammamhi kammūpacayo", V(f"{F.KAMMA}၌ {KU}", EXIST))
P("taññeva kammaṃ so kammūpacayo", V(f"ထို{F.KAMMA}ပင် ထို{KU}"))
P("kammamhi kammūpacayo, kammūpacayato vipāko nibbattati",
  Cl(f"{F.KAMMA}၌ {KU} ရှိ၍ {KU}မှ {VIPAKA_N}", *ARISE))
P("taññeva kammaṃ, so kammūpacayo, so kammavipāko", V(f"ထို{F.KAMMA}ပင် ထို{KU} ဖြစ်၍ ထို{VIPAKA_N}"))
P("kammamhi kammūpacayo, kammūpacayato vipāko nibbattati, vipāko sārammaṇo",
  V(f"{F.KAMMA}၌ {KU} ရှိ၍ {KU}မှ {VIPAKA_N} ဖြစ်ပေါ်၍ {VIPAKA_N}သည် {SARAMM} {THING}"))
_SB = "ဆင်းရဲစေတတ်သည်လည်း ဖြစ် မဆင်းရဲစေတတ်သည်လည်း ဖြစ်သော"                         # sabyābajjhampi abyābajjhampi
new("sabyābajjhampi abyābajjhampi", _SB)
Q("idha, puṇṇa, ekacco sabyābajjhampi abyābajjhampi kāyasaṅkhāraṃ abhisaṅkharoti, sabyābajjhampi abyābajjhampi "
  "vacīsaṅkhāraṃ…pe… manosaṅkhāraṃ abhisaṅkharoti, so sabyābajjhampi abyābajjhampi kāyasaṅkhāraṃ abhisaṅkharitvā, "
  "sabyābajjhampi abyābajjhampi vacīsaṅkhāraṃ…pe… manosaṅkhāraṃ abhisaṅkharitvā sabyābajjhampi abyābajjhampi lokaṃ "
  "upapajjati. Tamenaṃ sabyābajjhampi abyābajjhampi lokaṃ upapannaṃ samānaṃ sabyābajjhāpi abyābajjhāpi phassā "
  "phusanti. So sabyābajjhehipi abyābajjhehipi phassehi phuṭṭho samāno sabyābajjhampi abyābajjhampi vedanaṃ vedeti "
  "vokiṇṇasukhadukkhaṃ, seyyathāpi manussā ekacce ca devā ekacce ca vinipātikā. Iti kho, puṇṇa, bhūtā bhūtassa "
  "upapatti hoti, yaṃ karoti tena upapajjati, upapannametaṃ phassā phusanti. Evampāhaṃ, puṇṇa, kammadāyādā sattāti "
  "vadāmi",
  f"ပုဏ္ဏ၊ ဤလောက၌ အချို့သော သူသည် {_SB} ⟦b⟧ ကိုယ်ဖြင့် ပြုပြင်ဖန်တီးမှုကို ပြုပြင်ဖန်တီး၏၊ {_SB} နှုတ်ဖြင့် "
  f"ပြုပြင်ဖန်တီးမှုကို… စိတ်ဖြင့် ပြုပြင်ဖန်တီးမှုကို ပြုပြင်ဖန်တီး၏၊ ထိုသူသည် {_SB} ကိုယ်ဖြင့် ပြုပြင်ဖန်တီးမှုကို "
  f"ပြုပြင်ဖန်တီး၍ {_SB} နှုတ်ဖြင့် ပြုပြင်ဖန်တီးမှုကို… စိတ်ဖြင့် ပြုပြင်ဖန်တီးမှုကို ပြုပြင်ဖန်တီး၍ {_SB} လောက၌ "
  f"ပြန်လည် ဖြစ်ပေါ်၏။ {_SB} လောက၌ ပြန်လည် ဖြစ်ပေါ်နေသော ထိုသူကို {_SB} တွေ့ထိမှုတို့ တွေ့ထိကုန်၏။ "
  f"ထိုသူသည် {_SB} တွေ့ထိမှုတို့ တွေ့ထိခြင်း ခံရလျက် {_SB}၊ သာယာမှု နာကျင်မှု ရောယှက်နေသော ခံစားမှုကို ခံစား၏၊ "
  f"ဥပမာ လူတို့၊ အချို့သော နတ်တို့နှင့် အချို့သော အပါယ်သားတို့ကဲ့သို့တည်း။ ပုဏ္ဏ၊ ဤသို့လျှင် ဖြစ်ပြီးသော "
  f"သတ္တဝါမှ ဖြစ်ပေါ်မည့် သတ္တဝါ၏ ပြန်လည် ဖြစ်ပေါ်ခြင်း ဖြစ်၏၊ အကြင် ကံကို ပြု၏၊ ထိုကံဖြင့် ပြန်လည် "
  f"ဖြစ်ပေါ်၏၊ ပြန်လည် ဖြစ်ပေါ်ပြီးသော ထိုသူကို တွေ့ထိမှုတို့ တွေ့ထိကုန်၏။ ပုဏ္ဏ၊ ဤသို့လည်း ငါသည် ‹{F.SATTA}တို့သည် "
  f"ကံ၏ အမွေခံတို့ ဖြစ်ကုန်၏›ဟု ဆို၏")
BR_X["[sabyāpajjhampi abyāpajjhampi (ka.) ma. ni. 2.81 passitabbaṃ]"] = (
    f"[{F.LEKHANA} (Ka.): sabyāpajjhampi abyāpajjhampi၊ {F.REF['ma. ni.']} 2.81 ကြည့်ပါ]")
S("Aññaṃ kammaṃ añño kammūpacayoti, āmantā.", f"{F.KAMMA}နှင့် {KU}သည် {F.OTHER} ဖြစ်သလော၊ {F.YES}{END}")
PAT_SAM = W("1", "^1-1343", "paṭiccasamuppādakusalatā", "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ")
LINES_X[key("Paccayatā vavatthitā, paṭiccasamuppādo, addhā, khaṇo layo muhuttaṃ, cattāro āsavā anāsavā, lokuttarānaṃ "
            "dhammānaṃ jarāmaraṇaṃ lokuttarā, saññāvedayitanirodhasamāpatti lokuttarā, saññāvedayitanirodhasamāpatti "
            "lokiyā, saññāvedayitanirodhaṃ samāpanno kālaṃ kareyya, sveva maggo asaññasattupapattiyā, aññaṃ kammaṃ "
            "añño kammūpacayoti.")] = (
    f"{PCT}သည် ပိုင်းခြား သတ်မှတ်ပြီး ဖြစ်ခြင်း၊ {PAT_SAM}၊ "
    f"{ADDHA}၊ {KLM['khaṇo']} {KLM['layo']} {KLM['muhuttaṃ']}၊ {_AS4}တို့သည် {_ANAS_MY[0]} {THING} ဖြစ်ခြင်း၊ "
    f"{LOKUTTARA} {P6.DH_PL}၏ {JM}သည် {LOKUTTARA} {THING} ဖြစ်ခြင်း၊ {SVS}သည် {LOKUTTARA} {THING} ဖြစ်ခြင်း၊ "
    f"{SVS}သည် {LOKIYA} {THING} ဖြစ်ခြင်း၊ {SVP}သည် သေခြင်း၊ ထိုမဂ်ပင် {W('2', '^2-1015', 'asaññasattānaṃ devānaṃ', 'အသညသတ်')} "
    f"ဘုံ၌ ဖြစ်ပေါ်ရန်၊ {F.KAMMA}နှင့် {KU}သည် {F.OTHER} ဖြစ်ခြင်း{END}")
PANNASA = new("paṇṇāsaka", "ငါးဆယ်အစု")
LINES_X["Tatiyo paṇṇāsako."] = f"{F.ORD_MY[3]} {PANNASA}{END}"
LINES_X[key("Anusayā, saṃvaro, kappo, mūlañca vavatthitāti.")] = (
    f"{ANU}တို့၊ စောင့်စည်းမှု၊ {KAPPA}၊ အမြစ်နှင့် ပိုင်းခြား သတ်မှတ်ခြင်း{END}")


# ===================================================================================== 156. Niggahakathā / 157. Paggahakathā
PARO = "တစ်ဦးသည် အခြားသူ၏"                                           # paro parassa (+ genitive object)
NIGG = ("ချုပ်ကိုင်", "မချုပ်ကိုင်")                                     # niggaṇhāti (restrains; not the dialectic niggaha)
PAGG = ("မြှင့်တင်", "မမြှင့်တင်")                                       # paggaṇhāti
new("niggaṇhāti / paggaṇhāti (a mind)", f"{NIGG[0]} / {PAGG[0]}")
section("(156) 1. Niggahakathā", f"(156) 1. စိတ်ကို {NIGG[0]}ခြင်းအကြောင်း {KATHA}")
section("Niggahakathā", f"စိတ်ကို {NIGG[0]}ခြင်းအကြောင်း {KATHA}")
section("(157) 2. Paggahakathā", f"(157) 2. စိတ်ကို {PAGG[0]}ခြင်းအကြောင်း {KATHA}")
section("Paggahakathā", f"စိတ်ကို {PAGG[0]}ခြင်းအကြောင်း {KATHA}")
_MA4 = "«မတပ်မက်နှင့်»၊ «ဒေါသ မဖြစ်နှင့်»၊ «မတွေဝေနှင့်»၊ «မညစ်နွမ်းနှင့်»ဟု"
_UPN = "ဖြစ်ပေါ်ပြီးသော"                                               # uppanna (pi-1 termbase)
_MN = "«မချုပ်ငြိမ်းနှင့်»ဟု"
_UP9 = ["vedanā", "saññā", "cetanā", "cittaṃ", "saddhā", "vīriyaṃ", "sati", "samādhi", "paññā"]
_UP9M = dict(zip(_UP9, [F.VEDANA.my, F.SANNA.my, "စေ့ဆော်မှု", CITTA, "ယုံကြည်မှု", "ဝီရိယ", "သတိ", "သမာဓိ", "ပညာ"]))
for _v, _vm, _vv in (("niggaṇhāti", NIGG, "niggaṇhāti"), ("paggaṇhāti", PAGG, "paggaṇhāti")):
    P(f"paro parassa cittaṃ {_v}", Cl(f"{PARO} {CITTA}ကို", *_vm))
    for _sep in (", ", ","):
        P(f"paro parassa cittaṃ {_sep.join(['mā rajji', 'mā dussi', 'mā muyhi', 'mā kilissīti'])} {_v}",
          Cl(f"{PARO} {CITTA}ကို {_MA4}", *_vm))
    P(f"paro parassa uppanno phasso mā nirujjhīti {_v}", Cl(f"{PARO} {_UPN} တွေ့ထိမှုကို {_MN}", *_vm))
    P(f"paro parassa uppannā vedanā…pe… uppannā saññā… uppannā cetanā… uppannaṃ cittaṃ… uppannā saddhā… uppannaṃ "
      f"vīriyaṃ… uppannā sati… uppanno samādhi…pe… uppannā paññā mā nirujjhīti {_v}",
      Cl(f"{PARO} " + "… ".join(f"{_UPN} {_UP9M[x]}" for x in _UP9[:-1]) + f"… {_UPN} ပညာကို {_MN}", *_vm))
    P(f"paro parassa uppannā vedanā…pe… uppannā paññā mā nirujjhīti {_v}",
      Cl(f"{PARO} {_UPN} {F.VEDANA.my}… {_UPN} ပညာကို {_MN}", *_vm))
PAROA = "တစ်ဦးသည် အခြားသူ၏ အကျိုးအတွက်"                                 # paro parassa atthāya
P("paro parassa atthāya rāgaṃ pajahati", VV(f"{PAROA} ရာဂကို", "ပယ်"))
P("dosaṃ pajahati", VV("ဒေါသကို", "ပယ်"))
P("mohaṃ pajahati", VV("မောဟကို", "ပယ်"))
P("anottappaṃ pajahati", VV(f"{P6.KIL['anottappaṃ']}ကို", "ပယ်"))
P("paro parassa atthāya maggaṃ bhāveti", VV(f"{PAROA} မဂ်ကို", "ပွားများ"))
P("satipaṭṭhānaṃ bhāveti", VV(f"{SATIP}ကို", "ပွားများ"))
P("bojjhaṅgaṃ bhāveti", VV(f"{BJW}ကို", "ပွားများ"))
P("paro parassa atthāya dukkhaṃ parijānāti, samudayaṃ pajahati, nirodhaṃ sacchikaroti, maggaṃ bhāveti",
  VV(f"{PAROA} {P11.DK_ALL_MY.rsplit(' ', 1)[0]}", P11.DK_ALL_MY.rsplit(" ", 1)[1]))
_DK1 = P11.DK_ALL_MY.split("၊ ")
P("paro parassa atthāya dukkhaṃ parijānāti…pe… maggaṃ bhāveti",
  VV(f"{PAROA} {_DK1[0][:-len('သည်')]}… {_DK1[-1].rsplit(' ', 1)[0]}", _DK1[-1].rsplit(" ", 1)[1]))
P("añño aññassa kārako, paraṅkataṃ sukhaṃ dukkhaṃ añño karoti añño paṭisaṃvedeti",
  V(f"တစ်ယောက်သည် အခြားတစ်ယောက်၏ {MS.KARAKA} ဖြစ်၍ သူတစ်ပါး ပြုထားသော သုခ ဒုက္ခကို တစ်ယောက်က ပြု၍ "
    "အခြားတစ်ယောက်က", "ခံစား"))
_PAPA = "ယုတ်မာမှု"                                                     # pāpa
for _p, _m in (('"Attanāva kataṃ pāpaṃ, attanā saṃkilissati;',
                f"“မိမိကိုယ်တိုင်ပင် ပြုသော {_PAPA}ဖြင့် မိမိကိုယ်တိုင် ညစ်နွမ်း၏၊"),
               ("Attanā akataṃ pāpaṃ, attanāva visujjhati;",
                f"မိမိကိုယ်တိုင် မပြုသော {_PAPA}ဖြင့် မိမိကိုယ်တိုင်ပင် စင်ကြယ်၏၊"),
               ('Suddhi asuddhi paccattaṃ, nāñño aññaṃ visodhaye"ti [dha. pa. 165].',
                "စင်ကြယ်ခြင်း မစင်ကြယ်ခြင်းသည် ကိုယ်စီ ဖြစ်၏၊ တစ်ယောက်သည် အခြားတစ်ယောက်ကို မစင်ကြယ်စေနိုင်”ဟူ၍ ⟦0⟧။")):
    LINES_X[key(_p)] = _m
Q("attanāva kataṃ pāpaṃ…pe… nāñño aññaṃ visodhaye",
  f"မိမိကိုယ်တိုင်ပင် ပြုသော {_PAPA}ဖြင့်… တစ်ယောက်သည် အခြားတစ်ယောက်ကို မစင်ကြယ်စေနိုင်")
P("atthi balappattā, atthi vasībhūtā", Cl("စွမ်းအားသို့ ရောက်ပြီးသူတို့ ရှိ၍ အလိုအတိုင်း ဖြစ်စေနိုင်သူတို့", *EXN))
for _k, _m in (("alobhaṃ", "လောဘ မရှိခြင်း"), ("adosaṃ", "ဒေါသ မရှိခြင်း"), ("amohaṃ", "မောဟ မရှိခြင်း")):
    P(f"{_k} kusalamūlaṃ janeti", VV(f"{_m} ဟူသော {KM}ကို", "ဖြစ်စေ"))
P("paro parassa alobhaṃ kusalamūlaṃ janeti", VV(f"တစ်ဦးသည် အခြားသူအား လောဘ မရှိခြင်း ဟူသော {KM}ကို", "ဖြစ်စေ"))
for _k, _m in (("saddhaṃ", "ယုံကြည်မှု"), ("vīriyaṃ", "ဝီရိယ"), ("satiṃ", "သတိ"), ("samādhiṃ", "သမာဓိ"),
               ("paññaṃ", "ပညာ")):
    P(f"{_k} janeti", VV(f"{_m}ကို", "ဖြစ်စေ"))

# ===================================================================================== 158. Sukhānuppadānakathā
GIVEH = ("ပေး", "မပေး")
section("(158) 3. Sukhānuppadānakathā", f"(158) 3. သုခကို ပေးခြင်းအကြောင်း {KATHA}")
section("Sukhānuppadānakathā", f"သုခကို ပေးခြင်းအကြောင်း {KATHA}")
PAROD = "တစ်ဦးသည် အခြားသူအား"                                           # paro parassa (+ dative)
for _k, _m in (("sukhaṃ", "သုခ"), ("dukkhaṃ", "ဒုက္ခ")):
    for _n, _neg in (("", False), ("na ", True)):
        P(f"paro parassa {_k} {_n}anuppadeti", Cl(f"{PAROD} {_m}ကို", *GIVEH, neg=_neg))
P("paro parassa attano sukhaṃ anuppadeti, aññesaṃ sukhaṃ anuppadeti, tassa sukhaṃ anuppadeti",
  Cl(f"{PAROD} မိမိ၏ သုခကို ပေး၍ အခြားသူတို့၏ သုခကို ပေး၍ ထိုသူ၏ သုခကို", *GIVEH))
P("paro parassa nevattano, na aññesaṃ, na tassa sukhaṃ anuppadeti",
  Cl(f"{PAROD} မိမိ၏ သုခကိုလည်း မပေး၊ အခြားသူတို့၏ သုခကိုလည်း မပေး၊ ထိုသူ၏ သုခကိုလည်း", *GIVEH, neg=True))
UDAYI = f"{P11.AYASMA} ဥဒါယီ"
Q("bahūnaṃ vata no bhagavā dukkhadhammānaṃ apahattā, bahūnaṃ vata no bhagavā sukhadhammānaṃ upahattā, bahūnaṃ vata "
  "no bhagavā akusalānaṃ dhammānaṃ apahattā, bahūnaṃ vata no bhagavā kusalānaṃ dhammānaṃ upahattā",
  f"{BUDDHA}သည် ငါတို့အား ဆင်းရဲစေသော သဘောတရား များစွာကို ဖယ်ရှားပေးတော်မူခဲ့ပေစွ၊ {BUDDHA}သည် ငါတို့အား "
  f"ချမ်းသာစေသော သဘောတရား များစွာကို ဆောင်ယူပေးတော်မူခဲ့ပေစွ၊ {BUDDHA}သည် ငါတို့အား {AKUSALA} သဘောတရား "
  f"များစွာကို ဖယ်ရှားပေးတော်မူခဲ့ပေစွ၊ {BUDDHA}သည် ငါတို့အား {KUSALA} သဘောတရား များစွာကို ဆောင်ယူပေးတော်မူခဲ့ပေစွ")
REF_NOTE_X["laṭukikopame"] = "“လဋုကိကောပမ” သုတ်၌"


@F.frame(r"Nanu āyasmā udāyī etadavoca – (?P<x>.+?)ti!")
def _f_udayi(m):
    """Nanu āyasmā udāyī etadavoca – "Q"ti! (^5-748; ch11-12 «… ဤသို့ ပြောခဲ့သည် မဟုတ်လော –»)."""
    return f"{UDAYI}သည် ဤသို့ ပြောခဲ့သည် မဟုတ်လော – “{F.q_set(F.QUOTE_RAW(m['x']), 1)}”{END}"


before_generic()

# ===================================================================================== 159. Adhigayhamanasikārakathā
ADHIG = new("adhigayha manasi karoti", f"အလုံးစုံကို စုပေါင်း၍ {MK11[0]}")
section("(159) 4. Adhigayhamanasikārakathā", f"(159) 4. အလုံးစုံကို စုပေါင်း၍ နှလုံးသွင်းခြင်းအကြောင်း {KATHA}")
section("Adhigayhamanasikārakathā", f"အလုံးစုံကို စုပေါင်း၍ နှလုံးသွင်းခြင်းအကြောင်း {KATHA}")
P("adhigayha manasi karoti", Cl("အလုံးစုံကို စုပေါင်း၍", *MK11))
P("tena cittena taṃ cittaṃ pajānāti", VV(f"ထို{CITTA}ဖြင့် ထို{CITTA}ကို", "သိ"))
P("tena cittena taṃ cittaṃ cittanti pajānāti", VV(f"ထို{CITTA}ဖြင့် ထို{CITTA}ကို «{CITTA}»ဟု", "သိ"))
P("taṃ cittaṃ tassa cittassa ārammaṇaṃ", V(f"ထို{CITTA}သည် ထို{CITTA}၏ အာရုံ"))
P("tena phassena taṃ phassaṃ phusati, tāya vedanāya…pe… tāya saññāya… tāya cetanāya… tena cittena… tena vitakkena… "
  "tena vicārena… tāya pītiyā… tāya satiyā… tāya paññāya taṃ paññaṃ pajānāti",
  VV(f"ထိုတွေ့ထိမှုဖြင့် ထိုတွေ့ထိမှုကို တွေ့ထိ၍ " + "… ".join(f"ထို{n}ဖြင့်" for _, n, _ in _SELF[1:-1])
     + f"… ထို{_SELF[-1][1]}ဖြင့် ထို{_SELF[-1][1]}ကို", _SELF[-1][2]))
TM = {"atīt": P6.ATITA, "anāgat": P6.ANAGATA, "paccuppann": P6.PACCUP}
_ORD3 = list(TM)
for _a in _ORD3:
    _rest = [x for x in _ORD3 if x != _a]
    _head = f"{_a}aṃ {_a}anti manasikaronto"
    _hm = f"{TM[_a]}ကို «{TM[_a]}»ဟု နှလုံးသွင်းနေစဉ်"
    for _b in _rest:
        P(f"{_head}, {_b}aṃ {_b}anti manasi karoti", Cl(f"{_hm} {TM[_b]}ကို «{TM[_b]}»ဟု", *MK11))
    _b, _c = _rest
    P(f"{_head}, {_b}aṃ {_b}anti manasi karoti, {_c}aṃ {_c}anti manasi karoti",
      Cl(f"{_hm} {TM[_b]}ကို «{TM[_b]}»ဟု နှလုံးသွင်း၍ {TM[_c]}ကို «{TM[_c]}»ဟု", *MK11))
P("tiṇṇaṃ phassānaṃ…pe… tiṇṇaṃ cittānaṃ samodhānaṃ hoti",
  V(f"တွေ့ထိမှု {F.NUM_MY[3]}{F.CL}… {CITTA} {F.NUM_MY[3]}{F.CL}တို့၏ ပေါင်းဆုံခြင်း"))
_ANICC = W("2", "^2-154", "Cakkhuṃ aniccaṃ", "မမြဲ")
_ANATT = W("2", "^2-154", "anattā", "အတ္တ မဟုတ်")
_SK = f"ပြုပြင်ဖန်တီးမှု အားလုံးတို့သည်"
_ATHA = "ထိုအခါ ဒုက္ခ၌ ငြီးငွေ့၏၊ ဤသည်ကား စင်ကြယ်ခြင်းသို့ ရောက်ကြောင်း လမ်း ဖြစ်၏"
for _p, _m in (('"Sabbe saṅkhārā aniccāti, yadā paññāya passati;', f"“{_SK} {_ANICC}ကုန်ဟု အကြင်အခါ ပညာဖြင့် မြင်၏၊"),
               ("Atha nibbindati dukkhe, esa maggo visuddhiyā.", f"{_ATHA}။"),
               ('"Sabbe saṅkhārā dukkhāti, yadā paññāya passati;', f"“{_SK} ဒုက္ခ ဖြစ်ကုန်ဟု အကြင်အခါ ပညာဖြင့် မြင်၏၊"),
               ('"Sabbe dhammā anattāti, yadā paññāya passati;',
                f"“{P6.ALL_DH}တို့သည် {_ANATT}ကုန်ဟု အကြင်အခါ ပညာဖြင့် မြင်၏၊"),
               ('Atha nibbindati dukkhe, esa maggo visuddhiyā"ti [dha. pa. 277-279].', f"{_ATHA}”ဟူ၍ ⟦0⟧{END}")):
    LINES_X[key(_p)] = _m

# ===================================================================================== 160-163. Rūpaṃ hetu / sahetukaṃ / kusalākusalaṃ / vipāko
HETU = "အမြစ်"
SAHET = W("1", "^1-M2-2", "sahetukā dhammā", "အမြစ် ရှိသော")
section("(160) 5. Rūpaṃ hetūtikathā", f"(160) 5. ရုပ်သည် {HETU} ဖြစ်သည်ဟူသော {KATHA}")
section("Rūpaṃ hetūtikathā", f"ရုပ်သည် {HETU} ဖြစ်သည်ဟူသော {KATHA}")
section("(161) 6. Rūpaṃ sahetukantikathā", f"(161) 6. ရုပ်သည် {SAHET} အရာ ဖြစ်သည်ဟူသော {KATHA}")
section("Rūpaṃ sahetukantikathā", f"ရုပ်သည် {SAHET} အရာ ဖြစ်သည်ဟူသော {KATHA}")
section("(162) 7. Rūpaṃ kusalākusalantikathā", f"(162) 7. ရုပ်သည် {KUSALA} {AKUSALA} ဖြစ်သည်ဟူသော {KATHA}")
section("Rūpaṃ kusalākusalantikathā", f"ရုပ်သည် {KUSALA} {AKUSALA} ဖြစ်သည်ဟူသော {KATHA}")
section("(163) 8. Rūpaṃ vipākotikathā", f"(163) 8. ရုပ်သည် {VIPAKA_N} ဖြစ်သည်ဟူသော {KATHA}")
section("Rūpaṃ vipākotikathā", f"ရုပ်သည် {VIPAKA_N} ဖြစ်သည်ဟူသော {KATHA}")
H6 = {"alobho": "လောဘ မရှိခြင်း", "adoso": "ဒေါသ မရှိခြင်း", "amoho": "မောဟ မရှိခြင်း", "lobho": LOBHA,
      "doso": "ဒေါသ", "moho": "မောဟ"}
AVP = f"ထိုအရာ၏ {AVT}… {PANIDHI}"                                        # tassa āvaṭṭanā…pe… paṇidhi
AVPF = f"ထိုအရာ၏ {AVT}… {PANIDHI}"                                       # tāya (feminine): the same Burmese
P("rūpaṃ hetu", V(f"ရုပ်သည် {HETU}"))
for _k, _m in H6.items():
    P(f"{_k} hetu", V(f"{_m}သည် {HETU}"))
for _a, _an, _ex in (("sār", SARAMM, False), ("anār", ANARAMM, True)):
    _at = "natthi" if _ex else "atthi"
    _tail = f"{AVP}"
    P(f"{_a}ammaṇaṃ, {_at} tassa āvaṭṭanā…pe… paṇidhi", V(f"{_an} {THING} ဖြစ်၍ {_tail}", EXIST, neg=_ex))
def hp(subj, pred, a, ex, fem=False):
    """X (pred) sār-/anārammaṇo, atthi / natthi tassa (tāya) āvaṭṭanā…pe… paṇidhi."""
    return V(f"{subj}သည် {pred}{' ' if pred else ''}{a} {THING} ဖြစ်၍ {AVPF if fem else AVP}", EXIST, neg=ex)


_PR = {"hetu": HETU + " ဖြစ်၍", "sahetuk": SAHET + " အရာ ဖြစ်၍", "kusal": KUSALA + " ဖြစ်၍",
       "akusal": AKUSALA + " ဖြစ်၍"}
for _s, _sm in list(H6.items()) + [("rūpaṃ", F.RUPA.my)]:
    for _a, _an, _ex in (("sār", SARAMM, False), ("anār", ANARAMM, True)):
        _at = "natthi" if _ex else "atthi"
        _neut = _s == "rūpaṃ"
        _e = "aṃ" if _neut else "o"
        P(f"{_s} hetu {_a}ammaṇ{_e}, {_at} tassa āvaṭṭanā…pe… paṇidhi", hp(_sm, _PR["hetu"], _an, _ex))
        P(f"{_s} sahetuk{_e} {_a}ammaṇ{_e}, {_at} tassa āvaṭṭanā…pe… paṇidhi", hp(_sm, _PR["sahetuk"], _an, _ex))
        for _q in ("kusal", "akusal"):
            P(f"{_s} {_q}{_e} {_a}ammaṇ{_e}, {_at} tassa āvaṭṭanā…pe… paṇidhi", hp(_sm, _PR[_q], _an, _ex))
P("mahābhūtā upādāyarūpānaṃ upādāyahetu", V(f"{MAHAB}တို့သည် {MAHAB}တို့ကို မှီ၍ ဖြစ်သော ရုပ်တို့၏ မှီရာ {HETU}"))
ANCHOR_X["upādāyarūpānaṃ"] = "မှီ၍ ဖြစ်သော ရုပ်တို့၏"
VAR_X["upādārūpānaṃ"] = F.LEKHANA
P("rūpaṃ sahetukaṃ", V(f"ရုပ်သည် {SAHET} {THING}"))
for _k, _m in (("alobha", "လောဘ မရှိခြင်း"), ("adosa", "ဒေါသ မရှိခြင်း"), ("amoha", "မောဟ မရှိခြင်း"), ("lobha", LOBHA),
               ("dosa", "ဒေါသ"), ("moha", "မောဟ")):
    P(f"{_k}hetunā", V(f"{_m} ဟူသော {HETU}ဖြင့်"))
P("rūpaṃ sappaccayaṃ", V(f"ရုပ်သည် {F.SAPPACCAYA} {THING}"))
_SH19 = ["adoso", "amoho", "saddhā", "vīriyaṃ", "sati", "samādhi", "paññā", "lobho", "doso", "moho", "māno", "diṭṭhi",
         "vicikicchā", "thinaṃ", "uddhaccaṃ", "ahirikaṃ", "anottappaṃ"]
_SH19M = {"adoso": H6["adoso"], "amoho": H6["amoho"], "saddhā": "ယုံကြည်မှု", "vīriyaṃ": "ဝီရိယ", "sati": "သတိ",
          "samādhi": "သမာဓိ", "paññā": "ပညာ", "lobho": LOBHA, "doso": "ဒေါသ", "moho": "မောဟ"}
_SH19M.update({k: P6.KIL[k] for k in ("māno", "diṭṭhi", "vicikicchā", "thinaṃ", "uddhaccaṃ", "ahirikaṃ", "anottappaṃ")})
for _a, _an, _ex in (("sār", SARAMM, False), ("anār", ANARAMM, True)):
    _at = "natthi" if _ex else "atthi"
    P(f"adoso sahetuko…pe… amoho… saddhā… vīriyaṃ… sati… samādhi… paññā… lobho… doso… moho… māno… diṭṭhi… "
      f"vicikicchā… thinaṃ… uddhaccaṃ… ahirikaṃ… anottappaṃ sahetukaṃ {_a}ammaṇaṃ, {_at} tassa āvaṭṭanā…pe… paṇidhi",
      V(f"{H6['adoso']}သည် {SAHET} အရာ ဖြစ်၍… " + "… ".join(_SH19M[x] for x in _SH19[1:-1])
        + f"… {_SH19M['anottappaṃ']}သည် {SAHET} အရာ ဖြစ်၍ {_an} {THING} ဖြစ်၍ {AVP}", EXIST, neg=_ex))
    P(f"adoso sahetuko…pe… anottappaṃ sahetukaṃ {_a}ammaṇaṃ, {_at} tassa āvaṭṭanā…pe… paṇidhi",
      V(f"{H6['adoso']}သည် {SAHET} အရာ ဖြစ်၍… {_SH19M['anottappaṃ']}သည် {SAHET} အရာ ဖြစ်၍ {_an} {THING} ဖြစ်၍ {AVP}",
        EXIST, neg=_ex))
for _k in ("kusal", "akusal"):
    P(f"rūpaṃ {_k}aṃ", V(f"ရုပ်သည် {KUSALA if _k == 'kusal' else AKUSALA}"))
for _a, _an, _ex in (("sār", SARAMM, False), ("anār", ANARAMM, True)):
    _at = "natthi" if _ex else "atthi"
    P(f"adoso kusalo…pe… amoho kusalo…pe… saddhā… vīriyaṃ… sati… samādhi…pe… paññā kusalā {_a}ammaṇā, {_at} tāya "
      "āvaṭṭanā…pe… paṇidhi",
      V(f"{H6['adoso']}သည် {KUSALA} ဖြစ်၍… {H6['amoho']}သည် {KUSALA} ဖြစ်၍… ယုံကြည်မှု… ဝီရိယ… သတိ… သမာဓိ… "
        f"ပညာသည် {KUSALA} ဖြစ်၍ {_an} {THING} ဖြစ်၍ {AVPF}", EXIST, neg=_ex))
    P(f"adoso kusalo…pe… paññā kusalā {_a}ammaṇā, {_at} tāya āvaṭṭanā…pe… paṇidhi",
      V(f"{H6['adoso']}သည် {KUSALA} ဖြစ်၍… ပညာသည် {KUSALA} ဖြစ်၍ {_an} {THING} ဖြစ်၍ {AVPF}", EXIST, neg=_ex))
    P(f"doso… moho… māno…pe… anottappaṃ akusalaṃ {_a}ammaṇaṃ, {_at} tassa āvaṭṭanā…pe… paṇidhi",
      V(f"ဒေါသ… မောဟ… {P6.KIL['māno']}… {P6.KIL['anottappaṃ']}သည် {AKUSALA} ဖြစ်၍ {_an} {THING} ဖြစ်၍ {AVP}",
        EXIST, neg=_ex))
    P(f"doso… moho…pe… anottappaṃ akusalaṃ {_a}ammaṇaṃ, {_at} tassa āvaṭṭanā…pe… paṇidhi",
      V(f"ဒေါသ… မောဟ… {P6.KIL['anottappaṃ']}သည် {AKUSALA} ဖြစ်၍ {_an} {THING} ဖြစ်၍ {AVP}", EXIST, neg=_ex))
for _s, _sm in (("rūpaṃ", F.RUPA.my), ("kāyakammaṃ vacīkammaṃ", "ကာယကံ ဝစီကံ")):
    P(f"{_s} kusalampi akusalampi", V(f"{_sm}သည် {KUSALA}လည်း ဖြစ် {AKUSALA}လည်း"))
P("rūpaṃ vipāko", V(f"ရုပ်သည် {VIPAKA_N}"))
SVD = {"sukha": "သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော", "dukkha": "နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော",
       "adukkhamasukha": f"{ADUKKHA} ခံစားမှုကို ဖြစ်စေတတ်သော"}
new("sukhavedaniya / dukkhavedaniya / adukkhamasukhavedaniya", " / ".join(SVD.values()))
_V3S = "၊ ".join(f"{_VS[x]}နှင့် ယှဉ်တွဲသော" for x in ("sukhāya", "dukkhāya", "adukkhamasukhāya"))
P("rūpaṃ sukhavedaniyaṃ dukkhavedaniyaṃ adukkhamasukhavedaniyaṃ, sukhāya vedanāya sampayuttaṃ, dukkhāya vedanāya "
  "sampayuttaṃ, adukkhamasukhāya vedanāya sampayuttaṃ, phassena sampayuttaṃ…pe… cittena sampayuttaṃ, sārammaṇaṃ, "
  "atthi tassa āvaṭṭanā…pe… paṇidhi",
  V(f"ရုပ်သည် {SVD['sukha']}၊ {SVD['dukkha']}၊ {SVD['adukkhamasukha']}၊ {_V3S}၊ တွေ့ထိမှုနှင့် ယှဉ်တွဲသော… "
    f"{CITTA}နှင့် ယှဉ်တွဲသော၊ {SARAMM} {THING} ဖြစ်၍ {AVP}", EXIST))
_NSD = f"{SVD['sukha']} {THING} မဟုတ်၊ {SVD['dukkha']} {THING} မဟုတ်"
for _s, _sm, _e in (("", "", "aṃ"), ("rūpaṃ ", "ရုပ်သည် ", "aṃ"), ("phasso ", "တွေ့ထိမှုသည် ", "o")):
    _n = "na sukhavedaniy" + _e + " na dukkhavedaniy" + _e
    P(f"{_s}{_n}…pe… anārammaṇ{_e}, natthi tassa āvaṭṭanā…pe… paṇidhi",
      V(f"{_sm}{_NSD}… {ANARAMM} {THING} ဖြစ်၍ {AVP}", EXIST, neg=True))
for _s, _sm, _e in (("rūpaṃ", "ရုပ်", "aṃ"), ("phasso", "တွေ့ထိမှု", "o")):
    P(f"{_s} vipāko, {_s} sukhavedaniy{_e} dukkhavedaniy{_e}…pe… sārammaṇ{_e}, atthi tassa āvaṭṭanā…pe… paṇidhi",
      V(f"{_sm}သည် {VIPAKA_N} ဖြစ်၍ {_sm}သည် {SVD['sukha']}၊ {SVD['dukkha']}… {SARAMM} {THING} ဖြစ်၍ {AVP}", EXIST))
    P(f"{_s} vipāko, {_s} na sukhavedaniy{_e} na dukkhavedaniy{_e}…pe… anārammaṇ{_e}, natthi tassa āvaṭṭanā…pe… "
      "paṇidhi", V(f"{_sm}သည် {VIPAKA_N} ဖြစ်၍ {_sm}သည် {_NSD}… {ANARAMM} {THING} ဖြစ်၍ {AVP}", EXIST, neg=True))
KATATTA = W("1", "^1-431", "kammassa katattā", "ကံကို ပြုခဲ့") + "သောကြောင့်"           # kammassa katattā
P("kammassa katattā uppannā cittacetasikā dhammā vipāko",
  V(f"{KATATTA} {_UPN} {W('1', '^1-1029', 'cittacetasikā dhammā', 'စိတ်နှင့် စိတ်၏ အဖော်')} {P6.DH_PL}သည် {VIPAKA_N}"))
P("kammassa katattā uppannaṃ rūpaṃ vipāko", V(f"{KATATTA} {_UPN} ရုပ်သည် {VIPAKA_N}"))

# ===================================================================================== 164. Rūpaṃ rūpāvacarārūpāvacarantikathā
section("(164) 9. Rūpaṃ rūpāvacarārūpāvacarantikathā",
        f"(164) 9. ရုပ်သည် {RUPA_AV} အရာ၊ {ARUPA_AV} အရာ ဖြစ်သည်ဟူသော {KATHA}")
section("Rūpaṃ rūpāvacarārūpāvacarantikathā", f"ရုပ်သည် {RUPA_AV} အရာ၊ {ARUPA_AV} အရာ ဖြစ်သည်ဟူသော {KATHA}")
for _k, _m in (("rūpāvacaraṃ", RUPA_AV), ("arūpāvacaraṃ", ARUPA_AV), ("kāmāvacaraṃ", KAMA_AV)):
    P(f"atthi rūpaṃ {_k}", V(f"{_m} ရုပ်", EXIST))
P("atthi rūpaṃ rūpāvacaraṃ, atthi rūpaṃ arūpāvacaraṃ", Cl(f"{RUPA_AV} ရုပ် ရှိ၍ {ARUPA_AV} ရုပ်", *EXN))
_SAM = ("samāpattesiyaṃ upapattesiyaṃ diṭṭhadhammasukhavihāraṃ, samāpattesiyena cittena upapattesiyena cittena "
        "diṭṭhadhammasukhavihārena cittena sahagataṃ sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ ekuppādaṃ ekanirodhaṃ ekavatthukaṃ "
        "ekārammaṇaṃ")
P(_SAM, V(f"{SMS}၊ {UPS}၊ {DDS} {THING} ဖြစ်၍ {SMS} {CITTA}၊ {UPS} {CITTA}၊ {DDS} {CITTA}တို့နှင့်{_SH} {THING}"))
_SAMN = ("na samāpattesiyaṃ na upapattesiyaṃ na diṭṭhadhammasukhavihāraṃ, na samāpattesiyena cittena na upapattesiyena "
         "cittena na diṭṭhadhammasukhavihārena cittena sahagataṃ sahajātaṃ saṃsaṭṭhaṃ sampayuttaṃ ekuppādaṃ ekanirodhaṃ "
         "ekavatthukaṃ ekārammaṇaṃ")
P(_SAMN, V(f"{_N3}၍ {_N3C} {_SH} {THING}"))
P("na samāpattesiyaṃ na upapattesiyaṃ na diṭṭhadhammasukhavihāraṃ, na samāpattesiyena cittena…pe… ekārammaṇaṃ",
  V(f"{_N3}၍ {SMS} {CITTA}နှင့် မဟုတ်… {_SH_E} {THING}"))
P("na samāpattesiyaṃ na upapattesiyaṃ…pe… ekavatthukaṃ ekārammaṇaṃ",
  V(f"{SMS} {THING} မဟုတ်၊ {UPS} {THING} မဟုတ်… မှီရာ တူသော၊ {_SH_E} {THING}"))
P("na samāpattesiyo na upapattesiyo na diṭṭhadhammasukhavihāro, na samāpattesiyena cittena…pe… ekavatthuko ekārammaṇo",
  V(f"{_N3}၍ {SMS} {CITTA}နှင့် မဟုတ်… မှီရာ တူသော၊ {_SH_E} {THING}"))
P("kāmāvacarakammassa katattā rūpaṃ kāmāvacaraṃ", V(f"{KAMA_AV} {F.KAMMA}ကို ပြုခဲ့သောကြောင့် ရုပ်သည် {KAMA_AV} {THING}"))
P("rūpāvacarakammassa katattā rūpaṃ rūpāvacaraṃ, arūpāvacarakammassa katattā rūpaṃ arūpāvacaraṃ",
  V(f"{RUPA_AV} {F.KAMMA}ကို ပြုခဲ့သောကြောင့် ရုပ်သည် {RUPA_AV} {THING} ဖြစ်၍ {ARUPA_AV} {F.KAMMA}ကို ပြုခဲ့သောကြောင့် "
    f"ရုပ်သည် {ARUPA_AV} {THING}"))

# ===================================================================================== 165. Rūpārūpadhātupariyāpannakathā
section("(165) 10. Rūpārūpadhātupariyāpannakathā", f"(165) 10. {DHX['rūpa']}၊ {DHX['arūpa']}၌ အကျုံးဝင်ခြင်းအကြောင်း {KATHA}")
section("Rūpārūpadhātupariyāpannakathā", f"{DHX['rūpa']}၊ {DHX['arūpa']}၌ အကျုံးဝင်ခြင်းအကြောင်း {KATHA}")
for _k in RG:
    P(f"{_k}rāgo {_k}dhātupariyāpanno", Cl(f"{RG[_k]}သည် {DHX[_k]}၌", *INC))
P("gandharāgo…pe… rasarāgo…pe… phoṭṭhabbarāgo phoṭṭhabbadhātupariyāpanno",
  Cl(f"{RG['gandha']}… {RG['rasa']}… {RG['phoṭṭhabba']}သည် {DHX['phoṭṭhabba']}၌", *INC))
P("rūparāgo rūpadhātupariyāpanno, arūparāgo arūpadhātupariyāpanno",
  Cl(f"{RG['rūpa']}သည် {DHX['rūpa']}၌ အကျုံးဝင်၍ {RG['arūpa']}သည် {DHX['arūpa']}၌", *INC))
COLO_X["Rūparāgo rūpadhātupariyāpanno arūparāgo arūpadhātupariyāpannotikathā niṭṭhitā"] = F.DONE.format(
    f"{RG['rūpa']}သည် {DHX['rūpa']}၌ အကျုံးဝင်၍ {RG['arūpa']}သည် {DHX['arūpa']}၌ အကျုံးဝင်သည်ဟူသော {KATHA}")
P("gandharāgo…pe… rasarāgo…pe… phoṭṭhabbarāgo", FR(f"{RG['gandha']}… {RG['rasa']}… {RG['phoṭṭhabba']}"))


@F.frame(r"(?P<p>[^–,]*?rāgo) na vattabbaṃ – (?P<q>.+?)ti\?")
def _f_x_navatt(m):
    """X na vattabbaṃ – "Q"ti? (no comma, ^5-772) = «Xကို ဤသို့ မဆိုသင့်သလော – “Q”»."""
    return f"{F.pq(m['p'], 'bare')}ကို ဤသို့ မဆိုသင့်သလော – “{F.pq(m['q'], 'stmt', 1)}”{END}"


before_generic()
LINES_X[key("Cittaniggaho, cittapaggaho, sukhānuppadānaṃ, adhigayha manasikāro, rūpaṃ hetu, rūpaṃ sahetukaṃ, rūpaṃ "
            "kusalampi akusalampi, rūpaṃ vipāko, atthi rūpaṃ rūpāvacaraṃ atthi rūpaṃ arūpāvacaraṃ, sabbe kilesā "
            "kāmadhātupariyāpannāti.")] = (
    f"{CITTA}ကို {NIGG[0]}ခြင်း၊ {CITTA}ကို {PAGG[0]}ခြင်း၊ သုခကို ပေးခြင်း၊ အလုံးစုံကို စုပေါင်း၍ နှလုံးသွင်းခြင်း၊ "
    f"ရုပ်သည် {HETU} ဖြစ်ခြင်း၊ ရုပ်သည် {SAHET} {THING} ဖြစ်ခြင်း၊ ရုပ်သည် {KUSALA}လည်း ဖြစ် {AKUSALA}လည်း ဖြစ်ခြင်း၊ "
    f"ရုပ်သည် {VIPAKA_N} ဖြစ်ခြင်း၊ {RUPA_AV} ရုပ် ရှိခြင်း {ARUPA_AV} ရုပ် ရှိခြင်း၊ ကိလေသာ အားလုံးတို့သည် "
    f"{DHX['kāma']}၌ အကျုံးဝင်ခြင်း{END}")


# ===================================================================================== 166. Arahato puññūpacayakathā
PUU = new("puññūpacayo", "ကောင်းမှု စုဆောင်းခြင်း")
APUU = new("apuññūpacayo", "မကောင်းမှု စုဆောင်းခြင်း")
ARL = f"{ARAHA}၌"
section("(166) 1. Arahato puññūpacayakathā", f"(166) 1. {ARAHA}၏ {PUU}အကြောင်း {KATHA}")
section("Arahato puññūpacayakathā", f"{ARAHA}၏ {PUU}အကြောင်း {KATHA}")
COLO_X["Atthi arahato puññūpacayotikathā niṭṭhitā"] = F.DONE.format(f"{ARL} {PUU} ရှိသည်ဟူသော {KATHA}")
for _k, _m in (("puññūpacayo", PUU), ("apuññūpacayo", APUU)):
    for _n, _neg in (("", False), ("n", True)):
        P(f"{_n}atthi arahato {_k}", V(f"{ARL} {_m}", EXIST, neg=_neg))
_PAS = W("2", "^2-817", "Puññābhisaṅkhāro", "ကောင်းမှု ဖြစ်စေသော ပြုပြင်ဖန်တီးမှု")
_ANS = W("2", "^2-817", "āneñjābhisaṅkhāro", "မတုန်လှုပ်သော ပြုပြင်ဖန်တီးမှု")
_SVT = [("gati", "လားရာ"), ("bhava", "ဘဝ"), ("issariya", "အစိုးရခြင်း"), ("adhipacca", "အကြီးအကဲ ဖြစ်ခြင်း"),
        ("mahābhoga", "များပြားသော စည်းစိမ်"), ("mahāparivāra", "များပြားသော အခြံအရံ"),
        ("devasobhagya", "နတ်တို့၏ ကောင်းသော ကံကြမ္မာ"), ("manussasobhagya", "လူတို့၏ ကောင်းသော ကံကြမ္မာ")]
_SVT_MY = [f"{m}သို့ ရောက်စေတတ်သော {F.KAMMA}ကို" for _, m in _SVT]
P("arahā puññābhisaṅkhāraṃ abhisaṅkharoti, āneñjābhisaṅkhāraṃ abhisaṅkharoti, "
  + ", ".join(f"{k}saṃvattaniyaṃ kammaṃ karoti" for k, _ in _SVT),
  VV(f"{ARAHA}သည် {_PAS}ကို ပြုပြင်ဖန်တီး၍ {_ANS}ကို ပြုပြင်ဖန်တီး၍ " + " ".join(f"{x} ပြု၍" for x in _SVT_MY[:-1])
     + f" {_SVT_MY[-1]}", "ပြု"))
ANCHOR_X["adhipaccasaṃvattaniyaṃ"] = "အကြီးအကဲ ဖြစ်ခြင်းသို့ ရောက်စေတတ်သော"
VAR_X["ādhipaccasaṃvattanikaṃ"] = F.LEKHANA
ACINA = {"ācināti": "စုဆောင်း", "apacināti": "ဖြိုဖျက်", "pajahati": "ပယ်", "upādiyati": "စွဲလမ်း",
         "visineti": "ဖြန့်ကြဲ", "ussineti": "စုပုံ", "vidhūpeti": "ငြိမ်းစေ", "sandhūpeti": "တောက်လောင်စေ"}  # make_ch2-5 ACINA
for _k, _v in ACINA.items():
    P(f"arahā {_k}", VV(f"{ARAHA}သည်", _v))
_N2 = {("ācināti", "apacināti"): "apacināti", ("pajahati", "upādiyati"): "pajahati",
       ("visineti", "ussineti"): "visineti", ("vidhūpeti", "sandhūpeti"): "vidhūpeti"}


def _nn(a, b):       # neva A na B Bitvā ṭhito = «မA၊ မB၊ Bပြီး၍ တည်နေသူ» (make_ch2-5 pattern)
    c = _N2[(a, b)]
    return f"မ{ACINA[a]}၊ မ{ACINA[b]}၊ {ACINA[c]}ပြီး၍ တည်နေသူ"


for _p in ("arahā nevācināti na apacināti apacinitvā ṭhito", "arahā nevācināti nāpacināti apacinitvā ṭhito"):
    P(_p, V(f"{ARAHA}သည် {_nn('ācināti', 'apacināti')}"))
P("arahā neva pajahati na upādiyati pajahitvā ṭhito, neva visineti na ussineti visinetvā ṭhito, neva vidhūpeti na "
  "sandhūpeti vidhūpetvā ṭhito",
  V(f"{ARAHA}သည် {_nn('pajahati', 'upādiyati')} ဖြစ်၍ {_nn('visineti', 'ussineti')} ဖြစ်၍ "
    f"{_nn('vidhūpeti', 'sandhūpeti')}"))
P("arahā neva vidhūpeti na sandhūpeti vidhūpetvā ṭhito", V(f"{ARAHA}သည် {_nn('vidhūpeti', 'sandhūpeti')}"))
P("arahā dānaṃ dadeyya", Cl(f"{ARAHA}သည် ဒါန", "ပြုရာ", "မပြုရာ"))
P("arahā cīvaraṃ dadeyya", Cl(f"{ARAHA}သည် {DANA_I['cīvaraṃ']}ကို", *GIVE))
P("arahā cetiyaṃ abhidakkhiṇaṃ kareyya", Cl(f"{ARAHA}သည် {CETIYA}ကို လက်ယာရစ်", "လှည့်ပတ်ရာ", "မလှည့်ပတ်ရာ"))

# ===================================================================================== 167. Natthi arahato akālamaccūtikathā
AKM_D = new("akālamaccu", "အချိန်မတန်မီ သေခြင်း")
AGH = "ရဟန္တာကို သတ်သူ"                                                 # arahantaghātako (make_ch2-5 KILL5, copied)
section("(167) 2. Natthi arahato akālamaccūtikathā", f"(167) 2. {ARL} {AKM_D} မရှိဟူသော {KATHA}")
section("Natthi arahato akālamaccūtikathā", f"{ARL} {AKM_D} မရှိဟူသော {KATHA}")
for _n, _neg in (("", False), ("n", True)):
    P(f"{_n}atthi arahato akālamaccu", V(f"{ARL} {AKM_D}", EXIST, neg=_neg))
    P(f"{_n}atthi arahantaghātako", V(AGH, EXIST, neg=_neg))
_VOR = W("2", "^2-U55", "Mātā jīvitā voropitā hoti", "အသက်မှ ချ")
_SJ, _ASJ = "အသက်နှင့် အသက် အကြွင်းအကျန် ရှိစဉ်", "အသက်နှင့် အသက် အကြွင်းအကျန် မရှိစဉ်"
new("sati / asati jīvite jīvitāvasese", f"{_SJ} / {_ASJ}")
S("Yo arahantaṃ jīvitā voropeti, sati jīvite jīvitāvasese jīvitā voropeti, asati jīvite jīvitāvasese jīvitā "
  "voropetīti?", f"{ARAHA}ကို {_VOR}သူသည် {_SJ} {_VOR}သလော၊ {_ASJ} {_VOR}သလော{END}")
S("Sati jīvite jīvitāvasese jīvitā voropetīti.", f"{_SJ} {_VOR}ပါသည်{END}")
P("sati jīvite jīvitāvasese jīvitā voropeti", VV(_SJ, _VOR))
S("Asati jīvite jīvitāvasese jīvitā voropetīti, natthi arahantaghātakoti?",
  f"{_ASJ} {_VOR}လျှင် {AGH} {NEXIST}သလော{END}")
for _n, _neg in (("", False), ("na ", True)):
    P(f"arahato kāye visaṃ {_n}kameyya, satthaṃ {_n}kameyya, aggi {_n}kameyya", hit_cl(f"{ARAHA}၏ {F.KAYA}၌", _neg))
_DD = W("4", "^4-131", "diṭṭhe ceva dhamme", "မျက်မှောက်ဘဝ၌ပင်")
Q("nāhaṃ, bhikkhave, sañcetanikānaṃ kammānaṃ katānaṃ upacitānaṃ appaṭisaṃveditvā byantībhāvaṃ vadāmi; tañca kho "
  "diṭṭheva dhamme upapajjaṃ vā apare vā pariyāye",
  f"{_R} စေ့ဆော်၍ ပြုခဲ့ ဆည်းပူးခဲ့သော ကံတို့၏ အကျိုးကို မခံစားရဘဲ ကုန်ဆုံးခြင်းကို ငါ မဟော၊ ထိုအကျိုးကိုလည်း "
  f"{_DD}ဖြစ်စေ၊ နောက်ဘဝ၌ဖြစ်စေ၊ နောက်ထပ် ဘဝအဆက်ဆက်၌ဖြစ်စေ ခံစားရ၏")

# ===================================================================================== 168. Sabbamidaṃ kammatotikathā
ALLT = "ဤအရာ အားလုံးသည်"                                               # sabbamidaṃ
section("(168) 3. Sabbamidaṃ kammatotikathā", f"(168) 3. {ALLT} {F.KAMMA}ကြောင့် ဖြစ်သည်ဟူသော {KATHA}")
section("Sabbamidaṃ kammatotikathā", f"{ALLT} {F.KAMMA}ကြောင့် ဖြစ်သည်ဟူသော {KATHA}")
KV = f"{F.KAMMA}၏ အကျိုး"                                                # kammavipāka
P("sabbamidaṃ kammato", V(f"{ALLT} {F.KAMMA}ကြောင့်"))
P("kammampi kammato", V(f"{F.KAMMA}သည်လည်း {F.KAMMA}ကြောင့်"))
P("sabbamidaṃ pubbekatahetu", V(f"{ALLT} ရှေးက ပြုခဲ့သော {F.KAMMA}ကို အကြောင်းပြု၍"))
P("sabbamidaṃ kammavipākato", V(f"{ALLT} {KV}ကြောင့်"))
P("kammavipākena pāṇaṃ haneyya", Cl(f"{KV}ကြောင့် သူ့အသက်ကို", "သတ်ရာ", "မသတ်ရာ"))
for _s, _sm in (("pāṇātipāto", F.PANATIPATA), ("kammavipāko", KV),
                ("gilānapaccayabhesajjaparikkhāro", _GL)):
    P(f"{_s} saphalo", V(f"{_sm}သည် {PHALA} ရှိသော {THING}"))
    P(f"{_s} aphalo", V(f"{_sm}သည် {PHALA} မရှိသော {THING}"))
_MIS = [("kammavipākena adinnaṃ ādiyeyya", f"{KV}ကြောင့် မပေးသည်ကို", "ယူရာ"),
        ("musā bhaṇeyya", "မုသား", "ပြောရာ"), ("pisuṇaṃ bhaṇeyya", "ကုန်းတိုက်သော စကား", "ပြောရာ"),
        ("pharusaṃ bhaṇeyya", "ကြမ်းတမ်းသော စကား", "ပြောရာ"), ("samphaṃ palapeyya", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား", "ပြောရာ"),
        ("sandhiṃ chindeyya", "အိမ်ကို", "ဖောက်ထွင်းရာ"), ("nillopaṃ hareyya", "ဓားပြ", "တိုက်ရာ"),
        ("ekāgārikaṃ kareyya", "အိမ်တစ်အိမ်တည်းကို ဝိုင်းဝန်း၍", "လုယက်ရာ"), ("paripanthe tiṭṭheyya", "လမ်း၌", "စောင့်ဆိုင်းလုယက်ရာ"),
        ("paradāraṃ gaccheyya", "သူ့မယားထံသို့", "သွားရာ"), ("gāmaghātakaṃ kareyya", "ရွာကို", "ဖျက်ဆီးရာ"),
        ("nigamaghātakaṃ kareyya", "နိဂုံးကို", "ဖျက်ဆီးရာ"), ("kammavipākena dānaṃ dadeyya", f"{KV}ကြောင့် ဒါန", "ပြုရာ")]
W("2", "^2-487", "adinnādānā veramaṇī", "မပေးသည်ကို ယူခြင်း")
W("2", "^2-487", "Musāvādā veramaṇī, pisuṇāya vācāya veramaṇī, pharusāya vācāya veramaṇī, samphappalāpā",
  "မုသား ပြောခြင်းမှ ကင်းဝေးခြင်း၊ ကုန်းတိုက်သော စကားမှ ကင်းဝေးခြင်း၊ ကြမ်းတမ်းသော စကားမှ ကင်းဝေးခြင်း၊ "
  "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား")
for _p, _pre, _v in _MIS:
    P(_p, Cl(_pre, _v, "မ" + _v))
for _p, _m in (('"Kammunā vattatī [vattati (pī. ka., ma. ni. 2.460), vattate (?)] loko, kammunā vattatī [vattati '
                '(pī. ka., ma. ni. 2.460), vattate (?)] pajā;', "“လောကသည် ကံကြောင့် ဖြစ်၏ ⟦0⟧၊ သတ္တဝါ အပေါင်းသည် "
                                                               "ကံကြောင့် ဖြစ်၏ ⟦1⟧၊"),
               ("Kammanibandhanā sattā, rathassāṇīva yāyato [ma. ni. 2.460; su. ni. 659].",
                "သွားနေသော ရထားသည် ဝင်ရိုးချောင်းဖြင့် ချည်နှောင်ထားသကဲ့သို့ သတ္တဝါတို့သည် ကံဖြင့် ချည်နှောင်ထားကြ၏ ⟦0⟧။"),
               ('"Kammena kittiṃ labhate pasaṃsaṃ,', "“ကံကြောင့် ကျော်စောခြင်း၊ ချီးမွမ်းခံရခြင်းကို ရ၏၊"),
               ("Kammena jāniñca vadhañca bandhaṃ;", "ကံကြောင့် ဆုံးရှုံးခြင်း၊ သတ်ဖြတ်ခံရခြင်း၊ နှောင်ဖွဲ့ခံရခြင်းကိုလည်း ရ၏၊"),
               ("Taṃ kammaṃ nānākaraṇaṃ viditvā,", "ထိုကံကို အမျိုးမျိုး ကွဲပြားစေတတ်သည်ဟု သိလျက်"),
               ('Kasmā vade natthi kammanti loke"ti.', f"ကံ {NEXIST}ဟု လောက၌ အဘယ်ကြောင့် ဆိုရာအံ့နည်း”ဟူ၍{END}")):
    LINES_X[key(_p)] = _m
BR_X["[vattati (pī. ka., ma. ni. 2.460), vattate (?)]"] = (
    f"[{F.LEKHANA} (Pī., Ka., {F.REF['ma. ni.']} 2.460): vattati၊ (မသေချာ): vattate]")

# ===================================================================================== 169. Indriyabaddhakathā
IB = new("indriyabaddha", f"{INDRIYA}တို့နှင့် ဆက်စပ်သော")
AIB = new("anindriyabaddha", f"{INDRIYA}တို့နှင့် မဆက်စပ်သော")
section("(169) 4. Indriyabaddhakathā", f"(169) 4. {IB} {THING}အကြောင်း {KATHA}")
section("Indriyabaddhakathā", f"{IB} {THING}အကြောင်း {KATHA}")
AN9 = MS.ANICCA                                                        # aniccaṃ … vipariṇāmadhammaṃ (sample)
_A9 = AN9.split("၊ ")
AN_PE1 = f"{'၊ '.join(_A9[:3])}… {_A9[-1]}"                             # aniccaṃ saṅkhataṃ paṭiccasamuppannaṃ…pe…
AN_PE2 = f"{'၊ '.join(_A9[:2])}… {_A9[-1]}"                             # aniccaṃ saṅkhataṃ…pe…
P("indriyabaddhaññeva dukkhaṃ", V(f"{IB} {THING}သည်သာ ဒုက္ခ"))
_A9P = "aniccaṃ saṅkhataṃ paṭiccasamuppannaṃ khayadhammaṃ vayadhammaṃ virāgadhammaṃ nirodhadhammaṃ vipariṇāmadhammaṃ"
P(f"indriyabaddhaññeva {_A9P}", V(f"{IB} {THING}သည်သာ {AN9} {THING}"))
P(f"anindriyabaddhaṃ {_A9P}", V(f"{AIB} {THING}သည် {AN9} {THING}"))
for _s, _sm in (("indriyabaddhaṃ", IB), ("anindriyabaddhaṃ", AIB)):
    for _pe, _pem in (("aniccaṃ saṅkhataṃ paṭiccasamuppannaṃ…pe… vipariṇāmadhammaṃ", AN_PE1),
                      ("aniccaṃ saṅkhataṃ…pe… vipariṇāmadhammaṃ", AN_PE2)):
        for _n, _neg in (("na ", True), ("", False)):
            P(f"{_s} {_pe}, tañca {_n}dukkhaṃ", V(f"{_sm} {THING}သည် {_pem} {THING} ဖြစ်၍ ထိုအရာသည်လည်း ဒုက္ခ", neg=_neg))
BR_X["[idaṃ-pucchādvayena purimapucchādvayassa purato bhavitabbaṃ]"] = "[ဤအမေး နှစ်ခုသည် ရှေ့ အမေး နှစ်ခု၏ ရှေ့၌ ရှိသင့်သည်]"
P("yadaniccaṃ taṃ dukkhaṃ vuttaṃ bhagavatā – anindriyabaddhaṃ aniccaṃ",
  Cl(f"«{_ANICC}သော {THING}သည် ဒုက္ခ»ဟု ⟦b⟧ {BUDDHA}", *SAID, post=f" – «{AIB} {THING}သည် {_ANICC}»"))
_BRV = "မြတ်စွာဘုရား၏ ထံ၌ မြင့်မြတ်သော အကျင့်ကို ကျင့်ရ"                        # bhagavati brahmacariyaṃ vussati
W("2", "^2-509", "imasmiṃ brahmacariye", "မြင့်မြတ်သော အကျင့်")
for _s, _sm in (("indriyabaddhassa", IB), ("anindriyabaddhassa", AIB)):
    P(f"{_s} dukkhassa pariññāya bhagavati brahmacariyaṃ vussati",
      Cl(f"{_sm} ဒုက္ခကို ပိုင်းခြား သိရန် မြတ်စွာဘုရား၏ ထံ၌ မြင့်မြတ်သော အကျင့်ကို", "ကျင့်ရ", "မကျင့်ရ"))
    P(f"{_s[:-4]}aṃ dukkhaṃ pariññātaṃ na puna uppajjati",
      Cl(f"ပိုင်းခြား သိပြီးသော {_sm} ဒုက္ခသည် တစ်ဖန်", "မဖြစ်ပေါ်", "ဖြစ်ပေါ်"))


@F.frame(r"[Yy]athā (?P<a>.+?), evamevaṃ (?P<b>.+?)ti\?")
def _f_yatha_gen(m):
    """Yathā A, evamevaṃ B-ti? (generic, ^5-788) = «Aသကဲ့သို့ ထို့အတူပင် Bသလော»."""
    return f"{F.pq(m['a'], 'bare')}သကဲ့သို့ {MS.EVAM} {F.pq(m['b'], 'q')}{END}"


before_generic()

# ===================================================================================== 170. Ṭhapetvā ariyamaggantikathā
AMG = "အရိယာ မဂ်"                                                       # ariyamagga
section("(170) 5. Ṭhapetvā ariyamaggantikathā", f"(170) 5. {AMG}ကို ချန်ထား၍ဟူသော {KATHA}")
section("Ṭhapetvā ariyamaggantikathā", f"{AMG}ကို ချန်ထား၍ဟူသော {KATHA}")
P("ṭhapetvā ariyamaggaṃ avasesā saṅkhārā dukkhā",
  V(f"{AMG}ကို ချန်ထား၍ ကြွင်းသော ပြုပြင်ဖန်တီးမှုတို့သည် ဒုက္ခ"))
P("dukkhasamudayopi dukkho", V(f"{DUKKHASAM}သည်လည်း ဒုက္ခ"))
P("tīṇeva ariyasaccāni", V(f"{P11._AS} {F.NUM_MY[3]}{F.CL}သာ"))
_4T = [P11._TR[x] for x in ("dukkhaṃ", "dukkhasamudayaṃ", "dukkhanirodhaṃ", "dukkhanirodhagāminī paṭipadā")]
for _p in ("cattāri ariyasaccāni vuttāni bhagavatā – dukkhaṃ, dukkhasamudayo, dukkhanirodho, dukkhanirodhagāminī "
           "paṭipadā",):
    P(_p, Cl(f"{BUDDHA}သည် {P11._AS} {F.NUM_MY[4]}{F.CL}တို့ကို", *SAID, post=" – " + "၊ ".join(_4T)))
S("Kenaṭṭhenāti?", f"အဘယ် အနက်ကြောင့်နည်း{END}")
S("Aniccaṭṭhena.", f"{_ANICC}ခြင်း အနက်ကြောင့် ဖြစ်ပါသည်{END}")
for _s, _sm in (("ariyamaggo", AMG), ("dukkhasamudayo", DUKKHASAM)):
    P(f"{_s} anicco", V(f"{_sm}သည် {_ANICC}သော {THING}"))
    P(f"{_s} dukkho", V(f"{_sm}သည် ဒုက္ခ"))
    for _n, _neg in (("na ", True), ("", False)):
        P(f"{_s} anicco, so ca {_n}dukkho", V(f"{_sm}သည် {_ANICC}သော {THING} ဖြစ်၍ ထိုအရာသည်လည်း ဒုက္ခ", neg=_neg))
P("sā dukkhanirodhagāminī paṭipadā", V(f"ထိုအရာသည် {_4T[3]}"))

# ===================================================================================== 171-175. saṅgha / buddha
DAK = "အလှူ"                                                            # dakkhiṇā
SG = F.SANGHA
for _n, _h, _m in (("(171) 6. ", "Na vattabbaṃ saṅgho dakkhiṇaṃ paṭiggaṇhātikathā", f"{SG}သည် {DAK}ကို ခံယူသည်ဟု"),
                   ("(172) 7. ", "Na vattabbaṃ saṅgho dakkhiṇaṃ visodhetītikathā", f"{SG}သည် {DAK}ကို စင်ကြယ်စေသည်ဟု"),
                   ("(173) 8. ", "Na vattabbaṃ saṅgho bhuñjatītikathā", f"{SG}သည် စားသည်ဟု"),
                   ("(174) 9. ", "Na vattabbaṃ saṅghassadinnaṃ mahapphalantikathā",
                    f"{SG}အား လှူသော {DAK}သည် အကျိုး ကြီးမားသည်ဟု"),
                   ("(175) 10. ", "Na vattabbaṃ buddhassadinnaṃ mahapphalantikathā",
                    f"ဘုရားအား လှူသော {DAK}သည် အကျိုး ကြီးမားသည်ဟု")):
    section(_n + _h, f"{_n}{_m} မဆိုသင့်ဟူသော {KATHA}")
    section(_h, f"{_m} မဆိုသင့်ဟူသော {KATHA}")
COLO_X["Na vattabbaṃ saṅgho dakkhiṇaṃ paṭiggaṇhātītikathā niṭṭhitā"] = COLO_X[
    "Na vattabbaṃ saṅgho dakkhiṇaṃ paṭiggaṇhātikathā niṭṭhitā"]
COLO_X["Na vattabbaṃ saṅghassa dinnaṃ mahapphalantikathā niṭṭhitā"] = COLO_X[
    "Na vattabbaṃ saṅghassadinnaṃ mahapphalantikathā niṭṭhitā"]
COLO_X["Na vattabbaṃ buddhassa dinnaṃ mahapphalantikathā niṭṭhitā"] = COLO_X[
    "Na vattabbaṃ buddhassadinnaṃ mahapphalantikathā niṭṭhitā"]
P("saṅgho dakkhiṇaṃ paṭiggaṇhāti", Cl(f"{SG}သည် {DAK}ကို", "ခံယူ", "မခံယူ"))
P("saṅgho dakkhiṇaṃ visodheti", Cl(f"{SG}သည် {DAK}ကို", "စင်ကြယ်စေ", "မစင်ကြယ်စေ"))
EAT4 = "စား၍ သောက်၍ ခဲ၍"
P("saṅgho bhuñjati pivati khādati sāyati", Cl(f"{SG}သည် {EAT4}", "လျက်", "မလျက်"))
P("maggo paṭiggaṇhāti, phalaṃ paṭiggaṇhāti", Cl("မဂ်သည် ခံယူ၍ ဖိုလ်သည်", "ခံယူ", "မခံယူ"))
P("maggo visodheti, phalaṃ visodheti", Cl("မဂ်သည် စင်ကြယ်စေ၍ ဖိုလ်သည်", "စင်ကြယ်စေ", "မစင်ကြယ်စေ"))
P("maggo bhuñjati pivati khādati sāyati, phalaṃ bhuñjati pivati khādati sāyati",
  Cl(f"မဂ်သည် {EAT4} လျက်၍ ဖိုလ်သည် {EAT4}", "လျက်", "မလျက်"))
SGE = new("āhuneyyo pāhuneyyo dakkhiṇeyyo añjalikaraṇīyo anuttaraṃ puññakkhettaṃ lokassa",
          "ပူဇော်ဖွယ်တို့ကို ခံထိုက်သော၊ ဧည့်ဝတ်တို့ကို ခံထိုက်သော၊ အလှူကို ခံထိုက်သော၊ လက်အုပ်ချီ၍ ရှိခိုးထိုက်သော၊ "
          "လောက၏ အမြတ်ဆုံး ကောင်းမှု လယ်မြေ")
P("saṅgho āhuneyyo pāhuneyyo dakkhiṇeyyo añjalikaraṇīyo anuttaraṃ puññakkhettaṃ lokassa", V(f"{SG}သည် {SGE}"))
P("saṅgho āhuneyyo…pe… anuttaraṃ puññakkhettaṃ lokassa",
  V(f"{SG}သည် {SGE.split('၊ ')[0]}… {SGE.split('၊ ')[-1]}"))
P("atthi keci paṭiggāhakā āhuneyyā pāhuneyyā dakkhiṇeyyā añjalikaraṇīyā anuttaraṃ puññakkhettaṃ lokassa",
  V(f"{SGE} ဖြစ်သော အချို့သော အလှူခံတို့", EXIST))
PY8 = "လူ အစုံ လေးစုံ၊ ပုဂ္ဂိုလ် ရှစ်ယောက်"                                 # cattāro purisayugā aṭṭha purisapuggalā
new("cattāro purisayugā aṭṭha purisapuggalā", PY8)
for _p in ("cattāro purisayugā aṭṭha purisapuggalā dakkhiṇeyyā vuttā bhagavatā",
           "cattāro purisayugā aṭṭhapurisapuggalā dakkhiṇeyyā vuttā bhagavatā"):
    P(_p, Cl(f"{PY8}တို့ကို အလှူကို ခံထိုက်သူတို့ဟု {BUDDHA}", *SAID))
_GIFTS = [("dānaṃ", "အလှူ")] + [(k, DANA_I[k]) for k in ("cīvaraṃ", "piṇḍapātaṃ", "senāsanaṃ",
                                                         "gilānapaccayabhesajjaparikkhāraṃ", "khādanīyaṃ",
                                                         "bhojanīyaṃ", "pānīyaṃ")]
_GD = dict(_GIFTS)
SGA = f"{SG}အား"
P("atthi keci saṅghassa dānaṃ denti", V(f"{SGA} အလှူကို ပေးကြသော အချို့သူတို့", EXIST))
P("atthi keci saṅghassa pānīyaṃ denti", V(f"{SGA} {_GD['pānīyaṃ']}ကို ပေးကြသော အချို့သူတို့", EXIST))
P("atthi keci saṅghassa cīvaraṃ denti", FR(f"{SGA} {_GD['cīvaraṃ']}ကို ပေးကြသော"))
for _k in ("piṇḍapātaṃ", "senāsanaṃ", "gilānapaccayabhesajjaparikkhāraṃ", "khādanīyaṃ", "bhojanīyaṃ"):
    P(f"{_k} denti", FR(f"{_GD[_k]}ကို ပေးကြသော"))
P("pānīyaṃ denti", Cl(f"{_GD['pānīyaṃ']}ကို ပေးကြသော အချို့သူတို့", *EXN))
ARADH = "အလှူကို အောင်မြင်စေကြသော"                                     # dakkhiṇaṃ ārādhenti
for _who, _wm in (("saṅghassa", SGA), ("sotāpanne", f"{F.SOTAPANNA}အား"), ("arahato", f"{ARAHA}အား")):
    P(f"atthi keci {_who} dānaṃ datvā dakkhiṇaṃ ārādhenti", V(f"{_wm} အလှူကို ပေး၍ {ARADH} အချို့သူတို့", EXIST))
P("atthi keci saṅghassa pānīyaṃ datvā dakkhiṇaṃ ārādhenti",
  V(f"{SGA} {_GD['pānīyaṃ']}ကို ပေး၍ {ARADH} အချို့သူတို့", EXIST))
P("atthi keci saṅghassa cīvaraṃ datvā", FR(f"{SGA} {_GD['cīvaraṃ']}ကို ပေး၍"))
for _k in ("piṇḍapātaṃ", "senāsanaṃ", "gilānapaccayabhesajjaparikkhāraṃ", "khādanīyaṃ", "bhojanīyaṃ"):
    P(f"{_k} datvā", FR(f"{_GD[_k]}ကို ပေး၍"))
P("pānīyaṃ datvā dakkhiṇaṃ ārādhenti", V(f"{_GD['pānīyaṃ']}ကို ပေး၍ {ARADH} အချို့သူတို့", EXIST))
P("atthi keci sakadāgāmissa…pe… anāgāmissa…pe… arahato dānaṃ datvā dakkhiṇaṃ ārādhenti",
  V(f"{F.SAKADAGAMI}အား… {F.ANAGAMI}အား… {ARAHA}အား အလှူကို ပေး၍ {ARADH} အချို့သူတို့", EXIST))
for _p, _m in (('"Āhutiṃ jātavedova, mahāmeghaṃva medanī;',
                "“မီးသည် ပူဇော်ဖွယ်ကို ခံယူသကဲ့သို့၊ မြေကြီးသည် မိုးကြီးကို ခံယူသကဲ့သို့၊"),
               ('Saṅgho samādhisampanno, paṭiggaṇhāti dakkhiṇa"nti.',
                f"သမာဓိနှင့် ပြည့်စုံသော {SG}သည် {DAK}ကို ခံယူ၏”ဟူ၍{END}")):
    LINES_X[key(_p)] = _m
P("atthi keci saṅghabhattāni karonti, uddesabhattāni karonti, yāgupānāni karonti",
  V(f"{SG}အတွက် ဆွမ်းကို ပြုကြ၍ ခွဲဝေ ဆွမ်းကို ပြုကြ၍ ယာဂုနှင့် အဖျော်တို့ကို ပြုကြသော အချို့သူတို့", EXIST))
Q("gaṇabhojanaṃ paramparabhojanaṃ atirittabhojanaṃ anatirittabhojanaṃ",
  "အစုလိုက် စားခြင်း၊ အဆင့်ဆင့် စားခြင်း၊ ကြွင်းကျန်သော ဘောဇဉ်၊ မကြွင်းကျန်သော ဘောဇဉ်")
_P8 = ["သရက်သီး အဖျော်", "သပြေသီး အဖျော်", "အစေ့ပါ ငှက်ပျောသီး အဖျော်", "အစေ့ကင်း ငှက်ပျောသီး အဖျော်",
       "မဓုက သီး အဖျော်", "စပျစ်သီး အဖျော်", "ကြာရင်းမြစ် အဖျော်", "ဖာရုသက သီး အဖျော်"]
new("ambapānaṃ … phārusakapānaṃ", "၊ ".join(_P8))
_P8H = f"{BUDDHA}သည် အဖျော် {F.NUM_MY[8]}မျိုးတို့ကို"
P("aṭṭha pānāni vuttāni bhagavatā – ambapānaṃ, jambupānaṃ, cocapānaṃ, mocapānaṃ, madhukapānaṃ, muddikapānaṃ, "
  "sālukapānaṃ, phārusakapānaṃ", Cl(_P8H, *SAID, post=" – " + "၊ ".join(_P8)))
S("Nanu aṭṭha pānāni vuttāni bhagavatā – ambapānaṃ, jambupānaṃ, cocapānaṃ, mocapānaṃ, madhukapānaṃ, muddikapānaṃ, "
  "sālukapānaṃ, phārusakapānanti?",
  f"{_P8H} ဟောတော်မူသည် မဟုတ်လော – {'၊ '.join(_P8[:5])} ⟦b⟧၊ {'၊ '.join(_P8[5:])}{END}")
BR_X["[madhupānaṃ (sī. syā. kaṃ. pī.) mahāva. 300 pana passitabbaṃ]"] = (
    f"[{F.PATHA} (Sī., Syā., Kaṃ., Pī.): madhupānaṃ၊ “မဟာဝဂ်” 300 ကိုလည်း ကြည့်ပါ]")
for _s, _sm in (("saṅghassa", SG), ("buddhassa", "ဘုရား")):
    P(f"{_s} dinnaṃ mahapphalaṃ", Cl(f"{_sm}အား လှူသော {DAK}သည် အကျိုး", "ကြီးမား", "မကြီးမား"))
Q("saṅghe, gotami, dehi, saṅghe te dinne ahañceva pūjito bhavissāmi saṅgho ca",
  f"ဂေါတမီ၊ {SG}အား လှူလော့၊ {SG}အား သင် လှူသောအခါ ငါသည်လည်း ပူဇော်ခံရလိမ့်မည်၊ {SG}သည်လည်း ပူဇော်ခံရလိမ့်မည်")
S("Nanu sakko devānamindo bhagavantaṃ etadavoca –",
  f"နတ်တို့၏ အရှင် သိကြားမင်းသည် {BUDDHA}ကို ဤသို့ လျှောက်ခဲ့သည် မဟုတ်လော –")
_SAKKA = [
    ('"Yajamānānaṃ manussānaṃ, puññapekkhāna pāṇinaṃ;', "“ကောင်းမှုကို မျှော်ကိုးလျက် အလှူ ပေးနေကြသော လူတို့၊ သတ္တဝါတို့သည်"),
    ("Karotaṃ opadhikaṃ puññaṃ, kattha dinnaṃ mahapphalanti.",
     "ဘဝသစ်ကို ဖြစ်စေတတ်သော ကောင်းမှုကို ပြုကြရာ၌ အဘယ်မှာ လှူသော အလှူသည် အကျိုး ကြီးမားသနည်းဟူ၍။"),
    ('"Cattāro ca paṭipannā, cattāro ca phale ṭhitā;', "“ကျင့်ကြံဆဲသူ လေးယောက်နှင့် ဖိုလ်၌ တည်ပြီးသူ လေးယောက်တို့သည်"),
    ("Esa saṅgho ujubhūto, paññāsīlasamāhito.", f"ဖြောင့်မတ်၍ ပညာ၊ သီလ၊ သမာဓိနှင့် ပြည့်စုံသော ဤ{SG} ဖြစ်၏။"),
    ('"Yajamānānaṃ manussānaṃ, puññapekkhāna pāṇinaṃ;', ""),
    ('Karotaṃ opadhikaṃ puññaṃ, saṅghe dinnaṃ mahapphala"nti [saṃ. ni. 1.262; vi. va. 642, 751].',
     f"ဘဝသစ်ကို ဖြစ်စေတတ်သော ကောင်းမှုကို ပြုကြရာ၌ {SG}အား လှူသော အလှူသည် အကျိုး ကြီးမား၏”ဟူ၍ ⟦0⟧။"),
    ('"Eso hi saṅgho vipulo mahaggato,', f"“ဤ{SG}သည်ကား ပြန့်ပြော၍ ကြီးမြတ်၏၊"),
    ("Esappameyyo udadhīva sāgaro;", "ဤ{SG}သည် ပင်လယ် သမုဒ္ဒရာကဲ့သို့ အတိုင်းအဆ မရှိ၊"),
    ("Ete hi seṭṭhā naravīrasāvakā [narasīhasāvakā (ka.)],", "ဤသူတို့သည်ကား လူတို့တွင် သူရဲကောင်း ဖြစ်တော်မူသော ဘုရား၏ မြတ်သော တပည့်တို့ ⟦0⟧ ဖြစ်ကြ၍"),
    ("Pabhaṅkarā dhammamudīrayanti.", "အလင်းကို ပြုကြလျက် တရားကို ဟောကြား၏။"),
    ('"Tesaṃ sudinnaṃ suhutaṃ suyiṭṭhaṃ,', "“ထိုသူတို့၏ အလှူသည် ကောင်းစွာ ပေးလှူခြင်း၊ ကောင်းစွာ ပူဇော်ခြင်း၊ ကောင်းစွာ ယဇ်ပူဇော်ခြင်း ဖြစ်၏၊"),
    ("Ye saṅghamuddissa dadanti dānaṃ;", f"အကြင်သူတို့သည် {SG}ကို ရည်စူး၍ အလှူကို ပေးကြ၏၊"),
    ("Sā dakkhiṇā saṅghagatā patiṭṭhitā,", f"{SG}ထံ ရောက်သော ထိုအလှူသည် ခိုင်မြဲစွာ တည်၏၊"),
    ("Mahapphalā lokavidūna vaṇṇitā.", "အကျိုး ကြီးမားသည်ဟု လောကကို သိတော်မူသူတို့ ချီးမွမ်းတော်မူ၏။"),
    ('"Etādisaṃ yaññamanussarantā,', "“ဤသို့သော ယဇ်ကို အောက်မေ့လျက်"),
    ("Ye vedajātā vicaranti [viharanti (sī. ka.)] loke;", "ဝမ်းမြောက်ခြင်း ဖြစ်ပေါ်လျက် လောက၌ လှည့်လည်နေကြသူတို့သည် ⟦0⟧၊"),
    ("Vineyya maccheramalaṃ samūlaṃ,", "ဝန်တိုခြင်း အညစ်အကြေးကို အမြစ်နှင့်တကွ ဖယ်ရှား၍"),
    ('Aninditā saggamupenti ṭhāna"nti [vi. va. 645, 754].', "မကဲ့ရဲ့ခံရဘဲ နတ်ပြည် ဌာနသို့ ရောက်ကြ၏”ဟူ၍ ⟦0⟧။"),
]
_SAKKA[4] = (_SAKKA[4][0], _SAKKA[0][1])
_SAKKA[7] = (_SAKKA[7][0], _SAKKA[7][1].format(SG=SG))
for _p, _m in _SAKKA:
    LINES_X[key(_p)] = _m
VAR_X.update({"narasīhasāvakā": F.PATHA, "viharanti": F.PATHA})
BR_X["[saṃ. ni. 1.262; vi. va. 642, 751]"] = f"[{F.REF['saṃ. ni.']} 1.262၊ “ဝိမာနဝတ္ထု” 642၊ 751]"
BR_X["[vi. va. 645, 754]"] = "[“ဝိမာနဝတ္ထု” 645၊ 754]"
BR_X["[vi. va. 1047]"] = "[“ဝိမာနဝတ္ထု” 1047]"
_DVP = ["ခြေနှစ်ချောင်း ရှိသူတို့တွင် အမြတ်ဆုံး", "ခြေနှစ်ချောင်း ရှိသူတို့တွင် အမွန်မြတ်ဆုံး",
        "ခြေနှစ်ချောင်း ရှိသူတို့တွင် အကြီးမှူး", "ခြေနှစ်ချောင်း ရှိသူတို့တွင် အထွတ်အထိပ်",
        "ခြေနှစ်ချောင်း ရှိသူတို့တွင် အထူးမြတ်ဆုံး", "တူသူ မရှိသူ", "တူသူ မရှိသူတို့နှင့် တူသူ", "ပြိုင်ဘက် မရှိသူ",
        "နှိုင်းယှဉ်ဖွယ် မရှိသူ", "ပြိုင်ဘက် ပုဂ္ဂိုလ် မရှိသူ"]
P("bhagavā dvipadānaṃ aggo, dvipadānaṃ seṭṭho, dvipadānaṃ pamokkho, dvipadānaṃ uttamo, dvipadānaṃ pavaro asamo "
  "asamasamo appaṭisamo appaṭibhāgo appaṭipuggalo", V(f"{BUDDHA}သည် {'၊ '.join(_DVP)}"))
P("atthi koci buddhena samasamo – sīlena samādhinā paññāya",
  V(f"ဘုရားနှင့် တန်းတူ ဖြစ်သော {MS.KOCI} – သီလ၊ သမာဓိ၊ ပညာအားဖြင့်", EXIST))
P("natthi koci buddhena samasamo – sīlena samādhinā paññāya",
  V(f"ဘုရားနှင့် တန်းတူ ဖြစ်သော {MS.KOCI} – သီလ၊ သမာဓိ၊ ပညာအားဖြင့်", EXIST, neg=True))
for _p, _m in (('"Nayimasmiṃ vā loke parasmiṃ vā pana,', f"“ဤလောက၌ဖြစ်စေ၊ တမလွန်လောက၌ဖြစ်စေ {NEXIST}၊"),
               ("Buddhena seṭṭho ca samo ca vijjati;", "ဘုရားထက် မြတ်သူလည်း၊ ဘုရားနှင့် တူသူလည်း၊"),
               ("Yamāhuneyyānaṃ aggataṃ gato,", "အကြင် ဘုရားသည် ပူဇော်ဖွယ်ကို ခံထိုက်သူတို့၏ အမြတ်ဆုံး အဖြစ်သို့ ရောက်တော်မူ၏၊"),
               ('Puññatthikānaṃ vipulapphalesina"nti [vi. va. 1047].',
                "ထိုဘုရားသည် ကောင်းမှုကို လိုလား၍ ကြီးမားသော အကျိုးကို ရှာသူတို့၏ အလှူခံ ဖြစ်တော်မူ၏”ဟူ၍ ⟦0⟧။")):
    LINES_X[key(_p)] = _m
REF_X["vi. va."] = "“ဝိမာနဝတ္ထု”"

# ===================================================================================== 176. Dakkhiṇāvisuddhikathā
DKV = new("dakkhiṇāvisuddhi", f"{DAK}၏ စင်ကြယ်ခြင်း")
section("(176) 11. Dakkhiṇāvisuddhikathā", f"(176) 11. {DKV}အကြောင်း {KATHA}")
section("Dakkhiṇāvisuddhikathā", f"{DKV}အကြောင်း {KATHA}")
DY, PG = "ပေးလှူသူ", "အလှူခံသူ"
P("dāyakatova dānaṃ visujjhati, no paṭiggāhakato",
  Cl(f"{DAK}သည် {DY}ကြောင့်သာ စင်ကြယ်၍ {PG}ကြောင့်", "မစင်ကြယ်", "စင်ကြယ်"))
P("paṭiggāhakato dānaṃ visujjhati", Cl(f"{DAK}သည် {PG}ကြောင့်", "စင်ကြယ်", "မစင်ကြယ်"))
P("añño aññassa kārako, parakataṃ sukhadukkhaṃ, añño karoti añño paṭisaṃvedeti",
  V(f"တစ်ယောက်သည် အခြားတစ်ယောက်၏ {MS.KARAKA} ဖြစ်၍ သုခ ဒုက္ခသည် သူတစ်ပါး ပြုထားသော အရာ ဖြစ်၍ တစ်ယောက်က "
    "ပြု၍ အခြားတစ်ယောက်က", "ခံစား"))
_AN = "အာနန္ဒာ၊"
Q("catasso kho imā, ānanda, dakkhiṇā visuddhiyo! Katamā catasso? Atthānanda, dakkhiṇā dāyakato visujjhati, no "
  "paṭiggāhakato; atthānanda, dakkhiṇā paṭiggāhakato visujjhati, no dāyakato; atthānanda, dakkhiṇā dāyakato ceva "
  "visujjhati paṭiggāhakato ca; atthānanda, dakkhiṇā neva dāyakato visujjhati, no paṭiggāhakato. Imā kho, ānanda, "
  "catasso dakkhiṇā visuddhiyo",
  f"{_AN} {DKV} လေးမျိုးတို့သည် ဤသည်တို့ပင်တည်း။ အဘယ် လေးမျိုးတို့နည်း။ {_AN} {DY}ကြောင့် စင်ကြယ်၍ {PG}ကြောင့် "
  f"မစင်ကြယ်သော {DAK} {EXIST}၏၊ {_AN} {PG}ကြောင့် စင်ကြယ်၍ {DY}ကြောင့် မစင်ကြယ်သော {DAK} {EXIST}၏၊ {_AN} {DY}ကြောင့်လည်း "
  f"စင်ကြယ်၍ {PG}ကြောင့်လည်း စင်ကြယ်သော {DAK} {EXIST}၏၊ {_AN} {DY}ကြောင့်လည်း မစင်ကြယ်၊ {PG}ကြောင့်လည်း "
  f"မစင်ကြယ်သော {DAK} {EXIST}၏။ {_AN} ဤသည်တို့ကား {DKV} လေးမျိုးတို့ ဖြစ်ကုန်၏")
LINES_X[key("Atthi arahato puññūpacayo, natthi arahato akālamaccu, sabbamidaṃ kammato, indriyabaddhaññeva dukkhaṃ, "
            "ṭhapetvā ariyamaggaṃ avasesā saṅkhārā dukkhā, saṅgho dakkhiṇaṃ paṭiggaṇhāti, saṅgho dakkhiṇaṃ visodheti, "
            "saṅgho bhuñjati pivati khādati sāyati, saṅghassa dinnaṃ mahapphalaṃ, atthi dānaṃ visuddhiyāti "
            "[visujjhatīti (syā.)].")] = (
    f"{ARL} {PUU} {EXIST}ခြင်း၊ {ARL} {AKM_D} {NEXIST}ခြင်း၊ {ALLT} {F.KAMMA}ကြောင့် ဖြစ်ခြင်း၊ {IB} {THING}သည်သာ ဒုက္ခ "
    f"ဖြစ်ခြင်း၊ {AMG}ကို ချန်ထား၍ ကြွင်းသော ပြုပြင်ဖန်တီးမှုတို့သည် ဒုက္ခ ဖြစ်ခြင်း၊ {SG}သည် {DAK}ကို ခံယူခြင်း၊ "
    f"{SG}သည် {DAK}ကို စင်ကြယ်စေခြင်း၊ {SG}သည် {EAT4} လျက်ခြင်း၊ {SG}အား လှူသော {DAK}သည် အကျိုး ကြီးမားခြင်း၊ "
    f"{DAK}သည် စင်ကြယ်ခြင်း {EXIST}ခြင်း ⟦0⟧{END}")
VAR_X["visujjhatīti"] = F.PATHA


@F.frame(r"Tena hi na vattabbaṃ – (?P<p>.+?)ti(?P<e>…\.?)")
def _f_tenahi_na_pe(m):
    """Tena hi na vattabbaṃ – "P"ti…pe…. (^5-666) = the Tena hi frame ending in «…»."""
    return f"{F.TENA_HI} ဤသို့ မဆိုသင့် – “{F.pq(m['p'], 'stmt', 1)}”{F.endmark(m['e'])}"


before_generic()


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
for _k, _us in OPEN_Q_X.items():
    assert " ".join(_us) == _k, _k
    _my = [F.unit_my(u) for u in _us]
    if _k in SLOT_X:
        _i, _t = SLOT_X[_k]
        assert _my[_i].endswith(END)
        _my[_i] = f"{_my[_i][:-len(END)]} {_t}{END}"
    F.LINES[_k] = " ".join(_my)


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
