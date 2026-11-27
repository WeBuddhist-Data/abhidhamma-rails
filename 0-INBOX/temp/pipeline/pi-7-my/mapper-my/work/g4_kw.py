"""g4_kw.py ch kw [n]: uses of a keyword in one chapter: the Pāli sentence and the Burmese sentence of the same index
(read-only helper)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
ch, kw = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 3
W = int(sys.argv[4]) if len(sys.argv) > 4 else 500
rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])")
P, B = R.pali(ch), R.burmese(ch)
seen = 0
for sid, kws in R.keyword_rows(ch):
    if kw not in kws:
        continue
    p = P.get(sid, ""); b = B.get(sid, "")
    ps = re.split(r"(?<=[.)?])\s+", p); bs = re.split(r"(?<=[။)?])\s+", b)
    hit = [i for i, s in enumerate(ps) if rx.search(s)]
    i = hit[0] if hit else 0
    print(f"== ^{sid} [{i}/{len(ps)}|{len(bs)}]")
    print("PI:", ps[i][:W] if ps else "")
    print("MY:", (bs[i] if i < len(bs) else "?")[:W])
    if not hit:
        print("   (kw not in Pāli)")
    seen += 1
    if seen >= n:
        break
