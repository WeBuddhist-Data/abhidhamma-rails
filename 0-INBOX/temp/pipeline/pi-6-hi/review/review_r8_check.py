import re, glob, sys, collections
B = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['10-08', '10-09', '10-10', '10-11', '10-12', '10-13']

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

def load(f):
    p = glob.glob(B + r'\pali\pi-6_split_chapters\%s*.md' % f)[0]
    h = glob.glob(B + r'\hindi\pi-6-hindi-plain-rails_split_chapters\%s*.md' % f)[0]
    return lines(p), lines(h)

# ---------------- Pali verbs ----------------
PV = [
    ('U', r'uppajj(?:atī|ati|anti)', 'P'), ('U', r'uppajj(?:itthā|ittha)', 'A'), ('U', r'uppajj(?:issatī|issati|issanti)', 'F'),
    ('PJ', r'parijān(?:ātī|āti|anti)', 'P'), ('PJ', r'parijān(?:itthā|ittha)', 'A'), ('PJ', r'parijān(?:issatī|issati|issanti)', 'F'),
    ('PH', r'p?pajah(?:atī|ati|anti)', 'P'), ('PH', r'p?pajah(?:itthā|ittha)', 'A'), ('PH', r'p?pajah(?:issatī|issati|issanti)', 'F'),
    ('BH', r'bhāv(?:etī|eti|enti)', 'P'), ('BH', r'bhāv(?:itthā|ittha)', 'A'), ('BH', r'bhāv(?:essatī|essati|essanti)', 'F'),
    ('SK', r'sacchikar(?:otī|oti|onti)', 'P'), ('SK', r'sacchikar(?:itthā|ittha)', 'A'), ('SK', r'sacchākāsi', 'A'), ('SK', r'sacchikar(?:issatī|issati|issanti)', 'F'),
    ('NB', r'parinibbāyiss(?:anti|ati)', 'F'), ('ML', r'paṭilabhiss(?:anti|ati)', 'F'),
]
pv_re = re.compile(r'(?<![\w])(no ca\b[^.?]*?)?(na |n)?(' + '|'.join('(?:%s)' % p for _, p, _ in PV) + r')(?![\w])', re.I)

def pali_verbs(s):
    out = []
    # tokenise: find 'no ca' markers and verbs in order
    toks = []
    for m in re.finditer(r'\bno ca\b', s, re.I):
        toks.append((m.start(), 'NOCA', None))
    vre = re.compile(r'(?<![\w])(na |n(?=uppajj)|na(?=ppajah))?(' + '|'.join('(?:%s)' % p for _, p, _ in PV) + r')(?:ti)?(?![\w])', re.I)
    for m in vre.finditer(s):
        w = m.group(2)
        neg = bool(m.group(1))
        if w.lower().startswith('ppajah'):
            neg = True
        for lem, p, t in PV:
            if re.fullmatch(p, w, re.I):
                toks.append((m.start(), lem, (t, neg)))
                break
    toks.sort()
    flip = False
    for pos, kind, val in toks:
        if kind == 'NOCA':
            flip = True
            continue
        t, neg = val
        if flip:
            neg = not neg
            flip = False
        out.append((kind, t, neg))
    return out

# ---------------- Hindi verbs ----------------
HV = [
    ('U', r'उत्पन्न( नहीं)? (होता|होती|होते|हुआ|हुई|हुए|होगा|होगी|होंगे|होंगी)(?![ऀ-ॣ])'),
    ('PJ', r'पूरी तरह( नहीं)? (समझता|समझती|समझते|समझेगा|समझेगी|समझेंगे|समझेंगी|समझा|समझी|समझे)(?![ऀ-ॣ])'),
    ('PH', r'(नहीं )?(छोड़ता|छोड़ती|छोड़ते|छोड़ेगा|छोड़ेगी|छोड़ेंगे|छोड़ा|छोड़ी|छोड़े)(?![ऀ-ॣ])'),
    ('BH', r'अभ्यास( नहीं)? (करता|करती|करते|करेगा|करेगी|करेंगे|किया|कर लिया)(?![ऀ-ॣ])'),
    ('SK', r'साक्षात्कार( नहीं)? (करता|करती|करते|करेगा|करेगी|करेंगे|किया|कर लिया)(?![ऀ-ॣ])'),
    ('NB', r'निर्वाण( नहीं)? (पाएँगे|पाएँगी|पाएगा|पाएगी)(?![ऀ-ॣ])'),
    ('ML', r'मार्ग प्राप्त( नहीं)? (करेंगे|करेगा)(?![ऀ-ॣ])'),
]

def htense(lem, w):
    if lem == 'U':
        if w.startswith('हु'):
            return 'A'
        if w in ('होगा', 'होगी', 'होंगे', 'होंगी'):
            return 'F'
        return 'P'
    if w.endswith('गा') or w.endswith('गी') or w.endswith('गे') or w in ('पाएँगे', 'पाएँगी'):
        return 'F'
    if w.endswith('ता') or w.endswith('ती') or w.endswith('ते'):
        return 'P'
    return 'A'

def hindi_verbs(s):
    toks = []
    for lem, p in HV:
        for m in re.finditer(p, s):
            neg = bool(m.group(1))
            toks.append((m.start(), lem, htense(lem, m.group(2)), neg))
    toks.sort()
    return [(l, t, n) for _, l, t, n in toks]

# ---------------- items ----------------
PITEM = r'(?<![\w])(cakkhu|sot|ghān|ghāna|jivh|kāy|man|itth|puris|jīvit|sukh|dukkh|somanass|domanass|upekkh|saddh|vīriy|sat|samādh|paññ|anaññātaññassāmīt|aññātāv|aññ)(?:indriy|ndriy|andriy)'
PMAP = {'cakkhu': 'आँख', 'sot': 'कान', 'ghān': 'नाक', 'ghāna': 'नाक', 'man': 'मन', 'itth': 'स्त्रीत्व', 'puris': 'पुरुषत्व', 'jīvit': 'जीवन',
        'somanass': 'प्रसन्नता', 'domanass': 'उदासी', 'upekkh': 'समभाव', 'saddh': 'श्रद्धा', 'paññ': 'प्रज्ञा',
        'anaññātaññassāmīt': 'अनञ्ञात', 'aññātāv': 'चुके', 'aññ': 'पूर्णज्ञान', 'jivh': 'जीभ', 'kāy': 'शरीर', 'sukh': 'सुख', 'dukkh': 'दुःख'}
HITEM = r'(आँख|कान|नाक|जीभ|शरीर|मन|स्त्रीत्व|पुरुषत्व|प्रसन्नता|उदासी|समभाव|श्रद्धा|प्रज्ञा|सुख|दुःख) की क्षमता|जीवन-क्षमता|“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता|पूर्ण ज्ञान पा चुके की क्षमता|पूर्ण ज्ञान की क्षमता'

def hitems(s):
    out = []
    for m in re.finditer(HITEM, s):
        g = m.group(0)
        if m.group(1):
            out.append(m.group(1))
        elif g.startswith('जीवन'):
            out.append('जीवन')
        elif g.startswith('“'):
            out.append('अनञ्ञात')
        elif 'चुके' in g:
            out.append('चुके')
        else:
            out.append('पूर्णज्ञान')
    return out

def pitems(s):
    return [PMAP[m.group(1).lower()] for m in re.finditer(PITEM, s, re.I)]

# ---------------- feature counts ----------------
FEAT = [
    ('cav', r'cavant|cavantī', r'मरने वाल|मरने वाली'),
    ('upap', r'upapajjant', r'जन्म लेने वाल|जन्म लेने वाली'),
    ('parinibbant', r'parinibbant', r'परिनिर्वाण|निर्वाण प्राप्त कर रहे|निर्वाण पाने वाल'),
    ('asañña', r'asaññasatt', r'पहचान-रहित'),
    ('suddh', r'suddhāvās', r'शुद्ध निवास'),
    ('pañcavok', r'pañcavokār', r'पाँच समूहों|पाँच'),
    ('catuvok', r'catuvokār', r'चार या पाँच|चार समूहों'),
    ('kāma', r'kāmāvacar', r'इंद्रिय-सुखों'),
    ('rūpa', r'(?<!a)rūpāvacar', r'सूक्ष्म भौतिक'),
    ('arūpa', r'arūpāvacar|arūpān|arūpe\b|arūpaṃ', r'अभौतिक'),
    ('sa-organ', r'\bsacakkhuk|\bsaghānak', r'आँख वाल|नाक वाल'),
    ('a-organ', r'\bacakkhuk|\baghānak', r'आँख से रहित|नाक से रहित'),
    ('itthī', r'itthīnaṃ|itthiyo', r'स्त्रियों|स्त्रियाँ'),
    ('purisā', r'purisānaṃ|purisā\b', r'पुरुषों|पुरुष '),
    ('bhaṅga', r'bhaṅgakkhaṇ', r'भंग'),
    ('uppāda', r'uppādakkhaṇ', r'उत्पन्न होने के क्षण'),
    ('pavatte', r'pavatte', r'जीवन के दौरान'),
    ('nirodha', r'nirodhasamāpann', r'समाप्ति'),
    ('itare', r'itaresaṃ|itarāsaṃ', r'बाकी'),
    ('sabbe', r'sabbesaṃ', r'सभी'),
    ('pacchimabhav', r'pacchimabhavik', r'अंतिम जन्म'),
    ('pacchimacitta', r'pacchimacitt', r'अंतिम मन'),
    ('tattha', r'\btattha\b|\byattha\b', r'वहाँ|जिस स्थान'),
    ('āmantā', r'āmantā', r'हाँ।'),
    ('natthi', r'natthi', r'ऐसा कोई नहीं'),
    ('dve', r'\bdve\b', r'दो '),
    ('tayo', r'\btayo\b', r'तीन '),
    ('cattāro', r'\bcattāro\b', r'चार व्यक्ति'),
    ('pañca', r'\bpañca\b', r'पाँच व्यक्ति'),
    ('cha', r'\bcha\b', r'छह'),
    ('satta', r'\bsatta\b', r'सात'),
    ('aṭṭha', r'\baṭṭha\b', r'आठ व्यक्ति'),
    ('aṭṭhamaka', r'aṭṭhamak', r'आठवें'),
    ('agga', r'aggamagg', r'सर्वोच्च मार्ग'),
    ('anāgāmimagg', r'anāgāmimagg', r'फिर न लौटने के मार्ग'),
    ('anāgāmī', r'anāgāmī\b', r'फिर न लौटने वाल'),
    ('aggaphala', r'aggaphal', r'सर्वोच्च फल'),
    ('arahā', r'arahā\b|arahant', r'अर्हत्'),
    ('ṭhapetvā', r'ṭhapetvā', r'छोड़कर'),
    ('puthujjana', r'puthujjan', r'सामान्य'),
    ('sahetuka', r'sahetuk', r'मूल वाल'),
    ('ñāṇasamp', r'ñāṇasampayutt', r'ज्ञान से जुड़े'),
    ('ñāṇavipp', r'ñāṇavippayutt', r'ज्ञान से अलग|ज्ञान से रहित'),
    ('somanassa_s', r'somanassasampayutt|somanassena', r'प्रसन्नता से जुड़े|प्रसन्नता के साथ|प्रसन्नता से युक्त'),
    ('upekkhā_s', r'upekkhāsampayutt|upekkhāya', r'समभाव से जुड़े|समभाव के साथ|समभाव से युक्त'),
    ('vipp', r'vippayutt', r'से अलग|से रहित मन'),
    ('pe', r'…\s*pe\s*…', r'…'),
    ('ka', r'\(Ka\)', r'\(क\)'),
    ('kha', r'\(Kha\)', r'\(ख\)'),
]

def feats(s, idx):
    c = {}
    for name, pp, hp in FEAT:
        c[name] = len(re.findall(pp if idx == 0 else hp, s, re.I if idx == 0 else 0))
    return c

STRIP_H = ['“जो अब तक नहीं जाना उसे मैं जान लूँगा”', 'ऐसा कोई नहीं है']

def run():
    out = []
    total = 0
    for f in FILES:
        P, H = load(f)
        cur = None
        for i, (p, h) in enumerate(zip(P, H)):
            total += 1
            m = re.search(r'\^([\w-]+)\s*$', p)
            # id: next ID at or below this line
            idl = None
            for j in range(i, len(P)):
                mm = re.search(r'\^([\w-]+)\s*$', P[j])
                if mm:
                    idl = mm.group(1)
                    break
            probs = []
            pvs = pali_verbs(p)
            hvs = hindi_verbs(h)
            if pvs != hvs:
                probs.append('VERB P=%s H=%s' % (pvs, hvs))
            pi_, hi_ = pitems(p), hitems(h)
            if pi_ != hi_:
                probs.append('ITEM P=%s H=%s' % (pi_, hi_))
            fp, fh = feats(p, 0), feats(h, 1)
            d = [(k, fp[k], fh[k]) for k in fp if fp[k] != fh[k]]
            if d:
                probs.append('FEAT %s' % d)
            # stray negation in Hindi
            hh = h
            for s in STRIP_H:
                hh = hh.replace(s, '')
            nneg = len(re.findall(r'नहीं', hh)) - len(re.findall(r'\? नहीं।|^नहीं।', hh))
            vneg = sum(1 for v in hvs if v[2])
            if nneg != vneg:
                probs.append('NEGCOUNT hindi नहीं=%d verbneg=%d' % (nneg, vneg))
            if re.search(r'(?<![ऀ-ॿ])न(?![ऀ-ॣ])', hh.replace('फिर न लौटने', '')):
                probs.append('BARE-न')
            # typography
            if '–' in h or '—' in h:
                if not ('–' in p or '—' in p):
                    probs.append('DASH')
            if '"' in h or "'" in h:
                probs.append('STRAIGHTQUOTE')
            if '  ' in h:
                probs.append('DOUBLESPACE')
            if re.search(r'[A-Za-zāīūṃñṅṭḍṇ]{3,}', re.sub(r'\[[^\]]*\]', '', re.sub(r'\^[\w-]+', '', h))):
                probs.append('LATIN')
            core_p = re.sub(r'\s*(\([^)]*\))?\s*(\^[\w-]+)?\s*$', '', p).rstrip()
            core_h = re.sub(r'\s*(\([^)]*\))?\s*(\^[\w-]+)?\s*$', '', h).rstrip()
            if core_p[-1:] in '?.' and core_h[-1:] in '?।…':
                pe = core_p[-1]
                he = core_h[-1]
                if pe == '?' and he != '?' and not core_p.endswith('…pe…') :
                    probs.append('END p=%s h=%s' % (pe, he))
                if pe == '.' and he == '?':
                    probs.append('END p=%s h=%s' % (pe, he))
            nq_p = p.count('?'); nq_h = h.count('?')
            if nq_p != nq_h:
                probs.append('QCOUNT %d/%d' % (nq_p, nq_h))
            if probs:
                out.append((f, i + 1, idl, p, h, probs))
    return out, total

if __name__ == '__main__':
    res, total = run()
    with open(sys.argv[1], 'w', encoding='utf-8') as o:
        o.write('total lines %d flagged %d\n' % (total, len(res)))
        cnt = collections.Counter()
        for f, ln, idl, p, h, probs in res:
            for pr in probs:
                cnt[pr.split()[0]] += 1
        o.write(str(cnt) + '\n\n')
        for f, ln, idl, p, h, probs in res:
            o.write('== %s L%d ^%s\n P: %s\n H: %s\n' % (f, ln, idl, p, h))
            for pr in probs:
                o.write('   ! %s\n' % pr)
