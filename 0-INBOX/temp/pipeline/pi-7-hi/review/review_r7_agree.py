import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *

praw, pl = load(P)
hraw, hl = load(H)
S = segs(pl)

def head(t):
    t = IDRE.sub('', t)
    return re.split(r' – |…|\(|\. |\.$|।|;', t)[0]

for ((n, i, p), sid), (_, _, h) in zip(S, hl):
    if p.startswith('#'):
        continue
    ph, hh = head(p), head(h)
    if re.search(r'uppajj', ph):
        pv = 'pl' if 'uppajjanti' in ph else 'sg'
        if 'उत्पन्न होती हैं' in hh: hv = 'pl'
        elif 'उत्पन्न होती है' in hh: hv = 'sg'
        else: hv = '?'
        # subject number
        ps = 'pl' if re.search(r'dhammā uppajj', ph) else 'sg'
        hs = 'pl' if 'परिघटनाएँ' in hh else 'sg'
        if pv != hv or ps != hs or hv != hs:
            print('UPP', n, sid, 'P', ps, pv, 'H', hs, hv, '|', hh[-60:])
    elif re.search(r'dhamm\w* .*paccayo$', ph.strip()) or re.search(r'paccayena paccayo', ph):
        m = re.match(r'^(.*?)dhamm(o|ā) ', ph)
        if not m:
            continue
        ps = 'sg' if m.group(2) == 'o' else 'pl'
        hs = 'pl' if re.match(r'^[^,]*परिघटनाएँ,', hh) else 'sg'
        hv = 'pl' if 'कारण होती हैं' in hh else ('sg' if 'कारण होती है' in hh else '?')
        if ps != hs or hs != hv:
            print('PAN', n, sid, 'P', ps, 'H', hs, hv, '|', hh[:80], '...', hh[-40:])
# masculine verb with feminine subject in heads
for (n, i, h) in hl:
    if re.search(r'परिघटना(एँ)?,? [^–]*?कारण होता', head(h)):
        print('GENDER?', n, head(h)[-60:])
