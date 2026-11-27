"""g1 helper: kwval_g1.py KW [KW...]: every use of the keyword in the g1 chapters: sid, value (module + map_g1 if present), Pāli KWIC."""
import sys, pathlib, re
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map7_rules as R
try:
    import map_g1 as G
    M = G.mapper()
except ImportError:
    M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
CH = ["1-01-kusalattika", "1-03-vipakattika", "1-04-upadinnattika", "1-05-sankilitthattika"]
want = set(sys.argv[1:])
seen = set()
for ch in CH:
    my, pa = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        for kw in kws:
            if kw not in want or (sid, kw) in seen:
                continue
            seen.add((sid, kw))
            try:
                v = M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
            except KeyError:
                v = "?"
            p = pa.get(sid, "")
            m = re.search(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])", p)
            ctx = p[max(0, m.start() - 60):m.end() + 60] if m else "(not in Pāli) " + p[:100]
            print(f"{ch} ^{sid} {kw} = {v} [{M.SRC.get((sid, kw))}]\n    PA: {ctx}")
