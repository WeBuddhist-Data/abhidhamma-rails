"""pi-4 English: render mātikā / its uddesa headings as "matrix" instead of "outline" (user, 2026-11-10).

usage: python -I -X utf8 outline_to_matrix.py [--dry]
Fixed-string replacements only. Fails if any "outline" is left in a target file.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
EN = ROOT / "AI_translation" / "english"
TEXT_FILES = [
    EN / "pi-4-english-plain-zeroshot_split_chapters" / "1-matika.md",
    EN / "pi-4-english-plain-zeroshot.md",
    EN / "pi-4-english-plain-rails_split_chapters" / "1-matika.md",
    EN / "pi-4-english-plain.md",
    ROOT / "3-TRANSFORMATIONS" / "Translations" / "en-Contemporary-English-Abhidhamma" / "pi-4-english-plain.md",
]
TERM_FILES = [
    EN / "pi-4-pali-english-termbase-plain.md",
    EN / "pi-4-pali-word-english-senses-plain.md",
]
KEYWORD_FILES = [
    EN / "pi-4-keywords-by-reference-pali-english-plain.md",
    ROOT / "AI_translation" / "skills" / "scripts" / "Keyword_extractor" / "output" / "pi-4-english-plain-zeroshot-by-reference.md",
]

TEXT_SUBS = [
    ("### The Outline ^4-M-0", "### The Matrix ^4-M-0"),
    ("### Outline ^4-M-0", "### Matrix ^4-M-0"),
    ("#### Outline of ", "#### Matrix of "),
    ("The outline of the ", "The matrix of the "),
    ("Mātikā (outline)", "Mātikā (matrix)"),
]
TERM_SUBS = [
    ("Mātikā: {matrix, list of topics (heading): outline}", "Mātikā: {matrix, list of topics (heading): matrix}"),
    ("uddeso: {summary listing of topics (heading): outline}", "uddeso: {summary listing of topics (heading): matrix}"),
]


def keyword_fix(line):
    # only the matrix lines ([4-M-...]) carry "outline"; replace the whole word value
    if not line.startswith("[4-M-"):
        return line
    return re.sub(r"(?<![A-Za-z])outline(?![A-Za-z])", "matrix", line)


dry = "--dry" in sys.argv
total = 0
for path in TEXT_FILES + TERM_FILES + KEYWORD_FILES:
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    new = text
    n = 0
    if path in KEYWORD_FILES:
        lines = new.split("\n")
        fixed = [keyword_fix(l) for l in lines]
        n = sum(a != b for a, b in zip(lines, fixed))
        new = "\n".join(fixed)
    else:
        for old, rep in (TEXT_SUBS if path in TEXT_FILES else TERM_SUBS):
            n += new.count(old)
            new = new.replace(old, rep)
    left = len(re.findall(r"(?i)outline", new))
    print(f"{n:3} changed, {left} 'outline' left  {path.relative_to(ROOT)}")
    total += n
    if left:
        sys.exit(f"ERROR: outline left in {path}")
    if not dry and new != text:
        path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + new.encode("utf-8"))
print("total", total, "(dry run)" if dry else "")
