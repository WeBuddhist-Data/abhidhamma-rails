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


if book == "7":
    # Paṭṭhāna: negated conditions (Pāli na-hetuyā … <-> Vietnamese "phi Nhân …") and count
    # sections (Pāli number words <-> Vietnamese digits), presence agreement per block
    NW = re.compile(r"\b(ekaṃ|dve|tīṇi|cattāri|pañca|cha|satta|aṭṭha|nava|dasa)\b")
    n = neg_ok = cnt_ok = 0
    for b in R:
        if b["kind"] != "t" or b["id"] == "T-1":
            continue
        v = M[b["id"]]
        texts = [V[i]["text"] for i in v.get("items", [])] + [t for _, t in v.get("pieces", [])]
        if not texts:
            continue
        n += 1
        vt = " ".join(texts)
        neg_ok += bool(re.search(r"\bna(?!va\b|vahi|vasu)(?=[a-zāīūṭḍṇñṅ])", b["text"].lower())) == bool(re.search(r"\b[Pp]hi\s", vt))
        cnt_ok += (len(NW.findall(b["text"].lower())) >= 2) == (len(re.findall(r"\b[1-9]\b", vt)) >= 2)
    print(f"{os.path.basename(map_path)}: blocks with Vietnamese {n}; negation agreement {100 * neg_ok / max(n, 1):.1f}%, count-section agreement {100 * cnt_ok / max(n, 1):.1f}%")
    sys.exit(0)
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
