"""The brief's structural check for 2-03 and 2-05 (read-only)."""
import pathlib

d = pathlib.Path(__file__).resolve().parent
for ch in ("2-03-cittuppadakandam", "2-05-cittuppadakandam"):
    a = [l.split('] ', 1) for l in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()]
    b = [l.split('] ', 1) for l in (d / f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(', ')] != [k.split('=', 1)[0] for k in y.split(', ')]]
    print(ch, 'lines', len(a), 'bad', bad)
