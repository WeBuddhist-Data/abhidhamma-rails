"""r8: checks for pi-6 RU review, 10-05..10-13 indriyayamaka.
Usage: python r8_check.py <mode> [args]
 mode: struct | members | tense | neg | tpl | show <file> <from> <to> | typo | vocab
"""
import re, sys, collections

BASE = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['10-%02d-indriyayamaka.md' % i for i in range(5, 14)]

def load(f):
    p = open(BASE + '\\pali\\pi-6_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    r = open(BASE + '\\russian\\pi-6-russian-plain-rails_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    return p, r

# Pāli indriya stems -> code
P_IND = [
    ('anaññātaññassāmītindriy', 'AN'), ('aññātāvindriy', 'AV'), ('aññindriy', 'AÑ'),
    ('cakkhundriy', 'CK'), ('sotindriy', 'SO'), ('ghānindriy', 'GH'), ('jivhindriy', 'JI'),
    ('kāyindriy', 'KA'), ('manindriy', 'MA'), ('itthindriy', 'IT'), ('purisindriy', 'PU'),
    ('jīvitindriy', 'JV'), ('sukhindriy', 'SU'), ('dukkhindriy', 'DU'),
    ('somanassindriy', 'SM'), ('domanassindriy', 'DM'), ('upekkhindriy', 'UP'),
    ('saddhindriy', 'SA'), ('vīriyindriy', 'VI'), ('satindriy', 'ST'), ('samādhindriy', 'SD'),
    ('paññindriy', 'PA'),
]
R_IND = [
    ('способност\\w* познания непознанного', 'AN'),
    ('способност\\w* обладателя окончательного знания', 'AV'),
    ('способност\\w* окончательного знания', 'AÑ'),
    ('способност\\w* глаза', 'CK'), ('способност\\w* уха', 'SO'), ('способност\\w* носа', 'GH'),
    ('способност\\w* языка', 'JI'), ('способност\\w* тела', 'KA'), ('способност\\w* ума', 'MA'),
    ('способност\\w* женственности', 'IT'), ('способност\\w* мужественности', 'PU'),
    ('жизненн\\w* способност\\w*', 'JV'), ('способност\\w* счастья', 'SU'), ('способност\\w* боли', 'DU'),
    ('способност\\w* радости', 'SM'), ('способност\\w* уныния', 'DM'),
    ('способност\\w* невозмутимости', 'UP'), ('способност\\w* веры', 'SA'),
    ('способност\\w* усердия', 'VI'), ('способност\\w* осознанности', 'ST'),
    ('способност\\w* сосредоточения', 'SD'), ('способност\\w* мудрости', 'PA'),
]
P_RE = re.compile('|'.join('(%s\\w*)' % s for s, _ in P_IND), re.I)
R_RE = re.compile('|'.join('(%s)' % s for s, _ in R_IND), re.I)

def p_members(s):
    out = []
    for m in P_RE.finditer(s):
        out.append(P_IND[m.lastindex - 1][1])
    return out

def r_members(s):
    out = []
    for m in R_RE.finditer(s):
        out.append(R_IND[m.lastindex - 1][1])
    return out

def p_tpl(s):
    s = P_RE.sub(lambda m: '<' + P_IND[m.lastindex - 1][1] + '>', s)
    return s

def r_tpl(s):
    return R_RE.sub(lambda m: '<' + R_IND[m.lastindex - 1][1] + '>', s)

# tense
def p_tense(s):
    out = []
    for m in re.finditer(r'(?:uppajj|upapajj|nirujjh|parijān|pajah|pajjah|bhāv|sacchikar|sacchākāsi)\w*', s, re.I):
        w = m.group(0).lower()
        if w.startswith('upapajj') or w.startswith('bhāvena'):
            continue  # person-group participle
        if w=='sacchākāsi':
            out.append('P'); continue
        if 'issa' in w or 'essa' in w:
            out.append('F')
        elif 'ittha' in w or 'itth' in w or w.endswith('iṃsu') or w.endswith('esi') or w.endswith('ayittha'):
            out.append('P')
        else:
            out.append('N')
    return out

def r_tense(s):
    out = []
    for m in re.finditer(r'(?:возни\w*|возник\w*|прекрат\w*|прекращ\w*|понима\w*|понял\w*|поймёт|поймут|понимал\w*|устран\w*|разви\w*|развив\w*|разовь\w*|осуществ\w*|осуществл\w*)', s, re.I):
        w = m.group(0).lower()
        if w.startswith('возникнов') or w.startswith('прекращени') or w.startswith('развити') or w.startswith('устранени') or w.startswith('осуществлени') or w.startswith('понимани'):
            continue
        if re.match(r'(возникнет|возникнут|поймёт|поймут|устранит|устранят|разовьёт|разовьют|осуществит|осуществят|будет|прекратит)', w):
            out.append('F')
        elif re.match(r'(возникал|возникла|возник$|понимал|понял|устранил|развил|осуществил|устранял|развивал|осуществлял|прекращал)', w):
            out.append('P')
        elif re.match(r'(возникает|возникают|понимает|понимают|устраняет|устраняют|развивает|развивают|осуществляет|осуществляют|прекращает)', w):
            out.append('N')
        else:
            out.append('?' + w)
    return out

def p_neg_expected(s):
    """expected Russian neg count per line."""
    total = 0
    for sent in re.split(r'(?<=[.?])\s+', s):
        parts = re.split(r',?\s*\bno ca\b', sent)
        n0 = len(re.findall(r'\bna\b|\bnuppajj|\bnappajah|\bnanirujjh', parts[0]))
        total += n0
        for q in parts[1:]:
            n = len(re.findall(r'\bna\b|\bnuppajj|\bnappajah|\bnanirujjh', q))
            total += (1 - n) if n <= 1 else n
    return total

def r_neg(s):
    n = len(re.findall(r'(?<![а-яё])(не|ни)(?![а-яё])', s, re.I))
    n -= len(re.findall(r'(?<![а-яё])не (?:[а-яё]+ ){1,3}?ни(?![а-яё])', s, re.I))
    return n

def lines():
    for f in FILES:
        p, r = load(f)
        if len(p) != len(r):
            print('LINECOUNT', f, len(p), len(r))
        for i, (a, b) in enumerate(zip(p, r)):
            yield f, i + 1, a, b

def main():
    mode = sys.argv[1]
    if mode == 'show':
        p, r = load(sys.argv[2])
        for i in range(int(sys.argv[3]) - 1, int(sys.argv[4])):
            if p[i].strip():
                print(i + 1, 'P', p[i]); print(i + 1, 'R', r[i])
        return
    bad = 0; n = 0
    seen_ids = 0
    for f, i, a, b in lines():
        if not a.strip() and not b.strip():
            continue
        n += 1
        if mode == 'struct':
            ia = re.findall(r'\^[\w-]+\s*$', a); ib = re.findall(r'\^[\w-]+\s*$', b)
            if ia != ib or bool(a.strip()) != bool(b.strip()):
                print('ID', f, i, ia, ib); bad += 1
            if ia: seen_ids += 1
        elif mode == 'members':
            if a.startswith('#'): continue
            if p_members(a) != r_members(b):
                bad += 1; print('MEM', f, i, ' '.join(p_members(a)), '|', ' '.join(r_members(b)))
        elif mode == 'tense':
            if a.startswith('#'): continue
            t1, t2 = p_tense(a), r_tense(b)
            dd=lambda t:[x for k,x in enumerate(t) if k==0 or t[k-1]!=x]
            if dd(t1) != dd(t2):
                bad += 1; print('TENSE', f, i, ''.join(t1), ''.join(t2))
        elif mode == 'neg':
            if a.startswith('#'): continue
            e, g = p_neg_expected(a), r_neg(b)
            if e != g:
                bad += 1; print('NEG', f, i, e, g)
        elif mode == 'typo':
            if b.count('–') + b.count('—') != a.count('–') + a.count('—'):
                print('DASH', f, i); bad += 1
            if re.search(r'(?<![а-яё])ли(?![а-яё])', b): print('LI', f, i); bad += 1
            if re.search(r'[A-Za-zāīūṃṅñṭḍṇḷ]{3,}', re.sub(r'\[[^\]]*\]', '', b)): print('LAT', f, i, b[:80]); bad += 1
            if '"' in b: print('QUOTE', f, i); bad += 1
            if b.rstrip().endswith('?') != a.rstrip().endswith('?') and not a.startswith('#'):
                print('QEND', f, i); bad += 1
            if '  ' in b: print('DBLSPACE', f, i); bad += 1
    if mode == 'struct':
        print('segments(ids)', seen_ids)
    print(mode, 'lines', n, 'flags', bad)

if __name__ == '__main__':
    if sys.argv[1] == 'tpl':
        d = collections.defaultdict(collections.Counter); first = {}
        for f, i, a, b in lines():
            if not a.strip() or a.startswith('#'): continue
            a2 = re.sub(r'\s*\^[\w-]+\s*$', '', a); b2 = re.sub(r'\s*\^[\w-]+\s*$', '', b)
            ps = re.split(r'(?<=[.?])\s+', p_tpl(a2)); rs = re.split(r'(?<=[.?])\s+', r_tpl(b2))
            if len(ps) != len(rs):
                print('SENTCOUNT', f, i, len(ps), len(rs)); ps, rs = [p_tpl(a2)], [r_tpl(b2)]
            for x, y in zip(ps, rs):
                # generalise members to X
                x2 = re.sub(r'<\w+>', 'X', x); y2 = re.sub(r'<\w+>', 'X', y)
                d[x2][y2] += 1; first.setdefault((x2, y2), '%s:%d' % (f[:5], i))
        for x in sorted(d, key=lambda k: -sum(d[k].values())):
            print('P', sum(d[x].values()), x)
            for y, c in d[x].most_common():
                print('   R', c, first[(x, y)], y)
    else:
        main()
