# -*- coding: utf-8 -*-
"""pi-2 Hindi zero-shot: 11-maggangavibhango.md (Analysis of the Path Factors).
usage: python -I -X utf8 build_11-maggangavibhango_hi.py [show]
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import pp_5_7_10_11_hi as P  # noqa: E402
from pp_5_7_10_11_hi import (S, DASH, MAGGANGA, PANNA_PE, VIRIYA_PE, SATI_PE, SAMADHI_PE, SAMADHI_FULL,  # noqa: E402
                             FOUR_TRUTHS, SAMMAVAYAMA, VACA_DEF, KAMMANTA_DEF, AJIVA_DEF, SANKAPPA_FULL,
                             LOKUTTARA_HEAD, PHASSA_PE, KUSALA_END, VIPAKA, NISSITA, SB, MAGGA, M8, M5,
                             ATTHANGIKA, PANCANGIKA, AVASESA, JHANA4, FORMULA, anupassi)

CH = "11-maggangavibhango.md"
T = S.CHAPTER_TITLES[11]


def name(k):
    return MAGGA[k][0]


def q(k):
    return f"यहाँ {name(k)} क्या है?"


def called(k):
    return f"यह “{name(k)}” {'कहा जाता है' if MAGGA[k][1] == 'm' else 'कही जाती है'}।"


EIGHT = ", ".join(name(k) for k in M8)
FIVE = ", ".join(name(k) for k in M5)
ARIYA8 = f"आठ अंगों वाला आर्य मार्ग, यानी {DASH} {EIGHT}।"         # Ariyo aṭṭhaṅgiko maggo, seyyathidaṃ – …
LIST8 = f"{ATTHANGIKA} {DASH} {EIGHT}।"                            # Aṭṭhaṅgiko maggo – …
LIST8_PE = f"{ATTHANGIKA} {DASH} {name('ditthi')}… {name('samadhi')}।"
LIST5 = f"{PANCANGIKA} {DASH} {FIVE}।"
OBL8 = "आठ अंगों वाले मार्ग"
OBL5 = "पाँच अंगों वाले मार्ग"

DEF = {  # Abhidhammabhājanīya (after "जो")
    "ditthi": f"{PANNA_PE}, {SB['dv']}, {MAGGANGA}",
    "sankappa": f"{SANKAPPA_FULL}, सही संकल्प, {MAGGANGA}",
    "sankappa_pe": f"सोचना, आरंभिक विचार… सही संकल्प, {MAGGANGA}",
    "vaca": f"{VACA_DEF}, सही वाणी, {MAGGANGA}",
    "kammanta": f"{KAMMANTA_DEF}, सही कर्म, {MAGGANGA}",
    "ajiva": f"{AJIVA_DEF}, सही आजीविका, {MAGGANGA}",
    "vayama": f"{VIRIYA_PE}, {SB['viriya']}, {MAGGANGA}",
    "sati": f"{SATI_PE}, {SB['sati']}, {MAGGANGA}",
    "samadhi": f"{SAMADHI_PE}, {SB['samadhi']}, {MAGGANGA}",
    "samadhi_full": f"{SAMADHI_FULL}, {SB['samadhi']}, {MAGGANGA}",
}


def abh(k, d=None):
    return f"{q(k)} जो {DEF[d or k]} है {DASH} {called(k)}"


def bhaveti(k):
    return f"{name(k)} का अभ्यास करता है"


def joined(obl):
    return AVASESA.format(obl)


CHAIN4 = "… ".join(joined(name(k))[:-1] for k in ("ditthi", "sankappa", "vayama", "sati")) + "।"
VIP = f"{LOKUTTARA_HEAD}, {PHASSA_PE}। {KUSALA_END} {VIPAKA}"

M = {
    1: "### " + T,
    3: "#### " + S.SECTION_TITLES["Suttantabhājanīyaṃ"],
    5: ARIYA8,
    7: f"{q('ditthi')} {FOUR_TRUTHS} {DASH} {called('ditthi')}",
    8: f"{q('sankappa')} त्याग का संकल्प, दुर्भावना के अभाव का संकल्प, अहिंसा का संकल्प {DASH} {called('sankappa')}",
    9: (f"{q('vaca')} झूठ बोलने से दूर रहना, चुगली करने से दूर रहना, कठोर वचन बोलने से दूर रहना, व्यर्थ की बकवास से "
        f"दूर रहना {DASH} {called('vaca')}"),
    10: (f"{q('kammanta')} जीव-हत्या से दूर रहना, जो न दिया गया हो, उसे लेने से दूर रहना, काम-संबंधी ग़लत आचरण से "
         f"दूर रहना {DASH} {called('kammanta')}"),
    11: (f"{q('ajiva')} यहाँ आर्य शिष्य ग़लत आजीविका को छोड़कर सही आजीविका से जीवन-यापन करता है {DASH} "
         f"{called('ajiva')}"),
    12: f"{q('vayama')} {SAMMAVAYAMA} {DASH} {called('vayama')}",
    13: (f"{q('sati')} यहाँ भिक्षु "
         + ", ".join(f"{anupassi(k)}, {FORMULA}" for k in ("kaya", "vedana", "citta", "dhamma"))
         + f" {DASH} {called('sati')}"),
    14: f"{q('samadhi')} यहाँ भिक्षु {JHANA4} {DASH} {called('samadhi')}",
    16: ARIYA8,
    18: (f"{q('ditthi')} यहाँ भिक्षु {bhaveti('ditthi')}, {NISSITA['f']}, "
         + "… ".join(bhaveti(k) for k in M8[1:7]) + f"… {bhaveti('samadhi')}, {NISSITA['f']}।"),
    19: S.SECTION_TITLES["Suttantabhājanīyaṃ"] + "।",
    21: "#### " + S.SECTION_TITLES["Abhidhammabhājanīyaṃ"],
    23: LIST8,
    25: (f"यहाँ {ATTHANGIKA} क्या है? {LOKUTTARA_HEAD}, उस समय {ATTHANGIKA} होता है {DASH} "
         f"{name('ditthi')}… {name('samadhi')}।"),
    27: abh("ditthi"),
    28: abh("sankappa"),
    29: abh("vaca"),
    30: abh("kammanta"),
    31: abh("ajiva"),
    32: abh("vayama"),
    33: abh("sati"),
    34: f"{abh('samadhi')} यह “{ATTHANGIKA}” कहा जाता है। {joined(OBL8)}",
    36: LIST5,
    38: f"यहाँ {PANCANGIKA} क्या है? {LOKUTTARA_HEAD}, उस समय {PANCANGIKA} होता है {DASH} {FIVE}।",
    40: abh("ditthi"),
    41: abh("sankappa", "sankappa_pe"),
    42: abh("vayama"),
    43: abh("sati"),
    44: f"{abh('samadhi')} यह “{PANCANGIKA}” कहा जाता है। {joined(OBL5)}",
    46: LIST5,
    48: f"{q('ditthi')} {LOKUTTARA_HEAD}, उस समय जो {DEF['ditthi']} है {DASH} {called('ditthi')} {CHAIN4}",
    49: (f"{q('samadhi')} {LOKUTTARA_HEAD}, उस समय जो {DEF['samadhi']} है {DASH} {called('samadhi')} "
         + joined(name("samadhi"))),
    51: LIST8_PE,
    53: (f"यहाँ {ATTHANGIKA} क्या है? {VIP}, उस समय {ATTHANGIKA} होता है {DASH} {name('ditthi')}… "
         f"{name('samadhi')}। यह “{ATTHANGIKA}” कहा जाता है। {joined(OBL8)}"),
    55: LIST5,
    57: (f"यहाँ {PANCANGIKA} क्या है? {VIP}, उस समय {PANCANGIKA} होता है {DASH} {FIVE}। "
         f"यह “{PANCANGIKA}” कहा जाता है। {joined(OBL5)}"),
    59: LIST5,
    61: f"{q('ditthi')} {VIP}, उस समय जो {DEF['ditthi']} है {DASH} {called('ditthi')} {CHAIN4}",
    62: (f"{q('samadhi')} {VIP}, उस समय जो {DEF['samadhi_full']} है {DASH} {called('samadhi')} "
         + joined(name("samadhi"))),
    63: S.SECTION_TITLES["Abhidhammabhājanīyaṃ"] + "।",
    65: "#### " + S.SECTION_TITLES["Pañhāpucchakaṃ"],
    67: ARIYA8,
    69: P.question_kati("मार्ग के आठ अंगों", masc=True),
    71: P.TIKA_HEAD,
    75: P.DUKA_HEAD,
    82: S.SECTION_TITLES["Pañhāpucchakaṃ"] + "।",
    83: T + " पूरा हुआ।",
}
PP = {73, 77, 78, 79, 80, 81}

if __name__ == "__main__":
    P.check_pi1()
    P.build(CH, M, PP, P.THESE_M, show=len(sys.argv) > 1)
