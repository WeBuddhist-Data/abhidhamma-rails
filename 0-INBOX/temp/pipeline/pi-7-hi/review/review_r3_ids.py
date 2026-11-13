import re, os, sys
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
IDRE = re.compile(r'\^([0-9A-Za-z\-]+)\s*$')

def load(path):
    with open(path, encoding='utf-8') as f:
        return [l for l in f.read().split('\n') if l.strip()]
# args: file line,line,...
f = sys.argv[1]
P = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f))
for x in sys.argv[2].split(','):
    i = int(x)
    for j in range(i - 1, len(P)):
        m = IDRE.search(P[j])
        if m:
            print(f'{f[:4]}:{i} -> ^{m.group(1)} (line {j+1})'); break
