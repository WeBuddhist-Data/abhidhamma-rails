import re, os, sys, collections, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
P = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-1_split_chapters'
H = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters'
FILES = ['2-01-cittuppadakandam.md', '2-02-cittuppadakandam.md', '2-03-cittuppadakandam.md',
         '2-04-cittuppadakandam.md', '2-05-cittuppadakandam.md']
OUT = os.path.dirname(os.path.abspath(__file__))


def lines(d, f):
    return [l.rstrip('\n') for l in open(os.path.join(d, f), encoding='utf-8') if l.strip()]


def strip(s):
    s = re.sub(r'\s*\^[\w-]+\s*$', '', s)
    s = re.sub(r'\s*\[[^\]]*\]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def clauses(s, pal):
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


units = {}  # P -> (H, firstid, n)
order = []
for f in FILES:
    p = lines(P, f)
    h = lines(H, f)
    for i, (x, y) in enumerate(zip(p, h), 1):
        m = re.search(r'\^([\w-]+)\s*$', x)
        tag = f[:4] + ':' + (m.group(1) if m else f'L{i}')
        a = clauses(strip(x), True)
        b = clauses(strip(y), False)
        items = []
        if len(a) != len(b):
            items.append((norm(strip(x)), norm(strip(y))))
        else:
            for (t, d), (u, e) in zip(a, b):
                ca = [norm(c) for c in t.split(',')]
                cb = [norm(c) for c in u.split(',')]
                if len(ca) == len(cb):
                    items += list(zip(ca, cb))
                else:
                    items.append((norm(t), norm(u)))
        for k, v in items:
            if not k and not v:
                continue
            if k not in units:
                units[k] = [v, tag, 1]
                order.append(k)
            else:
                units[k][2] += 1


def toks(s):
    # keep … as own token
    return s.replace('…', ' … ').split()


def delta(a, b, ctx=1):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        l = ' '.join(a[max(0, i1 - ctx):i1])
        r = ' '.join(a[i2:i2 + ctx])
        out.append(f'{l} {{-{" ".join(a[i1:i2])}-}}{{+{" ".join(b[j1:j2])}+}} {r}')
    return ' | '.join(out)


idx = {}
seen = []
inv = collections.defaultdict(set)
res = []
for n, k in enumerate(order):
    v, tag, c = units[k]
    tk = toks(k)
    stk = set(tk)
    best = None
    if len(tk) >= 5:
        score = collections.Counter()
        for t in stk:
            for j in inv[t]:
                score[j] += 1
        cands = [j for j, s in score.most_common(12)]
        bs = 0
        for j in cands:
            r = difflib.SequenceMatcher(None, tk, toks(order[j]), autojunk=False).ratio()
            if r > bs:
                bs, best = r, j
        if bs < 0.55:
            best = None
    if best is None:
        res.append(f'U{n} [{tag} x{c}]\n  P: {k}\n  H: {v}\n')
    else:
        pd = delta(toks(order[best]), tk)
        hd = delta(toks(units[order[best]][0]), toks(v))
        res.append(f'U{n} [{tag} x{c}] ~U{best}\n  P: {pd}\n  H: {hd}\n')
    for t in stk:
        inv[t].add(n)
text = '\n'.join(res)
open(os.path.join(OUT, 'A_delta.txt'), 'w', encoding='utf-8').write(text)
print(len(order), len(text), text.count('\n'))
