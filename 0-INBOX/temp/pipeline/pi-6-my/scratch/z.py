"""Scratch: search the pi-6 Pāli (or Burmese with -b) by regex; print ch:line, Pāli, Burmese (zero-shot now).
usage: z.py REGEX [--max N] [-b] [--ch PREFIX] [--bk] (--bk: Burmese from harmonise-backup/chapters) [--count]"""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parents[1]
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"
MD = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
a = sys.argv[1:]
rx = re.compile(a[0])
mx = int(a[a.index("--max") + 1]) if "--max" in a else 5
ch = a[a.index("--ch") + 1] if "--ch" in a else ""
bur = "-b" in a
if "--bk" in a:
    MD = HERE / "harmonise-backup/chapters"
key = lambda p: [int(x) if x.isdigit() else 0 for x in re.findall(r"\d+", p.name)] or [0]
n = 0
per = {}
for p in sorted(PD.glob("*.md"), key=key):
    if not p.name.startswith(ch):
        continue
    A = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(A, B), 1):
        if rx.search(y if bur else x):
            n += 1
            c = p.name.rsplit("-", 1)[0] if p.name[0].isdigit() else p.name
            per[c] = per.get(c, 0) + 1
            if n <= mx:
                print(f"{c}:{i}\n  P: {x}\n  B: {y}")
print("total", n, per if "--count" in a else "")
