"""Audit a mapped pi-2 chapter: every keyword with the distinct values it got (and the segments).

usage: python -I -X utf8 audit_1-khandhavibhango_hi.py <chapter> [only-multi]
"""
import collections
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ch = sys.argv[1]
only_multi = len(sys.argv) > 2
vals = collections.defaultdict(lambda: collections.defaultdict(list))
for line in (HERE / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
    bid, rest = line.split("] ", 1)
    for pair in rest.split(", "):
        k, v = pair.split("=", 1)
        vals[k[:1].lower() + k[1:]][v].append(bid[1:])
for k in sorted(vals):
    d = vals[k]
    if only_multi and len(d) < 2:
        continue
    print(k, "::", " | ".join(f"{v} ({len(b)}{': ' + ' '.join(b[:4]) if len(d) > 1 else ''})" for v, b in d.items()))
