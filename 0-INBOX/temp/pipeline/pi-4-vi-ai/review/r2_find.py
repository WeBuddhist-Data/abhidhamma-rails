"""r2 reviewer: print the first N matches of a regex in a file with char context (console only).
usage: python -I -X utf8 r2_find.py <file> <regex> [before=300] [after=300] [max=2]
"""
import re, sys
path, pat = sys.argv[1], sys.argv[2]
b = int(sys.argv[3]) if len(sys.argv) > 3 else 300
a = int(sys.argv[4]) if len(sys.argv) > 4 else 300
mx = int(sys.argv[5]) if len(sys.argv) > 5 else 2
t = open(path, encoding='utf-8').read()
for i, m in enumerate(re.finditer(pat, t)):
    if i >= mx:
        break
    ln = t.count('\n', 0, m.start()) + 1
    print('--- line', ln)
    print(t[max(0, m.start() - b): m.end() + a])
