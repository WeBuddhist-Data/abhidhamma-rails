"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 5-05 .. 5-12
(Dhammapaccanīya duka-tika, tika-duka, tika-tika, duka-duka; Dhammānulomapaccanīya tika, duka, duka-tika, tika-duka).

Uses the approved sample constants read-only:  import build_rails_sample as R
Run:  python -I -B -X utf8 build_rails_5-05_5-12.py [file ...]
"""
import os
import re
import sys

RAILS = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails"
sys.path.insert(0, RAILS)
import build_rails_sample as R  # noqa: E402  (read-only)

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI_DIR = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
OUT_DIR = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters")
TERMBASE = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-pali-hindi-termbase-plain.md")
FILES = ["5-05-paccaniya-dukatika.md", "5-06-paccaniya-tikaduka.md", "5-07-paccaniya-tikatika.md",
         "5-08-paccaniya-dukaduka.md", "5-09-anulomapaccaniya-tika.md", "5-10-anulomapaccaniya-duka.md",
         "5-11-anulomapaccaniya-dukatika.md", "5-12-anulomapaccaniya-tikaduka.md"]

# ---------------------------------------------------------------- numbers (termbase numeral entries + R.NUM)
NUM = dict(R.NUM)
for _ln in open(TERMBASE, encoding="utf-8"):
    _m = re.match(r"^([^:]+): \{.*\(numeral\): ([^;}]+)", _ln)
    if _m:
        NUM[_m.group(1).strip().lower()] = _m.group(2).strip()
NUM.update({"dasa": "दस", "vīsa": "बीस", "vīsati": "बीस", "ekūnavīsati": "उन्नीस", "chabbīsati": "छब्बीस"})

# ---------------------------------------------------------------- items (pi-1 1-matika.md wording, feminine, singular)
# stem (short final vowel, multiword joined by "_") -> Hindi adjective phrase agreeing with परिघटना
POS = {
    # triads
    "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
    "sukhāya_vedanāya_sampayutta": "सुखद अनुभूति से जुड़ी",
    "dukkhāya_vedanāya_sampayutta": "दुःखद अनुभूति से जुड़ी",
    "adukkhamasukhāya_vedanāya_sampayutta": "न दुःखद, न सुखद अनुभूति से जुड़ी",
    "vipāka": "कर्म-फल रूपी", "vipākadhammadhamma": "कर्म-फल उत्पन्न करने वाली",
    "nevavipākanavipākadhammadhamma": "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाली",
    "upādinnupādāniya": "कर्म से उत्पन्न और आसक्ति का विषय बनने वाली",
    "anupādinnupādāniya": "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाली",
    "anupādinnaanupādāniya": "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाली",
    "saṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन और क्लेशों का विषय बनने वाली",
    "asaṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन न होने वाली, पर क्लेशों का विषय बनने वाली",
    "asaṃkiliṭṭhaasaṃkilesika": "क्लेशों से मलिन न होने वाली और क्लेशों का विषय न बनने वाली",
    "savitakkasavicāra": "आरंभिक विचार और सतत विचार वाली",
    "avitakkavicāramatta": "आरंभिक विचार से रहित, केवल सतत विचार वाली",
    "avitakkaavicāra": "आरंभिक विचार और सतत विचार दोनों से रहित",
    "pītisahagata": "उल्लास के साथ होने वाली", "sukhasahagata": "सुख के साथ होने वाली",
    "upekkhāsahagata": "समभाव के साथ होने वाली",
    "dassanena_pahātabba": "सत्य-दर्शन से छोड़ी जाने वाली",
    "bhāvanāya_pahātabba": "मानसिक अभ्यास से छोड़ी जाने वाली",
    "nevadassanena_nabhāvanāya_pahātabba": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली",
    "dassanena_pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली",
    "bhāvanāya_pahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "nevadassanena_nabhāvanāya_pahātabbahetuka": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "ācayagāmi": "संचय की ओर ले जाने वाली", "apacayagāmi": "संचय घटाने की ओर ले जाने वाली",
    "nevācayagāmināpacayagāmi": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली",
    "sekkha": "सीखने के चरण की", "asekkha": "सीखना पूरा होने के चरण की",
    "nevasekkhanāsekkha": "न सीखने के चरण की, न सीखना पूरा होने के चरण की",
    "paritta": "सीमित", "mahaggata": "उन्नत", "appamāṇa": "अपरिमित",
    "parittārammaṇa": "सीमित विषय वाली", "mahaggatārammaṇa": "उन्नत विषय वाली",
    "appamāṇārammaṇa": "अपरिमित विषय वाली",
    "hīna": "हीन", "majjhima": "मध्यम", "paṇīta": "उत्तम",
    "micchattaniyata": "ग़लत दिशा में निश्चित", "sammattaniyata": "सही दिशा में निश्चित", "aniyata": "अनिश्चित",
    "maggārammaṇa": "मार्ग को विषय बनाने वाली", "maggahetuka": "मार्ग को मूल बनाने वाली",
    "maggādhipati": "मार्ग की प्रधानता वाली",
    "uppanna": "उत्पन्न हो चुकी", "anuppanna": "उत्पन्न न हुई", "uppādi": "उत्पन्न होने वाली",
    "atīta": "अतीत की", "anāgata": "भविष्य की", "paccuppanna": "वर्तमान की",
    "atītārammaṇa": "अतीत के विषय वाली", "anāgatārammaṇa": "भविष्य के विषय वाली",
    "paccuppannārammaṇa": "वर्तमान के विषय वाली",
    "ajjhatta": "स्वयं से संबंधित", "bahiddhā": "दूसरों से संबंधित",
    "ajjhattabahiddhā": "स्वयं और दूसरों दोनों से संबंधित",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय वाली", "bahiddhārammaṇa": "दूसरों से संबंधित विषय वाली",
    "ajjhattabahiddhārammaṇa": "स्वयं और दूसरों दोनों से संबंधित विषय वाली",
    "sanidassanasappaṭigha": "दिखाई देने वाली और टकराव वाली",
    "anidassanasappaṭigha": "दिखाई न देने वाली, पर टकराव वाली",
    "anidassanaappaṭigha": "दिखाई न देने वाली और टकराव से रहित",
    # dyads
    "hetu": "मूल रूपी", "sahetuka": "मूल वाली", "ahetuka": "मूल से रहित",
    "hetusampayutta": "मूलों से जुड़ी", "hetuvippayutta": "मूलों से अलग",
    "sappaccaya": "कारणों पर निर्भर रहने वाली", "appaccaya": "कारणों पर निर्भर न रहने वाली",
    "saṅkhata": "निर्मित", "asaṅkhata": "अनिर्मित",
    "sanidassana": "दिखाई देने वाली", "anidassana": "दिखाई न देने वाली",
    "sappaṭigha": "टकराव वाली", "appaṭigha": "टकराव से रहित",
    "rūpi": "भौतिक", "arūpi": "अभौतिक", "lokiya": "लौकिक", "lokuttara": "लोकोत्तर",
    "kenaci_viññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली",
    "āsava": "मन के मैल रूपी", "sāsava": "मन के मैलों का विषय बनने वाली",
    "anāsava": "मन के मैलों का विषय न बनने वाली",
    "āsavasampayutta": "मन के मैलों से जुड़ी", "āsavavippayutta": "मन के मैलों से अलग",
    "saññojana": "बंधन रूपी", "gantha": "गाँठ रूपी", "ogha": "बाढ़ रूपी", "yoga": "जकड़न रूपी",
    "nīvaraṇa": "बाधा रूपी", "parāmāsa": "ग़लत धारणा रूपी",
    "sārammaṇa": "विषय वाली", "anārammaṇa": "विषय से रहित",
    "citta": "मन रूपी", "cetasika": "मन की सहचर", "cittasampayutta": "मन से जुड़ी",
    "cittavippayutta": "मन से अलग",
    "cittasaṃsaṭṭha": "मन से घुली-मिली", "cittasamuṭṭhāna": "मन से उत्पन्न",
    "cittasahabhu": "मन के साथ-साथ होने वाली", "cittānuparivatti": "मन का अनुसरण करने वाली",
    "cittasaṃsaṭṭhasamuṭṭhāna": "मन से घुली-मिली और मन से उत्पन्न",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhu": "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली",
    "ajjhattika": "आंतरिक", "bāhira": "बाह्य", "upādā": "व्युत्पन्न",
    "upādinna": "कर्म से उत्पन्न", "anupādinna": "कर्म से उत्पन्न न होने वाली",
    "upādāna": "आसक्ति रूपी", "upādāniya": "आसक्ति का विषय बनने वाली",
    "kilesa": "मन के क्लेश रूपी", "saṃkilesika": "क्लेशों का विषय बनने वाली",
    "asaṃkilesika": "क्लेशों का विषय न बनने वाली", "saṃkiliṭṭha": "क्लेशों से मलिन",
    "asaṃkiliṭṭha": "क्लेशों से मलिन न होने वाली",
    "kilesasampayutta": "क्लेशों से जुड़ी", "kilesavippayutta": "क्लेशों से अलग",
    "savitakka": "आरंभिक विचार वाली", "avitakka": "आरंभिक विचार से रहित",
    "savicāra": "सतत विचार वाली", "avicāra": "सतत विचार से रहित",
    "sappītika": "उल्लास वाली", "appītika": "उल्लास से रहित",
    "kāmāvacara": "इंद्रिय-सुखों के लोक से संबंधित", "rūpāvacara": "सूक्ष्म भौतिक लोक से संबंधित",
    "arūpāvacara": "अभौतिक लोक से संबंधित",
    "pariyāpanna": "अस्तित्व के लोकों में समाई हुई", "apariyāpanna": "अस्तित्व के लोकों में न समाई हुई",
    "niyyānika": "मुक्ति की ओर ले जाने वाली", "aniyyānika": "मुक्ति की ओर न ले जाने वाली",
    "niyata": "निश्चित",
    "sauttara": "सर्वोच्च न होने वाली", "anuttara": "सर्वोच्च",
    "saraṇa": "संघर्ष वाली", "araṇa": "संघर्ष से रहित",
}
# na / no forms that pi-1 words as its own negative item (harmonise-notes row 128; termbase)
SPECIAL = {
    "nakenaci_viññeyya": "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
    "nadassanena_pahātabba": "सत्य-दर्शन से न छोड़ी जाने वाली",
    "nabhāvanāya_pahātabba": "मानसिक अभ्यास से न छोड़ी जाने वाली",
    "nadassanena_pahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों से रहित",
    "nabhāvanāya_pahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों से रहित",
    "napītisahagata": "उल्लास के साथ न होने वाली",
    "nasukhasahagata": "सुख के साथ न होने वाली",
    "naupekkhāsahagata": "समभाव के साथ न होने वाली",
    "nocittasahabhu": "मन के साथ-साथ न होने वाली",
    "nocittānuparivatti": "मन का अनुसरण न करने वाली",
}
NEG = " न होने वाली"


def resolve(stem):
    if stem in POS:
        return POS[stem]
    if stem in SPECIAL:
        return SPECIAL[stem]
    if stem[:2] in ("na", "no") and len(stem) > 3:
        inner = resolve(stem[2:])
        if inner:
            return inner + NEG
    return None


def word_item(w):
    """One inflected component word -> Hindi, or None."""
    cands = [w]
    if w.endswith("ṃ"):
        cands.append(w[:-1])
    for suf, rep in (("assa", "a"), ("ussa", "u"), ("issa", "i"), ("ino", "i"), ("uno", "u"), ("o", "a"),
                     ("ī", "i"), ("ū", "u")):
        if w.endswith(suf):
            cands.append(w[: -len(suf)] + rep)
    for c in cands:
        h = resolve(c)
        if h:
            return h
    return None


CEVA = "⁂"


def component(tok):
    """A component token, possibly a ceva pair 'A⁂B' -> Hindi."""
    if CEVA in tok:
        a, b = tok.split(CEVA)
        ha = word_item(a)
        m = re.fullmatch(r"(na|no|nana|nano)_ca_(\S+)", b)
        if m:
            hb = word_item(m.group(2))
            if ha is None or hb is None:
                return None
            hb = "स्वयं " + hb + NEG + (NEG if m.group(1) in ("nana", "nano") else "")
            return f"{ha}, पर {hb}"
        hb = word_item(b)
        if ha is None or hb is None:
            return None
        return f"{ha} भी और {hb} भी"
    return word_item(tok)


def join_and(parts):
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + " और " + parts[-1]


SLIP_LOG = []


def item(phrase, case):
    """Pāli item phrase (lowercase, joined) in a case -> (Hindi, number) or None.
    case: 'acc' (object of paṭicca), 'nom' (subject), 'dat' (dative)."""
    words = phrase.split(" ")
    noun = None
    if words[-1] in ("dhammaṃ", "dhammo", "dhammā", "dhammassa"):
        noun = words.pop()
    elif not words[-1].startswith(("vipākadhammadhamm", "navipākadhammadhamm", "nanevavipāka", "nevavipāka",
                                    "nanavipākadhammadhamm")):
        return None
    if not words:
        return None
    if case == "acc" and noun not in (None, "dhammaṃ"):
        return None
    # conjuncts: separated by 'ca', by an accusative '-ñca', or by the 'ca' of a ceva pair ('ca⁎') when that
    # pair closes its conjunct (it follows another component, or a pair / the end follows it)
    conj, cur = [], []
    for i, w in enumerate(words):
        nxt = words[i + 1] if i + 1 < len(words) else None
        if w == "ca":
            conj.append(cur)
            cur = []
        elif w == "ca⁎":
            if len(cur) > 1 or nxt is None or CEVA in nxt:
                conj.append(cur)
                cur = []
        elif case == "acc" and w.endswith("ñca"):
            cur.append(w[:-3] + "ṃ")
            conj.append(cur)
            cur = []
        else:
            cur.append(w)
    if cur:
        conj.append(cur)
    conj = [c for c in conj if c]
    if noun == "dhammā" and len(conj) == 1 and len(conj[0]) >= 2 and len(conj[0]) % 2 == 0:
        # 'A B C D ca dhammā' with the first 'ca' missing in the source: two conjuncts of two components
        h = len(conj[0]) // 2
        conj = [conj[0][:h], conj[0][h:]]
        SLIP_LOG.append("missing ca: " + phrase)
    hs = []
    for c in conj:
        if not c:
            return None
        comps = [component(t) for t in c]
        if None in comps:
            return None
        hs.append(", ".join(comps))
    if case == "acc":
        return join_and([h + " परिघटना" for h in hs]), ("p" if len(hs) > 1 else "s")
    if case == "nom":
        if len(hs) > 1:
            if noun not in ("dhammā",):
                return None
            return join_and(hs) + " परिघटनाएँ", "p"
        if noun not in (None, "dhammo"):
            return None
        return hs[0] + " परिघटना", "s"
    if case == "dat":
        if noun not in (None, "dhammassa"):
            return None
        return join_and([h + " परिघटना" for h in hs]) + " के लिए", "s"
    return None


# pre-joining of multiword stems and ceva pairs (lowercase text)
JOINS = [
    (r"(?<![\w_])((?:na|nana)?(?:sukhāya|dukkhāya|adukkhamasukhāya)) vedanāya (sampayutt\w*)", r"\1_vedanāya_\2"),
    (r"(?<![\w_])((?:na|nana)?nevadassanena) (nabhāvanāya) (pahātabb\w*)", r"\1_\2_\3"),
    (r"(?<![\w_])((?:na|nana)?(?:dassanena|bhāvanāya)) (pahātabb\w*)", r"\1_\2"),
    (r"(?<![\w_])((?:na|nana)?kenaci) (viññeyy\w*)", r"\1_\2"),
    (r"(?<![\w_])nanevaācayagāmiṃ nāpacayagāmiṃ", "nanevācayagāmināpacayagāmiṃ"),
    (r"(?<![\w_])(na)?upādādhamm", r"\1upādā dhamm"),       # fused 'naupādādhammaṃ' (spacing slip)
    (r"(?<![\w_])((?:na)?kenaci) (naviññeyy\w*)", r"\1_\2"),
    (r"(?<![\w_])na (ārammaṇe)(?![\w_])", r"na\1"),                 # 'na ārammaṇe' (spacing slip)
    (r"nanahetu dhammo ca uppajjati", "nanahetu ca dhammo uppajjati"),  # word order slip, same sense
    # ceva pairs: accusative ('ca⁎' = a 'ca' that may also close a conjunct)
    (r"(?<![\w_])(\S+)ñceva (na|no|nana|nano) ca (\S+?)ñca(?=\s)", r"\1ṃ" + CEVA + r"\2_ca_\3ṃ ca⁎"),
    (r"(?<![\w_])(\S+)ñceva (na|no|nana|nano) ca (\S+)", r"\1ṃ" + CEVA + r"\2_ca_\3"),
    (r"(?<![\w_])(\S+)ñceva (\S+)ñca(?=\s)", r"\1ṃ" + CEVA + r"\2ṃ ca⁎"),
    (r"(?<![\w_])(\S+)ñceva (\S+ṃ)(?=\s)", r"\1ṃ" + CEVA + r"\2"),      # '…ñceva Xṃ' without -ñca
    # ceva pairs: nominative / dative
    (r"(?<![\w_])(\S+) ceva (na|no|nana|nano) ca (\S+)", r"\1" + CEVA + r"\2_ca_\3"),
    (r"(?<![\w_])(\S+) ceva (\S+) ca(?=\s)", r"\1" + CEVA + r"\2 ca⁎"),
    (r"(?<![\w_])(\S+) ceva (na|no|nana|nano) (\S+)", r"\1" + CEVA + r"\2_ca_\3"),   # 'ceva nana hetussa'
    (r"(?<![\w_])(\S+) ceva (\S+)", r"\1" + CEVA + r"\2"),               # 'X ceva Y' without ca
]
# spelling slips rendered as the word meant (stems)
ALIAS = {"apaccaya": "appaccaya", "nevāsekkhanāsekkha": "nevasekkhanāsekkha", "anupanna": "anuppanna"}
POS["acetasika"] = "मन की सहचर न होने वाली"          # 'acetasika' for the dyad's second item (pi-1 wording)
POS["kenaci_naviññeyya"] = SPECIAL["nakenaci_viññeyya"]
for _a, _b in ALIAS.items():
    POS[_a] = POS[_b]


def prejoin(text):
    for a, b in JOINS:
        text = re.sub(a, b, text)
    return text


# ---------------------------------------------------------------- frames
W = r"[a-zāīūṅñṭḍṇḷṃ_⁂⁎]+"
ITEM = rf"{W}(?: {W})*?"
COND_ALT = R.COND_ALT
INS_ALT = R.INS_ALT
FRAME_HI = {  # the dependent-section frames (hi-rails-formulas §4)
    "paṭicca": "पर निर्भर होकर", "paccayā": "के कारण", "nissāya": "के आश्रय से",
    "sahajāto": "के साथ जन्म लेकर", "sahajātā": "के साथ जन्म लेकर",
    "saṃsaṭṭho": "से घुल-मिलकर", "saṃsaṭṭhā": "से घुल-मिलकर",
    "sampayutto": "से जुड़कर", "sampayuttā": "से जुड़कर",
}
FRAME_ALT = "|".join(FRAME_HI)
PAT_FULL = re.compile(rf"(?<![\w_⁂])({ITEM}) ({FRAME_ALT}) ({ITEM}) (uppajjati|uppajjanti) ({R.CHAIN_RE})")
PAT_TRUNC = re.compile(rf"(?<![\w_⁂])({ITEM}) ({FRAME_ALT})(?![\w_])")
PAT_PANHA = re.compile(rf"(?<![\w_⁂])({ITEM}) (na )?({INS_ALT})paccayena paccayo")
PAT_ITEMONLY = None  # set below

PATICCA = "पर निर्भर होकर"


def f_full(m):
    acc = item(m.group(1), "acc")
    nom = item(m.group(3), "nom")
    if not acc or not nom:
        return None
    verb = R.ARISES[nom[1]]
    if (m.group(4) == "uppajjanti") != (nom[1] == "p"):
        raise KeyError(f"number mismatch: {m.group(0)!r}")
    return f"{acc[0]} {FRAME_HI[m.group(2)]} {nom[0]} {R.CH(m.group(5))} {verb}"


def f_trunc(m):
    acc = item(m.group(1), "acc")
    if not acc:
        return None
    return f"{acc[0]} {FRAME_HI[m.group(2)]}"


def f_panha(m):
    words = m.group(1).split(" ")
    k = next((i for i, w in enumerate(words) if re.search(r"(ssa|ino|uno)$", w)), None)
    if not k:
        return None
    nom = item(" ".join(words[:k]), "nom")
    dat = item(" ".join(words[k:]), "dat")
    if not nom or not dat:
        return None
    g = "fs" if nom[1] == "s" else "fp"
    LAST["g"] = g
    ins = R.NINS(m.group(3), g) if m.group(2) else R.INS(m.group(3), g)
    return f"{nom[0]}, {dat[0]} {ins}"


LAST = {"g": "fs"}
# a chain of pañhā predicates after the first: '…, sahajātapaccayena paccayo, …'
PAT_INS_CONT = re.compile(rf"(?<![\w_⁂])(na )?({INS_ALT})paccayena paccayo")


def f_ins_cont(m):
    return R.NINS(m.group(2), LAST["g"]) if m.group(1) else R.INS(m.group(2), LAST["g"])


# what arises, after an elided object: '…pe… nakusalo … dhammā uppajjanti hetupaccayā'
PAT_NOMVERB = re.compile(rf"(?<![\w_⁂])({ITEM}) (uppajjati|uppajjanti) ({R.CHAIN_RE})")


def f_nomverb(m):
    nom = item(m.group(1), "nom")
    if not nom:
        return None
    return f"{nom[0]} {R.CH(m.group(3))} {R.ARISES[nom[1]]}"


# pañhā cut short: 'abyākato sanidassano dhammo nakusalassa nasanidassanassa…pe…'
PAT_PANHA_TRUNC = re.compile(rf"(?<![\w_⁂])({ITEM} dhammo) ({ITEM})(?=…)")


def f_panha_trunc(m):
    nom = item(m.group(1), "nom")
    dat = item(m.group(2) + ("" if m.group(2).endswith("dhammassa") else " dhammassa"), "dat")
    if not nom or not dat:
        return None
    return f"{nom[0]}, {dat[0]}"


# a subject or object left alone before '…pe…': 'naakusalo naāsavo dhammo…pe…'
PAT_NOMTRUNC = re.compile(rf"(?<![\w_⁂])({ITEM} dhamm(?:o|ā))(?![\w_⁂⁎])")


def f_nomtrunc(m):
    nom = item(m.group(1), "nom")
    return nom[0] if nom else None


# ---------------------------------------------------------------- headings
TRI = {  # harmonise-notes §1 (binding)
    "kusala": "हितकर", "vedanā": "अनुभूति", "vipāka": "कर्म-फल",
    "upādinna": "कर्म से उत्पन्न परिघटनाओं", "saṃkiliṭṭha": "क्लेशों से मलिन परिघटनाओं",
    "vitakka": "आरंभिक विचार", "pīti": "उल्लास",
    "dassana": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं",
    "dassanenapahātabba": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं",
    "dassanahetu": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "dassanenapahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "ācayagāmi": "संचय की ओर ले जाने", "ācayagāma": "संचय की ओर ले जाने",
    "sekkha": "सीखने के चरण", "paritta": "सीमित", "parittārammaṇa": "सीमित विषय", "hīna": "हीन",
    "micchatta": "ग़लत दिशा में निश्चित परिघटनाओं", "micchattaniyata": "ग़लत दिशा में निश्चित परिघटनाओं",
    "maggārammaṇa": "मार्ग को विषय बनाने", "uppanna": "उत्पन्न", "atīta": "अतीत",
    "atītārammaṇa": "अतीत के विषय", "ajjhatta": "स्वयं से संबंधित परिघटनाओं",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय",
    "sanidassana": "दिखाई देने वाला और टकराव", "sanidassanasappaṭigha": "दिखाई देने वाला और टकराव",
    "saṃkiliṭṭhasaṃkilesika": "क्लेशों से मलिन परिघटनाओं",
}
DUK = {
    "hetu": "मूल", "hetv": "मूल", "sahetuka": "मूल वाली परिघटनाओं",
    "hetusampayutta": "मूलों से जुड़ी परिघटनाओं",
    "hetusahetuka": "मूल रूपी भी और मूल वाली भी परिघटनाओं",
    "hetuhetusampayutta": "मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं",
    "nahetusahetuka": "मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं",
    "sappaccaya": "कारणों पर निर्भर रहने वाली परिघटनाओं", "saṅkhata": "निर्मित परिघटनाओं",
    "sanidassana": "दिखाई देने वाली परिघटनाओं", "sappaṭigha": "टकराव वाली परिघटनाओं",
    "rūpī": "भौतिक परिघटनाओं", "lokiya": "लौकिक परिघटनाओं",
    "kenaciviññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं",
    "āsava": "मन के मैल", "sāsava": "मन के मैलों के विषय", "āsavasampayutta": "मन के मैलों से जुड़ाव",
    "āsavasāsava": "मन के मैल और मन के मैलों के विषय",
    "āsavaāsavasampayutta": "मन के मैल और मन के मैलों से जुड़ाव",
    "āsavavippayuttasāsava": "मन के मैलों से अलगाव और मन के मैलों के विषय",
    "saññojana": "बंधन", "parāmāsa": "ग़लत धारणा",
    "sārammaṇa": "विषय वाली परिघटनाओं", "citta": "मन रूपी परिघटनाओं",
    "cetasika": "मन की सहचर परिघटनाओं", "cittasampayutta": "मन से जुड़ी परिघटनाओं",
    "cittasaṃsaṭṭha": "मन से घुली-मिली परिघटनाओं", "cittasamuṭṭhāna": "मन से उत्पन्न परिघटनाओं",
    "cittasahabhū": "मन के साथ-साथ होने वाली परिघटनाओं",
    "cittānuparivatti": "मन का अनुसरण करने वाली परिघटनाओं",
    "cittānuparivatta": "मन का अनुसरण करने वाली परिघटनाओं",
    "cittasaṃsaṭṭhasamuṭṭhāna": "मन से घुली-मिली और मन से उत्पन्न परिघटनाओं",
    "cittasaṃsaṭṭhasamuṭṭhānasahabhū": "मन से घुली-मिली, मन से उत्पन्न और मन के साथ-साथ होने वाली परिघटनाओं",
    "cittasaṃsaṭṭhasamuṭṭhānānuparivatti": "मन से घुली-मिली, मन से उत्पन्न और मन का अनुसरण करने वाली परिघटनाओं",
    "ajjhattika": "आंतरिक परिघटनाओं", "ajjhatta": "आंतरिक परिघटनाओं",
    "upādā": "व्युत्पन्न परिघटनाओं", "upādinna": "कर्म से उत्पन्न परिघटनाओं",
    "upādāna": "आसक्ति", "kilesa": "मन के क्लेश",
    "dassanenapahātabba": "सत्य-दर्शन से छोड़े जाने", "dassana": "सत्य-दर्शन से छोड़े जाने",
    "bhāvanāyapahātabba": "मानसिक अभ्यास से छोड़े जाने",
    "dassanenapahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों",
    "bhāvanāyapahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों",
    "savitakka": "आरंभिक विचार", "savicāra": "सतत विचार", "sappītika": "उल्लास",
    "pītisahagata": "उल्लास के साथ होने", "sukhasahagata": "सुख के साथ होने",
    "upekkhāsahagata": "समभाव के साथ होने",
    "kāmāvacara": "इंद्रिय-सुखों के लोक", "rūpāvacara": "सूक्ष्म भौतिक लोक", "arūpāvacara": "अभौतिक लोक",
    "pariyāpanna": "अस्तित्व के लोकों में समाए होने", "niyyānika": "मुक्ति की ओर ले जाने",
    "niyata": "निश्चित", "sauttara": "सर्वोच्च न होने", "saraṇa": "संघर्ष",
}
GROUP = {
    "hetu": "मूलों का वर्ग", "āsava": "मन के मैलों का वर्ग", "saññojana": "बंधनों का वर्ग",
    "upādāna": "आसक्ति का वर्ग", "kilesa": "मन के क्लेशों का वर्ग",
}
SET = {
    "cūḷantaradukāni": "बीच के छोटे दो-दो के वर्गीकरण", "cūḷantaradukaṃ": "बीच के छोटे दो-दो के वर्गीकरण",
    "mahantaradukāni": "बीच के बड़े दो-दो के वर्गीकरण", "mahantaradukaṃ": "बीच के बड़े दो-दो के वर्गीकरण",
    "mahantaraduka": "बीच के बड़े दो-दो के वर्गीकरण",
    "piṭṭhidukaṃ": "अंतिम दो-दो के वर्गीकरण", "piṭṭhiduka": "अंतिम दो-दो के वर्गीकरण",
    "chagocchakāni": "छह वर्ग", "chagocchakadukāni": "छह वर्गों के दो-दो के वर्गीकरण",
    "dvigocchakāni": "दो वर्ग", "parāmāsadukāni": "ग़लत धारणा वाले दो के वर्गीकरण",
}


def member(m):
    ml = m[0].lower() + m[1:]
    if ml in SET:
        return SET[ml]
    for suf, tab, tail in (("ādittikāni", TRI, " वाला तीन का वर्गीकरण आदि"), ("ttikaṃ", TRI, " वाला तीन का वर्गीकरण"),
                           ("ttika", TRI, " वाला तीन का वर्गीकरण"),
                           ("ādidukāni", DUK, " वाला दो का वर्गीकरण आदि"),
                           ("dukādi", DUK, " वाला दो का वर्गीकरण आदि"), ("dukaṃ", DUK, " वाला दो का वर्गीकरण"),
                           ("duka", DUK, " वाला दो का वर्गीकरण"),
                           ("ādigocchakāni", GROUP, " आदि"), ("ādigocchakaṃ", GROUP, " आदि"),
                           ("gocchakāni", GROUP, ""), ("gocchakaṃ", GROUP, ""), ("gocchaka", GROUP, "")):
        if ml.endswith(suf):
            st = ml[: -len(suf)]
            for c in ((st, st + "a", st + "ā") if suf.startswith("ādi") else (st,)):
                if c in tab:
                    return tab[c] + tail
    raise KeyError(f"heading member: {m!r}")


HEAD = dict(R.HEAD)
HEAD.update({
    "Dhammapaccanīye dukatikapaṭṭhānaṃ": "परिघटनाओं का नकारात्मक क्रम: दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīye tikadukapaṭṭhānaṃ": "परिघटनाओं का नकारात्मक क्रम: तीन-तीन और दो-दो के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīye tikatikapaṭṭhānaṃ": "परिघटनाओं का नकारात्मक क्रम: तीन-तीन और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammapaccanīye dukadukapaṭṭhānaṃ": "परिघटनाओं का नकारात्मक क्रम: दो-दो और दो-दो के वर्गीकरणों के कारण-संबंध",
    "Dhammānulomapaccanīye tikapaṭṭhānaṃ":
        "परिघटनाओं का सकारात्मक-नकारात्मक क्रम: तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammānulomapaccanīye dukapaṭṭhānaṃ": "परिघटनाओं का सकारात्मक-नकारात्मक क्रम: दो-दो के वर्गीकरणों के कारण-संबंध",
    "Dhammānulomapaccanīye dukatikapaṭṭhānaṃ":
        "परिघटनाओं का सकारात्मक-नकारात्मक क्रम: दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Dhammānulomapaccanīye tikadukapaṭṭhānaṃ":
        "परिघटनाओं का सकारात्मक-नकारात्मक क्रम: तीन-तीन और दो-दो के वर्गीकरणों के कारण-संबंध",
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Paccanīyaṃ": "नकारात्मक क्रम",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Paccayavāro": "कारण का खंड",
    "Hetu-ārammaṇapaccayā": f"{R.NAME['hetu']} और {R.NAME['ārammaṇa']}",
    "Nahetu-naārammaṇapaccayā": f"{R.NNAME['hetu']} और {R.NNAME['ārammaṇa']}",
    "Tatiyapadaṃ": "तीसरा पद",
    "Paccanīyapaṭṭhānaṃ": "नकारात्मक क्रम के कारण-संबंध",
    "Dukkhāyavedanāyasampayuttapadaṃ": "दुःखद अनुभूति से जुड़ी परिघटना वाला पद",
})


def heading_body(body):
    if body in HEAD:
        return HEAD[body]
    parts = body.split("-")
    return " और ".join(member(p) for p in parts)


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)((?:\d+-)*\d+\.? )?(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    return f"{hashes} {st}{num or ''}{heading_body(body)}{en}"


def closing(body):
    """'X niṭṭhitaṃ.' -> 'X समाप्त।'"""
    m = re.fullmatch(r"(.+) niṭṭhitaṃ\.", body)
    if not m:
        return None
    x = m.group(1)
    if x in HEAD:
        return HEAD[x] + " समाप्त।"
    if x == "Kusalattikapiṭṭhidukaṃ":
        return member("Kusalattika") + " और " + SET["piṭṭhidukaṃ"] + " समाप्त।"
    return heading_body(x) + " समाप्त।"


# ---------------------------------------------------------------- notes
VARA = {"sahajāta": "सह-उत्पत्ति", "paccaya": "कारण", "nissaya": "आश्रय", "saṃsaṭṭha": "घुले-मिले होने",
        "sampayutta": "जुड़ाव", "pañhā": "प्रश्नों", "paṭicca": "निर्भरता"}


def oblique_name(n):
    """'X वाला दो का वर्गीकरण' -> 'X वाले दो के वर्गीकरण' (before के समान)."""
    return n.replace(" वाला दो का वर्गीकरण", " वाले दो के वर्गीकरण").replace(
        " वाला तीन का वर्गीकरण", " वाले तीन के वर्गीकरण").replace(" का वर्ग", " के वर्ग")


def vara_list(s, form):
    """'sahajātavārampi…pe… pañhāvārampi' -> Hindi list; form 'acc' (… के खंड का भी), 'nom' (… का खंड भी),
    'loc' (… के खंड में भी)."""
    out = []
    for tok in re.split(r"(…pe… | )", s):
        if tok == " ":
            out.append(", ")
        elif tok == "…pe… ":
            out.append("… ")
        elif tok:
            m = re.fullmatch(r"(\w+?)vār(?:ampi|epi)", tok)
            v = VARA[m.group(1)]
            out.append({"acc": f"{v} के खंड का भी", "nom": f"{v} का खंड भी", "loc": f"{v} के खंड में भी"}[form])
    return "".join(out)


VARA_RE = r"(?:\w+vār(?:ampi|epi))(?:(?: |…pe… )\w+vār(?:ampi|epi))*"


def num_hi(w):
    return NUM[w]


def note_sentence(s):
    """One sentence of a note (lowercase, without final '.') -> Hindi (without final '।')."""
    s0 = s
    if s in NOTE_S:
        return NOTE_S[s]
    m = re.fullmatch(rf"({VARA_RE}) (.+)", s)
    if m and m.group(1).split(" ")[0].split("…")[0].endswith("ampi"):
        pred = m.group(2)
        if pred in ("vitthāretabbaṃ", "evaṃ vitthāretabbaṃ", "sabbattha vitthāretabbaṃ"):
            pre = {"vitthāretabbaṃ": "", "evaṃ vitthāretabbaṃ": "इसी तरह ", "sabbattha vitthāretabbaṃ": "हर जगह "}[pred]
            return f"{vara_list(m.group(1), 'acc')} {pre}विस्तार करना चाहिए"
        if pred == "paṭiccavārasadisaṃ":
            many = len(re.findall(r"vārampi", m.group(1))) > 1 or "…" in m.group(1)
            return f"{vara_list(m.group(1), 'nom')} निर्भरता के खंड के समान {'हैं' if many else 'है'}"
        if pred == "paṭiccavārasadisaṃ vitthāretabbaṃ":
            return f"{vara_list(m.group(1), 'acc')} निर्भरता के खंड के समान विस्तार करना चाहिए"
    if m and m.group(1).split(" ")[0].split("…")[0].endswith("epi"):
        pred = m.group(2)
        tail = {"vitthāro": "विस्तार से", "sabbattha vitthāro": "हर जगह विस्तार से",
                "sabbattha vitthāretabbaṃ": "हर जगह विस्तार करना चाहिए",
                "sabbattha nava": "हर जगह नौ"}.get(pred)
        if tail:
            return f"{vara_list(m.group(1), 'loc')} {tail}"
        m2 = re.fullmatch(r"(hetuyā .*)", pred)
        if m2:
            return f"{vara_list(m.group(1), 'loc')} {count_piece_line(m2.group(1))}"
    m = re.fullmatch(r"sabbattha (\w+)", s)
    if m and m.group(1) in NUM:
        return f"हर जगह {NUM[m.group(1)]}"
    m = re.fullmatch(r"(\w+) pañhā", s)
    if m and m.group(1) in NUM:
        return f"{NUM[m.group(1)]} प्रश्न"
    m = re.fullmatch(r"(\w+) pañhā kātabbā", s)
    if m and m.group(1) in NUM:
        return f"{NUM[m.group(1)]} प्रश्न करने चाहिए"
    if s in NUM:
        return NUM[s]
    m = re.fullmatch(r"(\w+)sadisaṃ", s)
    if m:
        return f"{sadisa(m.group(1))} के समान"
    m = re.fullmatch(r"(\w+?)(dukaṃ|ttikaṃ) (\w+)sadisaṃ", s)
    if m:
        return f"{member(m.group(1) + m.group(2))} {sadisa(m.group(3))} के समान है"
    raise KeyError(f"note sentence: {s0!r}")


def sadisa(x):
    """X in 'Xsadisaṃ' -> oblique Hindi name."""
    if x.endswith("duka") or x.endswith("ttika") or x.endswith("gocchaka"):
        return oblique_name(member(x))
    raise KeyError(f"sadisa: {x!r}")


NOTE_S = {
    "saṃkhittaṃ": "संक्षिप्त",
    "saṃkhittā": "संक्षिप्त",
    "sabbattha vitthāro": "हर जगह विस्तार से",
    "sabbattha vitthāretabbaṃ": "हर जगह विस्तार करना चाहिए",
    "vitthāretabbaṃ": "विस्तार करना चाहिए",
    "pañhāvāraṃ vitthāretabbaṃ": "प्रश्नों के खंड का विस्तार करना चाहिए",
    "pañhāvāraṃ evaṃ vitthāretabbaṃ": "प्रश्नों के खंड का इसी तरह विस्तार करना चाहिए",
    "paccanīyaṃ vitthāretabbaṃ": "नकारात्मक क्रम का विस्तार करना चाहिए",
    "piṭṭhidukaṃ vitthāretabbaṃ": "अंतिम दो-दो के वर्गीकरणों का विस्तार करना चाहिए",
    "pañhāvāre na sadisaṃ": "प्रश्नों के खंड में समान नहीं है",
    "ekapañhameva": "केवल एक प्रश्न",
    "etena upāyena kusalākusaladukaṃ kusalattikameva ettha vaṭṭati":
        "इसी तरीके से यहाँ हितकर और हानिकर वाले दो के वर्गीकरण के साथ केवल हितकर वाला तीन का वर्गीकरण ही लागू होता है",
    "etena upāyena nava pañhā kātabbā": "इसी तरीके से नौ प्रश्न करने चाहिए",
    "etena upāyena kenaci naviññeyye ekūnavīsati pañhā kātabbā":
        "इसी तरीके से किसी एक प्रकार की चेतना से न जानी जा सकने वाली परिघटना में उन्नीस प्रश्न करने चाहिए",
    "cittasamuṭṭhānarūpameva ettha vattati": "यहाँ केवल मन से उत्पन्न भौतिक रूप ही लागू होता है",
    "ekūnavīsati pañhā kātabbā": "उन्नीस प्रश्न करने चाहिए",
    "cha pañhā kātabbā": "छह प्रश्न करने चाहिए",
    "nanocittapadaṃ na labbhati": "मन रूपी न होने वाली न होने वाली पद लागू नहीं होता",
    "abyākatamūlaṃ dve": "नैतिक रूप से अनिर्धारित से शुरू होने वाली शृंखला में दो",
    "abyākatamūle dve": "नैतिक रूप से अनिर्धारित से शुरू होने वाली शृंखला में दो",
    "abyākatamūlaṃ ekaṃyeva": "नैतिक रूप से अनिर्धारित से शुरू होने वाली शृंखला में एक ही",
    "abyākatamūlaṃ tīṇiyeva": "नैतिक रूप से अनिर्धारित से शुरू होने वाली शृंखला में तीन ही",
    "abyākatamūlaṃ tīṇiyeva paccayavasena":
        "नैतिक रूप से अनिर्धारित से शुरू होने वाली शृंखला में कारणों के अनुसार तीन ही",
    "abyākatavāre sabbattha paccayavasena gaṇetabbaṃ":
        "नैतिक रूप से अनिर्धारित के खंड में हर जगह कारणों के अनुसार गिनना चाहिए",
    "akusalaṃ kusalasadisaṃ": "हानिकर हितकर के समान है",
    "akusalaṃ tīṇi kātabbaṃ": "हानिकर के तीन करने चाहिए",
    "abyākataṃ tīṇi kātabbaṃ": "नैतिक रूप से अनिर्धारित के तीन करने चाहिए",
    "anāgato atītasadiso": "भविष्य की परिघटना अतीत की परिघटना के समान है",
    "asaṅkhataṃ appaccayasadisaṃ": "अनिर्मित परिघटना कारणों पर निर्भर न रहने वाली परिघटना के समान है",
    "saṅkhataṃ sappaccayasadisaṃ": "निर्मित परिघटना कारणों पर निर्भर रहने वाली परिघटना के समान है",
    "saṃkhittaṃ sappaccayasadisaṃ": "संक्षिप्त, कारणों पर निर्भर रहने वाली परिघटना के समान",
    "ete saṃkhittā": "ये संक्षिप्त हैं",
    "dukattayaṃ cittadukasadisaṃ": "तीनों दो के वर्गीकरण मन रूपी परिघटनाओं वाले दो के वर्गीकरण के समान हैं",
    "yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों के खंड का सकारात्मक क्रम, नकारात्मक क्रम, "
        "सकारात्मक-नकारात्मक क्रम और नकारात्मक-सकारात्मक क्रम भी गिना गया है",
    "evaṃ gaṇetabbaṃ": "वैसे ही गिनना चाहिए",
    "yathā kusalattike pañhāvāraṃ evaṃ vitthāretabbaṃ":
        "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों का खंड है, वैसे ही विस्तार करना चाहिए",
    "yathā kusalattike pañhāvāraṃ": "जैसे हितकर वाले तीन के वर्गीकरण में प्रश्नों का खंड है",
    "evaṃ vitthāretabbaṃ": "वैसे ही विस्तार करना चाहिए",
    "yāva pañhāvārepi ekaṃ": "प्रश्नों के खंड तक भी एक",
    "cittasamuṭṭhānameva": "केवल मन से उत्पन्न ही",
    "ārammaṇaṃ natthi": f"{R.NAME['ārammaṇa']} नहीं है",
    "vipākaṃ natthi": f"{R.NAME['vipāka']} नहीं है",
    "mahābhūtā natthi": "महाभूत नहीं हैं",
}


def note(inner):
    """Text inside '( … )' -> Hindi (inside the parentheses)."""
    lo = R.lower_initials(inner)
    # a whole frame inside a note
    try:
        if "paṭicca" in lo or "paccayena paccayo" in lo:
            return translate_text(inner)
    except KeyError:
        pass
    out = []
    for tok in re.split(r"(\. |, |\.$)", lo):
        if tok == ". ":
            out.append("। ")
        elif tok == ".":
            out.append("।")
        elif tok == ", ":
            out.append(", ")
        elif tok:
            if is_count(tok):
                out.append(count_piece_line(tok))
            else:
                out.append(note_sentence(tok).replace("…pe…", "…"))
    return "".join(out)


# ---------------------------------------------------------------- counts


def is_count(text):
    toks = [t for t in re.split(r"(…pe…|…|, |; | |\.)", text) if t and t not in ("…pe…", "…", ", ", "; ", " ", ".")]
    words = set(R.P_ABL) | set(R.P_NABL) | set(R.P_LOC) | set(R.P_NLOC) | set(NUM)
    return bool(toks) and all(t in words for t in toks) and any(t not in NUM for t in toks)


def count_piece_line(text):
    """R.count_hi with the full number list (Hindi number words beyond nine)."""
    toks = [t for t in re.split(r"(…pe…|…|, |; | |\.$)", text) if t]
    out = []
    for i, t in enumerate(toks):
        if t == " ":
            prev = toks[i - 1]
            out.append(", " if prev in R.P_ABL or prev in R.P_NABL else " ")
        elif t == "…pe…":
            out.append("…")
        elif t == ".":
            out.append("।")
        elif t in ("…", ", ", "; "):
            out.append(t)
        else:
            for d in (R.P_ABL, R.P_NABL, R.P_LOC, R.P_NLOC, NUM):
                if t in d:
                    out.append(d[t])
                    break
            else:
                raise KeyError(t)
    return "".join(out)


# ---------------------------------------------------------------- clauses (explanations after "–", leftovers)
CLAUSE = {w: h for w, h in NUM.items()}
CLAUSE.update({
    "nahetuṃ akusalaṃ abyākataṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        "मूल रूपी न होने वाले, हानिकर या नैतिक रूप से अनिर्धारित एक समूह पर निर्भर होकर तीन समूह और मन से उत्पन्न भौतिक रूप",
    "nahetū akusale abyākate khandhe paṭicca hetū":
        "मूल रूपी न होने वाले हानिकर और नैतिक रूप से अनिर्धारित समूहों पर निर्भर होकर मूल",
    "nahetuṃ kusalaṃ abyākataṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        "मूल रूपी न होने वाले, हितकर या नैतिक रूप से अनिर्धारित एक समूह पर निर्भर होकर तीन समूह और मन से उत्पन्न भौतिक रूप",
    "nahetū kusale abyākate khandhe paṭicca hetū":
        "मूल रूपी न होने वाले हितकर और नैतिक रूप से अनिर्धारित समूहों पर निर्भर होकर मूल",
    "dve khandhe": "दो समूह",          # object of an elided paṭicca ('dve khandhe…pe…'): plain form, no postposition
    "kusalākusalaṃ nahetuṃ ekaṃ khandhaṃ paṭicca tayo khandhā":
        "हितकर या हानिकर, मूल रूपी न होने वाले एक समूह पर निर्भर होकर तीन समूह",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ paṭicca cittasamuṭṭhānaṃ rūpaṃ":
        "संशय के साथ होने वाले या बेचैनी के साथ होने वाले मोह पर निर्भर होकर मन से उत्पन्न भौतिक रूप",
    "vicikicchāsahagataṃ uddhaccasahagataṃ mohaṃ paṭicca sampayuttakā khandhā":
        "संशय के साथ होने वाले या बेचैनी के साथ होने वाले मोह पर निर्भर होकर जुड़े हुए समूह",
    "paṭisandhikkhaṇe vatthuṃ paṭicca sahetukā khandhā": "पुनर्जन्म के क्षण में आधार पर निर्भर होकर मूल वाले समूह",
    "dve mahābhūte": "दो महाभूत",
    "vipākābyākataṃ": "कर्म-फल रूपी नैतिक रूप से अनिर्धारित",
    "sukhāya_vedanāya_sampayutte khandhe paṭicca sukhavedanā cittasamuṭṭhānañca rūpaṃ":
        "सुखद अनुभूति से जुड़े समूहों पर निर्भर होकर सुखद अनुभूति और मन से उत्पन्न भौतिक रूप",
    "sampayuttakā khandhā cittasamuṭṭhānañca rūpaṃ": "जुड़े हुए समूह और मन से उत्पन्न भौतिक रूप",
    "mahābhūtaṃ": "महाभूत",
    "vipākābyākataṃ kiriyābyākataṃ": "कर्म-फल रूपी या केवल क्रिया रूपी नैतिक रूप से अनिर्धारित",
    "sukhāya_vedanāya_sampayuttaṃ ekaṃ khandhaṃ paṭicca tayo khandhā cittasamuṭṭhānañca rūpaṃ":
        "सुखद अनुभूति से जुड़े एक समूह पर निर्भर होकर तीन समूह और मन से उत्पन्न भौतिक रूप",
    # per-item counts (5-11, 5-12)
    "abyākato ekaṃ": "नैतिक रूप से अनिर्धारित में एक",
    "akusalena tīṇiyeva": "हानिकर के साथ तीन ही",
    "abyākatena tīṇiyeva": "नैतिक रूप से अनिर्धारित के साथ तीन ही",
    "kusalaṃ appaṭighena tīṇi": "हितकर में टकराव से रहित के साथ तीन",
    "akusalaṃ appaṭighena tīṇi": "हानिकर में टकराव से रहित के साथ तीन",
    "abyākataṃ appaṭighena tīṇi": "नैतिक रूप से अनिर्धारित में टकराव से रहित के साथ तीन",
    "kusalaṃ appaṭighañca abyākataṃ appaṭighañca tīṇi":
        "हितकर, टकराव से रहित परिघटना और नैतिक रूप से अनिर्धारित, टकराव से रहित परिघटना में तीन",
    "akusalaṃ appaṭighañca abyākataṃ appaṭighañca tīṇi":
        "हानिकर, टकराव से रहित परिघटना और नैतिक रूप से अनिर्धारित, टकराव से रहित परिघटना में तीन",
    "abyākatāni tīṇi": "नैतिक रूप से अनिर्धारित में तीन",
    "acetasikāni nava": "मन की सहचर न होने वाली में नौ",
    "cittavippayutte tīṇi": "मन से अलग में तीन",
})
for _w, _h in list(NUM.items()):
    CLAUSE[_w + " pañhā"] = _h + " प्रश्न"


def clause(piece):
    core = piece.strip()
    if not core:
        return piece
    lead = piece[: len(piece) - len(piece.lstrip())]
    trail = piece[len(piece.rstrip()):]
    if core in CLAUSE:
        return lead + CLAUSE[core] + trail
    if is_count(core):
        return lead + count_piece_line(core) + trail
    # a bare item with the rest elided ('…pe… nooghaṃ…pe…')
    comps = [component(w) for w in prejoin(core).split(" ")]
    if comps and None not in comps:
        return lead + ", ".join(comps) + trail
    return R.clause(piece)


# ---------------------------------------------------------------- line translator
PH = re.compile("\ue000(\\d+)\ue001")
LINE_HAND = {
    "Hetuyā. Nava (sabbattha nava.)": f"{R.LOC['hetu']}। नौ (हर जगह नौ।)",
}


def translate_text(line):
    store = []

    def keep(h):
        store.append(h)
        return f"\ue000{len(store) - 1}\ue001"

    text = line
    # an untagged {…} note inside an item phrase ('nakusalaṃ {…} dhammaṃ'): the bracket goes after the
    # Hindi of the word before it
    inline = []
    mm = re.search(r"(\S+) \{([^}]*)\}(?= dhamm)", text)
    if mm:
        anchor = component(R.lower_initials(mm.group(1)))
        inline.append((anchor + " परिघटना", anchor + f" [पाठभेद: {mm.group(2)}] परिघटना"))
        text = text[: mm.start()] + mm.group(1) + text[mm.end():]
    # variants {…}: untagged notes -> [पाठभेद: …] (contents kept in Pāli)
    text = re.sub(r" ?\{([^}]*)\}", lambda m: (" " if m.group(0).startswith(" ") else "")
                  + keep(f"[पाठभेद: {m.group(1)}]"), text)
    # notes in parentheses (not counts like "(3)")
    text = re.sub(r"\(([^()]*[^\d().][^()]*)\)", lambda m: keep("(" + note(m.group(1)) + ")"), text)
    text = R.lower_initials(text)
    text = prejoin(text)
    # counting lines
    head = text.split("\ue000")[0]
    core = head.rstrip(" (")
    if core and is_count(core.rstrip(".")) and not re.search(r"[^\s]", text[len(core):].replace(".", "")
                                                               .replace("।", "")) if False else False:
        pass

    def sub(pat, fn, t):
        def rep(m):
            h = fn(m)
            return m.group(0) if h is None else keep(h)
        return pat.sub(rep, t)

    text = sub(PAT_FULL, f_full, text)
    text = sub(PAT_PANHA, f_panha, text)
    text = sub(PAT_INS_CONT, f_ins_cont, text)
    text = sub(PAT_PANHA_TRUNC, f_panha_trunc, text)
    text = sub(PAT_NOMVERB, f_nomverb, text)
    text = sub(PAT_TRUNC, f_trunc, text)
    text = sub(PAT_NOMTRUNC, f_nomtrunc, text)
    out = []
    for tok in re.split(r"( – |; |, |\. |…pe…|…|\.$|;$)", text):
        if tok in (" – ", "; ", ", ", "…"):
            out.append(tok)
        elif tok == ";":
            out.append(";")
        elif tok == ". ":
            out.append("। ")
        elif tok == ".":
            out.append("।")
        elif tok == "…pe…":
            out.append("…")
        elif tok:
            for part in re.split(r"(\ue000\d+\ue001|\(\d+\))", tok):
                if not part.strip() or PH.fullmatch(part) or re.fullmatch(r"\(\d+\)", part):
                    out.append(part)
                else:
                    out.append(clause(part))
    hi = "".join(out)
    for _ in range(3):
        hi = PH.sub(lambda m: store[int(m.group(1))], hi)
    for a, b in inline:
        assert a in hi, (a, hi)
        hi = hi.replace(a, b, 1)
    return hi.replace("?।", "?")


def translate_line(line):
    if line.startswith("#"):
        return heading(line)
    if line in LINE_HAND:
        return LINE_HAND[line]
    c = closing(line)
    if c:
        return c
    return translate_text(line)


def build_file(name, errors):
    src = os.path.join(PALI_DIR, name)
    lines = open(src, encoding="utf-8").read().split("\n")
    out = []
    for ln in lines:
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = R.ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        try:
            hi = translate_line(body)
        except (KeyError, AttributeError, TypeError) as e:
            errors.append((name, body[:160], repr(e)[:300]))
            hi = "@@" + body
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or FILES
    errors = []
    for n in names:
        txt = build_file(n, errors)
        if "--dry" not in sys.argv:
            with open(os.path.join(OUT_DIR, n), "w", encoding="utf-8", newline="\n") as f:
                f.write(txt)
    seen = set()
    for e in errors:
        if e[2] in seen:
            continue
        seen.add(e[2])
        print(e[0], "|", e[2], "|", e[1])
    print("errors:", len(errors))
