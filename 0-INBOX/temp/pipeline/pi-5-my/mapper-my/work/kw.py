import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import map5_rules as R
kw = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 3; stem = sys.argv[3] if len(sys.argv) > 3 else kw[:5]
c = 0
for ch in R.CHAPTERS:
    for sid, kws in R.keyword_rows(ch):
        if kw in kws:
            pa = R.pali(ch).get(sid, ""); my = R.burmese(ch).get(sid, "")
            i = pa.lower().find(stem.lower())
            print(f"--- {ch} ^{sid} :: {pa[max(0,i-80):i+120]}")
            print("    MY:", my[:500])
            c += 1
            if c >= n: sys.exit()
