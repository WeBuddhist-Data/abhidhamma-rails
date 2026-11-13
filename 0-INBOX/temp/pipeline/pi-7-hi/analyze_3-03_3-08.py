import re, sys, collections, pathlib
P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md",
         "3-06-oghayogagocchaka.md", "3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md"]
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
lines = collections.Counter()
words = collections.Counter()
for f in FILES:
    for l in (P / f).read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        l = ID.sub("", l)
        lines[l] += 1
        for w in re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+", l):
            words[w.lower()] += 1
print("nonempty", sum(lines.values()), "unique lines", len(lines))
print("unique words", len(words))
mode = sys.argv[1] if len(sys.argv) > 1 else ""
if mode == "words":
    for w, c in sorted(words.items()):
        print(c, w)
