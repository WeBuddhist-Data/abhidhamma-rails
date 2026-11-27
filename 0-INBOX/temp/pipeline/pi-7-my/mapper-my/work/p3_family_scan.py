"""phase 3 scan 2 (fix 8, one value per term): keywords grouped by R1 base form and case stem (a-, i-, u-stem endings
removed); prints every family whose members (different case forms) have different value sets.
usage: p3_family_scan.py [--dir DIR] [out.tsv]"""
import sys, pathlib, collections
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D)); sys.dont_write_bytecode = True
import map7_rules as R
a = sys.argv[1:]
d = D
if "--dir" in a:
    i = a.index("--dir"); d = pathlib.Path(a[i + 1]); del a[i:i + 2]
ENDS = sorted(set(R.A_ENDS + R.I_ENDS + R.U_ENDS), key=len, reverse=True)


def fam(k):
    w = R.low(k)
    b = R.base_forms(w)
    w = b[0] if b else w
    for e in ENDS:
        if w.endswith(e) and len(w) - len(e) >= 5:
            return w[:-len(e)]
    return w


vals = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
for c in R.chapters():
    for l in (d / f"{c}.mapped.md").read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            vals[fam(k)][R.low(k)][v] += 1
rows = []
for f in sorted(vals):
    m = vals[f]
    if len(m) < 2:
        continue
    sets = {k: set(c) for k, c in m.items()}
    allv = set().union(*sets.values())
    if len(allv) < 2:
        continue
    # members that share no value with the family's main value
    main = collections.Counter()
    for c in m.values():
        main.update(c)
    top = main.most_common(1)[0][0]
    odd = {k: dict(c) for k, c in m.items() if top not in c}
    if odd:
        rows.append(f"{f}\ttop «{top}» ({main[top]})\t" + " | ".join(f"{k}: " + "; ".join(f"«{v}» {n}" for v, n in c.items())
                                                              for k, c in sorted(odd.items())))
out = "\n".join(rows) + "\n"
if a:
    pathlib.Path(a[0]).write_text(out, encoding="utf-8")
print("families with an odd member", len(rows))
