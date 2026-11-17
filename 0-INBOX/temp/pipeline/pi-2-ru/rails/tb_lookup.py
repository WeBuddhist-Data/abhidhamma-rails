"""Look up Pāli headwords in the locked pi-2 Russian termbase (exact, or regex with -r).
usage: python -I -X utf8 tb_lookup.py word1 word2 ...   |   tb_lookup.py -r REGEX
"""
import re
import sys
import pathlib

TB = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-2-pali-russian-termbase-plain.md")
lines = TB.read_text(encoding="utf-8").splitlines()
idx = {}
for ln in lines:
    if ": {" in ln:
        k = ln.split(": {", 1)[0]
        idx.setdefault(k, []).append(ln)

args = sys.argv[1:]
if args and args[0] == "-r":
    rx = re.compile(args[1])
    for k, v in idx.items():
        if rx.search(k):
            for x in v:
                print(x)
else:
    for w in args:
        hits = idx.get(w)
        if hits:
            for x in hits:
                print(x)
        else:
            print(f"--- {w}: NOT FOUND")
