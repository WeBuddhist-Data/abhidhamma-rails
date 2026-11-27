"""diff_g3.py: uses whose value equals / differs from a pi-1 … pi-6 value of the same keyword (or base form), g3."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R, map_g3 as G
same = new = diff = 0
diffs = collections.defaultdict(collections.Counter)
for ch in G.CHAPTERS:
    for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            pv = R.prev_vals(k)
            if not pv:
                for b in R.base_forms(k):
                    pv = R.prev_vals(b)
                    if pv:
                        break
            if not pv:
                new += 1
            elif v in pv:
                same += 1
            else:
                diff += 1
                diffs[(k, v)][pv.most_common(1)[0][0]] += 1
print("same", same, "new", new, "diff", diff, "pairs", len(diffs))
for (k, v), c in sorted(diffs.items(), key=lambda x: -sum(x[1].values())):
    print(f"   {k} = {v}   prior {dict(c)}")
