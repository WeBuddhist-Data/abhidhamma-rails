"""Coordinator check: structural verifier + presence check for the given parts.
Usage: python -I -X utf8 check_parts_vi.py <part> [<part> ...]"""
import pathlib
import sys

D = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(D))
import map_common_vi as m  # noqa: E402

for ch in sys.argv[1:]:
    a = [l.split('] ', 1) for l in (D / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines()]
    b = [l.split('] ', 1) for l in (D / f'{ch}.mapped.md').read_text(encoding='utf-8').splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b], ch
    bad = [i for (i, x), (_, y) in zip(a, b)
           if [k.strip() for k in x.split(', ')] != [k.split('=', 1)[0] for k in y.split(', ')]]
    nde = sum(y.count('=(no direct equivalent)') for _, y in b)
    print(ch, 'lines', len(a), 'bad', bad, 'NDE', nde)
    print('  verify:', m.verify(ch))
