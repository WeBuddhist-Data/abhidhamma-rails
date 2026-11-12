# -*- coding: utf-8 -*-
"""Show aligned pi-1 Pāli / Hindi (rails) lines whose Pāli matches a regex.

usage: python -I -X utf8 kwic_3_14_15_hi.py <regex> [max_hits] [--book pi-3]
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
book = "pi-1"
args = [a for a in sys.argv[1:]]
if "--book" in args:
    i = args.index("--book"); book = args[i + 1]; del args[i:i + 2]
PDIR = os.path.join(ROOT, r"AI_translation\pali", book + "_split_chapters")
HDIR = os.path.join(ROOT, r"AI_translation\hindi", book + "-hindi-plain-rails_split_chapters")
rx = re.compile(args[0])
mx = int(args[1]) if len(args) > 1 else 5


def lines(p):
    return [l for l in open(p, encoding="utf-8-sig").read().splitlines() if l.strip()]


n = 0
for f in sorted(os.listdir(PDIR)):
    if not f.endswith(".md"):
        continue
    hp = os.path.join(HDIR, f)
    if not os.path.exists(hp):
        continue
    P, H = lines(os.path.join(PDIR, f)), lines(hp)
    if len(P) != len(H):
        continue
    for k, (p, h) in enumerate(zip(P, H)):
        if rx.search(p):
            print(f"=== {f}:{k}\nP: {p}\nH: {h}\n")
            n += 1
            if n >= mx:
                sys.exit(0)
