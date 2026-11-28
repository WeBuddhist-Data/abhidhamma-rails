"""Split aligned lines into sentences; print unique (Pali, Russian) sentence pairs
(first occurrence, with line number and count). Lines whose sentence counts differ
are printed whole and flagged."""
import sys, re
from collections import OrderedDict
P = 'AI_translation/pali/pi-6_split_chapters/'
R = 'AI_translation/russian/pi-6-russian-plain-rails_split_chapters/'
files = sys.argv[1].split(',')
mode = sys.argv[2] if len(sys.argv) > 2 else 'pairs'
ID = re.compile(r'\s*\^[\w-]+\s*$')
SPL = re.compile(r'(?<=[.?!])\s+(?=[(\[A-ZĀĪŪṄÑṬḌṆḶṂa-zāīūṅñṭḍṇḷṃ«А-ЯЁа-яё…])')
def sents(s):
    s = ID.sub('', s).strip()
    s = s.replace('…pe…', '…').replace('…Pe…', '…')
    return [x for x in SPL.split(s) if x]
seen = OrderedDict()
bad = []
for f in files:
    pl = open(P + f, encoding='utf-8').read().split('\n')
    rl = open(R + f, encoding='utf-8').read().split('\n')
    for i, (p, r) in enumerate(zip(pl, rl), 1):
        if not p.strip() or p.startswith('#'):
            continue
        ps, rs = sents(p), sents(r)
        if len(ps) != len(rs):
            bad.append((f, i, p, r))
            continue
        for a, b in zip(ps, rs):
            a2 = re.sub(r'^\((Ka|Kha)\)\s*', '', a)
            b2 = re.sub(r'^\((а|б)\)\s*', '', b)
            k = (a2, b2)
            if k in seen:
                seen[k][1] += 1
            else:
                seen[k] = [f'{f[:4]}:{i}', 1]
if mode == 'pairs':
    for (a, b), (loc, n) in seen.items():
        print(f'{loc} x{n}\n  P {a}\n  R {b}')
print('MISMATCHED SENTENCE COUNTS', len(bad))
for f, i, p, r in bad:
    print(f'{f}:{i}\n  P {p}\n  R {r}')
# Pali sentence with >1 Russian rendering
byp = {}
for (a, b), v in seen.items():
    byp.setdefault(a, []).append((b, v))
print('INCONSISTENT')
for a, lst in byp.items():
    if len(lst) > 1:
        print('P', a)
        for b, v in lst:
            print('   ', v, b)
