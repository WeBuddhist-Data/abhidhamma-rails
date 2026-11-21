"""r1: per-segment count / polarity / list-length cross-check, Pali vs our Vietnamese. Prints mismatches only."""
import re, sys
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-3_split_chapters"
V = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\vietnamese\pi-3-vietnamese-plain-rails_split_chapters"
IDRE = re.compile(r"\^([\w-]+)\s*$")

def segs(path):
    out, buf = {}, []
    order = []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        buf.append(line)
        m = IDRE.search(line)
        if m:
            out[m.group(1)] = buf
            order.append(m.group(1))
            buf = []
    return out, order

PNUM = {"eken": 1, "ekena": 1, "ekāya": 1, "dvīhi": 2, "dvīh": 2, "tīhi": 3, "tīh": 3, "catūhi": 4, "catūh": 4,
        "pañcahi": 5, "pañcah": 5, "chahi": 6, "chah": 6, "sattahi": 7, "sattah": 7, "aṭṭhahi": 8, "aṭṭhah": 8,
        "navahi": 9, "navah": 9, "dasahi": 10, "dasah": 10, "ekādasahi": 11, "ekādasah": 11, "dvādasahi": 12,
        "dvādasah": 12, "dvādas": 12, "terasahi": 13, "pannarasahi": 15, "soḷasahi": 16, "sattarasahi": 17,
        "aṭṭhārasahi": 18}
pw = "|".join(sorted(PNUM, key=len, reverse=True))
PRE = re.compile(r"(na kehici|na kāhici|" + pw + r")\s?(khandhehi|khandhena|dhātūhi|dhātuyā|āyatanehi|āyatanena)|(" + pw + r")(āyatanehi|āyatanena)", re.I)

def pali_counts(t):
    t = t.replace("Dvādasāyatanāni", "ITEM")
    res = []
    for m in PRE.finditer(t):
        if m.group(1):
            n, u = m.group(1), m.group(2)
        else:
            n, u = m.group(3), m.group(4)
        n = n.lower()
        n = 0 if n.startswith("na k") else PNUM[n]
        u = "k" if u.startswith("khandh") else ("a" if u.startswith("āyatan") else "d")
        res.append((n, u))
    return res

VN = {"một": 1, "hai": 2, "ba": 3, "bốn": 4, "năm": 5, "sáu": 6, "bảy": 7, "tám": 8, "chín": 9, "mười": 10,
      "mười một": 11, "mười hai": 12, "mười ba": 13, "mười lăm": 15, "mười sáu": 16, "mười bảy": 17, "mười tám": 18}
vw = "|".join(sorted(VN, key=len, reverse=True))
VRE = re.compile(r"(?<![\wÀ-ỹ])(" + vw + r") (khối|lĩnh vực nhận biết|yếu tố)(?![\wÀ-ỹ])|không có (khối|lĩnh vực nhận biết|yếu tố) nào|không được gộp vào (khối|lĩnh vực nhận biết|yếu tố) nào", re.I)

def vi_counts(t):
    # drop item names that carry a number (not answers)
    t = re.sub(r"(?<![\wÀ-ỹ])(Năm khối|Mười hai lĩnh vực nhận biết|Mười tám yếu tố)(?= được gộp vào bao| được gộp vào năm|,)", "ITEM", t)
    t = re.sub(r"gồm (năm|bốn|một) khối", "ITEM", t)
    t = re.sub(r"sáu lĩnh vực nhận biết (làm|”)", "ITEM", t, flags=re.I)
    t = re.sub(r"cho sáu lĩnh vực nhận biết", "ITEM", t)
    res = []
    for m in VRE.finditer(t):
        if m.group(1):
            n, u = VN[m.group(1).lower()], m.group(2)
        else:
            n, u = 0, (m.group(3) or m.group(4))
        u = "k" if u == "khối" else ("a" if u.startswith("lĩnh") else "d")
        res.append((n, u))
    return res

def pol_p(t):
    return re.findall(r"(asaṅgahit|saṅgahit|vippayutt|sampayutt)", t)

def pol_v(t):
    toks = []
    for m in re.finditer(r"(không được gộp vào|được gộp vào|không gắn liền|gắn liền)", t):
        toks.append(m.group(1))
    return toks

for ch in sys.argv[1:]:
    ps, po = segs(P + "\\" + ch)
    vs, vo = segs(V + "\\" + ch)
    if po != vo:
        print(ch, "ID ORDER MISMATCH", set(po) ^ set(vo))
    for i in po:
        p, v = ps[i], vs.get(i, [])
        if len(p) != len(v):
            print(ch, i, "LINECOUNT", len(p), len(v))
        pt, vt = " ".join(p), " ".join(v)
        pc, vc = pali_counts(pt), vi_counts(vt)
        if pc != vc:
            print(ch, i, "COUNTS\n   P", pc, "\n   V", vc)
        pe = pt.replace("…pe…", "…").count("…")
        ve = vt.count("…")
        if pe != ve:
            print(ch, i, "ELLIPSIS", pe, ve)
        for bad in ("—", "–", "….", "..", '"', "'", "chánh niệm", "\r"):
            if bad in vt and bad not in pt:
                print(ch, i, "TYPO", repr(bad))
        # Latin words outside brackets
        stripped = re.sub(r"\[[^\]]*\]", "", vt)
        stripped = re.sub(r"\^[\w-]+", "", stripped)
        lat = [w for w in re.findall(r"[A-Za-zāīūṅñṭḍṇḷṃ]+", stripped) if re.search(r"[āīūṅñṭḍṇḷṃ]", w)]
        if lat:
            print(ch, i, "PALI-IN-VI", lat)
    print(ch, "segments:", len(po))
