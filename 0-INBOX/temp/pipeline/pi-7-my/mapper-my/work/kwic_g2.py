"""kwic_g2.py: for each line of work/dev_g2-out.txt (UNM / STEM), the Pāli sentence with the keyword and the Burmese
sentence of the same index (read-only helper; g2)."""
import sys, re, pathlib
sys.dont_write_bytecode = True
D = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(D))
import map7_rules as R
maxper = int(sys.argv[1]) if len(sys.argv) > 1 else 2
seen = {}
for l in (D / "work/dev_g2-out.txt").read_text(encoding="utf-8").splitlines():
    f = l.split("\t")
    kind, ch, sid, kw = f[:4]
    seen[kw] = seen.get(kw, 0) + 1
    if seen[kw] > maxper:
        continue
    rx = re.compile(r"(?<![\wāīūṃṅñṭḍṇḷ])" + re.escape(kw) + r"(?![\wāīūṃṅñṭḍṇḷ])")
    p = R.pali(ch).get(sid, ""); b = R.burmese(ch).get(sid, "")
    ps = re.split(r"(?<=[.)?])\s+", p); bs = re.split(r"(?<=[။)?])\s+", b)
    for i, s in enumerate(ps):
        if rx.search(s):
            print(f"== {kind} {kw} {' '.join(f[4:])} | {ch} ^{sid} [{i}/{len(ps)}|{len(bs)}]")
            print("PI:", s[:500])
            print("MY:", (bs[i] if i < len(bs) else "?")[:600])
            break
    else:
        print(f"== {kind} {kw} | {ch} ^{sid} NOT FOUND in sentences; PI:", p[:300])
