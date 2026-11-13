"""Merge the pi-7 Hindi zero-shot files into AI_translation/hindi/pi-7-hindi-plain-zeroshot.md (no frontmatter).

usage: python -I -B -X utf8 merge_zeroshot_hi.py
Checks: the merged block-ID sequence equals the Pāli split's, and lines per segment are equal.
"""
import pathlib, re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
HI = ROOT / "AI_translation/hindi/pi-7-hindi-plain-zeroshot_split_chapters"
PI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/hindi/pi-7-hindi-plain-zeroshot.md"


def key(stem):
    m = re.match(r"(\d+)-(\d+)-", stem)
    return (int(m.group(1)), int(m.group(2)))


PARTS = ["preamble"] + sorted((p.stem for p in HI.glob("*.md") if p.stem != "preamble"), key=key)
ID = re.compile(r"\s(\^[\w-]+)\s*$")


def merge(d):
    return "\n\n".join((d / f"{p}.md").read_text(encoding="utf-8-sig").replace("\r\n", "\n").strip("\n")
                       for p in PARTS) + "\n"


def segs(text):
    out, n = [], 0
    for line in text.splitlines():
        if not line.strip():
            continue
        n += 1
        m = ID.search(line)
        if m:
            out.append((m.group(1), n)); n = 0
    return out


assert len(PARTS) == 75, len(PARTS)
hi, pi = merge(HI), merge(PI)
sh, sp = segs(hi), segs(pi)
assert [i for i, _ in sh] == [i for i, _ in sp], "ID sequence differs"
assert sh == sp, [(a, b) for a, b in zip(sh, sp) if a != b][:5]
OUT.write_text(hi, encoding="utf-8", newline="\n")
print(OUT.name, "parts", len(PARTS), "blocks", len(sh), sh[0][0], "…", sh[-1][0], "lines", hi.count("\n"))
