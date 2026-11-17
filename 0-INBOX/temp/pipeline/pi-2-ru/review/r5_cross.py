import re, sys
# usage: r5_cross.py <file> <before> <after> <maxhits> <pattern> [<pattern> ...]
path, before, after, maxhits = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
txt = open(path, encoding='utf-8').read()
for pat in sys.argv[5:]:
    print('#####', pat)
    n = 0
    for m in re.finditer(pat, txt):
        s = max(0, m.start() - before)
        e = min(len(txt), m.end() + after)
        # find block id after
        idm = re.search(r'\^[0-9a-zA-Z-]+', txt[m.end():m.end() + 20000])
        print('[' + (idm.group(0) if idm else '?') + '] ...' + txt[s:e].replace('\n', ' / ') + '...')
        n += 1
        if n >= maxhits:
            break
    if n == 0:
        print('  (no match)')
