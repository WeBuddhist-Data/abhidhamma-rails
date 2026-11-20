import re, unicodedata
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['14-sikkhapadavibhango.md', '15-patisambhidavibhango.md', '16-nanavibhango.md']
latin = re.compile(r'\b[a-zA-Zāīūṃṅñṭḍṇḷ]*[āīūṃṅñṭḍṇḷ][a-zA-Zāīūṃṅñṭḍṇḷ]*\b')
for f in FILES:
    V = open(ROOT + r'\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\\' + f, encoding='utf-8').read()
    P = open(ROOT + r'\pali\pi-2_split_chapters\\' + f, encoding='utf-8').read()
    print('=====', f, 'NFC' if unicodedata.is_normalized('NFC', V) else 'NOT NFC', 'CR' if '\r' in V else '', 'dblblank' if '\n\n\n' in V else '')
    for n, l in enumerate(V.split('\n'), 1):
        s = re.sub(r'\[[^\]]*\]', '', l)
        s = re.sub(r'\^[0-9a-z\-]+', '', s)
        for m in latin.finditer(s):
            print('LATIN', n, m.group(0))
        if '….' in l or '..' in l.replace('…', ''): print('DOTS', n, l[:80])
        if '"' in l or "'" in l: print('STRAIGHTQ', n)
        if re.search(r'\s[,.;:?!]', l): print('SPACEPUNCT', n, re.search(r'.{0,20}\s[,.;:?!].{0,10}', l).group(0))
        # quote balance
        if l.count('“') != l.count('”'): print('QUOTEBAL', n, l.count('“'), l.count('”'))
        if l.count('‘') != l.count('’'): print('SQUOTEBAL', n)
        # repeated item inside comma list
        body = re.sub(r'\^[0-9a-z\-]+', '', l)
        for chunk in re.split(r'[.;:?!–“”]', body):
            items = [i.strip() for i in chunk.split(',') if i.strip()]
            if len(items) >= 3:
                for i in range(len(items)):
                    for j in range(len(items)):
                        if i != j and len(items[i].split()) >= 2 and re.search(r'(^|\s)' + re.escape(items[i]) + r'(\s|$)', items[j]) and items[i] != items[j]:
                            print('SUBITEM', n, repr(items[i]), 'in', repr(items[j][:60]))
    # question lines: Pali '?' vs Vietnamese '?'
    pl = [x for x in P.split('\n') if x.strip()]
    vl = [x for x in V.split('\n') if x.strip()]
    for k, (a, b) in enumerate(zip(pl, vl)):
        if a.count('?') != b.count('?'):
            print('QMARK', k, a.count('?'), b.count('?'), b[:80])
        da = len(re.findall(r'\(\d+[^)]*\)', a)); db = len(re.findall(r'\(\d+[^)]*\)', b))
        if da != db: print('DIGITPAREN', k, da, db)
