import re, sys
# usage: r5_seg.py <file> <id> [<id> ...]   prints the segment ending with ^id
path = sys.argv[1]
txt = open(path, encoding='utf-8').read()
blocks = re.split(r'\n\s*\n', txt)
for want in sys.argv[2:]:
    hit = [b for b in blocks if re.search(r'\^' + re.escape(want) + r'\s*$', b.strip())]
    print('=====', want)
    for b in hit:
        print(b.strip())
    if not hit:
        print('  (not found)')
