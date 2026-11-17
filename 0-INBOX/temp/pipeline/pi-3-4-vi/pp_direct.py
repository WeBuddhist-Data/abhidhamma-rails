"""Puggalapaññatti: align a niddesa chapter directly, person by person, where the counts match.

Each root block of a chapter asks about one person ("Katamo ca puggalo …?"); each Vietnamese
unit opens with one ("Người … ra sao?"). Where the chapter has as many Vietnamese person
questions as root person questions, the Vietnamese text of the chapter is cut at those questions
and given to the root blocks in order (text before the first question goes with the first),
replacing the Thai-pivot assignment of that chapter.

Usage: pp_direct.py <root.md> <vi-4-draft.md> <map.json> <map_out.json> <chapter heading id> [...]
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "th-tools"))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, draft_path, map_in, map_out = sys.argv[1:5]
chapters = sys.argv[5:]
R = parse_root(root_path)
V = parse_draft(draft_path)
J = json.load(open(map_in, encoding="utf-8"))
M = J["mapping"]
PQ = re.compile(r"\bkatam\w*\s+(?:ca\s+)?(?:\w+\s+)?puggal", re.I)
VQ = re.compile(r"^(?:\d+\.\s+)?(?:Người|Bực|Hạng|Những)[^?.!]{0,160}\b(?:ra sao|thế nào|là ai|là những ai)\?")

for cid in chapters:
    k0 = next(k for k, b in enumerate(R) if b["id"] == cid)
    lvl = R[k0]["level"]
    blks = []
    for b in R[k0 + 1:]:
        if b["kind"] == "h" and b["level"] <= lvl:
            break
        if b["kind"] == "t":
            blks.append(b["id"])
    # Vietnamese range: the paired heading of this chapter up to the next paired heading
    v0 = M[cid]["heading"]
    nxt = [M[b["id"]]["heading"] for b in R[k0 + 1:] if b["kind"] == "h" and M[b["id"]].get("heading") is not None]
    v1 = min([x for x in nxt if x > v0] or [len(V)])
    lines = [i for i in range(v0 + 1, v1) if V[i]["kind"] in ("p", "li")]
    # sentences, so that a question inside a line can start a unit
    sents = []
    for i in lines:
        for s in re.split(r"(?<=[.?!…])\s+(?=\S)", V[i]["text"]):
            sents.append((i, s))
    starts = [n for n, (_, s) in enumerate(sents) if VQ.match(s)]
    qblocks = [b for b in blks if PQ.search(R[next(k for k, x in enumerate(R) if x["id"] == b)]["text"])]
    if len(starts) != len(qblocks):
        print(f"{cid}: Vietnamese person questions {len(starts)} vs root {len(qblocks)}: left as it is")
        continue
    # clear this chapter's Vietnamese (wherever it was placed) and its blocks
    rng = set(range(v0 + 1, v1))
    for b, v in M.items():
        v["items"] = [i for i in v["items"] if i not in rng]
        v["pieces"] = [p for p in v.get("pieces", []) if p[0] not in rng]
    cuts = starts[1:] + [len(sents)]
    prev = 0
    for b, end in zip(qblocks, cuts):
        chunk = sents[prev:end]
        # one piece per Vietnamese line (sentences of one line joined again)
        by_line = {}
        for i, s in chunk:
            by_line.setdefault(i, []).append(s)
        M[b]["pieces"].extend((i, " ".join(ss)) for i, ss in by_line.items())
        prev = end
    print(f"{cid}: {len(qblocks)} root blocks aligned person by person")
J["mapping"] = M
json.dump(J, open(map_out, "w", encoding="utf-8"), ensure_ascii=False)
