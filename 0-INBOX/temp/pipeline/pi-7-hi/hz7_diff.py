"""Word-level diff of current Hindi output vs backup-pre-harmonise.
usage: python -I -B -X utf8 hz7_diff.py [file-prefix] [hindi-regex-filter-on-new-line] [max] [ctx-words]
Prints each changed line's differing word spans (with a few words of context), grouped and counted by change.
"""
import sys, re, os, difflib, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hz7_common import PARTS, HDIR, BAK, lines, short

pref = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "*" else ""
flt = re.compile(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "*" else None
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 200
cw = int(sys.argv[4]) if len(sys.argv) > 4 else 3
cnt = collections.Counter()
ex = {}
for part in PARTS:
    if not part.startswith(pref):
        continue
    a = lines(os.path.join(BAK, part + ".md"))
    b = lines(os.path.join(HDIR, part + ".md"))
    for i, (x, y) in enumerate(zip(a, b)):
        if x == y or (flt and not flt.search(y)):
            continue
        ta, tb = x.split(" "), y.split(" ")
        sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                continue
            k = f"«{' '.join(ta[max(0, i1 - cw):i2 + cw])}» → «{' '.join(tb[max(0, j1 - cw):j2 + cw])}»"
            cnt[k] += 1
            ex.setdefault(k, f"{short(part)}:{i + 1}")
for k, v in cnt.most_common(mx):
    print(f"{v:5d} {ex[k]}  {k}")
print("distinct changes:", len(cnt), "total:", sum(cnt.values()))
