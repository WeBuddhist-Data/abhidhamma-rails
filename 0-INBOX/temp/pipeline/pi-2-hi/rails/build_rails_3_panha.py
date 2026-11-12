"""Shared Pañhāpucchaka (question-and-answer) engine for the pi-2 Hindi rails, chapters 3, 14, 15.

Turns a Pāli answer line (matrix triads/dyads with siyā / na vattabbā frames) into Hindi with fixed
item names (pi-1 rails matrix names, pi-2 termbase, masculine because तत्व / ज्ञान / नियम are masculine).
Imported read-only by build_rails_3.py, build_rails_14.py, build_rails_15.py.
"""
import re

# ------------------------------------------------------------------ item names (masc. plural, singular)
_V = re.compile(r"वाले(?! मूलों)")


def _sg(pl):
    s = _V.sub("वाला", pl)
    for a, b in (("छोड़े जाने वाला", "छोड़ा जाने वाला"), ("जुड़े", "जुड़ा"), ("घुले-मिले", "घुला-मिला"),
                 ("हुए", "हुआ"), ("जाने जा सकने", "जाना जा सकने"), ("चरण के", "चरण का")):
        s = s.replace(a, b)
    return s


ITEMS = {}


def _add(keys, pl, sg=None):
    for k in keys.split("|"):
        ITEMS[key(k)] = (pl, sg if sg is not None else _sg(pl))


def key(s):
    s = s.lower().replace('"', "").replace("“", "").replace("”", "").strip(" ,.;")
    s = re.sub(r"\s+", " ", s).replace("ñceva", "ṃ ceva")
    for suf in ("tipi", "ti"):
        if s.endswith(suf) and len(s) > len(suf) + 2:
            s = s[: -len(suf)]
            break
    if s.endswith("n"):
        s = s[:-1] + "ṃ"
    words = []
    for w in s.split(" "):
        w = w.replace("ī", "i").replace("ū", "u")
        w = re.sub(r"[āaoiueṃ]+$", "", w)
        words.append(w)
    return " ".join(words)


ADM = "न दुःखद, न सुखद"
# triads
_add("kusalā", "हितकर"); _add("akusalā", "हानिकर"); _add("abyākatā", "नैतिक रूप से अनिर्धारित")
_add("sukhāya vedanāya sampayuttā", "सुखद अनुभूति से जुड़े")
_add("dukkhāya vedanāya sampayuttā", "दुःखद अनुभूति से जुड़े")
_add("adukkhamasukhāya vedanāya sampayuttā", f"{ADM} अनुभूति से जुड़े")
_add("vipākā", "कर्म-फल रूपी"); _add("vipākadhammadhammā", "कर्म-फल उत्पन्न करने वाले")
_add("nevavipākanavipākadhammadhammā", "न कर्म-फल रूपी, न कर्म-फल उत्पन्न करने वाले")
_add("upādinnupādāniyā", "कर्म से उत्पन्न और आसक्ति का विषय बनने वाले")
_add("anupādinnupādāniyā", "कर्म से उत्पन्न न होकर भी आसक्ति का विषय बनने वाले")
_add("anupādinnaanupādāniyā", "न कर्म से उत्पन्न, न आसक्ति का विषय बनने वाले")
_add("saṃkiliṭṭhasaṃkilesikā", "क्लेशों से मलिन और क्लेशों का विषय बनने वाले")
_add("asaṃkiliṭṭhasaṃkilesikā", "क्लेशों से मलिन न होने वाले, पर क्लेशों का विषय बनने वाले")
_add("asaṃkiliṭṭhaasaṃkilesikā", "क्लेशों से मलिन न होने वाले और क्लेशों का विषय न बनने वाले")
_add("savitakkasavicārā", "आरंभिक विचार और सतत विचार वाले")
_add("avitakkavicāramattā", "आरंभिक विचार से रहित, केवल सतत विचार वाले")
_add("avitakkaavicārā", "आरंभिक विचार और सतत विचार दोनों से रहित")
_add("pītisahagatā", "उल्लास के साथ होने वाले"); _add("sukhasahagatā", "सुख के साथ होने वाले")
_add("upekkhāsahagatā", "समभाव के साथ होने वाले")
_add("dassanena pahātabbā", "सत्य-दर्शन से छोड़े जाने वाले")
_add("bhāvanāya pahātabbā|bhāvanāyapahātabbā", "मानसिक अभ्यास से छोड़े जाने वाले")
_add("neva dassanena na bhāvanāya pahātabbā", "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले")
_add("dassanena pahātabbahetukā", "सत्य-दर्शन से छोड़े जाने वाले मूलों वाले")
_add("bhāvanāya pahātabbahetukā", "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाले")
_add("neva dassanena na bhāvanāya pahātabbahetukā",
     "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाले")
_add("ācayagāmino|ācayagāminī", "संचय की ओर ले जाने वाले")
_add("apacayagāmino|apacayagāminī", "संचय घटाने की ओर ले जाने वाले")
_add("nevācayagāmināpacayagāmino|nevācayagāmināpacayagāminī", "न संचय की ओर, न संचय घटाने की ओर ले जाने वाले")
_add("sekkhā", "सीखने के चरण के"); _add("asekkhā", "सीखना पूरा होने के चरण के")
_add("nevasekkhanāsekkhā", "न सीखने के चरण के, न सीखना पूरा होने के चरण के",
     "न सीखने के चरण का, न सीखना पूरा होने के चरण का")
_add("parittā", "सीमित"); _add("mahaggatā", "उन्नत"); _add("appamāṇā", "अपरिमित")
_add("parittārammaṇā", "सीमित विषय वाले"); _add("mahaggatārammaṇā", "उन्नत विषय वाले")
_add("appamāṇārammaṇā", "अपरिमित विषय वाले")
_add("hīnā", "हीन"); _add("majjhimā", "मध्यम"); _add("paṇītā", "उत्तम")
_add("micchattaniyatā", "ग़लत दिशा में निश्चित"); _add("sammattaniyatā", "सही दिशा में निश्चित")
_add("aniyatā", "अनिश्चित"); _add("niyatā", "निश्चित")
_add("maggārammaṇā", "मार्ग को विषय बनाने वाले"); _add("maggahetukā", "मार्ग को मूल बनाने वाले")
_add("maggādhipatino|maggādhipatinī", "मार्ग की प्रधानता वाले")
_add("uppannā", "उत्पन्न हो चुके", "उत्पन्न हो चुका"); _add("anuppannā", "उत्पन्न न हुए"); _add("uppādino|uppādinī", "उत्पन्न होने वाले")
_add("atītā", "अतीत के", "अतीत का"); _add("anāgatā", "भविष्य के", "भविष्य का")
_add("paccuppannā", "वर्तमान के", "वर्तमान का")
_add("atītārammaṇā", "अतीत के विषय वाले"); _add("anāgatārammaṇā", "भविष्य के विषय वाले")
_add("paccuppannārammaṇā", "वर्तमान के विषय वाले")
_add("ajjhattā", "स्वयं से संबंधित"); _add("bahiddhā", "दूसरों से संबंधित")
_add("ajjhattabahiddhā", "स्वयं और दूसरों दोनों से संबंधित")
_add("ajjhattārammaṇā", "स्वयं से संबंधित विषय वाले"); _add("bahiddhārammaṇā", "दूसरों से संबंधित विषय वाले")
_add("ajjhattabahiddhārammaṇā", "स्वयं और दूसरों दोनों से संबंधित विषय वाले")
_add("sanidassanasappaṭighā", "दिखाई देने वाले और टकराव वाले")
_add("anidassanasappaṭighā", "दिखाई न देने वाले, पर टकराव वाले")
_add("anidassanaappaṭighā|anidassanaapaṭighā", "दिखाई न देने वाले और टकराव से रहित")
# dyads: roots
_add("hetū|hetu", "मूल रूपी"); _add("sahetukā", "मूल वाले"); _add("ahetukā", "मूल से रहित")
_add("hetusampayuttā", "मूलों से जुड़े"); _add("hetuvippayuttā", "मूलों से अलग")
_add("hetū ceva sahetukā ca", "मूल रूपी भी और मूल वाले भी")
_add("sahetukā ceva na ca hetū", "मूल वाले, पर स्वयं मूल रूपी न होने वाले")
_add("hetū ceva hetusampayuttā ca", "मूल रूपी भी और मूलों से जुड़े भी")
_add("hetusampayuttā ceva na ca hetū", "मूलों से जुड़े, पर स्वयं मूल रूपी न होने वाले")
_add("na hetusahetukā|na hetū sahetukā", "मूल रूपी न होने वाले, पर मूल वाले")
_add("na hetuahetukā|nahetūahetukā", "मूल रूपी न होने वाले और मूल से रहित")
# small intermediate dyads
_add("sappaccayā", "कारणों पर निर्भर रहने वाले"); _add("appaccayā", "कारणों पर निर्भर न रहने वाले")
_add("saṅkhatā", "निर्मित"); _add("asaṅkhatā", "अनिर्मित")
_add("sanidassanā", "दिखाई देने वाले"); _add("anidassanā", "दिखाई न देने वाले")
_add("sappaṭighā", "टकराव वाले"); _add("appaṭighā", "टकराव से रहित")
_add("rūpā|rūpino", "भौतिक"); _add("arūpā|arūpino", "अभौतिक")
_add("lokiyā", "लौकिक"); _add("lokuttarā", "लोकोत्तर")
_add("kenaci viññeyyā", "किसी एक प्रकार की चेतना से जाने जा सकने वाले")
_add("kenaci na viññeyyā", "किसी एक प्रकार की चेतना से न जाने जा सकने वाले")


def _cluster(pali_n, pali_obj, pali_ass, hi_n, hi_obl, hi_obj, hi_ass, pron="उनका", neg_obj=None):
    """āsava-type cluster: X (noun), X-iyā (object of X), X-sampayutta, X ceva X-iyā ca, … X-vippayutta-X-iyā."""
    o = hi_obj
    _add(pali_n, f"{hi_n} रूपी")
    _add(pali_obj, f"{hi_obl} {o} बनने वाले")
    if neg_obj:
        _add(neg_obj, f"{hi_obl} {o} न बनने वाले")
    _add(f"{pali_ass}sampayuttā", f"{hi_ass} से जुड़े")
    _add(f"{pali_ass}vippayuttā", f"{hi_ass} से अलग")
    _add(f"{pali_n} ceva {pali_obj} ca", f"{hi_n} रूपी भी और {hi_obl} {o} बनने वाले भी")
    _add(f"{pali_obj} ceva no ca {pali_n}", f"{hi_obl} {o} बनने वाले, पर स्वयं {hi_n} रूपी न होने वाले")
    _add(f"{pali_n} ceva {pali_ass}sampayuttā ca", f"{hi_n} रूपी भी और {hi_ass} से जुड़े भी")
    _add(f"{pali_ass}sampayuttā ceva no ca {pali_n}", f"{hi_ass} से जुड़े, पर स्वयं {hi_n} रूपी न होने वाले")
    _add(f"{pali_ass}vippayutta{pali_obj}", f"{hi_ass} से अलग, पर {pron} {o} बनने वाले")
    if neg_obj:
        _add(f"{pali_ass}vippayutta{neg_obj}", f"{hi_ass} से अलग और {pron} {o} न बनने वाले")


_cluster("āsavā", "sāsavā", "āsava", "मन के मैल", "मन के मैलों का", "विषय", "मन के मैलों", neg_obj="anāsavā")
_cluster("saṃyojanā", "saṃyojaniyā", "saṃyojana", "बंधन", "बंधनों का", "विषय", "बंधनों", neg_obj="asaṃyojaniyā")
_cluster("ganthā", "ganthaniyā", "gantha", "गाँठ", "गाँठों का", "विषय", "गाँठों", neg_obj="aganthaniyā")
_cluster("oghā", "oghaniyā", "ogha", "बाढ़", "बाढ़ों का", "विषय", "बाढ़ों", neg_obj="anoghaniyā")
_cluster("yogā", "yoganiyā", "yoga", "जकड़न", "जकड़नों का", "विषय", "जकड़नों", neg_obj="ayoganiyā")
_cluster("nīvaraṇā", "nīvaraṇiyā", "nīvaraṇa", "बाधा", "बाधाओं का", "विषय", "बाधाओं", neg_obj="anīvaraṇiyā")
_cluster("parāmāsā", "parāmaṭṭhā", "parāmāsa", "ग़लत धारणा", "ग़लत धारणा का", "विषय", "ग़लत धारणा",
         pron="उसका", neg_obj="aparāmaṭṭhā")
_cluster("upādānā", "upādāniyā", "upādāna", "आसक्ति", "आसक्ति का", "विषय", "आसक्ति", pron="उसका",
         neg_obj="anupādāniyā")
_cluster("kilesā", "saṃkilesikā", "kilesa", "मन के क्लेश", "क्लेशों का", "विषय", "क्लेशों",
         pron="क्लेशों का", neg_obj="asaṃkilesikā")
_add("saṃkiliṭṭhā", "क्लेशों से मलिन"); _add("asaṃkiliṭṭhā", "क्लेशों से मलिन न होने वाले")
_add("kilesā ceva saṃkiliṭṭhā ca", "मन के क्लेश रूपी भी और क्लेशों से मलिन भी")
_add("saṃkiliṭṭhā ceva no ca kilesā", "क्लेशों से मलिन, पर स्वयं मन के क्लेश रूपी न होने वाले")
# larger intermediate dyads
_add("sārammaṇā", "विषय वाले"); _add("anārammaṇā", "विषय से रहित")
_add("cittā", "मन रूपी"); _add("cetasikā", "मन के सहचर", "मन का सहचर")
_add("acetasikā", "मन के सहचर न होने वाले", "मन का सहचर न होने वाला")
_add("cittasampayuttā|cittena sampayuttā", "मन से जुड़े"); _add("cittavippayuttā|cittena vippayuttā", "मन से अलग")
_add("cittasaṃsaṭṭhā|cittena saṃsaṭṭhā", "मन से घुले-मिले")
_add("cittavisaṃsaṭṭhā|cittena visaṃsaṭṭhā", "मन से घुले-मिले न होने वाले")
_add("cittasamuṭṭhānā", "मन से उत्पन्न")
_add("cittasahabhuno|cittasahabhū", "मन के साथ-साथ होने वाले")
_add("cittānuparivattino|cittānuparivattī", "मन का अनुसरण करने वाले")
_add("cittasaṃsaṭṭhasamuṭṭhānā", "मन से घुले-मिले और मन से उत्पन्न")
_add("cittasaṃsaṭṭhasamuṭṭhānasahabhuno|cittasaṃsaṭṭhasamuṭṭhānasahabhū",
     "मन से घुले-मिले, मन से उत्पन्न और मन के साथ-साथ होने वाले")
_add("cittasaṃsaṭṭhasamuṭṭhānānuparivattino|cittasaṃsaṭṭhasamuṭṭhānānuparivattī",
     "मन से घुले-मिले, मन से उत्पन्न और मन का अनुसरण करने वाले")
_add("ajjhattikā", "आंतरिक"); _add("bāhirā", "बाह्य")
_add("upādā", "व्युत्पन्न"); _add("upādinnā", "कर्म से उत्पन्न"); _add("anupādinnā", "कर्म से उत्पन्न न होने वाले")
# last dyads
_add("savitakkā", "आरंभिक विचार वाले"); _add("avitakkā", "आरंभिक विचार से रहित")
_add("savicārā", "सतत विचार वाले"); _add("avicārā", "सतत विचार से रहित")
_add("sappītikā", "उल्लास वाले"); _add("appītikā", "उल्लास से रहित")
_add("kāmāvacarā", "इंद्रिय-सुखों के लोक से संबंधित"); _add("rūpāvacarā", "सूक्ष्म भौतिक लोक से संबंधित")
_add("arūpāvacarā", "अभौतिक लोक से संबंधित")
_add("pariyāpannā", "अस्तित्व के लोकों में समाए हुए", "अस्तित्व के लोकों में समाया हुआ")
_add("apariyāpannā", "अस्तित्व के लोकों में न समाए हुए", "अस्तित्व के लोकों में न समाया हुआ")
_add("niyyānikā", "मुक्ति की ओर ले जाने वाले"); _add("aniyyānikā", "मुक्ति की ओर न ले जाने वाले")
_add("sauttarā", "सर्वोच्च न होने वाले"); _add("anuttarā", "सर्वोच्च")
_add("saraṇā", "संघर्ष वाले"); _add("araṇā", "संघर्ष से रहित")
_add("kusalāyeva", "केवल हितकर")

# ------------------------------------------------------------------ subjects
NUMW = {"ekādasa": "ग्यारह", "dvādasa": "बारह", "sattarasa": "सत्रह", "soḷasa": "सोलह", "pannarasa": "पंद्रह",
        "dasa": "दस", "nava": "नौ", "aṭṭha": "आठ", "satta": "सात", "cha": "छह", "pañca": "पाँच",
        "dve": "दो", "tisso": "तीन"}
NOUN = {"dhātuyo": ("तत्व", "तत्वों"), "paṭisambhidā": ("विश्लेषणात्मक ज्ञान", "विश्लेषणात्मक ज्ञानों")}
NAMED = {  # Pāli: (Hindi direct, Hindi oblique), all singular masculine
    "kāyaviññāṇadhātu": ("शरीर की चेतना का तत्व", "शरीर की चेतना के तत्व"),
    "manoviññāṇadhātu": ("मन की चेतना का तत्व", "मन की चेतना के तत्व"),
    "dhammadhātu": ("मन के विषयों का तत्व", "मन के विषयों के तत्व"),
    "manodhātu": ("मन का तत्व", "मन के तत्व"),
    "saddadhātu": ("ध्वनि का तत्व", "ध्वनि के तत्व"),
    "rūpadhātu": ("दृश्य रूप का तत्व", "दृश्य रूप के तत्व"),
    "atthapaṭisambhidā": ("अर्थ का विश्लेषणात्मक ज्ञान", "अर्थ के विश्लेषणात्मक ज्ञान"),
    "niruttipaṭisambhidā": ("भाषा का विश्लेषणात्मक ज्ञान", "भाषा के विश्लेषणात्मक ज्ञान"),
}
SUBJ_RE = re.compile(r"^(?:(" + "|".join(NUMW) + r") (dhātuyo|paṭisambhidā)|(" + "|".join(NAMED) + r"))(?: |$)", re.I)


class Subj:
    def __init__(self, direct, obl, pl):
        self.direct, self.obl, self.pl = direct, obl, pl


def parse_subject(clause, default):
    m = SUBJ_RE.match(clause)
    if not m:
        return None, clause
    if m.group(1):
        n = NUMW[m.group(1).lower()]
        d, o = NOUN[m.group(2).lower()]
        return Subj(f"{n} {d}", f"{n} {o}", True), clause[m.end():]
    d, o = NAMED[m.group(3).lower()]
    return Subj(d, o, False), clause[m.end():]


# ------------------------------------------------------------------ clause splitting
def split_outside_quotes(s, sep):
    out, buf, q = [], "", False
    i = 0
    while i < len(s):
        if s[i] == '"':
            q = not q
        if not q and s.startswith(sep, i):
            out.append(buf)
            buf = ""
            i += len(sep)
            continue
        buf += s[i]
        i += 1
    out.append(buf)
    return out


def lookup(p, pl):
    """Hindi adjective for Pāli item p; returns (text, neg)."""
    k = key(p)
    if k in ITEMS:
        return ITEMS[k][0 if pl else 1], False
    if k.startswith("n ") and k[2:] in ITEMS:  # na / no + item = negated predicate
        return ITEMS[k[2:]][0 if pl else 1], True
    raise KeyError(f"no item for {p!r} (key {k!r})")


def ends_tipi(c):
    c = c.strip().rstrip(".;")
    return c.endswith("tipi")


def ends_ti(c):
    c = c.strip().rstrip(".;")
    return c.endswith("ti") or c.endswith('"ti') or c.endswith("nti")


def has_q(c):
    return '"' in c


def q(text, quoted):
    return f"“{text}”" if quoted else text


def render_sentence(sent, default, state):
    """sent: one Pāli sentence without final '.', may contain ';' sub-sentences.
    state: dict carrying nothing across sentences (subject resets per sentence)."""
    parts = split_outside_quotes(sent, "; ")
    return "; ".join(render_part(p, default) for p in parts)


def render_part(part, default):
    clauses = [c.strip() for c in split_outside_quotes(part, ", ")]
    out = []
    subj = None          # current subject (Subj)
    subj_said = False    # subject already named in output
    after_nv = False
    i = 0
    while i < len(clauses):
        c = clauses[i]
        if c.startswith("@"):
            c = c[1:].strip()
            subj, subj_said = default, False
        s, rest = parse_subject(c, default)
        if s:
            subj, subj_said, after_nv = s, False, False
            c = rest.strip()
        if subj is None:
            subj = default
        pl = subj.pl
        lead = "" if subj_said else subj.direct + " "
        m = re.match(r"^(siyā )?na vattabbā( –)? ?(.*)$", c, re.I)
        if m:
            siya, dash, first = bool(m.group(1)), bool(m.group(2)), m.group(3)
            items = [first]
            if ends_tipi(first):
                while i + 1 < len(clauses) and ends_tipi(clauses[i + 1]):
                    i += 1
                    items.append(clauses[i])
            his = []
            for it in items:
                txt, neg = lookup(it, pl)
                assert not neg, it
                his.append(q(txt, has_q(it)))
            if subj_said:
                obj = "उन्हें" if pl else "उसे"
            else:
                obj = subj.obl + " को"
            k = "कभी " if siya else ""
            if dash:
                body = (f"{k}{obj} नहीं कहा जा सकता – " +
                        (", ".join(f"न {h}" for h in his) if len(his) > 1 else his[0]))
            else:
                if len(his) > 1:
                    body = f"{k}{obj} न {his[0]} कहा जा सकता है, " + ", ".join(f"न {h}" for h in his[1:])
                else:
                    body = f"{k}{obj} {his[0]} नहीं कहा जा सकता"
            out.append(body)
            subj_said, after_nv = True, True
            i += 1
            continue
        siya = False
        if c.lower().startswith("siyā "):
            siya, c = True, c[5:]
        txt, neg = lookup(c, pl)
        txt = q(txt, has_q(c))
        pron = ""
        if after_nv:
            pron = ("वे " if pl else "वह ")
        if siya:
            verb = ("नहीं होते" if pl else "नहीं होता") if neg else ("होते हैं" if pl else "होता है")
            out.append(f"{lead}{pron}कभी {txt} {verb}")
        else:
            verb = ("नहीं हैं" if pl else "नहीं है") if neg else ("हैं" if pl else "है")
            out.append(f"{lead}{pron}{txt} {verb}")
        subj_said, after_nv = True, False
        i += 1
    return ", ".join(out)


def render_line(line, default, fixes=()):
    """line: a Pāli answer line (no block id). fixes: (pāli_old, pāli_new) parse-only normalisations."""
    for a, b in fixes:
        assert a in line, a
        line = line.replace(a, b)
    line = line.replace("…pe…", " …pe… ")
    sents = [s for s in split_outside_quotes(line.strip(), ". ") if s.strip()]
    out = []
    for s in sents:
        s = s.strip().rstrip(".")
        # '…pe…' chains: X…pe… Y …pe… Z  (each piece a separate predicate; joined by '…')
        if "…pe…" in s:
            pieces = [p.strip().rstrip(",") for p in s.split("…pe…")]
            hs = [render_sentence(p, default, {}) if p else "" for p in pieces]
            # after the first piece the subject is already given: drop the repeated subject
            first = hs[0]
            rest = [strip_subject(h, default) for h in hs[1:]]
            out.append("… ".join([first] + rest).replace("…  ", "… ").rstrip() + "।")
        else:
            out.append(render_sentence(s, default, {}) + "।")
    return " ".join(out)


def strip_subject(h, default):
    if h.startswith(default.direct + " "):
        return h[len(default.direct) + 1:]
    return h
