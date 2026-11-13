"""Case-insensitive termbase lookup: python tb_4-01.py word1 word2 ... (also tries regex with -r)."""
import re
import sys

TB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md"
tb = {}
for ln in open(TB, encoding="utf-8"):
    k, _, v = ln.rstrip("\n").partition(": ")
    tb.setdefault(k.lower(), []).append((k, v))
args = sys.argv[1:]
if args and args[0] == "-r":
    rx = re.compile(args[1])
    for k, vs in tb.items():
        if rx.search(k):
            for kk, v in vs:
                print(kk, ":", v)
else:
    for w in args:
        print(w, "=>", tb.get(w.lower(), "??"))
