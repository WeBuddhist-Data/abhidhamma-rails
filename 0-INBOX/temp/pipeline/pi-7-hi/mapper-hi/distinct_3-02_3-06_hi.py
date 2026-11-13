"""Distinct kw=value pairs (with counts) in my mapped files; keywords with more than one value first.
usage: python -I -B -X utf8 distinct_3-02_3-06_hi.py [multi|all]
"""
import collections, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
FILES = ["3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka", "3-05-ganthagocchaka",
         "3-06-oghayogagocchaka"]
by = collections.defaultdict(collections.Counter)
for f in FILES:
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        if "] " in line:
            for pair in line.split("] ", 1)[1].split(", "):
                k, v = pair.split("=", 1)
                by[k[:1].lower() + k[1:]][v] += 1
mode = sys.argv[1] if len(sys.argv) > 1 else "multi"
for k in sorted(by):
    c = by[k]
    if mode == "all" or len(c) > 1:
        print(k, "->", "; ".join(f"{v} ({n})" for v, n in c.most_common()))
