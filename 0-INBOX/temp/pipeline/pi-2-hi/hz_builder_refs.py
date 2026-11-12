"""For key old strings of the harmonise pass, list the builder/helper files and the assignment (constant) where they occur."""
import os, re, glob, collections

HERE = os.path.dirname(os.path.abspath(__file__))
KEYS = {
    "I1 sattanikāya (ch6)": "उन-उन प्राणी-वर्गों",
    "I1 byasana (ch6)": "प्रभावित व्यक्ति में",
    "I1 jāti (ch4)": "भली-भाँति जन्म, प्रवेश",
    "I1 maraṇa (ch4)": "च्युत होना, चल बसना",
    "I1 soka (ch4)": "शोक में डूबे रहना",
    "I1 parideva (ch4)": "रोना-धोना, विलाप करना",
    "I1 upāyāsa (ch4)": "परेशान रहना, निराश रहना",
    "I2 paṭipadā (ch4, ch16)": "ले जाने वाला मार्ग",
    "I2 paṭipadā oblique": "ले जाने वाले मार्ग",
    "I4 niddesa (ch6, ch7)": "का विवरण",
    "I5 heads (ch17)": "प्रकारों की",
    "I5 closings (ch17)": "एकल प्रकार",
    "I6 upekkhā (ch12)": "उदासीन भाव से देखना",
    "I7 akaniṭṭha (ch18)": "सबसे ऊँचे अकनिष्ठ",
    "B1 sacca (ch4)": "उत्पत्ति का सत्य",
    "B1 sacca magga (ch4)": "मार्ग का सत्य",
    "B2 Tena vuccati": "कहा जाता है “",
    "B2 Tena vuccati (इसलिए)": "इसलिए “",
    "B3 avasesā (ch7, 10, 11)": "बाकी परिघटनाएँ",
    "B4 iriyati (ch7)": "गतिशील रहता है",
    "B5 ātāpī (ch4)": "संसार के प्रति लालच",
    "B6 veramaṇī (ch4)": "कठोर वाणी से",
    "B6 veramaṇī (ch11)": "काम-संबंधी ग़लत आचरण",
    "B6 adinnādāna (ch4)": "न दी गई वस्तु",
    "B6 adinnādāna (ch11)": "जो न दिया गया हो",
    "B7 aṭṭhaṅgika (ch4)": "अष्टांगिक",
    "B8 metti (ch3)": "मैत्री रखना",
    "B9 upādānakkhandha (ch12)": "आसक्ति के विषय बनने वाले",
    "B9 upādānakkhandha (ch7)": "आसक्ति के पाँचों समूह",
    "B10 body parts (ch3)": "आँतों की बंधनी",
    "B11 paṭisambhidā (ch16)": "प्रत्युत्पन्न बुद्धि",
    "B12 yañca rūpaṃ (ch3)": "और जो भौतिक रूप दिखाई",
    "B13 upeto (ch7)": "इससे समन्वित",
    "B13 upeto (ch9)": "उनसे परिपूर्ण",
    "B13 upeto (ch12)": "भली-भाँति सहित",
    "B14 chanda (ch9)": "चाहत रखना",
    "B15 phassa (ch5)": "संपर्क से जुड़ी",
    "B16 gloss (ch9, ch16)": "का अर्थ है",
    "PP subject ये (ch7, 10, 11)": "\"ये \"",
    "PP subject सभी क्षमताएँ (ch5)": "सभी क्षमताएँ",
    "PP subject पाँचों समूह (ch1)": "पाँचों समूह",
    "PP neg «न होने वाल»": "न होने वाल",
    "PP sahagata short (ch1, 3, 8, 14, 15)": "के साथ होत",
    "PP pronoun इन्हें": "इन्हें",
    "PP kati": "कितने",
}
files = sorted(glob.glob(os.path.join(HERE, "*.py")))
files = [f for f in files if not os.path.basename(f).startswith(("hz_", "harmonise", "find_divergences", "check_", "test_"))]
for name, key in KEYS.items():
    hits = collections.OrderedDict()
    for f in files:
        for i, line in enumerate(open(f, encoding="utf-8"), 1):
            if key in line:
                m = re.match(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*=", line)
                d = re.search(r"def ([A-Za-z_][A-Za-z0-9_]*)", line)
                hits.setdefault(os.path.basename(f), []).append(m.group(1) if m else f"l.{i}")
    print(name, "::", "; ".join(f"{k}: {', '.join(sorted(set(v))[:6])}" for k, v in hits.items()) or "-")
