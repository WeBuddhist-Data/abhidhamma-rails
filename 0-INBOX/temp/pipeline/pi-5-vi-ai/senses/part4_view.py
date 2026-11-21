"""Part 4 helper (reads only; writes nothing).
Compact view of agg-part4.tsv rows with the pi-4..pi-1 Vietnamese and pi-5 Russian prior lines and the
drafted (copied prior) tag, for review row by row.

  python -I -X utf8 -B part4_view.py view <lo> <hi>      # rows lo..hi (1-based)
  python -I -X utf8 -B part4_view.py todo                # rows with no draftable prior tag (need a hand tag)
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

AGG = os.path.join(HERE, 'agg-part4.tsv')
DEC = os.path.join(HERE, 'decisions-part4.txt')
FUNC = {'sự', 'có', 'các', 'những', 'một', 'cách', 'khi', 'trong', 'sau', 'điều', 'thuộc', 'người', 'đã', 'đang',
        'sẽ', 'được', 'bị', 'niềm', 'trạng', 'thái', 'việc', 'của', '…'}


def core(v):
    toks = [t for t in re.split(r'\s+', v.lower()) if t]
    return frozenset(t for t in toks if t not in FUNC) or frozenset(toks)


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


def match(a, b):
    return a and b and (a == b or a <= b or b <= a)


def overlap(vals, senses):
    """indices of prior senses whose values share a core with any pi-5 value; and the pi-5 values matched"""
    cores = [core(v) for v in vals]
    hit, covered = [], set()
    for i, (t, vs) in enumerate(senses):
        pc = [core(x) for x in vs]
        ok = [j for j, a in enumerate(cores) if any(match(a, b) for b in pc)]
        if ok:
            hit.append(i)
            covered.update(ok)
    return hit, covered


def draft_line(hw, r, idx):
    vals = [stv.norm_value(v) for v in r['vals']]
    hints = {h.lower() for h in r['hints']}
    for label in ('pi-4 vi', 'pi-3 vi', 'pi-2 vi', 'pi-1 vi'):
        s = idx[label].get(hw.lower())
        if not s:
            continue
        hit, cov = overlap(vals, s)
        if len(hit) == 1:
            flag = '' if len(cov) == len(vals) else ' PARTIAL'
            pc = {core(x) for x in s[hit[0]][1]}
            if not any(core(v) in pc for v in vals):
                flag += ' VALDIFF[' + ' / '.join(s[hit[0]][1]) + ']'
            return s[hit[0]][0], label + flag
    ru = idx['pi-5 ru'].get(hw.lower())
    if ru and len(ru) == 1:
        t = ru[0][0]
        return t, 'ru' + (' BAREHINT' if t.lower() in hints else '')
    return None, 'TODO'


def view(lo, hi, only_todo=False):
    rows = stv.read_agg(AGG)
    idx = prior_idx()
    for n, (hw, r) in enumerate(rows.items(), 1):
        if n < lo or n > hi or not r['vals']:
            continue
        tag, src = draft_line(hw, r, idx)
        if only_todo and tag is not None and src in ('ru', 'pi-4 vi', 'pi-3 vi', 'pi-2 vi', 'pi-1 vi'):
            continue
        vs = ' | '.join(f'{v}={c}' for v, c in r['vals'].items())
        print(f'[{n}] {hw} <{vs}>  en: {", ".join(r["hints"][:3])}  ->{src}: {tag}')
        for label in ('pi-4 vi', 'pi-3 vi', 'pi-2 vi', 'pi-1 vi'):
            s = idx[label].get(hw.lower())
            if s and (len(s) > 1 or not src.startswith(label) or 'PARTIAL' in src):
                print(f'    {label[:4]}: ' + ' || '.join(f'{t} = {" / ".join(v)}' for t, v in s))
        ru = idx['pi-5 ru'].get(hw.lower())
        if ru and (len(ru) > 1 or src != 'ru'):
            print('    ru: ' + ' || '.join(t for t, _ in ru))


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'view':
        view(int(a[1]), int(a[2]))
    elif a and a[0] == 'todo':
        view(1, 10 ** 6, only_todo=True)
    elif a and a[0] == 'rucheck':   # ru-drafted rows that have a pi-1 … pi-4 Vietnamese line
        rows = stv.read_agg(AGG)
        idx = prior_idx()
        for n, (hw, r) in enumerate(rows.items(), 1):
            if not r['vals']:
                continue
            tag, src = draft_line(hw, r, idx)
            if src.startswith('ru') and any(idx[l].get(hw.lower()) for l in ('pi-4 vi', 'pi-3 vi', 'pi-2 vi', 'pi-1 vi')):
                view(n, n)
    else:
        sys.exit(__doc__)
