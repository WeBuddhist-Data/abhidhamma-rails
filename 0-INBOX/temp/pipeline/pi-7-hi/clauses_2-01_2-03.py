import re, sys, pathlib, collections
D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["2-01-vitakkattika.md", "2-02-pitittika.md", "2-03-dassanenapahatabbattika.md"]
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SPL = re.compile(r"\s*(?: – |\.\s|…pe…|…|; |, |\(\d\))\s*")
c = collections.Counter()
for f in FILES:
    for l in (D / f).read_text(encoding="utf-8").splitlines():
        if not l.strip() or l.startswith("#"):
            continue
        l = ID.sub("", l)
        for part in SPL.split(l):
            part = part.strip(" .")
            if part:
                c[part] += 1
print("unique", len(c), "total", sum(c.values()))
if len(sys.argv) > 1:
    for k, v in c.most_common():
        print(v, k)
