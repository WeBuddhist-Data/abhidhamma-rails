"""Merge the pi-7 Hindi rails files into AI_translation/hindi/pi-7-hindi-plain.md with frontmatter.

usage: python -I -B -X utf8 merge_rails_hi.py
Frontmatter: 0-INBOX/temp/pipeline/pi-7-hi/hi-frontmatter.yaml (SEGMENT_IDS is filled in).
Checks: the merged block-ID sequence equals the Pāli split's sequence (same order), lines per segment equal.
"""
import pathlib, re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
HI = ROOT / "AI_translation/hindi/pi-7-hindi-plain-rails_split_chapters"
PI = ROOT / "AI_translation/pali/pi-7_split_chapters"
FM = ROOT / "0-INBOX/temp/pipeline/pi-7-hi/hi-frontmatter.yaml"
OUT = ROOT / "AI_translation/hindi/pi-7-hindi-plain.md"


def key(stem):
    m = re.match(r"(\d+)(?:-(\d+))?-", stem)
    return (int(m.group(1)), int(m.group(2) or 0))


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


assert len(PARTS) == 75, PARTS
hi, pi = merge(HI), merge(PI)
sh, sp = segs(hi), segs(pi)
assert [i for i, _ in sh] == [i for i, _ in sp], "ID sequence differs"
assert sh == sp, [(a, b) for a, b in zip(sh, sp) if a != b][:5]
ids = [i for i, _ in sh]
fm = FM.read_text(encoding="utf-8-sig").replace(
    "SEGMENT_IDS", f"{ids[0]} … {ids[-1]} ({len(ids)} blocks, matching the source)")
OUT.write_text(fm.rstrip("\n") + "\n\n" + hi, encoding="utf-8", newline="\n")
print(OUT.name, "parts", len(PARTS), "blocks", len(ids), ids[0], "…", ids[-1], "lines", (fm + hi).count("\n"))
