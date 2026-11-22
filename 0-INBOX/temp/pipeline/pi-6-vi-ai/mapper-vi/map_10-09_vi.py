"""Pāli->Vietnamese keyword map, pi-6 chapter 10-09-indriyayamaka (Indriyayamaka, pavattivāra, uppādavāra
(5) paccuppannānāgatavāra: (Ka) anulomapuggalo, (Kha) anulomaokāso, (Ga) anulomapuggalokāsā; «uppajjati» /
«uppajjissati» in one pair question).

usage: python -I -X utf8 -B map_10-09_vi.py                  (writes 10-09-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-09_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-09_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Chain: T10_09 -> pacchima10 (also inside the moment keywords) ->
map_10-02_vi.value1002 (T10_02 / ATTR10 -> map_10-01_vi.T10_01 -> mulaka10 -> moment10 -> faculty_value ->
map_3-03_vi.value303 with the plane-being position and Itaresaṃ rules -> map_2-01_vi.frames201 with verb_value for
uppajjati / uppajjissati and their -ti forms -> map_sample_vi.value6).
Pacchima citta kinds (somanassasampayuttapacchimacittaṃ …) are not parsed by citta10: their word order is the
segment's «tâm cuối cùng gắn liền với niềm vui» (as 10-05 / 10-06 / 10-07, 8 / 6-01 «tâm cuối cùng <kind>»); the
moment keyword «Somanassasampayuttapacchimacittassa uppādakkhaṇe» = «khoảnh khắc sinh khởi của tâm cuối cùng gắn liền
với niềm vui» (moment10 with that owner).
Conventions: as map_10-02_vi.py, plus notes-map-10-01 … 10-04.md, map_10-05 … 10-07_vi.py, notes-map-6-01.md
(anantarā «ngay sau»), notes-map-8.md (moments, «tâm cuối cùng»).
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

J = importlib.import_module("map_10-02_vi")        # value1002, ATTR10, BEINGS_ATTR, C (map_8_vi), T5 (map_5-01_vi)
J7 = importlib.import_module("map_10-07_vi")       # pacchima10 «tâm cuối cùng <kind>» (coordinator rule)

PART = "10-09-indriyayamaka"

# ---------------------------------------------------------------------------- pacchima citta kinds
pacchima10 = J7.pacchima10        # <X>sampayuttapacchimacittaṃ -> «tâm cuối cùng gắn liền với <X>»


def pacchima_moment(kw, text):
    """«Somanassasampayuttapacchimacittassa uppādakkhaṇe» -> «khoảnh khắc sinh khởi của tâm cuối cùng gắn liền với
    niềm vui» (moment10 with the pacchima owner; «Vào» frame). None if not such a keyword."""
    words = kw.split()
    if len(words) != 2:
        return None
    owner = pacchima10(words[0])
    if not owner:
        return None
    m = J.C.moment_value(words[1], text)
    return (m + " của " + owner) if m else None


# ---------------------------------------------------------------------------- this chapter's fixed values
T10_09 = {
    "anantarā": "ngay sau",                                       # «tâm mà ngay sau đó …» (6-01 / 10-05 … 10-07)
    "sacakkhukā": J.BEINGS_ATTR["sacakkhukānaṃ"],                 # «có mắt» (10-05 / 10-06 / 10-07)
    "itthiyo": J.ATTR10["itthiyo"], "purisā": J.ATTR10["purisā"],  # «những người nữ / nam …» (10-07)
    # «ở những người nhập thành tựu thiền chấm dứt» (10-03 T10_03 = map_5-01_vi.PERSONS5; «ở những» frame)
    "nirodhasamāpannānaṃ": J.T5.PERSONS5["nirodhasamāpannānaṃ"],
}


def value1009(kw, kws, vi, pi):
    k = lc(kw).lower()
    if k in T10_09:
        return T10_09[k]
    v = pacchima_moment(kw, vi)
    if v:
        return v
    v = pacchima10(kw)
    if v:
        return v
    return J.value1002(kw, kws, vi, pi)


# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value1009(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
