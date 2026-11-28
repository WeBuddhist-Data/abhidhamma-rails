"""r5: structural / typography checks per line pair."""
import re, sys
P = 'AI_translation/pali/pi-6_split_chapters/'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/'
FILES = ['7-06-anusayayamaka', '7-07-anusayayamaka', '7-08-anusayayamaka', '7-09-anusayayamaka',
         '7-10-anusayayamaka', '7-11-anusayayamaka', '8-cittayamaka']
idrx = re.compile(r'\^[\w-]+\s*$')
segs = 0
for f in FILES:
    pt = open(P + f + '.md', encoding='utf-8').read()
    rt = open(R + f + '.md', encoding='utf-8').read()
    if '\r' in rt: print(f, 'CR in russian')
    if '\n\n\n' in rt: print(f, 'double blank')
    pl, rl = pt.split('\n'), rt.split('\n')
    if len(pl) != len(rl): print(f, 'LINECOUNT', len(pl), len(rl))
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        if bool(p.strip()) != bool(r.strip()):
            print(f, i, 'BLANK MISMATCH'); continue
        if not p.strip(): continue
        pid = re.findall(r'\^[\w-]+$', p.strip()); rid = re.findall(r'\^[\w-]+$', r.strip())
        if pid != rid: print(f, i, 'ID', pid, rid)
        if pid: segs += 1
        for ch in '–—':
            if p.count(ch) != r.count(ch): print(f, i, 'DASH', repr(ch), p.count(ch), r.count(ch))
        if re.search(r'(?<![а-яё])ли(?![а-яё])', r): print(f, i, 'LI')
        if p.count('?') != r.count('?'): print(f, i, 'QMARK', p.count('?'), r.count('?'))
        rr = re.sub(r'\[[^\]]*\]', '', r)
        rr = re.sub(r'\^[\w-]+', '', rr)
        lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', rr)
        if lat: print(f, i, 'LATIN', lat[:5])
        if p.count('…pe') != r.count('…'):
            print(f, i, 'PE', p.count('…pe'), r.count('…'))
        if '"' in r or '“' in r and '„' not in r: print(f, i, 'QUOTES')
        if re.search(r'(\b\w+\b) \1\b', r): print(f, i, 'REPEAT', re.search(r'(\b\w+\b) \1\b', r).group(0))
        if not p.startswith('#'):
            pe = p.rstrip(); pe = idrx.sub('', pe).rstrip()
            re_ = idrx.sub('', r.rstrip()).rstrip()
            if pe[-1:] != re_[-1:]: print(f, i, 'END', repr(pe[-12:]), repr(re_[-12:]))
print('segments', segs)
