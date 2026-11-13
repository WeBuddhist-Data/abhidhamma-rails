import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load, P, H

FILES = ["5-01-saccayamaka.md", "5-02-saccayamaka.md", "5-03-saccayamaka.md",
         "6-01-sankharayamaka.md", "6-02-sankharayamaka.md"]
IDRE = re.compile(r"\^[0-9-]+\s*$")

mode = sys.argv[1] if len(sys.argv) > 1 else "ids"
for fn in FILES:
    p, h = load(fn)
    if len(p) != len(h):
        print(fn, "LINECOUNT", len(p), len(h))
    for i, (a, b) in enumerate(zip(p, h), 1):
        ia = IDRE.search(a); ib = IDRE.search(b)
        if (ia.group().strip() if ia else None) != (ib.group().strip() if ib else None):
            print(fn, i, "IDMISMATCH", ia and ia.group(), ib and ib.group())
        if mode == "head" and (a.startswith("#") or b.startswith("#") or len(a) < 40):
            print(fn, i, "|", a, "|", b)
    # raw file checks: double blank lines
    for path in (P + fn, H + fn):
        txt = open(path, encoding="utf-8").read()
        if "\n\n\n" in txt:
            print(path, "DOUBLE BLANK")
