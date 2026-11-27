"""phase 3 helper: the group-table entries of map_g1 … map_g6 (and map_sample), keyword -> {group: value}; prints the
keywords that more than one group table holds (same / different values)."""
import sys, pathlib, importlib, collections
D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D)); sys.dont_write_bytecode = True
import map7_rules as R
tabs = {}
for g in ("map_g1", "map_g2", "map_g3", "map_g4", "map_g5", "map_g6"):
    m = importlib.import_module(g)
    t = {}
    for name in ("COMMON", "G2", "G4", "GROUP"):
        if isinstance(getattr(m, name, None), dict): t.update(getattr(m, name))
    if g == "map_g3": t.update(m.T_G3)
    tabs[g[4:]] = t
by = collections.defaultdict(dict)
for g, t in tabs.items():
    for k, v in t.items():
        by[R.low(k)][g] = v
if __name__ == "__main__":
    for k in sorted(by):
        if len(by[k]) > 1:
            vals = set(map(str, by[k].values()))
            print(("SAME " if len(vals) == 1 else "DIFF ") + k, by[k] if len(vals) > 1 else (list(by[k]), list(vals)[0]))
