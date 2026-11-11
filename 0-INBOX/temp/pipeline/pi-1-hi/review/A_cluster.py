import re, os, sys, collections, json
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-1_split_chapters'
H = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters'
FILES = ['2-01-cittuppadakandam.md', '2-02-cittuppadakandam.md', '2-03-cittuppadakandam.md',
         '2-04-cittuppadakandam.md', '2-05-cittuppadakandam.md']
OUT = os.path.dirname(os.path.abspath(__file__))


def lines(d, f):
    return [l.rstrip('\n') for l in open(os.path.join(d, f), encoding='utf-8') if l.strip()]


def strip(s):
    s = re.sub(r'\s*\^[\w-]+\s*$', '', s)
    s = re.sub(r'\[[^\]]*\]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def clauses(s, pal):
    # split on sentence-level punctuation, keeping the delimiter type
    pat = r'\s*(\?|;|–|—|।)\s*' if not pal else r'\s*(\?|;|–|—|\.(?=\s|$))\s*'
    parts = re.split(pat, s)
    out = []
    for i in range(0, len(parts), 2):
        t = parts[i].strip()
        d = parts[i + 1] if i + 1 < len(parts) else ''
        if t or d:
            out.append((t, d))
    return out


def norm(t):
    return re.sub(r'\s+', ' ', t.strip(' ,'))


pairs = collections.defaultdict(lambda: collections.defaultdict(list))
mism = []
seglist = []
for f in FILES:
    p = lines(P, f)
    h = lines(H, f)
    cur = None
    for i, (x, y) in enumerate(zip(p, h), 1):
        m = re.search(r'\^([\w-]+)\s*$', x)
        m2 = re.search(r'\^([\w-]+)\s*$', y)
        idp = m.group(1) if m else None
        idh = m2.group(1) if m2 else None
        if idp != idh:
            mism.append((f, i, 'ID', idp, idh))
        tag = idp or f'L{i}'
        a = clauses(strip(x), True)
        b = clauses(strip(y), False)
        if len(a) != len(b):
            mism.append((f, i, 'CLAUSECOUNT', tag, len(a), len(b), x[:2000], y[:3000]))
            pairs[norm(strip(x))][norm(strip(y))].append(f[:4] + ':' + tag)
            continue
        for (t, d), (u, e) in zip(a, b):
            ca = [norm(c) for c in t.split(',')]
            cb = [norm(c) for c in u.split(',')]
            if len(ca) == len(cb):
                for c1, c2 in zip(ca, cb):
                    pairs[c1][c2].append(f[:4] + ':' + tag)
            else:
                pairs[norm(t)][norm(u)].append(f[:4] + ':' + tag)

with open(os.path.join(OUT, 'A_pairs.txt'), 'w', encoding='utf-8') as o:
    for k in sorted(pairs, key=lambda k: min(pairs[k][v][0] for v in pairs[k])):
        vs = pairs[k]
        n = sum(len(v) for v in vs.values())
        o.write(f'P[{n}] {k}\n')
        for v, ids in sorted(vs.items(), key=lambda kv: -len(kv[1])):
            o.write(f'   H[{len(ids)}] {v}  <{ids[0]}>\n')
with open(os.path.join(OUT, 'A_variants.txt'), 'w', encoding='utf-8') as o:
    for k in sorted(pairs, key=lambda k: min(pairs[k][v][0] for v in pairs[k])):
        vs = pairs[k]
        if len(vs) > 1:
            o.write(f'P {k}\n')
            for v, ids in sorted(vs.items(), key=lambda kv: -len(kv[1])):
                o.write(f'   H[{len(ids)}] {v}  <{",".join(ids[:6])}>\n')
with open(os.path.join(OUT, 'A_mism.txt'), 'w', encoding='utf-8') as o:
    for m in mism:
        o.write(repr(m) + '\n')
print(len(pairs), 'distinct P units;', sum(1 for k in pairs if len(pairs[k]) > 1), 'with variants;', len(mism), 'mismatches')
print('pairs size', os.path.getsize(os.path.join(OUT, 'A_pairs.txt')))
print('variants size', os.path.getsize(os.path.join(OUT, 'A_variants.txt')))
print('mism size', os.path.getsize(os.path.join(OUT, 'A_mism.txt')))
