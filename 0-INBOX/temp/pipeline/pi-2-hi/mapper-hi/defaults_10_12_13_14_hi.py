"""List the keywords of a chapter whose value comes from the PI2 / CH2 defaults (not from my tables or
overrides), with the segments, for a semantic review.

usage: python -I -X utf8 defaults_10_12_13_14_hi.py <chapter>
"""
import collections
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, lc  # noqa
import common_10_12_13_14_hi as C  # noqa

ch = sys.argv[1]
mine = {**C.T_ALL, **C.CHAPTER_T.get(ch, {})}
hi = read_hindi(ch)
seen = collections.defaultdict(list)
for bid, kws in read_keywords(ch):
    for kw in kws:
        if kw in C.OVR.get(ch, {}).get(bid, {}) or lc(kw) in mine:
            continue
        seen[(lc(kw), C.resolve(ch, bid, kw, kws, hi.get(bid)))].append(bid)
for (k, v), bids in sorted(seen.items()):
    print(f"{k}={v}  ({len(bids)}: {' '.join(bids[:3])})")
