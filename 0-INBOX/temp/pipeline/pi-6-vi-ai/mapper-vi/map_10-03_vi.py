"""Pāli->Vietnamese keyword map, pi-6 chapter 10-03-indriyayamaka (Indriyayamaka pavattivāra, uppādavāra (1)
paccuppanna: end of the anulomapuggalokāsā series and the paccanīka (paccanīkapuggalo …) series).

usage: python -I -X utf8 -B map_10-03_vi.py                  (writes 10-03-indriyayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_10-03_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_10-03_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Chain: T10_03 -> map_10-02_vi.value1002 (T10_02 / ATTR10 -> map_10-01_vi
T10_01 -> mulaka10 -> moment10 (citta10 + map_8_vi.moment_value) -> faculty_value -> map_3-03_vi.value303 ->
map_sample_vi.value6). Values are the words of the zero-shot translation (build_10-03_vi.py); the translation file is
the truth.
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

PART = "10-03-indriyayamaka"

# ---------------------------------------------------------------------------- this chapter's fixed values
T10_03 = {
    # ^6-10-206 «Itthīnaṃ ñāṇasampayuttānaṃ uppajjantīnaṃ»: source slip for upapajjantīnaṃ (every parallel has it);
    # the translation renders it as meant «đang tái sinh» (notes-10-03) = ATTR10 upapajjantīnaṃ
    "uppajjantīnaṃ": J.ATTR10["upapajjantīnaṃ"],
    # «ở những người nhập thành tựu thiền chấm dứt» (= map_8_vi / 5-01 / 6-01 / 9-01; «ở những» frame)
    "nirodhasamāpannānaṃ": J.T5.PERSONS5["nirodhasamāpannānaṃ"],
}


def value1003(kw, kws, vi, pi):
    return J.value1002(kw, kws, vi, pi, T10_03)


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
        return value1003(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
