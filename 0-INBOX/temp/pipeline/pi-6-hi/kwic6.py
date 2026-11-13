"""KWIC: aligned Pāli/Hindi lines whose Pāli matches a regex (optionally Hindi matches/doesn't match another).
usage: python -I -X utf8 kwic6.py <pali_regex> [--h=<hindi_regex>] [--nh=<hindi_regex>] [--n=3] [--files=2-01,3-] [--bak]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C

args = [a for a in sys.argv[1:] if not a.startswith("--")]
opt = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
if "--bak" in sys.argv:
    C.CUR["hdir"] = C.BAK
rx = re.compile(args[0])
hx = re.compile(opt["h"]) if "h" in opt else None
nhx = re.compile(opt["nh"]) if "nh" in opt else None
n = int(opt.get("n", 3))
files = opt.get("files", "").split(",") if "files" in opt else None
tot = 0
for part in C.PARTS:
    if files and not any(part.startswith(f) for f in files):
        continue
    k = 0
    for i, (p, h) in enumerate(C.pairs(part)):
        if not rx.search(p):
            continue
        if hx and not hx.search(h):
            continue
        if nhx and nhx.search(h):
            continue
        k += 1; tot += 1
        if k <= n:
            print(f"[{C.short(part)} #{i}] {p}\n      {h}")
    if k > n:
        print(f"   ({C.short(part)}: {k} matches)")
print("total", tot)
