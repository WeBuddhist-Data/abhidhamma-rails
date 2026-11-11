"""Print Pāli/Hindi line pairs from two aligned split chapters, filtered by a regex on the Pāli.

usage: python -I -X utf8 align.py <pali_file> <hindi_file> <regex> [max]
"""
import re, sys

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(p):
    out, buf = [], []
    for line in open(p, encoding="utf-8").read().splitlines():
        if not line.strip():
            continue
        buf.append(line)
        if ID.search(line):
            out.append(buf)
            buf = []
    return out


a, b = segs(sys.argv[1]), segs(sys.argv[2])
rx = re.compile(sys.argv[3])
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 200
n = 0
for sa, sb in zip(a, b):
    for x, y in zip(sa, sb):
        if rx.search(x):
            w = int(sys.argv[5]) if len(sys.argv) > 5 else 10000
            print("P:", x[:w])
            print("H:", y[:w])
            n += 1
            if n >= mx:
                sys.exit()
