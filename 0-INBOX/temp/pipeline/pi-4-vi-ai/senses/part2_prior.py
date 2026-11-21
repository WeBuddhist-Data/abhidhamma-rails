"""Part 2 helper (read-only use of senses_tool_vi.py): compact prior view for a slice of agg-part2.tsv.
python -I -X utf8 part2_prior.py <start> <end> [en]   (1-based row numbers, inclusive)
Prints: #n hw | values ; then [3]/[2]/[1] pi-3/pi-2/pi-1 vi bodies and [ru] pi-4 ru body (only when present)."""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('stv', os.path.join(HERE, 'senses_tool_vi.py'))
stv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stv)

rows = stv.read_agg(os.path.join(HERE, 'agg-part2.tsv'))
idx = stv._prior_index()
labels = {'pi-3 vi': '3', 'pi-2 vi': '2', 'pi-1 vi': '1', 'pi-4 ru': 'ru', 'pi-4 en': 'en'}
a, b = int(sys.argv[1]), int(sys.argv[2])
show_en = len(sys.argv) > 3
for n, (hw, r) in enumerate(rows.items(), 1):
    if n < a or n > b:
        continue
    print(f'#{n} {hw} | ' + ' | '.join(f'{v}={c}' for v, c in r['vals'].items()))
    for label, d in idx:
        if label == 'pi-4 en' and not show_en:
            continue
        for line in d.get(hw.lower(), []):
            print(f'  [{labels[label]}] ' + line.split(': {', 1)[1][:-1])
