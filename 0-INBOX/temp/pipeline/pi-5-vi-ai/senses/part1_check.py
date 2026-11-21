"""Part 1 check: sample lines unchanged in part1-senses.md and decisions-part1.txt; no CR in part 1 files."""
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))


def lines(name):
    with open(os.path.join(HERE, name), encoding='utf-8') as f:
        return [x for x in f.read().splitlines() if x.strip() and not x.startswith('#')]


for name in ('part1-senses.md', 'decisions-part1.txt', 'part1_view.py', 'part1_check.py'):
    with open(os.path.join(HERE, name), 'rb') as f:
        print(f'{name}: CR={f.read().count(b"\r")}')
for a, b in (('sample-senses.md', 'part1-senses.md'), ('decisions-sample.txt', 'decisions-part1.txt')):
    sa = lines(a)
    sb = set(lines(b))
    diff = [x for x in sa if x not in sb]
    print(f'{a} lines: {len(sa)} | missing or changed in {b}: {len(diff)}')
    for x in diff[:10]:
        print('  ' + x[:120])
