"""pi-7 Pāli->Hindi keyword maps for 4-15 … 4-21 (tikaduka) and 5-01 … 5-04.
usage: python -I -B -X utf8 map_4-15_5-04_hi.py [file …]   (no args: all eleven files)
       add --audit to list every keyword whose value did not come from the table / heading / override.
Conventions: hi-map-conventions-pi7.md (map_sample_hi.py imported read-only). Additions here:
  * paccanīya items «naX / noX» not in the table = «<X> न होने वाला» (the Hindi «… न होने वाली परिघटना»),
    recursively (Nanoganthaṃ = गाँठ रूपी न होने वाला न होने वाला);
  * negative ablatives of the conditions are tuples: «<name> के बिना», or «<name> का अभाव» where a heading
    lists them («Nahetu-naārammaṇapaccayā» = «मूल-कारण का अभाव और विषय-कारण का अभाव»).
"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import *  # noqa
from map_sample_hi import (read_hindi, read_pali, read_keywords, lc, NDE, CONDITIONS, CLOSING,  # noqa
                           heading_value, lookup, _strip_particles, _pick, _is_closing)

FILES = ("4-15-tikaduka-hetuduka", "4-16-tikaduka-sappaccayaduka", "4-17-tikaduka-asavaduka",
         "4-18-tikaduka-sarammanaduka", "4-19-tikaduka-kilesaduka", "4-20-tikaduka-dassanenapahatabbaduka",
         "4-21-tikaduka-sauttaraduka", "5-01-anuloma-tikatika", "5-02-anuloma-dukaduka",
         "5-03-paccaniya-tika", "5-04-paccaniya-duka")

T = {}

# --- negative ablative: «के बिना» in the frames, «का अभाव» in the heading lists
for _st, _name, _loc, _neg, _plain in CONDITIONS:
    T[_neg + _st + "paccayā"] = (f"{_name} के बिना", f"{_name} का अभाव")
    # bare first members of the heading lists «Ārammaṇa-adhipati-anantarapaccayā» = the condition name
    if _st not in PI7:
        T[_st] = (_name, _plain) if _plain else _name

# --- numerals (prior maps: ग्यारह, बारह, पंद्रह …)
T.update({
    "ekādasa": "ग्यारह", "dvādasa": "बारह", "terasa": "तेरह", "cuddasa": "चौदह", "pannarasa": "पंद्रह",
    "soḷasa": "सोलह", "sattarasa": "सत्रह", "aṭṭhārasa": "अठारह", "ekūnavīsa": "उन्नीस", "vīsa": "बीस",
    "ekavīsa": "इक्कीस", "bāvīsa": "बाईस", "tevīsa": "तेईस", "catuvīsa": "चौबीस", "pañcavīsa": "पच्चीस",
    "chabbīsa": "छब्बीस", "sattavīsa": "सत्ताईस", "aṭṭhavīsa": "अट्ठाईस", "ekūnatiṃsa": "उनतीस", "tiṃsa": "तीस",
    "ekatiṃsa": "इकतीस", "dvattiṃsa": "बत्तीस", "tettiṃsa": "तैंतीस", "catuttiṃsa": "चौंतीस",
    "pañcatiṃsa": "पैंतीस", "chattiṃsa": "छत्तीस", "sattatiṃsa": "सैंतीस",
})

# --- dyad items (pi-1 1-matika / pi-2 labels in the wording of the pi-7 Hindi frames), every case form
ITEMS = {
    "sappaccay": "कारणों पर निर्भर रहने वाला", "appaccay": "कारणों पर निर्भर न रहने वाला",
    "saṅkhat": "निर्मित", "asaṅkhat": "अनिर्मित",
    "sanidassan": "दिखाई देने वाला", "anidassan": "दिखाई न देने वाला",
    "sappaṭigh": "टकराव वाला", "appaṭigh": "टकराव से रहित",
    "sanidassanasappaṭigh": "दिखाई देने वाला और टकराव वाला",
    "lokiy": "लौकिक", "lokuttar": "लोकोत्तर",
    "viññeyy": "जाना जा सकने वाला", "naviññeyy": "न जाना जा सकने वाला",
    "sārammaṇ": "विषय वाला", "anārammaṇ": "विषय से रहित",
    "cetasik": "मन का सहचर", "acetasik": "मन का सहचर न होने वाला",
    "cittasampayutt": "मन से जुड़ा", "cittavippayutt": "मन से अलग",
    "cittasaṃsaṭṭh": "मन से घुला-मिला", "cittavisaṃsaṭṭh": "मन से घुला-मिला न होने वाला",
    "nocittasamuṭṭhān": "मन से उत्पन्न न होने वाला",
    "cittasaṃsaṭṭhasamuṭṭhān": "मन से घुला-मिला और मन से उत्पन्न",
    "ajjhattik": "आंतरिक", "bāhir": "बाह्य",
    "upādinn": "कर्म से उत्पन्न", "anupādinn": "कर्म से उत्पन्न न होने वाला",
    "saṃkiliṭṭh": "क्लेशों से मलिन", "asaṃkiliṭṭh": "क्लेशों से मलिन न होने वाला",
    "savitakk": "आरंभिक विचार वाला", "avitakk": "आरंभिक विचार से रहित",
    "savicār": "सतत विचार वाला", "avicār": "सतत विचार से रहित",
    "sappītik": "उल्लास वाला", "appītik": "उल्लास से रहित",
    "napītisahagat": "उल्लास के साथ न होने वाला", "nasukhasahagat": "सुख के साथ न होने वाला",
    "naupekkhāsahagat": "समभाव के साथ न होने वाला",
    "vicikicchāsahagat": "संशय के साथ होने वाला", "uddhaccasahagat": "बेचैनी के साथ होने वाला",
    "kāmāvacar": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacar": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacar": "अभौतिक लोक से संबंधित",
    "pariyāpann": "अस्तित्व के लोकों में समाया हुआ", "apariyāpann": "अस्तित्व के लोकों में न समाया हुआ",
    "niyyānik": "मुक्ति की ओर ले जाने वाला", "aniyyānik": "मुक्ति की ओर न ले जाने वाला",
    "niyat": "निश्चित",
    "sauttar": "सर्वोच्च न होने वाला", "anuttar": "सर्वोच्च",
    "saraṇ": "संघर्ष वाला", "araṇ": "संघर्ष से रहित",
    "sahetuk": "मूल वाला", "ahetuk": "मूल से रहित",
    "vipākadhammadhamm": "कर्म-फल उत्पन्न करने वाला",
    "nevavipākanavipākadhammadhamm": "न कर्म-फल रूपी न कर्म-फल उत्पन्न करने वाला",
    "uppann": "उत्पन्न हो चुका", "anuppann": "उत्पन्न न हुआ",
}
_ENDS = ("aṃ", "o", "ā", "assa", "ānaṃ", "e", "a")
for _st, _h in ITEMS.items():
    for _e in _ENDS:
        T[_st + _e] = _h
for _st, _h in (("cittasahabh", "मन के साथ-साथ होने वाला"), ("nocittasahabh", "मन के साथ-साथ न होने वाला"),
                ("cittasaṃsaṭṭhasamuṭṭhānasahabh",
                 "मन से घुला-मिला मन से उत्पन्न और मन के साथ-साथ होने वाला")):
    for _e in ("uṃ", "ū", "u", "uno", "ussa"):
        T[_st + _e] = _h
for _st, _h in (("cittānuparivatt", "मन का अनुसरण करने वाला"), ("nocittānuparivatt", "मन का अनुसरण न करने वाला"),
                ("cittasaṃsaṭṭhasamuṭṭhānānuparivatt",
                 "मन से घुला-मिला मन से उत्पन्न और मन का अनुसरण करने वाला"),
                ("rūp", "भौतिक"), ("arūp", "अभौतिक"), ("uppād", "उत्पन्न होने वाला")):
    for _e in ("iṃ", "ī", "i", "ino", "issa"):
        T[_st + _e] = _h
T.update({
    "upādā": "व्युत्पन्न", "noupādā": "व्युत्पन्न न होने वाला",
    "cittaṃ": "मन", "nocittaṃ": "मन रूपी न होने वाला",
    "mohaṃ": "मोह", "kenaci": "किसी एक प्रकार की चेतना",
    "nasukhāya": "सुखद … न होने वाला", "nadukkhāya": "दुःखद … न होने वाला",
    # dassanena / bhāvanāya pahātabba(hetuka): the triad «न सत्य-दर्शन से, न मानसिक अभ्यास से …» or the
    # dyad «सत्य-दर्शन से न छोड़ी जाने वाली» (negation on the verb; «से» kept so the «न» stays readable)
    # In «nadassanena pahātabbahetuka» the Hindi is «सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित»: the
    # negation is «से रहित», so nadassanena = «सत्य-दर्शन … से रहित» and the positive fragment
    # pahātabbahetukaṃ = «छोड़े जाने वाले मूल» (its «वाला» is replaced by «से रहित»).
    "nevadassanena": "न सत्य-दर्शन",
    "nabhāvanāya": ("न मानसिक अभ्यास", "मानसिक अभ्यास से न", "मानसिक अभ्यास … से रहित"),
    "nadassanena": ("सत्य-दर्शन से न", "न सत्य-दर्शन", "सत्य-दर्शन … से रहित"),
    "pahātabbahetukaṃ": ("छोड़े जाने वाले मूलों वाला", "छोड़े जाने वाले मूल"),
    "pahātabbahetuko": ("छोड़े जाने वाले मूलों वाला", "छोड़े जाने वाले मूल"),
    "nanevadassanena": "न सत्य-दर्शन … न होने वाला",
    # headings, cross-references, instructions
    "hetudukaṃ": ("मूल वाला दो का वर्गीकरण", "मूल-कारण के साथ दो कारणों का मेल"),
    "hetuduka": ("मूल वाला दो का वर्गीकरण", "मूल-कारण के साथ दो कारणों का मेल"),
    "saññojanādiduka": "बंधन वाला दो का वर्गीकरण आदि", "saññojanādidukāni": "बंधन वाला दो का वर्गीकरण आदि",
    "sappaccayadukasadisaṃ": "कारणों पर निर्भर रहने वाली परिघटनाओं वाले दो के वर्गीकरण के समान",
    "kusalattikasanidassanattikaṃ": "हितकर वाला तीन का वर्गीकरण और दिखाई देने वाला और टकराव वाला तीन का वर्गीकरण",
    "vitthāro": "विस्तार", "āmasanaṃ": "उल्लेख", "pañhā": "प्रश्न", "pañhāni": "प्रश्न",
    "nīvaraṇagocchake": "बाधाओं का वर्ग", "saññojanagocchake": "बंधनों का वर्ग",
    "āsavagocchake": "मन के मैलों का वर्ग",
    "paccanīyadukamattāni": "केवल नकारात्मक क्रम के दो-दो के वर्गीकरण", "vattabbaṃ": "कहने योग्य",
    "sahetukā": "मूल वाला", "cittasampayuttakā": "मन से जुड़ा हुआ",
})

FT = {f: {} for f in FILES}
OVR = {f: {} for f in FILES}
OVR["5-03-paccaniya-tika"]["7-57-34"] = {"gaṇitaṃ": "गणना की गई"}          # text «… की गणना की गई है»
OVR["5-04-paccaniya-duka"]["7-58-64"] = {
    "kaṭattārūpaṃ": "किए गए कर्म से उत्पन्न … भौतिक रूप"}                   # «… उत्पन्न आंतरिक भौतिक रूप»
ALLOWED = {f: {} for f in FILES}
SAMAYA = "the checker does not model समाया ~ समाई (text «समाई हुई»; pi-2 precedent, masc. dictionary form)"


def allowed_for(f):
    """ALLOWED[f] plus the समाया ~ समाई cases (pariyāpanna), computed from the mapped file."""
    al = dict(ALLOWED[f])
    hi = read_hindi(f)
    mf = pathlib.Path(__file__).resolve().parent / f"{f}.mapped.md"
    for line in mf.read_text(encoding="utf-8").splitlines():
        bid, _, rest = line.partition("] ")
        bid = bid[1:]
        text = hi.get(bid)
        for pair in rest.split(", ") if rest else []:
            kw, v = pair.split("=", 1)
            if "समाया" in v and text and not present(v, text) and present(v.replace("समाया", "समाई"), text):
                al[(bid, kw)] = SAMAYA
    return al


# ---------------------------------------------------------------------------- resolver
def _table_value(k, table, text, closing, depth=0):
    """Table (with particle stripping), then the paccanīya rule naX / noX = «<X> न होने वाला»."""
    for cand in [k] + _strip_particles(k):
        if closing and cand in CLOSING:
            return CLOSING[cand]
        if cand in table:
            return _pick(table[cand], text)
    if depth < 3 and k[:2] in ("na", "no") and len(k) > 5:
        v = _table_value(k[2:], table, text, closing, depth + 1)
        if v is not None and v != NDE:
            return f"{v} न होने वाला"
    return None


def resolver_for(f, table, ovr, log=None):
    hi, pa = read_hindi(f), read_pali(f)

    def res(bid, kw, kws):
        o = ovr.get(bid, {})
        text = hi.get(bid)
        if kw in o:
            v, src = o[kw], "override"
        else:
            v = heading_value(kw, pa.get(bid), text)
            src = "heading"
            if v is None:
                closing = _is_closing(kws, text)
                v = _table_value(lc(kw), table, text, closing)
                src = "table"
                if v is None:
                    v, src = lookup(kw, kws, table, text, closing)
        if log is not None:
            log.setdefault((kw, v), collections.Counter())[src] += 1
        return v
    return res


def audit_mine(f, table, ovr):
    log = {}
    res = resolver_for(f, table, ovr, log)
    for bid, kws in read_keywords(f):
        for kw in kws:
            try:
                res(bid, kw, kws)
            except KeyError:
                print("   UNMAPPED", bid, kw)
    by = collections.defaultdict(list)
    for (kw, v), c in log.items():
        by[kw].append((v, dict(c)))
    for kw in sorted(by, key=lc):
        if all(set(c) <= {"table", "heading", "override"} for _, c in by[kw]):
            continue
        print("  ", kw, "->", "; ".join(f"{v} {c}" for v, c in by[kw]))


def table_for(f):
    return {**PI7, **T, **FT[f]}


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    todo = args or FILES
    for f in todo:
        build_part(f, resolver_for(f, table_for(f), OVR[f]))
        verify(f, allowed=allowed_for(f))
        if "--audit" in sys.argv:
            audit_mine(f, table_for(f), OVR[f])
