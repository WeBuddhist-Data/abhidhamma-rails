"""Part 5 helper (read-only viewer): compact per-headword view of agg-part5.tsv with the prior
pi-4 .. pi-1 Vietnamese and pi-5 Russian senses lines, the pi-5 English hint, and decision lines of
finished parts (sample, 2, 3) sharing a word with the headword (family wording). Writes nothing.
  python -I -X utf8 -B part5_view.py <from> <to> [todo]
"""
import os
import sys
import importlib.util

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('stv', os.path.join(HERE, 'senses_tool_vi.py'))
stv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stv)


def fam_index():
    idx = {}
    for name in ('decisions-sample.txt', 'decisions-part2.txt', 'decisions-part3.txt'):
        p = os.path.join(HERE, name)
        if not os.path.exists(p):
            continue
        for line in stv._lines(p):
            if line.startswith('#') or ': {' not in line:
                continue
            hw = line.split(': {', 1)[0]
            for tok in hw.lower().split():
                idx.setdefault(tok, []).append(line)
    return idx


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    only_todo = len(sys.argv) > 3 and sys.argv[3] == 'todo'
    aggp, decp, _ = stv.part_paths('5')
    rows = stv.read_agg(aggp)
    dec = stv.read_decisions(decp) if os.path.exists(decp) else {}
    idx = stv._prior_index()
    fam = fam_index()
    hws = [h for h in rows if rows[h]['vals']]
    for n, h in enumerate(hws, 1):
        if n < lo or n > hi or (only_todo and h in dec):
            continue
        r = rows[h]
        print(f'#{n} {h} | ' + ' | '.join(f'{v}={c}' for v, c in r['vals'].items())
              + f' || {r["eng"][3:].strip()[:80]}')
        for label, d in idx:
            for line in d.get(h.lower(), []):
                body = line.split(': {', 1)[1][:-1]
                print(f'   [{label}] {body[:300]}')
        toks = h.lower().split()
        if len(toks) > 1:
            seen = set()
            for t in toks:
                for line in fam.get(t, [])[:2]:
                    if line not in seen:
                        seen.add(line)
                        print(f'   [fam] {line[:200]}')


main()
