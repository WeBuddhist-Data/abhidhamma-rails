"""Word-level diff of backup-pre-harmonise vs current Hindi, per changed line.
usage: hz_diff.py [chapter-numbers comma-separated] [--max=N]"""
import sys, os, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz_common import PARTS, HDIR, HERE, lines, short

opts = {a.split("=")[0]: a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--") and "=" in a}
args = [a for a in sys.argv[1:] if not a.startswith("--")]
chs = set(args[0].split(",")) if args else None
mx = int(opts.get("--max", "100000"))
n = 0
for part in PARTS:
    if chs and part.split("-")[0] not in chs:
        continue
    a = lines(os.path.join(HERE, "backup-pre-harmonise", part + ".md"))
    b = lines(os.path.join(HDIR, part + ".md"))
    for i, (x, y) in enumerate(zip(a, b)):
        if x == y:
            continue
        n += 1
        if n > mx:
            continue
        ta, tb = x.split(" "), y.split(" ")
        sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
        d = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != "equal":
                ctx = " ".join(ta[max(0, i1 - 3):i1])
                d.append(f"…{ctx} «{' '.join(ta[i1:i2])}» → «{' '.join(tb[j1:j2])}»")
        print(f"[{short(part)} #{i}] " + " | ".join(d))
print("changed lines:", n)
