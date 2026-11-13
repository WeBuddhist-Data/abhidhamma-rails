"""Unique keyword=value pairs (with counts) of the mapped files of map_2-09_3-01_hi.py, for reading by eye.
usage: python -I -B -X utf8 pairs_2-09_3-01_hi.py <file> [<file> …]
"""
import collections
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
for f in sys.argv[1:]:
    c = collections.Counter()
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        if "] " in line:
            for pair in line.split("] ", 1)[1].split(", "):
                c[pair] += 1
    print("=====", f, len(c))
    for p, n in sorted(c.items(), key=lambda x: x[0][:1].lower() + x[0][1:]):
        print(f"{n:4} {p}")
