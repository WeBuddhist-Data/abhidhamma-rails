"""Unique pieces of 4-01 (analysis helper)."""
import re
import sys
from collections import Counter

SRC = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters\4-01-kilesagocchaka.md"
ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")
notes, pieces = Counter(), Counter()
for ln in open(SRC, encoding="utf-8").read().split("\n"):
    if not ln.strip() or ln.startswith("#"):
        continue
    m = ID_RE.search(ln)
    body = ln[: m.start()] if m else ln.rstrip()
    body = re.sub(r"\{[^}]*\}", "", body)
    for n in re.findall(r"\(([^()]*[^\d().][^()]*)\)", body):
        notes[n] += 1
    body = re.sub(r"\(([^()]*[^\d().][^()]*)\)", " ", body)
    body = re.sub(r"\(\d+\)", " ", body)
    for p in re.split(r" – |; |\. |…pe…|…|\.$", body):
        p = p.strip(" ,.")
        if p:
            pieces[p[0].lower() + p[1:]] += 1
mode = sys.argv[1] if len(sys.argv) > 1 else "pieces"
d = notes if mode == "notes" else pieces
for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(v, k)
print(len(d), sum(d.values()), file=sys.stderr)
