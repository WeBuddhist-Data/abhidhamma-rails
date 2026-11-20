import re, sys, unicodedata
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-2_split_chapters'
V = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-2-vietnamese-plain-rails_split_chapters'
CH = ['2-ayatanavibhango.md', '3-dhatuvibhango.md', '4-saccavibhango.md', '5-indriyavibhango.md']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f]

def sentences(s):
    return [x for x in re.split(r'(?<=[.?!])\s+', s) if x.strip()]

for ch in CH:
    pl = [l for l in lines(P + '\\' + ch) if l.strip()]
    vl = [l for l in lines(V + '\\' + ch) if l.strip()]
    raw = open(V + '\\' + ch, encoding='utf-8').read()
    print('=====', ch, len(pl), len(vl))
    if '\n\n\n' in raw: print('  double blank line')
    if '\r' in raw: print('  CR')
    if unicodedata.normalize('NFC', raw) != raw: print('  not NFC')
    if '….' in raw: print('  "…." found')
    if '"' in raw: print('  straight double quote found')
    for i, (p, v) in enumerate(zip(pl, vl)):
        # polarity counts
        a = (p.count('siyā'), v.count('đôi khi'))
        b = (len(re.findall(r'na vattabb', p)), v.count('không nên nói'))
        c = (p.count('…pe…') + p.count('…'), v.count('…'))
        d = (p.count('?'), v.count('?'))
        e = (len(re.findall(r'"', p)), v.count('“') + v.count('”'))
        f = (p.count('‘') + p.count('’'), v.count('‘') + v.count('’'))
        flags = []
        if a[0] != a[1]: flags.append('siyā %d/đôi khi %d' % a)
        if b[0] != b[1]: flags.append('na vattabb %d/không nên nói %d' % b)
        if p.count('…pe…') + p.count('…') - p.count('…pe…') != v.count('…'):
            flags.append('ellipsis p%d v%d' % (p.count('…'), v.count('…')))
        if d[0] != d[1]: flags.append('? %d/%d' % d)
        if e[0] != e[1]: flags.append('quotes %d/%d' % e)
        if f[0] != f[1]: flags.append("single quotes %d/%d" % f)
        # sentence count
        sp, sv = len(sentences(p)), len(sentences(v))
        if sp != sv: flags.append('sentences %d/%d' % (sp, sv))
        # latin words outside brackets
        vv = re.sub(r'\[[^\]]*\]', '', v)
        lat = re.findall(r'\b[a-zA-Zāīūṃṅñṭḍṇḷ]*[āīūṃṅñṭḍṇḷ][a-zA-Zāīūṃṅñṭḍṇḷ]*\b', vv)
        if lat: flags.append('pali? ' + ','.join(lat[:5]))
        idm = re.search(r'\^[\d-]+$', v)
        if flags:
            print(' line %d %s: %s' % (i + 1, idm.group(0) if idm else '', '; '.join(flags)))
