# -*- coding: utf-8 -*-
"""Helper for chapter 17: grep the Hindi termbases (pi-1, pi-3, pi-4, pi-5) for Pāli headwords.
usage: python -I -X utf8 khuddaka17_terms.py word1 word2 ...   (each is a regex matched at line start)
"""
import os, re, sys

D = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi"
files = ["pi-1-pali-hindi-termbase-plain.md", "pi-3-pali-hindi-termbase-plain.md",
         "pi-4-pali-hindi-termbase-plain.md", "pi-5-pali-hindi-termbase-plain.md"]
lines = {f: open(os.path.join(D, f), encoding="utf-8-sig").read().splitlines() for f in files}
for w in sys.argv[1:]:
    pat = re.compile("^" + w, re.I)
    print("###", w)
    n = 0
    for f in files:
        for l in lines[f]:
            if pat.search(l):
                print(f[:4], l[:300])
                n += 1
                if n > 6:
                    break
