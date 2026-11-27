import collections, pathlib, re, sys
R = pathlib.Path("/Users/lobsangtseten/Desktop/Abhidhamma-rails/abhidhamma-rails")
PD = R / "AI_translation/pali/pi-3_split_chapters"; MD = R / (sys.argv[1] if len(sys.argv) > 1 else "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters")
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
f = lambda p: [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
seen = collections.defaultdict(lambda: collections.defaultdict(set))
for p in sorted(PD.glob("*.md")):
    ch = p.name.split("-")[0].split(".")[0]
    for x, y in zip(f(p), f(MD / p.name)):
        xs, ys = re.split(r"(?<=[.?])\s+", x.strip()), re.split(r"(?<=။)\s+", y.strip())
        if len(xs) != len(ys): continue
        for s, t in zip(xs, ys):
            a = [c.strip(" ,") for c in re.split(r"…pe…|…Pe…|…|\.\.(?= )", s)]
            b = [c.strip(" ၊") for c in re.split(r"…|\.\.(?= )", t)]
            if len(a) != len(b): continue
            for c, d in zip(a, b):
                if c: seen[c][d].add(ch)
n = 0
for c, v in seen.items():
    if len(v) > 1 and len({d.replace("ကြ", "") for d in v}) > 1:
        chs = [set(x) for x in v.values()]
        n += 1
        print("PĀLI:", c[:120])
        for d, cs in v.items(): print("   ", sorted(cs), d[:160])
print("differing chunks:", n)
