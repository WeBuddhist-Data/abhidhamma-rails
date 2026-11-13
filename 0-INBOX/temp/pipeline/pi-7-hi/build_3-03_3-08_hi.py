# -*- coding: utf-8 -*-
"""Hindi plain zero-shot builder for pi-7 files 3-03 .. 3-08 (dyad clusters: āsava, saṃyojana,
gantha, ogha-yoga, nīvaraṇa, parāmāsa).

Every line is composed from fixed frames (imported from build_sample_hi) and item tables, so the
same Pāli always gives the same Hindi.  A small phrase engine renders the example clauses after
" – " left to right (Pāli and Hindi share the order "X paṭicca Y" = "X पर निर्भर होकर Y").

    python -I -B -X utf8 build_3-03_3-08_hi.py            # write + report
    python -I -B -X utf8 build_3-03_3-08_hi.py --dry      # report only
"""
import re
import sys
import pathlib

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

PALI_DIR, HI_DIR = S.PALI_DIR, S.HI_DIR
FILES = {"3-03-asavagocchaka.md": "āsava", "3-04-sannojanagocchaka.md": "saññojana",
         "3-05-ganthagocchaka.md": "gantha", "3-06-oghayogagocchaka.md": "ogha",
         "3-07-nivaranagocchaka.md": "nīvaraṇa", "3-08-paramasagocchaka.md": "parāmāsa"}

DH, DH_PL = S.DHAMMA, S.DHAMMA_PL


class Err(Exception):
    pass


# =====================================================================================
# 1. Hindi morphology
# =====================================================================================
def agree(tpl, g, pl, obl):
    """Fill agreement slots: {a} (-ा/-े/-ी), {h} (हुआ/हुए/हुई), {k} (का/के/की)."""
    if g == "f":
        a, h, k = "ी", "हुई", "की"
    elif not pl and not obl:
        a, h, k = "ा", "हुआ", "का"
    else:
        a, h, k = "े", "हुए", "के"
    return tpl.replace("{a}", a).replace("{h}", h).replace("{k}", k)


class N:
    """Hindi noun: forms (dir sg, obl sg, dir pl, obl pl) and gender."""

    def __init__(self, dsg, osg=None, dpl=None, opl=None, g="m"):
        self.dsg = dsg
        self.osg = osg if osg is not None else dsg
        self.dpl = dpl if dpl is not None else dsg
        self.opl = opl if opl is not None else dsg + "ों"
        self.g = g

    def form(self, pl, obl):
        return (self.opl if obl else self.dpl) if pl else (self.osg if obl else self.dsg)


def NK(tpl_head, head_pl_obl, g="m", head_pl=None):
    """Noun of the shape '<X> का <head>' ('इंद्रिय-सुखों का मैल'): tpl uses {k}."""
    dsg = agree(tpl_head, g, False, False)
    osg = agree(tpl_head, g, False, True)
    dpl = agree(tpl_head, g, True, False)
    if head_pl is not None:
        dpl = dpl.rsplit(" ", 1)[0] + " " + head_pl
    opl = agree(tpl_head, g, True, True).rsplit(" ", 1)[0] + " " + head_pl_obl
    return N(dsg, osg, dpl, opl, g)


def NKA(word):
    """'आँख का इंद्रिय-क्षेत्र' -> oblique/plural 'आँख के इंद्रिय-क्षेत्र'."""
    a, b = word.rsplit(" का ", 1)
    o = f"{a} के {b}"
    return N(word, o, o, o + "ों")


def NF(sg, pl=None, opl=None):
    """Feminine noun (क्षमता / क्षमताएँ / क्षमताओं)."""
    return N(sg, sg, pl if pl else sg, opl if opl else sg + "ओं", "f")


# =====================================================================================
# 2. The cluster terms (pi-1 Hindi)
# =====================================================================================
GOCCHAKA = {
    # key: noun X, "rūpī" adjective base, oblique plural used before का विषय/से, pronoun for उनका
    "āsava": dict(noun=N("मन का मैल", "मन के मैल", "मन के मैल", "मन के मैलों"), rupi="मन के मैल रूपी",
                  obj="मन के मैलों", pron="उन", name="मन के मैलों का वर्ग", short="मन के मैल",
                  niya="sāsava", aniya="anāsava"),
    "saññojana": dict(noun=N("बंधन"), rupi="बंधन रूपी", obj="बंधनों", pron="उन", name="बंधनों का वर्ग",
                      short="बंधन", niya="saññojaniya", aniya="asaññojaniya"),
    "gantha": dict(noun=NF("गाँठ", "गाँठें", "गाँठों"), rupi="गाँठ रूपी", obj="गाँठों", pron="उन",
                   name="गाँठों का वर्ग", short="गाँठ", niya="ganthaniya", aniya="aganthaniya"),
    "ogha": dict(noun=NF("बाढ़", "बाढ़ें", "बाढ़ों"), rupi="बाढ़ रूपी", obj="बाढ़ों", pron="उन",
                 name="बाढ़ों का वर्ग", short="बाढ़", niya="oghaniya", aniya="anoghaniya"),
    "yoga": dict(noun=NF("जकड़न", "जकड़नें", "जकड़नों"), rupi="जकड़न रूपी", obj="जकड़नों", pron="उन",
                 name="जकड़नों का वर्ग", short="जकड़न", niya="yoganiya", aniya="ayoganiya"),
    "nīvaraṇa": dict(noun=NF("बाधा", "बाधाएँ", "बाधाओं"), rupi="बाधा रूपी", obj="बाधाओं", pron="उन",
                     name="बाधाओं का वर्ग", short="बाधा", niya="nīvaraṇiya", aniya="anīvaraṇiya"),
    "parāmāsa": dict(noun=NF("ग़लत धारणा", "ग़लत धारणाएँ", "ग़लत धारणाओं"), rupi="ग़लत धारणा रूपी",
                     obj="ग़लत धारणा", pron="उस", name="ग़लत धारणा का वर्ग", short="ग़लत धारणा",
                     niya="parāmaṭṭha", aniya="aparāmaṭṭha"),
}


def item_adj(g, key):
    """Agreement template of a dyad item (pi-1 1-matika.md wording)."""
    G = GOCCHAKA[g]
    r, o, p = G["rupi"], G["obj"], G["pron"]
    return {
        "X": r,
        "noX": f"{r} न होने वाल{{a}}",
        "niya": f"{o} का विषय बनने वाल{{a}}",
        "aniya": f"{o} का विषय न बनने वाल{{a}}",
        "samp": f"{o} से जुड़{{a}}",
        "vipp": f"{o} से अलग",
        "X_niya": f"{r} भी और {o} का विषय बनने वाल{{a}} भी",
        "niya_noX": f"{o} का विषय बनने वाल{{a}}, पर स्वयं {r} न होने वाल{{a}}",
        "X_samp": f"{r} भी और {o} से जुड़{{a}} भी",
        "samp_noX": f"{o} से जुड़{{a}}, पर स्वयं {r} न होने वाल{{a}}",
        "vipp_niya": f"{o} से अलग, पर {p}का विषय बनने वाल{{a}}",
        "vipp_aniya": f"{o} से अलग और {p}का विषय न बनने वाल{{a}}",
    }[key]


def item_stems(g):
    """Pāli stem -> item key for cluster g."""
    G = GOCCHAKA[g]
    return {g: "X", "no" + g: "noX", G["niya"]: "niya", G["aniya"]: "aniya",
            g + "sampayutta": "samp", g + "sampayuttaka": "samp", g + "vippayutta": "vipp",
            g + "vippayutta" + G["niya"]: "vipp_niya", g + "vippayutta" + G["aniya"]: "vipp_aniya"}


# dyad names (headings) "<X> वाला दो का वर्गीकरण"
def duka_name(g, key):
    G = GOCCHAKA[g]
    s, o = G["short"], G["obj"]
    x = {"X": s, "niya": f"{o} के विषय", "samp": f"{o} से जुड़ाव", "X_niya": f"{s} और {o} के विषय",
         "X_samp": f"{s} और {o} से जुड़ाव", "vipp_niya": f"{o} से अलगाव और {o} के विषय"}[key]
    return f"{x} वाला दो का वर्गीकरण"


# members of each cluster (pi-1 4-01/4-02 nikkhepakaṇḍa)
MEMBERS = {
    "kāmāsava": NK("इंद्रिय-सुखों {k} मैल", "मैलों"), "bhavāsava": NK("अस्तित्व {k} मैल", "मैलों"),
    "diṭṭhāsava": NK("दृष्टि {k} मैल", "मैलों"), "avijjāsava": NK("अज्ञान {k} मैल", "मैलों"),
    "kāmarāgasaññojana": NK("इंद्रिय-सुखों के राग {k} बंधन", "बंधनों"),
    "paṭighasaññojana": NK("चिढ़ {k} बंधन", "बंधनों"), "mānasaññojana": NK("अहंकार {k} बंधन", "बंधनों"),
    "diṭṭhisaññojana": NK("दृष्टि {k} बंधन", "बंधनों"), "vicikicchāsaññojana": NK("संशय {k} बंधन", "बंधनों"),
    "sīlabbataparāmāsasaññojana": NK("सदाचार और व्रतों के बारे में ग़लत धारणा {k} बंधन", "बंधनों"),
    "bhavarāgasaññojana": NK("अस्तित्व के राग {k} बंधन", "बंधनों"),
    "issāsaññojana": NK("ईर्ष्या {k} बंधन", "बंधनों"), "macchariyasaññojana": NK("कंजूसी {k} बंधन", "बंधनों"),
    "avijjāsaññojana": NK("अज्ञान {k} बंधन", "बंधनों"),
    "abhijjhākāyagantha": NF("लालच रूपी काया की गाँठ", "लालच रूपी काया की गाँठें", "लालच रूपी काया की गाँठों"),
    "byāpādakāyagantha": NF("दुर्भावना रूपी काया की गाँठ", "दुर्भावना रूपी काया की गाँठें",
                            "दुर्भावना रूपी काया की गाँठों"),
    "sīlabbataparāmāsakāyagantha": NF("सदाचार और व्रतों के बारे में ग़लत धारणा रूपी काया की गाँठ",
                                      "सदाचार और व्रतों के बारे में ग़लत धारणा रूपी काया की गाँठें",
                                      "सदाचार और व्रतों के बारे में ग़लत धारणा रूपी काया की गाँठों"),
    "idaṃsaccābhinivesakāyagantha": NF("“केवल यही सत्य है” के आग्रह रूपी काया की गाँठ",
                                       "“केवल यही सत्य है” के आग्रह रूपी काया की गाँठें",
                                       "“केवल यही सत्य है” के आग्रह रूपी काया की गाँठों"),
    "kāyagantha": NF("काया की गाँठ", "काया की गाँठें", "काया की गाँठों"),
    "kāmacchandanīvaraṇa": NF("इंद्रिय-सुखों की चाह की बाधा", "इंद्रिय-सुखों की चाह की बाधाएँ",
                              "इंद्रिय-सुखों की चाह की बाधाओं"),
    "byāpādanīvaraṇa": NF("दुर्भावना की बाधा", "दुर्भावना की बाधाएँ", "दुर्भावना की बाधाओं"),
    "thinamiddhanīvaraṇa": NF("आलस्य और तंद्रा की बाधा", "आलस्य और तंद्रा की बाधाएँ", "आलस्य और तंद्रा की बाधाओं"),
    "thīnamiddhanīvaraṇa": NF("आलस्य और तंद्रा की बाधा", "आलस्य और तंद्रा की बाधाएँ", "आलस्य और तंद्रा की बाधाओं"),
    "uddhaccanīvaraṇa": NF("बेचैनी की बाधा", "बेचैनी की बाधाएँ", "बेचैनी की बाधाओं"),
    "kukkuccanīvaraṇa": NF("पछतावे की बाधा", "पछतावे की बाधाएँ", "पछतावे की बाधाओं"),
    "vicikicchānīvaraṇa": NF("संशय की बाधा", "संशय की बाधाएँ", "संशय की बाधाओं"),
    "avijjānīvaraṇa": NF("अज्ञान की बाधा", "अज्ञान की बाधाएँ", "अज्ञान की बाधाओं"),
    "sīlabbataparāmāsa": NF("सदाचार और व्रतों के बारे में ग़लत धारणा", "सदाचार और व्रतों के बारे में ग़लत धारणाएँ",
                            "सदाचार और व्रतों के बारे में ग़लत धारणाओं"),
    "idaṃsaccābhinivesa": NK("“केवल यही सत्य है” {k} आग्रह", "आग्रहों"),
}

# =====================================================================================
# 3. Frames (dependent sections, pañhāvāra)
# =====================================================================================
ENDINGS = [("ānaṃ", "dat", True), ("assa", "dat", False), ("āni", "nom", True), ("aṃ", "acc", False),
           ("o", "nom", False), ("ā", "nom", True), ("e", "acc", True), ("ena", "ins", False)]
NO_SPLIT = {"pañca"}


def split_end(word):
    for e, case, pl in ENDINGS:
        if word.endswith(e):
            return word[: -len(e)] + "a", case, pl
    return None


def norm_ca(words):
    """'āsavañca' -> 'āsavaṃ', 'ca'; 'āsavañceva' -> 'āsavaṃ', 'ceva'."""
    out = []
    for w in words:
        if w in NO_SPLIT:
            out.append(w)
        elif w.endswith("ñceva"):
            out += [w[:-5] + "ṃ", "ceva"]
        elif w.endswith("ñca") and len(w) > 4:
            out += [w[:-3] + "ṃ", "ca"]
        else:
            out.append(w)
    return out


def parse_items(text, g):
    """'Āsavañceva sāsavañca sāsavañceva no ca āsavañca' -> (['X_niya', 'niya_noX'], case)."""
    w = norm_ca(text.split())
    w = [w[0][0].lower() + w[0][1:]] + w[1:]
    stems = item_stems(g)
    keys, case = [], None

    def st(word):
        r = split_end(word)
        if not r or r[0] not in stems:
            raise Err(f"item word {word!r} in {text!r}")
        return stems[r[0]], r[1]

    i = 0
    while i < len(w):
        k0, c0 = st(w[i])
        case = case or c0
        if i + 1 < len(w) and w[i + 1] == "ceva":
            if w[i + 2:i + 4] == ["no", "ca"]:
                k2, _ = st(w[i + 4])
                assert k2 == "X", text
                keys.append(f"{k0}_noX")
                i += 5
            else:
                k2, _ = st(w[i + 2])
                assert k0 == "X", text
                keys.append(f"X_{k2}")
                # source slip: the closing "ca" is sometimes missing (Āsavañceva āsavasampayuttaṃ)
                if i + 3 < len(w) and w[i + 3] == "ca":
                    i += 4
                else:
                    SLIPS.append(("missing closing 'ca' in item", text))
                    i += 3
        elif k0 == "vipp" and i + 1 < len(w) and w[i + 1] not in ("ca", "ceva") and \
                st(w[i + 1])[0] in ("niya", "aniya"):
            keys.append(f"vipp_{st(w[i + 1])[0]}")
            i += 2
        else:
            keys.append(k0)
            i += 1
        if i < len(w) and w[i] == "ca":
            i += 1
    return keys, case


def has_and(g, keys):
    return any(" और " in item_adj(g, k) or ", पर" in item_adj(g, k) for k in keys)


def OBJ(g, keys):
    j = " तथा " if has_and(g, keys) else " और "
    return j.join(agree(item_adj(g, k), "f", False, False) + " " + DH for k in keys)


def RES(g, keys, force_pl=False):
    if len(keys) == 1 and force_pl:
        # source slip: one item with plural "dhammā uppajjanti" -> plural as written
        return agree(item_adj(g, keys[0]), "f", True, False) + " " + DH_PL
    if len(keys) == 1:
        return agree(item_adj(g, keys[0]), "f", False, False) + " " + DH
    j = " तथा " if has_and(g, keys) else " और "
    return j.join(agree(item_adj(g, k), "f", True, False) for k in keys) + " " + DH_PL


def DAT(g, keys):
    return OBJ(g, keys) + " के लिए"


COND_RX = "(?:na|no)?(?:" + "|".join(sorted(S.COND_KEYS, key=len, reverse=True)) + ")paccayā"
DEP_WORDS = {"paṭicca": "paṭicca", "paccayā": "paccaya", "nissāya": "nissaya", "saṃsaṭṭho": "saṃsaṭṭha",
             "saṃsaṭṭhā": "saṃsaṭṭha", "sahajāto": "sahajāta", "sahajātā": "sahajāta",
             "sampayutto": "sampayutta", "sampayuttā": "sampayutta"}
FRAME_DEP = re.compile(
    r"(?P<acc>[^–;()]+?) dhammaṃ (?P<rel>" + "|".join(DEP_WORDS) + r") (?P<nom>[^–;()]+?) "
    r"(?P<dh>dhammo|dhammā) (?P<verb>uppajjati|uppajjanti)(?P<conds>(?: " + COND_RX + r")*)")
FRAME_PANHA = re.compile(
    r"(?P<nom>[^–;()]+?) (?P<dh>dhammo|dhammā) (?P<dat>[^–;()]+?) dhammassa "
    r"(?P<cond>(?:" + "|".join(sorted(S.COND_KEYS, key=len, reverse=True)) + r"))paccayena paccayo")


def cond_chain(s):
    out = []
    for c in s.split():
        neg = c.startswith(("na", "no")) and c[2:-len("paccayā")] in S.COND_KEYS
        k = c[2:-len("paccayā")] if neg else c[:-len("paccayā")]
        if k not in S.COND_KEYS:
            raise Err(f"condition {c}")
        out.append(S.NABL(k) if neg else S.ABL(k))
    return ", ".join(out)


def verb_v(g, pl):
    """होता है / होती है / होते हैं / होती हैं"""
    if g == "f":
        return "होती हैं" if pl else "होती है"
    return "होते हैं" if pl else "होता है"


def frame_dep(m, g):
    acc, _ = parse_items(m["acc"], g)
    nom, _ = parse_items(m["nom"], g)
    slip_pl = m["dh"] == "dhammā" and len(nom) == 1
    if m["dh"] == "dhammo" and len(nom) > 1:
        raise Err("number in frame " + m.group(0))
    if slip_pl:
        SLIPS.append(("plural dhammā uppajjanti with one item", m.group(0)[:90]))
    dep = S.DEP[DEP_WORDS[m["rel"]]]
    verb = "उत्पन्न होती हैं" if m["verb"] == "uppajjanti" else "उत्पन्न होती है"
    conds = m["conds"].strip()
    mid = f" {cond_chain(conds)}" if conds else ""
    return f"{OBJ(g, acc)} {dep} {RES(g, nom, slip_pl)}{mid} {verb}", ("f", len(nom) > 1 or slip_pl)


SLIPS = []


def frame_panha(m, g):
    src, _ = parse_items(m["nom"], g)
    dst, _ = parse_items(m["dat"], g)
    pl = len(src) > 1
    return f"{RES(g, src)}, {DAT(g, dst)} {S.INS(m['cond'])} {verb_v('f', pl)}", ("f", pl)


FRAME_PANHA0 = re.compile(r"(?P<nom>[^–;()]+?) (?P<dh>dhammo|dhammā) (?P<dat>[^–;()]+?) dhammassa(?= )")
FILE_STATE = {}


def frame_panha0(m, g):
    """Pañhā frame without the condition word (abbreviated in the source)."""
    src, _ = parse_items(m["nom"], g)
    dst, _ = parse_items(m["dat"], g)
    return f"{RES(g, src)}, {DAT(g, dst)}", ("f", len(src) > 1)


# =====================================================================================
# 4. Lexicon for the example clauses
# =====================================================================================
NOUN = {  # a-stem nouns (Pāli stem -> Hindi noun)
    "khandha": N("समूह"), "mahābhūta": N("महाभूत"), "moha": N("मोह"), "dosa": N("द्वेष"),
    "lobha": N("लोभ"), "rāga": N("राग"), "māna": N("अहंकार"), "paṭigha": NF("चिढ़", "चिढ़", "चिढ़"),
    "rūpa": N("भौतिक रूप"), "kilesa": N("मन का क्लेश", "मन के क्लेश", "मन के क्लेश", "मन के क्लेशों"),
    "āhāra": N("आहार"), "dhamma": NF("परिघटना", "परिघटनाएँ", "परिघटनाओं"), "magga": N("मार्ग"),
    "jhāna": N("ध्यान"), "phala": N("फल"), "nibbāna": N("निर्वाण"), "citta": N("मन"),
    "kaṭattārūpa": N(S.KTR), "upādārūpa": N(S.UPR), "dāna": N("दान"), "sīla": N("सदाचार"),
    "uposathakamma": N("उपवास-व्रत"), "senāsana": N("निवास-स्थान"), "bhojana": N("भोजन"),
    "vipāka_n": N("कर्म-फल"), "ariya": N("आर्य"), "gotrabhu": N(S.GOTRABHU), "vodāna": N(S.VODANA),
    "cakkhāyatana": NKA(S.AYA_SENSE("cakkhu")), "sotāyatana": NKA(S.AYA_SENSE("sota")),
    "ghānāyatana": NKA(S.AYA_SENSE("ghāna")), "jivhāyatana": NKA(S.AYA_SENSE("jivhā")),
    "kāyāyatana": NKA(S.AYA_SENSE("kāya")), "rūpāyatana": NKA(S.AYA_OBJ("rūpa")),
    "saddāyatana": NKA(S.AYA_OBJ("sadda")), "gandhāyatana": NKA(S.AYA_OBJ("gandha")),
    "rasāyatana": NKA(S.AYA_OBJ("rasa")), "phoṭṭhabbāyatana": NKA(S.AYA_OBJ("phoṭṭhabba")),
    "ākāsānañcāyatana": N(S.ARUPA_AYATANA["ākāsānañca"], S.ARUPA_OBL("ākāsānañca")),
    "viññāṇañcāyatana": N(S.ARUPA_AYATANA["viññāṇañca"], S.ARUPA_OBL("viññāṇañca")),
    "ākiñcaññāyatana": N(S.ARUPA_AYATANA["ākiñcañña"], S.ARUPA_OBL("ākiñcañña")),
    "nevasaññānāsaññāyatana": N(S.ARUPA_AYATANA["nevasaññānāsañña"], S.ARUPA_OBL("nevasaññānāsañña")),
    "cakkhuviññāṇa": NF(S.VINNANA("cakkhu")), "sotaviññāṇa": NF(S.VINNANA("sota")),
    "ghānaviññāṇa": NF(S.VINNANA("ghāna")), "jivhāviññāṇa": NF(S.VINNANA("jivhā")),
    "kāyaviññāṇa": NF(S.VINNANA("kāya")), "domanassa": NF("उदासी"), "uddhacca": NF("बेचैनी"),
    "vuṭṭhāna": N("उत्थान"), "lokuttara": N("लोकोत्तर"),
    "diṭṭhigatavippayuttalobha": N("ग़लत दृष्टि से अलग लोभ"),
}
NOUN.update(MEMBERS)

ADJ = {  # a-stem adjectives: Pāli stem -> (Hindi agreement template, class)
    "sampayuttaka": ("जुड़{a} {h}", ""), "sampayutta": ("जुड़{a} {h}", ""), "vippayuttaka": ("अलग", ""),
    "domanassasahagata": ("उदासी के साथ होने वाल{a}", "sah"),
    "vicikicchāsahagata": ("संशय के साथ होने वाल{a}", "sah"),
    "uddhaccasahagata": ("बेचैनी के साथ होने वाल{a}", "sah"),
    "lobhasahagata": ("लोभ के साथ होने वाल{a}", "sah"),
    "diṭṭhigatavippayuttalobhasahagata": ("ग़लत दृष्टि से अलग और लोभ के साथ होने वाल{a}", "sah"),
    "diṭṭhigatavippayutta": ("ग़लत दृष्टि से अलग", ""), "diṭṭhigatasampayutta": ("ग़लत दृष्टि से जुड़{a}", ""),
    "ahetuka": ("मूल से रहित", ""), "cittasamuṭṭhāna": ("मन से उत्पन्न", ""), "vipāka": ("कर्म के फल रूपी", ""),
    "pacchājāta": ("बाद में उत्पन्न", "pre"), "purejāta": ("पहले उत्पन्न", "pre"),
    "purima": ("पहले-पहले {k}", "dbl"), "pacchima": ("बाद-बाद {k}", "dbl"),
    "pahīna": ("छोड़{a} जा चुक{a}", ""), "vikkhambhita": ("दबाए जा चुके", ""),
    "kāyika": ("शारीरिक", ""),
}

# surface forms that are not regular a-stem forms: word -> (kind, value, case, plural)
SURF = {
    "vatthu": ("N", N(S.VATTHU), "nom", False), "vatthuṃ": ("N", N(S.VATTHU), "acc", False),
    "vatthussa": ("N", N(S.VATTHU), "dat", False),
    "hetū": ("N", N("मूल"), "nom", True), "hetu": ("N", N("मूल"), "nom", False),
    "cetanā": ("N", N("इरादा", "इरादे", "इरादे", "इरादों"), "nom", False),
    "adhipati": ("N", NF("प्रधानता", "प्रधानताएँ", "प्रधानताओं"), "nom", False),
    "indriyā": ("N", NF("क्षमता", "क्षमताएँ", "क्षमताओं"), "nom", True),
    "āhārā": ("N", N("आहार"), "nom", True), "āhāro": ("N", N("आहार"), "nom", False),
    "diṭṭhi": ("N", NF("दृष्टि"), "nom", False), "diṭṭhiṃ": ("N", NF("दृष्टि"), "acc", False),
    "vicikicchā": ("N", N("संशय"), "nom", False), "uddhaccaṃ": ("N", NF("बेचैनी"), "nom", False),
    "domanassaṃ": ("N", NF("उदासी"), "nom", False), "vipāko": ("N", N("कर्म-फल"), "nom", False),
    "saddhaṃ": ("N", NF("श्रद्धा"), "acc", False), "saddhā": ("N", NF("श्रद्धा"), "nom", False),
    "saddhāya": ("N", NF("श्रद्धा"), "dat", False), "paññaṃ": ("N", NF("प्रज्ञा"), "acc", False),
    "paññā": ("N", NF("प्रज्ञा"), "nom", False), "utuṃ": ("N", N("तापमान"), "acc", False),
    "patthanāya": ("N", NF("कामना"), "dat", False),
    "āvajjanā": ("N", N("मन को विषय की ओर मोड़ना", "मन को विषय की ओर मोड़ने"), "nom", False),
    "āvajjanāya": ("N", N("मन को विषय की ओर मोड़ना", "मन को विषय की ओर मोड़ने"), "dat", False),
    "phalasamāpattiyā": ("N", NF("फल की ध्यान-अवस्था"), "dat", False),
    "anulomaṃ": ("N", NF("अनुरूपता"), "nom", False),
    "rūpajīvitindriyaṃ": ("N", NF(S.RUPAJIVITINDRIYA), "nom", False),
    "cakkhundriyaṃ": ("N", NF(S.INDRIYA_SENSE("cakkhu")), "nom", False),
    "kāyindriyaṃ": ("N", NF(S.INDRIYA_SENSE("kāya")), "nom", False),
    "cakkhuṃ": ("N", N("आँख"), "acc", False),
    "kaṭattā": ("A", ("किए गए कर्म से उत्पन्न", ""), "any", None),
    "taṃ": ("PRON", None, "acc", False),
    "gotrabhussa": ("N", N(S.GOTRABHU), "dat", False), "gotrabhuṃ": ("N", N(S.GOTRABHU), "acc", False),
    "patthanaṃ": ("N", NF("कामना"), "acc", False), "patthanā": ("N", NF("कामना"), "nom", False),
    "vicikicchaṃ": ("N", N("संशय"), "acc", False), "diṭṭhiyā": ("N", NF("दृष्टि"), "dat", False),
    "paññāya": ("N", NF("प्रज्ञा"), "dat", False), "vipassanaṃ": ("N", NF("अंतर्दृष्टि"), "acc", False),
    "abhiññaṃ": ("N", N("उच्च ज्ञान"), "acc", False), "upanissayā": ("N", N("प्रबल आश्रय"), "nom", True),
    "samāpattiṃ": ("N", NF("ध्यान-अवस्था"), "acc", False),
    "jhānā": ("N", N("ध्यान"), "abl", False),
    "maggaṅgāni": ("N", N("मार्ग का अंग", "मार्ग के अंग", "मार्ग के अंग", "मार्ग के अंगों"), "nom", True),
    "jhānaṅgāni": ("N", N("ध्यान का अंग", "ध्यान के अंग", "ध्यान के अंग", "ध्यान के अंगों"), "nom", True),
}
SPELL = {  # pure spelling slips in the source, read as the word meant (listed in the notes)
    "parāmāsampayuttakānaṃ": "parāmāsasampayuttakānaṃ",
}
TXT = {"paṭisandhikkhaṇe": S.PATISANDHI, "ahetukapaṭisandhikkhaṇe": S.AHETUKA_PATISANDHI, "arūpe": S.ARUPE,
       "nānākkhaṇikā": "भिन्न क्षण", "ārammaṇādhipati": S.ARAMMANADHIPATI,
       "sahajātādhipati": S.SAHAJATADHIPATI}
NUMW = {"eko": "एक", "ekaṃ": "एक", "ekassa": "एक", "dve": "दो", "dvinnaṃ": "दो", "tayo": "तीन",
        "tiṇṇaṃ": "तीन", "tiṇṇannaṃ": "तीन", "tīṇi": "तीन", "cattāri": "चार", "pañca": "पाँच",
        "cha": "छह", "satta": "सात", "nava": "नौ"}
NUM_PL = {"दो", "तीन", "चार", "पाँच", "छह", "सात", "नौ"}

# governors: word(s) -> (postposition on the preceding object(s), text, reach)
#   reach: "grp" = the group of objects right before; "far" = also across "…" ; "one" = one NP
GOV = {
    ("paṭicca",): ("पर", "निर्भर होकर", "grp"), ("paccayā",): ("के", "कारण", "grp"),
    ("nissāya",): ("के", "आश्रय से", "grp"), ("saṃsaṭṭho",): ("से", "घुल-मिलकर", "grp"),
    ("saṃsaṭṭhā",): ("से", "घुल-मिलकर", "grp"), ("saṃsaṭṭhaṃ",): ("से", "घुल-मिलकर", "grp"),
    ("vipassati",): ("को", S.VIPASSATI, "far"), ("vipassanti",): ("को", S.VIPASSANTI, "far"),
    ("ārabbha",): ("को", "विषय बनाकर", "grp"), ("garuṃ", "katvā"): ("को", "महत्व देकर", "grp"),
    ("upanissāya",): ("के", "प्रबल आश्रय से", "grp"), ("garuṃ",): ("को", "महत्व", "grp"), ("vuṭṭhahitvā",): ("से", "उठकर", "one"),
    ("paccavekkhati",): ("पर", S.REVIEW_SG, "far"), ("paccavekkhanti",): ("पर", S.REVIEW_PL, "far"),
    ("assādeti",): ("का", "रस लेता है", "far"), ("jānāti",): ("को", "जानता है", "far"),
    ("jānanti",): ("को", "जानते हैं", "far"),
    ("aniccato", "dukkhato", "anattato", "vipassati"): ("को", f"{S.ANICCA3} {S.VIPASSATI}", "far"),
    ("aniccato", "dukkhato", "anattato", "vipassanti"): ("को", f"{S.ANICCA3} {S.VIPASSANTI}", "far"),
    ("aniccato",): ("को", "अनित्य के रूप में", "far"),
}

# fixed phrases: tuple of words -> unit
FIX = {
    ("dānaṃ", "datvā"): ("txt", "दान देकर"), ("sīlaṃ", "samādiyitvā"): ("txt", "सदाचार ग्रहण करके"),
    ("uposathakammaṃ", "katvā"): ("txt", "उपवास-व्रत का पालन करके"),
    ("dibbena", "cakkhunā", "rūpaṃ", "passati"): ("txt", "दिव्य आँख से दृश्य रूप देखता है"),
    ("dibbāya", "sotadhātuyā", "saddaṃ", "suṇāti"): ("txt", "दिव्य कान के तत्व से ध्वनि सुनता है"),
    ("pubbe", "suciṇṇāni"): ("np", N("पहले भली-भाँति किए गए कार्य", None, None, "पहले भली-भाँति किए गए कार्यों"),
                             "acc", True),
    ("purejātassa", "imassa", "kāyassa"): ("np", N("पहले उत्पन्न इस शरीर", "पहले उत्पन्न इस शरीर"), "dat", False),
    ("imassa", "kāyassa"): ("np", N("इस शरीर"), "dat", False),
    ("kabaḷīkāro", "āhāro"): ("np", N("कौर-कौर खाया जाने वाला भोजन"), "nom", False),
    ("cetopariyañāṇena",): ("txt", S.CETOPARIYENA),
    ("iddhividhañāṇassa", ",", "cetopariyañāṇassa", ",", "pubbenivāsānussatiñāṇassa", ",",
     "yathākammūpagañāṇassa", ",", "anāgataṃsañāṇassa", ",", "āvajjanāya"):
        ("txt", f"{S.IDDHIVIDHA_OBL}, {S.CETOPARIYA_OBL}, {S.PUBBENIVASA_OBL}, {S.YATHAKAMMUPAGA_OBL} और "
                f"{S.ANAGATAMSA_OBL} के लिए तथा {S.AVAJJANA_FOR}"),
    ("cetopariyañāṇassa", ",", "pubbenivāsānussatiñāṇassa", ",", "yathākammūpagañāṇassa", ",",
     "anāgataṃsañāṇassa", ",", "āvajjanāya"):
        ("txt", f"{S.CETOPARIYA_OBL}, {S.PUBBENIVASA_OBL}, {S.YATHAKAMMUPAGA_OBL} और "
                f"{S.ANAGATAMSA_OBL} के लिए तथा {S.AVAJJANA_FOR}"),
    ("iddhividhañāṇassa", ",", "cetopariyañāṇassa", ",", "pubbenivāsānussatiñāṇassa", ",",
     "yathākammūpagañāṇassa", ",", "anāgataṃsañāṇassa"):
        ("txt", f"{S.IDDHIVIDHA_OBL}, {S.CETOPARIYA_OBL}, {S.PUBBENIVASA_OBL}, {S.YATHAKAMMUPAGA_OBL} और "
                f"{S.ANAGATAMSA_OBL} के लिए"),
    ("cetopariyañāṇassa", ",", "pubbenivāsānussatiñāṇassa", ",", "yathākammūpagañāṇassa", ",",
     "anāgataṃsañāṇassa"):
        ("txt", f"{S.CETOPARIYA_OBL}, {S.PUBBENIVASA_OBL}, {S.YATHAKAMMUPAGA_OBL} और {S.ANAGATAMSA_OBL} के लिए"),
    ("jhānaṃ", "uppādeti"): ("txt", "ध्यान उत्पन्न करता है"),
    ("nirodhā", "vuṭṭhahantassa"): ("txt", "निरोध से उठने वाले व्यक्ति में"),
    ("ariyā", "maggā", "vuṭṭhahitvā"): ("txt", "आर्य मार्ग से उठकर"),
    ("ariyā", "maggā"): ("txt", "आर्य मार्ग से"),
    ("jhānā", "vuṭṭhahitvā"): ("txt", "ध्यान से उठकर"),
    ("maggā", "vuṭṭhahitvā"): ("txt", "मार्ग से उठकर"),
    ("dānaṃ", "deti"): ("txt", "दान देता है"), ("samāpattiṃ", "uppādeti"): ("txt", "ध्यान-अवस्था उत्पन्न करता है"),
    ("mānaṃ", "jappeti"): ("txt", "अहंकार करता है"), ("diṭṭhiṃ", "gaṇhāti"): ("txt", "दृष्टि को पकड़ता है"),
    ("saṅghaṃ", "bhindati"): ("txt", "संघ में फूट डालता है"), ("pāṇaṃ", "hanati"): ("txt", "प्राणी की हत्या करता है"),
    ("pubbe", "samudāciṇṇe"): ("adj", ("पहले बार-बार उठे", ""), "acc", True),
    ("kāyikaṃ", "sukhaṃ"): ("np", N("शारीरिक सुख"), "acc", False),
    ("kāyikaṃ", "dukkhaṃ"): ("np", N("शारीरिक दुःख"), "acc", False),
    ("kāyikassa", "sukhassa"): ("np", N("शारीरिक सुख"), "dat", False),
    ("kāyikassa", "dukkhassa"): ("np", N("शारीरिक दुःख"), "dat", False),
    ("pubbe",): ("txt", "पहले"),
}
LABEL = {  # sub-kinds of a condition, used as labels ("Sahajātā – …") and in lists
    "sahajātā": "सह-उत्पत्ति", "sahajāto": "सह-उत्पत्ति", "sahajātaṃ": "सह-उत्पत्ति",
    "purejātaṃ": "पूर्व-उत्पत्ति", "pacchājātā": "पश्चात्-उत्पत्ति", "pacchājātaṃ": "पश्चात्-उत्पत्ति",
    "pacchājāto": "पश्चात्-उत्पत्ति",
    "āhāraṃ": "आहार", "indriyaṃ": "क्षमता", "nānākkhaṇikā": "भिन्न क्षण",
    "ārammaṇādhipati": S.ARAMMANADHIPATI, "sahajātādhipati": S.SAHAJATADHIPATI,
    "ārammaṇapurejātaṃ": S.ARAMMANAPUREJATA, "vatthupurejātaṃ": S.VATTHUPUREJATA,
    "ārammaṇūpanissayo": S.ARAMMANUPANISSAYA, "anantarūpanissayo": S.ANANTARUPANISSAYA,
    "pakatūpanissayo": S.PAKATUPANISSAYA,
}
INS_RX = re.compile(r"^(" + "|".join(sorted(S.COND_KEYS, key=len, reverse=True)) + r")paccayena$")
A_END = [("ānaṃ", "dat", True), ("assa", "dat", False), ("āni", "nom", True), ("aṃ", "acc", False),
         ("o", "nom", False), ("ā", "nom", True), ("e", "acc", True)]


# =====================================================================================
# 5. Phrase engine
# =====================================================================================
TOK_RX = re.compile(r"…pe…|…|–|[,;.]|\{[^{}]*\}|[^\s,;.…–{}]+")


def tokenize(s):
    out = []
    for m in TOK_RX.finditer(s):
        sp = m.start() > 0 and s[m.start() - 1] == " "
        out.append([m.group(0), sp])
    return out


def analyze_word(w, g):
    """One Pāli word -> analysis dict (kind N/A/ITEM/NUM/PRON) or None."""
    w = SPELL.get(w, w)
    if w.startswith("ahetuka") and len(w) > 9:
        r = analyze_word(w[7:], g)
        if r and r["kind"] == "ITEM":
            return dict(kind="A", tpl="मूल से रहित, " + item_adj(g, r["key"]), cls="", case=r["case"],
                        pl=r["pl"], w=w)
    if w.endswith("cittasamaṅgissa"):
        st = w[: -len("cittasamaṅgissa")]
        stems = item_stems(g)
        if st in stems:
            adj = agree(item_adj(g, stems[st]), "m", False, True)
            return dict(kind="N", n=N(f"{adj} मन से युक्त व्यक्ति"), case="gen", pl=False, w=w)
    if w in SURF:
        kind, val, case, pl = SURF[w]
        if kind == "A":
            return dict(kind="A", tpl=val[0], cls=val[1], case=case, pl=pl, w=w)
        return dict(kind=kind, n=val, case=case, pl=pl, w=w)
    if w in NUMW:
        case = {"eko": "nom", "ekassa": "dat", "tiṇṇaṃ": "dat", "tiṇṇannaṃ": "dat",
                "dvinnaṃ": "dat", "ekaṃ": "acc"}.get(w, "any")
        return dict(kind="NUM", txt=NUMW[w], case=case, pl=NUMW[w] in NUM_PL, w=w)
    stems = item_stems(g)
    for e, case, pl in A_END:
        if w.endswith(e):
            st = w[: -len(e)] + "a"
            if st in stems:
                return dict(kind="ITEM", key=stems[st], case=case, pl=pl, w=w)
            if st in NOUN:
                return dict(kind="N", n=NOUN[st], case=case, pl=pl, w=w)
            if st in ADJ:
                return dict(kind="A", tpl=ADJ[st][0], cls=ADJ[st][1], case=case, pl=pl, w=w)
            if st.endswith("ādhipati") or w.endswith("ādhipati"):
                pass
    # X-ādhipati compounds: "āsavasampayuttādhipati" = adjective + प्रधानता
    if w.endswith("ādhipati"):
        st = w[: -len("ādhipati")]
        for cand in (st, st + "a"):
            if cand in stems:
                return dict(kind="ADHI", key=stems[cand], w=w)
            if cand in ADJ:
                return dict(kind="ADHI", tpl=ADJ[cand][0], w=w)
    return None


def first_units(tokens, g):
    """Tokens -> flat list of units (dicts)."""
    words = []
    for t, sp in tokens:
        if t in ("…pe…", "…", "–", ",", ";", ".") or t.startswith("{"):
            words.append((t, sp))
            continue
        low = t[0].lower() + t[1:]
        parts = norm_ca([low])
        for j, p in enumerate(parts):
            words.append((p, sp if j == 0 else True))
    # "sīlabbataparāmāsaṃ kāyaganthaṃ" (two words) = the one tie "sīlabbataparāmāsakāyaganthaṃ"
    merged = []
    for w, sp in words:
        if merged and w.startswith("kāyaganth") and \
                re.fullmatch(r"(sīlabbataparāmās|idaṃsaccābhinives)(aṃ|o|assa|ā|e)", merged[-1][0]):
            merged[-1] = (re.sub(r"(aṃ|o|assa|ā|e)$", "a", merged[-1][0]) + w, merged[-1][1])
            continue
        merged.append((w, sp))
    words = merged
    units = []
    i = 0
    stems = item_stems(g)
    while i < len(words):
        t, sp = words[i]
        if t in ("…pe…", "…"):
            units.append(dict(t="ell", sp=sp)); i += 1; continue
        if t in ("–", ",", ";", "."):
            units.append(dict(t="p", s=t, sp=sp)); i += 1; continue
        if t.startswith("{"):
            units.append(dict(t="var", s=t, sp=sp)); i += 1; continue
        if t in ("ca", "ceva"):
            # 'ca' follows the first word of a conjunct
            for u in reversed(units):
                if u["t"] == "w":
                    u["ca"] = True
                    break
                raise Err(f"stray ca in {' '.join(w for w, _ in words)}")
            i += 1
            continue
        nxt = words[i + 1][0] if i + 1 < len(words) else None
        # multiword governors and fixed phrases (longest first)
        hit = None
        for L in range(11, 0, -1):
            seq = tuple(w for w, _ in words[i:i + L])
            if len(seq) < L:
                continue
            if seq in GOV:
                hit = ("gov", GOV[seq], L)
                break
            if seq in FIX:
                hit = ("fix", FIX[seq], L)
                break
        if hit:
            kind, val, L = hit
            if kind == "gov":
                units.append(dict(t="gov", post=val[0], txt=val[1], reach=val[2], sp=sp, w=t))
            elif val[0] == "txt":
                units.append(dict(t="txt", s=val[1], sp=sp))
            elif val[0] == "np":
                units.append(dict(t="w", kind="N", n=val[1], case=val[2], pl=val[3], sp=sp, ca=False, w=t))
            elif val[0] == "adj":
                units.append(dict(t="w", kind="A", tpl=val[1][0], cls=val[1][1], case=val[2], pl=val[3],
                                  sp=sp, ca=False, w=t))
            i += L
            continue
        m = INS_RX.match(t)
        if m and nxt == "paccayo":
            units.append(dict(t="ins", k=m.group(1), sp=sp)); i += 2; continue
        if t in ("uppajjati", "uppajjanti"):
            units.append(dict(t="verb", sp=sp, w=t)); i += 1; continue
        if t in TXT:
            units.append(dict(t="txt", s=TXT[t], sp=sp)); i += 1; continue
        if re.fullmatch(COND_RX, t):
            units.append(dict(t="txt", s=cond_chain(t), sp=sp)); i += 1; continue
        if t in LABEL and (nxt is None or nxt in ("–", ",", ".", ";", "…pe…", "…")):
            units.append(dict(t="txt", s=LABEL[t], sp=sp)); i += 1; continue
        if t in NUMW and (nxt is None or nxt in ("–", ",", ".", ";", "…pe…", "…")):
            units.append(dict(t="txt", s=NUMW[t], sp=sp)); i += 1; continue
        # dyad item compounds with ceva
        r = split_end(t)
        if r and r[0] in stems and nxt == "ceva":
            k0 = stems[r[0]]
            ws = [w for w, _ in words[i:i + 5]]
            if ws[2:4] == ["no", "ca"] and ws[4].endswith("ādhipati"):
                units.append(dict(t="w", kind="ADHI", key=f"{k0}_noX", sp=sp, ca=False, w=t))
                i += 5
                continue
            if ws[2:4] == ["no", "ca"]:
                last = split_end(ws[4])
                key, L, case, pl = f"{k0}_noX", 5, last[1], last[2]
            else:
                k2 = stems[split_end(ws[2])[0]]
                key, L, case, pl = f"X_{k2}", 4, r[1], r[2]
            units.append(dict(t="w", kind="ITEM", key=key, case=case, pl=pl, sp=sp, ca=False, w=t))
            i += L
            continue
        a = analyze_word(t, g)
        if a is None:
            raise Err(f"unknown word {t!r}")
        if a["kind"] == "ITEM" and a["key"] == "vipp" and nxt:
            r2 = split_end(nxt)
            if r2 and r2[0] in stems and stems[r2[0]] in ("niya", "aniya"):
                a["key"] = "vipp_" + stems[r2[0]]
                i += 1
        a.update(t="w", sp=sp, ca=False)
        # doubled adjective (purimā purimā)
        if a["kind"] == "A" and a.get("cls") == "dbl" and nxt == t:
            i += 1
        units.append(a)
        i += 1
    return units


def compatible(np, a):
    c1, c2 = np["case"], a["case"]
    return c1 == "any" or c2 == "any" or c1 == c2


def group(units):
    """Join word units into noun phrases."""
    out, cur = [], None
    for u in units:
        if u["t"] != "w":
            cur = None
            out.append(u)
            continue
        if u["kind"] == "ADHI":
            # adjective + प्रधानता as one NP
            np = dict(t="np", adjs=[u], num=None, head=NF("प्रधानता", "प्रधानताएँ", "प्रधानताओं"),
                      case="nom", pl=False, ca=u["ca"], sp=u["sp"], post=None, obl=False, words=[u["w"]])
            out.append(np)
            cur = None
            continue
        lone_x = (cur is not None and len(cur["adjs"]) == 1 and cur["num"] is None and
                  cur["adjs"][0].get("key") == "X" and cur["adjs"][0].get("kind") == "ITEM")
        start_new = (cur is None or cur["head"] is not None or not compatible(cur, u) or
                     (u["ca"] and (u["kind"] not in ("N", "PRON") or cur["ca"] or lone_x)))
        if start_new:
            cur = dict(t="np", adjs=[], num=None, head=None, case=u["case"], pl=u["pl"], ca=u["ca"],
                       sp=u["sp"], post=None, obl=False, words=[])
            out.append(cur)
        cur["words"].append(u["w"])
        cur["ca"] = cur["ca"] or u["ca"]
        if cur["case"] == "any":
            cur["case"] = u["case"]
        if u["kind"] == "N":
            cur["head"] = u["n"]
            cur["pl"] = u["pl"]
        elif u["kind"] == "NUM":
            cur["num"] = u["txt"]
            if cur["pl"] is None:
                cur["pl"] = u["pl"]
        elif u["kind"] == "PRON":
            cur["head"] = "PRON"
            cur["pl"] = False
        else:
            cur["adjs"].append(u)
            if cur["pl"] is None:
                cur["pl"] = u["pl"]
    return out


def mark_roles(units):
    """Postpositions from governors and datives; obliques."""
    for i, u in enumerate(units):
        if u["t"] == "np" and u["case"] == "dat":
            u["obl"], u["post"] = True, "के लिए"
        if u["t"] == "np" and u["case"] == "gen":
            u["obl"], u["post"] = True, "के"
        if u["t"] == "np" and u["case"] == "abl":
            u["obl"], u["post"] = True, "से"
    for i, u in enumerate(units):
        if u["t"] != "gov":
            continue
        targets = []
        j = i - 1
        seg_last = True
        while j >= 0:
            v = units[j]
            if v["t"] == "np" and v["case"] in ("acc", "any", "nom") and not v.get("gov") and v["post"] is None:
                if u["reach"] != "far" and v["case"] == "nom" and u["post"] != "से":
                    break
                if u["reach"] == "far" and v["case"] == "nom":
                    break
                targets.append((v, seg_last))
                seg_last = False
                if u["reach"] == "one" or v["head"] == "PRON":
                    break
            elif v["t"] == "p" and v["s"] == "," and targets and u["reach"] == "far":
                pass
            elif v["t"] == "ell" and u["reach"] == "far" and targets:
                seg_last = True
            elif v["t"] == "var":
                pass
            else:
                break
            j -= 1
        u["targets"] = len(targets)
        for v, last in targets:
            v["gov"] = True
            v["obl"] = True
            if u["post"] == "से" and u["reach"] == "one":
                v["pl"] = False  # Pāli ablative singular in -ā (maggā vuṭṭhahitvā)
            if last:
                v["post"] = u["post"]


def np_text(np, g):
    head = np["head"]
    pl = bool(np["pl"])
    obl = np["obl"]
    adjs = np["adjs"]
    if head is None:
        # substantive use of the cluster word ("āsavā" = मन के मैल)
        if adjs and adjs[-1]["kind"] == "ITEM" and adjs[-1]["key"] == "X":
            head, adjs = GOCCHAKA[g]["noun"], adjs[:-1]
        elif adjs:
            # adjective(s) standing before "…" (pacchimānaṃ…pe…, ahetukaṃ ganthavippayuttaṃ…pe…):
            # the noun and its postposition are left out with it
            np["post"] = None
            return ", ".join(agree(item_adj(g, a["key"]) if "key" in a else a["tpl"], "m", pl, obl)
                             for a in adjs)
        else:
            raise Err(f"NP without noun: {np['words']}")
    if head == "PRON":
        base = "उस" if obl else "वह"
        post = np["post"]
        fused = {"को": "उसे", "का": "उसका", "में": "उसमें", "के": "उसके"}
        if post in fused:
            np["post"] = None
            return fused[post]
        return base
    gg = head.g
    texts, cls = [], []
    for a in adjs:
        tpl = item_adj(g, a["key"]) if "key" in a else a["tpl"]
        texts.append(agree(tpl, gg, pl, obl))
        cls.append(a.get("cls", ""))
    if len(texts) > 1 and all(c == "sah" for c in cls):
        adj = ", ".join(texts[:-1]) + (" और " if pl else " या ") + texts[-1]
    else:
        adj = texts[0] if texts else ""
        for k in range(1, len(texts)):
            adj += (" " if cls[k - 1] in ("dbl", "pre") else ", ") + texts[k]
    parts = [x for x in (adj, np["num"], head.form(pl, obl)) if x]
    return " ".join(parts)


def same_role(a, b):
    """Two noun phrases are members of one list (same case, same governor)."""
    da, db = a["case"] in ("dat", "gen"), b["case"] in ("dat", "gen")
    return da == db and bool(a.get("gov")) == bool(b.get("gov"))


def is_premod(np):
    if np["head"] is not None or not np["adjs"]:
        return False
    a = np["adjs"][-1]
    return not (a.get("kind") == "ITEM" and a.get("key") == "X")


def np_gender(np, g):
    head = np["head"]
    if head is None:
        head = GOCCHAKA[g]["noun"] if np["adjs"] and np["adjs"][-1].get("key") == "X" else None
    if head is None or head == "PRON":
        return "m", bool(np["pl"])
    return head.g, bool(np["pl"])


def subject_agr(units, i, mode):
    """Gender/number of the subject for the verb at index i."""
    if mode == "verb":
        j, run = i - 1, []
        while j >= 0 and units[j]["t"] in ("np", "p", "var") and not (units[j]["t"] == "p" and units[j]["s"] != ","):
            v = units[j]
            if v["t"] == "np":
                if v.get("gov") or v["post"]:
                    break
                run.append(v)
            j -= 1
        nps = run
    else:
        # nearest group of nominative noun phrases before the verb, skipping datives, "…" and fixed text
        j, nps = i - 1, []
        while j >= 0:
            v = units[j]
            free = v["t"] == "np" and not v.get("gov") and v["post"] is None
            if free:
                nps.append(v)
            elif nps and not (v["t"] == "p" and v["s"] == ","):
                break
            elif not nps and not (v["t"] in ("ell", "txt", "var") or (v["t"] == "p" and v["s"] == ",")
                                  or (v["t"] == "np" and v["post"] is not None)):
                break
            j -= 1
    if not nps:
        return None
    gens = [np_gender(v, G_CUR[0]) for v in nps]
    gen = "m" if any(x[0] == "m" for x in gens) else "f"
    pl = len(nps) > 1 or any(v["pl"] for v in nps)
    return gen, pl


G_CUR = ["āsava"]


def render(units, g, state):
    out = []  # list of [text, space_before]
    prev_np = None
    for i, u in enumerate(units):
        t = u["t"]
        if t == "np":
            nxt = units[i + 1] if i + 1 < len(units) else None
            if is_premod(u) and nxt is not None and nxt["t"] == "np":
                # adjectives without a noun before a (coordinated) noun phrase
                hg, hpl = np_gender(nxt, g)
                obl = nxt["obl"]
                texts = [agree(item_adj(g, a["key"]) if "key" in a else a["tpl"], hg, hpl, obl)
                         for a in u["adjs"]]
                txt = ", ".join(texts)
                if all("_" in a.get("key", "") for a in u["adjs"]) and nxt["ca"]:
                    nxt_txt = np_text(dict(nxt), g)
                    txt += " तथा" if (" और " in txt or " और " in nxt_txt or ", पर" in txt) else " और"
                nxt["ca"] = False
                nxt["premodded"] = True
                if prev_np is not None and u["ca"]:
                    out[-1][0] += " और"
                out.append([txt, True])
                prev_np = None
                continue
            txt = np_text(u, g)
            if u["post"]:
                txt += " " + u["post"]
            sep_add = None
            same = prev_np is not None and same_role(prev_np, u)
            if u.get("premodded") or not same:
                pass
            elif out and out[-1][0] == ",":
                if u["ca"] and not (nxt is not None and nxt["t"] == "np" and nxt["ca"] and same_role(u, nxt)):
                    out.pop()
                    sep_add = " और"
            elif out and out[-1][0] not in (";", "–", "…"):
                sep_add = " और" if u["ca"] else ","
            if sep_add == " और" and nxt is not None and nxt["t"] == "np" and nxt["ca"] and same_role(u, nxt):
                sep_add = ","  # only the last conjunct of a list takes "और"
            if sep_add:
                out[-1][0] += sep_add
            out.append([txt, True])
            prev_np = u
            continue
        if t == "gov":
            if u["targets"] == 0:
                # object understood (Pāli leaves it out): pronoun as in the sample ("उसे महत्व देकर उस पर …")
                if u["post"] in ("से",) or u["reach"] == "one":
                    raise Err("governor without object: " + u["w"])
                pl = state.get("obj_pl", False)
                pr = "उन" if pl else "उस"
                fused = {("उस", "को"): "उसे", ("उन", "को"): "उन्हें", ("उस", "का"): "उसका",
                         ("उन", "का"): "उनका", ("उस", "के"): "उसके", ("उन", "के"): "उनके"}
                obj = fused.get((pr, u["post"]), f"{pr} {u['post']}")
                out.append([f"{obj} {u['txt']}", True])
            else:
                tg = [v for v in units[:i] if v["t"] == "np" and v.get("gov")]
                state["obj_pl"] = u["targets"] > 1 or bool(tg and tg[-1]["pl"])
                out.append([u["txt"], True])
            if u["post"] == "का":
                # abhinandati follows
                pass
            prev_np = None
            continue
        prev_np = None if t not in ("p", "var") or (t == "p" and u["s"] != ",") else prev_np
        if t == "p":
            s = {"." : "।"}.get(u["s"], u["s"])
            if s == "–":
                out.append(["–", True])
            else:
                out.append([s, False])
        elif t == "ell":
            out.append(["…", u["sp"]])
        elif t == "var":
            out.append([var_text(u["s"]), True])
        elif t == "txt":
            out.append([u["s"], True])
        elif t == "verb":
            agr = subject_agr(units, i, "verb")
            if agr is None:
                raise Err("verb without subject")
            gg, pl = agr
            out.append(["उत्पन्न " + verb_v(gg, pl), True])
        elif t == "ins":
            agr = subject_agr(units, i, "ins") or state.get("frame")
            if agr is None:
                raise Err("paccayo without subject")
            out.append([f"{S.INS(u['k'])} {verb_v(*agr)}", True])
        elif t == "abhi":
            pl = state.get("obj_pl", False) if u["pl"] is None else u["pl"]
            out[-1][0] += f", {'उन' if pl else 'उस'}{S.ABHINANDA}"
        else:
            raise Err(f"unit {t}")
    return out


def var_text(s):
    m = re.fullmatch(r"\{(\S+) \((syā)\.\)\}", s)
    if not m:
        raise Err("variant " + s)
    return f"[वर्तनी-भेद (Syā.): {m.group(1)}]"


def pre_abhinandati(units):
    """'… assādeti abhinandati' -> ', उसमें/उनमें आनंद लेता है'."""
    out = []
    for i, u in enumerate(units):
        out.append(u)
    return out


def join_out(pieces):
    s = ""
    for txt, sp in pieces:
        if not s:
            s = txt
        elif txt in (",", ";", "।"):
            s += txt
        elif sp and not s.endswith((" ", "(")):
            s += " " + txt
        else:
            s += txt
    return s


def engine(chunk, g, state):
    G_CUR[0] = g
    toks = tokenize(chunk)
    # abhinandati: handled as its own token after assādeti
    kept = []
    for t in toks:
        if t[0] == "abhinandati":
            if kept and kept[-1][0] == ",":
                kept.pop()  # "assādeti, abhinandati": the Hindi already has ", उसमें आनंद लेता है"
            continue
        kept.append(t)
    units = first_units(kept, g)
    has_abhi = any(t[0] == "abhinandati" for t in toks)
    units = group(units)
    mark_roles(units)
    # abhinandati: insert after each assādeti governor
    if has_abhi:
        new = []
        for u in units:
            new.append(u)
            if u["t"] == "gov" and u["post"] == "का":
                pl = None
                tg = [v for v in new[:-1] if v["t"] == "np" and v.get("gov")]
                if u["targets"] and tg:
                    pl = u["targets"] > 1 or bool(tg[-1]["pl"])
                new.append(dict(t="abhi", pl=pl, sp=False))
        units = new
    pieces = render(units, g, state)
    s = join_out(pieces)
    return s.replace(" , ", ", ")


# =====================================================================================
# 6. Line translation
# =====================================================================================
PAREN = {}   # filled below (section 7)
LINE = {}    # whole-line translations (section 7)
HEAD = {}    # headings (section 7)


def paren_text(content, g):
    c = content.strip()
    if re.fullmatch(r"\d+", c):
        return f"({c})"
    key = c
    m = re.fullmatch(r"sabbattha (\S+)", c)
    if m and m.group(1) in S.NUM:
        return f"(हर जगह {S.NUM[m.group(1)]})"
    if key in PAREN:
        v = PAREN[key]
        return "(" + (v(g) if callable(v) else v) + ")"
    raise Err(f"paren {c!r}")


def body_line(text, g):
    """A body line (no heading, no ID) -> Hindi."""
    out = []
    state = FILE_STATE
    # split off parentheses
    parts = re.split(r"(\([^()]*\)(?!\}))", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("("):
            out.append(("paren", paren_text(part[1:-1], g)))
            continue
        out.append(("text", part))
    res = ""
    for kind, s in out:
        if kind == "paren":
            res = res.rstrip() + (" " if res.strip() else "") + s
            continue
        lead_sp = s.startswith(" ")
        hs = text_part(s.strip(), g, state)
        if res and lead_sp and hs and hs[0] not in "।,;":
            res += " " + hs
        else:
            res += hs
    return res


FRAME_START = re.compile(r"(^|(?<=– )|(?<=; )|(?<=\. )|(?<=\.\s))")


def text_part(s, g, state):
    """Translate a paren-free piece: frames at sentence starts, the rest through the engine."""
    if not s:
        return ""
    if s.lstrip(", ") != s and is_count(s.lstrip(", ")):
        # counting words after a parenthesis (", napacchājāte nava, …")
        return "," + " " + count_hi2(s.lstrip(", "), g) if s.startswith(",") else count_hi2(s, g)
    res = []
    rest = s
    while rest:
        m = FRAME_DEP.match(rest) or FRAME_PANHA.match(rest) or FRAME_PANHA0.match(rest)
        if m:
            fn = {FRAME_DEP: frame_dep, FRAME_PANHA: frame_panha, FRAME_PANHA0: frame_panha0}[m.re]
            hi, agr = fn(m, g)
            state["frame"] = agr
            res.append(hi)
            rest = rest[m.end():]
            continue
        # up to the next sentence start that holds a frame
        nxt = None
        for mm in re.finditer(r"(?:\. |; )", rest):
            tail = rest[mm.end():]
            if FRAME_DEP.match(tail) or FRAME_PANHA.match(tail):
                nxt = mm.end()
                break
        piece = rest if nxt is None else rest[:nxt]
        res.append(engine(piece, g, state))
        rest = "" if nxt is None else rest[nxt:]
    out = ""
    for r in res:
        if out and not out.endswith(" ") and r and r[0] not in "।,;…":
            out += " " + r
        else:
            out += r
    return out


def count_hi2(pali, g):
    """S.count_hi with any parenthesis: same rules (identical output on lines without parentheses);
    a parenthesis is translated by paren_text and takes no comma before it."""
    toks = re.findall(r"…pe…|…|\([^()]*\)|[,;.]|na [^\s,;.…()]+|[^\s,;.…()]+", pali)
    items = []
    for t in toks:
        if t in ("…pe…", "…"):
            items.append(("ell", "…"))
        elif t.startswith("("):
            items.append(("paren", t))
        elif t in ",;.":
            items.append(("punct", t))
        else:
            kind, v = S._classify(t.replace(" ", ""))
            if kind == "other":
                raise ValueError(f"unknown word in count line: {t!r}")
            items.append((kind, v))
    words = ("abl", "neg_abl", "loc", "neg_loc", "num")
    out = ""
    for i, (kind, v) in enumerate(items):
        nxt = items[i + 1][0] if i + 1 < len(items) else None
        if kind in words or kind == "paren":
            if kind == "paren":
                text = paren_text(v[1:-1], g) if g else v
            else:
                text = {"abl": S.ABL, "neg_abl": S.NABL, "loc": S.LOC, "neg_loc": S.NLOC}[kind](v) \
                    if kind in ("abl", "neg_abl", "loc", "neg_loc") else S.NUM[v]
            if kind in ("abl", "neg_abl", "num") and nxt in words:
                text += ","
            if out and not out.endswith(" "):
                out += " "
            out += text
        else:
            out = out.rstrip(" ").rstrip(",") + ("…" if kind == "ell" else ("।" if v == "." else v))
    return out.strip()


def count_line(text, g):
    return count_hi2(text, g)


def is_count(text):
    try:
        count_hi2(text, None)
        return True
    except ValueError:
        return False


def tr_line(line, g):
    m = S.ID_RX.search(line)
    text = S.ID_RX.sub("", line) if m else line
    if text.startswith("#"):
        hashes = len(text) - len(text.lstrip("#"))
        body = text[hashes:].strip()
        it = body.startswith("*") and body.endswith("*")
        core = body.strip("*")
        hi = head_text(core, g)
        return "#" * hashes + " " + (f"*{hi}*" if it else hi)
    if text in LINE:
        v = LINE[text]
        return v(g) if callable(v) else v
    if is_count(text):
        return count_line(text, g)
    return body_line(text, g)


def head_text(core, g):
    num = ""
    mm = re.match(r"^(\d+(?:-\d+)?\.\s)(.*)$", core)
    if mm:
        num, core = mm.group(1), mm.group(2)
    if core in HEAD:
        v = HEAD[core]
        return num + (v(g) if callable(v) else v)
    h = cluster_heading(core)
    if h:
        return num + h
    m = re.fullmatch(r"(na|no)?(" + "|".join(sorted(S.COND_KEYS, key=len, reverse=True)) +
                     r")paccay(o|ādi)", core[0].lower() + core[1:])
    if m:
        base = S.NNAME(m.group(2)) if m.group(1) else S.NAME(m.group(2))
        return base + (" आदि" if m.group(3) == "ādi" else "")
    raise Err(f"heading {core!r}")


def cluster_heading(core):
    """Āsavagocchakaṃ / Āsavadukaṃ / Sāsavadukaṃ / … for every cluster."""
    low = core[0].lower() + core[1:]
    for g, G in GOCCHAKA.items():
        if low == g + "gocchakaṃ":
            return G["name"]
        names = {g + "dukaṃ": "X", G["niya"] + "dukaṃ": "niya", g + "sampayuttadukaṃ": "samp",
                 g + G["niya"] + "dukaṃ": "X_niya", g + g + "sampayuttadukaṃ": "X_samp",
                 g + "vippayutta" + G["niya"] + "dukaṃ": "vipp_niya"}
        if low in names:
            return duka_name(g, names[low])
    return None


# =====================================================================================
# 7. Headings, whole lines, parentheses
# =====================================================================================
HEAD.update({
    "Paṭiccavāro": S.VARA["paṭicca"], "Sahajātavāro": S.VARA["sahajāta"], "Paccayavāro": S.VARA["paccaya"],
    "Nissayavāro": S.VARA["nissaya"], "Saṃsaṭṭhavāro": S.VARA["saṃsaṭṭha"],
    "Sampayuttavāro": S.VARA["sampayutta"], "Pañhāvāro": S.VARA["pañhā"],
    "Vibhaṅgavāro": S.VARA["vibhaṅga"], "Saṅkhyāvāro": S.VARA["saṅkhyā"],
    "Paccayānulomaṃ": S.PACCAYANULOMA, "Paccayapaccanīyaṃ": S.PACCAYAPACCANIYA,
    "Paccayānulomapaccanīyaṃ": S.PACCAYANULOMAPACCANIYA,
    "Paccayapaccanīyānulomaṃ": S.PACCAYAPACCANIYANULOMA,
    "Suddhaṃ": S.SUDDHA, "Hetudukaṃ": S.DUKANI("hetu"), "Nahetudukaṃ": S.DUKANI("hetu", neg=True),
    "Paccanīyuddhāro": "नकारात्मक क्रम के लिए चयन",
    "Paccayacatukkaṃ": "कारणों के चार क्रम", "Paccayānulomādi": S.PACCAYANULOMA + " आदि",
    "Paṭiccavārādi": S.VARA["paṭicca"] + " आदि", "Vārasattakaṃ": "सात खंड",
    "Sahajāta-paccaya-nissaya-saṃsaṭṭha-sampayuttavāro": "सह-उत्पत्ति, कारण, आश्रय, घुले-मिले होने और जुड़ाव के खंड",
    "Nissaya-saṃsaṭṭha-sampayuttavāro": "आश्रय, घुले-मिले होने और जुड़ाव के खंड",
    "Anantara-samanantarapaccayā": f"{S.NAME('anantara')} और {S.NAME('samanantara')}",
    "Pacchājāta-āsevanapaccayā": f"{S.NAME('pacchājāta')} और {S.NAME('āsevana')}",
    "Pacchājātāsevanapaccayā": f"{S.NAME('pacchājāta')} और {S.NAME('āsevana')}",
    "Vipākāhārapaccayā": f"{S.NAME('vipāka')} और {S.NAME('āhāra')}",
    "Oghādidukāni": "बाढ़ आदि वाले दो-दो के वर्गीकरण",
    "Oghayogagocchakaṃ": "बाढ़ों और जकड़नों के वर्ग",
})
LINE.update({
    "Anulomaṃ.": S.ANULOMA + "।", "Paccanīyaṃ.": S.PACCANIYA + "।",
    "Anulomapaccanīyaṃ.": S.ANULOMAPACCANIYA + "।", "Paccanīyānulomaṃ.": S.PACCANIYANULOMA + "।",
    # summary stanza in 3-07 (nīvaraṇa dyad, pañhāvāra)
    "Dvikkhattuṃ kāmacchandena, catukkhattuṃ paṭighena ca;": "इंद्रिय-सुखों की चाह से दो बार, और चिढ़ से चार बार;",
    "Uddhaccaṃ vicikicchā ca, ubhopete sakiṃ sakiṃ;": "बेचैनी और संशय, ये दोनों एक-एक बार;",
    "Nīvaraṇānaṃ nīvaraṇehi, aṭṭhavidhaṃ payojanaṃ.": "बाधाओं का बाधाओं से आठ प्रकार का प्रयोग है।",
})


_K = "करना चाहिए"
_KP = "करने चाहिए"
_NN = "बिना किसी अंतर के"
_SAM = "संक्षिप्त"
_LOK = "लौकिक वाला दो का वर्गीकरण"
_LOK_OBL = "लौकिक वाले दो के वर्गीकरण"
_CUL = "बीच के छोटे दो-दो के वर्गीकरणों में"
_V = {k: v for k, v in S.VARA.items()}
_SIX = (f"{_V['paṭicca']} भी, {_V['sahajāta']} भी, {_V['paccaya']} भी, {_V['nissaya']} भी, "
        f"{_V['saṃsaṭṭha']} भी और {_V['sampayutta']} भी")
_FIVE = (f"{_V['sahajāta']} भी, {_V['paccaya']} भी, {_V['nissaya']} भी, {_V['saṃsaṭṭha']} भी और "
         f"{_V['sampayutta']} भी")
_PS = "निर्भरता के खंड के समान"
_AV = S.AVAJJANA_FOR.replace(" के लिए", "")          # मन को विषय की ओर मोड़ने
_AVJ = "मन को विषय की ओर मोड़ना"
_GARU = "महत्व दिए गए विषय"
_ARS = S.SADISA("ārammaṇa")
PAREN.update({
    "saṃkhittaṃ": _SAM, "Saṃkhittaṃ.": _SAM + "।", "sabbattha nava, saṃkhittaṃ": f"हर जगह नौ, {_SAM}",
    "Arūpaṃyeva paccayaṃ, ekekassa tīṇi tīṇi kātabbā. Ārammaṇañca sahajātañca upanissayañca navasupi "
    "parivattetabbaṃ. Evaṃ pañhāvārepi sabbaṃ kātabbaṃ.":
        f"केवल अभौतिक को कारण बनाकर, हर एक के तीन-तीन {_KP}। {S.NAME('ārammaṇa')}, {S.NAME('sahajāta')} और "
        f"{S.NAME('upanissaya')} को नौ में भी उलट-पलट कर लगाना चाहिए। इसी तरह {_V['pañhā']} में भी सब {_K}।",
    "Avasesā pañhā sabbe vitthāretabbā. Arūpaṃ paṭhamaṃ kātabbaṃ, rūpaṃ pacchā yathā labhati.":
        f"बाकी सभी प्रश्नों का विस्तार {_K}। अभौतिक को पहले {_K}, भौतिक रूप को बाद में, जैसा मिलता हो।",
    "Cakkaṃ": "चक्र", "cakkaṃ": "चक्र", "Cakkaṃ. Evaṃ sabbe paccayā kātabbā.": f"चक्र। इसी तरह सभी कारण {_KP}।",
    "Cakkaṃ. Saṃkhittaṃ.": f"चक्र। {_SAM}।", "cakkaṃ. Saṃkhittaṃ": f"चक्र। {_SAM}",
    "cakkaṃ. Saṃkhittaṃ.": f"चक्र। {_SAM}।", "sabbaṃ cakkaṃ": "पूरा चक्र",
    "cakkaṃ bandhitabbaṃ": "चक्र जोड़ना चाहिए", "cakkaṃ bandhitabbaṃ. Saṃkhittaṃ": f"चक्र जोड़ना चाहिए। {_SAM}",
    "evaṃ cakkaṃ bandhitabbaṃ": "इसी तरह चक्र जोड़ना चाहिए", "ekekampi cakkaṃ kātabbaṃ": "एक-एक का भी चक्र बनाना चाहिए",
    "cakkaṃ. Sabbaṃ nīvaraṇaṃ vitthāretabbaṃ": f"चक्र। हर बाधा का विस्तार {_K}",
    "cakkaṃ. Sabbepi nīvaraṇā kātabbā": "चक्र। सभी बाधाएँ भी करनी चाहिए",
    "Cūḷantaraduke lokiyadukasadisaṃ, ninnānākaraṇaṃ.": f"{_CUL} {_LOK_OBL} के समान, {_NN}।",
    "Evaṃ imampi dukaṃ vitthāretabbaṃ, ninnānākaraṇaṃ ṭhapetvā lokuttaraṃ":
        f"इसी तरह इस दो के वर्गीकरण का भी विस्तार {_K}, {_NN}, लोकोत्तर को छोड़कर",
    "Evaṃ itare dve gaṇanāpi nissayavāropi kātabbo.": f"इसी तरह बाकी दो गणनाएँ भी और {_V['nissaya']} भी {_K}।",
    "Evaṃ itare dve gaṇanāpi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi "
    "sampayuttavārampi paripuṇṇaṃ paṭiccasadisā.":
        f"इसी तरह बाकी दो गणनाएँ भी, {_FIVE} पूरे-पूरे {_PS} हैं।",
    "Evaṃ itare dve gaṇanāpi sahajātavāropi kātabbo. Paccayavāropi nissayavāropi saṃsaṭṭhavāropi "
    "sampayuttavāropi paṭiccavārasadisā.":
        f"इसी तरह बाकी दो गणनाएँ भी और {_V['sahajāta']} भी {_K}। {_V['paccaya']} भी, {_V['nissaya']} भी, "
        f"{_V['saṃsaṭṭha']} भी और {_V['sampayutta']} भी {_PS} हैं।",
    "Evaṃ itare dve gaṇanāpi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi "
    "paṭiccavārasadisā.": f"इसी तरह बाकी दो गणनाएँ भी, {_FIVE} {_PS} हैं।",
    "Evaṃ itare dve gaṇanāpi sampayuttavāropi kātabbo.": f"इसी तरह बाकी दो गणनाएँ भी और {_V['sampayutta']} भी {_K}।",
    "Evaṃ itare dve gaṇanāpi sampayuttavārāpi kātabbā.":
        f"इसी तरह बाकी दो गणनाएँ भी और जुड़ाव के खंड भी {_KP}।",
    "Evaṃ itarepi dve gaṇanā ca nissayavāro ca kātabbo.": f"इसी तरह बाकी दो गणनाएँ और {_V['nissaya']} भी {_K}।",
    "Evaṃ itarepi tīṇi pañhā kātabbā ārammaṇasadisaṃyeva. Adhipatiyāpi anantarepi upanissayepi vibhāgo natthi.":
        f"इसी तरह बाकी तीन प्रश्न भी {_ARS} ही {_KP}। {S.LOC('adhipati')} भी, {S.LOC('anantara')} भी, "
        f"{S.LOC('upanissaya')} भी कोई विभाजन नहीं है।",
    "Evaṃ itarepi tīṇi ārabbha kātabbāni. Imaṃ dukaṃ parāmāsadukasadisaṃ. Lokuttaraṃ yahiṃ na labbhati "
    "tahiṃ na kātabbaṃ.":
        f"इसी तरह बाकी तीन भी विषय बनाकर {_KP}। यह दो का वर्गीकरण ग़लत धारणा वाले दो के वर्गीकरण के समान है। "
        f"जहाँ लोकोत्तर नहीं मिलता, वहाँ उसे नहीं {_K}।",
    "Evaṃ paṭiccavāropi sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi yathā "
    "āsavadukaṃ evaṃ kātabbaṃ, ninnānaṃ.":
        f"इसी तरह {_SIX} जैसे मन के मैल वाला दो का वर्गीकरण है, वैसे ही {_K}, {_NN}।",
    "Evaṃ sabbe gaṇanā vibhajitabbā, nīvaraṇadukasadisaṃ ninnānākaraṇaṃ.":
        f"इसी तरह सभी गणनाओं का विश्लेषण {_K}, बाधा वाले दो के वर्गीकरण के समान, {_NN}।",
    "Evaṃ sabbe paccayā vitthāretabbā. Saṃkhittaṃ.": f"इसी तरह सभी कारणों का विस्तार {_K}। {_SAM}।",
    "Evaṃ sahajātavāropi paccayavāropi nissayavāropi saṃsaṭṭhavāropi sampayuttavāropi paṭiccavārasadisā "
    "ninnānākaraṇā.": f"इसी तरह {_FIVE} {_PS} हैं, {_NN}।",
    "Gaṇanāpi sampayuttavāropi saṃsaṭṭhavārasadiso.":
        f"गणना भी और {_V['sampayutta']} भी घुले-मिले होने के खंड के समान है।",
    "Idha assādanā natthi": "यहाँ रस लेना नहीं है",
    "Idha nahetupaccayo natthi": f"यहाँ {S.NNAME('hetu')} नहीं है",
    "Imaṃ dukaṃ cūḷantaraduke lokiyadukasadisaṃ ninnānākaraṇaṃ.":
        f"यह दो का वर्गीकरण {_CUL} {_LOK_OBL} के समान है, {_NN}।",
    "Itare dve gaṇanāpi sampayuttavāropi kātabbo.": f"बाकी दो गणनाएँ भी और {_V['sampayutta']} भी {_K}।",
    "Mūlaṃ kātabbaṃ": "मूल वाक्य बनाना चाहिए", "Mūlaṃ kātabbaṃ.": "मूल वाक्य बनाना चाहिए।",
    "Mūlaṃ pucchitabbaṃ": "मूल वाक्य पूछना चाहिए", "Pucchitabbaṃ mūlaṃ": "मूल वाक्य पूछना चाहिए",
    "Mūlaṃ pucchitabbaṃ, tīṇipi upanissayā": "मूल वाक्य पूछना चाहिए, तीनों प्रबल आश्रय भी",
    "Mūlaṃ, tīṇipi upanissayā": "मूल वाक्य, तीनों प्रबल आश्रय भी",
    "Mūlā pucchitabbā": "मूल वाक्य पूछने चाहिए", "Tīsupi mūlā pucchitabbā": "तीनों में भी मूल वाक्य पूछने चाहिए",
    "Napacchājātapaccayā nava, naāsevanapaccayā nava.":
        f"{S.NABL('pacchājāta')} नौ, {S.NABL('āsevana')} नौ।",
    "Nissayavāro paccayavārasadiso": f"{_V['nissaya']} कारण के खंड के समान है",
    "Nissayavāro paccayavārasadiso.": f"{_V['nissaya']} कारण के खंड के समान है।",
    "Nissayavāropi paccayavārasadiso.": f"{_V['nissaya']} भी कारण के खंड के समान है।",
    "Nissayavāro paccayavārasadisova. Saṃsaṭṭhavāropi sampayuttavāropi nava pañhā kātabbā, rūpaṃ natthi.":
        f"{_V['nissaya']} कारण के खंड के समान ही है। घुले-मिले होने के खंड में भी और जुड़ाव के खंड में भी "
        f"नौ प्रश्न {_KP}, भौतिक रूप नहीं है।",
    "Nīvaraṇadukassa mātikā idha katā.": "बाधा वाले दो के वर्गीकरण की मूल सूची यहाँ बनाई गई है।",
    "Pañhāvāre hetupaccayepi ārammaṇapaccayepi lokuttaraṃ na kātabbaṃ, sekhā gotrabhuṃ paccavekkhanti, "
    "vodānaṃ paccavekkhantīti kātabbā. Adhipatipaccayampi sabbaṃ jānitvā kātabbaṃ.":
        f"{_V['pañhā']} में {S.LOC('hetu')} भी और {S.LOC('ārammaṇa')} भी लोकोत्तर को नहीं {_K}, "
        f"“{S.SEKKHA} {S.GOTRABHU} पर {S.REVIEW_PL}, {S.VODANA} पर {S.REVIEW_PL}” ऐसा {_K}। "
        f"{S.NAME('adhipati')} को भी पूरा जानकर {_K}।",
    "Paṭiccavārampi sahajātavārampi paccayavārampi nissayavārampi saṃsaṭṭhavārampi sampayuttavārampi "
    "ganthadukasadisaṃ ninnānākaraṇaṃ.": f"{_SIX} गाँठ वाले दो के वर्गीकरण के समान है, {_NN}।",
    "Sabbaṃ vitthāretabbaṃ": f"सबका विस्तार {_K}",
    "Sabbe vārā yathā parāmāsadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ.":
        f"सभी खंड जैसे ग़लत धारणा वाला दो का वर्गीकरण है, वैसे ही {_KP}, {_NN}।",
    "Sahajātavāro paṭiccavārasadiso": f"{_V['sahajāta']} {_PS} है",
    "Sahajātavāro paṭiccavārasadiso.": f"{_V['sahajāta']} {_PS} है।",
    "Sahajātavāropi evaṃ kātabbo.": f"{_V['sahajāta']} भी इसी तरह {_K}।",
    "Sahajātavāropi evaṃ vitthāretabbo": f"सह-उत्पत्ति के खंड का भी इसी तरह विस्तार {_K}",
    "Sahajātavāropi paṭiccavārasadiso.": f"{_V['sahajāta']} भी {_PS} है।",
    "Sampayuttavāro saṃsaṭṭhavārasadiso": f"{_V['sampayutta']} घुले-मिले होने के खंड के समान है",
    "Sampayuttavāropi saṃsaṭṭhavārasadiso.": f"{_V['sampayutta']} भी घुले-मिले होने के खंड के समान है।",
    "Saññojanagocchake paṭhamadukasadisaṃ.": "बंधनों के वर्ग में पहले दो के वर्गीकरण के समान।",
    "Saṃkhittaṃ. Evaṃ nava pañhā kātabbā. Tīsuyeva padesu parivattetabbā, nānākkhaṇikā natthi.":
        f"{_SAM}। इसी तरह नौ प्रश्न {_KP}। तीनों पदों में ही उलट-पलट {_K}, भिन्न क्षण नहीं है।",
    "Saṃkhittaṃ. Āsavagocchakasadisaṃ. Naārammaṇāpi sabbe uddharitabbā.":
        f"{_SAM}। मन के मैलों के वर्ग के समान। {S.NNAME('ārammaṇa')} वाले भी सभी निकालने चाहिए।",
    "Saṃsaṭṭhavāropi sampayuttavāropi evaṃ kātabbā.":
        f"{_V['saṃsaṭṭha']} भी और {_V['sampayutta']} भी इसी तरह {_KP}।",
    "Yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ.":
        f"जैसे {_CUL} {_LOK} है, वैसे ही {_K}, {_NN}।",
    "Yathā cūḷantaraduke lokiyadukaṃ evaṃ vibhajitabbaṃ ninnānākaraṇaṃ.":
        f"जैसे {_CUL} {_LOK} है, वैसे ही विश्लेषण {_K}, {_NN}।",
    "Yathā cūḷantaraduke lokiyadukaṃ evaṃ vitthāretabbaṃ ninnānākaraṇaṃ, saṃkhittaṃ.":
        f"जैसे {_CUL} {_LOK} है, वैसे ही विस्तार {_K}, {_NN}, {_SAM}।",
    "yathā cūḷantaraduke lokiyadukaṃ evaṃ vitthāretabbaṃ ninnānākaraṇaṃ":
        f"जैसे {_CUL} {_LOK} है, वैसे ही विस्तार {_K}, {_NN}",
    "anantarasadisaṃ, āvajjanāpi vuṭṭhānampi natthi":
        f"{S.SADISA('anantara')}, {_AVJ} भी नहीं है और उत्थान भी नहीं",
    "anulomagaṇanā": "सकारात्मक क्रम की गणना", "anulomamātikā": "सकारात्मक क्रम की मूल सूची",
    "anulomamātikā kātabbā": "सकारात्मक क्रम की मूल सूची बनानी चाहिए",
    "anulomamātikā vitthāretabbā": f"सकारात्मक क्रम की मूल सूची का विस्तार {_K}",
    "anulomapadā paripuṇṇā": "सकारात्मक क्रम के पद पूरे",
    "anulomapadāni gaṇitabbāni": "सकारात्मक क्रम के पद गिनने चाहिए",
    "anulomapadāni kātabbāni": f"सकारात्मक क्रम के पद {_KP}",
    "anulomapadāni paripuṇṇāni kātabbāni": f"सकारात्मक क्रम के पद पूरे-पूरे {_KP}",
    "arūpe sīlabbataparāmāso natthi, evaṃ nava pañhā kātabbā":
        f"{S.ARUPE} सदाचार और व्रतों के बारे में ग़लत धारणा नहीं है, इसी तरह नौ प्रश्न {_KP}",
    "dutiyagamanaṃ": "दूसरा क्रम", "dve pañhā kātabbā": f"दो प्रश्न {_KP}",
    "dve āvajjanā kātabbā, paṭhamo natthi": f"{_AVJ} दो जगह {_K}, पहला नहीं है",
    "dvepi gocchakā āsavagocchakasadisā ninnānākaraṇā": f"दोनों वर्ग मन के मैलों के वर्ग के समान हैं, {_NN}",
    "ekampi vuṭṭhānaṃ kātabbaṃ, majjhe": f"एक उत्थान भी {_K}, बीच में",
    "evaṃ avasesā cattāri pañhā kātabbā": f"इसी तरह बाकी चार प्रश्न {_KP}",
    "evaṃ dvepi kātabbā": f"इसी तरह दोनों भी {_KP}", "evaṃ gaṇetabbaṃ": "इसी तरह गिनना चाहिए",
    "evaṃ gaṇetabbaṃ, saṃkhittaṃ": f"इसी तरह गिनना चाहिए, {_SAM}",
    "evaṃ itarepi dve gaṇanā kātabbā": "इसी तरह बाकी दो गणनाएँ भी करनी चाहिए",
    "evaṃ itarepi tīṇi kātabbā": f"इसी तरह बाकी तीन भी {_KP}",
    "evaṃ itarepi tīṇi vitthāretabbā": f"इसी तरह बाकी तीनों का भी विस्तार {_K}",
    "evaṃ nava pañhā vitthāretabbā": f"इसी तरह नौ प्रश्नों का विस्तार {_K}",
    "evaṃ nava pañhā. Arūpāyeva kātabbā": f"इसी तरह नौ प्रश्न। केवल अभौतिक ही {_KP}",
    "evaṃ navapi tīsu padesu parivattetabbā": f"इसी तरह नौ को भी तीनों पदों में उलट-पलट {_K}",
    "evaṃ nīvaraṇamūle tīṇi": "इसी तरह बाधा से शुरू होने वाली शृंखला में तीन",
    "evaṃ pañca pañhā kātabbā": f"इसी तरह पाँच प्रश्न {_KP}",
    "evaṃ pañca pañhā kātabbā arūpeyeva, saṃsaṭṭhavāropi sampayuttavāropi evaṃ kātabbā":
        f"इसी तरह पाँच प्रश्न केवल अभौतिक लोक में ही {_KP}, {_V['saṃsaṭṭha']} भी और {_V['sampayutta']} भी "
        f"इसी तरह {_KP}",
    "evaṃ sabbattha kātabbaṃ": f"इसी तरह हर जगह {_K}", "evaṃ sabbaṃ gaṇetabbaṃ": "इसी तरह सब गिनना चाहिए",
    "evaṃ sabbaṃ vitthāretabbaṃ": f"इसी तरह सबका विस्तार {_K}",
    "evaṃ sabbe gaṇanā gaṇetabbā": "इसी तरह सभी गणनाएँ गिननी चाहिए", "evaṃ tīṇipi": "इसी तरह तीनों भी",
    "evaṃ vitthāretabbaṃ": f"इसी तरह विस्तार {_K}",
    "garukārammaṇā": _GARU, "garukārammaṇāyeva": f"{_GARU} ही",
    "idha purimā purimāti natthi": "यहाँ “पहले-पहले की” नहीं है",
    "imāsu tīsupi pañhāsu ārammaṇādhipatipi sahajātādhipatipi kātabbā":
        f"इन तीनों प्रश्नों में भी {S.ARAMMANADHIPATI} भी और {S.SAHAJATADHIPATI} भी करनी चाहिए",
    "nahetumūlakaṃ natthi": f"{S.MULAKA('hetu', neg=True)} नहीं है",
    "napurejāte vibhajantena arūpaṃ paṭhamaṃ kātabbaṃ, rūpaṃ yattha labbhati pacchā kātabbaṃ, paṭighañca "
    "arūpe natthi":
        f"{S.NLOC('purejāta')} विश्लेषण करते हुए अभौतिक को पहले {_K}, जहाँ भौतिक रूप मिलता है उसे बाद में {_K}, "
        f"और {S.ARUPE} चिढ़ नहीं है",
    "ninnānākaraṇaṃ, vibhajanā natthi. Ārammaṇasadisā": f"{_NN}, विश्लेषण नहीं है। {_ARS}",
    "nīvaraṇiyadukaṃ yathā lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ":
        f"{duka_name('nīvaraṇa', 'niya')} जैसे {_LOK} है, वैसे ही {_K}, {_NN}",
    "pacchājātā kātabbā": "पश्चात्-उत्पत्ति करनी चाहिए",
    "parāmaṭṭhadukaṃ yathā cūḷantaraduke lokiyadukaṃ evaṃ kātabbaṃ ninnānākaraṇaṃ":
        f"{duka_name('parāmāsa', 'niya')} जैसे {_CUL} {_LOK} है, वैसे ही {_K}, {_NN}",
    "paṭiccasadisaṃ": _PS, "paṭiccasadisā": _PS, "paṭiccavārasadisaṃ": _PS, "paṭiccavārasadiso": _PS,
    "paṭiccavārasadisā": _PS,
    "purejātaṃ ārammaṇasadisaṃ kusalākusalassa vibhajitabbaṃ":
        f"पूर्व-उत्पत्ति {_ARS} है, हितकर और हानिकर के लिए विश्लेषण {_K}",
    "sahajātasadisaṃ": S.SADISA("sahajāta"),
    "saṃkhittaṃ, evaṃ gaṇetabbaṃ": f"{_SAM}, इसी तरह गिनना चाहिए", "saṃkhittaṃ, evaṃ kātabbaṃ": f"{_SAM}, इसी तरह {_K}",
    "saṃkhittaṃ, vibhajitabbaṃ": f"{_SAM}, विश्लेषण {_K}", "saṃkhittaṃ, vitthāretabbaṃ": f"{_SAM}, विस्तार {_K}",
    "saṃkhittaṃ, āsavasadisaṃ": f"{_SAM}, मन के मैलों के समान",
    "saṃkhittaṃ. Vitthāretabbaṃ": f"{_SAM}। विस्तार {_K}",
    "tiṇṇampi ārammaṇādhipati, sahajātādhipatipi kātabbā, vibhajitabbā tīṇipi":
        f"तीनों में भी {S.ARAMMANADHIPATI}, {S.SAHAJATADHIPATI} भी करनी चाहिए, तीनों का भी विश्लेषण {_K}",
    "tīṇi": "तीन", "tīṇi upanissayā": "तीन प्रबल आश्रय",
    "tīṇi ārammaṇasadisā, garukārammaṇā kātabbā": f"तीन, {_ARS}, {_GARU} {_KP}",
    "tīṇi, garukārammaṇā": f"तीन, {_GARU}",
    "vatthu ca dassetabbaṃ": "आधार भी दिखाना चाहिए", "vibhajitabbaṃ": f"विश्लेषण {_K}",
    "vibhajitabbaṃ āsavasadisaṃ": f"विश्लेषण {_K}, मन के मैलों के समान",
    "vipākaṃ natthi": f"{S.NAME('vipāka')} नहीं है",
    "yattha yattha vatthu labbhati, tattha tattha ninnetabbaṃ": "जहाँ-जहाँ आधार मिलता है, वहाँ-वहाँ जोड़ना चाहिए",
    "yāva ajjhattikā mahābhūtā": "आंतरिक महाभूतों तक", "yāva asaññasattā": "पहचान-रहित प्राणियों तक",
    "yāva āsaññasattā": "पहचान-रहित प्राणियों तक",
    "yāva asaññasattā mahābhūtā": "पहचान-रहित प्राणियों के महाभूतों तक",
    "yāva asaññasattā, mahābhūtā": "पहचान-रहित प्राणियों तक, महाभूत",
    "yāva asaññasattā, saṃkhittaṃ": f"पहचान-रहित प्राणियों तक, {_SAM}",
    "yāva asaññasattā. Saṃkhittaṃ": f"पहचान-रहित प्राणियों तक। {_SAM}",
    "yāva mahābhūtā": "महाभूतों तक", "yāva paṭisandhi": "पुनर्जन्म तक",
    "yāva āvajjanā sabbaṃ kātabbaṃ": f"{_AV} तक सब {_K}", "yāva āvajjanā tāva kātabbā": f"{_AV} तक {_K}",
    "yāva āvajjanāya": f"{_AV} तक",
    "Ārabbha kātabbā. Imasmiṃ duke lokuttaraṃ natthi, ganthadukasadisaṃ, ninnānākaraṇaṃ. "
    "\"Ganthaniya\"nti niyāmetabbaṃ, magge nava pañhā kātabbā.":
        f"विषय बनाकर {_KP}। इस दो के वर्गीकरण में लोकोत्तर नहीं है, गाँठ वाले दो के वर्गीकरण के समान, {_NN}। "
        f"“गाँठों का विषय बनने वाली” ऐसा निश्चित {_K}, {S.LOC('magga')} नौ प्रश्न {_KP}।",
    "Ārammaṇapaccaye rūpaṃ natthi. Adhipatipaccayo hetusadiso, vicikicchāsaññojanaṃ natthi.":
        f"{S.LOC('ārammaṇa')} भौतिक रूप नहीं है। {S.NAME('adhipati')} {S.SADISA('hetu')} है, संशय का बंधन नहीं है।",
    "Ārammaṇasadisā adhipatipaccayā, purejātampi ārammaṇasadisaṃ. Upanissayepi lokuttaraṃ na kātabbaṃ. "
    "Saṃkhittaṃ, evaṃ vitthāretabbaṃ yathā nīvaraṇadukaṃ, evaṃ paccavekkhitvā kātabbaṃ.":
        f"{S.NAME('adhipati')} {_ARS} हैं, पूर्व-उत्पत्ति भी {_ARS} है। {S.LOC('upanissaya')} भी लोकोत्तर को "
        f"नहीं {_K}। {_SAM}, जैसे बाधा वाला दो का वर्गीकरण है, वैसे ही विस्तार {_K}, इसी तरह जाँचकर {_K}।",
    "Āsavadukepi anantaraṃ iminā sadisaṃ kātabbaṃ. Āvajjanāpi vuṭṭhānampi evaṃ samuddiṭṭhaṃ saṃkhittaṃ. "
    "Sabbaṃ paripuṇṇaṃ. Āsavadukasadisaṃ kātabbaṃ, ninnānaṃ.":
        f"मन के मैल वाले दो के वर्गीकरण में भी {S.NAME('anantara')} इसी के समान {_K}। {_AVJ} भी और उत्थान भी "
        f"इसी तरह बताया गया है, {_SAM}। सब पूरा है। मन के मैल वाले दो के वर्गीकरण के समान {_K}, {_NN}।",
    "ārabbha kātabbā": f"विषय बनाकर {_KP}",
    "ārabbha kātabbāni parāmāsadukasadisaṃ": f"विषय बनाकर {_KP}, ग़लत धारणा वाले दो के वर्गीकरण के समान",
    "ārabbhayeva kātabbā": f"विषय बनाकर ही {_KP}", "ārammaṇanayena kātabbā": f"विषय-कारण की विधि से {_KP}",
    "ārammaṇasadisaṃ": _ARS, "ārammaṇasadisaṃ, vipāko natthi": f"{_ARS}, कर्म-फल नहीं है",
    "ārammaṇasadisaṃyeva, vibhajanā natthi… tīṇi. Upanissayaṃ sabbaṃ kātabbaṃ":
        f"{_ARS} ही, विश्लेषण नहीं है… तीन। प्रबल आश्रय पूरा {_K}",
    "ārammaṇasadisā, garukārammaṇā": f"{_ARS}, {_GARU}",
    "ārammaṇasadisā, garukārammaṇā kātabbā": f"{_ARS}, {_GARU} {_KP}",
    "ārammaṇasadisāyeva, purimā purimāti kātabbā.": f"{_ARS} ही, “पहले-पहले की” ऐसा {_K}।",
    "ārammaṇādhipatiyeva": f"{S.ARAMMANADHIPATI} ही",
    "ārammaṇādhipatiyeva kātabbā": f"{S.ARAMMANADHIPATI} ही करनी चाहिए",
    "āsavamūlakaṃ tīṇi, paṭiccasadisā": f"मन के मैल से शुरू होने वाले तीन, {_PS}",
    "āsavasadisaṃ": "मन के मैलों के समान",
    "āvajjanāpi vuṭṭhānampi natthi": f"{_AVJ} भी नहीं है और उत्थान भी नहीं",
    "āvajjanāpi vuṭṭhānampi natthi, sabbattha purimā purimā kātabbā":
        f"{_AVJ} भी नहीं है और उत्थान भी नहीं, हर जगह “पहले-पहले की” {_K}",
    "Sahajātavāropi evaṃ vitthāretabbo.": f"सह-उत्पत्ति के खंड का भी इसी तरह विस्तार {_K}।",
})


# =====================================================================================
# 8. Build, check, write
# =====================================================================================
def build_file(fname, g, errors):
    ptxt = (PALI_DIR / fname).read_text(encoding="utf-8")
    FILE_STATE.clear()
    hi = []
    for n, line in enumerate([l for l in ptxt.splitlines() if l.strip()], 1):
        text = S.ID_RX.sub("", line)
        gg = g
        if fname.startswith("3-06") and re.search(r"\b[Yy]og", text):
            gg = "yoga"
        try:
            m = re.fullmatch(r"(\S+) niṭṭhitaṃ\.", text)
            if m:
                hi.append(head_text(m.group(1), gg) + " समाप्त।")
            else:
                hi.append(tr_line(line, gg))
        except Err as e:
            errors.append((fname, n, str(e), text))
            hi.append("@@ " + text)
        except Exception as e:  # noqa
            errors.append((fname, n, "EXC " + repr(e), text))
            hi.append("@@ " + text)
    return S.assemble(ptxt, hi)


def main():
    only = [a for a in sys.argv[1:] if a.endswith(".md")]
    errors = []
    outs = {}
    for fname, g in FILES.items():
        if only and fname not in only:
            continue
        outs[fname] = build_file(fname, g, errors)
    if errors:
        import collections
        kinds = collections.Counter(re.sub(r"'.*", "", e[2]) for e in errors)
        print("ERRORS", len(errors), dict(kinds))
        seen = collections.Counter()
        for f, n, msg, text in errors:
            seen[msg] += 1
            if seen[msg] == 1:
                print(f"{f}:{n}: {msg}")
    if "--dry" in sys.argv:
        return
    for fname, text in outs.items():
        with open(HI_DIR / fname, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("wrote", fname)


if __name__ == "__main__":
    main()
