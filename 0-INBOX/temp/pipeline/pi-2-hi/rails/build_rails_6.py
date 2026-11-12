"""Builder for the Hindi rails translation (plain) of pi-2 chapter 6, Paṭiccasamuppādavibhaṅga.

Translates AI_translation/pali/pi-2_split_chapters/6-paticcasamuppadavibhango.md line by line from fixed
strings and small parsers (dependent-origination chain, mind-type openers, definition chunks), so identical
Pāli gives identical Hindi. Imports build_rails_sample read-only for shared constants.

usage: python -I -X utf8 build_rails_6.py
"""
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only import)

NAME = "6-paticcasamuppadavibhango.md"
SRC = S.PALI / NAME
DST = S.OUT / NAME
ID = re.compile(r"\s*(\^[0-9A-Za-z-]+)\s*$")
UNKNOWN = []
SLIPS = []

# =========================================================================== links of the chain
# key: (nominative, oblique before «के कारण» / «से», gender, plural)
L = {
    "avijjā": ("अज्ञान", "अज्ञान", "m", 0),
    "saṅkhāra": ("मानसिक रचनाएँ", "मानसिक रचनाओं", "f", 1),   # compound member / paccayā (termbase)
    "saṅkhāro": ("मानसिक रचना", "मानसिक रचना", "f", 0),
    "saṅkhārā": ("मानसिक रचनाएँ", "मानसिक रचनाओं", "f", 1),
    "viññāṇa": ("चेतना", "चेतना", "f", 0),
    "nāma": ("मानसिक पक्ष", "मानसिक पक्ष", "m", 0),
    "nāmarūpa": ("मानसिक पक्ष और भौतिक रूप", "मानसिक पक्ष और भौतिक रूप", "m", 0),
    "saḷāyatana": ("छह इंद्रिय-क्षेत्र", "छह इंद्रिय-क्षेत्रों", "m", 1),
    "chaṭṭhāyatana": ("छठा इंद्रिय-क्षेत्र", "छठे इंद्रिय-क्षेत्र", "m", 0),
    "phassa": ("संपर्क", "संपर्क", "m", 0),
    "vedanā": ("अनुभूति", "अनुभूति", "f", 0),
    "taṇhā": ("तृष्णा", "तृष्णा", "f", 0),
    "upādāna": ("आसक्ति", "आसक्ति", "f", 0),
    "bhava": ("अस्तित्व", "अस्तित्व", "m", 0),
    "jāti": ("जन्म", "जन्म", "m", 0),
    "jarāmaraṇa": ("बुढ़ापा और मृत्यु", "बुढ़ापे और मृत्यु", "m", 0),
    "adhimokkha": ("निश्चय", "निश्चय", "m", 0),
    "pasāda": ("आस्था", "आस्था", "f", 0),
    "paṭigha": ("चिढ़", "चिढ़", "f", 0),
    "vicikicchā": ("संशय", "संशय", "m", 0),
    "uddhacca": ("बेचैनी", "बेचैनी", "f", 0),
    "kusalamūla": ("हितकर मूल", "हितकर मूलों", "m", 1),
    "akusalamūla": ("हानिकर मूल", "हानिकर मूलों", "m", 1),
}
# Pāli nominative forms of the effect -> key
NOM = {"avijjā": "avijjā", "saṅkhāro": "saṅkhāro", "saṅkhārā": "saṅkhārā", "viññāṇaṃ": "viññāṇa",
       "nāmaṃ": "nāma", "nāmarūpaṃ": "nāmarūpa", "saḷāyatanaṃ": "saḷāyatana", "chaṭṭhāyatanaṃ": "chaṭṭhāyatana",
       "phasso": "phassa", "vedanā": "vedanā", "taṇhā": "taṇhā", "upādānaṃ": "upādāna", "bhavo": "bhava",
       "jāti": "jāti", "jarāmaraṇaṃ": "jarāmaraṇa", "adhimokkho": "adhimokkha", "pasādo": "pasāda",
       "paṭighaṃ": "paṭigha", "vicikicchā": "vicikicchā", "uddhaccaṃ": "uddhacca"}
TOK = re.compile(r"^(\w+?)paccayā(pi)? (\w+)(?: (\w+?)(hetuk[oaā]ṃ?|hetukaṃ|sampayutt[oaā]ṃ?))?(?: (nāmaṃ|chaṭṭhāyatanaṃ))?$")


def judaa(g, pl):
    if pl:
        return "जुड़ी हैं" if g == "f" else "जुड़े हैं"
    return "जुड़ी है" if g == "f" else "जुड़ा है"


def tok(t):
    """One link 'Xpaccayā[pi] Y [Z-hetuka/-sampayutta [nāmaṃ|chaṭṭhāyatanaṃ]]' -> (hindi, gender, plural, rel)."""
    m = TOK.match(t)
    if not m:
        raise KeyError(t)
    cause, pi, eff, qstem, qtype, extra = m.groups()
    cause = cause[0].lower() + cause[1:]
    cn, co, _, _ = L[cause]
    en, _, eg, ep = L[NOM[eff]]
    bhi = " भी" if pi else ""
    h = f"{co} के कारण{bhi} {en}"
    if not qtype:
        return h, eg, ep, False
    qn, qo, qg, qp = L[qstem]
    if qtype.startswith("hetuk"):
        jis = "जिनका" if ep else "जिसका"
        return f"{h}, {jis} मूल {qn} {'हैं' if qp else 'है'}", eg, ep, True
    if extra:
        xn = L[NOM[extra]][0]
        return f"{h}, जिनमें {xn} {qo} से जुड़ा है", eg, ep, True
    return f"{h}, जो {qo} से {judaa(eg, ep)}", eg, ep, True


def chain(text):
    """A whole chain (separators ', ', '; ', '…pe…') -> Hindi list (no verb)."""
    if "saṅkhārahetukaṃ viññāṇapaccayā" in text:
        SLIPS.append("^2-262: comma missing after «saṅkhārahetukaṃ» in the chain (translated as if present)")
        text = text.replace("saṅkhārahetukaṃ viññāṇapaccayā", "saṅkhārahetukaṃ, viññāṇapaccayā")
    parts = re.split(r"(, |; |…pe… ?)", text)
    toks = [tok(p) for p in parts[0::2]]
    seps = parts[1::2]
    out = toks[0][0]
    for i, sep in enumerate(seps):
        if sep.startswith("…"):
            s = "… "
        elif sep == "; " or toks[i][3] or toks[i + 1][3]:
            s = "; "
        else:
            s = ", "
        out += s + toks[i + 1][0]
    return out


VERB = " होते हैं"
GRIEF = "बुढ़ापा और मृत्यु, शोक, विलाप, दुःख, उदासी और निराशा"   # PI1 ^1-1343
EVAM = "इस प्रकार इस पूरे दुःख के समूह की उत्पत्ति होती है"          # PI1 ^1-1343
EVAM_DH = "इस प्रकार इन परिघटनाओं की उत्पत्ति होती है"
MEANING = ("इसका अर्थ है कि इस प्रकार इस पूरे दुःख के समूह का मेल होता है, एक साथ आना होता है, "
           "जुड़ाव होता है, प्रकट होना होता है")
MEANING_DH = ("इसका अर्थ है कि इस प्रकार इन परिघटनाओं का मेल होता है, एक साथ आना होता है, "
              "जुड़ाव होता है, प्रकट होना होता है")
TENA = f"इसीलिए कहा जाता है, “{EVAM}”"
TENA_DH = f"इसीलिए कहा जाता है, “{EVAM_DH}”"

# =========================================================================== simple (non-chain) items
SIMPLE = {
    "avijjā": ("अज्ञान", "m", 0), "saṅkhāro": ("मानसिक रचना", "f", 0),
    "puññābhisaṅkhāro": ("पुण्य की कर्म-रचना", "f", 0), "apuññābhisaṅkhāro": ("अपुण्य की कर्म-रचना", "f", 0),
    "āneñjābhisaṅkhāro": ("अविचल अवस्था की कर्म-रचना", "f", 0), "kāyasaṅkhāro": ("शरीर की रचना", "f", 0),
    "nāmaṃ": ("मानसिक पक्ष", "m", 0), "rūpaṃ": ("भौतिक रूप", "m", 0),
    "nāmarūpaṃ": ("मानसिक पक्ष और भौतिक रूप", "m", 0),
    "kammabhavo": ("कर्म रूपी अस्तित्व", "m", 0), "upapattibhavo": ("पुनर्जन्म रूपी अस्तित्व", "m", 0),
    "jarā": ("बुढ़ापा", "m", 0), "maraṇaṃ": ("मृत्यु", "f", 0), "soko": ("शोक", "m", 0),
    "paridevo": ("विलाप", "m", 0), "dukkhaṃ": ("दुःख", "m", 0), "domanassaṃ": ("उदासी", "f", 0),
    "upāyāso": ("निराशा", "f", 0), "kusalamūlā": ("हितकर मूल", "m", 1),
    "alobho": ("लोभ का अभाव", "m", 0), "adoso": ("द्वेष का अभाव", "m", 0), "amoho": ("मोह का अभाव", "m", 0),
}


def item(p):
    """Any item -> (hindi, gender, plural, rel)."""
    p = p.strip().strip('"').strip()
    if p in SIMPLE:
        h, g, pl = SIMPLE[p]
        return h, g, pl, False
    return tok(p)


def question(p):
    h, g, pl, rel = item(p)
    c = "," if rel else ""
    if pl:
        return f"यहाँ {h}{c} {'कौन-सी हैं' if g == 'f' else 'कौन-से हैं'}"
    return f"यहाँ {h}{c} क्या है"


def called(p, quoted):
    h, g, pl, _ = item(p)
    if quoted:
        h = f"“{h}”"
    if pl:
        return f"ये {h} {'कही जाती हैं' if g == 'f' else 'कहे जाते हैं'}"
    return f"यह {h} {'कही जाती है' if g == 'f' else 'कहा जाता है'}"


# =========================================================================== definitions (chunks)
KH4 = {"vedanākkhandho": "अनुभूति का समूह", "saññākkhandho": "पहचान का समूह",
       "saṅkhārakkhandho": "मानसिक रचनाओं का समूह", "viññāṇakkhandho": "चेतना का समूह"}
THAPETVA = {"upādānaṃ": "आसक्ति", "phassaṃ": "संपर्क", "adhimokkhaṃ": "निश्चय", "vicikicchaṃ": "संशय",
            "vedanaṃ": "अनुभूति"}
SENSE6 = S.SENSES
BYASANA = ("Ñātibyasanena vā phuṭṭhassa, bhogabyasanena vā phuṭṭhassa, rogabyasanena vā phuṭṭhassa, "
           "sīlabyasanena vā phuṭṭhassa, diṭṭhibyasanena vā phuṭṭhassa, aññataraññatarena byasanena samannāgatassa, "
           "aññataraññatarena dukkhadhammena phuṭṭhassa ")
BYASANA_H = ("रिश्तेदारों की हानि से पीड़ित, या धन-संपत्ति की हानि से पीड़ित, या रोग रूपी हानि से पीड़ित, "
             "या सदाचार की हानि से पीड़ित, या दृष्टि की हानि से पीड़ित, किसी न किसी हानि से घिरे, "
             "किसी न किसी दुःख रूपी परिघटना से पीड़ित व्यक्ति का जो ")
SOKA = "शोक, शोक करना, शोक से भरा होना, भीतर का शोक, भीतर का गहरा शोक, मन का जलना, उदासी, शोक का काँटा है"
PARIDEVA = ("रोना, विलाप, रोते रहना, विलाप करते रहना, रोने से भरा होना, विलाप से भरा होना, शब्दों की झड़ी, "
            "प्रलाप, बड़बड़ाना, बिलखना, बिलखते रहना, बिलखने से भरा होना है")
UPAYASA = "हताशा, निराशा, हताशा से भरा होना, निराशा से भरा होना है"
JATI_S = ("उन-उन प्राणियों का उस-उस प्राणी-वर्ग में जो जन्म, भली-भाँति जन्म, गर्भ में उतरना, पूरी तरह पैदा होना, "
          "समूहों का प्रकट होना, इंद्रिय-क्षेत्रों की उपलब्धि है")
JARA_S = ("उन-उन प्राणियों का उस-उस प्राणी-वर्ग में जो बुढ़ापा, जीर्ण होना, दाँतों का टूटना, बालों का पकना, "
          "त्वचा पर झुर्रियाँ पड़ना, आयु का घटना, इंद्रियों का पूरी तरह पक जाना है")  # list = PI1 ^1-643
MARANA_S = ("उन-उन प्राणियों का उस-उस प्राणी-वर्ग से जो गुज़र जाना, गुज़र जाने की अवस्था, टूटना, लुप्त हो जाना, "
            "मौत, मृत्यु, काल का पूरा होना [वर्तनी-भेद (Ka.): kālaṃkiriyā], समूहों का टूटना, शरीर का त्याग, "
            "जीवन-क्षमता का कट जाना है")
DUKKHA_K = ("जो शारीरिक असुहावनापन, शारीरिक दुःख, शरीर के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
            "शरीर के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति है")
SUKHA_K = ("जो शारीरिक सुहावनापन, शारीरिक सुख, शरीर के संपर्क से उत्पन्न सुहावना सुखद अनुभव, "
           "शरीर के संपर्क से उत्पन्न सुहावनी सुखद अनुभूति है")
DUKKHA_C = ("जो मानसिक असुहावनापन, मानसिक दुःख, मन के संपर्क से उत्पन्न असुहावना दुःखद अनुभव, "
            "मन के संपर्क से उत्पन्न असुहावनी दुःखद अनुभूति है")
SUKHA_C = ("जो मानसिक सुहावनापन, मानसिक सुख, मन के संपर्क से उत्पन्न सुहावना सुखद अनुभव, "
           "मन के संपर्क से उत्पन्न सुहावनी सुखद अनुभूति है")
ADM_C = ("जो न मानसिक सुहावनापन, न मानसिक असुहावनापन, मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभव, "
         "मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभूति है")
CITTA_FULL = ("जो मन, मानस, मानसिक क्रिया, हृदय, उज्ज्वलता, मानस, मन का इंद्रिय-क्षेत्र, मन की क्षमता, चेतना, "
              "चेतना का समूह, उसके अनुरूप मन की चेतना का तत्व है")  # PI1 ^1-6
RUPA_UPACAYA = (", ".join(f"{s} के इंद्रिय-क्षेत्र की वृद्धि" for s in SENSE6[:5])
                + ", या जो भी अन्य भौतिक रूप मन से जन्मा, मन के कारण होने वाला और मन से उत्पन्न है")
NISSAYA = "वह भौतिक रूप जिसके सहारे मन की चेतना का तत्व काम करता है"

DEFS = {
    # Suttantabhājanīya
    "Dukkhe aññāṇaṃ, dukkhasamudaye aññāṇaṃ, dukkhanirodhe aññāṇaṃ, dukkhanirodhagāminiyā paṭipadāya aññāṇaṃ":
        "दुःख को न जानना, दुःख की उत्पत्ति को न जानना, दुःख के अंत को न जानना, "
        "दुःख के अंत की ओर ले जाने वाले प्रगति के ढंग को न जानना",  # PI1 ^1-1067 (moha)
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro, kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāro":
        "पुण्य की कर्म-रचना, अपुण्य की कर्म-रचना, अविचल अवस्था की कर्म-रचना, शरीर की रचना, वाणी की रचना, मन की रचना",
    "Puññābhisaṅkhāro, apuññābhisaṅkhāro, āneñjābhisaṅkhāro":
        "पुण्य की कर्म-रचना, अपुण्य की कर्म-रचना, अविचल अवस्था की कर्म-रचना",
    "Kusalā cetanā kāmāvacarā rūpāvacarā dānamayā sīlamayā bhāvanāmayā":
        "इंद्रिय-सुखों के लोक से संबंधित और सूक्ष्म भौतिक लोक से संबंधित हितकर इरादा, "
        "जो दान से, सदाचार से और मानसिक अभ्यास से बना होता है",
    "Akusalā cetanā kāmāvacarā": "इंद्रिय-सुखों के लोक से संबंधित हानिकर इरादा",
    "Kusalā cetanā arūpāvacarā": "अभौतिक लोक से संबंधित हितकर इरादा",
    "Kāyasañcetanā kāyasaṅkhāro, vacīsañcetanā vacīsaṅkhāro, manosañcetanā cittasaṅkhāro":
        "शरीर से इरादा करना शरीर की रचना है, वाणी से इरादा करना वाणी की रचना है, मन से इरादा करना मन की रचना है",
    "Cakkhuviññāṇaṃ, sotaviññāṇaṃ, ghānaviññāṇaṃ, jivhāviññāṇaṃ, kāyaviññāṇaṃ, manoviññāṇaṃ":
        ", ".join(f"{s} की चेतना" for s in SENSE6),
    "Atthi nāmaṃ, atthi rūpaṃ": "मानसिक पक्ष भी है, भौतिक रूप भी है",
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho": "अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह",
    "Vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho":
        "अनुभूति का समूह, पहचान का समूह, मानसिक रचनाओं का समूह, चेतना का समूह",
    "Cattāro mahābhūtā, catunnañca mahābhūtānaṃ upādāya rūpaṃ": S.MAHABHUTA,
    "Iti idañca nāmaṃ, idañca rūpaṃ": "इस प्रकार यह मानसिक पक्ष है और यह भौतिक रूप",
    "Cakkhāyatanaṃ, sotāyatanaṃ, ghānāyatanaṃ, jivhāyatanaṃ, kāyāyatanaṃ, manāyatanaṃ":
        ", ".join(f"{s} का इंद्रिय-क्षेत्र" for s in SENSE6),
    "Cakkhusamphasso sotasamphasso ghānasamphasso jivhāsamphasso kāyasamphasso manosamphasso":
        ", ".join(f"{s} का संपर्क" for s in SENSE6),
    "Cakkhusamphassajā vedanā, sotasamphassajā vedanā, ghānasamphassajā vedanā, jivhāsamphassajā vedanā, "
    "kāyasamphassajā vedanā, manosamphassajā vedanā": ", ".join(f"{s} के संपर्क से उत्पन्न अनुभूति" for s in SENSE6),
    "Rūpataṇhā, saddataṇhā, gandhataṇhā, rasataṇhā, phoṭṭhabbataṇhā, dhammataṇhā":
        "दृश्य रूप की तृष्णा, ध्वनि की तृष्णा, गंध की तृष्णा, स्वाद की तृष्णा, स्पर्श की तृष्णा, मन के विषयों की तृष्णा",
    "Kāmupādānaṃ, diṭṭhupādānaṃ, sīlabbatupādānaṃ, attavādupādānaṃ":
        "इंद्रिय-सुखों के प्रति आसक्ति, दृष्टियों के प्रति आसक्ति, सदाचार और व्रतों के प्रति आसक्ति, "
        "आत्मा के सिद्धांत के प्रति आसक्ति",
    "Bhavo duvidhena": "अस्तित्व दो प्रकार का है",
    "atthi kammabhavo, atthi upapattibhavo": "कर्म रूपी अस्तित्व भी है, पुनर्जन्म रूपी अस्तित्व भी है",
    "Sabbampi bhavagāmikammaṃ kammabhavo": "अस्तित्व की ओर ले जाने वाला सारा कर्म भी कर्म रूपी अस्तित्व है",
    "Kāmabhavo, rūpabhavo, arūpabhavo, saññābhavo, asaññābhavo, nevasaññānāsaññābhavo, ekavokārabhavo, "
    "catuvokārabhavo, pañcavokārabhavo":
        "इंद्रिय-सुखों के लोक का अस्तित्व, सूक्ष्म भौतिक लोक का अस्तित्व, अभौतिक लोक का अस्तित्व, पहचान वाला अस्तित्व, "
        "पहचान से रहित अस्तित्व, न पहचान, न अ-पहचान वाला अस्तित्व, एक समूह वाला अस्तित्व, चार समूहों वाला अस्तित्व, "
        "पाँच समूहों वाला अस्तित्व",
    "Iti ayañca kammabhavo, ayañca upapattibhavo": "इस प्रकार यह कर्म रूपी अस्तित्व है और यह पुनर्जन्म रूपी अस्तित्व",
    "Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jāti sañjāti okkanti abhinibbatti, khandhānaṃ pātubhāvo, "
    "āyatanānaṃ paṭilābho": JATI_S,
    "Atthi jarā, atthi maraṇaṃ": "बुढ़ापा भी है, मृत्यु भी है",
    "Yā tesaṃ tesaṃ sattānaṃ tamhi tamhi sattanikāye jarā jīraṇatā khaṇḍiccaṃ pāliccaṃ valittacatā āyuno saṃhāni "
    "indriyānaṃ paripāko": JARA_S,
    "Yā tesaṃ tesaṃ sattānaṃ tamhā tamhā sattanikāyā cuti cavanatā bhedo antaradhānaṃ maccu maraṇaṃ kālakiriyā "
    "[kālaṃkiriyā (ka.)] khandhānaṃ bhedo kaḷevarassa nikkhepo jīvitindriyassupacchedo": MARANA_S,
    "Iti ayañca jarā, idañca maraṇaṃ": "इस प्रकार यह बुढ़ापा है और यह मृत्यु",
    BYASANA + "soko socanā socitattaṃ antosoko antoparisoko cetaso parijjhāyanā domanassaṃ sokasallaṃ":
        BYASANA_H + SOKA,
    BYASANA + "ādevo paridevo ādevanā paridevanā ādevitattaṃ paridevitattaṃ vācā palāpo vippalāpo lālappo "
              "lālappanā lālappitattaṃ": BYASANA_H + PARIDEVA,
    BYASANA + "āyāso upāyāso āyāsitattaṃ upāyāsitattaṃ": BYASANA_H + UPAYASA,
    "Yaṃ kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ kāyasamphassajā asātā dukkhā vedanā":
        DUKKHA_K,
    "Yaṃ cetasikaṃ asātaṃ, cetasikaṃ dukkhaṃ, cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ, "
    "cetosamphassajā asātā dukkhā vedanā": DUKKHA_C,
    "Yaṃ cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ "
    "cetosamphassajā asātā dukkhā vedanā": DUKKHA_C,
    "Yaṃ kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        SUKHA_K,
    "Yaṃ cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        SUKHA_C,
    "Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā "
    "adukkhamasukhā vedanā": ADM_C,
    "Yaṃ cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ, cetosamphassajā "
    "adukkhamasukhā vedanā": ADM_C,
    # Abhidhammabhājanīya
    "Yaṃ aññāṇaṃ adassanaṃ": "जो न जानना, न देखना",                       # PI1 ^1-1318
    "avijjālaṅgī moho akusalamūlaṃ": "अज्ञान की रुकावट, मोह रूपी हानिकर मूल है",
    "avijjālaṅgī moho akusamūlaṃ": "अज्ञान की रुकावट, मोह रूपी हानिकर मूल है",
    "Yā cetanā sañcetanā sañcetayitattaṃ": "जो इरादा, इरादा करना, इरादा कर चुका होना है",
    "Yā cetanā sañcetanā sañcetayitattaṃ [cetayitattaṃ (sī. ka.)]":
        "जो इरादा, इरादा करना, इरादा कर चुका होना [पाठभेद (Sī., Ka.): cetayitattaṃ] है",
    "Yaṃ cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho "
    "tajjāmanoviññāṇadhātu": CITTA_FULL,
    "Yaṃ cittaṃ mano mānasaṃ": "जो मन, मानस, मानसिक क्रिया",
    "tajjāmanoviññāṇadhātu": "उसके अनुरूप मन की चेतना का तत्व है",
    "tajjācakkhuviññāṇadhātu": "उसके अनुरूप आँख की चेतना का तत्व है",
    "tajjākāyaviññāṇadhātu": "उसके अनुरूप शरीर की चेतना का तत्व है",
    "tajjāmanodhātu": "उसके अनुरूप मन का तत्व है",
    "Yo phasso phusanā samphusanā samphusitattaṃ": "जो संपर्क, छूना, भली-भाँति छूना, भली-भाँति छू चुका होना है",
    "Yo rāgo sārāgo anunayo anurodho nandī nandirāgo cittassa sārāgo":
        "जो राग, प्रबल राग, झुकाव, अनुकूल होना, आनंद, आनंद का राग, मन का प्रबल राग है",
    "Yo rāgo sārāgo": "जो राग, प्रबल राग",
    "Yo rāgo": "जो राग",
    "cittassa sārāgo": "मन का प्रबल राग है",
    "Yā diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ gāho "
    "patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho "
    "[vipariyesaggāho (bahūsu)]":
        "जो दृष्टि, दृष्टियों में फँसना, दृष्टि का घना जंगल, दृष्टि का बीहड़, दृष्टि का टेढ़ापन, दृष्टि की छटपटाहट, "
        "दृष्टि का बंधन, पकड़, कसकर पकड़ना, आग्रह, ग़लत धारणा, कुमार्ग, ग़लत रास्ता, ग़लतपन, मतवादों का आधार, "
        "उलटी पकड़ [वर्तनी-भेद (अनेक प्रतियों में): vipariyesaggāho] है",  # PI1 ^1-381
    "Yā diṭṭhi diṭṭhigataṃ": "जो दृष्टि, दृष्टियों में फँसना",
    "titthāyatanaṃ vipariyāsaggāho": "मतवादों का आधार, उलटी पकड़ है",
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbatti pātubhāvo":
        "उन-उन परिघटनाओं का जो जन्म, भली-भाँति जन्म, पैदा होना, पूरी तरह पैदा होना, प्रकट होना है",
    "Yā tesaṃ tesaṃ dhammānaṃ jāti sañjāti nibbatti abhinibbati pātubhāvo":
        "उन-उन परिघटनाओं का जो जन्म, भली-भाँति जन्म, पैदा होना, पूरी तरह पैदा होना, प्रकट होना है",
    "Yā tesaṃ tesaṃ dhammānaṃ jarā jīraṇatā āyuno saṃhāni": "उन-उन परिघटनाओं का जो बुढ़ापा, जीर्ण होना, आयु का घटना है",
    "Yo tesaṃ tesaṃ dhammānaṃ khayo vayo bhedo paribhedo aniccatā antaradhānaṃ":
        "उन-उन परिघटनाओं का जो क्षय, नाश, टूटना, बिखर जाना, अनित्यता, लुप्त हो जाना है",  # PI1 ^1-644
    "Cakkhāyatanassa upacayo, sotāyatanassa upacayo, ghānāyatanassa upacayo, jivhāyatanassa upacayo, "
    "kāyāyatanassa upacayo, yaṃ vā panaññampi atthi rūpaṃ cittajaṃ cittahetukaṃ cittasamuṭṭhānaṃ": RUPA_UPACAYA,
    "Yaṃ rūpaṃ nissāya manoviññāṇadhātu vattati": NISSAYA,
    "Cattāro ca mahābhūtā, yañca rūpaṃ nissāya manoviññāṇadhātu vattati": "चार महाभूत और " + NISSAYA,
    "Yo cittassa adhimokkho adhimuccanā tadadhimuttatā": "जो मन का निश्चय, निश्चय करना, उस पर निश्चय कर चुका होना है",
    "Yā saddhā saddahanā okappanā abhippasādo": "जो श्रद्धा, श्रद्धा रखना, भरोसा करना, गहरी आस्था है",
    "Yo cittassa āghāto": "जो मन का आक्रोश",
    "caṇḍikkaṃ asuropo [asulopo (syā.)] anattamanatā cittassa":
        "उग्रता, कटु वचन [वर्तनी-भेद (Syā.): asulopo], मन की अप्रसन्नता है",
    "Yā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvidhāpatho [dvedhāpatho (sī. syā.)] saṃsayo "
    "anekaṃsaggāho āsappanā parisappanā apariyogāhaṇā [apariyogāhanā (sī. syā. ka.)] chambhitattaṃ cittassa "
    "manovilekho":
        "जो शंका, शंका करना, शंका से भरा होना, दुविधा, संशय, दुचित्तापन, दोराहा [वर्तनी-भेद (Sī., Syā.): dvedhāpatho], "
        "संदेह, किसी एक बात को पक्का न पकड़ पाना, हिचकिचाना, बार-बार हिचकिचाना, गहराई में न उतर पाना "
        "[वर्तनी-भेद (Sī., Syā., Ka.): apariyogāhanā], मन का जड़ हो जाना, मन की खरोंच है",  # PI1 ^1-? (vicikicchā)
    "Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa":
        "जो मन की बेचैनी, अशांति, मन का भटकाव, मन का डाँवाडोल होना है",
    "Alobho, adoso, amoho": "लोभ का अभाव, द्वेष का अभाव, मोह का अभाव",
    "Alobho, adoso": "लोभ का अभाव, द्वेष का अभाव",
    "Yo alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ":
        "जो लोभ का अभाव, लोभ न करना, लोभ से भरा न होना, प्रबल राग का अभाव, राग न करना, राग से भरा न होना, "
        "लालच का अभाव, लोभ का अभाव रूपी हितकर मूल है",  # PI1 ^1-32
    "Yo adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ":
        "जो द्वेष का अभाव, द्वेष न करना, द्वेष से भरा न होना, दुर्भावना का अभाव, दुर्भावना न रखना, "
        "द्वेष का अभाव रूपी हितकर मूल है",  # PI1 ^1-33
    "Yā paññā pajānanā": "जो प्रज्ञा, जानना",
    "amoho dhammavicayo sammādiṭṭhi": "मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि है",  # PI1 ^1-1343
    "amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ":
        "मोह का अभाव, परिघटनाओं की छानबीन, सही दृष्टि, परिघटनाओं की छानबीन नामक जागृति का अंग, मार्ग का अंग, "
        "मार्ग में समाया हुआ है",
    # closing formulas
    "Evametassa kevalassa dukkhakkhandhassa samudayo hoti": EVAM,
    "Evametesaṃ dhammānaṃ samudayo hoti": EVAM_DH,
    "Evametassa kevalassa dukkhakkhandhassa samudayo hotīti": f"“{EVAM}”",
    "Evametesaṃ dhammānaṃ samudayo hotīti": f"“{EVAM_DH}”",
    "Evametassa kevalassa dukkhakkhandhassa saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti": MEANING,
    "Evametesaṃ dhammānaṃ saṅgati hoti, samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti": MEANING_DH,
    "Evametassa kevalassa dukkhakkhandhassa samudayo hotīti, evametassa kevalassa dukkhakkhandhassa saṅgati hoti, "
    "samāgamo hoti, samodhānaṃ hoti, pātubhāvo hoti": f"“{EVAM}”, {MEANING}",
}

# =========================================================================== headings, closings
HEAD = {
    "### Paṭiccasamuppādavibhaṅgo": "### परस्पर-आश्रित उत्पत्ति का विश्लेषण",
    "#### Suttantabhājanīyaṃ": f"#### {S.SUTTANTA_BH}",
    "#### Abhidhammabhājanīyaṃ": f"#### {S.ABHI_BH}",
    "##### Paccayacatukkaṃ": "##### कारण के चार रूप",
    "##### Hetucatukkaṃ": "##### मूल के चार रूप",
    "##### Sampayuttacatukkaṃ": "##### जुड़ाव के चार रूप",
    "##### Aññamaññacatukkaṃ": "##### परस्परता के चार रूप",
    "##### Mātikā": "##### मूल सूची",
    "##### Akusalaniddeso": "##### हानिकर परिघटनाओं की व्याख्या",
    "##### Kusalaniddeso": "##### हितकर परिघटनाओं की व्याख्या",
    "##### Abyākataniddeso": "##### नैतिक रूप से अनिर्धारित परिघटनाओं की व्याख्या",
    "##### Avijjāmūlakakusalaniddeso": "##### अज्ञान से शुरू होने वाली हितकर परिघटनाओं की व्याख्या",
    "##### Kusalamūlakavipākaniddeso": "##### हितकर मूलों से शुरू होने वाले कर्म-फल की व्याख्या",
    "##### Akusalamūlakavipākaniddeso": "##### हानिकर मूलों से शुरू होने वाले कर्म-फल की व्याख्या",
}
CLOSE = {"Suttantabhājanīyaṃ.": f"{S.SUTTANTA_BH}।", "Abhidhammabhājanīyaṃ.": f"{S.ABHI_BH}।",
         "Paṭiccasamuppādavibhaṅgo [paccayākāravibhaṅgo (sī. syā.)] niṭṭhito.":
             f"परस्पर-आश्रित उत्पत्ति का विश्लेषण [पाठभेद (Sī., Syā.): paccayākāravibhaṅgo] {S.DONE}।"}
for k, v in HEAD.items():
    if k.startswith("##### "):
        CLOSE[k[6:] + "."] = v[6:] + "।"

# =========================================================================== mind-type openers
KIND = {"akusalā": "हानिकर", "kusalā": "हितकर", "abyākatā": "नैतिक रूप से अनिर्धारित"}
RUPA_JH = ("कोई सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है, इंद्रिय-सुखों से अलग होकर… "
           "पहले ध्यान को प्राप्त करके उसमें रहता है, जो पृथ्वी के ध्यान-मंडल वाला है")  # PI1 ^1-167
ARUPA_JH = ("कोई अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है, कुछ भी न होने के क्षेत्र को "
            "पूरी तरह पार करके, सुख को छोड़ने से… न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाले चौथे ध्यान "
            "को प्राप्त करके उसमें रहता है")  # PI1 2-04 #167
LOK_JH = ("कोई लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला होता है, "
          "दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए, इंद्रिय-सुखों से अलग होकर… "
          "पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है")  # PI1 ^1-505
KIRIYA_TAIL = "जो केवल क्रिया रूपी है, न हितकर, न हानिकर, न ही कर्म-फल"  # PI1 2-05
DDSV = "जो इसी जीवन में सुख से रहने के लिए होता है"
P_RUPA = "rūpūpapattiyā maggaṃ bhāveti vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ"
P_ARUPA = ("arūpūpapattiyā maggaṃ bhāveti sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ "
           "sukhassa ca pahānā…pe… catutthaṃ jhānaṃ upasampajja viharati")
P_LOK = ("lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā "
         "vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ")
JHANA = {
    P_RUPA: RUPA_JH,
    P_RUPA.replace("pathavīkasiṇaṃ", "pathavīkasiṇaṃ [paṭhavīkasiṇaṃ (sī. syā.)]"):
        RUPA_JH.replace("ध्यान-मंडल वाला", "ध्यान-मंडल [वर्तनी-भेद (Sī., Syā.): paṭhavīkasiṇaṃ] वाला"),
    P_ARUPA: ARUPA_JH,
    P_LOK: LOK_JH,
    "rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ "
    "vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati pathavīkasiṇaṃ":
        f"कोई सूक्ष्म भौतिक लोक से संबंधित ध्यान का अभ्यास करता है, {KIRIYA_TAIL}, {DDSV}, इंद्रिय-सुखों से अलग होकर… "
        "पहले ध्यान को प्राप्त करके उसमें रहता है, जो पृथ्वी के ध्यान-मंडल वाला है",  # PI1 ^1-577
    "arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ "
    "sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… "
    "catutthaṃ jhānaṃ upasampajja viharati":
        f"कोई अभौतिक लोक से संबंधित ध्यान का अभ्यास करता है, {KIRIYA_TAIL}, {DDSV}, कुछ भी न होने के क्षेत्र को "
        "पूरी तरह पार करके, सुख को छोड़ने से… न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाले चौथे ध्यान "
        "को प्राप्त करके उसमें रहता है",
}
TASSEVA = {
    "rūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja "
    "viharati pathavīkasiṇaṃ":
        "उसी सूक्ष्म भौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण जिस समय वह इंद्रिय-सुखों से "
        "अलग होकर… कर्म-फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है, जो पृथ्वी के ध्यान-मंडल वाला है",
    "arūpāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ sabbaso ākiñcaññāyatanaṃ samatikkamma "
    "nevasaññānāsaññāyatanasaññāsahagataṃ sukhassa ca pahānā…pe… catutthaṃ jhānaṃ upasampajja viharati":
        "उसी अभौतिक लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण जिस समय वह कुछ भी न होने के क्षेत्र को "
        "पूरी तरह पार करके, सुख को छोड़ने से… कर्म-फल रूपी और न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाले "
        "चौथे ध्यान को प्राप्त करके उसमें रहता है",
    "lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja "
    "viharati dukkhapaṭipadaṃ dandhābhiññaṃ":
        "उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण जिस समय वह इंद्रिय-सुखों से अलग होकर… "
        "कर्म-फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है",
}
TASSEVA["lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ "
        "upasampajja viharati dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ"] = (
    "उसी लोकोत्तर हितकर ध्यान के किए जाने और अभ्यास किए जाने के कारण जिस समय वह इंद्रिय-सुखों से अलग होकर… "
    "कर्म-फल रूपी पहले ध्यान को प्राप्त करके उसमें रहता है, जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला और शून्य होता है")

HEADS = [  # (Pāli prefix, Hindi, gender of the subject)
    ("akusalaṃ cittaṃ uppannaṃ hoti", "हानिकर मन उत्पन्न होता है", "m"),
    ("kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti", "इंद्रिय-सुखों के लोक से संबंधित हितकर मन उत्पन्न होता है", "m"),
]
VIPAKA_PRE = [
    ("kāmāvacarassa kusalassa kammassa katattā upacitattā vipākaṃ ",
     "इंद्रिय-सुखों के लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण कर्म-फल रूपी "),
    ("kāmāvacarassa kusalassa kammassa katattā upacitattā vipākā ",
     "इंद्रिय-सुखों के लोक से संबंधित हितकर कर्म किए जाने और संचित होने के कारण कर्म-फल रूपी "),
    ("akusalassa kammassa katattā upacitattā vipākaṃ ", "हानिकर कर्म किए जाने और संचित होने के कारण कर्म-फल रूपी "),
    ("akusalassa kammassa katattā upacitattā vipākā ", "हानिकर कर्म किए जाने और संचित होने के कारण कर्म-फल रूपी "),
]
SUBJ = [
    ("cakkhuviññāṇaṃ uppannaṃ hoti", "आँख की चेतना उत्पन्न होती है", "f"),
    ("sotaviññāṇaṃ uppannaṃ hoti", "कान की चेतना उत्पन्न होती है", "f"),
    ("ghānaviññāṇaṃ uppannaṃ hoti", "नाक की चेतना उत्पन्न होती है", "f"),
    ("jivhāviññāṇaṃ uppannaṃ hoti", "जीभ की चेतना उत्पन्न होती है", "f"),
    ("kāyaviññāṇaṃ uppannaṃ hoti", "शरीर की चेतना उत्पन्न होती है", "f"),
    ("manoviññāṇadhātu uppannā hoti", "मन की चेतना का तत्व उत्पन्न होता है", "m"),
    ("manodhātu uppannā hoti", "मन का तत्व उत्पन्न होता है", "m"),
]
SAHA = {"somanassa": "प्रसन्नता के साथ होने वाला", "upekkhā": "समभाव के साथ होने वाला",
        "domanassa": "उदासी के साथ होने वाला", "sukha": "सुख के साथ होने वाला", "dukkha": "दुःख के साथ होने वाला"}
SAMP = {"diṭṭhigatasampayutt": "ग़लत दृष्टि से जुड़ा", "diṭṭhigatavippayutt": "ग़लत दृष्टि से अलग",
        "paṭighasampayutt": "चिढ़ से जुड़ा", "vicikicchāsampayutt": "संशय से जुड़ा",
        "uddhaccasampayutt": "बेचैनी से जुड़ा", "ñāṇasampayutt": "ज्ञान से जुड़ा", "ñāṇavippayutt": "ज्ञान से अलग"}
OBJ = {"rūp": "दृश्य रूप", "sadd": "ध्वनि", "gandh": "गंध", "ras": "स्वाद", "phoṭṭhabb": "स्पर्श",
       "dhamm": "मन का विषय"}
YAM = "या जिस किसी को भी वह विषय बनाए"


def fem(s, g):
    if g != "f":
        return s
    return s.replace("होने वाला", "होने वाली").replace("जुड़ा", "जुड़ी")


def fragment(fr, g):
    """One '…pe…'-separated piece of a mind-type opener -> (hindi, gender)."""
    out = []
    head = ""
    for p, h in VIPAKA_PRE:
        if fr.startswith(p):
            head, fr = h, fr[len(p):]
    for p, h, gg in HEADS + SUBJ:
        if fr.startswith(p):
            head, fr, g = head + h, fr[len(p):].strip(), gg
            break
    else:
        if head:
            raise KeyError(fr)
    if head:
        out.append(head)
    if fr.startswith("kiriyā neva kusalā nākusalā na ca kammavipākā"):
        out.append(", " + KIRIYA_TAIL)
        fr = fr[len("kiriyā neva kusalā nākusalā na ca kammavipākā"):].strip()
    words = fr.split()
    attrs = []
    while words and "ārammaṇ" not in words[0] and words[0] != "yaṃ":
        w = words.pop(0)
        if w == "sasaṅkhārena":
            attrs.append("प्रेरणा सहित")
        elif "sahagat" in w:
            attrs.append(SAHA[w.split("sahagat")[0]])
        else:
            key = next(k for k in SAMP if w.startswith(k))
            attrs.append(SAMP[key])
    attrs = [fem(a, g) for a in attrs]
    if attrs:
        if len(attrs) == 1:
            d = f"जो {attrs[0]} है"
        elif len(attrs) == 2:
            d = f"जो {attrs[0]} और {attrs[1]} {'होती' if g == 'f' else 'होता'} है"
        else:
            d = f"जो {', '.join(attrs[:-1])} और {attrs[-1]} {'होती' if g == 'f' else 'होता'} है"
        out.append((", " if out else "") + d)
    rest = " ".join(words)
    if rest:
        objs = re.findall(r"(\w+?)ārammaṇ[aā]ṃ?( vā)?", rest)
        first = not attrs and not head
        s = ""
        for i, (o, va) in enumerate(objs):
            name = OBJ[o]
            if first and i == 0:
                s += f"या {name}"
            elif i == 0:
                s += f" और जिसका विषय {name} {'हो' if va else 'है'}"
            else:
                s += f", या {name}"
        if rest.endswith("yaṃ yaṃ vā panārabbha"):
            s += f", {YAM}" if s else YAM
        out.append(s)
    return "".join(out), g


def opener(text):
    if text in JHANA:
        return "जिस समय " + JHANA[text]
    frs = re.split(r"…pe… ?", text)
    g = "m"
    hs = []
    for fr in frs:
        h, g = fragment(fr.strip(), g)
        hs.append(h)
    return "जिस समय " + "… ".join(hs)


def rest_of(text):
    """after 'tasmiṃ samaye '"""
    if text == "phasso hoti…pe… avikkhepo hoti – ime dhammā kusalā.":
        return "संपर्क होता है… भटकाव का अभाव होता है – ये हितकर परिघटनाएँ हैं।"
    m = re.match(r"^(.*)\. (Evametassa kevalassa dukkhakkhandhassa samudayo hoti|Evametesaṃ dhammānaṃ samudayo hoti)\.$",
                 text)
    return chain(m.group(1)) + VERB + "। " + DEFS[m.group(2)] + "।"


# =========================================================================== chunk translator
SPLIT = re.compile(r"(\? |\?$|…pe…\.$|…pe… ?| – |\. |\.$)")
DMAP = {"? ": "? ", "?": "?", "…pe….": "…।", " – ": " – ", ". ": "। ", ".": "।"}


def chunk(c, nxt):
    c = c.strip()
    if c in DEFS:
        return DEFS[c]
    m = re.match(r"^Ṭhapetvā (\w+), (.+)$", c)
    if m:
        ks = [KH4[w.strip(",")] for w in m.group(2).split()]
        return f"{THAPETVA[m.group(1)]} को छोड़कर, " + ", ".join(ks)
    m = re.match(r"^Tattha katam(?:o|ā|aṃ|e) (.+)$", c)
    if m:
        return question(m.group(1))
    m = re.match(r"^[Tt]ena vuccati \"?(evametassa kevalassa dukkhakkhandhassa|evametesaṃ dhammānaṃ) samudayo hot[iī]\"ti$", c)
    if m:
        if not c.split("vuccati ")[1].startswith('"'):
            SLIPS.append("opening quote missing before «evametassa…» in a «Tena vuccati» line (balanced in Hindi)")
        if c.endswith('hoti"ti'):
            SLIPS.append("«hoti\"ti» for «hotī\"ti» in a «tena vuccati» line")
        return TENA if "kevalassa" in c else TENA_DH
    m = re.match(r"^(?:ayaṃ|idaṃ|ime|Ayaṃ|Idaṃ|Ime) vucca(?:ti|nti)(?: (.+))?$", c)
    if m:
        if m.group(1) is None:   # 'ayaṃ vuccati – "X"' (dash before the quote)
            return "यह कहा जाता है"
        q = m.group(1).count('"')
        if q == 1:
            SLIPS.append(f"unbalanced quote in «{c}» (balanced in Hindi)")
        elif q == 0:
            SLIPS.append(f"quotes missing in «{c}» (quoted in Hindi like the rest of the chapter)")
        return called(m.group(1), True)
    m = re.match(r'^"([^"]+)"$', c)
    if m:
        return f"“{item(m.group(1))[0]}”"
    m = re.match(r"^Tasmiṃ samaye (.+)$", c)
    if m:
        return "उस समय " + chain(m.group(1)) + VERB
    if c.endswith(" sokaparidevadukkhadomanassupāyāsā sambhavanti"):
        h = chain(c[: -len(" sokaparidevadukkhadomanassupāyāsā sambhavanti")])
        assert h.endswith("बुढ़ापा और मृत्यु")
        return h[: -len("बुढ़ापा और मृत्यु")] + GRIEF + VERB
    if "paccayā" in c and re.search(r", |; ", c):
        return chain(c) + VERB
    m = re.match(r"^(\w+?paccayā(?:pi)?(?: \w+)+?)(?:n|)ti$", c)
    if m and (c.endswith("nti") or c.endswith("oti")):
        p = c[:-3] + "ṃ" if c.endswith("nti") else c[:-2]
        return f"“{item(p)[0]}” के विषय में"
    try:
        h = item(c)[0]
    except KeyError:
        UNKNOWN.append(c)
        return f"<<{c}>>"
    if nxt in ("? ", "?"):
        return h + " क्या है"
    return h


def tr_line(line):
    m = ID.search(line)
    bid = ""
    if m:
        bid = " " + m.group(1)
        line = line[: m.start()]
    line = line.strip().replace(" …pe…", "…pe…")
    if line in HEAD:
        return HEAD[line] + bid
    if line in CLOSE:
        return CLOSE[line] + bid
    m = re.match(r"^Katame dhammā (akusalā|kusalā|abyākatā)\? Yasmiṃ samaye (.+?), tasmiṃ samaye (.+)$", line)
    if m:
        return f"{KIND[m.group(1)]} परिघटनाएँ कौन-सी हैं? {opener(m.group(2))}, उस समय {rest_of(m.group(3))}" + bid
    m = re.match(r"^Tasseva (.+?), tasmiṃ samaye (.+)$", line)
    if m:
        return f"{TASSEVA[m.group(1)]}, उस समय {rest_of(m.group(2))}" + bid
    line = re.sub(r"\[[^\]]*\]", lambda b: b.group(0).replace(".", "\x00"), line)  # no splits inside variants
    parts = [p.replace("\x00", ".") for p in SPLIT.split(line)]
    out = []
    for i in range(0, len(parts), 2):
        c = parts[i]
        d = parts[i + 1] if i + 1 < len(parts) else ""
        if c.strip():
            out.append(chunk(c, d))
        if d:
            if d.startswith("…pe…") and d != "…pe….":
                out.append("…" if i + 2 >= len(parts) or not parts[i + 2].strip() else "… ")
            else:
                out.append(DMAP[d])
    return "".join(out).replace("  ", " ") + bid


def main():
    src = SRC.read_text(encoding="utf-8").replace("\r", "")
    blocks = [b for b in re.split(r"\n\s*\n", src) if b.strip()]
    res = []
    for b in blocks:
        res.append("\n".join(tr_line(l) for l in b.split("\n") if l.strip()))
    text = "\n\n".join(res) + "\n"
    if UNKNOWN:
        print("UNKNOWN chunks:")
        for u in dict.fromkeys(UNKNOWN):
            print("  ", u)
        sys.exit(1)
    DST.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", DST, "blocks", len(blocks))
    for s in dict.fromkeys(SLIPS):
        print("SLIP:", s)


if __name__ == "__main__":
    main()
