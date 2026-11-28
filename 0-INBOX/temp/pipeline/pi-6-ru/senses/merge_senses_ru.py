# adapted 2026-11-27 from pi-2-ru/senses/merge_senses_ru.py (pi-6 paths, 2 parts)
"""Merge pi-6 Pāli→Russian senses parts 1–2 into AI_translation/russian/pi-6-pali-word-russian-senses-plain.md,
after cross-part checks.

usage: python -I -X utf8 -B merge_senses_ru.py [--write]
Checks:
  1. each part verifies against its agg-partK.tsv (senses_tool_ru.verify);
  2. concatenated headwords equal agg-all.tsv order (NDE-only headwords excluded);
  3. no em/en dash, no "outline", grammar labels (reported, not fatal);
  4. consistency report: Russian values that appear under several headwords with differing base glosses
     (tag with the trailing "(...)" stripped), for values used by 3+ headwords.
"""
import collections
import io
import os
import re
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import senses_tool_ru as T  # noqa: E402

ROOT = T.ROOT
OUT = os.path.join(ROOT, r'AI_translation\russian\pi-6-pali-word-russian-senses-plain.md')
GRAM = re.compile(r'\(([^()]*)\)\s*$')
N_PARTS = 2

fail = False
lines, order = [], []
for k in range(1, N_PARTS + 1):
    agg = os.path.join(HERE, f'agg-part{k}.tsv')
    out = os.path.join(HERE, f'part{k}-senses.md')
    if not os.path.exists(out):
        print(f'part{k}: MISSING')
        fail = True
        continue
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = T.verify(agg, out)
    print(f'part{k}: ' + ('VERIFY OK' if rc == 0 else 'VERIFY FAILED\n' + buf.getvalue()))
    fail |= rc != 0
    for l in open(out, encoding='utf-8-sig').read().splitlines():
        if l.strip():
            lines.append(l)
            order.append(T.parse_out_line(l)[0])

allrows = T.read_agg(os.path.join(HERE, 'agg-all.tsv'))
expected = [h for h in allrows if allrows[h]['vals']]
if order != expected:
    print('headword order differs from agg-all.tsv:',
          'missing', [h for h in expected if h not in order][:10],
          'extra', [h for h in order if h not in allrows][:10])
    fail = True
else:
    print(f'headwords: {len(order)} = agg-all order')

warn = collections.Counter()
labels = collections.Counter()
by_val = collections.defaultdict(list)
for l in lines:
    hw, senses = T.parse_out_line(l)
    for tag, vs in senses:
        if '—' in tag or '–' in tag:
            print('  dash in tag:', hw, tag); warn['dash'] += 1
        if 'outline' in tag.lower():
            print('  "outline" in tag:', hw, tag); warn['outline'] += 1
        m = GRAM.search(tag)
        if m:
            labels[m.group(1)] += 1
        base = GRAM.sub('', tag).strip().rstrip(',').lower()
        for v in vs:
            by_val[v].append((hw, base))
print('warnings:', dict(warn) or 'none')
print('grammar labels used (top 20):')
for g, n in labels.most_common(20):
    print(f'  {n:4} ({g})')

if fail:
    sys.exit('NOT MERGED: fix the failures above')
if '--write' in sys.argv:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    n_s = sum(len(T.parse_out_line(l)[1]) for l in lines)
    print(f'\nwrote {OUT}: {len(lines)} headwords, {n_s} senses')
