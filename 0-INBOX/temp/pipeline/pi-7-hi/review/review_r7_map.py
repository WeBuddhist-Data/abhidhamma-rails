import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *
praw, pl = load(P)
S = segs(pl)
m = {x[1]: (x[0], sid) for (x, sid) in S}
mn = {x[0]: (x[1], sid) for (x, sid) in S}
for a in sys.argv[1:]:
    print(a, mn.get(int(a[1:])) if a.startswith('n') else m.get(int(a)))

