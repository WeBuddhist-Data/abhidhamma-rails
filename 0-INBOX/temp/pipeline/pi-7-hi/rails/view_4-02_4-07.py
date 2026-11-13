"""Show Pāli / Hindi pairs (non-empty lines) for a file, filtered by a regex on the Pāli or by a line range.
usage: python -I -B -X utf8 view_4-02_4-07.py <file.md> [--re PATTERN] [--from N --to M] [--hi-only]"""
import re
import sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
args = sys.argv[1:]
name = args[0]
pat = args[args.index("--re") + 1] if "--re" in args else None
lo = int(args[args.index("--from") + 1]) if "--from" in args else 0
hi_ = int(args[args.index("--to") + 1]) if "--to" in args else 10 ** 9
p = [x for x in open(ROOT + r"\AI_translation\pali\pi-7_split_chapters\\" + name, encoding="utf-8").read().split("\n")
     if x.strip()]
h = [x for x in open(ROOT + r"\AI_translation\hindi\pi-7-hindi-plain-rails_split_chapters\\" + name,
                     encoding="utf-8").read().split("\n") if x.strip()]
for i, (a, b) in enumerate(zip(p, h), 1):
    if not (lo <= i <= hi_):
        continue
    if pat and not re.search(pat, a):
        continue
    if "--hi-only" not in args:
        print(f"P{i}: {a}")
    print(f"H{i}: {b}")
