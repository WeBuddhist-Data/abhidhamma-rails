import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi\review")
from review_r3_pairs import load
from review_r3_struct import FILES

MAP = [
    ("upapajjant", "जन्म लेने वाल"),
    ("cavant", "मरने वाल"),
    ("pavatte", "जीवन के दौरान"),
    (r"arūpe|arūpāvacar", "अभौतिक"),
    ("pañcavokār", "पाँच समूहों|पाँच समूह"),
    ("catuvokār", "चार समूहों|चार या पाँच|चार समूह"),
    ("asaññasatt|asaññatt", "पहचान-रहित"),
    ("apāy|āpāyik", "दुर्गति"),
    ("nirodhasamāpann", "समाप्ति की ध्यान-अवस्था"),
    ("samāpann", "लीन"),
    ("kāmāvacar", "इंद्रिय-सुखों"),
    (r"(?<!a)rūpāvacar", "सूक्ष्म भौतिक"),
    ("suddhāvās", "शुद्ध निवास"),
    ("arahant|arahato|arahā", "अर्हत"),
    ("aggamaggasamaṅg", "सर्वोच्च मार्ग से युक्त"),
    ("aggamagg", "सर्वोच्च मार्ग"),
    ("aggaphal", "सर्वोच्च फल"),
    ("puthujjan", "साधारण व्यक्ति"),
    ("anabhisametāv", "बोध न"),
    ("abhisametāv", "बोध"),
    ("pacchimabhavik", "अंतिम जन्म"),
    ("pacchimacitt", "अंतिम मन"),
    (r"(?<!agga)phal", "फल"),
    ("paṭhamajjhān", "पहली"),
    ("dutiyajjhān", "दूसरी"),
    ("tatiyajjhān", "तीसरी"),
    ("catutthajjhān", "चौथी"),
    (r"\bvinā\b", "बिना"),
    ("assāsapassās", "साँस"),
    ("vitakk", "आरंभिक विचार"),
    ("avitakkaavicār|vinā vitakk", "सतत विचार से रहित|सतत विचार के बिना"),
    ("savitakkasavicār", "आरंभिक विचार और सतत विचार वाल|आरंभिक विचार और सतत विचार से युक्त"),
    ("taṇh", "तृष्णा"),
    ("maggavippayutt|taṇhāvippayuttamaggavippayutt", "मार्ग से अलग"),
    ("vattamāne", "चलते समय"),
    ("paṭilabh", "प्राप्त (?:नहीं )?कर"),
    ("parinibbāy", "पूर्ण निर्वाण"),
    ("uppādakkhaṇe", "उत्पन्न होने के क्षण"),
    ("bhaṅgakkhaṇe", "भंग होने के क्षण"),
    (r"\bitaresaṃ\b|\bavasese\b", "बाकी"),
    (r"\bsabbesaṃ\b", "सभी"),
    ("anantarā", "ठीक बाद"),
    (r"\bakusale\b", "हानिकर"),
    (r"\bdutiye\b", "दूसरे (?!लोग)"),
    (r"\bmaggassa\b", "(?<!सर्वोच्च )मार्ग (?:और फल )?के (?:उत्पन्न|भंग)"),
    (r"bhūmiyaṃ", "भूमि|स्तर"),
    (r"\byattha\b|\btattha\b", "स्थान|वहाँ"),
]

def norm(s):
    return re.sub(r"\[[^\]]*\]", "", s)

if __name__ == "__main__":
    for fn in FILES:
        p, h = load(fn)
        for i, (a, b) in enumerate(zip(p, h), 1):
            if a.startswith("#"): continue
            A = norm(a).lower(); B = norm(b)
            probs = []
            for pr, hr in MAP:
                if pr in (r"\byattha\b|\btattha\b",): continue
                np_ = len(re.findall(pr, A)); nh = len(re.findall(hr, B))
                if pr == "samāpann":
                    np_ = len(re.findall(r"(?<!nirodha)samāpann", A)) + len(re.findall("nirodhasamāpann", A))
                if pr == "aggamagg":
                    np_ = len(re.findall(r"aggamagg", A))
                if np_ != nh:
                    probs.append(f"{pr.split('|')[0]}:{np_}/{nh}")
            if probs:
                print(fn[:4], i, " ".join(probs))


