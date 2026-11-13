import re, os, sys
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['2-01-vitakkattika.md', '2-02-pitittika.md', '2-03-dassanenapahatabbattika.md',
         '2-04-dassanenapahatabbahetukattika.md', '2-05-acayagamittika.md', '2-06-sekkhattika.md',
         '2-07-parittattika.md', '2-08-parittarammanattika.md']

def load(path):
    with open(path, encoding='utf-8') as f:
        return [l for l in f.read().split('\n') if l.strip()]

# usage: pali_regex hindi_regex  -> prints matched fragments (sentence-level) from both sides
pre, hre = sys.argv[1], sys.argv[2]
for f in FILES:
    P = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f)); H = load(os.path.join(B, 'hindi', 'pi-7-hindi-plain-rails_split_chapters', f))
    for i, (p, h) in enumerate(zip(P, H), 1):
        pm = re.findall(pre, p); hm = re.findall(hre, h) if hre != '-' else []
        if pm:
            print(f'{f[:4]}:{i}')
            for x in pm: print('  P:', x)
            for x in hm: print('  H:', x)
