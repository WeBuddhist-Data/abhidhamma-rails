import os, re, sys
from collections import defaultdict, OrderedDict
sys.path.insert(0, os.path.dirname(__file__))
from review_r9_common import *
from review_r9_slots import PR1, PR2, split_sent  # noqa (re-runs harvest silently is fine)

COUNT = re.compile(r'^(?:\(?[A-ZĀ]?[a-zāīūṃṅñṭḍṇḷ]*?(?:yā|e|paccayā)\s+(?:[a-zāīūṃṅñṭḍṇḷ]+)(?:,|\s|\(|…|$))')
mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
seen = OrderedDict()
for f, sid, ne, p, h, pid, hid in pairs():
    ps = p.strip()
    key = None
    if ps.startswith('#'):
        kind = 'HEAD'
    elif ps.startswith('('):
        kind = 'NOTE'
    else:
        sents = split_sent(re.sub(r'dhammadhamm', 'dhamma dhamm', ps), 'p')
        if all(PR1.match(s) or PR2.match(s) for s in sents) and '–' not in ps and '(' not in ps:
            continue
        # count lines: contain count words only
        if re.match(r'^[A-ZĀ][a-zāīūṃṅñṭḍṇḷ]+(yā|e) ', ps) or re.match(r'^(Na|No)?[A-ZĀa-zāīūṃṅñṭḍṇḷ]+paccayā [a-zāīūṃṅñṭḍṇḷ]+(yā|e) ', ps):
            if '(' not in ps.replace('(saṃkhittaṃ)', '').replace('(Saṃkhittaṃ.)', '') and '–' not in ps:
                continue
        kind = 'PROSE'
    if mode != 'all' and kind != mode:
        continue
    k = (kind, re.sub(r'\s+', ' ', ps))
    seen.setdefault(k, []).append((f[:4], ne, h.strip()))
print('unique', len(seen))
for (kind, pk), lst in seen.items():
    hs = sorted(set(x[2] for x in lst))
    print('==', kind, lst[0][0], lst[0][1], 'x%d' % len(lst), '' if len(hs) == 1 else '  !!HINDI VARIES %d' % len(hs))
    print('P:', pk)
    for hh in hs:
        print('H:', hh)
