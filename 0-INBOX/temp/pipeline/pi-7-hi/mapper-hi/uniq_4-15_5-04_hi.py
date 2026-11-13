"""Unique keyword=value pairs of mapped files (with counts), for reading by eye.
usage: python -I -B -X utf8 uniq_4-15_5-04_hi.py <file> [<file> …]
"""
import collections, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
c = collections.Counter()
for f in sys.argv[1:]:
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        _, _, rest = line.partition("] ")
        for pair in rest.split(", ") if rest else []:
            kw, v = pair.split("=", 1)
            c[(kw, v)] += 1
for (kw, v), n in sorted(c.items(), key=lambda x: (x[0][0].lower(), x[0][1])):
    if "-कारण" in v and "वर्गीकरण" not in v:
        continue
    print(f"{n:4} {kw} = {v}")
