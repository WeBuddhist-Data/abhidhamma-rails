"""ctx_g5.py kw [kw …]: every g5 use of the keywords: the mapped value, the Pāli words around it (read-only)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
import map_g5 as G
M = G.mapper()
want = set(sys.argv[1:])
for ch in G.CHAPTERS:
    my, pa = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        for kw in dict.fromkeys(kws):
            if kw not in want:
                continue
            try:
                v = M.lookup(ch, sid, kw, pa.get(sid, ""), my[sid])
            except KeyError:
                v = "?"
            p = pa.get(sid, "")
            ctxs = [p[max(0, m.start()-40):m.end()+40].replace("\n", " ") for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])", p)]
            print(f"{ch[:4]} ^{sid} {kw} = {v} [{M.SRC.get((sid, kw))}] | " + " || ".join(ctxs[:2]))
