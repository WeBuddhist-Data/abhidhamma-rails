"""Lint a senses file: tag = value, empty tag, '/' or ';' inside a candidate, Myanmar/Devanagari in tags,
the same tag twice in one line. usage: lint_senses_my.py <senses.md>"""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gen_decisions_my as g
bad = 0
for n, l in enumerate(open(sys.argv[1], encoding='utf-8'), 1):
    hw, s = g.parse_line(l.rstrip('\n'))
    if s is None:
        print(n, 'unparsable'); bad += 1; continue
    tags = [t for t, _ in s]
    if len(set(tags)) != len(tags): print(n, hw, 'duplicate tag'); bad += 1
    for t, vs in s:
        if not t or re.search(r'[ऀ-ॿက-႟]', t): print(n, hw, 'bad tag', t); bad += 1
        for v in vs:
            if v == t: print(n, hw, 'tag = value'); bad += 1
            if '/' in v or ';' in v or not v: print(n, hw, 'bad candidate', repr(v)); bad += 1
print('lint problems:', bad)
