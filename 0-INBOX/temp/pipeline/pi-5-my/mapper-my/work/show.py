import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import map5_rules as R
ch = sys.argv[1]
my, pa = R.burmese(ch), R.pali(ch)
rows = dict(R.keyword_rows(ch))
for sid in sys.argv[2:]:
    print("=====", sid); print("PI:", pa.get(sid, "")[:3000]); print("MY:", my.get(sid, "")[:5000]); print("KW:", ", ".join(rows.get(sid, [])))
