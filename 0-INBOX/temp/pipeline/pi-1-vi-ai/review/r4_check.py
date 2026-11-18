import sys, os, re, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r4_lib import *

PALI_DIA = re.compile(r'[āīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]')

for f in FILES:
    praw = open(os.path.join(PI, f), encoding='utf-8').read()
    vraw = open(os.path.join(VI, f), encoding='utf-8').read()
    print('#####', f)
    if '\r' in vraw: print('CR present')
    if unicodedata.normalize('NFC', vraw) != vraw: print('not NFC')
    if re.search(r'\n\s*\n\s*\n', vraw): print('double blank line')
    P = segs(os.path.join(PI, f)); V = segs(os.path.join(VI, f))
    if len(P) != len(V): print('SEGCOUNT', len(P), len(V))
    for (pid, pl), (vid, vl) in zip(P, V):
        if pid != vid: print('ID', pid, vid)
        if len(pl) != len(vl): print(pid, 'LINES', len(pl), len(vl))
        for k, (p, v) in enumerate(zip(pl, vl)):
            tag = f'{pid}.{k}'
            p0, v0 = strip_id(p), strip_id(v)
            for ch in '–—':
                if p0.count(ch) != v0.count(ch): print(tag, 'DASH', ch, p0.count(ch), v0.count(ch))
            # dash positions: segment counts by dash
            npe = p0.count('…pe…') + len(re.findall(r'(?<!pe)…(?!pe)', p0.replace('…pe…', '')))
            nv = v0.count('…')
            if npe != nv: print(tag, 'ELLIPSIS', npe, nv)
            if '….' in v0 or '…?' in v0 and '…?' not in p0: print(tag, 'ELL-PUNCT')
            pe, ve = p0.rstrip()[-1:], v0.rstrip()[-1:]
            if pe != ve: print(tag, 'END', repr(pe), repr(ve))
            if p0.count('?') != v0.count('?'): print(tag, 'QCOUNT', p0.count('?'), v0.count('?'))
            pd, vd = re.findall(r'\d+', re.sub(r'\[.*?\]', '', p0)), re.findall(r'\d+', re.sub(r'\[.*?\]', '', v0))
            if pd != vd: print(tag, 'DIGITS', pd, vd)
            outside = re.sub(r'\[.*?\]', '', v0)
            lat = [w for w in re.findall(r'\w+', outside) if PALI_DIA.search(w)]
            if lat: print(tag, 'LATIN', lat)
            m = re.search(r'\b(\w+) \1\b', outside)
            if m: print(tag, 'REPEAT', m.group(0))
            if re.search(r'\blà là\b', outside): print(tag, 'LA-LA')
            if '“' in v0 or '‘' in v0 or '"' in v0 or "'" in v0:
                if v0.count('“') != v0.count('”') or v0.count('‘') != v0.count('’') or '"' in v0: print(tag, 'QUOTES')
            if re.search(r' [.,;:?!]', outside): print(tag, 'SPACE-PUNCT')
            if re.search(r'\?', v0):
                for q in re.findall(r'[^.?;–]*\?', v0):
                    if not re.search(r'\b(nào|gì|bao nhiêu|không|ra sao|thế nào|sao)\?|\bnào\b|\bgì\b|bao nhiêu', q):
                        print(tag, 'QWORD?', q[-60:])
