# -*- coding: utf-8 -*-
"""Batch lookup for chapters 12/13: each line of the pattern file is "<books>|<regex>" (books comma-separated,
e.g. pi-1,pi-4). Prints the first hit (Pāli + aligned Hindi line) per pattern.

usage: python -I -X utf8 lookup_batch_ch12_13.py <patternfile> [maxchars]
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
maxc = int(sys.argv[2]) if len(sys.argv) > 2 else 1800
cache = {}


def load(book):
    if book in cache:
        return cache[book]
    pdir = os.path.join(ROOT, "AI_translation", "pali", f"{book}_split_chapters")
    hdir = os.path.join(ROOT, "AI_translation", "hindi", f"{book}-hindi-plain-rails_split_chapters")
    out = []
    for fn in sorted(os.listdir(pdir)):
        hp = os.path.join(hdir, fn)
        if not fn.endswith(".md") or not os.path.exists(hp):
            continue
        P = open(os.path.join(pdir, fn), encoding="utf-8-sig").read().splitlines()
        H = open(hp, encoding="utf-8-sig").read().splitlines()
        for i, l in enumerate(P):
            out.append((f"{book}/{fn}:{i+1}", l, H[i] if i < len(H) else "<none>"))
    cache[book] = out
    return out


for raw in open(sys.argv[1], encoding="utf-8"):
    raw = raw.rstrip("\n")
    if not raw.strip() or raw.startswith("#"):
        continue
    books, pat = raw.split("|", 1)
    rx = re.compile(pat)
    found = False
    for b in books.split(","):
        for loc, p, h in load(b):
            m = rx.search(p)
            if m:
                s = max(0, m.start() - 200)
                print(f"### [{pat}] {loc}")
                print("PI:", p[s:s + maxc])
                print("HI:", h[:maxc * 2] if len(h) < maxc * 2 else h[:maxc * 2] + " <...>")
                found = True
                break
        if found:
            break
    if not found:
        print(f"### [{pat}] NOT FOUND")
