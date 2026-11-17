import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review')
from r1_align import load
for ch in sys.argv[1:]:
    p, r, pt, rt = load(ch)
    for (pid, pl), (rid, rl) in zip(p, r):
        for a, b in zip(pl, rl):
            ps = [s for s in re.split(r'(?<=[.;?])\s+', a) if s.strip()]
            rs = [s for s in re.split(r'(?<=[.;?])\s+', b) if s.strip()]
            if len(ps) != len(rs):
                if a.count('siyā') != b.count('иногда'):
                    print('LINE', pid, a.count('siyā'), b.count('иногда'))
                continue
            for x, y in zip(ps, rs):
                sx = x.count('siyā'); sy = y.count('иногда')
                vx = x.count('vattabb'); vy = y.count('нельзя определить')
                nx = len(re.findall(r'\b(na|no|neva)\b', x))
                if sx != sy or vx != vy:
                    print('SENT', pid, sx, sy, vx, vy, '|', x[:90], '|', y[:90])
    print(ch, 'done')
