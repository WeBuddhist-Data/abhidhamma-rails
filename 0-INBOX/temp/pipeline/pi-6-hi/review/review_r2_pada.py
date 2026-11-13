import sys, re
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r2_align import pairs, IDRE
W = r"[A-Za-zāīūṃṅñṭḍṇḷĀĪŪṂṄÑṬḌṆḶ]+"
BARE = {"cakkhu": "आँख", "cakkhuṃ": "आँख", "sotaṃ": "कान", "ghānaṃ": "नाक", "jivhā": "जीभ", "jivhaṃ": "जीभ", "kāyo": "शरीर", "kāyaṃ": "शरीर",
        "rūpaṃ": "रूप", "saddo": "ध्वनि", "saddaṃ": "ध्वनि", "gandho": "गंध", "gandhaṃ": "गंध", "raso": "स्वाद", "rasaṃ": "स्वाद",
        "phoṭṭhabbo": "स्पर्श", "phoṭṭhabbaṃ": "स्पर्श", "mano": "मन", "manaṃ": "मन", "dhammo": "परिघटना"}
AY = {"cakkh": "आँख", "sot": "कान", "ghān": "नाक", "jivh": "जीभ", "kāy": "शरीर", "rūp": "दृश्य रूप", "sadd": "ध्वनि", "gandh": "गंध",
      "ras": "स्वाद", "phoṭṭhabb": "स्पर्श", "man": "मन", "dhamm": "मन के विषयों"}
P, H = pairs("3-01-ayatanayamaka.md")
for k, ((a, p), (b, h)) in enumerate(zip(P, H)):
    if k + 1 > 362 or p.startswith("#"):
        continue
    ps = re.sub(r"\[[^\]]*\]", "", IDRE.sub("", p)); hs = re.sub(r"\[[^\]]*\]", "", IDRE.sub("", h))
    toks = [t.lower() for t in re.findall(W, ps)]
    pn = sum(1 for t in toks if t == "na" or t.startswith("nāyatan"))
    hn = len(re.findall(r"नहीं", hs)) + len(re.findall(r"(?<![\u0900-\u097F])न(?![\u0900-\u097F])", hs))
    if pn != hn:
        print(f"#{k+1} L{b} NEG {pn}/{hn}")
    pit = []
    for t in toks:
        t2 = re.sub(r"(ti|nti|ñca|ñceva|ceva|ca)$", "", t)
        m = re.match(r"(cakkh|sot|ghān|jivh|kāy|rūp|sadd|gandh|ras|phoṭṭhabb|man|dhamm)āyatan", t)
        if m:
            pit.append(AY[m.group(1)] + "*")
        elif t in BARE or t2 in BARE or t.rstrip("ti") in BARE:
            pit.append(BARE.get(t) or BARE.get(t2) or BARE.get(t.rstrip("ti")))
    hit = []
    for m in re.finditer(r"(आँख|कान|नाक|जीभ|शरीर|दृश्य रूप|रूप|ध्वनि|गंध|स्वाद|स्पर्श|मन के विषयों|मन|परिघटना)( (?:का|के|को) इंद्रिय-क्षेत्र)?", hs):
        hit.append(m.group(1) + ("*" if m.group(2) else ""))
    if pit != hit:
        print(f"#{k+1} L{b} ITEMS P={pit}\n          H={hit}")
