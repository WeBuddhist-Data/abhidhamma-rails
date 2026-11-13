"""Show old/new full lines for changed lines of a file. usage: show6.py <file-prefix> [--n=5] [--skip=0] [--grep=regex-on-new]"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C

args = [a for a in sys.argv[1:] if not a.startswith("--")]
opt = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
n, skip = int(opt.get("n", 5)), int(opt.get("skip", 0))
gx = re.compile(opt["grep"]) if "grep" in opt else None
for part in C.PARTS:
    if not part.startswith(args[0]):
        continue
    a = C.lines(os.path.join(C.BAK, part + ".md"))
    b = C.lines(os.path.join(C.HDIR, part + ".md"))
    k = 0
    for i, (x, y) in enumerate(zip(a, b)):
        if x == y or (gx and not gx.search(y)):
            continue
        k += 1
        if k <= skip:
            continue
        if k > skip + n:
            break
        print(f"[{C.short(part)} #{i + 1}]\n  - {x}\n  + {y}")
