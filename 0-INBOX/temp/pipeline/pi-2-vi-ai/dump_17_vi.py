# -*- coding: utf-8 -*-
"""Scratch: aligned Pāli / Vietnamese non-empty lines of one pi-2 chapter (ch1-16 outputs), filtered by a regex.
usage: python -I -X utf8 dump_17_vi.py <chapter file> <regex> [maxchars]"""
import os
import re
import sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
P = os.path.join(ROOT, r"AI_translation\pali\pi-2_split_chapters")
V = os.path.join(ROOT, r"AI_translation\vietnamese\pi-2-vietnamese-plain-zeroshot_split_chapters")


def lines(path):
    return [l for l in open(path, encoding="utf-8").read().split("\n") if l.strip()]


fn, rx = sys.argv[1], re.compile(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 300
pl, vl = lines(os.path.join(P, fn)), lines(os.path.join(V, fn))
for i, l in enumerate(pl):
    if rx.search(l):
        print("P:", l[:mx])
        print("V:", vl[i][:mx])
