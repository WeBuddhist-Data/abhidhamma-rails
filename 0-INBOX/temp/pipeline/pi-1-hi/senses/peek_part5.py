"""Part-5 helper: short context windows. Usage: peek_part5.py agg-part5.tsv hw1 hw2 ...
For each headword: first id of each value; prints ~90 chars of Pāli around the headword and of Hindi around the value."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
PDIR = os.path.join(ROOT, r'AI_translation\pali\pi-1_split_chapters')
HDIR = os.path.join(ROOT, r'AI_translation\hindi\pi-1-hindi-plain-zeroshot_split_chapters')
idre = re.compile(r'\^([0-9A-Za-z-]+)\s*$')
seg = {}
for name in sorted(os.listdir(PDIR)):
    if not name.endswith('.md'):
        continue
    P = [l for l in open(os.path.join(PDIR, name), encoding='utf-8-sig').read().splitlines() if l.strip()]
    H = [l for l in open(os.path.join(HDIR, name), encoding='utf-8-sig').read().splitlines() if l.strip()]
    bp, bh = [], []
    for a, b in zip(P, H):
        bp.append(a); bh.append(b)
        m = idre.search(a)
        if m:
            seg[m.group(1)] = (' '.join(bp), ' '.join(bh)); bp, bh = [], []
rows = {}
for line in open(sys.argv[1], encoding='utf-8-sig'):
    c = line.rstrip('\n').split('\t')
    if len(c) == 4:
        rows[c[0]] = c[2]
def win(t, k, w=90):
    i = t.lower().find(k.lower())
    if i < 0:
        return '(not found) ' + t[:w]
    return t[max(0, i - w):i + len(k) + w]
for hw in sys.argv[2:]:
    if hw.startswith('@'):
        sid, pk, hk = hw[1:].split(':')
        p, h = seg[sid]
        print(sid, 'P:', win(p, pk, 120))
        print('   H:', win(h, hk, 120))
        continue
    print('=====', hw)
    for item in rows[hw].split(' | '):
        m = re.match(r'^(.*)=(\d+)\[([^\]]*)\]$', item)
        v, ids = m.group(1), m.group(3).replace('…', '').split(',')
        sid = ids[0]
        p, h = seg.get(sid, ('?', '?'))
        print(f'  [{v}] {sid}')
        print('   P:', win(p, hw.split()[0]))
        print('   H:', win(h, v.split(' … ')[0]))
