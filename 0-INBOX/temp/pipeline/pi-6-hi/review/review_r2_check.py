import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r2_align import pairs, FILES, IDRE

W = r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+"
# Pali verbs: (neg-prefix)(root)(tense)
PV = re.compile(r"^(n?)(uppajj|nirujjh|parijān)([a-zāīū]*)$", re.I)

def pali_tense(suf):
    if "itth" in suf: return "past"
    if "iss" in suf: return "fut"
    return "pres"

def pali_verbs(text):
    toks = re.findall(W, text)
    out = []
    negs = 0
    for t in toks:
        tl = t.lower()
        if tl in ("na", "no"):
            negs += 1
            continue
        if tl == "noti":
            negs += 1
            continue
        m = PV.match(tl)
        if m and not tl.startswith("uppajjamān"):
            neg = negs + (1 if m.group(1) else 0)
            root = {"uppajj": "U", "nirujjh": "N", "parijān": "P"}[m.group(2).lower()]
            out.append((root, pali_tense(m.group(3).lower()), neg % 2))
            negs = 0
    return out

HV = re.compile(r"(उत्पन्न|समाप्त|निरुद्ध|पूरी तरह समझ|पूरी तरह जान|परिज्ञा|समझ|जान)\s+(नहीं\s+)?(रहा|रही|रहे|लिया|ली|लिए|लेता|लेती|लेते|लेगा|लेगी|लेंगे|पाता|पाती|पाते|होता|होती|होते|हुआ|हुई|हुए|होगा|होगी|होंगे|होंगी|चुका|चुकी|चुके)(\s+(?:है|हैं|था|थी|थे|थीं|हो))?")

def hindi_verbs(text):
    out = []
    for m in HV.finditer(text):
        root = {"उत्पन्न": "U", "समाप्त": "N", "निरुद्ध": "N"}.get(m.group(1), "P")
        aux = m.group(3); tail = (m.group(4) or "").strip()
        if aux in ("हुआ", "हुई", "हुए", "लिया", "ली", "लिए", "चुका", "चुकी", "चुके") or tail in ("था", "थी", "थे", "थीं"):
            t = "past"
            if aux in ("होता", "होती", "होते", "लेता", "लेती", "लेते", "पाता", "पाती", "पाते"):
                t = "IMPERF?"
        elif aux.endswith("गा") or aux.endswith("गी") or aux.endswith("गे"):
            t = "fut"
        else:
            t = "pres"
        out.append((root, t, 1 if m.group(2) else 0))
    return out

ITEMS_P = re.compile(r"(cakkh|sot|ghān|jivh|kāy|rūp|sadd|gandh|ras|phoṭṭhabb|man|dhamm)āyatan", re.I)
PMAP = {"cakkh": "आँख", "sot": "कान", "ghān": "नाक", "jivh": "जीभ", "kāy": "शरीर", "rūp": "दृश्य रूप", "sadd": "ध्वनि",
        "gandh": "गंध", "ras": "स्वाद", "phoṭṭhabb": "स्पर्श", "man": "मन", "dhamm": "मन के विषयों"}
ITEMS_H = re.compile(r"(आँख|कान|नाक|जीभ|शरीर|दृश्य रूप|ध्वनि|गंध|स्वाद|स्पर्श|मन के विषयों|मन) (?:का|के|की|को) इंद्रिय-क्षेत्र")

BEINGS = [
    # (name, pali regex, hindi regex)
    ("upapajjantānaṃ", r"\bupapajjantānaṃ", r"जन्म लेने वालों"),
    ("cavantānaṃ", r"\bcavantānaṃ", r"मरने वालों"),
    ("parinibbantānaṃ", r"\bparinibb[aā]ntānaṃ", r"पूर्ण निर्वाण पाने वालों"),
    ("parinibbāyissanti", r"\bparinibbāyissanti", r"पूर्ण निर्वाण पाएँगे"),
    ("upapajjitvā", r"\bupapajjitvā", r"जन्म लेकर"),
    ("pacchimabhavikānaṃ", r"\bpacchimabhavikānaṃ", r"अंतिम जन्म"),
    ("itaresaṃ", r"\bitaresaṃ", r"बाकी"),
    ("sabbesaṃ", r"\bsabbesaṃ", r"सभी"),
    ("rūpāvacara", r"(?<![a-zā])rūpāvacar", r"सूक्ष्म भौतिक लोक"),
    ("arūpa(loka)", r"(?<![a-zā])(arūpāvacar|arūp(?:e|ānaṃ|aṃ|ā)\b)", r"अभौतिक लोक"),
    ("kāmāvacara", r"(?<![a-zā])kāmāvacar", r"इंद्रिय-सुखों के लोक"),
    ("asaññasatta", r"(?<![a-zā])asaññasatt", r"पहचान-रहित"),
    ("pañcavokāra", r"(?<![a-zā])pañcavokār", r"पाँच समूहों"),
    ("catuvokāra", r"(?<![a-zā])catuvokār", r"चार (?:या पाँच )?समूहों"),
    ("suddhāvāsa", r"(?<![a-zā])suddhāvās", r"शुद्ध निवास"),
    ("sacakkhuka", r"(?<![a-zā])sacakkhuk", r"आँख वाले"),
    ("acakkhuka", r"(?<![a-zā])acakkhuk", r"आँख से रहित"),
    ("sasotaka", r"(?<![a-zā])sasotak", r"कान वाले"),
    ("asotaka", r"(?<![a-zā])asotak", r"कान से रहित"),
    ("saghānaka", r"(?<![a-zā])saghānak", r"नाक वाले"),
    ("aghānaka", r"(?<![a-zā])aghānak", r"नाक से रहित"),
    ("sarūpaka", r"(?<![a-zā])sarūpak", r"भौतिक रूप वाले"),
    ("arūpaka", r"(?<![a-zā])arūpak", r"भौतिक रूप से रहित"),
    ("sacittaka", r"(?<![a-zā])sacittak", r"मन वाले"),
    ("acittaka", r"(?<![a-zā])acittak", r"मन से रहित"),
    ("āmantā", r"\bāmantā", r"(?<![\u0900-\u097F])हाँ"),
    ("natthi", r"\bnatthi\b", r"ऐसा कोई नहीं है"),
    ("arahā", r"\barah(?:ā|antañca)", r"अरहंत"),
    ("aggamagga", r"\baggamaggasamaṅg", r"सर्वोच्च मार्ग"),
    ("puthujjanā", r"\bputhujjan", r"सामान्य"),
]

def strip_variants(s):
    return re.sub(r"\[[^\]]*\]", "", s)

def main(only=None):
    total = 0
    issues = 0
    for f in FILES:
        if only and only not in f:
            continue
        P, H = pairs(f)
        for k, ((pn, p), (hn, h)) in enumerate(zip(P, H)):
            if p.startswith("#"):
                continue
            total += 1
            pid = IDRE.search(p)
            ps = strip_variants(IDRE.sub("", p)); hs = strip_variants(IDRE.sub("", h))
            probs = []
            pv = pali_verbs(ps); hv = hindi_verbs(hs)
            if pv != hv:
                probs.append(f"VERBS P={pv} H={hv}")
            pi = [PMAP[m.group(1).lower()] for m in ITEMS_P.finditer(ps)]
            hi = [m.group(1) for m in ITEMS_H.finditer(hs)]
            if pv and pi != hi:
                if sorted(pi) == sorted(hi):
                    probs.append(f"ITEM-ORDER P={pi} H={hi}")
                else:
                    probs.append(f"ITEMS P={pi} H={hi}")
            for name, pr, hr in BEINGS:
                a = len(re.findall(pr, ps, re.I)); b = len(re.findall(hr, hs))
                if a != b:
                    probs.append(f"{name} {a}/{b}")
            # yassa/yattha/tassa/tattha
            if re.search(r"\byassa\b", ps, re.I) and "जिस व्यक्ति" not in hs:
                probs.append("yassa?")
            if re.search(r"\byattha\b", ps, re.I) and "जिस स्थान" not in hs:
                probs.append("yattha?")
            if len(re.findall(r"\byattha\b", ps, re.I)) != len(re.findall(r"जिस स्थान", hs)):
                probs.append("yattha count")
            if len(re.findall(r"\byassa\b", ps, re.I)) != len(re.findall(r"जिस व्यक्ति", hs)):
                probs.append("yassa count")
            ps_t = re.sub(W + r"e tattha", "", ps)
            if len(re.findall(r"\btattha\b", ps_t, re.I)) != len(re.findall(r"वहाँ", hs)):
                probs.append("tattha")
            if len(re.findall(r"\bvā pana\b", ps)) != len(re.findall(r"(?:^|\) |[।?] )और जिस", hs)):
                probs.append("vā pana -> और?")
            # labels
            pl = re.findall(r"\((Ka|Kha|Ga|Gha|Ṅa|Ca)\)", ps); hl = re.findall(r"\((क|ख|ग|घ|ङ|च)\)", hs)
            LM = {"Ka": "क", "Kha": "ख", "Ga": "ग", "Gha": "घ", "Ṅa": "ङ", "Ca": "च"}
            if [LM[x] for x in pl] != hl:
                probs.append(f"LABELS {pl} {hl}")
            # ye -> जो
            if pv and len(re.findall(r"\b(ye|yo)\b", ps, re.I)) != len(re.findall(r"(?<![ऀ-ॿ])जो(?![ऀ-ॿ])", hs)):
                probs.append("ye/jo count")
            # sentence-level: split Pali on '. ' and Hindi on '। '
            psents = [s for s in re.split(r"(?<=[.?])\s+", ps) if s.strip()]
            hsents = [s for s in re.split(r"(?<=[।?])\s+", hs) if s.strip()]
            if len(psents) == len(hsents) and len(psents) > 1:
                for i, (a, b) in enumerate(zip(psents, hsents)):
                    if pali_verbs(a) != hindi_verbs(b):
                        probs.append(f"SENT{i+1} verbs")
                    for name, pr, hr in BEINGS:
                        if len(re.findall(pr, a, re.I)) != len(re.findall(hr, b)):
                            probs.append(f"SENT{i+1} {name}")
                    ai = [PMAP[m.group(1).lower()] for m in ITEMS_P.finditer(a)]
                    bi = [m.group(1) for m in ITEMS_H.finditer(b)]
                    if pv and ai != bi:
                        probs.append(f"SENT{i+1} items")
            elif pv and len(psents) != len(hsents):
                probs.append(f"sentcount {len(psents)}/{len(hsents)}")
            if probs:
                issues += 1
                rid = pid.group(1) if pid else ""
                print(f"{f[:4]} #{k+1} L{hn} {rid}: " + " | ".join(probs))
    print("checked", total, "lines with", issues, "flagged")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
