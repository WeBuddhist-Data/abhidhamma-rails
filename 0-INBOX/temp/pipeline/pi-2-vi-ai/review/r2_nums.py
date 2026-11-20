import re
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters'
V = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters'
CH = ['2-ayatanavibhango.md', '3-dhatuvibhango.md', '4-saccavibhango.md', '5-indriyavibhango.md']
PN = [('ekavīsat', 21), ('bāvīsat', 22), ('aṭṭhāras', 18), ('sattaras', 17), ('soḷas', 16), ('pannaras', 15),
      ('cuddas', 14), ('teras', 13), ('dvādas', 12), ('ekādas', 11), ('das', 10), ('nav', 9), ('aṭṭh', 8),
      ('satt', 7), ('cha', 6), ('pañc', 5), ('cattār', 4), ('catunn', 4), ('tīṇ', 3), ('tiss', 3), ('dv', 2)]
VN = [('hai mươi hai', 22), ('hai mươi mốt', 21), ('mười tám', 18), ('mười bảy', 17), ('mười sáu', 16), ('mười lăm', 15),
      ('mười bốn', 14), ('mười ba', 13), ('mười hai', 12), ('mười một', 11), ('mười', 10), ('chín', 9), ('tám', 8),
      ('bảy', 7), ('sáu', 6), ('năm', 5), ('bốn', 4), ('ba', 3), ('hai', 2)]

def pnum(s):
    w = s.strip().lower()
    for k, n in PN:
        if w.startswith(k):
            return n
    return None

def vnum(s):
    w = s.strip().lower()
    w = re.sub(r'^(về |trong )', '', w)
    for k, n in VN:
        if w.startswith(k + ' '):
            return n
    return None

def sents(s):
    return [x for x in re.split(r'(?<=[.?!])\s+', s) if x.strip()]

for ch in CH:
    pl = [l for l in open(P + '\\' + ch, encoding='utf-8').read().split('\n') if l.strip()]
    vl = [l for l in open(V + '\\' + ch, encoding='utf-8').read().split('\n') if l.strip()]
    tot = 0
    for i, (p, v) in enumerate(zip(pl, vl)):
        ps, vs = sents(p), sents(v)
        if len(ps) != len(vs):
            continue
        for a, b in zip(ps, vs):
            na, nb = pnum(a), vnum(b)
            if 'vidhena' in a or '–' in a[:40] and 'vattabb' not in a: continue
            if na or nb:
                tot += 1
                if na != nb:
                    print(ch, 'line', i + 1, '| P:', a[:60], '| V:', b[:60], na, nb)
    print(ch, 'numbered sentences compared:', tot)
