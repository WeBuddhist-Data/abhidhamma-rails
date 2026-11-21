"""Part 1 helper (read-only use of senses_tool_vi.py; writes nothing).
  python -I -X utf8 part1_helper.py prior <i> <j>   # prior lines for todo headwords [i:j] of part 1
  python -I -X utf8 part1_helper.py cmp             # sample decision lines copied unchanged into decisions-part1.txt?
  python -I -X utf8 part1_helper.py todo <i> <j>    # compact todo rows [i:j]
"""
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import senses_tool_vi as T  # noqa: E402

agg, dec, out = T.part_paths('1')


def todo_list():
    rows = T.read_agg(agg)
    d = T.read_decisions(dec) if os.path.exists(dec) else {}
    return rows, [h for h in rows if h not in d and rows[h]['vals']]


a = sys.argv[1:]
if a and a[0] == 'prior':
    rows, left = todo_list()
    i, j = int(a[1]), int(a[2])
    print(f'todo {len(left)}; showing {i}:{j}')
    T.prior(left[i:j], rows)
elif a and a[0] == 'todo':
    rows, left = todo_list()
    i, j = int(a[1]), int(a[2])
    print(f'todo {len(left)}')
    for h in left[i:j]:
        r = rows[h]
        print(h + '\t' + ' | '.join(f'{v}={c}' for v, c in r['vals'].items()) + '\t' + r['eng'])
elif a and a[0] == 'cmp':
    def lines(p):
        with open(p, encoding='utf-8-sig') as f:
            return [T.nfc(x.strip()) for x in f if x.strip() and not x.startswith('#')]
    s = lines(os.path.join(HERE, 'decisions-sample.txt'))
    p = set(lines(dec))
    miss = [x for x in s if x not in p]
    print(f'sample decision lines: {len(s)}; missing or changed in part 1: {len(miss)}')
    for x in miss:
        print('  ' + x)
else:
    print(__doc__)
