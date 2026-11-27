"""kwic_g3.py kw [n]: uses of a keyword in the g3 chapters: the Pāli sentence with it and the Burmese sentence of the
same index (read-only helper)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
CH = ["3-01-hetugocchaka", "3-02-culantaraduka", "3-03-asavagocchaka", "3-04-sannojanagocchaka",
      "3-05-ganthagocchaka", "3-06-oghayogagocchaka", "3-07-nivaranagocchaka", "3-08-paramasagocchaka"]
kw = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])", re.I)
seen = 0
for ch in CH:
    P, B = R.pali(ch), R.burmese(ch)
    for sid, kws in R.keyword_rows(ch):
        if kw not in kws:
            continue
        p = P.get(sid, ""); b = B.get(sid, "")
        ps = re.split(r"(?<=[.);])\s+", p); bs = re.split(r"(?<=[။);၊])\s+", b)
        ps2 = re.split(r"(?<=[.)])\s+", p); bs2 = re.split(r"(?<=[။)])\s+", b)
        for i, s in enumerate(ps2):
            if rx.search(s):
                print(f"== {ch} ^{sid} [{i}/{len(ps2)}|{len(bs2)}]")
                print("PI:", s[:700])
                print("MY:", (bs2[i] if i < len(bs2) else "?")[:900])
                break
        seen += 1
        if seen >= n:
            sys.exit()
