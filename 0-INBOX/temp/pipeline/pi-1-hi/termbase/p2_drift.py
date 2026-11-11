"""Part 2 helper: group single-word headwords by a crude stem; print groups touching lines 831-1660 with >1 Hindi term."""
import collections, pathlib, re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
LINES = (ROOT / "AI_translation/hindi/pi-1-pali-word-hindi-senses-plain.md").read_text(encoding="utf-8").splitlines()
ENDS = sorted("ameva ānaṃ assa ehi esu āya amhi asmiṃ ena āni iyaṃ iyā aṃ ā o e a ī i u ū ṃ".split(), key=len, reverse=True)


def stem(w):
    w = w.lower()
    for e in ENDS:
        if w.endswith(e) and len(w) - len(e) >= 4:
            return w[: -len(e)]
    return w


groups = collections.defaultdict(list)
for n, line in enumerate(LINES, 1):
    m = re.match(r"^(.+?): \{(.*)\}$", line)
    if not m or " " in m[1]:
        continue
    for i, part in enumerate(m[2].split("; ")):
        if ": " not in part:
            continue
        tag, terms = part.rsplit(": ", 1)
        groups[stem(m[1])].append((n, m[1], i, tag[:50], terms))

for st, items in sorted(groups.items()):
    if not any(831 <= it[0] <= 1660 for it in items):
        continue
    if len({it[4] for it in items}) < 2:
        continue
    print(f"== {st}")
    for n, hw, i, tag, terms in items:
        print(f"  {n}\t{hw}|{i}\t{terms}\t({tag})")
