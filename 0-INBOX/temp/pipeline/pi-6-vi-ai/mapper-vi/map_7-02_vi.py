"""Pāli->Vietnamese keyword map of pi-6 7-02-anusayayamaka (Anusayavāra, paṭiloma: «không nằm sẵn»).

usage: python -I -X utf8 -B map_7-02_vi.py                  (writes 7-02-anusayayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_7-02_vi.py dump [miss]      (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_7-02_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setter: map_7-01_vi.py (loaded with importlib); resolution
OVERRIDES[bid][kw] -> A.value701(kw, kws, T702, text) = T702 -> 7-01 T701 -> tendency_value -> vare_value ->
verb_value -> map_sample_vi.value6.
Conventions: vi-map-conventions-pi6.md, map-coordinator-rules.md, notes-map-7-01.md, notes-map-7-02.md.
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

_spec = importlib.util.spec_from_file_location("map_7_01_vi", HERE / "map_7-01_vi.py")
A = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(A)

PART = "7-02-anusayayamaka"

# Own table (lower-case keys): the paṭiloma headings «(d) Chiều ngược theo người», «(đ) Chiều ngược theo nơi chốn»,
# «(e) Chiều ngược theo người và nơi chốn» (as FORMULAS anulomapuggalo … / paccanīkapuggalo …).
T702 = {
    "paṭilomapuggalo": "chiều ngược theo người",
    "paṭilomaokāso": "chiều ngược theo nơi chốn",
    "paṭilomapuggalokāsā": "chiều ngược theo người và nơi chốn",
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value702(kw, kws, text):
    return A.value701(kw, kws, T702, text)


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value702(kw, kws, vi.get(bid, ""))
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
