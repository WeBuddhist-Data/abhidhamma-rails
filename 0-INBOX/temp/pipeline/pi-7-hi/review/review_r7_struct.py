import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review')
from review_r7_common import *

praw, pl = load(P)
hraw, hl = load(H)
print('nonempty', len(pl), len(hl), 'physical', len(praw), len(hraw))
# blank-line structure
for i, (a, b) in enumerate(zip(praw, hraw), 1):
    if bool(a.strip()) != bool(b.strip()):
        print('BLANK MISMATCH phys', i)
        break
# double blanks in Hindi
for i in range(1, len(hraw)):
    if not hraw[i].strip() and not hraw[i-1].strip() and i < len(hraw)-1:
        print('DOUBLE BLANK hindi phys', i+1)
nseg = 0
for (n, i, p), (_, _, h) in zip(pl, hl):
    pm = IDRE.search(p); hm = IDRE.search(h)
    pid = pm.group(1) if pm else None; hid = hm.group(1) if hm else None
    if pid != hid:
        print('ID MISMATCH', n, pid, hid)
    if pid and not pid.endswith('-0'):
        nseg += 1
    # heading level
    pl_ = re.match(r'^#+', p); hl_ = re.match(r'^#+', h)
    if (pl_ and pl_.group()) != (hl_ and hl_.group()):
        print('HEADING LEVEL', n)
    # count markers
    pc = re.findall(r'\((\d+)\)', p); hc = re.findall(r'\((\d+)\)', h)
    if pc != hc:
        print('COUNTMARK', n, pc, hc)
    # dashes
    pd = p.count('–') + p.count('—'); hd = h.count('–') + h.count('—')
    if pd != hd:
        print('DASH', n, pd, hd)
    if '—' in h:
        print('EMDASH in hindi', n)
    # latin letters in hindi outside brackets
    hs = IDRE.sub('', h)
    hs2 = re.sub(r'\[[^\]]*\]', '', hs)
    lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷ]{2,}', hs2)
    if lat:
        print('LATIN', n, lat[:5])
    # end punctuation
    if not h.startswith('#'):
        body = IDRE.sub('', h).rstrip()
        if not re.search(r'[।?]\)?$|\(\d+\)$|[।?]”$', body):
            print('ENDPUNCT', n, repr(body[-25:]))
    # straight quotes
    if '"' in h or "'" in h:
        print('STRAIGHTQUOTE', n)
    if '{' in p or '{' in h:
        print('VARIANT', n, re.findall(r'\{[^}]*\}', p), re.findall(r'\[[^\]]*\]', h))
    # pe count vs ellipsis
    ppe = len(re.findall(r'…pe…|…', p.replace('…pe…', '\x00')))
print('segments (content ids)', nseg)
