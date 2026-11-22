"""r3: structural bilingual check of pi-6 anusaya-yamaka chapters 7-02..7-08.
Reads Pali + our Vietnamese, compares per line/sentence: anusaya-name order,
person tokens, place tokens, verb polarity, answers, '?' counts. Prints only."""
import re, sys, unicodedata

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PI = ROOT + r"\AI_translation\pali\pi-6_split_chapters\\"
VI = ROOT + r"\AI_translation\vietnamese\pi-6-vietnamese-plain-rails_split_chapters\\"
FILES = ["7-0%d-anusayayamaka.md" % i for i in range(2, 9)]

def nfc(s):
    return unicodedata.normalize("NFC", s)

def lines(path):
    with open(path, encoding="utf-8") as f:
        return [nfc(l.rstrip("\n")) for l in f if l.strip()]

ID_RE = re.compile(r"\s\^([0-9a-z-]+)\s*$")

def split_sent(s):
    s = ID_RE.sub("", s).strip()
    # split after . or ? followed by space and an uppercase/paren char
    parts = re.split(r"(?<=[.?])\s+(?=[A-ZÀ-ỸĀĪŪṆÑṬḌṄĐ])", s)
    return [p for p in parts if p.strip()]

# ---------- anusaya names ----------
PN = [("K", r"kāmarāg"), ("B", r"bhavarāg"), ("P", r"paṭigh"), ("M", r"mānānusay"),
      ("D", r"diṭṭhānusay"), ("V", r"vicikicch"), ("A", r"avijj")]
VN = [("K", r"tham đắm dục lạc"), ("B", r"tham đắm hiện hữu"), ("P", r"ác cảm"),
      ("M", r"kiêu mạn"), ("D", r"quan điểm"), ("V", r"hoài nghi"), ("A", r"vô minh")]

def seq(text, table):
    hits = []
    for tag, rx in table:
        for m in re.finditer(rx, text, flags=re.I):
            hits.append((m.start(), tag))
    hits.sort()
    # drop overlaps
    out, last = [], -1
    for pos, tag in hits:
        if pos >= last:
            out.append(tag)
            last = pos + 1
    return out

# ---------- persons ----------
PP = [("SOM", r"sotāpattimagg"), ("SAM", r"sakadāgāmimagg"), ("ANM", r"anāgāmimagg"),
      ("AGG", r"aggamagg"), ("ARM", r"arahattamagg"),
      ("PU", r"puthujjan"), ("SO", r"sotāpann"), ("SA", r"sakadāgāmi(?!magg)"),
      ("AN", r"anāgāmi(?!magg)|anāgāmī"), ("AR", r"\barah(?:ato|ā|ant)"),
      ("8", r"aṭṭhamak"), ("N2", r"\b(?:dvinnaṃ|dve)\b"), ("N3", r"\b(?:tiṇṇaṃ|tayo)\b"),
      ("N4", r"\b(?:catunnaṃ|cattāro)\b"), ("N5", r"\b(?:pañcannaṃ|pañca)\b"),
      ("REST", r"avasesā|avasesānaṃ"), ("EXC", r"ṭhapetvā"), ("SAME", r"tesaññeva|tasseva|\bteva\b|\bsveva\b|tesaṃyeva|tassāyeva"),
      ("ALL", r"sabbattha"), ("MAGG", r"maggasamaṅgīnaṃ|maggasamaṅgino")]
VP = [("SOM", r"con đường nhập dòng"), ("SAM", r"con đường một lần trở lại"),
      ("ANM", r"con đường không trở lại"), ("AGG", r"con đường tối thượng"),
      ("ARM", r"con đường A-la-hán"),
      ("PU", r"phàm phu"), ("SO", r"(?<!đường )nhập dòng"), ("SA", r"(?<!đường )một lần trở lại"),
      ("AN", r"(?<!đường )không trở lại"), ("AR", r"(?<!đường )A-la-hán"),
      ("8", r"người thứ tám"), ("N2", r"\bhai (?:hạng người|người)"), ("N3", r"\bba (?:hạng người|người)"),
      ("N4", r"\bbốn (?:hạng người|người)"), ("N5", r"\bnăm (?:hạng người|người)"),
      ("REST", r"còn lại"), ("EXC", r"[Nn]goại trừ"), ("SAME", r"\bchính (?:những )?(?:hạng )?người"),
      ("ALL", r"ở mọi nơi"), ("MAGG", r"có được con đường(?! (?:nhập|một|không|tối|A-la))")]

# ---------- places ----------
PL = [("DU", r"dukkhāya vedanāya"), ("K2", r"kāmadhātuyā dvīsu vedanāsu"),
      ("K3", r"kāmadhātuyā tīsu vedanāsu"), ("KD", r"kāmadhātuyā(?! (?:dvīsu|tīsu))"),
      ("AR", r"arūpadhātuyā"), ("RU", r"(?<!a)rūpadhātuyā"), ("AP", r"apariyāpann"),
      ("SU", r"sukhāya vedanāya"), ("AD", r"adukkhamasukhāya")]
VL = [("DU", r"cảm giác khó chịu"), ("K2", r"hai loại cảm giác trong cõi dục lạc"),
      ("K3", r"ba loại cảm giác trong cõi dục lạc"),
      ("KD", r"(?<!cảm giác trong )cõi dục lạc"),
      ("AR", r"cõi không hình sắc"), ("RU", r"(?<!không )cõi hình sắc"),
      ("AP", r"không nằm trong các cõi tồn tại"),
      ("SU", r"cảm giác dễ chịu"), ("AD", r"không khó chịu cũng không dễ chịu")]

# ---------- verbs / polarity ----------
def pi_pol(sent):
    toks = re.findall(r"[\wāīūṃṅñṭḍṇḷ]+", sent.lower())
    out, flip, prev = [], False, ""
    for i, t in enumerate(toks):
        if t == "ca" and prev == "no":
            flip = True
        p = None
        if t.startswith("nānuse"):
            p = "N"
        elif t.startswith("anuse"):
            p = "P"
        elif t.startswith("sānusay"):
            p = "P"
        elif t.startswith("niranusay"):
            p = "N"
        elif t.startswith("nappajah"):
            p = "N"
        elif t.startswith("pajah"):
            p = "N" if prev == "na" else "P"
        elif t.startswith("napparijān"):
            p = "N"
        elif t.startswith("parijān"):
            p = "N" if prev == "na" else "P"
        if p:
            if flip:
                p = "P" if p == "N" else "N"
            out.append(p)
        prev = t
    return out

def vi_pol(sent, kind):
    if kind == "anusaya":
        rx = r"(không |vẫn |cũng |)nằm sẵn"
    elif kind == "sanusaya":
        rx = r"(không |vẫn |cũng |)có khuynh hướng tiềm ẩn"
    elif kind == "pajahana":
        rx = r"(không |vẫn |cũng |)dứt bỏ"
    else:
        rx = r"(không |vẫn |cũng |)hiểu biết trọn vẹn"
    out = []
    for m in re.finditer(rx, sent, flags=re.I):
        out.append("N" if m.group(1).lower() == "không " else "P")
    return out

def kind_of(heading):
    h = heading.lower()
    if "sānusay" in h:
        return "sanusaya"
    if "pajahan" in h:
        return "pajahana"
    if "pariññ" in h:
        return "pariñña"
    if "anusayavār" in h:
        return "anusaya"
    return None

def ans(sent_pi):
    s = sent_pi.strip()
    if re.search(r"\?\s*Āmantā\.?$", s) or s == "Āmantā.":
        return "YES"
    if re.search(r"\?\s*No\.?$", s) or s == "No.":
        return "NO"
    if re.search(r"Natthi\.?$", s):
        return "NONE"
    return None

def vans(sent_vi):
    s = sent_vi.strip()
    if s.endswith("Đúng vậy.") or s == "Đúng vậy.":
        return "YES"
    if re.search(r"\? Không\.$", s) or s == "Không.":
        return "NO"
    if s.endswith("Không có."):
        return "NONE"
    return None

def main():
    kind = None
    nseg = 0
    nlines = 0
    issues = []
    for fn in FILES:
        P = lines(PI + fn)
        V = lines(VI + fn)
        if len(P) != len(V):
            issues.append((fn, "-", "LINECOUNT", len(P), len(V)))
            continue
        for i, (p, v) in enumerate(zip(P, V)):
            nlines += 1
            ip = ID_RE.search(p)
            iv = ID_RE.search(v)
            if (ip and ip.group(1)) != (iv and iv.group(1)):
                issues.append((fn, i, "ID", ip and ip.group(1), iv and iv.group(1)))
            if ip:
                nseg += 1
            if p.startswith("#"):
                k = kind_of(p)
                if k:
                    kind = k
                continue
            if p.count("?") != v.count("?"):
                issues.append((fn, i, "QMARK", p.count("?"), v.count("?")))
            if v.count("…") != p.count("pe…"):
                issues.append((fn, i, "ELLIPSIS", p.count("…pe…"), v.count("…")))
            if "…." in v or "...." in v:
                issues.append((fn, i, "DOTS", "", "…."))
            if "–" in v and "–" not in p:
                issues.append((fn, i, "DASH", "", ""))
            sp, sv = split_sent(p), split_sent(v)
            if len(sp) != len(sv):
                issues.append((fn, i, "SENTCOUNT", len(sp), len(sv)))
                sp, sv = [ID_RE.sub("", p)], [ID_RE.sub("", v)]
            for a, b in zip(sp, sv):
                for name, f1, f2 in (("NAMES", lambda x: seq(x, PN), lambda x: seq(x, VN)),
                                     ("PERS", lambda x: seq(x, PP), lambda x: seq(x, VP)),
                                     ("PLACE", lambda x: seq(x, PL), lambda x: seq(x, VL)),
                                     ("POL", pi_pol, lambda x: vi_pol(x, kind)),
                                     ("ANS", lambda x: [ans(x)], lambda x: [vans(x)])):
                    x, y = f1(a), f2(b)
                    if name == "POL":
                        x = [k for j, k in enumerate(x) if j == 0 or x[j - 1] != k]
                        y = [k for j, k in enumerate(y) if j == 0 or y[j - 1] != k]
                    if x != y:
                        issues.append((fn, i, name, "".join(map(str, x)) if name != "PERS" and name != "PLACE" else " ".join(x),
                                       "".join(map(str, y)) if name != "PERS" and name != "PLACE" else " ".join(y)))
    want = set(sys.argv[1:])
    from collections import Counter
    c = Counter(t[2] for t in issues)
    print("lines", nlines, "segments", nseg, "issues", dict(c))
    for t in issues:
        if not want or t[2] in want:
            print(*t, sep=" | ")

if __name__ == "__main__":
    main()
