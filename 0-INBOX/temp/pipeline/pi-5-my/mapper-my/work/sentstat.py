import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent)); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map5_rules as R, sent1631 as S
eq = tot = 0
for ch in R.CHAPTERS[16:]:
    my, pa = R.burmese(ch), R.pali(ch)
    for sid, _ in R.keyword_rows(ch):
        a, b = S.pali_sents(pa.get(sid, "")), S.my_sents(my[sid]); tot += 1; eq += len(a) == len(b)
        if len(a) != len(b) and len(sys.argv) > 1: print(sid, len(a), len(b))
print(eq, tot)
