"""pi-7 Pāli->Hindi keyword maps for 5-05 .. 5-20 (paccanīya, anulomapaccanīya, paccanīyānuloma parts).

Conventions: hi-map-conventions-pi7.md (binding) plus, for the negated items of these parts:
  * naX / noX / nanaX (no table entry of its own) = the value of X with the negation the Hindi uses:
    «X न होने वाला» (nakusalaṃ = हितकर न होने वाला, nanahetuṃ = मूल रूपी न होने वाला न होने वाला);
    where the Hindi puts «न» inside the phrase, that form is chosen when present in the segment
    (napītisahagataṃ = उल्लास के साथ न होने वाला, nocittānuparivattī = मन का अनुसरण न करने वाला).
  * a negated member of a multi-word item carries the negation through a gap:
    nadukkhāya (vedanāya sampayuttaṃ) = दुःखद … न होने वाला, nadassanena (pahātabbaṃ) = सत्य-दर्शन से न
    (text «सत्य-दर्शन से न छोड़ी जाने वाली», as 5-02 / 5-04); with pahātabbahetuko = सत्य-दर्शन … से रहित;
    in «nevadassanena nabhāvanāya» (text «न सत्य-दर्शन से, न मानसिक अभ्यास से») = न सत्य-दर्शन / न मानसिक अभ्यास.
usage: python -I -B -X utf8 map_5-05_5-20_hi.py [--audit]
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa: F401,F403
from map_sample_hi import (PI7, NDE, GAP, build_part, verify, audit, lookup, heading_value, present, lc,
                           read_hindi, read_pali, read_keywords, _is_closing, _pick)

FILES = [
    "5-05-paccaniya-dukatika", "5-06-paccaniya-tikaduka", "5-07-paccaniya-tikatika", "5-08-paccaniya-dukaduka",
    "5-09-anulomapaccaniya-tika", "5-10-anulomapaccaniya-duka", "5-11-anulomapaccaniya-dukatika",
    "5-12-anulomapaccaniya-tikaduka", "5-13-anulomapaccaniya-tikatika", "5-14-anulomapaccaniya-dukaduka",
    "5-15-paccaniyanuloma-tika", "5-16-paccaniyanuloma-duka", "5-17-paccaniyanuloma-dukatika",
    "5-18-paccaniyanuloma-tikaduka", "5-19-paccaniyanuloma-tikatika", "5-20-paccaniyanuloma-dukaduka",
]

T = {}


def _add(k, v):
    if k not in PI7:
        T.setdefault(k, v)


# --- positive items of the dyads / triads (masc. sg. of the frame wording; pi-1/pi-2 values where the same)
_A = ("aṃ", "o", "ā", "assa", "ānaṃ", "e", "añca", "a", "āni", "ena", "añceva")      # a-stems
_I = ("iṃ", "ī", "ino", "issa", "īnaṃ", "i", "iñca", "ī")                               # in-stems
_U = ("uṃ", "ū", "uno", "ussa", "ūnaṃ", "u", "uñca")                                     # ū-stems
ITEMS_A = {
    "sahetuk": "मूल वाला", "ahetuk": "मूल से रहित",
    "sappaccay": "कारणों पर निर्भर रहने वाला", "appaccay": "कारणों पर निर्भर न रहने वाला",
    "saṅkhat": "निर्मित", "asaṅkhat": "अनिर्मित",
    "sanidassan": "दिखाई देने वाला", "anidassan": "दिखाई न देने वाला",
    "sappaṭigh": "टकराव वाला", "appaṭigh": "टकराव से रहित",
    "sanidassanasappaṭigh": "दिखाई देने वाला और टकराव वाला",
    "lokiy": "लौकिक", "lokuttar": "लोकोत्तर",
    "citt": "मन",                                                   # cluster noun of «मन रूपी» (pi-1 term)
    "cetasik": "मन का सहचर", "acetasik": "मन का सहचर न होने वाला",   # pi-2
    "cittasampayutt": "मन से जुड़ा", "cittavippayutt": "मन से अलग",
    "cittasaṃsaṭṭh": "मन से घुला-मिला", "cittavisaṃsaṭṭh": "मन से घुला-मिला न होने वाला",
    "cittasamuṭṭhān": "मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhān": "मन से घुला-मिला और मन से उत्पन्न",
    "ajjhattik": "आंतरिक", "bāhir": "बाह्य",
    "upādinn": "कर्म से उत्पन्न", "anupādinn": "कर्म से उत्पन्न न होने वाला",
    "savitakk": "आरंभिक विचार वाला", "avitakk": "आरंभिक विचार से रहित",
    "savicār": "सतत विचार वाला", "avicār": "सतत विचार से रहित",
    "sappītik": "उल्लास वाला", "appītik": "उल्लास से रहित",
    "kāmāvacar": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacar": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacar": "अभौतिक लोक से संबंधित",
    "pariyāpann": "अस्तित्व के लोकों में समाया हुआ", "apariyāpann": "अस्तित्व के लोकों में न समाया हुआ",
    "niyyānik": "मुक्ति की ओर ले जाने वाला", "aniyyānik": "मुक्ति की ओर न ले जाने वाला",
    "niyat": "निश्चित",
    "sauttar": "सर्वोच्च न होने वाला", "anuttar": "सर्वोच्च",
    "saraṇ": "संघर्ष वाला", "araṇ": "संघर्ष से रहित",
    "sārammaṇ": "विषय वाला", "anārammaṇ": "विषय से रहित",
    "vipākadhammadhamm": "कर्म-फल उत्पन्न करने वाला",
    "nevavipākanavipākadhammadhamm": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",   # pi-2
    "uppann": "उत्पन्न हो चुका", "anuppann": "उत्पन्न न हुआ",                         # pi-2
    "vicikicchāsahagat": "संशय के साथ होने वाला", "uddhaccasahagat": "बेचैनी के साथ होने वाला",
    "sanidassan": "दिखाई देने वाला",
}
ITEMS_I = {
    "rūp": "भौतिक", "arūp": "अभौतिक",
    "cittānuparivatt": "मन का अनुसरण करने वाला",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatt": "मन से घुला-मिला मन से उत्पन्न और मन का अनुसरण करने वाला",
    "uppād": "उत्पन्न होने वाला",
}
ITEMS_U = {
    "cittasahabh": "मन के साथ-साथ होने वाला",
    "cittasaṃsaṭṭhasamuṭṭhānasahabh": "मन से घुला-मिला मन से उत्पन्न और मन के साथ-साथ होने वाला",
}
for _d, _ends in ((ITEMS_A, _A), (ITEMS_I, _I), (ITEMS_U, _U)):
    for _st, _h in _d.items():
        for _e in _ends:
            _add(_st + _e, _h)
for _k in ("upādā", "upādāya"):
    _add(_k, "व्युत्पन्न")
_add("vipākābyākataṃ", "कर्म के फल रूपी नैतिक रूप से अनिर्धारित")

# --- negated members of multi-word items (the negation carried through a gap, see the docstring)
T.update({
    "nasukhāya": "सुखद … न होने वाला", "nadukkhāya": "दुःखद … न होने वाला",
    "naadukkhamasukhāya": "न दुःखद न सुखद … न होने वाला",
    "nadassanena": "सत्य-दर्शन से न", "nabhāvanāya": ("न मानसिक अभ्यास", "मानसिक अभ्यास से न"),
    "nevadassanena": "न सत्य-दर्शन", "nanevadassanena": "न सत्य-दर्शन",
    "nakenaci": "किसी एक प्रकार की चेतना … न होने वाला",
})

T.update({
    "naviññeyyo": ("न जाना जा सकने वाला", "जाना जा सकने वाला न होने वाला"),
    "naviññeyyaṃ": ("न जाना जा सकने वाला", "जाना जा सकने वाला न होने वाला"),
    # «nadassanena pahātabbahetuko» = «सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित»: see NAHETUKA in the resolver
    "pahātabbahetukaṃ": ("छोड़े जाने वाले मूलों वाला", "छोड़े जाने वाले मूल"),
    "pahātabbahetuko": ("छोड़े जाने वाले मूलों वाला", "छोड़े जाने वाले मूल"),
})
# negative ablative in a heading («Nahetu-naārammaṇapaccayā» = «… और विषय-कारण का अभाव»): the noun
for _st, _name, _loc, _ng, _plain in CONDITIONS:
    T[_ng + _st + "paccayā"] = (f"{_name} के बिना", f"{_name} का अभाव")

# --- triad items in other cases; headings and instructions of these parts
T.update({
    "akusalena": "हानिकर", "abyākatena": "नैतिक रूप से अनिर्धारित", "kusalena": "हितकर",
    "abyākatāni": "नैतिक रूप से अनिर्धारित", "akusalāni": "हानिकर", "kusalāni": "हितकर",
    "hetuduka": ("मूल वाला दो का वर्गीकरण", "मूल-कारण के साथ दो कारणों का मेल"),
    "hetudukaṃ": ("मूल वाला दो का वर्गीकरण", "मूल-कारण के साथ दो कारणों का मेल"),
    "cūḷantaradukāni": "बीच के छोटे दो-दो के वर्गीकरण", "mahantaradukāni": "बीच के बड़े दो-दो के वर्गीकरण",
    "piṭṭhidukāni": "अंतिम दो-दो के वर्गीकरण",
    "saññojanādigocchakāni": "बंधनों का वर्ग आदि", "saññojanādigocchakaṃ": "बंधनों का वर्ग आदि",
    "āsavagocchakāni": "मन के मैलों का वर्ग",
    "sahetukādidukāni": "मूल वाली परिघटनाओं वाला दो का वर्गीकरण आदि",
    "saññojanādidukāni": "बंधन वाला दो का वर्गीकरण आदि", "hetvādidukāni": "मूल वाला दो का वर्गीकरण आदि",
    "hetusahetukadukādi": "मूल रूपी भी और मूल वाली भी परिघटनाओं वाला दो का वर्गीकरण आदि",
    "hetuhetusampayuttaduke": "मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं वाला दो का वर्गीकरण",
    "āsavaāsavasampayuttaduke": "मन के मैल और मन के मैलों से जुड़ाव वाला दो का वर्गीकरण",
    "ajjhattattiko": "स्वयं से संबंधित वाला तीन का वर्गीकरण",
    "anulomadukatikapaṭṭhānato": "सकारात्मक क्रम में दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "lokiyadukasadisaṃ": "लौकिक परिघटनाओं वाले दो के वर्गीकरण के समान",
    "sappaccayadukasadisaṃ": "कारणों पर निर्भर रहने वाली परिघटनाओं वाले दो के वर्गीकरण के समान",
    "sappaccayasadisaṃ": "कारणों पर निर्भर रहने वाला … के समान",
    "atītasadisaṃ": "अतीत का … के समान",
    "abyākatamūlaṃ": "नैतिक रूप से अनिर्धारित से शुरू होने वाली शृंखला",
    "abyākatamūle": "नैतिक रूप से अनिर्धारित से शुरू होने वाली शृंखला",
    "paccayavasena": "कारणों के अनुसार", "purimanayena": "पहले की विधि",
    "kātabbā": "बनाना चाहिए", "kātabbaṃ": "बनाना चाहिए", "labbhati": "मिलना",
    "ekapañhameva": "एक प्रश्न", "cittasamuṭṭhānarūpameva": "मन से उत्पन्न भौतिक रूप",
    "mohaṃ": "मोह", "ete": "यह", "ovattā": "उलट दिया गया", "natthi": "नहीं",   # «… नहीं है» (as 2-0x)
})

# --- counts (Hindi number words as the text writes them)
NUMBERS = {
    "ekaṃ": "एक", "dve": "दो", "tīṇi": "तीन", "cattāri": "चार", "pañca": "पाँच", "cha": "छह", "satta": "सात",
    "aṭṭha": "आठ", "nava": "नौ", "dasa": "दस", "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह",
    "cuddasa": "चौदह", "pannarasa": "पंद्रह", "soḷasa": "सोलह", "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह",
    "ekūnavīsa": "उन्नीस", "ekūnavīsati": "उन्नीस", "vīsa": "बीस", "vīsati": "बीस", "ekavīsa": "इक्कीस",
    "dvāvīsa": "बाईस", "tevīsa": "तेईस", "catuvīsa": "चौबीस", "pañcavīsa": "पच्चीस", "chabbīsa": "छब्बीस",
    "chabbīsati": "छब्बीस", "sattavīsa": "सत्ताईस", "aṭṭhavīsa": "अट्ठाईस", "ekūnatiṃsa": "उनतीस",
    "tiṃsa": "तीस", "pañcatiṃsa": "पैंतीस", "aṭṭhacattālīsa": "अड़तालीस", "ekūnapaññāsa": "उनचास",
}
for _k, _v in NUMBERS.items():
    _add(_k, _v)

# --- per-segment overrides {file: {bid: {kw: value}}} and presence exceptions {file: {(bid, kw): reason}}
OVR = {f: {} for f in FILES}
# «Vipākābyākataṃ kiriyābyākataṃ ekaṃ khandhaṃ» = «कर्म के फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित»
OVR["5-15-paccaniyanuloma-tika"]["7-69-1"] = {"Vipākābyākataṃ": "कर्म के फल रूपी … नैतिक रूप से अनिर्धारित"}
# «ārammaṇaṃ natthi» = «विषय-कारण नहीं है» (as 3-09)
OVR["5-11-anulomapaccaniya-dukatika"]["7-65-1"] = {"ārammaṇaṃ": "विषय-कारण"}

# presence exceptions: regular inflections the checker does not model (listed by verify() with the reason)
EXC_REASON = {
    "pariyāpann": "masc. dictionary form of the participle; text has the feminine «समाई हुई»",
    "ovattā": "masc. dictionary form; text has the feminine plural «उलट दी गई हैं»",
}
ALLOWED = {f: {} for f in FILES}


def _fill_allowed():
    for f in FILES:
        for bid, kws in read_keywords(f):
            for kw in kws:
                k = lc(kw)
                for stem, reason in EXC_REASON.items():
                    if stem in k:
                        ALLOWED[f][(bid, kw)] = reason


_fill_allowed()


# «nadassanena / nabhāvanāya pahātabbahetuko»: the Hindi renders the negation as «… मूलों से रहित»
NAHETUKA = {"nadassanena": "सत्य-दर्शन … से रहित", "nabhāvanāya": "मानसिक अभ्यास … से रहित"}


# ---------------------------------------------------------------------------- negation
def neg(v, text, no_form=False):
    """Negate an item value the way the Hindi does («X न होने वाला»; «न» inside the phrase where the text
    has it). Alternatives are picked by presence in the segment."""
    cands = [v + " न होने वाला"]
    inner = None
    if v.endswith(" होने वाला") and not v.endswith(" न होने वाला"):
        inner = v[: -len(" होने वाला")] + " न होने वाला"
    elif v.endswith(" करने वाला"):
        inner = v[: -len(" करने वाला")] + " न करने वाला"
    if inner:
        cands = [inner] + cands if no_form or "के साथ होने" in v and "साथ-साथ" not in v else cands + [inner]
    return _pick(tuple(cands), text)


def make_resolver520(f, table=None, ovr=None, log=None):
    table = {**PI7, **T} if table is None else table
    ovr = ovr or {}
    hi, pa = read_hindi(f), read_pali(f)

    def table_value(kw, kws, text):
        v, src = lookup(kw, kws, table, text, closing=_is_closing(kws, text))
        return v, src

    def resolve(kw, kws, text, depth=0):
        k = lc(kw)
        if k in NAHETUKA and text and "मूलों से रहित" in text:
            return NAHETUKA[k], "table"
        try:
            v, src = table_value(kw, kws, text)
        except KeyError:
            v, src = None, None
        if src == "table":
            return v, src
        if depth < 3 and len(k) > 4 and k[:2] in ("na", "no"):
            try:
                rv, rsrc = resolve(k[2:], kws, text, depth + 1)
            except KeyError:
                rv = None
            if rv is not None and rsrc in ("table", "neg") and rv != NDE:
                return neg(rv, text, no_form=k.startswith("no")), "neg"
        if v is None:
            raise KeyError(kw)
        return v, src

    def resolver(bid, kw, kws):
        o = ovr.get(bid, {})
        text = hi.get(bid)
        if kw in o:
            v, src = o[kw], "override"
        else:
            v = heading_value(kw, pa.get(bid), text)
            src = "heading"
            if v is None:
                v, src = resolve(kw, kws, text)
        if log is not None:
            log.setdefault((kw, v), {}).setdefault(src, 0)
            log[(kw, v)][src] += 1
        return v
    return resolver


if __name__ == "__main__":
    for f in FILES:
        build_part(f, make_resolver520(f, None, OVR[f]))
        verify(f, allowed=ALLOWED[f])
