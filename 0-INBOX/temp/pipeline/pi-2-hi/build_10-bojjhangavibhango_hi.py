# -*- coding: utf-8 -*-
"""pi-2 Hindi zero-shot: 10-bojjhangavibhango.md (Analysis of the Factors of Awakening).
usage: python -I -X utf8 build_10-bojjhangavibhango_hi.py [show]
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import pp_5_7_10_11_hi as P  # noqa: E402
from pp_5_7_10_11_hi import (S, DASH, MAGGANGA, PANNA_PE, VIRIYA_PE, SATI_PE, SATI_SHORT, SAMADHI_PE,  # noqa: E402
                             PITI_FULL, PITI_END, PASSADDHI_REST, UPEKKHA_DEF, LOKUTTARA_HEAD, PHASSA_PE,
                             PHASSA_PE_YO, KUSALA_END, VIPAKA, NISSITA, SB, SB_ORDER, SEVEN_SB, AVASESA, obl_sb)

CH = "10-bojjhangavibhango.md"
T = S.CHAPTER_TITLES[10]
SEVEN = "जागृति के सात अंग"
SEVEN_PE = f"{SEVEN} {DASH} {SB['sati']}… {SB['upekkha']}।"             # Satta bojjhaṅgā – satisambojjhaṅgo…pe… upekkhāsambojjhaṅgo.
VIPAKA_NO_SUNNA = VIPAKA.replace("वाला और शून्य होता है", "वाला होता है")  # ^2-480 line 1: the Pāli lacks "suññataṃ"
assert VIPAKA_NO_SUNNA != VIPAKA


def q(k):
    return f"यहाँ {SB[k]} क्या है?"


def called(k, quoted=True):
    return f"यह “{SB[k]}” कहा जाता है।" if quoted else f"यह {SB[k]} कहा जाता है।"


DEF = {  # Abhidhammabhājanīya definitions (the part after "जो")
    "sati": f"{SATI_PE}, {SB['sati']}, {MAGGANGA}",
    "dv": f"{PANNA_PE}, {SB['dv']}, {MAGGANGA}",
    "viriya": f"{VIRIYA_PE}, {SB['viriya']}, {MAGGANGA}",
    "samadhi": f"{SAMADHI_PE}, {SB['samadhi']}, {MAGGANGA}",
    "upekkha": f"{UPEKKHA_DEF}, {SB['upekkha']}",
}
PITI_DEF = f"जो {PITI_FULL} [वर्तनी-भेद (Sī.): odaggaṃ; “परिघटनाओं की गणना” 9], {PITI_END}, {SB['piti']} है"
PASSADDHI_DEF = (f"अनुभूति के समूह, पहचान के समूह, मानसिक रचनाओं के समूह और चेतना के समूह की जो {PASSADDHI_REST}, "
                 f"{SB['passaddhi']} है")
SAMPAYUTTA7 = "बाकी परिघटनाएँ जागृति के सात अंगों से जुड़ी हैं।"   # Avasesā dhammā sattahi bojjhaṅgehi sampayuttā.
CHAIN6 = "… ".join(AVASESA.format(obl_sb(k))[:-1] for k in SB_ORDER[:6]) + "।"   # … satisambojjhaṅgasampayuttā…pe…


def abh(k):
    return f"{q(k)} जो {DEF[k]} है {DASH} {called(k)}"


def two_kinds(k, a, b, verb, a_first=None):
    """Atthi A, atthi B. Yadapi A tadapi X abhiññāya sambodhāya nibbānāya saṃvattati. Yadapi B …"""
    lead = "जो उच्च ज्ञान, पूर्ण जागृति और निर्वाण की ओर ले जाता है।"
    a1 = a_first[0] if a_first else a
    b1 = a_first[1] if a_first else b
    return (f"{q(k)} कुछ {a1} {verb}, कुछ {b1} {verb}। "
            f"जो {a} {verb}, वह भी {SB[k]} है, {lead} "
            f"जो {b} {verb}, वह भी {SB[k]} है, {lead}")


def bhaveti(k):
    return f"{obl_sb(k)} का अभ्यास करता है"


M = {
    1: "### " + T,
    3: "#### " + S.SECTION_TITLES["Suttantabhājanīyaṃ"],
    5: SEVEN_SB,
    7: (f"{q('sati')} यहाँ भिक्षु सजग होता है, उच्चतम सजगता और सावधानी से युक्त होता है, बहुत पहले किए गए और बहुत "
        f"पहले कहे गए को भी याद करने वाला और बार-बार याद करने वाला होता है {DASH} {called('sati')}"),
    8: (f"इस तरह सजग होकर रहते हुए वह उस शिक्षा की प्रज्ञा से छानबीन करता है, उसे गहराई से परखता है, उसकी पूरी "
        f"जाँच-पड़ताल में लग जाता है {DASH} {called('dv')}"),
    9: (f"जब वह उस शिक्षा की प्रज्ञा से छानबीन करता है, उसे गहराई से परखता है, उसकी पूरी जाँच-पड़ताल में लगा होता है, "
        f"तब उसका उत्साह जाग्रत होता है और ढीला नहीं पड़ता {DASH} {called('viriya')}"),
    10: f"जिसका उत्साह जाग्रत है, उसमें सांसारिक भोग से रहित उल्लास उत्पन्न होता है {DASH} {called('piti')}",
    11: f"जिसका मन उल्लास से भरा है, उसकी काया भी शांत होती है, मन भी शांत होता है {DASH} {called('passaddhi')}",
    12: f"जिसकी काया शांत है, उस सुखी व्यक्ति का मन एकाग्र होता है {DASH} {called('samadhi')}",
    13: f"इस तरह एकाग्र हुए मन को वह भली-भाँति समभाव से देखने वाला होता है {DASH} {called('upekkha')}",
    15: SEVEN_SB,
    17: two_kinds("sati", "स्वयं से संबंधित परिघटनाओं में सजगता", "दूसरों से संबंधित परिघटनाओं में सजगता", "होती है"),
    18: two_kinds("dv", "स्वयं से संबंधित परिघटनाओं में गहरी छानबीन", "दूसरों से संबंधित परिघटनाओं में गहरी छानबीन",
                  "होती है"),
    19: two_kinds("viriya", "शारीरिक उत्साह", "मानसिक उत्साह", "होता है"),
    20: two_kinds("piti", "आरंभिक विचार और सतत विचार वाला उल्लास",
                  "आरंभिक विचार और सतत विचार दोनों से रहित उल्लास", "होता है"),
    21: two_kinds("passaddhi", "मानसिक काया की प्रशांति", "मन की प्रशांति", "होती है",
                  a_first=("मानसिक काया की प्रशांति [वर्तनी-भेद (Syā., Ka.): kāyappassaddhi]",
                           "मन की प्रशांति [वर्तनी-भेद (Syā., Ka.): cittappassaddhi]")),
    22: two_kinds("samadhi", "आरंभिक विचार वाली और सतत विचार वाली एकाग्रता",
                  "आरंभिक विचार से रहित और सतत विचार से रहित एकाग्रता", "होती है"),
    23: two_kinds("upekkha", "स्वयं से संबंधित परिघटनाओं में समभाव", "दूसरों से संबंधित परिघटनाओं में समभाव", "होता है"),
    25: SEVEN_SB,
    27: (f"{q('sati')} यहाँ भिक्षु {bhaveti('sati')}, {NISSITA['m']}, {bhaveti('dv')}… "
         + "… ".join(bhaveti(k) for k in SB_ORDER[2:6]) + f"… {bhaveti('upekkha')}, {NISSITA['m']}।"),
    28: S.SECTION_TITLES["Suttantabhājanīyaṃ"] + "।",
    30: "#### " + S.SECTION_TITLES["Abhidhammabhājanīyaṃ"],
    32: SEVEN_SB,
    34: (f"यहाँ {SEVEN} क्या हैं? {LOKUTTARA_HEAD}, उस समय {SEVEN} होते हैं {DASH} {SB['sati']}… {SB['upekkha']}।"),
    36: abh("sati"),
    37: abh("dv"),
    38: abh("viriya"),
    39: f"{q('piti')} {PITI_DEF} {DASH} {called('piti')}",
    40: f"{q('passaddhi')} {PASSADDHI_DEF} {DASH} {called('passaddhi')}",
    41: abh("samadhi"),
    42: f"{abh('upekkha')} ये {SEVEN} कहे जाते हैं। {SAMPAYUTTA7}",
    44: SEVEN_PE,
    46: (f"{q('sati')} {LOKUTTARA_HEAD}, उस समय जो {SATI_SHORT}, {SB['sati']}, {MAGGANGA} है {DASH} {called('sati')} "
         f"{CHAIN6}"),
    47: (f"{q('upekkha')} {LOKUTTARA_HEAD}, उस समय जो {DEF['upekkha']} है {DASH} {called('upekkha')} "
         + AVASESA.format(obl_sb("upekkha"))),
    49: SEVEN_PE,
    51: (f"यहाँ {SEVEN} क्या हैं? {LOKUTTARA_HEAD}, {PHASSA_PE_YO} {DASH} {KUSALA_END} {VIPAKA}, उस समय {SEVEN} होते हैं "
         f"{DASH} {SB['sati']}… {SB['upekkha']}।"),
    53: f"{abh('sati')[:-1]}…।",
    54: f"{abh('upekkha')} ये “{SEVEN}” कहे जाते हैं। {SAMPAYUTTA7}",
    56: SEVEN_PE,
    58: (f"{q('sati')} {LOKUTTARA_HEAD}, {PHASSA_PE}। {KUSALA_END} {VIPAKA_NO_SUNNA}, उस समय जो {SATI_SHORT}, "
         f"{SB['sati']}, {MAGGANGA} है {DASH} {called('sati')} {CHAIN6}"),
    59: (f"{q('upekkha')} {LOKUTTARA_HEAD}, {PHASSA_PE}। {KUSALA_END} {VIPAKA}, उस समय जो {DEF['upekkha']} है "
         f"{DASH} {called('upekkha')} " + AVASESA.format(obl_sb("upekkha"))),
    60: S.SECTION_TITLES["Abhidhammabhājanīyaṃ"] + "।",
    62: "#### " + S.SECTION_TITLES["Pañhāpucchakaṃ"],
    64: SEVEN_SB,
    66: P.question_kati("जागृति के सात अंगों", masc=True),
    68: P.TIKA_HEAD,
    72: P.DUKA_HEAD,
    76: S.SECTION_TITLES["Pañhāpucchakaṃ"] + "।",
    77: T + " पूरा हुआ।",
}
PP = {70, 74, 75}

if __name__ == "__main__":
    P.check_pi1()
    P.build(CH, M, PP, P.THESE_M, show=len(sys.argv) > 1)
