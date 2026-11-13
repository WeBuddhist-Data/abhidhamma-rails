"""pi-7 (Paṭṭhāna) Pāli->Hindi keyword maps: shared tooling + the sample
(preamble, 1-00-paccaya, 2-13-atitattika, 4-07-dukatika-ganthaduka).

Importing this module writes nothing and prints nothing. Later chapter scripts:

    import sys, pathlib; sys.dont_write_bytecode = True   # no __pycache__ in the shared folder
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_sample_hi import *          # PI7, pi7_value, make_resolver, build_part, verify, audit, present, prior

    T = {...}                             # your chapter table (lower-case first letter keys)
    OVR = {"7-x-y": {"kw": "हिंदी"}}        # per-segment overrides (exact keyword spelling)
    build_part("<file>", make_resolver("<file>", {**PI7, **T}, OVR))
    verify("<file>", allowed={("7-x-y", "kw"): "reason"})
    audit("<file>", {**PI7, **T}, OVR)     # optional: each keyword, its values, where the value came from

Lookup order in pi7_value (see hi-map-conventions-pi7.md):
  1. heading rule: in a heading segment, a keyword that is the whole Pāli heading (numbering, asterisks,
     trailing «.» ignored) = the whole Hindi heading (numbering stripped, ", " -> " ", a final « में» dropped);
  2. the table (PI7 + your T); a value may be a tuple: the first alternative present in the segment's Hindi wins;
  3. after dropping the quotative -ti and the enclitics -ñca / -ñceva / -pi / -mpi;
  4. HEADNAMES: book-wide single-word heading -> Hindi heading (only where the Hindi is unique), also for
     the members of compound headings («Ganthaduka» -> «Ganthadukaṃ»);
  5. pi-2 PI2, pi-1 CH2, pi-1 matrix names (last resort; audit() flags these so you can check them).
usage (sample): python -I -B -X utf8 map_sample_hi.py
"""
import collections
import importlib.util
import pathlib
import re
import sys

sys.dont_write_bytecode = True                      # importing must not write anything, not even caches
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
_PI1 = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-1-hi" / "mapper-hi"
_PI2 = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-2-hi" / "mapper-hi"
if str(_PI1) not in sys.path:
    sys.path.append(str(_PI1))
from map_common_hi import CH2, lc, NDE, GAP  # noqa: E402  (read-only import)
from map_common_hi import present as _present_pi1  # noqa: E402
from map_common_hi import matrix_names as _matrix_names  # noqa: E402

_spec = importlib.util.spec_from_file_location("map_sample_hi_pi2", _PI2 / "map_sample_hi.py")
_pi2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_pi2)                     # read-only: pi-2's PI2 table (its __main__ does not run)
PI2 = _pi2.PI2

HI_DIR = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-7_split_chapters"
PRIOR_BOOKS = (1, 2, 3, 4, 5, 6)
PRIOR_MAPS = {n: ROOT / "AI_translation" / "hindi" / f"pi-{n}-keywords-by-reference-pali-hindi-plain.md"
              for n in PRIOR_BOOKS}
DEV = "ऀ-ॿ"


# ---------------------------------------------------------------------------- reading
def read_keywords(f):
    out = []
    for line in (HERE / f"{f}.keywords.md").read_text(encoding="utf-8").splitlines():
        if line.strip():
            bid, _, rest = line.partition("] ")
            out.append((bid[1:], [k.strip() for k in rest.split(", ")] if rest else []))
    return out


def _segments(path):
    segs = {}
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
        block = block.strip()
        m = re.search(r"\^([0-9A-Za-z-]+)\s*$", block)
        if m:
            segs[m.group(1)] = block[: m.start()].strip()
    return segs


def read_hindi(f):
    return _segments(HI_DIR / f"{f}.md")


def read_pali(f):
    return _segments(PI_DIR / f"{f}.md")


_PRIOR = None


def prior(kw):
    """{book: Counter(values)} for this keyword in the finished pi-1..6 Hindi maps."""
    global _PRIOR
    if _PRIOR is None:
        _PRIOR = collections.defaultdict(collections.Counter)
        for n, p in PRIOR_MAPS.items():
            if not p.exists():
                continue
            for line in p.read_text(encoding="utf-8").splitlines():
                if "] " in line:
                    for pair in line.split("] ", 1)[1].split(", "):
                        if "=" in pair:
                            k, v = pair.split("=", 1)
                            _PRIOR[(n, lc(k.strip()))][v] += 1
    return {n: _PRIOR[(n, lc(kw))] for n in PRIOR_BOOKS if (n, lc(kw)) in _PRIOR}


# ---------------------------------------------------------------------------- presence check
# pi-1 present() + regular inflections the pi-1 checker does not model: the oblique of the pronouns
# (यह ~ इस/इन, वह ~ उस/उन, कोई ~ किसी) and the perfective participle in -ाया (दबाया ~ दबाए/दबाई).
_TOK_ALT = {"यह": ("इस", "इन", "ये"), "वह": ("उस", "उन", "वे"), "कोई": ("किसी",)}


def present(value, text):
    if value == NDE:
        return True
    if text is None:
        return False
    cands = [value]
    toks = value.split(" ")
    for i, t in enumerate(toks):
        for alt in _TOK_ALT.get(t, ()):
            cands.append(" ".join(toks[:i] + [alt] + toks[i + 1:]))
    cands += [re.sub(r"ाया(?![" + DEV + "])", "ाए", c) for c in list(cands) if "ाया" in c]
    return any(_present_pi1(c, text) for c in cands)


# ============================================================================ PI7 default table
# Values: dictionary form (nouns direct sg, adjectives/participles masc. sg, verbs infinitive or the -कर /
# -करके form the text uses for an absolutive), the pi-1/2/6 wording where the Pāli is the same.
# A tuple = alternatives, the first one present in the segment's Hindi wins (else the first).
PI7 = {}

# --- book frame (pi-1/pi-2/pi-6 preamble; hi-zeroshot-terms.md §1)
PI7.update({
    "abhidhammapiṭake": "अभिधम्म पिटक", "abhidhamma": "अभिधम्म",
    "namo": "नमन", "bhagavato": "भगवान", "arahato": "अर्हत्", "sammā": "पूर्ण रूप से",
    "sambuddhassa": "जागृत बुद्ध", "sammāsambuddhassa": "पूर्ण रूप से जागृत बुद्ध",
    "paṭṭhānapāḷi": "कारण-संबंध", "paṭṭhāna": "कारण-संबंध", "paṭṭhānaṃ": "कारण-संबंध", "pāḷi": NDE,
    "paṭṭhānavaraṃ": "श्रेष्ठ कारण-संबंध",
    "bhāgo": "भाग",
})

# --- the 24 conditions in every case form (hi-zeroshot-terms.md §4).
# Brief: hetupaccayo / hetupaccayā / hetupaccayena / hetuyā = the NAME (मूल-कारण);
# negative ablative nahetupaccayā = «<name> के बिना»; negative noun (nahetupaccayo, heading) and negative
# count locative (nahetuyā «<name> के अभाव में») = «<name> का अभाव».
# (stem, Hindi name, count-locative ending form, negative prefix, plain term for a count form used outside counts)
CONDITIONS = [
    ("hetu", "मूल-कारण", "hetuyā", "na", "मूल"),
    ("ārammaṇa", "विषय-कारण", "ārammaṇe", "na", "विषय"),
    ("adhipati", "प्रधानता-कारण", "adhipatiyā", "na", "प्रधानता"),
    ("anantara", "निकटता-कारण", "anantare", "na", None),
    ("samanantara", "पूर्ण निकटता-कारण", "samanantare", "na", None),
    ("sahajāta", "सह-उत्पत्ति-कारण", "sahajāte", "na", None),
    ("aññamañña", "परस्पर-कारण", "aññamaññe", "na", None),
    ("nissaya", "आश्रय-कारण", "nissaye", "na", None),
    ("upanissaya", "प्रबल आश्रय-कारण", "upanissaye", "na", None),
    ("purejāta", "पूर्व-उत्पत्ति-कारण", "purejāte", "na", None),
    ("pacchājāta", "पश्चात्-उत्पत्ति-कारण", "pacchājāte", "na", None),
    ("āsevana", "पुनरावृत्ति-कारण", "āsevane", "na", None),
    ("kamma", "कर्म-कारण", "kamme", "na", "कर्म"),
    ("vipāka", "कर्म-फल-कारण", "vipāke", "na", "कर्म-फल"),
    ("āhāra", "आहार-कारण", "āhāre", "na", "आहार"),
    ("indriya", "क्षमता-कारण", "indriye", "na", "क्षमता"),
    ("jhāna", "ध्यान-कारण", "jhāne", "na", "ध्यान"),
    ("magga", "मार्ग-कारण", "magge", "na", "मार्ग"),
    ("sampayutta", "जुड़ाव-कारण", "sampayutte", "na", None),
    ("vippayutta", "अलगाव-कारण", "vippayutte", "na", None),
    ("atthi", "उपस्थिति-कारण", "atthiyā", "no", None),
    ("natthi", "अनुपस्थिति-कारण", "natthiyā", "no", None),
    ("vigata", "विलीनता-कारण", "vigate", "no", None),
    ("avigata", "अविलीनता-कारण", "avigate", "no", None),
]
COND_NAME = {c[0]: c[1] for c in CONDITIONS}
for _st, _name, _loc, _neg, _plain in CONDITIONS:
    for _e in ("paccayo", "paccayā", "paccayena", "paccayassa", "paccayaṃ", "paccaya", "paccayoti"):
        PI7[_st + _e] = _name
    # count locative: the name; where the same word is not a count (jhāne parihīne …), the plain term
    PI7[_loc] = (_name, _plain) if _plain else _name
    PI7[_neg + _st + "paccayā"] = f"{_name} के बिना"
    for _e in ("paccayo", "paccayena", "paccayaṃ", "paccaya", "paccayoti"):
        PI7[_neg + _st + _e] = f"{_name} का अभाव"
    PI7[_neg + _loc] = f"{_name} का अभाव"
    PI7[_st + "paccayasadisaṃ"] = f"{_name} के समान"
    PI7[_neg + _st + "paccayasadisaṃ"] = f"{_name} के अभाव के समान"
    PI7[_st + "sadisaṃ"] = f"{_name} के समान"                     # (anantarasadisaṃ), (atthisadisaṃ)
    PI7[_st + "paccayādi"] = f"{_name} आदि"
# the subtypes named in the Pañhāvāra («विषय रूपी प्रधानता» …)
PI7.update({
    "ārammaṇādhipati": "विषय रूपी प्रधानता", "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
    "ārammaṇūpanissayo": "विषय रूपी प्रबल आश्रय", "anantarūpanissayo": "निकटता रूपी प्रबल आश्रय",
    "pakatūpanissayo": "स्वाभाविक प्रबल आश्रय",
    "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति", "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति",
    "sahajātaṃ": ("साथ जन्म लेकर", "सह-उत्पत्ति"), "sahajātā": ("साथ जन्म लेकर", "सह-उत्पत्ति"),
    "sahajāto": ("साथ जन्म लेकर", "सह-उत्पत्ति"),
    "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति",
    "nānākkhaṇikā": "भिन्न क्षण", "paccuppannādhipati": "वर्तमान की प्रधानता",
    "chandādhipati": "प्रधान बनी हुई चाह", "vīriyādhipati": "प्रधान बना हुआ उत्साह",
    "cittādhipati": "प्रधान बना हुआ मन", "vīmaṃsādhipati": "प्रधान बनी हुई जाँच-परख",
    "paccayo": "कारण होना",                                        # bare predicate «… कारण होता है»
    "paccaya": "कारण", "paccayā": "के कारण",                        # Paccayavāra frame «X के कारण» (pi-2)
})

# --- methods, sections, series (hi-zeroshot-terms.md §2-3)
METHODS = {"anuloma": "सकारात्मक क्रम", "paccanīya": "नकारात्मक क्रम",
           "anulomapaccanīya": "सकारात्मक-नकारात्मक क्रम", "paccanīyānuloma": "नकारात्मक-सकारात्मक क्रम"}
_METHOD_ENDINGS = ("aṃ", "a", "e", "amhi", "ampi", "assa")
for _p, _h in METHODS.items():
    _s = _p[:-1]
    for _e in _METHOD_ENDINGS:
        PI7[_s + _e] = _h
        # Paccaya- / Dhamma- prefixed headings; a + a -> ā (Paccayānulomaṃ, Dhammānulome)
        _pp = "paccay" + ("ā" + _s[1:] if _s.startswith("a") else "a" + _s)
        _dp = "dhamm" + ("ā" + _s[1:] if _s.startswith("a") else "a" + _s)
        PI7[_pp + _e] = f"कारणों का {_h}"
        PI7[_dp + _e] = f"परिघटनाओं का {_h}"
VARAS = {"paṭicca": "निर्भरता", "sahajāta": "सह-उत्पत्ति", "paccaya": "कारण", "nissaya": "आश्रय",
         "saṃsaṭṭha": "घुले-मिले होने", "sampayutta": "जुड़ाव", "pañhā": "प्रश्नों", "vibhaṅga": "विश्लेषण",
         "saṅkhyā": "गणना", "pucchā": "पूछताछ", "niddesa": "व्याख्या", "hetupaccaya": "मूल-कारण"}
for _p, _h in VARAS.items():
    for _e in ("vāro", "vāre", "vārepi", "vāropi", "vārampi", "vāraṃ", "vārassa", "vāra"):
        PI7[_p + _e] = f"{_h} का खंड"
    PI7[_p + "vārādi"] = f"{_h} का खंड आदि"
    for _e in ("vārasadisā", "vārasadisaṃ", "vārasadiso"):
        PI7[_p + _e] = f"{_h} के खंड के समान"
PI7.update({
    "vāro": "खंड", "vāra": "खंड",
    "paccayuddeso": "कारणों की सूची", "paccayaniddeso": "कारणों की व्याख्या", "niddesavāre": "व्याख्या का खंड",
    "paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "paccayacatukkaṃ": "कारणों के चार क्रम",
    "tikapaṭṭhānaṃ": "तीन-तीन के वर्गीकरणों के कारण-संबंध", "dukapaṭṭhānaṃ": "दो-दो के वर्गीकरणों के कारण-संबंध",
    "dukatikapaṭṭhānaṃ": "दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "tikadukapaṭṭhānaṃ": "तीन-तीन और दो-दो के वर्गीकरणों के कारण-संबंध",
    "tikatikapaṭṭhānaṃ": "तीन-तीन और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "dukadukapaṭṭhānaṃ": "दो-दो और दो-दो के वर्गीकरणों के कारण-संबंध",
    # the stanza (tika/duka = the classifications, pi-2 «तीन-तीन / दो-दो के वर्गीकरण»)
    "tikañca": "तीन-तीन के वर्गीकरण", "tikañceva": "तीन-तीन", "dukañca": "दो-दो", "dukaṃ": "दो-दो",
    "tikaṃ": "तीन-तीन", "dukuttamaṃ": "दो-दो के वर्गीकरणों के उत्तम कारण-संबंध",
    "nayā": "विधि", "sugambhīrā": "अत्यंत गहन", "sugambhīrāti": "अत्यंत गहन",
    # series of conditions
    "ekamūlakaṃ": "एक कारण वाली शृंखला", "dumūlakaṃ": "दो कारणों वाली शृंखला",
    "timūlakaṃ": "तीन कारणों वाली शृंखला", "catumūlakaṃ": "चार कारणों वाली शृंखला",
    "pañcamūlakaṃ": "पाँच कारणों वाली शृंखला", "sabbamūlakaṃ": "सभी कारणों वाली शृंखला",
    "tevīsatimūlakaṃ": "तेईस कारणों वाली शृंखला", "dumūlakādi": "दो कारणों वाली शृंखला आदि",
    "pañcamūlakādikā": "पाँच कारणों वाली शृंखला आदि",
    "hetumūlakaṃ": "मूल-कारण से शुरू होने वाली शृंखला",
    "ārammaṇamūlakādi": "विषय-कारण से शुरू होने वाली शृंखला आदि",
    "nahetumūlakaṃ": "मूल-कारण के अभाव से शुरू होने वाली शृंखला",
    "padaṃ": "पद", "padassa": "पद", "pada": "पद",
    # instructions and abbreviations
    "vitthārito": "विस्तार किया गया", "vitthāretabbo": "विस्तार करना चाहिए",
    "vitthāretabbaṃ": "विस्तार करना चाहिए", "vitthāretabbā": "विस्तार करना चाहिए",
    "vācanāmaggena": "पाठ का क्रम", "asammuyhantena": "बिना भ्रमित हुए",
    "gaṇetabbaṃ": "गिनना चाहिए", "gaṇetabbā": "गिनना चाहिए", "gaṇitaṃ": "गिना गया",
    "saṃkhittaṃ": "संक्षिप्त", "saṃkhittā": "संक्षिप्त", "saṅkhittaṃ": "संक्षिप्त", "saṅkhitaṃ": "संक्षिप्त",
    "sabbattha": "हर जगह", "niṭṭhitaṃ": "समाप्त", "niṭṭhito": "समाप्त", "niṭṭhitā": "समाप्त",
    "lokiyalokuttaragamanasadisaṃ": "लौकिक और लोकोत्तर के प्रसंग के समान",
})

# --- frame words (hi-zeroshot-terms.md §5). The governing case marker of the noun is stripped
# («पर», «के», «से»), except «के कारण» (pi-2 paccayā).
PI7.update({
    "paṭicca": "निर्भर होकर", "nissāya": "आश्रय से", "upanissāya": "प्रबल आश्रय से",
    "saṃsaṭṭho": "घुल-मिलकर", "saṃsaṭṭhā": "घुल-मिलकर", "saṃsaṭṭhaṃ": "घुल-मिलकर",   # pi-2
    "uppajjati": "उत्पन्न होना", "uppajjanti": "उत्पन्न होना",
    "uppajjeyya": "उत्पन्न हो सकना", "uppajjeyyuṃ": "उत्पन्न हो सकना",
    "siyā": "क्या",
    "ārabbha": "विषय बनाना",                                         # pi-1 binding
    "garuṃ": "महत्व", "katvā": "देकर",                              # «को महत्व देकर»
    "anantarā": "ठीक बाद", "samanantarā": "बिलकुल ठीक बाद",
    "samanantaraniruddhā": "बिलकुल ठीक पहले समाप्त हो चुका", "samanantaravigatā": "बिलकुल ठीक पहले विलीन हो चुका",
    "purimā": "पहले-पहले का", "pacchimānaṃ": "बाद-बाद का", "kesañci": "कुछ",
    "kiñci": "कोई", "kāle": "समय", "aññamaññaṃ": "एक-दूसरा",
    "vattanti": "क्रियाशील होना", "taṃ": "वह", "yaṃ": "जो",
    "imassa": "यह", "kāyassa": "शरीर",
    "pacchājātā": "बाद में उत्पन्न", "purejātassa": "पहले उत्पन्न",
    "paṭuppannānaṃ": "वर्तमान", "paccuppannānaṃ": "वर्तमान का",
    "kaṭattā": "किए गए कर्म से उत्पन्न",
    "sampayuttakānaṃ": "जुड़ा हुआ", "sampayuttakā": "जुड़ा हुआ",
    "taṃsampayuttakānañca": "उससे जुड़ा", "taṃsampayuttakā": "उससे जुड़ा", "taṃsampayuttakānaṃ": "उससे जुड़ा",
    "taṃsamuṭṭhānānañca": "उनसे उत्पन्न", "taṃsamuṭṭhānānaṃ": "उनसे उत्पन्न",
    "hetusampayuttakānaṃ": "मूलों से जुड़ा",
    "cittasamuṭṭhānānaṃ": "मन से उत्पन्न", "cittasamuṭṭhānānañca": "मन से उत्पन्न",
    "cittasamuṭṭhānaṃ": "मन से उत्पन्न", "cittasamuṭṭhāna": "मन से उत्पन्न",
})

# --- khandha / matter / bases / elements (hi-zeroshot-terms.md §5-6; pi-1/2/6 values)
PI7.update({
    "dhamma": "परिघटना", "dhammaṃ": "परिघटना", "dhammo": "परिघटना", "dhammā": "परिघटना",
    "dhammānaṃ": "परिघटना", "dhammassa": "परिघटना", "dhamme": "परिघटना", "dhammesu": "परिघटना",
    "khandha": "समूह", "khandho": "समूह", "khandhā": "समूह", "khandhe": "समूह", "khandhaṃ": "समूह",
    "khandhānaṃ": "समूह", "khandhassa": "समूह",
    "rūpaṃ": "भौतिक रूप", "rūpānaṃ": "भौतिक रूप", "rūpassa": "भौतिक रूप", "rūpa": "भौतिक रूप",
    "rūpino": "भौतिक", "arūpino": "अभौतिक", "arūpīnaṃ": "अभौतिक", "rūpīnaṃ": "भौतिक",
    "mahābhūtā": "महाभूत", "mahābhūte": "महाभूत", "mahābhūtaṃ": "महाभूत", "mahābhūtānaṃ": "महाभूत",
    "upādārūpānaṃ": "व्युत्पन्न भौतिक रूप", "upādārūpaṃ": "व्युत्पन्न भौतिक रूप",
    "kaṭattārūpānaṃ": "किए गए कर्म से उत्पन्न भौतिक रूप", "kaṭattārūpaṃ": "किए गए कर्म से उत्पन्न भौतिक रूप",
    "vatthu": "आधार", "vatthuṃ": "आधार", "vatthussa": "आधार",
    "nāmarūpaṃ": "मानसिक पक्ष और भौतिक रूप",
    "paṭisandhikkhaṇe": "पुनर्जन्म का क्षण", "ahetukapaṭisandhikkhaṇe": "मूल से रहित पुनर्जन्म का क्षण",
    "okkantikkhaṇe": "गर्भ में उतरने का क्षण",
    "arūpe": "अभौतिक लोक", "asaññasattānaṃ": "पहचान-रहित प्राणी", "bāhiraṃ": "बाह्य", "bāhire": "बाह्य",
    "āhārasamuṭṭhānaṃ": "आहार से उत्पन्न", "āhārasamuṭṭhāne": "आहार से उत्पन्न",
    "utusamuṭṭhānaṃ": "तापमान से उत्पन्न", "utusamuṭṭhāne": "तापमान से उत्पन्न",
    "cittacetasikā": "मन और मन का सहचर", "cittacetasikānaṃ": "मन और मन का सहचर",     # pi-1
    "cetanā": "इरादा", "kammaṃ": "कर्म", "kusalākusalaṃ": "हितकर और हानिकर",
    "vipāko": ("कर्म-फल रूपी", "कर्म के फल रूपी"), "vipākā": ("कर्म-फल रूपी", "कर्म के फल रूपी"),
    "vipākānaṃ": ("कर्म-फल रूपी", "कर्म के फल रूपी"), "vipākaṃ": ("कर्म-फल रूपी", "कर्म के फल रूपी"),
    "kiriyābyākatā": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित",
    "kiriyābyākatānaṃ": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित",
    "vipākābyākataṃ": "कर्म के फल रूपी नैतिक रूप से अनिर्धारित",
    "kiriyābyākataṃ": "केवल क्रिया रूपी नैतिक रूप से अनिर्धारित",
    "kabaḷīkāro": "कौर-कौर खाया जाने वाला", "āhāro": "भोजन", "āhārā": "आहार",            # pi-1
    "indriyā": "क्षमता", "jhānaṅgāni": "ध्यान का अंग", "maggaṅgāni": "मार्ग का अंग",
    "rūpajīvitindriyaṃ": "भौतिक जीवन-क्षमता",
    "cakkhundriyaṃ": "आँख की क्षमता", "sotindriyaṃ": "कान की क्षमता", "ghānindriyaṃ": "नाक की क्षमता",
    "jivhindriyaṃ": "जीभ की क्षमता", "kāyindriyaṃ": "शरीर की क्षमता",
    "rūpāyatanaṃ": "दृश्य रूप का इंद्रिय-क्षेत्र", "saddāyatanaṃ": "ध्वनि का इंद्रिय-क्षेत्र",
    "gandhāyatanaṃ": "गंध का इंद्रिय-क्षेत्र", "rasāyatanaṃ": "स्वाद का इंद्रिय-क्षेत्र",
    "phoṭṭhabbāyatanaṃ": "स्पर्श का इंद्रिय-क्षेत्र",
    "cakkhāyatanaṃ": "आँख का इंद्रिय-क्षेत्र", "sotāyatanaṃ": "कान का इंद्रिय-क्षेत्र",
    "ghānāyatanaṃ": "नाक का इंद्रिय-क्षेत्र", "jivhāyatanaṃ": "जीभ का इंद्रिय-क्षेत्र",
    "kāyāyatanaṃ": "शरीर का इंद्रिय-क्षेत्र",
    "manodhātu": "मन का तत्व", "manodhātuyā": "मन का तत्व",
    "manoviññāṇadhātu": "मन की चेतना का तत्व", "manoviññāṇadhātuyā": "मन की चेतना का तत्व",
})
for _p, _h in (("cakkhu", "आँख"), ("sota", "कान"), ("ghāna", "नाक"), ("jivhā", "जीभ"), ("kāya", "शरीर")):
    PI7[_p + "viññāṇadhātu"] = f"{_h} की चेतना का तत्व"
    PI7[_p + "viññāṇadhātuyā"] = f"{_h} की चेतना का तत्व"
    PI7[_p + "viññāṇaṃ"] = f"{_h} की चेतना"
    PI7[_p + "viññāṇassa"] = f"{_h} की चेतना"
    PI7[_p + "sampadaṃ"] = f"{_h} की संपन्नता"
    PI7[_p + "sampadā"] = f"{_h} की संपन्नता"
PI7["ghāṇaviññāṇadhātu"] = "नाक की चेतना का तत्व"                # Pāli spelling variant (7-1-5)
for _p, _h in (("vaṇṇa", "रंग-रूप"), ("sadda", "ध्वनि"), ("gandha", "गंध"), ("rasa", "स्वाद"),
               ("phoṭṭhabba", "स्पर्श")):
    PI7[_p + "sampadaṃ"] = f"{_h} की संपन्नता"
    PI7[_p + "sampadā"] = f"{_h} की संपन्नता"

# --- Pañhāvāra vocabulary (hi-zeroshot-terms.md §6)
PI7.update({
    "dānaṃ": "दान", "datvā": "देकर", "deti": "देना", "sīlaṃ": "सदाचार", "samādiyitvā": "ग्रहण करके",
    "samādiyati": "ग्रहण करना", "uposathakammaṃ": "उपवास-व्रत", "karoti": "पालन करना",
    "paccavekkhati": "पुनः विचार करना", "paccavekkhanti": "पुनः विचार करना",
    "pubbe": "पहले", "suciṇṇāni": "भली-भाँति किए गए कार्य",
    "jhānā": "ध्यान", "maggā": "मार्ग", "vuṭṭhahitvā": "उठकर", "ariyā": "आर्य",
    "jhānaṃ": "ध्यान", "maggaṃ": "मार्ग", "phalaṃ": "फल", "maggassa": "मार्ग", "phalassa": "फल", "maggo": "मार्ग",
    "pahīne": "छोड़ा जा चुका", "vikkhambhite": "दबाया जा चुका", "samudāciṇṇe": "बार-बार उठा",
    "kilese": "मन के क्लेश", "jānanti": "जानना", "jānāti": "जानना",
    "aniccato": "अनित्य", "dukkhato": "दुःख", "anattato": "आत्मा से रहित", "vipassati": "अंतर्दृष्टि से देखना",
    "assādeti": "रस लेना", "abhinandati": "आनंद लेना",
    "rāgo": "राग", "rāgaṃ": "राग", "diṭṭhi": "दृष्टि", "diṭṭhiṃ": "दृष्टि", "vicikicchā": "संशय",
    "uddhaccaṃ": "बेचैनी", "domanassaṃ": "उदासी",
    "cakkhuṃ": "आँख", "sotaṃ": "कान", "ghānaṃ": "नाक", "jivhaṃ": "जीभ", "kāyaṃ": "शरीर",
    "rūpe": "दृश्य रूप", "sadde": "ध्वनि", "gandhe": "गंध", "rase": "स्वाद", "phoṭṭhabbe": "स्पर्श",
    "saddaṃ": "ध्वनि",
    "ākāsānañcāyatanaṃ": "अनंत आकाश का क्षेत्र", "viññāṇañcāyatanaṃ": "अनंत चेतना का क्षेत्र",
    "viññāṇañcāyatanassa": "अनंत चेतना का क्षेत्र", "ākiñcaññāyatanaṃ": "कुछ भी न होने का क्षेत्र",
    "nevasaññānāsaññāyatanaṃ": "न पहचान न अ-पहचान का क्षेत्र",
    "nevasaññānāsaññāyatanassa": "न पहचान न अ-पहचान का क्षेत्र",
    "iddhividhañāṇassa": "अलौकिक शक्तियों का ज्ञान", "cetopariyañāṇassa": "दूसरों के मन को जानने का ज्ञान",
    "pubbenivāsānussatiñāṇassa": "पूर्व जन्मों के अनुस्मरण का ज्ञान",
    "yathākammūpagañāṇassa": "प्राणियों के अपने कर्मों के अनुसार जाने का ज्ञान",
    "anāgataṃsañāṇassa": "भविष्य को जानने का ज्ञान", "āvajjanāya": "मन को विषय की ओर मोड़ना",
    "dibbena": "दिव्य", "dibbāya": "दिव्य", "cakkhunā": "आँख", "passati": "देखना",
    "sotadhātuyā": "कान का तत्व", "suṇāti": "सुनना",
    "gotrabhu": "गोत्र-परिवर्तन", "gotrabhussa": "गोत्र-परिवर्तन", "vodānaṃ": "शुद्धि", "vodānassa": "शुद्धि",
    "phalasamāpattiyā": "फल की ध्यान-अवस्था", "nirodhā": "समाप्ति की ध्यान-अवस्था",
    "vuṭṭhahantassa": "बाहर आने वाला व्यक्ति",
    "saddhaṃ": "श्रद्धा", "saddhā": "श्रद्धा", "saddhāya": "श्रद्धा", "paññaṃ": "प्रज्ञा", "paññā": "प्रज्ञा",
    "paññāya": "प्रज्ञा", "uppādeti": "उत्पन्न करना", "vipassanaṃ": "अंतर्दृष्टि", "abhiññaṃ": "उच्च ज्ञान",
    "samāpattiṃ": "ध्यान-अवस्था", "mānaṃ": "अहंकार", "jappeti": "पालना", "gaṇhāti": "ग्रहण करना",
    "patthanaṃ": "कामना", "patthanā": "कामना", "patthanāya": "कामना", "patthayamāno": "कामना करते हुए",
    "kāyikaṃ": "शारीरिक", "kāyikassa": "शारीरिक", "sukhaṃ": "सुख", "dukkhaṃ": "दुःख",
    "pāṇaṃ": "जीव", "hanati": "हत्या करना", "saṅghaṃ": "संघ", "bhindati": "फूट डालना",
    "utuṃ": "तापमान", "utu": "तापमान", "bhojanaṃ": "भोजन", "senāsanaṃ": "निवास-स्थान",
    "utubhojanampi": "तापमान और भोजन", "puggalopi": "व्यक्ति", "senāsanampi": "निवास-स्थान",
})

# --- time triad (pi-2 atīta/anāgata/paccuppanna = «… का»)
for _p, _h in (("atīt", "अतीत का"), ("anāgat", "भविष्य का"), ("paccuppann", "वर्तमान का")):
    for _e in ("o", "ā", "aṃ", "assa", "ānaṃ", "e", "āya", "a"):
        PI7[_p + _e] = _h
PI7["paccuppano"] = "वर्तमान का"                                    # Pāli misprint (7-19-13)
PI7.update({"uppannattike": "उत्पन्न वाला तीन का वर्गीकरण", "atītattikaṃ": "अतीत वाला तीन का वर्गीकरण"})

# --- triad items (kusalattika etc.): masc. sg. of the frame wording «X परिघटना»; harvested with
# items_sample_hi.py from the pi-7 Hindi. All case forms of the item get the same value.
TRIAD_ITEMS = {
    "kusal": "हितकर", "akusal": "हानिकर", "abyākat": "नैतिक रूप से अनिर्धारित",
    "savitakkasavicār": "आरंभिक विचार और सतत विचार वाला",
    "avitakkavicāramatt": "आरंभिक विचार से रहित केवल सतत विचार वाला",
    "avitakkaavicār": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "pītisahagat": "उल्लास के साथ होने वाला", "sukhasahagat": "सुख के साथ होने वाला",
    "upekkhāsahagat": "समभाव के साथ होने वाला",
    "upādinnupādāniy": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाला",
    "anupādinnupādāniy": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाला",
    "anupādinnaanupādāniy": "न कर्म से उत्पन्न न आसक्ति का विषय बनने वाला",
    "saṃkiliṭṭhasaṃkilesik": "क्लेशों से मलिन और क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhasaṃkilesik": "क्लेशों से मलिन न होने वाला पर क्लेशों का विषय बनने वाला",
    "asaṃkiliṭṭhaasaṃkilesik": "क्लेशों से मलिन न होने वाला और क्लेशों का विषय न बनने वाला",
    "ācayagām": "संचय की ओर ले जाने वाला", "apacayagām": "संचय घटाने की ओर ले जाने वाला",
    "nevācayagāmināpacayagām": "न संचय की ओर न संचय घटाने की ओर ले जाने वाला",
    "sekkh": "सीखने के चरण का", "asekkh": "सीखना पूरा होने के चरण का",
    "nevasekkhanāsekkh": "न सीखने के चरण का न सीखना पूरा होने के चरण का",
    "paritt": "सीमित", "mahaggat": "उन्नत", "appamāṇ": "अपरिमित",
    "parittārammaṇ": "सीमित विषय वाला", "mahaggatārammaṇ": "उन्नत विषय वाला",
    "appamāṇārammaṇ": "अपरिमित विषय वाला",
    "hīn": "हीन", "majjhim": "मध्यम", "paṇīt": "उत्तम",
    "micchattaniyat": "ग़लत दिशा में निश्चित", "sammattaniyat": "सही दिशा में निश्चित", "aniyat": "अनिश्चित",
    "maggārammaṇ": "मार्ग को विषय बनाने वाला", "maggahetuk": "मार्ग को मूल बनाने वाला",
    "maggādhipat": "मार्ग की प्रधानता वाला",
    "atītārammaṇ": "अतीत के विषय वाला", "anāgatārammaṇ": "भविष्य के विषय वाला",
    "paccuppannārammaṇ": "वर्तमान के विषय वाला",
    "ajjhatt": "स्वयं से संबंधित", "ajjhattārammaṇ": "स्वयं से संबंधित विषय वाला",
    "bahiddhārammaṇ": "दूसरों से संबंधित विषय वाला",
    "anidassanasappaṭigh": "दिखाई न देने वाला पर टकराव वाला",
    "anidassanaappaṭigh": "दिखाई न देने वाला और टकराव से रहित",
    "vipākadhamm": "कर्म-फल उत्पन्न करने वाला",
}
for _st, _h in TRIAD_ITEMS.items():
    for _e in ("aṃ", "o", "ā", "assa", "ānaṃ", "e", "añca", "a", "iṃ", "ī", "ino", "issa", "īnaṃ", "i"):
        PI7.setdefault(_st + _e, _h)
PI7.update({
    "bahiddhā": "दूसरों से संबंधित",
    "sukhāya": "सुखद", "dukkhāya": "दुःखद", "adukkhamasukhāya": "न दुःखद न सुखद",
    "vedanāya": "अनुभूति", "sampayuttaṃ": "जुड़ा", "sampayutto": "जुड़ा", "sampayuttā": "जुड़ा",
    "vippayuttaṃ": "अलग", "vippayutto": "अलग", "vippayuttā": "अलग",
    "dassanena": "सत्य-दर्शन", "bhāvanāya": "मानसिक अभ्यास",
    "pahātabbaṃ": "छोड़ा जाने वाला", "pahātabbo": "छोड़ा जाने वाला", "pahātabbā": "छोड़ा जाने वाला",
    "pahātabbahetukaṃ": "छोड़े जाने वाले मूलों वाला", "pahātabbahetuko": "छोड़े जाने वाले मूलों वाला",
    "kusalattikaṃ": "हितकर वाला तीन का वर्गीकरण", "kusalattike": "हितकर वाला तीन का वर्गीकरण",
    "kusalañca": "हितकर", "akusalañca": "हानिकर", "abyākatañca": "नैतिक रूप से अनिर्धारित",
})

# --- dyad items (the clusters; hi-zeroshot-terms.md §7 and pi-1 1-matika). X = the pi-1/pi-2 term
# (gantho = गाँठ, as pi-1/pi-2 map the «X रूपी» items); noX keeps its negative: «X रूपी न होने वाला»
# (pi-1 «hetu=मूल रूपी न होने वाला»); X-niya «Xों का विषय बनने वाला», aX-niya «… न बनने वाला»; in the
# closing pair «X-vippayutta X-niya» the -niya word = «उनका / उसका विषय (न) बनने वाला» (pi-1/pi-2 rule).
# (stem, Pāli -niya adjective stem, term, plural oblique, pronoun of the closing pair)
CLUSTERS = [
    ("hetu", None, "मूल", "मूलों", None),
    ("āsava", None, "मन के मैल", "मन के मैलों", "उनका"),
    ("saññojana", "saññojaniy", "बंधन", "बंधनों", "उनका"),
    ("saṃyojana", "saṃyojaniy", "बंधन", "बंधनों", "उनका"),
    ("gantha", "ganthaniy", "गाँठ", "गाँठों", "उनका"),
    ("ogha", "oghaniy", "बाढ़", "बाढ़ों", "उनका"),
    ("yoga", "yoganiy", "जकड़न", "जकड़नों", "उनका"),
    ("nīvaraṇa", "nīvaraṇiy", "बाधा", "बाधाओं", "उनका"),
    ("parāmāsa", "parāmaṭṭh", "ग़लत धारणा", "ग़लत धारणा", "उसका"),
    ("upādāna", "upādāniy", "आसक्ति", "आसक्ति", "उसका"),
    ("kilesa", "saṃkilesik", "मन के क्लेश", "क्लेशों", "उनका"),
]
CLOSING = {}                                    # -niya value inside the closing pair (pronoun form)
_NOUN_ENDINGS = ("o", "ā", "aṃ", "assa", "e", "a", "ānaṃ")      # applied to the stem without its final a / u
for _st, _niy, _term, _obl, _pron in CLUSTERS:
    _s = _st[:-1] if _st.endswith("a") else _st
    _forms = {_st} | ({_s + _e for _e in _NOUN_ENDINGS} if _st.endswith("a") else {_st + "ṃ", _st + "ssa"})
    for _form in _forms:
        PI7[_form] = _term
        PI7["no" + _form] = f"{_term} रूपी न होने वाला"
        PI7["na" + _form] = f"{_term} रूपी न होने वाला"
    for _e in _NOUN_ENDINGS:
        PI7[f"{_st}sampayutt{_e}"] = f"{_obl} से जुड़ा"
        PI7[f"{_st}vippayutt{_e}"] = f"{_obl} से अलग"
    if _niy:
        for _e in _NOUN_ENDINGS:
            PI7[_niy + _e] = f"{_obl} का विषय बनने वाला"
            PI7["a" + _niy + _e] = f"{_obl} का विषय न बनने वाला"
            CLOSING[_niy + _e] = f"{_pron} विषय बनने वाला"
            CLOSING["a" + _niy + _e] = f"{_pron} विषय न बनने वाला"
for _e in ("aṃ", "o", "ā", "assa", "a"):                          # āsava: sāsava / anāsava
    PI7["sāsav" + _e] = "मन के मैलों का विषय बनने वाला"
    PI7["anāsav" + _e] = "मन के मैलों का विषय न बनने वाला"
    CLOSING["sāsav" + _e] = "उनका विषय बनने वाला"
    CLOSING["anāsav" + _e] = "उनका विषय न बनने वाला"
PI7.update({
    "ceva": ("भी", NDE),                                            # «X रूपी भी और …» / «…, पर स्वयं …»
    "hetu": "मूल", "hetū": "मूल", "hetuṃ": "मूल", "nahetu": "मूल रूपी न होने वाला",
    "nahetuṃ": "मूल रूपी न होने वाला",
    "sahetukaṃ": "मूल वाला", "sahetuko": "मूल वाला", "ahetukaṃ": "मूल से रहित", "ahetuko": "मूल से रहित",
    "kenaci": "किसी एक प्रकार की चेतना", "viññeyyaṃ": "जाना जा सकने वाला",
})
DYAD_NAMES = {  # «X-dukaṃ» heading members (headings_sample_hi.py); the full single headings come from HEADNAMES
    "ganthaduka": "गाँठ वाला दो का वर्गीकरण", "ganthaniyaduka": "गाँठों के विषय वाला दो का वर्गीकरण",
    "ganthasampayuttaduka": "गाँठों से जुड़ाव वाला दो का वर्गीकरण",
    "ganthaganthaniyaduka": "गाँठ और गाँठों के विषय वाला दो का वर्गीकरण",
    "ganthaganthasampayuttaduka": "गाँठ और गाँठों से जुड़ाव वाला दो का वर्गीकरण",
    "ganthavippayuttaganthaniyaduka": "गाँठों से अलगाव और गाँठों के विषय वाला दो का वर्गीकरण",
}
PI7.update(DYAD_NAMES)


# ---------------------------------------------------------------------------- headings
def _strip_head(t):
    t = t.lstrip("#").strip().strip("*").strip()
    t = re.sub(r"^\(?\d+(?:[-.]\d+)*\.?\)?\.?\s+", "", t)           # 26-1. / (1) / (1.) / 1-7.
    t = re.sub(r"^\([कखगघ]\)\s+", "", t)
    t = re.sub(r"\s*\(\d+\)$", "", t)                                # trailing (3)
    return t.rstrip(".।").strip()


_HEADNAMES = None


def headnames():
    """Book-wide: Pāli single heading word (lower-case first letter) -> Hindi heading, where unique."""
    global _HEADNAMES
    if _HEADNAMES is None:
        seen = collections.defaultdict(set)
        for p in sorted(PI_DIR.glob("*.md")):
            a, b = _segments(p), _segments(HI_DIR / p.name)
            for bid, t in a.items():
                if t.startswith("#") and bid in b and b[bid].startswith("#"):
                    pa, hi = _strip_head(t), _strip_head(b[bid])
                    if " " not in pa:
                        seen[lc(pa)].add(_clean_head_value(hi))
        _HEADNAMES = {k: next(iter(v)) for k, v in seen.items() if len(v) == 1}
    return _HEADNAMES


def _clean_head_value(hi):
    hi = hi.replace(", ", " ").replace(",", "")
    return re.sub(r" में$", "", hi)


def heading_value(kw, pali_seg, hindi_seg):
    """Whole-heading rule: the keyword is the whole Pāli heading -> the whole Hindi heading."""
    if not pali_seg or not hindi_seg or not pali_seg.startswith("#") or not hindi_seg.startswith("#"):
        return None
    if lc(kw.rstrip(".")) == lc(_strip_head(pali_seg)):
        return _clean_head_value(_strip_head(hindi_seg))
    return None


# ---------------------------------------------------------------------------- lookup
def _strip_particles(k):
    """Candidate forms after dropping the quotative -ti and the enclitics -ñca / -ñceva / -pi / -mpi."""
    out = []
    for suf, rep in (("ñceva", "ṃ"), ("ñca", "ṃ"), ("mpi", "ṃ"), ("pi", ""), ("ceva", "")):
        if k.endswith(suf) and len(k) > len(suf) + 2:
            out.append(k[: -len(suf)] + rep)
    for suf, reps in (("īti", ("i",)), ("āti", ("ā", "a")), ("ūti", ("ū", "u")), ("nti", ("ṃ",)),
                      ("oti", ("o",)), ("eti", ("e",))):
        if k.endswith(suf) and len(k) > len(suf) + 2:
            out += [k[: -len(suf)] + r for r in reps]
            break
    return out


def _pick(v, text):
    if isinstance(v, tuple):
        if text is not None:
            for alt in v:
                if present(alt, text):
                    return alt
        return v[0]
    return v


SOURCES = ("table", "headnames", "PI2", "CH2", "matrix")


def lookup(kw, kws, table=None, text=None, closing=False):
    """(value, source) from the tables only (no heading rule, no override)."""
    table = PI7 if table is None else table
    k = lc(kw)
    for cand in [k] + _strip_particles(k):
        if closing and cand in CLOSING:
            return CLOSING[cand], "table"
        if cand in table:
            return _pick(table[cand], text), "table"
    hn = headnames()
    for cand in [k, k + "ṃ"] + _strip_particles(k):
        if cand in hn:
            return hn[cand], "headnames"
    for name, src in (("PI2", PI2), ("CH2", CH2)):
        for cand in [k] + _strip_particles(k):
            if cand in src:
                v = src[cand]
                return (v[0] if isinstance(v, tuple) else v), name
    mn = _matrix_names()
    for cand in [k] + _strip_particles(k):
        if cand in mn:
            return mn[cand], "matrix"
    raise KeyError(kw)


def _is_closing(kws, text):
    """Closing pair «X-vippayutta X-niya»: a cluster -vippayutta keyword in the segment and the Hindi has
    «उनका/उसका विषय»."""
    return any("vippayutt" in lc(x) for x in kws) and text is not None and (
        "उनका विषय" in text or "उसका विषय" in text)


def pi7_value(kw, kws, table=None, pali=None, text=None):
    v = heading_value(kw, pali, text)
    if v is not None:
        return v, "heading"
    return lookup(kw, kws, table, text, closing=_is_closing(kws, text))


def make_resolver(f, table=None, ovr=None, log=None):
    """resolver(bid, kw, kws): OVR[bid][kw] first, then pi7_value with the segment's Pāli and Hindi.
    log: optional dict collecting {(kw, value): Counter(source)}."""
    ovr = ovr or {}
    hi, pa = read_hindi(f), read_pali(f)

    def resolver(bid, kw, kws):
        o = ovr.get(bid, {})
        if kw in o:
            v, src = o[kw], "override"
        else:
            v, src = pi7_value(kw, kws, table, pa.get(bid), hi.get(bid))
        if log is not None:
            log.setdefault((kw, v), collections.Counter())[src] += 1
        return v
    return resolver


# ---------------------------------------------------------------------------- build, verify, audit
def build_part(f, resolver):
    """resolver(bid, kw, kws) -> Hindi value. Raises SystemExit listing unmapped keywords."""
    lines, missing = [], []
    for bid, kws in read_keywords(f):
        if not kws:
            lines.append(f"[{bid}]")
            continue
        pairs = []
        for kw in kws:
            try:
                v = resolver(bid, kw, kws)
            except KeyError:
                missing.append((bid, kw))
                v = "???"
            assert ", " not in v and "=" not in v, (bid, kw, v)
            pairs.append(f"{kw}={v}")
        lines.append(f"[{bid}] " + ", ".join(pairs))
    if missing:
        raise SystemExit(f"{f}: unmapped keywords: {missing}")
    (HERE / f"{f}.mapped.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(lines)


def verify(f, show=60, allowed=None):
    """The brief's structural check + presence check. allowed: {(bid, kw): reason} listed, not counted."""
    allowed = allowed or {}
    a = [l.split("] ", 1) for l in (HERE / f"{f}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for i, (x, y) in enumerate(zip(a, b))
           if len(x) > 1 and [k.strip() for k in x[1].split(", ")] != [k.split("=", 1)[0] for k in y[1].split(", ")]]
    hi = read_hindi(f)
    nde, miss, exc = 0, [], []
    for x in b:
        if len(x) < 2:
            continue
        bid, rest = x[0][1:], x[1]
        text = hi.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
            elif text is None or not present(v, text):
                (exc if (bid, kw) in allowed else miss).append((bid, kw, v))
    print(f, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss),
          "| listed exceptions", len(exc))
    for m in miss[:show]:
        print("   MISS", *m)
    for e in exc:
        print("   EXC ", *e, "--", allowed[(e[0], e[1])])
    return bad, nde, miss


def audit(f, table=None, ovr=None, only_fallback=False):
    """Each keyword with its values and where they came from (override / heading / table / headnames /
    PI2 / CH2 / matrix). Fallback sources are the ones to check by eye."""
    log = {}
    res = make_resolver(f, table, ovr, log)
    for bid, kws in read_keywords(f):
        for kw in kws:
            res(bid, kw, kws)
    by_kw = collections.defaultdict(list)
    for (kw, v), c in log.items():
        by_kw[kw].append((v, dict(c)))
    for kw in sorted(by_kw, key=lc):
        vals = by_kw[kw]
        if only_fallback and all(set(c) <= {"table", "heading", "override"} for _, c in vals):
            continue
        print(kw, "->", "; ".join(f"{v} {c}" for v, c in vals))


# ============================================================================ the sample
SAMPLE = ("preamble", "1-00-paccaya", "2-13-atitattika", "4-07-dukatika-ganthaduka")
# per-segment overrides {file: {bid: {kw (exact spelling): value}}}; reasons in hi-map-conventions-pi7.md
SAMPLE_OVR = {
    "preamble": {},
    "1-00-paccaya": {},
    "2-13-atitattika": {},
    "4-07-dukatika-ganthaduka": {},
}
# presence exceptions {file: {(bid, kw): reason}}
SAMPLE_ALLOWED = {
    "preamble": {},
    "1-00-paccaya": {},
    "2-13-atitattika": {},
    "4-07-dukatika-ganthaduka": {},
}

if __name__ == "__main__":
    for _f in SAMPLE:
        build_part(_f, make_resolver(_f, PI7, SAMPLE_OVR[_f]))
        verify(_f, allowed=SAMPLE_ALLOWED[_f])
    if "--audit" in sys.argv:
        for _f in SAMPLE:
            print("=" * 20, _f)
            audit(_f, PI7, SAMPLE_OVR[_f])
