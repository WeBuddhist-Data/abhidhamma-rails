"""Split a book-wide keyword file into per-chapter chunks, or reassemble mapped chunks.

The keyword file is sorted by ID, so one chapter's IDs are scattered across it.

split:    python -I mapper_chunks.py split <keywords.md> <chapter_dir> <out_dir>
          writes <out_dir>/<chapter>.keywords.md (input lines for that chapter's IDs, input order)
assemble: python -I mapper_chunks.py assemble <keywords.md> <out_dir> <result.md>
          reads <out_dir>/<chapter>.mapped.md and writes all lines in the keyword file's order,
          checking that every ID is present once and the keyword count per line is unchanged.
"""
import re, sys, pathlib

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
LINE = re.compile(r"^\[([^\]]+)\] (.*)$")


def read_kw(path):
    rows = []
    for l in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        m = LINE.match(l)
        if m:
            rows.append((m.group(1), m.group(2)))
    return rows


def chapter_of(chapter_dir):
    owner = {}
    for p in sorted(pathlib.Path(chapter_dir).glob("*.md")):
        for l in p.read_text(encoding="utf-8").splitlines():
            m = ID.search(l)
            if m:
                owner[m.group(1)] = p.stem
    return owner


cmd = sys.argv[1]
rows = read_kw(sys.argv[2])
if cmd == "split":
    owner = chapter_of(sys.argv[3])
    out = pathlib.Path(sys.argv[4]); out.mkdir(parents=True, exist_ok=True)
    chunks, orphans = {}, []
    for i, body in rows:
        if i not in owner:
            orphans.append(i); continue
        chunks.setdefault(owner[i], []).append(f"[{i}] {body}")
    for ch, lines in chunks.items():
        (out / f"{ch}.keywords.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(ch, len(lines))
    if orphans:
        print("IDs not found in any chapter:", orphans)
elif cmd == "assemble":
    out = pathlib.Path(sys.argv[3])
    mapped = {}
    for p in out.glob("*.mapped.md"):
        for i, body in read_kw(p):
            if i in mapped:
                sys.exit(f"duplicate ID {i} in {p.name}")
            mapped[i] = body
    errs, lines = [], []
    for i, body in rows:
        if i not in mapped:
            errs.append(f"missing {i}"); continue
        n_in, n_out = len(body.split(", ")), len(mapped[i].split(", "))
        if n_in != n_out:
            errs.append(f"{i}: {n_in} keywords in, {n_out} out")
        lines.append(f"[{i}] {mapped[i]}")
    if errs:
        print("\n".join(errs[:30])); sys.exit(f"{len(errs)} problems; not written")
    pathlib.Path(sys.argv[4]).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote", len(lines), "lines")
