"""Pāli->Vietnamese keyword map of pi-6 7-06-anusayayamaka (Pajahanavāra, paṭiloma: «không dứt bỏ»).

usage: python -I -X utf8 -B map_7-06_vi.py                  (writes 7-06-anusayayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_7-06_vi.py dump [miss]      (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_7-06_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters: map_7-01_vi.py (value701: TENDENCY, VERBS nappajahati, PERSONS,
PLANES, FEELINGS, vare_value), map_7-02_vi.py (T702), map_7-03_vi.py (T703), map_7-04_vi.py (T704), map_7-05_vi.py
(T705, tendency_ca), loaded with importlib; resolution OVERRIDES[bid][kw] -> value706() = the -ñca tendency forms
(7-05 tendency_ca) -> A.value701(kw, kws, T706, text) = T706 (T705 + own) -> 7-01 T701 -> tendency_value ->
vare_value -> verb_value -> map_sample_vi.value6.
Conventions: vi-map-conventions-pi6.md, map-coordinator-rules.md, notes-map-7-01.md … notes-map-7-06.md.
"""
import importlib.util
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_vi import (NDE, build_part, en, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, HERE / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


A = _load("map_7_01_vi", "map_7-01_vi.py")
B = _load("map_7_02_vi", "map_7-02_vi.py")
C = _load("map_7_03_vi", "map_7-03_vi.py")
D = _load("map_7_04_vi", "map_7-04_vi.py")
E = _load("map_7_05_vi", "map_7-05_vi.py")

PART = "7-06-anusayayamaka"

_ANAGAMI_MS = "người có được con đường không trở lại"   # «Người có được con đường không trở lại không dứt bỏ …»
_AGGA_MS = "người có được con đường tối thượng"          # conventions-pi6 / 2-02 / 7-05
_MS = "người có được con đường"                          # «Ngoại trừ hai người có được con đường» (Dvinnaṃ: no keyword)

# Own table (lower-case keys) on top of 7-05 T705 (7-02 paṭiloma headings + 7-03 puggalo «hạng người»).
T706 = {
    **E.T705,
    "ṭhapetvā": "ngoại trừ",                       # «Ngoại trừ …» (2-01, 3-01, 5-01, 10-01)
    "aṭṭhamakañca": "người thứ tám",               # «… và người thứ tám» (-ñca: no word of its own; Aṭṭhamako)
    "anāgāmimaggasamaṅgī": _ANAGAMI_MS,
    "anāgāmimaggasamaṅgiñca": _ANAGAMI_MS,         # «Ngoại trừ người có được con đường không trở lại và …»
    "anāgāmimaggasamaṅgiṃ": _ANAGAMI_MS,
    "aggamaggasamaṅgiñca": _AGGA_MS,               # «Ngoại trừ người có được con đường tối thượng và …» (2-02)
    "aggamaggasamaṅgiṃ": _AGGA_MS,
    "maggasamaṅgīnaṃ": _MS,                        # Dvinnaṃ maggasamaṅgīnaṃ ṭhapetvā «Ngoại trừ hai người có được …»
    "maggasamaṅgīnañca": _MS,                      # «Ngoại trừ hai người có được con đường và người thứ tám»
    "pajahanāvāre": "mục về sự dứt bỏ",            # source slip for Pajahanavāre (closer «… trong mục về sự dứt bỏ.»)
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value706(kw, kws, text):
    v = E.tendency_ca(kw)
    if v is not None:
        return v
    return A.value701(kw, kws, T706, text)


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value706(kw, kws, vi.get(bid, ""))
    return resolve


def dump(only_miss=False):
    res, vi = resolver(), read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            v = res(bid, kw, kws)
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        if only_miss and not miss.get((kw, v)):
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "")
              + (f"  MISS {miss[(kw, v)]}" if miss.get((kw, v)) else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False):
    res, vi, pi = resolver(), read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
            out = []
            for kw in kws:
                v = res(bid, kw, kws)
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                out.append(f"{kw}={v}{flag}")
            print("   " + " | ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
