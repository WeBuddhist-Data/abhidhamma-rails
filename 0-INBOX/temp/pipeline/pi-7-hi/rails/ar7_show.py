"""Show aligned Pāli / Hindi lines for the alignment pass.
usage: python -I -B -X utf8 ar7_show.py <pali_regex> [hindi_regex] [--max N] [--files PREFIX,...] [--bak] [--ctx N]
With hindi_regex, only the matching part of the Hindi (±ctx chars) is printed."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C

args = [a for a in sys.argv[1:]]
mx, files, ctx = 40, None, 120
if "--max" in args:
    i = args.index("--max"); mx = int(args[i + 1]); del args[i:i + 2]
if "--files" in args:
    i = args.index("--files"); files = tuple(args[i + 1].split(",")); del args[i:i + 2]
if "--ctx" in args:
    i = args.index("--ctx"); ctx = int(args[i + 1]); del args[i:i + 2]
if "--bak" in args:
    args.remove("--bak"); C.CUR["hdir"] = C.BAK
prx = re.compile(args[0])
hrx = re.compile(args[1]) if len(args) > 1 else None
n = 0
for part in C.PARTS:
    if files and not part.startswith(files):
        continue
    for i, (p, h) in enumerate(C.pairs(part)):
        if not prx.search(p):
            continue
        if hrx:
            ms = list(hrx.finditer(h))
            if not ms:
                continue
            n += 1
            if n <= mx:
                m = ms[0]
                pm = prx.search(p)
                print(f"{C.short(part)}:{i+1} P: …{p[max(0, pm.start()-ctx):pm.end()+ctx]}…")
                print(f"        H: …{h[max(0, m.start()-ctx):m.end()+ctx]}…")
        else:
            n += 1
            if n <= mx:
                print(f"{C.short(part)}:{i+1} P: {p[:600]}")
                print(f"        H: {h[:600]}")
print("total", n)
