import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *
praw, pl = load(P)
hraw, hl = load(H)
S = segs(pl)
prev_subj = None
for ((n, i, p), sid), (_, _, h) in zip(S, hl):
    if p.startswith('#'):
        continue
    m = re.match(r'^\S.*?dhamm(o|ā) [\wāīūṃṅñṭḍṇḷ ]*?dhammassa', p)
    if m:
        prev_subj = 'sg' if m.group(1) == 'o' else 'pl'
        subj = prev_subj
    elif re.match(r'^[A-ZĀ][\wāīūṃṅñṭḍṇḷ]*paccayena paccayo', p):
        subj = prev_subj  # continuation line
    else:
        continue
    want = 'होती है' if subj == 'sg' else 'होती हैं'
    for mm in re.finditer(r'(?:^|…\s?)((?:[^\s…]+ ){0,3}[^\s…]*-कारण के रूप में कारण (होती हैं|होती है|होते हैं|होता है))', h):
        got = mm.group(2)
        if got != want:
            print(n, sid, subj, '|', mm.group(1))
