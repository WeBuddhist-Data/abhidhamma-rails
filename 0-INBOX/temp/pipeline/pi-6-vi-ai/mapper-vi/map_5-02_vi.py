"""Pāli->Vietnamese keyword map, pi-6 chapter 5-02-saccayamaka (Saccayamaka, pavattivāra: nirodhavāra and
uppādanirodhavāra).

usage: python -I -X utf8 -B map_5-02_vi.py                  (writes 5-02-saccayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_5-02_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_5-02_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters (loaded with importlib): map_5-01_vi (value501: SACCA, sacca_value,
CITTA_KIND5, moment5, PERSONS5, PATH, NOTES5 …), through it map_2-01_vi (verb_value for every tense keyword, planes,
beings, relatives) and map_8_vi (moments). Resolution: OVERRIDES[bid][kw] -> T.value501(kw, kws, vi, pi, T502).
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-2-01.md, notes-map-8.md, notes-map-5-01.md,
notes-map-5-02.md.
"""
import importlib
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from map_common_vi import (NDE, build_part, en, present, read_keywords, read_pali,  # noqa: E402
                           read_vietnamese, verify)

T = importlib.import_module("map_5-01_vi")          # Saccayamaka frame-setter

PART = "5-02-saccayamaka"

# own table (lower-case keys)
# Editorial notes «(Phần về nơi chốn thì ở sự sinh khởi, ở sự chấm dứt, ở sự sinh khởi và sự chấm dứt đều giống
# nhau …)», «… trong mục về sự sinh khởi và sự chấm dứt cũng nên phân tích như vậy, cả chiều thuận lẫn chiều nghịch»:
# the locative «ở» / «trong» is the case frame (6-01 uppādavāre «mục về sự sinh khởi», 7-01 vare_value), -pi has no
# word of its own (5-01 NOTES5, 3-01 paccuppannepi), «cả … lẫn» is the frame of Xampi Yampi (6-01).
EDITORIAL502 = {
    "uppādepi": "sự sinh khởi", "nirodhepi": "sự chấm dứt",
    "uppādanirodhepi": "sự sinh khởi và sự chấm dứt",
    "uppādavāre": "mục về sự sinh khởi",                       # = 6-01
    "uppādavārepi": "mục về sự sinh khởi",
    "nirodhavārepi": "mục về sự chấm dứt",                     # = 6-01
    "uppādanirodhavārepi": "mục về sự sinh khởi và sự chấm dứt",  # = the heading uppādanirodhavāro (FORMULAS)
    "anulomampi": "chiều thuận", "paccanīkampi": "chiều nghịch",   # = 6-01
    # «… không nên đưa vào trường hợp những người nhập thành tựu thiền chấm dứt» (-nti quote mark; = 6-01)
    "nirodhasamāpannānanti": "người nhập thành tựu thiền chấm dứt",
}
# ^6-5-125 source slip «samudayasaccañca na nirujjhiti» (= na nirujjhati, notes-5-02): «cũng không chấm dứt»; the
# separate na keeps «không» (map_2-01_vi VERB_FORMS («na», pres)); verb_value does not parse the slip
SLIPS502 = {"nirujjhiti": "chấm dứt"}
T502 = {**EDITORIAL502, **SLIPS502}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value502(kw, kws, vi, pi):
    return T.value501(kw, kws, vi, pi, T502)


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value502(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
    return resolve


def dump(only_miss=False, part=PART):
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
