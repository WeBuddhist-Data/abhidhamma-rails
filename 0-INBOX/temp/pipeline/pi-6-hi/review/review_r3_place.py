import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load
from review_r3_struct import FILES

CHK = [
    (r"\btattha\b", r"वहाँ"),
    (r"\byattha\b", r"जिस स्थान पर"),
    (r"\byassa\b(?! cittassa anantarā)", r"जिस व्यक्ति में"),
    (r"\bye\b", r"(?<![\u0900-\u097F])जो(?![\u0900-\u097F])"),
    (r"\bvā pana\b", r"^\((?:ख)\) और |^और "),
    (r"āmantā", r"(?<!व)हाँ"),
    (r"\bno\.", r"नहीं।"),
    (r"natthi", r"ऐसा कोई नहीं है"),
    (r"pacchimacitt", r"अंतिम मन"),
    (r"\bcittassa\b", r"मन"),
]

for fn in FILES:
    p, h = load(fn)
    for i, (a, b) in enumerate(zip(p, h), 1):
        if a.startswith("#"): continue
        A = re.sub(r"\[[^\]]*\]", "", re.sub(r"^\((Ka|Kha)\)\s*", "", a)).lower()
        B = re.sub(r"\[[^\]]*\]", "", b)
        out = []
        for pr, hr in CHK:
            x = len(re.findall(pr, A)); y = len(re.findall(hr, B))
            if pr == r"\bcittassa\b":
                y = len(re.findall(r"मन (?:के|का)", B)) - len(re.findall(r"अंतिम मन (?:के|का)", B)) + len(re.findall(r"अंतिम मन के", B))
                x = len(re.findall(r"cittassa", A))
                continue
            if x != y: out.append(f"{pr}:{x}/{y}")
        if out: print(fn[:4], i, " ".join(out))

