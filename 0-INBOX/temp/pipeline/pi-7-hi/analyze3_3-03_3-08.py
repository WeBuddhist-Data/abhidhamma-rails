import re, sys, collections, pathlib
P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md",
         "3-06-oghayogagocchaka.md", "3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md"]
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
par = collections.Counter()
heads = collections.Counter()
for f in FILES:
    for l in (P / f).read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        l = ID.sub("", l)
        if l.startswith("#"):
            heads[l] += 1
            continue
        for m in re.findall(r"\(([^()]*)\)", l):
            if not re.fullmatch(r"\d+", m):
                par[m] += 1
mode = sys.argv[1]
src = par if mode == "par" else heads
for c, n in sorted(src.items()):
    print(n, c)
