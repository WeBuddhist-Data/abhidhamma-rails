import sys, re
from collections import Counter
sys.path.insert(0, 'D:/Work/OpenPecha/abhidhamma-rails/0-INBOX/temp/pipeline/pi-6-vi-ai/review')
from r1_check import load, PDIR, VDIR, FILES, PV
from r1_ts import load_ts

# console-only comparison of answer categories and "no ca" polarity


def p_answers(text):
    out = []
    for m in re.finditer(r'\?\s*(Āmantā|No|Natthi|Uppajjati|Uppajjittha|Uppajjissati|Nirujjhati|Nirujjhittha|Nirujjhissati)\b', text):
        out.append(m.group(1))
    return out


def p_nocapol(text):
    out = []
    for m in re.finditer(r'\bno ca\b([^,.]*?)(\bna |\bn)?(uppajj|nirujjh|parijān)(\w+)', text):
        neg = bool(m.group(2))
        out.append('pos' if neg else 'neg')
    return out


TSANS = [
    ('Āmantā', r'Phải rồi|Đúng rồi|Phải vậy'),
    ('Natthi', r'Không có'),
    ('No', r'Không phải|Chẳng phải|Không\b'),
]


def ts_answers(text):
    out = []
    for m in re.finditer(r'\?\s*([^.?…]{0,25})', text):
        a = m.group(1).strip()
        if not a:
            continue
        cat = None
        for k, rx in TSANS:
            if re.match(rx, a):
                cat = k
                break
        if cat is None:
            if re.match(r'(Đang|Có|Vẫn)?\s*(sanh|diệt)', a, re.I) and len(a.split()) <= 3:
                cat = 'X-pres'
            elif re.match(r'(Từng|Đã)\s*(sanh|diệt)', a, re.I) and len(a.split()) <= 3:
                cat = 'X-past'
            elif re.match(r'Sẽ\s*(sanh|diệt)', a, re.I) and len(a.split()) <= 3:
                cat = 'X-fut'
        if cat:
            out.append(cat)
    return out


def norm_p(a):
    return {'Uppajjati': 'X-pres', 'Nirujjhati': 'X-pres', 'Uppajjittha': 'X-past', 'Nirujjhittha': 'X-past',
            'Uppajjissati': 'X-fut', 'Nirujjhissati': 'X-fut'}.get(a, a)


def ts_nocapol(text):
    out = []
    for m in re.finditer(r'\bmà\b([^.]*?)(?=\.|,|$| với| cõi| đối)', text):
        c = m.group(1)
        if not re.search(r'sanh|diệt|biết|thấu|đắc', c):
            continue
        out.append('neg' if re.search(r'chẳng|không|chưa', c) else 'pos')
    return out


files = sys.argv[1:] or FILES
T = load_ts()
stats = Counter()
for f in files:
    P, _ = load(PDIR + f)
    for sid, pl in P.items():
        if sid not in T:
            stats['ts-missing'] += 1
            print('TS missing', f, sid)
            continue
        pt = ' '.join(pl)
        tt = ' '.join(T[sid])
        pa = [norm_p(x) for x in p_answers(pt)]
        ta = ts_answers(tt)
        stats['segs'] += 1
        if pa != ta:
            # report only category disagreements where both have items at same position
            diff = [(i, x, y) for i, (x, y) in enumerate(zip(pa, ta)) if x != y]
            if diff or len(pa) != len(ta):
                stats['ans-diff'] += 1
                print('ANS %s %s P=%s TS=%s' % (f, sid, pa, ta))
        pn = p_nocapol(pt)
        tn = ts_nocapol(tt)
        if len(pn) == len(tn) and pn != tn:
            stats['pol-diff'] += 1
            print('POL %s %s P=%s TS=%s' % (f, sid, pn, tn))
        elif len(pn) != len(tn):
            stats['pol-count'] += 1
print(stats)
