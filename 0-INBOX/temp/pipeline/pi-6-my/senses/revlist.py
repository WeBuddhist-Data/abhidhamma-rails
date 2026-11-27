"""List REVIEW / UNRESOLVED headwords of a gen_decisions_my.py output with: pi-6 values (count, first ids), the binding
senses (pi-5 … pi-1, with values), the Marathi pi-6 ENGLISH tags (values dropped), the mapper's kept category
(kept.tsv, from map-harmonise-notes §B). Adapted from pi-5-my/senses/revlist.py.
usage: revlist.py <gen-out.txt> <agg.tsv> [REVIEW|UNRESOLVED]"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
F = [('pi-5', 'burmese/pi-5'), ('pi-4', 'burmese/pi-4'), ('pi-3', 'burmese/pi-3'), ('pi-2', 'burmese/pi-2'),
     ('pi-1', 'burmese/pi-1')]
def load(p, keep):
    d = {}
    for l in p.read_text(encoding='utf-8-sig').splitlines():
        i = l.find(': {')
        if i < 0: continue
        hw, body = l[:i], l.strip()[i+3:-1]
        ss = []
        for s in body.split('; '):
            if ': ' in s:
                t, v = s.rsplit(': ', 1); ss.append(f'{t}: {v}' if keep else t)
        d[hw] = ss
    return d
B = [(k, load(ROOT / f'AI_translation/{p}-pali-word-burmese-senses-plain.md', True)) for k, p in F]
MR = load(ROOT / 'AI_translation/marathi/pi-6-pali-word-marathi-senses-plain.md', False)
KEPT = {}
kp = HERE / 'kept.tsv'
if kp.exists():
    for l in kp.read_text(encoding='utf-8').splitlines()[1:]:
        c = l.split('\t'); KEPT[c[0]] = c[1]
AGG = {}
for l in open(sys.argv[2], encoding='utf-8'):
    c = l.rstrip('\n').split('\t')
    if len(c) == 4: AGG[c[0]] = c[2]
def find(d, hw):
    if hw in d: return hw
    m = [k for k in d if k.lower() == hw.lower()]
    return m[0] if len(m) == 1 else None
mode = sys.argv[3] if len(sys.argv) > 3 else 'REVIEW'
on = False
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith(('REVIEW', 'UNRESOLVED', 'ERRORS', 'note')):
        on = l.startswith(mode); continue
    if not on or not l.startswith('  '): continue
    hw = l[2:].split(' [')[0].split('\t')[0]
    why = l[2:].split(' [', 1)[1].split(']:')[0] if ' [' in l and mode == 'REVIEW' else l[2:].split('\t')[1] if '\t' in l else ''
    print(f'## {hw}  ({why}) kept={KEPT.get(hw, KEPT.get(hw.lower(), "-"))}')
    print(f'   pi-6: {AGG.get(hw, "?")}')
    for k, d in B:
        m = find(d, hw)
        if m: print(f'   {k}: ' + ' || '.join(d[m]))
    m = find(MR, hw)
    if m: print('   mr-6 tags: ' + ' || '.join(MR[m]))
