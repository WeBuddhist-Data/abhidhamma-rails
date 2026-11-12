import re, sys, io
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
chs = ['6-paticcasamuppadavibhango', '8-sammappadhanavibhango', '9-iddhipadavibhango']
out = []
def lines(p):
    raw = open(p, encoding='utf-8').read()
    return raw, [l for l in raw.split('\n') if l.strip()]
for ch in chs:
    praw, P = lines(base + r'\pali\pi-2_split_chapters\%s.md' % ch)
    hraw, H = lines(base + r'\hindi\pi-2-hindi-plain-rails_split_chapters\%s.md' % ch)
    out.append('=== %s  P=%d H=%d' % (ch, len(P), len(H)))
    if '\n\n\n' in hraw: out.append('DOUBLE BLANK in hindi')
    for i, (p, h) in enumerate(zip(P, H), 1):
        pid = re.findall(r'\^[\d-]+\s*$', p); hid = re.findall(r'\^[\d-]+\s*$', h)
        if pid != hid: out.append('%d ID mismatch %s %s' % (i, pid, hid))
        pd = p.count('–') + p.count('—'); hd = h.count('–') + h.count('—')
        if pd != hd: out.append('%d dash P%d H%d' % (i, pd, hd))
        if '—' in h: out.append('%d emdash in H' % i)
        hs = re.sub(r'\[[^\]]*\]', '', h); hs = re.sub(r'\^[\d-]+', '', hs)
        lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', hs)
        if lat: out.append('%d latin %s' % (i, lat))
        if '"' in h or "'" in h: out.append('%d straight quote' % i)
        if h.count('“') != h.count('”'): out.append('%d unbalanced quotes' % i)
        if p.count('"') // 2 != h.count('“'): out.append('%d quote count P%d H%d' % (i, p.count('"') // 2, h.count('“')))
        pp = p.count('…pe…'); hp = h.count('…')
        if pp != hp: out.append('%d pe P%d H%d' % (i, pp, hp))
        hb = re.sub(r'\s*\^[\d-]+\s*$', '', h).rstrip()
        if not h.startswith('#') and hb and hb[-1] not in '।?': out.append('%d ending %r' % (i, hb[-5:]))
        if re.search(r'\.\s', hs) or hs.rstrip().endswith('.'): out.append('%d latin full stop' % i)
        pq = p.count('?'); hq = h.count('?')
        if pq != hq: out.append('%d ? P%d H%d' % (i, pq, hq))
        ps = len(re.findall(r'\bsiyā\b', p, re.I)); hs2 = h.count('कभी')
        if ps != hs2: out.append('%d siya P%d kabhi%d' % (i, ps, hs2))
open(r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\review\review_r2_checks.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('\n'.join(out))
