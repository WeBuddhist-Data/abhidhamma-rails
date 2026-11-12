# -*- coding: utf-8 -*-
"""Helper for chapter 17: print Pāli line(s) of an earlier book containing a pattern and the aligned Hindi rails line.
usage: python -I -X utf8 khuddaka17_pi1lookup.py <regex> [maxhits] [book, default pi-1]
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
book = sys.argv[3] if len(sys.argv) > 3 else "pi-1"
P = os.path.join(ROOT, r"AI_translation\pali", book + "_split_chapters")
H = os.path.join(ROOT, r"AI_translation\hindi", book + "-hindi-plain-rails_split_chapters")
pat = re.compile(sys.argv[1])
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 3
hits = 0
for f in sorted(os.listdir(P)):
    if not f.endswith(".md") or not os.path.exists(os.path.join(H, f)):
        continue
    pl = open(os.path.join(P, f), encoding="utf-8-sig").read().splitlines()
    hl = open(os.path.join(H, f), encoding="utf-8-sig").read().splitlines()
    pn = [l for l in pl if l.strip()]
    hn = [l for l in hl if l.strip()]
    if len(pn) != len(hn):
        print("WARN line count", f, len(pn), len(hn))
    for i, l in enumerate(pn):
        if pat.search(l):
            print("==", f, i)
            print("P:", l)
            print("H:", hn[i] if i < len(hn) else "?")
            hits += 1
            if hits >= mx:
                sys.exit(0)
