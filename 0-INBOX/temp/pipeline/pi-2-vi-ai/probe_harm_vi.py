"""Scratch probe for the harmonise pass: print aligned Pāli / Vietnamese lines whose Pāli (or Vietnamese) matches.

usage: python -I -X utf8 probe_harm_vi.py <regex> [--vi] [--p1] [--p2] [--max N] [--cut N] [--bak]
  --vi   match the Vietnamese line instead of the Pāli line
  --p1   search pi-1 only; --p2 pi-2 only (default both)
  --cut  print only N characters around the match (default whole line)
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vi_common
from vi_common import PARTS, P1_PARTS, pairs, pairs1, ID

a = sys.argv[1:]
rx = re.compile(a[0])
vi = "--vi" in a
mx = int(a[a.index("--max") + 1]) if "--max" in a else 40
cut = int(a[a.index("--cut") + 1]) if "--cut" in a else 0
if "--bak" in a:
    vi_common.CUR["vdir"] = vi_common.BAK
srcs = []
if "--p1" not in a:
    srcs += [("p2:" + p, pairs(p)) for p in PARTS]
if "--p2" not in a:
    srcs += [("p1:" + p, pairs1(p)) for p in P1_PARTS]
n = 0


def clip(s, m):
    if not cut or not m:
        return s
    i = max(0, m.start() - cut)
    return ("…" if i else "") + s[i:m.end() + cut]


for name, pv in srcs:
    # segment id per line
    sids, cur = [], []
    for k, (p, v) in enumerate(pv):
        cur.append(k)
        m = ID.search(p)
        if m:
            sids += [m.group(1)] * len(cur); cur = []
    sids += ["?"] * len(cur)
    for k, (p, v) in enumerate(pv):
        m = rx.search(v if vi else p)
        if m:
            n += 1
            if n > mx:
                break
            mp = m if not vi else None
            mv = m if vi else None
            print(f"== {name} line {k + 1} ^{sids[k]}")
            print("  P:", clip(p, mp) if mp else (p[:cut * 2] if cut else p))
            print("  V:", clip(v, mv) if mv else (v[:cut * 2] if cut else v))
print("matches:", n)
