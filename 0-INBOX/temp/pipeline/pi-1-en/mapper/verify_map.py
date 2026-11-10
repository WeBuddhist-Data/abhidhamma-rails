import pathlib, sys
d = pathlib.Path('0-INBOX/temp/pipeline/pi-1-en/mapper')
for ch in sys.argv[1:]:
    a = [l.split('] ', 1) for l in (d/f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()]
    b = [l.split('] ', 1) for l in (d/f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b) if [k.strip() for k in x.split(', ')] != [k.rsplit('=', 1)[1] for k in y.split(', ')]]
    print(ch, 'lines', len(a), 'bad', bad)