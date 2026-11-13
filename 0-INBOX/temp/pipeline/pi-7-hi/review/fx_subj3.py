"""SC variants: matches that need a comma inside the NP before «के लिए» (current output)."""
import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C
DEV = "ऀ-ॣ०-ॿ"
B = r"(?<![" + DEV + r"-])"
SUBJ = r"अनुरूपता|गोत्र-परिवर्तन|शुद्धि|मार्ग|मूल|इरादा|अंग|आहार|क्षमताएँ|क्षमता|प्रधानता"
NOT = r"(?!(?:के|की|का|को|से|में|पर|रूपी|और|या|भी|ही|न|नहीं|तथा|द्वारा|रूप)(?![" + DEV + r"])|वाल|बना)"
LB = r"(?<!को )(?<!सह-उत्पत्ति रूपी )(?<!विषय रूपी )"
A = re.compile(B + LB + r"(" + SUBJ + r") " + NOT + r"(?=[^।;–…()\[\]]*? के लिए)")
Bx = re.compile(B + LB + r"(" + SUBJ + r") " + NOT + r"(?=[^,।;–…()\[\]]*? के लिए)")
out = open(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review\fx_out.txt", "w", encoding="utf-8")
n = 0
for part in C.PARTS:
    if part in ("preamble", "1-00-paccaya"):
        continue
    for i, (p, h) in enumerate(C.pairs(part)):
        if not re.search(r"paccay(?:ena|o)\b", p):
            continue
        sa = {m.start() for m in A.finditer(h)}
        sb = {m.start() for m in Bx.finditer(h)}
        for s in sorted(sa - sb):
            n += 1
            out.write(f"{part[:4]}:{i+1}\t…{h[max(0, s - 30):s]}[{h[s:s + 90]}]\n")
print(n)
