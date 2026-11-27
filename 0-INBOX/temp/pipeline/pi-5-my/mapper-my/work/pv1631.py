import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import map5_rules as R
for k in sys.argv[1:]:
    out = []
    for t in R.PRIOR_ORDER:
        c = R.prev_vals(k, t)
        if c: out.append(t + ": " + " | ".join(f"{v} ({n})" for v, n in c.most_common(4)))
    tv = R.terms().get(R.low(k))
    print(k, "::", " ;; ".join(out) or "-", (" ;; terms: " + tv) if tv else "")
