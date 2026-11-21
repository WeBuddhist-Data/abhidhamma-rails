"""Part 5 helper (read-only): print a DRAFT decision line per headword of agg-part5.tsv for hand review.
Source order as senses-conventions.md §2: pi-4, pi-3, pi-2, pi-1 Vietnamese tag when every attested value
matches a value of that line (after stripping sự / có / classifiers / aspect words / case / gaps); otherwise
the pi-5 Russian tag when the Russian line has one sense. Everything else is flagged for a hand decision.
Writes nothing.   python -I -X utf8 -B part5_draft.py <from> <to> [flagged]
"""
import os
import sys
import importlib.util

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('stv', os.path.join(HERE, 'senses_tool_vi.py'))
stv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stv)

STRIP = ('trong khi ', 'sau khi ', 'khi ', 'sự ', 'có ', 'các ', 'những ', 'được ', 'đã ', 'điều ', 'việc ',
         'trạng thái ', 'người ', 'bậc ', 'một cách ', 'đang ', 'sẽ ', 'thuộc ', 'vị ', 'kẻ ', 'nỗi ', 'cái ')


def key(v):
    v = v.lower().replace(' … ', ' ').replace('…', ' ').strip()
    v = ' '.join(v.split())
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


def propose(h, r, idx):
    """-> (decision line or None, source label, notes, prior lines)"""
    vals = [stv.norm_value(v) for v in r['vals']]
    hints = {x.lower() for x in r['hints']}
    prop, src, notes, priors = None, None, [], []
    for label, d in idx:
        if label == 'pi-5 en':
            continue
        for line in d.get(h.lower(), []):
            priors.append((label, line))
    for label, line in priors:
        if label == 'pi-5 ru' or prop:
            continue
        senses = parse(line)
        if not senses:
            continue
        groups = {}
        ok = True
        for v in vals:
            hit = [t for t, vs in senses if key(v) in {key(x) for x in vs}]
            if not hit:
                ok = False
                break
            groups.setdefault(hit[0], []).append(v)
        if ok:
            prop, src = list(groups.items()), label
    if [p for p in priors if p[0] != 'pi-5 ru'] and not prop:
        notes.append('VI-MISMATCH')
    if not prop:
        ru = [parse(l) for lab, l in priors if lab == 'pi-5 ru']
        ru = [s for s in ru if s]
        if ru and len(ru[0]) == 1:
            prop, src = [(ru[0][0][0], vals)], 'ru'
        elif ru:
            notes.append('RU-MULTI')
        else:
            notes.append('NO-PRIOR')
    if prop:
        for t, _ in prop:
            if t.lower() in hints:
                notes.append('HINT')
    if len(vals) > 1:
        notes.append('MULTIVAL')
    if prop and len(prop) == 1:
        dl = f'{h}: {{{prop[0][0]}}}'
    elif prop:
        dl = f'{h}: {{' + '; '.join(t + ': ' + ' / '.join(v) for t, v in prop) + '}'
    else:
        dl = None
    return dl, src, notes, priors


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    flagged_only = len(sys.argv) > 3 and sys.argv[3] == 'flagged'
    aggp, _, _ = stv.part_paths('5')
    rows = stv.read_agg(aggp)
    idx = stv._prior_index()
    hws = [h for h in rows if rows[h]['vals']]
    for n, h in enumerate(hws, 1):
        if n < lo or n > hi:
            continue
        r = rows[h]
        dl, src, notes, priors = propose(h, r, idx)
        if flagged_only and not notes:
            continue
        vs = ' | '.join(f'{v}={c}' for v, c in r['vals'].items())
        print(f'{dl or h + ": ??"}\t## #{n} {src or "-"} {" ".join(notes)} :: {vs}')
        if notes:
            for label, line in priors:
                print(f'     [{label}] {line.split(": {", 1)[1][:-1][:260]}')


if __name__ == '__main__':
    main()
