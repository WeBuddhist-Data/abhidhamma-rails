"""Print aligned Pāli/Hindi non-empty lines whose Pāli matches a regex.
usage: python -I -X utf8 show-10-05-10-06.py <pali file> <hindi file> <regex> [max]
"""
import re, sys

pa = [l for l in open(sys.argv[1], encoding="utf-8").read().splitlines() if l.strip()]
hi = [l for l in open(sys.argv[2], encoding="utf-8").read().splitlines() if l.strip()]
rx = re.compile(sys.argv[3])
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 40
n = 0
for p, h in zip(pa, hi):
    if rx.search(p):
        print(p)
        print(h)
        print()
        n += 1
        if n >= mx:
            break
