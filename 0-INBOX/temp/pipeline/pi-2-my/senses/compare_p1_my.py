"""Compare a pi-2 senses file with the pi-1 Burmese senses: per headword, where its senses come from.
usage: python -I -X utf8 compare_p1_my.py <senses.md>"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gen_decisions_my as g  # noqa: E402

my1 = g.read_senses(g.MY1_SENSES, True)
cnt = {}
for line in open(sys.argv[1], encoding='utf-8'):
    line = line.rstrip('\n')
    if not line:
        continue
    hw, s = g.parse_line(line)
    k = g.lookup(my1, hw)
    if not k:
        kind = 'new in pi-2 (Marathi tag or MANUAL)'
    else:
        p1 = my1[k]
        p1t = [t for t, _ in p1]
        tags = [t for t, _ in s]
        if [(t, set(v)) for t, v in s] == [(t, set(v)) for t, v in p1]:
            kind = 'pi-1 senses unchanged'
        elif all(t in p1t for t in tags) and all(set(vs) <= set(dict(p1)[t]) for t, vs in s):
            kind = 'pi-1 senses, subset attested'
        else:
            kind = 'pi-1 senses + pi-2 change'
        if k != hw:
            kind += f' (pi-1 headword {k!r})'
        if kind.startswith('pi-1 senses + '):
            print(f'{hw}:\n   pi-1: {p1}\n   pi-2: {s}')
    cnt[kind.split(' (')[0]] = cnt.get(kind.split(' (')[0], 0) + 1
    if '(pi-1 headword' in kind:
        print(f'  case match: {hw} -> {k}  [{kind.split(" (")[0]}]')
print(cnt)
