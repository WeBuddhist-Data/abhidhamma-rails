import re, sys
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
files = sys.argv[1:] or ['17-khuddakavatthuvibhango.md', '14-sikkhapadavibhango.md', '10-bojjhangavibhango.md']
idre = re.compile(r'\^([0-9a-z-]+)\s*$')
for f in files:
    P = open(base + r'\pali\pi-2_split_chapters\\' + f, encoding='utf8').read()
    H = open(base + r'\hindi\pi-2-hindi-plain-rails_split_chapters\\' + f, encoding='utf8').read()
    print('=====', f)
    if '\n\n\n' in H:
        print('DOUBLE BLANK in Hindi')
    pl = [l for l in P.split('\n') if l.strip()]
    hl = [l for l in H.split('\n') if l.strip()]
    if len(pl) != len(hl):
        print('LINECOUNT', len(pl), len(hl))
    for i, (p, h) in enumerate(zip(pl, hl), 1):
        out = []
        pi = idre.search(p); hi = idre.search(h)
        if (pi and pi.group(1)) != (hi and hi.group(1)):
            out.append('ID %s/%s' % (pi and pi.group(1), hi and hi.group(1)))
        pd = p.count('–') + p.count('—'); hd = h.count('–') + h.count('—')
        if pd != hd:
            out.append('DASH p%d h%d' % (pd, hd))
        if '—' in h:
            out.append('EMDASH')
        # ellipses
        pe = len(re.findall(r'…', p)) ; he = len(re.findall(r'…', h))
        pp = len(re.findall(r'…\s*pe\s*…|…', p))
        npe = len(re.findall(r'…\s*pe\s*…', p)); nsingle = p.count('…') - 2 * npe
        exp = npe + nsingle
        if exp != he:
            out.append('ELL p%d h%d' % (exp, he))
        hs = idre.sub('', h).rstrip()
        if hs.startswith('#'):
            pass
        elif not (hs.endswith('।') or hs.endswith('?') or hs.endswith('।”') or hs.endswith('?”')):
            out.append('END[%s]' % hs[-6:])
        # latin outside brackets
        nob = re.sub(r'\[[^\]]*\]', '', idre.sub('', h))
        lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', nob)
        if lat:
            out.append('LATIN ' + ','.join(lat[:5]))
        if '"' in h or "'" in h:
            out.append('STRAIGHTQUOTE')
        if h.count('“') != h.count('”'):
            out.append('QUOTEBAL')
        pq = p.count('"') // 2 + p.count('“')
        hq = h.count('“')
        if pq != hq:
            out.append('QUOTES p%d h%d' % (pq, hq))
        if re.search(r'[0-9०-९]', idre.sub('', h)) or re.search(r'[0-9]', idre.sub('', p)):
            pn = re.findall(r'[0-9]+', re.sub(r'\[[^\]]*\]', '', idre.sub('', p)))
            hn = re.findall(r'[0-9०-९]+', re.sub(r'\[[^\]]*\]', '', idre.sub('', h)))
            if pn != hn:
                out.append('NUM p%s h%s' % (pn, hn))
        if re.search(r'।।|\s।|,,|  ', h):
            out.append('PUNCT')
        if out:
            print(i, (hi and hi.group(1)), ' | '.join(out))
