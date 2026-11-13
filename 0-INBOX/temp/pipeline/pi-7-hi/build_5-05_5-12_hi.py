"""Hindi plain zero-shot builder for pi-7 (Paṭṭhāna) files 5-05 .. 5-12
(Dhammapaccanīya and Dhammānulomapaccanīya parts).

Every line is composed from fixed frames (build_sample_hi, imported, never edited) and item tables,
so every repeated Pāli formula gets byte-identical Hindi.

    python -I -B -X utf8 build_5-05_5-12_hi.py            # build all 8 files
    python -I -B -X utf8 build_5-05_5-12_hi.py --report   # also write slip/anomaly report
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402  (import only)

HERE = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
PALI_DIR, HI_DIR = S.PALI_DIR, S.HI_DIR
FILES = ["5-05-paccaniya-dukatika.md", "5-06-paccaniya-tikaduka.md", "5-07-paccaniya-tikatika.md",
         "5-08-paccaniya-dukaduka.md", "5-09-anulomapaccaniya-tika.md", "5-10-anulomapaccaniya-duka.md",
         "5-11-anulomapaccaniya-dukatika.md", "5-12-anulomapaccaniya-tikaduka.md"]

# extra Pāli number words for the counting lines (the sample table lacks the short -vīsa forms)
S.NUM.update({
    "ekūnavīsa": "उन्नीस", "ekavīsa": "इक्कीस", "bāvīsa": "बाईस", "tevīsa": "तेईस", "catuvīsa": "चौबीस",
    "pañcavīsa": "पच्चीस", "chabbīsa": "छब्बीस", "sattavīsa": "सत्ताईस", "aṭṭhavīsa": "अट्ठाईस",
    "ekūnatiṃsa": "उनतीस", "tiṃsa": "तीस", "ekatiṃsa": "इकतीस", "dvattiṃsa": "बत्तीस", "tettiṃsa": "तैंतीस",
    "catuttiṃsa": "चौंतीस", "pañcatiṃsa": "पैंतीस", "chattiṃsa": "छत्तीस", "sattatiṃsa": "सैंतीस",
    "aṭṭhatiṃsa": "अड़तीस", "ekūnacattālīsa": "उनतालीस", "cattālīsa": "चालीस",
    "aṭṭhacattālīsa": "अड़तालीस", "ekūnapaññāsa": "उनचास", "paññāsa": "पचास", "tīṇiyeva": "तीन ही",
    "ekaṃyeva": "एक ही",
})

DH, DH_PL = S.DHAMMA, S.DHAMMA_PL          # परिघटना / परिघटनाएँ
NEG = " न होने वाली"                          # one "na"/"no" on an item (pattern of pi-1 "… न होने वाली")

# =====================================================================================
# 1. Items (positive Hindi, feminine with परिघटना), pi-1 matrix wording
# =====================================================================================
# (Pāli stem, class, Hindi); class: a / u / i / ind ; "+n" = the stem already contains "dhamma"
ITEMS = [
    # kusalattika and the other triads
    ("kusala", "a", "हितकर"), ("akusala", "a", "हानिकर"), ("abyākata", "a", "नैतिक रूप से अनिर्धारित"),
    ("kusalākusala", "a", "हितकर या हानिकर"),
    ("sukhāya vedanāya sampayutta", "a", "सुखद अनुभूति से जुड़ी"),
    ("dukkhāya vedanāya sampayutta", "a", "दुःखद अनुभूति से जुड़ी"),
    ("adukkhamasukhāya vedanāya sampayutta", "a", "न दुःखद, न सुखद अनुभूति से जुड़ी"),
    ("vipāka", "a", "कर्म-फल रूपी"),
    ("vipākadhammadhamma", "a+n", "कर्म-फल उत्पन्न करने वाली"),
    ("nevavipākanavipākadhammadhamma", "a+n", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली"),
    ("upādinnupādāniya", "a", "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली"),
    ("anupādinnupādāniya", "a", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली"),
    ("anupādinnaanupādāniya", "a", "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली"),
    ("saṃkiliṭṭhasaṃkilesika", "a", "क्लेशों से मलिन और क्लेशों का विषय बनने वाली"),
    ("asaṃkiliṭṭhasaṃkilesika", "a", "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली"),
    ("asaṃkiliṭṭhaasaṃkilesika", "a", "क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली"),
    ("savitakkasavicāra", "a", "आरंभिक विचार और सतत विचार वाली"),
    ("avitakkavicāramatta", "a", "आरंभिक विचार से रहित, केवल सतत विचार वाली"),
    ("avitakkaavicāra", "a", "आरंभिक विचार और सतत विचार दोनों से रहित"),
    ("pītisahagata", "a", "उल्लास के साथ होने वाली"), ("sukhasahagata", "a", "सुख के साथ होने वाली"),
    ("upekkhāsahagata", "a", "समभाव के साथ होने वाली"),
    ("dassanena pahātabba", "a", "सत्य-दर्शन से छोड़ी जाने वाली"),
    ("bhāvanāya pahātabba", "a", "मानसिक अभ्यास से छोड़ी जाने वाली"),
    ("nevadassanena nabhāvanāya pahātabba", "a", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली"),
    ("dassanena pahātabbahetuka", "a", "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली"),
    ("bhāvanāya pahātabbahetuka", "a", "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"),
    ("nevadassanena nabhāvanāya pahātabbahetuka", "a",
     "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली"),
    ("ācayagāmi", "i", "संचय की ओर ले जाने वाली"), ("apacayagāmi", "i", "संचय घटाने की ओर ले जाने वाली"),
    ("nevācayagāmināpacayagāmi", "i", "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली"),
    ("sekkha", "a", "सीखने के चरण की"), ("asekkha", "a", "सीखना पूरा होने के चरण की"),
    ("nevasekkhanāsekkha", "a", "न सीखने के चरण की, न सीखना पूरा होने के चरण की"),
    ("paritta", "a", "सीमित"), ("mahaggata", "a", "उन्नत"), ("appamāṇa", "a", "अपरिमित"),
    ("parittārammaṇa", "a", "सीमित विषय वाली"), ("mahaggatārammaṇa", "a", "उन्नत विषय वाली"),
    ("appamāṇārammaṇa", "a", "अपरिमित विषय वाली"),
    ("hīna", "a", "हीन"), ("majjhima", "a", "मध्यम"), ("paṇīta", "a", "उत्तम"),
    ("micchattaniyata", "a", "ग़लत दिशा में निश्चित"), ("sammattaniyata", "a", "सही दिशा में निश्चित"),
    ("aniyata", "a", "अनिश्चित"),
    ("maggārammaṇa", "a", "मार्ग को विषय बनाने वाली"), ("maggahetuka", "a", "मार्ग को मूल बनाने वाली"),
    ("maggādhipati", "i", "मार्ग की प्रधानता वाली"),
    ("uppanna", "a", "उत्पन्न हो चुकी"), ("anuppanna", "a", "उत्पन्न न हुई"), ("uppādi", "i", "उत्पन्न होने वाली"),
    ("atīta", "a", "अतीत की"), ("anāgata", "a", "भविष्य की"), ("paccuppanna", "a", "वर्तमान की"),
    ("atītārammaṇa", "a", "अतीत के विषय वाली"), ("anāgatārammaṇa", "a", "भविष्य के विषय वाली"),
    ("paccuppannārammaṇa", "a", "वर्तमान के विषय वाली"),
    ("ajjhatta", "a", "स्वयं से संबंधित"), ("bahiddhā", "ind", "दूसरों से संबंधित"),
    ("ajjhattabahiddhā", "ind", "स्वयं और दूसरों दोनों से संबंधित"),
    ("ajjhattārammaṇa", "a", "स्वयं से संबंधित विषय वाली"), ("bahiddhārammaṇa", "a", "दूसरों से संबंधित विषय वाली"),
    ("ajjhattabahiddhārammaṇa", "a", "स्वयं और दूसरों दोनों से संबंधित विषय वाली"),
    ("sanidassanasappaṭigha", "a", "दिखाई देने वाली और टकराव वाली"),
    ("anidassanasappaṭigha", "a", "दिखाई न देने वाली, पर टकराव वाली"),
    ("anidassanaappaṭigha", "a", "दिखाई न देने वाली और टकराव से रहित"),
    # hetugocchaka
    ("hetu", "u", "मूल रूपी"), ("sahetuka", "a", "मूल वाली"), ("ahetuka", "a", "मूल से रहित"),
    ("hetusampayutta", "a", "मूलों से जुड़ी"), ("hetuvippayutta", "a", "मूलों से अलग"),
    # cūḷantara
    ("sappaccaya", "a", "कारणों पर निर्भर रहने वाली"), ("appaccaya", "a", "कारणों पर निर्भर न रहने वाली"),
    ("saṅkhata", "a", "निर्मित"), ("asaṅkhata", "a", "अनिर्मित"),
    ("sanidassana", "a", "दिखाई देने वाली"), ("anidassana", "a", "दिखाई न देने वाली"),
    ("sappaṭigha", "a", "टकराव वाली"), ("appaṭigha", "a", "टकराव से रहित"),
    ("rūpi", "i", "भौतिक"), ("arūpi", "i", "अभौतिक"), ("lokiya", "a", "लौकिक"), ("lokuttara", "a", "लोकोत्तर"),
    ("kenaci viññeyya", "a", "किसी एक प्रकार की चेतना से जानी जा सकने वाली"),
    ("kenaci naviññeyya", "a", "किसी एक प्रकार की चेतना से न जानी जा सकने वाली"),
    # āsava and the other clusters
    ("āsava", "a", "मन के मैल रूपी"), ("sāsava", "a", "मन के मैलों का विषय बनने वाली"),
    ("anāsava", "a", "मन के मैलों का विषय न बनने वाली"), ("āsavasampayutta", "a", "मन के मैलों से जुड़ी"),
    ("āsavavippayutta", "a", "मन के मैलों से अलग"),
    ("saññojana", "a", "बंधन रूपी"), ("gantha", "a", "गाँठ रूपी"), ("ogha", "a", "बाढ़ रूपी"),
    ("yoga", "a", "जकड़न रूपी"), ("nīvaraṇa", "a", "बाधा रूपी"), ("parāmāsa", "a", "ग़लत धारणा रूपी"),
    ("upādāna", "a", "आसक्ति रूपी"), ("kilesa", "a", "मन के क्लेश रूपी"),
    ("saṃkilesika", "a", "क्लेशों का विषय बनने वाली"), ("asaṃkilesika", "a", "क्लेशों का विषय न बनने वाली"),
    ("saṃkiliṭṭha", "a", "क्लेशों से मलिन"), ("asaṃkiliṭṭha", "a", "क्लेशों से मलिन न होने वाली"),
    ("kilesasampayutta", "a", "क्लेशों से जुड़ी"), ("kilesavippayutta", "a", "क्लेशों से अलग"),
    # mahantara
    ("sārammaṇa", "a", "विषय वाली"), ("anārammaṇa", "a", "विषय से रहित"),
    ("citta", "a", "मन रूपी"), ("cetasika", "a", "मन की सहचर"), ("acetasika", "a", "मन की सहचर न होने वाली"),
    ("cittasampayutta", "a", "मन से जुड़ी"), ("cittavippayutta", "a", "मन से अलग"),
    ("cittasaṃsaṭṭha", "a", "मन से घुली-मिली"), ("cittasamuṭṭhāna", "a", "मन से उत्पन्न"),
    ("cittasahabhu", "u", "मन के साथ-साथ होने वाली"), ("cittānuparivatti", "i", "मन का अनुसरण करने वाली"),
    ("cittasaṃsaṭṭhasamuṭṭhāna", "a", "मन से घुली-मिली और मन से उत्पन्न"),
    ("cittasaṃsaṭṭhasamuṭṭhānasahabhu", "u", "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली"),
    ("cittasaṃsaṭṭhasamuṭṭhānānuparivatti", "i", "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली"),
    ("ajjhattika", "a", "आंतरिक"), ("bāhira", "a", "बाह्य"),
    ("upādā", "ind", "व्युत्पन्न"), ("upādādhamma", "a+n", "व्युत्पन्न"),
    ("upādinna", "a", "कर्म से उत्पन्न"), ("anupādinna", "a", "कर्म से उत्पन्न न होने वाली"),
    # piṭṭhi
    ("savitakka", "a", "आरंभिक विचार वाली"), ("avitakka", "a", "आरंभिक विचार से रहित"),
    ("savicāra", "a", "सतत विचार वाली"), ("avicāra", "a", "सतत विचार से रहित"),
    ("sappītika", "a", "उल्लास वाली"), ("appītika", "a", "उल्लास से रहित"),
    ("kāmāvacara", "a", "इंद्रिय-सुखों के लोक से संबंधित"), ("rūpāvacara", "a", "सूक्ष्म भौतिक लोक से संबंधित"),
    ("arūpāvacara", "a", "अभौतिक लोक से संबंधित"),
    ("pariyāpanna", "a", "अस्तित्व के लोकों में समाई हुई"), ("apariyāpanna", "a", "अस्तित्व के लोकों में न समाई हुई"),
    ("niyyānika", "a", "मुक्ति की ओर ले जाने वाली"), ("aniyyānika", "a", "मुक्ति की ओर न ले जाने वाली"),
    ("niyata", "a", "निश्चित"),
    ("sauttara", "a", "सर्वोच्च न होने वाली"), ("anuttara", "a", "सर्वोच्च"),
    ("saraṇa", "a", "संघर्ष वाली"), ("araṇa", "a", "संघर्ष से रहित"),
]
# spelling slips in the source, rendered as the word meant (listed in the notes)
SPELLING = {"anupanna": "anuppanna", "nevāsekkhanāsekkha": "nevasekkhanāsekkha", "apaccaya": "appaccaya"}
for wrong, right in SPELLING.items():
    ITEMS.append((wrong, "a", dict((s, h) for s, _, h in ITEMS)[right]))

ENDINGS = {  # class -> [(suffix replacing the final stem vowel, case, conj)]
    "a": [("aṃ", "acc", ""), ("o", "nom", ""), ("assa", "dat", ""), ("añca", "acc", "ca"),
          ("añceva", "acc", "ceva"), ("ā", "nompl", ""), ("ena", "ins", "")],
    "u": [("uṃ", "acc", ""), ("u", "nom", ""), ("ū", "nom", ""), ("ussa", "dat", ""), ("uñca", "acc", "ca"),
          ("uñceva", "acc", "ceva")],
    "i": [("iṃ", "acc", ""), ("i", "nom", ""), ("ī", "nom", ""), ("issa", "dat", ""), ("iñca", "acc", "ca"),
          ("iñceva", "acc", "ceva")],
    "ind": [("", None, ""), ("ñca", None, "ca"), ("ñceva", None, "ceva")],
}
# forms: tuple(words) -> list of (hindi, case, conj, has_noun)
FORMS = {}
for stem, cls, hi in ITEMS:
    words = stem.split(" ")
    base_cls = cls.split("+")[0]
    has_noun = cls.endswith("+n")
    last = words[-1]
    root = last if base_cls == "ind" else last[:-1]
    for suf, case, conj in ENDINGS[base_cls]:
        key = tuple(words[:-1] + [root + suf])
        FORMS.setdefault(key, []).append((hi, case, conj, has_noun))
# an odd spelling of the (Ga) item of the ācayagāmi triad in 5-05: two words
FORMS[("nevaācayagāmiṃ", "nāpacayagāmiṃ")] = [(dict((s, h) for s, _, h in ITEMS)["nevācayagāmināpacayagāmi"],
                                              "acc", "", False)]
MAXW = max(len(k) for k in FORMS)

NOUN = {"dhammaṃ": "acc", "dhammo": "nom", "dhammā": "nompl", "dhammassa": "dat"}
NEGWORD = {"na": 1, "no": 1, "nana": 2, "nano": 2}

ANOMALIES = []   # (file, line, text) collected for the slip review
CUR = {"file": "", "line": 0}


def _peel(word):
    """Yield (level, rest) for every way of peeling na/no prefixes, fewest first."""
    out, level, w = [(0, word)], 0, word
    while w.startswith(("na", "no")) and len(w) > 2:
        w = w[2:]
        level += 1
        out.append((level, w))
    return out


def match_item(toks, i):
    """Match an item at token index i. Returns dict or None."""
    if i >= len(toks) or toks[i]["kind"] != "w":
        return None
    first = toks[i]["low"]
    for level, rest in _peel(first):
        for n in range(MAXW, 0, -1):
            if i + n > len(toks) or any(t["kind"] != "w" for t in toks[i:i + n]):
                continue
            key = tuple([rest] + [t["low"] for t in toks[i + 1:i + n]])
            if key in FORMS:
                hi, case, conj, has_noun = FORMS[key][0]
                return {"level": level, "hi": hi, "case": case, "conj": conj, "noun": has_noun, "n": n}
    return None


def item_hi(m, extra=0):
    return m["hi"] + NEG * (m["level"] + extra)


def parse_phrase(toks, i):
    """Item phrase: entities (lists of Hindi parts) and its case. Returns (res, j) or None."""
    entities, cur, case, has_noun, levels = [], [], None, False, []
    j = i
    while j < len(toks):
        t = toks[j]
        if t["kind"] == "w" and t["low"] in NOUN and (cur or entities):
            case, has_noun = NOUN[t["low"]], True
            j += 1
            break
        m = match_item(toks, j)
        if not m:
            break
        j += m["n"]
        levels.append(m["level"])
        case = m["case"] or case
        has_noun = has_noun or m["noun"]
        nxt = toks[j]["low"] if j < len(toks) and toks[j]["kind"] == "w" else None
        if m["conj"] == "ceva" or nxt == "ceva":
            if nxt == "ceva":
                j += 1
            if any("भी और" in p or "पर स्वयं" in p for p in cur):
                # a second "ceva" group right after a closed one starts the next entity
                entities.append(cur)
                cur = []
            a = item_hi(m)
            t2 = toks[j] if j < len(toks) else None
            if t2 and t2["kind"] == "w" and t2["low"] in NEGWORD and j + 1 < len(toks) and \
                    (toks[j + 1]["low"] == "ca" or match_item(toks, j + 1)):
                lv = NEGWORD[t2["low"]]
                skip = 2 if toks[j + 1]["low"] == "ca" else 1
                if skip == 1:   # "nana hetussa" without "ca": read as "nana ca hetussa"
                    ANOMALIES.append((CUR["file"], CUR["line"], "neg-no-ca", [9], t2["tok"]))
                m2 = match_item(toks, j + skip)
                if not m2:
                    return None
                j += skip + m2["n"]
                levels.append(m2["level"] + lv)
                cur.append(f"{a}, पर स्वयं {item_hi(m2, lv)}")
                if m2["conj"] == "ca" or (j < len(toks) and toks[j]["low"] == "ca"):
                    # "…ñceva na ca hetuñca" / "… ceva nano ca āsavo ca": the "ca" closes the entity
                    if m2["conj"] != "ca":
                        j += 1
                    entities.append(cur)
                    cur = []
            else:
                m2 = match_item(toks, j)
                if not m2:
                    return None
                j += m2["n"]
                levels.append(m2["level"])
                if m2["conj"] != "ca":
                    if j < len(toks) and toks[j]["low"] == "ca":
                        j += 1
                    else:   # the source drops the closing "ca" ("naāsavañceva naanāsavaṃ"): read as meant
                        ANOMALIES.append((CUR["file"], CUR["line"], "ceva-no-ca", [9], toks[j - 1]["tok"]))
                cur.append(f"{item_hi(m)} भी और {item_hi(m2)} भी")
            continue
        cur.append(item_hi(m))
        if m["conj"] == "ca":
            entities.append(cur)
            cur = []
        elif nxt == "ca":
            j += 1
            entities.append(cur)
            cur = []
        mn = match_item(toks, j)
        same_case = mn and mn["case"] in (None, m["case"])
        if m["noun"] and m["conj"] == "" and nxt != "ca" and nxt not in NOUN and not same_case:
            # an item that contains its own noun ("vipākadhammadhammo") ends the phrase,
            # unless another item follows ("vipākadhammadhammaṃ nahetuṃ dhammaṃ")
            break
    if cur:
        entities.append(cur)
    if not entities:
        return None
    if case == "nompl":
        case = "nom"
    return {"ents": [", ".join(e) for e in entities], "case": case, "noun": has_noun, "levels": levels,
            "start": i, "end": j}, j


def join_and(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " और " + xs[-1]


def ph_hi(ph, case=None):
    case = case or ph["case"]
    ents = ph["ents"]
    if not ph["noun"]:
        return join_and(ents)
    if case == "nom":
        return ents[0] + " " + DH if len(ents) == 1 else join_and(ents) + " " + DH_PL
    s = join_and([e + " " + DH for e in ents])
    return s + " के लिए" if case == "dat" else s


# =====================================================================================
# 2. Tokenizer
# =====================================================================================
TOK_RX = re.compile(r"(\s*)(\{[^}]*\}|…pe…|…|[.,;:?!–—()]|[^\s.,;:?!…–—(){}]+)")
COND_ABL_RX = S._ABL_RX
COND_LOC_RX = S._LOC_RX
INS_RX = re.compile(r"^(" + "|".join(sorted(S.COND_KEYS, key=len, reverse=True)) + r")paccayena$")


def tokenize(text):
    toks = []
    for m in TOK_RX.finditer(text):
        ws, tok = m.group(1), m.group(2)
        kind = "w"
        if tok in ("…pe…", "…") or re.fullmatch(r"[.,;:?!–—()]", tok) or tok.startswith("{"):
            kind = "p"
        toks.append({"ws": ws, "tok": tok, "low": tok[0].lower() + tok[1:] if tok else tok, "kind": kind,
                     "s": m.start(2), "e": m.end(2)})
    return toks


def is_count_word(low):
    if low in S._SLIPS:
        return True
    return bool(COND_LOC_RX.match(low) or COND_ABL_RX.match(low))


def is_loc(low):
    return bool(COND_LOC_RX.match(low))


# =====================================================================================
# 3. Fixed phrase tables: explanations after "–", notes in brackets, special sentences
# =====================================================================================
VK = S.VK_SG
EXPL = {
    # 5-05
    "nahetuṃ akusalaṃ abyākataṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"मूल रूपी न होने वाले, हानिकर या नैतिक रूप से अनिर्धारित एक समूह पर निर्भर होकर तीन समूह {S.AND_CSR}",
    "nahetū akusale abyākate khandhe paṭicca hetū":
        "मूल रूपी न होने वाले, हानिकर और नैतिक रूप से अनिर्धारित समूहों पर निर्भर होकर मूल",
    "nahetuṃ kusalaṃ abyākataṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"मूल रूपी न होने वाले, हितकर या नैतिक रूप से अनिर्धारित एक समूह पर निर्भर होकर तीन समूह {S.AND_CSR}",
    "dve khandhe": "दो समूहों",
    "nahetū kusale abyākate khandhe paṭicca hetū":
        "मूल रूपी न होने वाले, हितकर और नैतिक रूप से अनिर्धारित समूहों पर निर्भर होकर मूल",
    "kusalākusalaṃ nahetuṃ ekaṃ khandhaṃ paṭicca tayo khandhā, tayo khandhe paṭicca eko khandho":
        "हितकर या हानिकर, मूल रूपी न होने वाले एक समूह पर निर्भर होकर तीन समूह, "
        "तीन समूहों पर निर्भर होकर एक समूह",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ paṭicca cittasamuṭṭhānaṃ rūpaṃ, ekaṃ mahābhūtaṃ paṭicca tayo mahābhūtā":
        "संशय के साथ होने वाले या बेचैनी के साथ होने वाले मोह पर निर्भर होकर मन से उत्पन्न भौतिक रूप, "
        "एक महाभूत पर निर्भर होकर तीन महाभूत",
    "dve mahābhūte": "दो महाभूतों",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ paṭicca sampayuttakā khandhā; paṭisandhikkhaṇe vatthuṃ paṭicca sahetukā khandhā":
        "संशय के साथ होने वाले या बेचैनी के साथ होने वाले मोह पर निर्भर होकर जुड़े हुए समूह; "
        f"{S.PATISANDHI} आधार पर निर्भर होकर मूल वाले समूह",
    # 5-10
    "hetuṃ dhammaṃ paṭicca sampayuttakā khandhā cittasamuṭṭhānañca rūpaṃ":
        f"मूल रूपी परिघटना पर निर्भर होकर जुड़े हुए समूह {S.AND_CSR}",
    # 5-09
    "kusale khandhe paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{S.KHE('हितकर')} {S.CSR}",
    "akusale khandhe paṭicca cittasamuṭṭhānaṃ rūpaṃ": f"{S.KHE('हानिकर')} {S.CSR}",
    "kusalaṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ": f"{S.KH13(S.KH_FIRST['k'])} {S.AND_CSR}",
    "akusalaṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ": f"{S.KH13(S.KH_FIRST['a'])} {S.AND_CSR}",
    "kusalaṃ ekaṃ khandhaṃ paṭicca tayo khandhā": S.KH13(S.KH_FIRST['k']),
    "vipākābyākataṃ kiriyābyākataṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"{S.KH13(S.KH_FIRST['vk'])} {S.AND_CSR}",
    "paṭisandhikkhaṇe": S.PATISANDHI,
    "ekaṃ mahābhūtaṃ paṭicca tayo mahābhūtā": S.MB13(),
    "dve mahābhūte paṭicca dve mahābhūtā, mahābhūte paṭicca cittasamuṭṭhānaṃ rūpaṃ":
        f"दो महाभूतों पर निर्भर होकर दो महाभूत, {S.MBE(S.CSR)}",
    "vipākābyākataṃ": S.VIPAKA_ABY,
    "mahābhūtaṃ": S.MAHABHUTA,
    "vipākābyākataṃ kiriyābyākataṃ": VK,
    "kusale khandhe ca mahābhūte ca paṭicca cittasamuṭṭhānaṃ rūpaṃ": S.KH_MB("हितकर"),
    "sukhāya vedanāya sampayutte khandhe paṭicca sukhavedanā cittasamuṭṭhānañca rūpaṃ":
        f"सुखद अनुभूति से जुड़े समूहों पर निर्भर होकर सुखद अनुभूति {S.AND_CSR}",
    "sukhāya vedanāya sampayuttaṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        f"सुखद अनुभूति से जुड़े एक समूह पर निर्भर होकर तीन समूह {S.AND_CSR}",
}
EXPL_KEYS = sorted(EXPL, key=len, reverse=True)


def VARA_OBL(name):            # "सह-उत्पत्ति का खंड" -> "सह-उत्पत्ति के खंड"
    return S.VARA[name].replace(" का खंड", " के खंड")


VNAME = {"sahajāta": "sahajāta", "paccaya": "paccaya", "nissaya": "nissaya", "saṃsaṭṭha": "saṃsaṭṭha",
         "sampayutta": "sampayutta", "pañhā": "pañhā", "paṭicca": "paṭicca"}


def vara_list(inner):
    """(Sahajātavārampi…pe… sampayuttavārampi [sabbattha] PRED.) -> Hindi (without the brackets)."""
    m = re.fullmatch(r"((?:(?:\w+?)vār(?:ampi|epi)(?:…pe…| )?\s*)+)(.*)", inner)
    if not m:
        return None
    names_part, pred = m.group(1), m.group(2).strip()
    parts = re.findall(r"(\w+?)vār(ampi|epi)(…pe…)?", names_part)
    if not parts:
        return None
    case = parts[0][1]
    dot = pred.endswith(".")
    pred = pred.rstrip(".")
    words = []
    for nm, cs, pe in parts:
        nm = nm[0].lower() + nm[1:]
        if nm not in VNAME:
            return None
        if cs == "epi":   # -vārepi (locative)
            w = f"{VARA_OBL(nm)} में भी"
        elif pred in ("vitthāretabbaṃ", "sabbattha vitthāretabbaṃ", "paṭiccavārasadisaṃ vitthāretabbaṃ"):
            w = f"{VARA_OBL(nm)} का भी"
        else:
            w = f"{S.VARA[nm]} भी"
        words.append(w + ("…" if pe else ""))
    s = " ".join(words)
    pred_hi = {
        "vitthāretabbaṃ": "विस्तार करना चाहिए",
        "sabbattha vitthāretabbaṃ": "हर जगह विस्तार करना चाहिए",
        "paṭiccavārasadisaṃ": f"{VARA_OBL('paṭicca')} के समान है",
        "paṭiccavārasadisaṃ vitthāretabbaṃ": f"{VARA_OBL('paṭicca')} के समान विस्तार करना चाहिए",
        "vitthāro": "विस्तार",
        "sabbattha vitthāro": "हर जगह विस्तार",
        "sabbattha nava": "हर जगह नौ",
    }.get(pred)
    if pred_hi is None:
        return None
    return f"{s} {pred_hi}" + ("।" if dot else "")


def TIKA_OBL(x):
    return f"{x} वाले तीन के वर्गीकरण"


def DUKA_OBL(x):
    return f"{x} वाले दो के वर्गीकरण"


ABY_MULA = "नैतिक रूप से अनिर्धारित से शुरू होने वाली शृंखला में"
PAREN = {
    "Saṃkhittaṃ.": "संक्षिप्त।", "Saṃkhittaṃ": "संक्षिप्त", "saṃkhittaṃ.": "संक्षिप्त।", "saṃkhittaṃ": "संक्षिप्त",
    "Sabbattha vitthāro.": "हर जगह विस्तार।", "sabbattha vitthāro": "हर जगह विस्तार",
    "Sabbattha vitthāretabbaṃ.": "हर जगह विस्तार करना चाहिए।",
    "Sabbattha nava.": "हर जगह नौ।", "Sabbattha nava": "हर जगह नौ", "sabbattha nava.": "हर जगह नौ।",
    "Sabbattha ekaṃ.": "हर जगह एक।", "Sabbattha ekavīsa.": "हर जगह इक्कीस।", "Sabbattha pañca.": "हर जगह पाँच।",
    "sabbattha nava, vipākaṃ natthi": f"हर जगह नौ, {S.NAME('vipāka')} नहीं है",
    "Pañhāvāraṃ evaṃ vitthāretabbaṃ.": "प्रश्नों के खंड का इसी तरह विस्तार करना चाहिए।",
    "Pañhāvāraṃ evaṃ vitthāretabbaṃ": "प्रश्नों के खंड का इसी तरह विस्तार करना चाहिए",
    "Pañhāvāraṃ vitthāretabbaṃ.": "प्रश्नों के खंड का विस्तार करना चाहिए।",
    "Pañhāvārampi vitthāretabbaṃ.": "प्रश्नों के खंड का भी विस्तार करना चाहिए।",
    "Pañhāvārampi evaṃ vitthāretabbaṃ.": "प्रश्नों के खंड का भी इसी तरह विस्तार करना चाहिए।",
    "Vitthāretabbaṃ.": "विस्तार करना चाहिए।",
    "Pañhāvāre na sadisaṃ.": "प्रश्नों के खंड में समान नहीं है।",
    "Piṭṭhidukaṃ vitthāretabbaṃ.": "अंतिम दो-दो के वर्गीकरणों का विस्तार करना चाहिए।",
    "Abyākatamūlaṃ dve.": f"{ABY_MULA} दो।", "Abyākatamūle dve.": f"{ABY_MULA} दो।",
    "Abyākatamūlaṃ ekaṃyeva.": f"{ABY_MULA} एक ही।", "Abyākatamūlaṃ tīṇiyeva.": f"{ABY_MULA} तीन ही।",
    "Abyākatamūlaṃ tīṇiyeva paccayavasena.": f"{ABY_MULA} कारणों के अनुसार तीन ही।",
    "Abyākatavāre sabbattha paccayavasena gaṇetabbaṃ.":
        "नैतिक रूप से अनिर्धारित वाले खंड में हर जगह कारणों के अनुसार गिनना चाहिए।",
    "Akusalaṃ kusalasadisaṃ.": "हानिकर हितकर के समान है।",
    "Akusalaṃ tīṇi kātabbaṃ, abyākataṃ tīṇi kātabbaṃ.":
        "हानिकर के तीन बनाने चाहिए, नैतिक रूप से अनिर्धारित के तीन बनाने चाहिए।",
    "Anāgato atītasadiso.": "भविष्य की परिघटना अतीत की परिघटना के समान है।",
    "Asaṅkhataṃ appaccayasadisaṃ.": "“अनिर्मित” पद “कारणों पर निर्भर न रहने वाली” पद के समान है।",
    "Saṅkhataṃ sappaccayasadisaṃ.": "“निर्मित” पद “कारणों पर निर्भर रहने वाली” पद के समान है।",
    "saṃkhittaṃ sappaccayasadisaṃ": "संक्षिप्त, “कारणों पर निर्भर रहने वाली” पद के समान",
    "Cha pañhā.": "छह प्रश्न।", "Cha pañhā, saṃkhittaṃ.": "छह प्रश्न, संक्षिप्त।",
    "Pañca pañhā.": "पाँच प्रश्न।", "pañca pañhā": "पाँच प्रश्न",
    "cha pañhā kātabbā": "छह प्रश्न बनाने चाहिए", "Nava pañhā kātabbā.": "नौ प्रश्न बनाने चाहिए।",
    "Cittasamuṭṭhānarūpameva ettha vattati, ekūnavīsati pañhā kātabbā.":
        "यहाँ मन से उत्पन्न भौतिक रूप ही लागू होता है, उन्नीस प्रश्न बनाने चाहिए।",
    "Ekapañhameva. Etena upāyena kusalākusaladukaṃ kusalattikameva ettha vaṭṭati.":
        f"केवल एक प्रश्न। इसी उपाय से यहाँ {S.DUKA('हितकर-हानिकर')}, यानी {S.TIKA('हितकर')} ही लागू होता है।",
    "Ekaṃ.": "एक।", "Nava.": "नौ।", "nava": "नौ", "tīṇi": "तीन",
    "Ete saṃkhittā, dukattayaṃ cittadukasadisaṃ.":
        f"ये संक्षिप्त हैं, ये तीन दो-दो के वर्गीकरण {DUKA_OBL('मन')} के समान हैं।",
    "Etena upāyena kenaci naviññeyye ekūnavīsati pañhā kātabbā.":
        "इसी उपाय से “किसी एक प्रकार की चेतना से न जानी जा सकने वाली” में उन्नीस प्रश्न बनाने चाहिए।",
    "Etena upāyena nava pañhā kātabbā.": "इसी उपाय से नौ प्रश्न बनाने चाहिए।",
    "Hetuhetusampayuttadukaṃ hetusahetukadukasadisaṃ.":
        f"{S.DUKA('मूल और मूलों से जुड़ाव')} {DUKA_OBL('मूल और मूल-सहित')} के समान है।",
    "Hetusampayuttadukaṃ sahetukadukasadisaṃ.":
        f"{S.DUKA('मूलों से जुड़ाव')} {DUKA_OBL('मूल-सहित')} के समान है।",
    "Sahetukadukasadisaṃ.": f"{DUKA_OBL('मूल-सहित')} के समान है।",
    "Nanocittapadaṃ na labbhati.": "“मन रूपी न होने वाली न होने वाली” पद नहीं मिलता।",
    "saṃkhittaṃ, nanocittapadaṃ na labbhati": "संक्षिप्त, “मन रूपी न होने वाली न होने वाली” पद नहीं मिलता",
    "saṃkhittaṃ, cittadukasadisaṃ": f"संक्षिप्त, {DUKA_OBL('मन')} के समान",
    "Paccanīyaṃ vitthāretabbaṃ. Sahajātavārampi paccayavārampi vitthāretabbaṃ. Paccayavārepi hetuyā chabbīsa, "
    "ārammaṇe aṭṭhārasa…pe… avigate chabbīsa. Nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi paṭiccavārasadisaṃ.":
        f"नकारात्मक क्रम का विस्तार करना चाहिए। {VARA_OBL('sahajāta')} का भी, {VARA_OBL('paccaya')} का भी "
        f"विस्तार करना चाहिए। {VARA_OBL('paccaya')} में भी मूल-कारण में छब्बीस, विषय-कारण में अठारह… "
        f"अविलीनता-कारण में छब्बीस। {S.VARA['nissaya']} भी, {S.VARA['saṃsaṭṭha']} भी, {S.VARA['sampayutta']} भी "
        f"{VARA_OBL('paṭicca')} के समान है।",
    "Saṃkhittaṃ, hetuhetusampayuttadukaṃ hetusahetukadukasadisaṃ. Saṃkhittaṃ. Nava pañhā.":
        f"संक्षिप्त, {S.DUKA('मूल और मूलों से जुड़ाव')} {DUKA_OBL('मूल और मूल-सहित')} के समान है। "
        f"संक्षिप्त। नौ प्रश्न।",
    "Saṃkhittaṃ. Pañca": "संक्षिप्त। पाँच", "Saṃkhittaṃ. Sabbattha ekaṃ.": "संक्षिप्त। हर जगह एक।",
    "Saṃkiliṭṭhasaṃkilesikattikasadisaṃ.": f"{TIKA_OBL('क्लेशों से मलिनता')} के समान है।",
    "Yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, "
    "evaṃ gaṇetabbaṃ.":
        f"जैसे {TIKA_OBL('हितकर')} में प्रश्नों के खंड का सकारात्मक क्रम भी, नकारात्मक क्रम भी, "
        "सकारात्मक-नकारात्मक क्रम भी और नकारात्मक-सकारात्मक क्रम भी गिना गया है, वैसे ही गिनना चाहिए।",
    "Yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ.":
        f"जैसे {TIKA_OBL('हितकर')} में प्रश्नों का खंड है, वैसे ही विस्तार करना चाहिए।",
    "Yathā kusalattike pañhāvāraṃ, evaṃ vitthāretabbaṃ.":
        f"जैसे {TIKA_OBL('हितकर')} में प्रश्नों का खंड है, वैसे ही विस्तार करना चाहिए।",
    "Yāva pañhāvārepi ekaṃ.": "प्रश्नों के खंड तक भी एक।",
    "cittasamuṭṭhānameva, ārammaṇaṃ natthi": f"मन से उत्पन्न ही, {S.NAME('ārammaṇa')} नहीं है",
    "lokiyadukasadisaṃ": f"{DUKA_OBL('लौकिक')} के समान",
    "mahābhūtā natthi": "महाभूत नहीं हैं",
    "Āsavagocchakasadisaṃ.": "मन के मैलों के वर्ग के समान है।",
    "Āsavaāsavasampayuttadukaṃ āsavasāsavadukasadisaṃ.":
        f"{S.DUKA('मन के मैल और उनसे जुड़ाव')} {DUKA_OBL('मन के मैल और उनका विषय बनने')} के समान है।",
}
BRACE = {
    "{ito paṭṭhāya yāva ajjhattārammaṇattikā sabbapotthakesu akusalābyākatapadāni na dissanti, "
    "vedanāttika sanidassanattikesu viya nanu tehipi bhavitabbaṃ}":
        "[यहाँ से लेकर स्वयं और दूसरों से संबंधित विषय वाले तीन के वर्गीकरण तक सभी पोथियों में हानिकर और "
        "नैतिक रूप से अनिर्धारित पद दिखाई नहीं देते, अनुभूति वाले और दिखाई देने वाले तीन के वर्गीकरणों की तरह "
        "निश्चय ही उनमें भी ये होने चाहिए]",
    "{ayaṃ saṅkhyā vicāretabbā, nalokiyanalokuttaradhammo nāma natthi}":
        "[इस गणना की जाँच करनी चाहिए, लौकिक न होने वाली और लोकोत्तर न होने वाली परिघटना नाम की कोई चीज़ नहीं है]",
    "{hetuyā aṭṭha?}": "[मूल-कारण में आठ?]",
}
DPACC_OBL = S.DHAMMAPACCANIYA.replace("परिघटनाओं का", "परिघटनाओं के")              # Dhammapaccanīye
DANUPACC_OBL = S.DHAMMANULOMAPACCANIYA.replace("परिघटनाओं का", "परिघटनाओं के")     # Dhammānulomapaccanīye
NITTHITA = {  # "X niṭṭhitaṃ." lines
    "Dhammapaccanīye dukatikapaṭṭhānaṃ niṭṭhitaṃ.": f"{DPACC_OBL} में {S.DUKATIKAPATTHANA} पूरे हुए।",
    "Dhammapaccanīye tikadukapaṭṭhānaṃ niṭṭhitaṃ.": f"{DPACC_OBL} में {S.TIKADUKAPATTHANA} पूरे हुए।",
    "Dhammapaccanīye tikatikapaṭṭhānaṃ niṭṭhitaṃ.": f"{DPACC_OBL} में {S.TIKATIKAPATTHANA} पूरे हुए।",
    "Dhammapaccanīye dukadukapaṭṭhānaṃ niṭṭhitaṃ.": f"{DPACC_OBL} में {S.DUKADUKAPATTHANA} पूरे हुए।",
    "Paccanīyapaṭṭhānaṃ niṭṭhitaṃ.": f"{S.PACCANIYA} के कारण-संबंध पूरे हुए।",
    "Dhammānulomapaccanīye tikapaṭṭhānaṃ niṭṭhitaṃ.": f"{DANUPACC_OBL} में {S.TIKAPATTHANA} पूरे हुए।",
    "Dhammānulomapaccanīye dukapaṭṭhānaṃ niṭṭhitaṃ.": f"{DANUPACC_OBL} में {S.DUKAPATTHANA} पूरे हुए।",
    "Dhammānulomapaccanīye dukatikapaṭṭhānaṃ niṭṭhitaṃ.": f"{DANUPACC_OBL} में {S.DUKATIKAPATTHANA} पूरे हुए।",
    "Dhammānulomapaccanīye tikadukapaṭṭhānaṃ niṭṭhitaṃ.": f"{DANUPACC_OBL} में {S.TIKADUKAPATTHANA} पूरे हुए।",
    "Kusalattikapiṭṭhidukaṃ niṭṭhitaṃ.": f"{S.TIKA('हितकर')} और अंतिम दो-दो के वर्गीकरण पूरे हुए।",
    "Hetugocchakaṃ niṭṭhitaṃ.": "मूलों का वर्ग पूरा हुआ।",
    "Cūḷantaradukaṃ niṭṭhitaṃ.": "बीच के छोटे दो-दो के वर्गीकरण पूरे हुए।",
    "Āsavagocchakaṃ niṭṭhitaṃ.": "मन के मैलों का वर्ग पूरा हुआ।",
    "Mahantaradukaṃ niṭṭhitaṃ.": "बीच के बड़े दो-दो के वर्गीकरण पूरे हुए।",
}
SPECIAL = {   # exact Pāli sentence (as in the source) -> Hindi, where the frames do not fit
    # 5-12: short count remarks with an instrumental or a neuter plural
    "Akusalena tīṇiyeva.": "हानिकर के साथ तीन ही।",
    "Abyākatena tīṇiyeva.": "नैतिक रूप से अनिर्धारित के साथ तीन ही।",
    "Kusalaṃ appaṭighena tīṇi.": "टकराव से रहित के साथ हितकर के तीन।",
    "Akusalaṃ appaṭighena tīṇi.": "टकराव से रहित के साथ हानिकर के तीन।",
    "Abyākataṃ appaṭighena tīṇi.": "टकराव से रहित के साथ नैतिक रूप से अनिर्धारित के तीन।",
    "Kusalaṃ appaṭighañca abyākataṃ appaṭighañca tīṇi.":
        "हितकर, टकराव से रहित और नैतिक रूप से अनिर्धारित, टकराव से रहित के तीन।",
    "Akusalaṃ appaṭighañca abyākataṃ appaṭighañca tīṇi.":
        "हानिकर, टकराव से रहित और नैतिक रूप से अनिर्धारित, टकराव से रहित के तीन।",
    "Abyākatāni tīṇi.": "नैतिक रूप से अनिर्धारित के तीन।",
    "Acetasikāni nava.": "मन की सहचर न होने वाली के नौ।",
    "Cittavippayutte tīṇi.": "मन से अलग में तीन।",
}

# =====================================================================================
# 4. Headings
# =====================================================================================
TIKA_KEY = {
    "kusala": "हितकर", "vedanā": "अनुभूति", "vedana": "अनुभूति", "vipāka": "कर्म-फल", "upādinna": "कर्म से उत्पन्न होने",
    "saṃkiliṭṭha": "क्लेशों से मलिनता", "vitakka": "आरंभिक विचार", "pīti": "उल्लास", "dassana": "सत्य-दर्शन",
    "dassanahetu": "सत्य-दर्शन से छोड़े जाने वाले मूलों", "ācayagāmi": "संचय", "ācayagāma": "संचय",
    "sekkha": "सीखने के चरण", "paritta": "सीमित", "parittārammaṇa": "सीमित विषय", "hīna": "हीन",
    "micchatta": "ग़लत दिशा में निश्चितता", "micchattaniyata": "ग़लत दिशा में निश्चितता",
    "maggārammaṇa": "मार्ग को विषय बनाने", "uppanna": "उत्पत्ति", "atīta": "अतीत",
    "atītārammaṇa": "अतीत के विषय", "ajjhatta": "स्वयं और दूसरों",
    "ajjhattārammaṇa": "स्वयं और दूसरों से संबंधित विषय", "sanidassana": "दिखाई देने",
}
DUKA_KEY = {
    "hetu": "मूल", "hetv": "मूल", "sahetuka": "मूल-सहित", "hetusampayutta": "मूलों से जुड़ाव",
    "hetusahetuka": "मूल और मूल-सहित", "hetuhetusampayutta": "मूल और मूलों से जुड़ाव",
    "nahetusahetuka": "मूल रूपी न होने पर मूल-सहित",
    "sappaccaya": "कारणों पर निर्भरता", "saṅkhata": "निर्मित", "sanidassana": "दिखाई देने",
    "sappaṭigha": "टकराव", "rūpī": "भौतिक", "lokiya": "लौकिक",
    "kenaciviññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने",
    "āsava": "मन के मैल", "sāsava": "मन के मैलों का विषय बनने", "āsavasampayutta": "मन के मैलों से जुड़ाव",
    "āsavasāsava": "मन के मैल और उनका विषय बनने", "āsavaāsavasampayutta": "मन के मैल और उनसे जुड़ाव",
    "āsavavippayuttasāsava": "मन के मैलों से अलग, पर उनका विषय बनने",
    "saññojana": "बंधन", "parāmāsa": "ग़लत धारणा", "upādāna": "आसक्ति", "kilesa": "मन के क्लेश",
    "sārammaṇa": "विषय", "citta": "मन", "cetasika": "मन की सहचर", "cittasampayutta": "मन से जुड़ाव",
    "cittasaṃsaṭṭha": "मन से घुले-मिले होने", "cittasamuṭṭhāna": "मन से उत्पत्ति",
    "cittasahabhū": "मन के साथ-साथ होने", "cittānuparivatti": "मन का अनुसरण करने",
    "cittānuparivatta": "मन का अनुसरण करने",
    "cittasaṃsaṭṭhasamuṭṭhāna": "मन से घुले-मिले होने और मन से उत्पत्ति",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhū": "मन से घुले-मिले होने, मन से उत्पत्ति और मन के साथ-साथ होने",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुले-मिले होने, मन से उत्पत्ति और मन का अनुसरण करने",
    "ajjhattika": "आंतरिक", "ajjhatta": "आंतरिक", "upādā": "व्युत्पन्न", "upādinna": "कर्म से उत्पन्न होने",
    "dassanenapahātabba": "सत्य-दर्शन से छोड़े जाने", "bhāvanāyapahātabba": "मानसिक अभ्यास से छोड़े जाने",
    "dassanenapahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "bhāvanāyapahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों",
    "dassana": "सत्य-दर्शन से छोड़े जाने",
    "savitakka": "आरंभिक विचार", "savicāra": "सतत विचार", "sappītika": "उल्लास",
    "pītisahagata": "उल्लास के साथ होने", "sukhasahagata": "सुख के साथ होने",
    "upekkhāsahagata": "समभाव के साथ होने", "kāmāvacara": "इंद्रिय-सुखों के लोक",
    "rūpāvacara": "सूक्ष्म भौतिक लोक", "arūpāvacara": "अभौतिक लोक", "pariyāpanna": "अस्तित्व के लोकों में समाने",
    "niyyānika": "मुक्ति की ओर ले जाने", "niyata": "निश्चितता", "sauttara": "सर्वोच्च न होने",
    "saraṇa": "संघर्ष", "kusalākusala": "हितकर-हानिकर",
}
GOCCHA_KEY = {"hetu": "मूलों का वर्ग", "āsava": "मन के मैलों का वर्ग", "saññojana": "बंधनों का वर्ग",
              "kilesa": "मन के क्लेशों का वर्ग", "upādāna": "आसक्ति का वर्ग"}
DUKA_SPECIAL = {"cūḷantara": "बीच के छोटे दो-दो के वर्गीकरण", "mahantara": "बीच के बड़े दो-दो के वर्गीकरण",
                "piṭṭhi": "अंतिम दो-दो के वर्गीकरण"}
HEAD_FIXED = {
    "Paṭiccavārādi": f"{S.VARA['paṭicca']} आदि", "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Hetupaccayo": S.NAME("hetu"), "Ārammaṇapaccayo": S.NAME("ārammaṇa"),
    "Nahetupaccayo": S.NNAME("hetu"), "Naārammaṇapaccayo": S.NNAME("ārammaṇa"),
    "Hetu-ārammaṇapaccayā": f"{S.NAME('hetu')} और {S.NAME('ārammaṇa')}",
    "Nahetu-naārammaṇapaccayā": f"{S.NNAME('hetu')} और {S.NNAME('ārammaṇa')}",
    "Paccanīyaṃ": S.PACCANIYA, "Paccayānulomaṃ": S.PACCAYANULOMA, "Pañhāvāro": S.VARA["pañhā"],
    "Paccayavāro": S.VARA["paccaya"], "Paccanīyuddhāro": f"{S.PACCANIYA} के लिए चयन",
    "Kusalapadaṃ": "हितकर पद", "Akusalapadaṃ": "हानिकर पद", "Abyākatapadaṃ": "नैतिक रूप से अनिर्धारित पद",
    "Tatiyapadaṃ": "तीसरा पद", "Dukkhāyavedanāyasampayuttapadaṃ": "दुःखद अनुभूति से जुड़ा पद",
    "Dhammapaccanīye dukatikapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYA}: {S.DUKATIKAPATTHANA}",
    "Dhammapaccanīye tikadukapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYA}: {S.TIKADUKAPATTHANA}",
    "Dhammapaccanīye tikatikapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYA}: {S.TIKATIKAPATTHANA}",
    "Dhammapaccanīye dukadukapaṭṭhānaṃ": f"{S.DHAMMAPACCANIYA}: {S.DUKADUKAPATTHANA}",
    "Dhammānulomapaccanīye tikapaṭṭhānaṃ": f"{S.DHAMMANULOMAPACCANIYA}: {S.TIKAPATTHANA}",
    "Dhammānulomapaccanīye dukapaṭṭhānaṃ": f"{S.DHAMMANULOMAPACCANIYA}: {S.DUKAPATTHANA}",
    "Dhammānulomapaccanīye dukatikapaṭṭhānaṃ": f"{S.DHAMMANULOMAPACCANIYA}: {S.DUKATIKAPATTHANA}",
    "Dhammānulomapaccanīye tikadukapaṭṭhānaṃ": f"{S.DHAMMANULOMAPACCANIYA}: {S.TIKADUKAPATTHANA}",
}
COMP_FIXED = {
    "chagocchakāni": "छह वर्ग", "chagocchakadukāni": "छह वर्गों के दो-दो के वर्गीकरण",
    "dvigocchakāni": "दो वर्ग", "parāmāsadukāni": f"ग़लत धारणा वाले दो के वर्गीकरण",
}


def comp_name(c):
    low = c[0].lower() + c[1:]
    if low in COMP_FIXED:
        return COMP_FIXED[low]
    m = re.fullmatch(r"(.+?)(ādi)?(ttik(?:aṃ|āni|a)?|duk(?:aṃ|āni|a)?|gocchak(?:aṃ|āni|a)?)(ādi)?", low)
    if not m:
        raise ValueError(f"heading component? {c!r}")
    base, adi1, kind, adi2 = m.groups()
    if adi1 and base == "hetv":              # hetv-ādi
        base = base[:-1] + "u"
    elif adi1 and base[-1] not in "aāiīuū":  # vipāk-ādi = vipāka + ādi
        base += "a"
    adi = " आदि" if (adi1 or adi2) else ""
    if kind.startswith("ttik"):
        return S.TIKA(TIKA_KEY[base]) + adi
    if kind.startswith("gocchak"):
        return GOCCHA_KEY[base] + adi
    if base in DUKA_SPECIAL:
        return DUKA_SPECIAL[base] + adi
    return S.DUKA(DUKA_KEY[base]) + adi


def heading_hi(text):
    if text in HEAD_FIXED:
        return HEAD_FIXED[text]
    m = re.fullmatch(r"(\d+(?:-\d+)*\.?)\s+(.+)", text)
    num, rest = (m.group(1) + " ", m.group(2)) if m else ("", text)
    if rest in HEAD_FIXED:
        return num + HEAD_FIXED[rest]
    return num + " और ".join(comp_name(c) for c in rest.split("-"))


# =====================================================================================
# 5. Sentence translator
# =====================================================================================
DEPW = {"paṭicca": "पर निर्भर होकर", "paccayā": "के कारण"}


def verb_hi(plural):
    return "उत्पन्न होती हैं" if plural else "उत्पन्न होती है"


def count_span(toks, i, text):
    """Collect a counting span from token i; returns (hindi, j) or None."""
    j = i
    seen_loc = False
    while j < len(toks):
        t = toks[j]
        low = t["low"]
        if t["kind"] == "w":
            if low == "na" and j + 1 < len(toks) and is_loc(toks[j + 1]["low"]):
                j += 1
                continue
            if is_count_word(low):
                seen_loc = seen_loc or is_loc(low) or low in S._SLIPS
                j += 1
                continue
            if low in S.NUM and j > i:
                j += 1
                continue
            break
        if t["tok"] in (",", "…pe…", "…"):
            j += 1
            continue
        if t["tok"] == ".":
            j += 1
            break
        break
    while j > i and toks[j - 1]["tok"] == ",":
        j -= 1
    if not seen_loc or j - i < 2:
        return None
    raw = text[toks[i]["s"]:toks[j - 1]["e"]]
    return S.count_hi(raw), j


def paren_inner(inner):
    if re.fullmatch(r"\d+", inner):
        return inner
    if inner in PAREN:
        return PAREN[inner]
    v = vara_list(inner)
    if v is not None:
        return v
    parts = re.split(r"(?<=\.) ", inner)
    if len(parts) > 1:
        hs = [PAREN.get(p) or vara_list(p) for p in parts]
        if all(hs):
            return " ".join(hs)
    return translate(inner)


def translate(text):
    """Translate one line body (no heading marks, no block ID)."""
    if text in NITTHITA:
        return NITTHITA[text]
    toks = tokenize(text)
    out = []
    i = 0
    while i < len(toks):
        t = toks[i]
        ws = t["ws"]
        rest = text[t["s"]:]
        # special sentences
        hit = next((k for k in SPECIAL if rest.startswith(k)), None)
        if hit:
            out.append(ws + SPECIAL[hit])
            end = t["s"] + len(hit)
            while i < len(toks) and toks[i]["s"] < end:
                i += 1
            continue
        # explanations / fixed phrases
        low_rest = rest[0].lower() + rest[1:]
        hit = next((k for k in EXPL_KEYS if low_rest.startswith(k) and
                    (len(low_rest) == len(k) or not re.match(r"\w", low_rest[len(k)]))), None)
        if hit:
            out.append(ws + EXPL[hit])
            end = t["s"] + len(hit)
            while i < len(toks) and toks[i]["s"] < end:
                i += 1
            continue
        if t["tok"].startswith("{"):
            out.append(ws + BRACE[t["tok"]])
            i += 1
            continue
        if t["tok"] == "(":
            depth, j = 0, i
            while j < len(toks):
                if toks[j]["tok"] == "(":
                    depth += 1
                elif toks[j]["tok"] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            inner = text[t["e"]:toks[j]["s"]]
            hi = paren_inner(inner)
            out.append(ws + "(" + hi + ")")
            i = j + 1
            continue
        if t["kind"] == "p":
            out.append(ws + {"…pe…": "…", ".": "।"}.get(t["tok"], t["tok"]))
            i += 1
            continue
        low = t["low"]
        # counting span
        if is_count_word(low) or (low == "na" and i + 1 < len(toks) and is_loc(toks[i + 1]["low"])):
            cs = count_span(toks, i, text)
            if cs:
                hi, i = cs
                out.append(ws + hi)
                continue
        # a bare number word ("… tīṇi.", "Pañca.") or "pañhā" ("… satta pañhā.")
        if low in S.NUM or low == "pañhā":
            out.append(ws + (S.NUM[low] if low in S.NUM else "प्रश्न"))
            i += 1
            continue
        # item phrases and frames
        pr = parse_phrase(toks, i)
        if pr:
            ph, j = pr
            nxt = toks[j]["low"] if j < len(toks) and toks[j]["kind"] == "w" else None
            if ph["case"] == "acc" and nxt in DEPW:
                ANOMALIES.append((CUR["file"], CUR["line"], "obj", ph["levels"], text[toks[i]["s"]:toks[j]["e"]]))
                s = f"{ph_hi(ph)} {DEPW[nxt]}"
                j += 1
                pr2 = parse_phrase(toks, j)
                if pr2 and pr2[0]["case"] == "nom":
                    ph2, k = pr2
                    ANOMALIES.append((CUR["file"], CUR["line"], "res", ph2["levels"],
                                      text[toks[j]["s"]:toks[k - 1]["e"]]))
                    res = ph_hi(ph2, "nom")
                    plural = len(ph2["ents"]) > 1
                    vt = toks[k]["low"] if k < len(toks) else None
                    if vt == "ca" and k + 1 < len(toks) and toks[k + 1]["low"] in ("uppajjati", "uppajjanti"):
                        # source slip "… dhammo ca uppajjati": the stray "ca" is left out
                        ANOMALIES.append((CUR["file"], CUR["line"], "stray-ca", [9], "dhammo ca uppajjati"))
                        k += 1
                        vt = toks[k]["low"]
                    if vt in ("uppajjati", "uppajjanti"):
                        k += 1
                        conds = []
                        while k < len(toks) and toks[k]["kind"] == "w" and COND_ABL_RX.match(toks[k]["low"]):
                            mm = COND_ABL_RX.match(toks[k]["low"])
                            conds.append(("-" if mm.group(1) else "") + mm.group(2))
                            k += 1
                        c = (S.CH(*conds) + " ") if conds else ""
                        s += f"{toks[j]['ws']}{res} {c}{verb_hi(plural or vt == 'uppajjanti')}"
                    else:
                        s += f"{toks[j]['ws']}{res}"
                    j = k
                out.append(ws + s)
                i = j
                continue
            if ph["case"] == "nom" and j < len(toks) and toks[j]["low"] in ("uppajjati", "uppajjanti"):
                # a result phrase after an elision ("…pe… nakusalo … dhammā uppajjanti hetupaccayā")
                ANOMALIES.append((CUR["file"], CUR["line"], "res", ph["levels"], text[toks[i]["s"]:toks[j - 1]["e"]]))
                vt = toks[j]["low"]
                k = j + 1
                conds = []
                while k < len(toks) and toks[k]["kind"] == "w" and COND_ABL_RX.match(toks[k]["low"]):
                    mm = COND_ABL_RX.match(toks[k]["low"])
                    conds.append(("-" if mm.group(1) else "") + mm.group(2))
                    k += 1
                c = (S.CH(*conds) + " ") if conds else ""
                out.append(ws + f"{ph_hi(ph, 'nom')} {c}{verb_hi(len(ph['ents']) > 1 or vt == 'uppajjanti')}")
                i = k
                continue
            if ph["case"] == "nom":
                pr2 = parse_phrase(toks, j)
                if pr2 and pr2[0]["case"] == "dat":
                    ph2, k = pr2
                    ANOMALIES.append((CUR["file"], CUR["line"], "src", ph["levels"],
                                      text[toks[i]["s"]:toks[j - 1]["e"]]))
                    ANOMALIES.append((CUR["file"], CUR["line"], "dst", ph2["levels"],
                                      text[toks[j]["s"]:toks[k - 1]["e"]]))
                    verb = "होती हैं" if len(ph["ents"]) > 1 else "होती है"
                    s = f"{ph_hi(ph, 'nom')}, {ph_hi(ph2, 'dat')}"
                    # one or more "Xpaccayena paccayo" (comma-separated)
                    first = True
                    while k + 1 < len(toks) and INS_RX.match(toks[k]["low"]) and toks[k + 1]["low"] == "paccayo":
                        kk = INS_RX.match(toks[k]["low"]).group(1)
                        s += ("" if first else ",") + f" {S.INS(kk)} {verb}"
                        first = False
                        k += 2
                        if k + 2 < len(toks) and toks[k]["tok"] == "," and INS_RX.match(toks[k + 1]["low"] or ""):
                            k += 1
                    out.append(ws + s)
                    i = k
                    continue
            out.append(ws + ph_hi(ph))
            i = j
            continue
        raise ValueError(f"cannot translate at {rest[:80]!r}  [in: {text[:120]!r}]")
    return "".join(out).strip()


# =====================================================================================
# 6. Files
# =====================================================================================
ID_RX = S.ID_RX


def build_file(fname):
    ptext = (PALI_DIR / fname).read_text(encoding="utf-8")
    hi_lines = []
    n = 0
    for line in ptext.splitlines():
        if not line.strip():
            continue
        n += 1
        CUR["file"], CUR["line"] = fname, n
        body = ID_RX.sub("", line).rstrip()
        hashes = len(body) - len(body.lstrip("#"))
        body = body[hashes:].strip()
        try:
            hi = heading_hi(body) if hashes else translate(body)
        except (ValueError, KeyError) as e:
            if "--collect" in sys.argv:
                print(f"FAIL {fname} line {n}: {str(e)[:160]}")
                hi = "FAIL"
            else:
                raise SystemExit(f"{fname} line {n}: {e}\n  {body[:200]}")
        hi_lines.append(("#" * hashes + " " + hi) if hashes else hi)
    return S.assemble(ptext, hi_lines)


NOTE_5_07 = ("{ito paṭṭhāya yāva ajjhattārammaṇattikā sabbapotthakesu akusalābyākatapadāni na dissanti, "
             "vedanāttika sanidassanattikesu viya nanu tehipi bhavitabbaṃ}")


def init_special():
    """Sentences the frames cannot compose directly (built from the frames, then adjusted)."""
    # 5-07: an editorial note in braces sits inside the item phrase, before "dhammaṃ"
    hi = translate("Naupādinnupādāniyaṃ nakusalaṃ dhammaṃ paṭicca")
    SPECIAL[f"Naupādinnupādāniyaṃ nakusalaṃ {NOTE_5_07} dhammaṃ paṭicca"] = \
        hi.replace(f" {DH} पर निर्भर होकर", f" {BRACE[NOTE_5_07]} {DH} पर निर्भर होकर")


def main():
    init_special()
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    for f in FILES:
        if only and not any(f.startswith(o) for o in only):
            continue
        text = build_file(f)
        with open(HI_DIR / f, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print("wrote", f)
    if "--report" in sys.argv:
        rep = []
        for fname, line, role, levels, txt in ANOMALIES:
            pacc = fname.startswith(("5-05", "5-06", "5-07", "5-08"))
            if pacc:
                bad = any(lv == 0 for lv in levels)
            else:
                bad = (role in ("obj", "src") and any(lv for lv in levels)) or \
                      (role in ("res", "dst") and any(lv == 0 for lv in levels))
            if bad:
                rep.append(f"{fname}\t{line}\t{role}\t{levels}\t{txt}")
        (HERE / "anomalies_5-05_5-12.txt").write_text("\n".join(rep) + "\n", encoding="utf-8")
        print("anomalies:", len(rep))


if __name__ == "__main__":
    main()
