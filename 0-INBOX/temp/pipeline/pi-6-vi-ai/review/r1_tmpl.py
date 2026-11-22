import sys, re
from collections import defaultdict
sys.path.insert(0, 'D:/Work/OpenPecha/abhidhamma-rails/0-INBOX/temp/pipeline/pi-6-vi-ai/review')
from r1_check import load, PDIR, VDIR, FILES, split_sents, IDRE, KH_P, AY_P, KH_V, AY_V

HP = re.compile(r'^(.*?)\s(tesaṃ|tattha|te)\s')
PT = re.compile(KH_P.pattern + '|' + AY_P.pattern, re.I)
VT = re.compile(KH_V.pattern + '|' + AY_V.pattern, re.I)


def templ(s, rx):
    seen = {}
    def rep(m):
        k = m.group(0).lower()
        k = re.sub(r'(ṃ|o|ā|e|a|aṃ|añca|añceva|āni|ānaṃ|ena|assa|ca)+$', '', k) if rx is PT else k
        if k not in seen:
            seen[k] = 'T%d' % (len(seen) + 1)
        return seen[k]
    return rx.sub(rep, s)


SHOWALL = False
ANSONLY = False
args = sys.argv[1:]
if args and args[0] == 'ans':
    ANSONLY = True
    args[0] = 'all'
if args and args[0] == 'all':
    SHOWALL = True
    args = args[1:]
files = args or FILES
groups = defaultdict(lambda: defaultdict(list))
for f in files:
    P, _ = load(PDIR + f)
    V, _ = load(VDIR + f)
    for sid in P:
        for a, b in zip(P[sid], V.get(sid, [])):
            if a.startswith('#'):
                continue
            a = IDRE.sub('', a)
            b = IDRE.sub('', b)
            ps, vs = split_sents(a), split_sents(b)
            if len(ps) != len(vs):
                ps, vs = [a], [b]
            for x, y in zip(ps, vs):
                m = HP.match(x)
                if m and ', thì' in y and not x.lstrip().startswith('('):
                    x = 'H ' + x[m.end(1):]
                    y = 'H' + y[len(y.split(', thì')[0]):]
                x = re.sub(r'^\((Ka|Kha)\) ', r'(\1) ', x)
                tx, ty = templ(x, PT), templ(y, VT)
                groups[tx][ty].append(f.split('-')[0] + ':' + sid)
nmulti = 0
for tx in sorted(groups):
    g = groups[tx]
    if ANSONLY and (tx.startswith('(') or tx.startswith('H ') or tx.startswith('Yassa') or tx.startswith('Yattha')):
        continue
    if SHOWALL and len(g) == 1:
        ty, ids = list(g.items())[0]
        print('P: %s\nV: %s   [%d %s]' % (tx, ty, len(ids), ids[0]))
    if len(g) > 1:
        nmulti += 1
        print('P: ' + tx)
        for ty, ids in sorted(g.items(), key=lambda kv: -len(kv[1])):
            print('   (%d %s) %s' % (len(ids), ','.join(ids[:3]), ty))
print('templates', len(groups), 'multi', nmulti)
