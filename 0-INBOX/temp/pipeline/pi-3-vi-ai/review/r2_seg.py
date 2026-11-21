# r2 helper: print segments by block-ID range from a block-aligned file (console only, writes nothing).
# usage: python -I -X utf8 r2_seg.py <file> <first_num> <last_num> [maxchars]
import re, sys
path, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 0
text = open(path, encoding='utf-8').read()
segs = []
buf = []
for line in text.split('\n'):
    buf.append(line)
    m = re.search(r'\^(3-[0-9a-z-]+)\s*$', line)
    if m:
        segs.append((m.group(1), '\n'.join(l for l in buf if l.strip())))
        buf = []
def num(i):
    p = i.split('-')
    return int(p[1]) if len(p) == 2 and p[1].isdigit() else None
on = False
for i, s in segs:
    n = num(i)
    if n == a:
        on = True
    if on:
        out = s if not mx else s[:mx]
        print('=== ' + i)
        print(out)
    if n == b:
        on = False
