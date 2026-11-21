"""Part 1 helper (read-only viewer + one-time init). Run with python -I -X utf8 -B.

  part1_view.py init                 copy decisions-sample.txt lines (unchanged) into a new decisions-part1.txt
  part1_view.py view <lo> <hi> [w]   compact view of todo headwords (rows lo..hi of the todo list):
                                     values with counts and first ids, en hint, ru / pi-4 / pi-3 / pi-2 / pi-1 vi lines
                                     (each prior line cut to w chars, default 260)
"""
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
ROOT = r'D:\Work\OpenPecha\abhidhamma-rails'
HERE = os.path.dirname(os.path.abspath(__file__))
AGG = os.path.join(HERE, 'agg-part1.tsv')
DEC = os.path.join(HERE, 'decisions-part1.txt')
SAMPLE = os.path.join(HERE, 'decisions-sample.txt')
PRIOR = [
    ('ru', os.path.join(ROOT, r'AI_translation\russian\pi-5-pali-word-russian-senses-plain.md')),
    ('v4', os.path.join(ROOT, r'AI_translation\vietnamese\pi-4-pali-word-vietnamese-senses-plain.md')),
    ('v3', os.path.join(ROOT, r'AI_translation\vietnamese\pi-3-pali-word-vietnamese-senses-plain.md')),
    ('v2', os.path.join(ROOT, r'AI_translation\vietnamese\pi-2-pali-word-vietnamese-senses-plain.md')),
    ('v1', os.path.join(ROOT, r'AI_translation\vietnamese\pi-1-pali-word-vietnamese-senses-plain.md')),
]
VAL_RE = re.compile(r'^(.*)=(\d+)\[([^\]]*)\]$')


def nfc(s):
    return unicodedata.normalize('NFC', s)


def lines(p):
    with open(p, encoding='utf-8-sig') as f:
        return [nfc(x) for x in f.read().splitlines()]


def dec_hws(p):
    out = set()
    if os.path.exists(p):
        for x in lines(p):
            x = x.strip()
            if x and not x.startswith('#') and ': {' in x:
                out.add(x.split(': {', 1)[0])
    return out


def init():
    if os.path.exists(DEC):
        sys.exit('decisions-part1.txt exists already')
    body = [x for x in lines(SAMPLE) if x.strip() and not x.startswith('#')]
    head = ['# pi-5 (Kathāvatthu) Pāli→Vietnamese senses, part 1 (agg-part1.tsv). Hand-written tag table, headword by headword.',
            '# The first block is copied unchanged from decisions-sample.txt (approved 2026-11-21); the rest follows senses-conventions.md.',
            '# Build: python -I -X utf8 -B senses_tool_vi.py build --part 1']
    with open(DEC, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(head + body) + '\n')
    print(f'wrote {len(body)} sample lines -> {DEC}')


def view(lo, hi, w):
    idx = []
    for lab, p in PRIOR:
        d = {}
        for x in lines(p):
            if ': {' in x:
                d.setdefault(x.split(': {', 1)[0].lower(), []).append(x)
        idx.append((lab, d))
    done = dec_hws(DEC)
    todo = []
    for x in lines(AGG):
        if not x.strip():
            continue
        hw, eng, viet, nde = x.split('\t')
        if hw in done or not viet.strip():
            continue
        todo.append((hw, eng, viet, nde))
    print(f'todo: {len(todo)}')
    for n, (hw, eng, viet, nde) in enumerate(todo[lo - 1:hi], lo):
        vals = []
        for it in viet.split(' | '):
            m = VAL_RE.match(it.strip())
            ids = m.group(3).split(',')
            vals.append(f'{m.group(1)}={m.group(2)}[{",".join(ids[:3])}]')
        e = eng.replace('en≈ ', '')
        print(f'#{n} {hw} || ' + ' | '.join(vals) + f' || {e[:90]}' + ('' if nde == 'NDE=0' else f' || {nde}'))
        for lab, d in idx:
            for y in d.get(hw.lower(), []):
                y = y.split(': {', 1)[1]
                print(f'   {lab} {y[:w]}')


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'init':
        init()
    elif len(a) >= 3 and a[0] == 'view':
        view(int(a[1]), int(a[2]), int(a[3]) if len(a) > 3 else 260)
    else:
        sys.exit(__doc__)
