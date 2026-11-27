"""List the Pāli sentences of a pi-2 chapter that also occur in pi-1 (Pāli), with pi-1's aligned Burmese sentence.
usage: p1sents.py CHAPTER.md"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]
P1 = ROOT / "AI_translation/pali/pi-1_split_chapters"
B1 = ROOT / "AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters"
P2 = ROOT / "AI_translation/pali/pi-2_split_chapters"
ID = re.compile(r" \^[0-9A-Za-z-]+\s*$")
def psplit(l):
    l = ID.sub("", l)
    return [s for s in re.split(r"(?<=[.?])(?:\"|”)? (?=\S)", l) if s]
def bsplit(l):
    l = ID.sub("", l)
    return [s for s in re.split(r"(?<=။) ", l) if s]
D, bad = {}, 0
for p in sorted(P1.glob("*.md")):
    pl = p.read_text(encoding="utf-8-sig").split("\n"); bl = (B1 / p.name).read_text(encoding="utf-8").split("\n")
    for a, b in zip(pl, bl):
        if not a.strip() or a.startswith("#"):
            continue
        ps, bs = psplit(a), bsplit(b)
        if len(ps) != len(bs):
            bad += 1
            continue
        for x, y in zip(ps, bs):
            D.setdefault(x, set()).add(y)
print("pi-1 lines with unequal sentence counts:", bad, file=sys.stderr)
src = (P2 / sys.argv[1]).read_text(encoding="utf-8-sig").split("\n")
seen = set()
for i, l in enumerate(src):
    if not l.strip() or l.startswith("#"):
        continue
    for s in psplit(l):
        if s in D and s not in seen:
            seen.add(s)
            print(f"{i+1}\t{s[:150]}\t{' || '.join(sorted(D[s]))[:300]}")
