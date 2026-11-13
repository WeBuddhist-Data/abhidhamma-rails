import re, os
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['2-01-vitakkattika.md', '2-02-pitittika.md', '2-03-dassanenapahatabbattika.md',
         '2-04-dassanenapahatabbahetukattika.md', '2-05-acayagamittika.md', '2-06-sekkhattika.md',
         '2-07-parittattika.md', '2-08-parittarammanattika.md']
IDRE = re.compile(r'\s*\^([0-9A-Za-z\-]+)\s*$')

def load(path):
    with open(path, encoding='utf-8') as f:
        return [l for l in f.read().split('\n') if l.strip()]

CHK = [('double-ellipsis', r'……'), ('space-before-danda', r' ।'), ('ascii-period', r'(?<![0-9])\.(?![0-9])'),
       ('comma-danda', r',।|।,'), ('double-danda', r'।\s*।'), ('straight-quote', r'["\']'), ('double-space', r'  '),
       ('space-before-comma', r' ,'), ('ellipsis-space-ellipsis', r'… …'), ('hyphen-dash', r' - '),
       ('danda-before-paren-close', r'।\)'), ('q-danda', r'\?।|।\?')]
for f in FILES:
    P = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f)); H = load(os.path.join(B, 'hindi', 'pi-7-hindi-plain-rails_split_chapters', f))
    for i, (p, h) in enumerate(zip(P, H), 1):
        hs = IDRE.sub('', h); ps = IDRE.sub('', p)
        hs2 = re.sub(r'\[[^\]]*\]', '', hs)
        for name, pat in CHK:
            if re.search(pat, hs2):
                # skip if pali has analogous
                pal = {'double-ellipsis': '……' in ps or '… …pe' in ps or ' …pe…' in ps, 'danda-before-paren-close': bool(re.search(r'\.\)', ps)),
                       'ascii-period': False, 'double-space': '  ' in ps, 'ellipsis-space-ellipsis': '… …' in ps}.get(name, False)
                m = re.search(pat, hs2)
                print(f'{f[:4]}:{i} {name}{" (pali has)" if pal else ""} ...{hs2[max(0,m.start()-30):m.end()+20]}')
        # space before ellipsis where pali has none
        a = len(re.findall(r' …', ps)); b = len(re.findall(r' …', hs))
        if a != b:
            print(f'{f[:4]}:{i} space-before-ellipsis p={a} h={b}')
        a = len(re.findall(r'…(?=[^\s.,;)!?\-–…])', re.sub(r'…pe…', '…', ps))); b = len(re.findall(r'…(?=[^\s,;।)?\-–…])', hs))
        if a != b:
            print(f'{f[:4]}:{i} no-space-after-ellipsis p={a} h={b}')
