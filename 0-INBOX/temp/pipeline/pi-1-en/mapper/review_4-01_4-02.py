"""Review helper for the 4-01 / 4-02 maps: per lowercased keyword, every value used and its segments.

usage: python -I -X utf8 review_4-01_4-02.py [keyword-regex]
"""
import collections, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
flt = re.compile(sys.argv[1]) if len(sys.argv) > 1 else None
d = collections.defaultdict(lambda: collections.defaultdict(list))
for ch in ("4-01-nikkhepakandam", "4-02-nikkhepakandam"):
    for line in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        for pair in rest.split(", "):
            p, e = pair.rsplit("=", 1)
            d[e.lower()][p].append(bid[3:])
for k in sorted(d):
    if flt and not flt.search(k):
        continue
    vals = d[k]
    s = " | ".join(f"{v} <{len(ids)}: {' '.join(ids[:6])}{' …' if len(ids) > 6 else ''}>" for v, ids in vals.items())
    print(f"{k}: {s}")
