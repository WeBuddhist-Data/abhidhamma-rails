"""Show aligned non-empty Pāli / Hindi lines whose Pāli matches a regex: show_3-09.py PALI HINDI REGEX [MAX]."""
import re
import sys

p = [l for l in open(sys.argv[1], encoding="utf-8").read().split("\n") if l.strip()]
h = [l for l in open(sys.argv[2], encoding="utf-8").read().split("\n") if l.strip()]
rx = re.compile(sys.argv[3])
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 30
n = 0
for i, (a, b) in enumerate(zip(p, h)):
    if rx.search(a):
        print(f"[{i + 1}] P: {a}\n     H: {b}\n")
        n += 1
        if n >= mx:
            break
