# -*- coding: utf-8 -*-
"""Shared strings and the Pañhāpucchaka engine for the Hindi zero-shot of pi-2 chapters 3, 14 and 15.

Imported by build_3-dhatuvibhango_hi.py, build_14-sikkhapadavibhango_hi.py, build_15-patisambhidavibhango_hi.py.
Reuses the approved chapter-1 sample module (S) verbatim; pi-1 Hindi wording is reused where the Pāli matches.
"""
import os, re, sys

HERE = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi"
sys.path.insert(0, HERE)
import build_ch1_sample_hi as S  # noqa: E402  (import only; it writes nothing on import)

DASH = S.DASH
PALI_DIR, HI_DIR = S.PALI_DIR, S.HI_DIR


def build(chapter, hindi_lines):
    pali = open(os.path.join(PALI_DIR, chapter), encoding="utf-8-sig").read().splitlines()
    n = sum(1 for l in pali if l.strip())
    assert n == len(hindi_lines), f"{chapter}: {n} Pāli lines vs {len(hindi_lines)} Hindi lines"
    text = S.assemble(pali, hindi_lines)
    with open(os.path.join(HI_DIR, chapter), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("written", chapter, len(hindi_lines), "lines")


# ---------------------------------------------------------------- frames shared with pi-1 (2-01 … 2-05 rails Hindi)
PHASSA_PE = "उस समय संपर्क होता है… भटकाव का अभाव होता है"          # tasmiṃ samaye phasso hoti…pe… avikkhepo hoti
OBJ_PE = "और जिसका विषय दृश्य रूप हो… या मन का विषय, या जिस किसी को भी वह विषय बनाए"  # rūpārammaṇaṃ vā…pe… dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha
OBJ_PE_5 = "और जिसका विषय दृश्य रूप हो… या स्पर्श, या जिस किसी को भी वह विषय बनाए"   # rūpārammaṇā vā…pe… phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha
KAMA_KUSALA = "इंद्रिय-सुखों के लोक से संबंधित हितकर मन उत्पन्न होता है"       # kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti
SOM_NS = "प्रसन्नता के साथ होने वाला और ज्ञान से जुड़ा"                      # somanassasahagataṃ ñāṇasampayuttaṃ
# the other seven kāmāvacara types after "somanassasahagataṃ ñāṇasampayuttaṃ sasaṅkhārena…pe…" (pi-1 ^1-269 ff.)
CITTA8_REST = [
    "प्रसन्नता के साथ होने वाला, ज्ञान से जुड़ा और प्रेरणा सहित",
    "प्रसन्नता के साथ होने वाला और ज्ञान से अलग",
    "प्रसन्नता के साथ होने वाला, ज्ञान से अलग और प्रेरणा सहित",
    "समभाव के साथ होने वाला और ज्ञान से जुड़ा",
    "समभाव के साथ होने वाला, ज्ञान से जुड़ा और प्रेरणा सहित",
    "समभाव के साथ होने वाला और ज्ञान से अलग",
    "समभाव के साथ होने वाला, ज्ञान से अलग और प्रेरणा सहित",
]
CITTA8 = "… ".join(CITTA8_REST)                                             # "…pe…" between the types
UPE_NV_SAS = CITTA8_REST[-1]                                               # upekkhāsahagataṃ ñāṇavippayuttaṃ sasaṅkhārena
# hīna / majjhima / paṇīta and the four predominances (pi-1 ^1-269, 2-02:162)
_HMP = "हीन… मध्यम… उत्तम"
_ADH4 = ["चाह की प्रधानता वाला", "उत्साह की प्रधानता वाला", "मन की प्रधानता वाला", "जाँच-परख की प्रधानता वाला"]
ADHI_CHAIN4 = _HMP + "… " + "… ".join(_ADH4) + "… " + "… ".join(f"{a} {_HMP}" for a in _ADH4)
ADHI_CHAIN3 = _HMP + "… " + "… ".join(_ADH4[:3]) + "… " + "… ".join(f"{a} {_HMP}" for a in _ADH4[:3])

RUPU = "जिस समय कोई सूक्ष्म भौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है"     # rūpūpapattiyā maggaṃ bhāveti
ARUPU = "जिस समय कोई अभौतिक लोक में जन्म की ओर ले जाने वाले मार्ग का अभ्यास करता है"         # arūpūpapattiyā maggaṃ bhāveti
VIVICCA_JH1 = "इंद्रिय-सुखों से अलग होकर… पहले ध्यान को प्राप्त करके उसमें रहता है"           # vivicceva kāmehi…pe… paṭhamaṃ jhānaṃ upasampajja viharati
PATHAVI_KASINA = "जो पृथ्वी के ध्यान-मंडल वाला है"                                           # pathavīkasiṇaṃ
NEVASANNA = ("कुछ भी न होने के क्षेत्र को पूरी तरह पार करके, सुख को छोड़ने से… "
             "न पहचान, न अ-पहचान के क्षेत्र की पहचान के साथ होने वाले चौथे ध्यान को प्राप्त करके उसमें रहता है")  # pi-1 2-04:167
LOKUTTARA = ("जिस समय कोई लोकोत्तर ध्यान का अभ्यास करता है, जो मुक्ति की ओर ले जाने वाला और संचय घटाने की ओर ले जाने वाला होता है, "
             "दृष्टियों में फँसने को छोड़ने के लिए और पहले चरण की प्राप्ति के लिए, " + VIVICCA_JH1 +
             ", जो दुःखद प्रगति और धीमे उच्च ज्ञान वाला होता है")                                 # pi-1 ^1-277
ARISEN_FORMLESS = "या उस समय जो भी अन्य परस्पर-आश्रित रूप से उत्पन्न अभौतिक परिघटनाएँ होती हैं"    # ye vā pana tasmiṃ samaye aññepi atthi ...


def hoti_list(items):
    """'phasso hoti, vedanā hoti, ...' -> 'संपर्क होता है, अनुभूति होती है, ...' (gender from the table)."""
    out = []
    for it in items:
        w, g = HOTI[it]
        out.append(f"{w} {'होती है' if g == 'f' else 'होता है'}")
    return ", ".join(out)


HOTI = {  # pi-1 words and gender
    "phasso": ("संपर्क", "m"), "vedanā": ("अनुभूति", "f"), "saññā": ("पहचान", "f"), "cetanā": ("इरादा", "m"),
    "cittaṃ": ("मन", "m"), "vitakko": ("आरंभिक विचार", "m"), "vicāro": ("सतत विचार", "m"), "pīti": ("उल्लास", "m"),
    "sukhaṃ": ("सुख", "m"), "dukkhaṃ": ("दुःख", "m"), "upekkhā": ("समभाव", "m"),
    "cittassekaggatā": ("मन की एकाग्रता", "f"), "manindriyaṃ": ("मन की क्षमता", "f"),
    "upekkhindriyaṃ": ("समभाव की क्षमता", "f"), "sukhindriyaṃ": ("सुख की क्षमता", "f"),
    "dukkhindriyaṃ": ("दुःख की क्षमता", "f"), "somanassindriyaṃ": ("प्रसन्नता की क्षमता", "f"),
    "jīvitindriyaṃ": ("जीवन-क्षमता", "f"), "vīriyindriyaṃ": ("उत्साह की क्षमता", "f"),
    "samādhindriyaṃ": ("एकाग्रता की क्षमता", "f"),
}

# ---------------------------------------------------------------- Pañhāpucchaka: matrix predicates, masculine (pl, sg)
P = {}


def _p(key, pl, sg=None):
    P[_norm(key)] = (pl, sg if sg is not None else pl)


_NORM_WORDS = [  # Pāli case/number variants that share one Hindi phrase
    ("hetū", "hetu"), ("āsavo", "āsavā"), ("saṃyojanañceva", "saṃyojanā ceva"), ("saṃyojanaṃ", "saṃyojanā"),
    ("gantho", "ganthā"), ("nīvaraṇañceva", "nīvaraṇā ceva"), ("nīvaraṇaṃ", "nīvaraṇā"), ("parāmāso", "parāmāsā"),
    ("upādānañceva", "upādānā ceva"), ("upādānaṃ", "upādānā"), ("kileso", "kilesā"), ("uppādinī", "uppādino"),
    ("gāminī", "gāmino"), ("dhipatinī", "dhipatino"), ("sahabhū", "sahabhuno"), ("parivattī", "parivattino"),
    ("anidassanaapaṭighā", "anidassanaappaṭighā"), ("bhāvanāyapahātabbā", "bhāvanāya pahātabbā"),
]


def _norm(s):
    s = re.sub(r"⟦\d+⟧", "", s).strip().lower()
    for a, b in _NORM_WORDS:
        s = s.replace(a, b)
    s = re.sub(r"\bcā$", "ca", s)
    s = s.replace("sahabhunoo", "sahabhuno")
    return s.replace(" ", "").lower()


# triads
for k, v in [("kusalā", "हितकर"), ("akusalā", "हानिकर"), ("abyākatā", "नैतिक रूप से अनिर्धारित"),
             ("kusalāyeva", "केवल हितकर"), ("vipākā", "कर्म-फल रूपी"),
             ("avitakkaavicārā", "आरंभिक विचार और सतत विचार दोनों से रहित"),
             ("parittā", "सीमित"), ("mahaggatā", "उन्नत"), ("appamāṇā", "अपरिमित"), ("anārammaṇā", "विषय से रहित"),
             ("hīnā", "हीन"), ("majjhimā", "मध्यम"), ("paṇītā", "उत्तम"),
             ("micchattaniyatā", "ग़लत दिशा में निश्चित"), ("sammattaniyatā", "सही दिशा में निश्चित"),
             ("aniyatā", "अनिश्चित"), ("niyatā", "निश्चित"),
             ("ajjhattā", "स्वयं से संबंधित"), ("bahiddhā", "दूसरों से संबंधित"),
             ("ajjhattabahiddhā", "स्वयं और दूसरों दोनों से संबंधित")]:
    _p(k, v)
for k, stem in [("sukhāya vedanāya sampayuttā", "सुखद अनुभूति से जुड़"), ("dukkhāya vedanāya sampayuttā", "दुःखद अनुभूति से जुड़"),
                ("adukkhamasukhāya vedanāya sampayuttā", "न दुःखद, न सुखद अनुभूति से जुड़")]:
    _p(k, stem + "े", stem + "ा")
for k, stem in [("vipākadhammadhammā", "कर्म-फल उत्पन्न करने वा"),
                ("nevavipākanavipākadhammadhammā", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वा"),
                ("upādinnupādāniyā", "कर्म से उत्पन्न और आसक्ति का विषय बनने वा"),
                ("anupādinnupādāniyā", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वा"),
                ("anupādinnaanupādāniyā", "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वा"),
                ("saṃkiliṭṭhasaṃkilesikā", "क्लेशों से मलिन और क्लेशों का विषय बनने वा"),
                ("savitakkasavicārā", "आरंभिक विचार और सतत विचार वा"),
                ("avitakkavicāramattā", "आरंभिक विचार से रहित, केवल सतत विचार वा"),
                ("pītisahagatā", "उल्लास के साथ होने वा"), ("sukhasahagatā", "सुख के साथ होने वा"),
                ("upekkhāsahagatā", "समभाव के साथ होने वा"),
                ("dassanena pahātabbahetukā", "सत्य-दर्शन से छोड़े जाने वाले मूलों वा"),
                ("bhāvanāya pahātabbahetukā", "मानसिक अभ्यास से छोड़े जाने वाले मूलों वा"),
                ("neva dassanena na bhāvanāya pahātabbahetukā", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वा"),
                ("ācayagāmino", "संचय की ओर ले जाने वा"), ("apacayagāmino", "संचय घटाने की ओर ले जाने वा"),
                ("nevācayagāmināpacayagāmino", "न संचय की ओर, न संचय घटाने की ओर ले जाने वा"),
                ("parittārammaṇā", "सीमित विषय वा"), ("mahaggatārammaṇā", "उन्नत विषय वा"),
                ("appamāṇārammaṇā", "अपरिमित विषय वा"), ("sārammaṇā", "विषय वा"),
                ("maggārammaṇā", "मार्ग को विषय बनाने वा"), ("maggahetukā", "मार्ग को मूल बनाने वा"),
                ("maggādhipatino", "मार्ग की प्रधानता वा"), ("uppādino", "उत्पन्न होने वा"),
                ("atītārammaṇā", "अतीत के विषय वा"), ("anāgatārammaṇā", "भविष्य के विषय वा"),
                ("paccuppannārammaṇā", "वर्तमान के विषय वा"),
                ("ajjhattārammaṇā", "स्वयं से संबंधित विषय वा"), ("bahiddhārammaṇā", "दूसरों से संबंधित विषय वा"),
                ("ajjhattabahiddhārammaṇā", "स्वयं और दूसरों दोनों से संबंधित विषय वा")]:
    _p(k, stem + "ले", stem + "ला")
_p("asaṃkiliṭṭhasaṃkilesikā", "क्लेशों से मलिन न होने वाले, पर क्लेशों का विषय बनने वाले",
   "क्लेशों से मलिन न होने वाला, पर क्लेशों का विषय बनने वाला")
_p("asaṃkiliṭṭhaasaṃkilesikā", "क्लेशों से मलिन न होने वाले और क्लेशों का विषय न बनने वाले",
   "क्लेशों से मलिन न होने वाला और क्लेशों का विषय न बनने वाला")
_p("dassanena pahātabbā", "सत्य-दर्शन से छोड़े जाने वाले", "सत्य-दर्शन से छोड़ा जाने वाला")
_p("bhāvanāya pahātabbā", "मानसिक अभ्यास से छोड़े जाने वाले", "मानसिक अभ्यास से छोड़ा जाने वाला")
_p("neva dassanena na bhāvanāya pahātabbā", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले",
   "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ा जाने वाला")
_p("sekkhā", "सीखने के चरण के", "सीखने के चरण का")
_p("asekkhā", "सीखना पूरा होने के चरण के", "सीखना पूरा होने के चरण का")
_p("nevasekkhanāsekkhā", "न सीखने के चरण के, न सीखना पूरा होने के चरण के", "न सीखने के चरण का, न सीखना पूरा होने के चरण का")
_p("uppannā", "उत्पन्न हो चुके", "उत्पन्न हो चुका")
_p("anuppannā", "उत्पन्न न हुए", "उत्पन्न न हुआ")
_p("atītā", "अतीत के", "अतीत का")
_p("anāgatā", "भविष्य के", "भविष्य का")
_p("paccuppannā", "वर्तमान के", "वर्तमान का")
_p("sanidassanasappaṭighā", "दिखाई देने वाले और टकराव वाले", "दिखाई देने वाला और टकराव वाला")
_p("anidassanasappaṭighā", "दिखाई न देने वाले, पर टकराव वाले", "दिखाई न देने वाला, पर टकराव वाला")
_p("anidassanaappaṭighā", "दिखाई न देने वाले और टकराव से रहित", "दिखाई न देने वाला और टकराव से रहित")
# dyads
for k, v in [("hetu", "मूल रूपी"), ("ahetukā", "मूल से रहित"), ("hetuvippayuttā", "मूलों से अलग"),
             ("saṅkhatā", "निर्मित"), ("asaṅkhatā", "अनिर्मित"), ("appaṭighā", "टकराव से रहित"),
             ("rūpā", "भौतिक"), ("arūpā", "अभौतिक"), ("lokiyā", "लौकिक"), ("lokuttarā", "लोकोत्तर"),
             ("cittā", "मन रूपी"), ("cittavippayuttā", "मन से अलग"), ("cittena vippayuttā", "मन से अलग"),
             ("cittasamuṭṭhānā", "मन से उत्पन्न"), ("ajjhattikā", "आंतरिक"), ("bāhirā", "बाह्य"),
             ("upādā", "व्युत्पन्न"), ("upādinnā", "कर्म से उत्पन्न"),
             ("avitakkā", "आरंभिक विचार से रहित"), ("avicārā", "सतत विचार से रहित"), ("appītikā", "उल्लास से रहित"),
             ("kāmāvacarā", "इंद्रिय-सुखों के लोक से संबंधित"), ("rūpāvacarā", "सूक्ष्म भौतिक लोक से संबंधित"),
             ("arūpāvacarā", "अभौतिक लोक से संबंधित"), ("anuttarā", "सर्वोच्च"), ("araṇā", "संघर्ष से रहित")]:
    _p(k, v)
for k, stem in [("sahetukā", "मूल वा"), ("sappaccayā", "कारणों पर निर्भर रहने वा"),
                ("appaccayā", "कारणों पर निर्भर न रहने वा"), ("sanidassanā", "दिखाई देने वा"),
                ("anidassanā", "दिखाई न देने वा"), ("sappaṭighā", "टकराव वा"),
                ("kenaci viññeyyā", None), ("acetasikā", None),
                ("cittavisaṃsaṭṭhā", None), ("cittena visaṃsaṭṭhā", None),
                ("cittasahabhuno", "मन के साथ-साथ होने वा"), ("cittānuparivattino", "मन का अनुसरण करने वा"),
                ("anupādinnā", "कर्म से उत्पन्न न होने वा"), ("savitakkā", "आरंभिक विचार वा"),
                ("savicārā", "सतत विचार वा"), ("sappītikā", "उल्लास वा"),
                ("niyyānikā", "मुक्ति की ओर ले जाने वा"), ("aniyyānikā", "मुक्ति की ओर न ले जाने वा"),
                ("sauttarā", "सर्वोच्च न होने वा"), ("saraṇā", "संघर्ष वा")]:
    if stem:
        _p(k, stem + "ले", stem + "ला")
# "भी … भी" as the chapter 1, 2 and 4 agents (both statements hold together)
_p("kenaci viññeyyā", "किसी एक प्रकार की चेतना से जाने जा सकने वाले भी", "किसी एक प्रकार की चेतना से जाना जा सकने वाला भी")
_p("kenaci na viññeyyā", "किसी एक प्रकार की चेतना से न जाने जा सकने वाले भी", "किसी एक प्रकार की चेतना से न जाना जा सकने वाला भी")
_p("hetusampayuttā", "मूलों से जुड़े", "मूलों से जुड़ा")
_p("hetu ceva sahetukā ca", "मूल रूपी भी और मूल वाले भी", "मूल रूपी भी और मूल वाला भी")
_p("sahetukā ceva na ca hetu", "मूल वाले, पर स्वयं मूल रूपी न होने वाले", "मूल वाला, पर स्वयं मूल रूपी न होने वाला")
_p("hetu ceva hetusampayuttā ca", "मूल रूपी भी और मूलों से जुड़े भी", "मूल रूपी भी और मूलों से जुड़ा भी")
_p("hetusampayuttā ceva na ca hetu", "मूलों से जुड़े, पर स्वयं मूल रूपी न होने वाले", "मूलों से जुड़ा, पर स्वयं मूल रूपी न होने वाला")
_p("na hetu sahetukā", "मूल रूपी न होने वाले, पर मूल वाले", "मूल रूपी न होने वाला, पर मूल वाला")
_p("na hetu ahetukā", "मूल रूपी न होने वाले और मूल से रहित", "मूल रूपी न होने वाला और मूल से रहित")
_p("cetasikā", "मन के सहचर", "मन का सहचर")
_p("acetasikā", "मन के सहचर न होने वाले", "मन का सहचर न होने वाला")
_p("cittasampayuttā", "मन से जुड़े", "मन से जुड़ा")
_p("cittena sampayuttā", "मन से जुड़े", "मन से जुड़ा")
_p("cittasaṃsaṭṭhā", "मन से घुले-मिले", "मन से घुला-मिला")
_p("cittena saṃsaṭṭhā", "मन से घुले-मिले", "मन से घुला-मिला")
_p("cittavisaṃsaṭṭhā", "मन से घुले-मिले न होने वाले", "मन से घुला-मिला न होने वाला")
_p("cittena visaṃsaṭṭhā", "मन से घुले-मिले न होने वाले", "मन से घुला-मिला न होने वाला")
_p("cittasaṃsaṭṭhasamuṭṭhānā", "मन से घुले-मिले और मन से उत्पन्न", "मन से घुला-मिला और मन से उत्पन्न")
_p("cittasaṃsaṭṭhasamuṭṭhānasahabhuno", "मन से घुले-मिले, मन से उत्पन्न और मन के साथ-साथ होने वाले",
   "मन से घुला-मिला, मन से उत्पन्न और मन के साथ-साथ होने वाला")
_p("cittasaṃsaṭṭhasamuṭṭhānānuparivattino", "मन से घुले-मिले, मन से उत्पन्न और मन का अनुसरण करने वाले",
   "मन से घुला-मिला, मन से उत्पन्न और मन का अनुसरण करने वाला")
_p("pariyāpannā", "अस्तित्व के लोकों में समाए हुए", "अस्तित्व के लोकों में समाया हुआ")
_p("apariyāpannā", "अस्तित्व के लोकों में न समाए हुए", "अस्तित्व के लोकों में न समाया हुआ")

# gocchaka dyads: (Pāli stem forms, rūpī phrase, object phrase, association phrase, pronoun in the last pair)
GOCCHAKA = [
    dict(n="āsavā", obj="sāsavā", nobj="anāsavā", sa="āsavasampayuttā", vi="āsavavippayuttā",
         rupi="मन के मैल रूपी", o="मन के मैलों का विषय", a="मन के मैलों से", pron="उनका"),
    dict(n="saṃyojanā", obj="saṃyojaniyā", nobj="asaṃyojaniyā", sa="saṃyojanasampayuttā", vi="saṃyojanavippayuttā",
         rupi="बंधन रूपी", o="बंधनों का विषय", a="बंधनों से", pron="उनका"),
    dict(n="ganthā", obj="ganthaniyā", nobj="aganthaniyā", sa="ganthasampayuttā", vi="ganthavippayuttā",
         rupi="गाँठ रूपी", o="गाँठों का विषय", a="गाँठों से", pron="उनका"),
    dict(n="nīvaraṇā", obj="nīvaraṇiyā", nobj="anīvaraṇiyā", sa="nīvaraṇasampayuttā", vi="nīvaraṇavippayuttā",
         rupi="बाधा रूपी", o="बाधाओं का विषय", a="बाधाओं से", pron="उनका"),
    dict(n="parāmāsā", obj="parāmaṭṭhā", nobj="aparāmaṭṭhā", sa="parāmāsasampayuttā", vi="parāmāsavippayuttā",
         rupi="ग़लत धारणा रूपी", o="ग़लत धारणा का विषय", a="ग़लत धारणा से", pron="उसका"),
    dict(n="upādānā", obj="upādāniyā", nobj="anupādāniyā", sa="upādānasampayuttā", vi="upādānavippayuttā",
         rupi="आसक्ति रूपी", o="आसक्ति का विषय", a="आसक्ति से", pron="उसका"),
    dict(n="kilesā", obj="saṃkilesikā", nobj="asaṃkilesikā", sa="kilesasampayuttā", vi="kilesavippayuttā",
         rupi="मन के क्लेश रूपी", o="क्लेशों का विषय", a="क्लेशों से", pron="क्लेशों का"),
]
for g in GOCCHAKA:
    r, o, a = g["rupi"], g["o"], g["a"]
    _p(g["n"], r)
    _p(g["obj"], o + " बनने वाले", o + " बनने वाला")
    _p(g["nobj"], o + " न बनने वाले", o + " न बनने वाला")
    _p(g["sa"], a + " जुड़े", a + " जुड़ा")
    _p(g["vi"], a + " अलग")
    _p(f"{g['n']} ceva {g['obj']} ca", f"{r} भी और {o} बनने वाले भी", f"{r} भी और {o} बनने वाला भी")
    _p(f"{g['obj']} ceva no ca {g['n']}", f"{o} बनने वाले, पर स्वयं {r} न होने वाले", f"{o} बनने वाला, पर स्वयं {r} न होने वाला")
    _p(f"{g['n']} ceva {g['sa']} ca", f"{r} भी और {a} जुड़े भी", f"{r} भी और {a} जुड़ा भी")
    _p(f"{g['sa']} ceva no ca {g['n']}", f"{a} जुड़े, पर स्वयं {r} न होने वाले", f"{a} जुड़ा, पर स्वयं {r} न होने वाला")
    _p(f"{g['vi']} {g['obj']}", f"{a} अलग, पर {g['pron']} विषय बनने वाले", f"{a} अलग, पर {g['pron']} विषय बनने वाला")
    _p(f"{g['vi']} {g['nobj']}", f"{a} अलग और {g['pron']} विषय न बनने वाले", f"{a} अलग और {g['pron']} विषय न बनने वाला")
    # the same two written as one compound (āsavavippayuttasāsavā, …vippayuttaanāsavā)
    _p(f"{g['vi'][:-1]}a{g['obj']}", f"{a} अलग, पर {g['pron']} विषय बनने वाले", f"{a} अलग, पर {g['pron']} विषय बनने वाला")
    _p(f"{g['vi'][:-1]}a{g['nobj']}", f"{a} अलग और {g['pron']} विषय न बनने वाले", f"{a} अलग और {g['pron']} विषय न बनने वाला")
_p("saṃkiliṭṭhā", "क्लेशों से मलिन")
_p("asaṃkiliṭṭhā", "क्लेशों से मलिन न होने वाले", "क्लेशों से मलिन न होने वाला")
_p("kilesā ceva saṃkiliṭṭhā ca", "मन के क्लेश रूपी भी और क्लेशों से मलिन भी")
_p("saṃkiliṭṭhā ceva no ca kilesā", "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाले",
   "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाला")
_p("oghā", "बाढ़ रूपी")
_p("yogā", "जकड़न रूपी")

SUBJ_NUM = {"soḷasa": "सोलह", "dve": "दो", "dasa": "दस", "pañca": "पाँच", "pannarasa": "पंद्रह",
            "sattarasa": "सत्रह", "cha": "छह", "nava": "नौ", "aṭṭha": "आठ", "satta": "सात", "ekādasa": "ग्यारह",
            "dvādasa": "बारह", "tisso": "तीन"}
DHATU_NAMED = {  # Hindi, oblique
    "manodhātu": ("मन का तत्व", "मन के तत्व"), "manoviññāṇadhātu": ("मन की चेतना का तत्व", "मन की चेतना के तत्व"),
    "dhammadhātu": ("मन के विषयों का तत्व", "मन के विषयों के तत्व"),
    "kāyaviññāṇadhātu": ("शरीर की चेतना का तत्व", "शरीर की चेतना के तत्व"),
    "saddadhātu": ("ध्वनि का तत्व", "ध्वनि के तत्व"), "rūpadhātu": ("दृश्य रूप का तत्व", "दृश्य रूप के तत्व"),
}
PS_NAMED = {
    "atthapaṭisambhidā": ("अर्थ का विश्लेषणात्मक ज्ञान", "अर्थ के विश्लेषणात्मक ज्ञान"),
    "niruttipaṭisambhidā": ("भाषा का विश्लेषणात्मक ज्ञान", "भाषा के विश्लेषणात्मक ज्ञान"),
}
_SUBJ_RX = re.compile(
    r"^(?:(soḷasa|dve|dasa|pañca|pannarasa|sattarasa|satta|cha|nava|aṭṭha|ekādasa|dvādasa|tisso) ?(dhātuyo|paṭisambhidā)"
    r"|(manoviññāṇadhātu|manodhātu|dhammadhātu|kāyaviññāṇadhātu|saddadhātu|rūpadhātu|atthapaṭisambhidā|niruttipaṭisambhidā))"
    r"(?= |$)", re.I)


def _subject(txt):
    m = _SUBJ_RX.match(txt)
    if not m:
        return None, txt
    if m.group(1):
        num = SUBJ_NUM[m.group(1).lower()]
        noun = "तत्व" if m.group(2) == "dhātuyo" else "विश्लेषणात्मक ज्ञान"
        obl = "तत्वों" if m.group(2) == "dhātuyo" else "विश्लेषणात्मक ज्ञानों"
        subj = (f"{num} {noun}", f"{num} {obl}", "pl")
    else:
        h, o = {**DHATU_NAMED, **PS_NAMED}[m.group(3).lower()]
        subj = (h, o, "sg")
    return subj, txt[m.end():].lstrip()


def _split_clauses(sentence):
    """Split on ',' / ';' outside double quotes -> [(text, sep)]."""
    out, buf, q = [], "", False
    i = 0
    while i < len(sentence):
        c = sentence[i]
        if c == '"':
            q = not q
        if c in ",;" and not q and sentence[i + 1:i + 2] == " ":
            out.append((buf.strip(), c))
            buf = ""
            i += 2
            continue
        buf += c
        i += 1
    out.append((buf.strip(), ""))
    return out


_TI_Q = re.compile(r'^"(.*)"(n?)ti(?:pi)?$')
_TI_U = re.compile(r'^(.*?)(n?)ti(?:pi)?$')


def _is_ti_item(t):
    if t.lower().startswith("siyā"):
        return False
    if t.startswith('"'):
        return bool(_TI_Q.match(t))
    return bool(re.search(r"(?:ti|tipi)$", t))


def _item(t):
    """-> (content, quoted) with the iti particle removed."""
    m = _TI_Q.match(t)
    if m:
        return m.group(1) + ("ṃ" if m.group(2) else ""), True
    m = _TI_U.match(t)
    return m.group(1) + ("ṃ" if m.group(2) else ""), False


BRACKETS = {}  # marker number -> Hindi bracket text (set by the chapter builder)


def _phrase(tok, num):
    """Pāli predicate -> (Hindi phrase, negated)."""
    marks = re.findall(r"⟦(\d+)⟧", tok)
    k = _norm(tok)
    neg = False
    if k not in P:
        m = re.match(r"^(na|no) (.+)$", re.sub(r"⟦\d+⟧", "", tok).strip(), re.I)
        if m and _norm(m.group(2)) in P:
            k, neg = _norm(m.group(2)), True
        elif k.endswith("ti") and k[:-2] in P:  # the closing "…araṇāti"
            k = k[:-2]
        else:
            raise KeyError(f"unknown predicate: {tok!r} ({k})")
    h = P[k][0 if num == "pl" else 1]
    for mk in marks:
        br = BRACKETS[int(mk)]
        h = h.replace("मन के मैल रूपी", "मन के मैल रूपी " + br, 1) if "मन के मैल रूपी" in h else h + " " + br
    return h, neg


def _q(h, quoted):
    return f"“{h}”" if quoted else h


def _cop(num, neg, siya):
    if siya:
        return ("नहीं होते" if neg else "होते हैं") if num == "pl" else ("नहीं होता" if neg else "होता है")
    return ("नहीं हैं" if neg else "हैं") if num == "pl" else ("नहीं है" if neg else "है")


def _pron(num, obj=False):  # वे/वह, उन्हें/उसे: the same pronouns as the chapter 1, 2 and 4 agents
    if obj:
        return "उन्हें" if num == "pl" else "उसे"
    return "वे" if num == "pl" else "वह"


def _cop_hona(num, neg):
    return ("नहीं होते" if neg else "होते हैं") if num == "pl" else ("नहीं होता" if neg else "होता है")


def _predicate(h, num, neg, siya):
    """'X होने वाले हैं' -> 'X होते हैं'; 'X न होने वाले हैं' -> 'X नहीं हैं' (chapter 1 agent's rule, natural Hindi)."""
    for tail in (" न होने वाले", " न होने वाला"):
        if h.endswith(tail):
            h, neg = h[: -len(tail)], not neg
            return f"{h} {_cop(num, neg, siya)}"
    for tail in (" होने वाले", " होने वाला"):
        if h.endswith(tail) and not h.startswith("उत्पन्न होने"):  # uppādino keeps "उत्पन्न होने वाले"
            return f"{h[: -len(tail)]} {_cop_hona(num, neg)}"
    return f"{h} {_cop(num, neg, siya)}"


def _render_simple(tok, subj, lead):
    """One predicate clause (may contain '…pe…' chains). lead = subject text or pronoun or ''."""
    siya = bool(re.match(r"^siyā ", tok, re.I))
    if siya:
        tok = tok[5:]
    num = subj[2]
    parts = [p.strip() for p in tok.split("…pe…")]
    outs = []
    for j, p in enumerate(parts):
        quoted = p.startswith('"') and p.endswith('"')
        h, neg = _phrase(p.strip('"'), num)
        pred = f"{_q(h, quoted)} {_cop(num, neg, siya)}" if quoted else _predicate(h, num, neg, siya)
        s = ("कभी " if siya else "") + pred
        outs.append(((lead + " ") if (j == 0 and lead) else "") + s)
    return "… ".join(outs)


def _render_nv(subj, explicit, siya, dash, items):
    num = subj[2]
    obj = f"{subj[1]} को" if explicit else _pron(num, obj=True)
    if siya:
        obj = "कभी " + obj
    hs = []
    for it in items:
        c, quoted = _item(it)
        h, neg = _phrase(c, num)
        assert not neg, it
        hs.append(_q(h, quoted))
    if dash:
        body = hs[0] if len(hs) == 1 else ", ".join("न " + h for h in hs)
        return f"{obj} नहीं कहा जा सकता {DASH} {body}"
    if len(hs) == 1:
        return f"{obj} {hs[0]} नहीं कहा जा सकता"
    return f"{obj} न {hs[0]} कहा जा सकता है, " + ", ".join("न " + h for h in hs[1:])


_NV = re.compile(r"^(siyā )?na vattabbā( –)?\s*(.*)$", re.I)


def panha_sentence(sentence, default_subj, pron_first=False):
    clauses = _split_clauses(sentence)
    out, subj, need_pron, i = [], default_subj, pron_first, 0
    while i < len(clauses):
        txt, sep = clauses[i]
        if txt.startswith("⟦R⟧"):  # builder marker: this clause speaks of the whole set again (default subject)
            txt, subj, need_pron = txt[3:].lstrip(), default_subj, True
        s2, rest = _subject(txt)
        explicit = s2 is not None
        if explicit:
            subj, txt, need_pron = s2, rest, False
        m = _NV.match(txt)
        if m:
            items, j = [m.group(3)], i + 1
            while j < len(clauses) and _is_ti_item(clauses[j][0]):
                items.append(clauses[j][0])
                j += 1
            h = _render_nv(subj, explicit, bool(m.group(1)), bool(m.group(2)), items)
            out.append((h, clauses[j - 1][1]))
            need_pron, i = True, j
            continue
        lead = subj[0] if explicit else (_pron(subj[2]) if need_pron else "")
        out.append((_render_simple(txt, subj, lead), sep))
        need_pron, i = False, i + 1
    text = ""
    for h, sep in out:
        text += h + (sep + " " if sep else "")
    return text.strip() + "।"


def panha_line(line, default_subj=("", "", "pl")):
    """Translate one Pañhāpucchaka line (no block ID) sentence by sentence."""
    line = line.strip()
    assert line.endswith("."), line
    sents = re.split(r"\.\s+", line[:-1])
    # implicit subject: the line's first clause opens with "ये" so the answer reads as a sentence
    return " ".join(panha_sentence(s, default_subj, pron_first=(k == 0)) for k, s in enumerate(sents))


def question(n_obl):
    """<N>-naṃ <X>-naṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?"""
    return (f"{n_obl} में से कितने हितकर हैं, कितने हानिकर हैं, कितने नैतिक रूप से अनिर्धारित हैं… "
            f"कितने संघर्ष वाले हैं, कितने संघर्ष से रहित हैं?")


TIKA = "##### तीन-तीन के वर्गीकरण"   # Tikaṃ (pi-1 matrix: तीन-तीन के वर्गीकरण)
DUKA = "##### दो-दो के वर्गीकरण"     # Dukaṃ
