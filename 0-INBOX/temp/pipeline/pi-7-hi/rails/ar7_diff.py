"""Word diffs of changed lines (backup-pre-align vs current) whose Pāli matches a regex.
usage: python -I -B -X utf8 ar7_diff.py <pali_regex> [--max N] [--hfilter REGEX]"""
import os, re, sys, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C

args = sys.argv[1:]
mx, hf = 30, None
if "--max" in args:
    i = args.index("--max"); mx = int(args[i + 1]); del args[i:i + 2]
if "--hfilter" in args:
    i = args.index("--hfilter"); hf = re.compile(args[i + 1]); del args[i:i + 2]
prx = re.compile(args[0])
n = 0
for part in C.PARTS:
    a = C.pairs(part, C.BAK)
    b = C.pairs(part, C.HDIR)
    for i, ((p, h0), (_, h1)) in enumerate(zip(a, b)):
        if h0 == h1 or not prx.search(p):
            continue
        ta, tb = h0.split(), h1.split()
        ops = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
            if op != "equal":
                ctx = " ".join(ta[max(0, i1 - 3):i1])
                ops.append(f"[{ctx}] «{' '.join(ta[i1:i2])}» → «{' '.join(tb[j1:j2])}»")
        s = " | ".join(ops)
        if hf and not hf.search(s):
            continue
        n += 1
        if n <= mx:
            print(f"{part[:4]}:{i+1} {s[:600]}")
print("total", n)
