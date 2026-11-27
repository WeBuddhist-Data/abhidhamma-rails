"""kwic.py kw [n]: the first n uses of a keyword in the book: the Pāli sentence with it and the Burmese sentence of
the same index (sentences cut at «. » / «။ »; read-only helper)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
kw = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])", re.I)
seen = 0
for ch in R.chapters():
    P, B = R.pali(ch), R.burmese(ch)
    for sid, kws in R.keyword_rows(ch):
        if kw not in kws:
            continue
        p = P.get(sid, ""); b = B.get(sid, "")
        ps = re.split(r"(?<=[.)])\s+", p); bs = re.split(r"(?<=[။)])\s+", b)
        for i, s in enumerate(ps):
            if rx.search(s):
                print(f"== {ch} ^{sid} [{i}/{len(ps)}|{len(bs)}]")
                print("PI:", s[:600])
                print("MY:", (bs[i] if i < len(bs) else "?")[:700])
                break
        seen += 1
        if seen >= n:
            sys.exit()
