"""g1 helper: show Pāli / Burmese / keywords of segments: show_g1.py CH SID [SID...]  (or CH grep:PALIWORD)"""
import sys, pathlib
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import map7_rules as R
ch = sys.argv[1]
my, pa = R.burmese(ch), R.pali(ch)
kw = dict(R.keyword_rows(ch))
sids = []
for a in sys.argv[2:]:
    if a.startswith("grep:"):
        w = a[5:]
        sids += [s for s, ks in kw.items() if w in ks]
    else:
        sids.append(a)
for s in sids:
    print(f"== ^{s}\nPA: {pa.get(s,'')}\nMY: {my.get(s,'')}\nKW: {kw.get(s)}\n")
