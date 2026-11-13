"""The brief's structural verifier, verbatim, for 7-06 .. 7-11 (run from the repo root)."""
import pathlib
d = pathlib.Path('0-INBOX/temp/pipeline/pi-6-hi/mapper-hi')
for ch in [f"7-{i:02d}-anusayayamaka" for i in range(6, 12)]:
    a = [l.split('] ', 1) for l in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()]
    b = [l.split('] ', 1) for l in (d / f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for i, (x, y) in enumerate(zip(a, b)) if len(x) > 1 and [k.strip() for k in x[1].split(', ')] != [k.split('=', 1)[0] for k in y[1].split(', ')]]
    print(ch, 'lines', len(a), 'bad', bad)
