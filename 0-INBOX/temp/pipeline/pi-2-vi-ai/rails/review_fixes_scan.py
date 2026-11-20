"""Scan: subjectless sentences («Đôi khi …», «Đều …», «Không nên nói …») whose preceding sentence names a subset
(subject is not itself subjectless). Prints part, ID, line, previous-sentence head, sentence head.
usage: review_fixes_scan.py [--bak]
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_fixes_lib import *

vdir = BAK if "--bak" in sys.argv else VDIR
SUBJLESS = re.compile(r"^(Đôi khi|Đều|Không nên nói|Chỉ là|Rằng)\b")
WHOLE = re.compile(r"^(Cả |Về cả )")  # restated whole set (decision 1)
n = 0
for part in PARTS:
    pl, vl, sid = aligned(part, vdir)
    prev_last = ""
    for k, v in enumerate(vl):
        body = ID.sub("", v).strip()
        sents = re.split(r"(?<=[.?”])\s+(?=[A-ZĐÂĂÊÔƠƯÁÀẢÃẠ“])", body)
        for i, s in enumerate(sents):
            prv = sents[i - 1] if i else prev_last
            if (SUBJLESS.match(s) and prv and not SUBJLESS.match(prv) and not WHOLE.match(prv)
                    and not prv.startswith("#")):
                n += 1
                print(f"{part[:3]} ^{sid.get(k)} L{k + 1}: PREV «{prv[:70]}» … «{prv[-40:]}» || «{s[:60]}»")
        prev_last = sents[-1] if sents else ""
print("TOTAL", n)
