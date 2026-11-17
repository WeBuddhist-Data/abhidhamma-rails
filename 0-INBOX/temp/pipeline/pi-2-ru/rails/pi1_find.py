"""Find a Pāli substring in pi-1 (or another book) and print the aligned Russian rails line.
usage: python -I -X utf8 pi1_find.py [-b N] [-n MAX] "pali substring"
Segments are aligned by block ID, lines by index inside the segment.
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")

args = sys.argv[1:]
book = "1"
mx = 5
while args and args[0].startswith("-"):
    if args[0] == "-b":
        book = args[1]; args = args[2:]
    elif args[0] == "-n":
        mx = int(args[1]); args = args[2:]
pat = args[0]


def segs(path):
    out = {}
    cur = []
    for ln in path.read_text(encoding="utf-8").splitlines():
        if not ln.strip():
            continue
        cur.append(ln)
        m = ID.search(ln)
        if m:
            out[m.group(1)] = cur
            cur = []
    return out


pdir = ROOT / "pali" / f"pi-{book}_split_chapters"
rdir = ROOT / "russian" / f"pi-{book}-russian-plain-rails_split_chapters"
n = 0
for pf in sorted(pdir.glob("*.md")):
    rf = rdir / pf.name
    if not rf.exists():
        continue
    P, R = segs(pf), segs(rf)
    for sid, pl in P.items():
        for i, ln in enumerate(pl):
            if pat in ln:
                rl = R.get(sid, [])
                print(f"== {pf.name} ^{sid} line {i}")
                print("PI:", ln[:3000])
                print("RU:", rl[i][:3000] if i < len(rl) else "(missing)")
                n += 1
                if n >= mx:
                    sys.exit()
