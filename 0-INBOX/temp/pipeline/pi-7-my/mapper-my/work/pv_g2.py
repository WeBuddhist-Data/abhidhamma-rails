"""pv_g2.py kw …: the pi-1 … pi-6 values of keywords (and of their base forms) (read-only helper; g2)."""
import sys, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
for k in sys.argv[1:]:
    out = []
    for t in R.PRIOR_ORDER:
        c = R.prev_vals(k, t)
        if c:
            out.append(f"{t}: " + "; ".join(f"{v} ({n})" for v, n in c.most_common(4)))
    print(k, "|", " || ".join(out) or "-", "| terms:", R.terms().get(R.low(k)), "| lexw:", R.LEXW.get(R.low(k)),
          "| base:", R.base_forms(k)[:4])
