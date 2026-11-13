import re, sys, collections

PB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
HB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-rails_split_chapters"
FILES = [f"7-0{i}-anusayayamaka.md" for i in range(1, 7)]

P_TEND = [("K", r"k[aā]m[aā]r[aā]g[aā]nusay"), ("P", r"paṭigh[aā]nusay"), ("M", r"(?<![a-zāīū])m[aā]n[aā]nusay"),
          ("D", r"diṭṭh[aā]nusay"), ("V", r"vicikicch[aā]nusay"), ("B", r"bhavar[aā]g[aā]nusay"), ("A", r"avijj[aā]nusay")]
H_TEND = [("K", r"इंद्रिय-सुखों के राग"), ("P", r"चिढ़"), ("M", r"अहंकार"), ("D", r"दृष्टि"), ("V", r"संशय"),
          ("B", r"अस्तित्व के राग"), ("A", r"अज्ञान")]

P_PLACE = [("K2", r"kāmadhātuyā dvīsu vedanāsu"), ("K3", r"kāmadhātuyā tīsu vedanāsu"), ("Du", r"dukkhāya vedanāya"),
           ("R", r"(?<![a-zā])rūpadhātuyā"), ("AR", r"arūpadhātuyā"), ("Ap", r"(?<![a-z])a?(?:p)?ariyāpanne"),
           ("S", r"sabbasakkāyapariyāpannesu"), ("All", r"sabbattha")]
H_PLACE = [("K2", r"इंद्रिय-सुखों के लोक की दो अनुभूति"), ("K3", r"इंद्रिय-सुखों के लोक की तीन अनुभूति"),
           ("Du", r"दुःखद अनुभूति"), ("R", r"सूक्ष्म भौतिक लोक"), ("AR", r"अभौतिक लोक"),
           ("Ap", r"न समाई हुई"), ("S", r"व्यक्तित्व में समाई"), ("All", r"सब जगह")]

P_PERS = [("AnM", r"anāgāmimaggasamaṅg\w*"), ("AgM", r"aggamaggasamaṅg\w*"), ("2M", r"dvinnaṃ maggasamaṅgīnaṃ"),
          ("8", r"aṭṭhamak\w*"), ("An", r"anāgām\w*"), ("Ar", r"arah\w*"), ("Pu", r"puthujjan\w*"),
          ("2P", r"(?:dvinnaṃ|dve) puggal\w*"), ("3P", r"(?:tiṇṇaṃ|tayo) puggal\w*"), ("4P", r"(?:catunnaṃ|cattāro) puggal\w*"),
          ("Rest", r"avasesā"), ("Same", r"\b(?:tesaññeva|tasseva|teva|sveva)\b")]
H_PERS = [("AnM", r"फिर न लौटने के मार्ग से युक्त"), ("AgM", r"सर्वोच्च मार्ग से युक्त"), ("2M", r"मार्ग से युक्त दो"),
          ("8", r"आठवें स्तर"), ("An", r"फिर न लौटने वाल"), ("Ar", r"अर्हत्"), ("Pu", r"साधारण व्यक्ति"),
          ("2P", r"दो व्यक्ति"), ("3P", r"तीन व्यक्ति"), ("4P", r"चार व्यक्ति"),
          ("Rest", r"शेष"), ("Same", r"(?:उन्हीं|उसी|वही|वे ही)")]

ROOT = {"ekamūlakaṃ": "एक मूल पर", "dukamūlakaṃ": "दो मूलों पर", "tikamūlakaṃ": "तीन मूलों पर",
        "catukkamūlakaṃ": "चार मूलों पर", "pañcakamūlakaṃ": "पाँच मूलों पर", "chakkamūlakaṃ": "छह मूलों पर"}


def seq(text, pats, consume=True):
    found = []
    t = text
    for code, p in pats:
        for m in re.finditer(p, t, flags=re.I):
            found.append((m.start(), code))
        if consume:
            t = re.sub(p, lambda m: "#" * len(m.group(0)), t, flags=re.I)
    return [c for _, c in sorted(found)]


def p_neg(s):
    s2 = s
    negv = len(re.findall(r"\b(?:nānuset\w*|nānusent\w*|nappajah\w*)", s2))
    noca = re.findall(r"\bno ca\b[^.,;?]*", s2)
    noca_neg = sum(1 for c in noca if re.search(r"\b(?:nānuset|nānusent|nappajah)", c))
    ans_no = len(re.findall(r"\?\s*No\b", s2)) + len(re.findall(r"^No\.", s2))
    natthi = len(re.findall(r"\bNatthi\b", s2))
    return negv + len(noca) - 2 * noca_neg + ans_no + natthi


def h_neg(s):
    s2 = s.replace("फिर न लौटने", "").replace("न समाई", "")
    return len(re.findall(r"नहीं", s2)) + len(re.findall(r"(?<![\u0900-\u097F])न(?![\u0900-\u097F])", s2))


def split_p(s):
    return [x for x in re.split(r"(?<=[.?])\s+", s) if x.strip()]


def split_h(s):
    return [x for x in re.split(r"(?<=[।?])\s+", s) if x.strip()]


def nonempty(path):
    out = []
    for i, l in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        if l.strip():
            out.append((i, l))
    return out


issues = []
nseg = 0
nlines = 0
for f in FILES:
    P = nonempty(f"{PB}\\{f}")
    H = nonempty(f"{HB}\\{f}")
    raw_h = open(f"{HB}\\{f}", encoding="utf-8").read()
    if "\n\n\n" in raw_h:
        issues.append((f, 0, "-", "TYPO", "double blank line"))
    if len(P) != len(H):
        issues.append((f, 0, "-", "ALIGN", f"nonempty lines P={len(P)} H={len(H)}"))
    curid = None
    # find id for each line: the id at end of the segment (look ahead)
    ids = [None] * len(P)
    nxt = None
    for k in range(len(P) - 1, -1, -1):
        m = re.search(r"\^([\d-]+)\s*$", P[k][1])
        if m:
            nxt = m.group(1)
        ids[k] = nxt
    for k, ((pl, p), (hl, h)) in enumerate(zip(P, H)):
        nlines += 1
        sid = ids[k]
        n = k + 1
        mp = re.search(r"\^([\d-]+)\s*$", p)
        mh = re.search(r"\^([\d-]+)\s*$", h)
        if mp:
            nseg += 1
        if (mp and not mh) or (mh and not mp) or (mp and mh and mp.group(1) != mh.group(1)):
            issues.append((f, n, sid, "ID", f"P={mp and mp.group(1)} H={mh and mh.group(1)}"))
        if p.startswith("#"):
            if not h.startswith("#") or p.split()[0] != h.split()[0]:
                issues.append((f, n, sid, "HEAD", "heading level"))
        # tendencies
        tp = seq(p, P_TEND, consume=False)
        th = seq(h, H_TEND)
        if tp != th:
            kind = "TEND-ORDER" if sorted(tp) == sorted(th) else "TEND"
            issues.append((f, n, sid, kind, f"P={''.join(tp)} H={''.join(th)}"))
        pp = seq(p, P_PLACE, consume=False)
        hp = seq(h, H_PLACE)
        if collections.Counter(pp) != collections.Counter(hp):
            issues.append((f, n, sid, "PLACE", f"P={pp} H={hp}"))
        elif pp != hp:
            issues.append((f, n, sid, "PLACE-ORDER", f"P={pp} H={hp}"))
        ps = seq(p, P_PERS)
        hs = seq(h, H_PERS)
        if collections.Counter(ps) != collections.Counter(hs):
            issues.append((f, n, sid, "PERS", f"P={ps} H={hs}"))
        # polarity per sentence when aligned
        sp, sh = split_p(re.sub(r"\s*\^[\d-]+\s*$", "", p)), split_h(re.sub(r"\s*\^[\d-]+\s*$", "", h))
        if len(sp) == len(sh):
            for j, (a, b) in enumerate(zip(sp, sh)):
                if p_neg(a) != h_neg(b):
                    issues.append((f, n, sid, "POL", f"sent{j+1}: P={p_neg(a)} H={h_neg(b)} | {a[:90]} || {b[:90]}"))
                if seq(a, P_TEND, False) != seq(b, H_TEND):
                    issues.append((f, n, sid, "TEND-SENT", f"sent{j+1}"))
                if collections.Counter(seq(a, P_PLACE, False)) != collections.Counter(seq(b, H_PLACE)):
                    issues.append((f, n, sid, "PLACE-SENT", f"sent{j+1}: {seq(a, P_PLACE, False)} {seq(b, H_PLACE)}"))
                if collections.Counter(seq(a, P_PERS)) != collections.Counter(seq(b, H_PERS)):
                    issues.append((f, n, sid, "PERS-SENT", f"sent{j+1}: {seq(a, P_PERS)} {seq(b, H_PERS)}"))
                # question vs statement
                if a.rstrip().endswith("?") != b.rstrip().endswith("?"):
                    issues.append((f, n, sid, "PUNCT-Q", f"sent{j+1}"))
        else:
            issues.append((f, n, sid, "SENTCOUNT", f"P={len(sp)} H={len(sh)}"))
            if p_neg(p) != h_neg(h):
                issues.append((f, n, sid, "POL", f"line: P={p_neg(p)} H={h_neg(h)}"))
        # answers
        nh = len(re.findall(r"(?<![\u0900-\u097F])हाँ", h))
        if p.count("Āmantā") != nh:
            issues.append((f, n, sid, "AMANTA", f"P={p.count('Āmantā')} H={nh}"))
        if len(re.findall(r"\bNatthi\b", p)) != h.count("ऐसा कोई नहीं है"):
            issues.append((f, n, sid, "NATTHI", ""))
        # pe
        npe = len(re.findall(r"pe…", p))
        nel = h.count("…")
        if npe != nel:
            issues.append((f, n, sid, "PE", f"pe={npe} …={nel}"))
        # root notes
        for kroot, v in ROOT.items():
            if kroot in p.lower() and v not in h:
                issues.append((f, n, sid, "ROOTNOTE", kroot))
        # tadekattha
        if p.count("adekaṭṭh") != h.count("साथ रहने वाल"):
            issues.append((f, n, sid, "TADEK", ""))
        # typography
        if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", re.sub(r"\^[\d-]+", "", h)):
            issues.append((f, n, sid, "LATIN", re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]+", re.sub(r"\^[\d-]+", "", h))[:5]))
        if p.count("–") + p.count("—") != h.count("–") or "—" in h:
            issues.append((f, n, sid, "DASH", ""))
        if not h.startswith("#"):
            body = re.sub(r"\s*\^[\d-]+\s*$", "", h).rstrip()
            body = re.sub(r"\s*\([^)]*\)$", "", body).rstrip()
            if not (body.endswith("।") or body.endswith("?")):
                issues.append((f, n, sid, "END", body[-20:]))
            if re.search(r"\.(?!\.)", body.replace("…", "")):
                issues.append((f, n, sid, "DOT", ""))
        if '"' in h or "'" in h:
            issues.append((f, n, sid, "QUOTE", ""))
        if "  " in h or h != h.strip():
            issues.append((f, n, sid, "SPACE", ""))

c = collections.Counter(i[3] for i in issues)
print("lines", nlines, "segments", nseg)
print(c)
for i in issues:
    print(*i, sep=" | ")
