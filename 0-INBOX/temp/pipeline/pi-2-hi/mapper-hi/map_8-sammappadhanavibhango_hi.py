"""pi-2 Pāli->Hindi keyword map: 8-sammappadhanavibhango.

usage: python -I -X utf8 map_8-sammappadhanavibhango_hi.py
Imports map_sample_hi (read-only) and the shared table of chapters 2/3/8/9; extends them here only.
"""
import importlib
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import PP_SEGMENTS, NDE, build_part, verify, read_hindi, lc  # noqa: E402
C = importlib.import_module("map_2-3-8-9_common_hi")

CH = "8-sammappadhanavibhango"
PP_SEGMENTS.update({"2-429", "2-430"})

T = {
    # padhāna = प्रयत्न, sammappadhāna = सही प्रयत्न (builder / the Hindi headings)
    "padhāna": "प्रयत्न", "padhānā": "प्रयत्न", "padhānaṃ": "प्रयत्न", "padhānānaṃ": "प्रयत्न",
    "sammappadhānā": "सही प्रयत्न", "sammappadhānaṃ": "सही प्रयत्न", "sammappadhānānaṃ": "सही प्रयत्न",
    "sammappadhānavibhaṅgo": "सही प्रयत्न का विश्लेषण",
    # «Tīṇi akusalamūlāni – lobho, doso, moho. Tadekaṭṭhā ca kilesā. Taṃsampayutto … taṃsamuṭṭhānaṃ …»
    "mūlāni": "मूल", "akusalamūlāni": "हानिकर मूल", "kusalamūlāni": "हितकर मूल",
    "lobho": "लोभ", "doso": "द्वेष", "moho": "मोह", "ekaṭṭhā": "साथ रहने वाला",
    "sampayutto": "जुड़ा", "samuṭṭhānaṃ": "उत्पन्न", "saṅkhāra": "मानसिक रचनाएँ",
    "kāya": "शारीरिक", "kāyakammaṃ": "शारीरिक कर्म", "vacī": "वाणी", "vacīkammaṃ": "वाणी का कर्म",
    "manokammaṃ": "मानसिक कर्म",
    # «Imaṃ chandaṃ janeti sañjaneti uṭṭhapeti samuṭṭhapeti nibbatteti abhinibbatteti»
    "imaṃ chandaṃ janeti": "इस चाह को जगाना", "sañjaneti": "भली-भाँति जगाना",
    "samuṭṭhapeti": "भली-भाँति उठाना", "nibbatteti": "पैदा करना",
    # «Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti» (Hindi order kept, see value())
    "imaṃ vīriyaṃ ārabhati": "इस उत्साह को जगाना", "samārabhati": "भली-भाँति जगाना",
    # «Imaṃ cittaṃ paggaṇhāti sampaggaṇhāti upatthambheti paccupatthambheti»
    "imaṃ cittaṃ paggaṇhāti": "इस मन को तत्पर करना", "sampaggaṇhāti": "भली-भाँति तत्पर करना",
    "upatthambheti": "सहारा देना", "paccupatthambheti": "दृढ़ सहारा देना",
    # quoted headwords («Chandaṃ janetīti» = «“चाह जगाता है”» …)
    "vāyamatīti": "प्रयास करना", "padahatīti": "पूरा ज़ोर लगाना", "paggaṇhātīti": "तत्पर करना",
    "cittaṃ paggaṇhātīti": "मन को तत्पर करना", "janetīti": "जगाना", "chandaṃ janetīti": "चाह जगाना",
    "ārabhatīti": "जगाना", "vīriyaṃ ārabhatīti": "उत्साह जगाना",
    # «Yā ṭhiti so asammoso … yā bhāvanā sā pāripūrī»
    "vepullaṃ": "विपुलता", "asammoso": "लुप्त न होना", "pāripūrī": "परिपूर्णता",
    "citta": "मन",
}
TABLE = {**C.SHARED_TABLE, **T}

# «Imaṃ vīriyaṃ ārabhati samārabhati āsevati bhāveti bahulīkaroti» =
# «… जगाता है, भली-भाँति जगाता है, उसका बार-बार अभ्यास करता है, उसे विकसित करता है, उसका बहुत अधिक सेवन करता है»
VIRIYA_STRING = {"āsevati": "बार-बार अभ्यास करना", "bhāveti": "विकसित करना", "bahulīkaroti": "बहुत अधिक सेवन करना"}

OVR = {
    # «Vipākadhammadhammā» = «कर्म-फल उत्पन्न करने वाले हैं»: the dhammā fragment has no word of its own
    "2-429": {"dhammā": NDE, "uppannā": "उत्पन्न हो चुका"},
}


def value(bid, kw, kws, text):
    k = lc(kw)
    if k in VIRIYA_STRING and "samārabhati" in kws:
        return VIRIYA_STRING[k]
    return C.shared_value(kw, kws, TABLE, bid, text)


def resolver(bid, kw, kws, _hi={}):
    if not _hi:
        _hi.update(read_hindi(CH))
    o = OVR.get(bid, {})
    if kw in o:
        return o[kw]
    return value(bid, kw, kws, _hi.get(bid))


ALLOWED = {}

if __name__ == "__main__":
    build_part(CH, resolver)
    verify(CH, allowed=ALLOWED)
