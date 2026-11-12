"""Show word-level diffs from align-preview.txt.  usage: python -I -X utf8 preview_diff_pi2.py <substr> [<substr> …] [--max N]"""
import difflib, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
args = [a for a in sys.argv[1:]]
mx = 10 ** 9
if "--max" in args:
    i = args.index("--max"); mx = int(args[i + 1]); del args[i:i + 2]
t = open(os.path.join(HERE, "align-preview.txt"), encoding="utf-8").read()
n = 0
for b in t.split("## ")[1:]:
    head, old, new = b.split("\n")[:3]
    if args and not any(x in head for x in args):
        continue
    n += 1
    if n > mx:
        break
    a, c = old[2:].split(), new[2:].split()
    sm = difflib.SequenceMatcher(None, a, c, autojunk=False)
    d = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            ctx = " ".join(a[max(0, i1 - 4):i1])
            d.append(f"…{ctx} «{' '.join(a[i1:i2])}» → «{' '.join(c[j1:j2])}»")
    print("##", head)
    for x in d[:12]:
        print("   ", x[:500])
