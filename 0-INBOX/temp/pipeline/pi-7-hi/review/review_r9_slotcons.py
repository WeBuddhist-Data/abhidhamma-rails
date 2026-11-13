import os, json, sys
from collections import defaultdict, Counter
d = os.path.dirname(__file__)
slots = json.load(open(os.path.join(d, 'review_r9_slots.json'), encoding='utf-8'))
p2h = defaultdict(Counter)
h2p = defaultdict(Counter)
ex = {}
for f, ne, sid, kind, pk, hv, praw, hraw in slots:
    p2h[pk][hv] += 1
    h2p[hv][pk] += 1
    ex.setdefault((pk, hv), []).append('%s:%s(%s)' % (f[:4], ne, sid))
print('distinct pkeys', len(p2h), 'distinct hvals', len(h2p))
print('==== P keys with >1 Hindi')
for pk, c in sorted(p2h.items()):
    if len(c) > 1:
        print('P:', pk)
        for hv, n in c.most_common():
            print('   %4d  %s   %s' % (n, hv, ex[(pk, hv)][:4]))
print('==== Hindi with >1 P key')
for hv, c in sorted(h2p.items()):
    if len(c) > 1:
        print('H:', hv)
        for pk, n in c.most_common():
            print('   %4d  %s   %s' % (n, pk, ex[(pk, hv)][:4]))
if '--all' in sys.argv:
    print('==== ALL')
    for pk, c in sorted(p2h.items()):
        for hv, n in c.most_common():
            print('%4d | %s | %s' % (n, pk, hv))
