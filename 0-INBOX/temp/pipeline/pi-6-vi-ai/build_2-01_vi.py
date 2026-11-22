# -*- coding: utf-8 -*-
"""pi-6 (Yamaka) Vietnamese zero-shot, chapter 2-01-khandhayamaka.md, and FRAME-SETTER of
family A (paṇṇattivāra) and family B (pavattivāra) for all later chapters.

Later chapters import this module and use the frames VERBATIM:

    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai")
    import build_sample_vi as S
    F = __import__("build_2-01_vi")          # the file name has a hyphen; importlib.import_module works too

Family A (naming questions, slots = Vietnamese noun phrases of the members):
    F.a_q(x, y, neg=False, label="Ka")       (Ka) X Y?  /  (Ka) na X na Y?
    F.a_is(s, a) / F.a_not(s, b)             predicate pieces «là X» / «không phải là X»
    F.a_but_not(s, a, b) = S.but_not         S A, na B.   /  S na B, A.  (pass the pieces in the Pāli order)
    F.a_both(s, a, b) = S.both               S Añceva Bañca.
    F.a_rest(n, b, var="")                   Avasesā N na B.
    F.a_except(x)                            X ṭhapetvā avasesā  (subject «ngoại trừ X, những gì còn lại»)
    F.a_except_n(x, n)                       X ṭhapetvā avasesā N (subject «ngoại trừ X, N còn lại»)
    F.a_neither(s, a, b)                     S na ceva A na ca B.
    F.a_and(a, b)                            Añca Bñca (ṭhapetvā)
    F.a_sense(x, y)                          X «hiểu theo nghĩa» Y  (piyarūpaṃ sātarūpaṃ, diṭṭhisaññā …)
Family B (occurrence questions, slots = member, verb (base, tense, polarity), person / place / both, beings).
The person / place shape (REL_VI, DEM_VI, NO_CA_VI, Q_FRAME, BUT_C, BOTH_C, STATEMENT_RES) is imported from
build_7-01_vi (coordinator decision); the verbs, «no ca» verbs, short answers, beings and planes are set here:
    F.verb(base, tense, neg)                 base: "sinh khởi" (uppajj-), "chấm dứt" (nirujjh-); tense pres|past|fut
    F.deny(base, tense, neg)                 the verb after «no ca …»
    F.b_q(kind, x, v1, y, v2, kha=False, label="Ka")       kind: "yassa" | "yattha" | "yassa yattha"
    F.b_not(res, head, x, v1, y, v2)         G tesaṃ X v1, no ca tesaṃ Y v2.  res: "tesaṃ" | "tattha" | "tesaṃ tattha"
    F.b_both(res, head, x, v1, y, v2)        G tesaṃ X ca v1 Y ca v2.         (v1, v2 = the Pāli verbs as triples)
    F.b_short(base, tense)                   Uppajjati. / Uppajjittha. / Nirujjhati. …  (contradicting answer)
    F.who(pali_genitive_phrase)              the beings (Asaññasattaṃ upapajjantānaṃ …) -> Vietnamese
    F.where(pali_locative_plane)             the place answers (Asaññasatte …) -> «Ở cõi Vô Tưởng»
    F.PLANE / F.BEINGS / F.PARTICIPLE        the plane and being vocabulary (extend locally, never change)

Importing writes nothing; run  python -I -X utf8 -B build_2-01_vi.py  to rebuild the chapter.
"""
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai")
import build_sample_vi as S  # noqa: E402

NAME = "2-01-khandhayamaka.md"
cap, low = S.cap, S.low
# Labels: always build_sample_vi.LABEL (coordinator: Vietnamese alphabet order, (a)(b)(c)(d)(đ)(e)(g)(h)).
LABEL_VI = S.LABEL

# ================================================================ members (Pāli word form -> Vietnamese noun phrase)
# pi-1 / pi-2: Năm khối – khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức.
KHANDHA_STEM = {"rūpa": "vật chất", "vedanā": "cảm giác", "saññā": "tri giác", "saṅkhāra": "tạo tác",
                "viññāṇa": "thức"}
MEMBER = {
    "rūpaṃ": "vật chất", "rūpa": "vật chất",
    "vedanā": "cảm giác", "vedanaṃ": "cảm giác",
    "saññā": "tri giác", "saññaṃ": "tri giác",
    "saṅkhārā": "các tạo tác", "saṅkhāre": "các tạo tác",
    "viññāṇaṃ": "thức",
    "khandho": "khối", "khandhaṃ": "khối",
    "khandhā": "các khối", "khandhe": "các khối",
}
for _k, _v in KHANDHA_STEM.items():
    MEMBER[f"{_k}kkhandho"] = MEMBER[f"{_k}kkhandhaṃ"] = f"khối {_v}"
PANCAKKHANDHA = "Năm khối – khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức."  # pi-2 ^2-1


def m(w):
    """Member word (any case form listed in MEMBER, capitalised or not) -> Vietnamese noun phrase."""
    return MEMBER[low(w)]


# ================================================================ FAMILY A: paṇṇattivāra frames
A_POS_Q = "{x} có phải là {y} không?"                                    # (Ka) X Y(ti)?
A_NEG_Q = "Những gì không phải là {x} thì không phải là {y}, có đúng không?"  # (Ka) na X na Y(ti)?
A_IS = "là {x}"                                                           # predicate X
A_NOT = "không phải là {x}"                                               # predicate na X
A_REST = "{n} còn lại{var} {y}."                                          # Avasesā N [var] na Y.
A_EXCEPT = "ngoại trừ {x}, những gì còn lại"                              # X ṭhapetvā avasesā
A_EXCEPT_N = "ngoại trừ {x}, {n} còn lại"                                 # X ṭhapetvā avasesā N
A_NEITHER = "{s} thì không phải là {a} cũng không phải là {b}."          # S na ceva A na ca B.
A_AND = "{a} và {b}"                                                      # Añca Bñca
A_SENSE = "{x} hiểu theo nghĩa {y}"                                       # piyarūpaṃ sātarūpaṃ / diṭṭhisaññā
SENSE = {                                                                 # the word-sense subjects of the niddesa
    "Piyarūpaṃ sātarūpaṃ": A_SENSE.format(x="vật chất", y="điều đáng yêu, điều khoan khoái"),
    "Diṭṭhisaññā": A_SENSE.format(x="tri giác", y="quan điểm"),
}
PANNATTI_UDDESAVARO = f"{S.UDDESAVARO} về sự định danh."                  # Paṇṇattiuddesavāro.
PANNATTI_NIDDESAVARO = f"{S.NIDDESAVARO} về sự định danh."                # Paṇṇattiniddesavāro.


def a_q(x, y, neg=False, label="Ka"):
    q = (A_NEG_Q if neg else A_POS_Q).format(x=x, y=y)
    return f"{LABEL_VI[label]} {cap(q)}" if label else cap(q)


def a_is(x):
    return A_IS.format(x=x)


def a_not(x):
    return A_NOT.format(x=x)


a_but_not = S.but_not      # «S thì A, nhưng B.»
a_both = S.both            # «S thì vừa A vừa B.»


def a_rest(n, y, var=""):
    return cap(A_REST.format(n=n, var=var, y=y))


def a_except(x):
    return A_EXCEPT.format(x=x)


def a_except_n(x, n):
    return A_EXCEPT_N.format(x=x, n=n)


def a_neither(s, a, b):
    return A_NEITHER.format(s=cap(s), a=a, b=b)


def a_and(a, b):
    return A_AND.format(a=a, b=b)


def a_sense(x, y):
    return A_SENSE.format(x=x, y=y)


# ================================================================ FAMILY B: pavattivāra frames
# The person / place shape is the one 7-01 set (coordinator, 2026-11-22): its constants are imported, not copied,
# so the two families stay byte-identical. This module sets the verbs (uppajjati / nirujjhati, three tenses, two
# polarities), the «no ca» verb, the short answers and the beings / planes.
import importlib  # noqa: E402
C7 = importlib.import_module("build_7-01_vi")
REL_VI = C7.REL_VI          # yassa / yattha / yassa yattha  = ở người nào / ở nơi nào / ở người nào, ở nơi nào
DEM_VI = C7.DEM_VI          # tassa / tattha / tassa tattha  = ở người ấy / ở nơi ấy / ở người ấy, ở nơi ấy
NO_CA_VI = C7.NO_CA_VI      # no ca tassa / tesaṃ / tattha / tassa tattha / tesaṃ tattha = nhưng ở …
RES_VI = dict(C7.RES_VI, **{"tesaṃ": C7.NO_CA_VI["tesaṃ"], "tattha": C7.NO_CA_VI["tattha"],
                            "tassa": C7.NO_CA_VI["tassa"]})   # G tesaṃ / L tattha … = «G, thì ở những người ấy …»
Q_FRAME = C7.Q_FRAME        # «{rel} mà {a} {pa}, thì {dem} có phải {b} {pb} không?»
VA_PANA = C7.VA_PANA        # «Còn »
BUT_C = C7.BUT_C            # «{a} {p}, nhưng {dem} {b} {no}»
BOTH_C = C7.BOTH_C          # «{a} {p}, đồng thời {b} cũng {p2}»
STATEMENT_RES = C7.STATEMENT_RES   # «{head}, thì {res} {clause}.»
NATTHI = C7.NATTHI          # Natthi. = Không có. (pi-3)
NO = C7.NO                  # No. = Không.
DEM_OF = {"yassa": "tassa", "yattha": "tattha", "yassa yattha": "tassa tattha"}

VERB_BASE = {"uppajj": "sinh khởi", "nirujjh": "chấm dứt"}       # uppajjati (pi-1), nirujjhati (pi-2)
TENSE_POS = {"pres": "{v}", "past": "đã {v}", "fut": "sẽ {v}"}    # uppajjati / uppajjittha / uppajjissati
TENSE_NEG = {"pres": "không {v}", "past": "chưa từng {v}", "fut": "sẽ không {v}"}  # nuppajjati / nuppajjittha / …
DENY_NEG = {"pres": "vẫn {v}", "past": "đã từng {v}", "fut": "vẫn sẽ {v}"}
# no ca … nuppajjati / nuppajjittha / nuppajjissati: the denied negative said plainly (7-01 «vẫn …»)
SHORT = {"pres": "Có {v}.", "past": "Đã {v}.", "fut": "Sẽ {v}."}  # Uppajjati. / Uppajjittha. / Uppajjissati.
PLACE_IN = "trong {p}"                                            # Asaññasatte (place answers; 7-01 «trong cõi …»)


def verb(base, tense, neg=False):
    return (TENSE_NEG if neg else TENSE_POS)[tense].format(v=base)


def deny(base, tense, neg=False):
    """The verb of a «no ca tesaṃ Y v» clause: no ca + positive = the negative form; no ca + negative = the
    positive said plainly («vẫn sinh khởi», «đã từng sinh khởi», «vẫn sẽ sinh khởi»)."""
    return DENY_NEG[tense].format(v=base) if neg else verb(base, tense, True)


def b_q(kind, x, v1, y, v2, kha=False, label="Ka"):
    """kind: "yassa" | "yattha" | "yassa yattha"; v1, v2 = (base, tense, neg) triples."""
    q = Q_FRAME.format(rel=REL_VI[kind], a=x, pa=verb(*v1), dem=DEM_VI[DEM_OF[kind]], b=y, pb=verb(*v2))
    q = cap(VA_PANA + q if kha else q)
    return f"{LABEL_VI[label]} {q}" if label else q


def b_not(res, head, x, v1, y, v2):
    """res: "tesaṃ" | "tattha" | "tesaṃ tattha" (also "tassa", "tassa tattha"); head: who() / where()."""
    clause = BUT_C.format(a=x, p=verb(*v1), dem=NO_CA_VI[res], b=y, no=deny(*v2))
    return cap(STATEMENT_RES.format(head=head, res=RES_VI[res], clause=clause))


def b_both(res, head, x, v1, y, v2):
    clause = BOTH_C.format(a=x, p=verb(*v1), b=y, p2=verb(*v2))
    return cap(STATEMENT_RES.format(head=head, res=RES_VI[res], clause=clause))


def b_short(base, tense):
    return SHORT[tense].format(v=base)


# ---------------------------------------------------------------- beings and planes
PLANE = {                                    # plane stem -> Vietnamese plane
    "asaññasatta": "cõi Vô Tưởng",           # pi-2 «chư thiên / chúng sinh Vô Tưởng»
    "arūpa": "cõi không hình sắc",            # pi-5 «Arūpe rūpakathā = … trong cõi không hình sắc»
    "pañcavokāra": "cõi gồm năm khối",        # pi-2 pañcavokārabhava «sự hiện hữu gồm năm khối»
    "catuvokāra": "cõi gồm bốn khối",         # pi-2 catuvokārabhava
    "ekavokāra": "cõi gồm một khối",          # pi-2 ekavokārabhava
    "suddhāvāsa": "cõi Tịnh Cư",              # new (Hán-Việt deva-realm style of pi-1 «Sắc Cứu Cánh»)
    "kāmāvacara": "cõi dục lạc",              # pi-1 (proposed for later chapters)
    "rūpāvacara": "cõi hình sắc",             # pi-1 (proposed for later chapters)
    "arūpāvacara": "cõi không hình sắc",      # pi-1 (proposed for later chapters)
}
BEINGS = {"asaññasatta": "chúng sinh Vô Tưởng"}   # beings with their own name (pi-2 / pi-5); else BEINGS_OF
BEINGS_OF = "chúng sinh trong {p}"                # arūpānaṃ, pañcavokārānaṃ, suddhāvāsānaṃ …
BEINGS_OTHER = "những chúng sinh khác trong {p}"  # itaresaṃ pañcavokārānaṃ …
HEAD = {None: "những người", "sabbesaṃ": "tất cả những người", "itaresaṃ": "những người khác"}
PARTICIPLE = {                                     # participle -> (Vietnamese, preposition, plane case)
    "upapajjantānaṃ": ("đang tái sinh", "vào", "acc"),               # pi-2 upapajjanti «tái sinh»
    "cavantānaṃ": ("đang chết đi", "khỏi", "abl"),                   # pi-2 / pi-5 cavanti «chết đi»
    "parinibbantānaṃ": ("đang nhập Niết-bàn trọn vẹn", "trong", "loc"),  # pi-5 parinibbāyati
}
PACCHIMA = "thuộc kiếp sống cuối cùng"           # pacchimabhavikānaṃ (new)
PACCHIMA_IN = "trong"                            # Arūpe pacchimabhavikānaṃ «… trong cõi không hình sắc»
WHO_HEAD = "ở {g}"                               # the genitive beings phrase heads the answer («Ở …, thì …»)
YE_UPAPAJJITVA = "những người nào sau khi tái sinh vào {p} sẽ nhập Niết-bàn trọn vẹn"
# Ye arūpaṃ upapajjitvā parinibbāyissanti (nominative relative: no «ở»)
LIST_SEP = ", "                                  # asyndetic Pāli lists stay comma lists
_FORMS = {}
for _s in PLANE:                                 # every plane stem ends in -a
    for _case, _w in (("acc", _s + "ṃ"), ("abl", _s[:-1] + "ā"), ("loc", _s[:-1] + "e"), ("gen", _s[:-1] + "ānaṃ")):
        _FORMS[_w] = (_case, _s)


def _plane_case(w):
    return _FORMS.get(w, (None, None))


def who(phrase):
    """Genitive beings phrase of a person answer -> Vietnamese head «ở …» (lowercase start). A trailing variant
    bracket is kept at the end."""
    var = ""
    mv = re.fullmatch(r"(.+?) (\[[^\]]+\])", phrase)
    if mv:
        phrase, var = mv.group(1), " " + variant(mv.group(2))
    mye = re.fullmatch(r"[Yy]e (\S+) upapajjitvā parinibbāyissanti", phrase)
    if mye:
        case, stem = _plane_case(mye.group(1))
        assert case == "acc", phrase
        return YE_UPAPAJJITVA.format(p=PLANE[stem]) + var
    w = [low(x) for x in phrase.split()]
    groups, i, n = [], 0, len(w)
    while i < n:
        mod = None
        if w[i] in ("sabbesaṃ", "itaresaṃ"):
            mod, i = w[i], i + 1
        planes, pcase = [], None
        while i < n:
            case, stem = _plane_case(w[i])
            if case in ("acc", "abl", "loc") and (pcase in (None, case)):
                planes.append(PLANE[stem]); pcase = case; i += 1
            else:
                break
        if i < n and w[i] in PARTICIPLE:
            vi, prep, need = PARTICIPLE[w[i]]
            assert pcase in (None, need), (phrase, w[i])
            g = f"{HEAD[mod]} {vi}" + (f" {prep} {LIST_SEP.join(planes)}" if planes else "")
            i += 1
        elif i < n and w[i] == "pacchimabhavikānaṃ":
            assert pcase in (None, "loc"), phrase
            g = f"{HEAD[mod]} {PACCHIMA}" + (f" {PACCHIMA_IN} {LIST_SEP.join(planes)}" if planes else "")
            i += 1
            j, pl2 = i, []
            while j < n and _plane_case(w[j])[0] == "acc":
                pl2.append(PLANE[_plane_case(w[j])[1]]); j += 1
            if not planes and j < n and w[j] == "upapajjantānaṃ":
                vi, prep, _ = PARTICIPLE["upapajjantānaṃ"]
                g += f" {vi}" + (f" {prep} {LIST_SEP.join(pl2)}" if pl2 else "")
                i = j + 1
        elif i < n and not planes and _plane_case(w[i])[0] == "gen":
            stem = _plane_case(w[i])[1]
            if stem in BEINGS:
                assert mod is None, phrase
                g = BEINGS[stem]; i += 1
            else:
                ps = []
                while i < n and _plane_case(w[i])[0] == "gen" and _plane_case(w[i])[1] not in BEINGS:
                    ps.append(PLANE[_plane_case(w[i])[1]]); i += 1
                assert mod in (None, "itaresaṃ"), phrase
                g = (BEINGS_OTHER if mod else BEINGS_OF).format(p=LIST_SEP.join(ps))
        elif i == n and mod == "itaresaṃ" and not planes:
            g = HEAD[mod]
        else:
            raise ValueError(f"unparsed beings phrase: {phrase!r} at {w[i:]}")
        groups.append(g)
    return WHO_HEAD.format(g=LIST_SEP.join(groups)) + var


def where(loc):
    """Locative plane of a place answer (Asaññasatte, Arūpe, Pañcavokāre …) -> «trong cõi …»."""
    case, stem = _plane_case(low(loc))
    assert case == "loc", loc
    return PLACE_IN.format(p=PLANE[stem])


# ---------------------------------------------------------------- Pāli verb forms
VFORM = re.compile(r"(?P<neg>na |n)?(?P<b>uppajj|nirujjh)(?P<t>atīti|ati|itthāti|ittha|attha|issatīti|issati)")
TENSE_OF = {"ati": "pres", "atīti": "pres", "ittha": "past", "itthāti": "past", "attha": "past",
            "issati": "fut", "issatīti": "fut"}
SLIPS = []          # (where, what) reported by the build


def vparse(s, ctx=""):
    mm = VFORM.fullmatch(s)
    if not mm:
        raise ValueError(f"unparsed verb {s!r}")
    if mm["t"] == "attha":
        SLIPS.append((ctx, f"{s} (read as {s.replace('attha', 'ittha')})"))
    return (VERB_BASE[mm["b"]], TENSE_OF[mm["t"]], bool(mm["neg"]))


# ================================================================ variants
SIGLA = {"sī.": "Sī.", "syā.": "Syā.", "ka.": "Ka.", "pī.": "Pī.", "kaṃ.": "Kaṃ."}
EVAMUPARIPI = ", cũng vậy ở các chỗ sau"   # evamuparipi (pi-2 ^2-568)


def variant(br, label=None):
    """[avasesā khandhā khandhā (syā.) evamuparipi] -> [dị bản (Syā.): avasesā khandhā khandhā, cũng vậy …]"""
    mm = re.fullmatch(r"\[(?P<t>.+?) \((?P<s>[^)]+)\)(?P<e> evamuparipi)?\]", br)
    assert mm, br
    sig = ", ".join(SIGLA[x] for x in mm["s"].split())
    return f"[{label or S.VAR} ({sig}): {mm['t']}{EVAMUPARIPI if mm['e'] else ''}]"


# ================================================================ headings and closing lines
def heading(t):
    if t in S.YAMAKA:
        return S.YAMAKA[t]
    if t == "(Ka) uddeso":
        return f"{S.LABEL['Ka']} {S.UDDESO}"
    if t == "(Kha) niddeso":
        return f"{S.LABEL['Kha']} {S.NIDDESO}"
    mm = re.fullmatch(r"(?P<a>Pavattivāro|Pavatti) (?P<n>\d)\. (?P<b>\S+)", t)
    if mm:
        return f"{S.SECTION[mm['a']]} {mm['n']}. {S.SECTION[mm['b']]}"
    mm = re.fullmatch(r"\((?P<l>[^)]+)\) (?P<w>\S+)", t)
    if mm:
        lab = LABEL_VI.get(mm["l"], f"({mm['l']})")
        return f"{lab} {S.SECTION[mm['w']]}"
    return S.SECTION[t]


EXACT = {
    "Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.":
        PANCAKKHANDHA,
    "Paṇṇattiuddesavāro.": PANNATTI_UDDESAVARO,
    "Paṇṇattiniddesavāro.": PANNATTI_NIDDESAVARO,
    "Uppādavāro niṭṭhito.": f"{cap(S.SECTION['uppādavāro'])} {S.NITTHITA}.",
    "Nirodhavāro niṭṭhito.": f"{cap(S.SECTION['nirodhavāro'])} {S.NITTHITA}.",
    "Āmantā.": S.AMANTA,
    "Natthi.": NATTHI,
}


# ================================================================ sentence parser for this chapter
def _strip_ti(w):
    if w.endswith("nti"):
        return w[:-3] + "ṃ"
    if w.endswith("ti"):
        return w[:-2]
    return w


def _acc_ca(w):
    """Rūpañca -> rūpaṃ; Saṅkhāre ca -> saṅkhāre (the « ca» is split off by the regex)."""
    return w[:-3] + "ṃ" if w.endswith("ñca") else w


def _sent_a_question(s, ctx):
    mm = re.fullmatch(r"\((?P<l>Ka|Kha)\) na (?P<x>\S+) na (?P<y>\S+?)(?P<p>[?.])", s) or \
        re.fullmatch(r"\((?P<l>Ka|Kha)\) (?P<x>\S+) (?P<y>\S+?)(?P<p>[?.])", s)
    if not mm or low(mm["x"]) not in MEMBER or low(_strip_ti(mm["y"])) not in MEMBER:
        return None
    if mm["p"] == ".":
        SLIPS.append((ctx, f"«{s}»: question ends with «.» in the Pāli; rendered with «?»"))
    neg = s.split(") ", 1)[1].startswith("na ")
    return a_q(m(mm["x"]), m(_strip_ti(mm["y"])), neg=neg, label=mm["l"])


def _var_vi(v):
    return f" {variant(v.strip())}" if v else ""


A_SENT = [
    # Piyarūpaṃ sātarūpaṃ rūpaṃ, na rūpakkhandho. / Diṭṭhisaññā saññā, na saññākkhandho.
    (r"(?P<s>Piyarūpaṃ sātarūpaṃ|Diṭṭhisaññā) (?P<a>\S+), na (?P<b>\S+)\.",
     lambda g: a_but_not(SENSE[g["s"]], a_is(m(g["a"])), a_not(m(g["b"])))),
    # Piyarūpaṃ sātarūpaṃ na rūpakkhandho, rūpaṃ.
    (r"(?P<s>Piyarūpaṃ sātarūpaṃ|Diṭṭhisaññā) na (?P<b>\S+), (?P<a>\S+)\.",
     lambda g: a_but_not(SENSE[g["s"]], a_not(m(g["b"])), a_is(m(g["a"])))),
    # Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā [var], na saṅkhārakkhandho.
    (r"(?P<e>\S+) ṭhapetvā avasesā (?P<a>\S+)(?P<v> \[[^\]]+\])?, na (?P<b>\S+)\.",
     lambda g: a_but_not(a_except(m(g["e"])), a_is(m(g["a"])) + _var_vi(g["v"]), a_not(m(g["b"])))),
    # Saṅkhārakkhandhaṃ ṭhapetvā avasesā na saṅkhārakkhandho, saṅkhārā.
    (r"(?P<e>\S+) ṭhapetvā avasesā na (?P<b>\S+), (?P<a>\S+)\.",
     lambda g: a_but_not(a_except(m(g["e"])), a_not(m(g["b"])), a_is(m(g["a"])))),
    # Rūpaṃ ṭhapetvā avasesā khandhā na rūpaṃ, khandhā.
    (r"(?P<e>\S+) ṭhapetvā avasesā (?P<n>khandhā) na (?P<b>\S+), (?P<a>\S+)\.",
     lambda g: a_but_not(a_except_n(m(g["e"]), m(g["n"])), a_not(m(g["b"])), a_is(m(g["a"])))),
    # (Rūpañca rūpakkhandhañca ṭhapetvā avasesā na ceva rūpaṃ na ca rūpakkhandho. -> _neither)
    # Rūpakkhandho rūpañceva rūpakkhandho ca. / Vedanākkhandho khandho ceva vedanākkhandho ca.
    (r"(?P<s>\S+) (?P<a>\S+?)(?P<k>ñceva| ceva) (?P<b>\S+) ca\.",
     lambda g: a_both(m(g["s"]), a_is(m(g["a"] + ("ṃ" if g["k"] == "ñceva" else ""))), a_is(m(g["b"])))),
    # Avasesā khandhā [var] na vedanākkhandho.
    (r"Avasesā (?P<n>khandhā)(?P<v> \[[^\]]+\])? na (?P<b>\S+)\.",
     lambda g: a_rest(m(g["n"]), a_not(m(g["b"])), _var_vi(g["v"]))),
]


def _neither(s):
    mm = re.fullmatch(r"(?P<a>\S+?)(?:ñca| ca) (?P<b>\S+?)(?:ñca| ca) ṭhapetvā avasesā na ceva (?P<c>\S+) na ca "
                      r"(?P<d>\S+)\.", s)
    if not mm:
        return None
    a = m(mm["a"] + "ṃ") if s.startswith(mm["a"] + "ñca") else m(mm["a"])
    rest = s[len(mm["a"]):]
    b = mm["b"] + ("ṃ" if rest.split(" ṭhapetvā")[0].endswith("ñca") else "")
    return a_neither(a_except(a_and(a, m(b))), m(mm["c"]), m(mm["d"]))


B_Q_RE = re.compile(r"\((?P<l>Ka|Kha)\) (?P<w1>yassa vā pana yattha|yassa yattha|yassa vā pana|yattha vā pana|yassa|"
                    r"yattha) (?P<x>\S+) (?P<v1>(?:na )?\S+) (?P<w2>tassa tattha|tassa|tattha) (?P<y>\S+) "
                    r"(?P<v2>(?:na )?\S+)\?")
V = r"(?:na )?\S+"
B_PERSON_NOT = re.compile(rf"(?P<g>.+?) tesaṃ(?P<t> tattha)? (?P<x>\S+khandho) (?P<v1>{V}), no ca tesaṃ(?P<t2> tattha)? "
                          rf"(?P<y>\S+khandho) (?P<v2>{V})\.")
B_PERSON_BOTH = re.compile(rf"(?P<g>.+?) tesaṃ(?P<t> tattha)? (?P<x>\S+khandho) ca (?P<v1>{V}) (?P<y>\S+khandho) ca "
                           rf"(?P<v2>{V})\.")
B_PLACE_NOT = re.compile(rf"(?P<g>\S+) tattha (?P<x>\S+khandho) (?P<v1>{V}), no ca tattha (?P<y>\S+khandho) (?P<v2>{V})\.")
B_PLACE_BOTH = re.compile(rf"(?P<g>\S+) tattha (?P<x>\S+khandho) ca (?P<v1>{V}) (?P<y>\S+khandho) ca (?P<v2>{V})\.")
B_SHORT_RE = re.compile(r"(?P<b>Uppajj|Nirujjh)(?P<t>ati|ittha|issati)\.")


def translate_sentence(s, ctx):
    if s in EXACT:
        return EXACT[s]
    r = _sent_a_question(s, ctx)
    if r:
        return r
    mm = B_Q_RE.fullmatch(s)
    if mm:
        kind = mm["w1"].replace(" vā pana", "")
        kind2 = {"tassa": "yassa", "tattha": "yattha", "tassa tattha": "yassa yattha"}[mm["w2"]]
        assert kind == kind2, s
        kha = "vā pana" in mm["w1"]
        if kha != (mm["l"] == "Kha"):
            SLIPS.append((ctx, f"label ({mm['l']}) on a «{'vā pana' if kha else 'no vā pana'}» question; kept as written"))
        return b_q(kind, m(mm["x"]), vparse(mm["v1"], ctx), m(mm["y"]), vparse(mm["v2"], ctx), kha=kha, label=mm["l"])
    for rx, both in ((B_PERSON_NOT, False), (B_PERSON_BOTH, True)):
        mm = rx.fullmatch(s)
        if mm:
            if not both:
                assert bool(mm["t"]) == bool(mm["t2"]), s
            res = "tesaṃ tattha" if mm["t"] else "tesaṃ"
            f = b_both if both else b_not
            return f(res, who(mm["g"]), m(mm["x"]), vparse(mm["v1"], ctx), m(mm["y"]), vparse(mm["v2"], ctx))
    for rx, both in ((B_PLACE_NOT, False), (B_PLACE_BOTH, True)):
        mm = rx.fullmatch(s)
        if mm:
            f = b_both if both else b_not
            return f("tattha", where(mm["g"]), m(mm["x"]), vparse(mm["v1"], ctx), m(mm["y"]),
                     vparse(mm["v2"], ctx))
    mm = B_SHORT_RE.fullmatch(s)
    if mm:
        return b_short(VERB_BASE[low(mm["b"])], TENSE_OF[mm["t"]])
    r = _neither(s)
    if r:
        return r
    for p, f in A_SENT:
        mm = re.fullmatch(p, s)
        if mm:
            return f(mm)
    raise ValueError(f"unmatched sentence: {s!r}")


def split_sentences(t):
    """Split at «. » / «? » outside square brackets."""
    out, cur, depth = [], "", 0
    i = 0
    while i < len(t):
        ch = t[i]
        cur += ch
        depth += (ch == "[") - (ch == "]")
        if ch in ".?" and depth == 0 and i + 1 < len(t) and t[i + 1] == " ":
            out.append(cur)
            cur = ""
            i += 1          # skip the space
        i += 1
    if cur:
        out.append(cur)
    return out


def translate_line(line, ctx):
    mm = re.match(r"^(?P<h>#+ )?(?P<t>.*?)(?P<id> \^[0-9A-Za-z-]+)?$", line)
    h, t, sid = mm["h"] or "", mm["t"], mm["id"] or ""
    if h:
        return h + heading(t) + sid
    if t in EXACT:
        return EXACT[t] + sid
    return " ".join(translate_sentence(s, ctx) for s in split_sentences(t)) + sid


def translate_file(name=NAME):
    src = (S.PALI_DIR / name).read_text(encoding="utf-8")
    out, seg = [], 1
    lines = src.splitlines()
    for ln in lines:
        mid = re.search(r"\^([0-9A-Za-z-]+)\s*$", ln)
        out.append(translate_line(ln, f"segment after ^{seg}") if ln.strip() else "")
        if mid:
            seg = mid.group(1)
    text = "\n".join(out).rstrip("\n") + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


# ================================================================ cross-book asserts
CROSS_BOOK = [
    (PANCAKKHANDHA, 2), ("khối vật chất", 1), ("khối cảm giác", 1), ("khối tri giác", 1), ("khối tạo tác", 1),
    ("khối thức", 1), ("vật chất", 1), ("cảm giác", 1), ("tri giác", 1), ("các tạo tác", 5), ("thức", 1),
    ("điều đáng yêu", 2), ("điều khoan khoái", 2), ("quan điểm", 2), ("ngoại trừ", 2), ("còn lại", 1),
    ("không phải có tri giác cũng không phải không có tri giác", 2), ("vừa là", 1),
    ("Vô Tưởng", 2), ("chúng sinh Vô Tưởng", 5), ("cõi không hình sắc", 5), ("cõi không hình sắc", 1),
    ("gồm năm khối", 2), ("gồm bốn khối", 2), ("gồm một khối", 2), ("cõi dục lạc", 1), ("cõi hình sắc", 1),
    ("tái sinh", 2), ("chết đi", 2), ("chết đi", 5), ("nhập Niết-bàn trọn vẹn", 5), ("chúng sinh", 2),
    ("sinh khởi", 1), ("đã sinh khởi", 1), ("sẽ sinh khởi", 1), ("chấm dứt", 2), ("không sinh khởi", 2),
    (NATTHI, 3), ("cũng vậy ở các chỗ sau", 2), ("Đúng vậy.", 5), ("dị bản", 1),
]


def check_cross_book():
    texts = {b: "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md")))
             for b, d in S.RAILS_DIR.items()}
    missing = [(s, b) for s, b in CROSS_BOOK if s not in texts[b]]
    for s, b in missing:
        print(f"CROSS-BOOK MISSING in pi-{b}: {s}")
    assert not missing, f"{len(missing)} cross-book strings not found"
    print(f"cross-book asserts: {len(CROSS_BOOK)} strings found in pi-1..5 rails")


# line-check problems that are expected because a Pāli slip was rendered as meant (Pāli line text -> problem)
EXPECTED = {
    "(Ka) na saṅkhārā na saṅkhārakkhandhoti. Āmantā.": "'?' count 0 vs 1",
}


def main():
    S.check_cross_book()
    check_cross_book()
    text = unicodedata.normalize("NFC", translate_file())
    pali = (S.PALI_DIR / NAME).read_text(encoding="utf-8")
    probs = S.check_lines(pali, text, NAME)
    pl = [x for x in pali.splitlines() if x.strip()]
    kept = []
    for p in probs:
        mm = re.search(r"line (\d+): (.*)$", p)
        if mm and EXPECTED.get(pl[int(mm.group(1)) - 1]) and EXPECTED[pl[int(mm.group(1)) - 1]] in mm.group(2):
            print("EXPECTED (slip rendered as meant):", p)
            continue
        kept.append(p)
    with open(S.OUT_DIR / NAME, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    segs = len(re.findall(r"\^[0-9A-Za-z-]+\s*$", text, flags=re.M))
    print(f"wrote {NAME}: {len([x for x in text.splitlines() if x.strip()])} lines, {segs} segments")
    for c, w in SLIPS:
        print("SLIP", c, "|", w)
    for p in kept[:80]:
        print("PROBLEM", p)
    print("line checks:", "OK" if not kept else f"{len(kept)} problems")
    sys.exit(1 if kept else 0)


if __name__ == "__main__":
    main()
