"""Pāli->Vietnamese keyword map, pi-6 chapter 10-10-indriyayamaka (Indriyayamaka, pavattivāra, uppādavāra
(5) paccuppannānāgata: paccanīkapuggalo and paccanīkaokāso, ^6-10-16-4-0 … ^6-10-394).

usage: python -I -X utf8 -B map_10-10_vi.py                  (writes 10-10-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-10_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-10_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Chain: T10_10 -> pacchima kinds (map_10-07_vi.pacchima10: «tâm cuối cùng
<kind>», also inside the moments «khoảnh khắc sinh khởi / tan rã của tâm cuối cùng <kind>» and the samaṅgī persons
«người có được tâm cuối cùng <kind>», as 6-01 / 6-02) -> bare uppādakkhaṇe (map_5-01_vi.moment5, = 10-08) ->
map_10-07_vi.value1007 (T10_07: anantarā, cittassa, sacakkhukā, itthiyo, purisā, Pacchimacittasamaṅgīnaṃ) ->
map_10-02_vi.value1002 (ATTR10, members, mūlaka headings, moment10, map_3-03_vi.value303 with the plane-being position
rule, map_2-01_vi.frames201 with verb_value for uppajjati / uppajjissati and their -ti forms).
upapajjitvā: «sau khi tái sinh» everywhere here; this chapter has no «dassetvā … upapajjitvā» clause (the dassetvā
clauses «sau khi trải qua một số kiếp sống …» have no upapajjitvā), so the 10-07 OVERRIDE case does not arise.
Conventions: as map_10-02_vi.py / map_10-07_vi.py, notes-map-10-01.md, notes-map-10-02.md, notes-map-10-07.md.
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

J = importlib.import_module("map_10-02_vi")        # value1002, ATTR10, citta10, moment10, mulaka10, T5 (5-01)
P = importlib.import_module("map_10-07_vi")        # pacchima10, value1007 (T10_07)

PART = "10-10-indriyayamaka"

# ---------------------------------------------------------------------------- this chapter's fixed values
T10_10 = {
    # «ở những người nhập thành tựu thiền chấm dứt» (= 10-03 / 10-08 / 8 / 5-01 PERSONS5; «ở những» frame)
    "nirodhasamāpannānaṃ": J.T5.PERSONS5["nirodhasamāpannānaṃ"],
}


def pacchima_moment(kw, text):
    """«<X>sampayuttapacchimacittassa uppādakkhaṇe / bhaṅgakkhaṇe» -> «khoảnh khắc sinh khởi / tan rã của tâm cuối
    cùng gắn liền với <X>» (6-01 / 6-02 form). None if not such a keyword."""
    words = kw.split()
    if len(words) != 2:
        return None
    owner = P.pacchima10(words[0])
    if not owner:
        return None
    m = J.C.moment_value(words[1], text)
    return (m + " của " + owner) if m else None


def pacchima_samangi(kw):
    """<X>sampayuttapacchimacittasamaṅgīnaṃ -> «người có được tâm cuối cùng gắn liền với <X>» (6-01 / 6-02:
    avitakkaavicārapacchimacittasamaṅgīnaṃ «người có được tâm cuối cùng …»; «ở những» frame)."""
    k = lc(kw).lower()
    e = "pacchimacittasamaṅgīnaṃ"
    if k.endswith(e) and len(k) > len(e):
        owner = P.pacchima10(k[: -len("samaṅgīnaṃ")] + "ṃ")
        if owner:
            return "người có được " + owner
    return None


def value1010(kw, kws, vi, pi):
    k = lc(kw).lower()
    if k in T10_10:
        return T10_10[k]
    v = pacchima_moment(kw, vi) or pacchima_samangi(kw)
    if v:
        return v
    v = J.T5.moment5(kw, vi)                        # bare uppādakkhaṇe (^6-10-389; = 10-08, map_5-01_vi / map_8_vi)
    if v and len(kw.split()) == 1:
        return v
    return P.value1007(kw, kws, vi, pi)


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
        return value1010(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
