import sys, os, re
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from review_r5_common import *

T = [
    ("nahetu", r"(?<![a-z])nahet[uū](?!y|paccay|duk|mūlak)", r"मूल रूपी न होने", None),
    ("sahetuk", r"sahetuk", r"मूल वाल", None),
    ("ahetuk", r"(?<!s)ahetuk", r"मूल से रहित", None),
    ("hetusampayutt", r"hetusampayutt", r"मूलों से जुड़", None),
    ("hetuvippayutt", r"hetuvippayutt", r"मूलों से अलग", None),
    ("na ca hetu", r"na ca hetu", r"पर स्वयं मूल रूपी न होने", None),
    ("noupādān", r"noupādān", r"आसक्ति रूपी न होने", None),
    ("no ca upādān", r"no ca upādān", r"पर स्वयं आसक्ति रूपी न होने", None),
    ("upādānasampayutt", r"upādānasampayutt", r"आसक्ति से जुड़", None),
    ("upādānavippayutt", r"upādānavippayutt", r"आसक्ति से अलग", None),
    ("anupādāniy", r"anupādāniy", r"विषय न बन", None),
    ("upādāniy", r"(?<!an)upādāniy", r"विषय बन", None),
    ("sappaccay", r"(?<![a-z])sappaccay", r"कारणों पर निर्भर रहने", None),
    ("appaccay", r"(?<![a-z])appaccay", r"कारणों पर निर्भर न रहने", None),
    ("saṅkhat", r"(?<![a-z])saṅkhat", r"(?<!अ)निर्मित", None),
    ("asaṅkhat", r"asaṅkhat", r"अनिर्मित", None),
    ("sanidassan", r"sanidassan", r"दिखाई देने", None),
    ("anidassan", r"(?<![a-z])anidassan", r"दिखाई न देने", None),
    ("sappaṭigh", r"sappaṭigh", r"टकराव वाल", None),
    ("appaṭigh", r"appaṭigh", r"टकराव से रहित", None),
    ("lokiy", r"lokiy", r"(?<!अ)लौकिक", None),
    ("lokuttar", r"lokuttar", r"लोकोत्तर", None),
    ("kenaci", r"kenaci", r"किसी एक प्रकार की चेतना से", None),
    ("kenaci na", r"kenaci na", r"चेतना से न ज", None),
    ("sampayuttak", r"sampayuttak", r"जुड़े हुए|जुड़ा हुआ|जुड़ी हुई", None),
    ("purimā", r"purim", r"पहले-पहले", None),
    ("pacchim", r"pacchim", r"बाद-बाद", None),
    ("garuṃ", r"garuṃ", r"महत्व देकर", None),
    ("ārabbha", r"ārabbha", r"विषय बनाकर", None),
    ("paccavekkh", r"paccavekkh", r"पुनः विचार", None),
    ("anicc", r"anicc", r"अनित्य", None),
    ("domanass", r"domanass", r"उदासी", None),
    ("dibb", r"dibb", r"दिव्य", None),
    ("saddh", r"saddh", r"श्रद्धा", None),
    ("senāsan", r"senāsan", r"निवास-स्थान", None),
    ("mān", r"(?<![a-z])mān", r"अहंकार", None),
    ("rāg", r"(?<![a-z])rāg", r"राग", None),
    ("dukkh", r"dukkh", r"दुःख", None),
    ("sukh", r"sukh", r"सुख", None),
    ("vipassan|vipass", r"vipass", r"अंतर्दृष्टि", None),
    ("samāpatti", r"samāpatt|samāpajj", r"ध्यान-अवस्था", None),
    ("nānākkhaṇik", r"nānākkhaṇik", r"भिन्न क्षण", None),
    ("cetopariy", r"cetopariy", r"दूसरों के मन को जानने", None),
    ("vipāk", r"vipāk", r"कर्म-फल", None),
    ("phal", r"phal", r"(?<!कर्म-)फल", None),
    ("magg", r"magg", r"मार्ग", None),
    ("jhān", r"jhān", r"ध्यान(?!-अवस्था)", None),
    ("vatthu", r"vatthu", r"आधार", None),
    ("mahābhūt", r"mahābhūt", r"महाभूत", None),
    ("diṭṭh", r"diṭṭh", r"दृष्टि", None),
    ("upanissāya", r"upanissāya", r"प्रबल आश्रय से", None),
    ("arūpe", r"(?<![a-z])arūpe(?![a-z])", r"अभौतिक लोक", None),
    ("arūpī-item", r"(?<![a-z])arūpi", r"अभौतिक(?! लोक)", None),
    ("ariyā", r"(?<![a-z])ariy", r"आर्य", None),
    ("nibbān", r"nibbān", r"निर्वाण", None),
    ("kilese", r"kiles", r"क्लेश", None),
    ("āhār", r"āhār", r"आहार|भोजन", None),
    ("indriy", r"indriy", r"क्षमता", None),
]


def cnt(rx, s):
    return len(re.findall(rx, s))


issues = defaultdict(list)
for fn in FILES:
    P, H = pairs(fn)
    for i, (a, b) in enumerate(zip(P, H), 1):
        if not a.strip() or a.startswith("#"):
            continue
        al = re.sub(r"\{[^}]*\}", "", a.lower())
        bl = re.sub(r"\[[^\]]*\]", "", b)
        for nm, pr, hr, _ in T:
            c1 = cnt(pr, al); c2 = cnt(hr, bl)
            if c1 != c2:
                issues[nm].append(f"{fn[:4]}:{i} {c1}/{c2}")
for k, v in issues.items():
    print(f"== {k}: {len(v)}")
    print("   ", "; ".join(v[:60]))
