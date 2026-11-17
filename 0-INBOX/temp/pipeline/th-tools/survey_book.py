"""Survey a Thai draft against its root: opening items (kind + first chars), question counts."""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft, parse_root  # noqa: E402

root, draft = sys.argv[1:3]
R = parse_root(root)
D = parse_draft(draft)
for k, it in enumerate(D[:14]):
    print(f"{k:3d} {it['kind']:5s} {it['text'][:40]}")
pq = sum(b["text"].count("?") for b in R if b["kind"] == "t")
pk = sum(len(re.findall(r"\b[Kk]atam", b["text"])) for b in R if b["kind"] == "t")
tq = sum(it["text"].count("เป็นไฉน") for it in D)
tp = sum(1 for it in D if it["kind"] in ("p", "li") and "เป็นไฉน" in it["text"])
print(f"root '?': {pq}, root 'katam': {pk}, Thai 'เป็นไฉน': {tq} (in {tp} paragraphs)")
print("root headings:", sum(1 for b in R if b["kind"] == "h"), " Thai headings:", sum(1 for it in D if it["kind"] == "h"))
