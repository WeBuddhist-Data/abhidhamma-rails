import sys, re, collections, unicodedata
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\review")
from r4_common import pairs, FILES

only = sys.argv[1].split(",") if len(sys.argv) > 1 and sys.argv[1] != "all" else None
feats = sys.argv[2].split(",") if len(sys.argv) > 2 and sys.argv[2] != "any" else None
maxshow = int(sys.argv[3]) if len(sys.argv) > 3 else 400

W = r"[a-zāīūṃṅñṭḍṇḷ]+"


def pw(p):
    return re.findall(W, p.lower())


NEG_FUSED = re.compile(r"^(appahīn|nānusent|nuppajj|nappajah|nanirodh|nakāma|narūpa|naarūpa|avītikkant|asamāhit|avimutt|amahaggat|acakkhuk|aghānak|asotak|ajivhak|akāyak|ahetuk|acittak|anuppann|anirujjh|apariññ|abhāvit|asacchik|anuppajj|aniruddh|aniruddh|apurisak|anitthik|aitthik|anaññāt)")


def p_neg(p):
    n = 0
    for w in pw(p):
        if w in ("na", "no", "natthi", "nāssa", "neva"):
            n += 1
        elif NEG_FUSED.match(w):
            n += 1
        n += w.count("vippayutt")
    # denied negative after no ca: "no ca ... na V" / "no ca ... appahīno" -> positive
    for m in re.finditer(r"\bno ca\b([^.?]*)", p):
        seg = m.group(1)
        if re.search(r"\bna\b|appahīn|nuppajj|nānusent", seg):
            n -= 2
    return n


def v_neg(v):
    s = v
    s = re.sub(r"không\?", "?", s)  # question particle
    s = s.replace("không xác định về mặt đạo đức", "")
    s = s.replace("không trở lại", "")
    s = s.replace("Vô Tưởng", "VT")
    s = s.replace("cũng không có", "")
    s = s.replace("không hình sắc", "")
    s = s.replace("Không nên nói", "không nên nói")
    n = len(re.findall(r"(?i)\b(không|chưa|chẳng)\b", s))
    return n


def p_ans(p):
    a = []
    for m in re.finditer(r"\?\s*(Āmantā|No|Natthi)\b", p):
        a.append({"Āmantā": "Y", "No": "N", "Natthi": "X"}[m.group(1)])
    return a


def v_ans(v):
    a = []
    for m in re.finditer(r"\?\s*(Đúng vậy|Không có|Không)\b", v):
        a.append({"Đúng vậy": "Y", "Không": "N", "Không có": "X"}[m.group(1)])
    return a


def p_tense(p):
    l = p.lower()
    return (len(re.findall(r"ittha|itthā", l)),
            len(re.findall(r"iss(?:ati|anti|atī|antī)", l)),
            len(re.findall(r"māna", l)))


def v_tense(v):
    l = v.lower()
    past = len(re.findall(r"\bđã\b", l)) - len(re.findall(r"đã được dứt bỏ|đã vượt|đã hiểu biết trọn vẹn|đã chết|đã được hiểu|đã được tu|đã được chứng", l)) - len(re.findall(r"trạng thái đã", l))
    past += len(re.findall(r"chưa từng", l))
    fut = len(re.findall(r"\bsẽ\b", l))
    prs = len(re.findall(r"\bđang\b", l)) - len(re.findall(r"đang tái sinh|đang diễn ra|đang nhập|đang chết", l))
    return past, fut, prs


NUM_P = {"dvinnaṃ": "hai", "tiṇṇaṃ": "ba", "catunnaṃ": "bốn", "pañcannaṃ": "năm", "channaṃ": "sáu",
         "sattannaṃ": "bảy", "aṭṭhannaṃ": "tám", "dvīsu": "hai", "tīsu": "ba", "catūsu": "bốn"}


NUMS = {"hai": r"dvinna|dvīsu|\bdve\b|dvinnaṃ|dvayaṃ", "ba": r"tiṇṇa|tīsu|\btayo\b|\btīṇi\b",
        "bốn": r"catunna|catūsu|\bcattāro\b", "năm": r"pañcanna|\bpañca\b", "sáu": r"channa|\bcha\b",
        "bảy": r"sattanna|\bsatta\b|satteva", "tám": r"aṭṭhanna|\baṭṭha\b"}


def nums(p, v):
    out = []
    pl = unicodedata.normalize("NFC", p.lower())
    vl = v.lower()
    for t, pat in NUMS.items():
        a = len(re.findall(pat, pl))
        b = len(re.findall(r"(?<![\wà-ỹ])" + t + r"(?![\wà-ỹ])", vl))
        if a != b:
            out.append(f"{t}:{a}/{b}")
    return out


counts = collections.Counter()
shown = collections.Counter()
for f, n, sid, p, v in pairs(only):
    if p.startswith("#"):
        continue
    probs = []
    if p.count("?") != v.count("?"):
        probs.append(f"Q {p.count('?')}/{v.count('?')}")
    pa, va = p_ans(p), v_ans(v)
    if pa != va:
        probs.append(f"ANS {pa}/{va}")
    pn, vn = p_neg(p), v_neg(v)
    if pn != vn:
        probs.append(f"NEG {pn}/{vn}")
    pt, vt = p_tense(p), v_tense(v)
    if pt[0] != vt[0]:
        probs.append(f"PAST {pt[0]}/{vt[0]}")
    if pt[1] != vt[1]:
        probs.append(f"FUT {pt[1]}/{vt[1]}")
    if pt[2] != vt[2]:
        probs.append(f"PRS {pt[2]}/{vt[2]}")
    nm = nums(p, v)
    if nm:
        probs.append("NUM " + " ".join(nm))
    if p.count("–") != v.count("–"):
        probs.append(f"DASH {p.count('–')}/{v.count('–')}")
    if "….". __len__() and "…." in v:
        probs.append("DOTS")
    npe = len(re.findall(r"…\s*p[ae]\s*…", p, re.I))
    nell = len(re.findall(r"…", re.sub(r"…\s*p[ae]\s*…", "", p, flags=re.I)))
    if npe + nell != v.count("…"):
        probs.append(f"PE {npe}+{nell}/{v.count('…')}")
    if p.count(".") and not v.rstrip().rstrip("^0123456789-").rstrip().endswith((".", "?", "…", ")", "]")):
        probs.append("END")
    for pr in probs:
        k = pr.split()[0]
        if feats and k not in feats:
            continue
        counts[(f, k)] += 1
        if shown[k] < maxshow:
            shown[k] += 1
            print(f"{f}:{n} {sid} {pr}\n  P: {p.strip()}\n  V: {v.strip()}")
for k, c in sorted(counts.items()):
    print(k, c)
