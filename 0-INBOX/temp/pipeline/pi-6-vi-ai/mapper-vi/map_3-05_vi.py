"""Pāli->Vietnamese keyword map, pi-6 (Yamaka) chapter 3-05-ayatanayamaka (Āyatanayamaka, pavatti: uppādanirodhavāra).

usage: python -I -X utf8 -B map_3-05_vi.py                (writes 3-05-ayatanayamaka.mapped.md and verifies it)
       python -I -X utf8 -B map_3-05_vi.py dump [miss]     (every distinct keyword=value; writes nothing)
       python -I -X utf8 -B map_3-05_vi.py show lo hi [pi] (segments lo..hi with their pairs; writes nothing)

Importing this module builds nothing. Frame-setters: map_3-04_vi (value304: uppāde- / nirodhe-pi, -vārepi values,
nirujjhatī) chaining map_3-03_vi.value303 (Itaresaṃ + plane-being rule -> map_3-02_vi.value302 -> map_3-01_vi.value3 /
map_2-01_vi.frames201 with verb_value).
Resolver: OVERRIDES -> T3_05 (this chapter) -> map_3-04_vi.value304.
Conventions: pi-1 … pi-5 vi-map-conventions*.md + notes, vi-map-conventions-pi6.md, pi-6 map-coordinator-rules.md,
notes-map-3-01.md … notes-map-3-05.md.
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

A34 = importlib.import_module("map_3-04_vi")
K = importlib.import_module("map_2-01_vi")

PART = "3-05-ayatanayamaka"

# ---------------------------------------------------------------------------- this chapter's own values
T3_05 = {
    # ^6-3-172 «Kāmāvacare parinibbāntānaṃ» (spelling slip for parinibbantānaṃ) «những người đang nhập Niết-bàn trọn vẹn
    # trong cõi dục lạc» = the 2-01 participle value
    "parinibbāntānaṃ": "đang nhập Niết-bàn trọn vẹn",
    # ^6-3-201 (yatthakaṃ itaresaṃ yatthakānaṃ sadisaṃ kātabbaṃ, yatthakaṃ tīsupi vāresu sadisaṃ) «… giống như các phần về
    # nơi chốn khác, phần về nơi chốn thì giống nhau trong cả ba mục»: leading «các» frame (= map_6-02_vi yatthakānaṃ);
    # vāresu = mục (FORMULAS vāro = mục; «trong cả ba» = the locative and tīsupi)
    "yatthakānaṃ": "phần về nơi chốn", "vāresu": "mục",
    # ^6-3-209 (Yassakampi yassayatthakampi sadisaṃ) «(Phần về người và phần về người và nơi chốn đều giống nhau)»
    # (= 5-01 / 5-02 / 6-01)
    "yassakampi": "phần về người", "yassayatthakampi": "phần về người và nơi chốn",
}

# per-segment choices (read from the segments)
OVERRIDES = {}

# presence-check exceptions: (id, keyword) -> reason
ALLOWED = {}


def value305(kw, kws, vi, pi):
    k = lc(kw).lower()
    if k in T3_05:
        return T3_05[k]
    return A34.value304(kw, kws, vi, pi)


def resolver_for(part=PART):
    vi, pi = read_vietnamese(part), read_pali(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        return value305(kw, kws, vi.get(bid, ""), pi.get(bid, ""))
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
