"""r4 helper: line-by-line mechanical checks of pi-2 Vietnamese vs Pali for chapters 8-13. Console only.
Checks: line counts per segment, dash counts per line, '…' (pe) counts per line, question marks,
'….' sequences, double blank lines, capital after semicolon, Latin-ish words outside brackets,
siyā vs «đôi khi» counts, na vattabbā vs «không nên nói» counts, number words.
"""
import re, sys
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
chs = ['8-sammappadhanavibhango', '9-iddhipadavibhango', '10-bojjhangavibhango',
       '11-maggangavibhango', '12-jhanavibhango', '13-appamannavibhango']
LAT = re.compile(r'\b[a-zA-Zāīūṃṅñṭḍṇḷ]*[āīūṃṅñṭḍṇḷ][a-zA-Zāīūṃṅñṭḍṇḷ]*\b')
for ch in chs:
    pl = open(base + r'\pali\pi-2_split_chapters\%s.md' % ch, encoding='utf-8').read()
    vl = open(base + r'\vietnamese\pi-2-vietnamese-plain-rails_split_chapters\%s.md' % ch, encoding='utf-8').read()
    if '\n\n\n' in vl: print(ch, 'DOUBLE BLANK')
    if '\r' in vl: print(ch, 'CR')
    P = [l for l in pl.split('\n') if l.strip()]
    V = [l for l in vl.split('\n') if l.strip()]
    print('==', ch, 'lines', len(P), len(V))
    for i, (p, v) in enumerate(zip(P, V)):
        pid = re.findall(r'\^[\d-]+', p); vid = re.findall(r'\^[\d-]+', v)
        if pid != vid: print(ch, i, 'ID mismatch', pid, vid)
        pd = p.count('–') + p.count('—'); vd = v.count('–') + v.count('—')
        if pd != vd: print(ch, i, pid, 'DASH', pd, vd)
        pe = p.count('…'); ve = v.count('…')
        if pe != ve: print(ch, i, pid, 'ELLIPSIS', pe, ve)
        if p.count('?') != v.count('?'): print(ch, i, pid, 'QMARK', p.count('?'), v.count('?'))
        if '….' in v or '…,' in v: print(ch, i, pid, 'ellipsis+punct', re.findall(r'.{20}…[.,].{0,10}', v))
        for m in re.finditer(r'; [A-ZĐÂĂÊÔƠƯ]', v): print(ch, i, pid, 'CAP after ;', v[m.start()-30:m.start()+20])
        vv = re.sub(r'\[[^\]]*\]', '', v)
        lat = [w for w in LAT.findall(vv)]
        if lat: print(ch, i, pid, 'LATIN?', lat[:5])
        sy = len(re.findall(r'\bsiyā\b', p, re.I)); dk = len(re.findall(r'đôi khi', v, re.I))
        if sy != dk: print(ch, i, pid, 'siya/doi khi', sy, dk)
        nv = len(re.findall(r'vattabb', p)); kn = len(re.findall(r'không nên nói', v, re.I))
        if nv != kn: print(ch, i, pid, 'na vattabba/khong nen noi', nv, kn)
