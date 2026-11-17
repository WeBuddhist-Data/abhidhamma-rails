import sys, re
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review')
from r1_align import load

CHS = ['preamble.md', '1-khandhavibhango.md', '2-ayatanavibhango.md', '3-dhatuvibhango.md']
LAT = re.compile(r'[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]{2,}')
DIG = re.compile(r'\d+')
nseg = 0
for ch in CHS:
    p, r, pt, rt = load(ch)
    print('##', ch, 'segs', len(p), len(r))
    if '\n\n\n' in rt: print('  DOUBLE BLANK')
    if '\r' in rt: print('  CR')
    nseg += sum(1 for x in p if x[0] and not x[1][0].startswith('#'))
    for (pid, pl), (rid, rl) in zip(p, r):
        if pid != rid:
            print('  IDMISMATCH', pid, rid)
        if len(pl) != len(rl):
            print('  LINECOUNT', pid, len(pl), len(rl))
        for a, b in zip(pl, rl):
            a2 = re.sub(r'\^[\w-]+\s*$', '', a)
            b2 = re.sub(r'\^[\w-]+\s*$', '', b)
            da = a2.count('–') + a2.count('—')
            db = b2.count('–') + b2.count('—')
            if da != db:
                print('  DASH', pid, da, db, '|', b2[:150])
            if '—' in b2: print('  EMDASH', pid)
            if a2.count('?') != b2.count('?'):
                print('  QMARK', pid, a2.count('?'), b2.count('?'))
            if re.search(r'\bли\b', b2): print('  LI', pid, b2[:120])
            a3 = re.sub(r'…\s*pe\s*…', '…', a2)
            a3 = re.sub(r'…\s*pa\s*…', '…', a3)
            if a3.count('…') != b2.count('…'):
                print('  ELLIPSIS', pid, a2.count('…'), b2.count('…'), '|', b2[:120])
            # latin outside brackets
            bb = re.sub(r'\[[^\]]*\]', '', b2)
            lat = [w for w in LAT.findall(bb)]
            if lat: print('  LATIN', pid, lat[:5])
            dig_a = DIG.findall(re.sub(r'\[[^\]]*\]', '', a2))
            dig_b = DIG.findall(re.sub(r'\[[^\]]*\]', '', b2))
            if dig_a != dig_b: print('  DIGITS', pid, dig_a, dig_b)
            # brackets count
            if a2.count('[') != b2.count('['): print('  BRACKET', pid, a2.count('['), b2.count('['))
            s = b2.rstrip()
            if s and not s.startswith('#') and s[-1] not in '.?»…:;!)]“':
                print('  ENDPUNCT', pid, repr(s[-20:]))
            if '"' in b2 or '“' in b2 and '„' not in b2:
                print('  QUOTE', pid, b2[:100])
            if re.search(r'\b(\w+) \1\b', b2, re.I):
                m = re.search(r'\b(\w+) \1\b', b2, re.I)
                print('  REPEAT', pid, m.group(0))
print('content segs', nseg)
