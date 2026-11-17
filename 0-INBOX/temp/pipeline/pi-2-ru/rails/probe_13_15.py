"""Print aligned Pāli / Russian lines of finished pi-2 chapters whose Pāli matches a regex.
usage: python -I -X utf8 probe_13_15.py REGEX [chapter-file-prefix ...] [-n MAX]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-2_split_chapters"
RU = ROOT / "AI_translation" / "russian" / "pi-2-russian-plain-rails_split_chapters"


def lines(p):
    return [ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]


args = sys.argv[1:]
mx = 6
if "-n" in args:
    i = args.index("-n")
    mx = int(args[i + 1])
    del args[i:i + 2]
rx = re.compile(args[0])
prefixes = args[1:]
n = 0
for rf in sorted(RU.glob("*.md")):
    if rf.name == "preamble.md":
        continue
    if prefixes and not any(rf.name.startswith(p + "-") for p in prefixes):
        continue
    pl, rl = lines(PALI / rf.name), lines(rf)
    if len(pl) != len(rl):
        continue
    for a, b in zip(pl, rl):
        if rx.search(a):
            print("P:", a)
            print("R:", b)
            print()
            n += 1
            if n >= mx:
                sys.exit(0)
