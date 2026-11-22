"""Pāli->Vietnamese keyword map, pi-6 chapter 10-04-indriyayamaka (Indriyayamaka, pavattivāra, uppādavāra (1)
paccuppanna: paccanīkaokāso and paccanīkapuggalokāsā, ^6-10-12-5-0 … ^6-10-239).

usage: python -I -X utf8 -B map_10-04_vi.py                  (writes 10-04-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-04_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-04_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Chain: map_10-02_vi.value1002 (T10_02 attribute beings / pavatte -> map_10-01_vi
T10_01 -> mulaka10 -> moment10 (citta10 kinds) -> faculty_value -> map_3-03_vi.value303 (3-02 planes, 3-01 ATTR /
PLANE_LOC / BEINGS_GEN with the position and Itaresaṃ rules, map_2-01_vi.frames201 with verb_value) -> value6).
Values are the words of the zero-shot translation; the presence check confirms them against each segment.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import NDE, build_part, en, present, read_keywords, read_pali, read_vietnamese, verify  # noqa: E402

J = importlib.import_module("map_10-02_vi")         # value1002 (frame-setter of the Indriyayamaka beings / citta kinds)

PART = "10-04-indriyayamaka"

# this chapter's table (none needed: every keyword resolves through value1002)
T10_04 = {}

# per-segment choices (none needed)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value1004(kw, kws, vi, pi):
    return J.value1002(kw, kws, vi, pi, T10_04)


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value1004(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(only_miss=False, part=PART):
    res, vi = resolver(part), read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            v = res(bid, kw, kws)
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v, vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        e = en(where[(kw, v)][0]).get(kw)
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:4]}" + (f"  en:{e}" if e else "") + (f"  MISS {m}" if m else ""))
    print("distinct", len(c), "miss-pairs", len(miss), "miss-total", sum(miss.values()))


def show(lo, hi, with_pali=False, part=PART):
    res, vi, pi = resolver(part), read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
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
