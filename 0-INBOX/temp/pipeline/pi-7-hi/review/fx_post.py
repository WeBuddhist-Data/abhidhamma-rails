"""Post checks: «आर्य, मार्ग» lines whose Pāli has no «ariyā magg-»; punctuation slips (",,", ", ,", " ,", "।,");
Pāli «ariyamagg»."""
import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import ar7_common as C
n1 = n2 = n3 = 0
for part in C.PARTS:
    for i, (p, h) in enumerate(C.pairs(part)):
        if "आर्य, मार्ग" in h and not re.search(r"[Aa]riyā (?:…pe… ?)?magg", p):
            n1 += 1
            print("ARIYA?", part[:4], i + 1, re.findall(r"[Aa]riy\w*(?: \S+){0,2}", p)[:3])
        for m in re.finditer(r",,|, ,| ,|।,|,।|, –", h):
            n2 += 1
            print("PUNCT", part[:4], i + 1, h[max(0, m.start() - 30):m.end() + 30])
        if re.search(r"ariyamagg", p):
            n3 += 1
print("ariya-no-magg", n1, "punct", n2, "ariyamagga lines", n3)
