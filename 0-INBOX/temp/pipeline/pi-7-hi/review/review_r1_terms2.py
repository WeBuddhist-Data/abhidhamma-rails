import re, sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from review_r1_common import *

T = [
    ("raga", r"rāg", r"राग"), ("ditthi", r"(?<!micchā)(?<!micchā)diṭṭh", r"(?<!ग़लत )(?<!गलत )(?<!निश्चित ग़लत )दृष्टि"),
    ("vicikiccha", r"vicikicch", r"संशय"), ("uddhacca", r"uddhacc", r"बेचैनी"), ("domanassa", r"domanass", r"उदासी"),
    ("moha", r"moh", r"मोह"), ("dosa", r"(?<![a-zā])dos", r"द्वेष"), ("mana", r"(?<![a-zāī])mān[oaṃ]", r"अहंकार"),
    ("patthana", r"patthan", r"कामना"), ("saddha", r"saddh", r"श्रद्धा"), ("cagga", r"cāg", r"त्याग"),
    ("panna", r"paññ(?!att)", r"प्रज्ञा"), ("sukha", r"sukh", r"सुख"), ("dukkha-kayika", r"kāyikaṃ dukkh|kāyik[aā]ssa dukkh|kāyikaṃ sukh|kāyikassa sukh", r"शारीरिक"),
    ("utu", r"(?<![a-zā])utu", r"तापमान"), ("bhojana", r"bhojan", r"भोजन"), ("senasana", r"senāsan", r"निवास"),
    ("puggala", r"puggal", r"व्यक्ति"),
    ("cakkhu", r"cakkh", r"आँख|दिव्य आँख"), ("sota", r"(?<![a-z])sot", r"कान"), ("ghana", r"ghān|ghāṇ", r"नाक"),
    ("jivha", r"jivh", r"जीभ"), ("kaya", r"(?<![a-zā])kāy(?!ik)", r"शरीर"),
    ("nibbana", r"nibbān", r"निर्वाण"), ("phala", r"phal", r"फल(?!-)"), ("gotrabhu", r"gotrabh", r"गोत्र"),
    ("vodana", r"vodān", r"शुद्धि"), ("anuloma", r"anulom", r"अनुरूपता"), ("bhavanga", r"bhavaṅg", r"जीवन-धारा"),
    ("avajjana", r"āvajjan", r"मोड़ने"), ("vutthana", r"vuṭṭhān", r"बाहर आने"),
    ("cetana", r"cetan", r"इरादा|इरादे"), ("iddhi", r"iddhividh", r"अलौकिक"), ("cetopariya", r"cetopariy", r"दूसरों के मन"),
    ("pubbenivasa", r"pubbenivās", r"पूर्व जन्म"), ("yathakamm", r"yathākammūpag", r"अपने कर्मों"),
    ("anagata", r"anāgataṃs", r"भविष्य"), ("dibba", r"dibb", r"दिव्य"),
    ("akasa", r"ākāsānañc", r"अनंत आकाश"), ("vinnanañca", r"viññāṇañc", r"अनंत चेतना"),
    ("akinc", r"ākiñcañ", r"कुछ भी न"), ("nevasanna", r"nevasaññ", r"न पहचान न"),
    ("sekkha", r"sekkh", r"सीखने के चरण"), ("puthujjana", r"puthujjan", r"साधारण व्यक्ति"),
    ("arahant", r"arah(?!antaghāt)", r"अर्हत्(?! की हत्या)"),
    ("panatipata", r"pāṇātipāt|pāṇaṃ", r"जीव"), ("adinna", r"adinn", r"बिना दिया"), ("musa", r"musā", r"झूठ"),
    ("pisuna", r"pisuṇ", r"चुगली"), ("pharusa", r"pharus", r"कठोर"), ("sampha", r"samph", r"बकवास"),
    ("abhijjha", r"abhijjh", r"लालच"), ("byapada", r"byāpād", r"दुर्भावना"), ("micchaditthi", r"micchādiṭṭh", r"ग़लत दृष्टि|गलत दृष्टि"),
    ("matu", r"mātu|mātaraṃ", r"माता"), ("pitu", r"pitu|pitaraṃ", r"पिता"), ("sangha", r"saṅgh", r"संघ"),
    ("lohita", r"lohit|ruhir", r"खून"), ("niyata", r"niyat", r"निश्चित"),
    ("jhana", r"jhān(?!apaccay|aṅg)", r"ध्यान(?!-कारण)"), ("magga", r"magg(?!apaccay|aṅg)", r"मार्ग(?!-कारण)"),
    ("dana", r"dān", r"दान"), ("sila", r"sīl", r"सदाचार"), ("uposatha", r"uposath", r"उपवास"),
    ("vipassana", r"vipassan|vippassan|vipassati|vipassanti|vippassati", r"अंतर्दृष्टि"),
    ("samapatti", r"samāpatt", r"ध्यान-अवस्था"), ("abhinna", r"abhiññ", r"उच्च ज्ञान"),
    ("assadeti", r"assād", r"रस लेत|रस ले"), ("abhinandati", r"abhinand", r"आनंद"),
    ("paccavekkh", r"paccavekkh", r"पुनः विचार"), ("garu", r"garuṃ", r"महत्व"),
    ("kabalikara", r"kabaḷ", r"कौर"), ("rupajivit", r"rūpajīvit", r"जीवन-क्षमता"),
    ("indriya-generic", r"indriy(?!apaccay)", r"क्षमता(?!-कारण)"),
    ("ahara-generic", r"āhār(?!apaccay|asamuṭṭh)", r"आहार(?!-कारण| से उत्पन्न)"),
    ("purejata", r"purejāt(?!apaccay)", r"पूर्व-उत्पत्ति(?!-कारण)|पहले उत्पन्न"),
    ("pacchajata", r"pacchājāt(?!apaccay)", r"पश्चात्-उत्पत्ति(?!-कारण)|बाद में उत्पन्न"),
    ("sahajata", r"sahajāt(?!apaccay)", r"सह-उत्पत्ति(?!-कारण)"),
    ("nana", r"nānākhaṇik", r"अलग-अलग क्षण"),
    ("hetu-noun", r"hetū|hetu(?![a-zā])", r"मूल(?!-कारण)"),
]

out = Counter(); rows = []
for f in FILES[1:]:
    for n, sid, p, h in pairs(f):
        q = re.sub(r"\{[^}]*\}", "", p.lower()); hb = re.sub(r"\[[^\]]*\]", "", h)
        for name, pr, hr in T:
            a = len(re.findall(pr, q)); b = len(re.findall(hr, hb))
            if a != b:
                out[name] += 1
                rows.append(f"{f} n={n} {sid} {name} P={a} H={b}")
with open(os.path.join(OUT, "review_r1_terms2_out.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(rows))
print(out.most_common())
