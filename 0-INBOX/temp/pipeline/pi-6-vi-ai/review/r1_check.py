import re, sys, unicodedata
from collections import Counter, defaultdict, OrderedDict

ROOT = 'D:/Work/OpenPecha/abhidhamma-rails/'
PDIR = ROOT + 'AI_translation/pali/pi-6_split_chapters/'
VDIR = ROOT + 'AI_translation/vietnamese/pi-6-vietnamese-plain-rails_split_chapters/'
FILES = ['preamble.md', '1-mulayamaka.md', '2-01-khandhayamaka.md', '2-02-khandhayamaka.md',
         '3-01-ayatanayamaka.md', '3-02-ayatanayamaka.md', '3-03-ayatanayamaka.md',
         '3-04-ayatanayamaka.md', '3-05-ayatanayamaka.md']

IDRE = re.compile(r'\s\^([0-9A-Za-z-]+)\s*$')


def load(path):
    raw = open(path, 'rb').read()
    txt = raw.decode('utf-8')
    probs = []
    if '\r' in txt:
        probs.append('CR')
    if '\n\n\n' in txt:
        probs.append('double blank')
    if unicodedata.normalize('NFC', txt) != txt:
        probs.append('not NFC')
    segs = OrderedDict()
    cur = []
    for ln in txt.split('\n'):
        if not ln.strip():
            continue
        cur.append(ln)
        m = IDRE.search(ln)
        if m:
            segs[m.group(1)] = cur
            cur = []
    if cur:
        probs.append('trailing lines without ID: %d' % len(cur))
    return segs, probs


KH_P = re.compile(r'(rūpa|vedanā|vadanā|saññā|saṅkhāra|viññāṇa)kkhandh\w*')
KH_PMAP = {'rūpa': 'vc', 'vedanā': 'cg', 'vadanā': 'cg', 'saññā': 'tg', 'saṅkhāra': 'tt', 'viññāṇa': 'th'}
KH_V = re.compile(r'khối (vật chất|cảm giác|tri giác|tạo tác|thức)')
KH_VMAP = {'vật chất': 'vc', 'cảm giác': 'cg', 'tri giác': 'tg', 'tạo tác': 'tt', 'thức': 'th'}
AY_P = re.compile(r'(cakkh|sot|ghān|jivh|kāy|rūp|sadd|gandh|ras|phoṭṭhabb|man|dhamm)āyatan\w*')
AY_PMAP = {'cakkh': 'mắt', 'sot': 'tai', 'ghān': 'mũi', 'jivh': 'lưỡi', 'kāy': 'thân', 'rūp': 'hình sắc',
           'sadd': 'âm thanh', 'gandh': 'mùi', 'ras': 'vị', 'phoṭṭhabb': 'vật xúc chạm', 'man': 'ý',
           'dhamm': 'đối tượng của ý'}
AY_V = re.compile(r'lĩnh vực (đối tượng của ý|vật xúc chạm|hình sắc|âm thanh|mắt|tai|mũi|lưỡi|thân|mùi|vị|ý)')


def pterms(s):
    out = []
    for m in re.finditer(KH_P.pattern + '|' + AY_P.pattern, s, re.I):
        t = m.group(0)
        t = t[0].lower() + t[1:]
        mk = KH_P.match(t)
        if mk:
            out.append('K:' + KH_PMAP[mk.group(1)])
        else:
            ma = AY_P.match(t)
            out.append('A:' + AY_PMAP[ma.group(1)])
    return out


def vterms(s):
    out = []
    for m in re.finditer(KH_V.pattern + '|' + AY_V.pattern, s.replace('Khối ', 'khối ').replace('Lĩnh vực ', 'lĩnh vực ')):
        t = m.group(0)
        if t.startswith('khối'):
            out.append('K:' + KH_VMAP[m.group(1)])
        else:
            out.append('A:' + m.group(2))
    return out


# verbs
PV = re.compile(r'(\bna |\bn)?(uppajj|nirujjh|parijān)(issatī|issati|issanti|ittha|itthā|attha|ātī|āti|atī|ati|anti)')
VV = re.compile(r'(sinh khởi|chấm dứt|hiểu biết trọn vẹn)')
ANS_ONLY = re.compile(r'^(Có sinh khởi|Đã sinh khởi|Sẽ sinh khởi|Có chấm dứt|Đã chấm dứt|Sẽ chấm dứt)\.?$')


def ptags(sent):
    # returns list of (tense, polarity) expected in Vietnamese
    tags = []
    # split at "no ca": verbs after it are flipped
    parts = re.split(r'\bno ca\b', sent)
    for i, part in enumerate(parts):
        for m in PV.finditer(part):
            neg = bool(m.group(1))
            suf = m.group(3)
            if suf.startswith('iss'):
                t = 'F'
            elif suf.startswith('itth') or suf == 'attha':
                t = 'P'
            else:
                t = 'N'
            pol = (not neg) if i > 0 else neg  # i>0: after "no ca"
            # pol True means NEG expected in Vietnamese
            tags.append((t, 'neg' if pol else 'pos'))
    return tags


CUT = re.compile(r'(,|\bthì\b|\bmà\b|\bấy\b|\bnào\b|\bphải\b|\bcũng\b|\bnhưng\b|\.|\?)')


def vtags(sent):
    tags = []
    last = 0
    for m in VV.finditer(sent):
        pre = sent[last:m.start()]
        # window after last cut token
        cuts = list(CUT.finditer(pre))
        ww = pre[cuts[-1].end():] if cuts else pre
        t = 'N'
        if re.search(r'\bsẽ\b', ww):
            t = 'F'
        elif re.search(r'\bđã\b|chưa từng', ww):
            t = 'P'
        neg = bool(re.search(r'\bkhông\b|\bchưa\b', ww))
        tags.append((t, 'neg' if neg else 'pos'))
        last = m.end()
    return tags


def split_sents(line):
    return [s for s in re.split(r'(?<=[.?])\s+', line) if s.strip()]


SHORTP = {'Āmantā.': 'Đúng vậy.', 'No.': 'Không.', 'Natthi.': 'Không có.'}


def short_answers(line, pali):
    out = []
    for m in re.finditer(r'\?\s*([^?]*?\.)(?=\s|$)', line):
        a = m.group(1).strip()
        if len(a.split()) <= 3:
            out.append(a)
    s = line.strip()
    s = IDRE.sub('', s).strip()
    if '?' not in s and len(s.split()) <= 3 and s.endswith('.'):
        out.append(s)
    return out


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'basic'
    files = sys.argv[2:] or FILES
    anscount = Counter()
    for f in files:
        P, pp = load(PDIR + f)
        V, vp = load(VDIR + f)
        print('=== %s  P-segs %d V-segs %d %s %s' % (f, len(P), len(V), pp, vp))
        if list(P.keys()) != list(V.keys()):
            print('  ID ORDER/SET MISMATCH')
        for sid in P:
            if sid not in V:
                print('  missing', sid)
                continue
            pl, vl = P[sid], V[sid]
            if len(pl) != len(vl):
                print('  %s line count %d vs %d' % (sid, len(pl), len(vl)))
                continue
            for i, (a, b) in enumerate(zip(pl, vl)):
                a0 = unicodedata.normalize('NFC', a)
                b0 = unicodedata.normalize('NFC', b)
                if mode == 'basic':
                    if a0.count('?') != b0.count('?'):
                        print('  %s L%d ?: %d vs %d' % (sid, i + 1, a0.count('?'), b0.count('?')))
                    da = a0.count('–') + a0.count('—')
                    db = b0.count('–') + b0.count('—')
                    if da != db:
                        print('  %s L%d dash %d vs %d' % (sid, i + 1, da, db))
                    a1 = a0.replace('…Pe…', '…pe…')
                    ea = a1.count('…pe…') + a1.replace('…pe…', '').count('…')
                    eb = b0.count('…')
                    if ea != eb:
                        print('  %s L%d ellipsis %d vs %d' % (sid, i + 1, ea, eb))
                    if '….' in b0 or '..' in b0:
                        print('  %s L%d bad dots' % (sid, i + 1))
                    if a0.lstrip().startswith('#') != b0.lstrip().startswith('#') or \
                            (a0.lstrip().startswith('#') and a0.split()[0] != b0.split()[0]):
                        print('  %s L%d heading level' % (sid, i + 1))
                    # pali diacritics outside brackets
                    bb = re.sub(r'\[[^\]]*\]', '', b0)
                    lat = re.findall(r'\w*[āīūṃṅñṭḍṇḷ]\w*', bb)
                    if lat:
                        print('  %s L%d latin: %s' % (sid, i + 1, lat))
                    # terms
                    tp, tv = pterms(a0), vterms(b0)
                    if tp != tv:
                        print('  %s L%d TERMS P=%s V=%s' % (sid, i + 1, tp, tv))
                    # short answers
                    sa, sb = short_answers(a0, True), short_answers(b0, False)
                    if len(sa) != len(sb):
                        print('  %s L%d ANSCOUNT %s vs %s' % (sid, i + 1, sa, sb))
                    for x, y in zip(sa, sb):
                        anscount[(x, y)] += 1
                    # tense / polarity per sentence
                    ps, vs = split_sents(a0), split_sents(b0)
                    if len(ps) != len(vs):
                        print('  %s L%d SENTS %d vs %d' % (sid, i + 1, len(ps), len(vs)))
                        continue
                    for j, (x, y) in enumerate(zip(ps, vs)):
                        if ANS_ONLY.match(y.strip()):
                            continue
                        tx, ty = ptags(x), vtags(y)
                        if tx != ty:
                            print('  %s L%d S%d TAGS P=%s V=%s' % (sid, i + 1, j + 1, tx, ty))
    if mode == 'basic':
        print('=== short answer pairs')
        for k, v in sorted(anscount.items(), key=lambda kv: -kv[1]):
            print('  %5d  %s -> %s' % (v, k[0], k[1]))


if __name__ == '__main__':
    main()
