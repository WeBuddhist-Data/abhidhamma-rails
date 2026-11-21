"""r2 reviewer: per-segment mechanical checks, Pali vs our Vietnamese (console only).
usage: python -I -X utf8 r2_check.py <pali_ch.md> <vi_ch.md>
"""
import re, sys, unicodedata

def segs(path):
    t = open(path, encoding='utf-8').read()
    out, buf = {}, []
    order = []
    for line in t.split('\n'):
        if line.strip():
            buf.append(line)
        m = re.search(r'\^([0-9A-Za-z\-]+)\s*$', line)
        if m:
            out[m.group(1)] = buf
            order.append(m.group(1))
            buf = []
    return out, order, t

P, po, pt = segs(sys.argv[1])
V, vo, vt = segs(sys.argv[2])
print('ids equal:', po == vo, len(po))
for k in ('\r', '—', '….', ' .', ' ,', ' ?', '  '):
    if k in vt:
        print('found', repr(k), vt.count(k))
print('NFC:', unicodedata.normalize('NFC', vt) == vt)
print('double blank:', '\n\n\n' in vt)

neg_p = re.compile(r"(?<![\w])(na|no|neva|nā\w*|n'|natthi)(?![\w])|(?<![\w])(a|an|ap|as|ab|av|ad|am|ah|ak|ay)\w+", re.I)
pneg = re.compile(r"\b(na|no|neva|natthi|nānubyañjanaggāhī)\b")
vneg = re.compile(r"\b(không|chưa|chẳng|chớ|đừng)\b")
for i in po:
    p = ' '.join(P[i]); v = ' '.join(V.get(i, []))
    lp, lv = len(P[i]), len(V.get(i, []))
    np_ = len(pneg.findall(p)); nv = len(vneg.findall(v))
    dp = p.count('–'); dv = v.count('–')
    flag = '' if (lp == lv and dp == dv) else '  <<< LINES/DASH'
    # question name vs quoted name
    q = re.match(r'Thế nào là (.+?)\?', v)
    quotes = re.findall(r'được gọi là “([^”]+)”', v)
    qname = q.group(1) if q else None
    nm = ''
    if qname and quotes and quotes[-1] != qname:
        nm = f'  NAME? q=[{qname}] quote=[{quotes[-1]}]'
    print(f'{i}: lines {lp}/{lv} dash {dp}/{dv} neg pali={np_} vi={nv}{flag}{nm}')
