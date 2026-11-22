import re, sys, os, collections
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
P = os.path.join(ROOT, 'pali', 'pi-6_split_chapters')
V = os.path.join(ROOT, 'vietnamese', 'pi-6-vietnamese-plain-rails_split_chapters')
FILES = ['3-06-ayatanayamaka.md', '4-dhatuyamaka.md', '5-01-saccayamaka.md', '5-02-saccayamaka.md',
         '5-03-saccayamaka.md', '6-01-sankharayamaka.md', '6-02-sankharayamaka.md', '7-01-anusayayamaka.md']
sel = sys.argv[1:] or FILES

def lines(path):
    with open(path, encoding='utf-8') as f:
        return [l.rstrip('\n') for l in f if l.strip()]

VERB = r'(?:uppajj|nirujjh|parijān|pajah|pajahi|bhāve|bhāvi|sacchikar|sacchikari|anuse|pahīn|upapajj|pariññāt|bhāvit|sacchikat)'

def strip(s):
    s = re.sub(r'\[[^\]]*\]', '', s)
    s = re.sub(r'\^[\d-]+\s*$', '', s)
    return s.strip()

def psplit(s):
    # sentences
    return [x for x in re.split(r'(?<=[.?])\s+', s) if x.strip()]

def pclause(c):
    t = c.lower()
    toks = re.findall(r"[\wāīūṃṅñṭḍṇḷ]+", t)
    vs = []
    for i, w in enumerate(toks):
        if re.match(r'^(n)?' + VERB, w) or re.match(r'^(nupp|nāsev|nānus|nappaj|nappah)', w) or re.match(r'^(appahīn|apariññāt|abhāvit|asacchikat|anuppann|aniruddh)', w):
            neg = w.startswith(('nupp', 'nānu', 'nappa', 'appah', 'apari', 'abhāv', 'asacch', 'anupp', 'aniru')) or (i > 0 and toks[i - 1] in ('na',))
            tense = 'past' if 'ittha' in w else ('fut' if 'issa' in w else 'pres')
            if re.search(r'(itvā|etvā|antānaṃ|antassa|amānaṃ|amānassa)$', w):
                continue
            vs.append((w, neg, tense))
    return vs

def vclause_neg(c):
    t = c.lower()
    t = re.sub(r'không hình sắc|không trở lại|không gắn liền|không có (mắt|tai|mũi|lưỡi|thân|ý)\b|không thiện không bất thiện|không có gốc rễ|không có tưởng|không phải người', '', t)
    return bool(re.search(r'\bkhông\b|\bchưa\b', t))

def vtense(c):
    t = c.lower()
    if re.search(r'\bsẽ\b', t):
        return 'fut'
    if re.search(r'\bđã\b|\bchưa từng\b', t):
        return 'past'
    return 'pres'

out = collections.Counter()
for fn in sel:
    pl = lines(os.path.join(P, fn)); vl = lines(os.path.join(V, fn))
    for li, (a, b) in enumerate(zip(pl, vl)):
        if a.startswith('#'):
            continue
        pa, vb = strip(a), strip(b)
        ps, vss = psplit(pa), psplit(vb)
        if len(ps) != len(vss):
            out['sentcount'] += 1
            print('SENTCOUNT', fn, 'L%d' % li, len(ps), len(vss))
            print('  P:', a); print('  V:', b)
            continue
        for s, v in zip(ps, vss):
            if '?' in s:
                continue
            if ' no ca ' in ' ' + s.lower() + ' ':
                p1, p2 = re.split(r'\bno ca\b', s, maxsplit=1, flags=re.I)
                if 'nhưng' not in v:
                    print('NO-NHUNG', fn, 'L%d' % li); print('  P:', s); print('  V:', v); continue
                v1, v2 = v.split('nhưng', 1)
                c1, c2 = pclause(p1), pclause(p2)
                if not c1 or not c2:
                    continue
                n1, t1 = c1[-1][1], c1[-1][2]
                n2, t2 = c2[0][1], c2[0][2]
                v1neg = vclause_neg(v1.split(',')[-1] if ',' in v1 else v1)
                # clause 1 neg check on last segment after 'thì'
                seg1 = v1.split('thì')[-1]
                v1neg = vclause_neg(seg1)
                prob = []
                if v1neg != n1:
                    prob.append('c1neg P=%s V=%s' % (n1, v1neg))
                if vtense(seg1) != t1:
                    prob.append('c1tense P=%s V=%s' % (t1, vtense(seg1)))
                # clause2: positive Pali -> Viet has 'không'; negative Pali -> 'vẫn' or 'đã từng' and no 'không'
                v2neg = vclause_neg(v2)
                if not n2 and not v2neg:
                    prob.append('c2 P=pos expected không')
                if n2 and (v2neg or not re.search(r'vẫn|đã từng', v2)):
                    prob.append('c2 P=neg expected vẫn/đã từng')
                vt2 = 'fut' if 'sẽ' in v2 else ('past' if re.search(r'đã|chưa từng', v2) else 'pres')
                if vt2 != t2:
                    prob.append('c2tense P=%s V=%s' % (t2, vt2))
                if prob:
                    out['noca'] += 1
                    print('NOCA', fn, 'L%d' % li, '; '.join(prob)); print('  P:', s); print('  V:', v)
            elif re.search(r'ñca\b.*ñca\b', s) or re.search(r'\bca\b.*\bca\b', s):
                cs = pclause(s)
                if len(cs) < 2:
                    continue
                negs = [x[1] for x in cs]
                tens = [x[2] for x in cs]
                vneg = vclause_neg(v)
                if any(negs) != vneg or (all(negs) and v.lower().count('không') + v.lower().count('chưa') < 2 and 'không có' not in v):
                    out['both'] += 1
                    print('BOTH-NEG', fn, 'L%d' % li, negs); print('  P:', s); print('  V:', v)
                seg = v.split('thì')[-1]
                if ', ' in seg and len(set(tens)) > 1:
                    pa_, pb_ = seg.rsplit(', ', 1)
                    if vtense(pa_) != tens[0] or vtense(pb_) != tens[-1]:
                        out['bothtense'] += 1
                        print('BOTH-TENSE', fn, 'L%d' % li, tens); print('  P:', s); print('  V:', v)
                elif tens[0] != vtense(v):
                    out['bothtense'] += 1
                    print('BOTH-TENSE', fn, 'L%d' % li, tens); print('  P:', s); print('  V:', v)
print(out)
