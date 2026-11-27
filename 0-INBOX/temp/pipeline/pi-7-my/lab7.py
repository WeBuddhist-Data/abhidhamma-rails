"""Sahajātā label survey (read-only): for every Pāli sentence starting «Sahajātā –» (or «Sahajātaṃ –»), the Burmese label
before « –» in the aligned sentence, with the condition of the enclosing line (kamma / other)."""
import pathlib, re, sys, collections
HERE = pathlib.Path(__file__).resolve().parent
R = HERE.parents[3]
PD = R / "AI_translation/pali/pi-7_split_chapters"; MD = R / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
c = collections.Counter(); ex = {}
for p in sorted(PD.glob("*.md")):
    pl = p.read_text(encoding="utf-8-sig").split("\n"); ml = (MD / p.name).read_text(encoding="utf-8").split("\n")
    sect = "?"
    for i, (x, y) in enumerate(zip(pl, ml), 1):
        if x.startswith("#") or re.match(r"^\*?\(?\d+\)?\.? ?[A-Z]", x):
            if re.search(r"[Kk]ammapaccay", x): sect = "kamma"
            elif re.search(r"paccay", x): sect = "other"
        n = len(re.findall(r"(?:^|[.;–] )Sahajātā – ", x))
        if not n: continue
        k = "kamma-line" if re.search(r"kammapaccayena", x) else "other-line"
        labs = re.findall(r"(?:^|[။၊–] )([^။၊–]{2,40}?) – ", y)
        lab = [l for l in labs if "ပေါ်ပေါက်" in l]
        for l in lab or ["(none found)"]:
            c[(k, sect, l)] += 1; ex.setdefault((k, sect, l), f"{p.name[:5]}:{i}")
for k, v in sorted(c.items()):
    print(v, k, ex[k])
