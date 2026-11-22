import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs
M = {"Ka": "a", "Kha": "b", "Ga": "c", "Gha": "d", "Ṅa": "đ", "Ca": "e", "Cha": "g", "Ja": "h"}
c = collections.Counter()
for f, n, sid, p, v in pairs():
    pl = re.findall(r"\((Ka|Kha|Ga|Gha|Ṅa|Ca|Cha|Ja)\)", p)
    vl = re.findall(r"\((a|b|c|d|đ|e|g|h)\)", v)
    if [M[x] for x in pl] != vl:
        c[f] += 1
        print(f, n, pl, vl, v[:120])
    # parenthesised digits kept
    if re.findall(r"\((\d+)\)", p) != re.findall(r"\((\d+)\)", v):
        print("DIGITS", f, n)
print(c)
