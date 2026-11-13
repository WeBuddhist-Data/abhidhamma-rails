import sys, re, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\review")
from review_r6_common import *

KW = [
    (r"khandh", r"समूह"),
    (r"cittasamuṭṭhān", r"मन से उत्पन्न"),
    (r"kaṭattā", r"किए गए कर्म से उत्पन्न"),
    (r"upādārūp", r"व्युत्पन्न"),
    (r"paṭisandhi", r"पुनर्जन्म"),
    (r"vatthu", r"आधार"),
    (r"mahābhūt", r"महाभूत"),
    (r"moh", r"मोह"),
    (r"lobh", r"लोभ"),
    (r"rāg", r"राग"),
    (r"domanass", r"उदासी"),
    (r"uddhacc", r"बेचैनी"),
    (r"vicikicch", r"संशय"),
    (r"paṭigh", r"चिढ़"),
    (r"diṭṭh", r"दृष्टि"),
    (r"avijj", r"अज्ञान"),
    (r"saddh", r"श्रद्धा"),
    (r"\bdān[aā]", r"दान"),
    (r"uposath", r"उपवास-व्रत"),
    (r"nibbān", r"निर्वाण"),
    (r"gotrabhu", r"गोत्र-परिवर्तन"),
    (r"vodān", r"शुद्धि"),
    (r"āvajjan", r"मोड़"),
    (r"vuṭṭhā|vuṭṭhah", r"बाहर आ"),
    (r"magg(?!a?paccay)", r"मार्ग(?!-कारण)"),
    (r"phal", r"फल"),
    (r"jhān(?!a?paccay)", r"ध्यान(?!-कारण)"),
    (r"cakkh", r"आँख"),
    (r"ārammaṇādhipati", r"विषय रूपी प्रधानता"),
    (r"sahajātādhipati", r"सह-उत्पत्ति रूपी प्रधानता"),
    (r"pakatūpanissay", r"स्वाभाविक"),
    (r"anantarūpanissay", r"निकटता रूपी प्रबल आश्रय"),
    (r"ārammaṇūpanissay", r"विषय रूपी प्रबल आश्रय"),
    (r"purim", r"पहले"),
    (r"pacchim", r"बाद"),
    (r"garu", r"महत्व"),
    (r"ariy", r"आर्य"),
    (r"āsav", r"मैल"),
    (r"saññojan", r"बंधन"),
    (r"ganth", r"गाँठ"),
    (r"nīvaraṇ", r"बाधा"),
    (r"parāmās|parāmaṭṭh", r"ग़लत धारणा"),
    (r"kabaḷīkār", r"कौर"),
    (r"jīvitindriy", r"जीवन-क्षमता"),
    (r"asaññasatt|āsaññasatt", r"पहचान-रहित"),
    (r"ahetuk", r"मूल से रहित"),
    (r"arūp", r"अभौतिक"),
    (r"kāmāsav|kāmarāg|kāmacchand", r"इंद्रिय-सुख"),
    (r"bhavāsav|bhavarāg", r"अस्तित्व"),
    (r"abhijjh", r"लालच"),
    (r"idaṃsaccābhinives", r"केवल यही सत्य है"),
    (r"sīlabbat", r"व्रत"),
    (r"thinamiddh|thīnamiddh", r"आलस्य"),
    (r"kukkucc", r"पछतावे"),
    (r"byāpād", r"दुर्भावना"),
    (r"dos[aoā]", r"द्वेष"),
    (r"\bmān[aoā]", r"अहंकार"),
    (r"\bissā", r"ईर्ष्या"),
    (r"macchariy", r"कंजूसी"),
    (r"sahajāt", r"सह-उत्पत्ति"),
    (r"purejāt", r"पूर्व-उत्पत्ति"),
    (r"pacchājāt", r"पश्चात्-उत्पत्ति"),
    (r"nānākkhaṇik", r"भिन्न क्षण"),
    (r"\bcetan", r"इरादा"),
    (r"viññāṇ", r"चेतना"),
    (r"paññ", r"प्रज्ञा"),
    (r"sukh", r"सुख"),
    (r"dukkh", r"दुःख"),
    (r"senāsan", r"निवास-स्थान"),
    (r"kiles", r"क्लेश"),
    (r"\bpāṇ", r"जीव की हत्या"),
    (r"saṅgh", r"संघ"),
]


def pe_count(p):
    return p.count("…pe…") + p.replace("…pe…", "").count("…")


def run(verbose=None):
    stats = collections.Counter(); bad = collections.defaultdict(list)
    for fi, f in enumerate(FILES):
        for r in pairs(f):
            p = IDRE.sub("", r["p"]); h = IDRE.sub("", r["h"])
            p = re.sub(r"\{[^}]*\}", "", p).lower()
            h = re.sub(r"\[(पाठभेद|वर्तनी-भेद)[^\]]*\]", "", h)
            tag = f"{fi}|{r['id']}|k{r['k']}"
            a, b = pe_count(r["p"]), r["h"].count("…")
            if a != b:
                bad["…pe…"].append((tag, a, b))
            for pk, hk in KW:
                a = len(re.findall(pk, p)); b = len(re.findall(hk, h))
                stats[pk] += a
                if a != b:
                    bad[pk].append((tag, a, b))
    return stats, bad

if __name__ == "__main__":
    stats, bad = run()
    for k in ["…pe…"] + [k for k, _ in KW]:
        print(f"{k:30s} occ={stats.get(k,0):5d} mismatchlines={len(bad[k]):4d}  {bad[k][:6]}")

