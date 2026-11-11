"""Build the Hindi plain zero-shot of pi-1 part 2-04 (the twelve unwholesome minds; results of the wholesome).

usage: python -I -X utf8 build_2-04_hi.py
Mirrors the English builder (pi-1-en/build_2-04.py + const_2_03_2_04.py): every Pāli line is parsed into
its formula pieces and rebuilt from fixed Hindi constants, so every repeat is byte-identical.
Imports the approved matrix and chapter-2 sample builders (importing them writes nothing).
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
import build_matika_hi as M  # noqa: E402
import build_ch2_01_sample_hi as C  # noqa: E402

PART = "2-04-cittuppadakandam.md"
PALI_DIR = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
OUT_DIR = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-zeroshot_split_chapters"
DASH = C.DASH
DANDA = M.DANDA
PE = "…pe…"
ELL = "…"
V = C.V

KIND = {"kusalā": C.KUSALA, "akusalā": C.AKUSALA, "abyākatā": C.ABYAKATA}

# ---- factor names (sample + new) ---------------------------------------------------------------
MA, FE = C.M, C.F
N = dict(C.NAMES)
G = dict(C.GENDER)
NEW_NAMES = {
    "micchādiṭṭhi": ("ग़लत दृष्टि", FE),
    "micchāsaṅkappo": ("ग़लत संकल्प", MA),
    "micchāvāyāmo": ("ग़लत प्रयास", MA),
    "micchāsamādhi": ("ग़लत एकाग्रता", FE),
    "ahirikabalaṃ": ("निर्लज्जता का बल", MA),
    "anottappabalaṃ": ("बुराई के प्रति निडरता का बल", MA),
    "lobho": ("लोभ", MA),
    "moho": ("मोह", MA),
    "abhijjhā": ("लालच", MA),
    "ahirikaṃ": ("निर्लज्जता", FE),
    "anottappaṃ": ("बुराई के प्रति निडरता", FE),
    "upekkhā": ("समभाव", MA),
    "upekkhindriyaṃ": ("समभाव की क्षमता", FE),
    "dukkhaṃ": ("दुःख", MA),
    "domanassindriyaṃ": ("उदासी की क्षमता", FE),
    "doso": ("द्वेष", MA),
    "byāpādo": ("दुर्भावना", FE),
    "vicikicchā": ("संशय", MA),
    "uddhaccaṃ": ("बेचैनी", FE),
    "sukhindriyaṃ": ("सुख की क्षमता", FE),
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", MA),
}
for k, (hi, g) in NEW_NAMES.items():
    assert k not in N, k
    N[k], G[k] = hi, g
# the matrix wording of ahirika / anottappa (^1-M2-115) and the core terms of the terms file
assert M.BARE[("1-M2-115", "क")] == N["ahirikaṃ"] and M.BARE[("1-M2-115", "ख")] == N["anottappaṃ"]


def LIST_ITEM(k):
    return f"{N[k]} {C.HOTI[G[k]]}"


assert all(LIST_ITEM(k) == C.LIST_ITEM(k) for k in C.NAMES)

# ---- synonym strings ------------------------------------------------------------------------------
UNROOT = "हानिकर मूल"
ABY_ROOT = "नैतिक रूप से अनिर्धारित मूल"


def strip_end(s, tail):
    assert s.endswith(tail), (s, tail)
    return s[: -len(tail)]


BASES = dict(C.STRINGS)
_VIT = "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā"
_SAM = ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho "
        "samādhindriyaṃ samādhibalaṃ")
_VIR = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
        "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ "
        "vīriyindriyaṃ vīriyabalaṃ")
BASES[_VIT] = strip_end(C.S_VITAKKA, ", " + N["sammāsaṅkappo"])
BASES[_SAM] = strip_end(C.S_SAMADHI, ", " + N["sammāsamādhi"])
BASES[_VIR] = strip_end(C.S_VIRIYA, ", " + N["sammāvāyāmo"])
BASES["cittassa ṭhiti"] = "मन की स्थिरता"
assert C.S_SAMADHI.startswith(BASES["cittassa ṭhiti"] + ",")

# feeling strings, built on the pattern of the approved sukha string (S_SUKHA)
# as build_2-01_2-02_hi.py (S_UPEKKHA), which defines this string first
S_UPEKKHA = ("न सुहावना, न असुहावना मानसिक भाव, मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभव, "
             "मन के संपर्क से उत्पन्न न दुःखद, न सुखद अनुभूति")
S_DUKKHA = ("मानसिक असुहावनापन, मानसिक दुःख, मन के संपर्क से उत्पन्न असुहावना, दुःखद अनुभव, "
            "मन के संपर्क से उत्पन्न असुहावनी, दुःखद अनुभूति")
S_KAYASUKHA = ("शारीरिक सुहावनापन, शारीरिक सुख, शरीर के संपर्क से उत्पन्न सुहावना, सुखद अनुभव, "
               "शरीर के संपर्क से उत्पन्न सुहावनी, सुखद अनुभूति")
assert C.S_SUKHA == ("मानसिक सुहावनापन, मानसिक सुख, मन के संपर्क से उत्पन्न सुहावना, सुखद अनुभव, "
                     "मन के संपर्क से उत्पन्न सुहावनी, सुखद अनुभूति")
# diṭṭhi string: the approved Hindi pi-4 (^4-62), with ग़लत धारणा for parāmāso (matrix ^1-M2-50)
S_DITTHI = ("दृष्टि, दृष्टि में पड़ जाना, दृष्टि का घना जंगल, दृष्टि का बीहड़, दृष्टि का टेढ़ापन, "
            "दृष्टि की छटपटाहट, दृष्टि का बंधन, पकड़, कसकर पकड़ना, आग्रह, ग़लत धारणा, कुमार्ग, "
            "ग़लत रास्ता, ग़लतपन, मतवादों का अड्डा, उलटी पकड़")
S_DITTHI_V = (S_DITTHI.replace("कसकर पकड़ना,", "कसकर पकड़ना" + V("p", "Sī., Syā.", "paṭiggāho") + ",", 1)
              + V("s", "Ka.", "vipariyesagāho"))
assert S_DITTHI_V.count("[") == 2
# lobha string: the approved alobha string (^1-32) turned positive, with हानिकर मूल
S_LOBHA = "लोभ, लोभ करना, लोभ से भरा होना, राग, राग करना, राग से भरा होना, लालच, लोभ, " + UNROOT
# moha string: the approved Hindi pi-4 (^4-60), with जकड़न for yoga (matrix) and हानिकर मूल
S_MOHA = ("न जानना, न देखना, सत्य तक न पहुँचना, बोध न होना, पूर्ण बोध न होना, भेद न पाना, न समेट पाना, "
          "गहराई में न उतर पाना, निष्पक्ष रूप से न देखना, पुनः विचार न करना, प्रत्यक्ष न करना, दुर्बुद्धि, "
          "मूर्खता, स्पष्ट समझ का अभाव, मोह, गहरा मोह, घोर मोह, अज्ञान, अज्ञान की बाढ़, अज्ञान की जकड़न, "
          "अज्ञान की सुप्त प्रवृत्ति, अज्ञान का आवेश, अज्ञान की रुकावट, मोह, " + UNROOT)
assert S_MOHA.count(",") == 24
# dosa string: the approved Hindi pi-4 (^4-45) verbatim from द्वेष on
S_DOSA = ("द्वेष, द्वेष करना, द्वेष से भरा होना, दुर्भावना, दुर्भावना रखना, दुर्भावना से भरा होना, विरोध, "
          "प्रतिविरोध, उग्रता, कटु वचन, मन की अप्रसन्नता")
S_VICIKICCHA = ("शंका, शंका करना, शंका से भरा होना, दुविधा, संशय, दुचित्तापन, दोराहा, संदेह, "
                "किसी एक बात को न पकड़ पाना, हिचकना, डगमगाना, गहराई में न उतर पाना, मन का जड़ हो जाना, "
                "मन की खरोंच")
assert S_VICIKICCHA.count(",") == 13
S_UDDHACCA = "मन की बेचैनी, अशांति, मन का भटकाव, मन का डोलना"
# ahirika / anottappa: the approved pi-4 wording (^4-53/54) in the form of the sample's hirī / ottappa strings
S_AHIRIKA = "जिस बात पर लज्जा आनी चाहिए, उस पर लज्जा न आना, बुरी और हानिकर परिघटनाओं को अपनाने पर लज्जा न आना"
S_ANOTTAPPA = "जिस बात से डरना चाहिए, उससे न डरना, बुरी और हानिकर परिघटनाओं को अपनाने से न डरना"
assert C.S_HIRI.replace("लज्जा आना", "लज्जा न आना") == S_AHIRIKA
assert C.S_OTTAPPA.replace("उससे डरना", "उससे न डरना").replace("अपनाने से डरना", "अपनाने से न डरना") == S_ANOTTAPPA

_CITTA_PI = "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho"
_CITTA_HI = strip_end(C.S_CITTA, ", उसके अनुरूप मन की चेतना का तत्व")

BASES.update({
    "cetasikaṃ neva sātaṃ nāsātaṃ cetosamphassajaṃ adukkhamasukhaṃ vedayitaṃ cetosamphassajā adukkhamasukhā vedanā":
        S_UPEKKHA,
    "cetasikaṃ asātaṃ cetasikaṃ dukkhaṃ cetosamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ cetosamphassajā asātā dukkhā vedanā":
        S_DUKKHA,
    "kāyikaṃ sātaṃ kāyikaṃ sukhaṃ kāyasamphassajaṃ sātaṃ sukhaṃ vedayitaṃ kāyasamphassajā sātā sukhā vedanā":
        S_KAYASUKHA,
    "diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ "
    "gāho patiṭṭhāho abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ vipariyāsaggāho":
        S_DITTHI,
    "diṭṭhi diṭṭhigataṃ diṭṭhigahanaṃ diṭṭhikantāro diṭṭhivisūkāyikaṃ diṭṭhivipphanditaṃ diṭṭhisaṃyojanaṃ "
    "gāho patiṭṭhāho [paṭiggāho (sī. syā.)] abhiniveso parāmāso kummaggo micchāpatho micchattaṃ titthāyatanaṃ "
    "vipariyāsaggāho [vipariyesagāho (ka.)]":
        S_DITTHI_V,
    "lobho lubbhanā lubbhitattaṃ sārāgo sārajjanā sārajjitattaṃ abhijjhā lobho akusalamūlaṃ": S_LOBHA,
    "aññāṇaṃ adassanaṃ anabhisamayo ananubodho asambodho appaṭivedho asaṃgāhanā apariyogāhanā asamapekkhanā "
    "apaccavekkhanā apaccakkhakammaṃ dummejjhaṃ bālyaṃ asampajaññaṃ moho pamoho sammoho avijjā avijjogho "
    "avijjāyogo avijjānusayo avijjāpariyuṭṭhānaṃ avijjālaṅgī moho akusalamūlaṃ": S_MOHA,
    "doso dussanā dussitattaṃ byāpatti byāpajjanā byāpajjitattaṃ virodho paṭivirodho caṇḍikkaṃ asuropo "
    "anattamanatā cittassa": S_DOSA,
    "kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā dveḷhakaṃ dvedhāpatho saṃsayo anekaṃsaggāho "
    "āsappanā parisappanā apariyogāhanā thambhitattaṃ cittassa manovilekho": S_VICIKICCHA,
    "cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa": S_UDDHACCA,
    "na hirīyati hiriyitabbena na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": S_AHIRIKA,
    "na ottappati ottappitabbena na ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā": S_ANOTTAPPA,
    _CITTA_PI + " tajjācakkhuviññāṇadhātu": _CITTA_HI + ", उसके अनुरूप आँख की चेतना का तत्व",
    _CITTA_PI + " tajjākāyaviññāṇadhātu": _CITTA_HI + ", उसके अनुरूप शरीर की चेतना का तत्व",
    _CITTA_PI + " tajjāmanodhātu": _CITTA_HI + ", उसके अनुरूप मन का तत्व",
})
SHAME_STRINGS = {C.S_HIRI, C.S_OTTAPPA, S_AHIRIKA, S_ANOTTAPPA}

TOKENS = {
    "micchāsaṅkappo": N["micchāsaṅkappo"],
    "micchāsamādhi": N["micchāsamādhi"],
    "micchāvāyāmo": N["micchāvāyāmo"],
    "sammāsaṅkappo": N["sammāsaṅkappo"],
    "sammāsamādhi": N["sammāsamādhi"],
    "sammāvāyāmo": N["sammāvāyāmo"],
}


def tr_string(pi):
    """A bare synonym string: the longest matching base plus suffix tokens."""
    best = None
    for k in BASES:
        if pi == k or pi.startswith(k + " "):
            if best is None or len(k) > len(best):
                best = k
    if best is None:
        raise KeyError("no base for: " + pi)
    out = [BASES[best]]
    rest = pi[len(best):].strip()
    while rest:
        for t in sorted(TOKENS, key=len, reverse=True):
            if rest == t or rest.startswith(t + " "):
                out.append(TOKENS[t])
                rest = rest[len(t):].strip()
                break
        else:
            raise KeyError(f"unknown token at: {rest!r} (in {pi!r})")
    return ", ".join(out)


# ---- frame qualifiers -------------------------------------------------------------------------------
def TAJJA_OF(element):
    return f"उसके अनुरूप {element} के संपर्क से उत्पन्न"


assert TAJJA_OF("मन की चेतना के तत्व") == C.TAJJA
PREFIXES = [
    (r"tajjāmanoviññāṇadhātusamphassaj(?:aṃ|ā) ", C.TAJJA),
    (r"tajjācakkhuviññāṇadhātusamphassaj(?:aṃ|ā) ", TAJJA_OF("आँख की चेतना के तत्व")),
    (r"tajjākāyaviññāṇadhātusamphassaj(?:aṃ|ā) ", TAJJA_OF("शरीर की चेतना के तत्व")),
    (r"tajjāmanodhātusamphassaj(?:aṃ|ā) ", TAJJA_OF("मन के तत्व")),
    (r"vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa ", C.G_KAYA),
    (r"viññāṇakkhandhassa ", C.G_CITTA),
]

# ---- closing formulas ---------------------------------------------------------------------------------
YEV_PI = "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā "


def YEV(kind):
    return C.YEVAPANA(KIND[kind])


assert "या " + YEV("kusalā") == C.FRAMES["Ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino "
                                         "dhammā – ime dhammā kusalā."]


def ell_end(s):
    """'…।' for a Pāli '…pe….' ending."""
    assert s.endswith(DANDA), s
    return s[:-1] + ELL + DANDA


def tr_tail(t):
    """Tail after '... X hoti' at the end of an answer or list (Hindi starts right after 'है')."""
    t = t.replace(" " + PE, PE)
    if t == ".":
        return DANDA
    if t == "?":
        return "?"
    if t == PE + ".":
        return ELL + DANDA
    m = re.fullmatch(r"(;|…pe…) " + re.escape(YEV_PI) + r"(kusalā|akusalā|abyākatā)(\.|…pe…\.)", t)
    if m:
        lead = "; या " if m.group(1) == ";" else ELL + " या "
        s = lead + YEV(m.group(2))
        return s if m.group(3) == "." else ell_end(s)
    m = re.fullmatch(r"…pe… ime dhammā (kusalā|akusalā|abyākatā)\.", t)
    if m:
        return ELL + " " + M.ANSWER(KIND[m.group(1)])
    raise ValueError("unknown tail: " + repr(t))


# ---- question / answer lines -----------------------------------------------------------------------------
QA_RX = re.compile(r"Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti([?.]) Y(?:o|ā|aṃ) (.*?) – (?:ayaṃ|idaṃ) "
                   r"tasmiṃ samaye (\S+) hoti(.*)")


def tr_qa(line):
    m = QA_RX.fullmatch(line)
    if not m:
        return None
    key, qmark, body, key2, tail = m.groups()
    assert key == key2, line
    x = N[key]
    q = C.Q(x)
    if qmark == ".":  # ^1-473: the Pāli question ends with "." (kept)
        q = q[:-1] + DANDA
    if body.startswith("tasmiṃ samaye "):
        body = body[len("tasmiṃ samaye "):]
        pre = ""
        for rx, hi in PREFIXES:
            mm = re.match(rx, body)
            if mm:
                body = body[mm.end():]
                pre = hi + " "
                break
        s = tr_string(body)
        if s in SHAME_STRINGS:
            assert not pre
            a = f"उस समय {s} {DASH} यह उस समय {x} है"
        else:
            a = C.A(s, x, pre)[:-1]
    elif body.startswith("tesaṃ arūpīnaṃ dhammānaṃ "):
        s = tr_string(body[len("tesaṃ arūpīnaṃ dhammānaṃ "):])
        a = f"{C.G_JIVITA} जो {s} है {DASH} यह उस समय {x} है"
    else:
        raise ValueError("unknown answer body: " + body)
    return q + " " + a + tr_tail(tail)


# the sample's frames, rebuilt here, must come out identical
assert tr_qa("Katamo tasmiṃ samaye phasso hoti? Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – "
             "ayaṃ tasmiṃ samaye phasso hoti.") == C.QA("phasso", C.S_PHASSA)
assert tr_qa("Katamā tasmiṃ samaye saññā hoti? Yā tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajā saññā "
             "sañjānanā sañjānitattaṃ – ayaṃ tasmiṃ samaye saññā hoti.") == C.T("saññā", C.S_SANNA)
assert tr_qa("Katamaṃ tasmiṃ samaye jīvitindriyaṃ hoti? Yo tesaṃ arūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā "
             "iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ – idaṃ tasmiṃ samaye jīvitindriyaṃ hoti.") == \
    C.JIVITA("jīvitindriyaṃ", C.S_JIVITA)


# ---- 'Katamo tasmiṃ samaye saṅkhārakkhandho hoti? Phasso cetanā …' ------------------------------------
KOTTHASA_RX = re.compile(r"Katamo tasmiṃ samaye saṅkhārakkhandho hoti\? (.*?); " + re.escape(
    "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā ṭhapetvā vedanākkhandhaṃ "
    "ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti")
    + r"(.*)")
EXCEPT = "अनुभूति के समूह को छोड़कर, पहचान के समूह को छोड़कर, चेतना के समूह को छोड़कर"
assert C.YEVAPANA_BODY.startswith("उस समय ")


def bare_list(pali):
    return ", ".join(N[k[0].lower() + k[1:]] for k in pali.split(" "))


def tr_kotthasa(line):
    m = KOTTHASA_RX.fullmatch(line)
    if not m:
        return None
    x = N["saṅkhārakkhandho"]
    # Pāli order, as build_2-03_hi.py: «या उस समय जो भी … होती हैं, <EXCEPT> – यह उस समय X है»
    return (C.Q(x) + " " + bare_list(m.group(1)) + "; या " + C.YEVAPANA_BODY + ", " + EXCEPT
            + f" {DASH} यह उस समय {x} है" + tr_tail(m.group(2)))


# ---- 'Tasmiṃ kho pana samaye cattāro khandhā honti, …' ----------------------------------------------------
SANGAHA_ITEMS = {
    "cattāro khandhā honti": "चार समूह होते हैं",
    "dvāyatanāni honti": "दो इंद्रिय-क्षेत्र होते हैं",
    "dve dhātuyo honti": "दो तत्व होते हैं",
    "tayo āhārā honti": "तीन आहार होते हैं",
    "pañcindriyāni honti": "पाँच क्षमताएँ होती हैं",
    "cattāri indriyāni honti": "चार क्षमताएँ होती हैं",
    "tīṇindriyāni honti": "तीन क्षमताएँ होती हैं",
    "pañcaṅgikaṃ jhānaṃ hoti": "पाँच अंगों वाला ध्यान होता है",
    "caturaṅgikaṃ jhānaṃ hoti": "चार अंगों वाला ध्यान होता है",
    "caturaṅgiko maggo hoti": "चार अंगों वाला मार्ग होता है",
    "tivaṅgiko maggo hoti": "तीन अंगों वाला मार्ग होता है",
    "duvaṅgiko maggo hoti": "दो अंगों वाला मार्ग होता है",
    "cattāri balāni honti": "चार बल होते हैं",
    "tīṇi balāni honti": "तीन बल होते हैं",
    "dve hetū honti": "दो मूल होते हैं",
    "eko hetu hoti": "एक मूल होता है",
    "eko phasso hoti": "एक संपर्क होता है",
    # word order «एक X होता है» as in build_2-03_hi.py (eko phasso … ekā dhammadhātu)
    "ekā cakkhuviññāṇadhātu hoti": "एक आँख की चेतना का तत्व होता है",
    "ekā kāyaviññāṇadhātu hoti": "एक शरीर की चेतना का तत्व होता है",
    "ekā manodhātu hoti": "एक मन का तत्व होता है",
    "ekā manoviññāṇadhātu hoti": "एक मन की चेतना का तत्व होता है",
    "ekaṃ dhammāyatanaṃ hoti": "एक मन के विषयों का इंद्रिय-क्षेत्र होता है",
    "ekā dhammadhātu hoti": "एक मन के विषयों का तत्व होता है",
}
SANGAHA_HEAD_PI = "Tasmiṃ kho pana samaye "
SANGAHA_HEAD = "और उस समय "


def tr_sangaha(line):
    if not line.startswith(SANGAHA_HEAD_PI + "cattāro khandhā honti"):
        return None
    body, tail = line[len(SANGAHA_HEAD_PI):].split("; ", 1)
    parts = []
    for item in body.split(", "):
        parts.append((ELL + " ").join(SANGAHA_ITEMS[x.strip()] for x in item.split(PE)))
    return SANGAHA_HEAD + ", ".join(parts) + tr_tail("; " + tail)


# ---- object strings of the opening sentences ---------------------------------------------------------------
ARAM_FULL = C.ARAMMANA
ARAM_VISIBLE = "जिसका विषय दृश्य रूप हो"
ARAM_ANY = "या चाहे वह जिस किसी को भी विषय बनाए"
assert ARAM_FULL.startswith(ARAM_VISIBLE + ", ") and ARAM_FULL.endswith(", " + ARAM_ANY)
assert ", या मन का विषय, " in ARAM_FULL and ", या स्पर्श, " in ARAM_FULL
ARAM_ABBR = f"{ARAM_VISIBLE}{ELL} या मन का विषय, {ARAM_ANY}"        # rūpa…pe… dhamma… yaṃ yaṃ
ARAM_ABBR_TOUCH = f"{ARAM_VISIBLE}{ELL} या स्पर्श, {ARAM_ANY}"      # rūpa…pe… phoṭṭhabba… yaṃ yaṃ
ARAM_ABBR_ANY = f"{ARAM_VISIBLE}{ELL} {ARAM_ANY}"                   # rūpa…pe… yaṃ yaṃ
PROMPTED = "जो प्रेरणा के साथ उत्पन्न होता है"  # sasaṅkhārena, as build_2-01_2-02_hi.py

# ---- opening sentences: 'Katame dhammā K? Yasmiṃ samaye <clause>, tasmiṃ samaye <rest>' ----------------------
OPEN_RX = re.compile(r"Katame dhammā (kusalā|akusalā|abyākatā)\? Yasmiṃ samaye (.*?), tasmiṃ samaye (.*)")
PIECES = {
    "ime dhammā kusalā": M.ANSWER_BARE(C.KUSALA),
    "ime dhammā akusalā": M.ANSWER_BARE(C.AKUSALA),
    "ime dhammā abyākatā": M.ANSWER_BARE(C.ABYAKATA),
    "alobho abyākatamūlaṃ": f"{N['alobho']}, {ABY_ROOT}",
    "adoso abyākatamūlaṃ": f"{N['adoso']}, {ABY_ROOT}",
}


def tr_rest(rest):
    """The part after 'tasmiṃ samaye' in an opening sentence -> 'उस समय …'."""
    if "; " + YEV_PI in rest:
        lst, tail = rest.split("; ", 1)
        items = lst.split(" hoti, ")
        assert items[-1].endswith(" hoti"), lst
        items[-1] = items[-1][: -len(" hoti")]
        return "उस समय " + ", ".join(LIST_ITEM(k) for k in items) + tr_tail("; " + tail)
    end = DANDA
    if rest.endswith(PE + "."):
        rest, end = rest[: -len(PE + ".")], ELL + DANDA
    else:
        assert rest.endswith("."), rest
        rest = rest[:-1]
    out = []
    for p in rest.split(PE):
        p = p.strip()
        if p.endswith(" hoti"):
            out.append(LIST_ITEM(p[: -len(" hoti")]))
        else:
            out.append(PIECES[p])
    return "उस समय " + (ELL + " ").join(out) + end


def tr_opening(line, clause_hi):
    m = OPEN_RX.fullmatch(line)
    assert m, line
    kind, _clause_pi, rest = m.groups()
    return f"{M.QUESTION(KIND[kind])} {clause_hi}, " + tr_rest(rest)


# the sample's ^1-1 must come out identical (apart from its variant brackets)
_L11 = ("Katame dhammā kusalā? Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ "
        "ñāṇasampayuttaṃ rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ "
        "vā dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha, tasmiṃ samaye "
        + ", ".join(f"{k} hoti" for k, _ in C.LIST_1_1) + "; " + YEV_PI + "kusalā.")
assert tr_opening(_L11, C.OPEN_KAMA_KUSALA + ", " + C.ACC_SOMA_NANA + ", " + ARAM_FULL) == \
    re.sub(r" \[[^\]]*\]", "", C.SEG_1_1)

# ---- the twelve unwholesome minds ------------------------------------------------------------------------------
OPEN_UNW = "जिस समय हानिकर मन उत्पन्न होता है"
JOY, EQU, SAD = "प्रसन्नता", "समभाव", "उदासी"
W_ASSOC = "ग़लत दृष्टि से जुड़ा"
W_DISS = "ग़लत दृष्टि से अलग"
assert C.ACC_SOMA_NANA == f"जो {JOY} के साथ होता है और ज्ञान से जुड़ा होता है"


def ACC(acc, assoc):
    return f"जो {acc} के साथ होता है और {assoc} होता है"


def U(acc, assoc, aram, prompted=False):
    return OPEN_UNW + ", " + ACC(acc, assoc) + ", " + (PROMPTED + ", " if prompted else "") + aram


# ---- results of the wholesome of the sense sphere --------------------------------------------------------------
# same shape as the unwholesome results in build_2-05_hi.py (AKUS_KAMMA) and as RES_OF below
RES_KAMA = ("जिस समय इंद्रिय-सुखों के लोक से संबंधित हितकर कर्म के किए जाने और संचित होने के कारण, "
            "उसके फल के रूप में, ")
KNOW_A = "ज्ञान से जुड़ा"
KNOW_D = "ज्ञान से अलग"
assert ACC(JOY, KNOW_A) == C.ACC_SOMA_NANA


def VINN(acc, obj):
    """'upekkhāsahagataṃ rūpārammaṇaṃ' after a viññāṇa (feminine), as build_2-05_hi.py."""
    return f"जो {acc} के साथ होती है और जिसका विषय {obj} है"


EIGHT = (ELL + " ").join(
    ACC(acc, kn) + (", " + PROMPTED if pr else "")
    for acc in (JOY, EQU) for kn in (KNOW_A, KNOW_D) for pr in (False, True))

OPEN = {
    "1-365": U(JOY, W_ASSOC, ARAM_FULL),
    "1-399": U(JOY, W_ASSOC, ARAM_ABBR, True),
    "1-400": U(JOY, W_DISS, ARAM_FULL),
    "1-402": U(JOY, W_DISS, ARAM_ABBR, True),
    "1-403": U(EQU, W_ASSOC, ARAM_FULL),
    "1-409": U(EQU, W_ASSOC, ARAM_ABBR, True),
    "1-410": U(EQU, W_DISS, ARAM_FULL),
    "1-412": U(EQU, W_DISS, ARAM_ABBR, True),
    "1-413": U(SAD, "चिढ़ से जुड़ा", ARAM_FULL),
    "1-421": U(SAD, "चिढ़ से जुड़ा", ARAM_ABBR, True),
    "1-422": U(EQU, "संशय से जुड़ा", ARAM_FULL),
    "1-427": U(EQU, "बेचैनी से जुड़ा", ARAM_ABBR_ANY),
    "1-431": RES_KAMA + "आँख की चेतना उत्पन्न होती है, " + VINN(EQU, "दृश्य रूप"),
    "1-443": (RES_KAMA + "कान की चेतना उत्पन्न होती है, " + VINN(EQU, "ध्वनि")
              + f"{ELL} नाक की चेतना उत्पन्न होती है, " + VINN(EQU, "गंध")
              + f"{ELL} जीभ की चेतना उत्पन्न होती है, " + VINN(EQU, "स्वाद")
              + f"{ELL} शरीर की चेतना उत्पन्न होती है, " + VINN("सुख", "स्पर्श")),
    "1-455": RES_KAMA + "मन का तत्व उत्पन्न होता है, " + f"जो {EQU} के साथ होता है, " + ARAM_ABBR_TOUCH,
    "1-469": RES_KAMA + "मन की चेतना का तत्व उत्पन्न होता है, " + f"जो {JOY} के साथ होता है, " + ARAM_ABBR,
    "1-484": RES_KAMA + "मन की चेतना का तत्व उत्पन्न होता है, " + f"जो {EQU} के साथ होता है, " + ARAM_ABBR,
    "1-498": RES_KAMA + "मन की चेतना का तत्व उत्पन्न होता है, " + EIGHT + ", " + ARAM_ABBR,
}

# ---- results of the fine-material and immaterial spheres (two sentences on one line) ----------------------------
# intro, absorption and immaterial phrases as build_2-01_2-02_hi.py (INTROS, PH)
FM_PATH = "सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है"
IM_PATH = "अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है"
EARTH = "पृथ्वी के ध्यान-मंडल को आधार बनाकर"
DWELL = "को प्राप्त करके उसमें रहता है"
J1 = f"इंद्रिय-सुखों से अलग होकर{ELL} पहले ध्यान {DWELL}"
J5 = (f"आरंभिक विचार और सतत विचार के शांत होने से{ELL} दूसरे ध्यान को{ELL} तीसरे ध्यान को{ELL} "
      f"चौथे ध्यान को{ELL} पहले ध्यान को{ELL} पाँचवें ध्यान {DWELL}")
J5_PLEASURE = f"सुख के त्याग से{ELL} पाँचवें ध्यान {DWELL}"
J4_PLEASURE = f"सुख के त्याग से{ELL} चौथे ध्यान {DWELL}"
ABBR_LIST_END = f", उस समय {LIST_ITEM('phasso')}{ELL} {LIST_ITEM('avikkhepo')}{ELL} "
WHOLESOME_END = ABBR_LIST_END + M.ANSWER(C.KUSALA)
RESULT_END = ABBR_LIST_END + M.ANSWER(C.ABYAKATA)
assert tr_rest("phasso hoti…pe… avikkhepo hoti…pe… ime dhammā kusalā.") == WHOLESOME_END[2:]


def RES_OF(sphere):
    return f"{sphere} उसी हितकर कर्म के किए जाने और संचित होने के कारण, उसके फल के रूप में, जब वह "


Q_ABY = M.QUESTION(C.ABYAKATA)


def FM(jh_kusala, jh_result):
    return (f"{Q_ABY} जिस समय कोई {FM_PATH} और {jh_kusala}, {EARTH}" + WHOLESOME_END + " "
            + RES_OF("सूक्ष्म भौतिक लोक से संबंधित") + jh_result + ", " + EARTH + RESULT_END)


SURMOUNT_FORM = ("भौतिक रूप की पहचानों को पूरी तरह पार कर जाने से,टकराव की पहचानों के मिट जाने से, "
                 "विविधता की पहचानों पर मनोयोग न करने से")
SPACE, CONSC, NOTHING, NEITHER = ("अनंत आकाश का क्षेत्र", "अनंत चेतना का क्षेत्र", "कुछ भी न होने का क्षेत्र",
                                  "न पहचान न अ-पहचान का क्षेत्र")


def obl(sphere):  # 'का क्षेत्र' -> 'के क्षेत्र'
    return sphere.replace(" का क्षेत्र", " के क्षेत्र")


def WITH_PERC(sphere):
    return f"{obl(sphere)} की पहचान के साथ"


def PASSED(sphere):
    return f"{obl(sphere)} को पूरी तरह पार करके"


ARUPA = {
    1: SURMOUNT_FORM + ", " + WITH_PERC(SPACE),
    2: PASSED(SPACE) + ", " + WITH_PERC(CONSC),
    3: PASSED(CONSC) + ", " + WITH_PERC(NOTHING),
    4: PASSED(NOTHING) + ", " + WITH_PERC(NEITHER),
}


def IM(n):
    jh = ARUPA[n] + ", " + J4_PLEASURE
    return (f"{Q_ABY} जिस समय कोई {IM_PATH} और {jh}" + WHOLESOME_END + " "
            + RES_OF("अभौतिक लोक से संबंधित") + jh + RESULT_END)


MANUAL = {
    ("1-499", 0): FM(J1, J1),
    ("1-500", 0): FM(J5, J5_PLEASURE),
    ("1-501", 0): IM(1),
    ("1-502", 0): IM(2),
    ("1-503", 0): IM(3),
    ("1-504", 0): IM(4),
}

# ---- headings and closing lines ------------------------------------------------------------------------------------
KV = "हितकर कर्म के फल रूपी"
HEAD = {
    "#### Dvādasa akusalāni": "#### बारह हानिकर मन",
    "#### Abyākatavipāko": "#### नैतिक रूप से अनिर्धारित कर्म-फल",
    "##### Kusalavipākapañcaviññāṇāni": f"##### {KV} पाँच प्रकार की चेतना",
    "##### Kusalavipākamanodhātu": f"##### {KV} मन का तत्व",
    "##### Kusalavipākamanoviññāṇadhātusomanassasahagatā":
        f"##### {KV}, प्रसन्नता के साथ होने वाला मन की चेतना का तत्व",
    "##### Kusalavipākamanoviññāṇadhātuupekkhāsahagatā":
        f"##### {KV}, समभाव के साथ होने वाला मन की चेतना का तत्व",
    "##### Aṭṭhamahāvipākā": "##### आठ बड़े कर्म-फल",
    "##### Rūpāvacaravipākā": "##### सूक्ष्म भौतिक लोक से संबंधित कर्म-फल",
    "##### Arūpāvacaravipākā": "##### अभौतिक लोक से संबंधित कर्म-फल",
}
CLOSE = {
    "Dvādasa akusalacittāni.": "बारह हानिकर मन।",
    "Kusalavipākāni pañcaviññāṇāni.": f"{KV} पाँच प्रकार की चेतना।",
    "Kusalavipākā manodhātu.": f"{KV} मन का तत्व।",
    "Kusalavipākā manoviññāṇadhātu somanassasahagatā.": f"{KV}, प्रसन्नता के साथ होने वाला मन की चेतना का तत्व।",
    "Kusalavipākā upekkhāsahagatā manoviññāṇadhātu.": f"{KV}, समभाव के साथ होने वाला मन की चेतना का तत्व।",
    "Aṭṭhamahāvipākā.": "आठ बड़े कर्म-फल।",
    "Rūpāvacaravipākā.": "सूक्ष्म भौतिक लोक से संबंधित कर्म-फल।",
    "Arūpāvacaravipākā.": "अभौतिक लोक से संबंधित कर्म-फल।",
}

# ---- segments --------------------------------------------------------------------------------------------------------
ID_RX = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")


def pali_segments(path):
    segs, buf = [], []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = ID_RX.search(line)
        if m:
            buf.append(line[: m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf, buf
    return segs


def cnt(s):
    return s.count("–") + s.count("—"), s.count("[")


def build():
    pali = pali_segments(PALI_DIR / PART)
    used = set()
    out = []
    for bid, lines in pali:
        hl = []
        for i, line in enumerate(lines):
            if (bid, i) in MANUAL:
                hi = MANUAL[(bid, i)]
                used.add(("M", bid, i))
            elif line in HEAD:
                hi = HEAD[line]
            elif line in CLOSE:
                hi = CLOSE[line]
            else:
                hi = tr_qa(line) or tr_kotthasa(line) or tr_sangaha(line)
                if hi is None:
                    assert i == 0 and bid in OPEN, (bid, i, line[:80])
                    hi = tr_opening(line, OPEN[bid])
                    used.add(("O", bid))
            assert cnt(line) == cnt(hi), (bid, cnt(line), cnt(hi), hi)
            assert line.endswith("?") == hi.endswith("?"), (bid, hi)
            assert "—" not in hi and ":-" not in hi and "pe…" not in hi, (bid, hi)
            assert not re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", re.sub(r"\[[^\]]*\]", "", hi)), (bid, hi)
            assert "  " not in hi and " ," not in hi, (bid, hi)
            hl.append(hi)
        hl[-1] += f" ^{bid}"
        out.append("\n".join(hl))
    unused = [k for k in OPEN if ("O", k) not in used] + [k for k in MANUAL if ("M",) + k not in used]
    assert not unused, unused
    return "\n\n".join(out) + "\n", len(pali)


if __name__ == "__main__":
    text, n = build()
    out = OUT_DIR / PART
    out.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", out, n, "segments")
