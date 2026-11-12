# -*- coding: utf-8 -*-
"""Lookup helper for chapter 6: find a Pāli substring in pi-1 split chapters and print the aligned Hindi line.

usage: python -I -X utf8 pi1_lookup_6.py "<pali substring>" [max_hits] [book]
book: pi-1 (default) or pi-3 / pi-4 / pi-5 (uses <book>-hindi-plain-rails_split_chapters)
"""
import os, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
pat = sys.argv[1]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 3
book = sys.argv[3] if len(sys.argv) > 3 else "pi-1"
P = os.path.join(ROOT, rf"AI_translation\pali\{book}_split_chapters")
H = os.path.join(ROOT, rf"AI_translation\hindi\{book}-hindi-plain-rails_split_chapters")
n = 0
for f in sorted(os.listdir(P)):
    if not f.endswith(".md"):
        continue
    hp = os.path.join(H, f)
    if not os.path.exists(hp):
        continue
    pl = open(os.path.join(P, f), encoding="utf-8-sig").read().splitlines()
    hl = open(hp, encoding="utf-8-sig").read().splitlines()
    for i, l in enumerate(pl):
        if pat in l:
            print(f"== {f}:{i+1}")
            print("P:", l)
            print("H:", hl[i] if i < len(hl) else "<none>")
            n += 1
            if n >= mx:
                sys.exit(0)
print("hits", n)
