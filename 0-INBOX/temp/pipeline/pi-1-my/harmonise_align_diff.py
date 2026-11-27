"""Word-level view of align_check_my.py differences: for every repeated Pāli sentence with differing Burmese, the
differing words of each variant against the first one (with locations). Identical diffs are grouped.
usage: harmonise_align_diff.py [--full]"""
import collections, difflib, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-1_split_chapters"
MD = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
SPLIT_PI = re.compile(r"(?<=[.?])\s+")
SPLIT_MY = re.compile(r"(?<=[။])\s+")
f = lambda p: [ID.sub("", l).strip() for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
loc = lambda p: p.name[:4] if p.name[1] == "-" and p.name[2].isdigit() else p.name.split("-")[0].split(".")[0]
seen = collections.defaultdict(lambda: collections.defaultdict(list))
for p in sorted(PD.glob("*.md")):
    for i, (x, y) in enumerate(zip(f(p), f(MD / p.name)), 1):
        xs, ys = SPLIT_PI.split(x), SPLIT_MY.split(y)
        if len(xs) != len(ys):
            xs, ys = [x], [y]
        for s, t in zip(xs, ys):
            if len(s) > 25:
                seen[s][t].append(f"{loc(p)}:{i}")
groups = collections.defaultdict(list)
for s, v in seen.items():
    if len(v) < 2:
        continue
    vs = sorted(v.items(), key=lambda kv: -len(kv[1]))
    ref, rl = vs[0]
    rw = ref.split(" ")
    for t, locs in vs[1:]:
        tw = t.split(" ")
        ops = []
        for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, rw, tw, autojunk=False).get_opcodes():
            if op != "equal":
                ops.append(f"«{' '.join(rw[a1:a2])}» / «{' '.join(tw[b1:b2])}»")
        groups[" ; ".join(ops)].append((s, rl, locs))
for k, lst in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    print(f"\n[{len(lst)}] {k[:600]}")
    for s, rl, locs in lst[: (99 if '--full' in sys.argv else 2)]:
        print(f"     {s[:110]}\n       ref {rl[:4]}  other {locs[:4]}")
