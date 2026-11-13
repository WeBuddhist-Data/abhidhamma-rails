import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *

praw, pl = load(P)
hraw, hl = load(H)
S = segs(pl)
W = r'(?<![\wāīūṃṅñṭḍṇḷ])'
prx = W + r'(?:no)?citt(?:aṃ|o|assa|añca|e|ena|ā|ānaṃ|āni|a)(?![\wāīūṃṅñṭḍṇḷ])'
EXC = [r'मन से उत्पन्न', r'मन को विषय की ओर', r'मन के क्लेश', r'दूसरों के मन को जानने', r'मन के साथ-साथ', r'मन का अनुसरण',
       r'मन से घुल', r'मन से जुड़', r'मन से अलग', r'मन (?:की|के|का) सहचर', r'मन रूपी', r'मन से युक्त', r'मन (?:के|का) तत्व',
       r'मन की चेतना', r'(?:हितकर|हानिकर|रूपी|अनिर्धारित) मन', r'मन की ओर']
def hcount(t):
    for e in EXC:
        t = re.sub(e, 'X', t)
    return len(re.findall(r'(?<![\u0900-\u097F])मन(?![\u0900-\u097F])', t))
for ((n, i, p), sid), (_, _, h) in zip(S, hl):
    if p.startswith('#'):
        continue
    pt = IDRE.sub('', p); ht = IDRE.sub('', h)
    pt2 = re.sub(r'(?:no)?citta(?:saṃsaṭṭha|samuṭṭhāna|sahabh|ānuparivatt|sampayutt|vippayutt|visaṃsaṭṭh)\w*', '', pt)
    a = len(re.findall(prx, pt2, flags=re.I)); b = hcount(ht)
    if a != b:
        print(n, sid, a, b)
