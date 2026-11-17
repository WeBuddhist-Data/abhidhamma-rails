"""Estimate content drift in a Thai map: for each root text block with Thai text, compare the
Pāli/Thai skeleton-trigram cosine of its own Thai with the cosine of that Thai against the
previous and next root text blocks. A block whose Thai fits a neighbour clearly better
(margin) is a drift suspect; runs of suspects in the same direction mark an off-by-one stretch.

Usage: check_drift.py <root.md> <draft.md> <map.json> [margin=0.08]
"""
import json
import math
import os
import sys
import unicodedata
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, draft_path, map_path = sys.argv[1:4]
MARGIN = float(sys.argv[4]) if len(sys.argv) > 4 else 0.08
R = parse_root(root_path)
D = parse_draft(draft_path)
M = json.load(open(map_path, encoding="utf-8"))["mapping"]

TH = {}
for chars, v in (("กขฃคฅฆ", "k"), ("จฉชฌ", "c"), ("ซศษส", "s"), ("ฎฏฐฑฒดตถทธ", "t"), ("งญณนํ", "n"),
                 ("บปผฝพฟภ", "p"), ("ม", "m"), ("ย", "y"), ("รฤ", "r"), ("ลฦฬ", "l"), ("ว", "v"), ("หฮ", "h")):
    for ch in chars:
        TH[ch] = v
PI = {"k": "k", "g": "k", "c": "c", "j": "c", "t": "t", "d": "t", "n": "n", "p": "p", "b": "p",
      "m": "m", "y": "y", "r": "r", "l": "l", "v": "v", "s": "s", "h": "h"}


def sk(s, th):
    if th:
        return "".join(TH[c] for i, c in enumerate(s) if c in TH and not (i + 1 < len(s) and s[i + 1] == "์"))
    s = "".join(c for c in unicodedata.normalize("NFD", s.lower()) if not unicodedata.combining(c))
    out = []
    for c in s:
        if c in PI and not (c == "h" and out and out[-1] in "kctp"):
            out.append(PI[c])
    return "".join(out)


def grams(k):
    return Counter(k[i:i + 3] for i in range(len(k) - 2))


df = Counter()
for b in R:
    df.update(grams(sk(b["text"], False)).keys())
idf = {g: math.log((len(R) + 1) / (c + 1)) + 1 for g, c in df.items()}


def vec(text, th):
    return {g: n * idf[g] for g, n in grams(sk(text, th)).items() if g in idf}


def cos(a, b):
    if len(a) > len(b):
        a, b = b, a
    d = sum(x * b.get(g, 0.0) for g, x in a.items())
    na = math.sqrt(sum(x * x for x in a.values())) or 1.0
    nb = math.sqrt(sum(x * x for x in b.values())) or 1.0
    return d / (na * nb)


tb = [b for b in R if b["kind"] == "t" and b["id"] != "T-1"]
RV = [vec(b["text"], False) for b in tb]
sus = []
for k, b in enumerate(tb):
    items = M[b["id"]]["items"]
    if not items:
        continue
    tv = vec(" ".join(D[i]["text"] for i in items), True)
    own = cos(tv, RV[k])
    prv = cos(tv, RV[k - 1]) if k else 0.0
    nxt = cos(tv, RV[k + 1]) if k + 1 < len(tb) else 0.0
    if max(prv, nxt) > own + MARGIN:
        sus.append((b["id"], "prev" if prv > nxt else "next", round(own, 2), round(max(prv, nxt), 2)))
n_with = sum(1 for b in tb if M[b["id"]]["items"])
# runs: consecutive suspects with the same direction
runs, cur = [], []
idx = {b["id"]: k for k, b in enumerate(tb)}
for s in sus:
    if cur and idx[s[0]] == idx[cur[-1][0]] + 1 and s[1] == cur[-1][1]:
        cur.append(s)
    else:
        if cur:
            runs.append(cur)
        cur = [s]
if cur:
    runs.append(cur)
long_runs = [r for r in runs if len(r) >= 3]
print(f"{os.path.basename(draft_path)}: blocks with Thai {n_with}, drift suspects {len(sus)} ({100 * len(sus) / max(1, n_with):.1f}%), "
      f"runs of >=3 {len(long_runs)} covering {sum(len(r) for r in long_runs)} blocks")
for r in sorted(long_runs, key=len, reverse=True)[:8]:
    print(f"   ^{r[0][0]} .. ^{r[-1][0]} ({len(r)} blocks, Thai fits the {r[0][1]} block)")
