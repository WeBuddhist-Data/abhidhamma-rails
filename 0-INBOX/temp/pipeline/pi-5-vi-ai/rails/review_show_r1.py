import sys, re
B = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch = sys.argv[1]
ids = sys.argv[2:]
def segs(p):
    t = open(p, encoding="utf-8").read()
    out = {}
    for s in t.split("\n\n"):
        m = re.search(r"\^(\S+)\s*$", s.strip())
        if m:
            out[m.group(1)] = s.strip()
    return out
P = segs(B + r"\pali\pi-5_split_chapters\%s" % ch)
V = segs(B + r"\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\%s" % ch)
for i in ids:
    print("=== ^" + i)
    print("PI:", P.get(i))
    print("VI:", V.get(i))
