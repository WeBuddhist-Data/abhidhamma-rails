"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 9-02-dhammayamaka (Dhammayamaka: pavattivāra, the nirodhavāra
and uppādanirodhavāra; the heading lines of the paccanīka / anuloma sub-sections).

usage: python -I -X utf8 -B map_9-02_vi.py                  (writes 9-02-dhammayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_9-02_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_9-02_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. The frame-setter is 9-01 (map_9-01_vi.value901: DHAMMA9, dhamma_value, citta9,
moment9, HEAD9; chains map_2-01_vi verb_value, map_2-02_vi, map_5-01_vi, map_8_vi and map_sample_vi.value6).
"""
import importlib
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import NDE, build_part, en, present, read_keywords, read_pali, read_vietnamese, verify  # noqa: E402

D = importlib.import_module("map_9-01_vi")          # the Dhammayamaka frame-setter

PART = "9-02-dhammayamaka"

# «vào khoảnh khắc tan rã của các hiện tượng thiện và bất thiện» (arūpe kusalākusalānaṃ bhaṅgakkhaṇe, ^6-9-169 / 170 /
# 173 / 174): the -ānaṃ form carries «hiện tượng» as 9-01 kusalānaṃ alone = «hiện tượng thiện» (leading «các» dropped);
# pi-2 «thiện và bất thiện» stood beside a separate dhammānaṃ. The moment keyword itself is the extraction placeholder
# «(no direct equivalent)» there (coordinator rule).
T902 = {"kusalākusalānaṃ": D.DHAMMA_NOUN["kusala"] + " và " + D.DHAMMA_ADJ["akusala"]}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value902(kw, kws, vi, pi):
    return D.value901(kw, kws, vi, pi, T902)


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value902(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(only_miss=False, part=PART):
    from collections import Counter
    res, vi = resolver(part), read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v != NDE and not present(v or "???", vi.get(bid, "")):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items(), key=lambda x: (x[0][0], str(x[0][1]))):
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
