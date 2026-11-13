import os, json, sys, re
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(__file__))
from review_r9_items import items_of as items_of2
d = os.path.dirname(__file__)
slots = json.load(open(os.path.join(d, 'review_r9_slots.json'), encoding='utf-8'))


def items_of(pk):
    items, cur = [], []
    for t in pk.split():
        if t == '&':
            if cur:
                items.append(' '.join(cur))
            cur = []
        elif t != 'dhamm':
            cur.append(t)
    if cur:
        items.append(' '.join(cur))
    return items


items_of = items_of2
single = defaultdict(Counter)
for f, ne, sid, kind, pk, hv, praw, hraw in slots:
    it = items_of(pk)
    if len(it) == 1:
        single[it[0]][hv] += 1
S = {k: c.most_common(1)[0][0] for k, c in single.items()}
nok = 0
conj = Counter()
amb = {}
for f, ne, sid, kind, pk, hv, praw, hraw in slots:
    it = items_of(pk)
    if len(it) < 2:
        continue
    if any(i not in S for i in it):
        print('UNKNOWN item', f, ne, sid, it, '|', hv)
        continue
    exp = [S[i] for i in it]
    ok = False
    for c in (' और ', ' तथा '):
        for sep in (', ', c):
            cand = sep.join(exp[:-1]) + c + exp[-1]
            if cand == hv:
                ok = True
                conj[c.strip()] += 1
                if any(' और ' in e for e in exp) and 'परिघटना और' not in hraw and 'परिघटना तथा' not in hraw:
                    amb.setdefault(c.strip(), set()).add(sid)
    if not ok:
        print('MISMATCH', f, ne, sid, kind)
        print('   P:', praw)
        print('   H:', hraw)
        print('   exp:', ' + '.join(exp))
    else:
        nok += 1
print('ok', nok, conj)
for k, v in amb.items():
    print('items containing और joined with', k, len(v), sorted(v, key=lambda s: [int(x) if x.isdigit() else 0 for x in s.split('-')]))
