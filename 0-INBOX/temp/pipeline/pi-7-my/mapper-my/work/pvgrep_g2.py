"""pvgrep_g2.py regex: pi-1 … pi-6 keywords matching a regex, with values (read-only helper; g2)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
rx = re.compile(sys.argv[1])
P = R.prior()
keys = set()
for t, d in (P.items() if isinstance(P, dict) else []):
    if isinstance(d, dict):
        keys |= {k for k in d if rx.search(k)}
for k in sorted(keys)[:int(sys.argv[2]) if len(sys.argv) > 2 else 60]:
    print(k, "|", " || ".join(f"{t}: " + "; ".join(f"{v} ({n})" for v, n in R.prev_vals(k, t).most_common(3))
                                for t in R.PRIOR_ORDER if R.prev_vals(k, t)))
