import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import map5_rules as R
M = R.Mapper()
for kw in sys.argv[1:]:
    n = 0
    for ch in R.CHAPTERS:
        for sid, kws in R.keyword_rows(ch):
            if kw not in kws: continue
            my, pa = R.burmese(ch)[sid], R.pali(ch)[sid]
            try:
                v = M.lookup(ch, sid, kw, pa, my)
                if R.presence(v, my)[0]: continue
            except KeyError:
                v = None
            i = pa.lower().find(kw.lower()[:4])
            print(f"{kw} {ch} ^{sid} v={v} :: {pa[max(0,i-60):i+80]}")
            n += 1
            if n >= 2: break
        if n >= 2: break
