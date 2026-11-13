import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load
from review_r3_struct import FILES

def strip(s):
    return re.sub(r"\s*\^[0-9-]+\s*$", "", s)

for fn in FILES:
    p, h = load(fn)
    for i, (a, b) in enumerate(zip(p, h), 1):
        A, B = strip(a), strip(b)
        probs = []
        da = A.count("–") + A.count("—"); db = B.count("–") + B.count("—")
        if da != db: probs.append(f"DASH {da}/{db}")
        if B.count("-") and re.search(r"\s-\s", B): probs.append("HYPHEN-AS-DASH")
        Bo = re.sub(r"\[[^\]]*\]", "", B)
        lat = re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", Bo)
        if lat: probs.append("LATIN " + ",".join(lat[:5]))
        if re.search(r"[\"']", B): probs.append("STRAIGHTQUOTE")
        if "  " in B: probs.append("DOUBLESPACE")
        if re.search(r"\s[।?,]", B): probs.append("SPACE-BEFORE-PUNCT")
        if "." in Bo: probs.append("PERIOD")
        if not a.startswith("#"):
            qa = A.count("?"); qb = B.count("?")
            if qa != qb: probs.append(f"Q {qa}/{qb}")
            ea = A[-1:]; eb = B[-1:]
            okmap = {".": "।", "?": "?", ")": ")", "…": "…"}
            if okmap.get(ea, ea) != eb:
                probs.append(f"END '{ea}'/'{eb}'")
            # sentence count
            sa = len(re.findall(r"\.(?=\s|$|\))", re.sub(r"\[[^\]]*\]", "", A).replace("…pe…", "…").replace("…Pe…", "…")))
            sb = B.count("।")
            if sa != sb: probs.append(f"SENT {sa}/{sb}")
            # parentheses
            if A.count("(") != B.count("(") or A.count("[") != B.count("["):
                probs.append(f"BRACKETS ({A.count('(')}/{B.count('(')} [{A.count('[')}/{B.count('[')}")
            # ellipses (pe)
            pa = len(re.findall(r"…\s*pe\s*…|…", A, re.I)); pb = B.count("…")
            if pa != pb: probs.append(f"ELLIPSIS {pa}/{pb}")
        if probs:
            print(fn[:4], i, "; ".join(probs))
