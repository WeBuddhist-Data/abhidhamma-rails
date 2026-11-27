"""Compact view of family_scan part B: one line per family, terms with their headwords. usage: fam_compact.py scan.txt"""
import sys, re, collections
txt = open(sys.argv[1], encoding="utf-8").read()
b = txt.split("== B.", 1)[1].split("== C.", 1)[0]
for blk in b.split("\n-- ")[1:]:
    lines = blk.splitlines()
    head = lines[0].split(" (")[0]
    d = collections.OrderedDict()
    for l in lines[1:]:
        if not l.startswith("   "): continue
        k, _, t = l.strip().partition(": ")
        d.setdefault(t, []).append(k)
    print(f"{head}: " + " | ".join(f"{t} [{', '.join(ks)}]" for t, ks in d.items()))
