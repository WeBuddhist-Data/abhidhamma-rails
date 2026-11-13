import os, re, sys
from collections import OrderedDict
sys.path.insert(0, os.path.dirname(__file__))
from review_r9_common import *
from review_r9_check import PNUM, P2C

W = r'[A-Za-zāīūṃṅñṭḍṇḷĀ]'
NUMS = '|'.join(sorted(PNUM, key=len, reverse=True))
CONDW = '|'.join(sorted(P2C, key=len, reverse=True))
F1 = re.compile(r'(?:^|(?<=[.?…] )|(?<=\. ))[A-ZĀ][^.?–(]*? (?:dhammaṃ )?paṭicca(?:…pe…)?\s[^.?–(]*? uppajja(?:ti|nti)')
F2 = re.compile(r'(?:^|(?<=[.?…] ))[A-ZĀ][^.?–(]*? dhammassa (?=\S+paccayena)')
PAR = re.compile(r'\((?:\d+|[Ss]aṃkhittaṃ\.?|saṃkhittaṃ, [a-zāṃ ]+|anulomaṃ|paccanīyaṃ|anulomapaccanīyaṃ|paccanīyānulomaṃ|anuloma paccanīyaṃ)\)')
COND = re.compile(r'(?<!%s)(?:no|na)?(?:%s)(?!%s)' % (W, CONDW, W), re.I)
NUM = re.compile(r'(?<!%s)(?:%s)(?!%s)' % (W, NUMS, W), re.I)


def resid(p):
    s = re.sub(r'dhammadhamm', 'dhamma dhamm', p)
    s = F1.sub(' ', s)
    s = F2.sub(' ', s)
    s = PAR.sub(' ', s)
    s = re.sub(r'paccayena paccayo', ' ', s)
    s = COND.sub(' ', s)
    s = NUM.sub(' ', s)
    s = s.replace('…pe…', ' ').replace('…', ' ')
    s = re.sub(r'[.,;?\s]+', ' ', s).strip()
    return s


if __name__ == '__main__':
    seen = OrderedDict()
    for f, sid, ne, p, h, pid, hid in pairs():
        if p.strip().startswith('#'):
            continue
        r = resid(p)
        if not r:
            continue
        seen.setdefault(r, []).append((f[:4], ne, p.strip(), h.strip()))
    print('unique residuals', len(seen))
    for r, lst in seen.items():
        f, ne, p, h = lst[0]
        print('== %s:%s x%d  RESID: %s' % (f, ne, len(lst), r))
        print('P:', p)
        print('H:', h)
