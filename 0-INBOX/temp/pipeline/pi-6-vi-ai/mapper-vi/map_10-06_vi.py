"""Pāli->Vietnamese keyword map, pi-6 chapter 10-06-indriyayamaka (Indriyayamaka pavattivāra, uppādavāra (3)
anāgata: anulomaokāso, anulomapuggalokāsā, paccanīkapuggalo, paccanīkaokāso; future «sẽ sinh khởi»).

usage: python -I -X utf8 -B map_10-06_vi.py                  (writes 10-06-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-06_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-06_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Chain: T10_06 -> map_10-07_vi.pacchima10 -> upapajjitva -> map_10-02_vi.value1002
(T10_02 -> T10_01 -> mulaka10 -> moment10 -> faculty_value -> map_3-03_vi.value303 -> … map_2-01_vi.frames201 with
verb_value -> value6).
    pacchima10(word)     = map_10-07_vi.pacchima10: <X>sampayuttapacchimacittaṃ -> «tâm cuối cùng gắn liền với <X>»
                         (the segment: «Vào tâm mà ngay sau đó tâm cuối cùng gắn liền với sự bình thản sẽ sinh khởi»)
    upapajjitva(pi)      «tái sinh» when the first upapajjitvā of the segment follows dassetvā in its clause (the one
                         «sau khi» belongs to dassetvā, coordinator / 10-07); else None (-> «sau khi tái sinh»)
Conventions: notes-map-10-01.md, notes-map-10-02.md, map-coordinator-rules.md, notes-map-6-01.md, notes-map-8.md.
"""
import importlib
import pathlib
import re
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import (NDE, build_part, en, lc, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

J = importlib.import_module("map_10-02_vi")         # value1002, citta10 parts (CITTA_MEMBER / CITTA_ASSOC)
K = importlib.import_module("map_2-01_vi")          # verb_vi (the pavatti verb templates)

PART = "10-06-indriyayamaka"

J7 = importlib.import_module("map_10-07_vi")        # pacchima10 (coordinator: «tâm cuối cùng <kind>»)
pacchima10 = J7.pacchima10


def upapajjitva(pi):
    """upapajjitvā (coordinator rule, 10-07): «tái sinh» where its first occurrence in the Pāli segment shares the one
    «sau khi» with a preceding dassetvā in the same clause («những người nữ nào sau khi trải qua một số kiếp sống trong
    chính trạng thái ấy và tái sinh có sự bình thản đi kèm …»); elsewhere «sau khi tái sinh» (2-01 PERSONS)."""
    m = re.search(r"(?<!\w)upapajjitvā(?!\w)", pi)
    if not m:
        return None
    clause = re.split(r"[.?!,;\n]", pi[: m.start()])[-1]
    clause = re.split(r"(?<!\w)(?:ye|yā) ca(?!\w)|(?<!\w)(?:Ye|Yā)(?!\w)", clause)[-1]
    return "tái sinh" if re.search(r"(?<!\w)dassetvā(?!\w)", clause) else None


# ---------------------------------------------------------------------------- this chapter's fixed values
T10_06 = {
    # «Ở người nào có tâm cuối cùng …»: the 5-01 / 6-01 / 8 / 9-01 value; Pacchimacittasamaṅgīna = the same word with
    # the anusvāra dropped in the Pāli (^6-10-314, line «Pacchimacittasamaṅgīna tesaṃ …»)
    "pacchimacittasamaṅgīnaṃ": "người có được tâm cuối cùng",
    "pacchimacittasamaṅgīna": "người có được tâm cuối cùng",
    # nominative attribute («Ye sacakkhukā upekkhāya upapajjitvā …» «Những người nào sau khi tái sinh có mắt và có
    # sự bình thản đi kèm …»): = the genitive sacakkhukānaṃ «có mắt» (map_3-01_vi.ATTR); «và» joins, frame
    "sacakkhukā": J.BEINGS_ATTR["sacakkhukānaṃ"],
    # ^6-10-309 source slip «no ca tesaṃ somanassindriyaṃ na upapajjissati» (= uppajjissati; the text renders it as
    # meant: «nhưng ở những người ấy năng lực niềm vui vẫn sẽ sinh khởi»): its own clause is «no ca … na», the 2-01
    # noca_neg future template (3-06 has the same slip without «na»: noca_pos «sẽ … sinh khởi»)
    "upapajjissati": K.verb_vi("uppajj", "fut", "noca_neg"),
}


def value1006(kw, kws, vi, pi, table=None):
    """your table -> T10_06 -> pacchima10 -> map_10-02_vi.value1002."""
    k = lc(kw).lower()
    if table:
        for x in (kw, lc(kw), k):
            if x in table:
                return table[x]
    if k in T10_06:
        return T10_06[k]
    v = pacchima10(kw)
    if v:
        return v
    if k == "upapajjitvā":
        v = upapajjitva(pi)
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
        return value1006(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
