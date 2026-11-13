"""Unique (last Pāli word | last Hindi part) of the Paṭicca-frame items, from the output of items_sample_hi.py.
usage: python -I -B -X utf8 items2_4-15_5-04_hi.py <items-output-file>
"""
import sys, collections, pathlib
c = collections.Counter()
for line in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    if "|" not in line:
        continue
    left, right = line.split("|", 1)
    n, *pw = left.split()
    if not pw:
        continue
    p = pw[-1]
    h = right.strip().split(", ")[-1]
    if len(pw) > 2:
        p = " ".join(pw[1:])
    c[(p, h)] += int(n)
for (p, h), n in sorted(c.items(), key=lambda x: x[0][0].lower()):
    print(f"{n:5} {p} | {h}")
