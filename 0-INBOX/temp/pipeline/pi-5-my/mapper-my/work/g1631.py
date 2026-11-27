"""g1631.py CH SID PALI-REGEX [W]: the Pāli sentences of the segment matching the regex, with the aligned Burmese."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent)); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map5_rules as R, sent1631 as S
ch, sid, rx = sys.argv[1:4]
W = int(sys.argv[4]) if len(sys.argv) > 4 else 600
a, b = S.pali_sents(R.pali(ch).get(sid, "")), S.my_sents(R.burmese(ch)[sid])
amap = {}
for ia, ib in S.align(a, b):
    for i in ia: amap[i] = ib
n = 0
for i, s in enumerate(a):
    if re.search(rx, s, flags=re.I):
        ib = amap.get(i) or [min(len(b) - 1, round(i * len(b) / max(1, len(a))))]
        print("PI:", s[:W]); print("MY:", " ".join(b[max(0, ib[0] - (1 if '-x' in sys.argv else 0)): ib[-1] + 1])[:int(W * 1.6)]); n += 1
        if n >= 2: break
