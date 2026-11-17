"""Question-count agreement of a Thai map: share of root text blocks with Pāli questions whose
Thai has the same number of questions (Vb/Ds/Dt/Pp: katam- vs ไฉน; Yamaka: ? vs หรือ;
Kathāvatthu: ? vs ?). A proxy for block-level correctness, for comparing two maps.

Usage: q_metric.py <root.md> <draft.md> <book> <map.json> [<map2.json> ...]
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_common import parse_draft, parse_root  # noqa: E402

root_path, draft_path, book = sys.argv[1:4]
R = parse_root(root_path)
D = parse_draft(draft_path)


def qp(t):
    if book in "1234":
        return len(re.findall(r"\bkatam", t.lower()))
    if book == "7":  # Paṭṭhāna: negated conditions (na-hetuyā, naārammaṇe …), presence only
        return 1 if re.search(r"\bna(?!va\b|vahi|vasu)(?=[a-zāīūṭḍṇñṅ])", t.lower()) else 0
    return t.count("?")


def qt(t):
    if book in "1234":
        return t.count("ไฉน")
    if book == "6":
        return t.count("หรือ")
    if book == "7":
        return 1 if "ไม่ใช่" in t else 0
    return t.count("?")


for mp in sys.argv[4:]:
    M = json.load(open(mp, encoding="utf-8"))["mapping"]
    n = ok = stacked = 0
    for b in R:
        if b["kind"] != "t" or b["id"] == "T-1":
            continue
        q = qp(b["text"])
        if not q:
            continue
        n += 1
        it = M[b["id"]]["items"]
        if not it:
            stacked += 1
            continue
        if qt(" ".join(D[i]["text"] for i in it)) == q:
            ok += 1
    print(f"{os.path.basename(mp)}: blocks with questions {n}, same count {ok} ({100 * ok / max(n, 1):.1f}%), stacked {stacked}")
    if book == "7":
        # count sections: Pāli number words <-> Thai "มีวาระ" / 'มี "'
        NW = re.compile(r"\b(ekaṃ|dve|tīṇi|cattāri|pañca|cha|satta|aṭṭha|nava|dasa)\b")
        n2 = ok2 = 0
        for b in R:
            if b["kind"] != "t" or not M[b["id"]]["items"]:
                continue
            n2 += 1
            th = " ".join(D[i]["text"] for i in M[b["id"]]["items"])
            ok2 += (len(NW.findall(b["text"].lower())) >= 2) == ("มีวาระ" in th or 'มี "' in th)
        print(f"   count-section agreement: {ok2}/{n2} ({100 * ok2 / max(n2, 1):.1f}%)")
