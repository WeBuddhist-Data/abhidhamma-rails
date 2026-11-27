"""diff_g5.py: g5 values against the module alone (no g5 tables) and against pi-1 … pi-6 (read-only)."""
import sys, pathlib, collections
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
import map_g5 as G
M0 = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
new = collections.Counter(); ovr = collections.Counter(); pri = collections.defaultdict(collections.Counter)
for ch in G.CHAPTERS:
    my, pa = R.burmese(ch), R.pali(ch)
    for l in (D / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        sid, rest = l[1:].split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            try:
                v0 = M0.lookup(ch, sid, k, pa.get(sid, ""), my[sid])
            except KeyError:
                v0 = None
            if v0 is None:
                new[(k, v)] += 1
            elif v0 != v:
                ovr[(k, v0, v)] += 1
            if v0 != v:
                pv = R.prev_vals(k)
                if not pv:
                    for b in R.base_forms(k):
                        pv = R.prev_vals(b)
                        if pv:
                            break
                if pv and v not in pv:
                    pri[(k, v)].update(pv)
print("NEW", sum(new.values()), len(new))
for x, n in sorted(new.items()): print("  ", x, n)
print("OVR", sum(ovr.values()), len(ovr))
for x, n in sorted(ovr.items()): print("  ", x, n)
print("PRIOR-DIFF")
for (k, v), c in sorted(pri.items()):
    print("  ", k, "=", v, "| prior", c.most_common(3), [t for t in R.PRIOR_ORDER if c and R.prev_vals(k, t)])
