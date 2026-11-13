import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *

praw, pl = load(P)
hraw, hl = load(H)
S = segs(pl)

PN = {'eka': 1, 'ekaṃ': 1, 'eko': 1, 'ekā': 1, 'ekassa': 1, 'ekaṃ,': 1,
      'dve': 2, 'dvinnaṃ': 2, 'dvīsu': 2, 'tayo': 3, 'tīṇi': 3, 'tiṇṇannaṃ': 3, 'tiṇṇaṃ': 3,
      'cattāri': 4, 'catunnaṃ': 4, 'pañca': 5, 'cha': 6, 'satta': 7, 'aṭṭha': 8, 'nava': 9, 'dasa': 10,
      'ekādasa': 11, 'dvādasa': 12, 'terasa': 13, 'cuddasa': 14, 'pannarasa': 15, 'soḷasa': 16, 'sattarasa': 17}
HN = {'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पाँच': 5, 'छह': 6, 'सात': 7, 'आठ': 8, 'नौ': 9, 'दस': 10,
      'ग्यारह': 11, 'बारह': 12, 'तेरह': 13, 'चौदह': 14, 'पंद्रह': 15, 'सोलह': 16, 'सत्रह': 17}

def pnums(t):
    t = IDRE.sub('', t)
    t = re.sub(r'\(\d+\)', '', t)
    out = []
    for w in re.findall(r"[^\s,.;:–…()?“”‘’]+", t):
        w2 = w.lower()
        if w2 in PN:
            out.append(PN[w2])
    return out

def hnums(t):
    t = IDRE.sub('', t)
    t = re.sub(r'\(\d+\)', '', t)
    t = re.sub(r'दो का वर्गीकरण|दो-दो', '', t)
    out = []
    for w in re.findall(r"[^\s,.;:–…()?।“”‘’\-]+", t):
        if w in HN:
            out.append(HN[w])
    return out

def ell(p):
    p = p.replace('…pe…', '\x00')
    return p.count('\x00') + p.count('…')

for ((n, i, p), sid), (_, _, h) in zip(S, hl):
    if p.startswith('#'):
        continue
    a, b = pnums(p), hnums(h)
    if a != b:
        print('NUM', n, sid, a, b)
    e1, e2 = ell(p), h.count('…')
    if e1 != e2:
        print('ELL', n, sid, e1, e2)
