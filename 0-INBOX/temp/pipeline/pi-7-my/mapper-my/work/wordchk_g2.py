"""wordchk_g2.py: g2 values whose first chunk stands in the aligned sentence only inside another word (not after a
space / start / quote / bracket): candidates for review (read-only helper; g2)."""
import sys, re, pathlib, collections, importlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
G = importlib.import_module("map_g2")
M = G.mapper()
SP = re.compile(r"(?<=[.)?])\s+"); SB = re.compile(r"(?<=[။)?])\s+")
bad = collections.Counter(); ex = {}
for ch in G.CHAPTERS:
    B, P = R.burmese(ch), R.pali(ch)
    for sid, kws in R.keyword_rows(ch):
        p, b = P.get(sid, ""), B.get(sid, "")
        ps, bs = SP.split(p), SB.split(b)
        if len(ps) != len(bs):
            continue
        for k in kws:
            v = M.lookup(ch, sid, k, p, b)
            if v == R.NONE:
                continue
            first = v.split(" … ")[0].split()[0].strip("“”()")
            if first.endswith(("သည်", "သော", "ည့်", "၍")):
                continue
            rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(k) + r"(?![\wāīūṃṅñṭḍṇḷ])")
            ss = [bs[i] for i, s in enumerate(ps) if rx.search(s)]
            if not ss:
                continue
            if not any(re.search(r"(^|[\s“(‘…–-])" + re.escape(first), s) for s in ss):
                key = (k, v, (M.SRC.get((sid, k)) or "").split(":")[0])
                bad[key] += 1
                ex.setdefault(key, f"{ch} ^{sid}")
for key, n in sorted(bad.items(), key=lambda x: -x[1]):
    print(n, key, ex[key])
