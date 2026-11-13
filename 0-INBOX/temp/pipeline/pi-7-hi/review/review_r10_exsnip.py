import os, sys, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs
from review_r10_examples import PAIRS
# show for each key the ids and short Pali/Hindi snippet of first mismatches
lines = open(os.path.join(os.path.dirname(__file__), 'review_r10_examples_out.txt'), encoding='utf-8').read().split('\n')
want = sys.argv[1].split(',')
per = int(sys.argv[2]) if len(sys.argv) > 2 else 2
data = {}
for f, pl, hl in pairs():
    data[f[:4]] = (pl, hl)
out = os.path.join(os.path.dirname(__file__), 'review_r10_exsnip_out.txt')
with open(out, 'w', encoding='utf-8') as o:
    for k in want:
        hits = [l for l in lines if re.search(r'(^|\s)' + re.escape(k) + ':', l)]
        o.write(f'##### {k} {len(hits)} ids: ' + ' '.join(l.split(']')[0][1:] for l in hits[:60]) + '\n')
        for l in hits[:per]:
            fid, ln = l[1:].split(']')[0].split(':')
            pl, hl = data[fid]
            a, b = pl[int(ln)-1], hl[int(ln)-1]
            o.write(f'[{fid}:{ln}] {l.split("] ")[1]}\n P: {a[:600]}\n H: {b[:900]}\n')
print(out)
