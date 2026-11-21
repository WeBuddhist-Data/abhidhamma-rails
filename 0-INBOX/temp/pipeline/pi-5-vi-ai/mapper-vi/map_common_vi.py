"""Shared helpers for the pi-5 (Kathāvatthu) Pāli->Vietnamese keyword maps (pi-5-vi-ai/mapper-vi/).

Importing this module writes nothing: sys.dont_write_bytecode is set before the pi-4 (and through it the pi-3 / pi-2 /
pi-1) modules are loaded, none of their build functions is called, and the pi-4 modules are loaded under private names
and removed from sys.modules again (check_parts_vi.py hashes every pi-1 … pi-4 *.mapped.md before and after).

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_vi import *

Main pieces
- read_keywords(part) / read_vietnamese(part) / read_pali(part)    pi-5 paths; a segment = the non-empty lines up to
                              and including the line that ends with ^id (pi-4 segments())
- present(value, text)        the pi-5 presence check = the pi-1 check (present1: literal, NFC, case-insensitive,
                              word-bounded; " … " parts in order, " / " alternatives) on editorial_text(text): the
                              Pāli of a variant bracket «[dị bản (…): X]» / «[khác chính tả (…): X]» removed (its
                              translated label kept), translated editorial brackets (the speaker notes, «[cần tham
                              khảo Phụ chú giải]», citations) kept as text
- CORE, MATRIX, SATI_BARE, KH, KD, PG, NAMES, lc, NDE, GAP, pi1_value, pi2_value, pi3_value, context3, context4
                              re-exported from pi-4
- T4ALL                       the part tables of the finished pi-4 chapters (pi-4 map_3_vi … map_11_vi T3 … T11)
- pi4_value(kw, kws, text)    the whole approved pi-4 chain without its segment overrides: T4ALL -> context4 -> PG ->
                              pi-3 chain (T15 … -> context3 -> KD -> pi-2 -> pi-1)
- pi1_map_values … pi4_map_values(kw)    Counter of the values the approved Vietnamese maps give
- en_ru(bid)                  {kw: [english, russian]} of the pi-5 English / Russian maps (meaning cross-check only)
- pick(text, *candidates)     the first candidate present in the segment (None if none)
- join(text, parts)           the Vietnamese parts joined contiguously if present, else with " … " (None if absent)
- value(kw, kws, table=None, text=None, single=None)
                              table -> two-word composition (each word by `single`, Vietnamese order as it stands)
                              -> pi4_value
- build_part(part, resolver)  writes <part>.mapped.md (LF); stops on an unmapped keyword; refuses ", " in a value
- verify(part, allowed=None)  the brief's structural check + the presence check; `allowed` = {(id, kw): reason}
- prior_hashes()              sha256 of every pi-1 / pi-2 / pi-3 / pi-4 *.mapped.md
The pi-5 tables (debate FORMULAS, the pi-5 terms, segment rules) live in map_sample_vi.py; later part scripts import
them from there.
"""
import hashlib
import importlib.util
import itertools
import pathlib
import re
import sys
import unicodedata
from collections import Counter

sys.dont_write_bytecode = True

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PIPE = ROOT / "0-INBOX" / "temp" / "pipeline"
PRIOR_DIRS = [PIPE / f"pi-{n}-vi-ai" / "mapper-vi" for n in (1, 2, 3, 4)]
PI4_DIR = PIPE / "pi-4-vi-ai" / "mapper-vi"
VI_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-5-vietnamese-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-5_split_chapters"
MAPS = {n: ROOT / "AI_translation" / "vietnamese" / f"pi-{n}-keywords-by-reference-pali-vietnamese-plain.md"
        for n in (1, 2, 3, 4)}
EN_MAP = ROOT / "AI_translation" / "english" / "pi-5-keywords-by-reference-pali-english-plain.md"
RU_MAP = ROOT / "AI_translation" / "russian" / "pi-5-keywords-by-reference-pali-russian-plain.md"


def prior_hashes():
    """sha256 of every pi-1 … pi-4 mapped file (approved outputs this module must never rewrite)."""
    out = {}
    for d in PRIOR_DIRS:
        for f in sorted(d.glob("*.mapped.md")):
            out[str(f)] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


# ---------------------------------------------------------------------------- pi-4 modules (read-only)
def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_PI4_NAMES = ("map_common_vi", "map_sample_vi") + tuple(f"map_{n}_vi" for n in range(3, 12))
_saved_mods = {n: sys.modules.get(n) for n in _PI4_NAMES}
_saved_path = list(sys.path)
try:
    for _n in _PI4_NAMES:
        sys.modules.pop(_n, None)
    P4 = _load("pi4_map_common_vi", PI4_DIR / "map_common_vi.py")
    # the pi-4 part scripts do `from map_common_vi import ...` / `import map_sample_vi` with the pi-4 folder on sys.path
    sys.modules["map_common_vi"] = P4
    sys.path.insert(0, str(PI4_DIR))
    sys.modules["map_sample_vi"] = _load("pi4_map_sample_vi", PI4_DIR / "map_sample_vi.py")
    T4ALL = {}
    for _n in range(3, 12):
        _m = _load(f"pi4_map_{_n}_vi", PI4_DIR / f"map_{_n}_vi.py")
        T4ALL.update(getattr(_m, f"T{_n}"))
finally:
    sys.path[:] = _saved_path
    for _n in _PI4_NAMES:
        if _saved_mods[_n] is not None:
            sys.modules[_n] = _saved_mods[_n]
        else:
            sys.modules.pop(_n, None)

present1, lc, NDE, GAP = P4.present, P4.lc, P4.NDE, P4.GAP

_VARIANT = re.compile(r"\[\s*((?:dị bản|khác chính tả)[^\]:]*)(?::[^\]]*)?\]")
_EDITORIAL = re.compile(r"\[([^\]]*)\]")


def editorial_text(text):
    """The segment with the Pāli of the variant brackets removed («[dị bản (nhiều bản): aññātāvindriyañca]» keeps only
    its translated label «dị bản (nhiều bản)») and the translated editorial brackets (speaker notes «[với dấu hiệu
    này, câu hỏi của …]», «[cần tham khảo Phụ chú giải]», citations) unwrapped."""
    t = _VARIANT.sub(lambda m: " " + m.group(1) + " ", unicodedata.normalize("NFC", text or ""))
    return _EDITORIAL.sub(lambda m: " " + m.group(1) + " ", t)


def present(value, text):
    """pi-5 presence check: the pi-1 check (present1) on editorial_text(text). Translated editorial brackets count as
    Vietnamese text; a word kept only inside a variant bracket is still NOT present."""
    return present1(value, editorial_text(text))
CORE, MATRIX, SATI_BARE, KH, KD, PG, NAMES = P4.CORE, P4.MATRIX, P4.SATI_BARE, P4.KH, P4.KD, P4.PG, P4.NAMES
pi1_value, pi2_value, pi3_value, context3, context4 = P4.pi1_value, P4.pi2_value, P4.pi3_value, P4.context3, P4.context4
segments = P4.segments


def pi4_value(kw, kws, text=None):
    """The approved pi-4 value of a keyword (finished pi-4 chain; pi-4 segment overrides not applied)."""
    return P4.value(kw, kws, T4ALL, text or "")


_MAP_CACHE = {}


def _map_values(n, kw):
    if n not in _MAP_CACHE:
        c = {}
        for line in MAPS[n].read_text(encoding="utf-8").splitlines():
            if "] " not in line:
                continue
            for pair in line.split("] ", 1)[1].split(", "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    c.setdefault(k, Counter())[v] += 1
        _MAP_CACHE[n] = c
    return _MAP_CACHE[n].get(kw, Counter())


def pi1_map_values(kw):
    return _map_values(1, kw)


def pi2_map_values(kw):
    return _map_values(2, kw)


def pi3_map_values(kw):
    return _map_values(3, kw)


def pi4_map_values(kw):
    return _map_values(4, kw)


_ENRU = {}


def en_ru(bid):
    """{kw: [english, russian]} for one block of the pi-5 English / Russian maps (meaning cross-check only)."""
    if not _ENRU:
        for lang, path in (("en", EN_MAP), ("ru", RU_MAP)):
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.startswith("[") or "] " not in line:
                    continue
                b, rest = line.split("] ", 1)
                d = _ENRU.setdefault(b[1:], {})
                for pair in rest.split(", "):
                    if "=" in pair:
                        k, v = pair.split("=", 1)
                        d.setdefault(k, ["", ""])[0 if lang == "en" else 1] = v
    return _ENRU.get(bid, {})


# ---------------------------------------------------------------------------- reading (pi-5 paths)
def read_keywords(part):
    out = []
    for line in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        bid, rest = line.split("] ", 1)
        out.append((bid[1:], [k.strip() for k in rest.split(", ")]))
    return out


def read_vietnamese(part):
    return segments(VI_DIR / f"{part}.md")


def read_pali(part):
    return segments(PI_DIR / f"{part}.md")


# ---------------------------------------------------------------------------- helpers
def pick(text, *candidates):
    """The first candidate value present in the segment, else None."""
    for c in candidates:
        if c and present(c, text):
            return c
    return None


def join(text, parts):
    """Parts (Vietnamese, in the order wanted) joined contiguously if present, else with " … "; None if absent."""
    v = " ".join(parts)
    if present_strict(v, text):
        return v
    v = GAP.join(parts)
    return v if present(v, text) else None


def compose(kw, kws, text, single):
    """A keyword of two or more words: each word by `single`, joined in the Vietnamese order as it stands (Pāli order
    first, then the other orders): contiguous, then with the inner «là» («vật chất là khác»), then " … ". None if no
    order is present."""
    words = kw.split()
    if len(words) < 2:
        return None
    vals = []
    for w in words:
        v = single(w)
        if v is None or v == NDE:
            return None
        vals.append(v)
    orders = [vals] + [list(p) for p in itertools.permutations(vals) if list(p) != vals]
    for o in orders:
        for sep in (" ", " là "):         # inner «là» kept (pi-1 saṃyojaniyā dhammā, pi-2 Sāsavā saññā)
            v = sep.join(o)
            if present_strict(v, text):
                return v
    best = None                           # " … ": the order whose parts stand closest together in the segment
    for o in orders:
        v = GAP.join(o)
        if present(v, text):
            sp = span(o, text)
            if best is None or sp < best[0]:
                best = (sp, v)
    return best[1] if best else None


def _norm5(t, spaced=False):
    t = unicodedata.normalize("NFC", editorial_text(t)).lower()
    if spaced:                            # a break («…», sentence end) counts as a long distance in span()
        t = re.sub(r"[…;.?!]", " " + "⁂" * 40 + " ", t)
    t = re.sub(r"[,;:.?!“”‘’\"()–—…#\[\]]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def span(parts, text):
    """The shortest stretch (in characters) of the normalised segment that holds the parts in this order; a «…» or a
    sentence end between the parts counts as a long stretch."""
    t = _norm5(text, spaced=True)
    pats = [re.compile(r"(?<!\w)" + re.escape(_norm5(p)) + r"(?!\w)") for p in parts]
    best = None
    for m0 in pats[0].finditer(t):
        pos, ok = m0.end(), True
        for p in pats[1:]:
            m = p.search(t, pos)
            if not m:
                ok = False
                break
            pos = m.end()
        if ok and (best is None or pos - m0.start() < best):
            best = pos - m0.start()
    return best if best is not None else 10 ** 9


_BOUNDARY = re.compile(r"[,;:.?!…–—“”‘’\"()]")


def present_strict(value, text):
    """present() where punctuation and «…» are boundaries: a contiguous value may not run across them (the
    abbreviated lists «… thức cũng được tìm thấy… tri giác …» would otherwise give «được tìm thấy thức»)."""
    return present(value, _BOUNDARY.sub(" ⁂ ", editorial_text(text)))


def value(kw, kws, table=None, text=None, single=None):
    """table -> two-word composition (`single` resolves each word; default: table -> pi4_value) -> pi4_value."""
    k = lc(kw)
    t = text or ""
    if table and k in table:
        return table[k]
    if " " in kw:
        def _single(w):
            wk = lc(w)
            if single is not None:
                return single(w)
            if table and wk in table:
                return table[wk]
            try:
                return pi4_value(w, kws, t)
            except KeyError:
                return None
        v = compose(kw, kws, t, _single)
        if v is not None:
            return v
    return pi4_value(kw, kws, t)


# ---------------------------------------------------------------------------- build and verify
def build_part(part, resolver):
    """resolver(bid, kw, kws) -> Vietnamese value. Stops on an unmapped keyword."""
    lines, missing = [], []
    for bid, kws in read_keywords(part):
        pairs = []
        for kw in kws:
            try:
                v = resolver(bid, kw, kws)
            except KeyError:
                missing.append((bid, kw))
                v = "???"
            v = unicodedata.normalize("NFC", v)
            assert ", " not in v, (bid, kw, v)
            pairs.append(f"{kw}={v}")
        lines.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        raise SystemExit(f"{part}: unmapped keywords: {missing}")
    (HERE / f"{part}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def verify(part, allowed=None, show=50):
    allowed = allowed or {}
    a = [l.split("] ", 1) for l in (HERE / f"{part}.keywords.md").read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [l.split("] ", 1) for l in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert [x[0] for x in a] == [x[0] for x in b], part
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(", ")] != [k.split("=", 1)[0] for k in y.split(", ")]]
    vi = read_vietnamese(part)
    nde, miss, exc = 0, [], []
    for bid, rest in b:
        bid = bid[1:]
        text = vi.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
            elif text is None or not present(v, text):
                (exc if (bid, kw) in allowed else miss).append((bid, kw, v))
    print(part, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss),
          "| listed exceptions", len(exc))
    for m in miss[:show]:
        print("   MISS", *m)
    for e in exc:
        print("   EXCEPTION", *e, "--", allowed[(e[0], e[1])])
    return bad, nde, miss
