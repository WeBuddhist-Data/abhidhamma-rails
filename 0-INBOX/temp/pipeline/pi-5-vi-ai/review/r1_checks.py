import sys, re, unicodedata
# usage: r1_checks.py <chapter.md>
BASE = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
ch = sys.argv[1]
P = open(BASE + r"\pali\pi-5_split_chapters\\" + ch, encoding="utf8").read()
V = open(BASE + r"\vietnamese\pi-5-vietnamese-plain-rails_split_chapters\\" + ch, encoding="utf8").read()
print("NFC:", unicodedata.normalize("NFC", V) == V, "CR:", "\r" in V, "emdash:", V.count("—"), "dblblank:", "\n\n\n" in V)

def segs(t):
    out = []
    for s in re.split(r"\n\s*\n", t.strip()):
        lines = [l for l in s.split("\n") if l.strip()]
        m = re.search(r"\^([\w-]+)\s*$", lines[-1])
        out.append((m.group(1) if m else "?", lines))
    return out

def strip_br(s):
    return re.sub(r"\[[^\]]*\]", " ", s)

PNEG = re.compile(r"(?<![\w])(na|no|natthi|nanu|neva|nāpi|nupalabbhati|nupalabbhanti|nāhaṃ|nāyaṃ|nāssa|nāhosi|nāhesuṃ|nāssu|nevā|nāpī|natthī|natthīti|nupalabbhatīti|nupalabbhatī)(?![\w])", re.I)
VNEG = re.compile(r"(?<![\w])(không|chưa|chẳng)(?![\w])", re.I)
ps, vs = segs(P), segs(V)
tot = dict(am=0, du=0, nh=0, kn=0, pq=0, vq=0)
for (pid, pl), (vid, vl) in zip(ps, vs):
    for i, (a, b) in enumerate(zip(pl, vl)):
        a2, b2 = strip_br(a), strip_br(b)
        am = len(re.findall(r"Āmantā", a2)); du = len(re.findall(r"Đúng vậy", b2))
        nh = len(re.findall(r"Na hevaṃ vattabbe", a2)); kn = len(re.findall(r"Không nên nói như (thế|vậy)", b2))
        pq = a2.count("?"); vq = b2.count("?")
        pn = len(PNEG.findall(a2)); vn = len(VNEG.findall(b2))
        # nanu frame 'Chẳng phải ... sao' counts once; 'có ... không?' question adds a 'không'
        vq_khong = len(re.findall(r"không\s*\?", b2))
        vn_adj = vn - vq_khong
        for k, x in (("am", am), ("du", du), ("nh", nh), ("kn", kn), ("pq", pq), ("vq", vq)):
            tot[k] += x
        flags = []
        if am != du: flags.append("Amanta %d/Dung vay %d" % (am, du))
        if nh != kn: flags.append("NaHevam %d/Khong nen %d" % (nh, kn))
        if pq != vq: flags.append("? %d/%d" % (pq, vq))
        if pn != vn_adj: flags.append("neg P%d V%d" % (pn, vn_adj))
        if flags:
            print("^%s L%d: %s" % (pid, i + 1, "; ".join(flags)))
print(tot)
