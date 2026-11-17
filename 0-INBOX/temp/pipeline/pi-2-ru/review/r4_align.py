import re, sys, os
BASE = r'D:\Work\OpenPecha\abhidhamma-rails'
P = os.path.join(BASE, r'AI_translation\pali\pi-2_split_chapters')
R = os.path.join(BASE, r'AI_translation\russian\pi-2-russian-plain-rails_split_chapters')
OUT = os.path.join(BASE, r'0-INBOX\temp\pipeline\pi-2-ru\review')
FILES = ['13-appamannavibhango.md', '14-sikkhapadavibhango.md', '15-patisambhidavibhango.md', '16-nanavibhango.md']
IDRE = re.compile(r'\^[0-9a-z-]+\s*$')

def lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().split('\n')

total = 0
for fn in FILES:
    pl = lines(os.path.join(P, fn)); rl = lines(os.path.join(R, fn))
    out = []
    issues = []
    if len(pl) != len(rl):
        issues.append(f'LINECOUNT {len(pl)} vs {len(rl)}')
    for i, (a, b) in enumerate(zip(pl, rl), 1):
        if not a.strip() and not b.strip():
            continue
        ida = IDRE.search(a); idb = IDRE.search(b)
        if ida: total += 1
        if (ida.group(0).strip() if ida else None) != (idb.group(0).strip() if idb else None):
            issues.append(f'{i}: ID mismatch {ida} {idb}')
        if bool(a.strip()) != bool(b.strip()):
            issues.append(f'{i}: blank mismatch')
        da = a.count('–') + a.count('—'); db = b.count('–') + b.count('—')
        if da != db:
            issues.append(f'{i}: dash {da} vs {db}')
        if '—' in b:
            issues.append(f'{i}: em dash in RU')
        qa = a.count('?'); qb = b.count('?')
        if qa != qb:
            issues.append(f'{i}: ? {qa} vs {qb}')
        if re.search(r'\bли\b', b):
            issues.append(f'{i}: ли')
        # digits
        na = re.findall(r'\d+', IDRE.sub('', a)); nb = re.findall(r'\d+', IDRE.sub('', b))
        if na != nb:
            issues.append(f'{i}: digits {na} vs {nb}')
        # latin outside brackets
        bb = re.sub(r'\[[^\]]*\]', '', IDRE.sub('', b))
        lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', bb)
        if lat:
            issues.append(f'{i}: latin {lat}')
        # ellipsis
        ea = a.count('…pe…') + a.count('…pa…'); eb = b.count('…')
        if ea and eb < ea:
            issues.append(f'{i}: pe {ea} vs … {eb}')
        out.append(f'[{i}] P: {a}\n[{i}] R: {b}\n')
    for i in range(len(rl) - 2):
        if rl[i] == '' and rl[i + 1] == '' :
            issues.append(f'{i+1}: double blank RU')
    with open(os.path.join(OUT, 'r4_out_' + fn[:2] + '.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print(fn, 'issues:', len(issues))
    for x in issues:
        print('  ', x)
print('segments', total)
