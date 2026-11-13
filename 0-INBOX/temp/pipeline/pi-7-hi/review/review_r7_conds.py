import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *

praw, pl = load(P)
hraw, hl = load(H)
S = segs(pl)

# canonical condition keys
PC = [('samanantar', 'samanantara'), ('anantar', 'anantara'), ('sahajāt', 'sahajata'), ('aññamañ', 'annamanna'),
      ('upanissay', 'upanissaya'), ('nissay', 'nissaya'), ('purejāt', 'purejata'), ('pacchājāt', 'pacchajata'),
      ('āsevan', 'asevana'), ('kamm', 'kamma'), ('vipāk', 'vipaka'), ('āhār', 'ahara'), ('indriy', 'indriya'),
      ('jhān', 'jhana'), ('magg', 'magga'), ('sampayutt', 'sampayutta'), ('vippayutt', 'vippayutta'),
      ('natthi', 'natthi'), ('atthi', 'atthi'), ('avigat', 'avigata'), ('vigat', 'vigata'),
      ('hetu', 'hetu'), ('ārammaṇ', 'arammana'), ('adhipati', 'adhipati')]
stems = '|'.join(re.escape(s) for s, _ in PC)
# forms: Xpaccayā / Xpaccayena / Xpaccayo ; locative count forms
LOC = {'hetuyā': 'hetu', 'ārammaṇe': 'arammana', 'adhipatiyā': 'adhipati', 'anantare': 'anantara',
       'samanantare': 'samanantara', 'sahajāte': 'sahajata', 'aññamaññe': 'annamanna', 'nissaye': 'nissaya',
       'upanissaye': 'upanissaya', 'purejāte': 'purejata', 'pacchājāte': 'pacchajata', 'āsevane': 'asevana',
       'kamme': 'kamma', 'vipāke': 'vipaka', 'āhāre': 'ahara', 'indriye': 'indriya', 'jhāne': 'jhana',
       'magge': 'magga', 'sampayutte': 'sampayutta', 'vippayutte': 'vippayutta', 'atthiyā': 'atthi',
       'natthiyā': 'natthi', 'vigate': 'vigata', 'avigate': 'avigata'}
key = dict(PC)

def pconds(t):
    t = IDRE.sub('', t)
    out = []
    for m in re.finditer(r"(?<![\wāīūṃṅñṭḍṇḷ])(n[ao] ?)?([\wāīūṃṅñṭḍṇḷ]+?)(paccayā|paccayena|paccayo|sadis[āaoṃ]+)(?![\wāīūṃṅñṭḍṇḷ])|(?<![\wāīūṃṅñṭḍṇḷ])(n[ao] ?)?(" + '|'.join(LOC) + r")(?![\wāīūṃṅñṭḍṇḷ])", t, flags=re.I):
        if m.group(2):
            neg, stem, form = m.group(1), m.group(2).lower(), m.group(3)
            def look(st):
                for s, kk in PC:
                    if st == s or st.startswith(s) and len(st) - len(s) <= 2:
                        return kk
                return None
            k = look(stem)
            if k is None and neg:
                k = look(neg.replace(' ', '').lower() + stem)
                if k is not None:
                    neg = None
            if k is None:
                out.append(('?' + stem, bool(neg)))
                continue
            # handle natthi/atthi with na/no prefix ambiguity: "natthi" stem itself
            out.append((k, bool(neg)))
        else:
            neg, w = m.group(4), m.group(5).lower()
            out.append((LOC[w], bool(neg)))
    return out

HC = [('पूर्ण निकटता', 'samanantara'), ('प्रबल आश्रय', 'upanissaya'), ('कर्म-फल', 'vipaka'),
      ('सह-उत्पत्ति', 'sahajata'), ('पूर्व-उत्पत्ति', 'purejata'), ('पश्चात्-उत्पत्ति', 'pacchajata'),
      ('अनुपस्थिति', 'natthi'), ('अविलीनता', 'avigata'), ('निकटता', 'anantara'), ('परस्पर', 'annamanna'),
      ('आश्रय', 'nissaya'), ('पुनरावृत्ति', 'asevana'), ('कर्म', 'kamma'), ('आहार', 'ahara'), ('क्षमता', 'indriya'),
      ('ध्यान', 'jhana'), ('मार्ग', 'magga'), ('जुड़ाव', 'sampayutta'), ('अलगाव', 'vippayutta'),
      ('उपस्थिति', 'atthi'), ('विलीनता', 'vigata'), ('मूल', 'hetu'), ('विषय', 'arammana'), ('प्रधानता', 'adhipati')]
hre = re.compile('(' + '|'.join(re.escape(a) for a, _ in HC) + r')-कारण( के अभाव में| के बिना| का अभाव)?')
hkey = dict(HC)

def hconds(t):
    t = IDRE.sub('', t)
    return [(hkey[m.group(1)], bool(m.group(2))) for m in hre.finditer(t)]

for ((n, i, p), sid), (_, _, h) in zip(S, hl):
    if p.startswith('#'): continue
    a, b = [x for x in pconds(p) if not x[0].startswith('?')], hconds(h)
    if a != b:
        print('COND', n, sid)
        print('   P', a)
        print('   H', b)

