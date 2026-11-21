"""Probe: count Vietnamese phrases (regex) on lines whose aligned Pāli matches a regex, per chapter and segment.

usage: python -I -X utf8 probe_terms_vi.py <pali_regex> <vi_regex> [chapters|all] [--bak]
Prints, per chapter:block, the Counter of distinct Vietnamese matches.
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, segments, short

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if "--bak" in sys.argv:
    vi_common.CUR["vdir"] = vi_common.BAK
pr, vr = re.compile(args[0]), re.compile(args[1])
chs = None if len(args) < 3 or args[2] == "all" else set(args[2].split(","))
tot = collections.Counter()
for part in PARTS:
    if chs and short(part) not in chs:
        continue
    for sid, ps, vs in segments(part):
        c = collections.Counter()
        np = 0
        for p, v in zip(ps, vs):
            if pr.search(p):
                np += len(pr.findall(p))
                for m in vr.finditer(v):
                    c[m.group(0)] += 1
        if np:
            tot.update(c)
            print(f"{short(part)}:{sid} pāli={np} :: " + "; ".join(f"«{k}»×{n}" for k, n in c.most_common()))
print("TOTAL:", "; ".join(f"«{k}»×{n}" for k, n in tot.most_common()))
