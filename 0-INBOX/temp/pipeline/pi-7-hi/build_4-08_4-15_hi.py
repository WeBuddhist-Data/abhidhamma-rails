"""Hindi plain zero-shot builder for pi-7 4-08..4-15 (duka-tika 4-08..4-14, tika-duka 4-15).

Every line is composed from fixed frames (imported from build_sample_hi) and item tables, so identical
Pāli gives identical Hindi.  Run:
    python -I -B -X utf8 build_4-08_4-15_hi.py            # write + check
    python -I -B -X utf8 build_4-08_4-15_hi.py --check    # check only
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402  (import only)

PALI_DIR, HI_DIR = S.PALI_DIR, S.HI_DIR
FILES = ["4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md", "4-10-dukatika-sarammanaduka.md",
         "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md",
         "4-13-dukatika-dassanenapahatabbaduka.md", "4-14-dukatika-saranaduka.md",
         "4-15-tikaduka-hetuduka.md"]

# extra number words (count lines of the tika-duka part); added to the shared table in memory only
EXTRA_NUM = {"ekavīsa": "इक्कीस", "tevīsa": "तेईस", "pañcavīsa": "पच्चीस", "aṭṭhavīsa": "अट्ठाईस",
             "tiṃsa": "तीस", "tettiṃsa": "तैंतीस", "pañcatiṃsa": "पैंतीस", "sattatiṃsa": "सैंतीस",
             "chabbīsa": "छब्बीस", "ekūnavīsa": "उन्नीस", "dvāvīsa": "बाईस", "catuvīsa": "चौबीस",
             "sattavīsa": "सत्ताईस", "ekūnatiṃsa": "उनतीस", "ekatiṃsa": "इकतीस", "dvattiṃsa": "बत्तीस",
             "catuttiṃsa": "चौंतीस", "chattiṃsa": "छत्तीस", "aṭṭhatiṃsa": "अड़तीस",
             "ekūnacattālīsa": "उनतालीस", "cattālīsa": "चालीस"}
S.NUM.update(EXTRA_NUM)

DH, DH_PL = S.DHAMMA, S.DHAMMA_PL   # परिघटना / परिघटनाएँ

# =====================================================================================
# 1. Item lexicon: Pāli accusative phrase -> Hindi adjective (pi-1 matrix items, singular, without परिघटना)
# =====================================================================================
ITEMS = [
    # triads
    ("kusalaṃ", "हितकर"), ("akusalaṃ", "हानिकर"), ("abyākataṃ", "नैतिक रूप से अनिर्धारित"),
    ("sukhāya vedanāya sampayuttaṃ", "सुखद अनुभूति से जुड़ी"),
    ("dukkhāya vedanāya sampayuttaṃ", "दुःखद अनुभूति से जुड़ी"),
    ("adukkhamasukhāya vedanāya sampayuttaṃ", "न दुःखद, न सुखद अनुभूति से जुड़ी"),
    ("vipākaṃ", "कर्म-फल रूपी"), ("vipākadhammadhammaṃ", "कर्म-फल उत्पन्न करने वाली"),
    ("vipākadhamma", "कर्म-फल उत्पन्न करने वाली"),
    ("nevavipākanavipākadhammadhammaṃ", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली"),
    ("nevavipākanavipākadhamma", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली"),
    ("upādinnupādāniyaṃ", "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली"),
    ("anupādinnupādāniyaṃ", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली"),
    ("anupādinnaanupādāniyaṃ", "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली"),
    ("saṃkiliṭṭhasaṃkilesikaṃ", "क्लेशों से मलिन और क्लेशों का विषय बनने वाली"),
    ("asaṃkiliṭṭhasaṃkilesikaṃ", "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली"),
    ("asaṃkiliṭṭhaasaṃkilesikaṃ", "क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली"),
    ("savitakkasavicāraṃ", "आरंभिक विचार और सतत विचार वाली"),
    ("avitakkavicāramattaṃ", "आरंभिक विचार से रहित, केवल सतत विचार वाली"),
    ("avitakkaavicāraṃ", "आरंभिक विचार और सतत विचार दोनों से रहित"),
    ("pītisahagataṃ", "उल्लास के साथ होने वाली"), ("sukhasahagataṃ", "सुख के साथ होने वाली"),
    ("upekkhāsahagataṃ", "समभाव के साथ होने वाली"),
    ("dassanena pahātabbaṃ", "सत्य-दर्शन से छोड़ी जाने वाली"),
    ("bhāvanāya pahātabbaṃ", "मानसिक अभ्यास से छोड़ी जाने वाली"),
    ("nevadassanena nabhāvanāya pahātabbaṃ", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली"),
    ("dassanena pahātabbahetukaṃ", "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली"),
    ("bhāvanāya pahātabbahetukaṃ", "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"),
    ("nevadassanena nabhāvanāya pahātabbahetukaṃ",
     "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"),
    ("ācayagāmiṃ", "संचय की ओर ले जाने वाली"), ("apacayagāmiṃ", "संचय घटाने की ओर ले जाने वाली"),
    ("nevācayagāmināpacayagāmiṃ", "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली"),
    ("sekkhaṃ", "सीखने के चरण की"), ("asekkhaṃ", "सीखना पूरा होने के चरण की"),
    ("nevasekkhanāsekkhaṃ", "न सीखने के चरण की, न सीखना पूरा होने के चरण की"),
    ("parittaṃ", "सीमित"), ("mahaggataṃ", "उन्नत"), ("appamāṇaṃ", "अपरिमित"),
    ("parittārammaṇaṃ", "सीमित विषय वाली"), ("mahaggatārammaṇaṃ", "उन्नत विषय वाली"),
    ("appamāṇārammaṇaṃ", "अपरिमित विषय वाली"),
    ("hīnaṃ", "हीन"), ("majjhimaṃ", "मध्यम"), ("paṇītaṃ", "उत्तम"),
    ("micchattaniyataṃ", "ग़लत दिशा में निश्चित"), ("sammattaniyataṃ", "सही दिशा में निश्चित"),
    ("aniyataṃ", "अनिश्चित"),
    ("maggārammaṇaṃ", "मार्ग को विषय बनाने वाली"), ("maggahetukaṃ", "मार्ग को मूल बनाने वाली"),
    ("maggādhipatiṃ", "मार्ग की प्रधानता वाली"),
    ("uppannaṃ", "उत्पन्न हो चुकी"), ("anuppannaṃ", "उत्पन्न न हुई"), ("uppādiṃ", "उत्पन्न होने वाली"),
    ("atītaṃ", "अतीत की"), ("anāgataṃ", "भविष्य की"), ("paccuppannaṃ", "वर्तमान की"),
    ("atītārammaṇaṃ", "अतीत के विषय वाली"), ("anāgatārammaṇaṃ", "भविष्य के विषय वाली"),
    ("paccuppannārammaṇaṃ", "वर्तमान के विषय वाली"),
    ("ajjhattaṃ", "स्वयं से संबंधित"), ("bahiddhā", "दूसरों से संबंधित"),
    ("ajjhattārammaṇaṃ", "स्वयं से संबंधित विषय वाली"), ("bahiddhārammaṇaṃ", "दूसरों से संबंधित विषय वाली"),
    ("sanidassanasappaṭighaṃ", "दिखाई देने वाली और टकराव वाली"),
    ("anidassanasappaṭighaṃ", "दिखाई न देने वाली, पर टकराव वाली"),
    ("anidassanaappaṭighaṃ", "दिखाई न देने वाली और टकराव से रहित"),
    # hetu cluster
    ("hetuṃ", "मूल रूपी"), ("nahetuṃ", "मूल रूपी न होने वाली"),
    ("sahetukaṃ", "मूल वाली"), ("ahetukaṃ", "मूल से रहित"),
    ("hetusampayuttaṃ", "मूलों से जुड़ी"), ("hetuvippayuttaṃ", "मूलों से अलग"),
    ("hetuñceva sahetukañca", "मूल रूपी भी और मूल वाली भी"),
    ("sahetukañceva na ca hetuṃ", "मूल वाली, पर स्वयं मूल रूपी न होने वाली"),
    ("hetuñceva hetusampayuttañca", "मूल रूपी भी और मूलों से जुड़ी भी"),
    ("hetusampayuttañceva na ca hetuṃ", "मूलों से जुड़ी, पर स्वयं मूल रूपी न होने वाली"),
    ("nahetuṃ sahetukaṃ", "मूल रूपी न होने वाली, पर मूल वाली"),
    ("nahetuṃ ahetukaṃ", "मूल रूपी न होने वाली और मूल से रहित"),
    # hindrance cluster
    ("nīvaraṇaṃ", "बाधा रूपी"), ("nonīvaraṇaṃ", "बाधा रूपी न होने वाली"),
    ("nīvaraṇiyaṃ", "बाधाओं का विषय बनने वाली"), ("anīvaraṇiyaṃ", "बाधाओं का विषय न बनने वाली"),
    ("nīvaraṇasampayuttaṃ", "बाधाओं से जुड़ी"), ("nīvaraṇavippayuttaṃ", "बाधाओं से अलग"),
    ("nīvaraṇañceva nīvaraṇiyañca", "बाधा रूपी भी और बाधाओं का विषय बनने वाली भी"),
    ("nīvaraṇiyañceva no ca nīvaraṇaṃ", "बाधाओं का विषय बनने वाली, पर स्वयं बाधा रूपी न होने वाली"),
    ("nīvaraṇañceva nīvaraṇasampayuttañca", "बाधा रूपी भी और बाधाओं से जुड़ी भी"),
    ("nīvaraṇasampayuttañceva no ca nīvaraṇaṃ", "बाधाओं से जुड़ी, पर स्वयं बाधा रूपी न होने वाली"),
    ("nīvaraṇavippayuttaṃ nīvaraṇiyaṃ", "बाधाओं से अलग, पर उनका विषय बनने वाली"),
    ("nīvaraṇavippayuttaṃ anīvaraṇiyaṃ", "बाधाओं से अलग और उनका विषय न बनने वाली"),
    # wrong-view cluster
    ("parāmāsaṃ", "ग़लत धारणा रूपी"), ("noparāmāsaṃ", "ग़लत धारणा रूपी न होने वाली"),
    ("parāmaṭṭhaṃ", "ग़लत धारणा का विषय बनने वाली"), ("aparāmaṭṭhaṃ", "ग़लत धारणा का विषय न बनने वाली"),
    ("parāmāsasampayuttaṃ", "ग़लत धारणा से जुड़ी"), ("parāmāsavippayuttaṃ", "ग़लत धारणा से अलग"),
    ("parāmāsañceva parāmaṭṭhañca", "ग़लत धारणा रूपी भी और ग़लत धारणा का विषय बनने वाली भी"),
    ("parāmaṭṭhañceva no ca parāmāsaṃ",
     "ग़लत धारणा का विषय बनने वाली, पर स्वयं ग़लत धारणा रूपी न होने वाली"),
    ("parāmāsavippayuttaṃ parāmaṭṭhaṃ", "ग़लत धारणा से अलग, पर उसका विषय बनने वाली"),
    ("parāmāsavippayuttaṃ aparāmaṭṭhaṃ", "ग़लत धारणा से अलग और उसका विषय न बनने वाली"),
    # mahantara dyads
    ("sārammaṇaṃ", "विषय वाली"), ("anārammaṇaṃ", "विषय से रहित"),
    ("cittaṃ", "मन रूपी"), ("nocittaṃ", "मन रूपी न होने वाली"),
    ("cetasikaṃ", "मन की सहचर"), ("acetasikaṃ", "मन की सहचर न होने वाली"),
    ("cittasampayuttaṃ", "मन से जुड़ी"), ("cittavippayuttaṃ", "मन से अलग"),
    ("cittasaṃsaṭṭhaṃ", "मन से घुली-मिली"), ("nocittasaṃsaṭṭhaṃ", "मन से घुली-मिली न होने वाली"),
    ("cittasamuṭṭhānaṃ", "मन से उत्पन्न"), ("nocittasamuṭṭhānaṃ", "मन से उत्पन्न न होने वाली"),
    ("cittasahabhuṃ", "मन के साथ-साथ होने वाली"), ("nocittasahabhuṃ", "मन के साथ-साथ न होने वाली"),
    ("cittānuparivattiṃ", "मन का अनुसरण करने वाली"), ("nocittānuparivattiṃ", "मन का अनुसरण न करने वाली"),
    ("cittasaṃsaṭṭhasamuṭṭhānaṃ", "मन से घुली-मिली और मन से उत्पन्न"),
    ("nocittasaṃsaṭṭhasamuṭṭhānaṃ", "मन से घुली-मिली और मन से उत्पन्न न होने वाली"),
    ("cittasaṃsaṭṭhasamuṭṭhānasahabhuṃ", "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली"),
    ("nocittasaṃsaṭṭhasamuṭṭhānasahabhuṃ",
     "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ न होने वाली"),
    ("cittasaṃsaṭṭhasamuṭṭhānānuparivattiṃ", "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली"),
    ("nocittasaṃsaṭṭhasamuṭṭhānānuparivattiṃ",
     "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण न करने वाली"),
    ("ajjhattikaṃ", "आंतरिक"), ("bāhiraṃ", "बाह्य"),
    ("upādā", "व्युत्पन्न"), ("noupādā", "व्युत्पन्न न होने वाली"),
    ("upādinnaṃ", "कर्म से उत्पन्न"), ("anupādinnaṃ", "कर्म से उत्पन्न न होने वाली"),
    # clinging cluster
    ("upādānaṃ", "आसक्ति रूपी"), ("noupādānaṃ", "आसक्ति रूपी न होने वाली"),
    ("upādāniyaṃ", "आसक्ति का विषय बनने वाली"), ("anupādāniyaṃ", "आसक्ति का विषय न बनने वाली"),
    ("upādānasampayuttaṃ", "आसक्ति से जुड़ी"), ("upādānavippayuttaṃ", "आसक्ति से अलग"),
    ("upādānañceva upādāniyañca", "आसक्ति रूपी भी और आसक्ति का विषय बनने वाली भी"),
    ("upādāniyañceva no ca upādānaṃ", "आसक्ति का विषय बनने वाली, पर स्वयं आसक्ति रूपी न होने वाली"),
    ("upādānañceva upādānasampayuttañca", "आसक्ति रूपी भी और आसक्ति से जुड़ी भी"),
    ("upādānasampayuttañceva no ca upādānaṃ", "आसक्ति से जुड़ी, पर स्वयं आसक्ति रूपी न होने वाली"),
    ("upādānavippayuttaṃ upādāniyaṃ", "आसक्ति से अलग, पर उसका विषय बनने वाली"),
    ("upādānavippayuttaṃ anupādāniyaṃ", "आसक्ति से अलग और उसका विषय न बनने वाली"),
    # defilement cluster
    ("kilesaṃ", "मन के क्लेश रूपी"), ("nokilesaṃ", "मन के क्लेश रूपी न होने वाली"),
    ("saṃkilesikaṃ", "क्लेशों का विषय बनने वाली"), ("asaṃkilesikaṃ", "क्लेशों का विषय न बनने वाली"),
    ("saṃkiliṭṭhaṃ", "क्लेशों से मलिन"), ("asaṃkiliṭṭhaṃ", "क्लेशों से मलिन न होने वाली"),
    ("kilesasampayuttaṃ", "क्लेशों से जुड़ी"), ("kilesavippayuttaṃ", "क्लेशों से अलग"),
    ("kilesañceva saṃkilesikañca", "मन के क्लेश रूपी भी और क्लेशों का विषय बनने वाली भी"),
    ("saṃkilesikañceva no ca kilesaṃ", "क्लेशों का विषय बनने वाली, पर स्वयं मन के क्लेश रूपी न होने वाली"),
    ("kilesañceva saṃkiliṭṭhañca", "मन के क्लेश रूपी भी और क्लेशों से मलिन भी"),
    ("saṃkiliṭṭhañceva no ca kilesaṃ", "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाली"),
    ("kilesañceva kilesasampayuttañca", "मन के क्लेश रूपी भी और क्लेशों से जुड़ी भी"),
    ("kilesasampayuttañceva no ca kilesaṃ", "क्लेशों से जुड़ी, पर स्वयं मन के क्लेश रूपी न होने वाली"),
    ("kilesavippayuttaṃ saṃkilesikaṃ", "क्लेशों से अलग, पर क्लेशों का विषय बनने वाली"),
    ("kilesavippayuttaṃ asaṃkilesikaṃ", "क्लेशों से अलग और क्लेशों का विषय न बनने वाली"),
    # last dyads
    ("nadassanena pahātabbaṃ", "सत्य-दर्शन से न छोड़ी जाने वाली"),
    ("nabhāvanāya pahātabbaṃ", "मानसिक अभ्यास से न छोड़ी जाने वाली"),
    ("nadassanena pahātabbahetukaṃ", "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित"),
    ("nabhāvanāya pahātabbahetukaṃ", "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित"),
    ("savitakkaṃ", "आरंभिक विचार वाली"), ("avitakkaṃ", "आरंभिक विचार से रहित"),
    ("savicāraṃ", "सतत विचार वाली"), ("avicāraṃ", "सतत विचार से रहित"),
    ("sappītikaṃ", "उल्लास वाली"), ("appītikaṃ", "उल्लास से रहित"),
    ("naupekkhāsahagataṃ", "समभाव के साथ न होने वाली"),
    ("kāmāvacaraṃ", "इंद्रिय-सुखों के लोक से संबंधित"),
    ("nakāmāvacaraṃ", "इंद्रिय-सुखों के लोक से संबंधित न होने वाली"),
    ("rūpāvacaraṃ", "सूक्ष्म भौतिक लोक से संबंधित"),
    ("narūpāvacaraṃ", "सूक्ष्म भौतिक लोक से संबंधित न होने वाली"),
    ("arūpāvacaraṃ", "अभौतिक लोक से संबंधित"), ("naarūpāvacaraṃ", "अभौतिक लोक से संबंधित न होने वाली"),
    ("pariyāpannaṃ", "अस्तित्व के लोकों में समाई हुई"),
    ("apariyāpannaṃ", "अस्तित्व के लोकों में न समाई हुई"),
    ("niyyānikaṃ", "मुक्ति की ओर ले जाने वाली"), ("aniyyānikaṃ", "मुक्ति की ओर न ले जाने वाली"),
    ("niyataṃ", "निश्चित"),
    ("sauttaraṃ", "सर्वोच्च न होने वाली"), ("anuttaraṃ", "सर्वोच्च"),
    ("saraṇaṃ", "संघर्ष वाली"), ("araṇaṃ", "संघर्ष से रहित"),
]


def _nom(stem):
    if stem.endswith("a"):
        return [stem[:-1] + "o"]
    if stem.endswith("i"):
        return [stem[:-1] + "ī", stem]
    if stem.endswith("bhu"):
        return [stem[:-1] + "ū"]
    if stem.endswith("u"):
        return [stem]
    return [stem]


def _dat(stem):
    if stem.endswith("a"):
        return [stem + "ssa"]
    if stem.endswith("i"):
        return [stem + "no", stem + "ssa"]
    if stem.endswith("u"):
        return [stem + "ssa", stem + "no"]
    return [stem]


def _word_forms(w):
    """acc word -> {case: [surface strings]}; the ceva/ca particles follow the word."""
    for suf, part in (("ñceva", " ceva"), ("ñca", " ca")):
        if w.endswith(suf):
            stem = w[:-len(suf)]
            return {"acc": [w], "nom": [n + part for n in _nom(stem)], "dat": [d + part for d in _dat(stem)],
                    "stem": stem, "part": part}
    if w.endswith("ṃ"):
        stem = w[:-1]
        return {"acc": [w], "nom": _nom(stem), "dat": _dat(stem), "stem": stem, "part": ""}
    return {"acc": [w], "nom": [w], "dat": [w], "stem": None, "part": ""}


def _product(lists):
    out = [""]
    for l in lists:
        out = [(a + " " + b).strip() for a in out for b in l]
    return out


LEX = {}   # surface -> (hindi, ca_flag)


def _add(surface, hi, ca):
    old = LEX.get(surface)
    if old and old != (hi, ca):
        raise SystemExit(f"lexicon clash: {surface!r}")
    LEX[surface] = (hi, ca)


for acc, hi in ITEMS:
    words = acc.split()
    wf = [_word_forms(w) for w in words]
    for case in ("acc", "nom", "dat"):
        for s in _product([f[case] for f in wf]):
            _add(s, hi, False)
        last = wf[-1]
        # whole item with a conjunct "ca"
        if last["part"] == " ca":       # ceva...ca item: also the combo form without the final ca
            bare = wf[:-1] + [_word_forms(last["stem"] + "ṃ")]
            for s in _product([f[case] for f in bare]):
                _add(s, hi, False)
        elif last["stem"] is not None:
            if case == "acc":
                ca_last = [last["stem"] + "ñca"]
            else:
                ca_last = [x + " ca" for x in last[case]]
            for s in _product([f[case] for f in wf[:-1]] + [ca_last]):
                _add(s, hi, True)
        else:
            for s in _product([f[case] for f in wf]):
                _add(s + " ca", hi, True)
LEX_MAXW = max(len(k.split()) for k in LEX)


def parse_items(text):
    """'Nīvaraṇañca nonīvaraṇañca akusalaṃ' -> (groups, shared)."""
    text = text[0].lower() + text[1:]
    words = text.split()
    toks, i = [], 0
    while i < len(words):
        for n in range(min(LEX_MAXW, len(words) - i), 0, -1):
            s = " ".join(words[i:i + n])
            if s in LEX:
                toks.append(LEX[s])
                i += n
                break
        else:
            raise ValueError(f"unknown item word {words[i]!r} in {text!r}")
    groups, cur = [], []
    for hi, ca in toks:
        cur.append(hi)
        if ca:
            groups.append(cur)
            cur = []
    if not groups:
        return [cur], []
    return groups, cur


def _adj(g):
    return ", ".join(g)


def items_hi(text, kind):
    """kind: 'sg' (acc/nom singular), 'pl' (nom plural dhammā), 'dat' (dative)."""
    groups, shared = parse_items(text)
    if kind == "pl" or (shared and len(groups) > 1):
        adjs = [_adj(g) for g in groups]
        body = ", ".join(adjs[:-1]) + " और " + adjs[-1] if len(adjs) > 1 else adjs[0]
        if shared:
            body += ", " + _adj(shared)
        res = body + " " + (DH_PL if kind == "pl" else DH)
    else:
        parts = [f"{_adj(g)} {DH}" for g in groups]
        if shared:   # one conjunct + shared (should not happen)
            parts = [f"{_adj(groups[0] + shared)} {DH}"]
        res = parts[0] if len(parts) == 1 else ", ".join(parts[:-1]) + " और " + parts[-1]
    return res + (" के लिए" if kind == "dat" else "")


# =====================================================================================
# 2. Regexes for frames
# =====================================================================================
COND = "|".join(sorted(S.COND_KEYS, key=len, reverse=True))
W = r"[^\W\d_]+"
ITM = rf"{W}(?: {W})*?"
PATICCA_RX = re.compile(
    rf"(?P<obj>{ITM}) dhammaṃ? paṭicca(?: (?P<res>{ITM}) (?P<rn>dhammo|dhammā) (?P<v>uppajjati|uppajjanti) "
    rf"(?P<neg>na|no)?(?P<c>{COND})paccayā)?")
PANHA_RX = re.compile(
    rf"(?P<src>{ITM}) (?P<sn>dhammo|dhammā) (?P<dst>{ITM}) dhammassa (?P<c>{COND})paccayena paccayo")
INS_RX = re.compile(rf"(?P<c>{COND})paccayena paccayo", re.IGNORECASE)
LOCS = "|".join(sorted(S.COND_LOC_PALI.values(), key=len, reverse=True))
NUMS = "|".join(sorted(S.NUM, key=len, reverse=True))
TOK = rf"(?:(?:na|no)?(?:{LOCS})|(?:na|no)?(?:{COND})paccayā|(?:{NUMS}))(?![^\W\d_])"
RUN_RX = re.compile(rf"{TOK}(?:(?:, | |…pe… ?|… ?){TOK})*", re.IGNORECASE)
PAREN_RX = re.compile(r"\(([^()]*)\)")


def cond_abl(neg, c):
    return S.NABL(c) if neg else S.ABL(c)


# =====================================================================================
# 3. Names of the dyads and triads (headings, "…sadisaṃ" notes)
# =====================================================================================
DUKA_X = {
    "hetu": "मूल", "sahetuka": "मूल से युक्त होने", "hetusampayutta": "मूलों से जुड़ाव",
    "hetusahetuka": "मूल होने और मूल से युक्त होने", "hetuhetusampayutta": "मूल होने और मूलों से जुड़ाव",
    "nahetusahetuka": "मूल रूपी न होने, पर मूल से युक्त होने",
    "sappaccaya": "कारणों पर निर्भर रहने", "lokiya": "लौकिक", "lokiyalokuttara": "लौकिक और लोकोत्तर",
    "nīvaraṇa": "बाधा", "nīvaraṇiya": "बाधाओं का विषय बनने", "nīvaraṇasampayutta": "बाधाओं से जुड़ाव",
    "nīvaraṇanīvaraṇiya": "बाधा और बाधाओं का विषय बनने",
    "nīvaraṇanīvaraṇasampayutta": "बाधा और बाधाओं से जुड़ाव",
    "nīvaraṇavippayuttanīvaraṇiya": "बाधाओं से अलग, पर उनका विषय बनने",
    "parāmāsa": "ग़लत धारणा", "parāmaṭṭha": "ग़लत धारणा का विषय बनने",
    "parāmāsasampayutta": "ग़लत धारणा से जुड़ाव",
    "parāmāsaparāmaṭṭha": "ग़लत धारणा और ग़लत धारणा का विषय बनने",
    "parāmāsavippayuttaparāmaṭṭha": "ग़लत धारणा से अलग, पर उसका विषय बनने",
    "sārammaṇa": "विषय", "citta": "मन", "cetasika": "मन की सहचर परिघटना",
    "cittasampayutta": "मन से जुड़ाव", "cittasaṃsaṭṭha": "मन से घुले-मिले होने",
    "cittasamuṭṭhāna": "मन से उत्पत्ति", "cittasahabhū": "मन के साथ-साथ होने",
    "cittānuparivatti": "मन का अनुसरण करने",
    "cittasaṃsaṭṭhasamuṭṭhāna": "मन से घुले-मिले होने और मन से उत्पत्ति",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhū": "मन से घुले-मिले होने, मन से उत्पत्ति और मन के साथ-साथ होने",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुले-मिले होने, मन से उत्पत्ति और मन का अनुसरण करने",
    "ajjhattika": "आंतरिक", "upādā": "व्युत्पन्न", "upādinna": "कर्म से उत्पत्ति",
    "upādāna": "आसक्ति", "upādāniya": "आसक्ति का विषय बनने", "upādānasampayutta": "आसक्ति से जुड़ाव",
    "upādānaupādāniya": "आसक्ति और आसक्ति का विषय बनने",
    "upādānaupādānasampayutta": "आसक्ति और आसक्ति से जुड़ाव",
    "upādānavippayuttaupādāniya": "आसक्ति से अलग, पर उसका विषय बनने",
    "kilesa": "मन के क्लेश", "saṃkilesika": "क्लेशों का विषय बनने", "saṃkiliṭṭha": "क्लेशों से मलिनता",
    "kilesasampayutta": "क्लेशों से जुड़ाव",
    "saṃkilesasaṃkilesika": "मन के क्लेश और क्लेशों का विषय बनने",
    "kilesasaṃkiliṭṭha": "मन के क्लेश और क्लेशों से मलिनता",
    "kilesakilesasampayutta": "मन के क्लेश और क्लेशों से जुड़ाव",
    "kilesavippayuttasaṃkilesika": "क्लेशों से अलग, पर क्लेशों का विषय बनने",
    "dassanenapahātabba": "सत्य-दर्शन से छोड़े जाने", "dassanena pahātabba": "सत्य-दर्शन से छोड़े जाने",
    "bhāvanāyapahātabba": "मानसिक अभ्यास से छोड़े जाने",
    "dassanenapahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "dassanena pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "bhāvanāyapahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों",
    "savitakka": "आरंभिक विचार", "savicāra": "सतत विचार", "sappītika": "उल्लास",
    "upekkhāsahagata": "समभाव के साथ होने", "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित होने",
    "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित होने", "arūpāvacara": "अभौतिक लोक से संबंधित होने",
    "pariyāpanna": "अस्तित्व के लोकों में समाए होने", "niyyānika": "मुक्ति की ओर ले जाने",
    "niyata": "निश्चित", "sauttara": "सर्वोच्च न होने", "saraṇa": "संघर्ष",
}
TIKA_X = {
    "kusala": "हितकर", "vedanā": "अनुभूति", "vipāka": "कर्म-फल", "upādinna": "कर्म से उत्पन्न",
    "saṃkiliṭṭha": "क्लेशों से मलिन", "vitakka": "आरंभिक विचार", "pīti": "उल्लास",
    "dassanenapahātabba": "सत्य-दर्शन से छोड़े जाने",
    "dassanenapahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "ācayagāmi": "संचय की ओर ले जाने", "sekkha": "सीखने के चरण", "paritta": "सीमित",
    "parittārammaṇa": "सीमित विषय", "hīna": "हीन", "micchatta": "ग़लत दिशा",
    "micchattaniyata": "ग़लत दिशा में निश्चित", "maggārammaṇa": "मार्ग को विषय बनाने",
    "uppanna": "उत्पन्न", "atīta": "अतीत", "atītārammaṇa": "अतीत के विषय",
    "ajjhatta": "स्वयं से संबंधित", "ajjhattārammaṇa": "स्वयं से संबंधित विषय",
    "sanidassana": "दिखाई देने", "sanidassanasappaṭigha": "दिखाई देने और टकराव",
}
GOCCHAKA_HI = {"hetugocchakaṃ": "मूलों का वर्ग", "nīvaraṇagocchaka": "बाधाओं का वर्ग",
               "parāmāsagocchaka": "ग़लत धारणा का वर्ग", "mahantaraduka": "बीच के बड़े दो-दो के वर्गीकरण",
               "upādānagocchaka": "आसक्ति का वर्ग", "kilesagocchaka": "मन के क्लेशों का वर्ग",
               "piṭṭhiduka": "अंतिम दो-दो के वर्गीकरण"}
PADA_HI = {"": "", "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित"}


def duka_obl(x):
    return f"{DUKA_X[x]} वाले दो के वर्गीकरण"


def tika_obl(x):
    return f"{TIKA_X[x]} वाले तीन के वर्गीकरण"


def sadisa_hi(word):
    """Pāli '<X>dukakusalasadisaṃ' etc. -> Hindi 'X वाले दो के वर्गीकरण के हितकर पद के समान'."""
    w = word[0].lower() + word[1:]
    m = re.fullmatch(r"(.+?)duka(kusala|akusala|abyākata|)sadis(?:aṃ|ā)", w)
    if m and m.group(1) in DUKA_X:
        p = m.group(2)
        return duka_obl(m.group(1)) + (f" के {PADA_HI[p]} पद" if p else "") + " के समान"
    m = re.fullmatch(r"(.+?)ttikasadis(?:aṃ|ā)", w)
    if m and m.group(1) in TIKA_X:
        return tika_obl(m.group(1)) + " के समान"
    fixed = {"kusalasadisaṃ": "हितकर पद के समान", "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान",
             "paṭiccavārasadisā": "निर्भरता के खंड के समान",
             "sappaccayakusalasadisaṃ": f"कारणों पर निर्भर रहने वाली, हितकर {DH} के समान"}
    if w in fixed:
        return fixed[w]
    raise ValueError(f"unknown sadisa {word!r}")


# =====================================================================================
# 4. Headings
# =====================================================================================
PADA_HEAD = {
    "Hetupadaṃ": "मूल रूपी पद", "Nahetupadaṃ": "मूल रूपी न होने वाला पद",
    "Ahetukapadaṃ": "मूल से रहित पद", "Hetuvippayuttapadaṃ": "मूलों से अलग पद",
    "Sahetukanahetupadaṃ": "मूल वाला, पर मूल रूपी न होने वाला पद",
    "Hetusampayuttanahetupadaṃ": "मूलों से जुड़ा, पर मूल रूपी न होने वाला पद",
    "Nahetuahetukapadaṃ": "मूल रूपी न होने वाला और मूल से रहित पद",
    "Akusalapadaṃ": "हानिकर पद", "Abyākatapadaṃ": "नैतिक रूप से अनिर्धारित पद",
}
HEAD_FIXED = {
    "Paṭiccavārādi": S.VARA["paṭicca"] + " आदि",
    "Pañhāvāro": S.VARA["pañhā"],
    "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Paccanīyaṃ": S.PACCANIYA,
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए चयन",
    "Nahetupadapaccayacatukkaṃ": "मूल रूपी न होने वाले पद के कारणों के चार क्रम",
    "Dhammānulome tikadukapaṭṭhānaṃ": f"{S.DHAMMANULOMA}: {S.TIKADUKAPATTHANA}",
}


def cond_list(stem):
    """'hetu-ārammaṇa-adhipati' / 'hetuārammaṇa' / 'nahetunaārammaṇa' -> [(neg, key), ...]."""
    out, s = [], stem.replace("-", "")
    s = s[0].lower() + s[1:]
    rx = re.compile(rf"(na|no)?({COND})")
    pos = 0
    while pos < len(s):
        m = rx.match(s, pos)
        if not m:
            raise ValueError(f"cannot split condition heading {stem!r}")
        out.append((bool(m.group(1)), m.group(2)))
        pos = m.end()
    return out


def cond_heading(t):
    m = re.fullmatch(r"(.+?)paccay(o|ā|ādi)", t)
    if not m:
        return None
    try:
        cl = cond_list(m.group(1))
    except ValueError:
        return None
    names = [S.NNAME(k) if n else S.NAME(k) for n, k in cl]
    if m.group(2) == "ādi":
        return ", ".join(names) + " आदि"
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + " और " + names[-1]


def heading_hi(t):
    if t in HEAD_FIXED:
        return HEAD_FIXED[t]
    if t in PADA_HEAD:
        return PADA_HEAD[t]
    m = re.fullmatch(r"(\d+-\d+)\. Paṭiccavārādi", t)
    if m:
        return f"{m.group(1)}. {HEAD_FIXED['Paṭiccavārādi']}"
    m = re.fullmatch(r"(.+?) – (.+)", t) or re.fullmatch(r"(.+?) –(.+)", t)
    if m:
        return f"{heading_hi(m.group(1))} – {heading_hi(m.group(2)[0].upper() + m.group(2)[1:])}"
    m = re.fullmatch(r"([\d-]+)\. (\w+?)duka-(\w+?)ttikaṃ", t)
    if m:
        d = m.group(2)[0].lower() + m.group(2)[1:]
        if d == "pītisahagatādi":
            dh = f"{S.DUKA('उल्लास के साथ होने')} आदि"
        else:
            dh = S.DUKA(DUKA_X[d])
        return f"{m.group(1)}. {dh} और {S.TIKA(TIKA_X[m.group(3)])}"
    m = re.fullmatch(r"([\d-]+)\. (\w+?)ttika-(\w+?)dukaṃ", t)
    if m:
        tk = m.group(2)[0].lower() + m.group(2)[1:]
        return f"{m.group(1)}. {S.TIKA(TIKA_X[tk])} और {S.DUKA(DUKA_X[m.group(3)])}"
    h = cond_heading(t)
    if h:
        return h
    raise ValueError(f"unknown heading {t!r}")


# =====================================================================================
# 5. Parenthetical notes
# =====================================================================================
VARA_OBL = {"sahajāta": "सह-उत्पत्ति के खंड", "paccaya": "कारण के खंड", "nissaya": "आश्रय के खंड",
            "saṃsaṭṭha": "घुले-मिले होने के खंड", "sampayutta": "जुड़ाव के खंड", "pañhā": "प्रश्नों के खंड",
            "paṭicca": "निर्भरता के खंड"}
VARA_DIR = {k: v[:-len("के खंड")] + "का खंड" for k, v in VARA_OBL.items()}
VITTH = "विस्तार करना चाहिए"
KAT = "करना चाहिए"
NUMHI = lambda w: S.NUM[w[0].lower() + w[1:]]  # noqa: E731

VARA_TOK = re.compile(r"(sahajāta|paccaya|nissaya|saṃsaṭṭha|sampayutta|pañhā)vār(epi|ampi|opi|ādi)",
                      re.IGNORECASE)


def vara_note(s):
    """Sahajātavārepi…pe… pañhāvārepi sabbattha ekaṃ / …vārampi … vitthāretabbaṃ / …ādi vitthāretabbo."""
    m0 = VARA_TOK.search(s)
    if not m0:
        return None
    prefix = s[:m0.start()]
    toks, pos, seps = [], m0.start(), []
    while True:
        m = VARA_TOK.match(s, pos)
        if not m:
            break
        toks.append((m.group(1).lower(), m.group(2)))
        pos = m.end()
        sm = re.match(r" ?…pe… ?| ?… ?| ", s[pos:])
        if sm and VARA_TOK.match(s, pos + sm.end()):
            seps.append("… " if "…" in sm.group(0) else ", ")
            pos += sm.end()
        else:
            break
    tail = s[pos:].strip()
    yatha = prefix.strip().lower() == "yathā"
    pre_hi = ""
    if prefix.strip() and not yatha:
        try:
            pre_hi = sadisa_hi(prefix.strip()) + " "
        except (ValueError, KeyError):
            return None
    # tail
    t_hi, mode = None, None
    m = re.fullmatch(r"sabbattha (\w+)", tail)
    if m and m.group(1).lower() in S.NUM:
        t_hi, mode = "हर जगह " + NUMHI(m.group(1)), "loc"
    m = re.fullmatch(r"(?:(sabbattha) )?(?:vitthāretabb(?:aṃ|o|ā)|vitthārebbaṃ)(?: (\w+sadisaṃ))?", tail)
    if m:
        t_hi = ("हर जगह " if m.group(1) else "") + VITTH
        if m.group(2):
            t_hi += ", " + sadisa_hi(m.group(2))
        mode = "acc"
    m = re.fullmatch(r"paṭiccavārasadis(?:aṃ|ā)(?: (?:vitthāretabb(?:aṃ|ā)|vitthārebbaṃ))?", tail)
    if m:
        verb = " " in tail
        t_hi = "निर्भरता के खंड के समान" + (" " + VITTH if verb else " है")
        mode = "acc" if verb else "nom"
    if tail == "kātabbaṃ":
        t_hi, mode = KAT, "ko"
    if tail == "evaṃ vitthāretabbaṃ":
        t_hi, mode = "वैसे ही " + VITTH, "acc"
    if tail == "ekaṃ sappaccayakusalasadisaṃ":
        t_hi, mode = "एक, " + sadisa_hi("sappaccayakusalasadisaṃ"), "loc"
    if t_hi is None:
        return None
    parts = []
    for name, suf in toks:
        if suf == "ādi":
            parts.append(f"{VARA_OBL[name]} आदि का")
        elif suf == "epi":
            parts.append(f"{VARA_OBL[name]} में भी")
        elif mode == "nom":
            parts.append(f"{VARA_DIR[name]} भी")
        elif mode == "ko":
            parts.append(f"{VARA_OBL[name]} को भी")
        else:
            parts.append(f"{VARA_OBL[name]} का भी")
    body = parts[0] + "".join(sep + p for sep, p in zip(seps, parts[1:]))
    if yatha:
        return f"जैसे {body}, {t_hi}"
    return f"{pre_hi}{body} {t_hi}"


SENT = {
    "saṃkhittaṃ": "संक्षिप्त",
    "sabbattha vitthāretabbaṃ": "हर जगह " + VITTH,
    "dve pañhā": "दो प्रश्न",
    "sabbe kātabbā": "सभी करने चाहिए",
    "Aññamaññanissayapaccayā sahajātapaccayasadisā":
        f"{S.NAME('aññamañña')} और {S.NAME('nissaya')} {S.SADISA('sahajāta')} हैं",
    "Imaṃ gamanaṃ upādānadukaakusalasadisaṃ": "यह क्रम " + sadisa_hi("upādānadukaakusalasadisaṃ") + " है",
    "Idha pana hetupaccayā idaṃ nānaṃ": f"पर यहाँ {S.ABL('hetu')} यह भिन्नता है",
    "Kusalampi akusalampi abyākatampi sappītikadukasadisaṃ":
        "हितकर भी, हानिकर भी, नैतिक रूप से अनिर्धारित भी " + sadisa_hi("sappītikadukasadisaṃ") + " हैं",
    "Akusalaṃ dhammaṃ paṭicca…pe… paccanīye nahetuyā ekaṃ":
        f"हानिकर {DH} पर निर्भर होकर… नकारात्मक क्रम में {S.NLOC('hetu')} एक",
    "Abyākataṃ dhammaṃ paṭicca…pe… paccanīye nahetuyā nava…pe… najhāne cha, kātabbā":
        f"नैतिक रूप से अनिर्धारित {DH} पर निर्भर होकर… नकारात्मक क्रम में {S.NLOC('hetu')} नौ… "
        f"{S.NLOC('jhāna')} छह, करने चाहिए",
    "Paccanīye pañhāvāre kusalākusale indriye jhāne cha, pañhāvāre abyākate nava":
        f"नकारात्मक क्रम में प्रश्नों के खंड में हितकर और हानिकर में {S.LOC('indriya')} {S.LOC('jhāna')} छह, "
        f"प्रश्नों के खंड में नैतिक रूप से अनिर्धारित में नौ",
    "Pañhāvāre kusalākusale indriye jhāne cha, abyākate nava":
        f"प्रश्नों के खंड में हितकर और हानिकर में {S.LOC('indriya')} {S.LOC('jhāna')} छह, "
        f"नैतिक रूप से अनिर्धारित में नौ",
    "upekkhāti nānāupekkhā abyākate":
        "“समभाव” के संबंध में, नैतिक रूप से अनिर्धारित में समभाव भिन्न प्रकार का है",
    "Paccanīye nahetuyā nava, najhāne cha": f"नकारात्मक क्रम में {S.NLOC('hetu')} नौ, {S.NLOC('jhāna')} छह",
    "Yathā cetasikadukamūlā tīṇi gamanā, evaṃ imepi tīṇi gamanā kātabbā":
        f"जैसे {duka_obl('cetasika')} पर आधारित तीन क्रम हैं, वैसे ही ये तीन क्रम भी करने चाहिए",
    "Yathā mahantaraduke cetasikadukakusalasadisaṃ, tattakā eva pañhā":
        f"जैसे बीच के बड़े दो-दो के वर्गीकरणों में {sadisa_hi('cetasikadukakusalasadisaṃ')}, उतने ही प्रश्न",
    "nahetuyāpi kattabbaṃ": f"{S.NLOC('hetu')} भी {KAT}",
    "Yathā cittasampayuttadukaṃ abyākatasadisaṃ":
        f"जैसे {S.DUKA(DUKA_X['cittasampayutta'])}, नैतिक रूप से अनिर्धारित पद के समान",
    "Yathā saṃkiliṭṭhattikahetudukaṃ, evaṃ vitthāretabbaṃ":
        f"जैसे {S.TIKA(TIKA_X['saṃkiliṭṭha'])} और {S.DUKA(DUKA_X['hetu'])} है, वैसे ही {VITTH}",
    "Yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ":
        f"जैसे {tika_obl('kusala')} में प्रश्नों का खंड है, वैसे ही {VITTH}",
    "Yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ":
        f"जैसे {tika_obl('kusala')} में प्रश्नों का खंड है, वैसे ही {VITTH}",
    "Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, "
    "evaṃ gaṇetabbaṃ":
        f"जैसे {tika_obl('kusala')} में प्रश्नों के खंड के {S.ANULOMA} को भी, {S.PACCANIYA} को भी, "
        f"{S.ANULOMAPACCANIYA} को भी और {S.PACCANIYANULOMA} को भी गिना गया है, वैसे ही गिनना चाहिए",
    "yathā sappaccayaṃ kusalaṃ, evaṃ vitthāretabbaṃ":
        f"जैसे कारणों पर निर्भर रहने वाली, हितकर {DH} में, वैसे ही {VITTH}",
    "yathā sappaccayaṃ akusalaṃ, evaṃ kātabbaṃ":
        f"जैसे कारणों पर निर्भर रहने वाली, हानिकर {DH} में, वैसे ही {KAT}",
    "yathā kusalanayaṃ evaṃ nahetupaccayampi kātabbaṃ":
        f"जैसे हितकर की विधि है, वैसे ही {S.NNAME_OBL('hetu')} को भी {KAT}",
    "Yathā kāmāvacaradukaabyākatasadisaṃ, ettakāyeva pañhā heṭṭhuparikaṃ parivattanti":
        f"जैसे {sadisa_hi('kāmāvacaradukaabyākatasadisaṃ')}, इतने ही प्रश्न, नीचे और ऊपर का क्रम उलट जाता है",
    "Evaṃ sabbattha akusalaṃ vitthāretabbaṃ": f"इसी तरह हर जगह हानिकर का {VITTH}",
    "ajjhattiko bāhirassa gamanakāle sahajātādhipati, majjhe tīsupi sahajātādhipati":
        f"आंतरिक से बाह्य के लिए जाने वाले क्रम में {S.SAHAJATADHIPATI}, बीच के तीनों में भी "
        f"{S.SAHAJATADHIPATI}",
    "arūpāvacaramūle dve, naarūpāvacare ekaṃ":
        "अभौतिक लोक से संबंधित से शुरू होने वाले में दो, अभौतिक लोक से संबंधित न होने वाली में एक",
    "arūpāvacaramūle tīṇi, naarūpe ekaṃ":
        "अभौतिक लोक से संबंधित से शुरू होने वाले में तीन, अभौतिक लोक से संबंधित न होने वाली में एक",
    "cattāri sahajātādhipati": f"चार, {S.SAHAJATADHIPATI}",
    "cittadukakusalasadisaṃ vitthāretabbaṃ": sadisa_hi("cittadukakusalasadisaṃ") + " " + VITTH,
    "cittasamuṭṭhānamūlaṃ nocittasamuṭṭhānassa kabaḷīkāro āhāro kātabbo":
        f"मन से उत्पन्न से शुरू होने वाले क्रम में मन से उत्पन्न न होने वाली {DH} के लिए "
        f"कौर-कौर खाया जाने वाला भोजन लेना चाहिए",
    "Nocittasamuṭṭhāno cittasamuṭṭhānassa kabaḷīkāro āhāro ghaṭane majjhe kabaḷīkāro āhāro":
        f"मन से उत्पन्न न होने वाली {DH}, मन से उत्पन्न {DH} के लिए कौर-कौर खाया जाने वाला भोजन; "
        f"मेल में, बीच में कौर-कौर खाया जाने वाला भोजन",
    "dassanamūlakaṃ ekaṃ, nadassane ekaṃ":
        "सत्य-दर्शन से छोड़ी जाने वाली से शुरू होने वाला एक, सत्य-दर्शन से न छोड़ी जाने वाली में एक",
    "dassane ekaṃ, nadassane dve":
        "सत्य-दर्शन से छोड़ी जाने वाली में एक, सत्य-दर्शन से न छोड़ी जाने वाली में दो",
    "dassanena pahātabbamūlakaṃ ekaṃ, nadassane dve, ārammaṇādhipati, sahajātādhipati, ekārammaṇādhipati":
        f"सत्य-दर्शन से छोड़ी जाने वाली से शुरू होने वाला एक, सत्य-दर्शन से न छोड़ी जाने वाली में दो, "
        f"{S.ARAMMANADHIPATI}, {S.SAHAJATADHIPATI}, एक {S.ARAMMANADHIPATI}",
    "ettha chasu sahajātādhipati": f"यहाँ छह में {S.SAHAJATADHIPATI}",
    "heṭṭhā tīsu sahajātādhipati, avitakke ekaṃ, sahajātādhipati":
        f"नीचे के तीन में {S.SAHAJATADHIPATI}, आरंभिक विचार से रहित में एक, {S.SAHAJATADHIPATI}",
    "kāmāvacare dve, nakāmāvacare ekaṃ":
        "इंद्रिय-सुखों के लोक से संबंधित में दो, इंद्रिय-सुखों के लोक से संबंधित न होने वाली में एक",
    "kāmāvacare ekaṃ, nakāmāvacare dve":
        "इंद्रिय-सुखों के लोक से संबंधित में एक, इंद्रिय-सुखों के लोक से संबंधित न होने वाली में दो",
    "kāmāvacare ekaṃ, nakāmāvacare tīṇi, kāmāvacare sahajātādhipatiyeva":
        "इंद्रिय-सुखों के लोक से संबंधित में एक, इंद्रिय-सुखों के लोक से संबंधित न होने वाली में तीन, "
        f"इंद्रिय-सुखों के लोक से संबंधित में केवल {S.SAHAJATADHIPATI}",
    "majjhe tīṇi sahajātādhipati": f"बीच में तीन, {S.SAHAJATADHIPATI}",
    "majjhime ca ante ca ārammaṇādhipati": f"बीच वाले में और अंतिम में {S.ARAMMANADHIPATI}",
    "nadassane dve, ghaṭane ekaṃ, saṃkhittaṃ":
        "सत्य-दर्शन से न छोड़ी जाने वाली में दो, मेल में एक, संक्षिप्त",
    "niyate sahajātādhipati, dutiye ārammaṇādhipati sahajātādhipati":
        f"निश्चित में {S.SAHAJATADHIPATI}, दूसरे में {S.ARAMMANADHIPATI}, {S.SAHAJATADHIPATI}",
    "noupādānamūlake tīṇi, sahajātādhipati":
        f"आसक्ति रूपी न होने वाली से शुरू होने वाले में तीन, {S.SAHAJATADHIPATI}",
    "noupādānamūlake": "आसक्ति रूपी न होने वाली से शुरू होने वाले में",
    "paṭhame dvepi adhipatī, dvīsu sahajātādhipati":
        f"पहले में दोनों प्रधानताएँ, दो में {S.SAHAJATADHIPATI}",
    "rūpajīvitindriyaṃ ekaṃ": f"{S.RUPAJIVITINDRIYA} एक",
    "rūpāvacare ekaṃ, narūpāvacare dve":
        "सूक्ष्म भौतिक लोक से संबंधित में एक, सूक्ष्म भौतिक लोक से संबंधित न होने वाली में दो",
    "rūpāvacare ekaṃ, sahajātādhipatiyeva, narūpāvacare dve":
        f"सूक्ष्म भौतिक लोक से संबंधित में एक, केवल {S.SAHAJATADHIPATI}, "
        f"सूक्ष्म भौतिक लोक से संबंधित न होने वाली में दो",
    "tiṇṇannaṃ kabaḷīkāro āhāro": "तीनों के लिए कौर-कौर खाया जाने वाला भोजन",
    "tiṇṇannaṃ rūpajīvitindriyaṃ": f"तीनों के लिए {S.RUPAJIVITINDRIYA}",
    "upādinnamūlake dve, anupādinnamūlake dve":
        "कर्म से उत्पन्न से शुरू होने वाले में दो, कर्म से उत्पन्न न होने वाली से शुरू होने वाले में दो",
    "upādānasampayuttamūlake tīṇi, sahajātādhipati, upādānavippayutte ekaṃ":
        f"आसक्ति से जुड़ी से शुरू होने वाले में तीन, {S.SAHAJATADHIPATI}, आसक्ति से अलग में एक",
    "ādimhi tīṇi, sahajātādhipati, majjhimesu tīsu majjhimānulomikāyeva pañhā, sahajātādhipati,":
        f"शुरुआत में तीन, {S.SAHAJATADHIPATI}, बीच के तीनों में केवल बीच के सकारात्मक क्रम वाले प्रश्न, "
        f"{S.SAHAJATADHIPATI},",
    "ārammaṇapurejātampi vatthupurejātampi": f"{S.ARAMMANAPUREJATA} भी, {S.VATTHUPUREJATA} भी",
    "ārammaṇapurejātaṃyeva, ghaṭanā dve, ārammaṇapurejātampi vatthupurejātampi":
        f"केवल {S.ARAMMANAPUREJATA}, मेल दो, {S.ARAMMANAPUREJATA} भी, {S.VATTHUPUREJATA} भी",
    "Lokiyadukasadisaṃ": sadisa_hi("lokiyadukasadisaṃ"),
}
SENT_LC = {k[0].lower() + k[1:]: v for k, v in SENT.items()}


def sent_hi(s, depth=0):
    key = s[0].lower() + s[1:]
    if key in SENT_LC:
        return SENT_LC[key]
    if key in S.NUM:
        return S.NUM[key]
    m = re.fullmatch(r"sabbattha (\w+)", key)
    if m and m.group(1) in S.NUM:
        return "हर जगह " + S.NUM[m.group(1)]
    v = vara_note(s)
    if v:
        return v
    if re.fullmatch(r"[\w ]+sadis(?:aṃ|ā)", key):
        try:
            return sadisa_hi(key.replace(" ", ""))
        except (ValueError, KeyError):
            try:
                return sadisa_hi(key)
            except (ValueError, KeyError):
                pass
    if RUN_RX.fullmatch(s):
        return S.count_hi(s)
    if depth == 0 and ", " in s:
        return ", ".join(sent_hi(p, 1) for p in s.split(", "))
    raise ValueError(f"unknown note sentence {s!r}")


def note_hi(inner):
    if re.fullmatch(r"\d+", inner):
        return inner
    if inner in SENT:
        return SENT[inner]
    body, end = inner, ""
    if body.endswith("."):
        body, end = body[:-1], "।"
    sents = body.split(". ")
    return "। ".join(sent_hi(x) for x in sents) + end


# =====================================================================================
# 6. Line converter
# =====================================================================================
LINE_FIXED = {
    "Nahetupadaṃ.": PADA_HEAD["Nahetupadaṃ"] + "।",
    "Dhammānulome dukatikapaṭṭhānaṃ niṭṭhitaṃ.": f"{S.DHAMMANULOMA}: {S.DUKATIKAPATTHANA} पूरे हुए।",
    "Hetugocchakaṃ niṭṭhitaṃ.": "मूलों का वर्ग पूरा हुआ।",
}
EXPL = {  # free phrases (after "–" and elsewhere), longest match first
    "vicikicchānīvaraṇaṃ uddhaccanīvaraṇaṃ paṭicca avijjānīvaraṇaṃ":
        "संशय की बाधा या बेचैनी की बाधा पर निर्भर होकर अज्ञान की बाधा",
    "vicikicchāsahagate uddhaccasahagate khandhe paṭicca avijjānīvaraṇaṃ":
        f"{S.KHANDHE_VU} पर निर्भर होकर अज्ञान की बाधा",
    "vicikicchānīvaraṇañca uddhaccanīvaraṇañca sampayuttake ca khandhe paṭicca avijjānīvaraṇaṃ":
        "संशय की बाधा, बेचैनी की बाधा और जुड़े हुए समूहों पर निर्भर होकर अज्ञान की बाधा",
    "vicikicchaṃ paṭicca vicikicchāsahagato moho, uddhaccaṃ paṭicca uddhaccasahagato moho":
        "संशय पर निर्भर होकर संशय के साथ होने वाला मोह, बेचैनी पर निर्भर होकर बेचैनी के साथ होने वाला मोह",
    "vicikicchāsahagate uddhaccasahagate khandhe paṭicca vicikicchāsahagato uddhaccasahagato moho":
        f"{S.KHANDHE_VU} पर निर्भर होकर {S.MOHA_VU}",
    "vicikicchāsahagate khandhe ca vicikicchañca paṭicca vicikicchāsahagato moho, uddhaccasahagate khandhe ca "
    "uddhaccañca paṭicca uddhaccasahagato moho":
        "संशय के साथ होने वाले समूहों और संशय पर निर्भर होकर संशय के साथ होने वाला मोह, बेचैनी के साथ होने "
        "वाले समूहों और बेचैनी पर निर्भर होकर बेचैनी के साथ होने वाला मोह",
    "vicikicchāsahagate khandhe paṭicca vicikicchāsahagato moho":
        "संशय के साथ होने वाले समूहों पर निर्भर होकर संशय के साथ होने वाला मोह",
    "upādinne khandhe ca mahābhūte ca paṭicca cittasamuṭṭhānaṃ rūpaṃ": S.KH_MB("कर्म से उत्पन्न"),
    "uppannā hetū sampayuttakānaṃ hetūnaṃ hetupaccayena paccayo":
        f"उत्पन्न हो चुके मूल जुड़े हुए मूलों के लिए {S.INS('hetu')} होते हैं",
    "anuppannā hetū cetopariyañāṇassa anāgataṃsañāṇassa ārammaṇapaccayena paccayo":
        f"उत्पन्न न हुए मूल {S.CETOPARIYA_OBL} के लिए और {S.ANAGATAMSA_OBL} के लिए {S.INS('ārammaṇa')} होते हैं",
    "uppādī hetū cetopariyañāṇassa anāgataṃsañāṇassa ārammaṇapaccayena paccayo":
        f"उत्पन्न होने वाले मूल {S.CETOPARIYA_OBL} के लिए और {S.ANAGATAMSA_OBL} के लिए "
        f"{S.INS('ārammaṇa')} होते हैं",
    "paṭisandhikkhaṇe": S.PATISANDHI,
    "ārammaṇādhipati": S.ARAMMANADHIPATI, "sahajātādhipati": S.SAHAJATADHIPATI,
    "ārammaṇapurejātaṃ": S.ARAMMANAPUREJATA, "vatthupurejātaṃ": S.VATTHUPUREJATA,
    "pañhā": "प्रश्न",
}
EXPL_KEYS = sorted(EXPL, key=len, reverse=True)

NORMALIZE = [  # (Pāli as written, Pāli the parser reads) – spacing/fused forms only
    (re.compile(r"\bnahetudhammo\b"), "nahetu dhammo"),
    (re.compile(r"…pe\. …"), "…pe…"),
    (re.compile(r"…Pe…"), "…pe…"),
    (re.compile(r"dhammadhamm(aṃ|o)(?= (?:paṭicca|uppajj))"), r"dhamma dhamm\1"),
]


def _close(out):
    return out


def line_hi(pali):
    for rx, rep in NORMALIZE:
        pali = rx.sub(rep, pali)
    if pali in LINE_FIXED:
        return LINE_FIXED[pali]
    m = re.fullmatch(r"(\w+?)(gocchaka|duka)kusalattikaṃ niṭṭhitaṃ\.", pali)
    if m:
        key = m.group(1).lower() + m.group(2)
        return f"{GOCCHAKA_HI[key]} और {S.TIKA('हितकर')} पूरा हुआ।"
    m = re.fullmatch(r"(\w+?)duka(\w+?)ttikaṃ niṭṭhitaṃ\.", pali)
    if m:
        return f"{S.DUKA(DUKA_X[m.group(1).lower()])} और {S.TIKA(TIKA_X[m.group(2)])} पूरा हुआ।"
    m = re.fullmatch(r"(\w+?)ttika(\w+?)dukaṃ niṭṭhitaṃ\.", pali)
    if m:
        tk = m.group(1)[0].lower() + m.group(1)[1:]
        return f"{S.TIKA(TIKA_X[tk])} और {S.DUKA(DUKA_X[m.group(2)])} पूरा हुआ।"
    out, pos, plural = [], 0, False
    n = len(pali)
    while pos < n:
        c = pali[pos]
        m = PAREN_RX.match(pali, pos)
        if m:
            out.append("(" + note_hi(m.group(1)) + ")")
            pos = m.end()
            continue
        m = PATICCA_RX.match(pali, pos)
        if m and (pos == 0 or not pali[pos - 1].isalpha()):
            obj = items_hi(m.group("obj"), "sg")
            s = f"{obj} पर निर्भर होकर"
            if m.group("res"):
                pl = m.group("rn") == "dhammā"
                res = items_hi(m.group("res"), "pl" if pl else "sg")
                s += f" {res} {cond_abl(m.group('neg'), m.group('c'))} {S.VERB([0, 0] if pl else [0])}"
            out.append(s)
            pos = m.end()
            continue
        m = PANHA_RX.match(pali, pos)
        if m and (pos == 0 or not pali[pos - 1].isalpha()):
            plural = m.group("sn") == "dhammā"
            src = items_hi(m.group("src"), "pl" if plural else "sg")
            dst = items_hi(m.group("dst"), "dat")
            out.append(f"{src}, {dst} {S.INS(m.group('c'))} {'होती हैं' if plural else 'होती है'}")
            pos = m.end()
            continue
        m = INS_RX.match(pali, pos)
        if m:
            k = m.group("c")[0].lower() + m.group("c")[1:]
            out.append(f"{S.INS(k)} {'होती हैं' if plural else 'होती है'}")
            pos = m.end()
            continue
        m = RUN_RX.match(pali, pos)
        if m and (pos == 0 or not pali[pos - 1].isalpha()):
            out.append(S.count_hi(m.group(0)))
            pos = m.end()
            continue
        for k in EXPL_KEYS:
            if pali.startswith(k, pos):
                out.append(EXPL[k])
                pos += len(k)
                break
        else:
            if pali.startswith("…pe…", pos) or pali.startswith("…Pe…", pos):
                out.append("…")
                pos += 4
            elif c == ".":
                out.append("।")
                pos += 1
            elif c in " ,;–…":
                out.append(c)
                pos += 1
            else:
                raise ValueError(f"cannot parse at {pali[pos:pos + 60]!r} in line {pali[:80]!r}")
    # "uppajjati hetupaccayā nava pañhā" -> a comma before the question count
    return "".join(out).replace("उत्पन्न होती है नौ प्रश्न", "उत्पन्न होती है, नौ प्रश्न")


# =====================================================================================
# 7. File assembly and checks
# =====================================================================================
ID_RX = S.ID_RX


def build_file(fname):
    ptxt = (PALI_DIR / fname).read_text(encoding="utf-8")
    H = []
    for line in ptxt.splitlines():
        if not line.strip():
            continue
        body = ID_RX.sub("", line).rstrip()
        if body.startswith("#"):
            hashes = len(body) - len(body.lstrip("#"))
            t = body[hashes:].strip()
            star = t.startswith("*") and t.endswith("*")
            t = t.strip("*")
            h = heading_hi(t)
            H.append("#" * hashes + " " + (f"*{h}*" if star else h))
        else:
            H.append(line_hi(body))
    return S.assemble(ptxt, H)


def main():
    pairs, errors = [], 0
    for f in FILES:
        try:
            text = build_file(f)
        except (ValueError, KeyError) as e:
            print(f"{f}: BUILD ERROR {e}")
            errors += 1
            continue
        out = HI_DIR / f
        if "--check" not in sys.argv:
            S._write(out, text)
            print("wrote", out.name)
        if out.exists():
            pairs.append((PALI_DIR / f, out))
    bad = S.check(pairs)
    sys.exit(1 if (bad or errors) else 0)


if __name__ == "__main__":
    main()
