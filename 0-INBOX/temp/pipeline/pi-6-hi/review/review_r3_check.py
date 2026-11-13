import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load
from review_r3_struct import FILES

PV = re.compile(r"\b(no ca|na|n?uppajj|nirujjh)(ati|anti|atī|antī|issati|issatī|issanti|issantī|ittha|itthā|iti)(?:ti)??\b")
TENSE = {"ati": "P", "anti": "P", "atī": "P", "antī": "P", "iti": "P",
         "issati": "F", "issatī": "F", "issanti": "F", "issantī": "F",
         "ittha": "X", "itthā": "X"}

def pali_verbs(s):
    s = re.sub(r"\[[^\]]*\]", "", s).lower()
    toks = re.findall(r"[a-zāīūṃṅñṭḍṇḷ]+", s)
    out = []; prevna = False; flip = False
    i = 0
    while i < len(toks):
        t = toks[i]
        if t == "no" and i + 1 < len(toks) and toks[i + 1] == "ca":
            flip = True; i += 2; continue
        m = re.fullmatch(r"(n?uppajj|nirujjh)(ati|anti|atī|antī|issati|issatī|issanti|issantī|ittha|itthā|iti)(?:ti)?", t)
        if m:
            neg = m.group(1).startswith("n") and m.group(1) != "nirujjh" or prevna
            if flip:
                neg = not neg; flip = False
            out.append(TENSE[m.group(2)] + ("-" if neg else "+"))
        prevna = (t == "na")
        i += 1
    return out

HV = re.compile(r"(उत्पन्न|समाप्त) (नहीं )?(होता|होती|होते|होतीं|हुआ|हुई|हुए|हुईं|होगा|होगी|होंगे|होंगी)")
HT = {"होता": "P", "होती": "P", "होते": "P", "होतीं": "P", "हुआ": "X", "हुई": "X", "हुए": "X", "हुईं": "X",
      "होगा": "F", "होगी": "F", "होंगे": "F", "होंगी": "F"}

def hindi_verbs(s):
    s = re.sub(r"\[[^\]]*\]", "", s)
    return [HT[m.group(3)] + ("-" if m.group(2) else "+") for m in HV.finditer(s)]

def root_seq_p(s):
    s = re.sub(r"\[[^\]]*\]", "", s).lower()
    return ["U" if "uppajj" in m.group(0) else "N" for m in re.finditer(r"\b(n?uppajj|nirujjh)(ati|anti|atī|antī|issati|issatī|issanti|issantī|ittha|itthā|iti)(?:ti)?\b", s)]

def root_seq_h(s):
    s = re.sub(r"\[[^\]]*\]", "", s)
    return ["U" if m.group(1) == "उत्पन्न" else "N" for m in HV.finditer(s)]

ITEMS_P = [("dukkhasacc", "D"), ("samudayasacc", "S"), ("nirodhasacc", "N"), ("maggasacc", "M"),
           ("kāyasaṅkhār", "K"), ("vacīsaṅkhār", "V"), ("cittasaṅkhār", "C")]
ITEMS_H = [("दुःख (?:का|के) सत्य", "D"), ("उत्पत्ति (?:का|के) सत्य", "S"), ("अंत (?:का|के) सत्य", "N"),
           ("मार्ग (?:का|के) सत्य", "M"), ("शरीर की रचना", "K"), ("वाणी की रचना", "V"), ("मन की रचना", "C")]

def items(s, table, lower):
    s = re.sub(r"\[[^\]]*\]", "", s)
    if lower: s = s.lower()
    rx = "|".join("(%s)" % a for a, b in table)
    res = []
    for m in re.finditer(rx, s):
        for k, (a, b) in enumerate(table):
            if m.group(k + 1):
                res.append(b)
    return res

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for fn in FILES:
        p, h = load(fn)
        for i, (a, b) in enumerate(zip(p, h), 1):
            if a.startswith("#"): continue
            probs = []
            pv, hv = pali_verbs(a), hindi_verbs(b)
            if pv != hv: probs.append(f"VERB P={''.join(pv)} H={''.join(hv)}")
            rp, rh = root_seq_p(a), root_seq_h(b)
            if rp != rh: probs.append(f"ROOT P={''.join(rp)} H={''.join(rh)}")
            ip, ih = items(a, ITEMS_P, True), items(b, ITEMS_H, False)
            if ip != ih: probs.append(f"ITEM P={''.join(ip)} H={''.join(ih)}")
            if probs and (only is None or any(x.startswith(only) for x in probs)):
                print(fn[:4], i, " | ".join(probs))

