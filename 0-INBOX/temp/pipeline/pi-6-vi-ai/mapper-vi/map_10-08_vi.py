"""Pāli->Vietnamese keyword map, pi-6 chapter 10-08-indriyayamaka (Indriyayamaka, pavattivāra, uppādavāra
(4) paccuppannātīta: all six sections, ^6-10-15-1-0 … ^6-10-365).

usage: python -I -X utf8 -B map_10-08_vi.py                  (writes 10-08-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-08_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-08_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Chain: T10_08 -> map_10-02_vi.value1002 (T10_02 / ATTR10 -> map_10-01_vi
T10_01 -> mulaka10 -> moment10 (citta10 + map_8_vi.moment_value) -> faculty_value -> map_3-03_vi.value303 (3-02
planes, 3-01 ATTR / PLANE_LOC / BEINGS_GEN with the position and Itaresaṃ rules, map_2-01_vi.frames201 with
verb_value for uppajjati / uppajjittha and their -ti forms) -> map_sample_vi.value6).
Values are the words of the zero-shot translation (build_10-08_vi.py); the translation file is the truth.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import (NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

J = importlib.import_module("map_10-02_vi")        # value1002, ATTR10, citta10, moment10, mulaka10

PART = "10-08-indriyayamaka"

# ---------------------------------------------------------------------------- this chapter's fixed values
T10_08 = {
    # ^6-10-336 «(Ghānandriyamūlakaṃ)»: source slip for Ghānindriyamūlakaṃ (^6-10-346); the translation renders it as
    # meant «(Phần dựa trên năng lực mũi)» (notes-10-08) = mulaka10("Ghānindriyamūlakaṃ")
    "ghānandriyamūlakaṃ": J.mulaka10("Ghānindriyamūlakaṃ"),
    # «ở những người nhập thành tựu thiền chấm dứt» (= 10-03 / 8 / 5-01 PERSONS5; «ở những» frame)
    "nirodhasamāpannānaṃ": J.T5.PERSONS5["nirodhasamāpannānaṃ"],
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


# source slips rendered as meant: the keyword takes the value of the intended form
SLIPS = {
    # ^6-10-361 «asaññasattā cavantāna» = cavantānaṃ (notes-10-08: «những người đang chết đi khỏi cõi Vô Tưởng»)
    "cavantāna": "cavantānaṃ",
}


def value1008(kw, kws, vi, pi):
    k = lc(kw).lower()
    if k in SLIPS:
        return value1008(SLIPS[k], kws, vi, pi)
    if k in T10_08:
        return T10_08[k]
    v = J.T5.moment5(kw, vi)                        # bare uppādakkhaṇe (^6-10-361; = 10-05, map_5-01_vi / map_8_vi)
    if v and len(kw.split()) == 1:
        return v
    return J.value1002(kw, kws, vi, pi, T10_08)


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value1008(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
