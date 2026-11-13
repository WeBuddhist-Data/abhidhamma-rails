import sys, re
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = {'1-02': '1-02-vedanattika.md', '1-03': '1-03-vipakattika.md', '1-04': '1-04-upadinnattika.md',
         '1-05': '1-05-sankilitthattika.md'}
# usage: review_r2_prose.py 1-04 250 431  -> lines in range whose Pāli has example prose (after ' – '),
# printing the Pāli example part and the Hindi example part only (head formula is script-checked)
key, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
ne = lambda path: [l for l in open(path, encoding='utf8').read().split('\n') if l.strip()]
p = ne(ROOT + '\\pali\\pi-7_split_chapters\\' + FILES[key])
h = ne(ROOT + '\\hindi\\pi-7-hindi-plain-rails_split_chapters\\' + FILES[key])
for n in range(a, b + 1):
    ps, hs = p[n - 1], h[n - 1]
    if ps.startswith('#'):
        continue
    if ' – ' not in ps and len(ps) < 200:
        continue
    pe = ps.split(' – ', 1)[1] if ' – ' in ps else ps
    he = hs.split(' – ', 1)[1] if ' – ' in hs else hs
    print('--- L%d' % n)
    print('P:', pe)
    print('H:', he)
