"""famchk_g2.py: keyword families (a keyword and its case siblings, R1 base forms) with more than one value in the
g2 mapped files (read-only helper; g2)."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
val = collections.defaultdict(collections.Counter)
for ch in [c for c in R.chapters() if c.startswith("2-")]:
    for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        for kv in l.split("] ", 1)[1].split(", "):
            k, v = kv.split("=", 1)
            b = R.base_forms(k)
            key = R.low(b[0] if b else k)
            val[key][(k, v)] += 1
fam = collections.defaultdict(collections.Counter)
for key, c in val.items():
    sibs = set([key] + R.case_siblings(key))
    root = min(sibs, key=len)
    for (k, v), n in c.items():
        fam[root][(k, v)] += n
for root, c in sorted(fam.items()):
    vs = {v for (k, v) in c}
    if len(vs) > 1:
        print(root, "|", "; ".join(f"{k}={v} ({n})" for (k, v), n in c.most_common()))
