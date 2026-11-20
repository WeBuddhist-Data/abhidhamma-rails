"""r4 helper: print Tịnh Sự segments for an ID range to the console only (never to a file).
usage: python -I -X utf8 r4_ts.py <first> <last> [maxchars]
IDs are the numeric part of ^2-N.
"""
import sys, re
a, b = int(sys.argv[1]), int(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 1200
path = r'1-SOURCES\Translations\Vietnamese\vi-2-tinh_su.md'
text = open(path, encoding='utf-8').read().replace('\r', '')
paras = re.split(r'\n\s*\n', text)
for p in paras:
    if p.strip().startswith('![['):
        continue
    m = re.search(r'\^2-(\d+)\s*$', p.strip())
    if m and a <= int(m.group(1)) <= b:
        body = re.sub(r'\s*\^2-\d+\s*$', '', p.strip())
        print('[' + m.group(1) + '] ' + body[:mx])
