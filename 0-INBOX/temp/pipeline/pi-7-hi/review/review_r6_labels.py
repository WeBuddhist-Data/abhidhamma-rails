import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *
c = collections.defaultdict(collections.Counter); ex = {}
for fi, f in enumerate(FILES):
    for r in pairs(f):
        p = IDRE.sub("", r["p"]); h = IDRE.sub("", r["h"])
        if " – " not in p:
            continue
        pl = re.findall(r"(?:^|[.;] )([A-ZĀ][^ .;–]*(?: [^ .;–]+)?) –", p)[1:]
        hl = re.findall(r"(?:^|[।;] )([^।;–]{1,40}?) –", h)[1:]
        tag = f"{fi}|{r['id']}|k{r['k']}"
        if len(pl) != len(hl):
            print("LABELCOUNT", tag, pl, hl); continue
        for a, b in zip(pl, hl):
            c[a][b] += 1; ex.setdefault((a, b), tag)
for a in c:
    print(a, "=>", {b: (n, ex[(a, b)]) for b, n in c[a].items()})
