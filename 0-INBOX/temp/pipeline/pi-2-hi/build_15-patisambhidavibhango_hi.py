# -*- coding: utf-8 -*-
"""pi-2 chapter 15 (Paṭisambhidāvibhaṅga), Hindi plain zero-shot.  usage: python -I -X utf8 build_15-patisambhidavibhango_hi.py"""
import os, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import hz_3_14_15_common as C
from hz_3_14_15_common import (S, DASH, build, KAMA_KUSALA, SOM_NS, CITTA8, CITTA8_REST, OBJ_PE, OBJ_PE_5, PHASSA_PE,
                               RUPU, ARUPU, VIVICCA_JH1, PATHAVI_KASINA, NEVASANNA, LOKUTTARA, ARISEN_FORMLESS,
                               hoti_list, panha_line, question, TIKA, DUKA)

CH = "15-patisambhidavibhango.md"
PS = {
    "attha": "अर्थ का विश्लेषणात्मक ज्ञान",
    "dhamma": "परिघटनाओं का विश्लेषणात्मक ज्ञान",     # dhamma = परिघटना (core rule)
    "nirutti": "भाषा का विश्लेषणात्मक ज्ञान",
    "patibhana": "सूझ-बूझ का विश्लेषणात्मक ज्ञान",
}
VAR_PATIBHANA = "[वर्तनी-भेद (Syā.): paṭibhāṇapaṭisambhidā, आगे भी इसी तरह]"
FOUR = f"चार विश्लेषणात्मक ज्ञान {DASH} " + ", ".join(PS.values())            # Catasso paṭisambhidā – ...
THREE = f"तीन विश्लेषणात्मक ज्ञान {DASH} " + ", ".join(PS[k] for k in ("attha", "nirutti", "patibhana"))
NIRUTTI = f"वहाँ परिघटनाओं की भाषा की अभिव्यक्ति का ज्ञान {PS['nirutti']} है"      # tatra dhammaniruttābhilāpe ñāṇaṃ niruttipaṭisambhidā
PATIBHANA = f"ज्ञानों का ज्ञान {PS['patibhana']} है"                               # ñāṇesu ñāṇaṃ paṭibhānapaṭisambhidā


def kn(x, k):
    """<X>-e ñāṇaṃ <k>paṭisambhidā -> '<X> का ज्ञान <name> है'"""
    return f"{x} का ज्ञान {PS[k]} है"


def truths(x, gen_f):
    """X / X-samudaya / X-nirodha / X-nirodhagāminī paṭipadā (pi-1 ^1-1067 wording)."""
    return ", ".join([kn(x, "attha"), f"{x} {gen_f} उत्पत्ति का ज्ञान {PS['dhamma']} है",
                      f"{x} के अंत का ज्ञान {PS['attha']} है",
                      f"{x} के अंत की ओर ले जाने वाले प्रगति के ढंग का ज्ञान {PS['dhamma']} है"])


def vara(name):
    return f"यह {name} का खंड है।"


JATA = ", ".join(S.SYN_PACCUPPANNA["f"].split(", ")[:6])   # jātā bhūtā sañjātā nibbattā abhinibbattā pātubhūtā
NAVANGA = ("उपदेश, गद्य-पद्य मिश्रित उपदेश, व्याख्याएँ, पद्य, प्रेरित उद्गार, उद्धृत वचन, पूर्व जन्मों की कथाएँ, "
           "अद्भुत घटनाओं के वर्णन और प्रश्नोत्तर")                              # pi-4 ^4-… (dhammaṃ pariyāpuṇāti)
JOTAKA = f"जिस ज्ञान से कोई उन ज्ञानों को जानता है {DASH} “ये ज्ञान इस अर्थ को प्रकाशित करने वाले हैं”, {PATIBHANA}।"
NAMING = "जिस भाषा से उन परिघटनाओं का नामकरण होता है"                          # yāya niruttiyā tesaṃ dhammānaṃ paññatti hoti
DHAMMA_KN = f"इन परिघटनाओं का ज्ञान {PS['dhamma']} है"
VIPAKA_KN = f"उनके कर्म-फल का ज्ञान {PS['attha']} है"
ABH_TAIL_C = f"{DHAMMA_KN}। {VIPAKA_KN}, {NAMING}, {NIRUTTI}। {JOTAKA}"           # ^2-725 (comma version)
ABH_TAIL = f"{DHAMMA_KN}। {VIPAKA_KN}। {NAMING}, {NIRUTTI}। {JOTAKA}"
VIP_TAIL = f"इन परिघटनाओं का ज्ञान {PS['attha']} है। {NAMING}, {NIRUTTI}। {JOTAKA}"

KQ = "हितकर परिघटनाएँ कौन-सी हैं?"
AQ = "हानिकर परिघटनाएँ कौन-सी हैं?"
NQ = "नैतिक रूप से अनिर्धारित परिघटनाएँ कौन-सी हैं?"
KA = "ये हितकर परिघटनाएँ हैं।"
AA = "ये हानिकर परिघटनाएँ हैं।"
NA = "ये नैतिक रूप से अनिर्धारित परिघटनाएँ हैं।"

DITTHI = [  # the twelve unwholesome types (pi-1 2-04)
    "प्रसन्नता के साथ होने वाला और ग़लत दृष्टि से जुड़ा",
    "प्रसन्नता के साथ होने वाला, ग़लत दृष्टि से जुड़ा और प्रेरणा सहित",
    "प्रसन्नता के साथ होने वाला और ग़लत दृष्टि से अलग",
    "प्रसन्नता के साथ होने वाला, ग़लत दृष्टि से अलग और प्रेरणा सहित",
    "समभाव के साथ होने वाला और ग़लत दृष्टि से जुड़ा",
    "समभाव के साथ होने वाला, ग़लत दृष्टि से जुड़ा और प्रेरणा सहित",
    "समभाव के साथ होने वाला और ग़लत दृष्टि से अलग",
    "समभाव के साथ होने वाला, ग़लत दृष्टि से अलग और प्रेरणा सहित",
    "उदासी के साथ होने वाला और चिढ़ से जुड़ा",
    "उदासी के साथ होने वाला, चिढ़ से जुड़ा और प्रेरणा सहित",
    "समभाव के साथ होने वाला और संशय से जुड़ा",
    "समभाव के साथ होने वाला और बेचैनी से जुड़ा",
]
AKUSALA_ARISES = "जिस समय हानिकर मन उत्पन्न होता है"
KUS_KAMMA = "जिस समय इंद्रिय-सुखों के लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण कर्म के फल रूपी"
AKUS_KAMMA = "जिस समय हानिकर कर्म किए जाने और संचित होने के कारण कर्म के फल रूपी"
KIRIYA = "जो केवल क्रिया रूपी है, न हितकर, न हानिकर, न ही कर्म-फल"
BASE10 = ["phasso", "vedanā", "saññā", "cetanā", "cittaṃ"]
MANO_UPE = BASE10 + ["vitakko", "vicāro", "upekkhā", "cittassekaggatā", "manindriyaṃ", "upekkhindriyaṃ", "jīvitindriyaṃ"]
MANO_SOM = BASE10 + ["vitakko", "vicāro", "pīti", "sukhaṃ", "cittassekaggatā", "manindriyaṃ", "somanassindriyaṃ", "jīvitindriyaṃ"]


def at_time(items):
    return f"उस समय {hoti_list(items)}, {ARISEN_FORMLESS}।"


C.BRACKETS[1] = "[पाठभेद (Sī.): āsavā; पर “तत्वों का विश्लेषण” अध्याय में पाठ में कोई अंतर नहीं है]"
BR_PALI = " [āsavā (sī.) dhātuvibhaṅge pana pāṭhanānattaṃ natthi]"


def panha(pali_line):
    # "kenaci viññeyyā, kenaci na viññeyyā" speak of all four again, not of atthapaṭisambhidā alone
    pali_line = pali_line.replace("siyā lokuttarā, kenaci viññeyyā", "siyā lokuttarā, ⟦R⟧kenaci viññeyyā")
    return panha_line(pali_line.replace(BR_PALI, "⟦1⟧"))


def lines(P):
    nid = lambda i: S.ID.sub("", P[i]).strip()
    H = ["### " + S.CHAPTER_TITLES[15], "#### " + S.SECTION_TITLES["Suttantabhājanīyaṃ"]]
    four_tail = f"{NIRUTTI}, {PATIBHANA}।"
    H += [
        "##### सारांश का खंड",
        (f"{FOUR} {VAR_PATIBHANA}। {kn('अर्थ', 'attha')}, {kn('परिघटनाओं', 'dhamma')}, " + four_tail + " " + vara("सारांश")),
        "##### सत्यों का खंड",
        f"{FOUR}। {truths('दुःख', 'की')}, {four_tail} {vara('सत्यों')}",
        "##### कारण का खंड",
        f"{FOUR}। {kn('कारण', 'dhamma')}, {kn('कारण के फल', 'attha')}, {four_tail} {vara('कारण')}",
        "##### परिघटनाओं का खंड",
        (f"{FOUR}। जो परिघटनाएँ {JATA} हैं, इन परिघटनाओं का ज्ञान {PS['attha']} है; "
         f"जिस परिघटना से वे परिघटनाएँ {JATA} हैं, उन परिघटनाओं का ज्ञान {PS['dhamma']} है; "
         f"{NIRUTTI}; {PATIBHANA}। {vara('परिघटनाओं')}"),
        "##### परस्पर-आश्रित उत्पत्ति का खंड",
        f"{FOUR}। {truths('बुढ़ापे और मृत्यु', 'की')}, {four_tail}",
        (f"{FOUR}। जन्म का ज्ञान… अस्तित्व का ज्ञान… आसक्ति का ज्ञान… तृष्णा का ज्ञान… अनुभूति का ज्ञान… संपर्क का ज्ञान… "
         f"छह इंद्रिय-क्षेत्रों का ज्ञान… मानसिक पक्ष और भौतिक रूप का ज्ञान… चेतना का ज्ञान… "
         f"{truths('मानसिक रचनाओं', 'की')}, {four_tail} {vara('परस्पर-आश्रित उत्पत्ति')}"),
        "##### शिक्षा के अध्ययन का खंड",
        f"{FOUR}।",
        (f"यहाँ {PS['dhamma']} क्या है? यहाँ भिक्षु शिक्षा को जानता है {DASH} {NAVANGA}। यह “{PS['dhamma']}” कहा जाता है। "
         f"वह उस-उस कथन का अर्थ जानता है {DASH} “यह इस कथन का अर्थ है, यह इस कथन का अर्थ है”। "
         f"यह “{PS['attha']}” कहा जाता है। {NIRUTTI}। {PATIBHANA}। {vara('शिक्षा के अध्ययन')}"),
        S.SECTION_TITLES["Suttantabhājanīyaṃ"] + "।",
        "#### " + S.SECTION_TITLES["Abhidhammabhājanīyaṃ"],
        "##### हितकर परिघटनाओं का खंड",
        f"{FOUR}।",
        f"{KQ} जिस समय {KAMA_KUSALA}, जो {SOM_NS} होता है {OBJ_PE}, {PHASSA_PE}, {KA[:-1]}। {ABH_TAIL_C}",
        f"{FOUR}।",
        f"{KQ} जिस समय {KAMA_KUSALA}, जो {CITTA8} होता है {OBJ_PE}, {PHASSA_PE}। {KA} {ABH_TAIL}",
        f"{FOUR}।",
        f"{KQ} {RUPU}, {VIVICCA_JH1}, {PATHAVI_KASINA}, {PHASSA_PE}। {KA} {ABH_TAIL}",
        f"{FOUR}।",
        f"{KQ} {ARUPU}, {NEVASANNA}, {PHASSA_PE}। {KA} {ABH_TAIL}",
        f"{FOUR}।",
        f"{KQ} {LOKUTTARA}, {PHASSA_PE}। {KA} {ABH_TAIL}",
        "##### हानिकर परिघटनाओं का खंड",
        f"{FOUR}।",
        f"{AQ} {AKUSALA_ARISES}, जो {DITTHI[0]} होता है {OBJ_PE}, {PHASSA_PE}। {AA} {ABH_TAIL}",
        f"{FOUR}।",
        f"{AQ} {AKUSALA_ARISES}, जो {'… '.join(DITTHI[1:])} होता है {OBJ_PE}, {PHASSA_PE}। {AA} {ABH_TAIL}",
        "##### कर्म-फल का खंड",
        f"{THREE}।",
        (f"{NQ} {KUS_KAMMA} आँख की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली है और जिसका विषय दृश्य रूप होता है, "
         f"{at_time(BASE10 + ['upekkhā', 'cittassekaggatā', 'manindriyaṃ', 'upekkhindriyaṃ', 'jīvitindriyaṃ'])} {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} {KUS_KAMMA} कान की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली है और जिसका विषय ध्वनि होती है… "
         f"नाक की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली है और जिसका विषय गंध होती है… "
         f"जीभ की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली है और जिसका विषय स्वाद होता है… "
         f"शरीर की चेतना उत्पन्न होती है, जो सुख के साथ होने वाली है और जिसका विषय स्पर्श होता है, "
         f"{at_time(BASE10 + ['sukhaṃ', 'cittassekaggatā', 'manindriyaṃ', 'sukhindriyaṃ', 'jīvitindriyaṃ'])} {NA} {VIP_TAIL}"),
        (f"{THREE}। {NQ} {KUS_KAMMA} मन का तत्व उत्पन्न होता है, जो समभाव के साथ होने वाला है {OBJ_PE_5}, "
         f"{at_time(MANO_UPE)} {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} {KUS_KAMMA} मन की चेतना का तत्व उत्पन्न होता है, जो प्रसन्नता के साथ होने वाला है {OBJ_PE}, "
         f"{at_time(MANO_SOM)} {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} {KUS_KAMMA} मन की चेतना का तत्व उत्पन्न होता है, जो समभाव के साथ होने वाला है {OBJ_PE}, "
         f"{at_time(MANO_UPE)} {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} {KUS_KAMMA} मन की चेतना का तत्व उत्पन्न होता है, "
         + "… ".join(f"जो {t} होता है" for t in [SOM_NS] + CITTA8_REST)
         + f" {OBJ_PE}, {PHASSA_PE}। {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} {RUPU}, {VIVICCA_JH1}, {PATHAVI_KASINA}, {PHASSA_PE}। {KA} "
         f"उसी सूक्ष्म भौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण जिस समय वह इंद्रिय-सुखों से अलग होकर… "
         f"कर्म के फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है, {PATHAVI_KASINA}, {PHASSA_PE}। {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} {ARUPU}, {NEVASANNA}, {PHASSA_PE}। {KA} "
         f"उसी अभौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण जिस समय वह कुछ भी न होने के क्षेत्र को "
         f"पूरी तरह पार करके, सुख को छोड़ने से… कर्म के फल रूपी और न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाले "
         f"चौथे ध्यान को प्राप्त करके उसमें रहता है, {PHASSA_PE}। {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} {LOKUTTARA}, {PHASSA_PE}। {KA} "
         f"उसी लोकोत्तर हितकर कर्म के किए जाने और अभ्यास किए जाने के कारण जिस समय वह इंद्रिय-सुखों से अलग होकर… "
         f"कर्म के फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला और शून्य होता है, "
         f"{PHASSA_PE}। {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} {AKUS_KAMMA} आँख की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली है और जिसका विषय दृश्य रूप है… "
         f"कान की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली है और जिसका विषय ध्वनि है… "
         f"नाक की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली है और जिसका विषय गंध है… "
         f"जीभ की चेतना उत्पन्न होती है, जो समभाव के साथ होने वाली है और जिसका विषय स्वाद है… "
         f"शरीर की चेतना उत्पन्न होती है, जो दुःख के साथ होने वाली है और जिसका विषय स्पर्श है, "
         f"{at_time(BASE10 + ['dukkhaṃ', 'cittassekaggatā', 'manindriyaṃ', 'dukkhindriyaṃ', 'jīvitindriyaṃ'])} {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} {AKUS_KAMMA} मन का तत्व उत्पन्न होता है, जो समभाव के साथ होने वाला है और जिसका विषय दृश्य रूप हो… या स्पर्श… "
         f"मन की चेतना का तत्व उत्पन्न होता है, जो समभाव के साथ होने वाला है {OBJ_PE}, {at_time(MANO_UPE)} {NA} {VIP_TAIL}"),
        "##### केवल क्रिया का खंड",
        f"{THREE}।",
        (f"{NQ} जिस समय मन का तत्व उत्पन्न होता है, {KIRIYA}, जो समभाव के साथ होने वाला है {OBJ_PE_5}, "
         f"{at_time(MANO_UPE)} {NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} जिस समय मन की चेतना का तत्व उत्पन्न होता है, {KIRIYA}, जो प्रसन्नता के साथ होने वाला है और जिसका विषय "
         f"दृश्य रूप हो… या मन का विषय… मन की चेतना का तत्व उत्पन्न होता है, {KIRIYA}, जो समभाव के साथ होने वाला है {OBJ_PE}, "
         f"{at_time(BASE10 + ['vitakko', 'vicāro', 'upekkhā', 'cittassekaggatā', 'vīriyindriyaṃ', 'samādhindriyaṃ', 'manindriyaṃ', 'upekkhindriyaṃ', 'jīvitindriyaṃ'])} "
         f"{NA} {VIP_TAIL}"),
        f"{THREE}।",
        (f"{NQ} जिस समय मन की चेतना का तत्व उत्पन्न होता है, {KIRIYA}, जो {SOM_NS} होता है… "
         + "… ".join(f"{t} होता है" for t in CITTA8_REST)
         + f"… कोई सूक्ष्म भौतिक लोक से संबंधित ध्यान का अभ्यास करता है… अभौतिक लोक से संबंधित ध्यान का अभ्यास करता है, {KIRIYA}, "
         f"जो इसी जीवन में सुख से रहने के लिए होता है… {NEVASANNA}, {PHASSA_PE}। {NA} {VIP_TAIL}"),
        (f"{FOUR}। तीन विश्लेषणात्मक ज्ञान इंद्रिय-सुखों के लोक से संबंधित हितकर मन की ज्ञान से जुड़ी चार उत्पत्तियों में, "
         f"और केवल क्रिया रूपी मन की ज्ञान से जुड़ी चार उत्पत्तियों में उत्पन्न होते हैं। "
         f"{PS['attha']} इनमें भी उत्पन्न होता है, और चार मार्गों और चार फलों में भी उत्पन्न होता है।"),
        S.SECTION_TITLES["Abhidhammabhājanīyaṃ"] + "।",
        "#### " + S.SECTION_TITLES["Pañhāpucchakaṃ"],
        f"{FOUR}।",
        question("चार विश्लेषणात्मक ज्ञानों"),
        TIKA,
    ]
    k = len(H)
    assert P[k - 1].startswith("##### Tikaṃ"), P[k - 1]
    H += [panha(nid(k + j)) for j in range(6)]
    H.append(DUKA)
    assert P[k + 6].startswith("##### Dukaṃ"), P[k + 6]
    H += [panha(nid(k + 7 + j)) for j in range(5)]
    H += [S.SECTION_TITLES["Pañhāpucchakaṃ"] + "।", S.CHAPTER_TITLES[15] + " पूरा हुआ।"]
    return H


if __name__ == "__main__":
    pali = open(os.path.join(S.PALI_DIR, CH), encoding="utf-8-sig").read().splitlines()
    P = [l for l in pali if l.strip()]
    build(CH, lines(P))
