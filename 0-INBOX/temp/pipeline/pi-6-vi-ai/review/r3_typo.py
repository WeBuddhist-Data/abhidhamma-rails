"""r3: typography on our Vietnamese (line endings, ellipsis spacing, double spaces, '?' needs a question word). Console only."""
import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
import r3_check as C

for fn in C.FILES:
    P, V = C.lines(C.PI + fn), C.lines(C.VI + fn)
    for i, (p, v) in enumerate(zip(P, V)):
        if v.startswith("#"):
            continue
        t = C.ID_RE.sub("", v).rstrip()
        if not re.search(r"[.?)…]$", t):
            print(fn, i, "END", repr(t[-25:]))
        if " …" in t:
            print(fn, i, "SPACE-ELLIPSIS", repr(t[t.index(" …") - 20:t.index(" …") + 6]), "| PI:", "…pe…" in p and repr(p[p.index("…pe…") - 12:p.index("…pe…") + 6]))
        if "  " in t:
            print(fn, i, "DOUBLE-SPACE")
        for q in re.findall(r"[^.?]*\?", t):
            if not re.search(r"\bkhông\?$|\bkhông có\?$", q.strip()) and "…" not in q[-4:]:
                print(fn, i, "QWORD", repr(q[-40:]))
        if re.search(r"\s[,.]", t):
            print(fn, i, "SPACE-PUNCT")
