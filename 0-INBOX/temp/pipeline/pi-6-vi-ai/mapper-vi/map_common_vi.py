"""Shared helpers for the pi-6 (Yamaka) Pāli->Vietnamese keyword maps (pi-6-vi-ai/mapper-vi/).

Importing this module writes nothing: sys.dont_write_bytecode is set before the pi-5 modules (and through them the
pi-4 … pi-1 modules) are loaded, none of their build functions is called, and the pi-5 modules are loaded with the
pi-5 folder on sys.path and removed from sys.modules again afterwards (check_parts_vi.py hashes every pi-1 … pi-5
*.mapped.md before and after the import).

    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_common_vi import *

Main pieces
- read_keywords(part) / read_vietnamese(part) / read_pali(part)    pi-6 paths; a segment = the non-empty lines up to
                              and including the line that ends with ^id (pi-4 segments()); chapter stems with
                              hyphenated numbers (2-01-khandhayamaka, 10-13-indriyayamaka) work unchanged
- present(value, text)        the pi-5 presence check (pi-1 check on editorial_text(text): translated editorial
                              brackets and the translated label of a variant bracket count as text, the Pāli after the
                              colon of «[dị bản (…): X]» does not)
- present_strict, pick, join, compose, span, editorial_text        the pi-5 helpers
- CORE, MATRIX, SATI_BARE, KH, KD, PG, NAMES, lc, NDE, GAP, pi1_value … pi4_value, context3, context4   (re-exported)
- FORMULAS5, KV5, context5, value5    the pi-5 debate frames / terms / segment rules / chain (pi-5 map_sample_vi)
- T5ALL                       the part tables of the finished pi-5 chapters (pi-5 map_2_vi … map_31_vi T2 … T31;
                              later chapters override earlier ones)
- pi5_value(kw, kws, text)    the whole approved pi-5 chain without its segment overrides: T5ALL -> context5 ->
                              FORMULAS5 -> KV5 -> two-word composition -> pi-4 chain
- pi1_map_values … pi5_map_values(kw)    Counter of the values the approved Vietnamese maps give
- en(bid)                     {kw: english} of the pi-6 English map (meaning cross-check only; there is no Russian pi-6)
- build_part(part, resolver)  writes <part>.mapped.md (LF); stops on an unmapped keyword; refuses ", " in a value
- verify(part, allowed=None)  the brief's structural check + the presence check; `allowed` = {(id, kw): reason}
- prior_hashes()              sha256 of every pi-1 … pi-5 *.mapped.md
The pi-6 tables (FORMULAS = the Yamaka frame words, YM = the pi-6 terms, root_value() = the root compounds,
context6(), value6()) live in map_sample_vi.py; later part scripts import them from there.
"""
import hashlib
import importlib
import importlib.util
import pathlib
import sys
import unicodedata
from collections import Counter

sys.dont_write_bytecode = True

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PIPE = ROOT / "0-INBOX" / "temp" / "pipeline"
PRIOR_DIRS = [PIPE / f"pi-{n}-vi-ai" / "mapper-vi" for n in (1, 2, 3, 4, 5)]
PI5_DIR = PIPE / "pi-5-vi-ai" / "mapper-vi"
VI_DIR = ROOT / "AI_translation" / "vietnamese" / "pi-6-vietnamese-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
MAPS = {n: ROOT / "AI_translation" / "vietnamese" / f"pi-{n}-keywords-by-reference-pali-vietnamese-plain.md"
        for n in (1, 2, 3, 4, 5)}
EN_MAP = ROOT / "AI_translation" / "english" / "pi-6-keywords-by-reference-pali-english-plain.md"


def prior_hashes():
    """sha256 of every pi-1 … pi-5 mapped file (approved outputs this module must never rewrite)."""
    out = {}
    for d in PRIOR_DIRS:
        for f in sorted(d.glob("*.mapped.md")):
            out[str(f)] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


# ---------------------------------------------------------------------------- pi-5 modules (read-only)
def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_PI5_CHAPTERS = tuple(range(2, 32))
_PI5_NAMES = ("map_common_vi", "map_sample_vi") + tuple(f"map_{n}_vi" for n in _PI5_CHAPTERS) \
    + tuple(f"map_{n}_vi" for n in range(32, 40))
_saved_mods = {n: sys.modules.get(n) for n in _PI5_NAMES}
_saved_path = list(sys.path)
try:
    for _n in _PI5_NAMES:
        sys.modules.pop(_n, None)
    P5 = _load("pi5_map_common_vi", PI5_DIR / "map_common_vi.py")
    # the pi-5 part scripts do `from map_common_vi import ...` / `from map_sample_vi import ...` / `import map_N_vi`
    # with the pi-5 folder on sys.path
    sys.modules["map_common_vi"] = P5
    sys.path.insert(0, str(PI5_DIR))
    S5 = _load("pi5_map_sample_vi", PI5_DIR / "map_sample_vi.py")
    sys.modules["map_sample_vi"] = S5
    T5ALL = {}
    for _n in _PI5_CHAPTERS:
        _m = importlib.import_module(f"map_{_n}_vi")
        T5ALL.update(getattr(_m, f"T{_n}", {}))
finally:
    sys.path[:] = _saved_path
    for _n in _PI5_NAMES:
        if _saved_mods[_n] is not None:
            sys.modules[_n] = _saved_mods[_n]
        else:
            sys.modules.pop(_n, None)

present, present1, present_strict, editorial_text = P5.present, P5.present1, P5.present_strict, P5.editorial_text
pick, join, compose, span = P5.pick, P5.join, P5.compose, P5.span
lc, NDE, GAP = P5.lc, P5.NDE, P5.GAP
CORE, MATRIX, SATI_BARE, KH, KD, PG, NAMES = P5.CORE, P5.MATRIX, P5.SATI_BARE, P5.KH, P5.KD, P5.PG, P5.NAMES
pi1_value, pi2_value, pi3_value, pi4_value = P5.pi1_value, P5.pi2_value, P5.pi3_value, P5.pi4_value
context3, context4 = P5.context3, P5.context4
FORMULAS5, KV5, context5, value5 = S5.FORMULAS, S5.KV, S5.context5, S5.value5
segments = P5.segments


def pi5_value(kw, kws, text=None):
    """The approved pi-5 value of a keyword (finished pi-5 chain; pi-5 segment overrides not applied)."""
    return value5(kw, kws, T5ALL, text or "")


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


def pi5_map_values(kw):
    return _map_values(5, kw)


_EN = {}


def en(bid):
    """{kw: english} for one block of the pi-6 English map (meaning cross-check only)."""
    if not _EN:
        for line in EN_MAP.read_text(encoding="utf-8").splitlines():
            if not line.startswith("[") or "] " not in line:
                continue
            b, rest = line.split("] ", 1)
            d = _EN.setdefault(b[1:], {})
            for pair in rest.split(", "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    d.setdefault(k, v)
    return _EN.get(bid, {})


# ---------------------------------------------------------------------------- reading (pi-6 paths)
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
            if v is None:
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
