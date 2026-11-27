"""Inspection helper (read only): regex windows in the files of a folder. usage: ctx.py <dir> <regex> [w] [max]"""
import pathlib, re, sys, unicodedata
d, rx = pathlib.Path(sys.argv[1]), re.compile(unicodedata.normalize("NFC", sys.argv[2]))
w = int(sys.argv[3]) if len(sys.argv) > 3 else 60
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 20
n = 0
for p in sorted(d.glob("*.md")):
    for k, l in enumerate(unicodedata.normalize("NFC", p.read_text(encoding="utf-8-sig")).splitlines(), 1):
        for m in rx.finditer(l):
            n += 1
            if n <= mx:
                print(f"{p.name[:5]}:{k}: …{l[max(0, m.start() - w):m.end() + w]}…")
print("matches", n)
