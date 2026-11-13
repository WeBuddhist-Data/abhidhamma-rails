"""The brief's one-line verifier, unchanged, for each file given (must print bad []).
usage: python -I -B -X utf8 briefcheck_4-15_5-04_hi.py <file> [<file> …]   (run from the repo root)
"""
import pathlib, sys
d = pathlib.Path('0-INBOX/temp/pipeline/pi-7-hi/mapper-hi')
for ch in sys.argv[1:]:
    a = [l.split('] ', 1) for l in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()]
    b = [l.split('] ', 1) for l in (d / f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for i, (x, y) in enumerate(zip(a, b)) if len(x) > 1 and [k.strip() for k in x[1].split(', ')] != [k.split('=', 1)[0] for k in y[1].split(', ')]]
    print(ch, 'lines', len(a), 'bad', bad)
