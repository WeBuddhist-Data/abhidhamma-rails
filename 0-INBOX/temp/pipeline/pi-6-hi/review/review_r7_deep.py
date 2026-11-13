"""Deeper abstraction: items + verbs (tense/polarity) -> templates; print uniques."""
import re, os, sys
from collections import OrderedDict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r7_abstract import rows

PVERB = re.compile(r'(?<![A-Za-zāīūṃ])(na\s+|n)?(uppajj|nirujjh)[A-Za-zāīūṃṅñṭḍṇḷ]*', re.I)
HVERB = re.compile(r'(उत्पन्न|निरुद्ध)(?! होने)( नहीं)? (होती|होता|होते|हुई|हुआ|होगी|होगा)( है| हैं| थी| था| थे)?')

def deep(ap, ah):
    ap = PVERB.sub(lambda m: '<V>' if not m.group(1) else '<nV>', ap)
    ah = HVERB.sub(lambda m: '<V>' if not m.group(2) else '<nV>', ah)
    for a, b in [('tāsaṃ', 'tesaṃ'), ('upapajjantīnaṃ', 'upapajjantānaṃ')]:
        ap = ap.replace(a, b)
    return ap, ah

if __name__ == '__main__':
    kind = sys.argv[1]
    lo, hi = int(sys.argv[2]), int(sys.argv[3])
    g = OrderedDict()
    for fn, i, pid, pb, hb, ap, ah, ex in rows():
        if pb.startswith('#'):
            continue
        isq = bool(re.match(r'(\(K\w+\) )?(Yassa|Yattha|yassa|yattha|na |<|indriy|Indriy)', ap)) or ap.startswith('(K')
        if (kind == 'q') != isq:
            continue
        dp, dh = deep(ap, ah)
        g.setdefault(dp, {}).setdefault(dh, []).append(f'{fn[3:5]}:{i}')
    print('templates', len(g))
    for n, (k, v) in enumerate(g.items()):
        if lo <= n < hi:
            print(f'#{n} P: {k}')
            for dh, locs in v.items():
                print(f'   [{len(locs)}] {",".join(locs[:3])} H: {dh}')
