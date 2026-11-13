"""Helper for build_2-04_2-08_hi.py: list parentheticals and word types in the five Pāli files."""
import re, pathlib, collections
D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["2-04-dassanenapahatabbahetukattika.md", "2-05-acayagamittika.md", "2-06-sekkhattika.md",
         "2-07-parittattika.md", "2-08-parittarammanattika.md"]
par = collections.Counter()
for f in FILES:
    t = (D / f).read_text(encoding="utf-8")
    t = re.sub(r"\{[^}]*\}", "", t)
    for m in re.finditer(r"\(([^()]*)\)", t):
        s = m.group(1).strip()
        if re.fullmatch(r"\d+\.?", s):
            continue
        par[s.lower()] += 1
for k, v in sorted(par.items()):
    print(v, "|", k)
