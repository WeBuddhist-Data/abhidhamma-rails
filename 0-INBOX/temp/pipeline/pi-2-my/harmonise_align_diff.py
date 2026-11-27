"""Word-level view of align_check_my.py: for every repeated Pāli sentence with differing Burmese, print the Pāli and,
for each Burmese variant after the first, only the words that differ (opcodes of difflib on space-separated words).
usage: python3 -I -X utf8 harmonise_align_diff.py [align-before.txt | align-after.txt] (default: re-run on the files)"""
import collections
import difflib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-2_split_chapters"
MD = ROOT / "AI_translation/burmese/pi-2-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SPLIT_PI = re.compile(r"(?<=[.?])\s+")
SPLIT_MY = re.compile(r"(?<=[။])\s+")


def groups(pd=PD, md=MD):
    f = lambda p: [ID.sub("", l) for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    loc = lambda p: p.name.split("-")[0].split(".")[0]
    seen = collections.defaultdict(lambda: collections.defaultdict(list))
    for p in sorted(pd.glob("*.md")):
        for i, (x, y) in enumerate(zip(f(p), f(md / p.name)), 1):
            xs, ys = SPLIT_PI.split(x.strip()), SPLIT_MY.split(y.strip())
            if len(xs) != len(ys):
                xs, ys = [x.strip()], [y.strip()]
            for s, t in zip(xs, ys):
                if len(s) > 25:
                    seen[s][t].append(f"{loc(p)}:{i}")
    return {s: v for s, v in seen.items() if len(v) > 1}


def wdiff(a, b):
    a, b = a.split(" "), b.split(" ")
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op != "equal":
            out.append(f"[{' '.join(a[i1:i2])}] -> [{' '.join(b[j1:j2])}]")
    return "; ".join(out)


if __name__ == "__main__":
    bad = groups()
    print(f"differing: {len(bad)}")
    for s, v in bad.items():
        vs = sorted(v.items(), key=lambda kv: -len(kv[1]))
        print(f"\nPĀLI: {s[:160]}")
        print(f"   {vs[0][1][:8]} (base)")
        for t, locs in vs[1:]:
            print(f"   {locs[:8]}: {wdiff(vs[0][0], t)[:400]}")
