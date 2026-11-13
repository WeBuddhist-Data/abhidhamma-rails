import re, sys, os
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
FILES = ['8-cittayamaka.md', '9-01-dhammayamaka.md', '9-02-dhammayamaka.md', '9-03-dhammayamaka.md']

def ne(path):
    return [l.rstrip('\n') for l in open(path, encoding='utf-8') if l.strip()]

def bid(s):
    m = re.search(r'\^(\S+)\s*$', s)
    return m.group(1) if m else ''

# --- polarity ---
def pali_neg(p):
    t = p.lower()
    t = re.sub(r'\^\S+', '', t)
    # 'no ca' clauses: up to next , . ? ;
    exp = 0
    for m in re.finditer(r'\bno ca\b([^,.?;]*)', t):
        inner = m.group(1)
        if re.search(r'\bna\b', inner):
            exp -= 1  # inner na counted below, but flip -> 0
        else:
            exp += 1
    exp += len(re.findall(r'\bna\b', t))
    exp += len(re.findall(r'\bno\b(?! ca)', t))
    exp += len(re.findall(r'\bnatthi\b', t))
    exp += len(re.findall(r'\bnuppajj', t))
    exp += len(re.findall(r'avītikkant', t))
    return exp

def hindi_neg(h):
    n = len(re.findall(r'नहीं', h))
    n += len(re.findall(r'(?<![\u0900-\u097F])न(?![\u0900-\u097F])', h))
    return n

# --- tense ---
def pali_tense(p):
    t = p.lower()
    past = len(re.findall(r'(uppajj|nirujjh)itth', t))
    fut = len(re.findall(r'(uppajj|nirujjh)iss', t))
    pres = len(re.findall(r'(uppajj|nirujjh)(a|a)(n)?ti', t)) + len(re.findall(r'(uppajj|nirujjh)at[iī]', t))
    pres = len(re.findall(r'\b(uppajj|nirujjh|nuppajj)(anti|antī|ati|atī)', t))
    return past, fut, pres

def hindi_tense(h):
    past = len(re.findall(r'(हुई थीं|हुआ था|हुई थी|हुए थे|नहीं हुई थीं|नहीं हुआ था)', h))
    past = len(re.findall(r'(?<= )(थीं|था|थी|थे)(?=[\s\u0964?,]|$)', h))
    fut = len(re.findall(r'(होंगी|होगा|होगी|होंगे)(?=[\s\u0964?,]|$)', h))
    pres = len(re.findall(r'(उत्पन्न|समाप्त)( नहीं| भी नहीं| भी)? (होती|होता|होते)(?! हुए)(?! हुआ)', h))
    return past, fut, pres

# --- items ---
def pali_items(p):
    t = p.lower()
    out = []
    for m in re.finditer(r'(akusal|abyākat|kusal)', t):
        out.append({'kusal': 'K', 'akusal': 'A', 'abyākat': 'B'}[m.group(1)])
    return ''.join(out)

def hindi_items(h):
    out = []
    for m in re.finditer(r'(हितकर|हानिकर|अनिर्धारित)', h):
        out.append({'हितकर': 'K', 'हानिकर': 'A', 'अनिर्धारित': 'B'}[m.group(1)])
    return ''.join(out)

CHUNKS = [
    (r'upapajjant', r'जन्म लेने'),
    (r'cavant', r'मरने'),
    (r'pavatte', r'जीवन के दौरान'),
    (r'arūp', r'अभौतिक'),
    (r'pañcavokār', r'पाँच'),
    (r'catuvokār', r'चार'),
    (r'asaññasatt', r'पहचान-रहित'),
    (r'nirodhasamāpann', r'समाप्ति की ध्यान'),
    (r'suddhāvās', r'शुद्ध निवास'),
    (r'aggamagg', r'सर्वोच्च मार्ग'),
    (r'arahant', r'अर्हत'),
    (r'pacchima', r'अंतिम'),
    (r'bhaṅgakkhaṇ', r'भंग होने के क्षण'),
    (r'uppādakkhaṇ', r'उत्पन्न होने के क्षण'),
    (r'itaresaṃ', r'बाकी'),
    (r'vippayutt', r'से अलग'),
    (r'dutiye', r'दूसरे'),
    (r'paṭilabh', r'प्राप्त करेंगे'),
    (r'\batīt', r'अतीत'),
    (r'\banāgat', r'भविष्य'),
    (r'paccuppann', r'वर्तमान'),
    (r'samaṅgī', r'(से युक्त|युक्त)'),
    (r'parinibbant', r'परिनिर्वाण|निर्वाण'),
    (r'\byattha\b', r'जिस स्थान'),
    (r'\bpe\b', r'…'),
]

def main():
    files = sys.argv[1:] or FILES
    total = 0
    for f in files:
        P = ne(base + '\\pali\\pi-6_split_chapters\\' + f)
        H = ne(base + '\\hindi\\pi-6-hindi-plain-rails_split_chapters\\' + f)
        cur = ''
        for i, (p, h) in enumerate(zip(P, H), 1):
            total += 1
            probs = []
            if bid(p) != bid(h):
                probs.append(f'ID {bid(p)} vs {bid(h)}')
            if p.lstrip().startswith('#') != h.lstrip().startswith('#'):
                probs.append('heading mismatch')
            if not p.lstrip().startswith('#'):
                pn, hn = pali_neg(p), hindi_neg(h)
                if pn != hn:
                    probs.append(f'NEG P{pn} H{hn}')
                pt, ht = pali_tense(p), hindi_tense(h)
                if pt[0] != ht[0] or pt[1] != ht[1]:
                    probs.append(f'TENSE past/fut P{pt[:2]} H{ht[:2]}')
                if pt[2] != ht[2]:
                    probs.append(f'PRES P{pt[2]} H{ht[2]}')
                pi_, hi_ = pali_items(p), hindi_items(h)
                if pi_ != hi_:
                    probs.append(f'ITEMS P{pi_} H{hi_}')
                for pr, hr in CHUNKS:
                    a = len(re.findall(pr, p.lower()))
                    b = len(re.findall(hr, h))
                    if a != b:
                        probs.append(f'CHUNK {pr}:{a}/{b}')
                # typography
                ps = re.sub(r'\s*\^\S+\s*$', '', p).rstrip()
                hs = re.sub(r'\s*\^\S+\s*$', '', h).rstrip()
                if ps.endswith('?') != hs.endswith('?'):
                    probs.append('END ? mismatch')
                if re.search(r'[a-zA-Zāīūṃṅñṭḍṇḷ]{3,}', re.sub(r'\^\S+', '', h)):
                    probs.append('LATIN in Hindi')
                if ('–' in h or '—' in h) and not ('–' in p or '—' in p):
                    probs.append('DASH added')
                if re.search(r'["\']', h):
                    probs.append('straight quote')
                if hs.endswith('.'):
                    probs.append('ends with .')
            if probs:
                print(f'{f} L{i} {bid(p) or "-"} :: ' + '; '.join(probs))
    print('lines', total)

main()
