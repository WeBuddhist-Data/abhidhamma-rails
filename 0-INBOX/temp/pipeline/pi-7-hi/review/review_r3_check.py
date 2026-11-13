import re, os, sys
from collections import Counter
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
IDRE = re.compile(r'\^([0-9A-Za-z\-]+)\s*$')

def load(path):
    with open(path, encoding='utf-8') as f:
        return [l for l in f.read().split('\n') if l.strip()]

# ---------- numbers
PN = {'ekaṃ':1,'eko':1,'ekā':1,'eka':1,'ekañca':1,'dve':2,'tayo':3,'tīṇi':3,'tisso':3,'cattāro':4,'cattāri':4,'pañca':5,'cha':6,
      'satta':7,'aṭṭha':8,'nava':9,'dasa':10,'ekādasa':11,'dvādasa':12,'bārasa':12,'terasa':13,'cuddasa':14,'pannarasa':15,
      'soḷasa':16,'sattarasa':17,'aṭṭhārasa':18,'ekūnavīsa':19,'vīsa':20,'vīsati':20,'ekavīsa':21,'bāvīsa':22,'dvāvīsa':22,
      'tevīsa':23,'catuvīsa':24,'pañcavīsa':25,'chabbīsa':26,'sattavīsa':27,'aṭṭhavīsa':28,'ekūnatiṃsa':29,'tiṃsa':30,
      'ekatiṃsa':31,'bāttiṃsa':32,'dvattiṃsa':32,'tettiṃsa':33,'catuttiṃsa':34,'pañcatiṃsa':35,'chattiṃsa':36,
      'sattatiṃsa':37,'aṭṭhatiṃsa':38,'ekūnacattālīsa':39,'cattālīsa':40,
      'dvinnaṃ':2,'tiṇṇannaṃ':3,'tiṇṇaṃ':3,'catunnaṃ':4,'ekassa':1,'dvīsu':2,'tīsu':3,'dvīhi':2,'tīhi':3,'ekasmiṃ':1}
HN = {'एक':1,'दो':2,'तीन':3,'चार':4,'पाँच':5,'छह':6,'सात':7,'आठ':8,'नौ':9,'दस':10,'ग्यारह':11,'बारह':12,'तेरह':13,
      'चौदह':14,'पंद्रह':15,'सोलह':16,'सत्रह':17,'अठारह':18,'उन्नीस':19,'बीस':20,'इक्कीस':21,'बाईस':22,'तेईस':23,
      'चौबीस':24,'पच्चीस':25,'छब्बीस':26,'सत्ताईस':27,'अट्ठाईस':28,'उनतीस':29,'तीस':30,'इकतीस':31,'बत्तीस':32,
      'तैंतीस':33,'चौंतीस':34,'पैंतीस':35,'छत्तीस':36,'सैंतीस':37,'अड़तीस':38,'उनतालीस':39,'चालीस':40}
PW = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+")
HW = re.compile(r"[\u0900-\u0963\u0966-\u097F]+")

def pnums(s):
    out = []
    for w in PW.findall(s):
        lw = w.lower()
        if lw in PN:
            out.append(PN[lw])
        elif re.search(r'(vīsa|tiṃsa|cattālīsa|rasa)$', lw) and lw not in ('rasa',):
            out.append('?' + lw)
    return out

def hnums(s):
    s = re.sub(r'(तीन|दो) के वर्गीकरण', '', s)
    return [HN[w] for w in HW.findall(s) if w in HN]

# ---------- conditions
CONDS = ['hetu','ārammaṇa','adhipati','anantara','samanantara','sahajāta','aññamañña','nissaya','upanissaya','purejāta',
         'pacchājāta','āsevana','kamma','vipāka','āhāra','indriya','jhāna','magga','sampayutta','vippayutta','atthi',
         'natthi','vigata','avigata']
LOC = {'hetuyā':'hetu','ārammaṇe':'ārammaṇa','adhipatiyā':'adhipati','anantare':'anantara','samanantare':'samanantara',
       'sahajāte':'sahajāta','aññamaññe':'aññamañña','nissaye':'nissaya','upanissaye':'upanissaya','purejāte':'purejāta',
       'pacchājāte':'pacchājāta','āsevane':'āsevana','kamme':'kamma','vipāke':'vipāka','āhāre':'āhāra','indriye':'indriya',
       'jhāne':'jhāna','magge':'magga','sampayutte':'sampayutta','vippayutte':'vippayutta','atthiyā':'atthi',
       'natthiyā':'natthi','vigate':'vigata','avigate':'avigata'}
HC = {'मूल':'hetu','विषय':'ārammaṇa','प्रधानता':'adhipati','निकटता':'anantara','पूर्ण निकटता':'samanantara',
      'सह-उत्पत्ति':'sahajāta','परस्पर':'aññamañña','आश्रय':'nissaya','प्रबल आश्रय':'upanissaya',
      'पूर्व-उत्पत्ति':'purejāta','पश्चात्-उत्पत्ति':'pacchājāta','पुनरावृत्ति':'āsevana','कर्म':'kamma',
      'कर्म-फल':'vipāka','आहार':'āhāra','क्षमता':'indriya','ध्यान':'jhāna','मार्ग':'magga','जुड़ाव':'sampayutta',
      'अलगाव':'vippayutta','उपस्थिति':'atthi','अनुपस्थिति':'natthi','विलीनता':'vigata','अविलीनता':'avigata'}
PC_RE = re.compile(r"(?<![A-Za-zāīūṃṅñṭḍṇḷ])(na|no)?(" + '|'.join(sorted(CONDS, key=len, reverse=True)) + r")paccay", re.I)
LOC_RE = re.compile(r"(?<![A-Za-zāīūṃṅñṭḍṇḷ])(na|no)?(" + '|'.join(sorted(LOC, key=len, reverse=True)) + r")(?![A-Za-zāīūṃṅñṭḍṇḷ])", re.I)
DEV = r"[\u0900-\u0963\u0966-\u097F]"
HC_RE = re.compile(r"(पूर्ण निकटता|प्रबल आश्रय|" + DEV + r"+(?:-" + DEV + r"+)*?)-कारण( के अभाव| के बिना| का अभाव)?")

def is_count_line(p):
    return ('paṭicca' not in p and 'paccayena' not in p and 'paccayo' not in p.lower() and 'uppajj' not in p
            and any(w.lower() in PN for w in PW.findall(p)))

def pconds(p, count):
    res = []
    for m in PC_RE.finditer(p):
        res.append((m.start(), m.group(2).lower(), bool(m.group(1))))
    if count:
        for m in LOC_RE.finditer(p):
            res.append((m.start(), LOC[m.group(2).lower()], bool(m.group(1))))
    res.sort()
    return [(c, n) for _, c, n in res]

def hconds(h):
    res = []
    for m in HC_RE.finditer(h):
        name = m.group(1)
        code = HC.get(name)
        if code is None:
            # try last component
            code = '?' + name
        res.append((code, bool(m.group(2))))
    return res

# ---------- items per file
ITEMS = {
 '2-01': ([('AV', r'avitakka-?avicār'), ('AVM', r'avitakkavicāramatt'), ('SV', r'savitakkasavicār'), ('VIT', r'vitakk'), ('VIC', r'vicār')],
          [('AV', 'आरंभिक विचार और सतत विचार दोनों से रहित'), ('AVM', 'आरंभिक विचार से रहित केवल सतत विचार'),
           ('SV', 'आरंभिक विचार और सतत विचार'), ('VIT', 'आरंभिक विचार'), ('VIC', 'सतत विचार')]),
 '2-02': ([('PI', r'pīti'), ('SU', r'sukh'), ('UP', r'upekkh')], [('PI', 'उल्लास'), ('SU', 'सुख'), ('UP', 'समभाव')]),
 '2-03': ([('N', r'nevadassanena\s+nabhāvanāya\s+pahātabb'), ('D', r'dassanena\s+pahātabb'), ('B', r'bhāvanāya\s+pahātabb')],
          [('N', 'न सत्य-दर्शन से न मानसिक अभ्यास से छोड़'), ('D', 'सत्य-दर्शन से छोड़'), ('B', 'मानसिक अभ्यास से छोड़')]),
 '2-04': ([('NH', r'nevadassanena\s+nabhāvanāya\s+pahātabbahetuk'), ('DH', r'dassanena\s+pahātabbahetuk'), ('BH', r'bhāvanāya\s+pahātabbahetuk'),
           ('N', r'nevadassanena\s+nabhāvanāya\s+pahātabb'), ('D', r'dassanena\s+pahātabb'), ('B', r'bhāvanāya\s+pahātabb')],
          [('NH', r'न सत्य-दर्शन से न मानसिक अभ्यास से छोड़े जाने वाले मूलों'), ('DH', r'सत्य-दर्शन से छोड़े जाने वाले मूलों'),
           ('BH', r'मानसिक अभ्यास से छोड़े जाने वाले मूलों'),
           ('N', 'न सत्य-दर्शन से न मानसिक अभ्यास से छोड़'), ('D', 'सत्य-दर्शन से छोड़'), ('B', 'मानसिक अभ्यास से छोड़')]),
 '2-05': ([('N', r'nevācayagāmināpacayagām'), ('AP', r'apacayagām'), ('AC', r'ācayagām')],
          [('N', 'न संचय की ओर न संचय घटाने की ओर'), ('AP', 'संचय घटाने की ओर'), ('AC', 'संचय की ओर')]),
 '2-06': ([('N', r'nevasekkh?anāsekkh?'), ('AS', r'asekkh'), ('S', r'sekkh')],
          [('N', r'न सीखने के चरण \S+ न सीखना पूरा होने के चरण'), ('AS', 'सीखना पूरा होने के चरण'), ('S', 'सीखने के चरण')]),
 '2-07': ([('AP', r'appamāṇ'), ('MA', r'mahaggat'), ('PA', r'paritt')], [('AP', 'अपरिमित'), ('MA', 'उन्नत'), ('PA', 'सीमित')]),
 '2-08': ([('APa', r'appamāṇārammaṇ'), ('MAa', r'mahaggatārammaṇ'), ('PAa', r'parittārammaṇ'), ('AP', r'appamāṇ'), ('MA', r'mahaggat'), ('PA', r'paritt')],
          [('APa', 'अपरिमित विषय'), ('MAa', 'उन्नत विषय'), ('PAa', 'सीमित विषय'), ('AP', 'अपरिमित'), ('MA', 'उन्नत'), ('PA', 'सीमित')]),
}

def seq(s, pats, flags=0):
    found = []
    s2 = s
    for code, pat in pats:
        for m in re.finditer(pat, s2, flags):
            found.append((m.start(), code))
        s2 = re.sub(pat, lambda m: '#' * len(m.group(0)), s2, flags=flags)
    found.sort()
    return [c for _, c in found]

# ---------- concepts (order-insensitive counts)
CONC = [
 ('patisandhi', r'paṭisandhi', 'पुनर्जन्म'),
 ('cittasamutthana', r'cittasamuṭṭhān', 'मन से उत्पन्न'),
 ('katatta', r'kaṭattā', 'किए गए कर्म से उत्पन्न'),
 ('upada', r'upādā', 'व्युत्पन्न'),
 ('mahabhuta', r'mahābhūt', 'महाभूत'),
 ('vatthu', r'vatthu', 'आधार'),
 ('khandha', r'khandh', 'समूह'),
 ('nibbana', r'nibbān', 'निर्वाण'),
 ('raga', r'rāg', 'राग'),
 ('dosa', r'(?<![a-z])dos(?!an)', 'द्वेष'),
 ('moha', r'(?<![a-z])moh', 'मोह'),
 ('ditthi', r'diṭṭh', 'दृष्टि'),
 ('vicikiccha', r'vicikicch', 'संशय'),
 ('uddhacca', r'uddhacc', 'बेचैनी'),
 ('cakkhu', r'cakkhu', 'आँख'),
 ('akusala', r'akusal', 'हानिकर'),
 ('kusala_all', r'kusal', 'हितकर|हानिकर'),
 ('phala', r'phal', 'फल'),
 ('magga', r'(?<![a-z])magg', 'मार्ग'),
 ('jhana', r'jhān', 'ध्यान'),
 ('saddha', r'saddh', 'श्रद्धा|आस्था'),
 ('sila', r'(?<![a-z])sīl', 'शील|नैतिक'),
 ('dana', r'(?<![a-z])dān', 'दान'),
 ('patisandhi_cuti', r'cut', 'च्युति|मृत्यु'),
 ('vipaka', r'vipāk', 'कर्म-फल'),
 ('kiriya', r'kiriy', 'क्रिया'),
 ('ahara', r'āhār', 'आहार|भोजन'),
 ('kaya', r'(?<![a-z])kāy', 'शरीर|काय'),
 ('pacchajata', r'pacchājāt', 'पश्चात्-उत्पत्ति|बाद में उत्पन्न'),
 ('purejata', r'purejāt', 'पूर्व-उत्पत्ति|पहले उत्पन्न'),
 ('sahajata', r'sahajāt', 'सह-उत्पत्ति|साथ उत्पन्न'),
 ('gotrabhu', r'gotrabh', 'गोत्र-परिवर्तन'),
 ('vodana', r'vodān', 'शुद्धि'),
 ('anuloma', r'anulom', 'अनुलोम|अनुकूलता'),
 ('avajjana', r'āvajjan', 'मोड़'),
 ('cetana', r'cetan', 'चेतना|इरादा|संकल्प'),
 ('sekha_maggaphala', r'arahat', 'अर्हत'),
]

CONC = [c for c in CONC if c[0] not in ('cetana', 'anuloma', 'avajjana', 'sekha_maggaphala')]
FIX = {'ditthi': r'(?<!अंतर्)दृष्टि', 'sila': r'सदाचार|शील', 'jhana': r'ध्यान(?!-अवस्था)', 'phala': r'(?<!कर्म-)फल',
       'ahara': r'आहार', 'kaya': r'शरीर|शारीरिक|काय', 'cakkhu': r'आँख'}
CONC = [(n, pp, FIX.get(n, hp)) for n, pp, hp in CONC]
REL = [
 ('paticca', r'paṭicca', r'पर निर्भर होकर'),
 ('paccaya_abl', r'(?<![a-zāīū])paccayā(?! )|(?<![a-zāīū])paccayā(?= )', r'के कारण(?! होत)'),
 ('sahajato', r'sahajāt[oāaṃ]\b(?! dhamm)', r'के साथ जन्म लेकर|के साथ उत्पन्न होकर'),
 ('samsattha', r'saṃsaṭṭh', r'घुल-मिल'),
 ('sampayutta', r'(?<![a-z])sampayutt[oāaṃ](?![a-z])', r'से जुड़'),
 ('uppajjanti', r'dhammā\s+(?:\S+\s+)?uppajjanti', r'परिघटनाएँ'),
 ('dhamma_pl_gen', r'dhammānaṃ', r'परिघटनाओं'),
]

def strip_var(s):
    s = re.sub(r'\{[^}]*\}', '', s)
    s = re.sub(r'\[(पाठभेद|वर्तनी-भेद)[^\]]*\]', '', s)
    return IDRE.sub('', s)

FILES = ['2-01-vitakkattika.md', '2-02-pitittika.md', '2-03-dassanenapahatabbattika.md',
         '2-04-dassanenapahatabbahetukattika.md', '2-05-acayagamittika.md', '2-06-sekkhattika.md',
         '2-07-parittattika.md', '2-08-parittarammanattika.md']
out = []
nseg = 0
stats = Counter()
for f in FILES:
    P = load(os.path.join(B, 'pali', 'pi-7_split_chapters', f))
    H = load(os.path.join(B, 'hindi', 'pi-7-hindi-plain-rails_split_chapters', f))
    key = f[:4]
    ppat, hpat = ITEMS[key]
    cid = None
    for i, (p0, h0) in enumerate(zip(P, H), 1):
        m = IDRE.search(p0)
        if m: nseg += 1
        p, h = strip_var(p0), strip_var(h0)
        tag = f'{f}:{i}'
        if p.startswith('#'):
            continue
        # numbers
        pn, hn = pnums(p), hnums(h)
        if Counter(pn) != Counter(hn):
            out.append(f'NUM {tag} p={pn} h={hn}'); stats['NUM'] += 1
        elif pn != hn and is_count_line(p):
            out.append(f'NUMORD {tag} p={pn} h={hn}'); stats['NUMORD'] += 1
        # conditions
        cnt = is_count_line(p)
        pc, hc = pconds(p, cnt), hconds(h)
        if pc != hc:
            out.append(f'COND {tag} p={pc} h={hc}'); stats['COND'] += 1
        # items
        ps, hs = seq(p, ppat, re.I), seq(h, hpat)
        if ps != hs:
            if Counter(ps) == Counter(hs):
                out.append(f'ITEMORD {tag} p={ps} h={hs}'); stats['ITEMORD'] += 1
            else:
                out.append(f'ITEM {tag} p={ps} h={hs}'); stats['ITEM'] += 1
        # verbs / relation forms
        for name, pp, hp in REL:
            a = len(re.findall(pp, p)); b = len(re.findall(hp, h))
            if a != b:
                out.append(f'REL {tag} {name} p={a} h={b}'); stats['REL:' + name] += 1
        # concepts
        pz = re.sub(r'\S*paccay\S*', ' ', p)
        if cnt:
            pz = LOC_RE.sub(' ', pz)
        hz = HC_RE.sub(' ', h)
        for name, pp, hp in CONC:
            a = len(re.findall(pp, pz, re.I)); b = len(re.findall(hp, hz))
            if a != b:
                out.append(f'CONC {tag} {name} p={a} h={b}'); stats['CONC:' + name] += 1
        # na/no
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'review_r3_check.out'), 'w', encoding='utf-8').write('\n'.join(out))
print('segments', nseg)
for k, v in sorted(stats.items()):
    print(k, v)
