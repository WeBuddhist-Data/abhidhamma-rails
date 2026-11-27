"""kwall_g2.py kw [grep]: every g2 use of a keyword: the aligned Pāli / Burmese sentences (read-only helper; g2)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
kw = sys.argv[1]
rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])")
for ch in [c for c in R.chapters() if c.startswith("2-")]:
    for sid, kws in R.keyword_rows(ch):
        if kw not in kws:
            continue
        p, b = R.pali(ch).get(sid, ""), R.burmese(ch).get(sid, "")
        ps, bs = re.split(r"(?<=[.)?])\s+", p), re.split(r"(?<=[။)?])\s+", b)
        for i, s in enumerate(ps):
            if rx.search(s):
                m = rx.search(s)
                print(f"{ch} ^{sid} [{i}/{len(ps)}|{len(bs)}] n={kws.count(kw)} PI: …{s[max(0, m.start()-120):m.end()+80]}")
                print("    MY:", (bs[i] if i < len(bs) and len(ps) == len(bs) else "(unaligned) " + b[:300])[:500])
