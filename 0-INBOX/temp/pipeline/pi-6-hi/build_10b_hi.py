r"""pi-6 Yamaka, Indriyayamaka 10-07 .. 10-13: Hindi plain zero-shot builder.

usage: python -I -X utf8 build_10b_hi.py [file ...]
Every line is composed from fixed frames (build_sample_hi + the tables below);
an unknown line raises an error, so nothing is hand-typed.
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-hi")
import build_sample_hi as S  # noqa: E402

PALI_DIR = S.PALI_DIR
HI_DIR = S.HI_DIR
FILES = [f"10-{i:02d}-indriyayamaka.md" for i in range(7, 14)]

# ---------------------------------------------------------------- items (faculties)
IND = {
    "cakkhundriya": "आँख की क्षमता",
    "sotindriya": "कान की क्षमता",
    "ghānindriya": "नाक की क्षमता",
    "jivhindriya": "जीभ की क्षमता",
    "kāyindriya": "शरीर की क्षमता",
    "manindriya": "मन की क्षमता",
    "itthindriya": "स्त्रीत्व की क्षमता",
    "purisindriya": "पुरुषत्व की क्षमता",
    "jīvitindriya": "जीवन-क्षमता",
    "sukhindriya": "सुख की क्षमता",
    "dukkhindriya": "दुःख की क्षमता",
    "somanassindriya": "प्रसन्नता की क्षमता",
    "domanassindriya": "उदासी की क्षमता",
    "upekkhindriya": "समभाव की क्षमता",
    "saddhindriya": "श्रद्धा की क्षमता",
    "vīriyindriya": "उत्साह की क्षमता",
    "satindriya": "सजगता की क्षमता",
    "samādhindriya": "एकाग्रता की क्षमता",
    "paññindriya": "प्रज्ञा की क्षमता",
    "anaññātaññassāmītindriya": "“जो अब तक नहीं जाना उसे मैं जान लूँगा” की क्षमता",
    "aññindriya": "पूर्ण ज्ञान की क्षमता",
    "aññātāvindriya": "पूर्ण ज्ञान पा चुके की क्षमता",
}
# "(Cakkhundriyamūlakaṃ)" = "(आँख की क्षमता पर आधारित)"
MULAKA = "({X} पर आधारित)"
MULAKA_SLIPS = {"Ghānandriya": "ghānindriya"}


def ind(tok):
    """'cakkhundriyaṃ' / 'cakkhundriyañca' / 'itthindriyaṃ…pe… purisindriyaṃ' -> Hindi."""
    if "… " in tok:
        return "… ".join(ind(t) for t in re.split(r"…(?:pe…)? ", tok))
    m = re.fullmatch(r"(\w+?ndriy)(?:aṃ|añca|a)", tok)
    if not m or m.group(1) + "a" not in IND:
        raise KeyError(tok)
    return IND[m.group(1) + "a"]


def mulaka_tag(t):
    m = re.fullmatch(r"\((\w+?)mūlakaṃ\)", t)
    if not m:
        return None
    k = m.group(1)
    k = MULAKA_SLIPS.get(k, k[0].lower() + k[1:])
    return MULAKA.format(X=IND[k])


# ---------------------------------------------------------------- short answers
NATTHI = "ऐसा कोई नहीं है"          # Natthi. (no such case)
NO = "नहीं"                        # No. (pi-2)
SHORT = {"Āmantā": "हाँ", "No": NO, "Natthi": NATTHI}
for _p, (_pos, _neg) in S.VERBS_F.items():
    SHORT[_p[0].upper() + _p[1:]] = _pos
    SHORT["N" + _p] = _neg

# ---------------------------------------------------------------- beings / places / moments
# notes-10a.md is binding: a WHO phrase that build_10a_hi.tr_who translates is taken from it
# unchanged (identical Pāli = identical Hindi across the chapter). Phrases it cannot parse go
# through my_who below, which uses the same chunk conventions and constants and only adds
# the vocabulary of 10-07..10-13 (notes-10b.md).
import build_10a_hi as A  # noqa: E402

PLACE = {   # stem -> Hindi noun (oblique, before में / से)
    "pañcavokār": "पाँच समूहों वाले अस्तित्व",
    "catuvokār": "चार समूहों वाले अस्तित्व",
    "kāmāvacar": "इंद्रिय-सुखों के लोक",
    "rūpāvacar": "सूक्ष्म भौतिक लोक",
    "arūpāvacar": "अभौतिक लोक",
    "arūp": "अभौतिक लोक",
    "suddhāvās": "शुद्ध निवास लोक",
    "asaññasatt": "पहचान-रहित प्राणियों के लोक",
}
_PL = "|".join(sorted(PLACE, key=len, reverse=True))
PLACE_JOIN = " या "                                   # as A.REL_PLACE (rūpāvacaraṃ arūpāvacaraṃ)
DYING_FROM = "{P} से मरने वालों में"                   # Xā cavantānaṃ
PARINIB_IN = "{P} में पूर्ण निर्वाण पाने वालों में"     # Xe parinibbantānaṃ
BORN_INTO = "{P} में"                                  # Xṃ upapajjantānaṃ (before जन्म लेने …)
SABBESAM_UPAPAJJANTANAM = "सभी जन्म लेने वालों में"    # Sabbesaṃ upapajjantānaṃ
# resumptive correlative after a relative clause (replaces ", उनमें")
RESUM = {"upapajjantānaṃ": ", उन जन्म लेने वालों में", "upapajjantīnaṃ": ", उन जन्म लेने वाली स्त्रियों में",
         "cavantānaṃ": ", उन मरने वालों में", "cavantīnaṃ": ", उन मरने वाली स्त्रियों में"}
# yassa cittassa anantarā Cpacchimacittaṃ uppajjissati tassa cittassa …kkhaṇe
ANANTARA_MOMENT = "जिस मन के ठीक बाद {C}अंतिम मन उत्पन्न होगा, उस मन के {M}"
MIND_KIND = {"upapatti": "जन्म के", "pacchima": "अंतिम"}


def places(txt, end):
    out = []
    for w in txt.split():
        if not w.endswith(end) or w[: -len(end)] not in PLACE:
            raise KeyError(w)
        out.append(PLACE[w[: -len(end)]])
    return PLACE_JOIN.join(out)


def citta_ext(comp):
    """A.citta_compound + an optional final upapatti-/pacchima-."""
    m = re.fullmatch(r"(.*?)(upapatti|pacchima)?", comp)
    c, kind = m.groups()
    parts = [p for p in (A.citta_compound(c), MIND_KIND.get(kind, "")) if p]
    return " ".join(parts)


def my_who(who):
    w = who[0].lower() + who[1:]
    w = re.sub(r"cavantāna$", "cavantānaṃ", w)                      # slip (10-08)
    w = w.replace("purisānaṃ uppajjantānaṃ", "purisānaṃ upapajjantānaṃ")  # slip (10-11)
    chunks, plain = [], True
    rest = w
    while rest:
        rest = rest.strip()
        if rest.startswith("ca "):
            rest = rest[3:]
        m = re.match(r"((?:ye|yā) .*?parinibbāyissanti)(?: |$)", rest)
        if m:
            cl = m.group(1).replace("ye ca ", "ye ").replace("yā ca ", "yā ")
            chunks.append(A.tr_relative(cl)); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"(tesaṃ|tāsaṃ) (upapajjantānaṃ|upapajjantīnaṃ|cavantānaṃ|cavantīnaṃ)(?: |$)", rest)
        if m and chunks and chunks[-1].endswith(A.TESAM):
            chunks[-1] = chunks[-1][: -len(A.TESAM)] + RESUM[m.group(2)]
            rest = rest[m.end():]; continue
        m = re.match(r"yassa cittassa anantarā (\S*?)pacchimacittaṃ uppajjissati tassa cittassa (uppāda|bhaṅga)kkhaṇe(?: |$)", rest)
        if m:
            c = A.citta_compound(m.group(1)).replace("जुड़े", "जुड़ा")
            mom = A.CITTA_UPPADA if m.group(2) == "uppāda" else A.CITTA_BHANGA
            chunks.append(ANANTARA_MOMENT.format(C=c + " " if c else "", M=mom.replace("मन के ", "")))
            plain = False; rest = rest[m.end():]; continue
        m = re.match(r"yassa cittassa anantarā (\S+?)pacchimacittaṃ uppajjissati(?: |$)", rest)
        if m:
            chunks.append(A.ANANTARA.format(C=A.citta_compound(m.group(1)).replace("जुड़े", "जुड़ा")) + A.TESAM)
            plain = False; rest = rest[m.end():]; continue
        m = re.match(r"sabbesaṃ cavantānaṃ(?: |$)", rest)
        if m:
            chunks.append(A.SABBESAM_CAVANTANAM); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"sabbesaṃ upapajjantānaṃ(?: |$)", rest)
        if m:
            chunks.append(SABBESAM_UPAPAJJANTANAM); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"sabbesaṃ cittassa bhaṅgakkhaṇe(?: |$)", rest)
        if m:
            chunks.append(A.SABBESAM + " " + A.CITTA_BHANGA); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"suddhāvāsānaṃ upapatticittassa (uppāda|bhaṅga)kkhaṇe(?: |$)", rest)
        if m:
            mom = A.UPAPATTI_UPPADA if m.group(1) == "uppāda" else A.UPAPATTI_UPPADA.replace(A.CITTA_UPPADA, A.CITTA_BHANGA)
            chunks.append(A.PLAIN["suddhāvāsānaṃ"] + " में " + mom); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"(pavatte )?(\S*?)cittassa (uppādakkhaṇe|bhaṅgakkhaṇe)(?: |$)", rest)
        if m:
            pav, comp, k = m.groups()
            c = citta_ext(comp)
            s = (A.PAVATTE + " " if pav else "") + (c + " " if c else "") + (A.CITTA_UPPADA if k == "uppādakkhaṇe" else A.CITTA_BHANGA)
            chunks.append(s); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"suddhāvāsānaṃ dutiye citte vattamāne(?: |$)", rest)
        if m:
            chunks.append(A.SUDDHAVASA_DUTIYE); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"(?:itaresaṃ|itarāsaṃ)((?: (?:kāmāvacarānaṃ|pañcavokārānaṃ|catuvokārānaṃ|rūpāvacarānaṃ|arūpāvacarānaṃ))*)(?: |$)", rest)
        if m:
            realms = m.group(1).split()
            if realms:
                chunks.append(A.ITARA.format(R=" और ".join(A.ITARA_REALM[r] for r in realms)))
            else:
                chunks.append(A.ITARESAM)
            plain = False; rest = rest[m.end():]; continue
        m = re.match(rf"((?:(?:{_PL})ā )+)cavantānaṃ(?: |$)", rest)
        if m:
            chunks.append(DYING_FROM.format(P=places(m.group(1), "ā"))); plain = False; rest = rest[m.end():]; continue
        m = re.match(rf"((?:(?:{_PL})e )+)parinibbantānaṃ(?: |$)", rest)
        if m:
            chunks.append(PARINIB_IN.format(P=places(m.group(1), "e"))); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"(somanassa|upekkhā)sampayuttapacchimacittasamaṅgīnaṃ(?: |$)", rest)
        if m:
            c = A.citta_compound(m.group(1) + "sampayutta")
            chunks.append(c + " " + A.PLAIN["pacchimacittasamaṅgīnaṃ"] + " में"); plain = False; rest = rest[m.end():]; continue
        # birth chunk (A's frame) with an optional destination: mods [na] [itthīnaṃ|purisānaṃ] [Xṃ …] upapajjantānaṃ
        m = re.match(r"((?:(?:vinā )?\S+ )*?)(upapajjantānaṃ|upapajjantīnaṃ)(?: |$)", rest)
        if m:
            toks = m.group(1).split()
            dest = []
            while toks and re.fullmatch(rf"(?:{_PL})aṃ", toks[-1]):
                dest.insert(0, toks.pop())
            if all((t in A.MODS or t in ("itthīnaṃ", "purisānaṃ", "na", "vinā")) for t in toks):
                mods, gender = [], None
                i = 0
                while i < len(toks):
                    t = toks[i]
                    if t == "vinā":
                        mods.append(A.MODS["vinā " + toks[i + 1]]); i += 2; continue
                    if t == "na":
                        gender = "not_" + toks[i + 1]; i += 2; continue
                    if t in ("itthīnaṃ", "purisānaṃ"):
                        gender = t; i += 1; continue
                    mods.append(A.MODS[t]); i += 1
                mod = " और ".join(mods)
                d = (BORN_INTO.format(P=places(" ".join(dest), "aṃ")) + " ") if dest else ""
                if gender == "itthīnaṃ":
                    s = (mod + " " if mod else "") + d + A.BORN_F
                elif gender == "purisānaṃ":
                    s = (mod + " " if mod else "") + d + A.BORN_M
                elif gender in ("not_itthīnaṃ", "not_purisānaṃ"):
                    s = (mod + ", " if mod else "") + (A.NOT_F if gender == "not_itthīnaṃ" else A.NOT_M) + " " + d + A.BORN
                else:
                    s = (mod + " " if mod else "") + d + A.BORN
                chunks.append(s); plain = False; rest = rest[m.end():]; continue
        m = re.match(r"(\S+)(?: |$)", rest)
        if m and m.group(1) in A.PLAIN:
            chunks.append(A.PLAIN[m.group(1)] + " में"); rest = rest[m.end():]; continue
        raise KeyError("WHO: " + who + " | at: " + rest)
    if plain and len(chunks) > 1:
        bare = [c[:-len(" में")] for c in chunks]
        return A.join(bare) + " में"
    return A.join(chunks)


def who_text(who):
    try:
        return A.tr_who(who)[0]
    except KeyError:
        return my_who(who)


def who_hi(who, loc):
    return who_text(who) + A.LOC1[loc]


LOC2 = A.LOC2
_LOC = r"tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tattha"


# plural verb with a singular faculty subject (source slip): rendered singular
FV_SLIPS = {"uppajjissanti": "uppajjissati"}


def _fv_fix(tok):
    for k, v in FV_SLIPS.items():
        if tok.endswith(k):
            return tok[: -len(k)] + v
    return tok


def fv(tok):
    return S.verb(_fv_fix(tok), S.VERBS_F)


def fv_flip(tok):
    return S.verb_flip(_fv_fix(tok), S.VERBS_F)


_V = r"(?:na |n)?(?:uppajj|nirujjh)(?:ati|ittha|issati|issanti)"


def tr_answer(sent):
    m = re.fullmatch(rf"(.+?) ({_LOC}) (\S+ndriyaṃ) ({_V}),? no ca ({_LOC}) (\S+ndriyaṃ) ({_V})", sent)
    if m:
        who, l1, x, v1, l2, y, v2 = m.groups()
        return S.ANS_BUT.format(WHO=who_hi(who, l1), L1="", X=ind(x), V1=fv(v1)[0],
                                L2=LOC2[l2], Y=ind(y), V2=fv_flip(v2))
    # (one source line lacks the first "ca": manindriyaṃ uppajjissati cakkhundriyañca …)
    m = re.fullmatch(rf"(.+?) ({_LOC}) (\S+ndriy(?:añca|aṃ)) ({_V}) (\S+ndriyañca) ({_V})", sent)
    if m:
        who, l1, x, v1, y, v2 = m.groups()
        return S.ANS_BOTH.format(WHO=who_hi(who, l1), L1="", X=ind(x), V1=fv(v1)[0],
                                 Y=ind(y), V2=fv(v2)[0])
    return None


def tr_pavatti_q(label, body):
    m = re.fullmatch(rf"([Yy]assa|[Yy]attha)( vā pana)?( yattha)? (.+?) ({_V}),? (tassa tattha|tassa|tattha) (.+?) ({_V})\?", body)
    if not m:
        return None
    rel, vp, rel2, x, v1, cor, y, v2 = m.groups()
    rel = rel.lower() + (rel2 or "")
    out = S.PAVATTI_Q.format(AND=S.VA_PANA if vp else "", REL=S.Q_REL[rel], X=ind(x), V1=fv(v1)[0],
                             COR=S.Q_COR[cor], Y=ind(y), V2=fv(v2)[0])
    return (S.LABELS[label] + " " if label else "") + out


# ---------------------------------------------------------------- Pariññāvāra (10-13)
# verb stem -> (prefix, root, object marker)
PV = {
    "parijān": ("पूरी तरह", "समझ", "को"),
    "pajah": ("", "छोड़", "को"),
    "bhāv": ("अभ्यास", "कर", "का"),
    "sacchikar": ("साक्षात्कार", "कर", "का"),
}
PERF = {"समझ": "समझा", "छोड़": "छोड़ा", "कर": "किया"}
# Pāli ending -> (tense, plural)
PV_END = [
    (r"parijānāti|pajahati|bhāveti|sacchikaroti", "pres", False),
    (r"parijānanti|pajahanti|bhāventi|sacchikaronti", "pres", True),
    (r"parijānittha|pajahittha|bhāvittha|sacchikarittha", "past", None),
    (r"parijānissati|pajahissati|bhāvessati|sacchikarissati", "fut", False),
    (r"parijānissanti|pajahissanti|bhāvessanti|sacchikarissanti", "fut", True),
]
PV_SLIPS = {"nappajjahittha": "nappajahittha", "bhavissanti": "bhāvessanti"}


def pv_parse(tok):
    """'na parijānāti' / 'nappajahati' -> (stem, tense, plural, neg)."""
    tok = PV_SLIPS.get(tok, tok)
    neg = False
    if tok.startswith("na "):
        neg, tok = True, tok[3:]
    elif tok.startswith("nappajah"):
        neg, tok = True, tok[3:]
    for rx, tense, pl in PV_END:
        if re.fullmatch(rx, tok):
            stem = next(k for k in PV if tok.startswith(k))
            return stem, tense, pl, neg
    raise KeyError(tok)


def pv_form(stem, tense, pl, neg):
    pre, root, _ = PV[stem]
    p = (pre + " ") if pre else ""
    n = "नहीं " if neg else ""
    if tense == "pres":
        v = root + ("ते" if pl else "ता") + ("" if neg else (" हैं" if pl else " है"))
    elif tense == "past":
        v = PERF[root] + " था"
    else:
        v = root + ("ेंगे" if pl else "ेगा")
    return p + n + v


def pv_clause(obj, verbtok, pl_override=None, also=False):
    stem, tense, pl, neg = pv_parse(verbtok)
    if pl_override is not None:
        pl = pl_override
    marker = PV[stem][2]
    return f"{ind(obj)} {marker}{' भी' if also else ''} {pv_form(stem, tense, pl, neg)}", tense


NUM = {"Dve": "दो", "Tayo": "तीन", "Cattāro": "चार", "Pañca": "पाँच", "Cha": "छह", "Satta": "सात", "Aṭṭha": "आठ"}
NUM_LOW = {k.lower(): v for k, v in NUM.items()}
AGGAMAGGA = "सर्वोच्च मार्ग से युक्त व्यक्ति"
ANAGAMIMAGGA = "फिर न लौटने के मार्ग से युक्त व्यक्ति"
ATTHAMAKA = "आठवें स्तर का व्यक्ति"
ATTHAMAKA_OBL = "आठवें स्तर के व्यक्ति"
MAGGASAMANGINO = "{N} मार्गों से युक्त व्यक्ति"   # as 7b (Dvinnaṃ maggasamaṅgīnaṃ)
ARAHA = "अर्हत्"
ANAGAMI = "फिर न लौटने वाला"
ANAGAMI_OBL = "फिर न लौटने वाले"
EXCEPT_REST = "{X} को छोड़कर शेष व्यक्ति"   # X ṭhapetvā avasesā puggalā


def _v(sigla, pali):
    sig = ", ".join(x.strip().capitalize() for x in sigla.split(" ") if x.strip())
    return S._var(S.VAR_READ, sig, pali)


def except_obj(x):
    """Pāli object of ṭhapetvā -> Hindi (oblique)."""
    m = re.fullmatch(r"(Dve|Tayo|Cattāro) maggasamaṅgino(?: ca)?(?: \[(.+?) \((.+?)\)\])?", x)
    if m:
        n, vp, vs = m.groups()
        out = MAGGASAMANGINO.format(N=NUM[n]).replace("व्यक्ति", "व्यक्तियों")
        if vp:
            out += " " + _v(vs, vp)
        return out
    m = re.fullmatch(r"(Aggamaggasamaṅgiñca|Anāgāmimaggasamaṅgiñca|Aṭṭhamakañca|Tayo maggasamaṅgino ca) arahantañca", x)
    if m:
        a = {"Aggamaggasamaṅgiñca": AGGAMAGGA, "Anāgāmimaggasamaṅgiñca": ANAGAMIMAGGA,
             "Aṭṭhamakañca": ATTHAMAKA_OBL,
             "Tayo maggasamaṅgino ca": MAGGASAMANGINO.format(N="तीन").replace("व्यक्ति", "व्यक्तियों")}[m.group(1)]
        return f"{a} और {ARAHA}"
    raise KeyError("except: " + x)


def subject(s):
    """Pāli subject of a Pariññā answer -> (nom, erg, plural, pron_nom, pron_erg)."""
    m = re.fullmatch(r"(Dve|Tayo|Cattāro|Pañca|Cha|Satta|Aṭṭha|pañca)(?: \[(\S+) \((.+?)\)\])? puggalā", s)
    if m:
        n, vp, vs = m.groups()
        num = NUM_LOW[n.lower()]
        var = (" " + _v(vs, vp)) if vp else ""
        return f"{num}{var} व्यक्ति", f"{num}{var} व्यक्तियों ने", True, "वे", "उन्होंने"
    m = re.fullmatch(r"Tayo maggasamaṅgino(?: \[(.+?) \((.+?)\)\])?", s)
    if m:
        vp, vs = m.groups()
        base = MAGGASAMANGINO.format(N="तीन")
        var = (" " + _v(vs, vp)) if vp else ""
        return base + var, base.replace("व्यक्ति", "व्यक्तियों") + var + " ने", True, "वे", "उन्होंने"
    m = re.fullmatch(r"(.+?) ṭhapetvā avasesā puggalā", s)
    if m:
        base = EXCEPT_REST.format(X=except_obj(m.group(1)))
        return base, base.replace("शेष व्यक्ति", "शेष व्यक्तियों") + " ने", True, "वे", "उन्होंने"
    sg = {"Arahā": (ARAHA, ARAHA),
          "Anāgāmī": (ANAGAMI, ANAGAMI_OBL),
          "Aggamaggasamaṅgī": (AGGAMAGGA, AGGAMAGGA),
          "Anāgāmimaggasamaṅgī": (ANAGAMIMAGGA, ANAGAMIMAGGA),
          "anāgāmimaggasamaṅgi": (ANAGAMIMAGGA, ANAGAMIMAGGA),
          "Aṭṭhamako": (ATTHAMAKA, ATTHAMAKA_OBL)}
    if s in sg:
        nom, obl = sg[s]
        return nom, obl + " ने", False, "वह", "उसने"
    m = re.fullmatch(r"Yo aggaphalaṃ (sacchikaroti|sacchākāsi) so", s)
    if m:
        rel = {"sacchikaroti": ("जो", "करता है"), "sacchākāsi": ("जिसने", "कर लिया है")}[m.group(1)]
        base = f"{rel[0]} सर्वोच्च फल का साक्षात्कार {rel[1]},"
        return base + " वह", base + " उसने", False, "वह", "उसने"
    m = re.fullmatch(r"Ye puthujjanā maggaṃ (na )?paṭilabhissanti te", s)
    if m:
        base = "जो साधारण व्यक्ति मार्ग " + ("प्राप्त नहीं करेंगे" if m.group(1) else "प्राप्त करेंगे") + ","
        return base + " वे", base + " उन्होंने", True, "वे", "उन्होंने"
    raise KeyError("subject: " + s)


_PVV = r"(?:na |n)?\S+"


def tr_parinna_answer(sent):
    m = re.fullmatch(rf"(.+?) (\S+ndriyaṃ) ((?:na )?[^\s,]+),? no ca (\S+ndriyaṃ) ((?:na )?\S+)", sent)
    if m:
        subj, x, v1, y, v2 = m.groups()
        nom, erg, pl, pn, pe = subject(subj)
        c1, t1 = pv_clause(x, v1, pl)
        # "no ca … V": the opposite polarity
        stem, tense2, _, neg2 = pv_parse(v2)
        marker = PV[stem][2]
        c2 = f"{ind(y)} {marker} {pv_form(stem, tense2, pl, not neg2)}"
        s1 = erg if t1 == "past" else nom
        p2 = pe if tense2 == "past" else pn
        return f"{s1} {c1}, पर {p2} {c2}"
    m = re.fullmatch(rf"(.+?) (\S+ndriyañca) ((?:na )?\S+) (\S+ndriyañca) ((?:na )?\S+)", sent)
    if m:
        subj, x, v1, y, v2 = m.groups()
        nom, erg, pl, pn, pe = subject(subj)
        c1, t1 = pv_clause(x, v1, pl, also=True)
        c2, t2 = pv_clause(y, v2, pl, also=True)
        s1 = erg if t1 == "past" else nom
        e1, e2 = t1 == "past", t2 == "past"
        p2 = "" if e1 == e2 else ((pe if e2 else pn) + " ")
        return f"{s1} {c1} और {p2}{c2}"
    return None


def tr_parinna_q(label, body):
    m = re.fullmatch(rf"[Yy]o( vā pana)? (\S+ndriyaṃ) ((?:na )?\S+?)\.? [Ss]o (\S+ndriyaṃ) ((?:na )?\S+?)(?:ti)?[?.]", body)
    if not m:
        return None
    vp, x, v1, y, v2 = m.groups()
    v2 = re.sub(r"ī$", "i", re.sub(r"ā$", "a", v2))
    c1, t1 = pv_clause(x, v1)
    c2, t2 = pv_clause(y, v2)
    rel = "जिसने" if t1 == "past" else "जो"
    cor = "उसने" if t2 == "past" else "वह"
    out = f"{S.VA_PANA if vp else ''}{rel} {c1}, क्या {cor} {c2}?"
    return (S.LABELS[label] + " " if label else "") + out


# ---------------------------------------------------------------- headings / fixed lines
HEADINGS = dict(S.HEADINGS)
HEADINGS.update({
    "Pariññāvāro": "पूरी तरह समझने का खंड",
    "Paccuppannavāro": "वर्तमान का खंड",
    "Atītavāro": "अतीत का खंड",
    "Anāgatavāro": "भविष्य का खंड",
    "Paccuppannātītavāro": "वर्तमान और अतीत का खंड",
    "Paccuppannānāgatavāro": "वर्तमान और भविष्य का खंड",
    "Atītānāgatavāro": "अतीत और भविष्य का खंड",
})
FIXED = {
    "Pavattivāro niṭṭhito.": "प्रक्रिया का खंड पूरा हुआ।",
    "Pariññāvāro.": "पूरी तरह समझने का खंड।",
    "Indriyayamakaṃ niṭṭhitaṃ.": S.CHAPTER_END.format(title=S.CHAPTER_TITLES["Indriyayamakaṃ"]),
    "Yamakapakaraṇaṃ niṭṭhitaṃ.": S.BOOK_END,
}
# punctuation-only slips in the Pāli, normalised before translation
PUNCT_SLIPS = {
    "Dve puggalā aññindriyaṃ bhāvessanti no ca domanassindriyaṃ pajahissanti, pañca puggalā":
        "Dve puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahissanti. Pañca puggalā",
    "no ca domanassindriyaṃ pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti.":
        "no ca domanassindriyaṃ pajahanti. anāgāmimaggasamaṅgi aññindriyañca bhāvessanti domanassindriyañca pajahanti.",
    "Dve puggalā aññindriyaṃ bhāvessanti no ca anaññātaññassāmītindriyaṃ bhāvittha.":
        "Dve puggalā aññindriyaṃ bhāvessanti, no ca anaññātaññassāmītindriyaṃ bhāvittha.",
    "aññindriyaṃ bhāvessati. So anaññātaññassāmītindriyaṃ bhāvitthāti?":
        "aññindriyaṃ bhāvessati so anaññātaññassāmītindriyaṃ bhāvitthāti?",
    "anaññātaññassāmītindriyaṃ na bhāvessatīti. Āmantā.":
        "anaññātaññassāmītindriyaṃ na bhāvessatīti? Āmantā.",
    "so cakkhundriyaṃ na parijānissatīti.":
        "so cakkhundriyaṃ na parijānissatīti?",
    "manindriyaṃ na uppajjissati pacchimacittassa bhaṅgakkhaṇe tesaṃ paññindriyañca":
        "manindriyaṃ na uppajjissati. Pacchimacittassa bhaṅgakkhaṇe tesaṃ paññindriyañca",
}


def split_sentences(text):
    """Split on '. ' / '? ' outside square brackets."""
    out, buf, depth = [], "", 0
    i = 0
    while i < len(text):
        c = text[i]
        buf += c
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        elif c in ".?" and depth == 0 and (i + 1 == len(text) or text[i + 1] == " "):
            out.append(buf.strip())
            buf = ""
        i += 1
    if buf.strip():
        out.append(buf.strip())
    return out


SADISAM = "(पहले जैसा)"   # (Sadisaṃ) = the same as before


def tr_sentence(sent, parinna):
    if sent in FIXED:
        return FIXED[sent]
    if re.fullmatch(r"\(Sadisaṃ ?\)", sent):
        return SADISAM
    # trailing "…pe…." / "…Pe…."
    tail = ""
    m = re.fullmatch(r"(.*?)…[pP]e…\.", sent)
    if m:
        sent, tail = m.group(1), "…।"
        if not sent:
            return "…।"
    tag = mulaka_tag(sent)
    if tag:
        return tag + ("…।" if tail else "")
    m = re.fullmatch(r"\((\w+)mūlakaṃ\)\.", sent)
    if m:
        return mulaka_tag(sent[:-1]) + "।"
    word = sent.rstrip(".")
    if word in SHORT:
        return SHORT[word] + (tail if tail else "।")
    lm = re.match(r"\((Ka|Kha)\) ", sent)
    label = "(" + lm.group(1) + ")" if lm else None
    body = sent[lm.end():] if lm else sent
    if body.endswith("?"):
        if parinna:
            r = tr_parinna_q(label, body)
        else:
            b2 = re.sub(r"(uppajj|nirujjh)(atī|itthā|issatī)ti\?$",
                        lambda mm: mm.group(1) + {"atī": "ati", "itthā": "ittha", "issatī": "issati"}[mm.group(2)] + "?", body)
            r = tr_pavatti_q(label, b2)
        if r is None:
            raise ValueError("untranslated question: " + sent)
        return r + tail
    if sent.endswith("."):
        core = sent[:-1]
        r = tr_parinna_answer(core) + "।" if parinna else tr_answer(core)
        if r:
            return r + tail
    raise ValueError("untranslated sentence: " + sent)


def tr_body(text, parinna):
    if text in FIXED:
        return FIXED[text]
    for k, v in PUNCT_SLIPS.items():
        text = text.replace(k, v)
    sents = split_sentences(text)
    return " ".join(tr_sentence(s, parinna) for s in sents)


def tr_line(line, parinna):
    if not line.strip():
        return ""
    m = S.ID_RE.search(line)
    bid = m.group(1) if m else None
    text = S.ID_RE.sub("", line) if m else line
    if text.startswith("#"):
        level = len(text) - len(text.lstrip("#"))
        h = text[level:].strip()
        if h not in HEADINGS:
            raise ValueError("untranslated heading: " + h)
        out = "#" * level + " " + HEADINGS[h]
    else:
        out = tr_body(text, parinna)
    return out + (" " + bid if bid else "")


def build(fname):
    lines = (PALI_DIR / fname).read_text(encoding="utf-8").splitlines()
    out = []
    parinna = False
    errors = []
    for n, l in enumerate(lines, 1):
        if re.match(r"#### Pariññāvāro", l):
            parinna = True
        if fname == "10-13-indriyayamaka.md":
            parinna = True
        try:
            out.append(tr_line(l, parinna))
        except (ValueError, KeyError) as e:
            errors.append(f"{fname}:{n}: {e}")
            out.append("")
    if errors:
        print("\n".join(errors[:40]))
        print(len(errors), "errors in", fname)
        return False
    (HI_DIR / fname).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(fname, "ok", len([l for l in lines if l.strip()]), "lines")
    return True


if __name__ == "__main__":
    for f in sys.argv[1:] or FILES:
        build(f)
