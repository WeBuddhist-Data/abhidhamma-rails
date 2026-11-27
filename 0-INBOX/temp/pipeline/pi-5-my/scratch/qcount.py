"""scratch: lines where the number of quote marks (all kinds) in the Burmese differs from the Pāli (brackets removed)."""
import pathlib, re, collections, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]
PD = ROOT / "AI_translation/pali/pi-5_split_chapters"; MD = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
BK = pathlib.Path(__file__).resolve().parents[1] / "harmonise-backup/chapters"
d = BK if "--before" in sys.argv else MD
c = collections.Counter(); ex = collections.defaultdict(list)
for p in PD.glob("*.md"):
    if p.suffix != ".md": continue
    for i, (x, y) in enumerate(zip(p.read_text(encoding="utf-8-sig").split("\n"), (d / p.name).read_text().split("\n")), 1):
        if x.startswith("#"): continue
        xb = re.sub(r"\[[^\]]*\]", "", x); yb = re.sub(r"\[[^\]]*\]", "", y)
        if re.search(r"niṭṭhit[āoa]ṃ?\.", xb) and "ပြီးဆုံးပြီ" in yb: continue       # colophons «“X” ပြီးဆုံးပြီ»
        a = sum(xb.count(q) for q in '"‘’“”'); b = sum(yb.count(q) for q in '“”‘’')
        if a != b:
            k = "fewer" if b < a else "more"
            c[(p.name.split("-")[0], k)] += 1; ex[(p.name.split("-")[0], k)].append(i)
for k in sorted(c, key=lambda t: (int(t[0]) if t[0].isdigit() else 0, t[1])): print(k, c[k], ex[k][:8])
print(sum(v for (ch, k), v in c.items() if k == "more"), "more;", sum(v for (ch, k), v in c.items() if k == "fewer"), "fewer")
