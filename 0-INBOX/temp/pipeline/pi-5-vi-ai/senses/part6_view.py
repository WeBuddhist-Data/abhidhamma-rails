"""Part 6 helper (reads senses_tool_vi.py as a module; writes only decisions-part6.txt in 'draft' mode, if absent).
Compact view of agg-part6.tsv rows with the pi-4..pi-1 Vietnamese and pi-5 Russian prior lines,
plus a drafted decision line (copied prior tag) for headword-by-headword review.

  python -I -X utf8 -B part6_view.py view <lo> <hi> [todo]   # compact view of rows lo..hi (1-based); 'todo' = only undrafted
  python -I -X utf8 -B part6_view.py draft                   # write decisions-part6.txt draft (only if absent)
  python -I -X utf8 -B part6_view.py dec <lo> <hi>           # agg values next to the current decision line, rows lo..hi
"""
import importlib.util
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('stv', os.path.join(HERE, 'senses_tool_vi.py'))
stv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stv)

AGG = os.path.join(HERE, 'agg-part6.tsv')
DEC = os.path.join(HERE, 'decisions-part6.txt')
FUNC = {'sự', 'có', 'các', 'những', 'một', 'cách', 'khi', 'trong', 'sau', 'điều', 'thuộc', 'người', 'đã', 'đang',
        'sẽ', 'được', 'bị', 'niềm', 'trạng', 'thái', 'việc', 'của', '…'}
DONE_PARTS = ('sample', '1', '2', '3')


def core(v):
    return frozenset(t for t in re.split(r'\s+', v.lower()) if t and t not in FUNC)


def prior_idx():
    idx = {}
    for label, path in stv.PRIOR:
        d = {}
        if os.path.exists(path):
            for line in stv._lines(path):
                if ': {' in line:
                    try:
                        hw, senses = stv.parse_out_line(line)
                    except ValueError:
                        continue
                    d.setdefault(hw.lower(), senses)
        idx[label] = d
    # finished pi-5 Vietnamese parts (same family wording)
    d = {}
    for k in DONE_PARTS:
        p = os.path.join(HERE, 'sample-senses.md' if k == 'sample' else f'part{k}-senses.md')
        if os.path.exists(p):
            for line in stv._lines(p):
                try:
                    hw, senses = stv.parse_out_line(line)
                except ValueError:
                    continue
                d.setdefault(hw.lower(), senses)
    idx['pi-5 vi'] = d
    return idx


def overlap(vals, senses):
    cores = [core(v) for v in vals]
    hit = []
    for i, (t, vs) in enumerate(senses):
        pc = [core(x) for x in vs]
        if any(a and b and (a == b or a <= b or b <= a) for a in cores for b in pc):
            hit.append(i)
    return hit


def draft_line(hw, r, idx):
    vals = [stv.norm_value(v) for v in r['vals']]
    for label in ('pi-4 vi', 'pi-3 vi', 'pi-2 vi', 'pi-1 vi'):
        s = idx[label].get(hw.lower())
        if not s:
            continue
        hit = overlap(vals, s)
        if len(hit) == 1:
            return f'{hw}: {{{s[hit[0]][0]}}}', label
    ru = idx['pi-5 ru'].get(hw.lower())
    if ru and len(ru) == 1:
        return f'{hw}: {{{ru[0][0]}}}', 'ru'
    return None, 'TODO'


def view(lo, hi, only_todo=False):
    rows = stv.read_agg(AGG)
    idx = prior_idx()
    for n, (hw, r) in enumerate(rows.items(), 1):
        if n < lo or n > hi:
            continue
        vs = ' | '.join(f'{v}={c}' for v, c in r['vals'].items())
        line, src = draft_line(hw, r, idx)
        if only_todo and line is not None and len(r['vals']) == 1:
            continue
        print(f'[{n}] {hw} <{vs}>' + (f' {r["nde"]}' if r['nde'] != 'NDE=0' else '') + f'  ->{src}')
        for label in ('pi-4 vi', 'pi-3 vi', 'pi-2 vi', 'pi-1 vi', 'pi-5 vi'):
            s = idx[label].get(hw.lower())
            if s:
                print(f'    {label[:4] if label != "pi-5 vi" else "p5vi"}: '
                      + ' ‖ '.join(f'{t} = {" / ".join(v)}' for t, v in s))
        ru = idx['pi-5 ru'].get(hw.lower())
        if ru:
            print('    ru: ' + ' ‖ '.join(t for t, _ in ru))
        else:
            en = idx['pi-5 en'].get(hw.lower())
            print('    ru: none; en: ' + (' ‖ '.join(t for t, v in en) if en else 'none') + f'  [{r["eng"]}]')


def draft():
    if os.path.exists(DEC):
        sys.exit('decisions-part6.txt exists; not overwriting')
    rows = stv.read_agg(AGG)
    idx = prior_idx()
    out = ['# pi-5 (Kathāvatthu) Pāli→Vietnamese senses, part 6 (agg-part6.tsv, 903 headwords).',
           '# Hand-reviewed tag table, headword by headword, following senses-conventions.md (pi-5) §2: the approved pi-4,',
           '# then pi-3, pi-2, pi-1 Vietnamese tag where the Vietnamese values match; otherwise the approved pi-5 Russian',
           '# tag word for word; new or combined tags only where needed. Same family wording as parts 1-3.',
           '# Build: python -I -X utf8 -B senses_tool_vi.py build --part 6']
    todo = 0
    for hw, r in rows.items():
        if not r['vals']:
            continue
        line, src = draft_line(hw, r, idx)
        if line is None:
            todo += 1
            line = f'#TODO {hw}'
        out.append(line)
    with open(DEC, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(out) + '\n')
    print(f'draft written: {len(out) - 5} lines, {todo} TODO')


def dec(lo, hi):
    rows = stv.read_agg(AGG)
    d = stv.read_decisions(DEC)
    for n, (hw, r) in enumerate(rows.items(), 1):
        if n < lo or n > hi:
            continue
        vs = ' | '.join(f'{v}={c}' for v, c in r['vals'].items())
        line = stv.fmt(hw, d[hw][1]) if hw in d and d[hw][1][0][1] is not None else (
            f'{hw}: {{{d[hw][1][0][0]}}}' if hw in d else '(none)')
        print(f'[{n}] <{vs}>  {line}')


if __name__ == '__main__':
    a = [stv.nfc(x) for x in sys.argv[1:]]
    if a and a[0] == 'view':
        view(int(a[1]), int(a[2]), len(a) > 3 and a[3] == 'todo')
    elif a and a[0] == 'draft':
        draft()
    elif a and a[0] == 'dec':
        dec(int(a[1]), int(a[2]))
    else:
        sys.exit(__doc__)
