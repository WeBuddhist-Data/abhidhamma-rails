import re, sys
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'

def ne(path):
    return [l.rstrip('\n') for l in open(path, encoding='utf-8') if l.strip()]

PV = re.compile(r'\b(na |no ca (?:tesaṃ |tassa |tattha |tesaṃ tattha |tassa tattha |taṃ )?(?:[^\s,.?]+ )*?(?:na )?)?(n?)(uppajj|nirujjh)(anti|antī|ati|atī|itth|iss|amān)')

def pali_seq(p):
    t = p.lower()
    t = re.sub(r'\^\S+', '', t)
    out = []
    # split into clauses on , . ? ;
    for cl in re.split(r'[,.?;]', t):
        noca = bool(re.search(r'\bno ca\b', cl))
        for m in re.finditer(r'(\bna |\bn)?(uppajj|nirujjh)(anti|antī|ati|atī|itth|iss|amān)', cl):
            # check 'na' immediately before verb
            pre = cl[:m.start()]
            neg = bool(re.search(r'\bna $', pre)) or (m.group(1) in ('n', 'na '))
            # na ... dhammā verb  (na kusalā dhammā uppajjanti not used here); also 'na ceva'/'na ca' forms
            if re.search(r'\bna (ceva|ca) $', pre):
                neg = True
            if noca:
                neg = not neg
            v = 'U' if m.group(2) == 'uppajj' else 'N'
            tn = {'anti': 'P', 'antī': 'P', 'ati': 'P', 'atī': 'P', 'itth': 'A', 'iss': 'F', 'amān': 'M'}[m.group(3)]
            out.append(v + tn + ('-' if neg else '+'))
    return out

HV = re.compile(r'(उत्पन्न|समाप्त)( भी)?( नहीं)?( भी)? (होती हैं|होतीं|होती|होता है|होता|होते|हुई थीं|हुआ था|हुई थी|हुए थे|होंगी|होगा|होगी|होंगे|होता हुआ|होते हुए)')

def hindi_seq(h):
    out = []
    for m in HV.finditer(h):
        v = 'U' if m.group(1) == 'उत्पन्न' else 'N'
        f = m.group(5)
        if f.startswith('हुई') or f.startswith('हुआ') or f.startswith('हुए'):
            tn = 'A'
        elif f in ('होंगी', 'होगा', 'होगी', 'होंगे'):
            tn = 'F'
        elif 'हुआ' in f or 'हुए' in f:
            tn = 'M'
        else:
            tn = 'P'
        neg = bool(m.group(3))
        out.append(v + tn + ('-' if neg else '+'))
    return out

def main():
    for f in sys.argv[1:]:
        P = ne(base + '\\pali\\pi-6_split_chapters\\' + f)
        H = ne(base + '\\hindi\\pi-6-hindi-plain-rails_split_chapters\\' + f)
        bad = 0
        for i, (p, h) in enumerate(zip(P, H), 1):
            if p.startswith('#'):
                continue
            # labels
            lp = re.match(r'\((Ka|Kha|Ga|Gha)\)', p)
            lh = re.match(r'\((क|ख|ग|घ)\)', h)
            mp = {'Ka': 'क', 'Kha': 'ख', 'Ga': 'ग', 'Gha': 'घ'}
            if (lp and not lh) or (lh and not lp) or (lp and lh and mp[lp.group(1)] != lh.group(1)):
                print(f'{f} L{i} LABEL mismatch')
            # person/place
            pp = (bool(re.search(r'yassa (vā pana )?yattha', p.lower())), 'yattha' in p.lower() and 'yassa' not in p.lower(), 'yassa' in p.lower() and 'yattha' not in p.lower())
            hp = ('जिस व्यक्ति में जिस स्थान' in h, 'जिस स्थान' in h and 'जिस व्यक्ति' not in h, 'जिस व्यक्ति' in h and 'जिस स्थान' not in h)
            if pp != hp and re.match(r'\(?(Ka|Kha)', p):
                print(f'{f} L{i} PERSON/PLACE {pp} {hp}')
            ps, hs = pali_seq(p), hindi_seq(h)
            if ps != hs:
                bad += 1
                print(f'{f} L{i} SEQ P{ps} H{hs}')
        print(f, 'seq mismatches', bad)

main()
