# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, chapter 2 (Āyatanavibhaṅga), Hindi plain zero-shot.

usage: python -I -X utf8 build_ayatanavibhango_hi.py
Writes AI_translation\\hindi\\pi-2-hindi-plain-zeroshot_split_chapters\\2-ayatanavibhango.md
Block IDs are copied from the Pāli at build time. The sense-base definitions are the reviewed pi-1 Hindi
(^1-596 … ^1-647) with only the question/closing frame changed; the Pañhāpucchaka is assembled by
matrix_ch2_ch4_hi from the pi-1 matrix strings.
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
from common_ch2_ch4_hi import S, DASH, pi1, sub1, check_in_pi, write_chapter, pali_lines, strip_id
import matrix_ch2_ch4_hi as M
import subjects_ch2_ch4_hi as SJ

NAME = "2-ayatanavibhango.md"
K = "इंद्रिय-क्षेत्र"

# ---------------------------------------------------------------- the twelve bases (pi-1 ^1-1342 / pi-4 ^4-M-3)
INNER = ["आँख", "कान", "नाक", "जीभ", "शरीर", "मन"]
OUTER = ["दृश्य रूप", "ध्वनि", "गंध", "स्वाद", "स्पर्श", "मन के विषयों"]
BASE = {w: f"{w} का {K}" for w in INNER + OUTER}
SUTTANTA_ORDER = [BASE[x] for pair in zip(INNER, OUTER) for x in pair]
ABHIDHAMMA_ORDER = [BASE[x] for x in INNER + OUTER]
TWELVE = "बारह " + K
LIST_SUTTANTA = f"{TWELVE} {DASH} " + ", ".join(SUTTANTA_ORDER) + "।"
LIST_ABHIDHAMMA = f"{TWELVE} {DASH} " + ", ".join(ABHIDHAMMA_ORDER) + "।"

# ---------------------------------------------------------------- impermanence line (^2-154)
# (subject, gender, plural)
ANICCA_ITEMS = [("आँख", "f", False), ("दृश्य रूप", "m", True), ("कान", "m", False), ("ध्वनियाँ", "f", True),
                ("नाक", "f", False), ("गंध", "f", True), ("जीभ", "f", False), ("स्वाद", "m", True),
                ("शरीर", "m", False), ("स्पर्श", "m", True), ("मन", "m", False), ("मन के विषय", "m", True)]


def anicca(subj, g, pl):
    """X aniccaṃ dukkhaṃ anattā vipariṇāmadhammaṃ."""
    c = "हैं" if pl else "है"
    v = "वाली" if g == "f" else ("वाले" if pl else "वाला")
    return f"{subj} अनित्य {c}, दुःख {c}, आत्मा से रहित {c}, बदल जाने {v} {c}।"


# ---------------------------------------------------------------- sense-base definitions from pi-1
def frame(line, x):
    """pi-1 'कौन-सा भौतिक रूप X है? … – यह भौतिक रूप X है।' -> 'यहाँ X क्या है? … । यह “X” कहा जाता है।'"""
    line = sub1(line, f"कौन-सा भौतिक रूप {x} है? ", f"यहाँ {x} क्या है? ")
    return sub1(line, f" {DASH} यह भौतिक रूप {x} है।", f"। यह “{x}” कहा जाता है।")


def base_defs():
    d = {}
    l = frame(pi1("1-596"), BASE["आँख"])
    d["cakkhu"] = sub1(l, "[वर्तनी-भेद (Sī., Syā.): cakkhuṃ]",
                       "[वर्तनी-भेद (Sī., Syā., Ka.): cakkhuṃ; परिघटनाओं की गणना 596-599]")
    d["sota"] = frame(pi1("1-600"), BASE["कान"])
    d["ghana"] = frame(pi1("1-604"), BASE["नाक"])
    d["jivha"] = frame(pi1("1-608"), BASE["जीभ"])
    d["kaya"] = frame(pi1("1-612"), BASE["शरीर"])
    l = frame(pi1("1-616"), BASE["दृश्य रूप"])
    l = sub1(l, "नीला, पीला, लाल,", "नीला, पीला, लाल [वर्तनी-भेद (Sī.): pītaṃ lohitaṃ],")
    l = sub1(l, "चौकोर [वर्तनी-भेद (Sī., Ka.): caturassaṃ],", "चौकोर,")
    l = sub1(l, "[वर्तनी-भेद (Sī., Syā.): suriyamaṇḍalassa]", "[वर्तनी-भेद (Sī., Syā., Kaṃ.): suriyamaṇḍalassa]")
    d["rupa"] = l
    l = frame(pi1("1-620"), BASE["ध्वनि"])
    d["sadda"] = sub1(l, "मृदंग की ध्वनि,", "मृदंग की ध्वनि [वर्तनी-भेद (Sī.): mutiṅgasaddho],")
    d["gandha"] = frame(pi1("1-624"), BASE["गंध"])
    l = frame(pi1("1-628"), BASE["स्वाद"])
    d["rasa"] = sub1(l, "नमकीन, खारा, हल्का खट्टा [पाठभेद (Sī.): lapilakaṃ],",
                     "नमकीन [पाठभेद: lapilakaṃ (Sī.), lampikaṃ (Ka., Sī.)], खारा, हल्का खट्टा,")
    d["photthabba"] = frame(pi1("1-647"), BASE["स्पर्श"])
    return d


# ---------------------------------------------------------------- Abhidhammabhājanīya classification frames
MANA = BASE["मन"]
DHAMMA = BASE["मन के विषयों"]


def cls(n, subj):
    return f"{S.NUM_WORDS[n]} प्रकार से {subj} {DASH}"


def cls_close(n, subj):
    word = "अनेक" if n == "bahu" else S.NUM_WORDS[n]
    return f"इस तरह {word} प्रकार से {subj} बताया गया।"


def atthi(*xs):
    """atthi X, atthi Y … (masc. subject: इंद्रिय-क्षेत्र / समूह) -> कुछ X है, कुछ Y है"""
    return ", ".join(f"कुछ {x} है" for x in xs)


def jisme(*xs, g="f"):
    """'…viññāṇaṃ atthi X, atthi Y' attached to a list member -> 'जिसमें कुछ X है, कुछ Y है' (pi-1 ^1-590 pattern)"""
    return "जिसमें " + ", ".join(f"कुछ {x} है" for x in xs)


PHASSA_SAMP = "संपर्क से जुड़ा है"         # phassasampayuttaṃ / phassasampayutto (terms file; «है» as in chapter 1)
CITTA_SAMP = "मन से जुड़ा है"             # cittasampayutto
SAHETUKA = ("मूल वाला", "मूल से रहित")    # atthi sahetuko, atthi ahetuko (terms file)
KUSALA3 = ("हितकर", "हानिकर", "नैतिक रूप से अनिर्धारित")
BHUMI4 = ("इंद्रिय-सुखों के लोक से संबंधित", "सूक्ष्म भौतिक लोक से संबंधित", "अभौतिक लोक से संबंधित",
          "अस्तित्व के लोकों में न समाया हुआ")
FAC5 = tuple(f"{x} की क्षमता से जुड़ा" for x in ("सुख", "दुःख", "प्रसन्नता", "उदासी", "समभाव"))
VED3 = ("सुखद अनुभूति से जुड़ा", "दुःखद अनुभूति से जुड़ा", "न दुःखद, न सुखद अनुभूति से जुड़ा")
V5 = [f"{c} की चेतना" for c in ("आँख", "कान", "नाक", "जीभ", "शरीर")]
MANODHATU, MANOVINNANADHATU = "मन का तत्व", "मन की चेतना का तत्व"
SUKHADUKKHA = jisme("सुख के साथ होने वाली", "दुःख के साथ होने वाली")
KUSALA_IN = jisme(*KUSALA3)


def mana_lines():
    six = S.MEMBERS["vinnana"]                                   # आँख की चेतना … और मन की चेतना
    v5 = ", ".join(V5)
    L = [
        f"यहाँ {MANA} क्या है? {cls(1, MANA)} {PHASSA_SAMP}।",
        f"{cls(2, MANA)} {atthi(*SAHETUKA)}।",
        f"{cls(3, MANA)} {atthi(*KUSALA3)}।",
        f"{cls(4, MANA)} {atthi(*BHUMI4)}।",
        f"{cls(5, MANA)} {atthi(*FAC5)}।",
        f"{cls(6, MANA)} {six}। {cls_close(6, MANA)}",
        f"{cls(7, MANA)} {v5}, {MANODHATU} और {MANOVINNANADHATU}। {cls_close(7, MANA)}",
        f"{cls(8, MANA)} {v5}, {SUKHADUKKHA}, {MANODHATU} और {MANOVINNANADHATU}। {cls_close(8, MANA)}",
        f"{cls(9, MANA)} {v5}, {MANODHATU} और {MANOVINNANADHATU}, {KUSALA_IN}। {cls_close(9, MANA)}",
        f"{cls(10, MANA)} {v5}, {SUKHADUKKHA}, {MANODHATU} और {MANOVINNANADHATU}, {KUSALA_IN}। {cls_close(10, MANA)}",
        f"{cls(1, MANA)} {PHASSA_SAMP}।",
        f"{cls(2, MANA)} {atthi(*SAHETUKA)}।",
        f"{cls(3, MANA)} {atthi(*VED3)}…। {cls_close('bahu', MANA)} यह “{MANA}” कहा जाता है।",
    ]
    return L


def khandha_line(a, one, two):
    """Tattha katamo vedanākkhandho? Ekavidhena … – phassasampayutto. Duvidhena … – atthi …, atthi …
    Tividhena … – atthi kusalo, atthi akusalo, atthi abyākato…pe… evaṃ dasavidhena …pe… evaṃ bahuvidhena … Ayaṃ vuccati "…"."""
    k = S.AGG[a]["khandha"]
    return (f"{S.khandha_question(a)} {cls(1, k)} {one}। {cls(2, k)} {atthi(*two)}। {cls(3, k)} {atthi(*KUSALA3)}… "
            f"{cls_close(10, k)[:-1]}… {cls_close('bahu', k)} यह “{k}” कहा जाता है।")


IN_DHAMMAYATANA = f"मन के विषयों के {K} में समाया हुआ"                                                     # pi-1 ^1-593
RUPA_DHAMMAYATANA = f"दिखाई न देने वाला और टकराव से रहित है और {IN_DHAMMAYATANA} है"                    # pi-1 ^1-593
ASANKHATA_DHATU = "अनिर्मित तत्व"                                                                        # pi-1 ^1-583


def dhamma_lines():
    return [
        (f"यहाँ {DHAMMA} क्या है? {S.AGG['vedana']['khandha']}, {S.AGG['sanna']['khandha']}, "
         f"{S.AGG['sankhara']['khandha']}, वह भौतिक रूप जो {RUPA_DHAMMAYATANA}, और {ASANKHATA_DHATU}।"),
        khandha_line("vedana", PHASSA_SAMP, SAHETUKA),
        khandha_line("sanna", PHASSA_SAMP, SAHETUKA),
        khandha_line("sankhara", CITTA_SAMP, ("मूल रूपी", "मूल रूपी न होने वाला")),   # as in chapter 1
        (f"यहाँ कौन-सा भौतिक रूप {RUPA_DHAMMAYATANA}? स्त्रीत्व की क्षमता, पुरुषत्व की क्षमता… कौर-कौर खाया जाने वाला भोजन। "
         f"यह भौतिक रूप “दिखाई न देने वाला और टकराव से रहित, {IN_DHAMMAYATANA}” कहा जाता है।"),
        f"यहाँ {ASANKHATA_DHATU} क्या है? राग का क्षय, द्वेष का क्षय, मोह का क्षय {DASH} यह “{ASANKHATA_DHATU}” कहा जाता है।",
        f"यह {DHAMMA} कहा जाता है।",
        S.SECTION_TITLES["Abhidhammabhājanīyaṃ"] + "।",
    ]


# ---------------------------------------------------------------- Pañhāpucchaka
TIKA_HEADING = "तीन-तीन के वर्गीकरण"   # pi-1 tika = तीन-तीन के वर्गीकरण (1-matika.md)
DUKA_HEADING = "दो-दो के वर्गीकरण"
QUESTION = (f"बारह {K}ों में से कितने हितकर हैं, कितने हानिकर हैं, कितने नैतिक रूप से अनिर्धारित हैं… "
            f"कितने संघर्ष वाले हैं, कितने संघर्ष से रहित हैं?")


def build():
    P = pali_lines(NAME)
    D = base_defs()
    H = []
    H += ["### " + S.CHAPTER_TITLES[2], "#### " + S.SECTION_TITLES["Suttantabhājanīyaṃ"], LIST_SUTTANTA,
          " ".join(anicca(*x) for x in ANICCA_ITEMS), S.SECTION_TITLES["Suttantabhājanīyaṃ"] + "।"]
    H += ["#### " + S.SECTION_TITLES["Abhidhammabhājanīyaṃ"], LIST_ABHIDHAMMA]
    H += [D["cakkhu"], D["sota"], D["ghana"], D["jivha"], D["kaya"]]
    H += mana_lines()
    H += [D["rupa"], D["sadda"], D["gandha"], D["rasa"], D["photthabba"]]
    H += dhamma_lines()
    H += ["#### " + S.SECTION_TITLES["Pañhāpucchakaṃ"], LIST_SUTTANTA, QUESTION, "##### " + TIKA_HEADING]
    # the Pañhāpucchaka paragraphs, parsed from the Pāli
    start = len(H)
    pan = [strip_id(l) for l in P[start:]]
    i = 0
    while not pan[i].startswith("##### Dukaṃ"):
        H.append(M.paragraph(pan[i], SJ.SUBJ_AYATANA, SJ.OVR_AYATANA))
        i += 1
    H.append("##### " + DUKA_HEADING)
    i += 1
    while pan[i] != "Pañhāpucchakaṃ.":
        H.append(M.paragraph(pan[i], SJ.SUBJ_AYATANA, SJ.OVR_AYATANA))
        i += 1
    H += [S.SECTION_TITLES["Pañhāpucchakaṃ"] + "।", S.CHAPTER_TITLES[2] + " पूरा हुआ।"]
    return H


def main():
    check_in_pi([LIST_SUTTANTA[:-1], "आँख की क्षमता", "मन का तत्व", "मन की चेतना का तत्व", "सुख की क्षमता",
                 "दुःख की क्षमता", "प्रसन्नता की क्षमता", "उदासी की क्षमता", "समभाव की क्षमता", RUPA_DHAMMAYATANA,
                 ASANKHATA_DHATU, "राग", "द्वेष", "मोह"])
    write_chapter(NAME, build())


if __name__ == "__main__":
    main()
