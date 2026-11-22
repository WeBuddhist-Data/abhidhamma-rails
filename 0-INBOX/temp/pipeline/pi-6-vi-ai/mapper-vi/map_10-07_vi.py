"""Pāli->Vietnamese keyword map, pi-6 chapter 10-07-indriyayamaka (Indriyayamaka, pavattivāra, uppādavāra
(3) anāgata: paccanīkapuggalokāsā, ^6-10-14-6-0 … ^6-10-334).

usage: python -I -X utf8 -B map_10-07_vi.py                  (writes 10-07-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-07_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-07_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Chain: T10_07 -> map_10-02_vi.value1002 (ATTR10 / BEINGS_ATTR, map_10-01_vi
members and mūlaka headings, map_3-03_vi.value303 with the plane-being position rule, map_2-01_vi.frames201 with
verb_value for uppajjissati / uppajjissatīti, PERSONS: pacchimabhavikānaṃ, upapajjitvā, parinibbāyissanti).
Pacchima citta kinds (upekkhāsampayuttapacchimacittaṃ …) are not parsed by citta10: their word order is taken from
the segment («tâm cuối cùng gắn liền với sự bình thản»), as 8 / 6-01 do («tâm cuối cùng <kind>»).
Conventions: as map_10-02_vi.py, plus notes-map-10-02.md, notes-map-6-01.md (anantarā, Pacchimacittasamaṅgīnaṃ).
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

J = importlib.import_module("map_10-02_vi")        # value1002, citta10, ATTR10, CITTA_MEMBER, CITTA_ASSOC
C8 = importlib.import_module("map_8_vi")           # KIND pacchima «cuối cùng»

PART = "10-07-indriyayamaka"


# ---------------------------------------------------------------------------- pacchima citta kinds
def pacchima10(kw):
    """<X>sampayuttapacchimacittaṃ -> «tâm cuối cùng gắn liền với <X>» (the segment's order: «tâm cuối cùng» first,
    then the association, as 6-01 «tâm cuối cùng <kind>»). None if not such a word."""
    k = lc(kw).lower()
    for e in ("pacchimacittaṃ", "pacchimacittassa", "pacchimacitte"):
        if k.endswith(e) and len(k) > len(e):
            pre = k[: -len(e)]
            kind = J._kind_chain(pre)
            if kind:
                return "tâm " + C8.KIND["pacchima"] + " " + kind
    return None


# ---------------------------------------------------------------------------- this chapter's fixed values
T10_07 = {
    "pacchimacittasamaṅgīnaṃ": "người có được tâm cuối cùng",   # 5-01 / 6-01 / 8 / 9-01
    "anantarā": "ngay sau",                                       # «Vào tâm mà ngay sau đó …» (6-01 / 5-01 / 9-01)
    "cittassa": "tâm",                                            # yassa cittassa «Vào tâm mà …» (citta10)
    "sacakkhukā": "có mắt",                                       # nominative of sacakkhukānaṃ (3-01 ATTR)
    "itthiyo": J.ATTR10["itthiyo"], "purisā": J.ATTR10["purisā"],  # «những người nữ / nam nào …» (10-02 proposal)
}

# per-segment choices: upapajjitvā after a second gerund shares its «sau khi» («những người nam nào sau khi trải qua
# một số kiếp sống trong chính trạng thái ấy và tái sinh có niềm vui đi kèm …»): the segment has «tái sinh» only
OVERRIDES = {
    "6-10-328": {"upapajjitvā": "tái sinh"},
    "6-10-329": {"upapajjitvā": "tái sinh"},
}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value1007(kw, kws, vi, pi):
    k = lc(kw).lower()
    if k in T10_07:
        return T10_07[k]
    v = pacchima10(kw)
    if v:
        return v
    return J.value1002(kw, kws, vi, pi)


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value1007(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
