import re, sys, collections

ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['1-02-vedanattika.md', '1-03-vipakattika.md', '1-04-upadinnattika.md', '1-05-sankilitthattika.md']

def load(f):
    p = open(ROOT + '\\pali\\pi-7_split_chapters\\' + f, encoding='utf8').read().split('\n')
    h = open(ROOT + '\\hindi\\pi-7-hindi-plain-rails_split_chapters\\' + f, encoding='utf8').read().split('\n')
    return p, h

ID_RE = re.compile(r'\s\^([\w-]+)\s*$')

# ---------- conditions ----------
CONDS = ['hetu', 'ārammaṇa', 'adhipati', 'anantara', 'samanantara', 'sahajāta', 'aññamañña', 'nissaya',
         'upanissaya', 'purejāta', 'pacchājāta', 'āsevana', 'kamma', 'vipāka', 'āhāra', 'indriya', 'jhāna',
         'magga', 'sampayutta', 'vippayutta', 'atthi', 'natthi', 'vigata', 'avigata']
LOC = {'hetu': 'hetuyā', 'ārammaṇa': 'ārammaṇe', 'adhipati': 'adhipatiyā', 'anantara': 'anantare',
       'samanantara': 'samanantare', 'sahajāta': 'sahajāte', 'aññamañña': 'aññamaññe', 'nissaya': 'nissaye',
       'upanissaya': 'upanissaye', 'purejāta': 'purejāte', 'pacchājāta': 'pacchājāte', 'āsevana': 'āsevane',
       'kamma': 'kamme', 'vipāka': 'vipāke', 'āhāra': 'āhāre', 'indriya': 'indriye', 'jhāna': 'jhāne',
       'magga': 'magge', 'sampayutta': 'sampayutte', 'vippayutta': 'vippayutte', 'atthi': 'atthiyā',
       'natthi': 'natthiyā', 'vigata': 'vigate', 'avigata': 'avigate'}
HI = {'hetu': 'मूल-कारण', 'ārammaṇa': 'विषय-कारण', 'adhipati': 'प्रधानता-कारण', 'anantara': 'निकटता-कारण',
      'samanantara': 'पूर्ण निकटता-कारण', 'sahajāta': 'सह-उत्पत्ति-कारण', 'aññamañña': 'परस्पर-कारण',
      'nissaya': 'आश्रय-कारण', 'upanissaya': 'प्रबल आश्रय-कारण', 'purejāta': 'पूर्व-उत्पत्ति-कारण',
      'pacchājāta': 'पश्चात्-उत्पत्ति-कारण', 'āsevana': 'पुनरावृत्ति-कारण', 'kamma': 'कर्म-कारण',
      'vipāka': 'कर्म-फल-कारण', 'āhāra': 'आहार-कारण', 'indriya': 'क्षमता-कारण', 'jhāna': 'ध्यान-कारण',
      'magga': 'मार्ग-कारण', 'sampayutta': 'जुड़ाव-कारण', 'vippayutta': 'अलगाव-कारण',
      'atthi': 'उपस्थिति-कारण', 'natthi': 'अनुपस्थिति-कारण', 'vigata': 'विलीनता-कारण',
      'avigata': 'अविलीनता-कारण'}
HI_REV = {v: k for k, v in HI.items()}
HI_RE = re.compile('|'.join(sorted(map(re.escape, HI.values()), key=len, reverse=True)))

NUM_P = {'ekaṃ': 1, 'eko': 1, 'ekā': 1, 'ekassa': 1, 'dve': 2, 'dvinnaṃ': 2, 'tayo': 3, 'tīṇi': 3,
         'tiṇṇannaṃ': 3, 'tisso': 3, 'cattāri': 4, 'pañca': 5, 'pañcannaṃ': 5, 'cha': 6, 'satta': 7,
         'aṭṭha': 8, 'nava': 9, 'dasa': 10, 'ekādasa': 11, 'dvādasa': 12, 'terasa': 13, 'cuddasa': 14,
         'pannarasa': 15, 'soḷasa': 16, 'sattarasa': 17, 'aṭṭhārasa': 18, 'ekūnavīsati': 19,
         'vīsati': 20, 'bāvīsati': 22, 'tevīsa': 23, 'tevīsati': 23, 'catuvīsati': 24,
         'tayokhandhā': 3}
NUM_H = {'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पाँच': 5, 'छह': 6, 'सात': 7, 'आठ': 8, 'नौ': 9, 'दस': 10,
         'ग्यारह': 11, 'बारह': 12, 'तेरह': 13, 'चौदह': 14, 'पंद्रह': 15, 'सोलह': 16, 'सत्रह': 17,
         'अठारह': 18, 'उन्नीस': 19, 'बीस': 20, 'इक्कीस': 21, 'बाईस': 22, 'तेईस': 23, 'चौबीस': 24,
         'दोनों': 2, 'तीनों': 3}

def pnum(tok):
    t = tok.lower()
    if t in NUM_P:
        return NUM_P[t]
    if t.startswith('catuviññāṇa'): return 4
    if t.startswith('pañcaviññāṇa'): return 5
    for suf, n in (('dukaṃ', 2), ('dukāni', 2), ('ttikaṃ', 3), ('ttikassa', 3), ('ttike', 3), ('tikaṃ', 3),
                   ('catukkaṃ', 4), ('pañcakaṃ', 5), ('chakkaṃ', 6), ('sattakaṃ', 7), ('aṭṭhakaṃ', 8),
                   ('navakaṃ', 9), ('ekādasakaṃ', 11), ('dasakaṃ', 10), ('tevīsakaṃ', 23), ('catuvīsakaṃ', 24)):
        if t.endswith(suf):
            if suf == 'dasakaṃ' and t.endswith('ekādasakaṃ'):
                continue
            return n
    return None

PTOK = re.compile(r"[^\s,.;:()…–—?“”\"'‘’\[\]{}^*#!=-]+")
HTOK = re.compile(r"[^\s,.;:()…–—?“”\"'‘’\[\]{}^*#!।]+")

COND_TOK = re.compile(r'^(no|na|nā)?(' + '|'.join(sorted(CONDS, key=len, reverse=True)) + r')(paccay\w*)$')
LOC_REV = {v: k for k, v in LOC.items()}
LOC_TOK = re.compile(r'^(no|na)?(' + '|'.join(sorted(map(re.escape, LOC.values()), key=len, reverse=True)) + r')$')

def strip_variants(s):
    return re.sub(r'\{[^}]*\}', ' ', s)

def strip_variants_h(s):
    return re.sub(r'\[(पाठभेद|वर्तनी-भेद)[^\]]*\]', ' ', s)

STEMS = '|'.join(sorted(CONDS, key=len, reverse=True))
BARE_TOK = re.compile(r'^(no|na|nā)?(' + STEMS + r')(dukaṃ|dukāni|ādidukāni|mūlakaṃ|ādi|nti|ā|aṃ|ṃ|anti|o)?$')
SUFFIX_TOK = re.compile(r'^(no|na|nā)?(' + STEMS + r')(dukaṃ|dukāni|ādidukāni|mūlakaṃ|ādi)$')

def pali_conds(s):
    s = strip_variants(s)
    heading = s.startswith('#')
    chain_words = set()
    for ch in re.findall(r"[^\s,.;:()…–—?“”\"'‘’\[\]{}^*#!=]+(?:-[^\s,.;:()…–—?“”\"'‘’\[\]{}^*#!=-]+)+", s):
        for w in ch.split('-'):
            chain_words.add(w.lower())
    toks = PTOK.findall(s)
    out = []
    for i, t in enumerate(toks):
        tl = t.lower()
        m = COND_TOK.match(tl)
        if m:
            out.append((m.group(2), 'N' if m.group(1) else 'P'))
            continue
        m = SUFFIX_TOK.match(tl)
        if m or ((heading or tl in chain_words) and BARE_TOK.match(tl)):
            m = m or BARE_TOK.match(tl)
            out.append((m.group(2), 'N' if m.group(1) else 'P'))
            continue
        m = LOC_TOK.match(tl)
        if m and i + 1 < len(toks) and pnum(toks[i + 1]) is not None:
            out.append((LOC_REV[m.group(2)], 'N' if m.group(1) else 'P'))
    return out

def hindi_conds(s):
    s = strip_variants_h(s)
    out = []
    for m in HI_RE.finditer(s):
        after = s[m.end():m.end() + 14]
        neg = after.startswith(' के बिना') or after.startswith(' के अभाव') or after.startswith(' का अभाव') \
            or after.startswith(' न होने')
        out.append((HI_REV[m.group(0)], 'N' if neg else 'P'))
    return out

def pali_nums(s):
    s = strip_variants(ID_RE.sub('', s))
    return [n for n in (pnum(t) for t in PTOK.findall(s)) if n is not None]

def hindi_nums(s):
    s = strip_variants_h(ID_RE.sub('', s))
    return [NUM_H[t] for t in HTOK.findall(s) if t in NUM_H]

def digits(s, h=False):
    s = ID_RE.sub('', s)
    s = strip_variants_h(s) if h else strip_variants(s)
    return re.findall(r'\d+(?:-\d+)?', s)

# ---------- items ----------
ITEMS_P = {
    '1-02': [('A', r'adukkhamasukhāya'), ('S', r'sukhāya'), ('D', r'dukkhāya'),
             ('s', r'sukhasahagat'), ('d', r'dukkhasahagat')],
    '1-03': [('N', r'nevavipākanavipākadhammadhamm'), ('VD', r'vipākadhammadhamm'),
             ('V', r'vipāk(?!apaccay|adhammadhamm|e (?:ekaṃ|dve|tīṇi|cattāri|pañca|cha|satta|aṭṭha|nava|dasa))')],
    '1-04': [('AA', r'anupādinnaanupādāniy'), ('AU', r'anupādinnupādāniy'), ('U', r'upādinnupādāniy')],
    '1-05': [('AA', r'asaṃkiliṭṭhaasaṃkilesik'), ('AS', r'asa[ṃṅ]kiliṭṭhasaṃkil[ei]sik'), ('S', r'saṃkiliṭṭhasaṃkilesik')],
}
ITEMS_H = {
    '1-02': [('A', r'न दुःखद न सुखद'), ('S', r'सुखद'), ('D', r'दुःखद'),
             ('s', r'सुख के साथ'), ('d', r'दुःख के साथ')],
    '1-03': [('N', r'न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वा'), ('VD', r'कर्म-फल उत्पन्न करने वा'),
             ('V', r'कर्म-फल रूपी')],
    '1-04': [('AA', r'न कर्म से उत्पन्न न आसक्ति का विषय बनने वा'),
             ('AU', r'कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वा'),
             ('U', r'कर्म से उत्पन्न और आसक्ति का विषय बनने वा')],
    '1-05': [('AA', r'क्लेशों से मलिन न होने वा(?:ली|ले|ला) और क्लेशों का विषय न बनने वा'),
             ('AS', r'क्लेशों से मलिन न होने वा(?:ली|ले|ला) पर क्लेशों का विषय बनने वा'),
             ('S', r'क्लेशों से मलिन और क्लेशों का विषय बनने वा')],
}

def items(s, table, lower=False):
    rx = re.compile('|'.join('(?P<%s>%s)' % (('g%d' % i), p) for i, (k, p) in enumerate(table)))
    keys = [k for k, p in table]
    if lower:
        s = s.lower()
    return [keys[int(m.lastgroup[1:])] for m in rx.finditer(s)]

def plain(s):
    return ID_RE.sub('', s).strip()

def main():
    want = sys.argv[1] if len(sys.argv) > 1 else 'all'
    seg_total = 0
    for f in FILES:
        key = f[:4]
        p, h = load(f)
        pn = [(i + 1, l) for i, l in enumerate(p) if l.strip()]
        hn = [(i + 1, l) for i, l in enumerate(h) if l.strip()]
        print('=====', f, 'nonempty', len(pn), len(hn), 'physical', len(p), len(h))
        if len(pn) != len(hn):
            print('LINECOUNT MISMATCH')
        # blank-line structure
        if [bool(x.strip()) for x in p] != [bool(x.strip()) for x in h]:
            print('BLANK STRUCTURE DIFFERS')
        for a, b in zip(p, p[1:]):
            pass
        hb = ''.join('1' if x.strip() else '0' for x in h)
        if '00' in hb.strip('0'):
            print('DOUBLE BLANK in hindi')
        segs = 0
        for k, ((pl, ps), (hl, hs)) in enumerate(zip(pn, hn), 1):
            pid = ID_RE.search(ps); hid = ID_RE.search(hs)
            pid = pid.group(1) if pid else None; hid = hid.group(1) if hid else None
            if pid and not pid.endswith('-0'):
                segs += 1
            tag = '%s L%d(%s) ' % (f[:4], k, pid or '')
            out = []
            if pid != hid:
                out.append('ID %s vs %s' % (pid, hid))
            if len(re.match(r'#*', ps).group(0)) != len(re.match(r'#*', hs).group(0)):
                out.append('HEADING LEVEL')
            if want in ('all', 'cond'):
                pc = pali_conds(ps); hc = hindi_conds(hs)
                if pc != hc:
                    out.append('COND P=%s | H=%s' % (' '.join(c + ('-' if n == 'N' else '') for c, n in pc),
                                                    ' '.join(c + ('-' if n == 'N' else '') for c, n in hc)))
            if want in ('all', 'num'):
                a = pali_nums(ps); b = hindi_nums(hs)
                if a != b:
                    out.append('NUM P=%s | H=%s' % (a, b))
                if digits(ps) != digits(hs, True):
                    out.append('DIGITS P=%s | H=%s' % (digits(ps), digits(hs, True)))
            if want in ('all', 'item'):
                a = items(strip_variants(ps), ITEMS_P[key], True); b = items(strip_variants_h(hs), ITEMS_H[key])
                if a != b:
                    flag = 'ITEMORDER' if sorted(a) == sorted(b) else 'ITEM'
                    out.append('%s P=%s | H=%s' % (flag, a, b))
            if want in ('all', 'typo'):
                pd = len(re.findall('[–—]', ps)); hd = len(re.findall('[–—]', hs))
                if pd != hd:
                    out.append('DASH P%d H%d' % (pd, hd))
                if re.search(r'[-–—]\s*$', plain(hs)) or '--' in hs:
                    out.append('DASH-END')
                if '"' in hs or "'" in hs or '‘' in hs:
                    out.append('STRAIGHT/SINGLE QUOTE')
                pe = plain(strip_variants(ps)).replace('…pe…', '…')
                pe = pe.replace('……', '…')
                he = plain(hs)
                if pe.count('…') != he.count('…'):
                    out.append('ELLIPSIS P%d H%d' % (pe.count('…'), he.count('…')))
                lat = re.sub(r'\[(पाठभेद|वर्तनी-भेद)[^\]]*\]', '', he)
                if re.search(r'[A-Za-zāīūṃṅñṭḍṇḷ]', lat):
                    out.append('LATIN')
                if not hs.startswith('#'):
                    body = re.sub(r'\s*\(\d+\)\s*$', '', he).rstrip()
                    if not (body.endswith('।') or body.endswith('?') or body.endswith('।)') or body.endswith('?)')
                            or body.endswith('…') or body.endswith('”')):
                        out.append('END "%s"' % body[-6:])
                    if body.endswith('?') != ('uppajjeyya' in ps or ps.rstrip().rstrip('^').find('?') >= 0):
                        if body.endswith('?') or 'uppajjeyya' in ps:
                            out.append('QMARK P? %s H? %s' % ('uppajjeyya' in ps, body.endswith('?')))
                    if re.search(r'।\s*।|\.\s*।|।\.', he):
                        out.append('DOUBLE STOP')
                    if re.search(r'\s[,;।]', he):
                        out.append('SPACE BEFORE PUNCT')
                    if '  ' in hs:
                        out.append('DOUBLE SPACE')
                pu = ps.count('uppajjanti'); hu = len(re.findall(r'होती हैं|होते हैं', hs))
                pu1 = len(re.findall(r'uppajjati\b', ps)); hu1 = len(re.findall(r'होती है(?!ं)|होता है(?!ं)', hs))
                if pu != hu:
                    out.append('PLURAL-VERB P%d H%d' % (pu, hu))
            for o in out:
                print(tag + o)
        print('segments', segs)
        seg_total += segs
    print('TOTAL segments', seg_total)

main()
