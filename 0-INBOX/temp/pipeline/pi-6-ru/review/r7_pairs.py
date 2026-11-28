import sys, re, collections
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters\\'
R = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-6-russian-plain-rails_split_chapters\\'
ch = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'all'
pl = open(P + ch, encoding='utf-8').read().split('\n')
rl = open(R + ch, encoding='utf-8').read().split('\n')
assert len(pl) == len(rl), (len(pl), len(rl))
pairs = []
cur = None
for i, (a, b) in enumerate(zip(pl, rl)):
    if (a.strip() == '') != (b.strip() == ''):
        print('BLANK MISMATCH', i + 1)
    if not a.strip():
        continue
    ia = re.search(r'\^[\d-]+$', a)
    ib = re.search(r'\^[\d-]+$', b)
    if (ia.group() if ia else None) != (ib.group() if ib else None):
        print('ID MISMATCH', i + 1, a[-20:], b[-20:])
    pairs.append((i + 1, a, b))
if mode == 'all':
    s = int(sys.argv[3]); e = int(sys.argv[4])
    for n, a, b in pairs:
        if s <= n <= e:
            print(n, a); print(n, b); print()
elif mode == 'first':
    s = int(sys.argv[3]); e = int(sys.argv[4])
    seen = set()
    for n, a, b in pairs:
        ka = re.sub(r'\s*\^[\d-]+$', '', a)
        if ka in seen or not (s <= n <= e):
            continue
        seen.add(ka)
        print(n, a); print(n, b); print()
elif mode == 'uniq':
    # unique by exact Pali line (block id stripped), show russian variants
    d = collections.OrderedDict()
    for n, a, b in pairs:
        ka = re.sub(r'\s*\^[\d-]+$', '', a)
        kb = re.sub(r'\s*\^[\d-]+$', '', b)
        d.setdefault(ka, collections.Counter())[kb] += 1
    print('unique pali lines', len(d), 'of', len(pairs))
    for ka, c in d.items():
        if len(c) > 1:
            print('MULTI', ka)
            for kb, k in c.items():
                print('   ', k, kb)
