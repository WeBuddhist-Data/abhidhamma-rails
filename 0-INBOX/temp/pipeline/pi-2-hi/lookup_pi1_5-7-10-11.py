# -*- coding: utf-8 -*-
"""Find a Pāli regex in pi-N (Pāli split) and print the same line of the pi-N Hindi rails.
usage: python -I -X utf8 lookup_pi1_5-7-10-11.py "<regex>" [maxhits] [full|short] [book=pi-1]
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
book = sys.argv[4] if len(sys.argv) > 4 else "pi-1"
PD = os.path.join(ROOT, rf"AI_translation\pali\{book}_split_chapters")
HD = os.path.join(ROOT, rf"AI_translation\hindi\{book}-hindi-plain-rails_split_chapters")

pat = re.compile(sys.argv[1])
maxhits = int(sys.argv[2]) if len(sys.argv) > 2 else 5
full = len(sys.argv) > 3 and sys.argv[3] == "full"
hits = 0
for f in sorted(os.listdir(PD)):
    if not f.endswith(".md"):
        continue
    if not os.path.exists(os.path.join(HD, f)):
        continue
    pl = open(os.path.join(PD, f), encoding="utf-8-sig").read().splitlines()
    hl = open(os.path.join(HD, f), encoding="utf-8-sig").read().splitlines()
    for i, l in enumerate(pl):
        if pat.search(l):
            h = hl[i] if i < len(hl) else "<none>"
            if full:
                print(f"== {f}:{i+1}\nP: {l}\nH: {h}\n")
            else:
                m = pat.search(l)
                s = max(0, m.start() - 150)
                # rough proportional window in the Hindi
                r = s / max(1, len(l))
                hs = int(r * len(h))
                print(f"== {f}:{i+1}\nP: …{l[s:s+500]}\nH: …{h[max(0,hs-200):hs+900]}\n")
            hits += 1
            if hits >= maxhits:
                sys.exit(0)
print("hits", hits)
