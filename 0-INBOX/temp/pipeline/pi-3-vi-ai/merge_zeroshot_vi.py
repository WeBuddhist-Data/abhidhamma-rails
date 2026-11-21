"""Merge the pi-3 Vietnamese zero-shot chapters into one file (no frontmatter, like pi-2) and
check its block IDs and per-segment line counts against the Pāli split."""
import pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation/pali/pi-3_split_chapters"
VI = ROOT / "AI_translation/vietnamese/pi-3-vietnamese-plain-zeroshot_split_chapters"
OUT = ROOT / "AI_translation/vietnamese/pi-3-vietnamese-plain-zeroshot.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def order(d):
    def key(p):
        return (-1,) if p.stem == "preamble" else (int(p.stem.split("-")[0]),)
    return sorted(d.glob("*.md"), key=key)


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


parts = [p.read_text(encoding="utf-8").strip("\n") for p in order(VI)]
text = "\n\n".join(parts) + "\n"
pali = "\n\n".join(p.read_text(encoding="utf-8-sig").strip("\n") for p in order(PALI))
a, b = segs(pali), segs(text)
if a != b:
    sys.exit(f"MISMATCH: pali {len(a)} vs vi {len(b)}; first diff at {next(i for i,(x,y) in enumerate(zip(a,b)) if x!=y) if any(x!=y for x,y in zip(a,b)) else min(len(a),len(b))}")
assert "\n\n\n" not in text and "\r" not in text
OUT.write_text(text, encoding="utf-8", newline="\n")
print(f"OK {OUT.name}: {len(b)} segments, {[p.name for p in order(VI)] == [p.name for p in order(PALI)]}")
