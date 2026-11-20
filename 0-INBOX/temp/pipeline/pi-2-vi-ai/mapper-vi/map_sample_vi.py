"""Build the SAMPLE Pāli->Vietnamese keyword maps for pi-2: preamble, 1-khandhavibhango.

usage: python -I -X utf8 map_sample_vi.py              (writes the two <part>.mapped.md and verifies them)
       python -I -X utf8 map_sample_vi.py dump PART [miss]   (every distinct keyword=value with count and first
                                                              segments; with «miss» only presence misses; writes nothing)

Resolution order per keyword: OVERRIDES[bid][kw] -> context() (segment rules) -> SAMPLE (this part's table)
-> map_common_vi.value(): KH (pi-2 table) -> the approved pi-1 chain (pi1_value).
Conventions: pi-1 vi-map-conventions.md + notes-map-*.md, and vi-map-conventions-pi2.md.
"""
import pathlib
import sys
from collections import Counter

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import (CORE, GAP, NDE, build_part, lc, present, read_keywords,  # noqa: E402
                           read_vietnamese, value, verify)

PARTS = ["preamble", "1-khandhavibhango"]

SAMPLE = {}

OVERRIDES = {
    # «có loại khi tiếp xúc thì dễ chịu / khó chịu» (sukhasamphassaṃ / dukkhasamphassaṃ); sukha stays «hạnh phúc»
    # (first in the segment: na sukhasahagataṃ «không có hạnh phúc đi kèm»; the Russian map chose the same)
    "2-33": {"dukkha": "khó chịu"},
}


def context(bid, kw, k, s, text):
    """Segment rules (k: lower-cased keyword, s: lower-cased keyword set). None = no rule."""
    if k == "ārammaṇo":       # stem of …ārammaṇo: «có đối tượng …»; only maggārammaṇo in the segment: «lấy … làm đối tượng»
        return "có đối tượng" if present("có đối tượng", text) else "lấy" + GAP + "làm đối tượng"
    if k == "hetuko":         # sa-/ahetuko, pahātabbahetuko «có gốc rễ»; only maggahetuko: «lấy … làm gốc rễ»
        return "có gốc rễ" if present("có gốc rễ", text) else "lấy" + GAP + "làm gốc rễ"
    return None


def resolver_for(part):
    vi = read_vietnamese(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        k = lc(kw)
        if part == "preamble" and k in CORE:      # the pi-1 preamble values (Namo … sammāsambuddhassa)
            return CORE[k]
        s = set(lc(x) for x in kws)
        text = vi.get(bid, "")
        v = context(bid, kw, k, s, text)
        if v is not None:
            return v
        return value(kw, kws, SAMPLE, text)
    return resolve


def dump(part, only_miss=False):
    res = resolver_for(part)
    vi = read_vietnamese(part)
    c, miss, where = Counter(), Counter(), {}
    for bid, kws in read_keywords(part):
        for kw in kws:
            try:
                v = res(bid, kw, kws)
            except KeyError:
                v = "???"
            c[(kw, v)] += 1
            where.setdefault((kw, v), []).append(bid)
            if v == "???" or (v != NDE and not present(v, vi.get(bid, ""))):
                miss[(kw, v)] += 1
    for (kw, v), n in sorted(c.items()):
        m = miss.get((kw, v), 0)
        if only_miss and not m:
            continue
        print(f"{kw}={v}  [{n}] {where[(kw, v)][:5]}" + (f"  MISS {m}" if m else ""))


if __name__ == "__main__":
    if sys.argv[1:2] == ["dump"]:
        dump(sys.argv[2], len(sys.argv) > 3)
    else:
        for p in PARTS:
            build_part(p, resolver_for(p))
            verify(p)
