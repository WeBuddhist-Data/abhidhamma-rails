"""pi-6 (Yamaka) Pāli->Hindi keyword maps: shared tooling + the sample (preamble, 1-mulayamaka, 2-01-khandhayamaka).

Importing this module writes nothing and prints nothing. Later chapter scripts:

    import sys, pathlib; sys.dont_write_bytecode = True   # no __pycache__ in the shared folder
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_sample_hi import *          # PI6, pi6_value, make_resolver, build_part, verify, present, prior, ...

    T = {...}                             # your chapter table (lower-case first letter keys)
    OVR = {"6-x-y": {"kw": "हिंदी"}}        # per-segment overrides (exact keyword spelling)
    build_part("<file>", make_resolver("<file>", {**PI6, **T}, OVR))
    verify("<file>", allowed={("6-x-y", "kw"): "reason"})

Main pieces
- read_keywords(f) / read_hindi(f) / read_pali(f)   pi-6 paths; segments end with ^id
- present(value, text)     pi-1 presence check (map_common_hi) plus two pi-6 tolerances:
                           «नहीं» counts as the dropped negative (value «समाप्त हुआ था» ~ text «समाप्त नहीं हुआ था»),
                           and the tense forms agree in gender/number (हुआ था ~ हुई थी / हुए थे; होगा ~ होगी / होंगे)
- PI6                      default table settled on the sample; a value may be a tuple of alternatives, the first
                           one present in the segment's Hindi wins (else the first); PI2 (pi-2) and CH2 (pi-1) are
                           the fallbacks
- BARE                     the bare words of the word-checking pairs (rūpaṃ = रूप, saṅkhārā = रचनाएँ), used when the
                           segment also has a khandha keyword
- pi6_value(kw, kws, table, bid, text)   table lookup + the context rules (see CONTEXT RULES)
- prior(kw)                values the same Pāli keyword got in the finished pi-1/2/3/4/5 Hindi maps
- make_resolver(f, table, ovr)  OVR[bid][kw] first, then pi6_value with the segment's Hindi
- build_part(f, resolver)  writes <f>.mapped.md; stops on unmapped keywords / ", " in a value
- verify(f, allowed)       the brief's structural check + presence check; prints a report
usage (sample): python -I -X utf8 map_sample_hi.py
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

_spec = importlib.util.spec_from_file_location("map_sample_hi_pi2", _PI2 / "map_sample_hi.py")
_pi2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_pi2)                     # read-only: pi-2's PI2 table (its __main__ does not run)
PI2 = _pi2.PI2

HI_DIR = ROOT / "AI_translation" / "hindi" / "pi-6-hindi-plain-zeroshot_split_chapters"
PI_DIR = ROOT / "AI_translation" / "pali" / "pi-6_split_chapters"
PRIOR_BOOKS = (1, 2, 3, 4, 5)
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
    """{book: Counter(values)} for this keyword in the finished pi-1/2/3/4/5 Hindi maps."""
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
_NAHIN = re.compile(f"(?<![{DEV}])नहीं(?![{DEV}])")
# gender/number forms of the tense endings (the value is masculine singular, the text agrees with its subject)
_AGREE = [("हुआ था", ("हुई थी", "हुए थे", "हुई थीं")), ("होगा", ("होगी", "होंगे", "होंगी")),
          ("होता", ("होती", "होते"))]


def present(value, text):
    """pi-1 present() + «नहीं» as a dropped negative + gender/number of the tense endings."""
    if value == NDE:
        return True
    if text is None:
        return False
    cands = [value]
    for a, alts in _AGREE:
        if a in value:
            cands += [value.replace(a, b) for b in alts]
    text = text.replace("सबमें", "सब में")                       # «बाकी सबमें» = बाकी सब + में
    t2 = _NAHIN.sub("न", text)
    for v in cands:
        if _present_pi1(v, text) or _present_pi1(_NAHIN.sub("न", v), t2):
            return True
    return False


# ---------------------------------------------------------------------------- PI6 default table
# Values: dictionary form (nouns direct sg, adjectives/participles masc. sg, verbs infinitive, past/future
# tense = the finite form the text uses, masc., in the Pāli's number), pi-1/pi-2 wording where the Pāli is the
# same. A tuple = alternatives, the first one present in the segment's Hindi wins.
PI6 = {}

# --- book frame (pi-1/pi-2 preamble) and chapter titles (hi-zeroshot-terms.md)
PI6.update({
    "abhidhammapiṭake": "अभिधम्म पिटक", "abhidhamma": "अभिधम्म",
    "namo": "नमन", "bhagavato": "भगवान", "arahato": "अर्हत्", "sammā": "पूर्ण रूप से",
    "sambuddhassa": "जागृत बुद्ध", "sammāsambuddhassa": "पूर्ण रूप से जागृत बुद्ध",
    "yamakapāḷi": "प्रश्नों के जोड़े", "yamaka": "प्रश्नों के जोड़े", "yamakaṃ": "प्रश्नों के जोड़े",
    "pāḷi": NDE,
})
CHAPTERS = {"mūla": "मूलों", "khandha": "समूहों", "āyatana": "इंद्रिय-क्षेत्रों", "dhātu": "तत्वों",
            "sacca": "सत्यों", "saṅkhāra": "रचनाओं", "anusaya": "सुप्त प्रवृत्तियों", "citta": "मन",
            "dhamma": "परिघटनाओं", "indriya": "क्षमताओं"}
for _p, _h in CHAPTERS.items():
    for _e in ("yamakaṃ", "yamakapāḷi", "yamaka"):
        PI6[_p + _e] = f"{_h} पर प्रश्नों के जोड़े"

# --- section headings (hi-zeroshot-terms.md «Section headings»)
PI6.update({
    "vāro": "खंड", "vāra": "खंड", "nayo": "विधि", "naya": "विधि",
    "uddeso": "सूची", "uddesa": "सूची", "niddeso": "व्याख्या", "niddesa": "व्याख्या",
    "uddesavāro": "सूची का खंड", "niddesavāro": "व्याख्या का खंड",
    "mūlavāro": "मूल का खंड", "mūlavārauddeso": "मूल के खंड की सूची", "mūlavāraniddeso": "मूल के खंड की व्याख्या",
    "mūlanayo": "मूल की विधि", "mūlamūlanayo": "मूल के मूल की विधि",
    "mūlakanayo": "मूल पर आधारित होने की विधि", "mūlamūlakanayo": "मूल के मूल पर आधारित होने की विधि",
    "hetuvārādi": "हेतु का खंड आदि", "hetuvāro": "हेतु का खंड",
    "paṇṇatti": "शब्दावली", "paṇṇattivāro": "शब्दावली का खंड",
    "paṇṇattivāraniddesa": "शब्दावली के खंड की व्याख्या", "paṇṇattivāraniddeso": "शब्दावली के खंड की व्याख्या",
    "paṇṇattiuddesavāro": "शब्दावली की सूची का खंड", "paṇṇattiniddesavāro": "शब्दावली की व्याख्या का खंड",
    "padasodhana": "शब्दों की जाँच", "padasodhanavāro": "शब्दों की जाँच का खंड",
    "padasodhanamūlacakkavāro": "शब्दों की जाँच पर आधारित चक्र का खंड",
    "cakka": "चक्र", "suddha": "केवल",
    "anulomaṃ": "सकारात्मक", "anuloma": "सकारात्मक", "paccanīkaṃ": "नकारात्मक", "paccanīka": "नकारात्मक",
    "paṭilomaṃ": "विपरीत", "paṭiloma": "विपरीत",
    "puggala": "व्यक्ति", "puggalo": "व्यक्ति", "okāsa": "स्थान", "okāso": "स्थान",
    "pavatti": "प्रक्रिया", "pavattivāro": "प्रक्रिया का खंड",
    "uppāda": ("उत्पन्न होना", "उत्पत्ति"), "nirodha": ("समाप्त होना", "निरोध"),
    "uppādavāro": "उत्पन्न होने का खंड", "nirodhavāro": "समाप्त होने का खंड",
    "uppādanirodhavāro": "उत्पन्न होने और समाप्त होने का खंड",
    "paccuppannavāro": "वर्तमान का खंड", "atītavāro": "अतीत का खंड", "anāgatavāro": "भविष्य का खंड",
    "paccuppannātītavāro": "वर्तमान और अतीत का खंड", "paccuppannānāgatavāro": "वर्तमान और भविष्य का खंड",
    "atītānāgatavāro": "अतीत और भविष्य का खंड",
    "puggalavāro": "व्यक्ति का खंड", "dhammavāro": "परिघटना का खंड", "puggaladhammavāro": "व्यक्ति और परिघटना का खंड",
    "pariññāvāro": "पूरी तरह समझने का खंड", "pajahanavāro": "छोड़ने का खंड",
    "pahīnavāro": "छोड़ा जा चुका होने का खंड", "bhāvanāvāro": "अभ्यास का खंड",
    "niṭṭhito": "पूरा हुआ", "niṭṭhitā": "पूरा हुआ", "niṭṭhitaṃ": "पूरा हुआ",
})
# anuloma/paccanīka/paṭiloma + puggala/okāsa headings: «सकारात्मक: व्यक्ति» (the Hindi heading, colon kept)
for _p, _ph in (("anuloma", "सकारात्मक"), ("paccanīka", "नकारात्मक"), ("paṭiloma", "विपरीत")):
    PI6[_p + "puggalo"] = f"{_ph}: व्यक्ति"
    PI6[_p + "okāso"] = f"{_ph}: स्थान"
    PI6[_p + "puggalokāsā"] = f"{_ph}: व्यक्ति और स्थान"
# Suddha-X-vāro / Suddha-X-mūlacakkavāro
for _p, _h in (("khandha", "समूहों"), ("āyatana", "इंद्रिय-क्षेत्रों"), ("dhātu", "तत्वों"), ("sacca", "सत्यों"),
               ("saṅkhāra", "रचनाओं"), ("dhamma", "परिघटनाओं"), ("indriya", "क्षमताओं")):
    PI6[f"suddha{_p}vāro"] = f"केवल {_h} का खंड"
    PI6[f"suddha{_p}mūlacakkavāro"] = f"केवल {_h} पर आधारित चक्र का खंड"
PI6["suddhindriyavāro"] = "केवल क्षमताओं का खंड"
PI6["suddhindriyamūlacakkavāro"] = "केवल क्षमताओं पर आधारित चक्र का खंड"
PI6["suddhāyatanavāro"] = "केवल इंद्रिय-क्षेत्रों का खंड"
PI6["suddhāyatanamūlacakkavāro"] = "केवल इंद्रिय-क्षेत्रों पर आधारित चक्र का खंड"

# --- the four kinds of dhamma and their roots (Mūlayamaka). T = the term, R = «<T> मूल» (direct / oblique)
TERMS = {  # stem: (term, term as the stem of a «… से उत्पन्न» compound, root direct, root oblique, genitive head)
    "kusala": ("हितकर", "हितकर", "हितकर मूल", "हितकर मूल", "हितकर"),
    "akusala": ("हानिकर", "हानिकर", "हानिकर मूल", "हानिकर मूल", "हानिकर"),
    "abyākata": ("नैतिक रूप से अनिर्धारित", "नैतिक रूप से अनिर्धारित", "नैतिक रूप से अनिर्धारित मूल",
                 "नैतिक रूप से अनिर्धारित मूल", "नैतिक रूप से अनिर्धारित"),
    "nāma": ("मानसिक पक्ष", "मानसिक पक्ष", "मानसिक पक्ष का मूल", "मानसिक पक्ष के मूल", "मानसिक पक्ष का"),
}
for _st, (_t, _ts, _rd, _ro, _g) in TERMS.items():
    for _e in ("ā", "aṃ", "o", "a"):
        PI6[_st[:-1] + _e] = _t                                     # kusal+ā = kusalā
    PI6[_st[:-1] + "ā dhammā"] = "मानसिक पक्ष की परिघटना" if _st == "nāma" else f"{_t} परिघटना"
    PI6["dhammā " + _st[:-1] + "ā"] = PI6[_st[:-1] + "ā dhammā"]
    for _e in ("ā", "āni", "aṃ", "ena", "o", "assa"):
        PI6[f"{_st}mūl{_e}"] = _rd                                  # kusalamūlā = हितकर मूल
        PI6[f"{_st}mūlamūl{_e}"] = f"{_ro} का मूल"                  # kusalamūlamūlā = हितकर मूल का मूल
    for _e in ("ā", "āni", "aṃ", "o"):
        PI6[f"{_st}mūlak{_e}"] = f"{_ro} पर आधारित"                 # kusalamūlakā = हितकर मूल पर आधारित
        PI6[f"{_st}mūlamūlak{_e}"] = f"{_ro} के मूल पर आधारित"
    PI6[f"{_st}mūlasahajātā"] = f"{_ro} के साथ उत्पन्न"
    PI6[f"{_st}mūlasahajātā dhammā"] = f"{_ro} के साथ उत्पन्न परिघटना"
    PI6[f"{_st}samuṭṭhānaṃ"] = f"{_ts} से उत्पन्न"                 # Kusalasamuṭṭhānaṃ rūpaṃ = हितकर से उत्पन्न …
    # the ten names of a root (Hetuvārādi): hetu हेतु, nidāna स्रोत, sambhava उद्भव, pabhava उद्गम,
    # samuṭṭhāna उत्पादक, āhāra आहार, ārammaṇa विषय, paccaya कारण, samudaya उत्पत्ति (fem.)
    for _n, _h, _fem in (("hetū", "हेतु", 0), ("hetu", "हेतु", 0), ("nidānā", "स्रोत", 0),
                         ("sambhavā", "उद्भव", 0), ("ppabhavā", "उद्गम", 0), ("pabhavā", "उद्गम", 0),
                         ("samuṭṭhānā", "उत्पादक", 0), ("āhārā", "आहार", 0), ("ārammaṇā", "विषय", 0),
                         ("paccayā", "कारण", 0), ("samudayā", "उत्पत्ति", 1)):
        _stem = _st[:-1] if _n[0] == "ā" else _st                 # kusal+āhārā, nām+ārammaṇā
        _head = (_g[:-2] + "की" if _fem else _g) if _st == "nāma" else _g
        PI6[_stem + _n] = f"{_head} {_h}"
for _e in ("ā", "āni", "aṃ", "o"):
    PI6[f"ekamūl{_e}"] = "एक ही मूल वाला"
    PI6[f"ekamūlamūl{_e}"] = "एक ही मूल के मूल वाला"
    PI6[f"ekamūlak{_e}"] = "एक ही मूल पर आधारित"
    PI6[f"ekamūlamūlak{_e}"] = "एक ही मूल के मूल पर आधारित"
    PI6[f"aññamaññamūl{_e}"] = "परस्पर मूल वाला"
    PI6[f"aññamaññamūlamūl{_e}"] = "परस्पर मूल के मूल वाला"
    PI6[f"aññamaññamūlak{_e}"] = "परस्पर मूल पर आधारित"
    PI6[f"aññamaññamūlamūlak{_e}"] = "परस्पर मूल के मूल पर आधारित"
PI6.update({
    "mūla": "मूल", "mūlaṃ": "मूल", "mūlāni": "मूल", "mūlā": "मूल",
    "hetu": "हेतु", "hetū": "हेतु",                               # the ten names (Hetuvārādi); root sense = मूल
    "nidānaṃ": "स्रोत", "nidāna": "स्रोत", "sambhavo": "उद्भव", "pabhavo": "उद्गम", "pabhavena": "उद्गम",
    "samuṭṭhāna": "उत्पादक", "āhāro": "आहार", "ārammaṇaṃ": "विषय", "paccayo": "कारण",
    "samudayo": "उत्पत्ति", "samudayena": "उत्पत्ति",
    "samuṭṭhānāhārārammaṇā": "उत्पादक आहार और विषय", "samuṭṭhānāhārārammaṇaṃ": "उत्पादक आहार और विषय",
    "ahetukaṃ": "मूल से रहित", "sahetukaṃ": "मूल वाला", "ahetuko": "मूल से रहित", "sahetuko": "मूल वाला",
    "ekato": "एक साथ", "sahajātā": "के साथ उत्पन्न",
    "avasesā": "शेष", "ṭhapetvā": "छोड़कर",
    "uppajjanti": "उत्पन्न होना",
})

# --- the aggregates (pi-2: X-kkhandho = «X का समूह»; khandha = समूह)
PI6.update({
    "khandha": "समूह", "khandho": "समूह", "khandhā": "समूह", "khandhe": "समूह", "khandhānaṃ": "समूह",
    "pañcakkhandhā": "पाँच समूह", "avasesā khandhā": "शेष समूह",
    "rūpaṃ": "भौतिक रूप", "rūpa": "भौतिक रूप", "vedanā": "अनुभूति", "vedanaṃ": "अनुभूति",
    "saññā": "पहचान", "saññaṃ": "पहचान", "saṅkhārā": "मानसिक रचनाएँ", "saṅkhāre": "मानसिक रचनाएँ",
    "saṅkhāra": "मानसिक रचनाएँ", "viññāṇaṃ": "चेतना", "viññāṇa": "चेतना",
    "diṭṭhisaññā": "दृष्टि के अर्थ में पहचान", "piyarūpaṃ": "प्रिय … रूप", "sātarūpaṃ": "सुहावना लगने वाला रूप",
})
for _p, _h in (("rūpa", "भौतिक रूप"), ("vedanā", "अनुभूति"), ("saññā", "पहचान"), ("saṅkhāra", "मानसिक रचनाओं"),
               ("viññāṇa", "चेतना")):
    for _e in ("o", "aṃ", "assa", "ā"):
        PI6[f"{_p}kkhandh{_e}"] = f"{_h} का समूह"
# the bare words of the word-checking pairs (Paṇṇattivāra): used when the segment has a khandha keyword
BARE = {"rūpaṃ": "रूप", "rūpa": "रूप", "saṅkhārā": "रचनाएँ", "saṅkhāre": "रचनाएँ", "saṅkhāra": "रचनाएँ"}

# --- process verbs (Pavattivāra). Present = infinitive; past/future = the finite form, masc., Pāli number;
#     a fused negative (n-uppajjati) keeps «नहीं» as the Hindi has it; a separate «na» is its own word.
PI6.update({
    "uppajjati": "उत्पन्न होना", "nuppajjati": "उत्पन्न नहीं होना",
    "uppajjittha": "उत्पन्न हुआ था", "nuppajjittha": "उत्पन्न नहीं हुआ था",
    "uppajjissati": "उत्पन्न होगा", "nuppajjissati": "उत्पन्न नहीं होगा",
    "nuppajjanti": "उत्पन्न नहीं होना", "uppajjiṃsu": "उत्पन्न हुए थे", "uppajjissanti": "उत्पन्न होंगे",
    "nirujjhati": "समाप्त होना", "nirujjhittha": "समाप्त हुआ था", "nirujjhissati": "समाप्त होगा",
    "nirujjhattha": "समाप्त हुआ था",                               # Pāli misprint in 6-2-111, same verb
    "nirujjhanti": "समाप्त होना",
    "uppajjamāna": "उत्पन्न होता हुआ", "uppajjamānaṃ": "उत्पन्न होता हुआ",
    "nirujjhamāna": "समाप्त होता हुआ", "nirujjhamānaṃ": "समाप्त होता हुआ",
    "uppanna": "उत्पन्न हो चुका", "uppannaṃ": "उत्पन्न हो चुका", "niruddha": "समाप्त हो चुका",
    "niruddhaṃ": "समाप्त हो चुका",
    "natthi": "ऐसा कोई नहीं",                                      # short answer «ऐसा कोई नहीं है।»
})

# --- beings and places. Place sense (acc. of destination, loc., abl.) = «… का लोक / अस्तित्व»;
#     beings sense (gen. pl.) = «… के प्राणी»; the participle nouns are masc. sg. «… वाला»
PI6.update({
    "asaññasatta": "पहचान-रहित प्राणी",
    "asaññasattaṃ": "पहचान-रहित प्राणियों का लोक", "asaññasatte": "पहचान-रहित प्राणियों का लोक",
    "asaññasattā": "पहचान-रहित प्राणियों का लोक", "asaññasattānaṃ": "पहचान-रहित प्राणी",
    "pañcavokāra": "पाँच समूहों वाला अस्तित्व",
    "pañcavokāraṃ": "पाँच समूहों वाला अस्तित्व", "pañcavokāre": "पाँच समूहों वाला अस्तित्व",
    "pañcavokārā": "पाँच समूहों वाला अस्तित्व", "pañcavokārānaṃ": "पाँच समूहों वाले अस्तित्व के प्राणी",
    "catuvokāra": "चार समूहों वाला अस्तित्व", "catuvokāraṃ": "चार समूहों वाला अस्तित्व",
    "catuvokāre": "चार समूहों वाला अस्तित्व", "catuvokārā": "चार समूहों वाला अस्तित्व",
    "catuvokārānaṃ": "चार समूहों वाले अस्तित्व के प्राणी",
    "ekavokāra": "एक समूह वाला अस्तित्व",
    "arūpa": "अभौतिक लोक", "arūpaṃ": "अभौतिक लोक", "arūpe": "अभौतिक लोक", "arūpā": "अभौतिक लोक",
    "arūpānaṃ": "अभौतिक लोक के प्राणी",
    "suddhāvāsa": "शुद्ध निवास लोक", "suddhāvāsaṃ": "शुद्ध निवास लोक", "suddhāvāse": "शुद्ध निवास लोक",
    "suddhāvāsā": "शुद्ध निवास लोक", "suddhāvāsānaṃ": "शुद्ध निवास लोक के प्राणी",
    "upapajjati": "जन्म लेना", "upapajjantānaṃ": "जन्म लेने वाला", "upapajjitvā": "जन्म लेकर",
    "upapajjantīnaṃ": "जन्म लेने वाली स्त्री",
    "cavati": "मरना", "cavantānaṃ": "मरने वाला", "cavantīnaṃ": "मरने वाली स्त्री",
    "parinibbantānaṃ": "पूर्ण निर्वाण पाने वाला", "parinibbāyissanti": "पूर्ण निर्वाण पाएँगे",
    "pacchimabhavikānaṃ": ("अंतिम जन्म वाला", "अंतिम जन्म"),       # «… में अंतिम जन्म लेने वालों में» (B2)
    "itaresaṃ": ("बाकी सब", "बाकी"),                               # «बाकी सबमें» alone, «बाकी X में» before a place
    "sabbesaṃ": "सभी", "tesaṃ": "उनमें", "tattha": "वहाँ", "tassa": "उसमें", "yassa": "जिस व्यक्ति",
    "yattha": "जिस स्थान", "puggalassa": "व्यक्ति",
})


# ---------------------------------------------------------------------------- context rules
def _strip_particles(k):
    """Candidate lookup forms after dropping the quotative -ti and the enclitics -ñca / -ñceva / ceva
    (pi-1: X-meva -> the Hindi of X; the quotative -ti is dropped in the Hindi, terms file)."""
    out = []
    for suf, rep in (("ñceva", "ṃ"), ("ñca", "ṃ"), ("ceva", ""), ("ñcāti", "ṃ")):
        if k.endswith(suf) and len(k) > len(suf) + 2:
            out.append(k[: -len(suf)] + rep)
    for suf, reps in (("īti", ("i",)), ("āti", ("ā", "a")), ("ūti", ("ū", "u")), ("nti", ("ṃ",)),
                      ("oti", ("o",)), ("eti", ("e",)), ("ti", ("",))):
        if k.endswith(suf) and len(k) > len(suf) + 2:
            out += [k[: -len(suf)] + r for r in reps]
            break
    return out


def _lookup(k, table):
    for src in (table, PI2, CH2):
        if k in src:
            return src[k]
    return None


def _pick(v, text):
    if isinstance(v, tuple):
        if text is not None:
            for alt in v:
                if present(alt, text):
                    return alt
        return v[0]
    return v


def pi6_value(kw, kws, table=PI6, bid=None, text=None):
    """Default Hindi for a keyword: table lookup (table, then PI2, then CH2; after that the same with the
    quotative -ti / the enclitic -ñca, -ñceva dropped) + the context rules:
    - bare words: rūpaṃ = रूप, saṅkhārā = रचनाएँ where the segment also has a khandha keyword (the word-checking
      pairs of the Paṇṇattivāra), else भौतिक रूप / मानसिक रचनाएँ;
    - tuple values: the first alternative present in the segment's Hindi (text) wins."""
    k = lc(kw)
    s = [lc(x) for x in kws]
    for cand in [k] + _strip_particles(k):
        if cand in BARE and any("khandh" in x for x in s):
            return _pick(BARE[cand], text)
        v = _lookup(cand, table)
        if v is not None:
            return _pick(v, text)
    raise KeyError(kw)


def make_resolver(f, table=PI6, ovr=None):
    """resolver(bid, kw, kws): OVR[bid][kw] first, then pi6_value with the segment's Hindi."""
    ovr = ovr or {}
    hi = read_hindi(f)

    def resolver(bid, kw, kws):
        o = ovr.get(bid, {})
        if kw in o:
            return o[kw]
        return pi6_value(kw, kws, table, bid, hi.get(bid))
    return resolver


# ---------------------------------------------------------------------------- build and verify
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


# ============================================================================ the sample
SAMPLE = ("preamble", "1-mulayamaka", "2-01-khandhayamaka")
# per-segment overrides {file: {bid: {kw (exact spelling): value}}}; reasons in hi-map-conventions-pi6.md
SAMPLE_OVR = {
    "preamble": {},
    "1-mulayamaka": {},
    "2-01-khandhayamaka": {},
}
# presence exceptions {file: {(bid, kw): reason}}
SAMPLE_ALLOWED = {
    "preamble": {},
    "1-mulayamaka": {},
    "2-01-khandhayamaka": {},
}

if __name__ == "__main__":
    for _f in SAMPLE:
        build_part(_f, make_resolver(_f, PI6, SAMPLE_OVR[_f]))
        verify(_f, allowed=SAMPLE_ALLOWED[_f])
