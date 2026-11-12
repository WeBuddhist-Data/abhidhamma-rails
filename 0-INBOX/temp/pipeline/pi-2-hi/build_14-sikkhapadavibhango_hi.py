# -*- coding: utf-8 -*-
"""pi-2 chapter 14 (Sikkhāpadavibhaṅga), Hindi plain zero-shot.  usage: python -I -X utf8 build_14-sikkhapadavibhango_hi.py"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
from hz_3_14_15_common import (S, DASH, build, KAMA_KUSALA, SOM_NS, CITTA8, CITTA8_REST, UPE_NV_SAS, ADHI_CHAIN3,
                               ADHI_CHAIN4, OBJ_PE, PHASSA_PE, RUPU, LOKUTTARA, panha_line, question, TIKA, DUKA)

CH = "14-sikkhapadavibhango.md"
ABST = {  # what one abstains from (pi-5 / pi-4 wording)
    "pana": "जीव-हत्या",
    "adinna": "बिना दी गई चीज़ लेने",
    "kama": "इंद्रिय-सुखों में दुराचार",
    "musa": "झूठ बोलने",
    "sura": "लापरवाही का कारण बनने वाली शराब, मदिरा और नशीली चीज़ों",
}
SP = {k: f"{v} से दूर रहने का प्रशिक्षण-नियम" for k, v in ABST.items()}   # <X>ā veramaṇī sikkhāpadaṃ
LIST5 = f"पाँच प्रशिक्षण-नियम {DASH} " + ", ".join(SP.values()) + "।"     # Pañca sikkhāpadāni – ...
OTHERS4 = "… ".join(SP[k] for k in ("adinna", "kama", "musa", "sura"))       # adinnādānā …pe… surāmeraya... sikkhāpadaṃ


def q(k):
    return f"यहाँ {SP[k]} क्या है?"


def when(k, types):
    """Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti <types> <X>ā viramantassa,"""
    return f"जिस समय {ABST[k]} से दूर रहने वाले व्यक्ति में {KAMA_KUSALA}, जो {types} होता है,"


def virati(k):  # yā tasmiṃ samaye <X>ā ārati virati paṭivirati veramaṇī ... setughāto (pi-1 ^1-299)
    return (f"उस समय जो {ABST[k]} से दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, "
            f"दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना है")


CETANA = "उस समय जो इरादा, इरादा करना, इरादा कर चुका होना है"      # yā tasmiṃ samaye cetanā sañcetanā sañcetayitattaṃ
PHASSA = "उस समय जो संपर्क… तत्परता, भटकाव का अभाव है"            # yo tasmiṃ samaye phasso…pe… paggāho avikkhepo
PHASSA_BARE = "संपर्क… तत्परता, भटकाव का अभाव"                     # phasso…pe… paggāho avikkhepo
REST_V = "शेष परिघटनाएँ दूर रहने से जुड़ी हैं।"                       # Avasesā dhammā veramaṇiyā sampayuttā.
REST_C = "शेष परिघटनाएँ इरादे से जुड़ी हैं।"                         # Avasesā dhammā cetanāya sampayuttā.


def called(k):
    return f"{DASH} यह “{SP[k]}” कहा जाता है।"


def tail3(k):  # Avasesā ... veramaṇiyā sampayuttā…pe… avasesā ... cetanāya sampayuttā…pe… phasso…pe… paggāho avikkhepo – idaṃ vuccati
    return f"{REST_V[:-1]}… {REST_C[:-1]}… {PHASSA_BARE} {called(k)}"


HINA4 = "प्रसन्नता के साथ होने वाला, ज्ञान से जुड़ा और " + ADHI_CHAIN4                  # pi-1 ^1-269
CITTA8_HINA3 = "… ".join(CITTA8_REST[:-1] + ["समभाव के साथ होने वाला, ज्ञान से अलग, प्रेरणा सहित और " + ADHI_CHAIN3])  # pi-1 2-02:162
SIKKHA_Q = "कौन-सी परिघटनाएँ प्रशिक्षण हैं?"                       # Katame dhammā sikkhā?
SIKKHA_A = "ये परिघटनाएँ प्रशिक्षण हैं।"                             # Ime dhammā sikkhā.
LOK_REST = LOKUTTARA[len("जिस समय कोई "):]
ARUPU_SHORT = "अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है"

# Pañhāpucchaka: punctuation fixes for parsing only (reported): "Na hetū sahetukā" = na hetū, sahetukā
PANHA_FIX = {"Na hetū sahetukā, hetusampayuttā.": "Na hetū, sahetukā, hetusampayuttā."}


def panha(pali_line):
    for a, b in PANHA_FIX.items():
        pali_line = pali_line.replace(a, b)
    return panha_line(pali_line)


def lines(pali):
    P = [l for l in pali if l.strip()]
    nid = lambda i: S.ID.sub("", P[i]).strip()
    H = [
        "### " + S.CHAPTER_TITLES[14],
        "#### " + S.SECTION_TITLES["Abhidhammabhājanīyaṃ"],
        LIST5,
        f"{q('pana')} {when('pana', SOM_NS)} {virati('pana')} {called('pana')} {REST_V}",
        f"{q('pana')} {when('pana', SOM_NS)} {CETANA} {called('pana')} {REST_C}",
        f"{q('pana')} {when('pana', SOM_NS)} {PHASSA} {called('pana')}",
        f"{q('pana')} {when('pana', CITTA8)} {virati('pana')} {called('pana')} {REST_V}",
        f"{q('pana')} {when('pana', UPE_NV_SAS)} {CETANA} {called('pana')} {REST_C}",
        f"{q('pana')} {when('pana', UPE_NV_SAS)} {PHASSA_BARE} {called('pana')}",           # Pāli lacks "yo tasmiṃ samaye"
        f"यहाँ {OTHERS4} क्या है? {when('sura', SOM_NS)} {virati('sura')} {called('sura')} {REST_V}",
        f"यहाँ {SP['sura']} क्या है, {when('sura', SOM_NS)} {CETANA} {called('sura')} {REST_C}",  # Pāli: "sikkhāpadaṃ, yasmiṃ"
        f"{q('sura')} {when('sura', SOM_NS)} {PHASSA} {called('sura')}",
        f"{q('sura')} {when('sura', CITTA8)} {virati('sura')} {called('sura')} {REST_V}",
        f"{q('sura')} {when('sura', UPE_NV_SAS)} {CETANA} {called('sura')} {REST_C}",
        f"{q('sura')} {when('sura', UPE_NV_SAS)} {PHASSA} {called('sura')}",
        LIST5,
        f"{q('pana')} {when('pana', HINA4)} {virati('pana')} {called('pana')} {REST_V}",
        f"{q('pana')} {when('pana', HINA4)} {CETANA} {called('pana')} {REST_C}",
        f"{q('pana')} {when('pana', HINA4)} {PHASSA} {called('pana')}",
        f"{q('pana')} {when('pana', CITTA8_HINA3)} {virati('pana')} {called('pana')} {tail3('pana')}",
        f"यहाँ {OTHERS4} क्या है? {when('sura', HINA4)} {virati('sura')} {called('sura')} {tail3('sura')}",
        f"{q('sura')} {when('sura', CITTA8_HINA3)} {virati('sura')} {called('sura')} {tail3('sura')}",
        f"{SIKKHA_Q} जिस समय {KAMA_KUSALA}, जो {SOM_NS} होता है {OBJ_PE}, {PHASSA_PE}। {SIKKHA_A}",
        f"{SIKKHA_Q} जिस समय {KAMA_KUSALA}, जो {CITTA8} होता है {OBJ_PE}, {PHASSA_PE}। {SIKKHA_A}",
        f"{SIKKHA_Q} {RUPU}… {ARUPU_SHORT}… {LOK_REST}, {PHASSA_PE}। {SIKKHA_A}",
        S.SECTION_TITLES["Abhidhammabhājanīyaṃ"] + "।",
        "#### " + S.SECTION_TITLES["Pañhāpucchakaṃ"],
        LIST5,
        question("पाँच प्रशिक्षण-नियमों"),
        TIKA,
        panha(nid(30)),
        panha(nid(31)),
        DUKA,
        panha(nid(33)),
        panha(nid(34)),
        panha(nid(35)),
        S.SECTION_TITLES["Pañhāpucchakaṃ"] + "।",
        S.CHAPTER_TITLES[14] + " पूरा हुआ।",
    ]
    return H


if __name__ == "__main__":
    import os
    pali = open(os.path.join(S.PALI_DIR, CH), encoding="utf-8-sig").read().splitlines()
    P = [l for l in pali if l.strip()]
    assert P[30].startswith("Kusalāyeva") and P[33].startswith("Na hetū") and P[36] == "Pañhāpucchakaṃ.", "line map"
    build(CH, lines(pali))
