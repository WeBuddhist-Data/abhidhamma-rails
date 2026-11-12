# -*- coding: utf-8 -*-
"""Helper for chapters 8 and 18: grep the pi-1 Pāli split chapters and print the aligned Hindi line.

usage: python -I -X utf8 grep_pi1_hi_ch8_ch18.py <regex> [max_hits] [book]
book: pi-1 (default), pi-3, pi-4, pi-5 (rails split chapters)
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
book = sys.argv[3] if len(sys.argv) > 3 else "pi-1"
PALI = os.path.join(ROOT, rf"AI_translation\pali\{book}_split_chapters")
HI = os.path.join(ROOT, rf"AI_translation\hindi\{book}-hindi-plain-rails_split_chapters")
pat = re.compile(sys.argv[1])
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 5
n = 0
for f in sorted(os.listdir(PALI)):
    hp = os.path.join(HI, f)
    if not f.endswith(".md") or not os.path.exists(hp):
        continue
    pl = open(os.path.join(PALI, f), encoding="utf-8-sig").read().splitlines()
    hl = open(hp, encoding="utf-8-sig").read().splitlines()
    for i, l in enumerate(pl):
        if pat.search(l):
            print(f"== {f}:{i+1}")
            print("P:", l)
            print("H:", hl[i] if i < len(hl) else "<none>")
            n += 1
            if n >= mx:
                sys.exit(0)
