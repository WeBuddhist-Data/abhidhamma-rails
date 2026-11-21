# adapted 2026-11-20 from pi-2-vi-ai/senses/merge_senses_vi.py (pi-3: 3 parts, pi-3 output path)
"""Merge pi-3 Pāli→Vietnamese senses parts 1–3 into AI_translation/vietnamese/pi-3-pali-word-vietnamese-senses-plain.md,
after cross-part checks.

usage: python -I -X utf8 merge_senses_vi.py [--write]
Checks:
  1. each part verifies against its agg-partK.tsv (senses_tool_vi.verify);
  2. concatenated headwords equal agg-all.tsv order (NDE-only headwords excluded);
  3. no em/en dash, no "outline", grammar labels (reported, not fatal);
  4. consistency report: Vietnamese values that appear under several headwords with differing base glosses
     (tag with the trailing "(...)" stripped), for values used by 3+ headwords.
"""
import collections
import io
import os
import re
import sys
from contextlib import redirect_stdout

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import senses_tool_vi as T  # noqa: E402

ROOT = T.ROOT
OUT = os.path.join(ROOT, r'AI_translation\vietnamese\pi-3-pali-word-vietnamese-senses-plain.md')
GRAM = re.compile(r'\(([^()]*)\)\s*$')
N_PARTS = 3

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
print('grammar labels used (top 25):')
for g, n in labels.most_common(25):
    print(f'  {n:4} ({g})')

print('\nVietnamese values under 3+ headwords with differing base glosses (top 40):')
shown = 0
for v, xs in sorted(by_val.items(), key=lambda x: -len(x[1])):
    bases = collections.Counter(b for _, b in xs)
    if len(xs) >= 3 and len(bases) > 1 and shown < 40:
        shown += 1
        print(f'  {v} ({len(xs)} headwords): ' +
              ' | '.join(f'{b[:60]} ×{n}' for b, n in bases.most_common(4)))

if fail:
    sys.exit('NOT MERGED: fix the failures above')

# User-added senses (not attested in the keyword map, so the part tool cannot build them): appended to the
# headword's senses line after the merge, as the last sense(s), so existing sense indices stay unchanged.
USER_EXTRA = {}
for i, l in enumerate(lines):
    hw = T.parse_out_line(l)[0]
    if hw in USER_EXTRA:
        assert l.endswith('}'), l
        lines[i] = l[:-1] + '; ' + USER_EXTRA[hw] + '}'
        T.parse_out_line(lines[i])
        print(f'user-added sense: {hw}: {USER_EXTRA[hw]}')
if '--write' in sys.argv:
    with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    n_s = sum(len(T.parse_out_line(l)[1]) for l in lines)
    print(f'\nwrote {OUT}: {len(lines)} headwords, {n_s} senses')
