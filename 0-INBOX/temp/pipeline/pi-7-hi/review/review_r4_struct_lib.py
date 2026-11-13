import re, sys, os, collections
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
PA = ROOT + r'\pali\pi-7_split_chapters'
HI = ROOT + r'\hindi\pi-7-hindi-plain-rails_split_chapters'
FILES = ['2-09-hinattika.md', '2-10-micchattaniyatattika.md', '2-11-maggarammanattika.md',
         '2-12-uppannattika.md', '2-13-atitattika.md', '2-14-atitarammanattika.md',
         '2-15-ajjhattattika.md', '2-16-ajjhattarammanattika.md', '2-17-sanidassanasappatighattika.md']

def load(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    return raw

def nonempty(raw):
    out = []
    for i, l in enumerate(raw.split('\n')):
        if l.strip():
            out.append((i + 1, l.rstrip('\r')))
    return out

PNUM = {'eka': 1, 'ekaṃ': 1, 'eko': 1, 'ekā': 1, 'ekassa': 1, 'ekaṃ,': 1,
        'dve': 2, 'dvinnaṃ': 2, 'dvīhi': 2,
        'tayo': 3, 'tīṇi': 3, 'tiṇṇannaṃ': 3, 'tiṇṇaṃ': 3, 'tisso': 3, 'tīhi': 3,
        'cattāro': 4, 'cattāri': 4, 'catunnaṃ': 4,
        'pañca': 5, 'cha': 6, 'satta': 7, 'aṭṭha': 8, 'nava': 9, 'dasa': 10,
        'ekādasa': 11, 'dvādasa': 12, 'terasa': 13, 'cuddasa': 14, 'pannarasa': 15,
        'soḷasa': 16, 'sattarasa': 17, 'aṭṭhārasa': 18, 'ekūnavīsati': 19, 'vīsati': 20,
        'ekavīsati': 21, 'bāvīsati': 22, 'tevīsati': 23, 'catuvīsati': 24, 'pañcavīsati': 25,
        'chabbīsati': 26, 'sattavīsati': 27, 'aṭṭhavīsati': 28, 'ekūnatiṃsa': 29, 'tiṃsa': 30}
HNUM = {'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पाँच': 5, 'छह': 6, 'सात': 7, 'आठ': 8, 'नौ': 9,
        'दस': 10, 'ग्यारह': 11, 'बारह': 12, 'तेरह': 13, 'चौदह': 14, 'पंद्रह': 15, 'सोलह': 16,
        'सत्रह': 17, 'अठारह': 18, 'उन्नीस': 19, 'बीस': 20, 'इक्कीस': 21, 'बाईस': 22, 'तेईस': 23,
        'चौबीस': 24, 'पच्चीस': 25, 'छब्बीस': 26, 'सत्ताईस': 27, 'अट्ठाईस': 28, 'उनतीस': 29, 'तीस': 30}

PPRE = [('ekavīsa', 21), ('bāvīsa', 22), ('tevīsa', 23), ('catuvīsa', 24), ('pañcavīsa', 25),
        ('pañcaviññāṇ', 5), ('pañcavokār', 5), ('catuvokār', 4), ('ekavokār', 1), ('dvipañca', 10)]

def pnums(s):
    toks = re.findall(r"[a-zA-Zāīūṃṅñṭḍṇḷ]+", s)
    out = []
    for t in toks:
        tl = t.lower()
        if tl in PNUM:
            out.append(PNUM[tl]); continue
        for k, v in PPRE:
            if tl.startswith(k):
                out.append(v); break
        else:
            if tl.endswith('dukaṃ') or tl.endswith('duka'):
                out.append(2)
            elif tl.endswith('ttikaṃ') or tl.endswith('tikaṃ'):
                out.append(3)
    return out

def hnums(s):
    toks = re.findall(r"[\u0900-\u0963\u0966-\u097F]+", s)
    return [HNUM[t] for t in toks if t in HNUM]

def blockid(l):
    m = re.search(r'\^(\S+)\s*$', l)
    return m.group(1) if m else None

LAT = re.compile(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}')

def strip_brackets(h):
    return re.sub(r'\[पाठभेद[^\]]*\]', '', re.sub(r'\[वर्तनी[^\]]*\]', '', h))

