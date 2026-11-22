"""Pāli->Vietnamese keyword map, pi-6 chapter 10-11-indriyayamaka (Indriyayamaka, pavattivāra, uppādavāra
(5) paccuppannānāgata: paccanīkapuggalokāsā, ^6-10-16-6-0 … ^6-10-403).

usage: python -I -X utf8 -B map_10-11_vi.py                  (writes 10-11-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-11_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-11_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Chain: T10_11 -> map_10-10_vi.value1010 (pacchima moments / samaṅgī persons
through map_10-07_vi.pacchima10 «tâm cuối cùng <kind>», bare uppādakkhaṇe, map_10-07_vi.value1007 (T10_07: anantarā,
cittassa, sacakkhukā, itthiyo, purisā), map_10-02_vi.value1002 (ATTR10, members, mūlaka headings, moment10,
map_3-03_vi.value303 with the plane-being position rule, map_2-01_vi.frames201 with verb_value)).
upapajjitvā: «sau khi tái sinh» everywhere here; the dassetvā clauses of this chapter («những người nam đang chết đi
mà sau khi trải qua một số kiếp sống trong chính trạng thái ấy sẽ nhập Niết-bàn trọn vẹn») have no upapajjitvā, so
the 10-07 «dassetvā … upapajjitvā» case (coordinator rule) does not arise.
Conventions: as map_10-02_vi.py / map_10-07_vi.py / map_10-10_vi.py and their notes.
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

P10 = importlib.import_module("map_10-10_vi")      # value1010 (pacchima_moment, pacchima_samangi, value1007)

PART = "10-11-indriyayamaka"

# ---------------------------------------------------------------------------- this chapter's fixed values
T10_11 = {
    # ^6-10-398 «Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ» (Pāli slip for upapajjantānaṃ, as the parallel ^6-10-398
    # (Ka) clauses and 10-10 write): the text has «đang tái sinh là người nam» (2-01 PERSONS upapajjantānaṃ)
    "uppajjantānaṃ": "đang tái sinh",
}


def value1011(kw, kws, vi, pi):
    k = lc(kw).lower()
    if k in T10_11:
        return T10_11[k]
    return P10.value1010(kw, kws, vi, pi)


# per-segment choices (none needed)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value1011(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
