# -*- coding: utf-8 -*-
"""Helper for chapters 12/13: grep the pi-1 (or pi-3/4/5) Pāli split chapters and print the aligned Hindi line.

usage: python -I -X utf8 lookup_pi1_ch12_13.py <book> <regex> [max_hits] [maxchars]
  book: pi-1 | pi-3 | pi-4 | pi-5   (Hindi rails split chapters, lines aligned with the Pāli split chapters)
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
book = sys.argv[1]
pat = re.compile(sys.argv[2])
max_hits = int(sys.argv[3]) if len(sys.argv) > 3 else 3
maxc = int(sys.argv[4]) if len(sys.argv) > 4 else 3000
pdir = os.path.join(ROOT, "AI_translation", "pali", f"{book}_split_chapters")
hdir = os.path.join(ROOT, "AI_translation", "hindi", f"{book}-hindi-plain-rails_split_chapters")
hits = 0
for fn in sorted(os.listdir(pdir)):
    if not fn.endswith(".md"):
        continue
    hp = os.path.join(hdir, fn)
    if not os.path.exists(hp):
        continue
    P = open(os.path.join(pdir, fn), encoding="utf-8-sig").read().splitlines()
    H = open(hp, encoding="utf-8-sig").read().splitlines()
    for i, l in enumerate(P):
        if pat.search(l):
            hits += 1
            h = H[i] if i < len(H) else "<no line>"
            print(f"=== {fn}:{i+1}  (P {len(P)} / H {len(H)} lines)")
            print("PI:", l[:maxc])
            print("HI:", h[:maxc])
            if hits >= max_hits:
                sys.exit(0)
print("hits", hits)
