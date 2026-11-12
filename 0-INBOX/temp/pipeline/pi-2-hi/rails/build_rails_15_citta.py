"""Shared mind-state (citta) formula strings for the pi-2 Hindi rails, chapters 14 and 15.

All strings are taken from the reviewed pi-1 rails Hindi (Dhammasaṅgaṇī ^1-1, ^1-167, ^1-277, ^1-365, ^1-427,
^1-431, ^1-455, ^1-469, ^1-499, ^1-505, ^1-556, ^1-568, ^1-577 and the abbreviated lines after them),
with the pi-2 termbase where it differs. Imported read-only by build_rails_14.py and build_rails_15.py.
"""
SN = "प्रसन्नता के साथ होने वाला"
UP = "समभाव के साथ होने वाला"
NS = "ज्ञान से जुड़ा"
NVP = "ज्ञान से अलग"
SAS = "प्रेरणा सहित"


def q2(a, b):
    return f"{a} और {b}"


def q3(a, b, c):
    return f"{a}, {b} और {c}"


# somanassasahagataṃ ñāṇasampayuttaṃ sasaṅkhārena…pe… upekkhāsahagataṃ ñāṇavippayuttaṃ sasaṅkhārena
CHAIN8 = "… ".join([q3(SN, NS, SAS), q2(SN, NVP), q3(SN, NVP, SAS), q2(UP, NS), q3(UP, NS, SAS),
                    q2(UP, NVP), q3(UP, NVP, SAS)])
CHAIN8_LIST = [q3(SN, NS, SAS), q2(SN, NVP), q3(SN, NVP, SAS), q2(UP, NS), q3(UP, NS, SAS),
               q2(UP, NVP), q3(UP, NVP, SAS)]

HINA = "हीन"
MAJJ = "मध्यम"
PANI = "उत्तम"
ADH = {"chanda": "चाह की प्रधानता वाला", "viriya": "उत्साह की प्रधानता वाला",
       "citta": "मन की प्रधानता वाला", "vimamsa": "जाँच-परख की प्रधानता वाला"}


def hina_chain(adhs):
    """hīnaṃ… majjhimaṃ… paṇītaṃ… <adh>… … <adh> hīnaṃ… majjhimaṃ… paṇītaṃ (without the first 'hīnaṃ')"""
    parts = [MAJJ, PANI] + [ADH[a] for a in adhs]
    for a in adhs:
        parts += [f"{ADH[a]} {HINA}", MAJJ, PANI]
    return "… ".join(parts)


KAMA_KUSALA = "इंद्रिय-सुखों के लोक से संबंधित हितकर मन"
UPP = "उत्पन्न होता है"
OBJ_ALL = "और जिसका विषय दृश्य रूप हो… या मन का विषय, या जिस किसी को भी वह विषय बनाए"
OBJ_5 = "और जिसका विषय दृश्य रूप हो… या स्पर्श, या जिस किसी को भी वह विषय बनाए"
PHASSA_PE = "उस समय संपर्क होता है… भटकाव का अभाव होता है"
KUSALA_Q = "हितकर परिघटनाएँ कौन-सी हैं?"
AKUSALA_Q = "हानिकर परिघटनाएँ कौन-सी हैं?"
ABYAKATA_Q = "नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं?"
IME_KUSALA = "ये हितकर परिघटनाएँ हैं"
IME_AKUSALA = "ये हानिकर परिघटनाएँ हैं"
IME_ABYAKATA = "ये नैतिक रूप से अनिर्धारित परिघटनाएँ हैं"
AÑÑE = "या उस समय जो भी अन्य परस्पर-आश्रित रूप से उत्पन्न अभौतिक परिघटनाएँ होती हैं"

# jhāna / path formulas (pi-1 ^1-167, the arūpa line after it, ^1-277); bhāveti = अभ्यास करना
RUPUPAPATTI = "जिस समय कोई सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है"
ARUPUPAPATTI = "जिस समय कोई अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है"
JHANA1_KASINA = "इंद्रिय-सुखों से अलग होकर… पहले ध्यान को प्राप्त करके उसमें रहता है, जो पृथ्वी के ध्यान-मंडल वाला है"
ARUPA4 = ("कुछ भी न होने के क्षेत्र को पूरी तरह पार करके, सुख को छोड़ने से… चौथे ध्यान को प्राप्त करके उसमें रहता है, "
          "जो न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाला है")
LOKUTTARA = ("जिस समय कोई लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर "
             "ले जाने वाला होता है, दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए")
JHANA1_PATH = "इंद्रिय-सुखों से अलग होकर… पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है"


def kusala_head(desc):
    """Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti <desc>"""
    return f"जिस समय {KAMA_KUSALA} {UPP}, जो {desc} होता है"
