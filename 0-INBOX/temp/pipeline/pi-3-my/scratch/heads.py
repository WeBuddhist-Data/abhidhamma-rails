import pathlib, re, collections
R = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails")
P = R / "AI_translation/pali/pi-3_split_chapters"; M = R / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
d = collections.defaultdict(lambda: collections.defaultdict(list))
for p in sorted(P.glob("*.md")):
    a = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [l for l in (M / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(a, b), 1):
        x, y = ID.sub("", x), ID.sub("", y)
        if x.startswith("#") or re.fullmatch(r"\([^()]+\.\)", x) or "padaniddeso" in x or "niṭṭhita" in x:
            d[re.sub(r"^#+ ", "", x)][re.sub(r"^#+ ", "", y)].append(p.name.split("-")[0].split(".")[0])
for x, v in d.items():
    print(x, "|", " || ".join(f"{y} [{','.join(sorted(set(c)))}]" for y, c in v.items()))
