"""r2 reviewer: print reference segments by block ID to the console only (never writes files).
usage: python -I -X utf8 r2_ts.py <file> <id1> [<id2> ...]   (ids without caret, e.g. 4-45)
"""
import re, sys

path = sys.argv[1]
ids = sys.argv[2:]
text = open(path, encoding='utf-8').read().replace('\r', '')
segs = {}
order = []
buf = []
for line in text.split('\n'):
    buf.append(line)
    m = re.search(r'\^([0-9A-Za-z\-]+)\s*$', line)
    if m:
        segs[m.group(1)] = '\n'.join(l for l in buf if l.strip())
        order.append(m.group(1))
        buf = []
for i in ids:
    print('=====', i)
    print(segs.get(i, '<<missing>>'))
