"""Print pi-2 termbase entries whose headword matches exactly (or by regex with -r).

usage: python -I -X utf8 build_rails_17_tb.py word [word ...]
       python -I -X utf8 build_rails_17_tb.py -r REGEX
       python -I -X utf8 build_rails_17_tb.py -ids 2-843 2-U1 ...   (all keywords of these segments)
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TB = ROOT / "AI_translation" / "hindi" / "pi-2-pali-hindi-termbase-plain.md"
KW = ROOT / "AI_translation" / "pali" / "pi-2-keywords-by-reference-pali-plain.md"

tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    if ": {" not in line:
        continue
    w, body = line.split(": {", 1)
    tb[w] = body[:-1]
tb_ci = {k.lower(): v for k, v in tb.items()}

args = sys.argv[1:]
if args and args[0] == "-r":
    rx = re.compile(args[1])
    for k, v in tb.items():
        if rx.search(k):
            print(f"{k}: {v}")
elif args and args[0] == "-ids":
    ids = set(args[1:])
    seen = set()
    for line in KW.read_text(encoding="utf-8").splitlines():
        i, body = line.split("] ", 1)
        i = i[1:]
        if i not in ids:
            continue
        for k in body.split(", "):
            for kk in k.split(" / "):
                if kk.lower() in seen:
                    continue
                seen.add(kk.lower())
                v = tb.get(kk) or tb_ci.get(kk.lower())
                print(f"{kk}: {v}")
else:
    for a in args:
        print(f"{a}: {tb.get(a) or tb_ci.get(a.lower())}")
