"""Show a root region with its Thai mapping, and the draft lines it covers.

Usage: show_region.py <root.md> <draft.md> <map.json> <first_id> <last_id> [max_draft_lines]
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, draft_path, map_path, a_id, z_id = sys.argv[1:6]
mx = int(sys.argv[6]) if len(sys.argv) > 6 else 60
R = parse_root(root_path)
D = parse_draft(draft_path)
M = json.load(open(map_path, encoding="utf-8"))["mapping"]
ids = [b["id"] for b in R]
a, z = ids.index(a_id), ids.index(z_id)
used = []
for b in R[a:z + 1]:
    v = M[b["id"]]
    h = v.get("heading")
    used += v["items"] + ([h] if h is not None else []) + v.get("after", [])
    first = D[v["items"][0]]["text"][:40] if v["items"] else ""
    print(f"^{b['id']:16} {b['kind']} {b['text'][:55]!r:60} H={h if h is None else (h, D[h]['text'][:25])} items={v['items'][:1]}..{v['items'][-1:]} ({len(v['items'])}) {first!r}")
if used:
    lo, hi = min(used), max(used)
    print(f"--- draft {lo}..{hi}")
    for i in range(lo, min(hi + 1, lo + mx)):
        print(i, D[i]["kind"], D[i]["text"][:75].replace("\n", " / "))
