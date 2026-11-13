"""Compare verb polarity/tense sequences between Pali and Hindi, line by line."""
import re, os, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r7_pairs import load
from review_r7_abstract import FILES

idre = re.compile(r'\s*\^(6-[\d-]+)\s*$')
PV = re.compile(r'(?<![A-Za-zāīūṃṅñṭḍṇḷ])(na\s+|n)?(uppajj|nirujjh)([A-Za-zāīūṃṅñṭḍṇḷ]*)', re.I)

def pali_seq(s):
    seq = []
    # mark positions of 'no ca' (flip next verb)
    flips = [m.end() for m in re.finditer(r'(?<![A-Za-zā])no ca\b', s, re.I)]
    for m in PV.finditer(s):
        neg = bool(m.group(1))
        # flip if a 'no ca' occurs between previous verb and this one
        prev_end = seq[-1][3] if seq else 0
        if any(prev_end <= f <= m.start() for f in flips):
            neg = not neg
        end = m.group(3)
        tense = 'P' if 'itth' in end else ('F' if 'iss' in end else 'N')
        seq.append((m.group(2)[0], neg, tense, m.end()))
    return [(v, n, t) for v, n, t, _ in seq]

HV = re.compile(r'(उत्पन्न|निरुद्ध)(?! होने)(?=((?:\s+\S+){0,4}))')
def hindi_seq(s):
    seq = []
    for m in HV.finditer(s):
        tail = m.group(2)
        words = tail.split()
        neg = len(words) > 0 and words[0] == 'नहीं'
        t = None
        for w in words:
            w = w.strip('।?,…')
            if re.match(r'^हो(ता|ती|ते|तीं)$', w):
                t = 'N'; break
            if re.match(r'^हु(आ|ई|ए|ईं)$', w):
                t = 'P'; break
            if re.match(r'^हो(गा|गी|गे|ंगे|ंगी|गीं)$', w):
                t = 'F'; break
            if w in ('है', 'हैं', 'था', 'थी', 'थे', 'थीं'):
                continue
        seq.append(('u' if m.group(1) == 'उत्पन्न' else 'n', neg, t or '?'))
    return seq

if __name__ == '__main__':
    bad = defaultdict(list)
    n = 0
    for fn in FILES:
        pl, hl = load(fn)
        for i, (p, h) in enumerate(zip(pl, hl), 1):
            if p.startswith('#'):
                continue
            n += 1
            ps, hs = pali_seq(idre.sub('', p)), hindi_seq(idre.sub('', h))
            if ps != hs:
                bad[fn].append((i, ps, hs))
    print('lines checked', n)
    for fn, v in bad.items():
        print(fn, len(v))
        for i, ps, hs in v:
            f = lambda q: ' '.join(f"{a}{'-' if b else '+'}{c}" for a, b, c in q)
            print(f'  {i}: P[{f(ps)}] H[{f(hs)}]')
