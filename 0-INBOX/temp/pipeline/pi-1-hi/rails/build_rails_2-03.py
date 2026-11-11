"""Builder for the Hindi rails translation of pi-1 chapter 2-03 (supramundane wholesome mind), plain audience.

Parses the Pāli segment by segment and composes the Hindi from fixed strings, so identical Pāli gives
byte-identical Hindi. Shared strings are imported from build_rails_sample.py (import only).

usage: python -I -X utf8 build_rails_2-03.py
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample as b  # noqa: E402

CH = "2-03-cittuppadakandam.md"

b.F.update({
    "anaññātaññassāmītindriyaṃ": ("“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता", "f"),
    "aññindriyaṃ": ("पूर्ण ज्ञान की क्षमता", "f"),
    "sammāvācā": ("सही वाणी", "f"),
    "sammākammanto": ("सही कर्म", "m"),
    "sammāājīvo": ("सही आजीविका", "f"),
    "saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", "m"),
})
F, S, d, dg, question, answer_end, hoti = b.F, b.S, b.d, b.dg, b.question, b.answer_end, b.hoti
Q, OTHERS, KUSALA = b.Q_KUSALA, b.CLOSE_OTHERS, b.CLOSE_KUSALA

# ------------------------------------------------------------------ additions to the fixed strings
MAGGA = ", मार्ग का अंग, मार्ग में समाया हुआ"
BJ_VICAYA = ", परिघटनाओं की छानबीन नामक जागृति का अंग"
BJ_SAMADHI = ", एकाग्रता नामक जागृति का अंग"
BJ_VIRIYA = ", उत्साह नामक जागृति का अंग"
BJ_SATI = ", सजगता नामक जागृति का अंग"
BJ_PITI = ", उल्लास नामक जागृति का अंग"
BJ_PASS = ", प्रशांति नामक जागृति का अंग"

CETANA = S["cetanā_var"].replace(" [पाठभेद (Syā.): sañcetayitattaṃ]", "")
JIVITA = S["jīvita_var"].replace(" [वर्तनी-भेद (Sī.): irīyanā]", "")
VITAKKA_M = S["vitakko"] + MAGGA
PITI_B = S["pīti"] + BJ_PITI
SAMADHI_M = S["samādhi"] + BJ_SAMADHI + MAGGA
VIRIYA_M = S["vīriya_plain"] + BJ_VIRIYA + MAGGA
SATI_M = S["sati"] + BJ_SATI + MAGGA
PANNA_M = S["paññā"] + BJ_VICAYA + MAGGA
PASS_B = S["passaddhi_plain"] + BJ_PASS

ABST = "दूर रहना, विरत रहना, पूरी तरह विरत रहना, बचना, न करना, न अपनाना, दोष में न पड़ना, मर्यादा का उल्लंघन न करना, पुल को तोड़ देना"

# Pāli bodies of the definition segments, exactly as in the source
P_MAGGA = " maggaṅgaṃ maggapariyāpannaṃ"
P_TAJJA = "tajjāmanoviññāṇadhātusamphassaj"
P_SUKHA = "cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā"
P_CITTA = "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu"
P_VITAKKA = "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo" + P_MAGGA
P_SAMADHI = ("cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ "
             "sammāsamādhi samādhisambojjhaṅgo" + P_MAGGA)
P_SADDHA = "saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ"
P_VIRIYA = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā "
            "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo vīriyasambojjhaṅgo"
            + P_MAGGA)
P_SATI = ("sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ sammāsati "
          "satisambojjhaṅgo" + P_MAGGA)
P_PANNA = ("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ nepuññaṃ "
           "vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā paññindriyaṃ paññābalaṃ "
           "paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ amoho dhammavicayo sammādiṭṭhi "
           "dhammavicayasambojjhaṅgo" + P_MAGGA)
P_ABST = " ārati virati paṭivirati veramaṇī akiriyā akaraṇaṃ anajjhāpatti velāanatikkamo setughāto "
P_ALOBHO = "alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ"
P_ADOSO = "adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ"
P_K3 = "vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa "
P_K1 = "viññāṇakkhandhassa "
P_PASS = "passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ passaddhisambojjhaṅgo"

PLAIN = {
    "phasso phusanā saṃphusanā saṃphusitattaṃ": S["phasso"],
    P_TAJJA + "aṃ " + P_SUKHA: S["vedanā"],
    P_TAJJA + "ā saññā sañjānanā sañjānitattaṃ": S["saññā"],
    P_TAJJA + "ā cetanā sañcetanā cetayitattaṃ": CETANA,
    P_CITTA: S["cittaṃ"],
    P_VITAKKA: VITAKKA_M,
    "cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā": S["vicāro"],
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa pītisambojjhaṅgo": PITI_B,
    P_SUKHA: S["sukhaṃ"],
    P_SAMADHI: SAMADHI_M,
    P_SADDHA: S["saddhā"],
    P_VIRIYA: VIRIYA_M,
    P_SATI: SATI_M,
    P_PANNA: PANNA_M,
    "catūhi vacīduccaritehi" + P_ABST + "sammāvācā" + P_MAGGA: f"वाणी के चार दुराचरणों से {ABST}, सही वाणी{MAGGA}",
    "tīhi kāyaduccaritehi" + P_ABST + "sammākammanto" + P_MAGGA: f"शरीर के तीन दुराचरणों से {ABST}, सही कर्म{MAGGA}",
    "micchāājīvā" + P_ABST + "sammāājīvo" + P_MAGGA: f"ग़लत आजीविका से {ABST}, सही आजीविका{MAGGA}",
    P_ALOBHO: S["alobho"],
    P_ADOSO: S["adoso_plain"],
}
KHANDHA_GEN = {
    P_K3 + P_PASS: (b.K3, "f", PASS_B),
    P_K1 + P_PASS: (b.K1, "f", PASS_B),
    P_K3 + "lahutā lahupariṇāmatā adandhanatā avitthanatā": (b.K3, "m", S["lahutā"]),
    P_K1 + "lahutā lahupariṇāmatā adandhanatā avitthanatā": (b.K1, "m", S["lahutā"]),
    P_K3 + "mudutā maddavatā akakkhaḷatā akathinatā": (b.K3, "f", S["mudutā"]),
    P_K1 + "mudutā maddavatā akakkhaḷatā akathinatā": (b.K1, "f", S["mudutā"]),
    P_K3 + "kammaññatā kammaññattaṃ kammaññabhāvo": (b.K3, "f", S["kammaññatā"]),
    P_K1 + "kammaññatā kammaññattaṃ kammaññabhāvo": (b.K1, "f", S["kammaññatā"]),
    P_K3 + "paguṇatā paguṇattaṃ paguṇabhāvo": (b.K3, "f", S["pāguññatā"]),
    P_K1 + "paguṇatā paguṇattaṃ paguṇabhāvo": (b.K1, "f", S["pāguññatā"]),
    P_K3 + "ujutā ujukatā ajimhatā avaṅkatā akuṭilatā": (b.K3, "f", S["ujukatā"]),
    P_K1 + "ujutā ujukatā ajimhatā avaṅkatā akuṭilatā": (b.K1, "f", S["ujukatā"]),
}

P_HIRI = "hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"
P_OTT = "ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā"

UNKNOWN = ("जो परिघटनाएँ अब तक जानी नहीं गई हैं, देखी नहीं गई हैं, प्राप्त नहीं की गई हैं, समझी नहीं गई हैं और "
           "प्रत्यक्ष अनुभव नहीं की गई हैं, उनके साक्षात्कार के लिए")
KNOWN = ("जो परिघटनाएँ जानी जा चुकी हैं, देखी जा चुकी हैं, प्राप्त की जा चुकी हैं, समझी जा चुकी हैं और "
         "प्रत्यक्ष अनुभव की जा चुकी हैं, उनके साक्षात्कार के लिए")
P_UNKNOWN = "tesaṃ dhammānaṃ anaññātānaṃ adiṭṭhānaṃ appattānaṃ aviditānaṃ asacchikatānaṃ sacchikiriyāya "
P_KNOWN = "tesaṃ dhammānaṃ ñātānaṃ diṭṭhānaṃ pattānaṃ viditānaṃ sacchikatānaṃ sacchikiriyāya "

# ------------------------------------------------------------------ the path formula
BHAV = {
    "lokuttaraṃ jhānaṃ": "लोकोत्तर ध्यान",
    "lokuttaraṃ maggaṃ": "लोकोत्तर मार्ग",
    "lokuttaraṃ satipaṭṭhānaṃ": "लोकोत्तर सजगता के आधार",
    "lokuttaraṃ sammappadhānaṃ": "लोकोत्तर सही प्रयास",
    "lokuttaraṃ iddhipādaṃ": "लोकोत्तर सिद्धि के आधार",
    "lokuttaraṃ indriyaṃ": "लोकोत्तर क्षमता",
    "lokuttaraṃ balaṃ": "लोकोत्तर बल",
    "lokuttaraṃ bojjhaṅgaṃ": "लोकोत्तर जागृति के अंग",
    "lokuttaraṃ saccaṃ": "लोकोत्तर सत्य",
    "lokuttaraṃ samathaṃ": "लोकोत्तर शांति",
    "lokuttaraṃ dhammaṃ": "लोकोत्तर परिघटना",
    "lokuttaraṃ khandhaṃ": "लोकोत्तर समूह",
    "lokuttaraṃ āyatanaṃ": "लोकोत्तर इंद्रिय-क्षेत्र",
    "lokuttaraṃ dhātuṃ": "लोकोत्तर तत्व",
    "lokuttaraṃ āhāraṃ": "लोकोत्तर आहार",
    "lokuttaraṃ phassaṃ": "लोकोत्तर संपर्क",
    "lokuttaraṃ vedanaṃ": "लोकोत्तर अनुभूति",
    "lokuttaraṃ saññaṃ": "लोकोत्तर पहचान",
    "lokuttaraṃ cetanaṃ": "लोकोत्तर इरादे",
    "lokuttaraṃ cittaṃ": "लोकोत्तर मन",
}
EMANCIPATING = "जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला होता है"
LEAVE_ALL = "बिना कुछ शेष रखे छोड़ने के लिए"
PURPOSE = {
    "diṭṭhigatānaṃ pahānāya": "दृष्टियों में फँसने को छोड़ने के लिए",
    "kāmarāgabyāpādānaṃ tanubhāvāya": "इंद्रिय-सुखों के राग और दुर्भावना को क्षीण करने के लिए",
    "kāmarāgabyāpādānaṃ anavasesappahānāya": f"इंद्रिय-सुखों के राग और दुर्भावना को {LEAVE_ALL}",
    "rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya":
        f"सूक्ष्म भौतिक लोक के राग, अभौतिक लोक के राग, अहंकार, बेचैनी और अज्ञान को {LEAVE_ALL}",
}
STAGE = {"paṭhamāya": "पहले", "dutiyāya": "दूसरे", "tatiyāya": "तीसरे", "catutthāya": "चौथे"}
JHANA = {
    "vivicceva kāmehi": "इंद्रिय-सुखों से अलग होकर",
    "vitakkavicārānaṃ vūpasamā": "आरंभिक विचार और सतत विचार के शांत होने से",
    "paṭhamaṃ jhānaṃ": "पहला ध्यान",
    "dutiyaṃ jhānaṃ": "दूसरा ध्यान",
    "tatiyaṃ jhānaṃ": "तीसरा ध्यान",
    "catutthaṃ jhānaṃ": "चौथा ध्यान",
    "pañcamaṃ jhānaṃ": "पाँचवाँ ध्यान",
}
MODE = {
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "दुःखद प्रगति और धीमे उच्च ज्ञान वाला",
    "dukkhapaṭipadaṃ khippābhiññaṃ": "दुःखद प्रगति और शीघ्र उच्च ज्ञान वाला",
    "sukhapaṭipadaṃ dandhābhiññaṃ": "सुखद प्रगति और धीमे उच्च ज्ञान वाला",
    "sukhapaṭipadaṃ khippābhiññaṃ": "सुखद प्रगति और शीघ्र उच्च ज्ञान वाला",
}
QUALITY = {
    "suññataṃ": "शून्य",
    "appaṇihitaṃ": "इच्छा-रहित",
    "chandādhipateyyaṃ": "चाह की प्रधानता वाला",
    "vīriyādhipateyyaṃ": "उत्साह की प्रधानता वाला",
    "cittādhipateyyaṃ": "मन की प्रधानता वाला",
    "vīmaṃsādhipateyyaṃ": "जाँच-परख की प्रधानता वाला",
}
PE = "…pe…"


def mode_item(item):
    if item in MODE:
        return MODE[item]
    if item in QUALITY:
        return QUALITY[item]
    head, last = item.rsplit(" ", 1)
    return f"{MODE[head]} और {QUALITY[last]}"


def factor(x):
    name, g = F[x]
    return f"{name} {hoti(g)}"


def tr_rest(r):
    """Everything after the opening 'tasmiṃ samaye'."""
    if r.endswith("ime dhammā kusalā" + PE + "."):
        body, tail = r[: -len("ime dhammā kusalā" + PE + ".")], f"{KUSALA}…।"
    else:
        assert r.endswith("ime dhammā kusalā."), r[-60:]
        body, tail = r[: -len("ime dhammā kusalā.")], f"{KUSALA}।"
    if ";" in body:
        items, others = body.split("; ", 1)
        assert others == "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ", others
        names = [i.removesuffix(" hoti") for i in items.split(", ")]
        return ", ".join(factor(n) for n in names) + f"; {OTHERS} – {tail}"
    assert body.endswith(PE + " "), body[-40:]
    names = [i.removesuffix(" hoti") for i in body[: -len(PE) - 1].split(PE + " ")]
    return "… ".join(factor(n) for n in names) + "… " + tail


OPEN = re.compile(
    r"^Katame dhammā kusalā\? Yasmiṃ samaye (?P<bhav>.+?) bhāveti niyyānikaṃ apacayagāmiṃ (?P<purp>.+?) "
    r"(?P<stage>paṭhamāya|dutiyāya|tatiyāya|catutthāya) bhūmiyā pattiyā (?P<jh>.+?) upasampajja viharati (?P<mode>.+?), "
    r"tasmiṃ samaye (?P<rest>.+)$"
)


def tr_open(m):
    bhav = m["bhav"].split(" bhāveti" + PE + " ")
    bhav_hi = "… ".join(f"{BHAV[x]} का अभ्यास करता है" for x in bhav)
    jh = "… ".join(JHANA[x] for x in m["jh"].split(PE + " "))
    mode = "… ".join(mode_item(x) for x in m["mode"].split(PE + " "))
    return (f"{Q} जिस समय कोई {bhav_hi}, {EMANCIPATING}, {PURPOSE[m['purp']]} और {STAGE[m['stage']]} चरण की प्राप्ति के लिए, "
            f"{jh} प्राप्त करके उसमें रहता है, जो {mode} होता है, उस समय {tr_rest(m['rest'])}")


DEF = re.compile(r"^Katam(?:o|ā|aṃ) tasmiṃ samaye (\S+) hoti\? (.+?) – (?:ayaṃ|idaṃ) tasmiṃ samaye (\S+) hoti(\.|; .+)$")
TAIL_OTHERS = "; ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā."


def tr_def(m):
    x, clause, x2, tail = m[1], m[2], m[3], m[4]
    assert x == x2, (x, x2)
    final = "।" if tail == "." else ";"
    if tail != ".":
        assert tail == TAIL_OTHERS, tail
    rel, _, rest = clause.partition(" ")
    if rest.startswith("tasmiṃ samaye "):
        body = rest[len("tasmiṃ samaye "):]
        if body in PLAIN:
            out = d(x, PLAIN[body], final)
        elif body in KHANDHA_GEN:
            gen, g2, string = KHANDHA_GEN[body]
            assert final == "।"
            out = dg(x, gen, g2, string)
        elif body == P_HIRI:
            out = f"{question(x)} उस समय {b.HIRI} – {answer_end(x, final)}"
        elif body == P_OTT:
            out = f"{question(x)} उस समय {b.OTT} – {answer_end(x, final)}"
        else:
            raise KeyError(body)
    elif rest == "tesaṃ arūpīnaṃ dhammānaṃ āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        out = f"{question(x)} उन अभौतिक परिघटनाओं की जो {JIVITA} है – {answer_end(x, final)}"
    elif rest == P_UNKNOWN + P_PANNA:
        out = f"{question(x)} {UNKNOWN} जो {PANNA_M} है – {answer_end(x, final)}"
    else:
        raise KeyError(clause)
    if tail != ".":
        out += f" {OTHERS} – {KUSALA}।"
    return out


HEAD = {
    "#### Lokuttarakusalaṃ": "#### लोकोत्तर हितकर मन",
    "##### Suddhikapaṭipadā": "##### केवल प्रगति का ढंग",
    "##### Suññataṃ": "##### शून्य",
    "##### Suññatamūlakapaṭipadā": "##### शून्यता पर आधारित प्रगति का ढंग",
    "##### Appaṇihitaṃ": "##### इच्छा-रहित",
    "##### Appaṇihitamūlakapaṭipadā": "##### इच्छाओं के अभाव पर आधारित प्रगति का ढंग",
    "##### Vīsati mahānayā": "##### बीस बड़ी विधियाँ",
    "##### Adhipati": "##### प्रधानता",
}
CLOSING = {f"{k.lstrip('# ')}.": f"{v.lstrip('# ')}।" for k, v in HEAD.items()}
CLOSING.update({
    "Paṭhamo maggo.": "पहला मार्ग।",
    "Dutiyo maggo.": "दूसरा मार्ग।",
    "Tatiyo maggo.": "तीसरा मार्ग।",
    "Catuttho maggo.": "चौथा मार्ग।",
    "Lokuttaraṃ cittaṃ.": "लोकोत्तर मन।",
})

COUNTS = (
    "उस समय चार समूह होते हैं, दो इंद्रिय-क्षेत्र होते हैं, दो तत्व होते हैं, तीन आहार होते हैं, नौ क्षमताएँ होती हैं, "
    "पाँच अंगों वाला ध्यान होता है, आठ अंगों वाला मार्ग होता है, सात बल होते हैं, तीन मूल होते हैं, "
    "एक संपर्क होता है, एक अनुभूति होती है, एक पहचान होती है, एक इरादा होता है, एक मन होता है, "
    "अनुभूति का एक समूह होता है, पहचान का एक समूह होता है, मानसिक रचनाओं का एक समूह होता है, चेतना का एक समूह होता है, "
    "मन का एक इंद्रिय-क्षेत्र होता है, मन की एक क्षमता होती है, मन की चेतना का एक तत्व होता है, "
    "मन के विषयों का एक इंद्रिय-क्षेत्र होता है, मन के विषयों का एक तत्व होता है"
)
P_COUNTS = (
    "Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, navindriyāni honti, "
    "pañcaṅgikaṃ jhānaṃ hoti, aṭṭhaṅgiko maggo hoti, satta balāni honti, tayo hetū honti, eko phasso hoti, ekā vedanā hoti, "
    "ekā saññā hoti, ekā cetanā hoti, ekaṃ cittaṃ hoti, eko vedanākkhandho hoti, eko saññākkhandho hoti, "
    "eko saṅkhārakkhandho hoti, eko viññāṇakkhandho hoti, ekaṃ manāyatanaṃ hoti, ekaṃ manindriyaṃ hoti, "
    "ekā manoviññāṇadhātu hoti, ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti; "
    "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā" + PE + "."
)


def tr_sankhara(line):
    head = "Katamo tasmiṃ samaye saṅkhārakkhandho hoti? "
    tail = ("; ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā ṭhapetvā vedanākkhandhaṃ "
            "ṭhapetvā saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti" + PE + " ime dhammā kusalā.")
    assert line.startswith(head) and line.endswith(tail), line[:80]
    names = line[len(head): -len(tail)].split(" ")
    names[0] = names[0].lower()
    listing = ", ".join(F[n][0] for n in names)
    return (f"{question('saṅkhārakkhandho')} {listing}; {OTHERS}, अनुभूति के समूह को छोड़कर, पहचान के समूह को छोड़कर, "
            f"चेतना के समूह को छोड़कर – {answer_end('saṅkhārakkhandho', '…')} {KUSALA}।")


P_ANNA_HEAD = "Katamaṃ tasmiṃ samaye aññindriyaṃ hoti? Yā "
P_ANNA_TAIL = (", idaṃ tasmiṃ samaye aññindriyaṃ hoti" + PE + " avikkhepo hoti" + PE +
               " ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā.")


def tr_line(line):
    line = line.replace(" " + PE, PE)  # stray space before …pe… in the source (^1-342, ^1-359)
    if line in HEAD:
        return HEAD[line]
    if line in CLOSING:
        return CLOSING[line]
    if line == P_COUNTS:
        return f"{COUNTS}; {OTHERS} – {KUSALA}…।"
    if line.startswith("Katamo tasmiṃ samaye saṅkhārakkhandho"):
        return tr_sankhara(line)
    if line.startswith(P_ANNA_HEAD):
        assert line == P_ANNA_HEAD + P_KNOWN + P_PANNA + P_ANNA_TAIL, line[-120:]
        return (f"{question('aññindriyaṃ')} {KNOWN} जो {PANNA_M} है, {answer_end('aññindriyaṃ', '…')} "
                f"{factor('avikkhepo')}… {OTHERS} – {KUSALA}।")
    m = OPEN.match(line)
    if m:
        return tr_open(m)
    m = DEF.match(line)
    if m:
        return tr_def(m)
    raise ValueError(line[:120])


def main():
    src = b.PALI / CH
    hindi = {}
    for sid, lines in b.segments(src):
        out = []
        for n, line in enumerate(lines):
            if n == len(lines) - 1:
                line = b.ID.sub("", line).rstrip()
            out.append(tr_line(line))
        hindi[sid] = out
    latin = [(k, l[:60]) for k, v in hindi.items() for l in v if re.search(r"[A-Za-zāīūṃṇṭḍñṅḷ]", l)]
    assert not latin, latin[:5]
    b.emit(src, hindi, b.OUT / CH)


if __name__ == "__main__":
    main()
