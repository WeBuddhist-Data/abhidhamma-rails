import re
P = 'D:\\Work\\OpenPecha\\abhidhamma-rails\\AI_translation\\pali\\pi-2_split_chapters\\'
R = 'D:\\Work\\OpenPecha\\abhidhamma-rails\\AI_translation\\russian\\pi-2-russian-plain-rails_split_chapters\\'
for ch in ['4-saccavibhango.md', '5-indriyavibhango.md', '6-paticcasamuppadavibhango.md']:
    rt = open(R + ch, encoding='utf-8').read()
    pt = open(P + ch, encoding='utf-8').read()
    print('==', ch)
    if '\n\n\n' in rt: print('double blank lines')
    if '\r' in rt: print('CR')
    if '—' in rt: print('em dash')
    pl = [l for l in pt.split('\n') if l.strip()]
    rl = [l for l in rt.split('\n') if l.strip()]
    for i, (p, r) in enumerate(zip(pl, rl)):
        rr = re.sub(r'\[[^\]]*\]', '', r)
        rr = re.sub(r'\^[\w\-]+$', '', rr)
        lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', rr)
        if lat: print(i, 'LATIN', lat[:5])
        if re.search(r'\bли\b', r): print(i, 'LI')
        checks = [
            (len(re.findall(r'\bsiyā\b', p)), len(re.findall(r'иногда', r)), 'siya'),
            (len(re.findall(r'vattabb', p)), len(re.findall(r'нельзя определить', r)), 'navattabba'),
            (p.count('?'), r.count('?'), '?'),
            (p.count('…'), r.count('…'), 'ellipsis'),
            (p.count('['), r.count('['), 'brackets'),
            (len(re.findall(r'"', p)) // 2, r.count('«'), 'quotes'),
        ]
        if ch.startswith('6'):
            checks.append((len(re.findall(r'paccayā(?:pi)?\b', p)), len(re.findall(r'обусловлен', r)), 'paccaya'))
        for a, b, n in checks:
            if a != b: print(i, n, a, b, '|', p[:70])
        end_p = re.sub(r'\s*\^[\w\-]+$', '', p).rstrip()
        end_r = re.sub(r'\s*\^[\w\-]+$', '', r).rstrip()
        if not end_p.startswith('#') and end_r[-1:] not in '.?!»':
            print(i, 'END', end_r[-20:])
