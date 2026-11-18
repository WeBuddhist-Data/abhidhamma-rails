import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r4_lib import *
from collections import Counter

def norm_pi(s):
    s = re.sub(r'\[.*?\]', '', s)
    s = s.replace('…pe…', ' ')
    toks = [t for t in re.findall(r'\w+', s.lower()) if t != 'dhammā']
    return ' '.join(toks)

def norm_vi(s):
    s = re.sub(r'\s*\[.*?\]', '', s).strip().rstrip('.?').strip()
    return s

# build matrix map
mp = {}
P = segs(os.path.join(PI, '1-matika.md')); V = segs(os.path.join(VI, '1-matika.md'))
for (pid, pl), (vid, vl) in zip(P, V):
    for p, v in zip(pl, vl):
        p, v = strip_id(p), strip_id(v)
        mp_ = re.match(r'\((\w+)\)\s*(.*)$', p)
        mv = re.match(r'\((\w)\)\s*(.*)$', v)
        if not mp_ or not mv:
            continue
        key = norm_pi(mp_.group(2))
        vv = norm_vi(mv.group(2))
        if vv.startswith('Các hiện tượng '):
            vv = vv[len('Các hiện tượng '):]
        else:
            vv = '##' + vv
        if key in mp and mp[key] != vv:
            print('MATIKA-DUP', key, mp[key], '|', vv)
        mp[key] = vv

print('matrix items:', len(mp))
stats = Counter()
seen_q = {}
for f in FILES:
    P = segs(os.path.join(PI, f)); V = segs(os.path.join(VI, f))
    for (pid, pl), (vid, vl) in zip(P, V):
        for p, v in zip(pl, vl):
            p, v = strip_id(p), strip_id(v)
            pq = re.findall(r'Katame dhammā ([^?]*?)(?:\?|…pe…)', p)
            vq = re.findall(r'Những hiện tượng nào ([^?…]*)', v)
            if len(pq) != len(vq):
                print(pid, 'QPAIR-COUNT', pq, vq)
            for a, b in zip(pq, vq):
                k = norm_pi(a)
                b = norm_vi(b)
                if k not in mp:
                    stats['q-notinmatrix'] += 1
                    print(pid, 'Q-NOT-IN-MATRIX', a, '|', b)
                    continue
                exp = mp[k]
                if b == exp:
                    stats['q-exact'] += 1
                elif b == 'là ' + exp:
                    stats['q-la'] += 1
                    print(pid, 'Q-LA', exp)
                else:
                    stats['q-MISMATCH'] += 1
                    print(pid, 'Q-MISMATCH', a, '| got:', b, '| matika:', exp)
            pc = re.findall(r'ime dhammā ([^.?]*?)[.?]', p)
            vc = re.findall(r'những hiện tượng này ([^.?]*?)[.?]', v)
            if len(pc) != len(vc):
                print(pid, 'CPAIR-COUNT', pc, vc)
            for a, b in zip(pc, vc):
                k = norm_pi(a)
                b = norm_vi(b)
                if k not in mp:
                    stats['c-notinmatrix'] += 1
                    print(pid, 'C-NOT-IN-MATRIX', a, '|', b)
                    continue
                exp = mp[k]
                if b == exp:
                    stats['c-exact'] += 1
                elif b == 'là ' + exp:
                    stats['c-la'] += 1
                else:
                    stats['c-MISMATCH'] += 1
                    print(pid, 'C-MISMATCH', a, '| got:', b, '| matika:', exp)
print(stats)
