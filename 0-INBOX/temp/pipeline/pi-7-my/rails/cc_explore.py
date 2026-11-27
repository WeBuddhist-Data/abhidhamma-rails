import pathlib, re, collections, unicodedata
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"; BD = ROOT / "AI_translation/burmese/pi-7-burmese-plain-rails_split_chapters"
c = collections.Counter(); ex = collections.defaultdict(list)
for p in sorted(PD.glob("*.md")):
    pl = N(p.read_text(encoding="utf-8-sig")).split("\n"); bl = N((BD / p.name).read_text(encoding="utf-8")).split("\n")
    for k, (a, b) in enumerate(zip(pl, bl), 1):
        np_ = len(re.findall(r"paccayena paccayo", a))
        nb = len(re.findall(r"အကြောင်းဖြင့် အကြောင်း (?:ဖြစ်|မဖြစ်)", b))
        c[(np_ > 0, np_ == nb)] += 1
        if np_ and np_ != nb and len(ex[p.name]) < 2: ex[p.name].append((k, np_, nb, a[:300], b[:300]))
print(c)
for f, v in list(ex.items())[:8]:
    for e in v: print(f, e)
