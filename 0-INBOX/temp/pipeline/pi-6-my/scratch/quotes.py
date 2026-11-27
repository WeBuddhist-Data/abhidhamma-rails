import pathlib, re, collections
HERE = pathlib.Path(__file__).resolve().parents[1]; ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"; MD = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
c = collections.Counter(); ex = {}
for p in sorted(PD.glob("*.md")):
    A = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(A, B), 1):
        xq = x.count('"') + x.count("“") + x.count("”")
        yq = y.count("“") + y.count("”")
        xs = x.count("‘") + x.count("’") + len(re.findall(r"(?<![a-zA-Zāīūṃṅñṭḍṇḷ])'|'(?![a-zA-Zāīūṃṅñṭḍṇḷ])", x))
        ys = y.count("‘") + y.count("’")
        if xq != yq or xs != ys:
            for q in re.findall(r"“[^”]*”", y):
                k = (p.name[:5], q)
                c[k] += 1; ex.setdefault(k, (i, x[:200], y[:200]))
for k, n in sorted(c.items()):
    print(n, k, ex[k][0]); print("   P:", ex[k][1]); print("   B:", ex[k][2])
