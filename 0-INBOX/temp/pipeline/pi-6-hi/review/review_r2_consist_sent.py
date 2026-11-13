import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r2_align import pairs, FILES, IDRE

PI = re.compile(r"(cakkh|sot|ghān|jivh|kāy|rūp|sadd|gandh|ras|phoṭṭhabb|man|dhamm)āyatan", re.I)
HI = re.compile(r"(आँख|कान|नाक|जीभ|शरीर|दृश्य रूप|ध्वनि|गंध|स्वाद|स्पर्श|मन के विषयों|मन) (का|के|की|को) इंद्रिय-क्षेत्र")
ORG = re.compile(r"\b(s|a)(cakkhuk|sotak|ghānak|rūpak|cittak)", re.I)
HORG = re.compile(r"(आँख|कान|नाक|भौतिक रूप|मन) (वाले|से रहित)")

def pskel(s):
    s = IDRE.sub("", s)
    s = re.sub(r"\[[^\]]*\]", "", s)
    s = PI.sub("X", s)
    s = ORG.sub(lambda m: m.group(1).lower() + "ORG", s)
    s = re.sub(r"^\((Ka|Kha|Ga|Gha)\) ", "", s)
    return s.lower()

def hskel(s):
    s = IDRE.sub("", s)
    s = re.sub(r"\[[^\]]*\]", "", s)
    s = HI.sub(lambda m: "X " + m.group(2) + " इंद्रिय-क्षेत्र", s)
    s = HORG.sub(lambda m: "ORG " + m.group(2), s)
    s = re.sub(r"^\((क|ख|ग|घ)\) ", "", s)
    return s

groups = collections.defaultdict(collections.Counter)
where = collections.defaultdict(list)
for f in FILES:
    P, H = pairs(f)
    for k, ((pn, p), (hn, h)) in enumerate(zip(P, H)):
        if p.startswith("#"):
            continue
        a = [s for s in re.split(r"(?<=[.?])\s+", pskel(p)) if s.strip()]
        b = [s for s in re.split(r"(?<=[।?])\s+", hskel(h)) if s.strip()]
        if len(a) != len(b): a, b = [pskel(p)], [hskel(h)]
        for ps, hs in zip(a, b):
            groups[ps][hs] += 1
            where[(ps, hs)].append(f"{f[:4]}#{k+1}")
n = 0
for ps, c in groups.items():
    if len(c) > 1:
        n += 1
        print("P:", ps)
        for hs, cnt in c.most_common():
            print(f"   {cnt}x H: {hs}   @ {where[(ps, hs)][:6]}")
print("groups", len(groups), "inconsistent", n)
