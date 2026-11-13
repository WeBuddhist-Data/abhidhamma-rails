"""pi-7 Hindi keyword maps for 4-02, 4-08 .. 4-14 (dukatika). Uses map_sample_hi.py read-only.

usage: python -I -B -X utf8 map_4-02_4-14_hi.py [--audit] [--only <file>]
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa: F401,F403

FILES = ("4-02-dukatika-hetuduka", "4-08-dukatika-nivaranaduka", "4-09-dukatika-paramasaduka",
         "4-10-dukatika-sarammanaduka", "4-11-dukatika-upadanaduka", "4-12-dukatika-kilesaduka",
         "4-13-dukatika-dassanenapahatabbaduka", "4-14-dukatika-saranaduka")

T = {}
_ADJ_END = ("aṃ", "o", "ā", "assa", "e", "a", "ānaṃ", "añca")
# dyad items of the sārammaṇa / mahantara / piṭṭhi dyads (pi-1 1-matika wording; noX / naX / aX keep the negative)
for _st, _h, _neg in (
    ("cetasik", "मन का सहचर", "मन का सहचर न होने वाला"),
    ("cittasampayutt", "मन से जुड़ा", None), ("cittavippayutt", "मन से अलग", None),
    ("cittasaṃsaṭṭh", "मन से घुला-मिला", "मन से घुला-मिला न होने वाला"),
    ("cittasamuṭṭhān", "मन से उत्पन्न", "मन से उत्पन्न न होने वाला"),
    ("cittasaṃsaṭṭhasamuṭṭhān", "मन से घुला-मिला और मन से उत्पन्न",
     "मन से घुला-मिला और मन से उत्पन्न न होने वाला"),
    ("ajjhattik", "आंतरिक", None), ("bāhir", "बाह्य", None),
    ("upādinn", "कर्म से उत्पन्न", "कर्म से उत्पन्न न होने वाला"),
    ("saṃkiliṭṭh", "क्लेशों से मलिन", "क्लेशों से मलिन न होने वाला"),
    ("savitakk", "आरंभिक विचार वाला", None), ("avitakk", "आरंभिक विचार से रहित", None),
    ("savicār", "सतत विचार वाला", None), ("avicār", "सतत विचार से रहित", None),
    ("sappītik", "उल्लास वाला", None), ("appītik", "उल्लास से रहित", None),
    ("kāmāvacar", "इंद्रिय-सुखों के लोक से संबंधित", "इंद्रिय-सुखों के लोक से संबंधित न होने वाला"),
    ("rūpāvacar", "सूक्ष्म भौतिक लोक से संबंधित", "सूक्ष्म भौतिक लोक से संबंधित न होने वाला"),
    ("arūpāvacar", "अभौतिक लोक से संबंधित", "अभौतिक लोक से संबंधित न होने वाला"),
    ("pariyāpann", "अस्तित्व के लोकों में समाया हुआ", None),
    ("apariyāpann", "अस्तित्व के लोकों में न समाया हुआ", None),
    ("niyyānik", "मुक्ति की ओर ले जाने वाला", None), ("aniyyānik", "मुक्ति की ओर न ले जाने वाला", None),
    ("sauttar", "सर्वोच्च न होने वाला", None), ("anuttar", "सर्वोच्च", None),
    ("saraṇ", "संघर्ष वाला", None), ("araṇ", "संघर्ष से रहित", None),
):
    for _e in _ADJ_END:
        T[_st + _e] = _h
        if _neg:
            T["a" + _st + _e] = _neg
            T["no" + _st + _e] = _neg
            T["na" + _st + _e] = _neg
for _st, _h, _neg in (                        # -bhu / -ī stems
    ("cittasahabh", "मन के साथ-साथ होने वाला", "मन के साथ-साथ न होने वाला"),
    ("cittānuparivatt", "मन का अनुसरण करने वाला", "मन का अनुसरण न करने वाला"),
    ("cittasaṃsaṭṭhasamuṭṭhānānuparivatt", "मन से घुला-मिला मन से उत्पन्न और मन का अनुसरण करने वाला",
     "मन से घुला-मिला मन से उत्पन्न और मन का अनुसरण न करने वाला"),
):
    for _e in ("uṃ", "ū", "uno", "unā", "iṃ", "ī", "ino", "issa", "īnaṃ", "i"):
        T[_st + _e] = _h
        T["no" + _st + _e] = _neg
for _e in _ADJ_END:
    T["anupādinn" + _e] = "कर्म से उत्पन्न न होने वाला"
T.update({
    "upādā": "व्युत्पन्न", "noupādā": "व्युत्पन्न न होने वाला",
    "upādinnaṃ": "कर्म से उत्पन्न",
    # neva dassanena na bhāvanāya / na dassanena / na bhāvanāya (the negative stays where the Hindi has it)
    "nevadassanena": "न सत्य-दर्शन", "nabhāvanāya": ("न मानसिक अभ्यास", "मानसिक अभ्यास से न"),
    "nadassanena": "सत्य-दर्शन से न",
    "dassane": "सत्य-दर्शन से छोड़ा जाने वाला", "nadassane": "सत्य-दर्शन से न छोड़ा जाने वाला",
    "nevavipākanavipākadhammadhammaṃ": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",     # pi-2
    "nevavipākanavipākadhammadhammo": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "nevavipākanavipākadhammadhammassa": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "hetuduka": "मूल वाला दो का वर्गीकरण",
    "labbhati": "लागू होना",                                         # pi-3
    "imamhi": "यह", "imaṃ": "यह", "gamanaṃ": "प्रसंग",
    "kamma": "कर्म-कारण", "avigata": "अविलीनता-कारण",                # count misprints (kamma nava, avigata nava)
    "ārammaṇa": "विषय-कारण",                                         # heading «Hetu-ārammaṇa-adhipatipaccayā»
    "kātabbaṃ": "करना चाहिए", "kātabbā": "करना चाहिए", "kātabbo": "करना चाहिए",
    "ādimhi": "शुरुआत", "majjhe": "बीच", "ghaṭane": "संयोजन", "pañhā": "प्रश्न",
    "adhipatī": "प्रधानता",
    "moho": "मोह", "vicikicchaṃ": "संशय", "vicikicchañca": "संशय", "uddhaccañca": "बेचैनी",
    "vicikicchāsahagate": "संशय के साथ होने वाला", "vicikicchāsahagato": "संशय के साथ होने वाला",
    "uddhaccasahagate": "बेचैनी के साथ होने वाला", "uddhaccasahagato": "बेचैनी के साथ होने वाला",
    "vicikicchānīvaraṇaṃ": "संशय की बाधा", "uddhaccanīvaraṇaṃ": "बेचैनी की बाधा",
    "avijjānīvaraṇaṃ": "अज्ञान की बाधा",                             # pi-1/pi-5
    "sampayuttake": "जुड़ा हुआ",
    "mahantaraduke": "बीच के बड़े दो-दो के वर्गीकरण",
    "cetasikadukamūlā": "मन की सहचर परिघटनाओं वाले दो के वर्गीकरण पर आधारित",
    # «X-duka-Y-sadisaṃ» = «X वाले दो के वर्गीकरण के Y पद के समान» (the text's wording)
    "cittadukakusalasadisaṃ": "मन रूपी परिघटनाओं वाले दो के वर्गीकरण के हितकर पद के समान",
    "cittasaṃsaṭṭhasamuṭṭhānadukaabyākatasadisaṃ":
        "मन से घुली-मिली और मन से उत्पन्न परिघटनाओं वाले दो के वर्गीकरण के नैतिक रूप से अनिर्धारित पद के समान",
    "lokiyadukasadisaṃ": "लौकिक परिघटनाओं वाले दो के वर्गीकरण के समान",
    "lokiyadukakusalasadisaṃ": "लौकिक परिघटनाओं वाले दो के वर्गीकरण के हितकर पद के समान",
    "lokiyadukaabyākatasadisaṃ": "लौकिक परिघटनाओं वाले दो के वर्गीकरण के नैतिक रूप से अनिर्धारित पद के समान",
    "upādānadukaakusalasadisaṃ": "आसक्ति वाले दो के वर्गीकरण के हानिकर पद के समान",
    "kilesadukaakusalasadisaṃ": "मन के क्लेश वाले दो के वर्गीकरण के हानिकर पद के समान",
    "sappītikadukasadisaṃ": "उल्लास वाले दो के वर्गीकरण के समान",
    "kāmāvacaradukaabyākatasadisaṃ":
        "इंद्रिय-सुखों के लोक वाले दो के वर्गीकरण के नैतिक रूप से अनिर्धारित पद के समान",
})
# negative ablative naXpaccayā: «<name> के बिना»; in the double headings «Nahetu-naārammaṇapaccayā» the text
# has the noun «… का अभाव और … का अभाव», so the noun value is the second alternative.
for _st, _name, _loc, _neg, _plain in CONDITIONS:
    T[_neg + _st + "paccayā"] = (f"{_name} के बिना", f"{_name} का अभाव")
T.update({
    "pahātabbahetukaṃ": ("छोड़े जाने वाले मूलों वाला", "छोड़े जाने वाले मूल"),   # «… मूलों से रहित» (na- form)
    "pahātabbahetuko": ("छोड़े जाने वाले मूलों वाला", "छोड़े जाने वाले मूल"),
})
OVR = {f: {} for f in FILES}
OVR["4-10-dukatika-sarammanaduka"]["7-44-52"] = {"kātabbo": "लेना चाहिए"}   # «… भोजन लेना चाहिए»
OVR["4-02-dukatika-hetuduka"]["7-36-11"] = {"anuloma": "सकारात्मक"}   # «anuloma paccanīyaṃ» = «सकारात्मक-नकारात्मक क्रम»
OVR["4-10-dukatika-sarammanaduka"]["7-44-42"] = {"cittasampayuttadukaṃ": "मन से जुड़ाव वाला दो का वर्गीकरण"}
# «Nadassanena / Nabhāvanāya pahātabbahetuka-» = «सत्य-दर्शन / मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित»:
# the negative is rendered by «रहित» (applied in resolver_for)
NA_HETUKA = {"nadassanena": "सत्य-दर्शन … रहित", "nabhāvanāya": "मानसिक अभ्यास … रहित"}
ALLOWED = {f: {} for f in FILES}
_FEM = "regular feminine of the masc. dictionary form: text «समाई हुई» = समाया हुआ (pi-2/pi-3 value)"
for _b in ("7-47-85", "7-47-87", "7-47-88"):
    ALLOWED["4-13-dukatika-dassanenapahatabbaduka"][(_b, "Pariyāpannaṃ")] = _FEM
    ALLOWED["4-13-dukatika-dassanenapahatabbaduka"][(_b, "Apariyāpannaṃ")] = _FEM


def resolver_for(f, table, ovr, log=None):
    """map_sample_hi resolver, with the closing-pair rule also applied where the -vippayutta word is in the
    segment's Pāli but not in its keyword list (e.g. 7-42-31: keywords nīvaraṇiyaṃ … only)."""
    hi, pa = read_hindi(f), read_pali(f)
    base = make_resolver(f, table, ovr, log)

    def res(bid, kw, kws):
        if kw in ovr.get(bid, {}):
            return base(bid, kw, kws)
        text, pali = hi.get(bid), pa.get(bid) or ""
        k = lc(kw)
        if k in NA_HETUKA and re.search(r"(?<!nevadassanena )\b" + k + r" pahātabbahetuk", pali.lower()):
            v = NA_HETUKA[k]
            if log is not None:
                log.setdefault((kw, v), collections.Counter())["table"] += 1
            return v
        if (heading_value(kw, pali, text) is None and "vippayutt" in pali.lower()
                and text is not None and ("उनका विषय" in text or "उसका विषय" in text)):
            v, _ = lookup(kw, kws, table, text, closing=True)
            if log is not None:
                log.setdefault((kw, v), collections.Counter())["table"] += 1
            return v
        return base(bid, kw, kws)
    return res


if __name__ == "__main__":
    files = FILES
    if "--only" in sys.argv:
        files = (sys.argv[sys.argv.index("--only") + 1],)
    for f in files:
        try:
            build_part(f, resolver_for(f, {**PI7, **T}, OVR[f]))
        except SystemExit as e:
            print(e)
            continue
        verify(f, allowed=ALLOWED[f])
        if "--audit" in sys.argv:
            print("=" * 10, f, "fallbacks")
            audit(f, {**PI7, **T}, OVR[f], only_fallback=True)
