# -*- coding: utf-8 -*-
"""pi-2 Hindi zero-shot: 7-satipatthanavibhango.md (Analysis of the Foundations of Mindfulness).
usage: python -I -X utf8 build_7-satipatthanavibhango_hi.py [show]
"""
import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import pp_5_7_10_11_hi as P  # noqa: E402
from pp_5_7_10_11_hi import (S, DASH, MAGGANGA, PANNA_PE, VIRIYA_PE, SATI_PE, SATI_SHORT, RAGA_PE,  # noqa: E402
                             DOMANASSA_DEF, LOKUTTARA_HEAD, PHASSA_PE, KUSALA_END, VIPAKA, FORMULA, SELF, OBJ,
                             ANUPASSI, VIHARATI, SB, anupassi, four_satipatthana)

CH = "7-satipatthanavibhango.md"
T = S.CHAPTER_TITLES[7]
SP = "सजगता का आधार"                      # satipaṭṭhānaṃ
SP_JOINED = "बाकी परिघटनाएँ सजगता के आधार से जुड़ी हैं।"   # Avasesā dhammā satipaṭṭhānasampayuttā.


def how(k, s=None):
    """Kathañca bhikkhu [ajjhattaṃ] kāye kāyānupassī viharati?"""
    a = anupassi(k, s)
    return "और भिक्षु " + a.replace(VIHARATI, "अवलोकन करते हुए कैसे रहता है?")


def evam(k, s):
    """Evaṃ bhikkhu ajjhattabahiddhā kāye kāyānupassī viharati ātāpī … abhijjhādomanassaṃ."""
    return f"इस तरह भिक्षु {anupassi(k, s)}, {FORMULA}।"


NIMITTA1 = "वह उस चिह्न का सेवन करता है, उसका अभ्यास करता है, उसे बार-बार करता है, उसे भली-भाँति निर्धारित करता है।"


def nimitta2(k, s):
    """So taṃ nimittaṃ āsevitvā … bahiddhā kāye cittaṃ upasaṃharati."""
    return (f"वह उस चिह्न का सेवन करके, उसका अभ्यास करके, उसे बार-बार करके, उसे भली-भाँति निर्धारित करके "
            f"{SELF[s]} {OBJ[k]} पर मन को ले जाता है।")


def nimitta(k, s):
    return f"{NIMITTA1} {nimitta2(k, s)}"


# --- body ------------------------------------------------------------------------------------------
def body_list(variants=False):
    v1 = " [वर्तनी-भेद (Sī.): nahāru]" if variants else ""
    v2 = " [वर्तनी-भेद (Sī.): aṭṭhimiñjā]" if variants else ""
    return ("सिर के बाल, रोएँ, नाखून, दाँत, त्वचा, मांस, नसें" + v1 + ", हड्डियाँ, हड्डियों की मज्जा" + v2 + ", गुर्दे, "
            "हृदय, यकृत, झिल्ली, तिल्ली, फेफड़े, आँतें, आँतों की मेखला, पेट का भोजन, मल, पित्त, कफ, पीब, रक्त, "
            "पसीना, चर्बी, आँसू, वसा, लार, नाक का मैल, जोड़ों का तरल और मूत्र")


def body(s, whose, variants=False):
    """Idha bhikkhu ajjhattaṃ kāyaṃ uddhaṃ pādatalā … paccavekkhati – "atthi imasmiṃ kāye …"nti."""
    return (f"यहाँ भिक्षु {SELF[s]} शरीर को, जो पैरों के तलवों से ऊपर और सिर के बालों के सिरे से नीचे है, त्वचा से "
            f"घिरा है और अनेक प्रकार की अशुद्धियों से भरा है, इस तरह जाँचता है {DASH} “{whose} शरीर में "
            f"{body_list(variants)} हैं”।")


# --- feelings ---------------------------------------------------------------------------------------
SAMISA, NIRAMISA = "सांसारिक भोग से जुड़ी", "सांसारिक भोग से रहित"     # sāmisa / nirāmisa (pi-5)
FEEL = ["सुखद अनुभूति", "दुःखद अनुभूति", "न दुःखद, न सुखद अनुभूति"]
VED9 = FEEL + [f"{x} {f}" for f in FEEL for x in (SAMISA, NIRAMISA)]


def ved_a(f):
    return f"{f} का अनुभव करते हुए “मैं {f} का अनुभव कर रहा हूँ” ऐसा जानता है"


def ved_b(f):
    return f"{f} का अनुभव कर रहे दूसरे व्यक्ति के बारे में “वह {f} का अनुभव कर रहा है” ऐसा जानता है"


def ved_ab(f):
    return f"{f} को “{f}” के रूप में जानता है"


# --- mind -------------------------------------------------------------------------------------------
CIT16 = ["राग-युक्त", "राग से मुक्त", "द्वेष-युक्त", "द्वेष से मुक्त", "मोह-युक्त", "मोह से मुक्त", "सिमटा हुआ",
         "बिखरा हुआ", "उन्नत", "उन्नत न होने वाला", "सर्वोच्च न होने वाला", "सर्वोच्च", "एकाग्र",
         "एकाग्रता से रहित", "मुक्त", "अमुक्त"]   # pi-5 ^5-436 list; mahaggata/sauttara as in the pi-1 matrix


def cit_a(x):
    return f"मन {x} होने पर “मेरा मन {x} है” ऐसा जानता है"


def cit_b(x):
    return f"उसका मन {x} होने पर “उसका मन {x} है” ऐसा जानता है"


def cit_ab(x):
    return f"मन {x} होने पर “मन {x} है” ऐसा जानता है"


# --- mental objects -----------------------------------------------------------------------------------
LOC = {"a": ("अपने भीतर ", "मेरे भीतर "), "b": ("उसमें ", "उसमें "), "ab": ("", "")}
KAMA = ("इंद्रिय-सुखों की चाह", "f")
VICI = ("संशय", "m")


def present_absent(s, name):
    loc, qloc = LOC[s]
    return (f"{loc}{name} होने पर “{qloc}{name} है” ऐसा जानता है, "
            f"{loc}{name} न होने पर “{qloc}{name} नहीं है” ऐसा जानता है")


def hindrance(s, nb):
    name, g = nb
    hu, cuk, chod, chodc, hoti = (("हुई", "चुकी", "छोड़ी जाती है", "छोड़ी जा चुकी", "होती") if g == "f"
                                  else ("हुआ", "चुका", "छोड़ा जाता है", "छोड़ा जा चुका", "होता"))
    return (f"{present_absent(s, name)}, और जिस तरह उत्पन्न न {hu} {name} उत्पन्न {hoti} है, उसे भी जानता है, "
            f"और जिस तरह उत्पन्न हो {cuk} {name} {chod}, उसे भी जानता है, "
            f"और जिस तरह {chodc} {name} भविष्य में फिर उत्पन्न नहीं {hoti}, उसे भी जानता है")


def bojjhanga(s, k):
    name = SB[k]
    obl = P.obl_sb(k)
    return (f"{present_absent(s, name)}, और जिस तरह उत्पन्न न हुआ {name} उत्पन्न होता है, उसे भी जानता है, "
            f"और जिस तरह उत्पन्न हो चुके {obl} का अभ्यास परिपूर्ण होता है, उसे भी जानता है")


def middle_hindrances(s, variant=False):
    loc = LOC[s][0]
    v = " [वर्तनी-भेद (Sī., Syā.): thīnamiddhaṃ]" if variant else ""
    return (f"{loc}दुर्भावना होने पर… {loc}आलस्य और तंद्रा{v} होने पर… {loc}बेचैनी और पछतावा होने पर… ")


def middle_sb(s, variant=False):
    loc = LOC[s][0]
    v = " [वर्तनी-भेद (Sī., Syā.): viriyasambojjhaṅgaṃ]" if variant else ""
    return (f"{loc}{SB['dv']} होने पर… {loc}{SB['viriya']}{v} होने पर… {loc}{SB['piti']} होने पर… "
            f"{loc}{SB['passaddhi']} होने पर… {loc}{SB['samadhi']} होने पर… ")


def dhamma_line1(s, variant=False):
    return (f"{how('dhamma', s)} यहाँ भिक्षु {hindrance(s, KAMA)}। {middle_hindrances(s, variant)}"
            f"{hindrance(s, VICI)}।")


def dhamma_line2(s, sep, variant=False):
    """sep: ', ' (Pāli comma before the elided factors) or '। ' (Pāli full stop)"""
    return f"{bojjhanga(s, 'sati')}{sep}{middle_sb(s, variant)}{bojjhanga(s, 'upekkha')}।"


# --- the word explanations (^2-357 …) ---------------------------------------------------------------
def upeta(np):
    return (f"वह {np} से युक्त, भली-भाँति युक्त, इस तक पहुँचा हुआ, भली-भाँति पहुँचा हुआ, इसे प्राप्त किए हुए, "
            f"इससे संपन्न और इससे समन्वित होता है।")


def upeta_pe(np):
    return f"वह {np} से युक्त… इससे समन्वित होता है।"


LEMMA = {"anupassi": "“अवलोकन करते हुए”", "viharati": "“रहता है”", "atapi": "“उद्यमी”",
         "sampajano": "“स्पष्ट समझ रखते हुए”", "satima": "“सजग”",
         "vineyya": "“लोक में लालच और उदासी को दूर करके”"}


def tena(k):
    return f"इसलिए {LEMMA[k]} कहा जाता है।"


def anupassi_def(quoted):
    called = "यह “अवलोकन” कहा जाता है।" if quoted else "यह अवलोकन कहा जाता है।"
    return (f"{LEMMA['anupassi']}। यहाँ अवलोकन क्या है? जो {PANNA_PE} है {DASH} {called} "
            f"{upeta('इस अवलोकन')} {tena('anupassi')}")


VIHARATI_DEF = (f"{LEMMA['viharati']}। वह गतिशील रहता है, बना रहता है, अपना पालन करता है, चलता रहता है, चलाए रखता है, "
                f"विचरता है, रहता है। {tena('viharati')}")


def atapi_def(variant, pe):
    v = " [पाठभेद (सभी संस्करण): katamaṃ ātāpaṃ]" if variant else ""
    up = upeta_pe("इस उद्यमशीलता") if pe else upeta("इस उद्यमशीलता")
    return (f"{LEMMA['atapi']}। यहाँ उद्यमशीलता{v} क्या है? जो {VIRIYA_PE} है {DASH} यह “उद्यमशीलता” कही जाती है। "
            f"{up} {tena('atapi')}")


def sampajano_def(pe):
    up = upeta_pe("इस स्पष्ट समझ") if pe else upeta("इस स्पष्ट समझ")
    return (f"{LEMMA['sampajano']}। यहाँ स्पष्ट समझ क्या है? जो {PANNA_PE} है {DASH} यह “स्पष्ट समझ” कही जाती है। "
            f"{up} {tena('sampajano')}")


def satima_def(pe):
    up = upeta_pe("इस सजगता") if pe else upeta("इस सजगता")
    return (f"{LEMMA['satima']}। यहाँ सजगता क्या है? जो {SATI_PE} है {DASH} यह “सजगता” कही जाती है। "
            f"{up} {tena('satima')}")


VINITA = ("इस तरह यह लालच और यह उदासी इस लोक में दूर कर दिए गए, पूरी तरह दूर कर दिए गए, शांत, शमित, पूरी तरह शांत, "
          "अस्त, पूरी तरह अस्त, समाप्त, पूरी तरह समाप्त, सुखा दिए गए, पूरी तरह सुखा दिए गए और मिटा दिए गए होते हैं।")
LOBHA_DOMANASSA = (f"यहाँ लालच क्या है? जो {RAGA_PE} है {DASH} यह “लालच” कहा जाता है। यहाँ उदासी क्या है? "
                   f"जो {DOMANASSA_DEF} है {DASH} यह “उदासी” कही जाती है। {VINITA} {tena('vineyya')}")
FIVE_UPADANA = "आसक्ति के पाँचों समूह भी लोक हैं"   # Pañcapi upādānakkhandhā loko


def vineyya_def(world, dash_join=False):
    """world: 'वही शरीर लोक है।' etc.; dash_join: Pāli "… loko – tattha katamā abhijjhā?" (no "Ayaṃ vuccati loko")"""
    if dash_join:
        mid = f"{FIVE_UPADANA} {DASH} {LOBHA_DOMANASSA}"
    else:
        mid = f"{FIVE_UPADANA}। यह “लोक” कहा जाता है। {LOBHA_DOMANASSA}"
    return f"यहाँ लोक क्या है? {world} {mid}"


LEMMAS_PE = "… ".join(LEMMA[k] for k in ("anupassi", "viharati", "atapi", "sampajano", "satima")) + "… " + LEMMA["vineyya"] + "।"


def lemmas_line(world, dash_join=False):
    return f"{LEMMAS_PE} {vineyya_def(world, dash_join)}"


# --- Abhidhammabhājanīya --------------------------------------------------------------------------
def anup_do(k):
    return f"और {ANUPASSI[k]} अवलोकन करता है"


def sp_called(quoted=True):
    return f"यह “{SP}” कहा जाता है।" if quoted else f"यह {SP} कहा जाता है।"


def abh_plain(k, quoted=True):
    return (f"{how(k)} {LOKUTTARA_HEAD}, {anup_do(k)}, उस समय जो {SATI_SHORT}, {SB['sati']}, {MAGGANGA} है "
            f"{DASH} {sp_called(quoted)} {SP_JOINED}")


def abh_vipaka(k):
    head = how(k) if k else f"यहाँ {SP} क्या है?"
    anup = f", {anup_do(k)}" if k else ""
    return (f"{head} {LOKUTTARA_HEAD}, {PHASSA_PE}। {KUSALA_END} {VIPAKA}{anup}, उस समय जो {SATI_SHORT}, "
            f"{SB['sati']}, {MAGGANGA} है {DASH} {sp_called()} {SP_JOINED}")


def four_full_self():
    """^2-355: ajjhattaṃ … bahiddhā … ajjhattabahiddhā kāye kāyānupassī viharati ātāpī …, ajjhattaṃ vedanāsu …"""
    parts = []
    for k in ("kaya", "vedana", "citta", "dhamma"):
        parts.append(", ".join(anupassi(k, s) for s in ("a", "b", "ab")) + ", " + FORMULA)
    return f"सजगता के चार आधार {DASH} यहाँ भिक्षु " + ", ".join(parts) + "।"


M = {
    1: "### " + T,
    3: "#### " + S.SECTION_TITLES["Suttantabhājanīyaṃ"],
    5: four_full_self(),
    7: "##### शरीर के अवलोकन का विवरण",
    9: f"{how('kaya', 'a')} {body('a', 'इस', variants=True)} {nimitta('kaya', 'b')}",
    10: f"{how('kaya', 'b')} {body('b', 'उसके')} {nimitta('kaya', 'ab')}",
    11: f"{how('kaya', 'ab')} {body('ab', 'इस')} {evam('kaya', 'ab')}",
    13: anupassi_def(True),
    15: VIHARATI_DEF,
    17: atapi_def(True, False),
    19: sampajano_def(False),
    21: satima_def(False),
    23: f"{LEMMA['vineyya']}। " + vineyya_def("वही शरीर लोक है।"),
    24: "शरीर के अवलोकन का विवरण।",
    26: "##### अनुभूतियों के अवलोकन का विवरण",
    28: f"{how('vedana', 'a')} यहाँ भिक्षु " + ", ".join(ved_a(f) for f in VED9) + f"। {nimitta('vedana', 'b')}",
    29: f"{how('vedana', 'b')} यहाँ भिक्षु " + ", ".join(ved_b(f) for f in VED9) + f"। {nimitta('vedana', 'ab')}",
    30: f"{how('vedana', 'ab')} यहाँ भिक्षु " + ", ".join(ved_ab(f) for f in VED9) + f"। {evam('vedana', 'ab')}",
    32: lemmas_line("वही अनुभूति लोक है।"),
    33: "अनुभूतियों के अवलोकन का विवरण।",
    35: "##### मन के अवलोकन का विवरण",
    37: f"{how('citta', 'a')} यहाँ भिक्षु " + ", ".join(cit_a(x) for x in CIT16) + f"। {nimitta('citta', 'b')}",
    38: f"{how('citta', 'b')} यहाँ भिक्षु " + ", ".join(cit_b(x) for x in CIT16) + f"। {nimitta('citta', 'ab')}",
    39: f"{how('citta', 'ab')} यहाँ भिक्षु " + ", ".join(cit_ab(x) for x in CIT16) + f"। {evam('citta', 'ab')}",
    41: lemmas_line("वही मन लोक है।", dash_join=True),
    42: "मन के अवलोकन का विवरण।",
    44: "##### परिघटनाओं के अवलोकन का विवरण",
    46: dhamma_line1("a", variant=True),
    47: dhamma_line2("a", ", ", variant=True) + " " + nimitta("dhamma", "b"),
    48: dhamma_line1("b"),
    49: dhamma_line2("b", "। ") + " " + nimitta("dhamma", "ab"),
    50: dhamma_line1("ab"),
    51: dhamma_line2("ab", "। ") + " " + evam("dhamma", "ab"),
    53: anupassi_def(False),
    55: VIHARATI_DEF,
    57: atapi_def(False, True),
    59: sampajano_def(True),
    61: satima_def(True),
    63: f"{LEMMA['vineyya']}। " + vineyya_def("वे ही परिघटनाएँ लोक हैं।"),
    64: "परिघटनाओं के अवलोकन का विवरण।",
    65: S.SECTION_TITLES["Suttantabhājanīyaṃ"] + "।",
    67: "#### " + S.SECTION_TITLES["Abhidhammabhājanīyaṃ"],
    69: four_satipatthana(False),
    71: abh_plain("kaya"),
    73: abh_plain("vedana", quoted=False),
    75: abh_plain("citta"),
    77: abh_plain("dhamma"),
    79: (f"यहाँ {SP} क्या है? {LOKUTTARA_HEAD}, {anup_do('dhamma')}, उस समय जो {SATI_SHORT}, {SB['sati']}, "
         f"{MAGGANGA} है {DASH} {sp_called()} {SP_JOINED}"),
    81: four_satipatthana(False),
    83: abh_vipaka("kaya"),
    85: abh_vipaka("vedana"),
    87: abh_vipaka("citta"),
    89: abh_vipaka("dhamma"),
    91: abh_vipaka(None),
    92: S.SECTION_TITLES["Abhidhammabhājanīyaṃ"] + "।",
    94: "#### " + S.SECTION_TITLES["Pañhāpucchakaṃ"],
    96: four_satipatthana(True),
    98: P.question_kati("सजगता के चार आधारों", masc=True),
    100: P.TIKA_HEAD,
    104: P.DUKA_HEAD,
    109: S.SECTION_TITLES["Pañhāpucchakaṃ"] + "।",
    110: T + " पूरा हुआ।",
}
PP = {102, 106, 107, 108}

if __name__ == "__main__":
    P.check_pi1()
    P.build(CH, M, PP, P.THESE_M, show=len(sys.argv) > 1)
