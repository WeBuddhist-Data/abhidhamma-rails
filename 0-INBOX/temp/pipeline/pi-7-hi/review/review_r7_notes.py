import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *
from collections import defaultdict
praw, pl = load(P)
hraw, hl = load(H)
seen = defaultdict(list)
mism = []
for (n, i, p), (_, _, h) in zip(pl, hl):
    pn = [x for x in re.findall(r'\(([^()]*)\)', p) if re.search(r'[a-zA-Z]', x)]
    hn = [x for x in re.findall(r'\(([^()]*)\)', h) if not re.fullmatch(r'\d+', x)]
    if len(pn) != len(hn):
        mism.append((n, pn, hn))
    for a, b in zip(pn, hn):
        seen[a].append((b, n))
for n, a, b in mism:
    print('NOTECOUNT', n, a, b)
for a, v in seen.items():
    hs = defaultdict(list)
    for b, n in v:
        hs[b].append(n)
    for b, ns in hs.items():
        print(f'{a}  =>  {b}  {ns[:4]}{"+" if len(ns) > 4 else ""}{" <<VAR" if len(hs) > 1 else ""}')
