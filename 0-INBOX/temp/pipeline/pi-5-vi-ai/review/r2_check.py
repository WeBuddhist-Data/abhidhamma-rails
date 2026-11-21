import re, sys
sys.path.insert(0, 'D:/Work/OpenPecha/abhidhamma-rails/0-INBOX/temp/pipeline/pi-5-vi-ai/review')
R = 'D:/Work/OpenPecha/abhidhamma-rails/AI_translation/'
PI = R + 'pali/pi-5_split_chapters/'
VI = R + 'vietnamese/pi-5-vietnamese-plain-rails_split_chapters/'
CH = ['3-brahmacariyakatha.md', '4-jahatikatha.md', '5-sabbamatthitikatha.md', '6-atitakkhandhadikatha.md',
      '7-ekaccam-atthitikatha.md', '8-satipatthanakatha.md', '9-hevatthikatha.md', '10-dutiyavaggo.md']


def lines(p):
    return [l.rstrip('\n') for l in open(p, encoding='utf-8') if l.strip()]


def strip_br(s):
    return re.sub(r'\[[^\]]*\]', '', s)


tot = 0
for ch in CH:
    P = lines(PI + ch)
    V = lines(VI + ch)
    if len(P) != len(V):
        print(ch, 'LINE COUNT', len(P), len(V))
    for i, (p, v) in enumerate(zip(P, V)):
        tot += 1
        pp = strip_br(p)
        vv = strip_br(v)
        a1 = len(re.findall(r'Āmantā', pp))
        a2 = len(re.findall(r'Đúng vậy', vv))
        n1 = len(re.findall(r'[Nn]a hevaṃ vattabbe', pp))
        n2 = len(re.findall(r'Không nên nói như vậy', vv))
        q1 = pp.count('?')
        q2 = vv.count('?')
        d1 = pp.count('–')
        d2 = vv.count('–')
        e1 = pp.count('!')
        e2 = vv.count('!')
        pe1 = pp.count('…')
        pe2 = vv.count('…')
        ids1 = re.findall(r'\^[0-9a-z-]+$', p)
        ids2 = re.findall(r'\^[0-9a-z-]+$', v)
        probs = []
        if a1 != a2: probs.append('amanta %d/%d' % (a1, a2))
        if n1 != n2: probs.append('nahevam %d/%d' % (n1, n2))
        if q1 != q2: probs.append('q %d/%d' % (q1, q2))
        if d1 != d2: probs.append('dash %d/%d' % (d1, d2))
        if e1 != e2: probs.append('excl %d/%d' % (e1, e2))
        if ids1 != ids2: probs.append('id %s/%s' % (ids1, ids2))
        if probs:
            print(ch, i + 1, probs, '|', p[:70])
        if '“' in v and v.count('“') != v.count('”'):
            print(ch, i + 1, 'quote imbalance')
        if '….' in v or '—' in v:
            print(ch, i + 1, 'bad typography')
print('lines checked', tot)
