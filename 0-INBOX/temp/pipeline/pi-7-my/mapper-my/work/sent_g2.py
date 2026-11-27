"""sent_g2.py ch sid kw: the aligned Pāli / Burmese sentences of a segment that contain the keyword, and the keyword
row (read-only helper; g2)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
ch, sid, kw = sys.argv[1:4]
p, b = R.pali(ch).get(sid, ""), R.burmese(ch).get(sid, "")
ps, bs = re.split(r"(?<=[.)?])\s+", p), re.split(r"(?<=[။)?])\s+", b)
print("ROW:", dict(R.keyword_rows(ch))[sid])
rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])")
for i, s in enumerate(ps):
    if rx.search(s):
        print(f"[{i}/{len(ps)}|{len(bs)}] PI:", s[:700]); print("   MY:", (bs[i] if i < len(bs) else "?")[:800])
