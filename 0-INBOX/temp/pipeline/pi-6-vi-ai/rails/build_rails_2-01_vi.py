"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 2-01 (Khandhayamaka, part 1) and the FAMILY A / FAMILY B module.

Family A = paṇṇattivāra: padasodhana, padasodhanamūlacakka, suddha-X, suddha-X-mūlacakka, anuloma / paccanīka,
           the naming questions "(Ka) A B(ti)?" / "(Ka) na A na B(ti)?" and their answers.
Family B = pavattivāra: yassa / yattha / yassa yattha questions in every tense and mixed tense (uppajjati /
           nirujjhati), the answers naming persons (beings) and planes.

Later chapters import this file READ-ONLY and substitute their own members:

    import importlib, sys
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    B = importlib.import_module("build_rails_2-01_vi")
    M = B.Members({"cakkhu": ("mắt", "mắt", ["cakkhu"]), ...}, special={...})
    segs = B.build("3-01-ayatanayamaka.md", M, yamaka="Āyatana", variant_kind={...})

Every slot function takes the member names (Vietnamese) as arguments; the parsers raise ValueError on any
Pāli line, word or bracket they cannot place (no silent fallback). Extend the person / plane registries by
passing your own copies (planes=, persons=) rather than editing this file. Importing writes nothing; outputs are
written only under `if __name__ == "__main__":`.

usage: python -I -X utf8 -B build_rails_2-01_vi.py
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (read-only: labels, checks, writer)
C = importlib.import_module("build_rails_7-01_vi")   # read-only: the shared answer shapes (coordinator, 7-01)

LABEL = S.LABEL
cap = S.cap
CH = "2-01-khandhayamaka.md"
N = "2-01"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"


# ===============================================================================================================
# Members (each yamaka supplies its own)
# ===============================================================================================================
class Members:
    """table: key -> (subject form, predicate form, [Pāli citation forms, any case]).

    subject   = the noun as a sentence subject or object («các tạo tác», «các khối»);
    predicate = the noun after «là» / «không phải là» («tạo tác», «khối»).
    special   = Pāli phrase (lower case) -> Vietnamese noun phrase for the «hiểu theo nghĩa …» subjects
                (Piyarūpaṃ sātarūpaṃ, Diṭṭhisaññā …)."""

    def __init__(self, table, special=None):
        self.vi, self.form = {}, {}
        for key, (subj, pred, forms) in table.items():
            self.vi[key] = (subj, pred)
            for f in forms:
                f0 = f.lower()
                if f0 in self.form and self.form[f0] != key:
                    raise ValueError(f"form {f!r} given for {self.form[f0]!r} and {key!r}")
                self.form[f0] = key
        self.special = {k.lower(): v for k, v in (special or {}).items()}

    def key(self, tok):
        """Member key of a Pāli word in any of its written forms: -ti / -nti / -īti / -āti / -ūti, -ñca, -ñceva."""
        t = tok.lower()
        cands = {t}
        if t.endswith("ti"):
            cands.add(t[:-2])
        for end, rep in (("nti", "ṃ"), ("īti", "i"), ("āti", "a"), ("ūti", "u"), ("ñceva", "ṃ"), ("ñca", "ṃ")):
            if t.endswith(end):
                cands.add(t[:-len(end)] + rep)
        keys = {self.form[c] for c in cands if c in self.form}
        if len(keys) != 1:
            raise ValueError(f"member word {tok!r}: {'unknown' if not keys else 'ambiguous ' + repr(keys)}")
        return keys.pop()

    def subj(self, tok):
        return self.vi[self.key(tok)][0]

    def pred(self, tok):
        return self.vi[self.key(tok)][1]

    def sp(self, phrase):
        if phrase.lower() not in self.special:
            raise ValueError(f"unknown special subject {phrase!r}")
        return self.special[phrase.lower()]


# Khandhayamaka members (termbase: rūpaṃ «vật chất», vedanā «cảm giác», saññā «tri giác», saṅkhārā «tạo tác»,
# viññāṇaṃ «thức», X-kkhandho «khối X», khandho / khandhā «khối», Diṭṭhisaññā «tri giác hiểu theo nghĩa quan điểm»)
def _kh(stem, vi):
    return (f"khối {vi}", f"khối {vi}", [f"{stem}kkhandho", f"{stem}kkhandhaṃ"])


KHANDHA = Members({
    "rūpa": ("vật chất", "vật chất", ["rūpaṃ"]),
    "vedanā": ("cảm giác", "cảm giác", ["vedanā", "vedanaṃ"]),
    "saññā": ("tri giác", "tri giác", ["saññā", "saññaṃ"]),
    "saṅkhārā": ("các tạo tác", "tạo tác", ["saṅkhārā", "saṅkhāre"]),
    "viññāṇa": ("thức", "thức", ["viññāṇaṃ"]),
    "rūpakkhandha": _kh("rūpa", "vật chất"),
    "vedanākkhandha": _kh("vedanā", "cảm giác"),
    "saññākkhandha": _kh("saññā", "tri giác"),
    "saṅkhārakkhandha": _kh("saṅkhāra", "tạo tác"),
    "viññāṇakkhandha": _kh("viññāṇa", "thức"),
    "khandha": ("khối", "khối", ["khandho"]),
    "khandhā": ("các khối", "khối", ["khandhā", "khandhe"]),
}, special={
    # pi-2 4-saccavibhango: piyarūpaṃ sātarūpaṃ «điều đáng yêu, là điều khoan khoái» (here no «là»: a noun phrase)
    "Piyarūpaṃ sātarūpaṃ": "vật chất hiểu theo nghĩa điều đáng yêu, điều khoan khoái",
    "Diṭṭhisaññā": "tri giác hiểu theo nghĩa quan điểm",          # termbase
})

# ===============================================================================================================
# Headings (family A / B); approved strings from S.LATER_HEADINGS / the termbase
# ===============================================================================================================
H = dict(S.LATER_HEADINGS)
PANNATTIVARO = H["Paṇṇattivāro"]                         # Mục về sự định danh
PADASODHANAVARO = H["Padasodhanavāro"]                   # Mục về sự làm sáng tỏ thuật ngữ
PADASODHANAMULACAKKAVARO = H["Padasodhanamūlacakkavāro"]
ANULOMA, PACCANIKA = "Chiều thuận", "Chiều nghịch"     # (Ka) anulomaṃ / (Kha) paccanīkaṃ
PAVATTIVARO = H["Pavattivāro"]                           # Mục về sự diễn tiến
PAVATTI = "Sự diễn tiến"                                 # Pavatti (heading member, termbase «sự diễn tiến»)
UPPADAVARO = H["uppādavāro"]                             # mục về sự sinh khởi
NIRODHAVARO = H["nirodhavāro"]                           # mục về sự chấm dứt
UPPADANIRODHAVARO = "mục về sự sinh khởi và sự chấm dứt"  # Uppādanirodhavāro (termbase)
PANNATTIVARANIDDESA = "Phần giải thích của mục về sự định danh"   # Paṇṇattivāraniddesa (= Mūlavāraniddeso shape)
PANNATTI_UDDESAVARO = "Mục nêu đề mục về sự định danh"   # Paṇṇattiuddesavāro. (termbase)
PANNATTI_NIDDESAVARO = "Mục giải thích về sự định danh"  # Paṇṇattiniddesavāro. (termbase)


def suddha_varo(x_pl):                   # Suddha<X>vāro: «Mục về các <X> thuần túy»
    return f"Mục về các {x_pl} thuần túy"


def suddha_mulacakka_varo(x_pl):         # Suddha<X>mūlacakkavāro (termbase Suddhakhandhamūlacakkavāro)
    return f"Mục về vòng luân chuyển dựa trên các {x_pl} thuần túy"


TIME = {"Paccuppanna": "hiện tại", "Atīta": "quá khứ", "Anāgata": "tương lai",
        "Paccuppannātīta": "hiện tại và quá khứ", "Paccuppannānāgata": "hiện tại và tương lai",
        "Atītānāgata": "quá khứ và tương lai"}   # <T>vāro «Mục về <T>» (approved: hiện tại / quá khứ / tương lai)

ORDER = {"anuloma": "Chiều thuận", "paccanīka": "Chiều nghịch"}
BY = {"puggalo": "theo người", "okāso": "theo nơi chốn", "puggalokāsā": "theo người và nơi chốn"}

CLOSING = {   # closing lines of the family A / B sections
    "Paṇṇattiuddesavāro.": PANNATTI_UDDESAVARO + ".",
    "Paṇṇattiniddesavāro.": PANNATTI_NIDDESAVARO + ".",
    "Uppādavāro niṭṭhito.": f"{cap(UPPADAVARO)} {S.NITTHITO}.",
    "Nirodhavāro niṭṭhito.": f"{cap(NIRODHAVARO)} {S.NITTHITO}.",
    "Uppādanirodhavāro niṭṭhito.": f"{cap(UPPADANIRODHAVARO)} {S.NITTHITO}.",
    "Pavattivāro niṭṭhito.": f"{PAVATTIVARO} {S.NITTHITO}.",
    "Paṇṇattivāro niṭṭhito.": f"{PANNATTIVARO} {S.NITTHITO}.",
}


def heading(text, x_pl, yamaka):
    """Heading text (no #s, no block ID). x_pl = the member class word after «các» («khối», «lĩnh vực nhận biết» …)."""
    fixed = {
        f"{yamaka}yamakaṃ": S.yamaka_title(yamaka),
        "Paṇṇattivāro": PANNATTIVARO, "Padasodhanavāro": PADASODHANAVARO,
        "Padasodhanamūlacakkavāro": PADASODHANAMULACAKKAVARO,
        "(Ka) uddeso": f"{LABEL['Ka']} {S.UDDESO}", "(Kha) niddeso": f"{LABEL['Kha']} {S.NIDDESO}",
        "(Ka) anulomaṃ": f"{LABEL['Ka']} {ANULOMA}", "(Kha) paccanīkaṃ": f"{LABEL['Kha']} {PACCANIKA}",
        "Paṇṇattivāraniddesa": PANNATTIVARANIDDESA,
        "Pavattivāro 1. uppādavāro": f"{PAVATTIVARO} 1. {UPPADAVARO}",
        "Pavatti 2. nirodhavāro": f"{PAVATTI} 2. {NIRODHAVARO}",
        "Pavatti 3. uppādanirodhavāro": f"{PAVATTI} 3. {UPPADANIRODHAVARO}",
    }
    if text in fixed:
        return fixed[text]
    if m := re.fullmatch(r"Suddha(\w+?)vāro", text):
        if m.group(1).endswith("mūlacakka"):
            return suddha_mulacakka_varo(x_pl)
        return suddha_varo(x_pl)
    if m := re.fullmatch(r"\((\d)\) (\w+?)vāro", text):
        if m.group(2) not in TIME:
            raise ValueError(f"unknown time section {text!r}")
        return f"({m.group(1)}) Mục về {TIME[m.group(2)]}"
    if m := re.fullmatch(r"\((\w+)\) (anuloma|paccanīka)(puggalokāsā|puggalo|okāso)", text):
        return f"{LABEL[m.group(1)]} {ORDER[m.group(2)]} {BY[m.group(3)]}"
    raise ValueError(f"unknown heading {text!r}")


# ===============================================================================================================
# FAMILY A: naming questions (paṇṇattivāra) and their answers
# ===============================================================================================================
NEG_SUBJ = "Những gì không phải là"      # na A … (subject of a negated naming question)
REST = "những gì còn lại"                # avasesā (standing alone; termbase Avasesā «còn lại»)
EXCEPT = "Ngoại trừ"                     # X ṭhapetvā (termbase ṭhapetvā «ngoại trừ»)


def name_q(label, a, b, end="?"):
    """(Ka) A B(ti)?  a = subject form, b = predicate form."""
    return f"{LABEL[label]} {cap(a)} có phải là {b} không{end}"


def name_q_neg(label, a, b, end="?"):
    """(Ka) na A na B(ti)?  a, b = predicate forms."""
    return f"{LABEL[label]} {NEG_SUBJ} {a} thì không phải là {b}, có phải không{end}"


def both_is(a, b, c):                    # A Bñceva C ca. / A B ceva C ca.
    return f"{cap(a)} vừa là {b} vừa là {c}."


def rest_not_is(rest_subj, y, var=""):   # Avasesā khandhā [var] na Y.
    return f"{cap(rest_subj)} còn lại{var} không phải là {y}."


def special_is(sp, x, y):                # Piyarūpaṃ sātarūpaṃ X, na Y.
    return f"{cap(sp)} thì là {x}, nhưng không phải là {y}."


def special_not(sp, y, x):               # Piyarūpaṃ sātarūpaṃ na Y, X.
    return f"{cap(sp)} thì không phải là {y}, mà là {x}."


def except_is(m, x, y, var=""):          # M ṭhapetvā avasesā X [var], na Y.
    return f"{EXCEPT} {m}, {REST} là {x}{var}, nhưng không phải là {y}."


def except_not(m, y, x):                 # M ṭhapetvā avasesā na Y, X.
    return f"{EXCEPT} {m}, {REST} không phải là {y}, mà là {x}."


def except_rest_not(m, rest_subj, y, x):  # M ṭhapetvā avasesā khandhā na Y, X.
    return f"{EXCEPT} {m}, {rest_subj} còn lại không phải là {y}, mà là {x}."


def except2_neither(m1, m2, x, y):       # M1ñca M2ñca ṭhapetvā avasesā na ceva X na ca Y.
    return f"{EXCEPT} {m1} và {m2}, {REST} không phải là {x}, cũng không phải là {y}."


PH = r"(?: (⟦\d+⟧))?"                    # an optional protected variant bracket
LABEL_RE = r"\((Ka|Kha|Ga|Gha|Ṅa|Ca|Cha|Ja)\)"
NAME_Q_RE = re.compile(LABEL_RE + r" (na )?(\S+) (na )?(\S+?)([?.])((?: .*)?)")


def a_sentence(s, M):
    """One family-A answer sentence (ends with «.»), or None if it is not one."""
    if m := re.fullmatch(r"(\S+) (\S+?)(ñceva| ceva) (\S+) ca\.", s):
        b = m.group(2) + ("ñceva" if m.group(3) == "ñceva" else "")
        return both_is(M.subj(m.group(1)), M.pred(b), M.pred(m.group(4)))
    if m := re.fullmatch(r"Avasesā (\S+)" + PH + r" na (\S+)\.", s):
        return rest_not_is(M.subj(m.group(1)), M.pred(m.group(3)), f" {m.group(2)}" if m.group(2) else "")
    if m := re.fullmatch(r"(\S+?)(ñca| ca) (\S+?)(ñca| ca) ṭhapetvā avasesā na ceva (\S+) na ca (\S+)\.", s):
        a1 = m.group(1) + ("ñca" if m.group(2) == "ñca" else "")
        a2 = m.group(3) + ("ñca" if m.group(4) == "ñca" else "")
        return except2_neither(M.subj(a1), M.subj(a2), M.pred(m.group(5)), M.pred(m.group(6)))
    if m := re.fullmatch(r"(\S+) ṭhapetvā avasesā na (\S+), (\S+)\.", s):
        return except_not(M.subj(m.group(1)), M.pred(m.group(2)), M.pred(m.group(3)))
    if m := re.fullmatch(r"(\S+) ṭhapetvā avasesā (\S+) na (\S+), (\S+)\.", s):
        return except_rest_not(M.subj(m.group(1)), M.subj(m.group(2)), M.pred(m.group(3)), M.pred(m.group(4)))
    if m := re.fullmatch(r"(\S+) ṭhapetvā avasesā (\S+?)" + PH + r", na (\S+)\.", s):
        return except_is(M.subj(m.group(1)), M.pred(m.group(2)), M.pred(m.group(4)),
                         f" {m.group(3)}" if m.group(3) else "")
    if (m := re.fullmatch(r"(.+?) na (\S+), (\S+)\.", s)) and m.group(1).lower() in M.special:
        return special_not(M.sp(m.group(1)), M.pred(m.group(2)), M.pred(m.group(3)))
    if (m := re.fullmatch(r"(.+?) (\S+), na (\S+)\.", s)) and m.group(1).lower() in M.special:
        return special_is(M.sp(m.group(1)), M.pred(m.group(2)), M.pred(m.group(3)))
    return None


def a_question(body, M):
    """A naming question line → (Vietnamese question, remaining Pāli after the question) or None."""
    m = NAME_Q_RE.fullmatch(body)
    if not m:
        return None
    label, na1, a, na2, b, end, rest = m.groups()
    if a in ("yassa", "yattha") or b in ("yassa", "yattha"):
        return None
    if bool(na1) != bool(na2):
        raise ValueError(f"half-negated naming question {body!r}")
    end = "?"   # a "." after the question (2-01 ^6-2-36) is a plain slip: the line is plainly a question
    q = name_q_neg(label, M.pred(a), M.pred(b), end) if na1 else name_q(label, M.subj(a), M.pred(b), end)
    return q, rest


# ===============================================================================================================
# FAMILY B: verbs, person / place shells, answer heads (shared with 7-01 family C and 8 family D)
# ===============================================================================================================
# (positive Pāli forms, negative Pāli forms, positive Vietnamese, negative Vietnamese)
# Termbase (user 2026-11-22): positive unbroken forms; a fused negative keeps «không»; a separate "na" negates the
# positive term; the negative past is «chưa từng …» (nuppajjittha).
VERB_TABLE = [
    (("uppajjati", "uppajjanti"), ("nuppajjati", "nuppajjanti"), "sinh khởi", "không sinh khởi"),
    (("uppajjittha",), ("nuppajjittha",), "đã sinh khởi", "chưa từng sinh khởi"),
    (("uppajjissati", "uppajjissanti", "upapajjissati"), ("nuppajjissati", "nuppajjissanti"),
     "sẽ sinh khởi", "sẽ không sinh khởi"),
    (("nirujjhati", "nirujjhanti"), ("na nirujjhati", "na nirujjhanti"), "chấm dứt", "không chấm dứt"),
    (("nirujjhittha", "nirujjhattha"), ("na nirujjhittha",), "đã chấm dứt", "chưa từng chấm dứt"),
    (("nirujjhissati", "nirujjhissanti"), ("na nirujjhissati", "na nirujjhissanti"),
     "sẽ chấm dứt", "sẽ không chấm dứt"),
]
VERB_SLIPS = {"nirujjhattha": "nirujjhittha (2-01 ^6-2-111)", "upapajjissati": "uppajjissati (termbase outside term)"}
DENIED = C.STILL   # after "no ca" a negative verb is denied: «A vẫn V» (coordinator, = 7-01)

VERB = {}          # Pāli form -> (Vietnamese, negative?, positive Vietnamese, negative Vietnamese)
for _pos, _neg, _pv, _nv in VERB_TABLE:
    for _f in _pos:
        VERB[_f] = (_pv, False, _pv, _nv)
    for _f in _neg:
        VERB[_f] = (_nv, True, _pv, _nv)


def verb(tok):
    """Pāli verb (with or without -ti) → (vi, negative, pos_vi, neg_vi)."""
    t = tok
    cands = [t]
    for end, rep in (("ntīti", "nti"), ("īti", "i"), ("āti", "a")):
        if t.endswith(end):
            cands.append(t[:-len(end)] + rep)
    hits = [VERB[c] for c in cands if c in VERB]
    if len(hits) != 1:
        raise ValueError(f"unknown verb {tok!r}")
    return hits[0]


def is_verb(tok):
    try:
        verb(tok)
        return True
    except ValueError:
        return False


PAST, DENIED_PAST = "đã ", "đã từng "    # coordinator: a denied PAST negative = «đã từng V» (no «vẫn»)


def denied_vi(pos_vi):
    """A negative verb denied after "no ca": past «đã từng V»; present «vẫn V»; future «vẫn sẽ V»."""
    if pos_vi.startswith(PAST):
        return DENIED_PAST + pos_vi[len(PAST):]
    return f"{DENIED} {pos_vi}"


def noca_vi(b, v):
    """The part after "no ca <pron>" (7-01 shapes): positive verb → «không có B V»; negative verb → «B vẫn V»
    (past: «B đã từng V»)."""
    return f"{b} {denied_vi(v[2])}" if v[1] else f"{C.NEITHER_FIRST} {b} {v[2]}"


def short_answer(pos_vi):                # Uppajjati. «Có sinh khởi.» / Uppajjittha. «Đã sinh khởi.» …
    return f"{cap(pos_vi)}." if pos_vi.startswith(("đã ", "sẽ ")) else f"Có {pos_vi}."


SHORT = dict(C.EXACT)                    # Āmantā. «Đúng vậy.» / No. «Không.» / Natthi. «Không có.» (7-01)
for _pos, _neg, _pv, _nv in VERB_TABLE:
    for _f in _pos:
        if _f not in VERB_SLIPS:
            SHORT[cap(_f) + "."] = short_answer(_pv)

# --- question shell (coordinator) ------------------------------------------------------------------------------
WHO = {k: v[0] for k, v in C.Q_REL.items()}             # yassa «người nào» / yattha «nơi nào» / … (7-01)
THEN = {C.Q_COR[k]: v[1] for k, v in C.Q_REL.items()}    # tassa «người ấy» / tattha «nơi ấy» / tassa tattha
OTHER = C.VA_PANA                                         # vā pana «Còn»


def b_q(label, who, then, a, v1, b, v2, other=False):
    """(Ka) Yassa A V1, tassa B V2ti? / (Kha) Yassa vā pana …  = C.pair_q (the coordinator shell, 7-01 module)."""
    if C.Q_COR[who] != then:
        raise ValueError(f"relative {who!r} with correlative {then!r}")
    return C.pair_q(who, f"{a} {v1}", f"{b} {v2}", label, other)


PQ_RE = re.compile(LABEL_RE + r" (yassa|yattha)( vā pana)?( yattha)? (.+?) (tassa tattha|tassa|tattha) (.+?)\?((?: .*)?)")


def split_mv(chunk, M):
    """'rūpakkhandho na nirujjhati' → (member Vietnamese, verb tuple). Verb = last two words, else the last word."""
    w = chunk.split()
    for k in (2, 1):
        if len(w) > k and is_verb(" ".join(w[-k:])):
            return M.subj(" ".join(w[:-k])), verb(" ".join(w[-k:]))
    raise ValueError(f"no member + verb in {chunk!r}")


def split_vm(chunk, M):
    """'na nirujjhati vedanākkhandho' → (verb tuple, member Vietnamese). Verb = first two words, else the first."""
    w = chunk.split()
    for k in (2, 1):
        if len(w) > k and is_verb(" ".join(w[:k])):
            return verb(" ".join(w[:k])), M.subj(" ".join(w[k:]))
    raise ValueError(f"no verb + member in {chunk!r}")


def b_question(body, M):
    m = PQ_RE.fullmatch(body)
    if not m:
        return None
    label, w1, vapana, w2, c1, then, c2, rest = m.groups()
    who = w1 + (w2 or "")
    a, v1 = split_mv(c1, M)
    b, v2 = split_mv(c2, M)
    return b_q(label, who, then, a, v1[0], b, v2[0], other=bool(vapana)), rest


# --- answer heads: persons and planes --------------------------------------------------------------------------
# Plane stems (lower case) -> (plane «cõi X», being «chúng sinh … »). Case endings: -aṃ accusative («vào» after
# upapajjantānaṃ), -ā ablative («khỏi» after cavantānaṃ), -e locative («trong» / «Ở» heading a place answer),
# -ānaṃ genitive plural = the beings of that plane (termbase: «chúng sinh trong cõi X»; «chúng sinh Vô Tưởng»).
PLANES = {
    "asaññasatt": ("cõi Vô Tưởng", "chúng sinh Vô Tưởng"),
    "pañcavokār": ("cõi gồm năm khối", "chúng sinh trong cõi gồm năm khối"),
    "catuvokār": ("cõi gồm bốn khối", "chúng sinh trong cõi gồm bốn khối"),
    "arūp": ("cõi không hình sắc", "chúng sinh trong cõi không hình sắc"),
    "suddhāvās": ("cõi Tịnh Cư", "chúng sinh trong cõi Tịnh Cư"),
}
CASES = (("ānaṃ", "gen"), ("aṃ", "acc"), ("ā", "abl"), ("e", "loc"))
PARTICIPLES = {   # participle -> (Vietnamese, plane case it takes, preposition before the plane)
    "upapajjantānaṃ": ("đang tái sinh", "acc", "vào"),
    "cavantānaṃ": ("đang chết đi", "abl", "khỏi"),
    "parinibbantānaṃ": ("đang nhập Niết-bàn trọn vẹn", "loc", "trong"),
}
ATTRS = {"pacchimabhavikānaṃ": "thuộc kiếp sống cuối cùng"}   # genitive attributes («người thuộc kiếp sống cuối cùng»)
QUANT = {"sabbesaṃ": "tất cả", "itaresaṃ": "khác"}            # Sabbesaṃ «tất cả», Itaresaṃ «người khác»
PERSON = "những người"                   # head noun of a person group (shell «ở người nào»)
LOC_PREP = "trong"                       # locative plane after an attribute («… trong cõi X»)
YE = "Những người nào"                   # Ye … (relative clause head)
YE_VERBS = {"parinibbāyissanti": "sẽ nhập Niết-bàn trọn vẹn"}   # termbase
UPAPAJJITVA = "sau khi tái sinh"         # upapajjitvā (termbase) + «vào <plane>»
# tesaṃ / tattha / tesaṃ tattha in the answers: «ở những người ấy» / «ở nơi ấy» / «ở những người ấy, ở nơi ấy» (7-01)
L = {k: f"{C.AT} {C.pron_vi(k)}" for k in ("tesaṃ", "tattha", "tesaṃ tattha", "tassa", "tassa tattha")}
AT = cap(C.AT)                           # one «Ở» for a run of person groups; each place its own «ở» (7-01)


def plane_tok(t, planes=None):
    planes = planes or PLANES
    t0 = t.lower()
    for end, case in CASES:
        if t0.endswith(end) and t0[:-len(end)] in planes:
            return t0[:-len(end)], case
    return None


def join_and(xs):
    xs = list(xs)
    if len(xs) == 1:
        return xs[0]
    return ", ".join(xs[:-1]) + " và " + xs[-1]


def being_run(keys, quant=None, planes=None):
    """A run of genitive plane-beings: first in full, the rest as «cõi X» (termbase position variant)."""
    planes = planes or PLANES
    first = planes[keys[0]][1]
    if quant:
        if quant != "itaresaṃ" or not first.startswith("chúng sinh trong "):
            raise ValueError(f"{quant!r} before {keys!r}")
        first = first.replace("chúng sinh", f"chúng sinh {QUANT[quant]}", 1)   # Itaresaṃ X-ānaṃ «chúng sinh khác …»
    if len(keys) == 1:
        return first
    if not first.startswith("chúng sinh") or " trong " not in first:
        return join_and([first] + [planes[k][1] for k in keys[1:]])
    return join_and([first] + [planes[k][0] for k in keys[1:]])


def person_group(quant, attrs, part, plane_keys, planes=None):
    planes = planes or PLANES
    words = []
    if quant == "sabbesaṃ":
        words.append(QUANT[quant])
    words.append(PERSON)
    if quant == "itaresaṃ":
        words.append(QUANT[quant])
    words += [ATTRS[a] for a in attrs]
    if part:
        pv, case, prep = PARTICIPLES[part]
        words.append(pv)
        if plane_keys:
            words.append(f"{prep} {join_and(planes[k][0] for k in plane_keys)}")
    elif plane_keys:
        words.append(f"{LOC_PREP} {join_and(planes[k][0] for k in plane_keys)}")
    return " ".join(words)


def persons(head, planes=None):
    """Pāli genitive person phrase (before 'tesaṃ') → Vietnamese groups joined («A, B và C»), without «Ở»."""
    toks = head.split()
    groups, quant, attrs, pl, i = [], None, [], [], 0

    def flush_check():
        if quant or attrs or pl:
            raise ValueError(f"dangling words in person phrase {head!r}")

    while i < len(toks):
        t = toks[i].lower()
        nxt = toks[i + 1].lower() if i + 1 < len(toks) else None
        pt = plane_tok(t, planes)
        if t in QUANT:
            flush_check()
            quant = t
            if nxt is None:                      # Itaresaṃ alone «những người khác»
                if t != "itaresaṃ":
                    raise ValueError(f"bare {t!r} in {head!r}")
                groups.append(person_group(quant, [], None, [], planes))
                quant = None
        elif t in ATTRS:
            np_ = plane_tok(nxt, planes) if nxt else None
            if pl and all(c == "loc" for _, c in pl):       # Pañcavokāre pacchimabhavikānaṃ «… trong cõi X»
                groups.append(person_group(quant, attrs + [t], None, [k for k, _ in pl], planes))
                quant, attrs, pl = None, [], []
            elif pl:
                raise ValueError(f"plane case before attribute in {head!r}")
            elif nxt in PARTICIPLES or (np_ and np_[1] in ("acc", "abl")):
                attrs.append(t)                              # Pacchimabhavikānaṃ (pañcavokāraṃ) upapajjantānaṃ
            else:
                groups.append(person_group(quant, attrs + [t], None, [], planes))
                quant, attrs = None, []
        elif t in PARTICIPLES:
            case = PARTICIPLES[t][1]
            if any(c != case for _, c in pl):
                raise ValueError(f"plane case does not fit {t!r} in {head!r}")
            groups.append(person_group(quant, attrs, t, [k for k, _ in pl], planes))
            quant, attrs, pl = None, [], []
        elif pt and pt[1] == "gen":
            if attrs or pl:
                raise ValueError(f"plane-being after modifiers in {head!r}")
            run = [pt[0]]
            while i + 1 < len(toks) and (q := plane_tok(toks[i + 1], planes)) and q[1] == "gen":
                run.append(q[0])
                i += 1
            groups.append(being_run(run, quant, planes))
            quant = None
        elif pt:
            pl.append(pt)
        else:
            raise ValueError(f"unknown word {toks[i]!r} in person phrase {head!r}")
        i += 1
    flush_check()
    return join_and(groups)


def ye_clause(head, planes=None):
    """Ye arūpaṃ upapajjitvā parinibbāyissanti → «Những người nào sau khi tái sinh vào cõi … sẽ nhập …»."""
    toks = head.split()
    assert toks[0] == "Ye", head
    pl, out = [], [YE]
    for t in toks[1:]:
        pt = plane_tok(t, planes)
        if pt and pt[1] == "acc":
            pl.append(pt[0])
        elif t == "upapajjitvā":
            if not pl:
                raise ValueError(f"upapajjitvā without a plane in {head!r}")
            out.append(f"{UPAPAJJITVA} vào {join_and((planes or PLANES)[k][0] for k in pl)}")
            pl = []
        elif t in YE_VERBS:
            out.append(YE_VERBS[t])
        else:
            raise ValueError(f"unknown word {t!r} in {head!r}")
    if pl:
        raise ValueError(f"dangling plane in {head!r}")
    return " ".join(out)


def place_head(head, planes=None):
    """Locative planes before 'tattha' → «Ở cõi X» (several: «Ở cõi X, ở cõi Y»: each place its own «ở», 7-01)."""
    keys = []
    for t in head.split():
        pt = plane_tok(t, planes)
        if not pt or pt[1] != "loc":
            raise ValueError(f"not a locative plane {t!r} in {head!r}")
        keys.append(pt[0])
    return cap(", ".join(f"{C.AT} {(planes or PLANES)[k][0]}" for k in keys))


def answer_head(head, loc, planes=None):
    var = ""
    if m := re.fullmatch(r"(.+) (⟦\d+⟧)", head):
        head, var = m.group(1), " " + m.group(2)
    if loc == "tattha":
        return place_head(head, planes) + var
    if head.startswith("Ye "):
        return ye_clause(head, planes) + var
    return f"{AT} {persons(head, planes)}" + var


def b_noca(head_vi, loc, a, v1, b, v2):
    """H tesaṃ A V1, no ca tesaṃ B V2. → «H, thì ở những người ấy A V1, nhưng ở những người ấy không có B V2.»
    (negative V2: «…, nhưng ở những người ấy B vẫn <positive V2>»)  = 7-01 shapes."""
    return f"{head_vi}, {C.THEN} {L[loc]} {a} {v1[0]}, {C.BUT} {L[loc]} {noca_vi(b, v2)}."


def b_both(head_vi, loc, a, v1, b, v2):
    """H tesaṃ A ca V1 B ca V2. → «H, thì ở những người ấy A V1, B cũng V2.»  (7-01 both-frame)"""
    return f"{head_vi}, {C.THEN} {L[loc]} {a} {v1[0]}, {b} {C.ALSO} {v2[0]}."


LOC_RE = r"(tesaṃ tattha|tesaṃ|tattha)"


def b_sentence(s, M, planes=None):
    if m := re.fullmatch(r"(.+?) " + LOC_RE + r" (.+?), no ca \2 (.+?)\.", s):
        head, loc, c1, c2 = m.groups()
        a, v1 = split_mv(c1, M)
        b, v2 = split_mv(c2, M)
        return b_noca(answer_head(head, loc, planes), loc, a, v1, b, v2)
    if m := re.fullmatch(r"(.+?) " + LOC_RE + r" (.+?) ca (.+?) ca (.+?)\.", s):
        head, loc, c1, mid, c3 = m.groups()
        a = M.subj(c1)
        v1, b = split_vm(mid, M)
        return b_both(answer_head(head, loc, planes), loc, a, v1, b, verb(c3))
    return None


# ===============================================================================================================
# Line translator
# ===============================================================================================================
def parse_variant(br, kind):
    """'[X (syā.) evamuparipi]' → «[dị bản (Syā.): X, cũng vậy ở các chỗ sau]» (kind: 'form' | 'spelling')."""
    m = re.fullmatch(r"\[(.+?) \(([^()]+)\)( evamuparipi)?\]", br)
    if not m or kind not in ("form", "spelling"):
        raise ValueError(f"cannot place variant {br!r} ({kind!r})")
    sig = ", ".join(cap(x.strip()) + "." for x in m.group(2).split(".") if x.strip())
    tail = ", cũng vậy ở các chỗ sau" if m.group(3) else ""      # evamuparipi (pi-2)
    body = f"{m.group(1)}{tail}"
    return S.var(sig, body) if kind == "form" else S.var_sp(sig, body)


def sentence(s, M, planes=None):
    if s in SHORT:
        return SHORT[s]
    if s in CLOSING:
        return CLOSING[s]
    for f in (a_sentence, b_sentence):
        out = f(s, M) if f is a_sentence else f(s, M, planes)
        if out is not None:
            return out
    raise ValueError(f"unknown sentence {s!r}")


def sentences(rest, M, planes=None):
    parts = [x for x in re.split(r"(?<=\.) ", rest.strip()) if x]
    return " ".join(sentence(x, M, planes) for x in parts)


def tr_line(p, M, yamaka, x_pl, fixed=None, variant_kind=None, planes=None):
    """One Pāli line → Vietnamese. fixed: exact Pāli body → Vietnamese; variant_kind: bracket → 'form' | 'spelling'."""
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    fixed = fixed or {}
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text, x_pl, yamaka)}"
    elif body in fixed:
        out = fixed[body]
    else:
        brs = re.findall(r"\[[^\]]*\]", body)
        for k, br in enumerate(brs):
            body = body.replace(br, f"⟦{k}⟧", 1)
        if (q := a_question(body, M)) or (q := b_question(body, M)):
            out, rest = q
            if rest.strip():
                out += " " + sentences(rest, M, planes)
        else:
            out = sentences(body, M, planes)
        for k, br in enumerate(brs):
            if br not in (variant_kind or {}):
                raise ValueError(f"undeclared variant {br!r}")
            if f"⟦{k}⟧" not in out:
                raise ValueError(f"variant {br!r} lost in {p!r}")
            out = out.replace(f"⟦{k}⟧", parse_variant(br, variant_kind[br]))
    if "⟦" in out:
        raise ValueError(f"unplaced variant in {p!r}")
    return f"{out} {bid}" if bid else out


def build(name, M, yamaka, x_pl, fixed=None, variant_kind=None, planes=None):
    return [[tr_line(ln, M, yamaka, x_pl, fixed, variant_kind, planes) for ln in seg]
            for seg in S.segments_of(name)]


# ===============================================================================================================
# This chapter
# ===============================================================================================================
UDDESA_2_01 = "Năm khối – khối vật chất, khối cảm giác, khối tri giác, khối tạo tác, khối thức."   # (pi-2 ^2-1)
FIXED_2_01 = {"Pañcakkhandhā – rūpakkhandho, vedanākkhandho, saññākkhandho, saṅkhārakkhandho, viññāṇakkhandho.":
              UDDESA_2_01}
VARIANTS_2_01 = {
    "[avasesā saṅkhārā saṅkhārā (syā.)]": "form",
    "[avasesā khandhā khandhā (syā.) evamuparipi]": "form",
    "[pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ (sī. syā.)]": "form",
}

REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("Pañcakkhandhā – rūpakkhandho, … viññāṇakkhandho. (^2-1)", UDDESA_2_01, "2"),
    ("Natthi. (answer)", "Không có.", "3"),
    ("piyarūpaṃ sātarūpaṃ", "điều đáng yêu, là điều khoan khoái", "2"),
    ("(X (syā.) evamuparipi)", ", cũng vậy ở các chỗ sau]", "2"),
    ("cavamāne / cavantānaṃ", "đang chết đi", "2"),
    ("upapajjamāne / upapajjantānaṃ", "đang tái sinh", "2"),
    ("upapajjati (+ accusative)", "tái sinh vào", "4"),
    ("parinibbāyī", "nhập Niết-bàn trọn vẹn", "4"),
    ("Ye … (relative person)", "Những người nào", "4"),
    ("Asaññasattā (beings)", "chúng sinh Vô Tưởng", "5"),
    ("arūpabhavo / arūpadhātu", "cõi không hình sắc", "2"),
    ("pañcavokārabhavo", "gồm năm khối", "2"),
    ("catuvokārabhavo", "gồm bốn khối", "2"),
]


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


# ===============================================================================================================
# Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = KHANDHA
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Khandhayamaka 1): family A (paṇṇattivāra) and family B (pavattivāra) frames", "",
            "Builder: build_rails_2-01_vi.py (import with importlib; `Members`, `heading`, `name_q`, `name_q_neg`, "
            "`both_is`, `rest_not_is`, `special_is`, `special_not`, `except_is`, `except_not`, `except_rest_not`, "
            "`except2_neither`, `b_q`, `b_noca`, `b_both`, `persons`, `ye_clause`, `place_head`, `answer_head`, "
            "`VERB_TABLE`, `SHORT`, `WHO`, `THEN`, `L`, `PLANES`, `PARTICIPLES`, `ATTRS`, `QUANT`, `tr_line`, `build`). "
            "A later chapter passes its own `Members` (subject form, predicate form, Pāli forms) and, for new "
            "planes / persons, its own copies of PLANES / PARTICIPLES / ATTRS (planes=). Format: Pāli = tiếng Việt.",
            ""]
    h("Headings")
    row("Khandhayamakaṃ", S.yamaka_title("Khandha"))
    for p in ("Paṇṇattivāro", "(Ka) uddeso", "(Kha) niddeso", "Padasodhanavāro", "Padasodhanamūlacakkavāro",
              "(Ka) anulomaṃ", "(Kha) paccanīkaṃ", "Paṇṇattivāraniddesa", "Pavattivāro 1. uppādavāro",
              "Pavatti 2. nirodhavāro", "Pavatti 3. uppādanirodhavāro"):
        row(p, heading(p, "khối", "Khandha"))
    row("Suddha<X>vāro / Suddhakhandhavāro", f"Mục về các <X> thuần túy / {suddha_varo('khối')}")
    row("Suddha<X>mūlacakkavāro / Suddhakhandhamūlacakkavāro",
        f"Mục về vòng luân chuyển dựa trên các <X> thuần túy / {suddha_mulacakka_varo('khối')}")
    for t in TIME:
        row(f"(n) {t}vāro", f"(n) Mục về {TIME[t]}")
    for o in ORDER:
        for b in BY:
            row(f"(Ka) {o}{b}", heading(f"(Ka) {o}{b}", "khối", "Khandha"))
    for p, v in CLOSING.items():
        row(p, v)
    h("Family A: naming questions")
    row("(Ka) A B? / (Ka) A Bti?", name_q("Ka", "<A subject>", "<B predicate>"))
    row("(Ka) na A na B? / … na Bti?", name_q_neg("Ka", "<A predicate>", "<B predicate>"))
    row("(Ka) rūpaṃ rūpakkhandho?", name_q("Ka", M.subj("rūpaṃ"), M.pred("rūpakkhandho")))
    row("(Kha) khandhā vedanākkhandho?", name_q("Kha", M.subj("khandhā"), M.pred("vedanākkhandho")))
    row("(Ka) saṅkhārā khandho?", name_q("Ka", M.subj("saṅkhārā"), M.pred("khandho")))
    row("(Kha) na khandhā na saṅkhārā?", name_q_neg("Kha", M.pred("khandhā"), M.pred("saṅkhārā")))
    row("(Ka) … ti. (a question the Pāli ends with «.», 2-01 ^6-2-36)", "«?» (plainly a question; reported)")
    h("Family A: answers")
    for s in ("Piyarūpaṃ sātarūpaṃ rūpaṃ, na rūpakkhandho.", "Rūpakkhandho rūpañceva rūpakkhandho ca.",
              "Diṭṭhisaññā saññā, na saññākkhandho.", "Saññākkhandho saññā ceva saññākkhandho ca.",
              "Saṅkhārakkhandhaṃ ṭhapetvā avasesā saṅkhārā, na saṅkhārakkhandho.",
              "Vedanākkhandho khandho ceva vedanākkhandho ca.", "Avasesā khandhā na vedanākkhandho.",
              "Piyarūpaṃ sātarūpaṃ na rūpakkhandho, rūpaṃ.",
              "Rūpañca rūpakkhandhañca ṭhapetvā avasesā na ceva rūpaṃ na ca rūpakkhandho.",
              "Saṅkhārakkhandhaṃ ṭhapetvā avasesā na saṅkhārakkhandho, saṅkhārā.",
              "Saṅkhāre ca saṅkhārakkhandhañca ṭhapetvā avasesā na ceva saṅkhārā na ca saṅkhārakkhandho.",
              "Rūpaṃ ṭhapetvā avasesā khandhā na rūpaṃ, khandhā.",
              "Rūpañca khandhe ca ṭhapetvā avasesā na ceva rūpaṃ na ca khandhā."):
        row(s, sentence(s, M))
    row("na ceva A na ca B", "không phải là A, cũng không phải là B")
    row("A Bñceva C ca", "A vừa là B vừa là C")
    row("X ṭhapetvā / avasesā (alone) / Avasesā khandhā", f"{EXCEPT} X / {REST} / các khối còn lại")
    row("[X (syā.) evamuparipi]", parse_variant("[X (syā.) evamuparipi]", "form") + " (pi-2)")
    row("[X (sī. syā.)]", parse_variant("[X (sī. syā.)]", "form"))
    h("Family B: verbs (shared with 7-01 and 8)")
    for pos, neg, pv, nv in VERB_TABLE:
        row(" / ".join(pos) + " ; " + " / ".join(neg), f"{pv} ; {nv}")
    row("no ca <pron> B <negative verb> (denied)", f"«B {DENIED} <positive term>»: «B vẫn sinh khởi», «B đã từng sinh khởi» "
        "(past: «đã từng», no «vẫn»; coordinator), «B vẫn sẽ sinh khởi», «B vẫn chấm dứt», «B đã từng chấm dứt»")
    row("no ca <pron> B <positive verb>", f"«{C.NEITHER_FIRST} B <positive term>»: «không có B sinh khởi», "
        "«không có B đã sinh khởi», «không có B sẽ sinh khởi» (7-01 shape)")
    for p, v in SHORT.items():
        row(p, v)
    row("nirujjhattha (slip, ^6-2-111) / upapajjissati (slip)", "= nirujjhittha «đã chấm dứt» / = uppajjissati «sẽ sinh khởi»")
    h("Family B: question shell (coordinator) as built")
    row("(Ka) yassa A V1 tassa B V2ti?", b_q("Ka", "yassa", "tassa", "A", "V1", "B", "V2"))
    row("(Kha) yassa vā pana B V1 tassa A V2ti?", b_q("Kha", "yassa", "tassa", "B", "V1", "A", "V2", other=True))
    row("(Ka) yattha … tattha …ti?", b_q("Ka", "yattha", "tattha", "A", "V1", "B", "V2"))
    row("(Ka) yassa yattha … tassa tattha …ti?", b_q("Ka", "yassa yattha", "tassa tattha", "A", "V1", "B", "V2"))
    row("(Kha) yassa vā pana yattha … tassa tattha …ti?",
        b_q("Kha", "yassa yattha", "tassa tattha", "A", "V1", "B", "V2", other=True))
    row("(Ka) yassa rūpakkhandho nuppajjittha tassa vedanākkhandho nuppajjitthāti?",
        b_question("(Ka) yassa rūpakkhandho nuppajjittha tassa vedanākkhandho nuppajjitthāti?", M)[0])
    row("(Ka) yassa rūpakkhandho na nirujjhati tassa vedanākkhandho na nirujjhatīti?",
        b_question("(Ka) yassa rūpakkhandho na nirujjhati tassa vedanākkhandho na nirujjhatīti?", M)[0])
    row("(Ka) yassa vā pana yattha … (^6-2-61: «(Ka)» for «(Kha)», kept as written)", "(a) Còn ở người nào, ở nơi nào …")
    h("Family B: answer frames")
    row("H tesaṃ A V1, no ca tesaṃ B V2.", b_noca("<H>", "tesaṃ", "A", ("V1",), "B", ("V2-", False, "V2", "<neg V2>")))
    row("H tesaṃ A ca V1 B ca V2.", b_both("<H>", "tesaṃ", "A", ("V1",), "B", ("V2",)))
    row("tesaṃ / tattha / tesaṃ tattha (answers)", " / ".join(L.values()))
    row("<plane-locative> tattha …", f"{AT} cõi X, {C.THEN} {L['tattha']} …  (several places: «Ở cõi X, ở cõi Y, …»)")
    row("<persons> tesaṃ …", f"{AT} <groups, «A, B và C»>, {C.THEN} {L['tesaṃ']} …")
    row("<persons> tesaṃ tattha …", f"{AT} <groups>, {C.THEN} {L['tesaṃ tattha']} …")
    row("Ye <plane-acc> upapajjitvā parinibbāyissanti tesaṃ …",
        f"{ye_clause('Ye arūpaṃ upapajjitvā parinibbāyissanti')}, {C.THEN} {L['tesaṃ']} …")
    h("Alignment with 7-01 (coordinator 2026-11-22): imported from build_rails_7-01_vi, not retyped")
    out += [
        "- C.pair_q (question shell), C.Q_REL / C.Q_COR / C.VA_PANA, C.AT, C.THEN, C.BUT, C.ALSO, C.STILL, "
        "C.NEITHER_FIRST, C.pron_vi (tesaṃ «những người ấy», tattha «nơi ấy»), C.EXACT (Āmantā. / No. / Natthi.).",
        "- 2-01 answer heads always carry the Pāli resumptive (tesaṃ / tattha / tesaṃ tattha), also after a person-only "
        "head, so the head is «Ở <persons>, thì ở những người ấy …» (7-01 has «Ở <person>, …» only where the Pāli has "
        "no tesaṃ). Same strings, no new shape.",
        "- Not covered by 7-01 and set here (family B only): planes inside a person group take a preposition, not "
        "«ở» («đang tái sinh vào cõi X», «đang chết đi khỏi cõi X», «… trong cõi X»), since they describe the person, "
        "not a place of the head; the Ye-clause head «Những người nào …, thì ở những người ấy …»; the one-word verb "
        "answers «Có sinh khởi.» / «Đã sinh khởi.» / «Sẽ sinh khởi.» / «Có chấm dứt.» / «Đã chấm dứt.».",
        "- Lists after no ca (neither / «A và B vẫn V») do not occur in 2-01; split_mv raises on them, so a later "
        "chapter must add the 7-01 list shapes explicitly (C.neg_clause_vi / C.tp_vi).",
    ]
    h("Family B: person / place answer heads (shared with 7-01 and 8)")
    for k, (pv, bv) in PLANES.items():
        row(f"{k}aṃ / {k}ā / {k}e / {k}ānaṃ", f"{pv} (vào / khỏi / trong / Ở …) / {bv}")
    for k, (pv, case, prep) in PARTICIPLES.items():
        row(f"<plane-{case}> {k}", f"{PERSON} {pv} {prep} cõi X")
    for k, v in ATTRS.items():
        row(k, f"{PERSON} {v}")
    row("Sabbesaṃ <participle> / Itaresaṃ / Itaresaṃ <participle> / Itaresaṃ <plane-ānaṃ>",
        f"tất cả {PERSON} … / {PERSON} khác / {PERSON} khác đang … / chúng sinh khác trong cõi X")
    row("<plane-ānaṃ> <plane-ānaṃ> (run)", "chúng sinh trong cõi X và cõi Y (termbase position variant)")
    for hd in ("Asaññasattaṃ upapajjantānaṃ", "Sabbesaṃ cavantānaṃ arūpaṃ upapajjantānaṃ",
               "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ asaññasattaṃ upapajjantānaṃ",
               "Itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ", "Pañcavokārā cavantānaṃ arūpānaṃ",
               "Suddhāvāse parinibbantānaṃ asaññasattā cavantānaṃ",
               "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ asaññasattā cavantānaṃ",
               "Pañcavokāre pacchimabhavikānaṃ asaññasattānaṃ", "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ",
               "Suddhāvāsānaṃ asaññasattānaṃ", "Parinibbantānaṃ"):
        row(hd, persons(hd))
    h("Termbase gaps and choices (for the coordinator)")
    out += [
        "- Piyarūpaṃ sātarūpaṃ: no termbase entry; pi-2 «điều đáng yêu, là điều khoan khoái» in the approved "
        "«hiểu theo nghĩa …» frame: «vật chất hiểu theo nghĩa điều đáng yêu, điều khoan khoái».",
        "- Catuvokāraṃ / Catuvokārā / catuvokārānaṃ: only Catuvokāre «cõi gồm bốn khối» is in the termbase; "
        "built by analogy with pañcavokāra.",
        "- Suddhāvāsā, Arūpā (ablative): plane forms as the termbase's other cases.",
        "- na nirujjhittha «chưa từng chấm dứt» (separate na on the positive past; = nuppajjittha «chưa từng sinh khởi»; "
        "the termbase lists «chưa từng chấm dứt» as the negative candidate of nirujjhittha).",
        "- Yassa yattha (termbase «người nào ở nơi nào») follows the coordinator shell «ở người nào, ở nơi nào».",
        "- cavantānaṃ + ablative plane «đang chết đi khỏi cõi X» (pi-4 avihā cuto «chết ở cõi …» is not identical Pāli).",
        "",
        "## Slips (translated as written or as plainly meant)",
        "",
        "- ^6-2-36 «(Ka) na saṅkhārā na saṅkhārakkhandhoti.»: question ending «.», rendered with «?».",
        "- ^6-2-61 second question labelled «(Ka)» (for «(Kha)»): label kept «(a)».",
        "- ^6-2-111 «nirujjhattha» for nirujjhittha: rendered «đã chấm dứt».",
        "- ^6-2-44 «Āmantā.» stands on its own line (kept as its own line).",
        "",
    ]
    return "\n".join(out)


def check_shared():
    """The verbs 7-01 lists for family B must be the ones built here."""
    for k in ("uppajjati", "uppajjittha", "uppajjissati"):
        assert C.FAMILY_TERMS[k] == VERB[k][0], (k, C.FAMILY_TERMS[k], VERB[k][0])
    assert join_and(["A", "B"]) == f"A {C.AND} B"


def main():
    S.check_reused()
    check_reused()
    check_shared()
    segs = build(CH, KHANDHA, "Khandha", "khối", FIXED_2_01, VARIANTS_2_01)
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)


if __name__ == "__main__":
    main()
