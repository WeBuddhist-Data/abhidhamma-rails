"""Check that the rendered file keeps the draft (PDF) order around headings.

Rebuilds the output order the renderer uses (root order; per heading its draft heading item and
'after' lines; per text block its items, with orphans prefixed to the next placed block) and
reports every draft item that sits on the other side of a paired heading than in the draft:
e.g. a Thai-only heading printed before a root heading in the PDF but rendered under it.
For each case it lists the unmatched root headings just before the paired one (the likely
home of a misplaced translation heading).

Also prints the book-title headings (^0, ^N-0) for a look.

Usage: check_heading_order.py <root.md> <draft.md> <map.json>
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, draft_path, map_path = sys.argv[1:4]
R = parse_root(root_path)
D = parse_draft(draft_path)
M = json.load(open(map_path, encoding="utf-8"))["mapping"]
pos = {b["id"]: k for k, b in enumerate(R)}

placed = {}
for b, v in M.items():
    for i in v["items"]:
        placed[i] = b
    for i, _ in v.get("pieces", []):
        placed.setdefault(i, b)
    if v.get("heading") is not None:
        placed[v["heading"]] = None
    for i in v.get("after", []):
        placed[i] = None
prefix = {}
for i, it in enumerate(D):
    if i in placed or it["kind"] == "hr":
        continue
    nxt = next((j for j in range(i + 1, len(D)) if placed.get(j)), None)
    if nxt is not None:
        prefix.setdefault(placed[nxt], []).append(i)
        placed[i] = placed[nxt]

seq = []  # (draft index, root id, is_heading)
for blk in R:
    b = blk["id"]
    v = M[b]
    if blk["kind"] == "h":
        if v.get("heading") is not None:
            seq.append((v["heading"], b, True))
        for i in v.get("after", []):
            seq.append((i, b, False))
    else:
        for i in prefix.get(b, []) + v["items"] + [i for i, _ in v.get("pieces", [])]:
            seq.append((i, b, False))

bad = []
heads = [(k, s) for k, s in enumerate(seq) if s[2]]
for k, (h, hb, _) in heads:
    after_wrong = [s for s in seq[k + 1:k + 60] if s[0] < h and not s[2]]
    before_wrong = [s for s in seq[max(0, k - 60):k] if s[0] > h and not s[2]]
    if after_wrong or before_wrong:
        j = pos[hb] - 1
        pu = []
        while j >= 0 and R[j]["kind"] == "h" and M[R[j]["id"]].get("heading") is None:
            pu.insert(0, R[j]["id"])
            j -= 1
        bad.append((hb, h, after_wrong, before_wrong, pu))

print(f"{os.path.basename(draft_path)}: {len(bad)} heading(s) with draft lines on the wrong side")
for hb, h, aw, bw, pu in bad[:40]:
    print(f"  ^{hb} '{D[h]['text'][:35]}'")
    for s in aw[:3]:
        print(f"      under it but before it in the PDF: [{D[s[0]]['kind']}] {D[s[0]]['text'][:45]}  (in ^{s[1]})")
    for s in bw[:3]:
        print(f"      above it but after it in the PDF: [{D[s[0]]['kind']}] {D[s[0]]['text'][:45]}  (in ^{s[1]})")
    if pu:
        print(f"      unmatched root heading(s) just before: {' '.join('^' + x + ' ' + R[pos[x]]['text'][:25] for x in pu)}")
book = os.path.basename(root_path).split("-")[1].split(".")[0]
for t in ("0", f"{book}-0"):
    h = M[t].get("heading")
    print(f"  title ^{t} root '{R[pos[t]]['text']}' <- draft {repr(D[h]['text'][:60]) if h is not None else None}")
