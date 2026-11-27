"""Print pi-1 locked termbase entries (and with -2 the pi-2 senses entries) whose headword matches a regex.
usage: p1look.py [-2] regex [regex ...]"""
import re, sys, pathlib
B = pathlib.Path(__file__).resolve().parents[5]
a = sys.argv[1:]; two = a and a[0] == "-2"
if two: a = a[1:]
F = [B / "AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md"] + ([B / "AI_translation/burmese/pi-2-pali-word-burmese-senses-plain.md"] if two else [])
for f in F:
    L = f.read_text(encoding="utf-8").splitlines()
    for rx in a:
        r = re.compile(rx, re.I)
        for l in L:
            hw = l.split(": {", 1)[0]
            if r.search(hw): print(("P1 " if "termbase" in f.name else "P2 ") + l[:400])
