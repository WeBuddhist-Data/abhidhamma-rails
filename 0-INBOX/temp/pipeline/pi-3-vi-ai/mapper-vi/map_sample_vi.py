"""Build the SAMPLE Pāli->Vietnamese keyword maps for pi-3 (Dhātukathā): preamble, 1-uddeso, 2-pathamanayo.

usage: python -I -X utf8 map_sample_vi.py                     (writes the three <part>.mapped.md and verifies them)
       python -I -X utf8 map_sample_vi.py dump PART [miss]    (every distinct keyword=value with count, first segments
                                                              and the pi-1 / pi-2 map values; writes nothing)
       python -I -X utf8 map_sample_vi.py show PART lo hi     (segments lo..hi with every pair; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> CORE (preamble only) -> SAMPLE (this script's table)
-> map_common_vi.value(): context3 (segment rules) -> KD (pi-3 table) -> alternatives / counts / «X saṅgahito» /
«X dhammā» rules -> the pi-2 chain (pi-2 map_18_vi.py tables) -> the approved pi-1 chain.
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, pi-2 vi-map-conventions-pi2.md + notes-map-*.md,
vi-map-conventions-pi3.md.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (CORE, NDE, build_part, lc, pi1_map_values, pi2_map_values,  # noqa: E402
                           present, read_keywords, read_pali, read_vietnamese, value, verify)

PARTS = ["preamble", "1-uddeso", "2-pathamanayo"]

# part-specific values (everything recurring lives in map_common_vi.KD)
SAMPLE = {}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {
    ("3-112", "pañhā"): "translated label of the variant bracket «[dị bản …: …; Phân tích các hiện tượng, cả trong "
                        "phần hỏi đáp về bộ đôi]» (dukapañhāpucchakepi); present() strips brackets",
    ("3-112", "pucchake"): "as pañhā: «phần hỏi đáp» inside the variant bracket",
}


def resolver_for(part):
    vi = read_vietnamese(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        if part == "preamble" and k in CORE:      # the pi-1 preamble values (Namo … sammāsambuddhassa)
            return CORE[k]
        return value(kw, kws, SAMPLE, vi.get(bid, ""))
    return resolve


def dump(part, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
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
        p1 = [x for x, _ in pi1_map_values(kw).most_common(2) if x != v]
        p2 = [x for x, _ in pi2_map_values(kw).most_common(2) if x != v]
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  pi1:{p1}" if p1 else "") + (f"  pi2:{p2}" if p2 else "")
              + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(part, lo, hi):
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]\n-- PI {pi.get(bid, '')}\n-- VI {vi.get(bid, '')}")
            print("   " + " | ".join(f"{kw}={res(bid, kw, kws)}" for kw in kws))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], sys.argv[3:4] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p, ALLOWED)
