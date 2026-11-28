"""Shared helpers and tables for the pi-6 (Yamaka) Pāli->Russian keyword maps (pi-6-ru/mapper-ru/).

Importing this module has no side effects (no file is written, nothing printed).

    import sys, pathlib; sys.dont_write_bytecode = True
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_pi6_ru import *

It re-uses the pi-1 tooling (pi-1-ru/mapper-ru/map_common_ru.py: present(), _segments, _norm, _token, CORE, CH2,
MATRIX) and the pi-2 table (pi-2-ru/mapper-ru/map_common_pi2_ru.py: KH, PREPOSITIONS, EXCEPTIONS) unchanged and
only swaps the paths to pi-6. Never edit the pi-1 / pi-2 modules.

Main pieces
- read_keywords(part)              -> [(id, [kw, ...]), ...]   from <part>.keywords.md (this folder)
- read_russian(part) / read_pali(part) -> {id: segment text}   (segments end with ^id)
- present(value, text)             -> pi-1 presence check (regular inflection allowed)
- present_gap(value, text)         -> same tokens in order, up to 3 words between them (root compounds only)
- YM                               -> pi-6 table settled on the sample (preamble + 1-mulayamaka)
- root_family(member, sg, pl, loc, ins, neut) -> the Mūlayamaka compound values for one member (kusala, nāma, ...)
- value(kw, kws, table)            -> table (or YM) -> pi-2 KH -> pi-1 CH2 / MATRIX, with the -ti / -ñca / -ñceva
                                      endings folded to the base keyword (see ru-map-conventions-pi6.md)
- build_part(part, resolver)       -> writes <part>.mapped.md here; resolver(id, kw, kws) returns the Russian
- verify(part, allowed=...)        -> the brief's structural check + presence check + non-word / preposition check
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True  # never write into the pi-1 / pi-2 folders
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
for _sub in ("pi-1-ru", "pi-2-ru"):
    _p = str(ROOT / "0-INBOX" / "temp" / "pipeline" / _sub / "mapper-ru")
    if _p not in sys.path:
        sys.path.insert(0, _p)
import map_common_ru as _pi1  # noqa: E402  (pi-1 tooling, read-only)
import map_common_pi2_ru as _pi2  # noqa: E402  (pi-2 tooling, read-only)
from map_common_ru import CH2, CORE, MATRIX, ch2_value, lc, present  # noqa: E402,F401
from map_common_pi2_ru import KH, PREPOSITIONS  # noqa: E402,F401

RU_DIR = ROOT / "AI_translation" / "russian" / "pi-6-russian-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
NDE = "(no direct equivalent)"
GAP = " … "
CYR = _pi1.CYR


# ---------------------------------------------------------------------------- reading
def read_keywords(part):
    out = []
    for line in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        bid, rest = line.split("] ", 1)
        out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


def read_russian(part):
    return _pi1._segments(RU_DIR / f"{part}.md")


def read_pali(part):
    return _pi1._segments(PI_DIR / f"{part}.md")


# ---------------------------------------------------------------------------- presence checks
def present_gap(value, text, max_between=3):
    """The value's words in order, with up to max_between words between two of them. Used only for the root
    compounds (ekamūla*, aññamaññamūla*), whose Russian is split by the member («общий благой корень») or by the
    «и …, и …» of a ceva … ca pair («имеют и общий корень, и взаимный корень»)."""
    t = _pi1._norm(text)
    for part in re.split(r" … | / ", value):
        toks = _pi1._norm(part).split()
        if not toks:
            continue
        sep = r"\s+(?:\S+\s+){0,%d}?" % max_between
        if not re.search(f"(?<![{CYR}])" + sep.join(_pi1._token(w) for w in toks), t):
            return False
    return True


GAP_OK = re.compile(r"^(ekamūl|aññamaññamūl)")   # keywords whose value may be matched with present_gap


def _bare(w):
    p = _pi1._token(w)
    return p[len("(?:не)?"):] if p.startswith("(?:не)?") else p


def glued_negation_only(value, text):
    """Words of the value that occur in the segment only with a glued «не» (cut from «не-X»): a value made by
    cutting a negative prefix off (user decision 2026-11-14: then the value must be (no direct equivalent))."""
    t = _pi1._norm(text)
    bad = []
    for part in re.split(r" … | / ", value):
        for w in _pi1._norm(part).split():
            if w in _pi1.EXACT or w in _pi1.ALT or len(w) <= 2 or w.startswith(("не", "без")):
                continue
            if not re.search(f"(?<![{CYR}])" + _bare(w), t) and re.search(f"(?<![{CYR}])" + _pi1._token(w), t):
                bad.append(w)
    return bad


# ---------------------------------------------------------------------------- pi-6 table (sample)
# Pāli keyword (lower-case first letter) -> Russian dictionary form. Later parts extend it in their own script
# ({**YM, ...}); value() falls back to pi-2 KH and then pi-1 CH2 / MATRIX.

# pi-2 user decision 2026-11-16: N-vidhena WITHOUT «классификация» (KH still carries it; YM overrides)
YM = {k: v.split(GAP, 1)[1] for k, v in _pi2.FRAME.items()}

# -- Mūlayamaka root compounds, one value each (the phrase the Russian uses; ru-map-conventions-pi6.md §2)
ROOT_ONLY = {
    "ekamūla": "имеющий общий корень", "aññamaññamūla": "имеющий взаимный корень",
    "ekamūlamūla": "имеющий общий корень корней", "aññamaññamūlamūla": "имеющий взаимный корень корней",
    "ekamūlaka": "основанный на общем корне", "aññamaññamūlaka": "основанный на взаимном корне",
    "ekamūlamūlaka": "основанный на общем корне корней",
    "aññamaññamūlamūlaka": "основанный на взаимном корне корней",
}
for _stem, _v in ROOT_ONLY.items():
    for _end in ("ā", "aṃ", "āni", "o"):
        YM[_stem[:-1] + _end] = _v                  # ekamūl + ā / aṃ / āni / o


def root_family(m, sg, pl, loc, ins, neut):
    """All Mūlayamaka / Hetuvārādi compounds of one member m (Pāli stem ending in -a).
    sg/pl: «благой»/«благие»; loc «благом» (на … корне); ins «благим» (вместе с … корнем / порождённый …);
    neut «благое» (… питание)."""
    d = {}
    for e in ("ā", "āni"):
        d[f"{m}mūl{e}"] = f"{pl} корни"
        d[f"{m}mūlamūl{e}"] = f"{pl} корни корней"
    for e in ("aṃ", "ena", "a"):
        d[f"{m}mūl{e}"] = f"{sg} корень"
    for e in ("ā", "aṃ", "āni"):
        d[f"{m}mūlak{e}"] = f"основанный на {loc} корне"
        d[f"{m}mūlamūlak{e}"] = f"основанный на {loc} корне корней"
    d[f"{m}mūlasahajātā dhammā"] = f"явления возникшие вместе с {ins} корнем"
    d[f"{m}mūlasahajātā"] = f"возникший вместе с {ins} корнем"
    d[f"{m}samuṭṭhānaṃ"] = f"порождённый {ins}"
    # Hetuvārādi series (Russian «являются благими причинами… благими источниками… …»)
    a = m[:-1] + "ā"                                    # kusala -> kusalā (before a vowel-initial member)
    d.update({
        f"{m}hetū": f"{pl} причины", f"{m}nidānā": f"{pl} источники", f"{m}sambhavā": f"{pl} начала",
        f"{m}ppabhavā": f"{pl} истоки", f"{m}pabhavā": f"{pl} истоки",
        f"{m}samuṭṭhānā": f"{pl} порождающие факторы", f"{a}hārā": f"{neut} питание",
        f"{a}rammaṇā": f"{pl} объекты", f"{m}paccayā": f"{pl} условия", f"{m}samudayā": f"{pl} возникновения",
    })
    return d


MEMBERS = {   # member: (sg, pl, loc, ins, neut)
    "kusala": ("благой", "благие", "благом", "благим", "благое"),
    "akusala": ("неблагой", "неблагие", "неблагом", "неблагим", "неблагое"),
    "abyākata": ("этически неопределённый", "этически неопределённые", "этически неопределённом",
                 "этически неопределённым", "этически неопределённое"),
    "nāma": ("умственный", "умственные", "умственном", "умственным", "умственное"),
}
for _m, _f in MEMBERS.items():
    YM.update(root_family(_m, *_f))

YM.update({
    # -- book frame (preamble; CORE has Abhidhammapiṭake, Namo, bhagavato, arahato, sammāsambuddhassa)
    "yamakapāḷi": "парные вопросы", "yamaka": "парные вопросы", "pāḷi": NDE,
    "mūlayamakaṃ": "парные вопросы о корнях", "mūlayamakapāḷi": "парные вопросы о корнях",
    # -- members as adjectives / substantives (pi-1, pi-2)
    "kusalā": "благой", "kusalaṃ": "благой", "kusala": "благой",
    "akusalā": "неблагой", "akusalaṃ": "неблагой", "akusala": "неблагой",
    "abyākatā": "этически неопределённый", "abyākataṃ": "этически неопределённый",
    "abyākata": "этически неопределённый",
    "nāmā": "умственный",                                # adjective of «nāmā dhammā» = «умственные явления»
    "nāmaṃ": "умственное", "nāma": "умственное",          # Pāli noun nāma = «умственное» (pi-2 81 lines, pi-1)
    "kusalā dhammā": "благие явления", "akusalā dhammā": "неблагие явления",
    "abyākatā dhammā": "этически неопределённые явления", "nāmā dhammā": "умственные явления",
    "dhammā": "явления",
    # -- answers and the root sentences
    "āmantā": "да", "natthi": "нет", "na": "не", "tīṇi": "три", "tayo": "три", "nava": "девять",
    "ye keci": NDE, "sabbe te": "все", "sabbe": "все", "vā pana": "а",
    "mūlāni": "корни", "mūlaṃ": "корень", "mūla": "корень", "uppajjanti": "возникать",
    "avasesā": "остальной", "avasesaṃ": "остальной", "avaseso": "остальной",
    "rūpaṃ": "материальная форма",
    "ahetukaṃ": "не имеющий корней", "sahetukaṃ": "имеющий корни",
    "ahetukā": "не имеющий корней", "sahetukā": "имеющий корни",
    # -- Hetuvārādi verse (Корень, причина и источник, начало вместе с истоком; …)
    "hetu": "причина", "nidānaṃ": "источник", "sambhavo": "начало", "pabhavena": "исток",
    "samuṭṭhānāhārārammaṇā": "порождающий фактор питание объект", "paccayo": "условие",
    "samudayena": "возникновение",
    # -- headings (ru-zeroshot-terms.md; lower-case first letter, label / number dropped)
    "uddeso": "перечень", "niddeso": "разъяснение", "vāro": "раздел", "nayo": "метод",
    "mūlavāro": "раздел о корнях", "hetuvārādi": "раздел о причинах и другие",
    "mūlanayo": "метод корней", "mūlamūlanayo": "метод корней корней",
    "mūlakanayo": "метод основания на корне", "mūlamūlakanayo": "метод основания на корне корней",
    "uddesavāro": "раздел перечня", "niddesavāro": "раздел разъяснения",
    "mūlavārauddeso": "перечень раздела о корнях", "mūlavāraniddeso": "разъяснение раздела о корнях",
    "niṭṭhito": "завершённый", "niṭṭhitā": "завершённый", "niṭṭhitaṃ": "завершённый",
})


# ---------------------------------------------------------------------------- default resolution
def _fold(k):
    """Endings that add no word of their own: -ti (quotation), -ñca / -ñceva («и … и»)."""
    out = [k]
    if k.endswith("ñceva"):
        out.append(k[:-5] + "ṃ")
    if k.endswith("ñca"):
        out.append(k[:-3] + "ṃ")
    if k.endswith(("āti", "īti", "ūti", "ṃti")):
        out.append(k[:-2])
    return out


def value(kw, kws, table=None):
    """Default: the given table (or YM), then pi-2 KH, then pi-1 CH2 / MATRIX; -ti / -ñca / -ñceva folded."""
    t = YM if table is None else table
    for k in _fold(lc(kw)):
        if k in t:
            return t[k]
    for k in _fold(lc(kw)):
        if k in KH:
            return KH[k]
        if k in CH2:
            return ch2_value(k, kws, CH2)
        if k in MATRIX:
            return MATRIX[k]
    raise KeyError(kw)


# presence-check exceptions by keyword (value correct; inflection outside present()'s tolerance)
EXCEPTIONS = dict(_pi2.EXCEPTIONS)


def allowed_for(part, exceptions=None):
    exc = EXCEPTIONS if exceptions is None else exceptions
    return {(bid, kw): exc[lc(kw)] for bid, kws in read_keywords(part) for kw in kws if lc(kw) in exc}


# ---------------------------------------------------------------------------- build and verify
def build_part(part, resolver):
    """resolver(bid, kw, kws) -> Russian value. Stops on an unmapped keyword or ", " in a value."""
    lines, missing = [], []
    for bid, kws in read_keywords(part):
        pairs = []
        for kw in kws:
            try:
                v = resolver(bid, kw, kws)
            except KeyError:
                missing.append((bid, kw))
                v = "???"
            assert ", " not in v, (bid, kw, v)
            pairs.append(f"{kw}={v}")
        lines.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        raise SystemExit(f"{part}: unmapped keywords: {sorted(set(k for _, k in missing))}")
    (HERE / f"{part}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def verify(part, show=60, allowed=None):
    """allowed: {(bid, kw): reason} presence-check exceptions (listed in the report).
    Root compounds matched only with present_gap are counted separately (reason: member or «и» in between)."""
    allowed = allowed or {}
    a = [l.split("] ", 1) for l in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    ru = read_russian(part)
    nde, miss, exc, gap, prep, cut, total = 0, [], [], 0, [], [], 0
    for bid, rest in b:
        bid = bid[1:]
        text = ru.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            total += 1
            if v == NDE:
                nde += 1
                continue
            if v.strip().lower() in PREPOSITIONS:
                prep.append((bid, kw, v))
            if text is not None and glued_negation_only(v, text):
                cut.append((bid, kw, v))
            if (bid, kw) in allowed:
                exc.append((bid, kw, v, allowed[(bid, kw)]))
            elif text is not None and present(v, text):
                pass
            elif text is not None and GAP_OK.match(lc(kw)) and present_gap(v, text):
                gap += 1
            else:
                miss.append((bid, kw, v))
    print(part, "lines", len(a), "bad", bad, "| pairs", total, "| no-direct-equivalent", nde,
          "| presence misses", len(miss), "| root-compound gap matches", gap, "| listed exceptions", len(exc),
          "| bare prepositions", len(prep), "| cut-negation values", len(cut))
    for m in miss[:show]:
        print("   MISS", *m)
    for e in exc:
        print("   EXC ", *e)
    for p in prep:
        print("   PREP", *p)
    for c in cut:
        print("   CUT ", *c)
    return bad, nde, miss, exc
