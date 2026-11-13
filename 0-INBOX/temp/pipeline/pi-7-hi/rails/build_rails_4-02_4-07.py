"""pi-7 Paṭṭhāna, Hindi plain RAILS: builder for 4-02 .. 4-07 (dukatika: hetu, sahetuka, sappaccaya, āsava,
saññojana, gantha dyads with the triads).

Imports the approved sample constants read-only (build_rails_sample as S) and adds the duka-tika item grammar.
usage: python -I -B -X utf8 build_rails_4-02_4-07.py [--check]   (--check: translate, report errors, write nothing)
"""
import os
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\rails")
import build_rails_sample as S  # noqa: E402  (read-only)

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI_DIR = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
OUT_DIR = os.path.join(ROOT, "AI_translation", "hindi", "pi-7-hindi-plain-rails_split_chapters")
FILES = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md"]

PARI = "परिघटना"
PARIS = "परिघटनाएँ"

# ---------------------------------------------------------------- items (feminine, before «परिघटना»)
# pi-1 1-matika.md wording (termbase words; Hindi commas inside the long items as in pi-1)
TIKA_ITEM = {
    "kusala": "हितकर", "akusala": "हानिकर", "abyākata": "नैतिक रूप से अनिर्धारित",
    "sukhāyavedanāyasampayutta": "सुखद अनुभूति से जुड़ी",
    "dukkhāyavedanāyasampayutta": "दुःखद अनुभूति से जुड़ी",
    "adukkhamasukhāyavedanāyasampayutta": "न दुःखद, न सुखद अनुभूति से जुड़ी",
    "vipāka": "कर्म-फल रूपी",
    "vipākadhammadhamma": "कर्म-फल उत्पन्न करने वाली",
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
    "pītisahagata": "उल्लास के साथ होने वाली",
    "sukhasahagata": "सुख के साथ होने वाली",
    "upekkhāsahagata": "समभाव के साथ होने वाली",
    "dassanenapahātabba": "सत्य-दर्शन से छोड़ी जाने वाली",
    "bhāvanāyapahātabba": "मानसिक अभ्यास से छोड़ी जाने वाली",
    "nevadassanenanabhāvanāyapahātabba": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़ी जाने वाली",
    "dassanenapahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाली",
    "bhāvanāyapahātabbahetuka": "मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "nevadassanenanabhāvanāyapahātabbahetuka": "न सत्य-दर्शन से, न मानसिक अभ्यास से छोड़े जाने वाले मूलों वाली",
    "ācayagāmi": "संचय की ओर ले जाने वाली",
    "apacayagāmi": "संचय घटाने की ओर ले जाने वाली",
    "nevācayagāmināpacayagāmi": "न संचय की ओर, न संचय घटाने की ओर ले जाने वाली",
    "sekkha": "सीखने के चरण की",
    "asekkha": "सीखना पूरा होने के चरण की",
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
    "anidassanasappaṭigha": "दिखाई न देने वाली, पर टकराव वाली",
    "anidassanaappaṭigha": "दिखाई न देने वाली और टकराव से रहित",
}
DUKA_ITEM = {
    "hetu": "मूल रूपी", "nahetu": "मूल रूपी न होने वाली",
    "sahetuka": "मूल वाली", "ahetuka": "मूल से रहित",
    "hetusampayutta": "मूलों से जुड़ी", "hetuvippayutta": "मूलों से अलग",
    "sappaccaya": "कारणों पर निर्भर रहने वाली", "appaccaya": "कारणों पर निर्भर न रहने वाली",
    "saṅkhata": "निर्मित", "asaṅkhata": "अनिर्मित",
    "sanidassana": "दिखाई देने वाली", "anidassana": "दिखाई न देने वाली",
    "sappaṭigha": "टकराव वाली", "appaṭigha": "टकराव से रहित",
    "rūpi": "भौतिक", "arūpi": "अभौतिक",
    "lokiya": "लौकिक", "lokuttara": "लोकोत्तर",
    "kenaciviññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली",
    "kenacinaviññeyya": "किसी एक प्रकार की चेतना से न जानी जा सकने वाली",
}
for _k, _n in (("āsava", "मन के मैल"), ("saññojana", "बंधन"), ("gantha", "गाँठ")):
    _pl = {"āsava": "मन के मैलों", "saññojana": "बंधनों", "gantha": "गाँठों"}[_k]
    _niya = {"āsava": "sāsava", "saññojana": "saññojaniya", "gantha": "ganthaniya"}[_k]
    _aniya = {"āsava": "anāsava", "saññojana": "asaññojaniya", "gantha": "aganthaniya"}[_k]
    DUKA_ITEM[_k] = f"{_n} रूपी"
    DUKA_ITEM["no" + _k] = f"{_n} रूपी न होने वाली"
    DUKA_ITEM[_niya] = f"{_pl} का विषय बनने वाली"
    DUKA_ITEM[_aniya] = f"{_pl} का विषय न बनने वाली"
    DUKA_ITEM[_k + "sampayutta"] = f"{_pl} से जुड़ी"
    DUKA_ITEM[_k + "vippayutta"] = f"{_pl} से अलग"
    # «X-vippayutta X-niya» (pi-1: «… से अलग, पर उनका विषय बनने वाली»)
    DUKA_ITEM[_k + "vippayutta|" + _niya] = f"{_pl} से अलग, पर उनका विषय बनने वाली"
    DUKA_ITEM[_k + "vippayutta|" + _aniya] = f"{_pl} से अलग और उनका विषय न बनने वाली"
# «nahetu sahetuka / ahetuka» (dyad 6, pi-1)
DUKA_ITEM["nahetu|sahetuka"] = "मूल रूपी न होने वाली, पर मूल वाली"
DUKA_ITEM["nahetu|ahetuka"] = "मूल रूपी न होने वाली और मूल से रहित"
LEX = dict(TIKA_ITEM)
LEX.update(DUKA_ITEM)

SLIP_WORDS = {"asakkho": "asekkho", "sāsavoca": "sāsavo ca"}   # spelling slips, rendered as meant


def stem(w):
    for suf in ("ñceva", "ñca", "ssa", "ṃ"):
        if w.endswith(suf):
            return w[: -len(suf)]
    if w.endswith("o"):
        return w[:-1] + "a"
    if w.endswith("ī"):
        return w[:-1] + "i"
    return w


def neg_of(y):
    for p in ("na", "no"):
        if p + y in LEX:
            return LEX[p + y]
    raise KeyError("neg " + y)


def slot_hi(slot):
    kind = slot[0]
    if kind == "one":
        w = slot[1]
        if "+" in w:
            a, b = w.split("+")
            return LEX[stem(a) + "|" + stem(b)]
        return LEX[stem(w)]
    x, y = slot[1], slot[2]
    if kind == "pos":
        return f"{LEX[x]} भी और {LEX[y]} भी"
    return f"{LEX[x]}, पर स्वयं {neg_of(y)}"          # X ceva no/na ca Y


def parse_items(text):
    """Pāli item phrase (any case, with or without dhamma-) -> list of conjuncts, each a Hindi adjective phrase."""
    t = S.lower_initials(text.strip())
    for a, b in SLIP_WORDS.items():
        t = re.sub(rf"\b{a}\b", b, t)
    t = t.replace("nevadassanena nabhāvanāya ", "nevadassanenanabhāvanāya")
    t = t.replace("dassanena ", "dassanena").replace("bhāvanāya ", "bhāvanāya")
    t = t.replace("sukhāya vedanāya ", "sukhāyavedanāya").replace("dukkhāya vedanāya ", "dukkhāyavedanāya")
    t = t.replace("kenaci ", "kenaci")
    t = t.replace("no ca ", "noca_").replace("na ca ", "naca_")
    t = re.sub(r"\b(nahetu\w*) ((?:a|sa)hetuk\w*)", r"\1+\2", t)
    t = re.sub(r"\b(\w+vippayutt\w*) ((?:sāsav|anāsav|saññojaniy|asaññojaniy|ganthaniy|aganthaniy)\w*)", r"\1+\2", t)
    toks = t.split()
    conj, cur, i = [], [], 0
    while i < len(toks):
        w = toks[i]
        if w in ("dhammaṃ", "dhammo", "dhammā", "dhammassa"):
            i += 1
            continue
        if w == "ca":
            conj.append(cur)
            cur = []
            i += 1
            continue
        if w.endswith("ñceva"):
            nxt = toks[i + 1]
            if nxt.startswith(("noca_", "naca_")):
                cur.append(("neg", stem(w), stem(nxt[5:])))
            else:
                # «Xñceva Yñca», or «Xñceva Y tikañca» where the ca sits on the triad word
                cur.append(("pos", stem(w), stem(nxt)))
            i += 2
            continue
        if i + 1 < len(toks) and toks[i + 1] == "ceva":
            nxt = toks[i + 2]
            if nxt.startswith(("noca_", "naca_")):
                cur.append(("neg", stem(w), stem(nxt[5:])))
                i += 3
            else:
                assert toks[i + 3] == "ca", text
                cur.append(("pos", stem(w), stem(nxt)))
                i += 4
            continue
        cur.append(("one", w))
        if w.endswith("ñca"):
            conj.append(cur)
            cur = []
        i += 1
    if cur:
        conj.append(cur)
    return [", ".join(slot_hi(s) for s in c) for c in conj]


def join_list(xs):
    if len(xs) == 1:
        return xs[0]
    return ", ".join(xs[:-1]) + " और " + xs[-1]


def acc_hi(text):        # X dhammaṃ (object of paṭicca), oblique: «… परिघटना»
    return join_list([c + " " + PARI for c in parse_items(text)])


def nom_hi(text, plural):
    cs = parse_items(text)
    if plural or len(cs) > 1:
        if len(cs) == 2 and any(" और " in c for c in cs):
            # an item that already has «और» inside: join the two items with «तथा» so the pair stays clear
            return cs[0] + " तथा " + cs[1] + " " + PARIS
        return join_list(cs) + " " + PARIS
    assert len(cs) == 1, text
    return cs[0] + " " + PARI


def dat_hi(text):
    return join_list([c + " " + PARI for c in parse_items(text)]) + " के लिए"


# ---------------------------------------------------------------- names (harmonise-notes.md §1)
TIKA_NAME = {
    "kusala": "हितकर वाला तीन का वर्गीकरण", "vedanā": "अनुभूति वाला तीन का वर्गीकरण",
    "vipāka": "कर्म-फल वाला तीन का वर्गीकरण",
    "upādinna": "कर्म से उत्पन्न परिघटनाओं वाला तीन का वर्गीकरण",
    "saṃkiliṭṭha": "क्लेशों से मलिन परिघटनाओं वाला तीन का वर्गीकरण",
    "vitakka": "आरंभिक विचार वाला तीन का वर्गीकरण", "pīti": "उल्लास वाला तीन का वर्गीकरण",
    "dassanenapahātabba": "सत्य-दर्शन से छोड़ी जाने वाली परिघटनाओं वाला तीन का वर्गीकरण",
    "dassanenapahātabbahetuka": "सत्य-दर्शन से छोड़े जाने वाले मूलों वाला तीन का वर्गीकरण",
    "ācayagāmi": "संचय की ओर ले जाने वाला तीन का वर्गीकरण", "sekkha": "सीखने के चरण वाला तीन का वर्गीकरण",
    "paritta": "सीमित वाला तीन का वर्गीकरण", "parittārammaṇa": "सीमित विषय वाला तीन का वर्गीकरण",
    "hīna": "हीन वाला तीन का वर्गीकरण",
    "micchattaniyata": "ग़लत दिशा में निश्चित परिघटनाओं वाला तीन का वर्गीकरण",
    "maggārammaṇa": "मार्ग को विषय बनाने वाला तीन का वर्गीकरण", "uppanna": "उत्पन्न वाला तीन का वर्गीकरण",
    "atīta": "अतीत वाला तीन का वर्गीकरण", "atītārammaṇa": "अतीत के विषय वाला तीन का वर्गीकरण",
    "ajjhatta": "स्वयं से संबंधित परिघटनाओं वाला तीन का वर्गीकरण",
    "ajjhattārammaṇa": "स्वयं से संबंधित विषय वाला तीन का वर्गीकरण",
    "sanidassanasappaṭigha": "दिखाई देने वाला और टकराव वाला तीन का वर्गीकरण",
}
DUKA_NAME = {
    "hetu": "मूल वाला दो का वर्गीकरण", "sahetuka": "मूल वाली परिघटनाओं वाला दो का वर्गीकरण",
    "hetusampayutta": "मूलों से जुड़ी परिघटनाओं वाला दो का वर्गीकरण",
    "hetusahetuka": "मूल रूपी भी और मूल वाली भी परिघटनाओं वाला दो का वर्गीकरण",
    "hetuhetusampayutta": "मूल रूपी भी और मूलों से जुड़ी भी परिघटनाओं वाला दो का वर्गीकरण",
    "nahetusahetuka": "मूल रूपी न होने वाली, पर मूल वाली परिघटनाओं वाला दो का वर्गीकरण",
    "sappaccaya": "कारणों पर निर्भर रहने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "saṅkhata": "निर्मित परिघटनाओं वाला दो का वर्गीकरण",
    "sanidassana": "दिखाई देने वाली परिघटनाओं वाला दो का वर्गीकरण",
    "sappaṭigha": "टकराव वाली परिघटनाओं वाला दो का वर्गीकरण",
    "rūpī": "भौतिक परिघटनाओं वाला दो का वर्गीकरण", "lokiya": "लौकिक परिघटनाओं वाला दो का वर्गीकरण",
    "kenaciviññeyya": "किसी एक प्रकार की चेतना से जानी जा सकने वाली परिघटनाओं वाला दो का वर्गीकरण",
}
for _k, _n, _pl in (("āsava", "मन के मैल", "मन के मैलों"), ("saññojana", "बंधन", "बंधनों"),
                    ("gantha", "गाँठ", "गाँठों")):
    _niya = {"āsava": "sāsava", "saññojana": "saññojaniya", "gantha": "ganthaniya"}[_k]
    DUKA_NAME[_k] = f"{_n} वाला दो का वर्गीकरण"
    DUKA_NAME[_niya] = f"{_pl} के विषय वाला दो का वर्गीकरण"
    DUKA_NAME[_k + "sampayutta"] = f"{_pl} से जुड़ाव वाला दो का वर्गीकरण"
    DUKA_NAME[_k + _niya] = f"{_n} और {_pl} के विषय वाला दो का वर्गीकरण"
    DUKA_NAME[_k + _k + "sampayutta"] = f"{_n} और {_pl} से जुड़ाव वाला दो का वर्गीकरण"
    DUKA_NAME[_k + "vippayutta" + _niya] = f"{_pl} से अलगाव और {_pl} के विषय वाला दो का वर्गीकरण"
GOCCHAKA = {"hetu": "मूलों का वर्ग", "āsava": "मन के मैलों का वर्ग", "saññojana": "बंधनों का वर्ग",
            "gantha": "गाँठों का वर्ग", "ogha": "बाढ़ों का वर्ग", "yoga": "जकड़नों का वर्ग"}
CULANTARA = "बीच के छोटे दो-दो के वर्गीकरण"
CULANTARE = "बीच के छोटे दो-दो के वर्गीकरणों में"        # cūḷantaraduke (locative)


def oblique_name(n):
    """«X वाला दो का वर्गीकरण» -> «X वाले दो के वर्गीकरण» (before a postposition)."""
    n = re.sub(r"वाला (दो|तीन) का वर्गीकरण$", r"वाले \1 के वर्गीकरण", n)
    return n.replace(" का वर्ग", " के वर्ग") if n.endswith("का वर्ग") else n


def masc(f):
    """feminine item -> masculine (before «पद»)."""
    m = f.replace("वाली", "वाला").replace("जुड़ी", "जुड़ा").replace("चुकी", "चुका").replace("न हुई", "न हुआ")
    m = m.replace("छोड़ी जाने", "छोड़ा जाने").replace("जानी जा सकने", "जाना जा सकने")
    m = re.sub(r" की(,|$)", r" का\1", m)
    return m


# ---------------------------------------------------------------- headings
HEAD = dict(S.HEAD)
HEAD.update({
    "Dhammānulome dukatikapaṭṭhānaṃ": "परिघटनाओं का सकारात्मक क्रम: दो-दो और तीन-तीन के वर्गीकरणों के कारण-संबंध",
    "Paṭiccavārādi": "निर्भरता का खंड आदि",
    "Paccayacatukkaṃ": "कारणों के चार क्रम",
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए कारणों की छँटाई",
    "Paccanīyaṃ": "नकारात्मक क्रम",
    "Suddhaṃ": "अकेले-अकेले कारण",
    "Vipākadhammapadaṃ": masc(TIKA_ITEM["vipākadhammadhamma"]) + " पद",
    "Nevavipākanavipākadhammapadaṃ": masc(TIKA_ITEM["nevavipākanavipākadhammadhamma"]) + " पद",
})
PADA_KEY = {"sukhāyavedanāyasampayutta": "sukhāyavedanāyasampayutta"}


def cond_key(word):
    """'Napurejāta' -> ('purejāta', True); 'Hetu' -> ('hetu', False)."""
    w = word[0].lower() + word[1:]
    if w in S.KEYS:
        return w, False
    for p in ("na", "no"):
        if w.startswith(p) and w[len(p):] in S.KEYS:
            return w[len(p):], True
    raise KeyError(word)


def cond_name(word):
    k, neg = cond_key(word)
    return S.NNAME[k] if neg else S.NAME[k]


def head_body(body):
    if body in HEAD:
        return HEAD[body]
    m = re.fullmatch(r"(\w+)duka-(\w+)ttikaṃ", body)
    if m:
        return DUKA_NAME[m.group(1).lower()] + " और " + TIKA_NAME[m.group(2)]
    m = re.fullmatch(r"(\w+)padaṃ", body)
    if m:
        k = m.group(1)[0].lower() + m.group(1)[1:]
        return masc(LEX[k]) + " पद"
    m = re.fullmatch(r"([\w-]+?)paccayā(di)?", body)
    if m:
        parts = m.group(1).split("-")
        if len(parts) == 1 and parts[0] == "Nahetunaārammaṇa":      # written without the hyphen
            parts = ["Nahetu", "naārammaṇa"]
        hi = " और ".join(cond_name(p) for p in parts)
        return hi + (" आदि" if m.group(2) else "")
    m = re.fullmatch(r"(\w+)paccayādi", body)
    if m:
        return cond_name(m.group(1)) + " आदि"
    raise KeyError("heading: " + body)


def heading(line):
    m = re.fullmatch(r"(#+) (\*?)(\d+(?:-\d+)*\.? )?(.*?)(\*?)", line)
    hashes, st, num, body, en = m.groups()
    return f"{hashes} {st}{num or ''}{head_body(body)}{en}"


# ---------------------------------------------------------------- notes (inside parentheses)
SECTION = {"sahajāta": "सह-उत्पत्ति", "paccaya": "कारण", "nissaya": "आश्रय", "saṃsaṭṭha": "घुले-मिले होने",
           "sampayutta": "जुड़ाव", "pañhā": "प्रश्नों", "paṭicca": "निर्भरता"}
METHODS = ("सकारात्मक क्रम, नकारात्मक क्रम, सकारात्मक-नकारात्मक क्रम और नकारात्मक-सकारात्मक क्रम")
YATHA_KUSALATTIKE = (f"जैसे {oblique_name(TIKA_NAME['kusala'])} में प्रश्नों के खंड को {METHODS} में भी गिना गया है, "
                     "वैसे ही गिनना चाहिए")
NOTE = {
    "saṃkhittaṃ": "संक्षिप्त",
    "anulomaṃ": "सकारात्मक क्रम",
    "paccanīyaṃ": "नकारात्मक क्रम",
    "anulomapaccanīyaṃ": "सकारात्मक-नकारात्मक क्रम",
    "anuloma paccanīyaṃ": "सकारात्मक-नकारात्मक क्रम",       # space slip for anulomapaccanīyaṃ
    "paccanīyānulomaṃ": "नकारात्मक-सकारात्मक क्रम",
    "yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ, "
    "evaṃ gaṇetabbaṃ": YATHA_KUSALATTIKE,
    # naṇitaṃ: spelling slip for gaṇitaṃ
    "yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi naṇitaṃ, "
    "evaṃ gaṇetabbaṃ": YATHA_KUSALATTIKE,
    "yathā kusalattike pañhāvārassa anulomampi paccanīyampi anulomapaccanīyampi paccanīyānulomampi gaṇitaṃ "
    "evaṃ gaṇetabbaṃ": YATHA_KUSALATTIKE,
    "imamhi dukatike paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi "
    "sampayuttavārampi anuppannampi uppādīpi natthi":
        "दो और तीन के इस वर्गीकरण में न निर्भरता का खंड है, न सह-उत्पत्ति का खंड, न कारण का खंड, न आश्रय का खंड, "
        "न घुले-मिले होने का खंड, न जुड़ाव का खंड, न उत्पन्न न हुई परिघटना और न उत्पन्न होने वाली परिघटना",
    "imamhi dukatike paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi "
    "sampayuttavārampi atītampi anāgatampi natthi":
        "दो और तीन के इस वर्गीकरण में न निर्भरता का खंड है, न सह-उत्पत्ति का खंड, न कारण का खंड, न आश्रय का खंड, "
        "न घुले-मिले होने का खंड, न जुड़ाव का खंड, न अतीत की परिघटना और न भविष्य की परिघटना",
    "ajjhattabahiddhā na labbhanti": f"{TIKA_ITEM['ajjhattabahiddhā']} परिघटनाएँ लागू नहीं होतीं",
    "ārammaṇādhipatiyeva": "केवल विषय रूपी प्रधानता",
    "tadārammaṇāyeva labbhanti": "केवल उसी विषय को लेकर होने वाले ही लागू होते हैं",
    "sahajātādhipatiyeva labbhati": "केवल सह-उत्पत्ति रूपी प्रधानता लागू होती है",
    "ārammaṇādhipati natthi": "विषय रूपी प्रधानता नहीं है",
    "itare dve anantarūpanissayo pakatūpanissayoyeva":
        "बाकी दो में केवल निकटता रूपी प्रबल आश्रय और स्वाभाविक प्रबल आश्रय",
    "sahajātakammameva": "केवल सह-उत्पत्ति रूपी कर्म",
    "majjhe tiṇṇaṃ sahajātādhipati labbhati": "बीच के तीन में सह-उत्पत्ति रूपी प्रधानता लागू होती है",
    "sabbe paccayā kātabbā": "सभी कारण शामिल करने चाहिए",
    "hetupaccayo natthi": f"{S.NAME['hetu']} नहीं है",
    "pañhāvārepi imesaṃ tiṇṇannaṃ hetupaccayo natthi": f"प्रश्नों के खंड में भी इन तीनों में {S.NAME['hetu']} नहीं है",
    "sappaccayasadisaṃ vitthāretabbaṃ": f"{oblique_name(DUKA_NAME['sappaccaya'])} के समान विस्तार करना चाहिए",
    "appaccayampi asaṅkhatampi sanidassanampi na labbhati":
        f"{DUKA_ITEM['appaccaya']} परिघटना, {DUKA_ITEM['asaṅkhata']} परिघटना और {DUKA_ITEM['sanidassana']} परिघटना "
        "भी लागू नहीं होतीं",
    "kenaci viññeyyaṃ akusalampi kenaci viññeyyaṃ abyākatampi kenaci viññeyyakusalasadisaṃ vitthāretabbaṃ":
        f"{DUKA_ITEM['kenaciviññeyya']}, हानिकर परिघटना का भी और {DUKA_ITEM['kenaciviññeyya']}, नैतिक रूप से "
        f"अनिर्धारित परिघटना का भी, {DUKA_ITEM['kenaciviññeyya']}, हितकर परिघटना के समान विस्तार करना चाहिए",
    "yathā cūḷantaraduke lokiyadukagamanaṃ, evaṃ imampi ñātabbaṃ":
        f"जैसे {CULANTARE} {oblique_name(DUKA_NAME['lokiya'])} का प्रसंग है, वैसे ही इसे भी जानना चाहिए",
    "yathā cūḷantaraduke lokiyadukasadisaṃ":
        f"जैसे {CULANTARE}, {oblique_name(DUKA_NAME['lokiya'])} के समान",
    "lokiyalokuttaragamanasadisaṃ": "लौकिक और लोकोत्तर के प्रसंग के समान",
    "oghagocchakampi yogagocchakampi āsavagocchakakusalattikasadisaṃ":
        f"{GOCCHAKA['ogha']} भी और {GOCCHAKA['yoga']} भी {oblique_name(GOCCHAKA['āsava'])} और "
        f"{oblique_name(TIKA_NAME['kusala'])} के समान हैं",
}
for _n, _h in S.NUM.items():
    NOTE["sabbattha " + _n] = "हर जगह " + _h

# sentences outside the parentheses
SENT = {
    "cūḷantaraduke lokiyadukasadisaṃ.": f"{CULANTARE} {oblique_name(DUKA_NAME['lokiya'])} के समान।",
    "pakatūpanissayo – uppannaṃ utuṃ upanissāya jhānaṃ uppādeti, vipassanaṃ… maggaṃ… abhiññaṃ… samāpattiṃ uppādeti":
        "स्वाभाविक प्रबल आश्रय – उत्पन्न हो चुके तापमान के प्रबल आश्रय से ध्यान उत्पन्न करता है, अंतर्दृष्टि… मार्ग… "
        "उच्च ज्ञान… ध्यान-अवस्था उत्पन्न करता है",
}

VARA_TOK = re.compile(r"(\w+?)vār(o|aṃ|am|e)(pi)?|( ?…pe… ?| ?… ?| )")
VARA_PRED = {
    "paṭiccavārasadisā vitthāretabbā": "निर्भरता के खंड के समान विस्तार करना चाहिए",
    "paṭiccavārasadisaṃ vitthāretabbaṃ": "निर्भरता के खंड के समान विस्तार करना चाहिए",
    "vitthāretabbā": "विस्तार करना चाहिए",
    "vitthāretabbo": "विस्तार करना चाहिए",
    "sabbattha vitthāretabbā": "हर जगह विस्तार करना चाहिए",
    "sabbattha vitthāretabbo": "हर जगह विस्तार करना चाहिए",
    "paṭiccavārasadisā": "निर्भरता के खंड के समान हैं",
    "paṭiccavārasadisaṃ": "निर्भरता के खंड के समान हैं",
    "sabbattha sadisā": "हर जगह समान हैं",
}
for _n, _h in S.NUM.items():
    VARA_PRED["sabbattha " + _n] = "हर जगह " + _h


def vara_note(s):
    """'sahajātavāropi paccayavāropi … paṭiccavārasadisā vitthāretabbā' and the like."""
    m = re.fullmatch(r"((?:\w+?vār(?:o|aṃ|am|e)(?:pi)?(?: ?…pe… ?| ?… ?| ))+)(.+)", s)
    if not m or m.group(2) not in VARA_PRED:
        raise KeyError("note: " + s)
    pred = VARA_PRED[m.group(2)]
    items, seps = [], []
    for x, case, pi, sep in VARA_TOK.findall(m.group(1)):
        if x:
            items.append((x, case))
        elif items:
            seps.append(sep)
    seps = seps[: len(items) - 1]
    oblique = "विस्तार" in pred
    loc = items[0][1] == "e"
    out = []
    for i, (x, case) in enumerate(items):
        nm = SECTION[x]
        if loc or oblique:
            out.append(f"{nm} के खंड")
        else:
            out.append(f"{nm} का खंड")
        if i < len(seps):
            sep = seps[i]
            if sep == " ":
                sep = " और " if i == len(items) - 2 else ", "
            out.append(sep.replace("…pe…", "…"))
    tail = " में भी" if loc else (" का भी" if oblique else " भी")
    return "".join(out) + tail + " " + pred


def note_part(p):
    key = S.lower_initials(p.strip())
    if key in NOTE:
        return NOTE[key]
    return vara_note(key)


def note_hi(content):
    """content of a parenthesised note (no digits-only) -> Hindi."""
    out = []
    for sent in re.split(r"(?<=\.) ", content.strip()):
        end = sent.endswith(".")
        core = sent[:-1] if end else sent
        key = S.lower_initials(core)
        if key in NOTE:
            h = NOTE[key]
        else:
            try:
                h = vara_note(key)
            except KeyError:
                h = ", ".join(note_part(p) for p in core.split(", "))
        out.append(h + ("।" if end else ""))
    return " ".join(out)


# ---------------------------------------------------------------- sentence translators
NUM = S.NUM
LABEL = {"ārammaṇādhipati": "विषय रूपी प्रधानता", "sahajātādhipati": "सह-उत्पत्ति रूपी प्रधानता",
         "ārammaṇūpanissayo": "विषय रूपी प्रबल आश्रय", "anantarūpanissayo": "निकटता रूपी प्रबल आश्रय",
         "pakatūpanissayo": "स्वाभाविक प्रबल आश्रय", "ārammaṇapurejātaṃ": "विषय रूपी पूर्व-उत्पत्ति",
         "vatthupurejātaṃ": "आधार रूपी पूर्व-उत्पत्ति"}
PH = re.compile(r"⟦\d+⟧")
COND_WORDS = set(S.P_ABL) | set(S.P_NABL)
COUNT_SLIPS = {"kamma nava": "kamme nava", "avigata nava": "avigate nava"}   # spelling slips (kamme, avigate)


def rest_tokens_hi(toks):
    out = []
    for tk in toks:
        lt = S.lower_initials(tk)
        if not tk.strip():
            out.append(tk)
        elif tk == "…pe…":
            out.append("…")
        elif tk in ("…", "–", ",") or PH.fullmatch(tk) or re.fullmatch(r"\(\d+\)", tk):
            out.append(tk)
        elif lt in NUM:
            out.append(NUM[lt])
        elif lt.rstrip(",") in NUM:
            out.append(NUM[lt.rstrip(",")] + ",")
        elif lt in COND_WORDS:
            out.append(S._cond_word(lt))
        else:
            raise KeyError("rest token: " + tk)
    return "".join(out)


def paticca_hi(m):
    obj, subj, verb, rest = m.group("obj"), m.group("subj"), m.group("verb"), m.group("rest")
    plural = verb == "uppajjanti"
    head = f"{acc_hi(obj)} {S.PATICCA} {nom_hi(subj, plural)}"
    clause = ""
    if " – " in rest:
        rest, cl = rest.split(" – ", 1)
        clause = " – " + DASH_CLAUSE[cl.strip()]
    toks = re.findall(r"…pe…|…|\s+|[^\s…]+", rest.strip())
    run_end = -1
    for j, tk in enumerate(toks):
        if S.lower_initials(tk) in COND_WORDS:
            run_end = j
        elif tk in ("…", "…pe…") or not tk.strip():
            continue
        else:
            break
    if run_end < 0:
        raise KeyError("no condition after the verb: " + m.group(0))
    chain = []
    for j, tk in enumerate(toks[: run_end + 1]):
        if not tk.strip():
            prev, nxt = toks[j - 1], toks[j + 1]
            chain.append(", " if prev in COND_WORDS and S.lower_initials(nxt) in COND_WORDS else tk)
        elif tk == "…pe…":
            chain.append("…")
        elif tk == "…":
            chain.append(tk)
        else:
            chain.append(S._cond_word(S.lower_initials(tk)))
    tail = rest_tokens_hi(toks[run_end + 1:])
    return f"{head} {''.join(chain)} {S.ARISES['p' if plural else 's']}{tail}{clause}"


DASH_CLAUSE = {   # sample formula: vicikicchāsahagate … khandhe paṭicca vicikicchāsahagato … moho
    "vicikicchāsahagate khandhe paṭicca vicikicchāsahagato moho":
        "संशय के साथ होने वाले समूहों पर निर्भर होकर संशय के साथ होने वाला मोह",
    "uddhaccasahagate khandhe paṭicca uddhaccasahagato moho":
        "बेचैनी के साथ होने वाले समूहों पर निर्भर होकर बेचैनी के साथ होने वाला मोह",
}


STATE = {"g": "fs"}


def panha_hi(text):
    m = re.search(r"(\w+)paccayena paccayo", text)
    pre = text[: m.start()].strip()
    parts = []
    if pre and pre != "…":
        toks = re.sub(r"(?i)\b(kenaci) ", r"\1", pre).split()
        i = next(k for k, t in enumerate(toks) if t.endswith("ssa"))
        subj, dat = " ".join(toks[:i]), " ".join(toks[i:])
        plural = "dhammā" in toks[:i] or len(parse_items(subj)) > 1
        STATE["g"] = "fp" if plural else "fs"
        parts.append(nom_hi(subj, plural) + ",")
        parts.append(dat_hi(dat))
        lead = ""
    else:
        lead = pre
        STATE["g"] = "fs"      # «…Xpaccayena paccayo»: elided subject, the series' first (singular) item
    rest = text[m.start():]
    g = STATE["g"]

    def ins(mm):
        k, neg = cond_key(mm.group(1))
        assert not neg
        return "⟪" + S.INS(k, g) + "⟫"

    rest = re.sub(r"(\w+)paccayena paccayo", ins, rest)
    for p, h in LABEL.items():
        rest = re.sub(rf"\b{p}\b", "⟪" + h + "⟫", rest)
    toks = re.findall(r"⟪[^⟫]*⟫|…pe…|…|\s+|[^\s…⟪]+", rest)
    out = []
    for tk in toks:
        if tk.startswith("⟪"):
            out.append(tk[1:-1])
        else:
            out.append(rest_tokens_hi([tk]))
    body = "".join(out)
    return lead + " ".join(parts + [body]) if parts else lead + body


def count_piece(piece):
    lead = piece[: len(piece) - len(piece.lstrip())]
    trail = piece[len(piece.rstrip()):]
    core = piece.strip()
    if not core or core in (",", "."):
        return piece.replace(".", "।")
    pre = post = ""
    if core.startswith(", "):
        pre, core = ", ", core[2:]
    if core.endswith(",") and not core.endswith(", "):
        post, core = ",", core[:-1]
    return lead + pre + S.count_hi(core) + post + trail


def is_count_sentence(s):
    for a, b in COUNT_SLIPS.items():
        s = s.replace(a, b)
    t = S.lower_initials(PH.sub(" ", s))
    t = re.sub(r"\s+", " ", t).strip().strip(",").strip()
    t = re.sub(r" ?, ?,", ",", t)
    return bool(t) and S.is_count(t.rstrip("."))


def count_sentence(s):
    for a, b in COUNT_SLIPS.items():
        s = s.replace(a, b)
    pieces = re.split(r"(⟦\d+⟧)", s)
    return "".join(p if PH.fullmatch(p) else count_piece(p) for p in pieces)


PAT_RE = re.compile(r"^(?P<obj>.+?) paṭicca (?P<subj>.+?) (?P<verb>uppajjati|uppajjanti)(?P<rest>.*)$")
CLOSE_RE = re.compile(r"^(\w+) niṭṭhitaṃ\.$")


def closing_name(w):
    w0 = w[0].lower() + w[1:]
    m = re.fullmatch(r"(\w+?)gocchaka(\w+)ttikaṃ", w0)
    if m:
        return GOCCHAKA[m.group(1)] + " और " + TIKA_NAME[m.group(2)]
    m = re.fullmatch(r"(\w+?)gocchakaṃ", w0)
    if m:
        return GOCCHAKA[m.group(1)]
    if w0 == "cūḷantaradukaṃ":
        return CULANTARA
    m = re.fullmatch(r"(\w+?)duka(\w+)ttikaṃ", w0)
    if m:
        return DUKA_NAME[m.group(1)] + " और " + TIKA_NAME[m.group(2)]
    raise KeyError("closing: " + w)


def sentence_hi(s):
    if not re.sub(r"⟦\d+⟧|\(\d+\)|[\s.]", "", s):      # only placeholders, counts like (1), spaces and "."
        return s.replace(".", "।")
    key = S.lower_initials(s.strip())
    if key in SENT:
        return SENT[key]
    k2 = re.sub(r" ?⟦\d+⟧", "", key)
    for p, h in SENT.items():
        if key.startswith(p):
            return h + rest_tokens_hi(re.findall(r"…pe…|…|\s+|[^\s…]+", key[len(p):].rstrip(".")))\
                + ("।" if key.endswith(".") else "")
    m = CLOSE_RE.match(s.strip())
    if m:
        return closing_name(m.group(1)) + " समाप्त।"
    if is_count_sentence(s):
        return count_sentence(s)
    end = ""
    core = s
    if core.endswith("."):
        end, core = "।", core[:-1]
    m = PAT_RE.match(core)
    if m:
        return paticca_hi(m) + end
    if "paccayena paccayo" in core:
        return panha_hi(core) + end
    raise KeyError("sentence: " + s + " | " + k2)


ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")


def translate_line(line):
    if line.startswith("#"):
        return heading(line)
    store = []

    def keep(m):
        store.append("(" + note_hi(m.group(1)) + ")")
        return f"⟦{len(store) - 1}⟧"

    text = re.sub(r"\(([^()]*[^\d().][^()]*)\)", keep, line)
    sents = re.split(r"(?<=\.) (?=\S)", text)
    hi = " ".join(sentence_hi(x) for x in sents)
    hi = re.sub(r"⟦(\d+)⟧", lambda mm: store[int(mm.group(1))], hi)
    hi = hi.replace("।।", "।")
    return hi


def build_file(name, write=True):
    src = os.path.join(PALI_DIR, name)
    lines = open(src, encoding="utf-8").read().split("\n")
    out, errors = [], []
    for n, ln in enumerate(lines, 1):
        if not ln.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        STATE["g"] = STATE.get("g", "fs")
        try:
            hi = translate_line(body)
        except (KeyError, AssertionError, StopIteration, AttributeError, IndexError) as e:
            errors.append(f"{name}:{n}: {type(e).__name__} {e}")
            hi = "!!" + body
        out.append(hi + (f" ^{m.group(1)}" if m else ""))
    while out and out[-1] == "":
        out.pop()
    if write:
        with open(os.path.join(OUT_DIR, name), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(out) + "\n")
    return errors


if __name__ == "__main__":
    write = "--check" not in sys.argv
    names = [a for a in sys.argv[1:] if not a.startswith("--")] or FILES
    allerr = []
    for nm in names:
        allerr += build_file(nm, write)
    for e in allerr:
        print(e)
    print("errors:", len(allerr), "| written" if write else "| not written")
