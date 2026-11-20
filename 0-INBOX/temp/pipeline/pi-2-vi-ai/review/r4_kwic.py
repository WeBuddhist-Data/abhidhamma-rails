"""r4 helper: keyword-in-context from a file. Console only.
usage: python -I -X utf8 r4_kwic.py <file> <width> <term> [<term> ...]
"""
import sys
path, width = sys.argv[1], int(sys.argv[2])
terms = sys.argv[3:]
text = open(path, encoding='utf-8').read()
for t in terms:
    print('##### ' + t)
    start = 0; n = 0
    while True:
        i = text.find(t, start)
        if i < 0 or n >= 4:
            break
        print('...' + text[max(0, i - width):i + width].replace('\n', ' / ') + '...')
        print('--')
        start = i + len(t); n += 1
