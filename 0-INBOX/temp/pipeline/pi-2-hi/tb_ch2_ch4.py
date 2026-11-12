# -*- coding: utf-8 -*-
"""Helper (chapters 2 and 4): look up Pāli words in the pi-1/3/4/5 Hindi termbases.
usage: python -I -X utf8 tb_ch2_ch4.py word1 word2 ...   (regex, matched at line start before ':')
"""
import os, re, sys
D = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi"
TB = [f"pi-{n}-pali-hindi-termbase-plain.md" for n in (1, 3, 4, 5)]
data = {t: open(os.path.join(D, t), encoding="utf-8-sig").read().splitlines() for t in TB}
for w in sys.argv[1:]:
    rx = re.compile(r"^(" + w + r")\s*:", re.I)
    print("###", w)
    for t, L in data.items():
        for l in L:
            if rx.match(l):
                print(f"  [{t[:4]}] {l[:400]}")
