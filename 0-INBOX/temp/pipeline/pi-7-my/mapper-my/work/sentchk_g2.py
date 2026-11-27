"""sentchk_g2.py: module values (or a g2 script's values) that are present in the segment but NOT in the aligned
sentence (same index; only where the Pāli and Burmese sentence counts agree): candidates for override review."""
import sys, re, pathlib, collections, importlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
if "-g" in sys.argv:
    G = importlib.import_module("map_g2")
    M = G.mapper()
else:
    M = R.Mapper(stem=R.make_stem([R.FRAME, R.STOCK, R.LEXW]))
chs = [c for c in R.chapters() if c.startswith("2-")]
SP = re.compile(r"(?<=[.)?])\s+"); SB = re.compile(r"(?<=[။)?])\s+")
bad = collections.Counter(); ex = {}; tot = collections.Counter()
for ch in chs:
    B, P = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        p, b = P.get(sid, ""), B.get(sid, "")
        ps, bs = SP.split(p), SB.split(b)
        if len(ps) != len(bs):
            continue
        for k in kws:
            try:
                v = M.lookup(ch, sid, k, p, b)
            except KeyError:
                continue
            if v == R.NONE:
                continue
            rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(k) + r"(?![\wāīūṃṅñṭḍṇḷ])")
            idx = [i for i, s in enumerate(ps) if rx.search(s)]
            if not idx:
                continue
            key = (k, v, (M.SRC.get((sid, k)) or "").split(":")[0])
            tot[key] += 1
            if not any(R.presence(v, bs[i])[0] for i in idx):
                bad[key] += 1
                ex.setdefault(key, (ch, sid, idx[0]))
for key, n in sorted(bad.items(), key=lambda x: -x[1]):
    print(f"{n}/{tot[key]}\t{key[0]}\t{key[1]}\t{key[2]}\t{ex[key][0]} ^{ex[key][1]} s{ex[key][2]}")
