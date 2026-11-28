"""r4: template grouping for pi-6 RU review (6-02, 7-01..7-05).
Usage: python r4_tpl.py <mode> [files...]
mode: tpl   -> unique Pāli sentence templates with their Russian templates (count, first line ref)
      seq   -> per line, compare member and person/place token sequences
"""
import re, sys, collections

BASE = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['6-02-sankharayamaka.md', '7-01-anusayayamaka.md', '7-02-anusayayamaka.md',
         '7-03-anusayayamaka.md', '7-04-anusayayamaka.md', '7-05-anusayayamaka.md']

def load(f):
    p = open(BASE + '\\pali\\pi-6_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    r = open(BASE + '\\russian\\pi-6-russian-plain-rails_split_chapters\\' + f, encoding='utf-8').read().split('\n')
    return p, r

AN_P = [('kāmarāg', 1), ('kāmārāg', 1), ('paṭigh', 2), ('mān', 3), ('diṭṭh', 4), ('vicikicch', 5), ('bhavarāg', 6), ('avijj', 7)]
AN_R = [('к страсти к существованию', 6), ('к чувственной страсти', 1), ('к неприязни', 2), ('к самомнению', 3),
        ('к воззрениям', 4), ('к колебанию', 5), ('к неведению', 7)]
SK_P = {'kāya': 'K', 'vacī': 'V', 'citta': 'C'}

PP_P = [(r'anāgāmissa|anāgāmī', 'NA'), (r'arahato|arahā', 'AR'), (r'puthujjanassa|puthujjano', 'PJ'),
        (r'dvinnaṃ puggalānaṃ|dve puggalā', 'D2'), (r'tiṇṇaṃ puggalānaṃ|tayo puggalā', 'T3'),
        (r'catunnaṃ puggalānaṃ|cattāro puggalā', 'C4'), (r'tesaññeva puggalānaṃ|teva puggalā', 'SP'),
        (r'tasseva puggalassa|sveva puggalo', 'SS'), (r'aṭṭhamako', 'A8'), (r'aggamaggasamaṅgī', 'AM'),
        (r'kāmadhātuyā', 'KD'), (r'arūpadhātuyā', 'AD'), (r'rūpadhātuyā', 'RD'), (r'dvīsu vedanāsu', 'V2'),
        (r'tīsu vedanāsu', 'V3'), (r'dukkhāya vedanāya', 'DV'), (r'apariyāpanne', 'AP'), (r'sabbattha', 'ALL')]
PP_R = [(r'невозвращающ\w+', 'NA'), (r'архат\w*', 'AR'), (r'обычн\w+ человек\w*', 'PJ'),
        (r'двух личностей|две личности', 'D2'), (r'трёх личностей|три личности', 'T3'),
        (r'четырёх личностей|четыре личности', 'C4'), (r'этих же личностей|эти же личности', 'SP'),
        (r'этой же личности|эта же личность', 'SS'), (r'личност\w+ восьмой ступени', 'A8'),
        (r'обладающ\w+ высшим путём', 'AM'),
        (r'в мире чувственных желаний', 'KD'), (r'в мире без форм', 'AD'), (r'в мире форм', 'RD'),
        (r'в двух видах чувства', 'V2'), (r'в трёх видах чувства', 'V3'), (r'в болезненном чувстве', 'DV'),
        (r'в том, что не принадлежит к кругам существования', 'AP'), (r'нигде|везде', 'ALL')]
PLACES = {'KD', 'AD', 'RD', 'V2', 'V3', 'DV', 'AP'}

def tok_pp(s, table, seq, flags):
    pat = '|'.join('(?P<g%d>%s)' % (i, p) for i, (p, _) in enumerate(table))
    def rep(m):
        for i, (_, t) in enumerate(table):
            if m.group('g%d' % i):
                seq.append(t)
                return '#' + ('PL' if t in PLACES else t)
    s = re.sub(r'\b(?:%s)\b' % pat, rep, s, flags=flags)
    s = re.sub(r'#PL(?:(?:,? и |, | )#PL)+', '#PL', s)
    return s

def pali_norm(s):
    seq, pseq = [], []
    def an(m):
        for k, n in AN_P:
            if m.group(1).lower() == k:
                seq.append(n)
        return 'A_' + m.group(2)
    s = re.sub(r'(kāmarāg|kāmārāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay(\w*)', an, s, flags=re.I)
    def sk(m):
        seq.append(SK_P[m.group(1).lower()])
        return 'S_' + m.group(2)
    s = re.sub(r'(kāya|vacī|citta)saṅkhār(\w*)', sk, s, flags=re.I)
    s = re.sub(r'(?:A_(\w+) ca ){2,}', lambda m: 'A+_' + m.group(1) + ' ca ', s)
    s = tok_pp(s, PP_P, pseq, re.I)
    return s, seq, pseq

RU_AN = '|'.join(re.escape(k) for k, _ in AN_R)
def ru_norm(s):
    seq, pseq = [], []
    def an(m):
        seq.append(dict(AN_R)[m.group(0)])
        return '@'
    s = re.sub(RU_AN, an, s)
    def sk(m):
        t = m.group(0).lower()
        seq.append('K' if t.startswith('телесн') else 'V' if t.startswith('речев') else 'C')
        return 'S'
    s = re.sub(r'телесн\w+ формирующ\w+ фактор\w*|речев\w+ формирующ\w+ фактор\w*|формирующ\w+ фактор\w* ума', sk, s, flags=re.I)
    s = re.sub(r'@(?:, @)*(?: и @)', '@+', s)
    s = tok_pp(s, PP_R, pseq, re.I)
    return s, seq, pseq

def sentences(s):
    s = re.sub(r'\s*\^[\w-]+\s*$', '', s)
    parts = re.split(r'(?<=[.?!])\s+(?=[A-ZĀĪŪṄÑṬḌṆḶṂ(А-ЯЁ«#])', s)
    return [x for x in parts if x.strip()]

def main():
    mode = sys.argv[1]
    files = sys.argv[2:] or FILES
    if mode == 'tpl':
        d = collections.defaultdict(collections.Counter)
        first = {}
        for f in files:
            p, r = load(f)
            for i, (a, b) in enumerate(zip(p, r)):
                if not a.strip() or a.startswith('#'):
                    continue
                pa = pali_norm(a)[0]; rb = ru_norm(b)[0]
                ps, rs = sentences(pa), sentences(rb)
                if len(ps) != len(rs):
                    print('SENTCOUNT', f, i + 1, len(ps), len(rs))
                    ps, rs = [' '.join(ps)], [' '.join(rs)]
                for x, y in zip(ps, rs):
                    d[x][y] += 1
                    first.setdefault((x, y), f'{f[:4]}:{i+1}')
        for x in sorted(d, key=lambda k: -sum(d[k].values())):
            print('P', sum(d[x].values()), x)
            for y, n in d[x].most_common():
                print('   R', n, first[(x, y)], y)
    elif mode == 'seq':
        bad = 0
        for f in files:
            p, r = load(f)
            for i, (a, b) in enumerate(zip(p, r)):
                if not a.strip():
                    continue
                _, s1, q1 = pali_norm(a); _, s2, q2 = ru_norm(b)
                if s1 != s2 or q1 != q2:
                    bad += 1
                    print('SEQ', f, i + 1, s1 if s1 != s2 else '', s2 if s1 != s2 else '', q1 if q1 != q2 else '', q2 if q1 != q2 else '')
        print('seq mismatches', bad)

main()
