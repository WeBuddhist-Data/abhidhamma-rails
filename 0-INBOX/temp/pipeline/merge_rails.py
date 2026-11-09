"""Merge rails chapter files into one translation file with frontmatter, then re-verify
the whole document against the concatenated Pāli split (IDs + per-segment line counts).

usage: python -I merge_rails.py <pali_split_dir> <rails_split_dir> <frontmatter.yaml> <out.md>
Chapter order: preamble, then files sorted by their leading number.
"""
import re, sys, pathlib

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
src_dir, tr_dir, fm_path, out = map(pathlib.Path, sys.argv[1:5])


def order(d):
    files = [p for p in d.glob("*.md")]
    key = lambda p: (-1 if p.stem == "preamble" else int(p.stem.split("-")[0]))
    return sorted(files, key=key)


def segments(text):
    segs, buf = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            segs.append((m.group(1), len(buf))); buf = []
    return segs, buf


tr_files = order(tr_dir)
src_files = order(src_dir)
assert [p.name for p in tr_files] == [p.name for p in src_files], "chapter file sets differ"

body = "\n\n".join(p.read_text(encoding="utf-8").strip() for p in tr_files) + "\n"
body = re.sub(r"\n{3,}", "\n\n", body)
fm = fm_path.read_text(encoding="utf-8-sig").strip()
fm = fm + "\n\n" if fm else ""  # empty frontmatter file -> no frontmatter (zero-shot merges)
out.write_text(fm + body, encoding="utf-8", newline="\n")

src_text = "\n\n".join(p.read_text(encoding="utf-8") for p in src_files)
s, _ = segments(src_text)
t, tail = segments(body)
ok = True
if [i for i, _ in s] != [i for i, _ in t]:
    ok = False; print("ID sequence differs", len(s), len(t))
else:
    diff = [i for (i, a), (_, b) in zip(s, t) if a != b]
    if diff:
        ok = False; print("line-count differs:", diff[:10])
if tail:
    ok = False; print("trailing lines after last ID")
dashes = body.count("—") + body.count("–")
print(f"{out}: {'OK' if ok else 'FAIL'}; {len(t)} segments; dashes {dashes}; double-blank {'\n\n\n' in body}")
sys.exit(0 if ok else 1)
