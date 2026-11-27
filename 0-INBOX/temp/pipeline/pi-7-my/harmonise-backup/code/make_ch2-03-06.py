"""Burmese zero-shot of pi-7 2-03 dassanenapahātabbattika, 2-04 dassanenapahātabbahetukattika, 2-05 ācayagāmittika,
2-06 sekkhattika («အကြောင်းနှင့် အကျိုး ဆက်စပ်ပုံ»), from the Pāli only.

usage: python3 -I -X utf8 make_ch2-03-06.py [chapter ...] [--dev] [--regress] [--slips] [--out DIR]
  (no flag)  translate the chapters and write them; stops on the first unmatched sentence (nothing is guessed).
  --dev      do not stop: list every unmatched skeleton with its count in chk-ch2-03-06/dev.txt (nothing written).
  --regress  regenerate the approved sample (1-00, 1-02) and 1-01 in memory through the engines of this script and
             compare them with the published files (the sample must be identical; 1-01 may differ only at KNOWN_DIFF).

Engines (both read-only, imported, never run as scripts):
  * PRIMARY: my7_formulas + make_sample + make_ch1-01.py (its setup_*() frames register on import).
  * FALLBACK, per sentence unit: an ISOLATED copy of my7_formulas + make_sample with make_ch1-03-05.py loaded on it
    (its tables and wrappers act only on that copy). A unit that the primary engine cannot match is tried there,
    after make_ch1-03-05's own prep(). So a unit gets the Burmese of 1-01 where 1-01 has a frame for it, else the
    Burmese of 1-03 … 1-05.
  * This script's frames (the four triads, their names, notes and unique sentences) are registered on both.
No file of the sample or of another group is edited; every new string is logged in notes-ch2-03-06.md.
"""
import collections
import importlib
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
NAMES = ["2-03-dassanenapahatabbattika.md", "2-04-dassanenapahatabbahetukattika.md", "2-05-acayagamittika.md",
         "2-06-sekkhattika.md"]
CHK = HERE / "chk-ch2-03-06"
WCH = r"[\wāīūṃṅñṭḍṇḷ]"


def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, HERE / fn)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---- the fallback engine first, on its own copies of the shared modules
import my7_formulas as F  # noqa: E402
import make_sample as S  # noqa: E402,F401
_mods = {k: sys.modules.pop(k) for k in ("my7_formulas", "make_sample")}
FG = importlib.import_module("my7_formulas")
SG = importlib.import_module("make_sample")
G = _load("ch10305", "make_ch1-03-05.py")
sys.modules.update(_mods)
assert G.F is FG and FG is not F
# ---- the primary engine
K = _load("ch101", "make_ch1-01.py")
assert K.F is F
C, END, PE, W = F.C, F.END, F.PE, F.W

NEW = collections.OrderedDict()     # every new string of this script: Pāli -> Burmese


def new(pali, my):
    NEW.setdefault(pali, my)
    return my


# ===================================================================================== the four triads (pi-1 final)
def _tw(pali, my, bid):
    """a pi-1 Mātikā term, read from the FINAL rails (attributive form, without « သဘောတရားများ»)"""
    return W(pali, my + " သဘောတရားများ", "1", bid)


_DPS = W("dassanena pahātabbā dhammā", "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့်", "1", "^1-M1-8")
_BPS = W("bhāvanāya pahātabbā dhammā", "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့်", "1", "^1-M1-8")
TRIADS_ADD = {
    "dassana": {
        "dassanena pahātabb": _DPS,
        "bhāvanāya pahātabb": _BPS,
        "nevadassanena nabhāvanāya pahātabb": W(
            "neva dassanena na bhāvanāya pahātabbā dhammā",
            "သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည် မဟုတ်၊ ဘာဝနာ ပွားများခြင်းဖြင့်လည်း ပယ်ရမည် မဟုတ်သော", "1", "^1-M1-8"),
    },
    "dassanahetu": {
        "dassanena pahātabbahetuk": W("dassanena pahātabbahetukā dhammā",
                                      "သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော", "1", "^1-M1-9"),
        "bhāvanāya pahātabbahetuk": W("bhāvanāya pahātabbahetukā dhammā",
                                      "ဘာဝနာ ပွားများခြင်းဖြင့် ပယ်ရမည့် အမြစ် ရှိသော", "1", "^1-M1-9"),
        "nevadassanena nabhāvanāya pahātabbahetuk": W(
            "neva dassanena na bhāvanāya pahātabbahetukā dhammā",
            "သစ္စာကို မြင်ခြင်းဖြင့်လည်း ပယ်ရမည့် အမြစ် ရှိသည် မဟုတ်၊ ဘာဝနာ ပွားများခြင်းဖြင့်လည်း ပယ်ရမည့် အမြစ် "
            "ရှိသည် မဟုတ်သော", "1", "^1-M1-9"),
    },
    "acaya": {
        "ācayagām": W("ācayagāmino dhammā", "စုပုံခြင်းဆီသို့ ဦးတည်သော", "1", "^1-M1-10"),
        "apacayagām": W("apacayagāmino dhammā", "လျော့ပါးခြင်းဆီသို့ ဦးတည်သော", "1", "^1-M1-10"),
        "nevācayagāmināpacayagām": W("nevācayagāmināpacayagāmino",
                                     "စုပုံခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်၊ လျော့ပါးခြင်းဆီသို့ ဦးတည်သည်လည်း မဟုတ်သော",
                                     "1", "^1-M1-10"),
    },
    "sekkha": {
        "sekkh": W("sekkhā dhammā", "ကျင့်ကြံဆဲသူ၏", "1", "^1-M1-11"),
        "asekkh": W("asekkhā dhammā", "ကျင့်ကြံမှု ပြီးဆုံးသူ၏", "1", "^1-M1-11"),
        "nevasekkhanāsekkh": W("nevasekkhanāsekkhā", "ကျင့်ကြံဆဲသူ၏လည်း မဟုတ်၊ ကျင့်ကြံမှု ပြီးဆုံးသူ၏လည်း မဟုတ်သော",
                               "1", "^1-M1-11"),
    },
}
# chapter -> its triad (only the chapter's own triad is active while it is translated: the 2-03 stems are a prefix
# of the 2-04 stems)
CH_TRIAD = {NAMES[0]: "dassana", NAMES[1]: "dassanahetu", NAMES[2]: "acaya", NAMES[3]: "sekkha"}
_END = G._END.replace("|āni|", "|āni|ena|")         # a-stem endings (1-03 … 1-05) + instrumental


# a term cut short by «…» («bhāvanāya…», «nevadassanena nabhāvanāya…»): the Pāli abbreviates the same term, so it
# gets the full term (the «…» follows)
CUT = {"dassana": {"nevadassanena nabhāvanāya": "nevadassanena nabhāvanāya pahātabb", "nevadassanena":
                   "nevadassanena nabhāvanāya pahātabb", "bhāvanāya": "bhāvanāya pahātabb"},
       "dassanahetu": {"nevadassanena nabhāvanāya": "nevadassanena nabhāvanāya pahātabbahetuk",
                       "nevadassanena": "nevadassanena nabhāvanāya pahātabbahetuk",
                       "bhāvanāya": "bhāvanāya pahātabbahetuk"}}


def set_triad(mod, tri):
    for t in list(mod.TRIADS):
        if t in TRIADS_ADD or t.endswith("_cut"):
            mod.TRIADS.pop(t, None)
            mod.TRIAD_END.pop(t, None)
    if tri:
        mod.TRIADS[tri] = TRIADS_ADD[tri]
        mod.TRIAD_END[tri] = _END
        if tri in CUT:
            mod.TRIADS[tri + "_cut"] = {k: TRIADS_ADD[tri][v] for k, v in CUT[tri].items()}
            mod.TRIAD_END[tri + "_cut"] = r"(?=…|\s*$)"
    mod.rebuild()


# ===================================================================================== Pāli preparation (in memory)
# The ācayagāmī triad is an -in stem; its endings are read as the a-stem endings that the frames know (the Burmese of
# a term does not depend on its ending; the noun carries number and case): ī -> o, iṃ -> aṃ, issa -> assa,
# iñca -> añca, īnaṃ -> ānaṃ, iyā -> āya, i-cittasamaṅgissa -> a-cittasamaṅgissa (logged). Variants in braces keep
# their Pāli untouched.
_IN = {"ī": "o", "iṃ": "aṃ", "issa": "assa", "iñca": "añca", "īnaṃ": "ānaṃ", "iyā": "āya", "ino": "ā",
       "icittasamaṅgissa": "acittasamaṅgissa"}
_IN_RE = re.compile(r"(?<!" + WCH + r")((?:[Nn]evācayagāmināpacayagām|[Aa]pacayagām|[Āā]cayagām))("
                    + "|".join(sorted(_IN, key=len, reverse=True)) + r")(?!" + WCH + ")")
SLIP_FIX = {   # source slips: read as the usual form (logged); the Burmese is that of the usual form
    "Nevācayagāmīnāpacayagāmī": "Nevācayagāmināpacayagāmī",
    "aññamaññe sattārasa nissaye": "aññamaññe sattarasa, nissaye",
    "utusamuṭṭhāna…": "utusamuṭṭhānaṃ…",
    "Natthivigatāvigatapaccayā": "Natthi-vigatāvigatapaccayā",
    "maggapaccaya…": "maggapaccayā…",
    "aññamaññapaccaya…": "aññamaññapaccayā…",
    "upanissayapaccayena paccaya –": "upanissayapaccayena paccayo –",
    # a link word missing (supplied from the section: paccayavāra «paccayā», saṃsaṭṭhavāra «saṃsaṭṭho»)
    "Nevadassanena nabhāvanāya pahātabbahetukaṃ dhammaṃ nevadassanena nabhāvanāya pahātabbahetuko dhammo uppajjati "
    "vippayuttapaccayā": "Nevadassanena nabhāvanāya pahātabbahetukaṃ dhammaṃ paccayā nevadassanena nabhāvanāya "
    "pahātabbahetuko dhammo uppajjati vippayuttapaccayā",
    "Bhāvanāya pahātabbahetukañca nevadassanena nabhāvanāya pahātabbahetukañca dhammaṃ bhāvanāya pahātabbahetuko dhammo "
    "uppajjati hetupaccayā": "Bhāvanāya pahātabbahetukañca nevadassanena nabhāvanāya pahātabbahetukañca dhammaṃ "
    "saṃsaṭṭho bhāvanāya pahātabbahetuko dhammo uppajjati hetupaccayā",
}


_STEMS_RX = "|".join(f"[{k[0].upper()}{k[0]}]" + re.escape(k[1:]) for tab in TRIADS_ADD.values()
                     for k in sorted(tab, key=len, reverse=True))


def _outside_braces(text, fn):
    parts = re.split(r"(\{[^{}]*\})", text)
    return "".join(p if p.startswith("{") else fn(p) for p in parts)


def prep(text):
    def fix(t):
        for a, b in SLIP_FIX.items():
            if a in t:
                F.SLIPS.add(f"«{a}» read as «{b}»")
                t = t.replace(a, b)
        t = _IN_RE.sub(lambda m: m[1] + _IN[m[2]], t)
        t = re.sub(r"(?<= khandhā) (?=moho ca(?![\wāīūṃṅñṭḍṇḷ]))", " ca ", t)
        t = re.sub(r"(?<= khandhānaṃ) (?=mohassa ca(?![\wāīūṃṅñṭḍṇḷ]))", " ca ", t)
        t = re.sub(r"(?<= āvajjanāya) (?=mohassa ca(?![\wāīūṃṅñṭḍṇḷ]))", " ca ", t)
        # «X-ādhipati» = «X-o adhipati» (the term qualifies the noun adhipati, as 1-03 … 1-05 «vipāko adhipati»)
        return re.sub(r"(?<![\wāīūṃṅñṭḍṇḷ])(" + _STEMS_RX + r")ādhipati(?![\wāīūṃṅñṭḍṇḷ])", r"\1o adhipati", t)
    return _outside_braces(text, fix)


# ===================================================================================== numbers
NUM_ADD = {"ekavīsa": (21, "နှစ်ဆယ့်တစ်")}          # short form of ekavīsati (1-03 … 1-05 «နှစ်ဆယ့်တစ်ခု»)


def setup_numbers(mod):
    for w, (n, my) in NUM_ADD.items():
        mod.COUNT.setdefault(w, my + "ခု")
        mod.COUNT_VAL.setdefault(w, n)
    mod._CNT_ALT = "|".join(sorted(mod.COUNT, key=len, reverse=True))
    mod.COUNT_RE = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])(?P<neg>[Nn]a|[Nn]o)?(?P<loc>(?i:" + mod._LOC_ALT + r")) (?P<num>"
                              + mod._CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])")


# ===================================================================================== chapter names
TIKA_ADD = {   # NEW (built like the pi-2 names: the key notion of the first term + «သုံးမျိုးတွဲ»)
    "Dassanenapahātabbattikaṃ": new("Dassanenapahātabbattikaṃ", f"သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ခြင်း {F.TIKA}"),
    "Dassanenapahātabbahetukattikaṃ": new("Dassanenapahātabbahetukattikaṃ",
                                          f"သစ္စာကို မြင်ခြင်းဖြင့် ပယ်ရမည့် အမြစ် {F.TIKA}"),
    "Ācayagāmittikaṃ": new("Ācayagāmittikaṃ", f"စုပုံခြင်းဆီသို့ ဦးတည်ခြင်း {F.TIKA}"),
    "Sekkhattikaṃ": new("Sekkhattikaṃ", f"ကျင့်ကြံဆဲသူ {F.TIKA}"),
}
# the triads as named inside the notes («dassanattika-», «kusalattike»)
TIKA_REF = {"dassanattik": TIKA_ADD["Dassanenapahātabbattikaṃ"], "kusalattik": S.KT}


def setup_names():
    F.TIKA_NAME.update(TIKA_ADD)
    for p, my in TIKA_ADD.items():
        F.HLINES[f"{p} niṭṭhitaṃ."] = F.finished(my)


# ===================================================================================== editorial notes
# Words of the notes (NEW unless marked); the shared ones come from make_ch1-01 (K) / make_ch1-03-05 (G) / the sample.
EVAM_THUS = new("evaṃ (alone: thus)", "ဤသို့")                 # as G «evaṃ kātūna» «ဤသို့ ပြု၍»
GANETABBA, KATABBA, VITTH = K.GANETABBA, K.KATABBA, K.VITTH
VIBHAJ = G.VIBHAJ                                                # «ခွဲခြမ်းစိတ်ဖြာရမည်» (1-03 … 1-05)
PANHA = K.PANHA                                                  # «ပြဿနာ»
NATTHI, ATTHI = K.NATTHI, K.ATTHI
PARIPUNNA = K.PARIPUNNA                                          # «ပြည့်စုံ»
ANUMAJJ = new("anumajjantena", "ပြန်လည် စိစစ်လျက်")
NATVA = new("ñatvā", "နားလည်၍")
VISUM = new("visuṃ", "သီးခြား")
NAYENA = new("X-nayena", "၏ နည်းအတိုင်း")
DASSITA = new("dassitanayena", "ပြထားသော နည်းအတိုင်း")
GAMANA = new("gamanaṃ", "သွားပုံ")
SABBE = new("sabbe / sabbepi (all)", "အားလုံး")
MAHABHUTA = F.NOUN["mahābhūtā"][0]
UPADHAR = new("upadhāretvā", "သေချာ စဉ်းစား၍")
LIKHITA_NEG = new("na likhitā", "မရေးထားသော")
PALIYAM = new("pāḷiyaṃ", "ပါဠိတော်၌")


def _cnt(w):
    w = {"ekā": "ekaṃ", "tisso": "tīṇi", "dvepi": "dve"}.get(w, w)
    return F.COUNT[w]


TERM_REF = {}       # per chapter: «dassanena» / «sekkha» / «ācayagāmi» … = a term named inside a note (term + dhamma)


def term_ref(w):
    if w in TERM_REF:
        return TERM_REF[w]
    raise KeyError("term ref: " + w)


def sadisa_name(x):
    """the model of an «X-sadisaṃ» note: condition (bare / -paccaya / -mūlaka), section, triad, term"""
    m = re.fullmatch(r"(na|no)?(" + K.STEM_RX + r")", x)
    if m:                                               # bare stem «anantarasadisaṃ» = N (as 1-03 … 1-05)
        return F.N[m[2]] + (" " + F.NOT + "ခြင်း" if m[1] else "")
    m = re.fullmatch(r"(paṭicca|sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta)vāra", x)
    if m:
        return K.vara(m[1])
    m = re.fullmatch(r"(paṭicca|sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta)vārapaccanīye (na|no)?(\w+)", x)
    if m:
        return f"{K.vara(m[1])}၏ {K.ORDER_L['paccanīye']} " + sadisa_name((m[2] or "") + m[3])
    m = re.fullmatch(r"(\w+?)ttika", x)
    if m and m[1] + "ttik" in TIKA_REF:
        return TIKA_REF[m[1] + "ttik"]
    if x == "paccaya":                                  # «paccayasadiso» = the paccayavāra (short)
        return K.vara("paccaya")
    if x == "paccanīya":
        return "အငြင်းပြ ပုံစံ"
    if x in TERM_REF:
        return TERM_REF[x]
    return K.sadisa_x(x)


SAD_E = {"aṃ": F.SADISA, "o": F.SADISA, "ā": K.SADISANI, "āni": K.SADISANI}


def my_clause(t):
    """note clauses that make_ch1-01's note_clause() does not cover (t: lower-case first, «,» spaced)"""
    w = t.split()
    # [B] [L] X-sadisaṃ / X sadisaṃ [kātabbaṃ | vibhajitabbaṃ | gamanaṃ]
    m = re.fullmatch(r"(?:(?P<b>.+?) )?(?P<x>\S+?) ?sadis(?P<e>aṃ|o|ā|āni)(?: (?P<v>kātabbaṃ|kātabbo|vibhajitabbaṃ|"
                     r"gamanaṃ))?", t)
    if m:
        x = m["x"]
        pre = ""
        b = m["b"].split() if m["b"] else []
        if b and re.fullmatch(r"(paṭicca|sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta)vāre", b[-1]):
            pre = K.vara(b[-1][:-4]) + "၌ "
            b = b[:-1]
        elif b and b[-1] in ("kusalattike",):
            pre = S.KT + "၌ "
            b = b[:-1]
        elif b and b[-1] == "paṭiccavārapaccanīye":
            pre = f"{K.vara('paṭicca')}၏ {K.ORDER_L['paccanīye']} "
            b = b[:-1]
        if b == ["paripuṇṇaṃ"]:
            pre, b = pre + PARIPUNNA + "စွာ ", []
        nm = sadisa_name(x)
        if m["v"] == "gamanaṃ":
            return f"{GAMANA} {pre}{nm}{F.SADISA}"
        if m["v"] in ("kātabbaṃ", "kātabbo", "vibhajitabbaṃ"):
            v = KATABBA if m["v"].startswith("kāt") else VIBHAJ
            return (f"{obj_my(b)} " if b else "") + f"{pre}{nm}နှင့် တူအောင် {v}"
        return (f"{subj_my(b)} " if b else "") + f"{pre}{nm}{SAD_E[m['e']]}"
    # counts: «tīṇi» «satta pañhā» «dve pañhā kātabbā» «dve kātabbā» «X-mūlake tīṇi» «sekkhaghaṭanesu tīṇi»
    m = re.fullmatch(r"(?P<n>\w+)(?P<p> pañhā)?(?P<k> kātabbā)?(?P<d> dassitanayena)?", t)
    if m and (m["n"] in F.COUNT or m["n"] in ("ekā", "tisso", "dvepi")):
        c = _cnt(m["n"])
        core = f"{PANHA} {c}" if m["p"] else c
        if m["k"]:
            return (f"{DASSITA} " if m["d"] else "") + f"{core}ကို {KATABBA}"
        return core
    m = re.fullmatch(r"(?P<n>\w+) pañhā paripuṇṇā", t)
    if m and m["n"] in F.COUNT:
        return f"{PANHA} {F.COUNT[m['n']]} {PARIPUNNA}သည်"
    m = re.fullmatch(r"(?P<x>\w+) nayena (?P<v>kātabbaṃ|vibhajitabbā|vibhajitabbaṃ)", t)
    if m and m["x"] in TERM_REF:
        return f"{TERM_REF[m['x']]}{NAYENA} " + (KATABBA if m["v"] == "kātabbaṃ" else VIBHAJ)
    m = re.fullmatch(r"(?P<x>ācayagāmi)nayena kātabbaṃ", t)
    if m and m["x"] in TERM_REF:
        return f"{TERM_REF[m['x']]}{NAYENA} {KATABBA}"
    m = re.fullmatch(r"(?P<x>\w+?)(?P<k>mūlake|ghaṭanesu) (?P<n>\w+)", t)
    if m and m["n"] in F.COUNT:
        cw = None if m["x"] in TERM_REF else F._cond_word(m["x"])
        if m["x"] not in TERM_REF and cw is None:
            raise KeyError("mūlake: " + m["x"])
        nm = term_ref(m["x"]) if m["x"] in TERM_REF else F.cond(*F._swap(cw))
        place = f"{nm}{F.MULAKA}၌" if m["k"] == "mūlake" else f"{nm} {F.GHATANA}တို့၌"
        return f"{place} {F.COUNT[m['n']]}"
    return None


def subj_my(b):
    j = " ".join(b)
    if j in SUBJ:
        return SUBJ[j]
    return K.subj(b)


def obj_my(b):
    j = " ".join(b)
    if j in OBJ:
        return OBJ[j]
    return K.obj(b)


SUBJ = {"idampi": "ဤသည်လည်း", "avasesā": f"{K.AVASESA}တို့သည်", "idhāpi ghaṭanā": f"ဤနေရာ၌လည်း {F.GHATANA}တို့သည်"}
OBJ = {"imāni padāni": f"ဤ {F.PADA}တို့ကို", "nissayavāro": K.vara("nissaya") + "ကို"}
_K_CLAUSE = K.note_clause


def note_clause(t):
    try:
        r = _K_CLAUSE(t)
    except KeyError:
        r = None
    if r is None:
        r = my_clause(t)
    return r


def _notes():
    """hand-written note clauses (keys as make_ch1-01's note_body() sees them: lower-case first, «,» spaced)"""
    cn, cd = F.cname, F.cond
    vg = S.PH
    return {
        "evaṃ gaṇetabbaṃ": f"{EVAM_THUS} {GANETABBA}",
        "evaṃ anumajjantena gaṇetabbaṃ": f"{EVAM_THUS} {ANUMAJJ} {GANETABBA}",
        "imāni padāni anumajjantena anulomaṃ gaṇetabbaṃ": f"ဤ {F.PADA}တို့ကို {ANUMAJJ} အဟုတ်ပြ ပုံစံကို {GANETABBA}",
        "ñatvā gaṇetabbaṃ": f"{NATVA} {GANETABBA}",
        "paṭisandhi natthi": f"{F.PATISANDHI} {NATTHI}",
        "vipākapaṭisandhi natthi": f"{F.VIPAKA_ADJ} {F.PATISANDHI} {NATTHI}",
        "vipākañca": f"{F.N['vipāka']}လည်း",             # «(paṭisandhi natthi, vipākañca)»: elliptic as the Pāli
        "paṭisandhikkhaṇe natthi": f"{F.PATISANDHI} နေသော ခဏ၌ {NATTHI}",
        "paripuṇṇaṃ kātabbaṃ": f"{PARIPUNNA}အောင် {KATABBA}",
        "mahābhūtā kātabbā": f"{MAHABHUTA}တို့ကို {KATABBA}",
        "sabbe mahābhūtā kātabbā": f"{MAHABHUTA} {SABBE}ကို {KATABBA}",
        "sabbepi mahābhūtā kātabbā": f"{MAHABHUTA} {SABBE}ကိုလည်း {KATABBA}",
        "ekā pañhā sabbe mahābhūtā kātabbā": f"{PANHA} {F.COUNT['ekaṃ']}၊ {MAHABHUTA} {SABBE}ကို {KATABBA}",
        "imepi dve kātabbā": f"ဤ {F.COUNT['dve']}ကိုလည်း {KATABBA}",
        "dvepi kātabbā": f"{F.COUNT['dve']}လုံးကို {KATABBA}",
        "sabbāni padāni vitthāretabbāni tīṇi": f"{F.PADA} အားလုံးတို့ကို {VITTH} {F.COUNT['tīṇi']}",
        "cittasamuṭṭhānampi kaṭattārūpampi upādārūpampi natthi":
            (f"{FG.FIXED['cittasamuṭṭhānaṃ rūpaṃ'][0]}လည်း{C} {F.KATATTARUPA}လည်း{C} {FG.FIXED['upādārūpaṃ'][0]}လည်း "
             f"{NATTHI}"),
        "kusalattikasadisā satta pañhā": f"{S.KT}{K.SADISANI}{C} {PANHA} {F.COUNT['satta']}",
        "saṃkhittaṃ": F.NOTES["(saṃkhittaṃ)"][1:-1],
        "sabbe ghaṭanā kātabbā": f"{F.GHATANA} {SABBE}ကို {KATABBA}",
        "ghaṭanā paripuṇṇā": f"{F.GHATANA} {PARIPUNNA}သည်",
        "paṭisandhipi mahābhūtāpi sabbe": f"{F.PATISANDHI}လည်း{C} {MAHABHUTA}လည်း {SABBE}",
        "visuṃ ghaṭanā natthi": f"{VISUM} {F.GHATANA} {NATTHI}",
        "cattāripi hi visuṃ ghaṭanā natthi": f"{F.COUNT['cattāri']}လုံး၌ပင် {VISUM} {F.GHATANA} {NATTHI}",
        "ninnānaṃ": new("ninnānaṃ", "ကွဲပြားမှု မရှိ"),
        "pavattipaṭisandhi": new("pavattipaṭisandhi", f"ဘဝ ဖြစ်စဉ်၌လည်း၊ {F.PATISANDHI}၌လည်း"),
        "moho kātabbo": f"{F.LEX['moho'][0]}ကို {KATABBA}",
        "ime sahetukā kātabbā": f"ဤတို့ကို " + new("sahetukā (made with roots)", "အမြစ် ရှိသည်များ") + f"အဖြစ် {KATABBA}",
        "vitthāretabbaṃ dassanattikasadisaṃ": f"{TIKA_REF['dassanattik']}နှင့် တူအောင် {VITTH}",
        "āsevanamūlake vuṭṭhānassapi āvajjanāyapi pahātabbaṃ":
            (f"{cd('āsevana', 'n')}{F.MULAKA}၌ {F.LEX['vuṭṭhānassa'][0]}ကိုလည်း{C} {F.LEX['āvajjanāya'][0]}ကိုလည်း "
             + new("pahātabbaṃ (to be left out)", "ပယ်ရမည်")),
        '"uddhacca"nti niyāmetabbaṃ': f"“{F.LEX['uddhaccaṃ'][0]}”ဟု " + new("niyāmetabbaṃ", "သတ်မှတ်ရမည်"),
        "idha sahajātaṃ , purejātaṃ , missagataṃ atthi , pāḷiyaṃ kātabbaṃ":
            (f"ဤနေရာ၌ {F.N['sahajāta']}{C} {F.N['purejāta']}{C} " + new("missagataṃ", "ရောစပ်ချက်")
             + f" {ATTHI}သည်{C} {PALIYAM} {KATABBA}"),
        "gaṇanāya upadhāretvā gaṇetabbaṃ": f"{S.GANANA}၌ {UPADHAR} {GANETABBA}",
        "gaṇentena upadhāretvā gaṇetabbaṃ": new("gaṇentena", "ရေတွက်သူသည်") + f" {UPADHAR} {GANETABBA}",
        "idhāpi ārammaṇapaccayā upanissayapaccayā atthi , pāḷiyaṃ natthi":
            f"{G.YADV['idhāpi']} {cd('ārammaṇa', 'n')}{C} {cd('upanissaya', 'n')} {ATTHI}သည်{C} {PALIYAM} {NATTHI}",
        'idhāpi "sahajātaṃ , purejātaṃ" yaṃ missakapañhā atthi , pāḷiyaṃ kātabbaṃ':
            (f"{G.YADV['idhāpi']} “{F.N['sahajāta']}{C} {F.N['purejāta']}”ဟူသော {K.MISSAKA} {PANHA} {ATTHI}သည်{C} "
             f"{PALIYAM} {KATABBA}"),
        'idhāpi "sahajātaṃ , purejātaṃ" yaṃ missakapañhā atthi':
            f"{G.YADV['idhāpi']} “{F.N['sahajāta']}{C} {F.N['purejāta']}”ဟူသော {K.MISSAKA} {PANHA} {ATTHI}သည်",
        "idhāpi ārammaṇaupanissayā atthi": f"{G.YADV['idhāpi']} {F.LEX['ārammaṇūpanissayo'][0]} {ATTHI}သည်",
        "idhāpi sahajātaṃ , purejātaṃ atthi": f"{G.YADV['idhāpi']} {F.N['sahajāta']}{C} {F.N['purejāta']} {ATTHI}သည်",
        "ye te pañhā na likhitā , te pāḷiyaṃ gaṇentānaṃ byañjanena na samenti":
            (f"{LIKHITA_NEG} ထို{PANHA}တို့သည် {PALIYAM} " + new("gaṇentānaṃ", "ရေတွက်သူတို့၏") + " "
             + new("byañjanena na samenti", "စကားလုံးနှင့် မညီကြ")),
        "te pāḷiyaṃ na likhitā gaṇanā pākaṭā honti":
            f"{PALIYAM} {LIKHITA_NEG} ထို{S.GANANA}တို့သည် " + new("pākaṭā honti", "ထင်ရှားကြသည်"),
        "yadi saṃsayo uppajjati , anulome atthipaccaye pekkhitabbaṃ":
            (new("yadi saṃsayo uppajjati", f"သံသယ {F.UP}ဆိုလျှင်") + f" {K.ORDER_L['anulome']} {cd('atthi', 'loc')} "
             + new("pekkhitabbaṃ", "ကြည့်ရမည်")),
        "sahajātapaccaye paṭiccavāre sahajātavārasadisā nava pañhā":
            f"{cd('sahajāta', 'loc')} {K.vara('paṭicca')}၌ {K.vara('sahajāta')}နှင့် တူသော {PANHA} {F.COUNT['nava']}",
        "aññamaññapaccaye paṭiccavāre aññamaññasadisaṃ tīṇi":
            f"{cd('aññamañña', 'loc')} {K.vara('paṭicca')}၌ {F.N['aññamañña']}နှင့် တူသော {F.COUNT['tīṇi']}",
        "nissayapaccaye paccayavāre nissayavārasadisaṃ":
            f"{cd('nissaya', 'loc')} {K.vara('paccaya')}၌ {K.vara('nissaya')}{F.SADISA}",
        "nissayapaccaye kusalattike nissayapaccayasadisaṃ":
            f"{cd('nissaya', 'loc')} {S.KT}၌ {cd('nissaya', 'n')}{F.SADISA}",
    }


NOTE_ADD = {}


def setup_notes():
    K.WORDS_N.setdefault("moho", F.NOUN["moho"][0])
    K.WORDS_N.setdefault("dassanattikaṃ", TIKA_REF["dassanattik"])
    NOTE_ADD.update(_notes())
    K.NOTE_FIXED.update(NOTE_ADD)
    K.note_clause = note_clause


def chapter_notes(name):
    """per chapter: the term named inside a note, and every note of the chapter registered for the chains
    (F.NOTES: a note between «…» or after a condition)"""
    tri = CH_TRIAD[name]
    t = TRIADS_ADD[tri]
    TERM_REF.clear()
    if tri in ("dassana", "dassanahetu"):
        first = list(t.values())[0]
        TERM_REF["dassanena"] = f"{first} {F.DHAMMA}"
    elif tri == "acaya":
        TERM_REF["ācayagāmi"] = f"{t['ācayagām']} {F.DHAMMA}"
    elif tri == "sekkha":
        TERM_REF.update({"sekkha": f"{t['sekkh']} {F.DHAMMA}", "asekkha": f"{t['asekkh']} {F.DHAMMA}",
                         "nevasekkhanāsekkha": f"{t['nevasekkhanāsekkh']} {F.DHAMMA}"})
    src = prep((PALI / name).read_text(encoding="utf-8-sig"))
    src = re.sub(r"\{[^{}]*\}", "", src)
    for m in re.finditer(r"\(([^()]*)\)", src):
        k = m[0]
        if re.fullmatch(r"\(\d+\)", k) or k in F.NOTES:
            continue
        r = K.note_unit(k)
        if r is not None:
            F.NOTES[k] = r
            FG.NOTES.setdefault(k, r)
        pieces = re.split(r"(?<=\.) (?=\S)", m[1])
        if len(pieces) > 1:                       # the closing piece starts a unit: «Ninnānaṃ)…» -> NOTES
            last = pieces[-1] + ")"
            r = K.note_unit(last)
            if r is not None:
                F.NOTES.setdefault(F.lc(last), r)
                FG.NOTES.setdefault(F.lc(last), r)


# ===================================================================================== counting lines: shared counts
# «anantare samanantare sahajāte aññamaññe dve» (one count for several conditions) and «kamme sabbattha tīṇi»:
# each condition in the locative, joined by «၊», then the count (and «နေရာတိုင်း၌» for sabbattha).
_K_CHAIN = None
_LOCW = None


def _run_tok(m):
    words = m[1].split()
    out = []
    for w in words:
        neg = bool(re.match(r"(?i)n[ao](?=" + F._LOC_ALT + ")", w)) and w.lower()[2:] in F.LOC2STEM
        lw = w.lower()[2:] if neg else w.lower()
        out.append(F.cond(F.LOC2STEM[lw], "loc", neg))
    return (C + " ").join(out)


def chain(s, slots, ci, ki, di, vi=None):
    try:
        return _K_CHAIN(s, slots, ci, ki, di, vi)
    except KeyError:
        pass
    loc = r"(?:(?:[Nn]a|[Nn]o)?(?:" + F._LOC_ALT + r"))"
    run_re = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ§])((?:" + loc + r" )+)(?=§K§|sabbattha (?:" + F._CNT_ALT + r")\b)")
    toks = {}

    def sub(m):
        k = f"\u0004R{len(toks)}\u0004"
        toks[k] = _run_tok(m) + " "
        return k
    s2 = run_re.sub(sub, s)
    s2 = re.sub(r"sabbattha (" + F._CNT_ALT + r")(?![\wāīūṃṅñṭḍṇḷ])",
                lambda m: f"\u0004S{m[1]}\u0004", s2)
    if s2 == s:
        raise KeyError("chain: " + s)
    for k in re.findall(r"\u0004S(\w+)\u0004", s2):
        toks[f"\u0004S{k}\u0004"] = f"{K.SABBATTHA} {F.COUNT[k]}"
    F.NOTES.update(toks)
    try:
        r = _K_CHAIN(s2, slots, ci, ki, di, vi)
    finally:
        for k in toks:
            F.NOTES.pop(k, None)
    return r


# ===================================================================================== lexicon, sentences, headings
CHANDARAGA = W("chandarāgo kāmo", "ဆန္ဒရာဂ", "2")
BHANDA = new("bhaṇḍa", "ပစ္စည်း")
SAKA, PARA = new("saka-", "မိမိ"), new("para-", "သူတစ်ပါး")
PARIGGAHA = W("pariggaho", "သိမ်းပိုက်ခြင်း", "2")
AJJHATTIKA = W("rūpaṃ ajjhattikaṃ", "အတွင်းပိုင်း ဖြစ်သော", "1")
PUBBE = F.LEX["pubbe samudāciṇṇe kilese"][0].split("က ")[0] + "က"          # «ရှေးက» (sample)
UPOSATHA = new("uposathakammaṃ", "ဥပုသ် စောင့်ထိန်းခြင်း")      # pi-2 «ဥပုသ်ကို စောင့်ထိန်း၍»
SK_ADD = {}
SKF_ADD = {}
HL_ADD = {}


# «asaññasattānaṃ»: 1-01 «အသညသတ်တို့၏» (genitive), 1-03 … 1-05 «အသညသတ်တို့၌»; one form inside these chapters: the
# primary engine's (1-01) genitive, also in the fallback copy (logged for the consistency pass)
ASANNA_G = F.PREFIX["asaññasattānaṃ"]


def setup_lex():
    FG.PREFIX["asaññasattānaṃ"] = ASANNA_G
    FG.LEX["asaññasattānaṃ"] = (ASANNA_G, "x")
    FG.SKF["asaññasattānaṃ"] = ASANNA_G
    G.ASANNA = ASANNA_G
    G.SKF["asaññasattānaṃ"] = ASANNA_G
    for mod in (F, FG):
        # 2-04: delusion accompanied by doubt / restlessness (pi-1 «ယုံမှားမှုနှင့်အတူ ဖြစ်သော မောဟ»)
        vic, udd = mod.QUAL["vicikicchāsahagato"], mod.QUAL["uddhaccasahagato"]
        for st, my in (("vicikicchāsahagat", vic), ("uddhaccasahagat", udd)):
            mod.add_qual(my, *[st + e for e in ("aṃ", "ā", "ānaṃ", "assa", "e", "o")])
        mod.add_qual(mod.QUAL["sampayuttakānaṃ"], "sampayuttakā")
        mod.add_qual(mod.QUAL["purimā purimā"], "purimo purimo")
        mod.add_qual(mod.QUAL["pacchimānaṃ pacchimānaṃ"], "pacchimassa pacchimassa")
        for st, my in (("vicikicchāsahagat", vic), ("uddhaccasahagat", udd)):
            for e in ("aṃ", "ā", "ānaṃ", "assa", "e", "o"):
                mod.LEX.setdefault(st + e, (my, "adj"))
        # coordinated items with delusion (each conjunct takes the marker, as the module's «Aလည်းကောင်း၊ Bလည်းကောင်း»)
        kh, mo, lk = mod.KHANDHA, mod.NOUN["moho"][0], mod.LAKAUNG
        sen = mod.NOUN["senāsanam"][0]
        for pk, my in (("khandhā ca moho ca", f"{kh}{lk}{C} {mo}{lk}"),
                       ("khandhe ca mohañca", f"{kh}တို့ကို{lk}{C} {mo}ကို{lk}"),
                       ("khandhānaṃ ca mohassa ca", f"{kh}တို့အား{lk}{C} {mo}အား{lk}"),
                       ("senāsanaṃ moho ca", f"{sen}{lk}{C} {mo}{lk}"),
                       ("āvajjanāya ca mohassa ca", f"{mod.LEX['āvajjanāya'][0]}အား{lk}{C} {mo}အား{lk}")):
            mod.LEX.setdefault(pk, (my, "x"))
        moha = mod.NOUN["moho"][0]
        mod.add_noun(moha, n=["moho"], a=["mohaṃ"], g=["mohassa"])
        mod.add_fixed(mod.KATATTARUPA, "g", True, "kaṭattārūpānaṃ")
        for w, my in mod.COUNT.items():                     # a bare count inside a fragment («… tīṇi (…)»)
            mod.LEX.setdefault(w, (my, "x"))
        mod.LEX.setdefault("pubbe", (PUBBE, "x"))
        mod.LEX.setdefault("uposathakammaṃ", (UPOSATHA, "na"))
        mod.LEX.setdefault("51anantarūpanissayo", ("51" + mod.LEX["anantarūpanissayo"][0], "n"))
        mod.LEX.setdefault("kāyikaṃ", (K.KAYIKA, "na"))      # «kāyikaṃ… sukhaṃ…» (the pair cut by «…»)
        mod.LEX.setdefault("sukhaṃ", (F.LEX["kāyikaṃ sukhaṃ"][0].split(" ", 1)[1] if "kāyikaṃ sukhaṃ" in F.LEX
                                      else "သာယာမှု", "na"))
    kab = F.FIXED["kabaḷīkāro §V§ āhāro"][0]
    sk = {
        "§T§o dhammo §T§assa dhammassa §C§ena paccayo (saṃkhittaṃ) kabaḷīkāro… satta pañhā… §C§ena paccayo… "
        "cakkhundriyañca… rūpajīvitindriyañca … satta pañhā §C§ena paccayo… §C§ena paccayo… §C§ena paccayo":
            (f"{{T1}} {F.DHAMMA}သည် {{T2}} {F.DHAMMA}အား {{C1.if}} {F.NOTES['(saṃkhittaṃ)']} {kab}… {PANHA} "
             f"{F.COUNT['satta']}… {{C2.if}}… {F.FIXED['cakkhundriyaṃ'][0]}{F.LAKAUNG}… "
             f"{F.FIXED['Rūpajīvitindriyaṃ'][0]}{F.LAKAUNG} … {PANHA} {F.COUNT['satta']} {{C3.if}}… {{C4.if}}… "
             f"{{C5.if}}"),
        "sakabhaṇḍe chandarāgo parabhaṇḍe chandarāgassa §C§ena paccayo":
            f"{SAKA} {BHANDA}၌ ဖြစ်သော {CHANDARAGA}သည် {PARA} {BHANDA}၌ ဖြစ်သော {CHANDARAGA}အား {{C1.if}}",
        "sakapariggahe chandarāgo parapariggahe chandarāgassa §C§ena paccayo":
            f"{SAKA} {PARIGGAHA}၌ ဖြစ်သော {CHANDARAGA}သည် {PARA} {PARIGGAHA}၌ ဖြစ်သော {CHANDARAGA}အား {{C1.if}}",
    }
    SK_ADD.update(sk)
    SKF_ADD.update({
        "purimā purimā §T§ā khandhā pacchimānaṃ pacchimānaṃ":
            f"{F.QUAL['purimā purimā']} {{T1}} {F.KHANDHA}တို့သည် {F.QUAL['pacchimānaṃ pacchimānaṃ']}",
        "ahetukaṃ §T§aṃ": f"{F.AHETUKA} {{T1}}",
        "§T§añca": f"{{T1}} {F.DHAMMA}နှင့်",                 # «X-añca… tīṇi» (the second term cut short)
        "ahetukaṃ ekaṃ": f"{F.AHETUKA} {F.PAA[1]}",
        "ahetukā §T§o": f"{F.AHETUKA} {{T1}}",
        "§T§aṃ (ekaṃ, paripuṇṇaṃ, §T§añca, §T§añca, ghaṭanā paripuṇṇā, dvepi kātabbā.":
            (f"{{T1}} ({F.COUNT['ekaṃ']}{C} {PARIPUNNA}သည်{C} {{T2}} {F.DHAMMA}{F.LAKAUNG}{C} {{T3}} {F.DHAMMA}"
             f"{F.LAKAUNG}{C} {F.GHATANA} {PARIPUNNA}သည်{C} {NOTE_ADD['dvepi kātabbā']}{F.END}"),
    })
    SK_ADD["uddhaccasahagate khandhe paṭicca moho ca cittasamuṭṭhānañca rūpaṃ"] = (
        f"{F.QUAL['uddhaccasahagate']} {F.KHANDHA}တို့ကို မှီ၍ {F.NOUN['moho'][0]}{F.LAKAUNG}{C} "
        f"{FG.FIXED['cittasamuṭṭhānaṃ rūpaṃ'][0]}{F.LAKAUNG}")
    for mod in (F, FG):
        mod.EDNOTES.update({
            "ācayagāmi (sī. syā.) evamuparipi": f"{mod.VAR_L} (Sī., Syā.): ācayagāmi{C} " + new(
                "evamuparipi", "နောက်တွင်လည်း ဤနည်းတူ"),           # pi-? rails «[… (Syā.): …၊ နောက်တွင်လည်း ဤနည်းတူ]»
            "nevasekhānāsekho (sī.), nevasekkhānāsekkho (syā. ka.)":
                f"{mod.VAR_L} (Sī.): nevasekhānāsekho{C} (Syā., Ka.): nevasekkhānāsekkho",   # pi-1 rails form
        })
    # the pañhāvāra lexicon of 1-03 … 1-05 that 1-01 does not have (persons, attainments …): the same Burmese
    for k, v in FG.LEX.items():
        F.LEX.setdefault(k, v)
    for mod in (F, FG):
        mod.LEX.setdefault("abhiññaṃ", (mod.LEX["abhiññaṃ uppādeti"][0].split("ကို ")[0], "na"))
        mod.LEX.setdefault("paṭibhānapaṭisambhidāya", (mod.LEX["paṭibhānappaṭisambhidāya"][0], "g"))
    for mod in (F, FG):
        mod.LEX.setdefault("samāpattiṃ", (G.SAMAPATTI, "na"))
    SKF_ADD["kāyāyatanaṃ paccayā kāyaviññāṇaṃ, vatthuṃ paccayā ahetukā §T§o"] = (
        f"{F.FIXED['kāyāyatanaṃ'][0]}{F.KYAUNG} {F.KAYAVINNANA}{C} {F.VATTHU}{F.KYAUNG} {F.AHETUKA} {{T1}}")
    SKF_ADD["asaññasattānaṃ ekaṃ mahābhūtaṃ"] = FG.unit_my(G.prep("asaññasattānaṃ ekaṃ mahābhūtaṃ"))
    for mod in (F, FG):
        mod.SKF.update(SKF_ADD)
    for lk in ("paṭicca", "nissāya", "paccayā", "sahajāto", "saṃsaṭṭho", "sampayutto"):
        # «X dhammaṃ paccayā Y…» (the conditioned term cut short): the term only, «…» follows
        SKF_ADD[f"§T§aṃ dhammaṃ {lk} §T§"] = F.LINK[lk](f"{{T1}} {F.DHAMMA}") + " {T2}"
    HL_ADD.update({
        "*1-4. Paccayānulomādi*": f"*1-4. {F.HEAD['Paccayānulomaṃ']} {F.ADI}*",
        "*Paccayānulomādi*": f"*{F.HEAD['Paccayānulomaṃ']} {F.ADI}*",
        "*Natthi-vigatāvigatapaccayā*": G.HLINES["*Natthi-vigatāvigatapaccayā*"],
    })
    for mod in (F, FG):
        mod.SK.update(SK_ADD)
        mod.SKF.update(SKF_ADD)
    F.HLINES.update(HL_ADD)
    NOTE_ADD.update({
        "ajjhattikā ca asaññasattānañca mahābhūtā":
            f"{AJJHATTIKA} {MAHABHUTA}တို့လည်းကောင်း{C} {ASANNA_G} {MAHABHUTA}တို့လည်းကောင်း",
        "ajjhattikā mahābhūtā ca āhārasamuṭṭhānañca":
            f"{AJJHATTIKA} {MAHABHUTA}တို့လည်းကောင်း{C} {G.SKF['āhārasamuṭṭhānaṃ']} ရုပ်လည်းကောင်း",
    })
    K.NOTE_FIXED.update(NOTE_ADD)
    SUBJ.update({v[0].lower() + v[1:]: K.vara(k) + "သည်" for k, v in K.VARA_OF.items() if k != "pañhā"})


_K_LEX = None


def lex(frag, slots, ti, ci, ki, di, vi):
    try:
        return _K_LEX(frag, slots, ti, ci, ki, di, vi)
    except KeyError as e:
        if "post word first" not in str(e) and not re.fullmatch(r".+? ca", frag.strip()):
            raise
    lead = frag[:len(frag) - len(frag.lstrip())]
    t = frag.strip()
    m = re.fullmatch(r"(.+?) ca", t)
    if m and K.CUR["link"] in G.LINK_IN:
        ph, _, pl, nt = F.np_parse(m[1].split(), iter(slots["T"][ti[0]:]))
        ti[0] += nt
        num = re.search(r" (?:" + "|".join(F.PAA.values()) + r")$", ph)
        return lead + ph + ("တို့" if pl and not num else "") + G.LINK_IN[K.CUR["link"]][0] + F.LAKAUNG
    for k, (my, kind) in sorted(F.LEX.items(), key=lambda kv: -len(kv[0])):
        if kind == "post" and t.startswith(k + " "):
            rest = _K_LEX(" " + t[len(k) + 1:], slots, ti, ci, ki, di, vi)
            # the object stands in the fragment before «…»: the post word without its «ကို»
            return lead + (my[len("ကို "):] if my.startswith("ကို ") else my) + rest
    raise KeyError("post word first")


def variant_after_term(u):
    """«… nevasekkhanāsekkho {…} dhammo …»: the variant stands after a term (before its noun); the unit is translated
    without it and the variant is put right after the same term in the Burmese"""
    m = re.search(r" (\{[^{}]*\})(?= )", u)
    if not m:
        return None
    before = u[:m.start()]
    tm = list(F.TERM_RE.finditer(before))
    if not tm or tm[-1].end() != len(before) and not before[tm[-1].end():].strip() == "":
        return None
    val = F.term_value(tm[-1])
    k = sum(1 for x in tm if F.term_value(x) == val)
    out = _unit_chain(u[:m.start()] + u[m.end():])
    pos = -1
    for _ in range(k):
        pos = out.index(val, pos + 1)
    pos += len(val)
    return out[:pos] + " " + F.variant(m[1][1:-1]) + out[pos:]


def kinds_after(u):
    """«X dhammo Yassa dhammassa Zpaccayena paccayo sahajātaṃ, purejātaṃ.» (the kinds follow without a dash), and
    «… dhammassa sahajātaṃ, …, indriyaṃ (note).» (the condition left out)"""
    kinds = set(K.KIND) | set(K.KIND_FIXED)
    m = re.fullmatch(r"(.*?) ((?:\w+, )*\w+)( \([^()]*\))?(\.?)", u.strip())
    if not m or not all(w in kinds for w in m[2].split(", ")):
        return None
    head = m[1]
    if head.endswith("paccayena paccayo"):
        left = _unit_chain(head)
    else:
        left = G.bits(*F.slot(F.lc(head)))
        if left is None:
            return None
    ks = (C + " ").join(K.kind_word(w) for w in m[2].split(", "))
    note = (" " + F.NOTES[m[3].strip()]) if m[3] else ""
    return f"{left} {ks}{note}" + F.punct(m[4])


def note_middle(u):
    """a unit with a note in the middle («… naadhipatipaccayā (paripuṇṇaṃ) asaññasattānaṃ… …»): the two sides as
    units, the note between them"""
    for m in re.finditer(r" (\([^()]*\)) ", u):
        if m[1] not in F.NOTES:
            continue
        try:
            a = _unit_chain(u[:m.start()])
            b = _unit_chain(u[m.end():])
        except ERRS:
            continue
        return f"{a} {F.NOTES[m[1]]} {b}"
    return None


# a unit of several comma parts that no frame takes whole: each part on its own, joined by «၊»
def comma_parts(u):
    s = u.strip()
    depth, parts, cur = 0, [], ""
    i = 0
    while i < len(s):
        ch = s[i]
        depth += ch in "({"
        depth -= ch in ")}"
        if depth == 0 and s.startswith(", ", i):
            parts.append(cur)
            cur = ""
            i += 2
            continue
        cur += ch
        i += 1
    parts.append(cur)
    if len(parts) < 2:
        return None
    out = []
    for p in parts:
        out.append(_unit_chain(p))
    return (C + " ").join(out)


# ===================================================================================== engine: unit fallback
_K_UNIT = None
VIA_G = collections.Counter()       # units translated by the fallback engine (listed in the notes)


ERRS = (F.Miss, FG.Miss, KeyError, ValueError, StopIteration, IndexError)


def _unit_chain(u):
    """K (1-01) first, then G (1-03 … 1-05) on its own copy of the module"""
    try:
        return _K_UNIT(u)
    except ERRS as e1:
        try:
            r = FG.unit_my(G.prep(u))
            VIA_G[u.strip()] += 1
            return r
        except ERRS:
            raise F.Miss(str(e1))


def unit_my(u):
    try:
        return _unit_chain(u)
    except ERRS as e1:
        lead = u[:len(u) - len(u.lstrip())]
        r = None
        m = re.fullmatch(r"(.*\.)(\(\d+\))", u.strip())
        if m:                                          # «… rūpaṃ.(2)»: no space before the digits (kept)
            return lead + _unit_chain(m[1]) + m[2]
        if re.search(r"\)\.?$", u.strip()):          # the second half of a note cut by a sentence end
            r = K.note_unit(u.strip())
        for fn in (variant_after_term, kinds_after, note_middle, comma_parts):
            if r is not None:
                break
            try:
                r = fn(u)
            except ERRS:
                r = None
        if r is None:
            raise F.Miss(str(e1))
        return lead + r


def setup():
    global _K_UNIT, _K_CHAIN
    setup_numbers(F)
    setup_numbers(FG)
    setup_names()
    setup_notes()
    setup_lex()
    global _K_LEX
    _K_LEX = F.lex
    F.lex = lex
    _K_CHAIN = F.chain
    F.chain = chain
    _K_UNIT = F.unit_my
    F.unit_my = unit_my


setup()


# ===================================================================================== run
class Counting(dict):
    cnt = collections.Counter()

    def setdefault(self, k, v):
        self.cnt[k] += 1
        return super().setdefault(k, v)


def translate(name):
    tri = CH_TRIAD.get(name)
    if tri:
        chapter_notes(name)
    set_triad(F, tri)
    set_triad(FG, tri)
    FG.translate("")                   # (re)builds the fallback's frame regexes
    src = (PALI / name).read_text(encoding="utf-8-sig")
    return F.translate(prep(src))


# 1-01 line 2237: «Uddhaccaṃ ārabbha» is rendered «ယောက်ယက်ခတ်မှုသည်ကို အာရုံပြု၍» there (a stray «သည်»); with the
# 1-03 … 1-05 lexicon this script gives «ယောက်ယက်ခတ်မှုကို အာရုံပြု၍» (logged for the consistency pass)
KNOWN_DIFF = {"1-01-kusalattika.md": {2236}}


def regress():
    bad = 0
    for n in ["1-00-paccaya.md", "1-02-vedanattika.md", "1-01-kusalattika.md"]:
        txt = translate(n)
        pub = (OUT / n).read_text(encoding="utf-8")
        a, b = txt.splitlines(), pub.splitlines()
        d = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
        known = KNOWN_DIFF.get(n, set())
        ok = len(a) == len(b) and set(d) <= known
        print(n, "identical" if not d else f"differs only at the known lines {sorted(d)}" if ok else
              f"DIFFERS ({len(d)} lines: {d[:10]})")
        bad += not ok
    return bad


def main():
    global OUT
    K.CUR["fix"] = True
    if "--out" in sys.argv:                  # write a review copy elsewhere (inside pi-7-my/)
        OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
        del sys.argv[sys.argv.index("--out"):sys.argv.index("--out") + 2]
    if "--regress" in sys.argv:
        sys.exit(1 if regress() else 0)
    F.DEV = "--dev" in sys.argv
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or NAMES
    if F.DEV:
        F.UNSEEN = Counting()
    for n in names:
        txt = translate(n)
        if not F.DEV:
            (OUT / n).write_text(txt, encoding="utf-8")
            print(f"wrote {n}: {sum(1 for l in txt.splitlines() if l)} lines")
    if F.DEV:
        rows = sorted(F.UNSEEN.items(), key=lambda kv: -F.UNSEEN.cnt[kv[0]])
        CHK.mkdir(exist_ok=True)
        with open(CHK / "dev.txt", "w", encoding="utf-8") as fh:
            for k, v in rows:
                fh.write(f"[{F.UNSEEN.cnt[k]}] SK: {k}\n    {v}\n")
        (CHK / "dev-out.md").write_text(txt, encoding="utf-8")
        with open(CHK / "via-g.txt", "w", encoding="utf-8") as fh:
            for k, v in VIA_G.most_common():
                fh.write(f"[{v}] {k}\n")
        print(len(rows), "unmatched skeletons,", sum(F.UNSEEN.cnt.values()), "occurrences")
    if F.SLIPS and "--slips" in sys.argv:
        print("slips:", *sorted(F.SLIPS), sep="\n  ")


if __name__ == "__main__":
    main()
