"""read-only helper (g1): the module value of keyword KW in each segment of chapter CH (and how often the Burmese
strings B… occur in that segment). usage: val_g1.py CH KW [B …]"""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map6_rules as R
ch, kw, bs = sys.argv[1], sys.argv[2], sys.argv[3:]
M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK]))
for sid, ks in R.keyword_rows(ch):
    if kw in ks:
        my = R.burmese(ch)[sid]
        try:
            v = M.lookup(ch, sid, kw, R.pali(ch).get(sid, ""), my)
        except KeyError:
            v = "?"
        print(f"^{sid} {kw}={v} [{M.SRC.get((sid, kw))}] " + " ".join(f"{b}:{my.count(b)}" for b in bs))
