import re, sys, os, collections
sys.path.insert(0, os.path.dirname(__file__))
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(ROOT, 'pali', 'pi-6_split_chapters')
V = os.path.join(ROOT, 'vietnamese', 'pi-6-vietnamese-plain-rails_split_chapters')
FILES = ['3-06-ayatanayamaka.md', '4-dhatuyamaka.md', '5-01-saccayamaka.md', '5-02-saccayamaka.md',
         '5-03-saccayamaka.md', '6-01-sankharayamaka.md', '6-02-sankharayamaka.md', '7-01-anusayayamaka.md']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

# usage: r2_ctx.py <viet-regex> [pali-regex]  -> counts of matched phrases (Vietnamese side), per file
vre = re.compile(sys.argv[1])
pre = re.compile(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != '-' else None
show = int(sys.argv[3]) if len(sys.argv) > 3 else 0
c = collections.Counter()
shown = 0
for fn in FILES:
    pl = lines(os.path.join(P, fn)); vl = lines(os.path.join(V, fn))
    for i, (a, b) in enumerate(zip(pl, vl)):
        if pre and not pre.search(a):
            continue
        ms = vre.findall(b)
        for m in ms:
            c[m if isinstance(m, str) else ' '.join(m)] += 1
        if ms and shown < show:
            shown += 1
            print('--', fn, 'L%d' % i); print('  P:', a); print('  V:', b)
for k, n in c.most_common(80):
    print(n, k)
