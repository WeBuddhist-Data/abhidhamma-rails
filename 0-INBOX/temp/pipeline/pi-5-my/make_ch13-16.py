"""Burmese zero-shot of pi-5 (Kathāvatthu, «အငြင်းပွားရာ အကြောင်းအရာများကို ဆွေးနွေးခြင်း»), chapters 13-16:
13-pancamavaggo, 14-chatthavaggo, 15-sattamavaggo, 16-atthamavaggo.

usage: python3 -I -X utf8 make_ch13-16.py [chapter ...] [--misses] [--units] [--q REGEX] [--try LINE]
Model: the approved sample. Every line is generated from the Pāli by my5_formulas.translate_line() through the
frames, rules and tables of my5_formulas.py, make_sample.py, make_ch6-10.py and make_ch11-12.py (all imported READ
ONLY: they install their tables at import and write nothing; their __main__ never runs) and the tables of THIS
script, which extends them IN MEMORY only (nothing in the imported files or in my5-zeroshot-terms.md changes).
  * PROP_X (propositions), QUOTE_X (sutta quotations), SENT_X (unique sentences), LINES_X (uddāna, colophons with
    brackets), HEAD_X / COLO_X (headings, colophons); productive propositions are built from small tables;
  * a key that an imported table already has is never overwritten (P() / S() stop the run), so the imported
    chapters rebuild byte for byte (check_ch13-16.py A2);
  * NEW: every new recurring term or phrase (Pāli = Burmese), copied into notes-ch13-16.md.
A unit no frame / rule / table matches stops the run (Miss): nothing is guessed.
--q / --try are scratch lookups (they write nothing).
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
_spec.loader.exec_module(P11)          # installs make_sample + make_ch6-10 + make_ch11-12 tables; writes nothing
P6 = P11.P6
MS = P11.MS
F = P11.F
from my5_formulas import V, FR, Cl, C, END, PE  # noqa: E402,F401

PALI = MS.PALI
OUT = MS.OUT
NAMES_OUT = ["13-pancamavaggo.md", "14-chatthavaggo.md", "15-sattamavaggo.md", "16-atthamavaggo.md"]
W = P6.W
PROP_X, QUOTE_X, SENT_X, LINES_X, HEAD_X, COLO_X, ANCHOR_X = {}, {}, {}, {}, {}, {}, {}
VAR_X, REF_X, REF_NOTE_X, BR_X = {}, {}, {}, {}
NEW = {}
key = P11.key
KATHA = F.KATHA_W
EXIST, NEXIST = P6.EXIST, P6.NEXIST


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


def section(pali, my):
    if pali in F.HEAD and F.HEAD[pali] != my:
        raise SystemExit(f"heading clash: {pali}")
    HEAD_X[pali] = my
    COLO_X[f"{pali} niṭṭhitā"] = F.DONE.format(my)
    new(pali, my)
    return my


BASE_RULES = list(F.RULES)                                           # the imported rules (before this script's own)
SKIPPED = {}                                                         # key -> imported Burmese (kept, ours dropped)


def base_lookup(k):
    """What the imported tables already give for a canonical key (PROP or an imported RULE), else None."""
    if k in F.PROP:
        return F.PROP[k]
    for rx, fn in BASE_RULES:
        m = rx.fullmatch(k)
        if m:
            r = fn(m)
            if r is not None:
                return r
    return None


def P(pali, cl):
    """A proposition (canonical form: first letter small, quotes / brackets out); never overwrites an import:
    where an imported table or rule already translates the key, the imported Burmese is kept (identical Pāli =
    identical Burmese) and ours is dropped (SKIPPED)."""
    k = key(pali)
    k = k[:1].lower() + k[1:]
    b = base_lookup(k) if k not in F.PROP else None
    if b is not None:
        if b.f("stmt") != cl.f("stmt"):
            SKIPPED[k] = b.f("stmt")
        return b
    if k in F.PROP and F.PROP[k].f("stmt") != cl.f("stmt"):
        raise SystemExit(f"PROP clash with an imported table: {k}\n  old {F.PROP[k].f('stmt')}\n  new {cl.f('stmt')}")
    if k in PROP_X and PROP_X[k].f("stmt") != cl.f("stmt"):
        raise SystemExit(f"PROP defined twice: {k}")
    PROP_X[k] = cl
    return cl


def has(pali):
    k = key(pali)
    k = k[:1].lower() + k[1:]
    return k in F.PROP or k in PROP_X


def S(pali, my):
    """A whole sentence (as cut by the engine) -> Burmese with its end mark."""
    k = key(pali)
    if k in F.SENT and F.SENT[k] != my:
        raise SystemExit(f"SENT clash with an imported table: {k}")
    SENT_X[k] = my
    return my


def Q(pali, my):
    """A sutta quotation (without its final «ti») -> Burmese (inner quotes written ‹…›)."""
    QUOTE_X[key(pali)] = my
    return my


def TI(x):
    """Pāli x + «ti» with the sandhi of the text («…ṃ» -> «…nti»)."""
    return x[:-1] + "nti" if x.endswith("ṃ") else x + "ti"


def VV(pre, verb, neg=False, post=""):
    return Cl(pre, verb, "မ" + verb, neg, post)


def SAYQ(pre, quote_my, neg=False):
    """«S (na) vattabbaṃ – "Q"» inside a proposition: «Sကို ဤသို့ (မ)ဆိုသင့် – “Q”ဟု» (ch11 NSAY pattern)."""
    return Cl(f"{pre} ဤသို့".strip(), "ဆိုသင့်", "မဆိုသင့်", neg=neg, post=f" – {quote_my}")


def before_generic():
    """Move the frame just registered before the generic «P-ti?» / «P-ti.» frames."""
    fr = F.FRAMES.pop()
    F.FRAMES.insert(next(i for i, (_, fn) in enumerate(F.FRAMES) if fn is F._f_q), fr)


# ===================================================================================== shared vocabulary
BUDDHA = F.BHAGAVA
PUG = F.PUGGALA
ARAHA = F.ARAHA
NANA = "ဉာဏ်"
KNOWING = "ကို သိသော ဉာဏ်"                                           # X-e ñāṇaṃ (pi-1 ^1-1063 «ဒုက္ခကို သိသော ဉာဏ်»)
W("1", "^1-1063", "Dukkhe ñāṇaṃ", "ဒုက္ခကို သိသော ဉာဏ်")
PATP = P6.PAT                                                        # «သောတာပတ္တိဖိုလ်» … «ရဟန္တာ ဖိုလ်»
MG = P11.MG                                                          # «သောတာပတ္တိမဂ်» … «ရဟန္တာ မဂ်»
GP = P11.GP                                                          # gotrabhū puggalo
ARAHATTA_N = P11.ARAHATTA_N                                          # «ရဟန္တာ အဖြစ်»
AYASMA = P11.AYASMA
SAV = P11.SAV
EPI11 = P11.EPI11
MAGGA_EPI = P11.MAGGA_EPI
VIMUTTA = P11.VIMUTTA                                                # «လွတ်မြောက်ပြီးသော အရာ»
BEC = P11.BEC                                                        # hoti (becomes)
ATT = P6.ATT                                                         # attainments (kasiṇa, jhāna, arūpa)
KIL = P6.KIL
DK = P11.DK
SAMAP_V = ("ဝင်စား", "မဝင်စား")
SAT_W = F.heads("Satipaṭṭhānavibhaṅgo").split("များကို")[0]
GRPS = {"satipaṭṭhānā": SAT_W, "sammappadhānā": P6._SP, "iddhipādā": P6._ID, "indriyā": F.INDRIYA_W,
        "balā": "စွမ်းအား", "bojjhaṅgā": P6._BJW}
LOKUTTARA = P6.LOKUTTARA
PFX = {"sotāpatti": PATP["sotāpattiphala"], "sakadāgāmi": PATP["sakadāgāmiphala"],
       "anāgāmi": PATP["anāgāmiphala"], "arahatta": PATP["arahatta"]}
# the practitioners of the four paths (genitive Pāli -> Burmese)
PRAC = {f"{k}{'phala' if k != 'arahatta' else ''}sacchikiriyāya paṭipannassa puggalassa":
        f"{v}ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော {PUG}" for k, v in PFX.items()}
W("4", "^4-208", "sotāpattiphalasacchikiriyāya paṭipannassa", "သောတာပတ္တိဖိုလ်ကို မျက်မှောက်ပြုရန် ကျင့်ကြံသော")
HAVING = "ကို ရရှိထားသော"                                            # X-phalasamaṅgī (proposed)
SAMANGI = {f"{k}phalasamaṅgissa puggalassa": f"{v}{HAVING} {PUG}" for k, v in PFX.items()}
new("X-phalasamaṅgī puggalo", f"Xဖိုလ်{HAVING} {PUG}")

# ===================================================================================== 13. Pañcamavaggo
section("Pañcamavaggo", f"{F.ORD_MY[5]} {F.VAGGA_W}")
COLO_X["Pañcamavaggo"] = HEAD_X["Pañcamavaggo"]
# ------------------------------------------------------------------------------------- 43. Vimuttikathā
section("(43) 1. Vimuttikathā", f"(43) 1. {F.HEAD['Vimuttikathā']}")
VN = new("vimuttiñāṇaṃ", f"လွတ်မြောက်ခြင်း{KNOWING}")
PVN = W("2", "^2-804", "paccavekkhaṇāñāṇaṃ", "ပြန်လည် ဆင်ခြင်သော ဉာဏ်")
P("vimuttiñāṇaṃ vimuttaṃ", V(f"{VN}သည် {VIMUTTA}"))
P("yaṃ kiñci vimuttiñāṇaṃ sabbaṃ taṃ vimuttaṃ", V(f"{VN} မှန်သမျှ ထိုအားလုံးသည် {VIMUTTA}"))
P("paccavekkhaṇañāṇaṃ vimuttaṃ", V(f"{PVN}သည် {VIMUTTA}"))
GOT = new("attained … (pattassa paṭiladdhassa adhigatassa sacchikatassa)",
          "သို့ ရောက်ပြီး၊ ရပြီး၊ ပြည့်မီပြီး၊ မျက်မှောက်ပြုပြီးသူ")
PHALA_PERS = dict(PRAC, **SAMANGI)
PHALA_PERS["gotrabhuno puggalassa"] = GP
for _g, _gm in PHALA_PERS.items():
    P(f"{_g} vimuttiñāṇaṃ vimuttaṃ", V(f"{_gm}၏ {VN}သည် {VIMUTTA}"))
    P(f"{_g} vimuttiñāṇaṃ vimuttaṃ tañca phalaṃ pattassa ñāṇaṃ",
      V(f"{_gm}၏ {VN}သည် {VIMUTTA} ဖြစ်၍ ထိုဉာဏ်သည်လည်း ဖိုလ်သို့ ရောက်ပြီးသူ၏ {NANA}"))
for _p, _pm, _f, _fm in (("sotāpannassa", F.SOTAPANNA, "sotāpattiphalaṃ", PFX["sotāpatti"]),
                         ("sakadāgāmissa", F.SAKADAGAMI, "sakadāgāmiphalaṃ", PFX["sakadāgāmi"]),
                         ("anāgāmissa", F.ANAGAMI, "anāgāmiphalaṃ", PFX["anāgāmi"]),
                         ("arahato", ARAHA, "arahattaṃ", ARAHATTA_N)):
    P(f"{_p} ñāṇaṃ, {_f} pattassa paṭiladdhassa adhigatassa sacchikatassa ñāṇaṃ",
      V(f"{_pm}၏ {NANA} ဖြစ်၍ {_fm}{GOT}၏ {NANA}"))

# ------------------------------------------------------------------------------------- 44. Asekhañāṇakathā
SEKHA = W("1", "^1-M1-11", "sekkhā dhammā", "ကျင့်ကြံဆဲသူ")
ASEKHA = W("1", "^1-M1-11", "asekkhā dhammā", "ကျင့်ကြံမှု ပြီးဆုံးသူ")
AN = new("asekhaṃ ñāṇaṃ", f"{ASEKHA}၏ {NANA}")
section("(44) 2. Asekhañāṇakathā", f"(44) 2. {AN}အကြောင်း {KATHA}")
section("Asekhañāṇakathā", f"{AN}အကြောင်း {KATHA}")
ADH = f"{ASEKHA}၏ သဘောတရား"
for _s, _sm in (("sekhassa", SEKHA), ("asekhassa", ASEKHA)):
    P(f"{_s} asekhaṃ ñāṇaṃ atthi", V(f"{_sm}၌ {AN}", EXIST))
for _s, _sm in (("sekho", SEKHA), ("asekho", ASEKHA)):
    P(f"{_s} asekhaṃ dhammaṃ jānāti passati", Cl(f"{_sm}သည် {ADH}ကို သိ၍", "မြင်", "မမြင်"))
    P(f"{_s} asekhaṃ dhammaṃ na jānāti na passati", Cl(f"{_sm}သည် {ADH}ကို မသိ၊", "မြင်", "မမြင်", neg=True))
SEEN3 = new("diṭṭhaṃ viditaṃ sacchikataṃ upasampajja viharati", "မြင်ပြီး၊ သိပြီး၊ မျက်မှောက်ပြုပြီးသော ထိုတရားကို "
            "ပြည့်စုံစေလျက် နေ")
P("diṭṭhaṃ viditaṃ sacchikataṃ upasampajja viharati",
  Cl("မြင်ပြီး၊ သိပြီး၊ မျက်မှောက်ပြုပြီးသော ထိုတရားကို", "ပြည့်စုံစေလျက် နေ", "ပြည့်စုံစေလျက် မနေ"))
P("adiṭṭhaṃ aviditaṃ asacchikataṃ na upasampajja viharati",
  Cl("မမြင်ရသေး၊ မသိရသေး၊ မျက်မှောက် မပြုရသေးသော ထိုတရားကို", "ပြည့်စုံစေလျက် နေ", "ပြည့်စုံစေလျက် မနေ", neg=True))
TOUCH = (f"{F.KAYENA} နေ", f"{F.KAYENA} မနေ")      # (na) kāyena phusitvā viharati (harmonise B6: pi-4 / ch3; was «… တွေ့ထိ၍»)
P("kāyena phusitvā viharati", Cl("", *TOUCH))
P("na kāyena phusitvā viharati", Cl("", *TOUCH, neg=True))
P("gotrabhuno puggalassa sotāpattimagge ñāṇaṃ atthi", V(f"{GP}၌ {MG['sotāpatti']}{KNOWING}", EXIST))
for _k, _f in (("sotāpatti", "sotāpattiphale"), ("sakadāgāmi", "sakadāgāmiphale"), ("anāgāmi", "anāgāmiphale"),
               ("arahatta", "arahatte")):
    _g = [g for g in PRAC if g.startswith(_k)][0]
    _fm = PFX[_k] if _k != "arahatta" else ARAHATTA_N
    P(f"{_g} {_f} ñāṇaṃ atthi", V(f"{PRAC[_g]}၌ {_fm}{KNOWING}", EXIST))
for _k in ("sakadāgāmiphala", "anāgāmiphala"):
    P(_k, FR(PATP[_k]))
for _k, _m in (("sakadāgāmi", F.SAKADAGAMI), ("anāgāmi", F.ANAGAMI)):
    P(_k, FR(_m))
UL = "မြင့်မြတ်သူ ဖြစ်သည်"                                          # uḷāro (proposed)
THERA2 = f"{P11.SARIPUTTA} မထေရ်၊ {P11.THERA['mahāmoggallāno']} မထေရ်"
_AN_PI = 'āyasmā ānando sekho – "bhagavā uḷāro"ti jānāti, "sāriputto thero, mahāmoggallāno thero uḷāro"ti jānāti'
P(_AN_PI, Cl(f"{AYASMA} အာနန္ဒာသည် {SEKHA} ဖြစ်လျက် – «{BUDDHA}သည် {UL}»ဟု သိ၏၊ «{THERA2}တို့သည် {UL}»ဟု",
             "သိ", "မသိ"))
new("uḷāro", UL)

# ------------------------------------------------------------------------------------- 45. Viparītakathā
VPN = new("viparīte ñāṇaṃ", "ဖောက်ပြန်သော ဉာဏ်")
VPS = new("vipariyeso", "ဖောက်ပြန်ခြင်း")
section("(45) 3. Viparītakathā", f"(45) 3. ဖောက်ပြန်သော အရာအကြောင်း {KATHA}")
section("Viparītakathā", f"ဖောက်ပြန်သော အရာအကြောင်း {KATHA}")
PKS = ATT["pathavīkasiṇaṃ samāpattiṃ"]                               # «မြေ ကသိုဏ်း သမာပတ်»
PKS_IN = f"{PKS}ကို ဝင်စားနေသူ"
P("pathavīkasiṇaṃ samāpattiṃ samāpannassa viparīte ñāṇaṃ", V(f"{PKS_IN}၏ {NANA}သည် {VPN}"))
P("pathavīkasiṇaṃ samāpattiṃ samāpannassa viparīte ñāṇaṃ, tañca akusalaṃ",
  V(f"{PKS_IN}၏ {NANA}သည် {VPN} ဖြစ်၍ ထိုဉာဏ်သည်လည်း အကုသိုလ်"))
P("pathavīkasiṇaṃ samāpattiṃ samāpannassa viparīte ñāṇaṃ, arahā pathavīkasiṇaṃ samāpattiṃ samāpajjeyya",
  Cl(f"{PKS_IN}၏ {NANA}သည် {VPN} ဖြစ်၍ {ARAHA}သည် {PKS}ကို", "ဝင်စားရာ", "မဝင်စားရာ"))
P("arahā pathavīkasiṇaṃ samāpattiṃ samāpajjeyya", Cl(f"{ARAHA}သည် {PKS}ကို", "ဝင်စားရာ", "မဝင်စားရာ"))
VP4 = {"anicce niccanti": "မမြဲသော အရာ၌ မြဲသည်ဟု", "dukkhe sukhanti": "ဆင်းရဲသော အရာ၌ ချမ်းသာသည်ဟု",
       "anattani attāti": "အတ္တ မဟုတ်သော အရာ၌ အတ္တဟု", "asubhe subhanti": "မတင့်တယ်သော အရာ၌ တင့်တယ်သည်ဟု"}
new("anicce niccanti … asubhe subhanti vipariyeso", " / ".join(VP4.values()) + f" {VPS}")
for _k, _m in VP4.items():
    P(_k, FR(_m))
    P(f"{_k} vipariyeso", V(f"{_m} {VPS}"))
    P(f"{_k} vipariyeso, so ca akusalo", V(f"{_m} {VPS} ဖြစ်၍ ထိုဖောက်ပြန်ခြင်းသည်လည်း အကုသိုလ်"))
    P(f"{_k} vipariyeso, so ca kusalo", V(f"{_m} {VPS} ဖြစ်၍ ထိုဖောက်ပြန်ခြင်းသည်လည်း ကုသိုလ်"))
P("akusalaṃ", V("အကုသိုလ်"))
P("kusalaṃ", V("ကုသိုလ်"))
P("atthi arahato vipariyeso", V(f"{ARAHA}၌ {VPS}", EXIST))
_V3 = f"မှတ်သိမှု {VPS}၊ စိတ် {VPS}၊ အယူ {VPS}"
new("saññāvipariyeso cittavipariyeso diṭṭhivipariyeso", _V3)
P("atthi arahato saññāvipariyeso cittavipariyeso diṭṭhivipariyeso", V(f"{ARAHA}၌ {_V3}", EXIST))
P("natthi arahato saññāvipariyeso cittavipariyeso diṭṭhivipariyeso", V(f"{ARAHA}၌ {_V3}", EXIST, neg=True))
PATH = "မြေ"
P("pathavīkasiṇaṃ samāpattiṃ samāpajjantassa sabbeva pathavī",
  V(f"{PKS}ကို ဝင်စားနေသူအတွက် အရာအားလုံးသည် {PATH}ပင်"))
P("pathavī atthi", V(PATH, EXIST))
P("atthi ca koci pathaviṃ pathavito samāpajjati", V(f"{PATH}ကို {PATH}အဖြစ် ဝင်စားသူ တစ်စုံတစ်ယောက်လည်း", EXIST))
P("pathaviṃ pathavito samāpajjantassa viparītaṃ hoti", Cl(f"{PATH}ကို {PATH}အဖြစ် ဝင်စားနေသူ၌ ဖောက်ပြန်ခြင်း", *BEC))
P("nibbānaṃ atthi", V(F.NIBBANA, EXIST))
P("nibbānaṃ nibbānato samāpajjantassa viparītaṃ hoti",
  Cl(f"{F.NIBBANA}ကို {F.NIBBANA}အဖြစ် ဝင်စားနေသူ၌ ဖောက်ပြန်ခြင်း", *BEC))
VAR_X["pathavīkasiṇasamāpattiṃ"] = F.LEKHANA
ANCHOR_X["samāpattiṃ"] = PKS

# ------------------------------------------------------------------------------------- 46. Niyāmakathā
NIYAMA = W("4", "^4-13", "niyāmaṃ okkamituṃ", "သေချာသော လမ်းကြောင်း")       # niyāmo (pi-4 ^4-13, ch11-12)
NIYATA = W("1", "^1-M1-15", "aniyatā dhammā", "ကျိန်းသေ") + "သူ"          # niyato (person; pi-1 niyata)
ANIYATA = "မ" + NIYATA
section("(46) 4. Niyāmakathā", f"(46) 4. {NIYAMA}အကြောင်း {KATHA}")
section("Niyāmakathā", f"{NIYAMA}အကြောင်း {KATHA}")
GO = {"niyāmagamanāya": f"{NIYAMA}သို့ ရောက်ခြင်းအတွက်", "aniyāmagamanāya": f"{NIYAMA} မဟုတ်ရာသို့ ရောက်ခြင်းအတွက်"}
new("niyāmagamanāya / aniyāmagamanāya", " / ".join(GO.values()))
new("niyato / aniyato (person)", f"{NIYATA} / {ANIYATA}")
for _s, _sm in (("niyatassa", NIYATA), ("aniyatassa", ANIYATA)):
    for _g, _gm in GO.items():
        for _n, _neg in (("atthi", False), ("natthi", True)):
            P(f"{_s} {_g} {_n} ñāṇaṃ", V(f"{_sm}၌ {_gm} {NANA}", EXIST, neg=_neg))
    P(f"{_s} niyāmagamanāya atthi niyāmo", V(f"{_sm}၌ {GO['niyāmagamanāya']} {NIYAMA}", EXIST))
    P(f"{_s} niyāmagamanāya natthi niyāmo", V(f"{_sm}၌ {GO['niyāmagamanāya']} {NIYAMA}", EXIST, neg=True))
    P(f"{_s} niyāmagamanāya atthi satipaṭṭhānā", FR(f"{_sm}၌ {GO['niyāmagamanāya']} {SAT_W}တို့"))
    P(f"{_s} niyāmagamanāya natthi satipaṭṭhānā", FR(f"{_sm}၌ {GO['niyāmagamanāya']} {SAT_W}တို့"))
    P(f"{_s} niyāmagamanāya natthi satipaṭṭhānā… bojjhaṅgā",
      V(f"{_sm}၌ {GO['niyāmagamanāya']} {SAT_W}တို့… {P6._BJW}တို့", EXIST, neg=True))
    P(f"{_s} niyāmagamanāya natthi bojjhaṅgā",
      V(f"{_sm}၌ {GO['niyāmagamanāya']} {P6._BJW}တို့", EXIST, neg=True))
P("aniyatassa niyāmagamanāya atthi satipaṭṭhānā… sammappadhānā… iddhipādā… indriyā… balā… bojjhaṅgā",
  V(f"{ANIYATA}၌ {GO['niyāmagamanāya']} " + "… ".join(f"{GRPS[g]}တို့" for g in GRPS), EXIST))
for _g in ("sammappadhānā", "iddhipādā", "indriyā", "balā"):
    P(_g, FR(GRPS[_g])) if not has(_g) else None
P("bojjhaṅgā", V(f"{P6._BJW}တို့", EXIST)) if "bojjhaṅgā" not in F.PROP else None
# «Aniyatassa … natthi satipaṭṭhānā…pe… bojjhaṅgāti?» : the negative series ends in «… bojjhaṅgā» (natthi)
_SPN = "ayaṃ puggalo sammattaniyāmaṃ okkamissati, bhabbo ayaṃ puggalo dhammaṃ abhisametuṃ"
SAMMATTA = W("1", "^1-M1-15", "sammattaniyatā dhammā", "မှန်ကန်မှု၌ ကျိန်းသေသော")
SN = new("sammattaniyāmo", f"မှန်ကန်မှု၌ {NIYAMA}")
_SPN_MY = (f"ဤ{PUG}သည် {SN}သို့ သက်ဆင်းလိမ့်မည်၊ ဤ{PUG}သည် တရားကို ထိုးထွင်း သိနိုင်သူ ဖြစ်သည်")
P(f"bhagavā jānāti – {_SPN}", Cl(f"{BUDDHA}သည်", "သိတော်မူ", "မသိတော်မူ", post=f" – «{_SPN_MY}»ဟု"))

# ------------------------------------------------------------------------------------- 47. Paṭisambhidākathā
PSB = W("2", "^2-718", "Catasso paṭisambhidā", "ပိုင်းခြားသိသော ဉာဏ်")
section("(47) 5. Paṭisambhidākathā", f"(47) 5. {PSB}အကြောင်း {KATHA}")
section("Paṭisambhidākathā", f"{PSB}အကြောင်း {KATHA}")
SMN = W("2", "^2-796", "sammutiñāṇaṃ", "သမုတ်ကို သိသော ဉာဏ်")
SMT = "သမုတ်"
CPN = W("2", "^2-796", "pariye ñāṇaṃ", "စိတ်ကို ပိုင်းခြား၍ သိသော ဉာဏ်")      # cetopariyāye ñāṇaṃ
new("cetopariyāye ñāṇaṃ", CPN)
P("sabbaṃ ñāṇaṃ paṭisambhidā", V(f"{NANA} အားလုံးသည် {PSB}"))
P("sammutiñāṇaṃ paṭisambhidā", V(f"{SMN}သည် {PSB}"))
P("cetopariyāye ñāṇaṃ paṭisambhidā", V(f"{CPN}သည် {PSB}"))
P("sabbā paññā paṭisambhidā", V(f"ပညာ အားလုံးသည် {PSB}"))
P("sā paññā paṭisambhidā", V(f"ထိုပညာသည် {PSB}"))
P("sā paññā na paṭisambhidā", V(f"ထိုပညာသည် {PSB}", neg=True))
P("atthi lokuttarā paññā", V(f"{LOKUTTARA} ပညာ", EXIST))
PSP = new("paṭisambhidāpatto", f"{PSB}သို့ ရောက်ပြီးသူ")
for _k, _m in (("sammutiṃ", f"{SMT}ကို"), ("paracittaṃ", "အခြားသူ၏ စိတ်ကို")):
    P(f"ye keci {_k} jānanti, sabbe te paṭisambhidāpattā",
      V(f"{_m} သိကြသူ မှန်သမျှ ထိုသူ အားလုံးတို့သည် {PSP}တို့"))
GIVE = {"dānaṃ": "အလှူ", "cīvaraṃ": "သင်္ကန်း", "piṇḍapātaṃ": "ဆွမ်း", "senāsanaṃ": "ကျောင်းအိပ်ရာနေရာ",
        "gilānapaccayabhesajjaparikkhāraṃ": "သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်"}
W("2", "^2-929", "Itarītaracīvarapiṇḍapātasenāsanagilānapaccayabhesajjaparikkhārehi",
  "သင်္ကန်း၊ ဆွမ်း၊ ကျောင်းအိပ်ရာနေရာ၊ သူနာ၏ အထောက်အပံ့ ဖြစ်သော ဆေးအသုံးအဆောင်")
GIVER = {}
for _k, _m in GIVE.items():
    GIVER[f"{_k} dadantassa"] = f"{_m}ကို ပေးလှူနေသူ၌"
GIVER["dānaṃ dadantassa"] = f"{GIVE['dānaṃ']}ကို ပေးနေသူ၌"
GIVER["pathavīkasiṇaṃ samāpattiṃ samāpannassa"] = f"{PKS_IN}၌"
for _a in ("ākāsānañcāyatanaṃ", "viññāṇañcāyatanaṃ", "ākiñcaññāyatanaṃ", "nevasaññānāsaññāyatanaṃ"):
    GIVER[f"{_a} samāpannassa"] = f"{ATT[_a]}ကို ဝင်စားနေသူ၌"
new("X dadantassa", "Xကို ပေးလှူနေသူ၌")
for _g, _gm in GIVER.items():
    P(_g, FR(_gm)) if not has(_g) else None
    P(f"{_g} atthi paññā", V(f"{_gm} ပညာ", EXIST))
    P(f"{_g} atthi ñāṇaṃ", V(f"{_gm} {NANA}", EXIST))
for _k in GIVE:
    P(_k + " dadantassa", FR(GIVER[_k + " dadantassa"])) if not has(_k + " dadantassa") else None

# ------------------------------------------------------------------------------------- 48. Sammutiñāṇakathā
section("(48) 6. Sammutiñāṇakathā", f"(48) 6. {SMN}အကြောင်း {KATHA}")
section("Sammutiñāṇakathā", f"{SMN}အကြောင်း {KATHA}")
ONLY = ("ကိုသာ အာရုံပြု၏၊ အခြားကို", "အာရုံပြု", "အာရုံ မပြု")         # X-ārammaṇaññeva na aññārammaṇaṃ
new("X-ārammaṇaññeva na aññārammaṇaṃ", "Xကိုသာ အာရုံပြု၏၊ အခြားကို အာရုံ မပြု")
P("sammutiñāṇaṃ saccārammaṇaññeva na aññārammaṇaṃ", Cl(f"{SMN}သည် သစ္စာ{ONLY[0]}", ONLY[1], ONLY[2], neg=True))
P("cetopariyāye ñāṇaṃ cittārammaṇaññeva na aññārammaṇaṃ",
  Cl(f"{CPN}သည် စိတ်{ONLY[0]}", ONLY[1], ONLY[2], neg=True))
SMS = new("sammutisaccaṃ", f"{SMT} သစ္စာ")
P("pathavīkasiṇañca sammutisaccamhi", Cl(f"{ATT['pathavīkasiṇaṃ']}သည်လည်း {SMS}၌", "ပါဝင်", "မပါဝင်"))
P("gilānapaccayabhesajjaparikkhāro ca sammutisaccamhi", Cl(f"{GIVE['gilānapaccayabhesajjaparikkhāraṃ']}သည်လည်း {SMS}၌",
                                                            "ပါဝင်", "မပါဝင်"))
P("tena ñāṇena dukkhaṃ parijānāti", Cl("ထိုဉာဏ်ဖြင့် ဒုက္ခကို", "ပိုင်းခြား သိ", "ပိုင်းခြား မသိ"))

# ------------------------------------------------------------------------------------- 49. Cittārammaṇakathā
section("(49) 7. Cittārammaṇakathā", f"(49) 7. စိတ်ကို အာရုံပြုခြင်းအကြောင်း {KATHA}")
section("Cittārammaṇakathā", f"စိတ်ကို အာရုံပြုခြင်းအကြောင်း {KATHA}")
CT = {  # the mind states of pi-2 ^2-796 (cetopariya passage)
    "sarāgaṃ": "ရာဂ ရှိသော", "vītarāgaṃ": "ရာဂ ကင်းသော", "sadosaṃ": "ဒေါသ ရှိသော", "vītadosaṃ": "ဒေါသ ကင်းသော",
    "samohaṃ": "မောဟ ရှိသော", "vītamohaṃ": "မောဟ ကင်းသော", "saṃkhittaṃ": "တွန့်ဆုတ်နေသော",
    "vikkhittaṃ": "ပျံ့လွင့်နေသော", "mahaggataṃ": "ကြီးမြတ်သော", "amahaggataṃ": "မကြီးမြတ်သော",
    "sauttaraṃ": "ထိုထက် သာလွန်သည် ရှိသေးသော", "anuttaraṃ": "ထိုထက် သာလွန်သည် မရှိသော",
    "samāhitaṃ": "တည်ကြည်သော", "asamāhitaṃ": "မတည်ကြည်သော", "vimuttaṃ": "လွတ်မြောက်သော",
    "avimuttaṃ": "မလွတ်မြောက်သော"}
for _k, _m in CT.items():
    W("2", "^2-796", _k.replace("sauttaraṃ", "sauttaraṃ"), f"{_m} စိတ်")
PAJ = ("ကွဲပြားစွာ သိ", "ကွဲပြားစွာ မသိ")                            # pajānāti (pi-2 ^2-796)
for _k, _m in CT.items():
    P(f"atthi koci {_k} cittaṃ", FR(f"{_m} စိတ်ကို"))
    P(f"{_k} cittaṃ", FR(f"{_m} စိတ်ကို"))
    P(f"atthi koci {_k} cittaṃ {_k} cittanti pajānāti",
      V(f"{_m} စိတ်ကို «{_m} စိတ်»ဟု {PAJ[0]}သူ တစ်စုံတစ်ယောက်", EXIST))
    P(f"{_k} cittaṃ {_k} cittanti pajānāti", V(f"{_m} စိတ်ကို «{_m} စိတ်»ဟု {PAJ[0]}သူ တစ်စုံတစ်ယောက်", EXIST))
ARM = [("phass", "phassa", "တွေ့ထိမှု"), ("vedan", "vedanā", "ခံစားမှု"), ("saññ", "saññā", "မှတ်သိမှု"),
       ("cetan", "cetanā", "စေ့ဆော်မှု"), ("citt", "citta", "စိတ်"), ("saddh", "saddhā", "ယုံကြည်မှု"),
       ("vīriy", "vīriya", "ဝီရိယ"), ("sat", "sati", "သတိ"), ("samādh", "samādhi", "သမာဓိ"),
       ("paññ", "paññā", "ပညာ"), ("rāg", "rāga", "ရာဂ"), ("dos", "dosa", "ဒေါသ"), ("moh", "moha", "မောဟ"),
       ("anottapp", "anottappa", KIL["anottappaṃ"])]
for _k, _pp, _m in ARM:
    _x = f"{_k}ārammaṇe ñāṇaṃ"
    _xm = f"{_m}ကို အာရုံပြုသော {NANA}"
    P(_x, FR(f"{_xm}ကို"))
    P(f"{_x} vattabbaṃ – cetopariyāye ñāṇaṃ", SAYQ(f"{_xm}ကို", f"«{CPN}»ဟု"))
    P(f"{_x} na vattabbaṃ – cetopariyāye ñāṇaṃ", SAYQ(f"{_xm}ကို", f"«{CPN}»ဟု", neg=True))
    P(f"{_x} vattabbaṃ cetopariyāye ñāṇaṃ", Cl(f"{_xm}ကို {CPN}ဟု", "ဆိုသင့်", "မဆိုသင့်"))
    P(f"{_pp}pariyāye ñāṇaṃ", V(f"{_m}ကို ပိုင်းခြား၍ သိသော {NANA}"))
P("cetopariyāye ñāṇaṃ", V(CPN))

# ------------------------------------------------------------------------------------- 50. Anāgatañāṇakathā
ANAG = P6.ANAGATA
ANN = new("anāgate ñāṇaṃ", f"{ANAG}{KNOWING}")
section("(50) 8. Anāgatañāṇakathā", f"(50) 8. {ANN}အကြောင်း {KATHA}")
section("Anāgatañāṇakathā", f"{ANN}အကြောင်း {KATHA}")
P("anāgate ñāṇaṃ atthi", V(ANN, EXIST))
_BY = {"mūlato": "မူလ", "hetuto": "အမြစ်", "nidānato": "အစ", "sambhavato": "ဖြစ်ပေါ်ရာ", "pabhavato": "ပေါ်ပေါက်ရာ",
       "samuṭṭhānato": "ထကြွရာ", "āhārato": "အာဟာရ", "ārammaṇato": "အာရုံ", "paccayato": "အကြောင်း",
       "samudayato": "ဖြစ်ပေါ်ခြင်း"}
new("mūlato … samudayato jānāti", "၊ ".join(f"{m}အားဖြင့်" for m in _BY.values()) + " သိ")
P("anāgataṃ " + ", ".join(f"{k} jānāti" for k in _BY),
  VV(f"{ANAG}ကို " + "၊ ".join(f"{m}အားဖြင့် သိသည်" for m in list(_BY.values())[:-1]) + f"၊ {_BY['samudayato']}အားဖြင့်",
     "သိ"))
_PC = {"hetupaccayataṃ": "အမြစ်", "ārammaṇapaccayataṃ": "အာရုံ", "adhipatipaccayataṃ": "အကြီးအမှူး",
       "anantarapaccayataṃ": "ကြားမလပ်", "samanantarapaccayataṃ": "ကောင်းစွာ ကြားမလပ်"}
new("hetupaccayatā … samanantarapaccayatā", " / ".join(f"{m} အကြောင်း ဖြစ်ခြင်း" for m in _PC.values()))
P("anāgataṃ " + ", ".join(f"{k} jānāti" for k in _PC),
  VV(f"{ANAG}၏ " + "၊ ".join(f"{m} အကြောင်း ဖြစ်ခြင်းကို သိသည်" for m in list(_PC.values())[:-1])
     + f"၊ {_PC['samanantarapaccayataṃ']} အကြောင်း ဖြစ်ခြင်းကို", "သိ"))
Q("pāṭaliputtassa kho, ānanda, tayo antarāyā bhavissanti – aggito vā udakato vā mithubhedā vā",
  "အာနန္ဒာ၊ ပါဋလိပုတ်မြို့အား အန္တရာယ် သုံးပါး ဖြစ်လိမ့်မည် – မီးကြောင့်ဖြစ်စေ၊ ရေကြောင့်ဖြစ်စေ၊ "
  "အချင်းချင်း ကွဲပြားခြင်းကြောင့်ဖြစ်စေ")

# ------------------------------------------------------------------------------------- 51. Paṭuppannakathā
PACC = P6.PACCUP
PNN = new("paṭuppanne ñāṇaṃ", f"{PACC}{KNOWING}")
section("(51) 9. Paṭuppannakathā", f"(51) 9. {PACC}အကြောင်း {KATHA}")
LINES_X[key("Paṭuppannañāṇakathā [paccuppannakathā (sī.)] niṭṭhitā.")] = F.DONE.format(f"{PNN}အကြောင်း {KATHA}") \
    .replace("”", "” ⟦0⟧", 1) + END
VAR_X.update({"paccuppanne": F.LEKHANA, "paccuppannakathā": F.PATHA})
ANCHOR_X["Paṭuppanne"] = PACC
P("paṭuppanne ñāṇaṃ atthi", V(PNN, EXIST))
P("tena ñāṇena taṃ ñāṇaṃ jānāti", VV("ထိုဉာဏ်ဖြင့် ထိုဉာဏ်ကို", "သိ"))
P("tena ñāṇena taṃ ñāṇaṃ ñāṇanti jānāti", VV("ထိုဉာဏ်ဖြင့် ထိုဉာဏ်ကို «ဉာဏ်»ဟု", "သိ"))
P("taṃ ñāṇaṃ tassa ñāṇassa ārammaṇaṃ", V("ထိုဉာဏ်သည် ထိုဉာဏ်၏ အာရုံ"))
_SELF = [("tena phassena taṃ phassaṃ phusati", "တွေ့ထိမှု", "တွေ့ထိ"),
         ("tāya vedanāya taṃ vedanaṃ vedeti", "ခံစားမှု", "ခံစား"),
         ("tāya saññāya taṃ saññaṃ sañjānāti", "မှတ်သိမှု", "မှတ်သိ"),
         ("tāya cetanāya taṃ cetanaṃ ceteti", "စေ့ဆော်မှု", "စေ့ဆော်"),
         ("tena cittena taṃ cittaṃ cinteti", "စိတ်", "ကြံစည်"),
         ("tena vitakkena taṃ vitakkaṃ vitakketi", "စတင်ကြံစည်မှု", "စတင်ကြံစည်"),
         ("tena vicārena taṃ vicāraṃ vicāreti", "ဆက်လက်သုံးသပ်မှု", "ဆက်လက်သုံးသပ်"),
         ("tāya pītiyā taṃ pītiṃ piyāyati", "ပီတိ", "နှစ်သက်"),
         ("tāya satiyā taṃ satiṃ sarati", "သတိ", "အောက်မေ့"),
         ("tāya paññāya taṃ paññaṃ pajānāti", "ပညာ", "ကွဲပြားစွာ သိ"),
         ("tena khaggena taṃ khaggaṃ chindati", "ဓား", "ဖြတ်"),
         ("tena pharasunā taṃ pharasuṃ tacchati", "ပုဆိန်", "ခုတ်"),
         ("tāya kudhāriyā taṃ kudhāriṃ tacchati", "ပုဆိန်ငယ်", "ခုတ်"),
         ("tāya vāsiyā taṃ vāsiṃ tacchati", "ပေါက်ပြား", "ခုတ်"),
         ("tāya sūciyā taṃ sūciṃ sibbeti", "အပ်", "ချုပ်"),
         ("tena aṅgulaggena taṃ aṅgulaggaṃ parāmasati", "လက်ချောင်းဖျား", "ထိ"),
         ("tena nāsikaggena taṃ nāsikaggaṃ parāmasati", "နှာခေါင်းဖျား", "ထိ"),
         ("tena matthakena taṃ matthakaṃ parāmasati", "ဦးခေါင်း", "ထိ"),
         ("tena gūthena taṃ gūthaṃ dhovati", "ကျင်ကြီး", "ဆေး"),
         ("tena muttena taṃ muttaṃ dhovati", "ကျင်ငယ်", "ဆေး"),
         ("tena kheḷena taṃ kheḷaṃ dhovati", "တံတွေး", "ဆေး"),
         ("tena pubbena taṃ pubbaṃ dhovati", "ပြည်", "ဆေး"),
         ("tena lohitena taṃ lohitaṃ dhovati", "သွေး", "ဆေး")]
P(", ".join(p for p, _, _ in _SELF),
  VV("၊ ".join(f"ထို{n}ဖြင့် ထို{n}ကို {v}သည်" for _, n, v in _SELF[:-1]) + f"၊ ထို{_SELF[-1][1]}ဖြင့် "
     f"ထို{_SELF[-1][1]}ကို", _SELF[-1][2]))
new("tena X-ena taṃ X-aṃ … (the self-reference list)", "ထိုXဖြင့် ထိုXကို …")
P("sabbasaṅkhāre aniccato diṭṭhe tampi ñāṇaṃ aniccato diṭṭhaṃ hoti",
  Cl(f"{F.SANKHARA.my[:-len('တို့')]} အားလုံးကို မမြဲဟု မြင်ပြီးသောအခါ ထိုဉာဏ်ကိုလည်း မမြဲဟု", "မြင်ပြီး ဖြစ်",
     "မြင်ပြီး မဖြစ်"))

# ------------------------------------------------------------------------------------- 52. Phalañāṇakathā
PHN = new("phale ñāṇaṃ", f"ဖိုလ်{KNOWING}")
section("(52) 10. Phalañāṇakathā", f"(52) 10. {PHN}အကြောင်း {KATHA}")
section("Phalañāṇakathā", f"{PHN}အကြောင်း {KATHA}")
P("sāvakassa phale ñāṇaṃ atthi", V(f"{SAV}၌ {PHN}", EXIST))
P("sāvako phalassa kataṃ paññāpeti", VV(f"{SAV}သည် ဖိုလ်၏ ပြုလုပ်ချက်ကို", "သတ်မှတ်ဖော်ပြ"))
_PO = "မြင့်မြတ်ခြင်း နိမ့်ကျခြင်း"                                    # paropariyatta (pi-2 ^2-760 indriyaparopariyattaṃ)
P("atthi sāvakassa phalaparopariyatti indriyaparopariyatti puggalaparopariyatti",
  V(f"{SAV}၌ ဖိုလ်တို့ {_PO}ကို သိခြင်း၊ {F.INDRIYA_W}တို့ {_PO}ကို သိခြင်း၊ {PUG}တို့ {_PO}ကို သိခြင်း", EXIST))
new("X-paropariyatti", f"Xတို့ {_PO}ကို သိခြင်း")
_PN = [("khandha", F.KHANDHA_W), ("āyatana", F.AYATANA_W), ("dhātu", F.DHATU_W), ("sacca", "သစ္စာ"),
       ("indriya", F.INDRIYA_W), ("puggala", PUG)]
P("atthi sāvakassa " + " ".join(f"{k}paññatti" for k, _ in _PN),
  V(f"{SAV}၌ " + "၊ ".join(f"{m} {F.PANNATTI}" for _, m in _PN), EXIST))
for _s, _sm in (("sāvako", SAV),):
    pass
P("sāvako aññāṇī", V(f"{SAV}သည် {NANA} မရှိသူ"))
S("Na hevaṃ vattabba…pe….", F.NO_SAY + PE)
new("Mahāpaṇṇāsako", "ကြီးမားသော ငါးဆယ်အစု")
SENT_X["Mahāpaṇṇāsako."] = "ကြီးမားသော ငါးဆယ်အစု" + END
LINES_X[key("Tassāpi uddānaṃ –")] = "ထို၏လည်း အကျဉ်းချုပ် –"
LINES_X[key("Vimuttiñāṇaṃ vimuttaṃ, sekhassa asekhaṃ ñāṇaṃ, viparīte ñāṇaṃ, aniyatassa niyāmagamanāya atthi ñāṇaṃ, "
            "sabbaṃ ñāṇaṃ paṭisambhidāti, sammutiñāṇaṃ, cetopariyāye ñāṇaṃ, anāgate ñāṇaṃ, paṭuppanne ñāṇaṃ, "
            "sāvakassa phale ñāṇanti.")] = (
    f"{VN}သည် {VIMUTTA}၊ {SEKHA}၌ {AN}၊ {VPN}၊ {ANIYATA}၌ {GO['niyāmagamanāya']} {NANA} {EXIST}ခြင်း၊ "
    f"{NANA} အားလုံးသည် {PSB}၊ {SMN}၊ {CPN}၊ {ANN}၊ {PNN}၊ {SAV}၌ {PHN}{END}")
LINES_X[key("Sattupaladdhiṃ, upaharato, balaṃ, gihissa arahā ca, vimuttipañcamanti.")] = (
    f"သတ္တဝါကို တွေ့ရခြင်း၊ {P6.LST['parūpahāro']}၊ စွမ်းအား၊ {P11.GIHI} {ARAHA}၊ ပဉ္စမ လွတ်မြောက်ခြင်း{END}")

# ===================================================================================== 14. Chaṭṭhavaggo
section("Chaṭṭhavaggo", f"{F.ORD_MY[6]} {F.VAGGA_W}")
COLO_X["Chaṭṭhavaggo"] = HEAD_X["Chaṭṭhavaggo"]
SKT, ASKT = f"{F.SANKHATA} အရာ", f"{F.ASANKHATA} အရာ"               # saṅkhata / asaṅkhata (ch6-10 _VP wording)
NUMS = {"dve": 2, "tīṇi": 3, "cattāri": 4, "pañca": 5, "dvādasa": 12}
REF5 = ["tāṇāni", "leṇāni", "saraṇāni", "parāyanāni", "accutāni", "amatāni", "nibbānāni"]
REF5_MY = {"tāṇāni": "ကာကွယ်ရာ", "leṇāni": "ပုန်းအောင်းရာ", "saraṇāni": "ကိုးကွယ်ရာ", "parāyanāni": "မှီခိုရာ",
           "accutāni": "မစုတေသော အရာ", "amatāni": "အမြိုက်", "nibbānāni": F.NIBBANA}     # ch6-10 (^5-332 …)
P("nibbānaṃ tāṇaṃ leṇaṃ saraṇaṃ parāyanaṃ accutaṃ amataṃ",
  V(f"{F.NIBBANA}၊ " + "၊ ".join(REF5_MY[k] for k in REF5[:-1])))
new("nibbānaṃ tāṇaṃ leṇaṃ saraṇaṃ parāyanaṃ accutaṃ amataṃ", f"{F.NIBBANA}၊ " + "၊ ".join(REF5_MY[k] for k in REF5[:-1]))
for _n, _v in NUMS.items():
    _nm = f"{F.NUM_MY[_v]}{F.CL}"
    P(f"{_n} asaṅkhatāni", V(f"{ASKT} {_nm}", EXIST))
    P(" ".join(f"{_n} {k}" for k in REF5), V("၊ ".join(f"{REF5_MY[k]} {_nm}" for k in REF5), EXIST))
    for _k in ("tāṇāni", "nibbānāni"):
        if not has(f"{_n} {_k}"):
            P(f"{_n} {_k}", V(f"{REF5_MY[_k]} {_nm}", EXIST))
    P(f"{_n} tāṇāni {_n} leṇāni", V(f"{REF5_MY['tāṇāni']} {_nm}၊ {REF5_MY['leṇāni']} {_nm}", EXIST))
_UCC = F.PROP["atthi dvinnaṃ nibbānānaṃ uccanīcatā hīnapaṇītatā ukkaṃsāvakaṃso sīmā vā bhedo vā rāji vā antarikā vā"]
P("atthi catunnaṃ nibbānānaṃ uccanīcatā hīnapaṇītatā ukkaṃsāvakaṃso sīmā vā bhedo vā rāji vā antarikā vā",
  V(_UCC.pre.replace(f"{F.NUM_MY[2]}{F.CL}", f"{F.NUM_MY[4]}{F.CL}", 1), EXIST))
P("antarikā vā", V("ကြားအပိုင်းဖြစ်စေ", EXIST))
SUBJ14 = {  # subjects of «X (a)saṅkhato / -ā / -aṃ / -āni»
    "niyāmo": NIYAMA, "maggo": "မဂ်", "sammattaniyāmo": SN, "micchattaniyāmo": f"မှားယွင်းမှု၌ {NIYAMA}",
    "paṭiccasamuppādo": F.heads("Paṭiccasamuppādavibhaṅgo").split("ကို ")[0] if False else "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ",
    "avijjā": "အမှန်ကို မသိမှု", "dukkhasaccaṃ": "ဒုက္ခ သစ္စာ", "samudayasaccaṃ": "ဖြစ်ပေါ်ခြင်း သစ္စာ",
    "nirodhasaccaṃ": "ချုပ်ငြိမ်းခြင်း သစ္စာ", "maggasaccaṃ": "မဂ် သစ္စာ", "dukkhaṃ": "ဒုက္ခ",
    "samudayo": "ဖြစ်ပေါ်ခြင်း", "nirodho": "ချုပ်ငြိမ်းခြင်း", "sammāsamādhi": "မှန်ကန်သော သမာဓိ",
    "cattāri saccāni": f"သစ္စာ {F.NUM_MY[4]}{F.CL}", "ākāsānañcāyatanaṃ": ATT["ākāsānañcāyatanaṃ"],
    "nirodhasamāpatti": "ချုပ်ငြိမ်းခြင်း သမာပတ်", "ākāso": "ဟင်းလင်းပြင်",
    "cattāro āruppā": f"ရုပ်မရှိသော ဘုံ {F.NUM_MY[4]}{F.CL}",
}
W("1", "^1-1063", "idappaccayatā", "ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ")
PSAM = W("2", "^2-225", "Avijjāpaccayā saṅkhārā", "အမှန်ကို မသိမှုကြောင့် ပြုပြင်ဖန်တီးမှုများ ဖြစ်ပေါ်")
CHAIN = {"avijjāpaccayā saṅkhārā": ("အမှန်ကို မသိမှု", "ပြုပြင်ဖန်တီးမှုများ"),
         "saṅkhārapaccayā viññāṇaṃ": ("ပြုပြင်ဖန်တီးမှုများ", "သိစိတ်"),
         "viññāṇapaccayā nāmarūpaṃ": ("သိစိတ်", "စိတ်ပိုင်းနှင့် ရုပ်ပိုင်း"),
         "jātipaccayā jarāmaraṇaṃ": ("မွေးဖွားခြင်း", "အိုခြင်း၊ သေခြင်း")}
for _k, (_a, _b) in CHAIN.items():
    W("2", "^2-225", _k.split()[0], f"{_a}ကြောင့် {_b}")
    SUBJ14[_k] = f"{_a}ကြောင့် ဖြစ်ပေါ်သော {_b}"
    P(TI(_k), FR(f"{_a}ကြောင့် {_b} ဖြစ်ပေါ်သည်"))
SOKA = W("2", "^2-225", "sokaparidevadukkhadomanassupāyāsā", "စိုးရိမ်ခြင်း၊ ငိုကြွေးခြင်း၊ ကိုယ်ဆင်းရဲခြင်း၊ "
         "စိတ်ဆင်းရဲမှု၊ ပြင်းစွာ ပူပန်ခြင်းတို့")
SUBJ14["kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ sokaparidevadukkhadomanassaupāyāsā"] = f"ကိုယ်၏ ဒုက္ခ၊ စိတ်၏ ဒုက္ခ၊ {SOKA}"
SUBJ14["kāmataṇhā bhavataṇhā vibhavataṇhā"] = W("2", "^2-916", "Kāmataṇhā, bhavataṇhā, vibhavataṇhā",
                                                "ကာမကို တပ်မက်မှု၊ ဘဝကို တပ်မက်မှု၊ ဘဝ ပျောက်ကွယ်ခြင်းကို တပ်မက်မှု")
for _k, _m in (("sotāpatti", "သောတာပတ္တိ"), ("sakadāgāmi", "သကဒါဂါမိ"), ("anāgāmi", "အနာဂါမိ"), ("arahatta", "ရဟန္တာ")):
    SUBJ14[f"{_k}niyāmo"] = f"{_m} {NIYAMA}"
    SUBJ14[f"{_k}maggo"] = MG[_k]
    P(f"{_k}niyāmo", FR(f"{_m} {NIYAMA}"))
new("sotāpattiniyāmo … arahattaniyāmo", f"သောတာပတ္တိ {NIYAMA} … ရဟန္တာ {NIYAMA}")
new("micchattaniyāmo", SUBJ14["micchattaniyāmo"])
P("sammādiṭṭhi", FR(F.SAMMADITTHI)) if "sammādiṭṭhi" not in F.PROP else None
for _s, _sm in SUBJ14.items():
    for _a, _am in (("", SKT), ("a", ASKT)):
        for _e in ("o", "ā", "aṃ", "āni"):
            P(f"{_s} {_a}saṅkhat{_e}", V(f"{_sm}သည် {_am}"))
P("saṅkhatā", V(SKT))
P("asaṅkhataṃ", FR(ASKT))
P("saṅkhataṃ asaṅkhataṃ hoti", Cl(f"{SKT}သည် {ASKT}", *BEC))
_OKK = ["okkamanti", "paṭilabhanti", "uppādenti", "samuppādenti", "uṭṭhāpenti", "samuṭṭhāpenti", "nibbattenti",
        "abhinibbattenti", "janenti", "sañjanenti"]
_OKK_MY = ["သက်ဆင်းကြ", "ရရှိကြ", "ဖြစ်ပေါ်စေကြ", "ကောင်းစွာ ဖြစ်ပေါ်စေကြ", "ထစေကြ", "ကောင်းစွာ ထစေကြ", "ဖြစ်စေကြ",
           "ထူးကဲစွာ ဖြစ်စေကြ", "မွေးဖွားစေကြ", "ကောင်းစွာ မွေးဖွားစေကြ"]
new("okkamanti paṭilabhanti … sañjanenti", "၊ ".join(_OKK_MY))
SOME_P = P6.SOME                                                     # «အချို့»
for _o, _om, _v1, _v1m in (("niyāmaṃ", f"{NIYAMA}သို့", "okkamanti", "သက်ဆင်းကြ"),
                           ("asaṅkhataṃ", f"{ASKT}သို့", "okkamanti", "သက်ဆင်းကြ"),
                           ("nirodhaṃ", "ချုပ်ငြိမ်းခြင်း သမာပတ်ကို", "samāpajjanti", "ဝင်စားကြ"),
                           ("asaṅkhataṃ", f"{ASKT}ကို", "samāpajjanti", "ဝင်စားကြ")):
    for _ut, _utm in (("uṭṭhāpenti samuṭṭhāpenti", None), ("uṭṭhapenti samuṭṭhapenti", None)):
        _pi = " ".join([_v1] + _OKK[1:4]) + f" {_ut} " + " ".join(_OKK[6:])
        P(f"atthi keci {_o} {_pi}", V(f"{_om} " + "၊ ".join([_v1m] + _OKK_MY[1:]) + f"သူ {SOME_P}", EXIST))
P("niyāme uppajja niruddhe aniyato hoti",
  Cl(f"{NIYAMA} ဖြစ်ပေါ်၍ ချုပ်ငြိမ်းသွားသောအခါ {ANIYATA}", *BEC))
P("micchattaniyāme uppajja niruddhe aniyato hoti",
  Cl(f"{SUBJ14['micchattaniyāmo']} ဖြစ်ပေါ်၍ ချုပ်ငြိမ်းသွားသောအခါ {ANIYATA}", *BEC))

# ------------------------------------------------------------------------------------- 53-54
section("(53) 1. Niyāmakathā", f"(53) 1. {NIYAMA}အကြောင်း {KATHA}")
PS_N = "အကြောင်းတို့ကို မှီ၍ ဖြစ်ပေါ်ပုံ"
W("1", "^1-1-1-0", "paṭiccasamuppād", PS_N) if False else None
section("(54) 2. Paṭiccasamuppādakathā", f"(54) 2. {PS_N}အကြောင်း {KATHA}")
section("Paṭiccasamuppādakathā", f"{PS_N}အကြောင်း {KATHA}")
_DT = "ထိုအရာ၌ ရှိသော တရား၏ တည်ရှိခြင်း၊ တရား၏ သေချာခြင်း"           # yā tattha dhammaṭṭhitatā dhammaniyāmatā
new("dhammaṭṭhitatā dhammaniyāmatā", "တရား၏ တည်ရှိခြင်း၊ တရား၏ သေချာခြင်း")
for _k, (_a, _b) in CHAIN.items():
    P(f"{TI(_k)} yā tattha dhammaṭṭhitatā dhammaniyāmatā asaṅkhatā",
      V(f"{_a}ကြောင့် {_b} ဖြစ်ပေါ်သည်ဟူသော {_DT}သည် {ASKT}"))
_R = "ရဟန်းတို့၊"
_UPP = "မြတ်စွာဘုရားတို့ ပွင့်ပေါ်သည် ဖြစ်စေ၊ မပွင့်ပေါ်သည် ဖြစ်စေ ထိုဓာတ်သည် တည်လျက်ပင် ရှိ၏"
Q("jātipaccayā, bhikkhave, jarāmaraṇaṃ. Uppādā vā tathāgatānaṃ anuppādā vā tathāgatānaṃ ṭhitāva sā dhātu "
  "dhammaṭṭhitatā dhammaniyāmatā idappaccayatā. Taṃ tathāgato abhisambujjhati abhisameti. Abhisambujjhitvā "
  "abhisametvā ācikkhati deseti paññāpeti paṭṭhapeti vivarati vibhajati uttāniṃ karoti. ‘Passathā’ti cāha – "
  "jātipaccayā, bhikkhave, jarāmaraṇaṃ. Bhavapaccayā, bhikkhave, jāti…pe… avijjāpaccayā, bhikkhave, saṅkhārā. "
  "Uppādā vā tathāgatānaṃ anuppādā vā tathāgatānaṃ ṭhitāva sā dhātu…pe… ‘passathā’ti cāha – avijjāpaccayā, "
  "bhikkhave, saṅkhārā. Iti kho, bhikkhave, yā tatra tathatā avitathatā anaññathatā idappaccayatā – ayaṃ vuccati, "
  "bhikkhave, paṭiccasamuppādo",
  f"{_R} မွေးဖွားခြင်းကြောင့် အိုခြင်း၊ သေခြင်း ဖြစ်ပေါ်၏။ {_UPP}၊ တရား၏ တည်ရှိခြင်း၊ တရား၏ သေချာခြင်း၊ "
  "ဤအကြောင်းကြောင့် ဤအကျိုး ဖြစ်ပုံ ဖြစ်၏။ ထိုတရားကို မြတ်စွာဘုရားသည် ထိုးထွင်း သိတော်မူ၏၊ ကောင်းစွာ "
  "သိတော်မူ၏။ ထိုးထွင်း သိ၍ ကောင်းစွာ သိပြီးလျှင် ပြောကြား၏၊ ဟောကြား၏၊ သတ်မှတ်ဖော်ပြ၏၊ တည်ထောင်၏၊ ဖွင့်ပြ၏၊ "
  f"ခွဲခြားပြ၏၊ ထင်ရှားအောင် ပြု၏။ ‹ကြည့်ကြလော့›ဟုလည်း မိန့်တော်မူ၏ – {_R} မွေးဖွားခြင်းကြောင့် အိုခြင်း၊ "
  f"သေခြင်း ဖြစ်ပေါ်၏။ {_R} ဘဝကြောင့် မွေးဖွားခြင်း ဖြစ်ပေါ်၏… {_R} အမှန်ကို မသိမှုကြောင့် ပြုပြင်ဖန်တီးမှုများ "
  f"ဖြစ်ပေါ်၏။ {_UPP}… ‹ကြည့်ကြလော့›ဟုလည်း မိန့်တော်မူ၏ – {_R} အမှန်ကို မသိမှုကြောင့် ပြုပြင်ဖန်တီးမှုများ "
  f"ဖြစ်ပေါ်၏။ {_R} ဤသို့လျှင် ထိုအရာ၌ ရှိသော ဟုတ်မှန်ခြင်း၊ မဖောက်ပြန်ခြင်း၊ အခြား မဟုတ်ခြင်း၊ ဤအကြောင်းကြောင့် "
  f"ဤအကျိုး ဖြစ်ပုံ – {_R} ဤသည်ကို {PS_N}ဟု ခေါ်၏")
new("tathatā avitathatā anaññathatā", "ဟုတ်မှန်ခြင်း၊ မဖောက်ပြန်ခြင်း၊ အခြား မဟုတ်ခြင်း")

# ------------------------------------------------------------------------------------- 55. Saccakathā
section("(55) 3. Saccakathā", f"(55) 3. သစ္စာအကြောင်း {KATHA}")
section("Saccakathā", f"သစ္စာအကြောင်း {KATHA}")
P(f"cattāri {' cattāri '.join(REF5)}".replace("cattāri tāṇāni", "cattāri tāṇāni", 1),
  V("၊ ".join(f"{REF5_MY[k]} {F.NUM_MY[4]}{F.CL}" for k in REF5), EXIST)) \
    if key("cattāri " + " cattāri ".join(REF5)) not in PROP_X else None
_T3 = "ဟုတ်မှန်၏၊ မဖောက်ပြန်၊ အခြား မဟုတ်"
Q("cattārimāni, bhikkhave, tathāni avitathāni anaññathāni! Katamāni cattāri? ‘Idaṃ dukkha’nti, bhikkhave, "
  "tathametaṃ avitathametaṃ anaññathametaṃ…pe… ‘ayaṃ dukkhasamudayo’ti…pe… ‘ayaṃ dukkhanirodho’ti…pe… ‘ayaṃ "
  "dukkhanirodhagāminī paṭipadā’ti tathametaṃ avitathametaṃ anaññathametaṃ. Imāni kho, bhikkhave, cattāri tathāni "
  "avitathāni anaññathānī",
  f"{_R} ဟုတ်မှန်သော၊ မဖောက်ပြန်သော၊ အခြား မဟုတ်သော ဤအရာ လေးပါးတို့ ရှိကုန်၏။ အဘယ် လေးပါးနည်း။ {_R} "
  f"‹ဤသည်ကား ဒုက္ခ›ဟူသည် {_T3}… ‹ဤသည်ကား ဒုက္ခ ဖြစ်ပေါ်ခြင်း›ဟူ၍… ‹ဤသည်ကား ဒုက္ခ ချုပ်ငြိမ်းခြင်း›ဟူ၍… "
  f"‹ဤသည်ကား {P11._TR['dukkhanirodhagāminī paṭipadā']}›ဟူသည် {_T3}။ {_R} ဤအရာ လေးပါးတို့သည် ဟုတ်မှန်ကုန်၏၊ "
  "မဖောက်ပြန်ကုန်၊ အခြား မဟုတ်ကုန်")
new("tatha / avitatha / anaññatha", "ဟုတ်မှန် / မဖောက်ပြန် / အခြား မဟုတ်")

# ------------------------------------------------------------------------------------- 56. Āruppakathā
ARUPPA = new("cattāro āruppā", SUBJ14["cattāro āruppā"])
section("(56) 4. Āruppakathā", f"(56) 4. ရုပ်မရှိသော ဘုံအကြောင်း {KATHA}")
section("Āruppakathā", f"ရုပ်မရှိသော ဘုံအကြောင်း {KATHA}")
AKA = ATT["ākāsānañcāyatanaṃ"]
_EXL = "ဘဝ၊ " + "၊ ".join(P11.TOK[k] for k in ("gati", "sattāvāso", "saṃsāro", "yoni")) + \
       f"၊ သိစိတ် တည်ရာ၊ {P11.TOK['attabhāvapaṭilābho']}"
new("viññāṇaṭṭhiti", "သိစိတ် တည်ရာ")
P("ākāsānañcāyatanaṃ bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho", V(f"{AKA}သည် {_EXL}"))
P("asaṅkhataṃ bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho", V(f"{ASKT}သည် {_EXL}"))
for _a, _am in (("ākāsānañcāyatan", AKA), ("asaṅkhat", ASKT)):
    P(f"atthi {_a}ūpagaṃ kammaṃ", V(f"{_am}သို့ ရောက်စေသော ကံ", EXIST))
    P(f"atthi {_a}ūpagā sattā", V(f"{_am}သို့ ရောက်သော {F.SATTA}တို့", EXIST))
    P(f"{_a}e sattā jāyanti jīyanti mīyanti cavanti upapajjanti",
      Cl(f"{_am}၌ {F.SATTA}တို့ မွေးဖွားကြ၏၊ အိုကြ၏၊ သေဆုံးကြ၏၊ စုတေကြ၏၊", "ပြန်လည် ဖြစ်ပေါ်ကြ", "ပြန်လည် မဖြစ်ပေါ်ကြ"))
    P(f"{_a}e atthi vedanā saññā saṅkhārā viññāṇaṃ",
      V(f"{_am}၌ {F.VEDANA.my}၊ {F.SANNA.my}၊ {F.SANKHARA.my}၊ {F.VINNANA.my}", EXIST))
P("asaṅkhataṃ catuvokārabhavo", V(f"{ASKT}သည် {P11.TOK['catuvokārabhavo']}"))
ANEJA = new("aneja (of the āruppa)", "မတုန်လှုပ်သော အရာ")
P("cattāro āruppā anejā vuttā bhagavatā", Cl(f"{ARUPPA}ကို {ANEJA}ဟု {BUDDHA}", "ဟောတော်မူ", "မဟောတော်မူ"))


@F.frame(r"Hañci (?P<p>.+?), tena vata re vattabbe (?P<q>[^–]+?)ti\.")
def _f_if_nodash(m):
    """Hañci P, tena vata re vattabbe "Q"ti. (no dash, ^5-456): the dash stays out."""
    return f"အကယ်၍ {F.pq(m['p'], 'cond')} ထို့ကြောင့် အမှန်ပင် ဤသို့ ဆိုသင့်သည် “{F.pq(m['q'], 'stmt', 1)}”{END}"


before_generic()

# ------------------------------------------------------------------------------------- 57. Nirodhasamāpattikathā
NSM = SUBJ14["nirodhasamāpatti"]
section("(57) 5. Nirodhasamāpattikathā", f"(57) 5. {NSM}အကြောင်း {KATHA}")
section("Nirodhasamāpattikathā", f"{NSM}အကြောင်း {KATHA}")
new("nirodhasamāpatti", NSM)
for _a, _am in (("nirodhā", f"{NSM}မှ"), ("asaṅkhatā", f"{ASKT}မှ")):
    P(f"{_a} vodānaṃ vuṭṭhānaṃ paññāyati", Cl(f"{_am} စင်ကြယ်ခြင်း၊ ထမြောက်ခြင်း", "ထင်ရှား", "မထင်ရှား"))
    P(f"{_a} vuṭṭhitaṃ tayo phassā phusanti – suññato phasso, animitto phasso, appaṇihito phasso",
      Cl(f"{_am} ထမြောက်ပြီးသူကို တွေ့ထိမှု {F.NUM_MY[3]}{F.CL}တို့", "တွေ့ထိကြ", "မတွေ့ထိကြ",
         post=" – ဆိတ်သုဉ်းသော တွေ့ထိမှု၊ အမှတ်အသား မရှိသော တွေ့ထိမှု၊ တောင့်တမှု မရှိသော တွေ့ထိမှု"))
    P(f"{_a} vuṭṭhitassa vivekaninnaṃ cittaṃ hoti vivekapoṇaṃ vivekapabbhāraṃ",
      V(f"{_am} ထမြောက်ပြီးသူ၏ စိတ်သည် ကင်းဆိတ်ခြင်းသို့ ညွတ်သော၊ ကင်းဆိတ်ခြင်းသို့ ကိုင်းသော၊ "
        "ကင်းဆိတ်ခြင်းသို့ ရှိုင်းသော စိတ်"))
    P(f"{_a} vuṭṭhahantassa paṭhamaṃ uppajjati cittasaṅkhāro, tato kāyasaṅkhāro, tato vacīsaṅkhāro",
      Cl(f"{_am} ထမြောက်နေသူ၏ ပထမဦးစွာ စိတ်၏ ပြုပြင်ဖန်တီးမှု ဖြစ်ပေါ်၏၊ ထို့နောက် ကိုယ်၏ ပြုပြင်ဖန်တီးမှု၊ "
         "ထို့နောက် နှုတ်၏ ပြုပြင်ဖန်တီးမှု", "ဖြစ်ပေါ်", "မဖြစ်ပေါ်"))
for _a, _am in (("nirodhaṃ", f"{NSM}ကို"), ("asaṅkhataṃ", f"{ASKT}ကို")):
    P(f"{_a} samāpajjantassa paṭhamaṃ nirujjhati vacīsaṅkhāro, tato kāyasaṅkhāro, tato cittasaṅkhāro",
      Cl(f"{_am} ဝင်စားနေသူ၏ ပထမဦးစွာ နှုတ်၏ ပြုပြင်ဖန်တီးမှု ချုပ်ငြိမ်း၏၊ ထို့နောက် ကိုယ်၏ ပြုပြင်ဖန်တီးမှု၊ "
         "ထို့နောက် စိတ်၏ ပြုပြင်ဖန်တီးမှု", "ချုပ်ငြိမ်း", "မချုပ်ငြိမ်း"))
new("vivekaninnaṃ … vivekapabbhāraṃ", "ကင်းဆိတ်ခြင်းသို့ ညွတ်သော၊ … ကိုင်းသော၊ … ရှိုင်းသော")

# ------------------------------------------------------------------------------------- 58. Ākāsakathā
AKS = "ဟင်းလင်းပြင်"
section("(58) 6. Ākāsakathā", f"(58) 6. {AKS}အကြောင်း {KATHA}")
section("Ākāsakathā", f"{AKS}အကြောင်း {KATHA}")
for _a, _am, _b, _bm in (("anākāsaṃ", f"{AKS} မဟုတ်သော အရာကို", "ākāsaṃ", AKS), ("ākāsaṃ", f"{AKS}ကို", "anākāsaṃ",
                                                                                  f"{AKS} မဟုတ်သော အရာ"),
                         ("saṅkhataṃ", f"{SKT}ကို", "asaṅkhataṃ", ASKT), ("asaṅkhataṃ", f"{ASKT}ကို", "saṅkhataṃ", SKT)):
    P(f"atthi keci {_a} {_b} karonti", V(f"{_am} {_bm}အဖြစ် ပြုလုပ်ကြသူ {SOME_P}", EXIST))
_SKY = [("pakkhino gacchanti", "ငှက်တို့ သွားကြ"), ("candimasūriyā gacchanti", "လနှင့် နေတို့ သွားကြ"),
        ("tārakarūpāni gacchanti", "ကြယ်တာရာတို့ သွားကြ"), ("iddhiṃ vikubbanti", f"{F.IDDHI}ကို ဖန်ဆင်းကြ"),
        ("bāhuṃ cālenti", "လက်မောင်းကို လှုပ်ကြ"), ("pāṇiṃ cālenti", "လက်ကို လှုပ်ကြ"),
        ("leḍḍuṃ khipanti", "မြေစိုင်ခဲကို ပစ်ကြ"), ("laguḷaṃ khipanti", "တုတ်ကို ပစ်ကြ"),
        ("iddhiṃ khipanti", f"{F.IDDHI}ကို ⟦b⟧ ပစ်ကြ"), ("usuṃ khipanti", "မြားကို ပစ်ကြ")]
for _a, _am, _slot in (("ākāse", f"{AKS}၌", True), ("asaṅkhate", f"{ASKT}၌", False)):
    _my = [m if _slot else m.replace(" ⟦b⟧", "") for _, m in _SKY]
    P(f"{_a} " + ", ".join(p for p, _ in _SKY),
      Cl(f"{_am} " + "၏၊ ".join(_my[:-1]) + "၏၊ မြားကို", "ပစ်ကြ", "မပစ်ကြ"))
VAR_X["sattiṃ"] = F.PATHA
for _a, _am in (("ākāsaṃ", f"{AKS}ကို"), ("asaṅkhataṃ", f"{ASKT}ကို")):
    P(f"{_a} parivāretvā gharāni karonti koṭṭhāni karonti",
      Cl(f"{_am} ဝန်းရံ၍ အိမ်တို့ကို ဆောက်ကြ၏၊ ကျီတို့ကို", "ဆောက်ကြ", "မဆောက်ကြ"))
P("udapāne khaññamāne anākāso ākāso hoti", Cl(f"ရေတွင်းကို တူးနေစဉ် {AKS} မဟုတ်သော အရာသည် {AKS}", *BEC))
P("tucchaudapāne pūriyamāne, tucchakoṭṭhe pūriyamāne, tucchakumbhiyā pūriyamānāya ākāso antaradhāyati",
  Cl(f"ဗလာ ရေတွင်းကို ဖြည့်နေစဉ်၊ ဗလာ ကျီကို ဖြည့်နေစဉ်၊ ဗလာ အိုးကို ဖြည့်နေစဉ် {AKS}", "ကွယ်ပျောက်", "မကွယ်ပျောက်"))
P("asaṅkhataṃ antaradhāyati", Cl(ASKT, "ကွယ်ပျောက်", "မကွယ်ပျောက်"))

# ------------------------------------------------------------------------------------- 59-62. … sanidassana
SAN = f"{F.SANIDASSANA} အရာ"
_RUPA_LIST = F.PROP["puggalo rūpaṃ rūpāyatanaṃ rūpadhātu nīlaṃ pītakaṃ lohitakaṃ odātaṃ cakkhuviññeyyaṃ cakkhusmiṃ "
                    "paṭihaññati"]
_RL = _RUPA_LIST.pre[len(f"{PUG}သည် "):]                              # «ရုပ်၊ … မျက်စိဖြင့် သိနိုင်သော အရာ ဖြစ်၍ မျက်စိ၌»
SUBJ_SAN = {"ākāso": (AKS, "ākāsañca"), "pathavīdhātu": ("မြေဓာတ်", "pathavīdhātuñca"),
            "cakkhundriyaṃ": (F.INDRIYA["cakkhundriya"].my, "cakkhundriyañca"),
            "kāyakammaṃ": ("ကိုယ်ဖြင့် ပြုသော ကံ", "kāyakammañca")}
W("2", "^2-?" if False else "^2-1", "rūpakkhandho", F.KHANDHA_W) if False else None
W("1", "^1-985", "kāyakammaṃ", "ကိုယ်ဖြင့် ပြုသော ကံ")
for _d, _dm in (("pathavī", "မြေ"), ("āpo", "ရေ"), ("tejo", "မီး"), ("vāyo", "လေ")):
    SUBJ_SAN[f"{_d}dhātu"] = (f"{_dm}ဓာတ်", f"{_d}dhātuñca")
W("2", "^2-?" if False else "^2-1", "Pathavīdhātu", "") if False else None
SUBJ_SAN["pañcindriyāni"] = (f"{F.INDRIYA_W} {F.NUM_MY[5]}{F.CL}တို့", None)
_SANH = {"ākāso": "ākāso sanidassano", "pathavīdhātu": "pathavīdhātu sanidassanā",
         "cakkhundriyaṃ": "cakkhundriyaṃ sanidassanaṃ", "kāyakammaṃ": "kāyakammaṃ sanidassanaṃ"}
for _s, (_sm, _ca) in SUBJ_SAN.items():
    _e = {"ākāso": "o", "cakkhundriyaṃ": "aṃ", "kāyakammaṃ": "aṃ", "pañcindriyāni": "āni"}.get(_s, "ā")
    P(f"{_s} sanidassan{_e}", V(f"{_sm}သည် {SAN}"))
    if _ca:
        P(f"cakkhuñca paṭicca {_ca} uppajjati cakkhuviññāṇaṃ",
          Cl(f"မျက်စိကိုလည်းကောင်း၊ {_sm}ကိုလည်းကောင်း မှီ၍ မျက်စိ သိစိတ်", "ဖြစ်ပေါ်", "မဖြစ်ပေါ်"))
P("cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṃ",
  Cl("မျက်စိကိုလည်းကောင်း၊ အဆင်းအရောင်တို့ကိုလည်းကောင်း မှီ၍ မျက်စိ သိစိတ်", "ဖြစ်ပေါ်", "မဖြစ်ပေါ်"))
W("2", "^2-?" if False else "^2-1", "", "") if False else None
P("rūpaṃ rūpāyatanaṃ rūpadhātu nīlaṃ pītakaṃ lohitakaṃ odātaṃ cakkhuviññeyyaṃ cakkhusmiṃ paṭihaññati "
  "cakkhussa āpāthaṃ āgacchati", Cl(f"{_RL} ထိခိုက်၍ မျက်စိ၏ အာရုံ နယ်ပယ်သို့", "ရောက်လာ", "မရောက်လာ"))
P("rūpaṃ rūpāyatanaṃ rūpadhātu", FR(_RL.split("၊ ")[0] + "၊ " + _RL.split("၊ ")[1] + "၊ " + _RL.split("၊ ")[2]))
SUTTA_Q = {}
for _k in [f"cakkhuñca paṭicca {c} uppajjati cakkhuviññāṇaṃ" for c in
           ("ākāsañca", "pathavīdhātuñca", "cakkhundriyañca", "kāyakammañca", "rūpe ca")]:
    _q = F.PROP[key(_k)].f("stmt", 1) if key(_k) in F.PROP else PROP_X[key(_k)].f("stmt", 1)
    P(f"{TI(_k)} – attheva suttanto", V(f"«{_q}»{F.SUTTA_TI} – {F.SUTTA_IS}", EXIST))   # harmonise B5: F.SUTTA_*
ANCHOR_X["attheva"] = "အမှန်ပင်"
ANCHOR_X["cakkhuviññāṇanti"] = "”ဟု"
BR_X["[ma. ni. 1.400; 3.421; saṃ. ni. 4.60]"] = f"[{F.REF['ma. ni.']} 1.400၊ 3.421၊ {F.REF['saṃ. ni.']} 4.60]"
VAR_X["atthi"] = F.PATHA
P("passati dvinnaṃ rukkhānaṃ antaraṃ, dvinnaṃ thambhānaṃ antaraṃ, tāḷacchiddaṃ vātapānacchiddaṃ",
  VV(f"သစ်ပင် {F.NUM_MY[2]}ပင်တို့၏ ကြားကို၊ တိုင် {F.NUM_MY[2]}တိုင်တို့၏ ကြားကို၊ သော့ပေါက်ကို၊ "
     "လေသာပြတင်းပေါက်ကို", "မြင်"))
P("passati bhūmiṃ pāsāṇaṃ pabbataṃ", VV("မြေကို၊ ကျောက်ကို၊ တောင်ကို", "မြင်"))
VAR_X["passasi"] = F.PATHA
BR_X["[passasi (sī. syā. ka.) evamuparipi]"] = "[ပါဌ်ကွဲ (Sī., Syā., Ka.): passasi၊ အထက်၌လည်း ဤနည်းတူ]"
P("passati udakaṃ", VV("ရေကို", "မြင်"))
P("passati aggiṃ jalantaṃ", VV("တောက်လောင်နေသော မီးကို", "မြင်"))
P("passati vātena rukkhe sañcāliyamāne", VV("လေကြောင့် လှုပ်ယမ်းနေသော သစ်ပင်တို့ကို", "မြင်"))
P("passati cakkhuṃ sotaṃ ghānaṃ jivhaṃ kāyaṃ", VV("မျက်စိ၊ နား၊ နှာခေါင်း၊ လျှာ၊ ကိုယ်ကို", "မြင်"))
P("passati abhikkamantaṃ paṭikkamantaṃ ālokentaṃ vilokentaṃ samiñjentaṃ pasārentaṃ",
  VV("ရှေ့သို့ တိုးသွားသူ၊ နောက်သို့ ဆုတ်သူ၊ ရှေ့သို့ ကြည့်သူ၊ ဘေးသို့ ကြည့်သူ၊ ကွေးသူ၊ ဆန့်သူကို", "မြင်"))
section("(59) 7. Ākāso sanidassanotikathā", f"(59) 7. {AKS}သည် {SAN} ဖြစ်သည်ဟူသော {KATHA}")
section("Ākāso sanidassanotikathā", f"{AKS}သည် {SAN} ဖြစ်သည်ဟူသော {KATHA}")
section("(60) 8. Pathavīdhātu sanidassanātiādikathā", f"(60) 8. မြေဓာတ်သည် {SAN} ဖြစ်သည် စသည်ဟူသော {KATHA}")
section("Pathavīdhātu sanidassanātiādikathā", f"မြေဓာတ်သည် {SAN} ဖြစ်သည် စသည်ဟူသော {KATHA}")
_CI = F.INDRIYA["cakkhundriya"].my
section("(61) 9. Cakkhundriyaṃ sanidassanantiādikathā", f"(61) 9. {_CI}သည် {SAN} ဖြစ်သည် စသည်ဟူသော {KATHA}")
section("Cakkhundriyaṃ sanidassanantiādikathā", f"{_CI}သည် {SAN} ဖြစ်သည် စသည်ဟူသော {KATHA}")
section("(62) 10. Kāyakammaṃ sanidassanantikathā", f"(62) 10. ကိုယ်ဖြင့် ပြုသော ကံသည် {SAN} ဖြစ်သည်ဟူသော {KATHA}")
section("Kāyakammaṃ sanidassanantikathā", f"ကိုယ်ဖြင့် ပြုသော ကံသည် {SAN} ဖြစ်သည်ဟူသော {KATHA}")
LINES_X[key("Niyamo asaṅkhato, paṭiccasamuppādo asaṅkhato, cattāri saccāni asaṅkhatāni, cattāro āruppā asaṅkhatā, "
            "nirodhasamāpatti asaṅkhatā, ākāso asaṅkhato, ākāso sanidassano, cattāro mahābhūtā, pañcindriyāni, "
            "tatheva kāyakammanti.")] = (
    f"{NIYAMA}သည် {ASKT}၊ {PS_N}သည် {ASKT}၊ သစ္စာ {F.NUM_MY[4]}{F.CL}သည် {ASKT}၊ {ARUPPA}သည် {ASKT}၊ "
    f"{NSM}သည် {ASKT}၊ {AKS}သည် {ASKT}၊ {AKS}သည် {SAN}၊ မဟာဘုတ် {F.NUM_MY[4]}{F.CL}၊ "
    f"{F.INDRIYA_W} {F.NUM_MY[5]}{F.CL}၊ {F.TATHEVA} ကိုယ်ဖြင့် ပြုသော ကံ{END}")   # harmonise B7: tatheva

# ===================================================================================== 15. Sattamavaggo
section("Sattamavaggo", f"{F.ORD_MY[7]} {F.VAGGA_W}")
COLO_X["Sattamavaggo"] = HEAD_X["Sattamavaggo"]


class WH(Cl):
    """A clause whose question is a «which» question: q form «…သနည်း» (katama… gacchati?)."""

    def f(self, form, depth=0):
        if form == "q":
            return F.q_set(f"{self.pre} {self.v}သနည်း", depth)
        return super().f(form, depth)


NOM = {  # nominative nouns of the series (Pāli -> Burmese)
    "phasso": "တွေ့ထိမှု", "vedanā": F.VEDANA.my, "saññā": F.SANNA.my, "cetanā": "စေ့ဆော်မှု", "cittaṃ": "စိတ်",
    "saddhā": "ယုံကြည်မှု", "vīriyaṃ": "ဝီရိယ", "sati": "သတိ", "samādhi": "သမာဓိ", "paññā": "ပညာ",
    "rāgo": "ရာဂ", "doso": "ဒေါသ", "moho": "မောဟ", "māno": KIL["māno"], "diṭṭhi": KIL["diṭṭhi"],
    "vicikicchā": KIL["vicikicchā"], "thinaṃ": KIL["thinaṃ"], "uddhaccaṃ": KIL["uddhaccaṃ"],
    "ahirikaṃ": KIL["ahirikaṃ"], "anottappaṃ": KIL["anottappaṃ"]}
INSTR = {"phassena": "တွေ့ထိမှု", "vedanāya": F.VEDANA.my, "saññāya": F.SANNA.my, "cetanāya": "စေ့ဆော်မှု",
         "saddhāya": "ယုံကြည်မှု", "vīriyena": "ဝီရိယ", "satiyā": "သတိ", "samādhinā": "သမာဓိ", "paññāya": "ပညာ",
         "rāgena": "ရာဂ", "dosena": "ဒေါသ", "mohena": "မောဟ", "anottappena": KIL["anottappaṃ"], "cittena": "စိတ်"}
for _k, _m in NOM.items():
    if not has(_k):
        P(_k, FR(_m))
for _k, _m in INSTR.items():
    if not has(_k):
        P(_k, FR(f"{_m}နှင့်"))
KH = {k: F._KH[k] for k in F._KH}                                    # rūpakkhandho … -> «ရုပ် အစုအဝေး» …
KHI = {k[:-1] + "ena": v for k, v in KH.items()}                     # … -khandhena
KHI["vedanākhandhena"] = KH["vedanākkhandho"]                         # ^5-473 «vedanākhandhena» (as written)
for _k, _m in list(KH.items()) + [(k, v) for k, v in KHI.items()]:
    if not has(_k):
        P(_k, FR(_m if _k.endswith("o") else f"{_m}နှင့်"))
# ------------------------------------------------------------------------------------- 63. Saṅgahitakathā
SNG = W("3", "^3-7", "saṅgahito", "အကျုံးဝင်")                      # saṅgahita (pi-3 «… တွင် အကျုံးဝင်»)
section("(63) 1. Saṅgahitakathā", f"(63) 1. {SNG}ခြင်းအကြောင်း {KATHA}")
section("Saṅgahitakathā", f"{SNG}ခြင်းအကြောင်း {KATHA}")
SOMED = f"{SOME_P} သဘောတရားတို့"
for _n, _neg in (("natthi", True), ("atthi", False)):
    P(f"{_n} keci dhammā kehici dhammehi saṅgahitā", V(f"{SOMED}တွင် {SNG}သော {SOMED}", EXIST, neg=_neg))
    P(f"{_n} keci dhammā kehici dhammehi sampayuttā", V(f"{SOMED}နှင့် ယှဉ်တွဲသော {SOMED}", EXIST, neg=_neg))
P("atthi keci dhammā kehici dhammehi gaṇanaṃ gacchanti uddesaṃ gacchanti pariyāpannā",
  V(f"{SOMED}နှင့်အတူ ရေတွက်ခြင်းသို့ ရောက်ကြ၊ ညွှန်ပြခြင်းသို့ ရောက်ကြ၊ အကျုံးဝင်ကြသော {SOMED}", EXIST))
SUBJ63 = {f"{F.AYATANA[a].pali['nom']}": F.AYATANA[a].my for a in F.AYATANA}
SUBJ63.update({"sukhā vedanā": "သာယာသော ခံစားမှု", "dukkhā vedanā": "နာကျင်သော ခံစားမှု",
               "adukkhamasukhā vedanā": "မနာကျင် မသာယာသော ခံစားမှု"})
_SENSES = [("cakkhu", "မျက်စိ"), ("sota", "နား"), ("ghāna", "နှာခေါင်း"), ("jivhā", "လျှာ"), ("kāya", "ကိုယ်"),
           ("mano", "မနော")]
for _s, _sm in _SENSES:
    SUBJ63[f"{_s}samphassajā saññā"] = f"{_sm}၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော {F.SANNA.my}"
    SUBJ63[f"{_s}samphassajā cetanā"] = f"{_sm}၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော စေ့ဆော်မှု"
    SUBJ63[f"{_s if _s != 'jivhā' else 'jivhā'}viññāṇaṃ"] = f"{_sm} {F.VINNANA.my}"
W("2", "^2-1", "cakkhusamphassajā saññā", f"မျက်စိ၏ တွေ့ထိမှုမှ ဖြစ်ပေါ်သော {F.SANNA.my}") if False else None
for _s, _sm in SUBJ63.items():
    if not has(_s):
        P(_s, FR(_sm))
    for _k, _km in KH.items():
        _g = _k[:-1] + "agaṇanaṃ"
        P(f"{_s} {_g} gacchati", Cl(f"{_sm}သည် {_km}၏ ရေတွက်ခြင်းသို့", "ရောက်", "မရောက်"))
        for _e in ("aṃ", "ā", "o"):
            P(f"{_s} {_k[:-1]}ena saṅgahit{_e}", V(f"{_sm}သည် {_km}တွင် {SNG}", "ဖြစ်") if False else
              Cl(f"{_sm}သည် {_km}တွင်", SNG, "မ" + SNG))
    P(f"{_s} katamakkhandhagaṇanaṃ gacchati", WH(f"{_sm}သည် အဘယ် အစုအဝေး၏ ရေတွက်ခြင်းသို့", "ရောက်", "မရောက်"))
for _k, _km in KH.items():
    P(f"{_k[:-1]}agaṇanaṃ gacchati", Cl(f"{_km}၏ ရေတွက်ခြင်းသို့", "ရောက်", "မရောက်"))
VAR_X.update({"saṅgahītāti": F.LEKHANA, "katamaṃ khandhagaṇanaṃ": F.LEKHANA})
ANCHOR_X["katamakkhandhagaṇanaṃ"] = "အဘယ် အစုအဝေး၏"
_YO = ("ကြိုးဖြင့်ဖြစ်စေ၊ ထမ်းပိုးဖြင့်ဖြစ်စေ နွား နှစ်ကောင်တို့ကို စုစည်းထားသကဲ့သို့၊ ချိုင့်ကြိုး၌ ဆွမ်းကို "
       "စုစည်းထားသကဲ့သို့၊ ထိုချိုင့်ကြိုးကို ချိတ်ဖြင့် စုစည်းထားသကဲ့သို့")
S("Yathā dāmena vā yottena vā dve balibaddā saṅgahitā, sikkāya piṇḍapāto saṅgahito, sā gaddulena saṅgahito; evameva "
  "te dhammā tehi dhammehi saṅgahitāti?", f"{_YO} {P11.EVAM} ထိုသဘောတရားတို့သည် ထိုသဘောတရားတို့တွင် {SNG}ကြသလော{END}")
P("dāmena vā yottena vā dve balībaddā saṅgahitā, sikkāya piṇḍapāto saṅgahito, sā gaddulena saṅgahito",
  Cl("ကြိုးဖြင့်ဖြစ်စေ၊ ထမ်းပိုးဖြင့်ဖြစ်စေ နွား နှစ်ကောင်တို့ကို စုစည်းထား၍ ချိုင့်ကြိုး၌ ဆွမ်းကို စုစည်းထားကာ "
     "ထိုချိုင့်ကြိုးကို ချိတ်ဖြင့်", "စုစည်းထား", "မစုစည်းထား"))
new("saṅgahita (the simile, tied together)", "စုစည်းထား")
F.NOTE_BR = getattr(F, "NOTE_BR", None)
BR_X["[sakavādivacanaṃ (aṭṭhakathā passitabbā)]"] = f"[{F.SAKAVADI}၏ စကား (အဋ္ဌကထာကို ကြည့်ပါ)]"

# ------------------------------------------------------------------------------------- 64. Sampayuttakathā
section("(64) 2. Sampayuttakathā", f"(64) 2. ယှဉ်တွဲခြင်းအကြောင်း {KATHA}")
section("Sampayuttakathā", f"ယှဉ်တွဲခြင်းအကြောင်း {KATHA}")
_SH = ["နှင့်အတူ ဖြစ်ကြ", "နှင့်အတူ ပေါ်ပေါက်ကြ", "နှင့် ရောနှောကြ", "နှင့် ယှဉ်တွဲကြ", "နှင့် တစ်ပြိုင်နက် ဖြစ်ပေါ်ကြ",
       "နှင့် တစ်ပြိုင်နက် ချုပ်ငြိမ်းကြ", "နှင့် မှီရာ တူကြ", "နှင့် အာရုံ တူကြ"]
_SH_PI = ["sahagatā", "sahajātā", "saṃsaṭṭhā", "sampayuttā", "ekuppādā", "ekanirodhā", "ekavatthukā", "ekārammaṇā"]
new("sahagatā … ekārammaṇā (with X)", "၊ ".join("X" + x for x in _SH))


def sh_list(x_my, with_samp, verb=False):
    """«Xနှင့်အတူ ဖြစ်သော၊ ထိုတို့နှင့်အတူ ပေါ်ပေါက်သော၊ ထိုတို့နှင့် ရောနှောသော …» (each item keeps «နှင့်»)."""
    items = [m[:-len("ကြ")] for p, m in zip(_SH_PI, _SH) if with_samp or p != "sampayuttā"]
    return f"{x_my}{items[0]}သော၊ " + "၊ ".join(f"ထိုတို့{i}သော" for i in items[1:])


P("atthi keci dhammā kehici dhammehi " + " ".join(p for p in _SH_PI if p != "sampayuttā"),
  V(f"{sh_list(SOMED, False)} {SOMED}", EXIST))
P("atthi keci dhammā cittena " + " ".join(_SH_PI), V(f"{sh_list('စိတ်', True)} {SOMED}", EXIST))
for _a, _am in KH.items():
    for _b, _bm in KHI.items():
        if _b == "vedanākhandhena":
            continue
        P(f"{_a} {_b} sahajāto", V(f"{_am}သည် {_bm}နှင့်အတူ ပေါ်ပေါက်သော အရာ"))
        P(f"{_a} {_b} sampayutto", V(f"{_am}သည် {_bm}နှင့် ယှဉ်တွဲသော အရာ"))
        P(f"{_a} {_b}", FR(f"{_am}သည် {_bm}နှင့်"))
    P(f"{_a[:-1]}ena sahajāto" if False else f"{_a.replace('kkhandho', 'kkhandhena')} sahajāto",
      FR(f"{KHI[_a.replace('kkhandho', 'kkhandhena')]}နှင့်အတူ ပေါ်ပေါက်သော အရာ ဖြစ်")) if False else None
for _b, _bm in KHI.items():
    P(f"{_b} sahajāto", V(f"{_bm}နှင့်အတူ ပေါ်ပေါက်သော အရာ"))
P("viññāṇakkhandho vedanākhandhena", FR(f"{KH['viññāṇakkhandho']}သည် {KH['vedanākkhandho']}နှင့်"))
S("Yathā tilamhi telaṃ anugataṃ anupaviṭṭhaṃ, ucchumhi raso anugato anupaviṭṭho; evameva te dhammā tehi dhammehi "
  "anugatā anupaviṭṭhāti?",
  "နှမ်းစေ့၌ ဆီသည် ပျံ့နှံ့လျက် အတွင်းသို့ ဝင်ရောက်နေသကဲ့သို့၊ ကြံ၌ အရည်သည် ပျံ့နှံ့လျက် အတွင်းသို့ "
  f"ဝင်ရောက်နေသကဲ့သို့ {P11.EVAM} ထိုသဘောတရားတို့သည် ထိုသဘောတရားတို့၌ ပျံ့နှံ့လျက် အတွင်းသို့ ဝင်ရောက်နေကြသလော{END}")

# ------------------------------------------------------------------------------------- 65. Cetasikakathā
CET = W("1", "^1-M2-57", "cetasikā dhammā", "စိတ်၏ အဖော် ဖြစ်သော")
section("(65) 3. Cetasikakathā", f"(65) 3. {CET} သဘောတရားအကြောင်း {KATHA}")
section("Cetasikakathā", f"{CET} သဘောတရားအကြောင်း {KATHA}")
for _n, _neg in (("natthi", True), ("atthi", False)):
    P(f"{_n} cetasiko dhammo", V(f"{CET} သဘောတရား", EXIST, neg=_neg))
for _k, _m in NOM.items():
    for _e in ("o", "aṃ", "ā"):
        pass
    _stem = {"phasso": "phass", "anottappaṃ": "anottapp"}.get(_k)
    if _stem:
        _e = "o" if _k.endswith("o") else "aṃ"
        P(f"{_k} cittena sahajāt{_e}", V(f"{_m}သည် စိတ်နှင့်အတူ ပေါ်ပေါက်သော အရာ"))
        P(f"{_k} cetasik{_e}", V(f"{_m}သည် {CET} အရာ"))
P("cittena sahajātā", V("စိတ်နှင့်အတူ ပေါ်ပေါက်သော အရာတို့"))
P("cetasikā", V(f"{CET} အရာတို့"))
for _k, _m in INSTR.items():
    P(f"{_k} sahajātā", V(f"{_m}နှင့်အတူ ပေါ်ပေါက်သော အရာတို့"))
P("phassasikā", V("တွေ့ထိမှု၏ အဖော် ဖြစ်သော အရာတို့"))
P("anottappāsikā", V(f"{KIL['anottappaṃ']}၏ အဖော် ဖြစ်သော အရာတို့"))
VAR_X.update({"anottappikāti": F.PATHA, "āvajjanā": F.PATHA})
BR_X["[phassikāti (pī. aṭṭha.)]"] = "[ပါဌ်ကွဲ (Pī., အဋ္ဌကထာ): phassikāti]"


@F.frame(r"(?P<x>[^–]+?)ti katvā (?P<p>[^?–]+?)ti\?")
def _f_katva_p(m):
    """X-ti katvā P-ti? (^5-476, ^5-509): «Xဟု အကြောင်းပြု၍ Pသလော»."""
    return f"{F.pq(m['x'], 'stmt')}{F.KATVA} {F.pq(m['p'], 'q')}{END}"


before_generic()
_CV = [('"Cittañhidaṃ cetasikā ca dhammā,', f"“ဤစိတ်နှင့် {CET} သဘောတရားတို့သည်၊"),
       ("Anattato saṃviditassa honti;", "အတ္တ မဟုတ်ဟု ကောင်းစွာ သိသူအား ထင်ရှား ဖြစ်ကုန်၏၊"),
       ("Hīnappaṇītaṃ tadubhaye viditvā,", "ယုတ်ညံ့ခြင်း မြင့်မြတ်ခြင်း ထိုနှစ်မျိုးလုံးကို သိ၍၊"),
       ('Sammaddaso vedi palokadhamma"nti.', "မှန်ကန်စွာ မြင်သူသည် ပျက်စီးတတ်သော သဘောကို သိ၏”။")]
for _p, _m in _CV:
    LINES_X[key(_p)] = _m
Q("idha, kevaṭṭa, bhikkhu parasattānaṃ parapuggalānaṃ cittampi ādisati cetasikampi ādisati vitakkitampi ādisati "
  "vicāritampi ādisati – ‘evampi te mano, itthampi te mano, itipi te cittaṃ’",
  "ကေဝဋ္ဋ၊ ဤသာသနာ၌ ရဟန်းသည် အခြား သတ္တဝါ၊ အခြား ပုဂ္ဂိုလ်တို့၏ စိတ်ကိုလည်း ဖော်ပြ၏၊ စိတ်၏ အဖော်ကိုလည်း ဖော်ပြ၏၊ "
  "ကြံစည်ထားသည်ကိုလည်း ဖော်ပြ၏၊ သုံးသပ်ထားသည်ကိုလည်း ဖော်ပြ၏ – ‹သင်၏ မနောသည် ဤသို့လည်း ဖြစ်၏၊ သင်၏ "
  "မနောသည် ဤနည်းလည်း ဖြစ်၏၊ သင်၏ စိတ်သည် ဤသို့ပင် ဖြစ်၏›")
P("atthi cetasiko dhammo", V(f"{CET} သဘောတရား", EXIST)) if not has("atthi cetasiko dhammo") else None

# ------------------------------------------------------------------------------------- 66. Dānakathā
DANA = F.PROP["dānaṃ"].pre[:-len("သည်")]                               # dānaṃ (ch6-10 «ပေးလှူခြင်း»)
GIFT = GIVE["dānaṃ"]                                                  # dānaṃ as the thing given (deti / dadāti)
section("(66) 4. Dānakathā", f"(66) 4. {DANA}အကြောင်း {KATHA}")
section("Dānakathā", f"{DANA}အကြောင်း {KATHA}")
P("cetasiko dhammo dānaṃ", V(f"{CET} သဘောတရားသည် {DANA}"))
DEYYA = new("deyyadhammo", "ပေးလှူဖွယ် ဝတ္ထု")
P("deyyadhammo dānaṃ", V(f"{DEYYA}သည် {DANA}"))
_GIVE_OBJ = {"cetasiko dhammo": f"{CET} သဘောတရား"}
_GIVE_OBJ.update({k: v for k, v in NOM.items() if k in ("phasso", "vedanā", "saññā", "cetanā", "saddhā", "vīriyaṃ",
                                                       "sati", "samādhi", "paññā")})
for _k, _m in _GIVE_OBJ.items():
    P(f"labbhā {_k} paresaṃ dātuṃ", Cl(f"{_m}ကို သူတစ်ပါးတို့အား ပေးရန်", "ဖြစ်နိုင်", "မဖြစ်နိုင်"))
    P(f"{_k} paresaṃ dātuṃ", Cl(f"{_m}ကို သူတစ်ပါးတို့အား ပေးရန်", "ဖြစ်နိုင်", "မဖြစ်နိုင်"))
P("labbhā vedanā", FR(F.VEDANA.my))
_G = F.PROP["kusalaṃ viññāṇaṃ saphalaṃ savipākaṃ iṭṭhaphalaṃ kantaphalaṃ manuññaphalaṃ asecanakaphalaṃ sukhudrayaṃ "
            "sukhavipākaṃ"].pre.split("ရှိသော၊ ", 2)[2][:-len(" အရာ")]
_B = F.PROP["akusalaṃ viññāṇaṃ saphalaṃ savipākaṃ aniṭṭhaphalaṃ akantaphalaṃ amanuññaphalaṃ secanakaphalaṃ dukkhudrayaṃ "
            "dukkhavipākaṃ"].pre.split("ရှိသော၊ ", 2)[2][:-len(" အရာ")]
assert _G.startswith("လိုလားဖွယ်") and _B.startswith("မလိုလားဖွယ်"), (_G, _B)
_GP = "iṭṭhaphal{e} kantaphal{e} manuññaphal{e} asecanakaphal{e} sukhudray{e} sukhavipāk{e}"
_BP = "aniṭṭhaphal{e} akantaphal{e} amanuññaphal{e} secanakaphal{e} dukkhudray{e} dukkhavipāk{e}"
_GOODS = {"cīvaraṃ": GIVE["cīvaraṃ"], "deyyadhammo": DEYYA,
          "gilānapaccayabhesajjaparikkhāro": GIVE["gilānapaccayabhesajjaparikkhāraṃ"]}
for _s, _sm in _GOODS.items():
    _e = "o" if _s.endswith("o") else "aṃ"
    P(f"{_s} {_GP.format(e=_e)}", V(f"{_sm}သည် {_G} အရာ"))
    P(f"{_s} {_BP.format(e=_e)}", V(f"{_sm}သည် {_B} အရာ"))
_DIP = f"{DANA}ကို လိုလားဖွယ် အသီးအပွင့် ရှိသော အရာဟု {BUDDHA} ဟောတော်မူ၏"
new("dānaṃ iṭṭhaphalaṃ vuttaṃ bhagavatā", _DIP)
P("dānaṃ iṭṭhaphalaṃ vuttaṃ bhagavatā, cīvaraṃ dānaṃ", V(f"{_DIP}၊ {GIVE['cīvaraṃ']}သည် {DANA}"))
P("dānaṃ iṭṭhaphalaṃ vuttaṃ bhagavatā, piṇḍapāto senāsanaṃ gilānapaccayabhesajjaparikkhāro dānaṃ",
  V(f"{_DIP}၊ {GIVE['piṇḍapātaṃ']}၊ {GIVE['senāsanaṃ']}၊ {GIVE['gilānapaccayabhesajjaparikkhāraṃ']}သည် {DANA}"))
P("dānaṃ iṭṭhaphalaṃ vuttaṃ bhagavatā, piṇḍapāto dānaṃ", FR(f"{_DIP}၊ {GIVE['piṇḍapātaṃ']}သည် {DANA}"))
P("senāsanaṃ dānaṃ", FR(f"{GIVE['senāsanaṃ']}သည် {DANA}"))
P("gilānapaccayabhesajjaparikkhāro dānaṃ", V(f"{GIVE['gilānapaccayabhesajjaparikkhāraṃ']}သည် {DANA}"))
BR_X["[upari vuccamānāya paravādīpucchāya sadisā, aṭṭhakathā oloketabbā]"] = (
    f"[အောက်၌ ဆိုမည့် {F.PARAVADI}၏ အမေးနှင့် တူသည်၊ အဋ္ဌကထာကို ကြည့်ပါ]")
_DV = [('"Saddhā hiriyaṃ kusalañca dānaṃ,', "“ယုံကြည်မှု၊ ရှက်ခြင်း၊ ကုသိုလ် ဖြစ်သော အလှူ –"),
       ("Dhammā ete sappurisānuyātā;", "ဤတရားတို့ကို သူတော်ကောင်းတို့ လိုက်နာ ကျင့်သုံးကုန်၏၊"),
       ("Etañhi maggaṃ diviyaṃ vadanti,", "ဤတရားကို နတ်ပြည်သို့ သွားရာ လမ်းဟု ဆိုကြကုန်၏၊"),
       ('Etena hi gacchati devaloka"nti [a. ni. 8.32].', "ဤတရားဖြင့် နတ်ပြည်သို့ ရောက်၏” ⟦0⟧။")]
_DV[0] = (_DV[0][0], "“ယုံကြည်မှု၊ ရှက်ခြင်း၊ ကုသိုလ် ဖြစ်သော အလှူ၊")
for _p, _m in _DV:
    LINES_X[key(_p)] = _m
_PS = "ပါဏာတိပါတ"
_MD = ("ကြီးမြတ်သော အလှူ၊ အမြတ်ဆုံးဟု သိအပ်သော၊ ကြာမြင့်စွာ တည်ခဲ့သည်ဟု သိအပ်သော၊ အနွယ်ဟု သိအပ်သော၊ ရှေးကျသော၊ "
       "မရောယှက်သော၊ ရှေးကလည်း မရောယှက်ခဲ့သော")
_NS = "မရောယှက်ကုန်၊ မရောယှက်လတ္တံ့၊ ပညာရှိ ရဟန်း ပုဏ္ဏားတို့ မကဲ့ရဲ့အပ်ကုန်"
_ABH = ("အတိုင်းအဆ မရှိသော သတ္တဝါတို့အား ဘေးမဲ့ခြင်းကို ပေး၏၊ ရန်မဲ့ခြင်းကို ပေး၏၊ ညှဉ်းဆဲမှု ကင်းခြင်းကို ⟦b⟧ "
        "ပေး၏။ အတိုင်းအဆ မရှိသော သတ္တဝါတို့အား ဘေးမဲ့ခြင်းကို ပေး၍ ရန်မဲ့ခြင်းကို ပေး၍ ညှဉ်းဆဲမှု ကင်းခြင်းကို ပေး၍ "
        "အတိုင်းအဆ မရှိသော ဘေးမဲ့ခြင်း၊ ရန်မဲ့ခြင်း၊ ညှဉ်းဆဲမှု ကင်းခြင်း၏ ဝေစု ရှိသူ ဖြစ်၏")
_ABH2 = _ABH.replace(" ⟦b⟧", "")
_SURA = W("2", "^2-703", "Surāmerayamajjapamādaṭṭhānā", "သေရည် သေရက် မူးယစ်ဖွယ်ရာကို သောက်စားခြင်း") \
    if False else "သေရည် သေရက် မူးယစ်ဖွယ်ရာ မေ့လျော့ရာ ဌာနမှ"
S('Nanu vuttaṃ bhagavatā – "pañcimāni, bhikkhave, dānāni mahādānāni aggaññāni rattaññāni vaṃsaññāni porāṇāni '
  'asaṅkiṇṇāni asaṅkiṇṇapubbāni, na saṅkiyanti na saṅkiyissanti, appaṭikuṭṭhāni samaṇehi brāhmaṇehi viññūhi! '
  'Katamāni pañca? Idha, bhikkhave, ariyasāvako pāṇātipātaṃ pahāya pāṇātipātā paṭivirato hoti. Pāṇātipātā '
  'paṭivirato, bhikkhave, ariyasāvako aparimāṇānaṃ sattānaṃ abhayaṃ deti averaṃ deti abyābajjhaṃ deti. '
  'Aparimāṇānaṃ sattānaṃ abhayaṃ datvā averaṃ datvā abyābajjhaṃ datvā aparimāṇassa abhayassa averassa '
  'abyābajjhassa bhāgī hoti. Idaṃ, bhikkhave, paṭhamaṃ dānaṃ mahādānaṃ aggaññaṃ rattaññaṃ vaṃsaññaṃ porāṇaṃ '
  'asaṅkiṇṇaṃ asaṅkiṇṇapubbaṃ, na saṅkiyati na saṅkiyissati, appaṭikuṭṭhaṃ samaṇehi brāhmaṇehi viññūhi. Puna '
  'caparaṃ, bhikkhave, ariyasāvako adinnādānaṃ pahāya…pe… kāmesumicchācāraṃ pahāya…pe… musāvādaṃ pahāya…pe… '
  'surāmerayamajjapamādaṭṭhānaṃ pahāya surāmerayamajjapamādaṭṭhānā paṭivirato hoti. Surāmerayamajjapamādaṭṭhānā '
  'paṭivirato, bhikkhave, ariyasāvako aparimāṇānaṃ sattānaṃ abhayaṃ deti averaṃ deti abyābajjhaṃ deti. '
  'Aparimāṇānaṃ sattānaṃ abhayaṃ datvā averaṃ datvā abyābajjhaṃ datvā aparimāṇassa abhayassa averassa '
  'abyābajjhassa bhāgī hoti. Idaṃ, bhikkhave, pañcamaṃ dānaṃ mahādānaṃ aggaññaṃ rattaññaṃ vaṃsaññaṃ porāṇaṃ '
  'asaṅkiṇṇaṃ asaṅkiṇṇapubbaṃ, na saṅkiyati na saṅkiyissati, appaṭikuṭṭhaṃ samaṇehi brāhmaṇehi viññūhi. Imāni '
  'kho, bhikkhave, pañca dānāni mahādānāni aggaññāni rattaññāni vaṃsaññāni porāṇāni asaṅkiṇṇāni asaṅkiṇṇapubbāni, '
  'na saṅkiyanti na saṅkiyissanti, appaṭikuṭṭhāni samaṇehi brāhmaṇehi viññūhī"ti.',
  f"{F.VUTTA_PRE}သည် မဟုတ်လော – “{_R} ဤအလှူ ငါးပါးတို့သည် {_MD} အလှူတို့ ဖြစ်ကုန်၏၊ {_NS}။ အဘယ် ငါးပါးနည်း။ "
  f"{_R} ဤသာသနာ၌ အရိယာ တပည့်သည် သူ့အသက်ကို သတ်ခြင်းကို ပယ်၍ သူ့အသက်ကို သတ်ခြင်းမှ ရှောင်ကြဉ်သူ ဖြစ်၏။ "
  f"{_R} သူ့အသက်ကို သတ်ခြင်းမှ ရှောင်ကြဉ်သော အရိယာ တပည့်သည် {_ABH}။ {_R} ဤသည်ကား ပထမ အလှူ ဖြစ်၏၊ {_MD} "
  f"အလှူ ဖြစ်၏၊ မရောယှက်၊ မရောယှက်လတ္တံ့၊ ပညာရှိ ရဟန်း ပုဏ္ဏားတို့ မကဲ့ရဲ့အပ်။ {_R} တစ်ဖန် နောက်ထပ် အရိယာ "
  f"တပည့်သည် မပေးသည်ကို ယူခြင်းကို ပယ်၍… ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်းကို ပယ်၍… မုသား ပြောခြင်းကို ပယ်၍… "
  f"{P11.SURA}ကို ပယ်၍ {P11.SURA}မှ ရှောင်ကြဉ်သူ ဖြစ်၏။ {_R} {P11.SURA}မှ ရှောင်ကြဉ်သော အရိယာ တပည့်သည် {_ABH2}။ "
  f"{_R} ဤသည်ကား ပဉ္စမ အလှူ ဖြစ်၏၊ {_MD} အလှူ ဖြစ်၏၊ မရောယှက်၊ မရောယှက်လတ္တံ့၊ ပညာရှိ ရဟန်း ပုဏ္ဏားတို့ "
  f"မကဲ့ရဲ့အပ်။ {_R} ဤအလှူ ငါးပါးတို့သည် {_MD} အလှူတို့ ဖြစ်ကုန်၏၊ {_NS}” ⟦b⟧{END}")
VAR_X["abyāpajjhaṃ"] = F.PATHA
S('Nanu vuttaṃ bhagavatā – "idhekacco annaṃ deti, pānaṃ deti, vatthaṃ deti, yānaṃ deti, mālaṃ deti, gandhaṃ deti, '
  'vilepanaṃ deti, seyyaṃ deti, āvasathaṃ deti, padīpeyyaṃ detī"ti!',
  f"{F.VUTTA_PRE}သည် မဟုတ်လော – “ဤလောက၌ အချို့သူသည် ထမင်းကို ပေး၏၊ သောက်ဖွယ်ကို ပေး၏၊ အဝတ်ကို ပေး၏၊ "
  "ယာဉ်ကို ပေး၏၊ ပန်းကို ပေး၏၊ နံ့သာကို ပေး၏၊ နံ့သာ လိမ်းဖွယ်ကို ပေး၏၊ အိပ်ရာကို ပေး၏၊ နေရာကို ပေး၏၊ "
  "ဆီမီးကို ပေး၏” ⟦b⟧" + END)
BR_X["[saṃ. ni. 3.362-391 thokaṃ visadisaṃ]"] = f"[{F.REF['saṃ. ni.']} 3.362-391၊ အနည်းငယ် ကွဲပြားသည်]"

# ------------------------------------------------------------------------------------- 67. Paribhogamayapuññakathā
PUNNA = new("puññaṃ", "ကောင်းမှု")
PBM = new("paribhogamayaṃ puññaṃ", f"သုံးဆောင်ခြင်းမှ ဖြစ်သော {PUNNA}")
section("(67) 5. Paribhogamayapuññakathā", f"(67) 5. {PBM}အကြောင်း {KATHA}")
section("Paribhogamayapuññakathā", f"{PBM}အကြောင်း {KATHA}")
GROW = ("တိုးပွား", "မတိုးပွား")
P("paribhogamayaṃ puññaṃ vaḍḍhati", Cl(f"{PBM}သည်", *GROW))
_PB10 = ["phasso", "vedanā", "saññā", "cetanā", "cittaṃ", "saddhā", "vīriyaṃ", "sati", "samādhi", "paññā"]
P("paribhogamayo " + ", ".join(f"{k} vaḍḍhati" for k in _PB10),
  VV("သုံးဆောင်ခြင်းမှ ဖြစ်သော " + "၊ ".join(f"{NOM[k]} တိုးပွားသည်" for k in _PB10[:-1]) + f"၊ {NOM['paññā']}",
     "တိုးပွား"))
_LIKE = F.LIKE_GROW            # harmonise B6: one value (my5_formulas), also used by make_ch17-20
P(", ".join(f"{k} viya vaḍḍhati" for k, _ in _LIKE),
  VV("၊ ".join(f"{m}ကဲ့သို့ တိုးပွားသည်" for _, m in _LIKE[:-1]) + f"၊ {_LIKE[-1][1]}ကဲ့သို့", "တိုးပွား"))
DAYAKA = "အလှူရှင်"
P("dāyako dānaṃ datvā na samannāharati", Cl(f"{DAYAKA}သည် {GIFT}ကို ပေးပြီးနောက် စိတ်ကို", "ဆောင်", "မဆောင်", neg=True))
P("hoti puññaṃ", V(PUNNA, "ဖြစ်"))
_AV = [("āvaṭṭentassa", "စိတ်ကို လှည့်ဆောင်သူ၌", "စိတ်ကို မလှည့်ဆောင်သူ၌"), ("ābhogassa", "စိတ်ညွတ်သူ၌", "စိတ် မညွတ်သူ၌"),
       ("samannāharantassa", "စိတ်ကို ဆောင်သူ၌", "စိတ်ကို မဆောင်သူ၌"),
       ("manasikarontassa", "နှလုံးသွင်းသူ၌", "နှလုံး မသွင်းသူ၌"), ("cetayantassa", "စေ့ဆော်သူ၌", "မစေ့ဆော်သူ၌"),
       ("patthayantassa", "တောင့်တသူ၌", "မတောင့်တသူ၌"), ("paṇidahantassa", "ဆုတောင်းသူ၌", "ဆု မတောင်းသူ၌")]
_NEGPI = {"āvaṭṭentassa": "anāvaṭṭentassa", "ābhogassa": "anābhogassa", "samannāharantassa": "asamannāharantassa",
          "manasikarontassa": "amanasikarontassa", "cetayantassa": "acetayantassa", "patthayantassa": "apatthayantassa",
          "paṇidahantassa": "appaṇidahantassa"}
for _k, _pm, _nm in _AV:
    P(f"{_k} hoti", Cl(f"({PUNNA}သည်) {_pm}" if False else _pm, "ဖြစ်", "မဖြစ်"))
    P(f"{_NEGPI[_k]} hoti", Cl(_nm, "ဖြစ်", "မဖြစ်"))
new("āvaṭṭentassa … paṇidahantassa hoti", "၊ ".join(m for _, m, _ in _AV) + " ဖြစ်")
VAR_X.update({"anāvaṭṭantassa": F.LEKHANA, "anāvajjhantassa": F.PATHA})
ANCHOR_X["Anāvaṭṭentassa"] = "စိတ်ကို မလှည့်ဆောင်သူ၌"
_VT = W("2", "^2-916", "Kāmavitakko, byāpādavitakko, vihiṃsāvitakko",
        "ကာမကို စတင်ကြံစည်မှု၊ ဖျက်ဆီးလိုစိတ်ဆိုင်ရာ စတင်ကြံစည်မှု၊ ညှဉ်းပန်းမှုဆိုင်ရာ စတင်ကြံစည်မှု") \
    if False else "ကာမကို စတင်ကြံစည်မှု၊ ဖျက်ဆီးလိုစိတ်ဆိုင်ရာ စတင်ကြံစည်မှု၊ ညှဉ်းပန်းမှုဆိုင်ရာ စတင်ကြံစည်မှု"
_VT3 = _VT.split("၊ ")
P("dāyako dānaṃ datvā kāmavitakkaṃ vitakketi, byāpādavitakkaṃ vitakketi, vihiṃsāvitakkaṃ vitakketi",
  VV(f"{DAYAKA}သည် {GIFT}ကို ပေးပြီးနောက် {_VT3[0]}ကို ကြံစည်သည်၊ {_VT3[1]}ကို ကြံစည်သည်၊ {_VT3[2]}ကို", "ကြံစည်"))
P("dvinnaṃ phassānaṃ", FR(f"တွေ့ထိမှု {F.NUM_MY[2]}{F.CL}"))
P("dvinnaṃ cittānaṃ samodhānaṃ hoti", V(f"စိတ် {F.NUM_MY[2]}{F.CL}တို့၏ ပေါင်းဆုံခြင်း"))
_KS = f"{F.KSA}သည်"          # harmonise B6: = pi-4 ^4-104 (identical Pāli words); the verb F.SAMMUKHA (this chapter's)
P("kusalākusalā sāvajjānavajjā hīnapaṇītā kaṇhasukkasappaṭibhāgā dhammā sammukhībhāvaṃ āgacchanti",
  Cl(_KS, *F.SAMMUKHA))
new("kusalākusalā sāvajjānavajjā hīnapaṇītā kaṇhasukkasappaṭibhāgā", _KS[:-len(" သဘောတရားတို့သည်")])
_FAR = "အလွန် ဝေးကွာသော အရာ"
Q("cattārimāni, bhikkhave, suvidūravidūrāni! Katamāni cattāri? Nabhañca, bhikkhave, pathavī ca – idaṃ paṭhamaṃ "
  "suvidūravidūraṃ. Orimañca, bhikkhave, tīraṃ samuddassa pārimañca tīraṃ – idaṃ dutiyaṃ suvidūravidūraṃ. Yato "
  "ca, bhikkhave, verocano abbhudeti yattha ca atthameti – idaṃ tatiyaṃ suvidūravidūraṃ. Satañca, bhikkhave, "
  "dhammo asatañca dhammo – idaṃ catutthaṃ suvidūravidūraṃ. Imāni kho, bhikkhave, cattāri suvidūravidūrāni",
  f"{F.FAR4_HEAD}။ "
  f"{_R} သမုဒ္ဒရာ၏ ဤမှာဘက် ကမ်းနှင့် ဟိုမှာဘက် ကမ်း – ဤသည်ကား ဒုတိယ {_FAR} ဖြစ်၏။ {_R} နေ ထွက်ရာ အရပ်နှင့် "
  f"နေ ဝင်ရာ အရပ် – ဤသည်ကား တတိယ {_FAR} ဖြစ်၏။ {_R} သူတော်ကောင်းတို့၏ တရားနှင့် သူတော်ကောင်း မဟုတ်သူတို့၏ "
  f"တရား – ဤသည်ကား စတုတ္ထ {_FAR} ဖြစ်၏။ {_R} ဤသည်တို့ကား {_FAR} လေးပါးတို့ ဖြစ်ကုန်၏")
_FV = [('"Nabhañca dūre pathavī ca dūre,', "“ကောင်းကင်သည်လည်း ဝေး၏၊ မြေသည်လည်း ဝေး၏၊"),
       ("Pāraṃ samuddassa tadāhu dūre;", "သမုဒ္ဒရာ၏ ဟိုမှာဘက် ကမ်းကိုလည်း ဝေး၏ဟု ဆိုကြ၏၊"),
       ("Yato ca verocano abbhudeti,", "အလင်းရောင် ဖြာထွက်သော နေသည် ထွက်ရာ အရပ်နှင့်"),
       ("Pabhaṅkaro yattha ca atthameti.", "အလင်းကို ပြုသော နေသည် ဝင်ရာ အရပ်လည်း ဝေး၏။"),
       ('"Tato have dūrataraṃ vadanti,', "“ထိုအရာတို့ထက် ပို၍ ဝေး၏ဟု ဆိုကြ၏၊"),
       ("Satañca dhammaṃ asatañca dhammaṃ;", "သူတော်ကောင်းတို့၏ တရားနှင့် သူတော်ကောင်း မဟုတ်သူတို့၏ တရားကို၊"),
       ("Abyāyiko hoti sataṃ samāgamo,", "သူတော်ကောင်းတို့၏ ပေါင်းဆုံခြင်းသည် မပျက်စီးတတ်၊"),
       ("Yāvampi tiṭṭheyya tatheva hoti.", "တည်နေသမျှ ကာလပတ်လုံး ထိုအတိုင်းပင် ဖြစ်၏။"),
       ('"Khippañhi veti [khippaṃhaveti (bahūsu)] asataṃ samāgamo;',
        "“သူတော်ကောင်း မဟုတ်သူတို့၏ ပေါင်းဆုံခြင်းသည် လျင်မြန်စွာ ⟦0⟧ ပျက်စီး၏၊"),
       ('Tasmā sataṃ dhammo asabbhi ārakā"ti [a. ni. 4.47].',
        f"{F.FAR4_LAST}” ⟦0⟧။")]
for _p, _m in _FV:
    LINES_X[key(_p)] = _m
VAR_X["khippaṃhaveti"] = F.PATHA
_AR = [('"Ārāmaropā vanaropā, ye janā setukārakā;', "“ဥယျာဉ် စိုက်ပျိုးသူ၊ တော စိုက်ပျိုးသူ၊ တံတား တည်ဆောက်သူ အကြင်လူတို့ ရှိကုန်၏၊"),
       ("Papañca udapānañca, ye dadanti upassayaṃ.", "ရေသောက်ဇရပ်ကိုလည်းကောင်း၊ ရေတွင်းကိုလည်းကောင်း၊ နေရာကိုလည်းကောင်း ပေးလှူကြကုန်၏။"),
       ('"Tesaṃ divā ca ratto ca, sadā puññaṃ pavaḍḍhati;', f"“ထိုသူတို့၏ {PUNNA}သည် နေ့ရော ညပါ အမြဲ တိုးပွား၏၊"),
       ('Dhammaṭṭhā sīlasampannā, te janā saggagāmino"ti [saṃ. ni. 1.47].',
        "တရား၌ တည်၍ သီလနှင့် ပြည့်စုံသော ထိုလူတို့သည် နတ်ပြည်သို့ သွားသူတို့ ဖြစ်ကုန်၏” ⟦0⟧။")]
for _p, _m in _AR:
    LINES_X[key(_p)] = _m
_ABS = ("ကောင်းမှု၏ စီးဆင်းရာ၊ ကုသိုလ်၏ စီးဆင်းရာ၊ ချမ်းသာ၏ အစာ၊ နတ်ပြည်နှင့် ဆိုင်သော၊ ချမ်းသာသော အကျိုး ရှိသော၊ "
        "နတ်ပြည်သို့ ရောက်စေတတ်သော")
_TO = "လိုလားဖွယ်၊ ချစ်ခင်ဖွယ်၊ နှစ်သက်ဖွယ်၊ အကျိုးစီးပွား၊ ချမ်းသာ ဖြစ်ခြင်းငှာ ဖြစ်စေ"
_APP = "အတိုင်းအဆ မရှိသော စိတ်၏ တည်ကြည်ခြင်းကို ပြည့်စုံစေလျက် နေ၏"
Q("cattārome, bhikkhave, puññābhisandā kusalābhisandā sukhassāhārā sovaggikā sukhavipākā saggasaṃvattanikā iṭṭhāya "
  "kantāya manāpāya hitāya sukhāya saṃvattanti! Katame cattāro? Yassa, bhikkhave, bhikkhu cīvaraṃ paribhuñjamāno "
  "appamāṇaṃ cetosamādhiṃ upasampajja viharati, appamāṇo tassa puññābhisando kusalābhisando sukhassāhāro sovaggiko "
  "sukhavipāko saggasaṃvattaniko iṭṭhāya kantāya manāpāya hitāya sukhāya saṃvattati. Yassa, bhikkhave, bhikkhu "
  "piṇḍapātaṃ paribhuñjamāno…pe… senāsanaṃ paribhuñjamāno…pe… gilānapaccayabhesajjaparikkhāraṃ paribhuñjamāno "
  "appamāṇaṃ cetosamādhiṃ upasampajja viharati, appamāṇo tassa puññābhisando kusalābhisando sukhassāhāro sovaggiko "
  "sukhavipāko saggasaṃvattaniko iṭṭhāya kantāya manāpāya hitāya sukhāya saṃvattati. Ime kho, bhikkhave, cattāro "
  "puññābhisandā kusalābhisandā sukhassāhārā sovaggikā sukhavipākā saggasaṃvattanikā iṭṭhāya kantāya manāpāya "
  "hitāya sukhāya saṃvattantī",
  f"{_R} {_ABS} ဤအရာ လေးပါးတို့သည် {_TO}ကုန်၏။ အဘယ် လေးပါးနည်း။ {_R} အကြင် ဒါယကာ၏ {GIVE['cīvaraṃ']}ကို "
  f"သုံးဆောင်နေသော ရဟန်းသည် {_APP}၊ ထိုဒါယကာ၏ {_ABS} အရာသည် အတိုင်းအဆ မရှိ၊ {_TO}၏။ {_R} အကြင် "
  f"ဒါယကာ၏ {GIVE['piṇḍapātaṃ']}ကို သုံးဆောင်နေသော… {GIVE['senāsanaṃ']}ကို သုံးဆောင်နေသော… "
  f"{GIVE['gilānapaccayabhesajjaparikkhāraṃ']}ကို သုံးဆောင်နေသော ရဟန်းသည် {_APP}၊ ထိုဒါယကာ၏ {_ABS} အရာသည် "
  f"အတိုင်းအဆ မရှိ၊ {_TO}၏။ {_R} ဤသည်တို့ကား {_ABS} အရာ လေးပါးတို့ ဖြစ်၍ {_TO}ကုန်၏")
_DD = f"{DAYAKA}သည် {GIFT}ကို ပေး၏၊ "
P("dāyako dānaṃ deti, paṭiggāhako paṭiggahetvā na paribhuñjati chaḍḍeti vissajjeti, hoti puññaṃ",
  V(f"{_DD}အလှူခံသည် ခံယူပြီး မသုံးဆောင်ဘဲ စွန့်ပစ်၏၊ စွန့်လွှတ်၏၊ {PUNNA}", "ဖြစ်"))
P("dāyako dānaṃ deti, paṭiggāhake paṭiggahite rājāno vā haranti, corā vā haranti, aggi vā dahati, udakaṃ vā vahati, "
  "appiyā vā dāyādā haranti, hoti puññaṃ",
  V(f"{_DD}အလှူခံ ခံယူပြီးသောအခါ မင်းတို့ဖြစ်စေ ယူဆောင်သွားကြ၏၊ ခိုးသူတို့ဖြစ်စေ ယူဆောင်သွားကြ၏၊ မီးဖြစ်စေ "
    f"လောင်၏၊ ရေဖြစ်စေ မျှောပါသွား၏၊ မချစ်ခင်သော အမွေခံတို့ဖြစ်စေ ယူဆောင်သွားကြ၏၊ {PUNNA}", "ဖြစ်"))

# ------------------------------------------------------------------------------------- 68. Itodinnakathā
ITO = new("ito dinnena tattha yāpenti", "ဤလောကမှ ပေးလှူသော အရာဖြင့် ထိုလောက၌ အသက်မွေးကြ")
section("(68) 6. Itodinnakathā", f"(68) 6. ဤလောကမှ ပေးလှူသော အရာအကြောင်း {KATHA}")
section("Ito dinnakathā", f"ဤလောကမှ ပေးလှူသော အရာအကြောင်း {KATHA}")
P("ito dinnena tattha yāpenti", Cl("ဤလောကမှ ပေးလှူသော အရာဖြင့် ထိုလောက၌", "အသက်မွေးကြ", "အသက် မမွေးကြ"))
P("ito cīvaraṃ denti taṃ cīvaraṃ tattha paribhuñjanti",
  Cl(f"ဤလောကမှ {GIVE['cīvaraṃ']}ကို ပေးကြ၏၊ ထို{GIVE['cīvaraṃ']}ကို ထိုလောက၌", "သုံးဆောင်ကြ", "မသုံးဆောင်ကြ"))
_ITO = [("piṇḍapātaṃ", GIVE["piṇḍapātaṃ"]), ("senāsanaṃ", GIVE["senāsanaṃ"]),
        ("gilānapaccayabhesajjaparikkhāraṃ", GIVE["gilānapaccayabhesajjaparikkhāraṃ"]), ("khādanīyaṃ", "ခဲဖွယ်"),
        ("bhojanīyaṃ", "စားဖွယ်"), ("pānīyaṃ", "သောက်ဖွယ်")]
P(", ".join(f"ito {k} denti" for k, _ in _ITO) + "; taṃ pānīyaṃ tattha paribhuñjanti",
  Cl("၊ ".join(f"ဤလောကမှ {m}ကို ပေးကြ၏" for _, m in _ITO) + "၊ ထိုသောက်ဖွယ်ကို ထိုလောက၌", "သုံးဆောင်ကြ", "မသုံးဆောင်ကြ"))
P("añño aññassa kārako parakataṃ sukhadukkhaṃ añño karoti, añño paṭisaṃvedeti",
  Cl("တစ်ယောက်သည် အခြားတစ်ယောက်၏ ပြုသူ ဖြစ်၏၊ သူတစ်ပါး ပြုသော ချမ်းသာ ဆင်းရဲကို တစ်ယောက်က ပြု၍ အခြားတစ်ယောက်က",
     "ခံစား", "မခံစား"))
_PETA = f"{F.PETA}တို့"
P("petā attano atthāya dānaṃ dentaṃ anumodenti, cittaṃ pasādenti, pītiṃ uppādenti, somanassaṃ paṭilabhanti",
  Cl(f"{_PETA}သည် မိမိတို့အတွက် {GIFT}ကို ပေးနေသူကို အနုမောဒနာ ပြုကြ၏၊ စိတ်ကို ကြည်လင်စေကြ၏၊ ပီတိကို "
     "ဖြစ်ပေါ်စေကြ၏၊ ဝမ်းမြောက်မှုကို", "ရကြ", "မရကြ"))
_TV = [('"Unname udakaṃ vuṭṭhaṃ, yathāninnaṃ pavattati;', "“ကုန်းမြင့်ပေါ်၌ ရွာသော မိုးရေသည် နိမ့်ရာသို့ စီးဆင်းသကဲ့သို့၊"),
       ("Evameva ito dinnaṃ, petānaṃ upakappati.", f"ထို့အတူပင် ဤလောကမှ ပေးလှူသော အရာသည် {_PETA}အား အထောက်အကူ ဖြစ်၏။"),
       ('"Yathā vārivahā pūrā, paripūrenti sāgaraṃ;', "“ရေပြည့်သော မြစ်တို့သည် သမုဒ္ဒရာကို ပြည့်စေသကဲ့သို့၊"),
       ('Na hi tattha kasī atthi, gorakkhettha na vijjati;', f"“ထိုလောက၌ လယ်ထွန်ခြင်း {NEXIST}၊ နွားမွေးခြင်းလည်း {NEXIST}၊"),
       ("Vaṇijjā tādisī natthi, hiraññena kayākayaṃ [kayakkayaṃ (sī. pī.)];",
        f"ထိုသို့သော ကုန်သွယ်ခြင်း၊ ငွေဖြင့် ဝယ်ခြင်း ရောင်းခြင်း ⟦0⟧ {NEXIST}၊"),
       ('Ito dinnena yāpenti, petā kālaṅkatā tahi"nti [khu. pā. 7.6; pe. va. 19].',
        f"ထိုလောက၌ သေလွန်သော {_PETA}သည် ဤလောကမှ ပေးလှူသော အရာဖြင့် အသက်မွေးကြကုန်၏” ⟦0⟧။")]
_TV.insert(3, ("Evameva ito dinnaṃ, petānaṃ upakappati.", _TV[1][1]))
for _p, _m in _TV:
    LINES_X[key(_p)] = _m
VAR_X["kayakkayaṃ"] = F.LEKHANA
REF_X.update({"khu. pā.": "“ခုဒ္ဒကပါဌ”", "pe. va.": "“ပေတဝတ္ထု”"})
_FIVE = ("ဝေယျာဝစ္စ ပြုသူသည် ငါတို့ကို ကျွေးမွေးလိမ့်မည်၊ ငါတို့၏ ကိစ္စကို ပြုလိမ့်မည်၊ မျိုးရိုး အနွယ်သည် ကြာမြင့်စွာ "
         "တည်လိမ့်မည်၊ အမွေကို ခံယူလိမ့်မည်၊ ထို့ပြင် သေလွန်ပြီးသော ပြိတ္တာတို့အား အလှူကို ပေးလှူလိမ့်မည်")
Q("pañcimāni, bhikkhave, ṭhānāni sampassantā mātāpitaro puttaṃ icchanti kule jāyamānaṃ! Katamāni pañca? Bhaṭo vā "
  "no bharissati, kiccaṃ vā no karissati, kulavaṃso ciraṃ ṭhassati, dāyajjaṃ paṭipajjissati, atha vā pana petānaṃ "
  "kālaṅkatānaṃ dakkhiṇaṃ anuppadassati – imāni kho, bhikkhave, pañca ṭhānāni sampassantā mātāpitaro puttaṃ "
  "icchanti kule jāyamānaṃ",
  f"{_R} ဤအကြောင်း ငါးပါးတို့ကို မြင်ကြသော မိဘတို့သည် အမျိုး၌ ဖြစ်ပေါ်လာမည့် သားကို အလိုရှိကြကုန်၏။ "
  f"အဘယ် ငါးပါးနည်း။ {_FIVE} – {_R} ဤအကြောင်း ငါးပါးတို့ကို မြင်ကြသော မိဘတို့သည် အမျိုး၌ ဖြစ်ပေါ်လာမည့် "
  "သားကို အလိုရှိကြကုန်၏")
_SV = [('"Pañca ṭhānāni sampassaṃ, puttaṃ icchanti paṇḍitā;', "“ပညာရှိတို့သည် အကြောင်း ငါးပါးတို့ကို မြင်၍ သားကို အလိုရှိကြကုန်၏၊"),
       ("Bhaṭo vā no bharissati, kiccaṃ vā no karissati.", "ဝေယျာဝစ္စ ပြုသူသည် ငါတို့ကို ကျွေးမွေးလိမ့်မည်၊ ငါတို့၏ ကိစ္စကို ပြုလိမ့်မည်။"),
       ('"Kulavaṃso ciraṃ tiṭṭhe, dāyajjaṃ paṭipajjati;', "“မျိုးရိုး အနွယ်သည် ကြာမြင့်စွာ တည်ရာ၏၊ အမွေကို ခံယူ၏၊"),
       ("Atha vā pana petānaṃ, dakkhiṇaṃ anuppadassati.", f"ထို့ပြင် {_PETA}အား အလှူကို ပေးလှူလိမ့်မည်။"),
       ('"Ṭhānānetāni sampassaṃ, puttaṃ icchanti paṇḍitā;', "“ဤအကြောင်းတို့ကို မြင်၍ ပညာရှိတို့သည် သားကို အလိုရှိကြကုန်၏၊"),
       ("Tasmā santo sappurisā, kataññū katavedino.", "ထို့ကြောင့် ကျေးဇူးကို သိ၍ ကျေးဇူးကို ဆပ်တတ်သော သူတော်ကောင်း၊ ယောကျ်ားကောင်းတို့သည်၊"),
       ('"Bharanti mātāpitaro, pubbe katamanussaraṃ;', "“ရှေးက ပြုခဲ့သည်ကို အောက်မေ့လျက် မိဘတို့ကို ကျွေးမွေးကြကုန်၏၊"),
       ("Karonti tesaṃ kiccāni, yathā taṃ pubbakārinaṃ.", "ရှေးဦးစွာ ကျေးဇူး ပြုခဲ့သူတို့အား ပြုသကဲ့သို့ ထိုမိဘတို့၏ ကိစ္စတို့ကို ပြုကြကုန်၏။"),
       # harmonise B3: ovāda «ဆုံးမ» (was «ဩဝါဒ»)
       ('"Ovādakārī bhaṭaposī, kulavaṃsaṃ ahāpayaṃ;', "“ဆုံးမ စကားကို လိုက်နာ၍ ကျွေးမွေးသူတို့ကို ကျွေးမွေးသော၊ မျိုးရိုး အနွယ်ကို မဆုတ်ယုတ်စေသော၊"),
       ('Saddho sīlena sampanno, putto hoti pasaṃsiyo"ti [a. ni. 5.31].',
        "ယုံကြည်မှု ရှိ၍ သီလနှင့် ပြည့်စုံသော သားသည် ချီးမွမ်းထိုက်သူ ဖြစ်၏” ⟦0⟧။")]
for _p, _m in _SV:
    LINES_X[key(_p)] = _m

# ------------------------------------------------------------------------------------- 69-70. … vipāka
KV = new("kammavipāko", f"{F.KAMMA}၏ {F.VIPAKA}")
VIPK = KV                                                            # vipāko alone (pi-1 «ကံ၏ အကျိုး»)
JM = "အိုခြင်း၊ သေခြင်း"
section("(69) 7. Pathavī kammavipākotikathā", f"(69) 7. မြေသည် {KV} ဖြစ်သည်ဟူသော {KATHA}")
section("Pathavī kammavipākotikathā", f"မြေသည် {KV} ဖြစ်သည်ဟူသော {KATHA}")
section("(70) 8. Jarāmaraṇaṃ vipākotikathā", f"(70) 8. {JM}သည် {KV} ဖြစ်သည်ဟူသော {KATHA}")
section("Jarāmaraṇaṃ vipākotikathā", f"{JM}သည် {KV} ဖြစ်သည်ဟူသော {KATHA}")
for _s, _sm in (("pathavī", "မြေ"), ("phasso", "တွေ့ထိမှု"), ("jarāmaraṇaṃ", JM)):
    P(f"{_s} kammavipāko", V(f"{_sm}သည် {KV}"))
    P(f"{_s} vipāko", V(f"{_sm}သည် {VIPK}"))
ADJ = [  # (Pāli stem, Burmese positive attribute, Burmese negative attribute)
    ("sukhavedaniy", "သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော", "သာယာသော ခံစားမှုကို မဖြစ်စေတတ်သော"),
    ("dukkhavedaniy", "နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော", "နာကျင်သော ခံစားမှုကို မဖြစ်စေတတ်သော"),
    ("adukkhamasukhavedaniy", "မနာကျင် မသာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော",
     "မနာကျင် မသာယာသော ခံစားမှုကို မဖြစ်စေတတ်သော"),
    ("sukhāya vedanāya sampayutt", "သာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော", "သာယာသော ခံစားမှုနှင့် မယှဉ်တွဲသော"),
    ("dukkhāya vedanāya sampayutt", "နာကျင်သော ခံစားမှုနှင့် ယှဉ်တွဲသော", "နာကျင်သော ခံစားမှုနှင့် မယှဉ်တွဲသော"),
    ("adukkhamasukhāya vedanāya sampayutt", "မနာကျင် မသာယာသော ခံစားမှုနှင့် ယှဉ်တွဲသော",
     "မနာကျင် မသာယာသော ခံစားမှုနှင့် မယှဉ်တွဲသော"),
    ("phassena sampayutt", "တွေ့ထိမှုနှင့် ယှဉ်တွဲသော", "တွေ့ထိမှုနှင့် မယှဉ်တွဲသော"),
    ("vedanāya sampayutt", "ခံစားမှုနှင့် ယှဉ်တွဲသော", "ခံစားမှုနှင့် မယှဉ်တွဲသော"),
    ("saññāya sampayutt", "မှတ်သိမှုနှင့် ယှဉ်တွဲသော", "မှတ်သိမှုနှင့် မယှဉ်တွဲသော"),
    ("cetanāya sampayutt", "စေ့ဆော်မှုနှင့် ယှဉ်တွဲသော", "စေ့ဆော်မှုနှင့် မယှဉ်တွဲသော"),
    ("cittena sampayutt", "စိတ်နှင့် ယှဉ်တွဲသော", "စိတ်နှင့် မယှဉ်တွဲသော"),
    ("sārammaṇ", "အာရုံ ရှိသော", None), ("anārammaṇ", "အာရုံ မရှိသော", None),
    ("dukkhāya", "နာကျင်သော ခံစားမှု", None)]
W("1", "^1-M2-55", "sārammaṇā dhammā", "အာရုံ ရှိသော") if False else None
_ADJ_RX = re.compile(r"(?P<na>na )?(?P<a>" + "|".join(re.escape(a) for a, _, _ in sorted(ADJ, key=lambda x: -len(x[0])))
                     + r")(?P<e>ā|o|aṃ|)(?=$|[ ,…])")
_ADJ = {a: (pm, nm) for a, pm, nm in ADJ}
_SUBJ69 = {"pathavī": "မြေ", "phasso": "တွေ့ထိမှု", "jarāmaraṇaṃ": JM}


@F.rule(r"(?:(?P<s>pathavī|phasso|jarāmaraṇaṃ) )?(?P<l>(?:na )?(?:sukhavedaniy|dukkhavedaniy|adukkhamasukhavedaniy|"
        r"sukhāya|dukkhāya|adukkhamasukhāya|sārammaṇ|anārammaṇ).*)")
def _r_adj(m):
    """A chain of the feeling / association adjectives (kathā 69-70): «(S သည်) A၊ B… Z အရာ»."""
    text, pos, out = m["l"], 0, []
    while pos < len(text):
        mm = _ADJ_RX.match(text, pos)
        if not mm:
            return None
        pm, nm = _ADJ[mm["a"]]
        if mm["na"] and nm is None:
            return None
        out.append(nm if mm["na"] else pm)
        pos = mm.end()
        sep = re.match(r"(…\s?|, | )", text[pos:])
        if pos < len(text):
            if not sep:
                return None
            out.append("… " if "…" in sep.group(0) else "၊ ")
            pos += sep.end()
    if out and out[-1] in ("… ", "၊ "):
        return None
    pre = f"{_SUBJ69[m['s']]}သည် " if m["s"] else ""
    last = "".join(out)
    if last.endswith("ခံစားမှု"):
        return None
    return V(f"{pre}{last} အရာ")


_AVL = "၊ ".join(F.AVATTANA)     # harmonise B6: the list is in my5_formulas (one value book-wide)
W("1", "^1-1194", "āvaṭṭanā vā ābhogo vā samannāhāro vā manasikāro", "စိတ်ကို လှည့်ဆောင်ခြင်း") if False else None
new("āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi", _AVL)
for _t in ("tāya", "tassa"):
    for _n, _neg in (("atthi", False), ("natthi", True)):
        P(f"{_n} {_t} āvaṭṭanā ābhogo samannāhāro manasikāro cetanā patthanā paṇidhi",
          V(f"ထိုအရာ၌ {_AVL}", EXIST, neg=_neg))
        P(f"{_n} {_t} āvaṭṭanā… paṇidhi", V(f"ထိုအရာ၌ {_AVL.split('၊ ')[0]}… {_AVL.split('၊ ')[-1]}", EXIST, neg=_neg))
P("pathavī paggahaniggahupagā chedanabhedanupagā",
  V(f"မြေသည် {F.PAGGAHA_UPAGA} အရာ"))                 # harmonise B6: = ch5
P("kammavipāko paggahaniggahupago chedanabhedanupago",
  V(f"{KV}သည် {F.PAGGAHA_UPAGA} အရာ"))
for _s, _sm in (("pathavī", "မြေ"), ("kammavipāko", KV)):
    P(f"labbhā {_s} ketuṃ vikketuṃ āṭhapetuṃ ocinituṃ vicinituṃ",
      Cl(f"{_sm}ကို ဝယ်ရန်၊ ရောင်းရန်၊ ပေါင်နှံရန်၊ စုဆောင်းရန်၊ ရွေးချယ်ရန်", "ဖြစ်နိုင်", "မဖြစ်နိုင်"))
    for _e in ("ā", "o"):
        P(f"{_s} paresaṃ sādhāraṇ{_e}", Cl(f"{_sm}သည် သူတစ်ပါးတို့နှင့်", "ဆက်ဆံ", "မဆက်ဆံ"))
LINES_X[key('"Asādhāraṇamaññesaṃ, acoraharaṇo nidhi;')] = "“သူတစ်ပါးတို့နှင့် မဆက်ဆံသော၊ ခိုးသူတို့ မယူဆောင်နိုင်သော ရတနာသိုက် ဖြစ်၏၊"
LINES_X[key('Kayirātha macco puññāni, sace sucaritaṃ care"ti [khu. pā. 8.9 khuddakapāṭhe, thokaṃ visadisaṃ].')] = (
    f"အကယ်၍ ကောင်းသော အကျင့်ကို ကျင့်လိုလျှင် သတ္တဝါသည် {PUNNA}တို့ကို ပြုရာ၏” ⟦0⟧။")
BR_X["[khu. pā. 8.9 khuddakapāṭhe, thokaṃ visadisaṃ]"] = "[“ခုဒ္ဒကပါဌ” 8.9၊ ခုဒ္ဒကပါဌ၌ အနည်းငယ် ကွဲပြားသည်]"
P("paṭhamaṃ pathavī saṇṭhāti, pacchā sattā uppajjanti",
  Cl(f"ပထမဦးစွာ မြေ တည်၏၊ နောက်မှ {F.SATTA}တို့", "ဖြစ်ပေါ်ကြ", "မဖြစ်ပေါ်ကြ"))
P("paṭhamaṃ vipāko uppajjati, pacchā vipākapaṭilābhāya kammaṃ karonti",
  Cl(f"ပထမဦးစွာ {F.VIPAKA} ဖြစ်ပေါ်၏၊ နောက်မှ {F.VIPAKA} ရရှိရန် {F.KAMMA}ကို", "ပြုကြ", "မပြုကြ"))
P("pathavī sabbasattānaṃ kammavipāko", V(f"မြေသည် {F.SATTA} အားလုံးတို့၏ {KV}"))
P("sabbe sattā pathaviṃ paribhuñjanti", Cl(f"{F.SATTA} အားလုံးတို့သည် မြေကို", "သုံးဆောင်ကြ", "မသုံးဆောင်ကြ"))
P("atthi keci pathaviṃ aparibhuñjitvā parinibbāyanti", V(f"မြေကို မသုံးဆောင်ဘဲ ပရိနိဗ္ဗာန် ပြုကြသူ {SOME_P}", EXIST))
P("atthi keci kammavipākaṃ akhepetvā parinibbāyanti",
  V(f"{KV}ကို မကုန်ခန်းစေဘဲ ပရိနိဗ္ဗာန် ပြုကြသူ {SOME_P}", EXIST))
CVS = P11.CVS
P("pathavī cakkavattisattassa kammavipāko", V(f"မြေသည် {CVS}၏ {KV}"))
P("aññe sattā pathaviṃ paribhuñjanti", Cl(f"အခြား {F.SATTA}တို့သည် မြေကို", "သုံးဆောင်ကြ", "မသုံးဆောင်ကြ"))
P("cakkavattisattassa kammavipākaṃ aññe sattā paribhuñjanti",
  Cl(f"{CVS}၏ {KV}ကို အခြား {F.SATTA}တို့", "သုံးဆောင်ကြ", "မသုံးဆောင်ကြ"))
P("cakkavattisattassa phassaṃ vedanaṃ saññaṃ cetanaṃ cittaṃ saddhaṃ vīriyaṃ satiṃ samādhiṃ paññaṃ aññe sattā "
  "paribhuñjanti", Cl(f"{CVS}၏ " + "၊ ".join(NOM[k] for k in _PB10) + f"ကို အခြား {F.SATTA}တို့",
                      "သုံးဆောင်ကြ", "မသုံးဆောင်ကြ"))
P("atthi issariyasaṃvattaniyaṃ kammaṃ adhipaccasaṃvattaniyaṃ kammaṃ",
  V(f"အစိုးရခြင်းကို ဖြစ်စေတတ်သော {F.KAMMA}၊ အုပ်ချုပ်ခြင်းကို ဖြစ်စေတတ်သော {F.KAMMA}", EXIST))
P("atthi dubbaṇṇasaṃvattaniyaṃ kammaṃ appāyukasaṃvattaniyaṃ kammaṃ",
  V(f"အဆင်း ဆိုးခြင်းကို ဖြစ်စေတတ်သော {F.KAMMA}၊ အသက် တိုခြင်းကို ဖြစ်စေတတ်သော {F.KAMMA}", EXIST))
DH = {"akusalānaṃ dhammānaṃ": "အကုသိုလ် သဘောတရားတို့၏", "kusalānaṃ dhammānaṃ": "ကုသိုလ် သဘောတရားတို့၏",
      "kusalānañca akusalānañca dhammānaṃ": "ကုသိုလ် သဘောတရားတို့၏လည်းကောင်း၊ အကုသိုလ် သဘောတရားတို့၏လည်းကောင်း"}
for _a, _am in DH.items():
    for _b in ("akusalānaṃ dhammānaṃ", "kusalānaṃ dhammānaṃ"):
        _bm = DH[_b]
        P(f"{_a} jarāmaraṇaṃ, {_b} vipāko", V(f"{_am} {JM}သည် {_bm} {F.VIPAKA}"))
        P(f"{_a} jarāmaraṇaṃ, na vattabbaṃ – {_b} vipāko",
          SAYQ(f"{_am} {JM}ကို", f"«{_bm} {F.VIPAKA} ဖြစ်သည်»ဟု", neg=True))

# ------------------------------------------------------------------------------------- 71. Ariyadhammavipākakathā
ADV = new("ariyadhammavipāko", f"အရိယာ တရား၏ {F.VIPAKA}")
section("(71) 9. Ariyadhammavipākakathā", f"(71) 9. {ADV}အကြောင်း {KATHA}")
section("Ariyadhammavipākakathā", f"{ADV}အကြောင်း {KATHA}")
for _n, _neg in (("natthi", True), ("atthi", False)):
    P(f"{_n} ariyadhammavipāko", V(ADV, EXIST, neg=_neg))
P("mahapphalaṃ sāmaññaṃ mahapphalaṃ brahmaññaṃ",
  V("ရဟန်း၏ အဖြစ်သည် အကျိုး ကြီးမား၏၊ မြင့်မြတ်သူ၏ အဖြစ်သည် အကျိုး ကြီးမားသော အရာ"))
_PHL = {"sotāpattiphalaṃ": PFX["sotāpatti"], "sakadāgāmiphalaṃ": PFX["sakadāgāmi"], "anāgāmiphalaṃ": PFX["anāgāmi"],
        "arahattaphalaṃ": PFX["arahatta"], "dānaphalaṃ": f"{DANA}၏ {F.VIPAKA}", "sīlaphalaṃ": f"သီလ၏ {F.VIPAKA}",
        "bhāvanāphalaṃ": f"ပွားများခြင်း၏ {F.VIPAKA}"}
for _k, _m in _PHL.items():
    if not has(f"atthi {_k}"):
        P(f"atthi {_k}", V(_m, EXIST))
    P(f"{_k} na vipāko", V(f"{_m}သည် {VIPK}", neg=True))
    P(f"{_k} vipāko", V(f"{_m}သည် {VIPK}"))
    if not has(_k):
        P(_k, FR(_m))
P("atthi sakadāgāmiphalaṃ… anāgāmiphalaṃ… arahattaphalaṃ",
  V(f"{PFX['sakadāgāmi']}… {PFX['anāgāmi']}… {PFX['arahatta']}", EXIST))
AVC = {"kāmāvacaraṃ": "ကာမဘုံနှင့် ဆိုင်သော", "rūpāvacaraṃ": "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ဆိုင်သော",
       "arūpāvacaraṃ": "ရုပ်မရှိသော ဘုံနှင့် ဆိုင်သော", "lokuttaraṃ": LOKUTTARA}
for _k, _m in AVC.items():
    _km = f"{_m} ကုသိုလ်"
    P(f"{_k} kusalaṃ savipākaṃ", V(f"{_km}သည် {F.VIPAKA} ရှိသော အရာ"))
    P(f"{_k} kusalaṃ avipākaṃ", V(f"{_km}သည် {F.VIPAKA} မရှိသော အရာ"))
    P(f"{_k} kusalaṃ savipākaṃ ācayagāmi", V(f"{_km}သည် {F.VIPAKA} ရှိ၍ စုပုံခြင်းဆီသို့ ဦးတည်သော အရာ"))
    P(f"{_k} kusalaṃ savipākaṃ apacayagāmi", V(f"{_km}သည် {F.VIPAKA} ရှိ၍ လျော့ပါးခြင်းဆီသို့ ဦးတည်သော အရာ"))
    if not has(_k):
        P(_k, FR(_m))
    P(f"{_k} kusalaṃ", FR(_km))
W("1", "^1-M2-?" if False else "^1-M1-19", "ācayagāmino dhammā", "စုပုံခြင်းဆီသို့ ဦးတည်သော") if False else None

# ------------------------------------------------------------------------------------- 72. Vipāko vipākadhammadhammo
VDD = W("1", "^1-M1-3", "vipākadhammadhammā", "အကျိုး ပေးတတ်သော") + " သဘောတရား"
section("(72) 10. Vipāko vipākadhammadhammotikathā", f"(72) 10. {VIPK}သည် {VDD} ဖြစ်သည်ဟူသော {KATHA}")
section("Vipāko vipākadhammadhammotikathā", f"{VIPK}သည် {VDD} ဖြစ်သည်ဟူသော {KATHA}")
P("vipāko vipākadhammadhammo", V(f"{VIPK}သည် {VDD}"))
P("tassa vipāko vipākadhammadhammo", V(f"ထို{VIPK}၏ {F.VIPAKA}သည် {VDD}"))
P("tassa tasseva natthi dukkhassa antakiriyā natthi vaṭṭupacchedo natthi anupādāparinibbānaṃ",
  V(f"ထိုထိုသူ၏ပင် {F.DUKKHA_END}ခြင်း {NEXIST}၊ ဝဋ်ကို ဖြတ်တောက်ခြင်း {NEXIST}၊ "
    "စွဲလမ်းမှု မရှိဘဲ ပရိနိဗ္ဗာန် ပြုခြင်း", EXIST, neg=True))
_ESE = F.PROP["kāyoti vā sarīranti vā, sarīranti vā kāyoti vā, kāyaṃ appiyaṃ karitvā esese ekaṭṭhe same samabhāge "
              "tajjāte"].pre
_ESE = _ESE[_ESE.index("ဤစကားတို့သည်"):]
P("vipākoti vā vipākadhammadhammoti vā vipākadhammadhammoti vā vipākoti vā esese ekaṭṭhe same samabhāge tajjāte",
  V(f"{VIPK}ဟုဖြစ်စေ၊ {VDD}ဟုဖြစ်စေ၊ {VDD}ဟုဖြစ်စေ၊ {VIPK}ဟုဖြစ်စေ {_ESE}"))
P("vipāko ca vipākadhammadhammo ca vipākadhammadhammo ca vipāko ca " + " ".join(_SH_PI),
  V(f"{VIPK}နှင့် {VDD}၊ {VDD}နှင့် {VIPK}တို့သည် " + sh_list("အချင်းချင်း", True) + " အရာတို့"))
P("taññeva akusalaṃ so akusalassa vipāko, taññeva kusalaṃ so kusalassa vipāko",
  V(f"ထိုအကုသိုလ်ပင် အကုသိုလ်၏ {F.VIPAKA} ဖြစ်၍ ထိုကုသိုလ်ပင် ကုသိုလ်၏ {F.VIPAKA}"))
P("yeneva cittena pāṇaṃ hanati teneva cittena niraye paccati, yeneva cittena dānaṃ deti teneva cittena sagge modati",
  Cl(f"အကြင် စိတ်ဖြင့် သတ္တဝါကို သတ်၏၊ ထိုစိတ်ဖြင့်ပင် ငရဲ၌ ကျက်၏၊ အကြင် စိတ်ဖြင့် {GIFT}ကို ပေး၏၊ "
     "ထိုစိတ်ဖြင့်ပင် နတ်ပြည်၌", "မွေ့လျော်", "မမွေ့လျော်"))
ARUPI = new("arūpino (khandhā / dhammā)", "ရုပ် မဟုတ်သော")
P("vipākā cattāro khandhā arūpino aññamaññapaccayā",
  Cl(f"{F.VIPAKA} ဖြစ်သော {ARUPI} {F.KHANDHA_W} {F.NUM_MY[4]}{F.CL}တို့သည် အချင်းချင်း အကြောင်း", "ဖြစ်ကြ", "မဖြစ်ကြ"))
LINES_X[key("Saṅgaho, sampayutto, cetasiko dhammo, cetasikaṃ dānaṃ, paribhogamayaṃ puññaṃ vaḍḍhati, ito dinnena "
            "tattha yāpenti, pathavī kammavipāko, jarāmaraṇaṃ vipāko, natthi ariyadhammavipāko, vipāko "
            "vipākadhammadhammoti.")] = (
    f"{SNG}ခြင်း၊ အခြား သဘောတရားနှင့် ယှဉ်တွဲသော အရာ၊ {CET} သဘောတရား၊ {CET} {DANA}၊ {PBM} တိုးပွားခြင်း၊ {ITO}ခြင်း၊ မြေသည် {KV}၊ "
    f"{JM}သည် {VIPK}၊ {ADV} {NEXIST}ခြင်း၊ {VIPK}သည် {VDD}{END}")

# ===================================================================================== 16. Aṭṭhamavaggo
section("Aṭṭhamavaggo", f"{F.ORD_MY[8]} {F.VAGGA_W}")
COLO_X["Aṭṭhamavaggo"] = HEAD_X["Aṭṭhamavaggo"]
# ------------------------------------------------------------------------------------- 73. Chagatikathā
GATI = P11.TOK["gati"]                                               # «လားရာ»
section("(73) 1. Chagatikathā", f"(73) 1. {GATI} ခြောက်ပါးအကြောင်း {KATHA}")
section("Chagatikathā", f"{GATI} ခြောက်ပါးအကြောင်း {KATHA}")
P("cha gatiyo", V(f"{GATI} {F.NUM_MY[6]}{F.CL}", EXIST))
_G5 = f"ငရဲ၊ {F.TIRACCHANA} မွေးဖွားရာ၊ {F.PETA} နယ်ပယ်၊ {F.MANUSSA}တို့၊ {F.DEVA}တို့"
P("pañca gatiyo vuttā bhagavatā – nirayo, tiracchānayoni, pettivisayo, manussā, devā",
  Cl(f"{GATI} {F.NUM_MY[5]}{F.CL}တို့ကို {BUDDHA}", "ဟောတော်မူ", "မဟောတော်မူ", post=f" – {_G5}"))
new("nirayo, tiracchānayoni, pettivisayo, manussā, devā", _G5)
_SAME = "အဆင်း တူကြ၏၊ စည်းစိမ် တူကြ၏၊ အစာ တူကြ၏၊ အသက် တူကြ၏၊"
for _w, _wm in (("kālakañcikā surā", "ကာလကဉ္စိက နတ်တို့"), ("kālakañcikā asurā", "ကာလကဉ္စိက အသုရာတို့")):
    P(f"{_w} petānaṃ samānavaṇṇā samānabhogā samānāhārā samānāyukā petehi saha āvāhavivāhaṃ gacchanti",
      Cl(f"{_wm}သည် {F.PETA}တို့နှင့် {_SAME} {F.PETA}တို့နှင့်အတူ ထိမ်းမြားခြင်း", "ပြုကြ", "မပြုကြ"))
ANCHOR_X["kālakañcikā"] = "ကာလကဉ္စိက"
VAR_X.update({"kālakañjikā": F.LEKHANA, "kāḷakañjakā": F.LEKHANA})
VPP = "ဝေပစိတ္တိ အသုရာ၏ ပရိသတ်တို့"
P("vepacittiparisā devānaṃ samānavaṇṇā samānabhogā samānāhārā samānāyukā devehi saha āvāhavivāhaṃ gacchanti",
  Cl(f"{VPP}သည် {F.DEVA}တို့နှင့် {_SAME} {F.DEVA}တို့နှင့်အတူ ထိမ်းမြားခြင်း", "ပြုကြ", "မပြုကြ"))
P("vepacittiparisā pubbadevā", V(f"{VPP}သည် ရှေးနတ်တို့"))
S("Nanu atthi asurakāyoti, āmantā.", f"အသုရာ အပေါင်း {EXIST}သည် မဟုတ်လော၊ {F.YES}{END}")
P("atthi asurakāyo", V("အသုရာ အပေါင်း", EXIST))

# ------------------------------------------------------------------------------------- existence lists (74-78)
_EXL6 = "ဘဝ၊ " + "၊ ".join(P11.TOK[k] for k in ("gati", "sattāvāso", "saṃsāro", "yoni"))   # bhavo … yoni
_VT_ = "သိစိတ် တည်ရာ"
_ATB = P11.TOK["attabhāvapaṭilābho"]
_EXL_FULL = f"{_EXL6}၊ {_VT_}၊ {_ATB}"
_EXL_PE = f"ဘဝ၊ {P11.TOK['gati']}… {_ATB}"
_EXL_G = f"ဘဝ၊ {P11.TOK['gati']}…"
BHV = {"kāmabhav": "ကာမဘုံ၌ ဖြစ်သော ဘဝ", "rūpabhav": "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော ဘဝ",
       "arūpabhav": "ရုပ်မရှိသော ဘုံ၌ ဖြစ်သော ဘဝ"}
for _k, _m in BHV.items():
    W("2", "^2-234", _k[0].upper() + _k[1:] + "o", _m)
ANTB = new("antarābhavo", "ကြားဘဝ")
SUBJ74 = {  # nom -> (Burmese, upaga stem, locative Pāli)
    "antarābhavo": (ANTB, "antarābhav", "antarābhave"), "kāmabhavo": (BHV["kāmabhav"], "kāmabhav", "kāmabhave"),
    "rūpabhavo": (BHV["rūpabhav"], "rūpabhav", "rūpabhave"), "arūpabhavo": (BHV["arūpabhav"], "arūpabhav", "arūpabhave"),
    "kāmaguṇā": ("ကာမဂုဏ်တို့", "kāmaguṇ", "kāmaguṇe"), "kāmadhātu": ("ကာမဘုံ", "kāmadhāt", "kāmadhātuyā"),
    "rūpaṃ": (F.RUPA.my, "rūp", "rūpe"), "rūpadhātu": ("သိမ်မွေ့သော ရုပ်ဘုံ", "rūpadhāt", "rūpadhātuyā"),
    "vedanā": (F.VEDANA.my, "vedan", "vedanāya"), "arūpadhātu": ("ရုပ်မရှိသော ဘုံ", "arūpadhāt", "arūpadhātuyā"),
}
new("kāmadhātu / rūpadhātu / arūpadhātu (realms)", "ကာမဘုံ / သိမ်မွေ့သော ရုပ်ဘုံ / ရုပ်မရှိသော ဘုံ (pi-2 ^2-916)")
W("2", "^2-916", "Rūpadhātuarūpadhātupaṭisaṃyutto", "သိမ်မွေ့သော ရုပ်ဘုံနှင့် ရုပ်မရှိသော ဘုံနှင့် စပ်ယှဉ်သော")
_UPA = {"ū": ""}
for _s, (_sm, _u, _l) in SUBJ74.items():
    _ux = _u + ("ū" if not _u.endswith("t") else "ū")
    P(f"{_s} bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho", V(f"{_sm}သည် {_EXL_FULL}"))
    P(f"{_s} bhavo gati… attabhāvapaṭilābho", V(f"{_sm}သည် {_EXL_PE}"))
    P(f"atthi {_s}", V(_sm, EXIST)) if not has(f"atthi {_s}") else None
    P(_s, V(_sm)) if not has(_s) else None
    P(f"atthi {_u}ūpagaṃ kammaṃ", V(f"{_sm}သို့ ရောက်စေသော {F.KAMMA}", EXIST))
    P(f"atthi {_u}ūpagā sattā", V(f"{_sm}သို့ ရောက်သော {F.SATTA}တို့", EXIST))
    P(f"{_l} sattā jāyanti jīyanti mīyanti cavanti upapajjanti",
      Cl(f"{_sm}၌ {F.SATTA}တို့ မွေးဖွားကြ၏၊ အိုကြ၏၊ သေဆုံးကြ၏၊ စုတေကြ၏၊", "ပြန်လည် ဖြစ်ပေါ်ကြ", "ပြန်လည် မဖြစ်ပေါ်ကြ"))
    P(f"{_l} atthi rūpaṃ vedanā saññā saṅkhārā viññāṇaṃ",
      V(f"{_sm}၌ {F.RUPA.my}၊ {F.VEDANA.my}၊ {F.SANNA.my}၊ {F.SANKHARA.my}၊ {F.VINNANA.my}", EXIST))
    P(f"{_l} atthi vedanā saññā saṅkhārā viññāṇaṃ",
      V(f"{_sm}၌ {F.VEDANA.my}၊ {F.SANNA.my}၊ {F.SANKHARA.my}၊ {F.VINNANA.my}", EXIST))
    for _v in ("pañcavokārabhavo", "catuvokārabhavo"):
        P(f"{_s} {_v}", V(f"{_sm}သည် {P11.TOK[_v]}"))
for _s in ("kāmabhavo", "rūpabhavo", "arūpabhavo"):
    P(f"atthi {_s}, {_s} bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho",
      V(f"{SUBJ74[_s][0]} {EXIST}၍ {SUBJ74[_s][0]}သည် {_EXL_FULL}"))
P("atthi antarābhavo, antarābhavo bhavo gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho",
  V(f"{ANTB} {EXIST}၍ {ANTB}သည် {_EXL_FULL}"))

# ------------------------------------------------------------------------------------- 74. Antarābhavakathā
section("(74) 2. Antarābhavakathā", f"(74) 2. {ANTB}အကြောင်း {KATHA}")
section("Antarābhavakathā", f"{ANTB}အကြောင်း {KATHA}")
for _a, _b in (("kāmabhavassa", "rūpabhavassa"), ("rūpabhavassa", "arūpabhavassa")):
    _am, _bm = BHV[_a[:-4]], BHV[_b[:-4]]
    for _n, _neg in (("atthi", False), ("natthi", True)):
        P(f"{_a} ca {_b} ca antare {_n} antarābhavo", V(f"{_am}နှင့် {_bm}တို့၏ ကြား၌ {ANTB}", EXIST, neg=_neg))
P("pañcamī sā yoni, chaṭṭhamī sā gati, aṭṭhamī sā viññāṇaṭṭhiti, dasamo so sattāvāso",
  V(f"ထိုကြားဘဝသည် {F.ORD_MY[5]} {P11.TOK['yoni']}၊ {F.ORD_MY[6]} {GATI}၊ {F.ORD_MY[8]} {_VT_}၊ "
    f"{F.ORD_MY[10]} {P11.TOK['sattāvāso']}"))
ANANT = new("ānantariyo puggalo", "အနန္တရိယ ကံကို ပြုသော ပုဂ္ဂိုလ်")
P11_ASAT = P11.ASAT
_P74 = {"sabbesaññeva sattānaṃ": f"{F.SATTA} အားလုံးတို့၌ပင်", "ānantariyassa puggalassa": f"{ANANT}၌",
        "na ānantariyassa puggalassa": f"{ANANT} မဟုတ်သူ၌",
        "nirayūpagassa puggalassa": f"ငရဲသို့ ရောက်မည့် {PUG}၌",
        "asaññasattūpagassa puggalassa": f"{P11_ASAT}သို့ ရောက်မည့် {PUG}၌",
        "arūpūpagassa puggalassa": f"ရုပ်မရှိသော ဘုံသို့ ရောက်မည့် {PUG}၌",
        "na arūpūpagassa puggalassa": f"ရုပ်မရှိသော ဘုံသို့ ရောက်မည့် {PUG} မဟုတ်သူ၌"}
for _g, _gm in _P74.items():
    P(_g, FR(_gm))
    for _n, _neg in (("atthi", False), ("natthi", True)):
        P(f"{_g} {_n} antarābhavo", V(f"{_gm} {ANTB}", EXIST, neg=_neg))


@F.frame(r"Na vattabbaṃ (?P<p>[^–\"]+?)ti\?")
def _f_navatt_nodash(m):
    """Na vattabbaṃ P-ti? without dash and quotes (^5-509): «Pဟု မဆိုသင့်သလော» (no dash, no marks added)."""
    return f"{F.pq(m['p'], 'stmt')}ဟု ဤသို့ မဆိုသင့်သလော{END}"


before_generic()
P("antarāparinibbāyī puggalo atthi", V(f"{P6._PT4['antarāparinibbāyī']} {PUG}", EXIST))
P("upahaccaparinibbāyī puggalo atthi", V(f"{P6._PT4['upahaccaparinibbāyī']} {PUG}", EXIST))
P("asaṅkhāraparinibbāyī puggalo", FR(f"{P6._PT4['asaṅkhāraparinibbāyī']} {PUG}"))
P("sasaṅkhāraparinibbāyī puggalo atthi", V(f"{P6._PT4['sasaṅkhāraparinibbāyī']} {PUG}", EXIST))
P("atthi upahaccabhavo", V("သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ ဖြစ်သော ဘဝ", EXIST))
P("atthi sasaṅkhārabhavo", V("တိုက်တွန်းမှုဖြင့် ဖြစ်သော ဘဝ", EXIST))
new("upahaccabhavo / sasaṅkhārabhavo", "သက်တမ်း၏ အလယ်ကို ကျော်ပြီးမှ ဖြစ်သော ဘဝ / တိုက်တွန်းမှုဖြင့် ဖြစ်သော ဘဝ")
VAR_X.update({"no ca vata re": F.PATHA, "no vata re": F.PATHA})

# ------------------------------------------------------------------------------------- 75-76. Kāmaguṇa / Kāma
KGN = "ကာမဂုဏ်"
section("(75) 3. Kāmaguṇakathā", f"(75) 3. {KGN}အကြောင်း {KATHA}")
section("Kāmaguṇakathā", f"{KGN}အကြောင်း {KATHA}")
section("(76) 4. Kāmakathā", f"(76) 4. ကာမအကြောင်း {KATHA}")
section("Kāmakathā", f"ကာမအကြောင်း {KATHA}")
P("pañceva kāmaguṇā kāmadhātu", V(f"{KGN} {F.NUM_MY[5]}{F.CL}သည်သာ ကာမဘုံ"))
AY5 = f"အာရုံခံ နယ်ပယ် {F.NUM_MY[5]}{F.CL}"
P("pañcevāyatanā kāmā", V(f"{AY5}သည်သာ ကာမတို့"))
TAPP = "ထိုအရာနှင့် စပ်ယှဉ်သော"                                     # tappaṭisaññutto / tappaṭisaṃyutto (pi-2 paṭisaṃyutto)
_TP = [("rāgo", "ရာဂ"), ("chando", "လိုလားမှု"), ("chandarāgo", "လိုလားမှု ရာဂ"), ("saṅkappo", "ကြံစည်မှု"),
       ("rāgo", "ရာဂ"), ("saṅkapparāgo", "ကြံစည်မှု ရာဂ"), ("pīti", "ပီတိ"), ("somanassaṃ", "ဝမ်းမြောက်မှု"),
       ("pītisomanassaṃ", "ပီတိ ဝမ်းမြောက်မှု")]
for _t in ("tappaṭisaññutt", "tappaṭisaṃyutt"):
    P(f"atthi {_t}o chando", V(f"{TAPP} လိုလားမှု", EXIST))
    P(f"atthi {_t}aṃ pītisomanassaṃ", V(f"{TAPP} ပီတိ ဝမ်းမြောက်မှု", EXIST))
    _pi = " ".join(f"{_t}{'ā' if k == 'pīti' else ('aṃ' if k.endswith('aṃ') else 'o')} {k}" for k, _ in _TP)
    P(f"atthi {_pi}", V("၊ ".join(f"{TAPP} {m}" for _, m in _TP), EXIST))
new("tappaṭisaññutto / tappaṭisaṃyutto", TAPP)
_SN6 = [("cakkhu", "မျက်စိ"), ("sotaṃ", "နား"), ("ghānaṃ", "နှာခေါင်း"), ("jivhā", "လျှာ"), ("kāyo", "ကိုယ်"),
        ("mano", "မနော")]
for _k, _m in _SN6:
    P(f"manussānaṃ {_k}", FR(f"{F.MANUSSA}တို့၏ {_m}"))
    P(f"manussānaṃ {_k} na kāmadhātu", V(f"{F.MANUSSA}တို့၏ {_m}သည် ကာမဘုံ", neg=True))
_KV = [('"Pañca kāmaguṇā loke, manocchaṭṭhā paveditā;', f"“လောက၌ မနော ခြောက်ခုမြောက် ရှိသော {KGN} ငါးပါးတို့ကို ဟောကြားထား၏၊"),
       ('Ettha chandaṃ virājetvā, evaṃ dukkhā pamuccatī"ti [su. ni. 173; saṃ. ni. 1.30].',
        "ဤကာမဂုဏ်တို့၌ လိုလားမှုကို ကင်းစေ၍ ဤသို့ ဆင်းရဲမှ လွတ်မြောက်၏” ⟦0⟧။")]
for _p, _m in _KV:
    LINES_X[key(_p)] = _m
_BUD = [("sammāsambuddhā uppajjanti", f"{EPI11.split('၊ ')[2]}တို့ ပွင့်ကြ၏"),
        ("paccekasambuddhā uppajjanti", W("4", "^4-M-1" if False else "^4-M-7", "Paccekasambuddho", "ပစ္စေကဗုဒ္ဓါ") + "တို့ ပွင့်ကြ၏")
        if False else ("paccekasambuddhā uppajjanti", "ပစ္စေကဗုဒ္ဓါတို့ ပွင့်ကြ၏")]
for _l, _lm in (("kāmaguṇe", f"{KGN}တို့၌"), ("kāmadhātuyā", "ကာမဘုံ၌")):
    for _pc in ("paccekasambuddhā", "paccekasabuddhā"):
        P(f"{_l} sammāsambuddhā uppajjanti, {_pc} uppajjanti, sāvakayugaṃ uppajjati",
          Cl(f"{_lm} {_BUD[0][1]}၊ {_BUD[1][1]}၊ အဂ္ဂသာဝက နှစ်ပါး", "ပေါ်ပေါက်", "မပေါ်ပေါက်"))
_KGQ = ("ရဟန်းတို့၊ ဤ{KGN} ငါးပါးတို့ ရှိကုန်၏။ အဘယ် ငါးပါးနည်း။ မျက်စိဖြင့် သိနိုင်သော၊ လိုလားဖွယ် ကောင်းသော၊ "
        "ချစ်ခင်ဖွယ် ကောင်းသော၊ နှစ်သက်ဖွယ် ကောင်းသော၊ ချစ်ဖွယ် သဘော ရှိသော၊ ကာမနှင့် စပ်သော၊ တပ်မက်ဖွယ် ကောင်းသော "
        "အဆင်းအရောင်တို့")
_IK = ("လိုလားဖွယ် ကောင်းသော၊ ချစ်ခင်ဖွယ် ကောင်းသော၊ နှစ်သက်ဖွယ် ကောင်းသော၊ ချစ်ဖွယ် သဘော ရှိသော၊ ကာမနှင့် စပ်သော၊ "
       "တပ်မက်ဖွယ် ကောင်းသော")
_K5 = f"{_R} ဤ{KGN} ငါးပါးတို့ ရှိကုန်၏။ အဘယ် ငါးပါးနည်း။"
Q("pañcime, bhikkhave, kāmaguṇā! Katame pañca? Cakkhuviññeyyā rūpā iṭṭhā kantā manāpā piyarūpā kāmūpasaṃhitā "
  "rajanīyā, sotaviññeyyā saddā…pe… ghānaviññeyyā gandhā…pe… jivhāviññeyyā rasā…pe… kāyaviññeyyā phoṭṭhabbā iṭṭhā "
  "kantā manāpā piyarūpā kāmūpasaṃhitā rajanīyā – ime kho, bhikkhave, pañca kāmaguṇā",
  f"{_K5} မျက်စိဖြင့် သိနိုင်သော၊ {_IK} အဆင်းအရောင်တို့၊ နားဖြင့် သိနိုင်သော အသံတို့… နှာခေါင်းဖြင့် သိနိုင်သော "
  f"အနံ့တို့… လျှာဖြင့် သိနိုင်သော အရသာတို့… ကိုယ်ဖြင့် သိနိုင်သော၊ {_IK} အထိအတွေ့တို့ – {_R} ဤသည်တို့ကား "
  f"{KGN} ငါးပါးတို့ ဖြစ်ကုန်၏")
Q("pañcime, bhikkhave, kāmaguṇā! Katame pañca? Cakkhuviññeyyā rūpā…pe… kāyaviññeyyā phoṭṭhabbā iṭṭhā kantā manāpā "
  "piyarūpā kāmūpasaṃhitā rajanīyā – ime kho, bhikkhave, pañca kāmaguṇā",
  f"{_K5} မျက်စိဖြင့် သိနိုင်သော အဆင်းအရောင်တို့… ကိုယ်ဖြင့် သိနိုင်သော၊ {_IK} အထိအတွေ့တို့ – {_R} ဤသည်တို့ကား "
  f"{KGN} ငါးပါးတို့ ဖြစ်ကုန်၏")
S('Nanu vuttaṃ bhagavatā – "pañcime, bhikkhave, kāmaguṇā! Katame pañca? Cakkhuviññeyyā rūpā…pe… kāyaviññeyyā '
  'phoṭṭhabbā iṭṭhā kantā manāpā piyarūpā kāmūpasaṃhitā rajanīyā – ime kho, bhikkhave, pañca kāmaguṇā. Api ca, '
  'bhikkhave, nete kāmā kāmaguṇā nāmete ariyassa vinaye vucca"nti –',
  f"{F.VUTTA_PRE}သည် မဟုတ်လော – “{_K5} မျက်စိဖြင့် သိနိုင်သော အဆင်းအရောင်တို့… ကိုယ်ဖြင့် သိနိုင်သော၊ {_IK} "
  f"အထိအတွေ့တို့ – {_R} ဤသည်တို့ကား {KGN} ငါးပါးတို့ ဖြစ်ကုန်၏။ {_R} သို့ရာတွင် ဤကာမဂုဏ်တို့သည် ကာမတို့ မဟုတ်ကုန်၊ "
  "အရိယာ၏ ဝိနည်း၌ ဤသည်တို့ကို ကာမဂုဏ်တို့ဟု ခေါ်ကုန်၏”ဟု –")   # harmonise B5: «"…"nti –» = «”ဟု –»
_KMV = [('"Saṅkapparāgo purisassa kāmo,', "ယောကျ်ား၏ ကြံစည်မှု ရာဂသည် ကာမ ဖြစ်၏၊"),
        ("Na te kāmā yāni citrāni loke;", "လောက၌ အဆန်းတကြယ် ရှိသော အရာတို့သည် ကာမတို့ မဟုတ်ကုန်၊"),
        ("Saṅkapparāgo purisassa kāmo,", "ယောကျ်ား၏ ကြံစည်မှု ရာဂသည် ကာမ ဖြစ်၏၊"),
        ("Tiṭṭhanti citrāni tatheva loke;", "လောက၌ အဆန်းတကြယ် ရှိသော အရာတို့သည် ထိုအတိုင်းပင် တည်ကုန်၏၊"),
        ('Athettha dhīrā vinayanti chanda"nti [a. ni. 6.63 nibbedhikasutte].',
         "ထိုအရာတို့၌ ပညာရှိတို့သည် လိုလားမှုကို ပယ်ဖျောက်ကြကုန်၏” ⟦0⟧။")]
for _p, _m in _KMV:
    LINES_X[key(_p)] = _m
BR_X["[a. ni. 6.63 nibbedhikasutte]"] = f"[{F.REF['a. ni.']} 6.63၊ “နိဗ္ဗေဓိက သုတ်”]"

# ------------------------------------------------------------------------------------- 77-78. Rūpadhātu / Arūpadhātu
RPD = SUBJ74["rūpadhātu"][0]
ARPD = SUBJ74["arūpadhātu"][0]
RUPI = W("1", "^1-M2-11", "rūpino dhammā", "ရုပ် ဖြစ်သော") if False else "ရုပ် ဖြစ်သော"
section("(77) 5. Rūpadhātukathā", f"(77) 5. {RPD}အကြောင်း {KATHA}")
section("Rūpadhātukathā", f"{RPD}အကြောင်း {KATHA}")
section("(78) 6. Arūpadhātukathā", f"(78) 6. {ARPD}အကြောင်း {KATHA}")
section("Arūpadhātukathā", f"{ARPD}အကြောင်း {KATHA}")
P("rūpino dhammā rūpadhātu", V(f"{RUPI} သဘောတရားတို့သည် {RPD}"))
P("arūpino dhammā arūpadhātu", V(f"{ARUPI} သဘောတရားတို့သည် {ARPD}"))
P("kāmadhātuyā atthi rūpaṃ", V(f"ကာမဘုံ၌ {F.RUPA.my}", EXIST))
P("sāva kāmadhātu, sā rūpadhātu", V(f"ထိုကာမဘုံပင် {RPD}"))
P("sāva kāmadhātu, sā arūpadhātu", V(f"ထိုကာမဘုံပင် {ARPD}"))
P("sāva kāmadhātu, sā rūpadhātu, sā arūpadhātu", V(f"ထိုကာမဘုံပင် {RPD} ဖြစ်၍ {ARPD}"))
_KBS = f"{BHV['kāmabhav']}နှင့် ပြည့်စုံသော {PUG}သည် ဘဝ "
for _n, _nm, _l, _lm in (("dvīhi", F.NUM_MY[2], "kāmabhavena ca rūpabhavena ca",
                          f"{BHV['kāmabhav']}နှင့်လည်းကောင်း၊ {BHV['rūpabhav']}နှင့်လည်းကောင်း"),
                         ("dvīhi", F.NUM_MY[2], "kāmabhavena ca arūpabhavena ca",
                          f"{BHV['kāmabhav']}နှင့်လည်းကောင်း၊ {BHV['arūpabhav']}နှင့်လည်းကောင်း"),
                         ("tīhi", F.NUM_MY[3], "kāmabhavena ca rūpabhavena ca arūpabhavena ca",
                          f"{BHV['kāmabhav']}နှင့်လည်းကောင်း၊ {BHV['rūpabhav']}နှင့်လည်းကောင်း၊ "
                          f"{BHV['arūpabhav']}နှင့်လည်းကောင်း")):
    P(f"kāmabhavena samannāgato puggalo {_n} bhavehi samannāgato hoti – {_l}",
      Cl(f"{_KBS}{_nm}{F.CL}တို့နှင့်", "ပြည့်စုံ", "မပြည့်စုံ", post=f" – {_lm}"))
P("kāmadhātuyā atthi vedanā saññā saṅkhārā viññāṇaṃ",
  V(f"ကာမဘုံ၌ {F.VEDANA.my}၊ {F.SANNA.my}၊ {F.SANKHARA.my}၊ {F.VINNANA.my}", EXIST)) \
    if not has("kāmadhātuyā atthi vedanā saññā saṅkhārā viññāṇaṃ") else None

# ------------------------------------------------------------------------------------- 79. Rūpadhātuyā āyatana
section("(79) 7. Rūpadhātuyāāyatanakathā", f"(79) 7. {RPD}၌ အာရုံခံ နယ်ပယ်အကြောင်း {KATHA}")
section("Rūpadhātuyā āyatanakathā", f"{RPD}၌ အာရုံခံ နယ်ပယ်အကြောင်း {KATHA}")
SAL = new("saḷāyataniko attabhāvo", f"အာရုံခံ နယ်ပယ် {F.NUM_MY[6]}{F.CL} ရှိသော {_ATB}")
P("atthi saḷāyataniko attabhāvo rūpadhātuyā", V(f"{RPD}၌ {SAL}", EXIST))
P("saḷāyataniko attabhāvo rūpadhātuyā", V(f"{RPD}၌ {SAL}", EXIST))
AYN = {F.AYATANA[a].pali["nom"]: F.AYATANA[a].my for a in F.AYATANA}
for _a, _am in AYN.items():
    for _n, _neg in (("atthi", False), ("natthi", True)):
        P(f"{_n} tattha {_a}", V(f"ထိုဘုံ၌ {_am}", EXIST, neg=_neg))
        P(f"{_n} {_a}", V(_am, EXIST, neg=_neg)) if not has(f"{_n} {_a}") else None
_PAIRS = [("cakkhāyatanaṃ", "rūpāyatanaṃ"), ("sotāyatanaṃ", "saddāyatanaṃ"), ("ghānāyatanaṃ", "gandhāyatanaṃ"),
          ("jivhāyatanaṃ", "rasāyatanaṃ"), ("kāyāyatanaṃ", "phoṭṭhabbāyatanaṃ"), ("manāyatanaṃ", "dhammāyatanaṃ")]
for _a, _b in _PAIRS:
    P(f"atthi tattha {_a} atthi {_b}", V(f"ထိုဘုံ၌ {AYN[_a]} {EXIST}၍ {AYN[_b]}", EXIST))
    P(f"atthi tattha {_a}, atthi {_b}", V(f"ထိုဘုံ၌ {AYN[_a]} {EXIST}၍ {AYN[_b]}", EXIST))
    P(f"atthi tattha {_a}, natthi {_b}", V(f"ထိုဘုံ၌ {AYN[_a]} {EXIST}၍ {AYN[_b]}", EXIST, neg=True))
_SEE = [("tena cakkhunā taṃ rūpaṃ passati", "ထိုမျက်စိဖြင့် ထိုအဆင်းအရောင်ကို", "မြင်"),
        ("tena ghānena taṃ gandhaṃ ghāyati", "ထိုနှာခေါင်းဖြင့် ထိုအနံ့ကို", F.GHAYATI),    # harmonise B2: pi-1 / pi-2
        ("tāya jivhāya taṃ rasaṃ sāyati", "ထိုလျှာဖြင့် ထိုအရသာကို", F.SAYATI),
        ("tena kāyena taṃ phoṭṭhabbaṃ phusati", "ထိုကိုယ်ဖြင့် ထိုအထိအတွေ့ကို", "ထိ"),
        ("tena manena taṃ dhammaṃ vijānāti", "ထိုမနောဖြင့် ထိုသဘောတရားကို", "သိ")]
for _k, _m, _v in _SEE:
    P(_k, VV(_m, _v))
    P("na ca " + _k, VV(_m, _v, neg=True))
new("tena cakkhunā taṃ rūpaṃ passati … (the five)", "ထိုမျက်စိဖြင့် ထိုအဆင်းအရောင်ကို မြင် … (ခံ / ခံ / ထိ / သိ; ch6-10 SENSE)")
_GN = W("1", "^1-625", "mūlagandho sāragandho", "အမြစ် အနံ့၊ အနှစ် အနံ့") if False else None
_GNL = ("အမြစ် အနံ့၊ အနှစ် အနံ့၊ အခေါက် အနံ့၊ အရွက် အနံ့၊ ပန်း အနံ့၊ အသီး အနံ့၊ အစိမ်း အနံ့၊ ပုပ်သိုး အနံ့၊ "
        "မွှေးသော အနံ့၊ နံစော်သော အနံ့")
_RSL = ("အမြစ် အရသာ၊ ပင်စည် အရသာ၊ အခေါက် အရသာ၊ အရွက် အရသာ၊ ပန်း အရသာ၊ အသီး အရသာ၊ အချဉ်၊ အချို၊ အခါး၊ အစပ်၊ "
        "အငန်၊ ပြာရည် အရသာ၊ အချဉ်စူး၊ အဖန်၊ စားကောင်းသော အရသာ၊ စားမကောင်းသော အရသာ")
_PHL = ("ကြမ်းတမ်းသောအရာ၊ ပျော့ပျောင်းသောအရာ၊ ချောမွေ့သောအရာ၊ ဖုထစ်သောအရာ၊ ထိတွေ့ရ သာယာသောအရာ၊ "
        "ထိတွေ့ရ နာကျင်သောအရာ၊ လေးလံသောအရာ၊ ပေါ့ပါးသောအရာ")
for _p, _m in (("mūlagandho sāragandho", _GNL.split("၊ ")[0]), ("mūlaraso khandharaso", _RSL.split("၊ ")[0]),
               ("kakkhaḷaṃ mudukaṃ", _PHL.split("၊ ")[0])):
    W("1", {"mūlagandho sāragandho": "^1-624", "mūlaraso khandharaso": "^1-625",
            "kakkhaḷaṃ mudukaṃ": "^1-626"}[_p], _p, _m) if False else None
P("atthi tattha mūlagandho sāragandho tacagandho pattagandho pupphagandho phalagandho āmagandho vissagandho "
  "sugandho duggandho", V(f"ထိုဘုံ၌ {_GNL}", EXIST))
P("atthi tattha mūlaraso khandharaso tacaraso pattaraso puppharaso phalaraso ambilaṃ madhuraṃ tittakaṃ kaṭukaṃ "
  "loṇiyaṃ khāriyaṃ lambilaṃ kasāvo sādu asādu", V(f"ထိုဘုံ၌ {_RSL}", EXIST))
P("atthi tattha kakkhaḷaṃ mudukaṃ saṇhaṃ pharusaṃ sukhasamphassaṃ dukkhasamphassaṃ garukaṃ lahukaṃ",
  V(f"ထိုဘုံ၌ {_PHL}", EXIST))
P("atthi tattha ghānanimittaṃ jivhānimittaṃ kāyanimittaṃ",
  V(f"ထိုဘုံ၌ နှာခေါင်း၏ {F.NIMITTA}၊ လျှာ၏ {F.NIMITTA}၊ ကိုယ်၏ {F.NIMITTA}", EXIST))

# ------------------------------------------------------------------------------------- 80. Arūpe rūpakathā
ARUPESU = "ရုပ်မရှိသော ဘုံတို့၌"
BR_X["[arūpadhātuyā (sabbattha)]"] = "[ပါဌ်ကွဲ (Sabbattha): arūpadhātuyā]"     # pi-2 ^2-754 label
ANCHOR_X["rūpadhātuyā"] = "သိမ်မွေ့သော ရုပ်ဘုံ၌"
section("(80) 8. Arūpe rūpakathā", f"(80) 8. ရုပ်မရှိသော ဘုံ၌ ရုပ်အကြောင်း {KATHA}")
section("Arūpe rūpakathā", f"ရုပ်မရှိသော ဘုံ၌ ရုပ်အကြောင်း {KATHA}")
P("atthi rūpaṃ arūpesu", V(f"{ARUPESU} {F.RUPA.my}", EXIST))
P("atthi rūpaṃ rūpadhātuyā", V(f"{RPD}၌ {F.RUPA.my}", EXIST))
_RL6 = ["bhavo", "gati", "sattāvāso", "saṃsāro", "yoni", "ttabhāvapaṭilābho"]
_RLM = ["ဘဝ", P11.TOK["gati"], P11.TOK["sattāvāso"], P11.TOK["saṃsāro"], P11.TOK["yoni"], _ATB]
for _p, _pm in (("rūpa", "သိမ်မွေ့သော ရုပ်ဘုံ၌ ဖြစ်သော"), ("arūpa", "ရုပ်မရှိသော ဘုံ၌ ဖြစ်သော")):
    _full = " ".join(_p + w for w in _RL6)
    _my = f"{_pm} " + "၊ ".join(_RLM)
    _pe = f"{_p}bhavo {_p}gati… {_p}ttabhāvapaṭilābho"
    _pem = f"{_pm} ဘဝ၊ {_RLM[1]}… {_ATB}"
    _pe2 = f"{_p}bhavo… {_p}ttabhāvapaṭilābho"
    _pe2m = f"{_pm} ဘဝ… {_ATB}"
    for _k, _m in ((_full, _my), (_pe, _pem), (_pe2, _pe2m)):
        P(_k, V(_m))
        P(f"so ca {_k}", V(f"ထိုဘဝသည်လည်း {_m}"))
for _v, _vm in (("pañcavokārabhavo", P11.TOK["pañcavokārabhavo"]), ("catuvokārabhavo", P11.TOK["catuvokārabhavo"])):
    _gl = "၊ ".join(_RLM[1:5])
    P(f"{_v} gati sattāvāso saṃsāro yoni viññāṇaṭṭhiti attabhāvapaṭilābho",
      V(f"{_vm}၊ {_gl}၊ {_VT_}၊ {_ATB}"))
    P(f"{_v}… attabhāvapaṭilābho", V(f"{_vm}… {_ATB}"))
    P(f"{_v} gati… attabhāvapaṭilābho", V(f"{_vm}၊ {_RLM[1]}… {_ATB}"))
    P(f"so ca {_v} gati… attabhāvapaṭilābho", V(f"ထိုဘဝသည်လည်း {_vm}၊ {_RLM[1]}… {_ATB}"))
    P(_v, V(_vm)) if not has(_v) else None
NISS = "ထွက်မြောက်ရာ"
P("rūpānaṃ nissaraṇaṃ arūpaṃ vuttaṃ bhagavatā",
  Cl(f"{F.RUPA.my}တို့မှ {NISS}ကို {F.RUPA.my} မဟုတ်သော အရာဟု {BUDDHA}", "ဟောတော်မူ", "မဟောတော်မူ"))
ANCHOR_X["arūpaṃ"] = f"{F.RUPA.my} မဟုတ်သော အရာဟု"
BR_X["[itivu. 72; a. ni. 5.200; dī. ni. 3.321]"] = (
    f"[{F.REF['itivu.']} 72၊ {F.REF['a. ni.']} 5.200၊ {F.REF['dī. ni.']} 3.321]")
_APR = W("1", "^1-1036", "apariyāpannā", "ဘဝဘုံတို့၌ အကျုံးမဝင်သော")
P("kāmānaṃ nissaraṇaṃ nekkhammaṃ vuttaṃ bhagavatā, atthi nekkhammesu kāmā, atthi anāsavesu āsavā, atthi "
  "apariyāpannesu pariyāpannā",
  V(f"ကာမတို့မှ {NISS}ကို ကာမမှ ထွက်မြောက်ခြင်းဟု {BUDDHA} ဟောတော်မူ၏၊ ကာမမှ ထွက်မြောက်ခြင်းတို့၌ ကာမတို့ {EXIST}သည်၊ "
    f"{P11.ANAS} အရာတို့၌ စိတ်အစွန်းအထင်းတို့ {EXIST}သည်၊ {_APR} အရာတို့၌ ဘဝဘုံတို့၌ အကျုံးဝင်သော အရာတို့", EXIST))

# ------------------------------------------------------------------------------------- 81. Rūpaṃ kammantikathā
section("(81) 9. Rūpaṃ kammantikathā", f"(81) 9. ရုပ်သည် {F.KAMMA} ဖြစ်သည်ဟူသော {KATHA}")
section("Rūpaṃ kammantikathā", f"ရုပ်သည် {F.KAMMA} ဖြစ်သည်ဟူသော {KATHA}")
KK = SUBJ_SAN["kāyakammaṃ"][0]                                        # «ကိုယ်ဖြင့် ပြုသော ကံ»
VK = "နှုတ်ဖြင့် ပြုသော ကံ"
MK_ = "မနောဖြင့် ပြုသော ကံ"
W("1", "^1-985", "vacīkammaṃ, manokammaṃ", "နှုတ်ဖြင့် ပြုသော ကံ၊ မနောဖြင့် ပြုသော ကံ")
SUB81 = {"kāyakammaṃ rūpaṃ": f"{KK} ဖြစ်သော {F.RUPA.my}", "vacīkammaṃ rūpaṃ": f"{VK} ဖြစ်သော {F.RUPA.my}",
         "rūpaṃ": F.RUPA.my, "phasso": NOM["phasso"]}
SUB81.update({k: v for k, v in AYN.items()})
SUB81.update({f"{_d}dhātu": f"{_dm}ဓာတ်" for _d, _dm in (("pathavī", "မြေ"), ("āpo", "ရေ"), ("tejo", "မီး"), ("vāyo", "လေ"))})
SUB81.update({k: v for k, v in NOM.items()})
SUB81["vāyodhātu asuci assu lohitaṃ sedo"] = f"လေဓာတ်၊ {P6.ASUCI}၊ မျက်ရည်၊ သွေး၊ ချွေး"
PRED81 = {"kusal": "ကုသိုလ်", "akusal": "အကုသိုလ်", "abyākat": F.HEAD.get("__abyakata__", "ကုသိုလ်လည်း မဟုတ်၊ အကုသိုလ်လည်း မဟုတ်သော"),
          "sārammaṇ": "အာရုံ ရှိသော", "anārammaṇ": "အာရုံ မရှိသော", "phassavippayutt": "တွေ့ထိမှုနှင့် ကင်းကွာသော"}
_PRED_RX = r"(?:akusal|abyākat|kusal|sārammaṇ|anārammaṇ|phassavippayutt)(?:aṃ|o|ā)"
_SUBS_RX = "|".join(re.escape(k) for k in sorted(SUB81, key=len, reverse=True))


@F.rule(r"(?:(?P<c>kusalena|akusalena) cittena samuṭṭhit(?:aṃ|o|ā) )?(?P<s>" + _SUBS_RX + r")(?P<p>(?: " + _PRED_RX
        + r")*)")
def _r_81(m):
    """(A)kusalena cittena samuṭṭhitaṃ S (P1 P2 …): «(အ)ကုသိုလ် စိတ်ကြောင့် ဖြစ်ပေါ်သော Sသည် P1၊ P2 … အရာ»."""
    if not m["c"] and not m["p"]:
        return None
    pre = f"{'ကုသိုလ်' if m['c'] == 'kusalena' else 'အကုသိုလ်'} စိတ်ကြောင့် ဖြစ်ပေါ်သော " if m["c"] else ""
    subj = pre + SUB81[m["s"]]
    preds = re.findall(r"(akusal|abyākat|kusal|sārammaṇ|anārammaṇ|phassavippayutt)", m["p"])
    if not preds:
        return FR(subj)
    out = []
    for i, pr in enumerate(preds):
        w = PRED81[pr]
        if pr in ("kusal", "akusal") and i == len(preds) - 1:
            out.append(w)
        elif pr in ("kusal", "akusal"):
            out.append(w + " ဖြစ်သော")
        else:
            out.append(w)
    body = "၊ ".join(out)
    if preds[-1] in ("kusal", "akusal"):
        return V(f"{subj}သည် {body}")
    return V(f"{subj}သည် {body} အရာ")


for _d in ("pathavīdhātu", "āpodhātu", "tejodhātu"):
    P(_d, FR(SUB81[_d])) if not has(_d) else None
new("kusalena cittena samuṭṭhitaṃ X", "ကုသိုလ် စိတ်ကြောင့် ဖြစ်ပေါ်သော X")
for _c, _cm in (("kusalena", "ကုသိုလ်"), ("akusalena", "အကုသိုလ်")):
    _e = _c[:-len("ena")]
    P(f"yaṃ kiñci {_c} cittena samuṭṭhitaṃ rūpaṃ sabbaṃ taṃ {_e}aṃ",
      V(f"{_cm} စိတ်ကြောင့် ဖြစ်ပေါ်သော {F.RUPA.my} မှန်သမျှ ထိုအားလုံးသည် {_cm}"))
P("yathā kāyakammaṃ tathā vacīkammaṃ", V(f"{KK}ကဲ့သို့ {VK}သည် ထိုနည်းတူ"))
for _s, _sm in (("rūpaṃ", F.RUPA.my), ("kāyakammaṃ vacīkammaṃ", f"{KK}၊ {VK}"), ("cakkhāyatanaṃ", AYN["cakkhāyatanaṃ"])):
    P(f"{_s} kusalampi akusalampi", V(f"{_sm}သည် ကုသိုလ်လည်း ဖြစ် အကုသိုလ်လည်း"))   # harmonise A4: no «၊» added
P("vāyodhātu asuci assu lohitaṃ sedo kusalopi akusalopi",
  V(f"{SUB81['vāyodhātu asuci assu lohitaṃ sedo']}သည် ကုသိုလ်လည်း ဖြစ်၏၊ အကုသိုလ်လည်း"))
for _k, _km in (("kāyo", F.KAYA), ("mano", "မနော"), ("kāyakammaṃ", KK), ("manokammaṃ", MK_)):
    P(f"{_k} rūpaṃ", V(f"{_km}သည် {F.RUPA.my}"))
    P(f"{_k} arūpaṃ", V(f"{_km}သည် {F.RUPA.my} မဟုတ်သော အရာ"))
for _a, _b, _am, _bm in (("cakkhāyatanaṃ", "cakkhuviññāṇaṃ", AYN["cakkhāyatanaṃ"], "မျက်စိ သိစိတ်"),
                         ("sotāyatanaṃ", "sotaviññāṇaṃ", AYN["sotāyatanaṃ"], "နား သိစိတ်"),
                         ("ghānāyatanaṃ", "ghānaviññāṇaṃ", AYN["ghānāyatanaṃ"], "နှာခေါင်း သိစိတ်"),
                         ("jivhāyatanaṃ", "jivhāviññāṇaṃ", AYN["jivhāyatanaṃ"], "လျှာ သိစိတ်"),
                         ("kāyāyatanaṃ", "kāyaviññāṇaṃ", AYN["kāyāyatanaṃ"], "ကိုယ် သိစိတ်")):
    P(f"{_a} rūpaṃ", V(f"{_am}သည် {F.RUPA.my}"))
    P(f"{_b} rūpaṃ", V(f"{_bm}သည် {F.RUPA.my}"))
P("rūpaṃ kammaṃ", V(f"{F.RUPA.my}သည် {F.KAMMA}"))
S('Nanu vuttaṃ bhagavatā – "cetanāhaṃ, bhikkhave, kammaṃ vadāmi; cetayitvā kammaṃ karoti kāyena vācāya manasā"ti!',
  f"{F.VUTTA_PRE}သည် မဟုတ်လော – “{_R} ငါသည် စေ့ဆော်မှုကို {F.KAMMA}ဟု ဆို၏၊ စေ့ဆော်ပြီး၍ ကိုယ်ဖြင့်၊ နှုတ်ဖြင့်၊ "
  f"မနောဖြင့် {F.KAMMA}ကို ပြု၏” ⟦b⟧{END}")
_AJ = "မိမိ၌ ချမ်းသာ ဆင်းရဲ ဖြစ်ပေါ်၏"
S('Nanu vuttaṃ bhagavatā – "kāye vā, ānanda, sati kāyasañcetanāhetu uppajjati ajjhattaṃ sukhadukkhaṃ; vācāya vā, '
  'ānanda, sati vacīsañcetanāhetu uppajjati ajjhattaṃ sukhadukkhaṃ; mane vā, ānanda, sati manosañcetanāhetu '
  'uppajjati ajjhattaṃ sukhadukkha"nti!',
  f"{F.VUTTA_PRE}သည် မဟုတ်လော – “အာနန္ဒာ ⟦b⟧၊ ကိုယ် ရှိသော် ကိုယ်ဖြင့် စေ့ဆော်မှုကြောင့် {_AJ}၊ အာနန္ဒာ ⟦b⟧၊ နှုတ် ရှိသော် "
  f"နှုတ်ဖြင့် စေ့ဆော်မှုကြောင့် {_AJ}၊ အာနန္ဒာ ⟦b⟧၊ မနော ရှိသော် မနောဖြင့် စေ့ဆော်မှုကြောင့် {_AJ}” ⟦b⟧{END}")
BR_X["[hānanda (saṃ. ni. 2.25)]"] = f"[ပါဌ်ကွဲ ({F.REF['saṃ. ni.']} 2.25): hānanda]"
_TV3 = {"tividhā": F.NUM_MY[3], "catubbidhā": F.NUM_MY[4]}
_SC = [("tividhā", "ကိုယ်", "akusalaṃ", KK, "dukkh"), ("catubbidhā", "နှုတ်", "akusalaṃ", VK, "dukkh"),
       ("tividhā", "မနော", "akusalaṃ", MK_, "dukkh"), ("tividhā", "ကိုယ်", "kusalaṃ", KK, "sukh"),
       ("catubbidhā", "နှုတ်", "kusalaṃ", VK, "sukh"), ("tividhā", "မနော", "kusalaṃ", MK_, "sukh")]
_SCM = []
for _n, _b, _q, _km, _f in _SC:
    _qm = "အကုသိုလ်" if _q == "akusalaṃ" else "ကုသိုလ်"
    _fm = "ဆင်းရဲကို ဖြစ်ပေါ်စေသော၊ ဆင်းရဲသော အကျိုး ရှိသော" if _f == "dukkh" else "ချမ်းသာကို ဖြစ်ပေါ်စေသော၊ ချမ်းသာသော အကျိုး ရှိသော"
    _SCM.append(f"{_R} {_TV3[_n]}မျိုးသော {_b}ဖြင့် စေ့ဆော်မှုသည် {_fm} {_qm} {_km} ဖြစ်၏")
S('Nanu vuttaṃ bhagavatā – "tividhā, bhikkhave, kāyasañcetanā akusalaṃ kāyakammaṃ dukkhudrayaṃ dukkhavipākaṃ; '
  'catubbidhā, bhikkhave, vacīsañcetanā akusalaṃ vacīkammaṃ dukkhudrayaṃ dukkhavipākaṃ; tividhā, bhikkhave, '
  'manosañcetanā akusalaṃ manokammaṃ dukkhudrayaṃ dukkhavipākaṃ; tividhā, bhikkhave, kāyasañcetanā kusalaṃ '
  'kāyakammaṃ sukhudrayaṃ sukhavipākaṃ; catubbidhā, bhikkhave, vacīsañcetanā kusalaṃ vacīkammaṃ sukhudrayaṃ '
  'sukhavipākaṃ; tividhā, bhikkhave, manosañcetanā kusalaṃ manokammaṃ sukhudrayaṃ sukhavipāka"nti!',
  f"{F.VUTTA_PRE}သည် မဟုတ်လော – “" + "၊ ".join(_SCM) + f"” ⟦b⟧{END}")
BR_X["[a. ni. 10.217 thokaṃ pana visadisaṃ]"] = f"[{F.REF['a. ni.']} 10.217၊ သို့သော် အနည်းငယ် ကွဲပြားသည်]"
_SAM = ("ငါ့ရှင် ပါဋလိပုတ္တ၊ စေ့ဆော်၍ ကိုယ်ဖြင့်၊ နှုတ်ဖြင့်၊ မနောဖြင့် {k}ကို ပြုပြီးလျှင် ထိုသူသည် {v}ကို ခံစား၏")
_SV3 = [_SAM.format(k=F.KAMMA, v=v) for v in ("သာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော ချမ်းသာ",
                                              "နာကျင်သော ခံစားမှုကို ဖြစ်စေတတ်သော ဆင်းရဲ",
                                              "မနာကျင် မသာယာသော ခံစားမှုကို ဖြစ်စေတတ်သော မနာကျင် မသာယာမှု")]
S('Nanu vuttaṃ bhagavatā – "sacāyaṃ, ānanda, samiddhi moghapuriso pāṭaliputtassa paribbājakassa evaṃ puṭṭho evaṃ '
  'byākareyya – ‘sañcetaniyaṃ, āvuso pāṭaliputta, kammaṃ katvā kāyena vācāya manasā sukhavedaniyaṃ sukhaṃ so '
  'vedayati; sañcetaniyaṃ, āvuso pāṭaliputta, kammaṃ katvā kāyena vācāya manasā dukkhavedaniyaṃ dukkhaṃ so '
  'vedayati; sañcetaniyaṃ, āvuso pāṭaliputta, kammaṃ katvā kāyena vācāya manasā adukkhamasukhavedaniyaṃ '
  'adukkhamasukhaṃ so vedayatī’ti, evaṃ byākaramāno kho, ānanda, samiddhi moghapuriso pāṭaliputtassa paribbājakassa '
  'sammā byākaramāno byākareyyā"ti!',
  f"{F.VUTTA_PRE}သည် မဟုတ်လော – “အာနန္ဒာ၊ အကယ်၍ ဤအချည်းနှီးသော ယောကျ်ား သမိဒ္ဓိသည် ပါဋလိပုတ္တ ⟦b⟧ ပရိဗ္ဗာဇ်က "
  "ဤသို့ မေးအပ်သည်ရှိသော် ဤသို့ ဖြေဆိုရာ၏ – ‘" + "၊ ".join(_SV3) + "’ဟူ၍၊ အာနန္ဒာ၊ ဤသို့ ဖြေဆိုသော "
  "အချည်းနှီးသော ယောကျ်ား သမိဒ္ဓိသည် ပါဋလိပုတ္တ ပရိဗ္ဗာဇ်အား မှန်ကန်စွာ ဖြေဆိုသည် ဖြစ်ရာ၏” ⟦b⟧" + END)
VAR_X["potaliputtassa"] = F.PATHA
BR_X["[potaliputtassa (ma. ni. 3.300)]"] = f"[ပါဌ်ကွဲ ({F.REF['ma. ni.']} 3.300): potaliputtassa]"

# ------------------------------------------------------------------------------------- 82. Jīvitindriyakathā
JIV = F.INDRIYA["jīvitindriya"].my                                    # «အသက်၏ စွမ်းရည်»
RJIV = new("rūpajīvitindriyaṃ / arūpajīvitindriyaṃ", f"ရုပ် {JIV}")
ARJIV = f"{ARUPI} {JIV}"
new("arūpajīvitindriyaṃ", ARJIV)
section("(82) 10. Jīvitindriyakathā", f"(82) 10. {JIV}အကြောင်း {KATHA}")
section("Jīvitindriyakathā", f"{JIV}အကြောင်း {KATHA}")
_AYU = W("1", "^1-19", "arūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā",
         "သက်တမ်း၊ တည်တံ့ခြင်း၊ ဆက်လက် ဖြစ်နေခြင်း၊ ဆက်လက် ရှင်သန်စေခြင်း၊ လှုပ်ရှားခြင်း") + \
    "၊ လည်ပတ်ခြင်း၊ စောင့်ရှောက်ခြင်း"
_DH2 = {"rūpīnaṃ": f"{RUPI} သဘောတရားတို့၏", "arūpīnaṃ": f"{ARUPI} သဘောတရားတို့၏",
        "rūpīnañca arūpīnañca": f"{RUPI} သဘောတရားတို့၏လည်းကောင်း၊ {ARUPI} သဘောတရားတို့၏လည်းကောင်း"}
for _n, _neg in (("atthi", False), ("natthi", True)):
    P(f"{_n} rūpajīvitindriyaṃ", V(RJIV, EXIST, neg=_neg))
    P(f"{_n} arūpajīvitindriyaṃ", V(ARJIV, EXIST, neg=_neg))
    for _d in ("rūpīnaṃ", "arūpīnaṃ"):
        P(f"{_n} {_d} dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā", V(f"{_DH2[_d]} {_AYU}", EXIST, neg=_neg))
for _d, _dm in _DH2.items():
    P(f"{_d} dhammānaṃ āyu", FR(f"{_dm} သက်တမ်းသည်"))
    for _j, _jm in (("rūpajīvitindriyaṃ", RJIV), ("arūpajīvitindriyaṃ", ARJIV)):
        P(f"{_d} dhammānaṃ āyu {_j}", V(f"{_dm} သက်တမ်းသည် {_jm}"))
        P(f"{_d} dhammānaṃ āyu na vattabbaṃ – {_j}", SAYQ(f"{_dm} သက်တမ်းကို", f"«{_jm}»ဟု", neg=True))
NSP = f"{NSM}ကို ဝင်စားနေသူ၌"
for _x, _xm in (("nirodhaṃ samāpannassa", NSP), ("asaññasattānaṃ", f"{P11_ASAT}တို့၌")):
    for _n, _neg in (("atthi", False), ("natthi", True)):
        P(f"{_x} {_n} jīvitindriyaṃ", V(f"{_xm} {JIV}", EXIST, neg=_neg))
    for _k in ("saṅkhārakkhandho", "vedanākkhandho", "viññāṇakkhandho"):
        P(f"{_x} atthi {_k}", V(f"{_xm} {KH[_k]}", EXIST))
for _k in ("saññākkhandho",):
    pass
S("Katamakkhandhapariyāpannanti?", f"အဘယ် {F.KHANDHA_W}၌ အကျုံးဝင်သနည်း{END}")
S("Saṅkhārakkhandhapariyāpannanti.", f"{KH['saṅkhārakkhandho']}၌ အကျုံးဝင်သည်{END}")
P("na nirodhaṃ samāpanno", V(f"{NSM}ကို ဝင်စားနေသူ", neg=True))
P("pañcavokārabhavo", V(P11.TOK["pañcavokārabhavo"])) if not has("pañcavokārabhavo") else None
UPC = P11.UPC                                                         # «ပြန်လည် ဖြစ်ပေါ်ခြင်းကို ရှာသော စိတ်»
for _s, _sm, _e in (("jīvitindriyaṃ", JIV, "aṃ"), ("phasso", NOM["phasso"], "o")):
    _pre = f"{UPC}ကြောင့် ဖြစ်ပေါ်သော {_sm}သည် {UPC} ပျက်နေစဉ်"
    _sam = "samuṭṭhitaṃ" if _e == "aṃ" else "samuṭṭhito"
    P(f"upapattesiyena cittena {_sam} {_s} upapattesiye citte bhijjamāne ekades{_e} bhijjati",
      Cl(f"{_pre} {P11.EK}", "ပျက်", "မပျက်"))
    P(f"upapattesiyena cittena {_sam} {_s} upapattesiye citte bhijjamāne anavases{_e} bhijjati",
      Cl(f"{_pre} အကြွင်းမဲ့", "ပျက်", "မပျက်"))
P("dve jīvitindriyāni", V(f"{JIV} {F.NUM_MY[2]}{F.CL}", EXIST))
P("dvīhi jīvitehi jīvati, dvīhi maraṇehi mīyati",
  Cl(f"အသက် {F.NUM_MY[2]}{F.CL}ဖြင့် အသက်ရှင်၏၊ သေခြင်း {F.NUM_MY[2]}{F.CL}ဖြင့်", "သေဆုံး", "မသေဆုံး"))
VAR_X["na hevaṃ vattabbe"] = F.PATHA

# ------------------------------------------------------------------------------------- 83. Kammahetukathā
section("(83) 11. Kammahetukathā", f"(83) 11. {F.KAMMA}ကြောင့်ဟူသော {KATHA}")
section("Kammahetukathā", f"{F.KAMMA}ကြောင့်ဟူသော {KATHA}")
_FALL = ("ဆုတ်ယုတ်", "မဆုတ်ယုတ်")
for _p, _pm, _f, _fm in (("arahā", ARAHA, "arahattā", ARAHATTA_N), ("sotāpanno", F.SOTAPANNA, "sotāpattiphalā",
                                                                    PFX["sotāpatti"]),
                         ("anāgāmī", F.ANAGAMI, "anāgāmiphalā", PFX["anāgāmi"])):
    for _n, _neg in (("", False), ("na ", True)):
        P(f"kammahetu {_p} {_f} {_n}parihāyati", Cl(f"{F.KAMMA}ကြောင့် {_pm}သည် {_fm}မှ", *_FALL, neg=_neg))
    P(f"arahantānaṃ abbhācikkhanakammassa hetu {_p} {_f} parihāyati",
      Cl(f"ရဟန္တာတို့ကို စွပ်စွဲ ပြောဆိုခြင်း {F.KAMMA}ကြောင့် {_pm}သည် {_fm}မှ", *_FALL)) if _p == "arahā" else None
for _n, _neg in (("", False), ("na ", True)):
    P(f"anāgāmī anāgāmiphalā {_n}parihāyati", Cl(f"{F.ANAGAMI}သည် {PFX['anāgāmi']}မှ", *_FALL, neg=_neg))
P("kammahetu sakadāgāmī", FR(f"{F.KAMMA}ကြောင့် {F.SAKADAGAMI}"))
_KH10 = [("pāṇātipāta", "သူ့အသက်ကို သတ်ခြင်း"), ("adinnādāna", "မပေးသည်ကို ယူခြင်း"),
         ("kāmesumicchācāra", "ကာမတို့၌ မှားယွင်းစွာ ကျင့်ခြင်း"), ("musāvāda", "မုသား ပြောခြင်း"),
         ("pisuṇavācā", "ကုန်းတိုက်သော စကား"), ("pharusavācā", "ကြမ်းတမ်းသော စကား"),
         ("samphappalāpa", "အကျိုးမဲ့ ပြိန်ဖျင်းသော စကား"), ("mātughāta", "အမိကို သတ်ခြင်း"),
         ("pitughāta", "အဖကို သတ်ခြင်း"), ("arahantaghāta", "ရဟန္တာကို သတ်ခြင်း"),
         ("ruhiruppāda", "ဘုရား၏ ကိုယ်တော်မှ သွေးကို ထွက်စေခြင်း"), ("saṅghabheda", "သံဃာကို သင်းခွဲခြင်း")]
W("2", "^2-?" if False else "^2-1", "", "") if False else None
for _k, _m in _KH10:
    P(f"{_k}kammassa hetu", V(f"{_m} {F.KAMMA}ကြောင့်"))
VAR_X.update({"mātughātakakammassa": F.PATHA, "mātughātikammassa": F.PATHA})
BR_X["[mātughātakakammassa (syā.), mātughātikammassa (ka.) tathā pitughātaarahantaghātakammassātipadesu]"] = (
    "[ပါဌ်ကွဲ (Syā.): mātughātakakammassa၊ (Ka.): mātughātikammassa၊ pitughāta-, arahantaghātakammassa "
    "ဟူသော ပုဒ်တို့၌လည်း ထို့အတူ]")
S("Katamassa kammassa hetūti?", f"အဘယ် {F.KAMMA}ကြောင့်နည်း{END}")
S("Handa hi arahantānaṃ abbhācikkhatīti.", f"ကောင်းပြီ၊ ရဟန္တာတို့ကို စွပ်စွဲ ပြောဆိုသောကြောင့်တည်း{END}")
P("ye keci arahantānaṃ abbhācikkhanti, sabbe te arahattaṃ sacchikaronti",
  Cl(f"ရဟန္တာတို့ကို စွပ်စွဲ ပြောဆိုကြသူ မှန်သမျှ ထိုသူ အားလုံးတို့သည် {ARAHATTA_N}ကို", "မျက်မှောက်ပြုကြ",
     "မျက်မှောက် မပြုကြ"))
LINES_X[key("Cha gatiyo, antarābhavo, pañceva kāmaguṇā kāmadhātu, pañceva āyatanā kāmā, rūpino dhammā rūpadhātu, "
            "arūpino dhammā arūpadhātu, saḷāyataniko attabhāvo rūpadhātuyā, atthi rūpaṃ arūpesu, rūpaṃ kammaṃ, "
            "rūpaṃ jīvitaṃ, kammahetukā parihāyatīti.")] = (
    f"{GATI} {F.NUM_MY[6]}{F.CL}၊ {ANTB}၊ {KGN} {F.NUM_MY[5]}{F.CL}သည်သာ ကာမဘုံ၊ {AY5}သည်သာ ကာမတို့၊ "
    f"{RUPI} သဘောတရားတို့သည် {RPD}၊ {ARUPI} သဘောတရားတို့သည် {ARPD}၊ {RPD}၌ {SAL}၊ {ARUPESU} {F.RUPA.my} {EXIST}ခြင်း၊ "
    f"{F.RUPA.my}သည် {F.KAMMA}၊ {F.RUPA.my}သည် အသက်၊ {F.KAMMA}ကြောင့် ဆုတ်ယုတ်ခြင်း{END}")


# ===================================================================================== new frames
@F.frame(r"(?P<h>[Hh])añci (?P<p>.+?)[,;] no vata re vattabbe – (?P<q>.+?)ti\.")
def _f_if_no(m):
    """Hañci P, no vata re vattabbe – "Q"ti. («ca» missing, ^5-429): the negative consequence of «no ca vata re»."""
    return F.if_my(m["p"], m["q"], neg=True) + END


before_generic()


@F.frame(r"(?P<t>[Tt])ena hi (?P<p>.+?)ti…\.?")
def _f_tenahi_pe(m):
    """Tena hi P-ti…pe…. (^5-443): «သို့ဖြစ်လျှင် P…»."""
    return f"{F.TENA_HI} {F.pq(m['p'], 'stmt')}{PE}"


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


def run(name, misses=False):
    """P6.run (harmonise A1 / A2: the post-pass «a verse line whose Pāli opens with «"» opens with «“»» is now a rule of
    my5_formulas.line_my, for every chapter)."""
    return P6.run(name, misses)


def main():
    args = sys.argv[1:]
    misses = "--misses" in args
    names = [a for a in args if a.endswith(".md")] or NAMES_OUT
    if "--q" in args:          # scratch lookup of the installed tables (writes nothing)
        rx = re.compile(args[args.index("--q") + 1])
        for k, v in F.PROP.items():
            if rx.search(k):
                try:
                    print("P", k, "=>", v.f("stmt"))
                except Exception as e:  # noqa: BLE001
                    print("P", k, "=> ERR", e)
        for d, n in ((F.SENT, "S"), (F.QUOTE, "Q"), (F.LINES, "L"), (F.HEAD, "H")):
            for k, v in d.items():
                if rx.search(k):
                    print(n, k[:150], "=>", str(v)[:200])
        return
    if "--try" in args:        # scratch: translate one Pāli line
        print(F.translate_line(args[args.index("--try") + 1]))
        return
    if "--skipped" in args:
        for k, v in SKIPPED.items():
            print("SKIP", k, "=>", v[:150])
        return
    if "--units" in args:
        for name in names:
            print("=====", name)
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
