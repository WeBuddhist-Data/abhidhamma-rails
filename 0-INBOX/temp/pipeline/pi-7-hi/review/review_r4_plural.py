import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *

for f in FILES:
    P = nonempty(load(os.path.join(PA, f)))
    H = nonempty(load(os.path.join(HI, f)))
    for n, ((_, p), (_, h)) in enumerate(zip(P, H), 1):
        if p.startswith('#'):
            continue
        ph = re.split(r' – |\. |\(', p)[0]
        hh = re.split(r' – |। |\(', h)[0]
        if 'uppajj' in ph:
            pp = 'uppajjanti' in ph
            hp = 'होती हैं' in hh or 'परिघटनाएँ' in hh
            hs = 'होती है' in hh and 'होती हैं' not in hh
            if pp != ('होती हैं' in hh) or pp != ('परिघटनाएँ' in hh):
                print(f[:4], n, 'UPP', pp, '|', hh[-80:])
        elif re.search(r'dhamm[oā] .*dhammassa', ph) or re.search(r'dhamm[oā] \w+ssa', ph):
            subj_pl = bool(re.match(r'^\S.*? dhammā ', ph))
            h_pl = 'परिघटनाएँ' in hh.split(',')[0] or 'होती हैं' in hh
            if subj_pl != ('परिघटनाएँ' in hh) or subj_pl != ('होती हैं' in hh):
                print(f[:4], n, 'PAN', subj_pl, '|', hh[-90:])
