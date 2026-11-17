"""Make a Thai map respect heading boundaries.

The aligner places text by similarity; headings are paired separately, so a Thai line can end up
on the wrong side of a paired heading (an opening question pulled into the block before the
heading, a chapter's "... จบบริบูรณ์" end line pushed under the next chapter's heading, a Thai
heading printed under the root heading it precedes).

1. Paired headings (titles ^0 / ^N-0 excluded) must follow draft order in root order: pairs
   that break it (outside the longest increasing run) are unpaired.
2. The paired headings cut both the root and the draft into segments. Every draft item goes to
   a root text block of its own segment: one that moved back goes to the end of the segment's
   last text block, one that moved forward to the start of its first text block.
3. A segment with no root text block (headings only): its Thai heading lines pair with the
   root headings there that have no Thai heading (in order); anything left is printed under the
   heading that opens the segment ("after").

Usage: fix_heading_bounds.py <root.md> <draft.md> <map_in.json> <map_out.json> <book> <report.txt>
"""
import bisect
import json
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, draft_path, map_in, map_out, book, rep_path = sys.argv[1:7]
R = parse_root(root_path)
D = parse_draft(draft_path)
J = json.load(open(map_in, encoding="utf-8"))
M = J["mapping"]
pos = {b["id"]: k for k, b in enumerate(R)}
TITLES = {"0", f"{book}-0"}
rep = []

# ---- 1. keep the longest run of paired headings that follows draft order
pairs = [(pos[b["id"]], M[b["id"]]["heading"], b["id"]) for b in R
         if b["kind"] == "h" and M[b["id"]].get("heading") is not None]
# longest increasing subsequence on draft index
tails, tail_idx, prev = [], [], [-1] * len(pairs)
for k, (_, h, _) in enumerate(pairs):
    j = bisect.bisect_left(tails, h)
    if j == len(tails):
        tails.append(h)
        tail_idx.append(k)
    else:
        tails[j] = h
        tail_idx[j] = k
    prev[k] = tail_idx[j - 1] if j else -1
keep = set()
k = tail_idx[-1] if tail_idx else -1
while k != -1:
    keep.add(k)
    k = prev[k]
for k, (_, h, b) in enumerate(pairs):
    if k not in keep:
        M[b]["heading"] = None
        rep.append(f"UNPAIR ^{b} (out of draft order): '{D[h]['text'][:50]}'")
kept = [p for k, p in enumerate(pairs) if k in keep]

# ---- 1b. a Thai heading printed twice (section name, then the same name again as the section's
# end line, e.g. "นวกนิทเทส" ... "นวกนิทเทส"): if the root heading is paired with the later one
# while the text after it starts at the earlier one, pair it with the earlier one.
def _nh(s):
    return re.sub(r"[\s\[\]().]|^[๐-๙]+\.\s*", "", s)


text_after = {}
for k, b in enumerate(R):
    if b["kind"] == "h":
        nxt = next((x for x in R[k + 1:] if x["kind"] == "t"), None)
        text_after[b["id"]] = nxt["id"] if nxt else None
for n, (rp, h, b) in enumerate(kept):
    tb = text_after.get(b)
    if not tb or not M[tb]["items"]:
        continue
    first = min(M[tb]["items"])
    if first >= h:
        continue
    lo = kept[n - 1][1] if n else -1
    cands = [i for i in range(max(lo + 1, first), h) if D[i]["kind"] == "h" and _nh(D[i]["text"]) == _nh(D[h]["text"])]
    if cands:
        new = cands[0]
        M[b]["heading"] = new
        kept[n] = (rp, new, b)
        if new in M[tb]["items"]:
            M[tb]["items"].remove(new)
        M[tb]["items"] = sorted(M[tb]["items"] + [h])  # the later copy: an end line, text for now
        rep.append(f"REPAIR ^{b}: '{D[h]['text'][:40]}' {h} -> earlier copy {new}")
k_root = [p[0] for p in kept]
k_draft = [p[1] for p in kept]
title_items = {M[t]["heading"] for t in TITLES if t in M and M[t].get("heading") is not None}


def seg_root(rp):
    return bisect.bisect_left(k_root, rp)


def seg_draft(i):
    return bisect.bisect_left(k_draft, i)


# ---- 2. collect every draft item with its current owner
seg_text = defaultdict(list)  # segment -> root text block ids in root order
seg_unmatched = defaultdict(list)  # segment -> root heading ids with no Thai heading
for b in R:
    s = seg_root(pos[b["id"]])
    if b["kind"] == "t":
        seg_text[s].append(b["id"])
    elif b["id"] not in TITLES and M[b["id"]].get("heading") is None:
        seg_unmatched[s].append(b["id"])

owner = {}
for b, v in M.items():
    for i in v["items"]:
        owner[i] = ("t", b)
    for i in v.get("after", []):
        owner[i] = ("a", b)
heading_items = set(k_draft) | title_items
# orphans (the renderer would put them in the next block): give them an owner first
for i, it in enumerate(D):
    if it["kind"] == "hr" or i in owner or i in heading_items:
        continue
    owner[i] = ("o", None)

moves = []
for i in sorted(owner):
    kind, b = owner[i]
    if b == "T-1" or i < (min(title_items) if title_items else -1):
        continue  # homage and anything before the title page: root order, leave as is
    s = seg_draft(i)
    cur = seg_root(pos[b]) if b is not None else None
    if kind == "a":
        cur = seg_root(pos[b]) + 1 if b in {p[2] for p in kept} else seg_root(pos[b])
    if cur == s:
        continue
    moves.append((i, kind, b, s, cur))

# ---- 3. apply the moves
def remove(i, kind, b):
    if kind == "t":
        M[b]["items"].remove(i)
    elif kind == "a":
        M[b]["after"].remove(i)


pending_after = defaultdict(list)
thai_heads = []  # Thai-only section names moved into the next block
for i, kind, b, s, cur in moves:
    remove(i, kind, b)
    tb = seg_text.get(s, [])
    if tb:
        # moved back: end of the segment's last text block; moved forward: start of its first
        dest = tb[-1] if cur is not None and cur > s else tb[0]
        M[dest]["items"] = sorted(M[dest]["items"] + [i])
        rep.append(f"MOVE {D[i]['kind']:5} '{D[i]['text'][:45]}'  ^{b} -> ^{dest}")
    else:
        pending_after[s].append(i)

NOT_NAME = re.compile(r'"|\sมี\s|^ใน|พึง|ผู้มีปัญญา|เหมือน|ฯลฯ|^บท|^หัวข้อ')
TH_SK = {}
for chars, v in (("กขฃคฅฆ", "k"), ("จฉชฌ", "c"), ("ซศษส", "s"), ("ฎฏฐฑฒดตถทธ", "t"), ("งญณนํ", "n"),
                 ("บปผฝพฟภ", "p"), ("ม", "m"), ("ย", "y"), ("รฤ", "r"), ("ลฦฬ", "l"), ("ว", "v"), ("หฮ", "h")):
    for ch in chars:
        TH_SK[ch] = v
PI_SK = {"k": "k", "g": "k", "c": "c", "j": "c", "t": "t", "d": "t", "n": "n", "p": "p", "b": "p",
         "m": "m", "y": "y", "r": "r", "l": "l", "v": "v", "s": "s", "h": "h"}


def _sk(s, th):
    import unicodedata
    if th:
        s = s.replace("รร", "")  # ธรรม / กรรม / วรรค: Thai spelling of Pāli -amm- / -agg-
        k = "".join(TH_SK[c] for i, c in enumerate(s) if c in TH_SK and not (i + 1 < len(s) and s[i + 1] == "์"))
    else:
        s = "".join(c for c in unicodedata.normalize("NFD", s.lower()) if not unicodedata.combining(c))
        out = []
        for c in s:
            if c in PI_SK and not (c == "h" and out and out[-1] in "kctp"):
                out.append(PI_SK[c])
        k = "".join(out)
    return re.sub(r"(.)\1+", r"\1", k)  # doubled consonants count once


def head_sim(pi, th):
    p = re.sub(r"^\(?(ka|kha|ga|gha)\)\s*", "", pi.lower().strip("* "))
    t = re.sub(r"^[๐-๙]+\.\s*", "", th.strip())
    if p.startswith("uddes") and (t.startswith("อุทเทส") or t == "มาติกา"):
        return 1.0
    if p.startswith("niddes") and t.startswith("นิทเทส"):
        return 1.0
    a, b = _sk(pi, False), _sk(th, True)
    ga = {a[i:i + 3] for i in range(len(a) - 2)}
    gb = {b[i:i + 3] for i in range(len(b) - 2)}
    return len(ga & gb) / max(1, min(len(ga), len(gb)))


for s, items in pending_after.items():
    items.sort()
    um = list(seg_unmatched.get(s, []))
    # text printed between two headings with no root text between them (e.g. a list the Thai
    # prints before its "อุทเทสวาร" heading) belongs to the next root text block: it goes forward
    nxt_seg = next((x for x in range(s + 1, len(kept) + 1) if seg_text.get(x)), None)
    # centred Thai lines that are content, not section names (count lines "ในอธิปติปัจจัย มี " ๕",
    # instructions "พึงนับอย่างนี้"), go forward with the text
    for i in [i for i in items if D[i]["kind"] != "h" or NOT_NAME.search(D[i]["text"].strip())]:
        if nxt_seg is None:
            continue
        dest = seg_text[nxt_seg][0]
        M[dest]["items"] = sorted(M[dest]["items"] + [i])
        items.remove(i)
        rep.append(f"FWD   {D[i]['kind']:5} '{D[i]['text'][:45]}' -> ^{dest} (Thai prints it before the heading)")
    heads = [i for i in items if D[i]["kind"] == "h"]
    # pair Thai heading lines with unmatched root headings there, in order, when the names match
    j = 0
    for b in um:
        for jj in range(j, len(heads)):
            if head_sim(R[pos[b]]["text"], D[heads[jj]]["text"]) >= 0.5:
                i = heads[jj]
                M[b]["heading"] = i
                items.remove(i)
                rep.append(f"PAIR  ^{b} ({R[pos[b]]['text'][:25]}) <- '{D[i]['text'][:45]}'")
                j = jj + 1
                break
    if items:
        # Thai-only section names with no root heading: they open the next root text block as
        # bold lines and share its block ID (user decision 2026-11-17: no IDs of their own)
        if nxt_seg is None:
            rep.append(f"!! no place for {[D[i]['text'][:30] for i in items]}")
            continue
        dest = seg_text[nxt_seg][0]
        M[dest]["items"] = sorted(M[dest]["items"] + items)
        thai_heads.extend(items)
        for i in items:
            rep.append(f"FWD   h     '{D[i]['text'][:45]}' -> ^{dest} (Thai-only heading, opens the block)")

# any line still printed "under a heading" (an older map's "after" list) opens the first root
# text block after that heading instead: no line stands outside a block
for k, b in enumerate(R):
    v = M[b["id"]]
    if not v.get("after"):
        continue
    nxt = next((x["id"] for x in R[k + 1:] if x["kind"] == "t"), None)
    if nxt is None:
        rep.append(f"!! no block after ^{b['id']} for {v['after']}")
        continue
    M[nxt]["items"] = sorted(M[nxt]["items"] + v["after"])
    thai_heads.extend(i for i in v["after"] if D[i]["kind"] == "h")
    for i in v["after"]:
        rep.append(f"FWD   {D[i]['kind']:5} '{D[i]['text'][:45]}' (under ^{b['id']}) -> ^{nxt}")
    v["after"] = []
J["mapping"] = M
J["thai_heads"] = sorted(thai_heads)  # rendered bold at the start of their block
json.dump(J, open(map_out, "w", encoding="utf-8"), ensure_ascii=False)
n_move = sum(1 for r in rep if r.startswith("MOVE"))
n_pair = sum(1 for r in rep if r.startswith("PAIR"))
n_after = sum(1 for r in rep if r.startswith("AFTER"))
n_un = sum(1 for r in rep if r.startswith("UNPAIR"))
summary = f"th-{book}: unpaired {n_un}, moved {n_move}, newly paired headings {n_pair}, under-heading lines {n_after}"
open(rep_path, "w", encoding="utf-8").write(summary + "\n" + "\n".join(rep) + "\n")
print(summary)
