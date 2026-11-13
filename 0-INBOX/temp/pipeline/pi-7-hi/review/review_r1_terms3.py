import re, sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *

T = [
    ("ahetuka", r"ahetuk", r"मूल-रहित|बिना मूल"),
    ("vicikicchasahagata", r"vicikicchāsahagat", r"संशय के साथ"),
    ("uddhaccasahagata", r"uddhaccasahagat", r"बेचैनी के साथ"),
    ("moha", r"(?<![a-z])moh", r"मोह"),
    ("panca-vinnana", r"pañcaviññāṇ", r"पाँच प्रकार की चेतना"),
    ("arupa", r"āruppe", r"अरूप"),
    ("manovinnana", r"manoviññāṇ", r"मन की चेतना"),
    ("manodhatu", r"manodhāt", r"मन के तत्व|मन का तत्व"),
    ("cakkhuvinnana", r"cakkhuviññāṇ", r"आँख की चेतना"),
    ("kayavinnana", r"kāyaviññāṇ", r"शरीर की चेतना"),
    ("vatthu", r"vatth[uū]", r"आधार"),
    ("patisandhi", r"paṭisandhi", r"पुनर्जन्म"),
    ("pavatte", r"pavatt", r"जीवन-प्रवाह|जीवन के दौरान|प्रवाह"),
    ("saṃsattha", r"saṃsaṭṭh", r"घुल-मिल|घुले-मिले"),
    ("sampayutta-adj", r"sampayutt(?!apaccay|e |adukaṃ|amūlak|avār|attaṃ|asabh|aghaṭ)", r"जुड़"),
    ("vippayutta-adj", r"vippayutt(?!apaccay)", r"अलगाव"),
    ("nana-kkhana", r"nānākkhaṇik|nānākhaṇik", r"भिन्न क्षण"),
    ("kiriya", r"kiriy", r"क्रिया"),
    ("katatta", r"kaṭattā", r"किए गए कर्म से उत्पन्न"),
    ("cittasamutthana", r"cittasamuṭṭhān", r"मन से उत्पन्न"),
    ("upada", r"upādā", r"व्युत्पन्न"),
    ("mahabhuta", r"mahābhūt", r"महाभूत"),
    ("bahira", r"bāhir", r"बाह्य"),
    ("asanna", r"asaññasatt", r"पहचान-रहित"),
    ("utusam", r"utusamuṭṭhān", r"तापमान से उत्पन्न"),
    ("aharasam", r"āhārasamuṭṭhān", r"आहार से उत्पन्न"),
    ("vipakabyakata", r"vipākābyākat", r"कर्म-फल रूपी"),
]
out = Counter(); rows = []
for f in FILES[1:]:
    for n, sid, p, h in pairs(f):
        if p.startswith("#"):
            continue
        q = re.sub(r"\{[^}]*\}", "", p.lower()); hb = re.sub(r"\[[^\]]*\]", "", h)
        for name, pr, hr in T:
            a = len(re.findall(pr, q)); b = len(re.findall(hr, hb))
            if a != b:
                out[name] += 1
                rows.append(f"{f} n={n} {sid} {name} P={a} H={b}")
with open(os.path.join(OUT, "review_r1_terms3_out.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(rows))
print(out.most_common())
