"""Pāli regex -> the matching Pāli lines of pi-2 with their Burmese line (zero-shot), or -b <block id>.
usage: python3 -I -X utf8 grep_pm.py <regex> [chapter-prefix] [-n max] | -b 2-171 [-o: backup chapters-before] [-s: matching sentences only]"""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-2_split_chapters"
MD = HERE / "harmonise-backup/chapters-before" if "-o" in sys.argv else ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
a = [x for x in sys.argv[1:] if x not in ("-o", "-s")]
mx = 10**6
if "-n" in a:
    i = a.index("-n"); mx = int(a[i + 1]); del a[i:i + 2]
blk = None
if a[0] == "-b":
    blk = a[1]; a = a[2:]
    rx = re.compile(r"\^" + re.escape(blk) + r"\s*$")
else:
    rx = re.compile(a[0]); a = a[1:]
pref = a[0] if a else ""
k = 0
for p in sorted(PD.glob("*.md")):
    if pref and not p.name.startswith(pref + "-"):
        continue
    P = p.read_text(encoding="utf-8-sig").split("\n"); M = (MD / p.name).read_text(encoding="utf-8").split("\n")
    for i, (x, y) in enumerate(zip(P, M), 1):
        if x.strip() and rx.search(x):
            k += 1
            if k <= mx:
                if "-s" in sys.argv and not blk:
                    ps = re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", x); bs = re.split(r"(?<=။) ", y)
                    if len(ps) == len(bs):
                        for u, v in zip(ps, bs):
                            if rx.search(u):
                                print(f"== {p.name.split('-')[0]}:{i}\nPI: {u}\nMY: {v}")
                        continue
                print(f"== {p.name.split('-')[0]}:{i}\nPI: {x}\nMY: {y}")
print(f"({k} lines)")
