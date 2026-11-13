import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *
# print every line that is a ^7-U note line, or contains a non-count parenthesis, or {variant}, or quotes
mode = sys.argv[1] if len(sys.argv) > 1 else "U"
for fi, f in enumerate(FILES):
    for r in pairs(f):
        p, h = r["p"], r["h"]
        if mode == "U" and "^7-U" in p:
            print(f"{fi}|{r['id']}|k{r['k']}\n  P: {p}\n  H: {h}")
        elif mode == "paren":
            ps = re.findall(r"\((?!\d+\))[^()]*(?:\([^()]*\)[^()]*)*\)", IDRE.sub("", p))
            hs = re.findall(r"\((?!\d+\))[^()]*(?:\([^()]*\)[^()]*)*\)", IDRE.sub("", h))
            if "^7-U" in p:
                continue
            if ps or hs:
                print(f"{fi}|{r['id']}|k{r['k']}: " + " || ".join(f"{a}  =>  {b}" for a, b in zip(ps, hs)) + ("" if len(ps) == len(hs) else f"  !!COUNT {len(ps)} {len(hs)} {ps} {hs}"))
        elif mode == "var" and "{" in p:
            print(f"{fi}|{r['id']}|k{r['k']}\n  P: {p}\n  H: {h}")
        elif mode == "k" and fi == int(sys.argv[2]) and r["k"] in [int(x) for x in sys.argv[3].split(",")]:
            print(f"{fi}|{r['id']}|k{r['k']}\n  P: {p}\n  H: {h}")
