"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 2-02 (Khandhayamaka, part 2) and the FAMILY E module.

Family E = pariññāvāra: "yo A V so B Vti?" questions with a transitive person verb (parijānāti in every tense,
           present / past / future and the mixed tenses, positive and "na" negative), and the answers whose
           subjects are persons (Arahā, Aggamaggasamaṅgī, "X-ñca Y-ñca ṭhapetvā avasesā puggalā",
           "Ye … te", "P ye ca Q … te"), with the "no ca" frame and the both-frame.
The rest of 2-02 (nirodhavāra tail, uppādanirodhavāra) is family B: imported from build_rails_2-01_vi unchanged;
this file only adds the heads and cut lines 2-01 did not have (see notes-rails-2-02.md).

Later chapters (3-06, 5-03, 7-07, 7-08, 10-13 …) import this file READ-ONLY:

    import importlib, sys
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    E = importlib.import_module("build_rails_2-02_vi")
    verbs = {**E.E_VERBS, **E.make_verbs("dứt bỏ", E.rows_fused("pajah", ...))}   # their own verbs, same tense rule
    out = E.e_line(body, M, verbs=verbs, persons=E.Persons(nom={...}, acc={...}))

Every slot function takes the member names (Vietnamese) as arguments; the parsers raise ValueError on any word
or shape they cannot place (no silent fallback). Importing writes nothing; outputs are written only under
`if __name__ == "__main__":`.

usage: python -I -X utf8 -B build_rails_2-02_vi.py
"""
import copy
import importlib
import re
import sys
import unicodedata
from collections import namedtuple

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY: labels, checks, writer)
B = importlib.import_module("build_rails_2-01_vi")   # READ-ONLY: families A, B (setter 2-01)
C = importlib.import_module("build_rails_7-01_vi")   # READ-ONLY: family C and the shared answer shapes (setter 7-01)

cap = S.cap
LABEL = S.LABEL
CH = "2-02-khandhayamaka.md"
N = "2-02"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
TERMBASE = S.ROOT / "AI_translation/vietnamese/pi-6-pali-vietnamese-termbase-plain.md"

SLIPS_SEEN = []   # (where, what) collected while building; printed by main() and listed in the notes


# ===============================================================================================================
# FAMILY E 1. Verbs: one positive base term per verb, the tense rule of the termbase (= family B's VERB_TABLE)
# ===============================================================================================================
PARIJANATI = "hiểu biết trọn vẹn"        # parijānāti (termbase; = 7-01 FAMILY_TERMS)
TENSE_VI = {                              # (positive, negative) from the base term V (user 2026-11-22)
    "present": ("{v}", "không {v}"),
    "past": ("đã {v}", "chưa từng {v}"),
    "future": ("sẽ {v}", "sẽ không {v}"),
}
EVerb = namedtuple("EVerb", "vi negative pos_vi neg_vi number tense")   # number 1 / 2 / 0 (past: any)


def tense_vi(base, tense):
    """(positive, negative) Vietnamese of a verb in a tense: «V» / «không V», «đã V» / «chưa từng V», «sẽ V» / «sẽ không V»."""
    p, n = TENSE_VI[tense]
    return p.format(v=base), n.format(v=base)


def make_verbs(base, rows):
    """rows: [(Pāli form, tense, negative?, number)] → {form: EVerb}. One table per verb; merge the dicts."""
    out = {}
    for form, tense, negative, number in rows:
        pv, nv = tense_vi(base, tense)
        if form in out:
            raise ValueError(f"verb form {form!r} twice")
        out[form] = EVerb(nv if negative else pv, negative, pv, nv, number, tense)
    return out


def rows_na(present_sg, present_pl, past, future_sg, future_pl):
    """The rows of a verb negated by a separate "na" (parijānāti, bhāveti …)."""
    rows = []
    for neg, pre in ((False, ""), (True, "na ")):
        rows += [(pre + present_sg, "present", neg, 1), (pre + present_pl, "present", neg, 2),
                 (pre + past, "past", neg, 0),
                 (pre + future_sg, "future", neg, 1), (pre + future_pl, "future", neg, 2)]
    return rows


def rows_fused(pos, neg):
    """The rows of a verb with a fused negative (pajahati / nappajahati): pos, neg = 5-tuples as rows_na's."""
    keys = (("present", 1), ("present", 2), ("past", 0), ("future", 1), ("future", 2))
    return ([(f, t, False, n) for f, (t, n) in zip(pos, keys)] +
            [(f, t, True, n) for f, (t, n) in zip(neg, keys)])


E_VERBS = make_verbs(PARIJANATI, rows_na("parijānāti", "parijānanti", "parijānittha",
                                         "parijānissati", "parijānissanti"))


def e_verb(tok, verbs=None):
    """A Pāli verb (one or two words, with or without the -ti of a question) → EVerb."""
    verbs = verbs or E_VERBS
    cands = [tok]
    for end, rep in (("ntīti", "nti"), ("īti", "i"), ("āti", "a")):
        if tok.endswith(end):
            cands.append(tok[:-len(end)] + rep)
    hits = [verbs[c] for c in cands if c in verbs]
    if len(hits) != 1:
        raise ValueError(f"unknown family-E verb {tok!r}")
    return hits[0]


def is_e_verb(tok, verbs=None):
    try:
        e_verb(tok, verbs)
        return True
    except ValueError:
        return False


def denied(v):
    """After "no ca" (no pronoun in family E): a NEGATIVE verb is denied → «vẫn V» / «đã từng V» / «vẫn sẽ V»
    (coordinator, = B.denied_vi); a POSITIVE verb is negated → its own negative term («không V», «chưa từng V» …)."""
    return B.denied_vi(v.pos_vi) if v.negative else v.neg_vi


# ===============================================================================================================
# FAMILY E 2. Objects (the member in the accusative): one word, "A-ñca" / "A ca", or a "…pe…" run
# ===============================================================================================================
def obj_run(text, M):
    """An object run → C.tp_vi-style dict(names, conj, pe): 'A' / 'A-ñca' / 'A ca' / 'A-ñca B-ñca' / 'A ca B ca' /
    'A…pe… B' / 'A …pe… B' (7-01 run rules: a list needs 'ca' on every item or a …pe… in every gap)."""
    names, has_ca, pe = [], [], {}
    for m in C.PE_RE.finditer(text.strip()):
        tok = m.group(0)
        if tok.strip().startswith("…"):
            if not names:
                raise ValueError(f"…pe… before any object: {text!r}")
            pe[len(names) - 1] = m.group(1) == " "
        elif tok == "ca":
            if not names or has_ca[-1]:
                raise ValueError(f"misplaced 'ca' in {text!r}")
            has_ca[-1] = True
        else:
            names.append(M.subj(tok))          # raises on an unknown object word
            has_ca.append(tok.endswith("ñca"))
    if not names:
        raise ValueError(f"empty object {text!r}")
    if any(has_ca) and not all(has_ca):
        raise ValueError(f"mixed 'ca' in {text!r}")
    if len(names) > 1 and not all(has_ca) and len(pe) != len(names) - 1:
        raise ValueError(f"object list without 'ca' or …pe… in {text!r}")
    return {"names": names, "conj": all(has_ca), "pe": pe}


def obj_vi(text, M):
    """'rūpakkhandhaṃ' / 'rūpakkhandhañca' → «khối vật chất»; 'A ca B ca' → «A và B»; 'A…pe… B' → «A… B» (C.tp_vi)."""
    return C.tp_vi(obj_run(text, M))


def conj(text, M):
    """True if the object run carries the 'ca' of a both-frame / list ('rūpakkhandhañca', 'saṅkhāre ca')."""
    return obj_run(text, M)["conj"]


def single(text, M):
    """True if the run is one item without 'ca' (or a …pe… run): the only shape a question slot takes."""
    r = obj_run(text, M)
    return not r["conj"]


def neither_vi(text, M, v):
    """After "no ca", positive verb: «không V A[, cũng không V B …]» (user "neither" rule; = 7-03 / 7-05)."""
    r = obj_run(text, M)
    if r["pe"]:
        raise ValueError(f"…pe… inside a 'no ca' part: {text!r}")
    return f"{v.neg_vi} " + f", {ALSO} {v.neg_vi} ".join(r["names"])


def still_vi(text, M, v):
    """After "no ca", negative verb (denied): «vẫn V A» / «vẫn V A và B» / «đã từng V A» / «vẫn sẽ V A»
    (coordinator: the list is denied as a whole, as «A và B vẫn V» in family C)."""
    r = obj_run(text, M)
    if r["pe"]:
        raise ValueError(f"…pe… inside a 'no ca' part: {text!r}")
    if r["conj"] and len(r["names"]) == 1:
        raise ValueError(f"dangling 'ca' in a 'no ca' part: {text!r}")
    return f"{B.denied_vi(v.pos_vi)} {C.tp_vi(r)}"


def split_groups(text, M, verbs=None):
    """'A V1' / 'A-ñca V1 B-ñca V2' → [(object text, EVerb), …]. Verbs: two words first ('na parijānāti')."""
    w = text.split()
    groups, cur, i = [], [], 0
    while i < len(w):
        two = " ".join(w[i:i + 2])
        if cur and i + 1 < len(w) and is_e_verb(two, verbs):
            groups.append((" ".join(cur), e_verb(two, verbs)))
            cur, i = [], i + 2
        elif cur and is_e_verb(w[i], verbs):
            groups.append((" ".join(cur), e_verb(w[i], verbs)))
            cur, i = [], i + 1
        else:
            cur.append(w[i])
            i += 1
    if cur or not groups:
        raise ValueError(f"no object + verb in {text!r}")
    for o, _ in groups:
        obj_vi(o, M)                       # raises on an unknown object
    return groups


def ov(o, v, M):                           # one object + verb: «V A» (Vietnamese verb before the object)
    return f"{v.vi} {obj_vi(o, M)}"


# ===============================================================================================================
# FAMILY E 3. Person subjects (nominative). Registries are passed in (Persons); this chapter's are below.
# ===============================================================================================================
class Persons:
    """nom: Pāli nominative phrase → (Vietnamese, number); acc: Pāli accusative (after ṭhapetvā, '-ñca' as '-ṃ')
    → Vietnamese; rel_np: the noun of "ye ca <NP> … te" → plural Vietnamese; rel_vp: the verb phrase of a
    "ye" clause → Vietnamese."""

    def __init__(self, nom, acc, rel_np, rel_vp):
        self.nom, self.acc, self.rel_np, self.rel_vp = dict(nom), dict(acc), dict(rel_np), dict(rel_vp)

    def extended(self, nom=None, acc=None, rel_np=None, rel_vp=None):
        p = copy.deepcopy(self)
        p.nom.update(nom or {})
        p.acc.update(acc or {})
        p.rel_np.update(rel_np or {})
        p.rel_vp.update(rel_vp or {})
        return p


ARAHA = "bậc A-la-hán"                                   # Arahā / arahantañca (termbase)
AGGAMAGGASAMANGI = "người có được con đường tối thượng"   # Aggamaggasamaṅgī / Aggamaggasamaṅgiñca (termbase)
PUTHUJJANA_PL = "những người phàm phu"                    # puthujjanā (termbase «người phàm phu», plural «những»)
MAGGAM_PATILABHISSANTI = "sẽ đạt được con đường"          # maggaṃ paṭilabhissanti (termbase)
MAGGAM_NA_PATILABHISSANTI = "sẽ không đạt được con đường"  # maggaṃ na paṭilabhissanti (separate na: «sẽ không …»)
AVASESA_PUGGALA = "những hạng người còn lại"              # avasesā puggalā (termbase Avasesā «còn lại», puggalā «hạng người»)
EXCEPT = B.EXCEPT                                          # ṭhapetvā «Ngoại trừ» (2-01)
YE = B.YE                                                  # Ye … «Những người nào» (2-01)
REL = "nào"                                                # ye ca <NP> … «<NP> nào …»
TE = C.PRON["tesaṃ"]                                       # te «những người ấy» (= 7-03 PRON_NOM['te'])
THEN = C.THEN                                              # «thì»
BUT = C.BUT                                                # no ca «nhưng»
ALSO = C.ALSO                                              # both-frame «cũng»
AND = C.AND                                                # «và»

PERSONS = Persons(
    nom={"Arahā": (ARAHA, 1), "Aggamaggasamaṅgī": (AGGAMAGGASAMANGI, 1)},
    acc={"Aggamaggasamaṅgiṃ": AGGAMAGGASAMANGI, "arahantaṃ": ARAHA},
    rel_np={"puthujjanā": PUTHUJJANA_PL},
    rel_vp={"maggaṃ paṭilabhissanti": MAGGAM_PATILABHISSANTI, "maggaṃ na paṭilabhissanti": MAGGAM_NA_PATILABHISSANTI},
)


def _nom(txt, P):
    """Longest registered nominative person at the start of txt → (key, rest) or (None, txt)."""
    for k in sorted(P.nom, key=len, reverse=True):
        if txt == k or txt.startswith(k + " "):
            return k, txt[len(k):].strip()
    return None, txt


def _acc_list(txt, P):
    """'Aggamaggasamaṅgiñca arahantañca' / 'X' → [Vietnamese, …] (accusatives before ṭhapetvā)."""
    keys = sorted(P.acc, key=len, reverse=True)
    for k in keys:
        if txt == k:
            return [P.acc[k]]
    out = []
    for w in txt.split():
        k = w[:-3] + "ṃ" if w.endswith("ñca") else None
        if k is None or k not in P.acc:
            raise ValueError(f"unknown person before ṭhapetvā: {w!r} in {txt!r}")
        out.append(P.acc[k])
    if len(out) < 2:
        raise ValueError(f"'-ñca' on a single person: {txt!r}")
    return out


def except_head(accs):                     # X-ñca Y-ñca ṭhapetvā avasesā puggalā «Ngoại trừ X và Y, những hạng người còn lại»
    return f"{EXCEPT} {B.join_and(accs)}, {AVASESA_PUGGALA}"


def ye_head(vp):                           # Ye <VP> te «Những người nào <VP>, thì những người ấy»
    return f"{YE} {vp}, {THEN} {TE}"


def ye_ca_head(person, np_pl, vp):         # P ye ca <NP> <VP> te «P và <NP> nào <VP>, thì những người ấy»
    return f"{cap(person)} {AND} {np_pl} {REL} {vp}, {THEN} {TE}"


def e_head(txt, P=None):
    """Pāli words before the clause → (Vietnamese head, number, rest). Raises on anything unregistered."""
    P = P or PERSONS
    if m := re.fullmatch(r"(.+?) ṭhapetvā avasesā puggalā (.+)", txt):
        return except_head(_acc_list(m.group(1), P)), 2, m.group(2)
    if m := re.fullmatch(r"Ye (.+?) te (.+)", txt):
        if m.group(1) not in P.rel_vp:
            raise ValueError(f"unknown 'ye' clause {m.group(1)!r}")
        return ye_head(P.rel_vp[m.group(1)]), 2, m.group(2)
    key, rest = _nom(txt, P)
    if key is None:
        return None, 0, txt                # no head: a bare answer («Hiểu biết trọn vẹn …»)
    if m := re.fullmatch(r"ye ca (\S+) (.+?) te (.+)", rest):
        if m.group(1) not in P.rel_np or m.group(2) not in P.rel_vp:
            raise ValueError(f"unknown 'ye ca' clause in {txt!r}")
        return ye_ca_head(P.nom[key][0], P.rel_np[m.group(1)], P.rel_vp[m.group(2)]), 2, m.group(3)
    return cap(P.nom[key][0]), P.nom[key][1], rest


# ===============================================================================================================
# FAMILY E 4. Answer frames
# ===============================================================================================================
def e_single(head, o_vi, v_vi):            # P A V. «P V A.» / bare: «V A.»
    return f"{head} {v_vi} {o_vi}." if head else f"{cap(v_vi)} {o_vi}."


def e_noca(head, o1, v1, noca_part):       # P A V1, no ca B V2. «P V1 A, nhưng <noca part>.»
    """noca_part = still_vi(…) for a negative V2 («vẫn V B», «đã từng V B», «vẫn sẽ V B») or neither_vi(…) for a
    positive V2 («không V B[, cũng không V C]»)."""
    return f"{head} {v1} {o1}, {BUT} {noca_part}." if head else f"{cap(v1)} {o1}, {BUT} {noca_part}."


def e_both(head, o1, v1, o2, v2):          # P A-ñca V1 B-ñca V2. «P V1 A, cũng V2 B.»  (7-01 / 7-03 / 7-05 both-frame)
    return f"{head} {v1} {o1}, {ALSO} {v2} {o2}." if head else f"{cap(v1)} {o1}, {ALSO} {v2} {o2}."


def _num_ok(head_num, v, s):
    if head_num and v.number and v.number != head_num:
        raise ValueError(f"verb number does not fit the subject: {s!r}")


def e_sentence(s, M, verbs=None, persons=None):
    """One family-E answer sentence, or None if it has no family-E verb."""
    if not s.endswith("."):
        raise ValueError(f"sentence without «.»: {s!r}")
    body = s[:-1]
    if not any(is_e_verb(w, verbs) for w in body.replace(",", "").split()):
        return None
    main, _, neg = body.partition(", no ca ")
    head, num, rest = e_head(main, persons)
    groups = split_groups(rest, M, verbs)
    for _, v in groups:
        _num_ok(num, v, s)
    def one_ok(o):                          # one group: a single item, or a list with 'ca' on every item
        r = obj_run(o, M)
        return not r["conj"] or len(r["names"]) > 1

    if neg:
        ng = split_groups(neg, M, verbs)
        if len(groups) != 1 or len(ng) != 1 or not one_ok(groups[0][0]):
            raise ValueError(f"unknown 'no ca' shape: {s!r}")
        _num_ok(num, ng[0][1], s)
        (o1, v1), (o2, v2) = groups[0], ng[0]
        part = still_vi(o2, M, v2) if v2.negative else neither_vi(o2, M, v2)
        return e_noca(head, obj_vi(o1, M), v1.vi, part)
    if len(groups) == 1 and one_ok(groups[0][0]):
        o, v = groups[0]
        return e_single(head, obj_vi(o, M), v.vi)
    if len(groups) == 2 and all(conj(o, M) for o, _ in groups):
        (o1, v1), (o2, v2) = groups
        return e_both(head, obj_vi(o1, M), v1.vi, obj_vi(o2, M), v2.vi)
    raise ValueError(f"unknown family-E sentence shape: {s!r}")


# ===============================================================================================================
# FAMILY E 5. Questions: yo / so (nominative person shell; = 7-03 yo_q wording, no «ở»)
# ===============================================================================================================
WHO, THAT = C.Q_REL["yassa"]               # «người nào» / «người ấy»
OTHER = C.VA_PANA                          # vā pana «Còn»


def yo_q(a, b, label=None, vapana=False):
    """(Ka) yo A so B ti? = «(a) Người nào mà A, thì người ấy có phải B không?»; (Kha) … vā pana … = «(b) Còn người
    nào mà …». a / b = the slots («hiểu biết trọn vẹn khối vật chất»)."""
    s = cap(f"{OTHER + ' ' if vapana else ''}{WHO} mà {a}, {THEN} {THAT} có phải {b} không?")
    return f"{LABEL[label]} {s}" if label else s


YO_RE = re.compile(r"(?:\((Ka|Kha|Ga|Gha|Ṅa|Ca)\) )?([Yy])o( vā pana)? (.+?) so (.+?)\?(?: (.+))?")


def e_question(body, M, verbs=None, persons=None):
    """A "yo … so …ti?" line (+ answers on the same line) → Vietnamese, or None if it is not one."""
    m = YO_RE.fullmatch(body)
    if not m:
        return None
    label, y, vapana, a, b, rest = m.groups()
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {body!r}")
    if label in ("Ka", "Kha") and (label == "Kha") != bool(vapana):
        raise ValueError(f"label {label} with vā pana={bool(vapana)}: {body!r}")
    ga, gb = split_groups(a, M, verbs), split_groups(b, M, verbs)
    if len(ga) != 1 or len(gb) != 1 or not single(ga[0][0], M) or not single(gb[0][0], M):
        raise ValueError(f"question slots must be one object + verb: {body!r}")
    out = yo_q(ov(*ga[0], M), ov(*gb[0], M), label, bool(vapana))
    return out + (" " + e_answers(rest, M, verbs, persons) if rest else "")


def e_answers(text, M, verbs=None, persons=None):
    out = []
    for x in [x for x in re.split(r"(?<=\.) ", text.strip()) if x]:
        if x in C.EXACT:
            out.append(C.EXACT[x])
        elif (r := e_sentence(x, M, verbs, persons)) is not None:
            out.append(r)
        else:
            raise ValueError(f"unknown family-E answer {x!r}")
    return " ".join(out)


def e_line(body, M, verbs=None, persons=None):
    """A family-E line body (no block ID): a question (+ answers) or a run of answers; None if not family E."""
    if (q := e_question(body, M, verbs, persons)) is not None:
        return q
    parts = [x for x in re.split(r"(?<=\.) ", body.strip()) if x]
    if parts and all(p in C.EXACT or any(is_e_verb(w, verbs) for w in p.replace(",", "").split()) for p in parts) \
            and any(p not in C.EXACT for p in parts):
        return e_answers(body, M, verbs, persons)
    return None


# ===============================================================================================================
# Family B additions for 2-02 (2-01 did not have these heads / cut lines); the frames are B's, unchanged
# ===============================================================================================================
YE_CA = "ye ca"
KHI_CAVANTA = f"khi {TE} {B.PARTICIPLES['cavantānaṃ'][0]}"   # (ye ca …) tesaṃ cavantānaṃ «khi những người ấy đang chết đi»


def b_head(head, loc, planes=None):
    """B.answer_head, plus "P… ye ca <plane> upapajjitvā parinibbāyissanti [tesaṃ cavantānaṃ]":
    «Ở <P> và những người nào sau khi tái sinh vào cõi X sẽ nhập Niết-bàn trọn vẹn[, khi những người ấy đang chết đi]»
    (one «Ở» for the run of person groups; the ye clause = B.ye_clause)."""
    if f" {YE_CA} " not in head:
        return B.answer_head(head, loc, planes)
    left, right = head.split(f" {YE_CA} ", 1)
    cav = right.endswith(" tesaṃ cavantānaṃ")
    if cav:
        right = right[: -len(" tesaṃ cavantānaṃ")]
    ye = B.ye_clause("Ye " + right, planes)
    ye = ye[0].lower() + ye[1:]
    return f"{B.AT} {B.persons(left, planes)} {AND} {ye}" + (f", {KHI_CAVANTA}" if cav else "")


LOCS = ("tesaṃ tattha", "tesaṃ", "tattha")


def _is_member(w, M):
    try:
        M.key(w)
        return True
    except ValueError:
        return False


def b_sentence(s, M, planes=None):
    """Family-B answer with a person / place head: the no-ca frame (B.b_noca) and the both-frame (B.b_both).
    The head is everything before the resumptive that stands right before the first member word."""
    if not s.endswith("."):
        return None
    w = s[:-1].split()
    i = next((k for k, x in enumerate(w) if _is_member(x.rstrip(","), M)), None)
    if not i:
        return None
    if i >= 2 and " ".join(w[i - 2:i]) == "tesaṃ tattha":
        loc, h = "tesaṃ tattha", i - 2
    elif w[i - 1] in ("tesaṃ", "tattha"):
        loc, h = w[i - 1], i - 1
    else:
        return None
    head = " ".join(w[:h])
    clause = " ".join(w[i:])
    head_vi = b_head(head, loc, planes)
    if f", no ca {loc} " in clause:
        c1, c2 = clause.split(f", no ca {loc} ")
        a, v1 = B.split_mv(c1, M)
        b, v2 = B.split_mv(c2, M)
        return B.b_noca(head_vi, loc, a, v1, b, v2)
    if ", no ca " in clause:
        raise ValueError(f"'no ca' pronoun does not fit {loc!r}: {s!r}")
    # both-frame: A [ca] V1[,] B [ca] V2  (the second member word starts the second half)
    t = clause.split()
    j = next((k for k, x in enumerate(t) if k > 0 and _is_member(x, M)), None)
    if j is None:
        raise ValueError(f"no second member in {s!r}")
    h1, h2 = t[:j], t[j:]
    if h1[-1].endswith(","):
        h1[-1] = h1[-1][:-1]
        SLIPS_SEEN.append(("comma inside the both-frame (absorbed by «, … cũng …»)", s[:70]))
    ca1, ca2 = len(h1) > 1 and h1[1] == "ca", len(h2) > 1 and h2[1] == "ca"
    if not (ca1 or ca2):
        raise ValueError(f"no 'ca' in a two-verb answer: {s!r}")
    if not (ca1 and ca2):
        SLIPS_SEEN.append(("missing 'ca' in the both-frame (rendered as the both-frame)", s[:90]))
    a, v1 = M.subj(h1[0]), B.verb(" ".join(h1[2 if ca1 else 1:]))
    b, v2 = M.subj(h2[0]), B.verb(" ".join(h2[2 if ca2 else 1:]))
    return B.b_both(head_vi, loc, a, v1, b, v2)


# --- cut lines of family B -------------------------------------------------------------------------------------
YATTHAKAM_FULL = "phần về nơi chốn nên được trình bày đầy đủ"   # (yatthakaṃ paripuṇṇaṃ kātabbaṃ): termbase yatthakaṃ
CUT_RE = re.compile(r"(Yattha|Yassa) (.+?)(…pe…\.| \(yatthakaṃ paripuṇṇaṃ kātabbaṃ\)\.)")


def b_cut(body, M):
    """'Yattha A V…pe….' → «Ở nơi nào mà A V…»; 'Yattha A V (yatthakaṃ paripuṇṇaṃ kātabbaṃ).' →
    «Ở nơi nào mà A V (phần về nơi chốn nên được trình bày đầy đủ).» (the question shell's first half)."""
    m = CUT_RE.fullmatch(body)
    if not m:
        return None
    a, v = B.split_mv(m.group(2), M)
    who = C.Q_REL[m.group(1).lower()][0]
    first = f"{cap(C.AT)} {who} mà {a} {v[0]}"
    return first + (S.PE if m.group(3).startswith("…") else f" ({YATTHAKAM_FULL}).")


def pe_tail(s, fn):
    """'<sentence>…pe….' → fn('<sentence>.') with its «.» turned into «…» (same spot; = 7-03 pe_tail)."""
    m = re.fullmatch(r"(.+?)( ?)…pe…\.", s)
    if not m:
        return None
    vi = fn(m.group(1) + ".")
    assert vi.endswith("."), vi
    return vi[:-1] + m.group(2) + S.PE


# ===============================================================================================================
# Headings and fixed lines of 2-02
# ===============================================================================================================
H = dict(S.LATER_HEADINGS)
PARINNAVARO = H["Pariññāvāro"]                              # Mục về sự hiểu biết trọn vẹn
PARINNAVARO_CLOSE = PARINNAVARO + "."                       # Pariññāvāro. (closing; = 7-01 «Uppattiṭṭhānavāro.»)
NIRODHAVARO_CLOSE = cap(B.NIRODHAVARO) + "."                # Nirodhavāro. «Mục về sự chấm dứt.»
UPPADANIRODHAVARO_CLOSE = cap(B.UPPADANIRODHAVARO) + "."    # Uppādanirodhavāro. «Mục về sự sinh khởi và sự chấm dứt.»
HEADINGS = {
    "Uppādanirodhavāro": cap(B.UPPADANIRODHAVARO),
    "Pariññāvāro": PARINNAVARO,
    **{f"{t}vāro": f"Mục về {v}" for t, v in B.TIME.items()},   # unnumbered time sections (pariññāvāra)
}
# (Yathā X vibhattaṃ tathā idha vibhajitabbaṃ): pi-2 1-khandhavibhango «Như đã được phân tích trong …, ở đây cũng
# nên phân tích như vậy.»; paccuppannātītaṃ = the section «mục về hiện tại và quá khứ»; uppādavāre (termbase).
YATHA_IDHA = (f"(Mục về {B.TIME['Paccuppannātīta']} như đã được phân tích trong {B.UPPADAVARO}, "
              f"ở đây cũng nên phân tích như vậy).")
FIXED = {
    "Nirodhavāro.": NIRODHAVARO_CLOSE,
    "Uppādanirodhavāro.": UPPADANIRODHAVARO_CLOSE,
    "Pariññāvāro.": PARINNAVARO_CLOSE,
    "Khandhayamakapāḷi niṭṭhitā.": S.yamaka_end("Khandha"),
    "Namo tassa bhagavato arahato sammāsambuddhassa": S.HOMAGE,
    "(Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ).": YATHA_IDHA,
}


def heading(text):
    if text in HEADINGS:
        return HEADINGS[text]
    return B.heading(text, "khối", "Khandha")


# Members: 2-01's KHANDHA plus the slip vadanākkhandho (termbase lists it: «khối cảm giác»)
KHANDHA = copy.deepcopy(B.KHANDHA)
MEMBER_SLIPS = {"vadanākkhandho": "vedanākkhandha"}          # ^6-2-185: vadanā- for vedanā- (spelling slip)
for _f, _k in MEMBER_SLIPS.items():
    KHANDHA.form[_f] = _k


# ===============================================================================================================
# Line translator
# ===============================================================================================================
def sentence(s, M, planes=None):
    if (t := pe_tail(s, lambda x: sentence(x, M, planes))) is not None:
        return t
    if s in B.SHORT:
        return B.SHORT[s]
    if s in B.CLOSING:
        return B.CLOSING[s]
    if s in FIXED:
        return FIXED[s]
    if (r := e_sentence(s, M)) is not None:
        return r
    if (r := b_sentence(s, M, planes)) is not None:
        return r
    raise ValueError(f"unknown sentence {s!r}")


def sentences(rest, M, planes=None):
    return " ".join(sentence(x, M, planes) for x in re.split(r"(?<=\.) ", rest.strip()) if x)


def tr_line(p, M=KHANDHA, planes=None):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    for w in MEMBER_SLIPS:
        if w in body:
            SLIPS_SEEN.append((f"{w} (rendered as meant)", body[:70]))
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    elif body in FIXED:
        out = FIXED[body]
    elif (c := b_cut(body, M)) is not None:
        out = c
    elif (q := e_question(body, M)) is not None:
        out = q
    elif (q := B.b_question(body, M)) is not None:
        out, rest = q
        if rest.strip():
            out += " " + sentences(rest, M, planes)
    else:
        out = sentences(body, M, planes)
    return f"{out} {bid}" if bid else out


def build(name=CH, M=KHANDHA, planes=None):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln, M, planes))
            except ValueError as e:
                raise ValueError(f"{name}: cannot place line {ln[:140]!r}: {e}") from None
        segs.append(out)
    return segs


# ===============================================================================================================
# Assertions: termbase entries used verbatim, reused pi-N strings, agreement with families B / C
# ===============================================================================================================
TERMBASE_USED = [
    ("parijānāti", PARIJANATI), ("parijānātīti", PARIJANATI), ("parijānanti", PARIJANATI),
    ("parijānittha", "đã " + PARIJANATI), ("parijānitthāti", "đã " + PARIJANATI),
    ("parijānissati", "sẽ " + PARIJANATI), ("parijānissatīti", "sẽ " + PARIJANATI),
    ("parijānissanti", "sẽ " + PARIJANATI),
    ("Arahā", ARAHA), ("arahantañca", ARAHA), ("Aggamaggasamaṅgī", AGGAMAGGASAMANGI),
    ("Aggamaggasamaṅgiñca", AGGAMAGGASAMANGI), ("puggalā", "hạng người"), ("puthujjanā", "người phàm phu"),
    ("maggaṃ paṭilabhissanti", MAGGAM_PATILABHISSANTI), ("paṭilabhissanti", "sẽ đạt được"),
    ("ṭhapetvā", "ngoại trừ"), ("Avasesā", "còn lại"), ("Pariññāvāro", "mục về sự hiểu biết trọn vẹn"),
    ("Uppādanirodhavāro", "mục về sự sinh khởi và sự chấm dứt"), ("nirodhavāro", "mục về sự chấm dứt"),
    ("uppādavāre", "mục về sự sinh khởi"), ("yatthakaṃ", "phần về nơi chốn"), ("vadanākkhandho", "khối cảm giác"),
    ("Yattha", "ở nơi nào"), ("Khandhayamakapāḷi", "các cặp câu hỏi về các khối"),
    ("Atītānāgatavāro", "mục về quá khứ và tương lai"),
]
REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("(Yathā rūpakaṇḍe vibhattaṃ, tathā idha vibhajitabbaṃ.) (pi-2 1-khandhavibhango)", "như đã được phân tích trong", "2"),
    ("… tathā idha vibhajitabbaṃ", "ở đây cũng nên phân tích như vậy", "2"),
    ("parijānāti (pi-5 12-catutthavaggo)", PARIJANATI, "5"),
    ("maggaṃ (pi-5 10-dutiyavaggo)", "con đường", "5"),
    ("puthujjano", "người phàm phu", "1"),
]


def check_assertions():
    tb = TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M | re.I)]
    assert not bad, "termbase strings not found: " + repr(bad)
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    # the family-E tense rule reproduces family B's VERB_TABLE (2-01) for uppajjati / nirujjhati
    for (pos, neg, pv, nv), base, tense in zip(B.VERB_TABLE, ["sinh khởi"] * 3 + ["chấm dứt"] * 3,
                                               ["present", "past", "future"] * 2):
        assert tense_vi(base, tense) == (pv, nv), (base, tense, pv, nv)
    assert C.FAMILY_TERMS["parijānāti"] == PARIJANATI and C.FAMILY_TERMS["na parijānāti"] == E_VERBS["na parijānāti"].vi
    assert B.denied_vi("đã x") == "đã từng x" and B.denied_vi("x") == "vẫn x" and B.denied_vi("sẽ x") == "vẫn sẽ x"
    # module self-test on shapes later chapters meet (not in 2-02; nothing is written)
    M = KHANDHA
    assert e_sentence("Arahā rūpakkhandhaṃ na parijānāti, no ca vedanākkhandhañca saññākkhandhañca na parijānittha.",
                      M) == ("Bậc A-la-hán không hiểu biết trọn vẹn khối vật chất, nhưng đã từng hiểu biết trọn vẹn "
                             "khối cảm giác và khối tri giác.")
    assert e_sentence("Arahā rūpakkhandhaṃ parijānittha, no ca vedanākkhandhañca saññākkhandhañca parijānāti.",
                      M) == ("Bậc A-la-hán đã hiểu biết trọn vẹn khối vật chất, nhưng không hiểu biết trọn vẹn "
                             "khối cảm giác, cũng không hiểu biết trọn vẹn khối tri giác.")
    assert e_sentence("Rūpakkhandhaṃ parijānāti.", M) == "Hiểu biết trọn vẹn khối vật chất."
    assert e_sentence("Arahā rūpakkhandhañca vedanākkhandhañca parijānittha.", M) == \
        "Bậc A-la-hán đã hiểu biết trọn vẹn khối vật chất và khối cảm giác."
    for bad in ("Arahā rūpakkhandhaṃ parijānanti.", "Arahā rūpakkhandhañca parijānittha.",
                "Anāgāmī rūpakkhandhaṃ parijānāti.", "Arahā rūpaṃxyz parijānāti."):
        try:
            e_sentence(bad, M)
        except ValueError:
            continue
        raise AssertionError(f"no error on {bad!r}")
    # the yo shell is the coordinator's person shell without «ở» (7-03 wording)
    assert yo_q("A", "B", "Ka") == "(a) Người nào mà A, thì người ấy có phải B không?"
    assert yo_q("B", "A", "Kha", True) == "(b) Còn người nào mà B, thì người ấy có phải A không?"


# ===============================================================================================================
# Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = KHANDHA
    out = [f"# pi-6 rails {N} (Khandhayamaka 2): family E (pariññāvāra) frames; family B additions", "",
           "Builder: build_rails_2-02_vi.py (family E setter; import with importlib). Family E API: `PARIJANATI`, "
           "`TENSE_VI`, `tense_vi`, `make_verbs`, `rows_na`, `rows_fused`, `E_VERBS`, `e_verb`, `denied`, `obj_vi`, "
           "`split_groups`, `Persons` / `PERSONS` (.extended(nom=, acc=, rel_np=, rel_vp=)), `e_head`, `except_head`, "
           "`ye_head`, `ye_ca_head`, `e_single`, `e_noca`, `e_both`, `e_sentence`, `yo_q`, `e_question`, "
           "`e_answers`, `e_line`. A later chapter passes its own `Members` (2-01 class), its verbs merged into "
           "E_VERBS (same tense rule) and its persons via PERSONS.extended(...). Families A / B come from "
           "build_rails_2-01_vi, family C shapes from build_rails_7-01_vi, unchanged. Format: Pāli = tiếng Việt.",
           ""]

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    h("Family E: verbs (tense rule = family B's VERB_TABLE; asserted)")
    row("<V> present / past / future (positive)", "«V» / «đã V» / «sẽ V»")
    row("<V> present / past / future (negative, separate na or fused)", "«không V» / «chưa từng V» / «sẽ không V»")
    for f, v in E_VERBS.items():
        row(f, v.vi)
    row("after no ca, negative verb (denied)", "present «vẫn V», past «đã từng V», future «vẫn sẽ V» (B.denied_vi)")
    row("after no ca, positive verb", "the verb's own negative: «không V» / «chưa từng V» / «sẽ không V»")
    h("Family E: question shell (yo / so; = coordinator person shell without «ở», as 7-03)")
    row("(Ka) yo A V1 so B V2ti?", yo_q("V1 A", "V2 B", "Ka"))
    row("(Kha) yo vā pana B V1 so A V2ti?", yo_q("V1 B", "V2 A", "Kha", True))
    row("Yo … so …ti? (no label)", yo_q("V1 A", "V2 B"))
    for q in ("(Ka) yo rūpakkhandhaṃ parijānāti so vedanākkhandhaṃ parijānātīti?",
              "(Kha) yo vā pana vedanākkhandhaṃ na parijānittha so rūpakkhandhaṃ na parijānātīti?",
              "(Ka) yo rūpakkhandhaṃ na parijānāti so vedanākkhandhaṃ na parijānissatīti?"):
        row(q, e_question(q, M))
    h("Family E: answer heads (nominative persons)")
    for k, (v, n) in PERSONS.nom.items():
        row(f"{k} … ({'sg' if n == 1 else 'pl'})", f"{cap(v)} …")
    row("X-ñca Y-ñca ṭhapetvā avasesā puggalā …", except_head(["X", "Y"]) + " …")
    row("Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā …",
        e_head("Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā x")[0] + " …")
    row("Ye <VP> te …", ye_head("<VP>") + " …")
    row("Ye maggaṃ paṭilabhissanti te …", e_head("Ye maggaṃ paṭilabhissanti te x")[0] + " …")
    row("<P> ye ca <NP> <VP> te …", ye_ca_head("<P>", "<NP>", "<VP>") + " …")
    row("Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te …",
        e_head("Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te x")[0] + " …")
    row("Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te …",
        e_head("Aggamaggasamaṅgī ye ca puthujjanā maggaṃ na paṭilabhissanti te x")[0] + " …")
    for k, v in PERSONS.rel_vp.items():
        row(k, v)
    h("Family E: answer frames")
    row("P A V.", e_single("P", "A", "V"))
    row("A V. (bare answer, e.g. 7-07 «Tadekaṭṭhaṃ parijānāti.»)", e_single(None, "A", "V"))
    row("P A V1, no ca B V2 (V2 negative: denied)", e_noca("P", "A", "V1", "vẫn V2 B / đã từng V2 B / vẫn sẽ V2 B"))
    row("P A V1, no ca B V2 (V2 positive)", e_noca("P", "A", "V1", "không V2 B / chưa từng V2 B / sẽ không V2 B"))
    row("…, no ca B ca C ca V2 (positive; neither)", e_noca("P", "A", "V1", "không V2 B, cũng không V2 C"))
    row("…, no ca B ca C ca na V2 (negative; the list denied)", e_noca("P", "A", "V1", "vẫn V2 B và C"))
    row("P A ca B ca V. (one verb, a list)", e_single("P", "A và B", "V"))
    row("P A-ñca V1 B-ñca V2.", e_both("P", "A", "V1", "B", "V2"))
    for s in ("Arahā rūpakkhandhaṃ na parijānāti, no ca vedanākkhandhaṃ na parijānittha.",
              "Aggamaggasamaṅgiñca arahantañca ṭhapetvā avasesā puggalā rūpakkhandhañca na parijānanti "
              "vedanākkhandhañca na parijānittha.",
              "Ye maggaṃ paṭilabhissanti te rūpakkhandhaṃ na parijānanti, no ca vedanākkhandhaṃ na parijānissanti.",
              "Arahā ye ca puthujjanā maggaṃ na paṭilabhissanti te rūpakkhandhañca na parijānanti "
              "vedanākkhandhañca na parijānissanti.",
              "Aggamaggasamaṅgī vedanākkhandhaṃ na parijānissati, no ca rūpakkhandhaṃ na parijānāti."):
        row(s, e_sentence(s, M))
    h("Headings and closing lines")
    for k, v in HEADINGS.items():
        row(k, v)
    for k, v in FIXED.items():
        row(k, v)
    h("Family B additions (2-01 frames, new heads / cut lines)")
    row("<persons> ye ca <plane-acc> upapajjitvā parinibbāyissanti tesaṃ …",
        b_head("Pacchimabhavikānaṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ")
        + f", {C.THEN} {B.L['tesaṃ']} …")
    row("<persons> ye ca <plane-acc> upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ …",
        b_head("Pacchimabhavikānaṃ arūpaṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ",
               "tesaṃ") + f", {C.THEN} {B.L['tesaṃ']} …")
    row("tesaṃ cavantānaṃ (after a ye ca clause)", KHI_CAVANTA)
    row("Yattha A V…pe….", b_cut("Yattha rūpakkhandho nirujjhati…pe….", M))
    row("Yattha A V (yatthakaṃ paripuṇṇaṃ kātabbaṃ).",
        b_cut("Yattha rūpakkhandho na nirujjhati (yatthakaṃ paripuṇṇaṃ kātabbaṃ).", M))
    row("<sentence>…pe….", "<câu>…  (7-03 pe_tail)")
    row("A ca V1, B ca V2 (comma) / A ca V1 B V2 / A V1 B ca V2 (one ca missing)", "the both-frame «A V1, B cũng V2»")
    h("Termbase gaps and choices (for the coordinator)")
    out += [
        "- na parijānittha «chưa từng hiểu biết trọn vẹn»: no termbase entry for the negative past; built by the "
        "family-B rule (na nirujjhittha «chưa từng chấm dứt», nuppajjittha «chưa từng sinh khởi»). Likewise "
        "na parijānissati / na parijānissanti «sẽ không hiểu biết trọn vẹn», na parijānanti «không hiểu biết trọn vẹn».",
        "- No-pronoun 'no ca' (person subject, transitive verb): denied negative «nhưng vẫn V B» / «nhưng đã từng V B» "
        "/ «nhưng vẫn sẽ V B»; positive «nhưng không V B» (the verb's own negative; = 7-05 «nhưng không dứt bỏ A, "
        "cũng không dứt bỏ B»; 7-01's «không có B V» is the intransitive-subject frame and does not fit an object). "
        "A denied negative LIST «nhưng vẫn V B và C» is built by analogy with the coordinator's «A và B vẫn V» "
        "(not met in 2-02; for the coordinator to confirm).",
        "- maggaṃ na paṭilabhissanti «sẽ không đạt được con đường» (termbase has only the positive; separate na).",
        "- avasesā puggalā «những hạng người còn lại» (termbase Avasesā «còn lại» + puggalā «hạng người»).",
        "- puthujjanā in «… ye ca puthujjanā … te» = «những người phàm phu nào …» (termbase «người phàm phu»).",
        "- (yatthakaṃ paripuṇṇaṃ kātabbaṃ): termbase yatthakaṃ «phần về nơi chốn»; paripuṇṇaṃ kātabbaṃ has no "
        "entry: «nên được trình bày đầy đủ».",
        "- (Yathā uppādavāre paccuppannātītaṃ vibhattaṃ tathā idha vibhajitabbaṃ): pi-2's «như đã được phân tích "
        "trong …, ở đây cũng nên phân tích như vậy»; paccuppannātītaṃ = «mục về hiện tại và quá khứ»; the Pāli has no "
        "comma, the Vietnamese clause break takes one; the Pāli's «).» kept.",
        "- tesaṃ cavantānaṃ after a ye ca clause: «khi những người ấy đang chết đi» (the dying applies to the ye group).",
        "",
        "## Slips (translated as written or as plainly meant)",
        "",
    ]
    out += [
        "- ^6-2-185 «vadanākkhandho» for vedanākkhandho (spelling slip; termbase lists it): «khối cảm giác».",
        "- ^6-2-134 «saññākkhandho ca nirujjhissati vedanākkhandho nirujjhati» (second «ca» missing) and ^6-2-163 "
        "«rūpakkhandho nuppajjati vedanākkhandho ca na nirujjhati» (first «ca» missing): rendered as the both-frame "
        "«A V1, B cũng V2», as the parallel lines.",
        "- ^6-2-151 «rūpakkhandho ca na nirujjhittha, vedanākkhandho ca na nirujjhissati»: the comma inside the "
        "both-frame is the frame's own «,».",
        "- ^6-2-130 «Yattha … (yatthakaṃ paripuṇṇaṃ kātabbaṃ).» and ^6-2-135 … «Yattha … …pe….»: cut opening halves "
        "of the place question, no «?» in the Pāli: «Ở nơi nào mà …» + the note / «…».",
        "- ^6-2-185 «…uppajjati…pe….» then the editorial note «(Yathā … vibhajitabbaṃ).»: kept as two lines.",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    check_assertions()
    segs = build(CH)
    C.write(CH, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for p, v in sorted(set(SLIPS_SEEN)):
        print("slip:", p, "|", v)


if __name__ == "__main__":
    main()
