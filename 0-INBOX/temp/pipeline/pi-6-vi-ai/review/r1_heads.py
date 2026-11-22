import sys, re
from collections import defaultdict
sys.path.insert(0, 'D:/Work/OpenPecha/abhidhamma-rails/0-INBOX/temp/pipeline/pi-6-vi-ai/review')
from r1_check import load, PDIR, VDIR, FILES, split_sents, IDRE

HP = re.compile(r'^(.*?)\s(tesaṃ|tattha|te)\s')
files = sys.argv[1:] or FILES
pairs = defaultdict(list)
nohead = []
for f in files:
    P, _ = load(PDIR + f)
    V, _ = load(VDIR + f)
    for sid in P:
        for a, b in zip(P[sid], V.get(sid, [])):
            if a.lstrip().startswith('(') and '?' in a:
                # question line; may still carry answer after '?'
                a = a.split('?', 1)[1]
                b = b.split('?', 1)[1] if '?' in b else ''
            ps, vs = split_sents(IDRE.sub('', a)), split_sents(IDRE.sub('', b))
            if len(ps) != len(vs):
                continue
            for x, y in zip(ps, vs):
                m = HP.match(x)
                if not m:
                    continue
                hp = m.group(1).strip()
                if ', thì' in y:
                    hv = y.split(', thì')[0].strip()
                else:
                    hv = '<<' + y[:70] + '>>'
                pairs[(hp, hv)].append(sid)
byp = defaultdict(list)
for (hp, hv), ids in pairs.items():
    byp[hp].append((hv, ids))
for hp in sorted(byp):
    vs = byp[hp]
    flag = '  !!MULTI' if len(vs) > 1 else ''
    print('P: %s%s' % (hp, flag))
    for hv, ids in vs:
        print('   V(%d, %s): %s' % (len(ids), ids[0], hv))
