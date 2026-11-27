"""vals_g2.py regex: the module's values for g2 keywords matching a regex (all uses; read-only helper; g2)."""
import sys, re, pathlib, collections
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
rx = re.compile(sys.argv[1])
chs = [c for c in R.chapters() if c.startswith(sys.argv[2] if len(sys.argv) > 2 else "2-")]
M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
c = collections.Counter(); ex = {}
for ch in chs:
    B, P = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        for k in kws:
            if rx.search(k):
                try:
                    v = M.lookup(ch, sid, k, P.get(sid, ""), B.get(sid, ""))
                except KeyError:
                    v = "?"
                c[(k, v, M.SRC.get((sid, k)))] += 1
                ex.setdefault((k, v, M.SRC.get((sid, k))), f"{ch} ^{sid}")
for (k, v, s), n in sorted(c.items()):
    print(f"{k} = {v} [{s}] ({n}) e.g. {ex[(k, v, s)]}")
