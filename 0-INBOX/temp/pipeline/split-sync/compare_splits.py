"""Compare AI_translation/pali/pi-N_split_chapters against 1-SOURCES/Text/pi-N.md (read-only).

usage: python -I -X utf8 compare_splits.py [N ...]
The split is the root text with the frontmatter moved to frontmatter.txt, transclusion lines dropped,
and the body cut at chapter markers (AI_translation/skills/scripts/split_chapters.py). Here the split
files are put back in root order (by where each file's first line sits in the root) and compared:
  - frontmatter.txt vs the root frontmatter
  - every line, blank lines included, per file vs the root slice it should equal
"""
import difflib, pathlib, re, sys

BASE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
TRANS = re.compile(r"^\s*!\[\[.*\]\]\s*$")


def split_fm(text):
    s = text.lstrip("\n")
    lines = s.split("\n")
    if lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[:i + 1]), "\n".join(lines[i + 1:])
    return None, text


def check(n):
    root = (BASE / f"1-SOURCES/Text/pi-{n}.md").read_text(encoding="utf-8")
    sdir = BASE / f"AI_translation/pali/pi-{n}_split_chapters"
    fm, body = split_fm(root.replace("\r\n", "\n"))
    out = []
    fm_s = (sdir / "frontmatter.txt").read_text(encoding="utf-8").replace("\r\n", "\n").rstrip("\n")
    if fm is not None and fm_s != fm.rstrip("\n"):
        d = [l for l in difflib.unified_diff(fm_s.split("\n"), fm.split("\n"), "split", "root", n=0, lineterm="")][2:]
        out.append(f"frontmatter differs: {d[:8]}")
    rlines = [l for l in body.split("\n") if not TRANS.match(l)]
    files = [p for p in sdir.glob("*.md")]
    pos = {}
    first_nonblank = {}
    for p in files:
        fl = p.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
        first = next(l for l in fl if l.strip())
        first_nonblank[p] = first
    # locate each file's first line in the root, in order of occurrence
    starts = []
    for i, l in enumerate(rlines):
        for p, f in first_nonblank.items():
            if l == f and p not in pos:
                pos[p] = i
    missing = [p.name for p in files if p not in pos]
    if missing:
        out.append(f"first line not found in root for: {missing}")
    ordered = sorted((p for p in files if p in pos), key=lambda p: pos[p])
    cuts = [pos[p] for p in ordered] + [len(rlines)]
    ndiff_lines = 0
    for k, p in enumerate(ordered):
        want = "\n".join(rlines[cuts[k]:cuts[k + 1]]).strip() + "\n"
        have = p.read_text(encoding="utf-8").replace("\r\n", "\n")
        if have != want:
            d = [l for l in difflib.unified_diff(have.split("\n"), want.split("\n"), "split", "root", n=0, lineterm="")
                 if l[:1] in "+-" and not l.startswith(("---", "+++"))]
            ndiff_lines += len(d)
            out.append(f"{p.name}: {len(d)} differing lines, e.g. " + " || ".join(x[:110] for x in d[:4]))
    # content before the first file's start (should be blank)
    pre = [l for l in rlines[:cuts[0]] if l.strip()]
    if pre:
        out.append(f"root lines before the first split file: {pre[:3]}")
    crlf = [p.name for p in files if b"\r" in p.read_bytes()]
    status = "UP TO DATE" if not out else "STALE"
    print(f"pi-{n}: {len(files)} files, root {len(rlines)} lines -> {status}" + (f" (CRLF in {len(crlf)} files)" if crlf else ""))
    for o in out[:25]:
        print("   ", o)
    return not out


books = [int(a) for a in sys.argv[1:]] or range(1, 8)
ok = [check(n) for n in books]
sys.exit(0 if all(ok) else 1)
