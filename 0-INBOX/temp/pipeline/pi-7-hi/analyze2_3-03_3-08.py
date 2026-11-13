import re, sys, collections, pathlib
P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md",
         "3-06-oghayogagocchaka.md", "3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md"]
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SUB = [("saññojaniy", "XNIY"), ("ganthaniy", "XNIY"), ("nīvaraṇiy", "XNIY"), ("parāmaṭṭh", "XNIY"),
       ("asaññojaniy", "aXNIY"), ("sāsav", "XNIY"), ("anāsav", "aXNIY"),
       ("saññojan", "X"), ("ganth", "X"), ("nīvaraṇ", "X"), ("parāmās", "X"), ("āsav", "X")]
cl = collections.Counter()
for f in FILES:
    for l in (P / f).read_text(encoding="utf-8").splitlines():
        if not l.strip() or l.startswith("#"):
            continue
        l = ID.sub("", l)
        for a, b in SUB:
            l = l.replace(a, b).replace(a.capitalize(), b)
        for c in re.split(r" – |; |\. |…pe…|…", l):
            c = c.strip(" .,")
            if c:
                cl[c] += 1
print("unique clause templates", len(cl), "total", sum(cl.values()))
if len(sys.argv) > 1:
    for c, n in sorted(cl.items(), key=lambda x: -x[1]):
        print(n, c)
