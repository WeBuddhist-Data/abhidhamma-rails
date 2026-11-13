import os, re, sys
from collections import OrderedDict
sys.path.insert(0, os.path.dirname(__file__))
from review_r9_common import *
from review_r9_resid import resid
from review_r9_check import CONDS

WL = set(s for s, l, h in CONDS) | {'–', 'ārammaṇādhipati', 'sahajātādhipati', 'ārammaṇūpanissayo', 'anantarūpanissayo',
                                     'pakatūpanissayo', 'pe', 'Pe', '(', ')', 'Vipāka', 'Āsevana', 'Sahajāta'}
EX = [('ārammaṇādhipati', 'विषय रूपी प्रधानता'), ('sahajātādhipati', 'सह-उत्पत्ति रूपी प्रधानता'),
      ('ārammaṇūpanissayo', 'विषय रूपी प्रबल आश्रय'), ('anantarūpanissayo', 'निकटता रूपी प्रबल आश्रय'),
      ('pakatūpanissayo', 'स्वाभाविक प्रबल आश्रय')]
seen = OrderedDict()
exbad = []
for f, sid, ne, p, h, pid, hid in pairs():
    if p.strip().startswith('#'):
        continue
    # example-token sequence check for dash parts
    pseq = [x for m in re.finditer('|'.join(e for e, _ in EX), p) for x in [m.group(0)]]
    hseq = []
    for m in re.finditer('|'.join(hh for _, hh in EX), h):
        hseq.append([e for e, hh in EX if hh == m.group(0)][0])
    if pseq != hseq:
        exbad.append((f[:4], ne, pseq, hseq, p, h))
    r = resid(p)
    if not r:
        continue
    toks = set(re.findall(r'\S+', r.replace('(', ' ( ').replace(')', ' ) ')))
    if toks <= WL:
        continue
    seen.setdefault(r, []).append((f[:4], ne, p.strip(), h.strip()))
print('EXAMPLE-TOKEN MISMATCHES', len(exbad))
for x in exbad:
    print(x[:4]); print('  P:', x[4]); print('  H:', x[5])
print('unique prose residuals', len(seen))
for r, lst in seen.items():
    f, ne, p, h = lst[0]
    hs = set(x[3] for x in lst)
    print('== %s:%s x%d' % (f, ne, len(lst)))
    print('P:', p)
    print('H:', h)
