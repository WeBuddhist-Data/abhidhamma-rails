# -*- coding: utf-8 -*-
"""Assert that the strings reused from pi-1 (and pi-4/pi-5) still occur verbatim there."""
import os, re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import hz_3_14_15_common as C
import importlib.util

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi"


def corpus(book):
    d = os.path.join(ROOT, f"{book}-hindi-plain-rails_split_chapters")
    t = "\n".join(open(os.path.join(d, f), encoding="utf-8-sig").read() for f in os.listdir(d) if f.endswith(".md"))
    return re.sub(r"\s*\[[^\]]*\]", "", t)


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), os.path.join(C.HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


B3, B14, B15 = load("build_3-dhatuvibhango_hi"), load("build_14-sikkhapadavibhango_hi"), load("build_15-patisambhidavibhango_hi")
pi1, pi4, pi5 = corpus("pi-1"), corpus("pi-4"), corpus("pi-5")
checks = {
    "pi-1": [C.PHASSA_PE, C.OBJ_PE, C.OBJ_PE_5, C.KAMA_KUSALA, C.SOM_NS, C.ARISEN_FORMLESS, C.PATHAVI_KASINA,
             C.VIVICCA_JH1, C.LOKUTTARA, C.NEVASANNA, C.RUPU, C.ARUPU, C.ADHI_CHAIN4, C.ADHI_CHAIN3, B14.CETANA[7:-3],
             "दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना",
             B3.AVIJJA, B3.CITTA_SYN, B3.TAKKA_FULL, B3.X["apo"], B3.X["tejo"], B3.X["vayo"], B3.X["akasa"],
             B3.DHAMMA_RUPA, *[t for _, t in B3.FEEL.values()], B15.KIRIYA, "जो इसी जीवन में सुख से रहने के लिए होता है",
             "आँख की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली है और जिसका विषय दृश्य रूप होता है",
             "मानसिक पक्ष और भौतिक रूप", "दुःख के अंत की ओर ले जाने वाले प्रगति के ढंग", "कर्म के फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है",
             "मन का आक्रोश, प्रतिघात, चिढ़, प्रतिविरोध, कोप, प्रकोप, तीव्र प्रकोप, द्वेष, गहरा द्वेष, तीव्र द्वेष, मन की दुर्भावना, मन का गहरा द्वेष, क्रोध, क्रोध करना, क्रोध से भरा होना, द्वेष, द्वेष करना, द्वेष से भरा होना, दुर्भावना, दुर्भावना रखना",
             "नीचे अवीचि नरक को सीमा बनाकर, ऊपर दूसरों की रची गई चीज़ों पर अधिकार रखने वाले देवताओं",
             *[C.P[C._norm(k)][0] for k in ("upādinnupādāniyā", "sāsavā")]] + C.CITTA8_REST + B15.DITTHI,
    "pi-4": [B15.NAVANGA, "बिना दी गई चीज़ लेने", "इंद्रिय-सुखों में दुराचार"],
    "pi-5": ["जीव-हत्या से दूर रहना", "लापरवाही का कारण बनने वाली शराब, मदिरा और नशीली चीज़ों से दूर रहना"],
}
corp = {"pi-1": pi1, "pi-4": pi4, "pi-5": pi5}
miss = []
for b, strs in checks.items():
    for s in strs:
        s2 = s.replace("वाले", "वाली") if b == "pi-1" and s in (C.P[C._norm("upādinnupādāniyā")][0], C.P[C._norm("sāsavā")][0]) else s
        if s2 not in corp[b]:
            miss.append((b, s2[:90]))
print("missing:", len(miss))
for m in miss:
    print("  ", m)
