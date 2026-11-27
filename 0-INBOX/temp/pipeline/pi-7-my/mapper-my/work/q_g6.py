"""q_g6.py: prior values of keywords (pi-1 … pi-6) and the module's value per keyword in a segment.
usage: q_g6.py kw [kw …]   |   q_g6.py @ch sid [sid …]"""
import sys, pathlib
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import map7_rules as R
a = sys.argv[1:]
if a and a[0].startswith("@"):
    ch = a[0][1:]
    M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
    my, pa = R.burmese(ch), R.pali(ch)
    rows = dict(R.keyword_rows(ch))
    for sid in a[1:]:
        print("==", sid)
        for kw in rows[sid]:
            try:
                v = M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
            except KeyError:
                v = "?"
            print(f"   {kw} = {v}   [{M.SRC.get((sid, kw))}]")
else:
    for k in a:
        for t in R.PRIOR_ORDER:
            pv = R.prev_vals(k, t)
            if pv:
                print(k, t, pv.most_common(6))
        print(k, "terms", R.terms().get(R.low(k)), "LEXW", R.LEXW.get(R.low(k)), "head", R.head_lex().get(R.low(k)),
              "gen", R.gen_values(R.low(k)))
