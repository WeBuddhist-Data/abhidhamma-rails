import re, sys, io
base = r'D:\Work\OpenPecha\abhidhamma-rails\AI_translation'
ch = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else 'flags'
P = [l.rstrip('\n') for l in io.open(base + r'\pali\pi-2_split_chapters\\' + ch, encoding='utf8')]
H = [l.rstrip('\n') for l in io.open(base + r'\hindi\pi-2-hindi-plain-rails_split_chapters\\' + ch, encoding='utf8')]
E = [l.rstrip('\n') for l in io.open(base + r'\english\pi-2-english-plain-zeroshot_split_chapters\\' + ch, encoding='utf8')]

def ne(L):
    return [l for l in L if l.strip()]
p, h, e = ne(P), ne(H), ne(E)
print('nonempty', len(p), len(h), len(e))
# double blank lines
for name, L in (('P', P), ('H', H)):
    for i in range(1, len(L)):
        if not L[i].strip() and not L[i-1].strip():
            print('DOUBLE BLANK', name, i+1)
# blank-line structure equal?
if [bool(x.strip()) for x in P] != [bool(x.strip()) for x in H]:
    print('blank-line structure differs')
idre = re.compile(r'\^[\w-]+\s*$')
cur = ''
for i, (a, b) in enumerate(zip(p, h), 1):
    ia = idre.search(a); ib = idre.search(b)
    fl = []
    if (ia.group(0) if ia else None) != (ib.group(0) if ib else None):
        fl.append('IDMISMATCH')
    if ia: cur = ia.group(0)
    da = a.count('–') + a.count('—'); db = b.count('–') + b.count('—')
    if da != db: fl.append(f'DASH {da}/{db}')
    if '—' in b: fl.append('EMDASH-H')
    na = re.findall(r'\((\d+)\)', a); nb = re.findall(r'\((\d+)\)', b)
    if na != nb: fl.append(f'PARENNUM {na}/{nb}')
    # latin outside brackets
    bb = re.sub(r'\[[^\]]*\]', '', b); bb = re.sub(r'\^[\w-]+', '', bb)
    lat = re.findall(r'[A-Za-zāīūṃṅñṭḍṇḷĀĪŪ]{2,}', bb)
    if lat: fl.append('LATIN ' + ' '.join(lat[:5]))
    if '"' in b or "'" in b: fl.append('STRAIGHTQUOTE')
    if b.count('“') != b.count('”'): fl.append('QUOTEBAL')
    if a.count('[') != b.count('['): fl.append(f'BRACKET {a.count("[")}/{b.count("[")}')
    if re.search(r'\d', re.sub(r'\^[\w-]+|\(\d+\)|\[[^\]]*\]', '', b)): fl.append('DIGIT-H')
    if re.search(r'\d', re.sub(r'\^[\w-]+|\(\d+\)|\[[^\]]*\]', '', a)): fl.append('DIGIT-P')
    # end punctuation
    sa = re.sub(r'\s*\^[\w-]+\s*$', '', a).rstrip(); sb = re.sub(r'\s*\^[\w-]+\s*$', '', b).rstrip()
    if sa.endswith('.') and not sb.endswith('।') and not sb.endswith('?') : fl.append('END-।')
    if sa.endswith('?') and not sb.endswith('?'): fl.append('END-?')
    if '..' in sb or '. ' in sb: fl.append('DOT')
    if re.search(r'pe(…|\.\.\.)|…pe', a) and '…' not in b and '...' not in b: fl.append('PE-missing')
    # comma counts
    ca = a.count(','); cb = b.count(',')
    if mode == 'flags':
        if fl: print(i, cur, ' | '.join(fl))
    elif mode == 'commas':
        if ca != cb: print(i, cur, f'commas {ca}/{cb}')
    elif mode == 'dump':
        lo, hi = int(sys.argv[3]), int(sys.argv[4])
        if lo <= i <= hi:
            print(f'[{i}] P: {a}\n[{i}] H: {b}\n')

