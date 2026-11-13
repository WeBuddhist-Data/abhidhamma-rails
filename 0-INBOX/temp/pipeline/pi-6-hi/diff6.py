"""Word-level diff of backup-pre-harmonise vs current output.
usage: python -I -X utf8 diff6.py [file-prefix] [--n=5] [--grep=<regex on the diff text>]"""
import os, re, sys, difflib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hz6_common as C

args = [a for a in sys.argv[1:] if not a.startswith("--")]
opt = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
n = int(opt.get("n", 5))
gx = re.compile(opt["grep"]) if "grep" in opt else None
kinds = collections.Counter()
for part in C.PARTS:
    if args and not part.startswith(args[0]):
        continue
    a = C.lines(os.path.join(C.BAK, part + ".md"))
    b = C.lines(os.path.join(C.HDIR, part + ".md"))
    shown = 0
    for i, (x, y) in enumerate(zip(a, b)):
        if x == y:
            continue
        ta, tb = x.split(), y.split()
        ops = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
            if op != "equal":
                ops.append(f"«{' '.join(ta[max(0, i1 - 2):i2])}» → «{' '.join(tb[max(0, j1 - 2):j2])}»")
        d = " ; ".join(ops)
        if gx and not gx.search(d):
            continue
        for o in ops:
            kinds[re.sub(r"\s+", " ", o)] += 1
        if shown < n:
            print(f"[{C.short(part)} #{i + 1}] {d}")
            shown += 1
if "--kinds" in sys.argv:
    for k, v in kinds.most_common(int(opt.get("k", 80))):
        print(v, k)
