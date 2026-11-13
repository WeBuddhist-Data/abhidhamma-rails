import re, os
from collections import defaultdict
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['2-01-vitakkattika.md', '2-02-pitittika.md', '2-03-dassanenapahatabbattika.md',
         '2-04-dassanenapahatabbahetukattika.md', '2-05-acayagamittika.md', '2-06-sekkhattika.md',
         '2-07-parittattika.md', '2-08-parittarammanattika.md']
IDRE = re.compile(r'\s*\^([0-9A-Za-z\-]+)\s*$')

def load(path):
    with open(path, encoding='utf-8') as f:
        return [l for l in f.read().split('\n') if l.strip()]

m = defaultdict(lambda: defaultdict(list))
for f in FILES:
    P = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f)); H = load(os.path.join(B, 'hindi', 'pi-7-hindi-plain-rails_split_chapters', f))
    for i, (p, h) in enumerate(zip(P, H), 1):
        ps = IDRE.sub('', p).strip(); hs = IDRE.sub('', h).strip()
        if p.startswith('#') or (len(ps.split()) <= 2 and not ps.startswith('(')):
            key = re.sub(r'^#+\s*', '', ps).strip('*. ')
            val = re.sub(r'^#+\s*', '', hs).strip('*।. ')
            m[key][val].append(f'{f[:4]}:{i}')
for k, v in sorted(m.items()):
    if len(v) > 1:
        print(k)
        for val, locs in v.items():
            print('   ', val, locs[:6], len(locs))
    else:
        val = list(v)[0]
        print(f'{k} => {val}')
