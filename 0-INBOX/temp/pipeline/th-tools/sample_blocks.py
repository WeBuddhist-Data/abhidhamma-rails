"""Print random root text blocks with the start and end of their Thai, for a manual check.

Usage: sample_blocks.py <root.md> <draft.md> <map.json> <n> [seed]
"""
import json
import os
import random
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, draft_path, map_path, n = sys.argv[1:5]
seed = int(sys.argv[5]) if len(sys.argv) > 5 else 1
R = parse_root(root_path)
D = parse_draft(draft_path)
M = json.load(open(map_path, encoding="utf-8"))["mapping"]
tb = [b for b in R if b["kind"] == "t" and M[b["id"]]["items"]]
random.seed(seed)
for b in sorted(random.sample(tb, int(n)), key=lambda x: R.index(x)):
    it = M[b["id"]]["items"]
    th = " / ".join(D[i]["text"].replace("\n", " ") for i in it)
    print(f"^{b['id']}: {b['text'][:110]!r}  ...  {b['text'][-60:]!r}")
    print(f"   TH({len(it)}): {th[:130]!r}  ...  {th[-70:]!r}")
