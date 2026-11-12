# -*- coding: utf-8 -*-
"""Print the English zero-shot segment(s) for given block IDs. usage: show_en_ch12_13.py <chapter.md> <id> [<id> ...]"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
fn = sys.argv[1]
L = open(os.path.join(ROOT, r"AI_translation\english\pi-2-english-plain-zeroshot_split_chapters", fn), encoding="utf-8").read().split("\n\n")
want = set(sys.argv[2:])
for seg in L:
    m = re.search(r"\^([0-9A-Za-z-]+)\s*$", seg.strip())
    if m and m.group(1) in want:
        print(seg.strip())
        print("----")
