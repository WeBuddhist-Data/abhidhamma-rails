# Console-only reader for the reference translation (prints, never writes).
import re, sys
F = r'D:\Work\OpenPecha\abhidhamma-rails\1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md'
t = open(F, encoding='utf-8').read()
# split into blocks ending with a block id
blocks = re.split(r'(\^[0-9a-z-]+)\s*\n', t)
seg = {}
buf = ''
for part in blocks:
    if re.fullmatch(r'\^[0-9a-z-]+', part):
        seg.setdefault(part[1:], []).append(buf.strip())
        buf = ''
    else:
        buf += part
mode = sys.argv[1]
if mode == 'len':
    for k in sys.argv[2:]:
        print(k, [len(x) for x in seg.get(k, [])])
elif mode == 'show':
    k = sys.argv[2]
    a = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    b = int(sys.argv[4]) if len(sys.argv) > 4 else 3000
    for x in seg.get(k, []):
        print(x[a:b])
        print('-----')
elif mode == 'grep':
    k = sys.argv[2]
    pat = sys.argv[3]
    w = int(sys.argv[4]) if len(sys.argv) > 4 else 200
    for x in seg.get(k, []):
        for m in re.finditer(pat, x):
            print('...', x[max(0, m.start() - w):m.end() + w].replace('\n', ' / '), '...')
