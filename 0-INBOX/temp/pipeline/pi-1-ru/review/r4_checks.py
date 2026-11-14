import re, os
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(base, 'pali', 'pi-1_split_chapters')
R = os.path.join(base, 'russian', 'pi-1-russian-plain-rails_split_chapters')
files = ['4-01-nikkhepakandam.md', '4-02-nikkhepakandam.md', '4-03-nikkhepakandam.md', '5-atthakathakandam.md']

def nonempty(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

def bid(l):
    m = re.search(r'\^([\w-]+)\s*$', l)
    return m.group(1) if m else '?'

def strip_var(l):
    return re.sub(r'\[[^\]]*\]', '', l)

for fn in files:
    pn = nonempty(os.path.join(P, fn)); rn = nonempty(os.path.join(R, fn))
    for a, b in zip(pn, rn):
        i = bid(a)
        pa, rb = strip_var(a), strip_var(b)
        dp = pa.count('–') + pa.count('—'); dr = rb.count('–') + rb.count('—')
        if dp != dr:
            print(f'{fn} {i} DASH pali={dp} ru={dr}')
        if re.search(r'\bли\b', b):
            print(f'{fn} {i} LI')
        if re.search(r'[A-Za-zāīūṃṅñṭḍṇḷ]{3,}', rb.replace('^' + i, '')):
            print(f'{fn} {i} LATIN: ' + ', '.join(re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{3,}', rb))[:120])
        if '"' in b or '“' in b and '„' not in b:
            print(f'{fn} {i} QUOTES')
        # question count
        if a.count('?') != b.count('?'):
            print(f'{fn} {i} QMARK pali={a.count("?")} ru={b.count("?")}')
        body = re.sub(r'\s*\^[\w-]+\s*$', '', b)
        if not body.startswith('#') and body and body[-1] not in '.?!»…:':
            print(f'{fn} {i} END "{body[-5:]}"')
        pe = a.count('…pe…') + a.count('...pe...')
        el = b.count('…')
        if el < pe:
            print(f'{fn} {i} PE pali={pe} ru_ellipsis={el}')
        dig_p = re.findall(r'\d+', re.sub(r'\^[\w-]+', '', a)); dig_r = re.findall(r'\d+', re.sub(r'\^[\w-]+', '', b))
        if dig_p != dig_r:
            print(f'{fn} {i} DIGITS {dig_p} {dig_r}')
        if '  ' in body:
            print(f'{fn} {i} DOUBLESPACE')
        if re.search(r' ,|,,|\.\.(?!\.)| \.', body):
            print(f'{fn} {i} PUNCT')
