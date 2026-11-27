"""Consistency pass: identical Pāli units of ANY length (headings, colophons, short sentences ≤ 25 characters,
which align_check.py skips) must have identical Burmese across the book.
usage: python3 -I -X utf8 harmonise_lines.py [-v]
Units: whole headings; sentences of lines whose Pāli and Marathi split into the same number of sentences."""
import collections, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-1_split_chapters"
MD = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SPLIT = re.compile(r"(?<=[.?])\s+"); SPLIT_MY = re.compile(r"(?<=[။])\s+")
f = lambda p: [ID.sub("", l).strip() for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
seen = collections.defaultdict(lambda: collections.defaultdict(list))
for p in sorted(PD.glob("*.md")):
    for i, (x, y) in enumerate(zip(f(p), f(MD / p.name)), 1):
        if x.startswith("#"):
            seen["H " + x.lstrip("# ")][y.lstrip("# ")].append(f"{p.name[:4]}:{i}")
            continue
        xs, ys = SPLIT.split(x), SPLIT_MY.split(y)
        if len(xs) == len(ys):
            for s, t in zip(xs, ys):
                seen[s][t].append(f"{p.name[:4]}:{i}")
bad = {s: v for s, v in seen.items() if len(v) > 1}
nh = sum(1 for s in bad if s.startswith("H "))
print(f"Pāli units: {len(seen)}; with differing Burmese: {len(bad)} (headings {nh})")
for s, v in bad.items():
    print("\nPĀLI:", s[:140])
    for t, locs in v.items():
        print("  ", locs[:5], t[:140])
