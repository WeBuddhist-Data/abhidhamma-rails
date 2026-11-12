# -*- coding: utf-8 -*-
"""Helper (chapters 2 and 4): grep the Pāli of a book and show the same line of its reviewed Hindi.
usage: python -I -X utf8 show_ch2_ch4_pi1.py <book 1|3|4|5> <regex> [maxhits] [clip]
"""
import os, re, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
book = sys.argv[1]
PD = os.path.join(ROOT, rf"pali\pi-{book}_split_chapters")
HD = os.path.join(ROOT, rf"hindi\pi-{book}-hindi-plain-rails_split_chapters")
rx = re.compile(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 10
clip = int(sys.argv[4]) if len(sys.argv) > 4 else 0


def lines(d, f):
    return open(os.path.join(d, f), encoding="utf-8-sig").read().splitlines()


def cl(s, m=None):
    if not clip:
        return s
    if m is None:
        return s[:clip]
    a = max(0, m.start() - clip // 2)
    return s[a:a + clip]


n = 0
for f in sorted(os.listdir(PD)):
    if not f.endswith(".md") or not os.path.exists(os.path.join(HD, f)):
        continue
    P, H = lines(PD, f), lines(HD, f)
    for i, l in enumerate(P):
        m = rx.search(l)
        if m:
            print(f"== {f}:{i+1}\nPI: {cl(l, m)}\nHI: {cl(H[i]) if i < len(H) else '???'}\n")
            n += 1
            if n >= mx:
                sys.exit()
