"""Question agreement of a Vietnamese map (items + split pieces) against the root:
Pāli 'katam…' (Ds/Vb/Dt/Pp) or '?' (Yamaka, Kathāvatthu) vs Vietnamese '?'.

Usage: vi_q_metric.py <root.md> <draft.md> <book> <map.json>
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "th-tools"))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, draft_path, book, map_path = sys.argv[1:5]
R = parse_root(root_path)
V = parse_draft(draft_path)
M = json.load(open(map_path, encoding="utf-8"))["mapping"]


def qp(t):
    return len(re.findall(r"\bkatam", t.lower())) if book in ("1", "2", "4") else t.count("?")


n = ok = stacked = 0
bad = []
for b in R:
    if b["kind"] != "t" or b["id"] == "T-1":
        continue
    q = qp(b["text"])
    if not q:
        continue
    n += 1
    v = M[b["id"]]
    texts = [V[i]["text"] for i in v.get("items", [])] + [t for _, t in v.get("pieces", [])]
    if not texts:
        stacked += 1
        continue
    qv = " ".join(texts).count("?")
    if qv == q:
        ok += 1
    else:
        bad.append((b["id"], q, qv))
print(f"{os.path.basename(map_path)}: blocks with questions {n}, same count {ok} ({100 * ok / max(n, 1):.1f}%), stacked {stacked}")
print("   first mismatches:", bad[:12])
