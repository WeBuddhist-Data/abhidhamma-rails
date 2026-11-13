import os, json, sys, re
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(__file__))
from review_r9_items import items_of as items_of2
d = os.path.dirname(__file__)
slots = json.load(open(os.path.join(d, 'review_r9_slots.json'), encoding='utf-8'))
HET = {'het': 'मूल रूपी', 'nahet': 'मूल रूपी न होने वाली'}
atoms = defaultdict(Counter)
exs = {}
bad = []


def items_of(pk):
    items, cur = [], []
    for t in pk.split():
        if t == '&':
            if cur:
                items.append(cur)
            cur = []
        elif t != 'dhamm':
            cur.append(t)
    if cur:
        items.append(cur)
    return items


def add(part, p, h, f, ne):
    atoms[(part, p)][h] += 1
    exs.setdefault(((part, p), h), '%s:%s' % (f[:4], ne))


items_of = lambda pk: [x.split() for x in items_of2(pk)]
# pass 1
for f, ne, sid, kind, pk, hv, praw, hraw in slots:
    items = items_of(pk)
    if len(items) != 1:
        continue
    it = items[0]
    if f.startswith('4-15'):
        duka = it[-1]
        if duka in HET and hv.endswith(', ' + HET[duka]):
            add('tika', ' '.join(it[:-1]), hv[:-len(', ' + HET[duka])], f, ne)
        else:
            bad.append((f, ne, sid, pk, hv))
    elif f.startswith('4-02'):
        duka = it[0]
        if duka in HET and hv.startswith(HET[duka] + ', '):
            add('tika', ' '.join(it[1:]), hv[len(HET[duka] + ', '):], f, ne)
        else:
            bad.append((f, ne, sid, pk, hv))
TIKA = {k[1]: c.most_common(1)[0][0] for k, c in atoms.items() if k[0] == 'tika'}
# pass 2
for f, ne, sid, kind, pk, hv, praw, hraw in slots:
    if f.startswith('4-15') or f.startswith('4-02'):
        continue
    items = items_of(pk)
    if len(items) != 1:
        continue
    it = items[0]
    found = None
    for n in (4, 3, 2, 1):
        if len(it) > n and ' '.join(it[-n:]) in TIKA:
            found = n
            break
    if not found:
        bad.append((f, ne, sid, pk, hv, 'no tika'))
        continue
    tp = ' '.join(it[-found:]); th = TIKA[tp]
    if not hv.endswith(', ' + th):
        bad.append((f, ne, sid, pk, hv, 'tika mismatch: expected ' + th))
        continue
    add('duka', ' '.join(it[:-found]), hv[:-len(', ' + th)], f, ne)
print('BAD (not decomposable):', len(bad))
for b in bad:
    print('  ', b)
rev = defaultdict(Counter)
for k, c in atoms.items():
    for h, n in c.items():
        rev[(k[0], h)][k[1]] += n
print('==== atoms')
for k in sorted(atoms):
    c = atoms[k]
    flag = '!!' if len(c) > 1 else '  '
    for h, n in c.most_common():
        flag2 = '<<' if len(rev[(k[0], h)]) > 1 else ''
        print('%s %-5s %-45s %4d  %s  %s %s' % (flag, k[0], k[1], n, h, exs[(k, h)], flag2))
