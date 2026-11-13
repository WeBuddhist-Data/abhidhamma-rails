"""pi-6 Pāli->Hindi keyword maps: 5-01/5-02/5-03-saccayamaka and 8-cittayamaka.

Imports the sample module map_sample_hi.py read-only (PI6, pi6_value, make_resolver, build_part, present ...)
and extends its table here. Wording from notes-5-8.md / build_5_hi.py / build_8_hi.py, as the harmonised
translation files have it (the translation file is the truth).

usage: python -I -X utf8 map_5_8_hi.py            build + verify all four files
       python -I -X utf8 map_5_8_hi.py <file> ...  only these
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True                      # no __pycache__ in the shared folder
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import (HERE, PI6, NDE, present, make_resolver, build_part, read_hindi,  # noqa: E402
                           read_keywords)

FILES = ("5-01-saccayamaka", "5-02-saccayamaka", "5-03-saccayamaka", "8-cittayamaka")

T = {}
# ---------------------------------------------------------------- Saccayamaka: truths and the bare words
T.update({
    "dukkhasaccaṃ": "दुःख का सत्य", "samudayasaccaṃ": "उत्पत्ति का सत्य",
    "nirodhasaccaṃ": "अंत का सत्य", "maggasaccaṃ": "मार्ग का सत्य",
    "saccāni": "सत्य", "saccā": "सत्य", "saccaṃ": "सत्य",
    "dukkhaṃ": "दुःख", "samudayo": "उत्पत्ति", "samudayaṃ": "उत्पत्ति", "nirodho": "अंत", "nirodhaṃ": "अंत",
    "maggo": "मार्ग", "maggaṃ": "मार्ग",
    "kāyikaṃ dukkhaṃ": "शारीरिक दुःख", "cetasikaṃ dukkhaṃ": "मानसिक दुःख",
    "avasesaṃ": "शेष", "avaseso": "शेष", "avasesā": "शेष",
    "avasese": "बाकी",                                            # avasese catuvokāre pañcavokāre = «बाकी …»
    "paṇṇattivāra": "शब्दावली का खंड",
})

# ---------------------------------------------------------------- Pavatti: moments, beings, places (build_5_hi WHO_TOKENS)
GEN = {
    "cittassa": "मन", "taṇhāya": "तृष्णा", "maggassa": "मार्ग", "aggamaggassa": "सर्वोच्च मार्ग",
    "phalassa": "फल", "aggaphalassa": "सर्वोच्च फल",
    "taṇhāvippayuttacittassa": "तृष्णा से अलग मन", "maggavippayuttacittassa": "मार्ग से अलग मन",
    "taṇhāvippayuttamaggavippayuttacittassa": "तृष्णा से अलग और मार्ग से अलग मन",
    "maggavippayuttataṇhāvippayuttacittassa": "मार्ग से अलग और तृष्णा से अलग मन",
    "upapatticittassa": "जन्म के मन", "pacchimacittassa": "अंतिम मन",
    "sarāgapacchimacittassa": "राग-युक्त अंतिम मन", "sarāgacittassa": "राग-युक्त मन",
    "pacchimakusalacittassa": "अंतिम हितकर मन", "kusalacittassa": "हितकर मन",
}
MOMENT = {"uppādakkhaṇe": "उत्पन्न होने का क्षण", "bhaṅgakkhaṇe": "भंग होने का क्षण"}
for _g, _h in GEN.items():
    T[_g] = _h
    for _k, _m in MOMENT.items():
        T[f"{_g} {_k}"] = f"{_h} के {_m}"                       # «मन के उत्पन्न होने के क्षण में» -> direct «… का क्षण»
T.update(MOMENT)
T.update({"uppādakkhaṇaṃ": MOMENT["uppādakkhaṇe"], "bhaṅgakkhaṇaṃ": MOMENT["bhaṅgakkhaṇe"], "khaṇaṃ": "क्षण"})
T.update({
    "pavatte": "जीवन के दौरान",
    "citte": "मन", "taṇhāvippayuttacitte": "तृष्णा से अलग मन", "akusale citte": "हानिकर मन",
    "vattamāne": "चलना",                                         # «… मन के चलते समय»; pi-1..5 vattamāne = चलना
    "apāye": "दुर्गति का लोक", "āpāyikānaṃ": "दुर्गति के प्राणी",
    # «चार या पाँच समूहों वाले अस्तित्व» (harmonise I3): catuvokāra keeps its own words, the gap is «या पाँच»
    "catuvokāre": ("चार समूहों वाला अस्तित्व", "चार … समूहों वाला अस्तित्व"),
    "catuvokāraṃ": ("चार समूहों वाला अस्तित्व", "चार … समूहों वाला अस्तित्व"),
    "catuvokārā": ("चार समूहों वाला अस्तित्व", "चार … समूहों वाला अस्तित्व"),
    "catuvokārānaṃ": ("चार समूहों वाले अस्तित्व के प्राणी", "चार … समूहों वाले अस्तित्व के प्राणी"),
    "asaññattā": "पहचान-रहित प्राणियों का लोक",                  # source slip for asaññasattā (6-5-76)
    # beings (gen. pl.): the Hindi head noun where the text has one («… लोगों में»), else the participle
    "abhisametāvīnaṃ": ("सत्यों का बोध पा चुके लोग", "सत्यों का बोध पा चुका"),
    "anabhisametāvīnaṃ": ("सत्यों का बोध न पाए लोग", "सत्यों का बोध न पाया"),
    "nirodhasamāpannānaṃ": "समाप्ति की ध्यान-अवस्था में लीन लोग",
    "aggamaggasamaṅgīnaṃ": "सर्वोच्च मार्ग से युक्त लोग", "pacchimacittasamaṅgīnaṃ": "अंतिम मन से युक्त लोग",
    "cittasamaṅgīnaṃ": "मन से युक्त लोग",
    "aggamaggasamaṅgī": "सर्वोच्च मार्ग से युक्त व्यक्ति", "aggamaggasamaṅgiṃ": "सर्वोच्च मार्ग से युक्त व्यक्ति",
    "arahantānaṃ": "अर्हत्", "arahā": "अर्हत्", "arahantaṃ": "अर्हत्",
    "puthujjanā": "साधारण व्यक्ति", "caññe": "दूसरे लोग", "puggalā": "व्यक्ति",
    "anantarā": "ठीक बाद",
    "aggamaggaṃ paṭilabhissanti": "सर्वोच्च मार्ग प्राप्त करेंगे",
    "aggamaggaṃ paṭilabhissānti": "सर्वोच्च मार्ग प्राप्त करेंगे",    # source slip (6-5-74)
    "maggaṃ paṭilabhissanti": "मार्ग प्राप्त करेंगे", "paṭilabhissanti": "प्राप्त करेंगे",
    "nirujjhiti": "समाप्त होना",                                    # source slip for nirujjhati (6-5-125)
})

# ---------------------------------------------------------------- editorial notes (harmonise N-yassaka)
T.update({
    "yassa yattha": "जिस व्यक्ति में जिस स्थान",
    "yassakampi": "व्यक्ति वाला भाग", "yassakaṃ": "व्यक्ति वाला भाग",
    "yatthakampi": "स्थान वाला भाग", "yatthakaṃ": "स्थान वाला भाग",
    "yatthakā": ("स्थान वाला भाग", "स्थान वाला … भाग"),            # «स्थान वाले सभी भाग»
    "yassayatthakampi": "व्यक्ति और स्थान वाला भाग", "yassayatthakepi": "व्यक्ति और स्थान वाला भाग",
    "yatthakasadisaṃ": "स्थान वाले भाग के समान", "yassayatthakasadisaṃ": "व्यक्ति और स्थान वाले भाग के समान",
    "(no direct equivalent)": NDE,                                 # keyword-list artefact, kept as given
    "uppādepi": "उत्पन्न होना", "nirodhepi": "समाप्त होना", "uppādanirodhepi": "उत्पन्न होना और समाप्त होना",
    "uppādavāre": "उत्पन्न होने का खंड", "uppādavārepi": "उत्पन्न होने का खंड",
    "nirodhavāre": "समाप्त होने का खंड", "nirodhavārepi": "समाप्त होने का खंड",
    "uppādanirodhavārepi": "उत्पन्न होने और समाप्त होने का खंड",
    "pucchā": "प्रश्न", "anulomampi": "सकारात्मक", "paccanīkampi": "नकारात्मक",
})

# ---------------------------------------------------------------- Pariññāvāra (build_5_hi PARI)
T.update({
    "parijānāti": "पूरी तरह समझना", "parijānanti": "पूरी तरह समझना",
    "parijānittha": "पूरी तरह समझा था", "parijānissati": "पूरी तरह समझेगा",
    "pajahati": "छोड़ना", "nappajahati": "नहीं छोड़ना",
    "pajahittha": "छोड़ा था", "nappajahittha": "नहीं छोड़ा था",
    "pajahissati": "छोड़ेगा", "nappajahissati": "नहीं छोड़ेगा", "nappajahissanti": "नहीं छोड़ेंगे",
})

# ---------------------------------------------------------------- Cittayamaka (notes-5-8.md «Cittayamaka»)
T.update({
    "suddhacittasāmaññaṃ": "सामान्य रूप से केवल मन", "suddhacittasāmañña": "सामान्य रूप से केवल मन",
    "uppādanirodhakālasambhedavāro": "उत्पन्न होने और समाप्त होने के समयों के मेल का खंड",
    "uppāduppannavāro": "उत्पन्न होने और उत्पन्न हो चुके होने का खंड",
    "nirodhuppannavāro": "समाप्त होने और उत्पन्न हो चुके होने का खंड",
    "nanirodhavāro": "समाप्त न होने का खंड",
    "uppajjamānananirodhavāro": "उत्पन्न होते हुए होने और समाप्त न होने का खंड",
    "uppajjamānuppannavāro": "उत्पन्न होते हुए होने और उत्पन्न हो चुके होने का खंड",
    "nirujjhamānuppannavāro": "समाप्त होते हुए होने और उत्पन्न हो चुके होने का खंड",
    "uppannuppādavāro": "उत्पन्न हो चुके होने और उत्पन्न होने का खंड",
    "uppannuppajjamānavāro": "उत्पन्न हो चुके होने और उत्पन्न होते हुए होने का खंड",
    "niruddhanirujjhamānavāro": "समाप्त हो चुके होने और समाप्त होते हुए होने का खंड",
    "atikkantakālavāro": "समय बीत चुकने का खंड",
    "suttantacittamissakaviseso": "सुत्तों के मन के प्रकारों से मिला विशेष रूप",
    "abhidhammacittamissakaviseso": "अभिधम्म के मन के प्रकारों से मिला विशेष रूप",
    # the mind kinds (pi-2 ch. 7 wording, as in the text)
    "sarāgaṃ": "राग-युक्त", "vītarāgaṃ": "राग से मुक्त", "sadosaṃ": "द्वेष-युक्त", "samohaṃ": "मोह-युक्त",
    "saṃkhittaṃ": "सिमटा हुआ", "vikkhittaṃ": "बिखरा हुआ", "mahaggataṃ": "उन्नत",
    "amahaggataṃ": "उन्नत न होने वाला", "sauttaraṃ": "सर्वोच्च न होने वाला", "anuttaraṃ": "सर्वोच्च",
    "samāhitaṃ": "एकाग्र", "asamāhitaṃ": "एकाग्रता से रहित", "vimuttaṃ": "मुक्त", "avimuttaṃ": "अमुक्त",
    "sampayuttaṃ": "जुड़ा", "vedanāya": "अनुभूति",
    "saraṇaaraṇā": "संघर्ष वाला और संघर्ष से रहित", "araṇaṃ": "संघर्ष से रहित",
    "kusalaṃ cittaṃ": "हितकर मन", "akusalaṃ cittaṃ": "हानिकर मन", "abyākataṃ cittaṃ": "नैतिक रूप से अनिर्धारित मन",
    # time of a mind: «अतीत का / भविष्य का / वर्तमान / अतीत और भविष्य का मन»
    "atītaṃ": "अतीत का", "anāgataṃ": "भविष्य का", "paccuppannaṃ": "वर्तमान", "atītānāgataṃ": "अतीत और भविष्य का",
    "cittake": "मन … वाला भाग",                                    # «“जिस व्यक्ति में मन” वाला भाग»
    "yamakāni": "भाग",                                             # «ये तीनों भाग» (6-8-116)
})

# per-segment overrides {file: {bid: {kw: value}}}
OVR = {f: {} for f in FILES}

# ---------------------------------------------------------------- presence check
# map_sample_hi.present() plus three regular forms that the pi-1/pi-6 checker does not model:
#   अर्हत् ~ अर्हतों (oblique plural), न पाया ~ न पाए (participle agreeing with a plural noun),
#   and «X भी Y» where a ceva … ca answer puts «भी» inside the verb phrase («उत्पन्न भी हो चुका है»).
_BHI = re.compile(r"(?<=\S) भी(?= )")


def present_ext(v, text):
    if present(v, text):
        return "plain"
    for a, b in (("अर्हत्", "अर्हत"), ("पाया", "पाए")):
        if a in v and present(v.replace(a, b), text):
            return "inflection"
    if text and present(v, _BHI.sub("", text)):
        return "bhi"
    return None


def verify(f, allowed=None, show=80):
    allowed = allowed or {}
    a = [l.split("] ", 1) for l in (HERE / f"{f}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for i, (x, y) in enumerate(zip(a, b))
           if len(x) > 1 and [k.strip() for k in x[1].split(", ")] != [k.split("=", 1)[0] for k in y[1].split(", ")]]
    hi = read_hindi(f)
    nde, miss, exc, tol = 0, [], [], []
    for x in b:
        if len(x) < 2:
            continue
        bid, rest = x[0][1:], x[1]
        text = hi.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
                continue
            how = present_ext(v, text) if text is not None else None
            if how is None:
                (exc if (bid, kw) in allowed else miss).append((bid, kw, v))
            elif how != "plain":
                tol.append((how, bid, kw, v))
    print(f, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss),
          "| listed exceptions", len(exc), "| via extra tolerance", len(tol))
    for m in miss[:show]:
        print("   MISS", *m)
    for e in exc:
        print("   EXC ", *e, "--", allowed[(e[0], e[1])])
    return bad, nde, miss, tol


ALLOWED = {f: {} for f in FILES}


def resolver_5_8(f, table, ovr):
    """make_resolver, but a tuple value of THIS table picks its alternative with present_ext (so «न पाया»
    is chosen on «… न पाए जन्म लेने वालों में», where the plain checker finds neither alternative)."""
    base = make_resolver(f, table, ovr)
    hi = read_hindi(f)

    def resolver(bid, kw, kws):
        k = kw[0].lower() + kw[1:]
        v = T.get(k)
        if isinstance(v, tuple) and kw not in ovr.get(bid, {}):
            text = hi.get(bid)
            for alt in v:
                if text is not None and present_ext(alt, text):
                    return alt
            return v[0]
        return base(bid, kw, kws)
    return resolver


if __name__ == "__main__":
    args = sys.argv[1:]
    tolmode = "--tol" in args
    files = [x for x in args if not x.startswith("--")] or FILES
    table = {**PI6, **T}
    for _f in files:
        build_part(_f, resolver_5_8(_f, table, OVR[_f]))
        _, _, _, _tol = verify(_f, ALLOWED[_f])
        if tolmode:
            for t in _tol:
                print("   TOL ", *t)
