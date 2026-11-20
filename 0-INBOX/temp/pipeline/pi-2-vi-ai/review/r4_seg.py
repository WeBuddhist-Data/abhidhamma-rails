"""r4 helper: print segments (paragraph blocks) containing given block IDs. Console only.
usage: python -I -X utf8 r4_seg.py <file> <id> [<id> ...] [--grep TEXT] [--max N]
--grep: print paragraphs containing TEXT (case-sensitive) instead.
"""
import sys, re

args = sys.argv[1:]
path = args[0]
rest = args[1:]
grep = None
mx = 2000
if '--max' in rest:
    i = rest.index('--max'); mx = int(rest[i+1]); rest = rest[:i] + rest[i+2:]
if '--grep' in rest:
    i = rest.index('--grep'); grep = rest[i+1]; rest = rest[:i] + rest[i+2:]
text = open(path, encoding='utf-8').read().replace('\r', '')
paras = re.split(r'\n\s*\n', text)
if grep:
    n = 0
    for p in paras:
        if grep in p:
            print(p[:mx]); print('-----'); n += 1
            if n > 10: break
else:
    for bid in rest:
        pat = re.compile(r'\^' + re.escape(bid) + r'(?![\d-])')
        found = False
        for p in paras:
            if pat.search(p):
                print('=== ' + bid); print(p[:mx]); found = True
        if not found:
            print('=== ' + bid + ' NOT FOUND')
