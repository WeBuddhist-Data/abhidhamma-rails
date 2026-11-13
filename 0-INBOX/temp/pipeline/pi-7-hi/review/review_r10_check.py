import os, sys, re, collections
sys.path.insert(0, os.path.dirname(__file__))
from review_r10_align import pairs, IDRE

PNUM = {
 'ekaṃ':1,'eko':1,'ekā':1,'ekena':1,'ekassa':1,'ekato':None,
 'dve':2,'dvinnaṃ':2,'dvīsu':2,'tīṇi':3,'tayo':3,'tisso':3,'tiṇṇaṃ':3,'tīsu':3,
 'cattāri':4,'cattāro':4,'catunnaṃ':4,'pañca':5,'pañcannaṃ':5,'cha':6,'satta':7,'aṭṭha':8,'nava':9,'dasa':10,
 'ekādasa':11,'dvādasa':12,'bārasa':12,'terasa':13,'cuddasa':14,'pannarasa':15,'paṇṇarasa':15,'soḷasa':16,
 'sattarasa':17,'aṭṭhārasa':18,'aṭṭharasa':18,'ekūnavīsa':19,'ekūnavīsati':19,'vīsa':20,'vīsati':20,'ekavīsa':21,'ekavīsati':21,
 'dvāvīsa':22,'bāvīsa':22,'bāvīsati':22,'tevīsa':23,'tevīsati':23,'catuvīsa':24,'catuvīsati':24,'pañcavīsa':25,'pañcavīsati':25,
 'chabbīsa':26,'chabbīsati':26,'sattavīsa':27,'sattavīsati':27,'aṭṭhavīsa':28,'aṭṭhavīsati':28,'ekūnatiṃsa':29,'tiṃsa':30,
 'ekatiṃsa':31,'dvattiṃsa':32,'battiṃsa':32,'tettiṃsa':33,'catuttiṃsa':34,'pañcatiṃsa':35,'chattiṃsa':36,'sattatiṃsa':37,
 'aṭṭhatiṃsa':38,'ekūnacattālīsa':39,'cattālīsa':40,
}
HNUM = {'एक':1,'दो':2,'तीन':3,'चार':4,'पाँच':5,'छह':6,'सात':7,'आठ':8,'नौ':9,'दस':10,'ग्यारह':11,'बारह':12,'तेरह':13,
 'चौदह':14,'पंद्रह':15,'सोलह':16,'सत्रह':17,'अठारह':18,'उन्नीस':19,'बीस':20,'इक्कीस':21,'बाईस':22,'तेईस':23,'चौबीस':24,
 'पच्चीस':25,'छब्बीस':26,'सत्ताईस':27,'अट्ठाईस':28,'उनतीस':29,'तीस':30,'इकतीस':31,'बत्तीस':32,'तैंतीस':33,'चौंतीस':34,
 'पैंतीस':35,'छत्तीस':36,'सैंतीस':37,'अड़तीस':38,'उनतालीस':39,'चालीस':40}

CONDS = ['hetu','ārammaṇa','adhipati','anantara','samanantara','sahajāta','aññamañña','nissaya','upanissaya','purejāta',
 'pacchājāta','āsevana','kamma','vipāka','āhāra','indriya','jhāna','magga','sampayutta','vippayutta','atthi','natthi','vigata','avigata']
HC = {'मूल':'hetu','विषय':'ārammaṇa','प्रधानता':'adhipati','निकटता':'anantara','पूर्ण निकटता':'samanantara','सह-उत्पत्ति':'sahajāta',
 'परस्पर':'aññamañña','आश्रय':'nissaya','प्रबल आश्रय':'upanissaya','पूर्व-उत्पत्ति':'purejāta','पश्चात्-उत्पत्ति':'pacchājāta',
 'पुनरावृत्ति':'āsevana','कर्म':'kamma','कर्म-फल':'vipāka','आहार':'āhāra','क्षमता':'indriya','ध्यान':'jhāna','मार्ग':'magga',
 'जुड़ाव':'sampayutta','अलगाव':'vippayutta','उपस्थिति':'atthi','अनुपस्थिति':'natthi','विलीनता':'vigata','अविलीनता':'avigata'}
# Pali count (locative) forms
def locform(c):
    if c in ('hetu','adhipati','atthi','natthi'):
        return c + 'yā'
    return c[:-1] + 'e'
alts = []
for c in CONDS:
    alts.append((c + 'paccayena', c, 'I'))
    alts.append((c + 'paccayā', c, 'A'))
    alts.append((c + 'paccayo', c, 'B'))
    alts.append((locform(c), c, 'C'))
alts.sort(key=lambda x: -len(x[0]))
FORMMAP = {a: (c, k) for a, c, k in alts}
PCOND = re.compile(r"(?<![a-zāīūṃṅñṭḍṇḷ])(na|no)?(" + '|'.join(re.escape(a) for a, _, _ in alts) + r")(?![a-zāīūṃṅñṭḍṇḷ])")
hk = sorted(HC, key=len, reverse=True)
HCOND = re.compile(r"(" + '|'.join(re.escape(k) for k in hk) + r")-कारण( के अभाव में| के बिना| का अभाव| के रूप में| में| से)?")

def pconds(s):
    out = []
    for m in PCOND.finditer(s.lower()):
        c, k = FORMMAP[m.group(2)]
        out.append((c, bool(m.group(1)), k))
    return out
def hconds(s):
    out = []
    for m in HCOND.finditer(s):
        c = HC[m.group(1)]
        suf = m.group(2) or ''
        neg = suf in (' के अभाव में', ' के बिना', ' का अभाव')
        k = {' के अभाव में':'C',' में':'C',' के बिना':'A',' से':'A',' के रूप में':'I'}.get(suf, 'B')
        if suf == ' का अभाव': k = 'B'
        out.append((c, neg, k))
    return out

PW = re.compile(r"[a-zāīūṃṅñṭḍṇḷ]+")
def ptoks(s):
    return PW.findall(s.lower())
def pnums(s):
    return [PNUM[t] for t in ptoks(s) if t in PNUM and PNUM[t]]
HSTRIP = [re.compile(r"(तीन|दो)(-(तीन|दो))? (का|के|की) वर्गीकरण"), re.compile(r"चार क्रम"), re.compile(r"किसी एक प्रकार")]
HW = re.compile(r"[^\s,।…()\[\]“”?:;\-–—\*\.]+")
def hnums(s):
    for r in HSTRIP:
        s = r.sub(' ', s)
    return [HNUM[t] for t in HW.findall(s) if t in HNUM]

LEX = {'nava','natthi','natthiyā','nayena','nayo','nayaṃ','nanu'}
def pneg(s):
    toks = ptoks(s)
    n = 0
    for i, t in enumerate(toks):
        if t in ('na', 'no'):
            n += 1; continue
        if t in ('nana', 'nano'):
            n += 2; continue
        if t in LEX or t in PNUM:
            continue
        if PCOND.fullmatch(t):
            continue
        if t.startswith('nabhāvanāya') and i > 0 and toks[i-1].endswith('nevadassanena'):
            continue
        u = t
        while (u.startswith('na') or u.startswith('no')) and len(u) > 4:
            n += 1; u = u[2:]
    return n
def hneg(s):
    return len(re.findall(r"न होने वाल", s))

def strip_id(s):
    return IDRE.sub('', s)

results = collections.defaultdict(list)
nseg = 0
for f, pl, hl in pairs():
    curid = None
    for i, (a, b) in enumerate(zip(pl, hl), 1):
        a0, b0 = strip_id(a), strip_id(b)
        head = a.startswith('#')
        tag = (f, i, (IDRE.search(a).group(1) if IDRE.search(a) else ''))
        if pnums(a0) != hnums(b0):
            results['num'].append((tag, pnums(a0), hnums(b0)))
        pd = re.findall(r"\d+", a0); hd = re.findall(r"\d+", b0)
        if pd != hd:
            results['digits'].append((tag, pd, hd))
        if not head:
            pc, hc = pconds(a0), hconds(b0)
            if pc != hc:
                results['cond'].append((tag, pc, hc))
        if pneg(a0) != hneg(b0):
            results['neg'].append((tag, pneg(a0), hneg(b0)))
        # agreement / counts
        for pk, hk_ in (("uppajjati", r"उत्पन्न होती है(?!ं)"), ("uppajjanti", r"उत्पन्न होती हैं"), ("uppajjeyya", r"\?")):
            x = a0.count(pk); y = len(re.findall(hk_, b0))
            if pk == 'uppajjati': x = len(re.findall(r"uppajjati(?!\w)", a0))
            if x != y:
                results['verb'].append((tag, pk, x, y))
        pe = a0.replace('…pe…', '…').count('…'); he = b0.count('…')
        if pe != he:
            results['ellipsis'].append((tag, pe, he))
        for ch in '–—':
            if a0.count(ch) != b0.count(ch):
                results['dash'].append((tag, ch, a0.count(ch), b0.count(ch)))
        if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", re.sub(r"\[[^\]]*\]", "", b0)):
            results['latin'].append((tag, b0[:120]))
        bb = b0.rstrip()
        if not head and bb and bb[-1] not in '।?)' :
            results['endpunct'].append((tag, bb[-30:]))
        if '  ' in b0 or ' ।' in b0 or '..' in b0 or '।।' in b0:
            results['spacing'].append((tag, b0[:80]))
        for k, pk_, hk2 in (('kus', r"(?<![a-zā])(?:na|no)*kusal", 'हितकर'), ('akus', r"(?<![a-zā])(?:na|no)*akusal", 'हानिकर'), ('abya', r"abyākat", 'अनिर्धारित')):
            x = len(re.findall(pk_, a0.lower())); y = b0.count(hk2)
            if x != y:
                results['triad-' + k].append((tag, x, y))
        if IDRE.search(a): nseg += 1
out = os.path.join(os.path.dirname(__file__), 'review_r10_check_out.txt')
with open(out, 'w', encoding='utf-8') as o:
    for k, v in results.items():
        o.write(f'=== {k} {len(v)}\n')
        for r in v:
            o.write(repr(r) + '\n')
print(out, {k: len(v) for k, v in results.items()}, 'segments', nseg)
