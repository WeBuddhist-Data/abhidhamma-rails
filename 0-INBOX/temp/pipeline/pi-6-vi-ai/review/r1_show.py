import sys
sys.path.insert(0, 'D:/Work/OpenPecha/abhidhamma-rails/0-INBOX/temp/pipeline/pi-6-vi-ai/review')
from r1_check import load, PDIR, VDIR

# usage: r1_show.py file id[:line] id[:line] ...
f = sys.argv[1]
P, _ = load(PDIR + f)
V, _ = load(VDIR + f)
if sys.argv[2:] == ['headings']:
    seen = set()
    for sid in P:
        a, b = P[sid][0], V[sid][0]
        if a.startswith('#'):
            k = (a.split(' ^')[0].lower(), b.split(' ^')[0])
            if k not in seen:
                seen.add(k)
                print('%-12s %s  ||  %s' % (sid, a.split(' ^')[0], b.split(' ^')[0]))
    sys.exit()
for arg in sys.argv[2:]:
    sid, _, ln = arg.partition(':')
    pl, vl = P.get(sid, []), V.get(sid, [])
    idx = [int(ln) - 1] if ln else range(max(len(pl), len(vl)))
    print('##', sid)
    for i in idx:
        print('P%d: %s' % (i + 1, pl[i] if i < len(pl) else ''))
        print('V%d: %s' % (i + 1, vl[i] if i < len(vl) else ''))
