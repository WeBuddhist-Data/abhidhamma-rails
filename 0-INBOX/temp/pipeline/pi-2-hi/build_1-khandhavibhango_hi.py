# -*- coding: utf-8 -*-
"""pi-2 Vibhaṅga, Hindi plain zero-shot: chapter 1 (Khandhavibhaṅga), full chapter.

usage: python -I -X utf8 build_1-khandhavibhango_hi.py
Writes AI_translation\\hindi\\pi-2-hindi-plain-zeroshot_split_chapters\\1-khandhavibhango.md

Lines 1-118 of the Pāli (the approved sample) are copied byte for byte from ch1-sample.md.
Lines 119-end are generated here from the Pāli by a small rule-based translator with a fixed
lexicon (pi-1 mātikā wording, turned into the masculine forms that agree with "समूह"), so that
every repeated Pāli formula gets byte-identical Hindi. Unknown Pāli raises an error.
"""
import os, re, sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-hi")
import build_ch1_sample_hi as S  # noqa: E402  (READ-ONLY: constants and frame functions)

CH = "1-khandhavibhango.md"
DASH = S.DASH
PI1_MATIKA = os.path.join(S.PI1_HI_DIR, "1-matika.md")

# ---------------------------------------------------------------- gender / number helpers
F2M = {"वाली": "वाला", "जुड़ी": "जुड़ा", "छोड़ी": "छोड़ा", "जानी": "जाना", "हुई": "हुआ", "चुकी": "चुका",
       "समाई": "समाया", "घुली-मिली": "घुला-मिला"}
M2PL = {"वाला": "वाले", "जुड़ा": "जुड़े", "छोड़ा": "छोड़े", "जाना": "जाने", "हुआ": "हुए", "चुका": "चुके",
        "समाया": "समाए", "घुला-मिला": "घुले-मिले"}
M2F = {v: k for k, v in F2M.items()}


def _swap(text, table):
    return " ".join(table.get(w.rstrip(","), w.rstrip(",")) + ("," if w.endswith(",") else "") for w in text.split(" "))


# ---------------------------------------------------------------- Pāli normalisation (number-neutral key)
def neutral(p):
    p = p.strip().replace("ñceva", " ceva")
    out = []
    for w in p.split():
        if w in ("hetū", "hetu"):
            w = "hetu"
        elif w.endswith("aṃ"):
            w = w[:-2] + "a"
        elif w.endswith("o") or w.endswith("ā"):
            w = w[:-1] + "a"
        out.append(w)
    return " ".join(out)


# ---------------------------------------------------------------- lexicon
# Each entry: Pāli surface forms (sg first), pi-1 mātikā feminine-plural Hindi (checked against pi-1),
# or an explicit masculine singular; optional explicit masculine plural.
LEX = {}          # neutral Pāli key -> (m.sg, m.pl)
PI1_FPL = []      # pi-1 strings to verify


def add(surfaces, fpl=None, msg=None, mpl=None):
    if isinstance(surfaces, str):
        surfaces = [surfaces]
    if fpl is not None:
        PI1_FPL.append(fpl)
        msg = _swap(fpl, F2M)
    if mpl is None:
        mpl = _swap(msg, M2PL)
    for s in surfaces:
        k = neutral(s)
        if k in LEX and LEX[k] != (msg, mpl):
            raise ValueError(f"lexicon clash for {s}: {LEX[k]} vs {(msg, mpl)}")
        LEX[k] = (msg, mpl)


# --- triads (pi-1 Tikamātikā)
add("kusalo", msg="हितकर")
add("akusalo", msg="हानिकर")
add("abyākato", msg="नैतिक रूप से अनिर्धारित")
add("sukhāya vedanāya sampayutto", "सुखद अनुभूति से जुड़ी")
add("dukkhāya vedanāya sampayutto", "दुःखद अनुभूति से जुड़ी")
add("adukkhamasukhāya vedanāya sampayutto", "न दुःखद, न सुखद अनुभूति से जुड़ी")
add("vipāko", msg="कर्म-फल रूपी")
add("vipākadhammadhammo", "कर्म-फल उत्पन्न करने वाली")
add("nevavipākanavipākadhammadhammo", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली")
add("upādinnupādāniyo", "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली")
add("anupādinnupādāniyo", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली")
add("anupādinnaanupādāniyo", "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली")
add("saṃkiliṭṭhasaṃkilesiko", "क्लेशों से मलिन और क्लेशों का विषय बनने वाली")
add("asaṃkiliṭṭhasaṃkilesiko", "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली")
add("asaṃkiliṭṭhaasaṃkilesiko", "क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली")
add("savitakkasavicāro", "आरंभिक विचार और सतत विचार वाली")
add("avitakkavicāramatto", "आरंभिक विचार से रहित, केवल सतत विचार वाली")
add("avitakkaavicāro", msg="आरंभिक विचार और सतत विचार दोनों से रहित")
add("pītisahagato", "उल्लास के साथ होने वाली")
add("sukhasahagato", "सुख के साथ होने वाली")
add("upekkhāsahagato", "समभाव के साथ होने वाली")
add("dassanena pahātabbo", "सत्य-दर्शन से छोड़ी जाने वाली")
add("bhāvanāya pahātabbo", "मानसिक अभ्यास से छोड़ी जाने वाली")
add("neva dassanena na bhāvanāya pahātabbo", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली")
add("dassanena pahātabbahetuko", "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली")
add("bhāvanāya pahātabbahetuko", "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली")
add("neva dassanena na bhāvanāya pahātabbahetuko", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली")
add(["ācayagāmī", "ācayagāmino"], "संचय की ओर ले जाने वाली")
add(["apacayagāmī", "apacayagāmino"], "संचय घटाने की ओर ले जाने वाली")
add(["nevācayagāmināpacayagāmī", "nevācayagāmināpacayagāmino"], "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली")
add("sekkho", msg="सीखने के चरण का", mpl="सीखने के चरण के")
add("asekkho", msg="सीखना पूरा होने के चरण का", mpl="सीखना पूरा होने के चरण के")
add("nevasekkhanāsekkho", msg="न सीखने के चरण का, न सीखना पूरा होने के चरण का",
    mpl="न सीखने के चरण के, न सीखना पूरा होने के चरण के")
add("paritto", msg="सीमित")
add("mahaggato", msg="उन्नत")
add("appamāṇo", msg="अपरिमित")
add("parittārammaṇo", "सीमित विषय वाली")
add("mahaggatārammaṇo", "उन्नत विषय वाली")
add("appamāṇārammaṇo", "अपरिमित विषय वाली")
add("hīno", msg="हीन")
add("majjhimo", msg="मध्यम")
add("paṇīto", msg="उत्तम")
add("micchattaniyato", msg="ग़लत दिशा में निश्चित")
add("sammattaniyato", msg="सही दिशा में निश्चित")
add("aniyato", msg="अनिश्चित")
add("niyato", msg="निश्चित")
add("maggārammaṇo", "मार्ग को विषय बनाने वाली")
add("maggahetuko", "मार्ग को मूल बनाने वाली")
add(["maggādhipati", "maggādhipatino"], "मार्ग की प्रधानता वाली")
add("uppanno", "उत्पन्न हो चुकी")
add("anuppanno", "उत्पन्न न हुई")
add(["uppādī", "uppādino"], "उत्पन्न होने वाली")
add("atīto", msg="अतीत का", mpl="अतीत के")
add("anāgato", msg="भविष्य का", mpl="भविष्य के")
add("paccuppanno", msg="वर्तमान का", mpl="वर्तमान के")
add("atītārammaṇo", "अतीत के विषय वाली")
add("anāgatārammaṇo", "भविष्य के विषय वाली")
add("paccuppannārammaṇo", "वर्तमान के विषय वाली")
add("ajjhatto", msg="स्वयं से संबंधित")
add("bahiddho", msg="दूसरों से संबंधित")
add("ajjhattabahiddho", msg="स्वयं और दूसरों दोनों से संबंधित")
add("ajjhattārammaṇo", "स्वयं से संबंधित विषय वाली")
add("bahiddhārammaṇo", "दूसरों से संबंधित विषय वाली")
add("ajjhattabahiddhārammaṇo", "स्वयं और दूसरों दोनों से संबंधित विषय वाली")
add("sanidassanasappaṭigho", "दिखाई देने वाली और टकराव वाली")
add("anidassanasappaṭigho", "दिखाई न देने वाली, पर टकराव वाली")
add("anidassanaappaṭigho", "दिखाई न देने वाली और टकराव से रहित")

# --- dyads: roots (pi-1 Hetugocchaka)
add("hetu", msg="मूल रूपी")
add("na hetu", "मूल रूपी न होने वाली")
add("sahetuko", "मूल वाली")
add("ahetuko", msg="मूल से रहित")
add("hetusampayutto", "मूलों से जुड़ी")
add("hetuvippayutto", msg="मूलों से अलग")
add("hetu ceva sahetuko ca", "मूल रूपी भी और मूल वाली भी")
add("sahetuko ceva na ca hetu", "मूल वाली, पर स्वयं मूल रूपी न होने वाली")
add("hetu ceva hetusampayutto ca", "मूल रूपी भी और मूलों से जुड़ी भी")
add("hetusampayutto ceva na ca hetu", "मूलों से जुड़ी, पर स्वयं मूल रूपी न होने वाली")
add(["na hetusahetuko", "na hetu sahetuko"], "मूल रूपी न होने वाली, पर मूल वाली")
add(["na hetuahetuko", "na hetu ahetuko"], "मूल रूपी न होने वाली और मूल से रहित")
# --- small intermediate dyads
add("sappaccayo", "कारणों पर निर्भर रहने वाली")
add("saṅkhato", msg="निर्मित")
add("sanidassano", "दिखाई देने वाली")
add("anidassano", "दिखाई न देने वाली")
add("sappaṭigho", "टकराव वाली")
add("appaṭigho", msg="टकराव से रहित")
add("rūpaṃ", msg="भौतिक")        # pi-1 rūpino = भौतिक
add(["arūpo", "arūpā"], msg="अभौतिक")
add("lokiyo", msg="लौकिक")
add("lokuttaro", msg="लोकोत्तर")
add("kenaci viññeyyo", "किसी एक प्रकार की चेतना से जानी जा सकने वाली")
add("kenaci na viññeyyo", "किसी एक प्रकार की चेतना से न जानी जा सकने वाली")


# --- the clusters (āsava, saṃyojana, gantha, ogha, yoga, nīvaraṇa, parāmāsa, upādāna)
def cluster(noun, adj, nadj, stem, rupi, obj, pron, ceva2=True, plural_noun=None):
    """noun: āsavo / saṃyojanaṃ; adj: sāsavo / saṃyojaniyo; nadj: anāsavo / asaṃyojaniyo; stem: āsava."""
    neg_noun = "no " + noun
    nb = noun[:-2] + "añceva" if noun.endswith("aṃ") else noun + " ceva"
    add(noun, f"{rupi}")
    add(neg_noun, f"{rupi} न होने वाली")
    add(adj, f"{obj} का विषय बनने वाली")
    add(nadj, f"{obj} का विषय न बनने वाली")
    add(stem + "sampayutto", f"{obj} से जुड़ी")
    add(stem + "vippayutto", msg=f"{obj} से अलग")
    add(f"{nb} {adj} ca", f"{rupi} भी और {obj} का विषय बनने वाली भी")
    add(f"{adj} ceva no ca {noun}", f"{obj} का विषय बनने वाली, पर स्वयं {rupi} न होने वाली")
    if ceva2:
        add(f"{nb} {stem}sampayutto ca", f"{rupi} भी और {obj} से जुड़ी भी")
        add(f"{stem}sampayutto ceva no ca {noun}", f"{obj} से जुड़ी, पर स्वयं {rupi} न होने वाली")
    add(f"{stem}vippayutta{adj}", f"{obj} से अलग, पर {pron} विषय बनने वाली")
    add(f"{stem}vippayutta{nadj}", f"{obj} से अलग और {pron} विषय न बनने वाली")


cluster("āsavo", "sāsavo", "anāsavo", "āsava", "मन के मैल रूपी", "मन के मैलों", "उनका")
cluster("saṃyojanaṃ", "saṃyojaniyo", "asaṃyojaniyo", "saṃyojana", "बंधन रूपी", "बंधनों", "उनका")
cluster("gantho", "ganthaniyo", "aganthaniyo", "gantha", "गाँठ रूपी", "गाँठों", "उनका")
cluster("ogho", "oghaniyo", "anoghaniyo", "ogha", "बाढ़ रूपी", "बाढ़ों", "उनका")
cluster("yogo", "yoganiyo", "ayoganiyo", "yoga", "जकड़न रूपी", "जकड़नों", "उनका")
cluster("nīvaraṇaṃ", "nīvaraṇiyo", "anīvaraṇiyo", "nīvaraṇa", "बाधा रूपी", "बाधाओं", "उनका")
cluster("parāmāso", "parāmaṭṭho", "aparāmaṭṭho", "parāmāsa", "ग़लत धारणा रूपी", "ग़लत धारणा", "उसका", ceva2=False)
cluster("upādānaṃ", "upādāniyo", "anupādāniyo", "upādāna", "आसक्ति रूपी", "आसक्ति", "उसका")
add("āsavippayuttaanāsavo", "मन के मैलों से अलग और उनका विषय न बनने वाली")  # Pāli slip for āsavavippayutta-
# Pāli of 2-1 ^2-152 ff. uses "upādānañceva upādāniyā" with a plural subject: same key
# --- big intermediate dyads
add("sārammaṇo", "विषय वाली")
add("anārammaṇo", msg="विषय से रहित")
add(["cittaṃ", "cittā"], "मन रूपी")
add(["no cittaṃ", "no cittā"], "मन रूपी न होने वाली")
add(["cetasiko", "cetasikā"], msg="मन का सहचर", mpl="मन के सहचर")
add(["acetasiko", "acetasikā"], msg="मन का सहचर न होने वाला", mpl="मन के सहचर न होने वाले")
add(["cittasampayutto", "cittena sampayutto"], "मन से जुड़ी")
add(["cittavippayutto", "cittena vippayutto"], msg="मन से अलग")
add(["cittasaṃsaṭṭho", "cittena saṃsaṭṭho"], "मन से घुली-मिली")
add(["cittavisaṃsaṭṭho", "cittena visaṃsaṭṭho"], "मन से घुली-मिली न होने वाली")
add("cittasamuṭṭhāno", msg="मन से उत्पन्न")
add("no cittasamuṭṭhāno", msg="मन से उत्पन्न नहीं")                                  # as the sample (pi-1 ^1-U1)
add(["cittasahabhū", "cittasahabhuno"], "मन के साथ-साथ होने वाली")
add(["no cittasahabhū", "no cittasahabhuno"], "मन के साथ-साथ न होने वाली")
add(["cittānuparivatti", "cittānuparivattino"], "मन का अनुसरण करने वाली")
add(["no cittānuparivatti", "no cittānuparivattino"], "मन का अनुसरण न करने वाली")
add("cittasaṃsaṭṭhasamuṭṭhāno", "मन से घुली-मिली और मन से उत्पन्न")
add("no cittasaṃsaṭṭhasamuṭṭhāno", msg="मन से घुला-मिला और मन से उत्पन्न नहीं")
add(["cittasaṃsaṭṭhasamuṭṭhānasahabhū", "cittasaṃsaṭṭhasamuṭṭhānasahabhuno"],
    "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली")
add(["no cittasaṃsaṭṭhasamuṭṭhānasahabhū", "no cittasaṃsaṭṭhasamuṭṭhānasahabhuno"],
    msg="मन से घुला-मिला, मन से उत्पन्न और मन के साथ-साथ होने वाला नहीं")
add(["cittasaṃsaṭṭhasamuṭṭhānānuparivatti", "cittasaṃsaṭṭhasamuṭṭhānānuparivattino"],
    "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली")
add(["no cittasaṃsaṭṭhasamuṭṭhānānuparivatti", "no cittasaṃsaṭṭhasamuṭṭhānānuparivattino"],
    msg="मन से घुला-मिला, मन से उत्पन्न और मन का अनुसरण करने वाला नहीं")
add("ajjhattiko", msg="आंतरिक")
add("bāhiro", msg="बाह्य")
add("upādā", msg="व्युत्पन्न")                       # as the sample
add("no upādā", msg="व्युत्पन्न नहीं")               # as the sample
add("upādinno", msg="कर्म से उत्पन्न")              # as the sample
add("anupādinno", msg="कर्म से उत्पन्न नहीं")       # as the sample
# --- defilements (pi-1 Kilesagocchaka)
add("kileso", "मन के क्लेश रूपी")
add("no kileso", "मन के क्लेश रूपी न होने वाली")
add("saṃkilesiko", "क्लेशों का विषय बनने वाली")
add("asaṃkilesiko", "क्लेशों का विषय न बनने वाली")
add("saṃkiliṭṭho", msg="क्लेशों से मलिन")
add("asaṃkiliṭṭho", "क्लेशों से मलिन न होने वाली")
add("kilesasampayutto", "क्लेशों से जुड़ी")
add("kilesavippayutto", msg="क्लेशों से अलग")
add("kileso ceva saṃkilesiko ca", "मन के क्लेश रूपी भी और क्लेशों का विषय बनने वाली भी")
add("saṃkilesiko ceva no ca kileso", "क्लेशों का विषय बनने वाली, पर स्वयं मन के क्लेश रूपी न होने वाली")
add("kileso ceva saṃkiliṭṭho ca", msg="मन के क्लेश रूपी भी और क्लेशों से मलिन भी")
add("saṃkiliṭṭho ceva no ca kileso", "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाली")
add("kileso ceva kilesasampayutto ca", "मन के क्लेश रूपी भी और क्लेशों से जुड़ी भी")
add("kilesasampayutto ceva no ca kileso", "क्लेशों से जुड़ी, पर स्वयं मन के क्लेश रूपी न होने वाली")
add("kilesavippayuttasaṃkilesiko", "क्लेशों से अलग, पर क्लेशों का विषय बनने वाली")
add("kilesavippayuttaasaṃkilesiko", "क्लेशों से अलग और क्लेशों का विषय न बनने वाली")
# --- last dyads (pi-1 Piṭṭhiduka)
add("na dassanena pahātabbo", "सत्य-दर्शन से न छोड़ी जाने वाली")
add("na bhāvanāya pahātabbo", "मानसिक अभ्यास से न छोड़ी जाने वाली")
add("na dassanena pahātabbahetuko", msg="सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित")
add("na bhāvanāya pahātabbahetuko", msg="मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित")
add("savitakko", "आरंभिक विचार वाली")
add("avitakko", msg="आरंभिक विचार से रहित")
add("savicāro", "सतत विचार वाली")
add("avicāro", msg="सतत विचार से रहित")
add("sappītiko", "उल्लास वाली")
add("appītiko", msg="उल्लास से रहित")
add("na pītisahagato", "उल्लास के साथ न होने वाली")
add("na sukhasahagato", "सुख के साथ न होने वाली")
add("na upekkhāsahagato", "समभाव के साथ न होने वाली")
add("kāmāvacaro", msg="इंद्रिय-सुखों के लोक से संबंधित")
add("na kāmāvacaro", "इंद्रिय-सुखों के लोक से संबंधित न होने वाली")
add("rūpāvacaro", msg="सूक्ष्म भौतिक लोक से संबंधित")
add("na rūpāvacaro", "सूक्ष्म भौतिक लोक से संबंधित न होने वाली")
add("arūpāvacaro", msg="अभौतिक लोक से संबंधित")
add("na arūpāvacaro", "अभौतिक लोक से संबंधित न होने वाली")
add("pariyāpanno", "अस्तित्व के लोकों में समाई हुई")
add("apariyāpanno", "अस्तित्व के लोकों में न समाई हुई")
add("niyyāniko", "मुक्ति की ओर ले जाने वाली")
add("aniyyāniko", "मुक्ति की ओर न ले जाने वाली")
add("sauttaro", "सर्वोच्च न होने वाली")
add("anuttaro", msg="सर्वोच्च")
add("saraṇo", "संघर्ष वाली")
add("araṇo", msg="संघर्ष से रहित")
# --- chapter-specific (new)
add("phassasampayutto", msg="संपर्क से जुड़ा")                                        # pi-1 phassa + sampayutta
add("sukhindriyaṃ", msg="सुख की क्षमता")
add("dukkhindriyaṃ", msg="दुःख की क्षमता")
add("somanassindriyaṃ", msg="प्रसन्नता की क्षमता")
add("domanassindriyaṃ", msg="उदासी की क्षमता")
add("upekkhindriyaṃ", msg="समभाव की क्षमता")
for _p, _h in (("sukh", "सुख"), ("dukkh", "दुःख"), ("somanass", "प्रसन्नता"), ("domanass", "उदासी"), ("upekkh", "समभाव")):
    add(_p + "indriyasampayutto", msg=f"{_h} की क्षमता से जुड़ा")
add("pītisahagato na sukhasahagato na upekkhāsahagato",
    msg="उल्लास के साथ होने वाला, पर सुख या समभाव के साथ न होने वाला")

# attributes inside the member lists (agree with the listed noun: अनुभूति, पहचान, चेतना f.; इरादा, तत्व m.)
NP_ATTR = {"sukhā": "सुखद", "dukkhā": "दुःखद",
           "kusalā": "हितकर", "akusalā": "हानिकर", "abyākatā": "नैतिक रूप से अनिर्धारित",
           "kusalaṃ": "हितकर", "akusalaṃ": "हानिकर", "abyākataṃ": "नैतिक रूप से अनिर्धारित",
           "sukhasahagatā": "सुख के साथ होने वाला", "dukkhasahagatā": "दुःख के साथ होने वाला",
           "sukhasahagataṃ": "सुख के साथ होने वाला", "dukkhasahagataṃ": "दुःख के साथ होने वाला"}


def lex(p, num="sg"):
    k = neutral(p)
    if k not in LEX:
        raise KeyError(f"unknown Pāli: {p!r}")
    return LEX[k][0 if num == "sg" else 1]


# ---------------------------------------------------------------- nouns
KH = {"rūpakkhandho": "rupa", "vedanākkhandho": "vedana", "saññākkhandho": "sanna",
      "saṅkhārakkhandho": "sankhara", "viññāṇakkhandho": "vinnana"}
ORG = {"cakkhu": "आँख", "sota": "कान", "ghāna": "नाक", "jivhā": "जीभ", "kāya": "शरीर", "mano": "मन",
       "manodhātu": "मन के तत्व", "manoviññāṇadhātu": "मन की चेतना के तत्व"}
CONTACT_NOUN = {"vedanā": ("अनुभूति", "f"), "saññā": ("पहचान", "f"), "cetanā": ("इरादा", "m")}
DHATU = {"manodhātu": "मन का तत्व", "manoviññāṇadhātu": "मन की चेतना का तत्व"}
NUM = {"eka": "एक", "du": "दो", "ti": "तीन", "catu": "चार", "pañca": "पाँच", "cha": "छह", "satta": "सात",
       "aṭṭha": "आठ", "nava": "नौ", "dasa": "दस", "catuvīsati": "चौबीस", "tiṃsa": "तीस", "tiṃsati": "तीस",
       "bahu": "अनेक"}
APARA = "दूसरे ढंग से भी "   # Aparopi


def khandha(pali):
    return S.AGG[KH[pali.lower()]]["khandha"]


# ---------------------------------------------------------------- Abhidhammabhājanīya
ORG_RE = "cakkhu|sota|ghāna|jivhā|kāya|manoviññāṇadhātu|manodhātu|mano"
RE_CONTACT = re.compile(rf"^({ORG_RE})samphassajā (vedanā|saññā|cetanā)(?: atthi (.+))?$")
RE_VINNANA = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)viññāṇaṃ(?: atthi (.+))?$")
RE_DHATU = re.compile(r"^(manodhātu|manoviññāṇadhātu)(?: atthi (.+))?$")
RE_PACCAYA = re.compile(r"^(cakkhu|sota|ghāna|jivhā|kāya|mano)samphassapaccayā(?: (\w+kkhandho))?(?: atthi (.+))?$", re.I)
RE_CLOSE = re.compile(r"^[Ee]vaṃ (\w+?)(?:vidhena|bbidhena) (\w+kkhandho)$")
RE_ATTHI = re.compile(r"^[Aa]tthi (.+)$")
RE_HEAD = re.compile(r"^(Aparopi )?(\w+?)(?:vidhena|bbidhena) (\w+?kkhandho)( –)?")
SEP_RE = re.compile(r"(\s*…pe…\.?\s*|,\s+|;\s+|\.\s+|\.$)")


def np_attr(x, g):
    h = NP_ATTR.get(x)
    if h is None:
        h = lex(x)  # khandha nouns are masculine
    return _swap(h, M2F) if g == "f" else h


def item(text, ctx_g=None):
    """-> (kind, hindi, gender). kind: NP / NPX (listed noun, NPX with 'atthi') or ATTHI/BARE/CLOSE.
    ctx_g: gender of the listed noun that a following 'atthi X' still belongs to."""
    m = RE_CLOSE.match(text)
    if m:
        n, k = m.groups()
        return "CLOSE", f"इस तरह {NUM[n.lower()]} प्रकार से {khandha(k)} बताया गया", None
    m = RE_ATTHI.match(text)
    if m:
        x = m.group(1)
        return "ATTHI", f"कुछ {np_attr(x, ctx_g) if ctx_g else lex(x)} है", ctx_g
    for rx, kind in ((RE_CONTACT, "c"), (RE_VINNANA, "v"), (RE_DHATU, "d"), (RE_PACCAYA, "p")):
        m = rx.match(text)
        if not m:
            continue
        if kind == "c":
            o, n, x = m.groups()
            noun, g = CONTACT_NOUN[n]
            h = f"{ORG[o]} के संपर्क से उत्पन्न {noun}"
        elif kind == "v":
            o, x = m.groups()
            h, g = f"{ORG[o]} की चेतना", "f"
        elif kind == "d":
            o, x = m.groups()
            h, g = DHATU[o], "m"
        else:
            o, k, x = m.groups()
            h, g = f"{ORG[o.lower()]} के संपर्क के कारण", "m"
            if k:
                h += f" होने वाला {khandha(k)}"
        if x:
            h += f", जिसमें कुछ {np_attr(x, g)} है"
            return "NPX", h, g
        return "NP", h, None
    return "BARE", f"{lex(text)} है", None


def render_sep(s):
    t = s.strip()
    if t.startswith("…pe…"):
        return ("…।" if t.endswith(".") else "…") + (" " if s.endswith(" ") else "")
    return {",": ", ", ";": "; ", ".": "। " if s.endswith(" ") else "।"}[t]


def body(text):
    parts = [p for p in SEP_RE.split(text) if p != ""]
    toks = []  # [kind, hindi, sep_after]
    lead, g = "", None
    for p in parts:
        if SEP_RE.fullmatch(p):
            r = render_sep(p)
            if toks:
                toks[-1][2] += r
            else:
                lead += r
            if r.strip() != ",":
                g = None  # only ", atthi …" continues the listed noun
        else:
            kind, h, g = item(p.strip(), g)
            toks.append([kind, h, ""])
    # «और» before the last listed noun of each sentence, when the item before it is a listed noun
    start = 0
    for i, t in enumerate(toks):
        if t[2].strip() in ("।", ";", "…।", "") or i == len(toks) - 1:
            sent = toks[start:i + 1]
            idx = [j for j, s in enumerate(sent) if s[0] in ("NP", "NPX")]
            if idx:
                j = idx[-1]
                if j > 0 and sent[j - 1][0] == "NP" and sent[j - 1][2] == ", ":
                    sent[j - 1][2] = " और "
            start = i + 1
    return lead + "".join(t[1] + t[2] for t in toks)


def ab_line(p):
    out = ""
    m = re.match(r"^Tattha katamo (\w+kkhandho)\? ", p)
    if m:
        out = S.khandha_question(KH[m.group(1)]) + " "
        p = p[m.end():]
    m = re.match(r"^Ayaṃ vuccati (\w+kkhandho)\.$", p)
    if m:
        return S.khandha_answer(KH[m.group(1)])
    m = RE_HEAD.match(p)
    if m:
        apara, n, k, dash = m.groups()
        head = f"{APARA if apara else ''}{NUM[n.lower()]} प्रकार से {khandha(k)}"
        rest = p[m.end():]
        if dash:
            out += f"{head} {DASH} " + body(rest.strip())
        elif rest.startswith("…pe…"):
            out += head + body(rest)
        elif rest.strip().startswith("atthi"):
            out += f"{head}: " + body(rest.strip())          # Pāli has no dash here
        else:
            out += f"{head} " + body(rest.strip())
        return out
    return out + body(p)


# ---------------------------------------------------------------- Pañhāpucchaka
SUBJ = {  # Pāli -> (nominative, oblique + को, number)
    "Rūpakkhandho": ("भौतिक रूप का समूह", "भौतिक रूप के समूह को", "sg"),
    "Vedanākkhandho": ("अनुभूति का समूह", "अनुभूति के समूह को", "sg"),
    "Saṅkhārakkhandho": ("मानसिक रचनाओं का समूह", "मानसिक रचनाओं के समूह को", "sg"),
    "Viññāṇakkhandho": ("चेतना का समूह", "चेतना के समूह को", "sg"),
    "Cattāro khandhā": ("चार समूह", "चार समूहों को", "pl"),
    "cattāro khandhā": ("चार समूह", "चार समूहों को", "pl"),
    "Tayo khandhā": ("तीन समूह", "तीन समूहों को", "pl"),
    "Dve khandhā": ("दो समूह", "दो समूहों को", "pl"),
}
RE_Q = re.compile(r'"([^"]*)"(ntipi|nti|tipi|ti pi|ti)')
RE_NV = re.compile(r"(siyā )?na vattabb[oā] – ")


def _norm_q(text, suffix):
    t = text.strip()
    if suffix.startswith("n"):
        t += "ṃ"
    w = t.split()
    if w and w[-1] == "cā":
        w[-1] = "ca"
    return " ".join(w)


def _read_pred(s, i):
    js = [j for j in (s.find(", ", i), s.find("; ", i), s.find("…pe…", i)) if j != -1]
    j = min(js) if js else len(s)
    return s[i:j].strip(), j


def pp_clauses(rest):
    cl, i, sep = [], 0, ""
    while i < len(rest):
        if rest.startswith(", ", i):
            sep, i = ", ", i + 2
            continue
        if rest.startswith("; ", i):
            sep, i = "; ", i + 2
            continue
        if rest.startswith("…pe… ", i):
            sep, i = "… ", i + len("…pe… ")
            continue
        m = RE_NV.match(rest, i)
        if m:
            i = m.end()
            qs = []
            while True:
                q = RE_Q.match(rest, i)
                if not q:
                    raise ValueError("bad quote list at: " + rest[i:i + 60])
                qs.append(_norm_q(q.group(1), q.group(2)))
                i = q.end()
                if q.group(2) in ("ti", "nti"):
                    break
                if rest.startswith(", ", i) and RE_Q.match(rest, i + 2):
                    i += 2
                    continue
                break
            cl.append(("SIYA_NV" if m.group(1) else "NV", qs, sep))
        elif rest.startswith('"', i):
            q = re.compile(r'"([^"]*)"').match(rest, i)
            cl.append(("BAREQ", q.group(1), sep))
            i = q.end()
        elif rest.startswith("siyā ", i):
            pred, i = _read_pred(rest, i + 5)
            cl.append(("SIYA", pred, sep))
        else:
            pred, i = _read_pred(rest, i)
            cl.append(("BARE", pred, sep))
        sep = ""
    return cl


def pp_sentence(s):
    for key in sorted(SUBJ, key=len, reverse=True):
        if s.startswith(key + " "):
            nom, obl, num = SUBJ[key]
            rest = s[len(key) + 1:]
            break
    else:
        raise ValueError("no subject: " + s[:60])
    pl = num == "pl"
    cop = "हैं" if pl else "है"
    hota = "होते हैं" if pl else "होता है"
    pron = "वे" if pl else "वह"
    pron_obj = "उन्हें" if pl else "उसे"
    out, pron_needed = [], False
    for n, (kind, data, sep) in enumerate(pp_clauses(rest)):
        first = n == 0
        lead = nom + " " if first else (pron + " " if pron_needed and kind in ("BARE", "BAREQ", "SIYA") else "")
        if kind in ("BARE", "SIYA", "BAREQ") and not first:
            pron_needed = False
        if kind == "BARE":
            pr = lex(data, num)
            vala = " होने वाले" if pl else " होने वाला"
            if "," not in pr and pr.endswith("साथ न" + vala):         # "... के साथ(-साथ) न होने वाला है" -> "... नहीं होता"
                t = f"{lead}{pr[:-len(' न' + vala)]} नहीं {'होते' if pl else 'होता'}"
            elif "," not in pr and pr.endswith("साथ" + vala):       # "... के साथ होने वाला है" -> "... के साथ होता है"
                t = f"{lead}{pr[:-len(vala)]} {hota}"
            elif "," not in pr and pr.endswith(" न" + vala):          # "... न होने वाला है" -> "... नहीं है"
                t = f"{lead}{pr[:-len(' न' + vala)]} नहीं {cop}"
            else:
                t = f"{lead}{pr} {cop}"
        elif kind == "BAREQ":
            t = f"{lead or pron + ' '}“{lex(data, num)}” {cop}"
        elif kind == "SIYA":
            pr = lex(data, num)
            vala = " होने वाले" if pl else " होने वाला"
            if "," not in pr and pr.endswith(" न" + vala):      # "... न होने वाला होता है" -> "... नहीं होता"
                pr = pr[:-len(" न" + vala)] + " नहीं"
            elif "," not in pr and (pr.endswith(" साथ" + vala) or pr.endswith(" साथ-साथ" + vala)):
                pr = pr[:-len(vala)]                              # "... के साथ होने वाला होता है" -> "... के साथ होता है"
            verb = (("होते" if pl else "होता") if pr.endswith(" नहीं") else hota)
            t = f"{lead}कभी {pr} {verb}"
        else:
            qs = [lex(q, num) for q in data]
            ql = f"“{qs[0]}”" if len(qs) == 1 else ", ".join(f"न “{q}”" for q in qs)
            if kind == "NV":
                t = f"{obl if first else pron_obj} नहीं कहा जा सकता {DASH} {ql}"
            else:
                t = f"{lead if first else ''}कभी {pron_obj} नहीं कहा जा सकता {DASH} {ql}"
            pron_needed = True
        out.append((sep if not first else "") + t)
    return "".join(out)


RE_SUBSPLIT = re.compile(r", (?=cattāro khandhā )")
PP_FIX = {  # Pāli typing slips fixed before parsing (reported)
    'siyā na vattabbā – kilesasampayuttā ceva no ca kilesā"ti.': 'siyā na vattabbā – "kilesasampayuttā ceva no ca kilesā"ti.',
    "siyā araṇāti.": "siyā araṇā.",
}
PP_POST = {
    # siyā pītisahagato na sukhasahagato na upekkhāsahagato
    "कभी उल्लास के साथ होने वाला, पर सुख या समभाव के साथ न होने वाला होता है":
        "कभी उल्लास के साथ होता है, पर सुख या समभाव के साथ नहीं",
    # «भी»: both statements hold at once (kenaci viññeyyā, kenaci na viññeyyā)
    "; किसी एक प्रकार की चेतना से जाने जा सकने वाले हैं, किसी एक प्रकार की चेतना से न जाने जा सकने वाले हैं।":
        "; वे किसी एक प्रकार की चेतना से जाने जा सकने वाले भी हैं, किसी एक प्रकार की चेतना से न जाने जा सकने वाले भी हैं।",
}


def pp_line(p):
    for a, b in PP_FIX.items():
        p = p.replace(a, b)
    sents = re.split(r"(?<=\.) ", p)
    res = []
    for s in sents:
        assert s.endswith("."), s[-40:]
        subs = RE_SUBSPLIT.split(s[:-1])
        res.append(", ".join(pp_sentence(x) for x in subs) + "।")
    h = " ".join(res)
    for a, b in PP_POST.items():
        h = h.replace(a, b)
    return h


# ---------------------------------------------------------------- fixed lines
FIXED = {
    "Dukamūlakaṃ.": "दो-दो के वर्गीकरणों पर आधारित क्रम।",
    "Tikamūlakaṃ.": "तीन-तीन के वर्गीकरणों पर आधारित क्रम।",
    "Ubhatovaḍḍhakaṃ.": "दोनों ओर से बढ़ने वाला क्रम।",
    "(Yathā kusalattike vitthāro, evaṃ sabbepi tikā vitthāretabbā.)":
        "(जैसे “हितकर” से शुरू होने वाले तीन के वर्गीकरण का विस्तार किया गया है, वैसे ही सभी तीन-तीन के वर्गीकरणों का विस्तार करना चाहिए।)",
    "Abhidhammabhājanīyaṃ.": S.SECTION_TITLES["Abhidhammabhājanīyaṃ"] + "।",
    "#### Pañhāpucchakaṃ": "#### " + S.SECTION_TITLES["Pañhāpucchakaṃ"],
    "Pañhāpucchakaṃ.": S.SECTION_TITLES["Pañhāpucchakaṃ"] + "।",
    "Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.":
        S.FIVE_AGGREGATES + "।",
    "Pañcannaṃ khandhānaṃ kati kusalā, kati akusalā, kati abyākatā…pe… kati saraṇā, kati araṇā?":
        "पाँच समूहों में से कितने हितकर हैं, कितने हानिकर हैं, कितने नैतिक रूप से अनिर्धारित हैं… "
        "कितने संघर्ष वाले हैं, कितने संघर्ष से रहित हैं?",
    "##### Tikaṃ": "##### तीन-तीन के वर्गीकरण",
    "##### Dukaṃ": "##### दो-दो के वर्गीकरण",
    "Sappaccayā, saṅkhatā.": "पाँचों समूह कारणों पर निर्भर रहने वाले हैं, निर्मित हैं।",
    "Khandhavibhaṅgo niṭṭhito.": S.CHAPTER_TITLES[1] + " पूरा हुआ।",
}
BODY_FIX = {  # missing comma in the Pāli (^2-120): "atthi bahiddhārammaṇo atthi ajjhattabahiddhārammaṇo"
    "atthi bahiddhārammaṇo atthi ajjhattabahiddhārammaṇo": "atthi bahiddhārammaṇo, atthi ajjhattabahiddhārammaṇo",
}


def translate(p, section):
    if p.startswith("##### "):
        k = p[6:].strip()
        return FIXED.get(p) or "##### " + khandha(k)
    if p in FIXED:
        return FIXED[p]
    if section == "pp":
        return pp_line(p)
    for a, b in BODY_FIX.items():
        p = p.replace(a, b)
    return ab_line(p)


def main():
    missing = [s for s in PI1_FPL if s + " परिघटनाएँ" not in re.sub(r"\s*\[[^\]]*\]", "", open(PI1_MATIKA, encoding="utf-8").read())]
    assert not missing, "pi-1 mātikā strings not found: " + " | ".join(missing)
    S.check_pi1()
    pali = open(os.path.join(S.PALI_DIR, CH), encoding="utf-8").read().splitlines()
    sample = open(os.path.join(S.HERE, "ch1-sample.md"), encoding="utf-8", newline="").read()
    assert pali[S.SAMPLE_LAST_PALI_LINE - 1].endswith("^2-33") and sample.endswith("^2-33\n")
    out, section = [], "ab"
    for p in pali[S.SAMPLE_LAST_PALI_LINE:]:
        if not p.strip():
            out.append("")
            continue
        m = S.ID.search(p)
        core = p[:m.start()] if m else p
        if core.startswith("#### Pañhāpucchakaṃ"):
            section = "pp"
        h = translate(core.strip(), section)
        out.append(h + (" " + m.group(1) if m else ""))
    text = sample + "\n".join(out) + "\n"
    with open(os.path.join(S.HI_DIR, CH), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("written", CH, len(text.splitlines()), "lines")


if __name__ == "__main__":
    main()
