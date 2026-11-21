# r2 helper: print a character window around each regex match (console only, writes nothing).
# usage: python -I -X utf8 r2_kw.py <file> <regex> [window]
import re, sys
path, pat = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 300
t = open(path, encoding='utf-8').read()
for m in re.finditer(pat, t):
    s = max(0, m.start() - w); e = min(len(t), m.end() + w)
    print('--- @%d' % m.start())
    print(t[s:e].replace('\n', ' / '))
