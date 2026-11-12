"""List unique keywords of a chapter: PI2/CH2 default (or MISSING) and the pi-1/3/4/5 values.

usage: python -I -X utf8 lst_2-3-8-9_hi.py <chapter> [missing-only]
"""
import collections
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PI2, CH2, lc, prior, read_keywords  # noqa: E402

ch = sys.argv[1]
only_missing = len(sys.argv) > 2
cnt = collections.Counter()
for bid, kws in read_keywords(ch):
    for k in kws:
        cnt[lc(k)] += 1
for k, c in sorted(cnt.items()):
    d = PI2.get(k, CH2.get(k, "MISSING"))
    if only_missing and d != "MISSING":
        continue
    pr = prior(k)
    ps = " ;; ".join(f"pi{n}: " + " | ".join(f"{v}({x})" for v, x in cn.most_common(3)) for n, cn in pr.items())
    print(f"{c:3d} {k} = {d} :: {ps}")
