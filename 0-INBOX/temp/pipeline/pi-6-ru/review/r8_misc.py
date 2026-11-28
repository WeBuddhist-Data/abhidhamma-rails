"""r8: ellipsis counts, mūlaka labels, sentence-final punctuation, block ID lookup.
Usage: python r8_misc.py check | id <file> <line>..."""
import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review')
from r8_check import FILES, load

def block_id(f, n):
    p, r = load(f)
    for k in range(n - 1, len(p)):
        m = re.search(r'\^([\w-]+)\s*$', p[k])
        if m: return m.group(1)

if sys.argv[1] == 'id':
    f = sys.argv[2]
    for n in sys.argv[3:]:
        print(f, n, block_id(f, int(n)))
    sys.exit()

lab = collections.defaultdict(collections.Counter)
bad = 0
for f in FILES:
    p, r = load(f)
    for i, (a, b) in enumerate(zip(p, r)):
        pe = len(re.findall(r'…pe…|…', a.replace('…pe…', '\x00'))) if a else 0
        pe = a.count('…pe…') + a.replace('…pe…', '').count('…')
        if pe != b.count('…'):
            bad += 1; print('ELL', f, i + 1, pe, b.count('…'))
        for x in re.findall(r'\((\w+mūlakaṃ)\)', a):
            pass
        pm = re.findall(r'\((\w+?)(?:mūlakaṃ)\)', a); rm = re.findall(r'\((На основе [^)]*)\)', b)
        if len(pm) != len(rm):
            bad += 1; print('MUL', f, i + 1, pm, rm)
        for x, y in zip(pm, rm): lab[x][y] += 1
        # sentence-final punctuation of the line
        ae = re.sub(r'\s*\^[\w-]+\s*$', '', a).rstrip(); be = re.sub(r'\s*\^[\w-]+\s*$', '', b).rstrip()
        if ae and be and ae[-1] in '.?)…' and be[-1] != ae[-1]:
            bad += 1; print('END', f, i + 1, repr(ae[-6:]), repr(be[-6:]))
        if ae.count('?') != be.count('?') or ae.count('(') != be.count('('):
            bad += 1; print('PUNC', f, i + 1, ae.count('?'), be.count('?'), ae.count('('), be.count('('))
for x in lab:
    print(x, dict(lab[x]))
print('flags', bad)
