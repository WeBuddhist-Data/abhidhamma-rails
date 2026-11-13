"""7-05 (pajahati, anuloma) vs 7-07 (parijānāti, anuloma): same Pāli modulo the verb -> same Hindi modulo the verb."""
import re
P = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-6_split_chapters"
H = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def ne(p):
    return [ID.sub("", l) for l in open(p, encoding="utf-8").read().splitlines() if l.strip() and not l.startswith("#")]


p5, h5 = ne(P + r"\7-05-anusayayamaka.md"), ne(H + r"\7-05-anusayayamaka.md")
p7, h7 = ne(P + r"\7-07-anusayayamaka.md"), ne(H + r"\7-07-anusayayamaka.md")
pv = lambda s: s.replace("nappajahat", "na parijānāt").replace("pajahat", "parijānāt").replace("Pajahana", "Pariññā")
hv = lambda s: (s.replace("नहीं छोड़ता", "पूरी तरह नहीं समझता").replace("नहीं छोड़ते", "पूरी तरह नहीं समझते")
                .replace("छोड़ता है", "पूरी तरह समझता है").replace("छोड़ते हैं", "पूरी तरह समझते हैं")
                .replace("छोड़ने के खंड", "पूरी तरह समझने के खंड").replace("छोड़ने का खंड", "पूरी तरह समझने का खंड"))
idx7 = {}
for a, b in zip(p7, h7):
    idx7.setdefault(a, b)
same = diff = 0
for a, b in zip(p5, h5):
    k = pv(a)
    if k in idx7:
        if hv(b) == idx7[k]:
            same += 1
        else:
            diff += 1
            if diff <= 5:
                print("P:", k[:150]); print(" 5:", hv(b)[:300]); print(" 7:", idx7[k][:300])
print("same", same, "diff", diff)
