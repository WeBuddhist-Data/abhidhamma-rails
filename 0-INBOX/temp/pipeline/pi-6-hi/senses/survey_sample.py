"""Survey helper for the pi-6 Hindi senses sample: list headwords of agg-part1..3 whose Hindi values match
a regex (to settle conventions for the parts). Usage: python -I -X utf8 survey_sample.py <regex> [multi]
'multi' = only headwords with more than one attested value."""
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
pat = re.compile(sys.argv[1])
multi = len(sys.argv) > 2 and sys.argv[2] == 'multi'
for k in (1, 2, 3):
    for n, line in enumerate(open(os.path.join(HERE, f'agg-part{k}.tsv'), encoding='utf-8-sig'), 1):
        cols = line.rstrip('\r\n').split('\t')
        if len(cols) != 4:
            continue
        hw, eng, hin, nde = cols
        vals = [re.sub(r'\[[^\]]*\]$', '', v.strip()) for v in hin.split(' | ') if v.strip()]
        if multi and len(vals) < 2:
            continue
        if any(pat.search(v.rsplit('=', 1)[0]) for v in vals) or pat.search(hw):
            print(f'p{k}:{n}\t{hw}\t{" | ".join(vals)}\t{eng[:70]}')
