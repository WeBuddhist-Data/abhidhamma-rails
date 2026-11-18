import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r4_lib import *
from collections import defaultdict, OrderedDict

# usage: r4_tmpl.py incons            -> list Pali templates with >1 Vietnamese template
#        r4_tmpl.py uniq <file> a b   -> print segments a..b, skipping lines whose template was already shown
PSTEMS = ['āsav', 'saṃyojan', 'ganth', 'ogh', 'yog', 'nīvaraṇ', 'upādān', 'kiles', 'parāmās', 'parāmaṭṭh']
VTERMS = ['ô nhiễm', 'xiềng xích', 'nút thắt', 'dòng lũ', 'ách', 'chướng ngại', 'sự bám víu', 'phiền não', 'sự hiểu sai lệch']


def ptmpl(s):
    s = strip_id(s)
    for st in PSTEMS:
        s = re.sub(r'(?<![\wāīūṃṅñṭḍṇḷ])(a|an|s|saṃ)?' + st, lambda m: (m.group(1) or '') + ('Y' if st == 'parāmaṭṭh' else 'X'), s)
    return s


def vtmpl(s):
    s = strip_id(s)
    for t in VTERMS:
        s = re.sub(r'(?<!\w)' + t + r'(?!\w)', 'X', s)
    return s


def load():
    rows = []
    for f in FILES:
        P = segs(os.path.join(PI, f)); V = segs(os.path.join(VI, f))
        for (pid, pl), (vid, vl) in zip(P, V):
            for k, (p, v) in enumerate(zip(pl, vl)):
                rows.append((f, pid, k, p, v, ptmpl(p), vtmpl(v)))
    return rows


rows = load()
mode = sys.argv[1]
if mode == 'incons':
    g = defaultdict(lambda: defaultdict(list))
    for f, pid, k, p, v, pt, vt in rows:
        g[pt][vt].append(pid)
    n = 0
    for pt, vs in g.items():
        if len(vs) > 1:
            n += 1
            print('#### P:', pt[:300])
            for vt, ids in vs.items():
                print('   ', ids[:8], len(ids), 'V:', vt[:400])
    print('inconsistent groups:', n, 'of', len(g))
elif mode == 'uniq':
    f, a, b = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    seen = {}
    for ff, pid, k, p, v, pt, vt in rows:
        key = pt
        if ff == f:
            P = [x[0] for x in segs(os.path.join(PI, f))]
            break
    order = [x[0] for x in segs(os.path.join(PI, f))]
    idx = {sid: i for i, sid in enumerate(order)}
    for ff, pid, k, p, v, pt, vt in rows:
        i = idx.get(pid) if ff == f else None
        if ff == f and a <= i < b:
            if pt in seen:
                same = seen[pt][1] == vt
                print(f'=== [{i}] {pid}.{k} DUP of {seen[pt][0]} ' + ('(VI same)' if same else '(VI DIFFERS)'))
                if not same:
                    print('P:', strip_id(p)); print('V:', strip_id(v))
            else:
                print(f'=== [{i}] {pid}.{k}')
                print('P:', strip_id(p)); print('V:', strip_id(v))
        if pt not in seen:
            seen[pt] = (pid, vt)
