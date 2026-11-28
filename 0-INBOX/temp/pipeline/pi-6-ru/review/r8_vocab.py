"""r8: Russian word-form frequency in the nine files (verbs and rare words), with first location."""
import re, sys, collections
sys.path.insert(0, r'D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\review')
from r8_check import FILES, load
c = collections.Counter(); first = {}
for f in FILES:
    p, r = load(f)
    for i, b in enumerate(r):
        for w in re.findall(r'[А-Яа-яЁё]+', b):
            c[w] += 1; first.setdefault(w, '%s:%d' % (f[:5], i + 1))
mode = sys.argv[1] if len(sys.argv) > 1 else 'verbs'
if mode == 'verbs':
    for w, n in sorted(c.items()):
        if re.match(r'(возни|прекра|понима|понял|пойм|устран|разви|разов|осущест|перерож|переро|умира|достиг|живёт|обрет|присутств)', w.lower()):
            print(n, w, first[w])
else:
    for w, n in sorted(c.items(), key=lambda x: x[1]):
        if n <= int(mode):
            print(n, w, first[w])
