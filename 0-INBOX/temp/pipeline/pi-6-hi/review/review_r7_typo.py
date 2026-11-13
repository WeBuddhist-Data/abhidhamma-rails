import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from review_r7_pairs import load, P, H

FILES = [f'10-0{i}-indriyayamaka.md' for i in range(1, 8)]
idre = re.compile(r'\^(6-[\d-]+)\s*$')
for fn in FILES:
    pl, hl = load(fn)
    if len(pl) != len(hl):
        print(fn, 'LINECOUNT', len(pl), len(hl))
    # double blank lines
    raw = open(os.path.join(H, fn), encoding='utf-8').read()
    if '\n\n\n' in raw:
        print(fn, 'DOUBLE BLANK')
    for i, (p, h) in enumerate(zip(pl, hl), 1):
        mp, mh = idre.search(p), idre.search(h)
        if (mp and mp.group(1)) != (mh and mh.group(1)):
            print(fn, i, 'ID MISMATCH', mp and mp.group(1), mh and mh.group(1))
        pc = p.count('–') + p.count('—')
        hc = h.count('–') + h.count('—')
        if pc != hc:
            print(fn, i, 'DASH', pc, hc)
        if re.search(r'[A-Za-zāīūṃṅñṭḍṇḷ]{3,}', re.sub(r'\[[^\]]*\]', '', idre.sub('', h))):
            print(fn, i, 'LATIN', h[:120])
        if '"' in h or "'" in h:
            print(fn, i, 'STRAIGHTQUOTE')
        hb = idre.sub('', h).rstrip()
        pb = idre.sub('', p).rstrip()
        if h.startswith('#'):
            continue
        # sentence end check
        pend = pb[-1:] if pb else ''
        hend = hb[-1:] if hb else ''
        if pend == '?' and hend != '?':
            print(fn, i, 'END? ', repr(pb[-15:]), repr(hb[-15:]))
        if pend == '.' and hend not in '।':
            print(fn, i, 'END. ', repr(pb[-15:]), repr(hb[-15:]))
        if hb.count('?') != pb.count('?'):
            print(fn, i, 'QCOUNT', pb.count('?'), hb.count('?'))
        if '.' in hb.replace('...', '').replace('…', ''):
            print(fn, i, 'LATINDOT', hb[-40:])
        if re.search(r'\s[।?]', hb) or '।।' in hb or '  ' in hb:
            print(fn, i, 'SPACING', hb[-60:])
