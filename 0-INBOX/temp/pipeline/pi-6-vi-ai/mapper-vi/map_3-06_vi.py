"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 3-06-ayatanayamaka (Āyatanayamaka, end of the pavatti section:
atītānāgatavāra / paccuppannānāgatavāra … of the uppādanirodhavāra, the pariññāvāra and the yamaka closer).

usage: python -I -X utf8 -B map_3-06_vi.py                (writes 3-06-ayatanayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_3-06_vi.py dump [miss]     (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_3-06_vi.py show lo hi [pi] (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters: map_3-05_vi.value305 (chaining 3-04 … 3-01 and 2-01, incl. the
Itaresaṃ + plane-being rule of map_3-03_vi and verb_value for every uppajjati / nirujjhati tense keyword),
map_2-02_vi (parinna_value and PARINNA_PERSONS for the pariññāvāra; the yamaka closer as HEAD202 maps
Khandhayamakapāḷi).
Resolver: OVERRIDES -> T3_06 (this chapter) -> map_2-02_vi.parinna_value (pariññā verbs) -> map_2-02_vi
PARINNA_PERSONS (pariññāvāra segments only) -> map_3-05_vi.value305.
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes, vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md,
notes-map-3-01.md … notes-map-3-06.md, notes-map-2-02.md.
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

A35 = importlib.import_module("map_3-05_vi")
P = importlib.import_module("map_2-02_vi")
K = importlib.import_module("map_2-01_vi")

PART = "3-06-ayatanayamaka"

# the pariññāvāra segments (person subjects take PARINNA_PERSONS there)
PARINNA_IDS = {f"6-3-{n}" for n in range(249, 255)}

# ---------------------------------------------------------------------------- this chapter's own values
T3_06 = {
    # ^6-3-212 source slip «no ca tesaṃ ghānāyatanaṃ upapajjissati» (= uppajjissati; the text renders it as meant:
    # «nhưng ở những người ấy lĩnh vực mũi sẽ không sinh khởi»): the 2-01 noca_pos future template, as verb_value
    # gives uppajjissati in that clause
    "upapajjissati": K.verb_vi("uppajj", "fut", "noca_pos"),
    # ^6-3-248 «(… đã được phân tích trong mục về sự chấm dứt …)» (= 5-03 / 6-02)
    "nirodhavāre": "mục về sự chấm dứt",
    # ^6-3-248 «cả phần về người, phần về nơi chốn lẫn phần về người và nơi chốn»: standalone yatthakampi = the 2-02 /
    # 3-05 yatthakaṃ value (3-04 / 3-05 «phần về người và nơi chốn» was «Yassa yatthakampi» written as two words)
    "yatthakampi": "phần về nơi chốn",
    # ^6-3-254 closer «Phần các cặp câu hỏi về các lĩnh vực nhận biết đã hoàn tất.»: lower case as written, «Phần» frame
    # (= 2-02 Khandhayamakapāḷi, 5-03 Saccayamakaṃ; the 3-01 heading has «Các …»)
    "āyatanayamakaṃ": "các cặp câu hỏi về các lĩnh vực nhận biết",
}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value306(kw, kws, vi, pi, bid=""):
    k = lc(kw).lower()
    if kw in T3_06:
        return T3_06[kw]
    if k in T3_06:
        return T3_06[k]
    v = P.parinna_value(kw, pi)
    if v is not None:
        return v
    if bid in PARINNA_IDS and k in P.PARINNA_PERSONS:
        return P.PARINNA_PERSONS[k]
    return A35.value305(kw, kws, vi, pi)


def resolver_for(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value306(kw, kws, vi.get(bid, ""), pi.get(bid, ""), bid)
    return resolve


def dump(part=PART, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError as e:
                v = f"KEYERROR {e}"
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
    res = resolver_for(part)
    vi, pi = read_vietnamese(part), read_pali(part)
    for i, (bid, kws) in enumerate(read_keywords(part)):
        if lo <= i < hi:
            print(f"== {i} [{bid}]")
            if with_pali:
                print(f"-- PI {pi.get(bid, '')}")
            print(f"-- VI {vi.get(bid, '')}")
            out = []
            for kw in kws:
                try:
                    v = res(bid, kw, kws)
                except KeyError as e:
                    v = f"KEYERROR {e}"
                flag = "" if v == NDE or present(v, vi.get(bid, "")) else " <<MISS"
                out.append(f"{kw}={v}{flag}")
            print("   " + " | ".join(out))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(PART, sys.argv[2:3] == ["miss"])
    elif sys.argv[1:2] == ["show"]:
        show(int(sys.argv[2]), int(sys.argv[3]), "pi" in sys.argv[4:])
    else:
        build_part(PART, resolver_for(PART))
        verify(PART, ALLOWED)
