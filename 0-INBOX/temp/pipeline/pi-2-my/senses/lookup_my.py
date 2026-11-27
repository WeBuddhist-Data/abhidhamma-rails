"""For each headword of an agg.tsv: pi-2 Burmese values, the pi-1 Burmese senses line (if any) and the
ENGLISH tags only of the Marathi pi-2 senses line (Marathi values dropped).
usage: python -I -X utf8 lookup_my.py <agg.tsv> [headword ...]"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY1 = ROOT / 'AI_translation/burmese/pi-1-pali-word-burmese-senses-plain.md'
MR2 = ROOT / 'AI_translation/marathi/pi-2-pali-word-marathi-senses-plain.md'

def lines(p):
    d = {}
    for l in p.read_text(encoding='utf-8-sig').splitlines():
        i = l.find(': {')
        if i > 0 and l.endswith('}'):
            d[l[:i]] = l[i + 3:-1]
    return d

def tags(body):
    return [s.rsplit(': ', 1)[0] for s in body.split('; ')]

my1, mr2 = lines(MY1), lines(MR2)
want = set(sys.argv[2:])
for l in open(sys.argv[1], encoding='utf-8-sig'):
    c = l.rstrip('\n').split('\t')
    if want and c[0] not in want:
        continue
    print('==', c[0], '|', c[2])
    print('   my1:', my1.get(c[0], '-'))
    print('   mr2 tags:', tags(mr2[c[0]]) if c[0] in mr2 else '-')
