"""Show, for each headword of an agg.tsv (or the headwords given), the pi-7 Burmese values, the pi-6, pi-5, pi-4, pi-3,
pi-2 and pi-1 Burmese senses (exact, else case-insensitive matches) and the Marathi pi-7 ENGLISH tags only (values dropped).
Adapted from pi-6-my/senses/lookup_my.py.
usage: lookup_my.py <agg.tsv> | lookup_my.py -h hw [hw ...]"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
F = {'pi-6': ROOT / 'AI_translation/burmese/pi-6-pali-word-burmese-senses-plain.md',
     'pi-5': ROOT / 'AI_translation/burmese/pi-5-pali-word-burmese-senses-plain.md',
     'pi-4': ROOT / 'AI_translation/burmese/pi-4-pali-word-burmese-senses-plain.md',
     'pi-3': ROOT / 'AI_translation/burmese/pi-3-pali-word-burmese-senses-plain.md',
     'pi-2': ROOT / 'AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md',
     'pi-1': ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md',
     'mr-7': ROOT / 'AI_translation/marathi/pi-7-pali-word-marathi-senses-plain.md'}
def load(p, keep):
    d = {}
    for l in p.read_text(encoding='utf-8-sig').splitlines():
        l = l.strip()
        i = l.find(': {')
        if i < 0: continue
        hw, body = l[:i], l[i+3:-1]
        ss = []
        for s in body.split('; '):
            if ': ' in s:
                t, v = s.rsplit(': ', 1); ss.append((t, v) if keep else (t, None))
            elif ss:
                ss[-1] = (ss[-1][0] + '; ' + s, ss[-1][1])
        d[hw] = ss
    return d
D = {k: load(p, k != 'mr-7') for k, p in F.items()}
def find(d, hw):
    if hw in d: return [hw]
    return [k for k in d if k.lower() == hw.lower()]
if sys.argv[1] == '-h':
    rows = [(h, '') for h in sys.argv[2:]]
else:
    rows = [(l.split('\t')[0], l.split('\t')[2]) for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
for hw, vals in rows:
    print(f'## {hw}\t{vals}')
    for k in F:
        for m in find(D[k], hw):
            print(f'  {k} [{m}]: ' + ' || '.join(f'{t}: {v}' if v else t for t, v in D[k][m]))
