import re, sys, pathlib, collections
D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["2-01-vitakkattika.md", "2-02-pitittika.md", "2-03-dassanenapahatabbattika.md"]
pat = re.compile(sys.argv[1])
c = collections.Counter()
for f in FILES:
    t = (D / f).read_text(encoding="utf-8")
    for m in pat.finditer(t):
        c[m.group(0)] += 1
for k, v in sorted(c.items()):
    print(v, k)
