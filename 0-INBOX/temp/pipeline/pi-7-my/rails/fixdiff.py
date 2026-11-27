"""Inspection helper: word-level diff of the pre-fix rails (review/fix-backup/rails-text) against a folder
(default rails/dev-out). usage: fixdiff.py [folder] [--grep REGEX] [--max N] [--stats]"""
import collections, difflib, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
N = lambda s: unicodedata.normalize("NFC", s)
A = HERE.parent / "review/fix-backup/rails-text"
args = sys.argv[1:]
B = pathlib.Path(args[0]) if args and not args[0].startswith("--") else HERE / "dev-out"
g = re.compile(args[args.index("--grep") + 1]) if "--grep" in args else None
mx = int(args[args.index("--max") + 1]) if "--max" in args else 40
per = collections.Counter(); shown = 0; kinds = collections.Counter()
for p in sorted(A.glob("*.md")):
    a = N(p.read_text(encoding="utf-8")).split("\n"); b = N((B / p.name).read_text(encoding="utf-8")).split("\n")
    for k, (x, y) in enumerate(zip(a, b), 1):
        if x == y:
            continue
        per[p.name[:-3]] += 1
        sm = difflib.SequenceMatcher(None, x.split(" "), y.split(" "), autojunk=False)
        xs, ys = x.split(" "), y.split(" ")
        for t, i1, i2, j1, j2 in sm.get_opcodes():
            if t == "equal":
                continue
            d = f"[{' '.join(xs[i1:i2])} → {' '.join(ys[j1:j2])}]"
            kinds[d] += 1
            if (g is None or g.search(d)) and shown < mx and "--stats" not in args:
                shown += 1
                print(f"{p.name[:4]}:{k} …{' '.join(xs[max(0, i1 - 3):i1])} {d}")
if "--stats" in args:
    for k, v in kinds.most_common(60):
        print(v, k)
print("lines changed:", sum(per.values()), dict(per))
