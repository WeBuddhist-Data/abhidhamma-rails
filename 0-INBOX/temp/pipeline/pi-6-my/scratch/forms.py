"""Scratch: for a Pāli regex, list the Burmese n-gram windows matching a Burmese regex on those lines (form survey)."""
import pathlib, re, collections, sys
HERE = pathlib.Path(__file__).resolve().parents[1]; ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"; MD = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
prx, brx = re.compile(sys.argv[1]), re.compile(sys.argv[2])
c = collections.defaultdict(collections.Counter); n = collections.Counter()
for p in sorted(PD.glob("*.md")):
    A = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for x, y in zip(A, B):
        if prx.search(x):
            n[p.name[:5]] += 1
            for m in brx.finditer(y):
                c[m[0]][p.name[:5]] += 1
for k, v in sorted(c.items(), key=lambda kv: -sum(kv[1].values())):
    print(sum(v.values()), k, dict(v))
print("lines", dict(n))
