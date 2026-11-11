import re, os
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-1_split_chapters'
H = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters'
FILES = ['preamble.md', '1-matika.md', '2-01-cittuppadakandam.md', '2-02-cittuppadakandam.md', '2-03-cittuppadakandam.md',
         '2-04-cittuppadakandam.md', '2-05-cittuppadakandam.md']
ORD = {'पहल': 1, 'प्रथम': 1, 'दूसर': 2, 'द्वितीय': 2, 'तीसर': 3, 'तृतीय': 3, 'चौथ': 4, 'चतुर्थ': 4, 'पाँचव': 5, 'छठ': 6, 'सातव': 7, 'आठव': 8}
PORD = {'paṭham': 1, 'dutiy': 2, 'tatiy': 3, 'catutth': 4, 'pañcam': 5, 'chaṭṭh': 6, 'sattam': 7, 'aṭṭham': 8}


def raw(d, f):
    return open(os.path.join(d, f), encoding='utf-8').read()


segs = 0
for f in FILES:
    a = raw(P, f)
    b = raw(H, f)
    pl = [l for l in a.split('\n') if l.strip()]
    hl = [l for l in b.split('\n') if l.strip()]
    print('==', f, len(pl), len(hl), 'double-blank', len(re.findall(r'\n\s*\n\s*\n', b)), 'trailing-ws', sum(1 for l in b.split('\n') if l != l.rstrip()))
    for i, (x, y) in enumerate(zip(pl, hl), 1):
        idx = re.search(r'\^([\w-]+)\s*$', x)
        idy = re.search(r'\^([\w-]+)\s*$', y)
        if idx: segs += 1
        if bool(idx) != bool(idy) or (idx and idx.group(1) != idy.group(1)):
            print('ID', i, idx and idx.group(1), idy and idy.group(1))
        tag = idx.group(1) if idx else f'L{i}'
        xs = re.sub(r'\[[^\]]*\]', '', x)
        ys = re.sub(r'\[[^\]]*\]', '', y)
        # dash count
        dp = len(re.findall('[–—]', xs))
        dh = len(re.findall('[–—]', ys))
        if dp != dh:
            print('DASH', tag, dp, dh)
        # ellipsis vs pe
        pe = len(re.findall(r'…\s*pe\s*…', xs))
        el = ys.count('…')
        if pe != el:
            print('PE', tag, pe, el)
        if '...' in y:
            print('ASCII-ELLIPSIS', tag)
        # Latin outside brackets
        lat = re.findall(r'[A-Za-zāīūṃṇñṭḍḷṅ]{2,}', re.sub(r'\^[\w-]+', '', ys))
        if lat:
            print('LATIN', tag, lat[:5])
        # terminal punct: statements
        body = re.sub(r'\s*\^[\w-]+\s*$', '', y).rstrip()
        bodyp = re.sub(r'\s*\^[\w-]+\s*$', '', x).rstrip()
        if not body.startswith('#'):
            if body.endswith('.') or not re.search(r'[।?…”]$', re.sub(r'\[[^\]]*\]$', '', body)):
                print('END', tag, repr(body[-30:]), repr(bodyp[-20:]))
            if '.' in re.sub(r'\[[^\]]*\]', '', body).replace('(', ''):
                print('DOT', tag, [m for m in re.findall(r'.{10}\..{5}', re.sub(r'\[[^\]]*\]', '', body))][:3])
        # straight quotes
        if '"' in y or "'" in y:
            print('STRAIGHTQ', tag)
        if y.count('“') != y.count('”'):
            print('QBAL', tag, y.count('“'), y.count('”'))
        if len(re.findall('["“]', xs)) != y.count('“'):
            print('QCOUNT', tag, len(re.findall('["“]', xs)), y.count('“'))
        # variant bracket count
        if len(re.findall(r'\[', x)) != len(re.findall(r'\[', y)):
            print('BRACK', tag, x.count('['), y.count('['))
        # variant content
        vp = re.findall(r'\[([^\]]*)\]', x)
        vh = re.findall(r'\[([^\]]*)\]', y)
        for v1, v2 in zip(vp, vh):
            w1 = re.sub(r'\s*\([^)]*\)\s*$', '', v1).strip()
            if w1 not in v2:
                print('VAR', tag, v1, '|', v2)
        # ordinals
        po = sorted(n for k, n in PORD.items() for _ in re.findall(k, xs.lower()))
        ho = sorted(n for k, n in ORD.items() for _ in re.findall(k + r'[ािीेंोाँ]*', ys))
        if po != ho:
            print('ORD', tag, po, ho)
        # double spaces
        if re.search(r'[^\s]  +[^\s]', y) or ' ,' in ys or ' ।' in ys.replace(' ।', ' ।') and re.search(r'\s।', ys):
            print('SPACE', tag, re.findall(r'.{8}(?:\s,|\s।|  ).{5}', y)[:3])
print('segments with ID', segs)
