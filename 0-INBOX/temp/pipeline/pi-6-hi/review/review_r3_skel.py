import re, sys, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load
from review_r3_struct import FILES

PI = r"(dukkha|samudaya|nirodha|magga|kāya|vacī|citta)(sacc|saṅkhār)\w*"
HI = r"(दुःख|उत्पत्ति|अंत|मार्ग) (का|के) सत्य|(शरीर|वाणी|मन) की रचना"

def strip(s):
    s = re.sub(r"\s*\^[0-9-]+\s*$", "", s)
    s = re.sub(r"^\((Ka|Kha|Ga|Gha|Ṅa|क|ख|ग|घ|ङ)\)\s*", "", s)
    return s

def sents(s, hindi):
    s = re.sub(r"\[[^\]]*\]", "[VAR]", s)
    parts = re.split(r"(?<=[।?])\s+" if hindi else r"(?<=[.?])\s+", s)
    return [x for x in parts if x.strip()]

def skp(s):
    s = re.sub(PI, "ITEM", s, flags=re.I)
    return s.lower()

def skh(s):
    s = re.sub(HI, "ITEM", s)
    for a, b in (("होती", "होता"), ("हुई", "हुआ"), ("थी", "था"), ("होगी", "होगा")):
        s = re.sub(a + r"(?=[\s,।?…)]|$)", b, s)
    return s

groups = collections.defaultdict(lambda: collections.defaultdict(list))
mism = 0
for fn in FILES:
    p, h = load(fn)
    for i, (a, b) in enumerate(zip(p, h), 1):
        if a.startswith("#"): continue
        sa, sb = sents(strip(a), False), sents(strip(b), True)
        if len(sa) != len(sb):
            mism += 1
            continue
        for x, y in zip(sa, sb):
            groups[skp(x)][skh(y)].append(f"{fn[:4]}:{i}")

mode = sys.argv[1] if len(sys.argv) > 1 else "incons"
if mode == "incons":
    n = 0
    for k, v in groups.items():
        if len(v) > 1:
            n += 1
            print("P:", k)
            for hk, locs in sorted(v.items(), key=lambda t: -len(t[1])):
                print(f"   [{len(locs)}] {hk}  @ {','.join(locs[:4])}")
    print("groups", len(groups), "inconsistent", n, "unpaired lines", mism)

