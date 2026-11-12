import re, sys, unicodedata
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
CHS = sys.argv[1:] or ['2-ayatanavibhango', '3-dhatuvibhango', '4-saccavibhango', '5-indriyavibhango', '7-satipatthanavibhango']

PNUM = [  # (regex at word start, value)
    ('aṭṭhāras', 18), ('sattaras', 17), ('soḷas', 16), ('pannaras', 15), ('cuddas', 14), ('teras', 13),
    ('bāvīsat', 22), ('ekavīsat', 21), ('vīsat', 20), ('ekūnavīsat', 19), ('sattindriy', 7), ('navindriy', 9),
    ('aṭṭhindriy', 8), ('pañcindriy', 5), ('sattadhātu', 7), ('chaḷindriy', 6), ('chindriy', 6),
    ('dvādas', 12), ('ekādas', 11),('das', 10), ('chāyatan', 6), ('chadhātu', 6), ('nava', 9), ('navā', 9), ('aṭṭha', 8),
    ('sattavidh', 7), ('satta ', 7), ('chabbidh', 6), ('chā', 6), ('cha ', 6), ('pañca', 5), ('pañcā', 5),
    ('cattāro', 4), ('catasso', 4), ('cattāri', 4), ('catu', 4), ('tayo', 3), ('tīṇi', 3), ('tisso', 3), ('tividh', 3),
    ('dve', 2), ('dvā', 2), ('duvidh', 2), ('dvi', 2), ('eka', 1), ('ekaṃ', 1), ('eko', 1), ('ekā', 1),
]
HNUM = {'एक': 1, 'दो': 2, 'तीन': 3, 'चार': 4, 'पाँच': 5, 'छह': 6, 'सात': 7, 'आठ': 8, 'नौ': 9, 'दस': 10,
        'ग्यारह': 11, 'बारह': 12, 'तेरह': 13, 'चौदह': 14, 'पंद्रह': 15, 'सोलह': 16, 'सत्रह': 17, 'अठारह': 18, 'उन्नीस': 19, 'बीस': 20, 'इक्कीस': 21, 'बाईस': 22}


def lines(p):
    out = []
    for raw in Path(p).read_text(encoding='utf-8').split('\n'):
        if raw.strip():
            out.append(raw.rstrip())
    return out


def pnum(s):
    w = s.strip().lstrip('"“(').lower()
    for pre, v in PNUM:
        if pre.endswith(' '):
            if w.startswith(pre):
                return v
        elif w.startswith(pre):
            # avoid 'chāyā', 'sattā' etc
            if pre == 'chā' and w.startswith('chāyā'):
                return None
            return v
    return None


def hnum(s):
    w = s.strip().split(' ')[0] if s.strip() else ''
    return HNUM.get(w)


def psplit(t):
    t = re.sub(r'\s*\^[\w-]+\s*$', '', t)
    t = re.sub(r'\[[^\]]*\]', '', t)
    parts = re.split(r'(?<=[.?])\s+(?=[A-ZĀĪŪṄÑṬḌṆḶṂ"])', t)
    return [p for p in parts if p.strip()]


def hsplit(t):
    t = re.sub(r'\s*\^[\w-]+\s*$', '', t)
    t = re.sub(r'\[[^\]]*\]', '', t)
    parts = re.split(r'(?<=[।?])\s+', t)
    return [p for p in parts if p.strip()]


def pc(s):
    return dict(
        siya=len(re.findall(r'\bsiyā\b', s)),
        nv=len(re.findall(r'\bna vattabb', s)),
        q=s.count('"') // 2,
    )


def hc(s):
    return dict(
        siya=len(re.findall(r'कभी', s)),
        nv=len(re.findall(r'नहीं कहा जा सकता', s)),
        q=s.count('“'),
    )


for ch in CHS:
    P = lines(ROOT / 'pali' / 'pi-2_split_chapters' / f'{ch}.md')
    H = lines(ROOT / 'hindi' / 'pi-2-hindi-plain-rails_split_chapters' / f'{ch}.md')
    print(f'===== {ch}: P {len(P)} H {len(H)}')
    raw = (ROOT / 'hindi' / 'pi-2-hindi-plain-rails_split_chapters' / f'{ch}.md').read_text(encoding='utf-8')
    if '\n\n\n' in raw:
        print('  DOUBLE BLANK LINE present')
    curid = None
    for i, (p, h) in enumerate(zip(P, H), 1):
        pid = re.search(r'\^([\w-]+)\s*$', p)
        hid = re.search(r'\^([\w-]+)\s*$', h)
        if (pid and pid.group(1)) != (hid and hid.group(1)):
            print(f'  L{i} ID mismatch {pid and pid.group(1)} vs {hid and hid.group(1)}')
        # dashes
        pd = p.count('–') + p.count('—')
        hd = h.count('–') + h.count('—')
        if pd != hd or '—' in h:
            print(f'  L{i} dash P{pd} H{hd}')
        if '"' in h or '‘' in h or '’' in h or "'" in h:
            print(f'  L{i} bad quote char in Hindi')
        if h.count('“') != h.count('”'):
            print(f'  L{i} unbalanced quotes {h.count("“")}/{h.count("”")}')
        noBr = re.sub(r'\[[^\]]*\]', '', h)
        noBr = re.sub(r'\^[\w-]+', '', noBr)
        lat = re.findall(r'[A-Za-zĀ-ž\u1e00-\u1eff]{2,}', noBr)
        if lat:
            print(f'  L{i} Latin outside brackets: {lat[:6]}')
        body = re.sub(r'\s*\^[\w-]+\s*$', '', h).rstrip()
        if not h.startswith('#') and body and body[-1] not in '।?”' and not body.endswith('…'):
            print(f'  L{i} line end: {body[-15:]!r}')
        if '.' in re.sub(r'\[[^\]]*\]', '', body) and not h.startswith('#'):
            print(f'  L{i} has ASCII period')
        if h.startswith('#'):
            continue
        ps, hs = psplit(p), hsplit(h)
        if len(ps) != len(hs):
            print(f'  L{i} sentence count P{len(ps)} H{len(hs)}  (id {pid and pid.group(1)})')
            # still compare totals
            a, b = pc(p), hc(h)
            if a != b:
                print(f'     totals P{a} H{b}')
            continue
        for j, (a, b) in enumerate(zip(ps, hs), 1):
            ca, cb = pc(a), hc(b)
            na, nb = pnum(a), hnum(b)
            msg = []
            if ca['siya'] != cb['siya']:
                msg.append(f'siya {ca["siya"]}/{cb["siya"]}')
            if ca['nv'] != cb['nv']:
                msg.append(f'nv {ca["nv"]}/{cb["nv"]}')
            if ca['q'] != cb['q']:
                msg.append(f'q {ca["q"]}/{cb["q"]}')
            if na is not None and nb is not None and na != nb:
                msg.append(f'NUM {na}/{nb}')
            if (na is None) != (nb is None):
                msg.append(f'num? {na}/{nb}')
            if msg:
                print(f'  L{i} s{j}: {"; ".join(msg)} | {a[:70]} || {b[:70]}')
