"""Build the Pāli->Vietnamese keyword map for pi-4 part 10-navakapuggalapannatti (chapter 10).

usage: python -I -X utf8 map_10_vi.py                     (writes 10-navakapuggalapannatti.mapped.md and verifies it)
       python -I -X utf8 map_10_vi.py show lo hi          (segments lo..hi: Pāli, Vietnamese, pairs; writes nothing)
       python -I -X utf8 map_10_vi.py dump [miss]         (every distinct keyword=value; writes nothing)
       python -I -X utf8 map_10_vi.py look kw ...         (pi-1 / pi-2 / pi-3 map values; writes nothing)

Importing this module builds nothing (check_parts_vi.py imports it only for ALLOWED).
Resolution order per keyword: OVERRIDES[bid][kw] -> T10 (this script's table) -> map_common_vi.value():
context4 -> PG -> the pi-3 chain.
The whole navaka niddesa (nine definitions and the closer) is one segment, ^4-208; the nine definitions repeat the
ekaka definitions ^4-22 … ^4-30 (sample 2-ekakapuggalapannatti.mapped.md).
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (NDE, build_part, en_ru, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           pi3_map_values, present, read_keywords, read_pali, read_vietnamese, value, verify)

PART = "10-navakapuggalapannatti"

# part-specific values (^4-208, read from the segment)
T10 = {
    "dukkhaṃ": "khổ đau",                                     # "idaṃ dukkha"nti «“Đây là khổ đau”» (sample ^4-27
                                                              # dukkha, map_6 dukkhaṃ)
}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver():
    vi = read_vietnamese(PART)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value(kw, kws, T10, vi.get(bid, ""))
    return resolve


def show(lo, hi):
    res = resolver()
    vi, pi = read_vietnamese(PART), read_pali(PART)
    for i, (bid, kws) in enumerate(read_keywords(PART)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            er = en_ru(bid)
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError:
                    v = "???"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else "   <<MISS"
                e = er.get(kw, ["", ""])
                print(f"   {kw}={v}   [{e[0]} | {e[1]}]{flag}")


def dump(only_miss=False):
    res = resolver()
    vi = read_vietnamese(PART)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(PART):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        ps = []
        for i, f in ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values)):
            p = [x for x, _ in f(kw).most_common(2) if x != v]
            if p:
                ps.append(f"pi{i}:{p}")
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + ("  " + " ".join(ps) if ps else "")
              + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def look(kws):
    for kw in kws:
        for k in dict.fromkeys((kw, lc(kw), kw[:1].upper() + kw[1:])):
            out = [f"pi{i}:{dict(f(k).most_common(4))}" for i, f in
                   ((1, pi1_map_values), (2, pi2_map_values), (3, pi3_map_values)) if f(k)]
            if out:
                print(k, " ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["look"]:
        look(sys.argv[2:])
    else:
        build_part(PART, resolver())
        verify(PART, ALLOWED)
