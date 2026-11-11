import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parents[5]
d = pathlib.Path(__file__).parent
ch = '1-khandhavibhango'


def segs(path):
    out, buf, order = {}, [], []
    for line in path.read_text(encoding='utf-8').splitlines():
        buf.append(line)
        m = re.search(r'\^([\w-]+)\s*$', line)
        if m:
            out[m.group(1)] = '\n'.join(x for x in buf if x.strip()); buf = []; order.append(m.group(1))
    return out, order


P, order = segs(root / 'AI_translation' / 'pali' / 'pi-2_split_chapters' / f'{ch}.md')
E, _ = segs(d / f'{ch}.en.md')
K = {}
for line in (d / f'{ch}.keywords.md').read_text(encoding='utf-8').splitlines():
    sid, kws = line.split('] ', 1)
    K[sid[1:]] = kws
a, b = sys.argv[1], sys.argv[2]
what = sys.argv[3] if len(sys.argv) > 3 else 'pek'
on = False
for sid in order:
    if sid == a: on = True
    if on and what == 'd':
        ls = [l for l in P[sid].splitlines() if l.startswith(('Duvidhena', 'Tividhena'))]
        print(sid, ' | '.join(l[:120] for l in ls), '| lines', len(P[sid].splitlines()))
    elif on:
        print('=====', sid)
        if 'p' in what: print('P:', P[sid])
        if 'e' in what: print('E:', E.get(sid))
        if 'k' in what: print('K:', K.get(sid))
    if sid == b: break
