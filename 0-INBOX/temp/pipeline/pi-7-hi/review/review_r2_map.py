import sys, re
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = {'1-02': '1-02-vedanattika.md', '1-03': '1-03-vipakattika.md', '1-04': '1-04-upadinnattika.md',
         '1-05': '1-05-sankilitthattika.md'}
ID_RE = re.compile(r'\s\^([\w-]+)\s*$')
# usage: review_r2_map.py 1-04 594 599 ...   (physical line numbers) -> nonempty L and segment ID
key = sys.argv[1]
lines = open(ROOT + '\\hindi\\pi-7-hindi-plain-rails_split_chapters\\' + FILES[key], encoding='utf8').read().split('\n')
ne = {}
k = 0
for i, l in enumerate(lines, 1):
    if l.strip():
        k += 1
        ne[i] = k
for a in sys.argv[2:]:
    i = int(a)
    seg = None
    for j in range(i, len(lines) + 1):
        m = ID_RE.search(lines[j - 1])
        if m:
            seg = m.group(1); break
    print('%s phys %d -> L%d seg %s' % (key, i, ne.get(i, -1), seg))
