import re, os, sys
base = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"

def lines(path):
    return [l.rstrip("\n") for l in open(path, encoding="utf-8") if l.strip()]

IDRE = re.compile(r"\s*\^[\w-]+\s*$")

# ---------- anusaya items
P_ITEM = re.compile(r"(?i)(kāmarāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)ānusay")
PMAP = {"kāmarāg": "K", "paṭigh": "P", "mān": "M", "diṭṭh": "D", "vicikicch": "V", "bhavarāg": "B", "avijj": "A"}
H_ITEM = re.compile(r"(इंद्रिय-सुखों के राग|चिढ़|अहंकार|दृष्टि|संशय|अस्तित्व के राग|अज्ञान) की सुप्त प्रवृत्ति")
HMAP = {"इंद्रिय-सुखों के राग": "K", "चिढ़": "P", "अहंकार": "M", "दृष्टि": "D", "संशय": "V", "अस्तित्व के राग": "B", "अज्ञान": "A"}

# ---------- places (non-dhatu sections)
P_PLACE = re.compile(r"(?i)(kāmadhātuyā (?:dvīsu|tīsu) vedanāsu|dukkhāya vedanāya|\barūpadhātuyā|\brūpadhātuyā|apariyāpanne|sabbattha)")
def pplace(m):
    s = m.lower()
    if s.startswith("kāmadhātuyā dvīsu"): return "K2"
    if s.startswith("kāmadhātuyā tīsu"): return "K3"
    if s.startswith("dukkhāya"): return "D"
    if s == "arūpadhātuyā": return "A"
    if s == "rūpadhātuyā": return "R"
    if s == "apariyāpanne": return "X"
    if s == "sabbattha": return "S"
H_PLACE = re.compile(r"(इंद्रिय-सुखों के लोक की (?:दो|तीन) अनुभूतियों|दुःखद अनुभूति|सूक्ष्म भौतिक लोक|अभौतिक लोक|न समाई हुई परिघटनाओं|सब जगह)")
def hplace(m):
    if "दो अनुभूतियों" in m: return "K2"
    if "तीन अनुभूतियों" in m: return "K3"
    if m.startswith("दुःखद"): return "D"
    if m.startswith("सूक्ष्म"): return "R"
    if m.startswith("अभौतिक"): return "A"
    if m.startswith("न समाई"): return "X"
    if m == "सब जगह": return "S"

# ---------- persons
P_PERS = [
    (r"Aggamaggasamaṅgī|Aggamaggasamaṅgiñca|Aggamaggasamaṅgiṃ", "AG"),
    (r"Anāgāmimaggasamaṅgī|Anāgāmimaggasamaṅgiñca|Anāgāmimaggasamaṅgiṃ", "AN"),
    (r"(?i:aṭṭhamak(?:o|añca|aṃ))", "8"),
    (r"(?i:dvinnaṃ maggasamaṅgīna(?:ṃ|ñca))", "2M"),
    (r"Sveva puggalo|Tasseva puggalassa|Tesaññeva puggalānaṃ", "SV"),
    (r"avasesā puggalā", "AV"),
    (r"Anāgāmissa", "ANG"),
    (r"Arahato", "AR"),
    (r"(?i:dvinnaṃ puggalānaṃ)", "2P"),
    (r"(?i:tiṇṇaṃ puggalānaṃ)", "3P"),
    (r"(?i:catunnaṃ puggalānaṃ)", "4P"),
    (r"Puthujjanassa", "PU"),
]
P_PERS_RE = re.compile("|".join("(%s)" % p for p, _ in P_PERS))
H_PERS = [
    (r"सर्वोच्च मार्ग से युक्त", "AG"),
    (r"फिर न लौटने के मार्ग से युक्त", "AN"),
    (r"आठवें स्तर के? व्यक्ति|आठवें स्तर का व्यक्ति", "8"),
    (r"मार्ग से युक्त दो व्यक्तियों", "2M"),
    (r"वही व्यक्ति|उसी व्यक्ति|उन्हीं व्यक्तियों", "SV"),
    (r"शेष व्यक्ति", "AV"),
    (r"फिर न लौटने वाले", "ANG"),
    (r"अर्हत्", "AR"),
    (r"(?<!युक्त )दो व्यक्तियों", "2P"),
    (r"तीन व्यक्तियों", "3P"),
    (r"चार व्यक्तियों", "4P"),
    (r"साधारण व्यक्ति", "PU"),
]
H_PERS_RE = re.compile("|".join("(%s)" % p for p, _ in H_PERS))
def seq(rx, table, s):
    out = []
    for m in rx.finditer(s):
        for i, g in enumerate(m.groups()):
            if g is not None:
                out.append(table[i][1]); break
    return out

# ---------- negation
def pali_neg(s):
    s2 = s
    n = 0
    n += len(re.findall(r"\bna (?:parijān|uppajj)", s2))
    n += len(re.findall(r"\bappahīn", s2))
    n += len(re.findall(r"\bnuppajj", s2))
    n += len(re.findall(r"\bNo\.", s2))
    n += len(re.findall(r"(?i)\bnatthi\b", s2))
    n += len(re.findall(r"\bna sameti", s2))
    # "na vattabba 'pahina'ti va 'appahina'ti va": Hindi has na..., na ... nahin = 3 ; pali counted appahin (1) -> add 2
    nv = len(re.findall(r"(?i)\bna vattabb", s2))
    n += 2 * nv
    # no ca flips
    for m in re.finditer(r"no ca ([^.;?]*)", s2):
        seg = m.group(1)
        # first verb only
        vm = re.search(r"(na parijān\w*|parijān\w*|appahīn\w*|pahīn\w*|nuppajj\w*|uppajj\w*)", seg)
        if not vm: continue
        v = vm.group(1)
        if v.startswith("na ") or v.startswith("appahīn") or v.startswith("nuppajj"):
            n -= 1
        else:
            n += 1
    return n

def hindi_neg(s):
    n = len(re.findall(r"नहीं", s))
    for m in re.finditer(r"(?<![\u0900-\u097F])न(?![\u0900-\u097F])", s):
        after = s[m.end():m.end() + 8]
        if after.startswith(" लौटने") or after.startswith(" समाई"):
            continue
        n += 1
    return n

# ---------- verb counts
def pali_verbs(s):
    s = re.sub(r"\"(?:pahīn|appahīn)\w*\"ti", "", s)
    s = re.sub(r"\[[^\]]*\]", "", s)
    return {
        "parij": len(re.findall(r"parijān", s)),
        "parij_pl": len(re.findall(r"parijānanti", s)),
        "pahina": len(re.findall(r"(?<![a-z])(?:ap)?pahīn", s)),
        "pahina_pl": len(re.findall(r"(?<![a-z])(?:ap)?pahīnā", s)),
        "upp": len(re.findall(r"uppajj", s)),
    }
def hindi_verbs(s):
    s = re.sub(r"“[^”]*”", "", s)
    s = re.sub(r"\[[^\]]*\]", "", s)
    return {
        "parij": len(re.findall(r"समझ(?:ता|ते|ा जाता)", s)),
        "parij_pl": len(re.findall(r"समझते", s)),
        "pahina": len(re.findall(r"छोड़ी (?:जा चुकी|नहीं गई)", s)),
        "pahina_pl": len(re.findall(r"छोड़ी (?:जा चुकी|नहीं गई) हैं", s)),
        "upp": len(re.findall(r"उत्पन्न", s)),
    }

def strip_id(s):
    return IDRE.sub("", s)

def endp(s):
    s = strip_id(s).rstrip()
    s = re.sub(r"\s*\([^()]*\)\.?$", "", s).rstrip()  # trailing (Ekamulakam) etc
    return s[-1:] if s else ""

report = []
total = 0
for n in range(7, 12):
    f = "7-%02d-anusayayamaka.md" % n
    P = lines(os.path.join(base, "pali", "pi-6_split_chapters", f))
    H = lines(os.path.join(base, "hindi", "pi-6-hindi-plain-rails_split_chapters", f))
    dhatu = False
    for i, (p, h) in enumerate(zip(P, H), 1):
        total += 1
        tag = "%s:%d" % (f[:4], i)
        if "dhātupucchāvāro" in p or "dhātuvisajjanāvāro" in p:
            dhatu = True
        pi = [PMAP[m.group(1).lower()] for m in P_ITEM.finditer(p)]
        hi = [HMAP[m.group(1)] for m in H_ITEM.finditer(h)]
        if pi != hi:
            report.append((tag, "ITEMS", "".join(pi), "".join(hi)))
        if not dhatu:
            pp = [pplace(m.group(1)) for m in P_PLACE.finditer(p)]
            hp = [hplace(m.group(1)) for m in H_PLACE.finditer(h)]
            if pp != hp:
                report.append((tag, "PLACES", pp, hp))
        ps = seq(P_PERS_RE, P_PERS, p)
        hs = seq(H_PERS_RE, H_PERS, h)
        if ps != hs:
            report.append((tag, "PERSONS", ps, hs))
        if not dhatu:
            pn, hn = pali_neg(p), hindi_neg(h)
            if pn != hn:
                report.append((tag, "NEG", pn, hn))
        pv, hv = pali_verbs(p), hindi_verbs(h)
        if pv != hv and not dhatu:
            report.append((tag, "VERBS", pv, hv))
        # labels
        for lab, hl in (("(Ka)", "(क)"), ("(Kha)", "(ख)"), ("(Ga)", "(ग)"), ("(Gha)", "(घ)"), ("(Ṅa)", "(ङ)"), ("(Ca)", "(च)")):
            if p.count(lab) != h.count(hl):
                report.append((tag, "LABEL", lab, h[:30]))
        # ellipsis
        if p.count("pe…") != h.count("…"):
            report.append((tag, "ELLIPSIS", p.count("pe…"), h.count("…")))
        # end punctuation
        ep, eh = endp(p), endp(h)
        exp = {"?": "?", ".": "।"}.get(ep, ep)
        if not p.startswith("#") and exp != eh:
            report.append((tag, "ENDP", ep, eh))
        # typography
        if ("–" in h or "—" in h) and not ("–" in p or "—" in p):
            report.append((tag, "DASH", "", ""))
        if '"' in h or "'" in h:
            report.append((tag, "STRAIGHTQUOTE", "", ""))
        if re.search(r" [।?,;]|  |\?।|।।", strip_id(h)):
            report.append((tag, "SPACING", "", re.search(r" [।?,;]|  |\?।|।।", strip_id(h)).group()))
        lat = re.sub(r"\[[^\]]*\]", "", strip_id(h))
        if re.search(r"[A-Za-zāīūṃñṭḍṇḷ]{2,}", lat):
            report.append((tag, "LATIN", "", re.findall(r"[A-Za-zāīūṃñṭḍṇḷ]{2,}", lat)))
        # sentence counts
        ps_ = len(re.findall(r"[.?](?:\s|$)", strip_id(p)))
        hs_ = len(re.findall(r"[।?](?:\s|$)", strip_id(h)))
        if ps_ != hs_:
            report.append((tag, "SENTCOUNT", ps_, hs_))
        # numbers (dhatu)
        pnum = re.findall(r"\b(satteva|satta|pañca|tayo)\b", p)
        hnum = re.findall(r"(सातों ही|सात|पाँच|तीन)(?= सुप्त)", h)
        mp = {"satteva": "सातों ही", "satta": "सात", "pañca": "पाँच", "tayo": "तीन"}
        if [mp[x] for x in pnum] != hnum:
            report.append((tag, "NUMS", pnum, hnum))

for r in report:
    print(*r, sep=" | ")
print("segments", total, "flags", len(report))
