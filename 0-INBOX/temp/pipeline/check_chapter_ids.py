"""Compare block IDs and per-segment line counts between a source chapter and its translation.

usage: python -I check_chapter_ids.py <source_dir> <target_dir> [chapter.md ...]
With no chapter names, checks every .md present in target_dir.
"""
import re, sys, pathlib

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segments(path):
    segs, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            segs.append((m.group(1), len(buf)))
            buf = []
    return segs, len(buf)


src, tgt = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
names = sys.argv[3:] or sorted(p.name for p in tgt.glob("*.md"))
bad = 0
for name in names:
    s, s_tail = segments(src / name)
    t_path = tgt / name
    if not t_path.exists():
        print(f"{name}: MISSING in target"); bad += 1; continue
    t, t_tail = segments(t_path)
    errs = []
    if [i for i, _ in s] != [i for i, _ in t]:
        missing = [i for i, _ in s if i not in {j for j, _ in t}]
        extra = [i for i, _ in t if i not in {j for j, _ in s}]
        errs.append(f"ID mismatch (missing {missing[:5]}, extra {extra[:5]}, src {len(s)} vs tgt {len(t)})")
    else:
        diff = [i for (i, a), (_, b) in zip(s, t) if a != b]
        if diff:
            errs.append(f"line-count differs in {len(diff)} segments, e.g. {diff[:5]}")
    if t_tail:
        errs.append(f"{t_tail} trailing lines after last ID")
    if errs:
        bad += 1
        print(f"{name}: " + "; ".join(errs))
    else:
        print(f"{name}: OK ({len(t)} segments)")
sys.exit(1 if bad else 0)
