"""Part 2 helper (read-only on everything except decisions-part2.draft lines it prints).
Compact view of agg-part2.tsv rows with the pi-4..pi-1 Vietnamese and pi-5 Russian prior lines,
plus a drafted decision line (copied prior tag) for review.

  python -I -X utf8 -B part2_view.py view <lo> <hi>      # compact view of rows lo..hi (1-based)
  python -I -X utf8 -B part2_view.py draft               # write decisions-part2.txt draft (only if absent)
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

AGG = os.path.join(HERE, 'agg-part2.tsv')
DEC = os.path.join(HERE, 'decisions-part2.txt')
FUNC = {'sự', 'có', 'các', 'những', 'một', 'cách', 'khi', 'trong', 'sau', 'điều', 'thuộc', 'người', 'đã', 'đang',
        'sẽ', 'được', 'bị', 'niềm', 'trạng', 'thái', 'việc', 'của', '…'}


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
    return idx


def overlap(vals, senses):
    """indices of prior senses whose values share a core with any pi-5 value"""
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


def view(lo, hi):
    rows = stv.read_agg(AGG)
    idx = prior_idx()
    for n, (hw, r) in enumerate(rows.items(), 1):
        if n < lo or n > hi:
            continue
        vs = ' | '.join(f'{v}={c}' for v, c in r['vals'].items())
        line, src = draft_line(hw, r, idx)
        print(f'[{n}] {hw} ⟨{vs}⟩' + (f' {r["nde"]}' if r['nde'] != 'NDE=0' else '') + f'  →{src}')
        for label in ('pi-4 vi', 'pi-3 vi', 'pi-2 vi', 'pi-1 vi'):
            s = idx[label].get(hw.lower())
            if s:
                print(f'    {label[:4]}: ' + ' ‖ '.join(f'{t} = {" / ".join(v)}' for t, v in s))
        ru = idx['pi-5 ru'].get(hw.lower())
        if ru:
            if len(ru) > 1 or src != 'ru':
                print('    ru: ' + ' ‖ '.join(t for t, _ in ru))
        else:
            en = idx['pi-5 en'].get(hw.lower())
            print('    ru: none; en: ' + (' ‖ '.join(f'{t} = {" / ".join(v)}' for t, v in en) if en else 'none'))
        if src == 'ru':
            print(f'    ru1: {ru[0][0]}')


def draft():
    if os.path.exists(DEC):
        sys.exit('decisions-part2.txt exists; not overwriting')
    rows = stv.read_agg(AGG)
    idx = prior_idx()
    out = ['# pi-5 (Kathāvatthu) Pāli→Vietnamese senses, part 2 (agg-part2.tsv, 908 rows).',
           '# Hand-reviewed tag table, headword by headword (senses-conventions.md §2: pi-4 … pi-1 Vietnamese tag where',
           '# the Vietnamese values match, else the pi-5 Russian tag word for word, new tags only where needed).',
           '# Build: python -I -X utf8 -B senses_tool_vi.py build --part 2']
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
    print(f'draft written: {len(out) - 4} lines, {todo} TODO')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'view':
        view(int(a[1]), int(a[2]))
    elif a and a[0] == 'draft':
        draft()
    else:
        sys.exit(__doc__)
