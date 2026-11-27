"""phase 3 task 2: every stem-fallback (S1) value left in the 44 chapters, with the phase-2 value of the same use.
usage: p3_s1.py OUT.tsv   (chapter, segment, keyword, value, phase-2 value, same/changed, Burmese context)"""
import sys
import re
import pathlib
import importlib.util
import collections

D = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(D))
import map6_rules as R  # noqa: E402


def load(n):
    spec = importlib.util.spec_from_file_location(n, D / f"{n}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


GROUPS = [("map_sample", R.SAMPLE)]
g1, g2, g3 = load("map_g1"), load("map_g2"), load("map_g3")
GROUPS += [("map_g1", g1.G1), ("map_g2", g2.GROUP), ("map_g3", g3.G3)]
MS = {"map_sample": load("map_sample").mapper(), "map_g1": g1.mapper(), "map_g2": g2.mapper(), "map_g3": g3.mapper()}


def old_vals(ch):
    out = {}
    for l in (D / "work/phase2-mapped" / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines():
        sid, rest = l[1:].split("] ", 1)
        for i, kv in enumerate(rest.split(", ")):
            out[(sid, i)] = kv.split("=", 1)[1]
    return out


rows = []
for g, chs in GROUPS:
    M = MS[g]
    for ch in chs:
        my, pa = R.burmese(ch), R.pali(ch)
        old = old_vals(ch)
        for sid, kws in R.keyword_rows(ch):
            for i, kw in enumerate(kws):
                M.SRC.pop((sid, kw), None)
                v = M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
                if M.SRC.get((sid, kw)) == "stem":
                    t = my[sid]
                    c = v.split(" … ")[0]
                    p = t.find(c if c in t else c[:-3])
                    ctx = t[max(0, p - 40):p + len(c) + 40] if p >= 0 else ""
                    rows.append((ch, sid, kw, v, old[(sid, i)], "same" if v == old[(sid, i)] else "CHANGED", ctx))
pathlib.Path(sys.argv[1]).write_text("".join("\t".join(r) + "\n" for r in rows), encoding="utf-8")
c = collections.Counter((r[2], r[3]) for r in rows)
print("stem uses", len(rows), "pairs", len(c), "changed", sum(r[5] == "CHANGED" for r in rows))
for (k, v), n in sorted(c.items(), key=lambda x: (R.low(x[0][0]), x[0][1])):
    chs = sorted({r[0].split("-")[0] for r in rows if r[2] == k and r[3] == v})
    print(f"   {n:4d}  {k} = {v}   [{' '.join(chs)}]")
