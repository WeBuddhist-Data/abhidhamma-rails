"""Merge pi-2 Pāli→Hindi senses parts 1–6 into AI_translation/hindi/pi-2-pali-word-hindi-senses-plain.md,
after cross-part checks.

usage: python -I -X utf8 merge_senses_pi2.py [--write]
Checks:
  1. each part verifies against its agg-partK.tsv (senses_tool_pi2.verify);
  2. concatenated headwords equal agg-all.tsv order (NDE-only headwords excluded);
  3. no em/en dash, no "outline", grammar labels from the fixed set (reported, not fatal);
  4. consistency report: Hindi values that appear under several headwords with differing base glosses
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
import senses_tool_pi2 as T  # noqa: E402

ROOT = T.ROOT
OUT = os.path.join(ROOT, r'AI_translation\hindi\pi-2-pali-word-hindi-senses-plain.md')
GRAM = re.compile(r'\(([^()]*)\)\s*$')

fail = False
lines, order = [], []
for k in range(1, 7):
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
print('grammar labels used (top 40):')
for g, n in labels.most_common(40):
    print(f'  {n:4} ({g})')

print('\nHindi values under 3+ headwords with differing base glosses:')
for v, xs in sorted(by_val.items(), key=lambda x: -len(x[1])):
    bases = collections.Counter(b for _, b in xs)
    if len(xs) >= 3 and len(bases) > 1:
        print(f'  {v} ({len(xs)} headwords): ' +
              ' | '.join(f'{b} ×{n}' for b, n in bases.most_common(6)))

if fail:
    sys.exit('NOT MERGED: fix the failures above')
if '--write' in sys.argv:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    n_s = sum(len(T.parse_out_line(l)[1]) for l in lines)
    print(f'\nwrote {OUT}: {len(lines)} headwords, {n_s} senses')
