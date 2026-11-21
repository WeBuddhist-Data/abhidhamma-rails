import sys, re
# consistency check of rebuttal-pentad lines: distinct quoted fragments per segment, P vs V
BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch = sys.argv[1]
P = open(BASE + r"\pali\pi-5_split_chapters\\" + ch, encoding="utf8").read()
V = open(BASE + r"\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\\" + ch, encoding="utf8").read()

def segs(t):
    out = []
    for s in re.split(r"\n\s*\n", t.strip()):
        lines = [l for l in s.split("\n") if l.strip()]
        m = re.search(r"\^([\w-]+)\s*$", lines[-1])
        out.append((m.group(1) if m else "?", lines))
    return out

PENT = re.compile(r"^(Ājānāhi|No ce pana|Hañci|Tvaṃ ce pana|Ese ce|Na hevaṃ niggahetabbe|Tena hi yaṃ)")
def frags(line, pali):
    line = re.sub(r"\[[^\]]*\]", "", line)
    parts = re.split(r"[\"“”‘’–]", line)
    out = []
    for p in parts:
        p = p.strip(" ,.;:")
        if pali:
            p = re.sub(r"(ti|nti)$", "", p).strip(" ,.")
            p = re.sub(r"ā$", "a", p)
        if len(p) > 12:
            out.append(p)
    return out

nq = 0
for (pid, pl), (vid, vl) in zip(segs(P), segs(V)):
    pf, vf = set(), set()
    for a, b in zip(pl, vl):
        if PENT.match(a):
            fa, fb = frags(a, True), frags(b, False)
            ca = len(re.findall(r"[\"“”‘’]", a)); cb = len(re.findall(r"[\"“”‘’]", b))
            if ca != cb:
                print("^%s quote-mark count P%d V%d: %s" % (pid, ca, cb, a[:50]))
            pf |= set(fa); vf |= set(fb)
    if pf or vf:
        nq += 1
        if len(pf) != len(vf):
            print("^%s distinct quoted fragments P%d V%d" % (pid, len(pf), len(vf)))
            for x in sorted(vf):
                print("    V:", x[:140])
print("pentad segments:", nq)
