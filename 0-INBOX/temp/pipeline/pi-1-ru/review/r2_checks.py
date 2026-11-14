import sys, re
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
files = ['2-03-cittuppadakandam.md', '2-04-cittuppadakandam.md', '2-05-cittuppadakandam.md']
nseg = 0
for f in files:
    rawR = open(base + r'\russian\pi-1-russian-plain-rails_split_chapters\\' + f, 'rb').read()
    if b'\r' in rawR:
        print(f, 'CR present')
    tR = rawR.decode('utf-8')
    if '\n\n\n' in tR:
        print(f, 'double blank line')
    P = open(base + r'\pali\pi-1_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    R = tR.split('\n')
    for i, (p, r) in enumerate(zip(P, R)):
        if not p.strip():
            continue
        if re.search(r'\^[\w-]+\s*$', p):
            nseg += 1
        tag = f'{f[:4]} L{i+1} {(re.search(r"\^[\w-]+", p) or re.search("", "")).group(0)}'
        # dashes
        dp = len(re.findall('[–—]', p)); dr = len(re.findall('[–—]', r))
        if dp != dr:
            print(tag, 'DASH', dp, dr)
        # ellipses
        ep = len(re.findall(r'…pe…|…', re.sub(r'…pe…', '§', p).replace('§', '…')))
        er = r.count('…')
        if ep != er:
            print(tag, 'ELLIPSIS', ep, er)
        # questions
        if p.count('?') != r.count('?'):
            print(tag, 'QMARK', p.count('?'), r.count('?'))
        if re.search(r'\bли\b', r):
            print(tag, 'LI')
        # hoti/honti vs есть
        hp = len(re.findall(r'\bhon?ti\b', p))
        # Latin outside brackets
        rr = re.sub(r'\[[^\]]*\]', '', r)
        rr = re.sub(r'\^[\w-]+', '', rr)
        lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', rr)
        if lat:
            print(tag, 'LATIN', lat[:5])
        # brackets
        if p.count('[') != r.count('['):
            print(tag, 'BRACKETS', p.count('['), r.count('['))
        # end punctuation
        pe = re.sub(r'\s*\^[\w-]+\s*$', '', p).rstrip()
        re_ = re.sub(r'\s*\^[\w-]+\s*$', '', r).rstrip()
        if pe and re_ and not pe.startswith('#') and pe[-1] != re_[-1]:
            print(tag, 'ENDPUNCT', repr(pe[-3:]), repr(re_[-3:]))
        if '—' in r:
            print(tag, 'EMDASH')
        if '  ' in r:
            print(tag, 'DOUBLESPACE')
        if re.search(r' [,.;:]', r):
            print(tag, 'SPACE BEFORE PUNCT', re.findall(r'.{10} [,.;:]', r)[:3])
        if re.search(r'"', r):
            print(tag, 'STRAIGHT QUOTE')
print('segments', nseg)
