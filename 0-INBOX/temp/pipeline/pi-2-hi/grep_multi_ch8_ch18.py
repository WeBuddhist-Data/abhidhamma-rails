# -*- coding: utf-8 -*-
"""Helper for chapters 8 and 18: for each pattern, first hit per book (pi-1, pi-3, pi-4, pi-5).
Prints only a window of the Pāli line around the match and the full Hindi line, truncated.

usage: python -I -X utf8 grep_multi_ch8_ch18.py <pattern> [<pattern> ...]
"""
import os, re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
BOOKS = ["pi-1", "pi-3", "pi-4", "pi-5"]
HMAX = 900


def search(pat, book):
    PALI = os.path.join(ROOT, rf"AI_translation\pali\{book}_split_chapters")
    HI = os.path.join(ROOT, rf"AI_translation\hindi\{book}-hindi-plain-rails_split_chapters")
    for f in sorted(os.listdir(PALI)):
        hp = os.path.join(HI, f)
        if not f.endswith(".md") or not os.path.exists(hp):
            continue
        pl = open(os.path.join(PALI, f), encoding="utf-8-sig").read().splitlines()
        hl = open(hp, encoding="utf-8-sig").read().splitlines()
        for i, l in enumerate(pl):
            m = pat.search(l)
            if m:
                s = max(0, m.start() - 150)
                return f"{book} {f}:{i+1}\n  P: …{l[s:m.end()+150]}…\n  H: {(hl[i] if i < len(hl) else '')[:HMAX]}"
    return None


for a in sys.argv[1:]:
    pat = re.compile(a)
    print(f"######## {a}")
    for b in BOOKS:
        r = search(pat, b)
        if r:
            print(r)
