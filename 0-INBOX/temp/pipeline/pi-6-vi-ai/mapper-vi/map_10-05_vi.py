"""Pāli->Vietnamese keyword map, pi-6 chapter 10-05-indriyayamaka (Indriyayamaka pavattivāra, uppādavāra:
(2) atīta «uppajjittha» and (3) anāgata «uppajjissati», with the paccanīka headings).

usage: python -I -X utf8 -B map_10-05_vi.py                  (writes 10-05-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-05_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-05_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. value1005(kw, kws, vi, pi) = T10_05 -> map_10-02_vi.value1002 (T10_02 ->
map_10-01_vi.T10_01 -> mulaka10 -> moment10 -> faculty_value -> map_3-03_vi.value303 -> map_sample_vi.value6).
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

PART = "10-05-indriyayamaka"

# ---------------------------------------------------------------------------- pacchima citta kinds (anāgata)
# «Vào tâm mà ngay sau đó tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi» (^6-10-285 … 287): «tâm cuối cùng
# <kind>» (coordinator rule: map_10-07_vi.pacchima10).
# upapajjitvā: «sau khi tái sinh» here; the «dassetvā … upapajjitvā» clause («… và tái sinh có niềm vui đi kèm», where
# «tái sinh» alone would be the value, 10-07) comes after a plain «Ye … upapajjitvā» in every segment of this chapter
# (^6-10-281 … 284), so the first-rendering rule keeps «sau khi tái sinh» and no override is needed.
P7 = importlib.import_module("map_10-07_vi")
pacchima10 = P7.pacchima10


T10_05 = {
    # «Những người nào sau khi tái sinh có mắt và có sự bình thản đi kèm sẽ nhập Niết-bàn trọn vẹn» (^6-10-281):
    # nominative plural of sacakkhuka (map_3-01_vi.ATTR sacakkhukānaṃ «có mắt»; «Những … nào» = ye, frame)
    "sacakkhukā": "có mắt",
}

OVERRIDES = {}
ALLOWED = {}


def value1005(kw, kws, vi, pi):
    k = lc(kw).lower()
    if k in T10_05:
        return T10_05[k]
    if " " not in kw:
        v = pacchima10(kw)
        if v:
            return v
        v = J.T5.moment5(kw, vi)                    # bare uppādakkhaṇe (map_5-01_vi / map_8_vi.moment_value)
        if v:
            return v
        v = J.citta10(kw)
        if v:
            return v
    return J.value1002(kw, kws, vi, pi, T10_05)


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value1005(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
