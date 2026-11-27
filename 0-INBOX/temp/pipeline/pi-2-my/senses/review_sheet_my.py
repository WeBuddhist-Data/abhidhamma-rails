"""Review sheet for the REVIEW / UNRESOLVED headwords of a gen_decisions_my.py run: values with counts,
pi-1 Burmese senses, Marathi pi-2 ENGLISH tags only, and the mapper harmonise reason (map-harmonise-notes.md).
usage: review_sheet_my.py <gen-out.txt> <agg.tsv>"""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gen_decisions_my as g
notes = (HERE.parent / 'mapper-my/map-harmonise-notes.md').read_text(encoding='utf-8')
why = {}
for l in notes.splitlines():
    m = re.match(r'^\| ([^|]+?) \| ([^|]+) \| (.+) \|$', l)
    if m and m.group(1) not in ('keyword', '---'):
        why.setdefault(m.group(1).lower(), []).append(m.group(2) + ' || ' + m.group(3))
rows = g.read_agg(sys.argv[2])
my1 = g.read_senses(g.MY1_SENSES, True)
mr = g.read_senses(g.MR_SENSES, False)
hws = []
for l in open(sys.argv[1], encoding='utf-8'):
    m = re.match(r'^  (\S.*?)(?: \[|\t)', l)
    if m and m.group(1) in rows:
        hws.append(m.group(1))
for hw in hws:
    print('==', hw, '|', ' | '.join(f'{v}={c}' for v, c in rows[hw].items()))
    k = g.lookup(my1, hw)
    if k: print('   my1:', my1[k])
    k2 = g.lookup(mr, hw)
    if k2: print('   mr :', mr[k2])
    for w in why.get(hw.lower(), []): print('   why:', w[:600])
