"""Part 3 helper (read-only viewer): compact per-headword view of agg-part3.tsv with the prior
pi-4 .. pi-1 Vietnamese and pi-5 Russian senses lines, and a draft proposal to review by hand.
Writes nothing.  python -I -X utf8 -B part3_view.py <from> <to> [todo]
"""
import os
import re
import sys
import importlib.util

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('stv', os.path.join(HERE, 'senses_tool_vi.py'))
stv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stv)

STRIP = ('trong khi ', 'sau khi ', 'khi ', 'sự ', 'có ', 'các ', 'những ', 'được ', 'đã ', 'điều ', 'việc ',
         'trạng thái ', 'người ', 'bậc ', 'một cách ')


def key(v):
    v = v.lower().strip()
    changed = True
    while changed:
        changed = False
        for p in STRIP:
            if v.startswith(p):
                v = v[len(p):]
                changed = True
    return v


def parse(line):
    try:
        return stv.parse_out_line(line)[1]
    except ValueError:
        return None


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    only_todo = len(sys.argv) > 3 and sys.argv[3] == 'todo'
    aggp, decp, _ = stv.part_paths('3')
    rows = stv.read_agg(aggp)
    dec = stv.read_decisions(decp) if os.path.exists(decp) else {}
    idx = stv._prior_index()
    hws = [h for h in rows if rows[h]['vals']]
    for n, h in enumerate(hws, 1):
        if n < lo or n > hi or (only_todo and h in dec):
            continue
        r = rows[h]
        vals = [stv.norm_value(v) for v in r['vals']]
        print(f'#{n} {h} | ' + ' | '.join(f'{v}={c}' for v, c in r['vals'].items()))
        prop = None
        for label, d in idx:
            for line in d.get(h.lower(), []):
                if label == 'pi-5 en':
                    continue
                print(f'   [{label}] {line.split(": {", 1)[1][:-1]}')
                senses = parse(line)
                if not senses or prop:
                    continue
                if label == 'pi-5 ru':
                    if len(senses) == 1:
                        prop = ('ru', [(senses[0][0], vals)])
                    continue
                # vi: map each value to a prior sense by normalised key
                groups = {}
                ok = True
                for v in vals:
                    hit = [t for t, vs in senses if key(v) in {key(x) for x in vs}]
                    if not hit:
                        ok = False
                        break
                    groups.setdefault(hit[0], []).append(v)
                if ok:
                    prop = (label, list(groups.items()))
        if prop:
            src, gs = prop
            if len(gs) == 1:
                print(f'   >> [{src}] {h}: {{{gs[0][0]}}}')
            else:
                print(f'   >> [{src}] {h}: {{' + '; '.join(t + ": " + " / ".join(v) for t, v in gs) + '}')
        else:
            print('   >> (none)')


main()
