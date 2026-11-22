"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 9-03-dhammayamaka (Dhammayamaka: the last headings of the
uppādavāra, the rest of the uppādanirodhavāra (atītānāgata), the bhāvanāvāra and the yamaka closer).

usage: python -I -X utf8 -B map_9-03_vi.py                  (writes 9-03-dhammayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_9-03_vi.py dump [miss]      (every distinct keyword=value with count; writes nothing)
       python -I -X utf8 -B map_9-03_vi.py show lo hi [pi]  (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setter: map_9-01_vi (value901: members DHAMMA9 / dhamma_value, moments,
citta kinds, bhavana_value; through it map_5-01_vi, map_2-01_vi.verb_value for every uppajjati / nirujjhati keyword,
map_8_vi, map_sample_vi.value6). pajahati and its tenses: map_5-03_vi.pajahati_value (coordinator: the parijānāti
templates of 2-02, first-occurrence polarity; bhāveti follows the same templates through 9-01 bhavana_value).
Resolution: OVERRIDES[bid][kw] -> T903 -> pajahati_value -> map_9-01_vi.value901(kw, kws, vi, pi, T903).
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes-map-*.md, pi-5 map-coordinator-rules.md,
vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md, notes-map-9-01.md, notes-map-5-03.md, notes-map-6-02.md.
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

D = importlib.import_module("map_9-01_vi")          # Dhammayamaka frame-setter
J = importlib.import_module("map_5-03_vi")          # pajahati tenses (pajahati_value)

PART = "9-03-dhammayamaka"

# ---------------------------------------------------------------------------- own table (lower-case keys)
T903 = {
    # closer «Phần các cặp câu hỏi về các hiện tượng đã hoàn tất.» (lower case as written, = 6-02 / 5-03 closers)
    "dhammayamakaṃ": D.HEAD9["dhammayamakapāḷi"],
}

# per-segment choices
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value903(kw, kws, vi, pi):
    k = lc(kw).lower()
    for x in (kw, lc(kw), k):
        if x in T903:
            return T903[x]
    v = J.pajahati_value(kw, pi)
    if v is not None:
        return v
    return D.value901(kw, kws, vi, pi, T903)


def resolver(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value903(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
