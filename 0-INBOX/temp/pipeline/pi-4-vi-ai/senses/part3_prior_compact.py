"""Part 3 helper (read-only use of senses_tool_vi.py): compact prior view for a slice of agg-part3.tsv.
Usage: python -I -X utf8 part3_prior_compact.py <start row 1-based> <end row inclusive>
Prints: row no, headword, values; then [vi3]/[vi2]/[vi1] full prior lines (body only) and [ru] tags only.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import senses_tool_vi as T  # noqa: E402

a, b = int(sys.argv[1]), int(sys.argv[2])
rows = T.read_agg(os.path.join(HERE, 'agg-part3.tsv'))
idx = T._prior_index()
labels = {'pi-3 vi': 'vi3', 'pi-2 vi': 'vi2', 'pi-1 vi': 'vi1', 'pi-4 ru': 'ru'}
for n, (hw, r) in enumerate(rows.items(), 1):
    if n < a or n > b:
        continue
    print(f'{n} {hw} | ' + ' | '.join(f'{v}={c}' for v, c in r['vals'].items()))
    for label, d in idx:
        if label not in labels:
            continue
        for line in d.get(hw.lower(), []):
            body = line.split(': {', 1)[1][:-1]
            if label == 'pi-4 ru':
                try:
                    _, senses = T.parse_out_line(line)
                    body = ' || '.join(t for t, _ in senses)
                except ValueError:
                    pass
            print(f'   {labels[label]}: {body}')
