import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *
from collections import defaultdict
praw, pl = load(P)
hraw, hl = load(H)
m = defaultdict(list)
for (n, i, p), (_, _, h) in zip(pl, hl):
    if p.startswith('#'):
        pk = IDRE.sub('', p).strip()
        hk = IDRE.sub('', h).strip()
        m[pk].append((hk, n))
for pk, v in m.items():
    hs = defaultdict(list)
    for hk, n in v:
        hs[hk].append(n)
    flag = '  <<< VARIES' if len(hs) > 1 else ''
    print(pk, flag)
    for hk, ns in hs.items():
        print('     ', hk, ns[:6], len(ns))
