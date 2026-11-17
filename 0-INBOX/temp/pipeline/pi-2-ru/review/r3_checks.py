import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-ru\review")
from r3_align import load

CHS = ["7-satipatthanavibhango.md", "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md",
       "10-bojjhangavibhango.md", "11-maggangavibhango.md", "12-jhanavibhango.md"]

PI_NEG = re.compile(r"\b(na|no|neva|natthi|nāsātaṃ|nānubyañjanaggāhī|nākusalaṃ)\b", re.I)
RU_NEG = re.compile(r"(?<![а-яё])(не|ни|нет|нельзя)(?![а-яё])", re.I)
PI_SIYA = re.compile(r"\bsiyā\b", re.I)
RU_SIYA = re.compile(r"иногда", re.I)
PI_PE = re.compile(r"…\s*pe\s*…")
NUMS_PI = {"eka": 1, "dve": 2, "dvi": 2, "tīṇi": 3, "tayo": 3, "cattāro": 4, "cattāri": 4, "catunnaṃ": 4, "catasso": 4,
           "pañca": 5, "cha": 6, "satta": 7, "sattannaṃ": 7, "aṭṭh": 8, "pañcaṅgik": 5, "caturaṅgik": 4, "tivaṅgik": 3, "duvaṅgik": 2}
ORD_PI = ["paṭham", "dutiy", "tatiy", "catutth", "pañcam"]
ORD_RU = ["перв", "втор", "трет", "четвёрт", "пят"]

def strip_brackets(s):
    return re.sub(r"\[[^\]]*\]", "", s)

total = 0
for ch in CHS:
    p, r, pt, rt = load(ch)
    total += len(p)
    for (pid, pl), (rid, rl) in zip(p, r):
        for k, (a, b) in enumerate(zip(pl, rl)):
            a2, b2 = strip_brackets(a), strip_brackets(b)
            msgs = []
            # ellipsis
            npe = len(PI_PE.findall(a2)) + a2.count("…") - 2 * len(PI_PE.findall(a2))
            nru = b2.count("…")
            if len(PI_PE.findall(a2)) != nru:
                msgs.append(f"pe {len(PI_PE.findall(a2))} vs … {nru}")
            ps, rs = len(PI_SIYA.findall(a2)), len(RU_SIYA.findall(b2))
            if ps != rs:
                msgs.append(f"siyā {ps} vs иногда {rs}")
            for i, (po, ro) in enumerate(zip(ORD_PI, ORD_RU)):
                cp = len(re.findall(po, a2, re.I)); cr = len(re.findall(ro, b2, re.I))
                if cp != cr and not (po == "paṭham" and "pathav" in a2):
                    msgs.append(f"ord {po} {cp} vs {cr}")
            # Latin outside brackets
            lat = re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{3,}", b2)
            lat = [x for x in lat if x not in ("pe",)]
            if lat:
                msgs.append("latin " + ",".join(lat[:5]))
            if re.search(r"\bли\b", b2):
                msgs.append("ли")
            if "—" in b:
                msgs.append("emdash")
            if re.search(r"[,;:.?](?=[А-Яа-яЁё«])", b):
                msgs.append("nospace " + re.search(r".{10}[,;:.?](?=[А-Яа-яЁё«]).{10}", b).group(0))
            if "  " in b:
                msgs.append("double space")
            if re.search(r"(?<![а-яё])(\w+) \1(?![а-яё])", b2, re.I):
                m = re.search(r"(?<![а-яё])(\w+) \1(?![а-яё])", b2, re.I)
                msgs.append("repeat " + m.group(0))
            if b.rstrip().endswith(("^" + pid,)) is False and k == len(pl) - 1:
                msgs.append("id end")
            if not re.search(r"[.?!»…:]\s*(\^[0-9a-z-]+)?\s*$", b) and not b.startswith("#"):
                msgs.append("end punct")
            if msgs:
                print(ch, pid, k, "; ".join(msgs))
print("segments", total)
