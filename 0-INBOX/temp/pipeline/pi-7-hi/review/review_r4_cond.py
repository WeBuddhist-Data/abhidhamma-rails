import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r4_struct_lib import *

PC = ['hetu', 'ārammaṇa', 'adhipati', 'anantara', 'samanantara', 'sahajāta', 'aññamañña', 'nissaya',
      'upanissaya', 'purejāta', 'pacchājāta', 'āsevana', 'kamma', 'vipāka', 'āhāra', 'indriya', 'jhāna',
      'magga', 'sampayutta', 'vippayutta', 'atthi', 'natthi', 'vigata', 'avigata']
LOC = {'hetu': 'hetuyā', 'ārammaṇa': 'ārammaṇe', 'adhipati': 'adhipatiyā', 'anantara': 'anantare',
       'samanantara': 'samanantare', 'sahajāta': 'sahajāte', 'aññamañña': 'aññamaññe', 'nissaya': 'nissaye',
       'upanissaya': 'upanissaye', 'purejāta': 'purejāte', 'pacchājāta': 'pacchājāte', 'āsevana': 'āsevane',
       'kamma': 'kamme', 'vipāka': 'vipāke', 'āhāra': 'āhāre', 'indriya': 'indriye', 'jhāna': 'jhāne',
       'magga': 'magge', 'sampayutta': 'sampayutte', 'vippayutta': 'vippayutte', 'atthi': 'atthiyā',
       'natthi': 'natthiyā', 'vigata': 'vigate', 'avigata': 'avigate'}
HC = {'hetu': 'मूल', 'ārammaṇa': 'विषय', 'adhipati': 'प्रधानता', 'anantara': 'निकटता',
      'samanantara': 'पूर्ण निकटता', 'sahajāta': 'सह-उत्पत्ति', 'aññamañña': 'परस्पर', 'nissaya': 'आश्रय',
      'upanissaya': 'प्रबल आश्रय', 'purejāta': 'पूर्व-उत्पत्ति', 'pacchājāta': 'पश्चात्-उत्पत्ति',
      'āsevana': 'पुनरावृत्ति', 'kamma': 'कर्म', 'vipāka': 'कर्म-फल', 'āhāra': 'आहार', 'indriya': 'क्षमता',
      'jhāna': 'ध्यान', 'magga': 'मार्ग', 'sampayutta': 'जुड़ाव', 'vippayutta': 'अलगाव', 'atthi': 'उपस्थिति',
      'natthi': 'अनुपस्थिति', 'vigata': 'विलीनता', 'avigata': 'अविलीनता'}
H2P = {v: k for k, v in HC.items()}
order = sorted(PC, key=len, reverse=True)
NUMW = set(PNUM) | {'ekavīsa', 'pañcavīsa', 'bāvīsa', 'dvāvīsa', 'tevīsa', 'catuvīsa'}
pre = r'(?<![a-zāīūṃṅñṭḍṇḷ])(no|na)?'
P_PAC = re.compile(pre + '(' + '|'.join(order) + r')paccay', re.I)
P_LOC = re.compile(pre + '(' + '|'.join(LOC[c] for c in order) + r')(?=[ ,]+(?:' + '|'.join(sorted(NUMW, key=len, reverse=True)) + r'|' + pre + '(?:' + '|'.join(LOC[c] for c in order) + r'))|…|\s*\()', re.I)
LOC2C = {v: k for k, v in LOC.items()}
hord = sorted(HC.values(), key=len, reverse=True)
H_RE = re.compile('(' + '|'.join(re.escape(x) for x in hord) + r')-कारण(\s+(?:के बिना|के अभाव|का अभाव))?')

def pal_conds(p):
    res = []
    for m in P_PAC.finditer(p):
        res.append((m.start(), m.group(2).lower(), 'N' if m.group(1) else 'P'))
    for m in P_LOC.finditer(p):
        res.append((m.start(), LOC2C[m.group(2).lower()], 'N' if m.group(1) else 'P'))
    res.sort()
    return [(c, s) for _, c, s in res]

def hin_conds(h):
    res = []
    for m in H_RE.finditer(h):
        # exclude preceding letter (e.g. अविलीनता vs विलीनता handled by order); check char before
        st = m.start()
        if st > 0 and re.match(r'[ऀ-ॣ०-ॿ]', h[st - 1]) and h[st - 1] not in ' ':
            continue
        res.append((H2P[m.group(1)], 'N' if m.group(2) else 'P'))
    return res

if __name__ == '__main__':
    tot = 0
    for f in FILES:
        P = nonempty(load(os.path.join(PA, f)))
        H = nonempty(load(os.path.join(HI, f)))
        for n, ((_, p), (_, h)) in enumerate(zip(P, H), 1):
            a = pal_conds(p); b = hin_conds(h)
            if a != b:
                tot += 1
                print(f, n)
                print('  P', a)
                print('  H', b)
    print('TOTAL', tot)
