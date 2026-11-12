import re, sys
BASE = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
CH = '1-khandhavibhango.md'
P = BASE + r'\pali\pi-2_split_chapters\\' + CH
H = BASE + r'\hindi\pi-2-hindi-plain-rails_split_chapters\\' + CH
E = BASE + r'\english\pi-2-english-plain-zeroshot_split_chapters\\' + CH

def load(f):
    raw = open(f, encoding='utf-8').read()
    return raw, [l for l in raw.split('\n') if l.strip()]

praw, pl = load(P)
hraw, hl = load(H)
eraw, el = load(E)
idre = re.compile(r'\^([\w-]+)\s*$')

def pid(l):
    m = idre.search(l); return m.group(1) if m else None

mode = sys.argv[1] if len(sys.argv) > 1 else 'check'
if mode == 'show':
    a, b = int(sys.argv[2]), int(sys.argv[3])
    lang = sys.argv[4] if len(sys.argv) > 4 else 'ph'
    for i in range(a - 1, min(b, len(pl))):
        print(f'--- {i+1}')
        if 'p' in lang: print('P:', pl[i])
        if 'h' in lang: print('H:', hl[i])
        if 'e' in lang: print('E:', el[i])
    sys.exit()

print('lines', len(pl), len(hl), len(el))
print('double blanks H:', len(re.findall(r'\n\s*\n\s*\n', hraw)))
NUMP = {'eka':1,'dvi':2,'duv':2,'ti':3,'tiv':3,'catu':4,'catub':4,'pañca':5,'cha':6,'satta':7,'aṭṭha':8,'nava':9,'dasa':10}
for i, (p, h) in enumerate(zip(pl, hl), 1):
    iss = []
    if pid(p) != pid(h): iss.append(f'ID {pid(p)} vs {pid(h)}')
    hp = re.match(r'#+', p); hh = re.match(r'#+', h)
    if (hp and hp.group()) != (hh and hh.group()): iss.append('heading level')
    dp = p.count('–') + p.count('—'); dh = h.count('–') + h.count('—')
    if dp != dh: iss.append(f'dash {dp} vs {dh}')
    if '—' in h: iss.append('em dash in H')
    body = idre.sub('', h).rstrip()
    if not p.startswith('#'):
        if not (body.endswith('।') or body.endswith('?') or body.endswith('…') or body.endswith(':')):
            iss.append('end:' + body[-8:])
    nob = re.sub(r'\[[^\]]*\]', '', idre.sub('', h))
    lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]+', nob)
    if lat: iss.append('latin ' + ','.join(lat[:5]))
    if re.search(r'["\'«»]', nob): iss.append('quote chars')
    pe = p.count('…pe…') + p.count('...pe...') + len(re.findall(r'\bpe\b', p.replace('…pe…','')))
    hel = h.count('…')
    if pe != hel: iss.append(f'pe {pe} vs … {hel}')
    if '. ' in body or body.endswith('.'): iss.append('period')
    if '  ' in h: iss.append('double space')
    si = len(re.findall(r'\bsiyā\b', p, re.I)); ka = h.count('कभी')
    if si != ka: iss.append(f'siyā {si} vs कभी {ka}')
    if iss: print(i, pid(p) or '', '|', '; '.join(iss))
