import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r8_common import load, H
p, h, ids = load()

COND = ['hetu', 'ārammaṇa', 'adhipati', 'anantara', 'samanantara', 'sahajāta', 'aññamañña', 'nissaya',
        'upanissaya', 'purejāta', 'pacchājāta', 'āsevana', 'kamma', 'vipāka', 'āhāra', 'indriya', 'jhāna',
        'magga', 'sampayutta', 'vippayutta', 'atthi', 'natthi', 'vigata', 'avigata']
LOC = ['hetuyā', 'ārammaṇe', 'adhipatiyā', 'anantare', 'samanantare', 'sahajāte', 'aññamaññe', 'nissaye',
       'upanissaye', 'purejāte', 'pacchājāte', 'āsevane', 'kamme', 'vipāke', 'āhāre', 'indriye', 'jhāne',
       'magge', 'sampayutte', 'vippayutte', 'atthiyā', 'natthiyā', 'vigate', 'avigate']
HC = ['मूल', 'विषय', 'प्रधानता', 'निकटता', 'पूर्ण निकटता', 'सह-उत्पत्ति', 'परस्पर', 'आश्रय', 'प्रबल आश्रय',
      'पूर्व-उत्पत्ति', 'पश्चात्-उत्पत्ति', 'पुनरावृत्ति', 'कर्म', 'कर्म-फल', 'आहार', 'क्षमता', 'ध्यान', 'मार्ग',
      'जुड़ाव', 'अलगाव', 'उपस्थिति', 'अनुपस्थिति', 'विलीनता', 'अविलीनता']
H2I = {c: i for i, c in enumerate(HC)}
NUMW = r'(?:ekaṃ|dve|tīṇi|cattāri|pañca|cha|satta|aṭṭha|nava|dasa|ekādasa|dvādasa|terasa|cuddasa|pannarasa|soḷasa|sattarasa|aṭṭhārasa|ekūnavīsati|vīsati)'
rp = re.compile(r'(?<![a-zāīūṃṅñṭḍṇḷ])(na|no)?(' + '|'.join(sorted(COND, key=len, reverse=True)) + r')paccay(?:ā|ena|o|e)\b', re.I)
rl = re.compile(r'(?<![a-zāīūṃṅñṭḍṇḷ])(na|no)?(' + '|'.join(sorted(LOC, key=len, reverse=True)) + r')(?=(?:\s*\(?[a-zā ]*\)?)?[\s,…]*(?:…pe…\s*)?' + NUMW + r'\b|,|…)', re.I)
rh = re.compile(r'(?<![\u0900-\u097F-])(' + '|'.join(sorted(HC, key=len, reverse=True)) + r')-कारण( के बिना| का अभाव| के अभाव)?')

def pconds(s):
    out = []
    for m in rp.finditer(s):
        out.append((m.start(), COND.index(m.group(2).lower() if m.group(2)[0].islower() else m.group(2)[0].lower() + m.group(2)[1:]), bool(m.group(1))))
    for m in rl.finditer(s):
        g = m.group(2); g = g[0].lower() + g[1:]
        out.append((m.start(), LOC.index(g), bool(m.group(1))))
    out.sort()
    return [(c, n) for _, c, n in out]

def hconds(s):
    return [(H2I[m.group(1)], bool(m.group(2))) for m in rh.finditer(s)]

PN = {'ekaṃ': 1, 'eko': 1, 'ekā': 1, 'ekassa': 1, 'ekaṃ,': 1, 'dve': 2, 'dvinnaṃ': 2, 'tayo': 3, 'tīṇi': 3, 'tiṇṇaṃ': 3,
      'tiṇṇannaṃ': 3, 'tisso': 3, 'cattāri': 4, 'cattāro': 4, 'catunnaṃ': 4, 'pañca': 5, 'pañcannaṃ': 5, 'cha': 6,
      'channaṃ': 6, 'satta': 7, 'aṭṭha': 8, 'nava': 9, 'navapi': 9, 'dasa': 10, 'ekādasa': 11, 'dvādasa': 12, 'terasa': 13,
      'cuddasa': 14, 'pannarasa': 15, 'soḷasa': 16, 'sattarasa': 17, 'aṭṭhārasa': 18, 'ekūnavīsati': 19, 'vīsati': 20,
      'catūsu': 4, 'tīsu': 3, 'dvīsu': 2, 'pañcasu': 5, 'chasu': 6, 'navasu': 9}
HN = {'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पाँच': 5, 'छह': 6, 'सात': 7, 'आठ': 8, 'नौ': 9, 'दस': 10, 'ग्यारह': 11,
      'बारह': 12, 'तेरह': 13, 'चौदह': 14, 'पंद्रह': 15, 'सोलह': 16, 'सत्रह': 17, 'अठारह': 18, 'उन्नीस': 19, 'बीस': 20}

def pnums(s):
    toks = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷĀĪŪ]+', s)
    return sorted(PN[t.lower()] for t in toks if t.lower() in PN)

def hnums(s):
    s = re.sub(r'दो(-दो)? (का|के) वर्गीकरण', '', s)
    s = re.sub(r'तीन (का|के) वर्गीकरण', '', s)
    toks = re.findall(r'[\u0900-\u0963\u0966-\u097F]+', s)
    return sorted(HN[t] for t in toks if t in HN)

def strip_id(s):
    return re.sub(r'\s*\^\S+\s*$', '', s)

issues = collections.defaultdict(list)
for i, (a, b) in enumerate(zip(p, h)):
    ln = i + 1
    A, B = strip_id(a), strip_id(b)
    if a.startswith('#'):
        continue
    # markers (N)
    ma = re.findall(r'\((\d+)\)', A); mb = re.findall(r'\((\d+)\)', B)
    if ma != mb: issues['marker'].append((ln, ma, mb))
    # digits overall
    da = re.findall(r'\d+', A); db = re.findall(r'\d+', B)
    if sorted(da) != sorted(db): issues['digits'].append((ln, da, db))
    # conds
    ca, cb = pconds(A), hconds(B)
    if ca != cb: issues['cond'].append((ln, ca, cb))
    # numbers
    na, nb = pnums(A), hnums(B)
    if na != nb: issues['num'].append((ln, na, nb))
    # ellipsis
    ea = A.count('…pe…') + A.replace('…pe…', '').count('…'); eb = B.count('…')
    if ea != eb: issues['ellipsis'].append((ln, ea, eb))
    # dashes
    da_ = A.count('–') + A.count('—'); db_ = B.count('–') + B.count('—')
    if da_ != db_ or '—' in B and '—' not in A: issues['dash'].append((ln, da_, db_))
    # hyphen-minus used as dash
    if ' - ' in B: issues['hyphen'].append((ln,))
    # latin outside brackets
    Bn = re.sub(r'\[[^\]]*\]', '', B)
    lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', Bn)
    if lat: issues['latin'].append((ln, lat[:5]))
    # quotes
    if '"' in B or "'" in B: issues['quote'].append((ln,))
    # ending
    t = re.sub(r'\s*\(\d+\)$', '', B.rstrip())
    t = re.sub(r'(\s*\(\d+\))+$', '', t)
    if not re.search(r'[।?]\)?$|[।?]\s*\(\d+\)\)?$|…$|।\)$|\)$', B.rstrip()):
        issues['ending'].append((ln, B[-25:]))
    if '.' in Bn.replace('...', ''):
        issues['period'].append((ln, Bn[Bn.find('.') - 15: Bn.find('.') + 5]))
    # paren count
    if A.count('(') != B.count('(') or A.count('[') + A.count('{') != B.count('['):
        issues['paren'].append((ln, A.count('('), B.count('('), A.count('{'), B.count('[')))
    # cakkam / samkhittam
    for pw, hw in [('cakkaṃ', 'चक्र'), ('saṃkhitt', 'संक्षिप्त'), ('pucchitabb', None), ('ninnānākaraṇ', 'बिना किसी अंतर'), ('sadis', 'समान')]:
        if hw and len(re.findall(pw, A, re.I)) != B.count(hw):
            issues['kw-' + pw].append((ln, len(re.findall(pw, A, re.I)), B.count(hw)))
    # question marks
    if A.count('?') != B.count('?'): issues['qmark'].append((ln, A.count('?'), B.count('?')))

raw = open(H, encoding='utf-8').read()
if '\n\n\n' in raw: print('DOUBLE BLANK LINES present', raw.count('\n\n\n'))
for k, v in issues.items():
    print('==', k, len(v))
    for x in v[:60]:
        print('  ', x)


