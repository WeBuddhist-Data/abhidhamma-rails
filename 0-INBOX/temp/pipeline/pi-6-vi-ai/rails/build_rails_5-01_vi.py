"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 5-01 (Saccayamaka, part 1: paṇṇattivāra + pavattivāra uppādavāra).

Families A (paṇṇattivāra) and B (pavattivāra) come from build_rails_2-01_vi (setter), the shared answer shapes from
build_rails_7-01_vi, the moment words from build_rails_8_vi, the cut lines and "ye" heads from build_rails_2-02_vi;
all imported READ-ONLY. This file plugs in the four truths (termbase / pi-2 names) and adds the answer heads the
Saccayamaka needs (moments «vào khoảnh khắc …», «khi tâm … đang diễn ra», pavatte «trong đời sống», «tâm mà ngay
sau đó họ sẽ đạt được …», ye ca / ye caññe groups, places inside person heads).

5-02 and 5-03 import this file READ-ONLY:

    import importlib, sys
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    T = importlib.import_module("build_rails_5-01_vi")
    T.SACCA_A / T.SACCA_B (members), T.TRUTH, T.KC_VI, T.head_vi(), T.b_sentence(), T.b_question(), T.tr_line() …

Every parser raises ValueError on a word or shape it cannot place (no silent fallback). Importing writes nothing;
outputs are written only under `if __name__ == "__main__":`.

usage: python -I -X utf8 -B build_rails_5-01_vi.py
"""
import copy
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY: labels, checks)
B = importlib.import_module("build_rails_2-01_vi")   # READ-ONLY: families A, B (setter 2-01)
C = importlib.import_module("build_rails_7-01_vi")   # READ-ONLY: shared answer shapes, writer (setter 7-01)
D = importlib.import_module("build_rails_8_vi")      # READ-ONLY: moments, persons of family D (setter 8)
E = importlib.import_module("build_rails_2-02_vi")   # READ-ONLY: family E, cut lines, ye heads (setter 2-02)
T9 = importlib.import_module("build_rails_9-01_vi")  # READ-ONLY: the shared head parts (coordinator, from 9-01)

cap = S.cap
LABEL = S.LABEL
PE = S.PE
CH = "5-01-saccayamaka.md"
N = "5-01"
YAMAKA = "Sacca"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
TERMBASE = S.ROOT / "AI_translation/vietnamese/pi-6-pali-vietnamese-termbase-plain.md"

SLIPS_SEEN = []   # (what, where) collected while building; printed by main() and listed in the notes


def _lc(w):
    return w[:1].lower() + w[1:]


def _decap(s):
    return s[:1].lower() + s[1:]


# ===============================================================================================================
# 1. Members: the four truths (termbase; pi-2 «sự thật về khổ đau», «sự thật về sự phát sinh» …)
# ===============================================================================================================
TRUTH = {   # key → Vietnamese (subject = predicate form)
    "dukkha": "khổ đau",                      # dukkhaṃ, bare: the truth's member (user 2026-11-22: «khổ đau»)
    "samudaya": "sự phát sinh",               # samudayo (termbase)
    "nirodha": "sự chấm dứt",                 # nirodho (termbase)
    "magga": "con đường",                     # maggo (termbase)
    "dukkhasacca": "sự thật về khổ đau",      # dukkhasaccaṃ (termbase; pi-2)
    "samudayasacca": "sự thật về sự phát sinh",   # samudayasaccaṃ (termbase; pi-2)
    "nirodhasacca": "sự thật về sự chấm dứt",     # nirodhasaccaṃ (termbase)
    "maggasacca": "sự thật về con đường",         # maggasaccaṃ (termbase)
    "sacca": "sự thật",                       # saccaṃ (termbase)
}
SACCA_PL = "các sự thật"                      # saccā as a subject («các»); predicate «sự thật»
CATTARI_SACCANI = "Bốn sự thật"               # Cattāri saccāni (pi-2 4-saccavibhango)
KAYIKA = "sự khó chịu nơi thân"              # Kāyikaṃ dukkhaṃ (termbase; pi-1; user decision)
CETASIKA = "sự khó chịu trong tâm"           # cetasikaṃ dukkhaṃ (termbase; pi-1; user decision)
KC_PALI = "Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ"
KC_TOKEN = "kc⁰"                              # the two-word pair as one member token (internal)
KC_VI = f"{KAYIKA} {C.AND} {CETASIKA}"        # juxtaposed pair, joined «và» (as 2-01 joins juxtaposed runs)


def _t(key, forms, subj=None):
    v = TRUTH[key]
    return (subj or v, v, forms)


# Paṇṇattivāra members (all case forms the naming questions and answers use)
SACCA_A = B.Members({
    "dukkha": _t("dukkha", ["dukkhaṃ"]),
    "samudaya": _t("samudaya", ["samudayo", "samudayaṃ"]),
    "nirodha": _t("nirodha", ["nirodho", "nirodhaṃ"]),
    "magga": _t("magga", ["maggo", "maggaṃ"]),
    "dukkhasacca": _t("dukkhasacca", ["dukkhasaccaṃ"]),
    "samudayasacca": _t("samudayasacca", ["samudayasaccaṃ"]),
    "nirodhasacca": _t("nirodhasacca", ["nirodhasaccaṃ"]),
    "maggasacca": _t("maggasacca", ["maggasaccaṃ"]),
    "sacca": _t("sacca", ["saccaṃ"]),
    "saccā": _t("sacca", ["saccā"], subj=SACCA_PL),
    "kc": (KC_VI, KC_VI, [KC_TOKEN]),
})
# Pavattivāra members: only the four truths (so that maggaṃ / maggassa in the answer heads are never members)
SACCA_B = B.Members({k: _t(k, [f"{k}ṃ"]) for k in ("dukkhasacca", "samudayasacca", "nirodhasacca", "maggasacca")})
X_PL = "sự thật"                              # Suddha<X>vāro «Mục về các sự thật thuần túy» (termbase)

UDDESA_PALI = "Cattāri saccāni – dukkhasaccaṃ, samudayasaccaṃ nirodhasaccaṃ, maggasaccaṃ."
UDDESA_VI = f"{CATTARI_SACCANI} – " + ", ".join(TRUTH[k] for k in ("dukkhasacca", "samudayasacca", "nirodhasacca",
                                                                    "maggasacca")) + "."
# (the Pāli lacks the comma after samudayasaccaṃ: missing punctuation, rendered as meant)

# ===============================================================================================================
# 2. Headings and fixed lines
# ===============================================================================================================
PANNATTIVARA = cap("mục về sự định danh")    # Paṇṇattivāra (heading; termbase) = Paṇṇattivāro (S.LATER_HEADINGS)
assert PANNATTIVARA == B.PANNATTIVARO
UPPADAVARO_CLOSE = cap(B.UPPADAVARO) + "."   # Uppādavāro. «Mục về sự sinh khởi.» (= 2-02 «Nirodhavāro.»)
HEADINGS = {"Paṇṇattivāra": PANNATTIVARA}


def heading(text):
    if text in HEADINGS:
        return HEADINGS[text]
    return B.heading(text, X_PL, YAMAKA)


# editorial notes (termbase: Yassakampi «phần về người», yassayatthakampi «phần về người và nơi chốn», yatthakampi /
# yatthakā «phần về nơi chốn», yatthakasadisaṃ «giống như phần về nơi chốn», yassayatthakasadisaṃ «giống như phần
# về người và nơi chốn»; pi-5 vitthāretabbaṃ «nên được trình bày chi tiết», nānākaraṇaṃ «sự khác biệt»; 2-02
# kātabbaṃ «nên được trình bày»; coordinator: sabbattha in an editorial note «ở mọi chỗ»)
P_PERSON = "phần về người"
P_PLACE = "phần về nơi chốn"
P_PERSON_PLACE = "phần về người và nơi chốn"
VITTHARETABBAM = "nên được trình bày chi tiết"
NOTE_YASSAKA = f"(Cả {P_PERSON} lẫn {P_PERSON_PLACE} đều {VITTHARETABBAM} giống nhau)."
SABBATTHA_SADISAM = "ở mọi chỗ cũng đều giống nhau"         # sabbattha sadisaṃ (3-01 «ở mọi chỗ đều giống nhau»)
SADISAM_KATABBAM = "nên được làm cho giống như"               # X-sadisaṃ kātabbaṃ (4 sadisaṃ kātabbaṃ «nên được làm cho giống nhau»)
NOTE_YATTHAKA_SABBATTHA = (f"({cap(P_PLACE)} {SABBATTHA_SADISAM}. Sự khác biệt trong lời văn thì "
                           f"giống như {P_PLACE} ở trên).")
NOTE_YATTHAKA_SABBE = f"(tất cả các {P_PLACE} đều giống nhau)"
NOTE_YATTHAKA_AS_YY = f"({P_PLACE} cũng {SADISAM_KATABBAM} {P_PERSON_PLACE})"
NOTES_PALI = {
    "(yatthakā sadisā sabbe)": NOTE_YATTHAKA_SABBE,
    "(yatthakampi yassayatthakasadisaṃ kātabbaṃ)": NOTE_YATTHAKA_AS_YY,
}

FIXED = {
    UDDESA_PALI: UDDESA_VI,
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ).": NOTE_YASSAKA,
    "(Yatthakampi sabbattha sadisaṃ. Tantinānākaraṇaṃ heṭṭhā yatthakasadisaṃ).": NOTE_YATTHAKA_SABBATTHA,
}
CLOSING = {**B.CLOSING, "Uppādavāro.": UPPADAVARO_CLOSE}

# ===============================================================================================================
# 3. Variant brackets
# ===============================================================================================================
EVAM = "cũng vậy"                              # evaṃ … (2-01 evamuparipi «, cũng vậy ở các chỗ sau»)


def _sig(s):
    return ", ".join(cap(x.strip()) + "." for x in s.split(".") if x.strip())


VARIANTS = {   # bracket → Vietnamese (the variant's Pāli kept, the label and the note translated)
    "[avasesaṃ dukkhasaccaṃ dukkhasaccaṃ (syā.) evamuparipi]":
        B.parse_variant("[avasesaṃ dukkhasaccaṃ dukkhasaccaṃ (syā.) evamuparipi]", "form"),
    "[avasesaṃ dukkhasaccaṃ na dukkhaṃ (sī. syā. ka.) evaṃ avasesesu tīsu saccesu]":
        S.var(_sig("sī. syā. ka."), f"avasesaṃ dukkhasaccaṃ na dukkhaṃ, {EVAM} ở ba sự thật còn lại"),
    "[avasesā saccā saccā (syā.)]": B.parse_variant("[avasesā saccā saccā (syā.)]", "form"),
    "[taṇhāvippayuttamaggavippayuttacittassa (sī.) evaṃ puggalokāsepi nirodhavārepi]":
        S.var(_sig("sī."), f"taṇhāvippayuttamaggavippayuttacittassa, {EVAM} ở {P_PERSON_PLACE} và ở "
                           f"{B.NIRODHAVARO}"),
    "[uppatticittassa (syā.)]": B.parse_variant("[uppatticittassa (syā.)]", "form"),
    "[paṭilabhissanti tassa cittassa uppādakkhaṇe ye (sī. syā.) puggalokāsavārepi]":
        S.var(_sig("sī. syā."), f"paṭilabhissanti tassa cittassa uppādakkhaṇe ye, {EVAM} ở mục về người và nơi chốn"),
}
VAR_RE = re.compile(r"\[[^\]]*\]")

# ===============================================================================================================
# 4. FAMILY A in the Saccayamaka: naming questions and answers (2-01 slot functions; wider regexes for the
#    avaseso / avasesaṃ forms, the -ñca both-frame and the kāyika / cetasika pair)
# ===============================================================================================================
AVA = r"avases(?:ā|o|aṃ)"
PH = r"( ⟦\d+⟧)?"


def kc_in(s):
    """Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ → one member token (the pair is the subject of the answer)."""
    return s.replace(KC_PALI, KC_TOKEN)


def a_sentence(s, M=SACCA_A):
    """One family-A answer sentence (ends with «.»), or None."""
    s = kc_in(s)
    if m := re.fullmatch(r"(\S+) (\S+?)(ñceva| ceva) (\S+?)(ñca| ca)\.", s):
        b = m.group(2) + ("ñceva" if m.group(3) == "ñceva" else "")
        c = m.group(4) + ("ñca" if m.group(5) == "ñca" else "")
        return B.both_is(M.subj(m.group(1)), M.pred(b), M.pred(c))
    if m := re.fullmatch(r"Avasesā (\S+)" + PH + r" na (\S+)\.", s):
        return B.rest_not_is(M.subj(m.group(1)), M.pred(m.group(3)), m.group(2) or "")
    if m := re.fullmatch(r"(\S+?)(ñca| ca) (\S+?)(ñca| ca) ṭhapetvā " + AVA + r" na ceva (\S+) na ca (\S+)\.", s):
        a1 = m.group(1) + ("ñca" if m.group(2) == "ñca" else "")
        a2 = m.group(3) + ("ñca" if m.group(4) == "ñca" else "")
        return B.except2_neither(M.subj(a1), M.subj(a2), M.pred(m.group(5)), M.pred(m.group(6)))
    if m := re.fullmatch(r"(\S+) ṭhapetvā avasesā (\S+) na (\S+), (\S+)\.", s):
        return B.except_rest_not(M.subj(m.group(1)), M.subj(m.group(2)), M.pred(m.group(3)), M.pred(m.group(4)))
    if m := re.fullmatch(r"(\S+) ṭhapetvā " + AVA + r" na ([^\s,]+)" + PH + r"(,?) (\S+)\.", s):
        if not m.group(4):
            SLIPS_SEEN.append(("comma before the last word missing (after a variant bracket): «, mà là»", s[:60]))
        return B.except_not(M.subj(m.group(1)), M.pred(m.group(2)) + (m.group(3) or ""), M.pred(m.group(5)))
    if m := re.fullmatch(r"(\S+) ṭhapetvā " + AVA + r" (\S+?)" + PH + r", na (\S+)\.", s):
        return B.except_is(M.subj(m.group(1)), M.pred(m.group(2)), M.pred(m.group(4)), m.group(3) or "")
    return None


A_Q_RE = re.compile(r"(?:\((Ka|Kha)\) )?([Nn]a )?(\S+) (na )?(\S+)\?")


def a_question(q, M=SACCA_A):
    """A naming question piece (ends with «?»), labelled or not, or None. Unlabelled pieces keep the Pāli's case."""
    m = A_Q_RE.fullmatch(q.strip())
    if not m:
        return None
    label, na1, a, na2, b = m.groups()
    if _lc(a) in ("yassa", "yattha") or (na1 is None) != (na2 is None):
        return None
    lab = label or "Ka"
    out = B.name_q_neg(lab, M.pred(a), M.pred(b)) if na1 else B.name_q(lab, M.subj(a), M.pred(b))
    if label:
        return out
    out = out[len(LABEL["Ka"]) + 1:]                  # same string without the label
    first = (na1 or a)[0]
    return out if first.isupper() else _decap(out)


def a_partial(p, M=SACCA_A):
    """A piece cut by …pe… before its end: 'Āmantā' / 'X ṭhapetvā'."""
    if p == "Āmantā":
        return S.YES[:-1]                              # «Đúng vậy» + the cut
    if m := re.fullmatch(r"(\S+) ṭhapetvā", p):
        vi = f"{B.EXCEPT} {M.subj(m.group(1))}"
        return vi if p[0].isupper() else _decap(vi)
    return None


# ===============================================================================================================
# 5. FAMILY B in the Saccayamaka: answer heads (persons, places, moments) and the answer frames
# ===============================================================================================================
PLANES = dict(B.PLANES)
PLANES["apāy"] = ("cõi khổ", "chúng sinh trong cõi khổ")          # Apāye «cõi khổ», āpāyikānaṃ (termbase)
PLANES["asaññatt"] = B.PLANES["asaññasatt"]                       # asaññattā: slip for asaññasattā (termbase)
PLANE_SLIPS = {"asaññatt": "asaññasatt"}
AVASESE = "còn lại"                                               # Avasese (termbase «còn lại»)

PEOPLE = B.PERSON                                                 # «những người» (2-01)
ALL_PEOPLE = T9.ALL_BEINGS                                        # Sabbesaṃ (bare) «tất cả chúng sinh» (9-01)
PERSON_GEN = {   # genitive plural (lower case) → Vietnamese group
    "nirodhasamāpannānaṃ": D.PERSON["nirodhasamāpannānaṃ"],      # «những người nhập thành tựu thiền chấm dứt» (8)
    "pacchimacittasamaṅgīnaṃ": D.PERSON["pacchimacittasamaṅgīnaṃ"],   # «những người có được tâm cuối cùng» (8)
    "aggamaggasamaṅgīnaṃ": f"{PEOPLE} có được con đường tối thượng",   # termbase
    "arahantānaṃ": "các bậc A-la-hán",                            # termbase «bậc A-la-hán» (plural «các»)
    "āpāyikānaṃ": PLANES["apāy"][1],                              # «chúng sinh trong cõi khổ» (termbase)
}
ATTR = {   # genitive attributes: alone «những người <attr>», before a participle «những người <attr> đang …»
    "anabhisametāvīnaṃ": "chưa thấu hiểu",                       # termbase «người chưa thấu hiểu»
    "abhisametāvīnaṃ": "đã thấu hiểu",                           # termbase «người đã thấu hiểu»
}
MAGGAM = "con đường"
AGGAMAGGAM = "con đường tối thượng"                               # aggamaggaṃ (termbase)
WILL_ATTAIN = "sẽ đạt được"                                       # paṭilabhissanti (termbase)
WILL_NOT_ATTAIN = "sẽ không đạt được"                             # na paṭilabhissanti (2-02)
REL = E.REL                                                       # «nào» (2-02 ye ca <NP> «<NP> nào …»)
OTHERS = "những người khác"                                       # caññe (termbase «khác») = D.PERSON['itaresaṃ']
ANANTARA_PERSON = T9.PERSON_ATTAIN          # yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (person group; 9-01)
ANANTARA_MIND = f"{D.MIND} mà {T9.ANANTARA} đó {T9.ATTAIN_TOP}"   # … tassa cittassa <moment> (= 9-01 that_mind_moment)
assert T9.that_mind_moment("uppādakkhaṇe") == f"{D.AT_TIME} {D.MOMENT['uppādakkhaṇe']} {D.OF} {ANANTARA_MIND}"
YE_GROUPS = {   # (Pāli words, Vietnamese group, conj?)  ye / ye ca / ye caññe … (2-02 wording)
    "ye ca puthujjanā maggaṃ na paṭilabhissanti": (f"{E.PUTHUJJANA_PL} {REL} {E.MAGGAM_NA_PATILABHISSANTI}", True),
    "ye caññe maggaṃ paṭilabhissanti": (f"{OTHERS} {REL} {E.MAGGAM_PATILABHISSANTI}", True),
    "yassa cittassa anantarā aggamaggaṃ paṭilabhissanti": (ANANTARA_PERSON, False),
    "yassa cittassa anantarā aggamaggaṃ paṭilabhissānti": (ANANTARA_PERSON, False),   # termbase variant spelling
}
YE_HEADS = {   # a "Ye …" clause opening the head: «Những … nào …» (2-01 / 2-02 «Những người nào …»)
    "ye puthujjanā maggaṃ na paṭilabhissanti": f"Những người phàm phu {REL} {E.MAGGAM_NA_PATILABHISSANTI}",
    "ye maggaṃ paṭilabhissanti": f"{B.YE} {E.MAGGAM_PATILABHISSANTI}",
}
INNER_TESAM = {   # tesaṃ inside a head
    "tesaṃ upapajjantānaṃ": f"khi {E.TE} {B.PARTICIPLES['upapajjantānaṃ'][0]}",   # «khi những người ấy đang tái sinh»
    "tesaṃ cavantānaṃ": E.KHI_CAVANTA,                                             # «khi những người ấy đang chết đi» (2-02)
    "tesaṃ": f"{C.AT} {E.TE}",                                                     # «ở những người ấy»
}

# --- moments («vào khoảnh khắc … của …», 8 / pi-5) and «khi tâm … đang diễn ra» (pi-5) ---------------------------
MIND = D.MIND                                                     # «tâm»
MIND_KIND = {   # <stem>cittassa / <stem>citte → «tâm …» (termbase; coordinator: two-part kinds «tâm A và B»)
    "": MIND,
    "taṇhāvippayutta": f"{MIND} không gắn liền với khao khát",
    "maggavippayutta": f"{MIND} không gắn liền với con đường",
    "taṇhāvippayuttamaggavippayutta": f"{MIND} không gắn liền với khao khát và không gắn liền với con đường",
    "maggavippayuttataṇhāvippayutta": f"{MIND} không gắn liền với con đường và không gắn liền với khao khát",
    "upapatti": f"{MIND} tái sinh",                               # upapatticittassa (termbase «tâm tái sinh»)
}
OWNER = {   # genitive before a moment (not a mind)
    "taṇhāya": "khao khát",                                       # Taṇhāya uppādakkhaṇe (termbase)
    "maggassa": MAGGAM,                                           # maggassa (termbase «con đường»)
    "phalassa": "thành quả",                                      # phalassa (termbase «thành quả»)
    "aggamaggassa": AGGAMAGGAM,                                   # Aggamaggassa (termbase)
}
VATTAMANE = (T9.WHILE, T9.OCCURRING)                              # <mind> citte vattamāne (termbase; pi-5; 9-01)
DUTIYE = T9.ORDINAL["dutiye"]                                     # dutiye «thứ hai» (9-01)
CITTE_KIND = {"": MIND, "akusale": f"{MIND} bất thiện", "taṇhāvippayutta": MIND_KIND["taṇhāvippayutta"]}
PAVATTE = T9.PAVATTE                                              # pavatte «trong đời sống» (user; 9-01: its own item)


def moment(moment_word, owner_vi):
    """'uppādakkhaṇe', «tâm» → «vào khoảnh khắc sinh khởi của tâm» (= 8 moment_phrase)."""
    return f"{D.AT_TIME} {D.MOMENT[moment_word]} {D.OF} {owner_vi}"


assert moment("uppādakkhaṇe", MIND) == D.moment_phrase("uppādakkhaṇe", "Cittassa")
assert moment("bhaṅgakkhaṇe", MIND) == D.moment_phrase("bhaṅgakkhaṇe", "Cittassa")

MOMENT_W = r"(uppādakkhaṇe|bhaṅgakkhaṇe)"
T_PATTERNS = [   # (regex over the lower-cased words, function → Vietnamese time item)
    (re.compile(r"yassa cittassa anantarā aggamaggaṃ paṭilabhiss(?:a|ā)nti tassa cittassa " + MOMENT_W),
     lambda m: moment(m.group(1), ANANTARA_MIND)),
    (re.compile(r"(\w*?)cittassa " + MOMENT_W),
     lambda m: moment(m.group(2), MIND_KIND[m.group(1)])),
    (re.compile(r"(maggassa|aggamaggassa) ca phalassa ca " + MOMENT_W),
     lambda m: moment(m.group(2), f"{OWNER[m.group(1)]} {C.AND} {OWNER['phalassa']}")),
    (re.compile(r"(taṇhāya|maggassa|phalassa|aggamaggassa) " + MOMENT_W),
     lambda m: moment(m.group(2), OWNER[m.group(1)])),
    (re.compile(r"(?:(dutiye) )?(?:(akusale) )?(\w*?)citte vattamāne"),
     lambda m: f"{VATTAMANE[0]} {CITTE_KIND[m.group(2) or m.group(3)]}"
               f"{' ' + DUTIYE if m.group(1) else ''} {VATTAMANE[1]}"),
]


def _match_at(words, i, pat):
    """Longest fullmatch of pat over words[i:j] → (match, j) or None."""
    for j in range(len(words), i, -1):
        if m := pat.fullmatch(" ".join(words[i:j])):
            return m, j
    return None


def person_group(quant, attr, part, plane_keys):
    """[Sabbesaṃ | Itaresaṃ] [attr] [<planes acc / abl>] <participle> → Vietnamese (2-01 word order)."""
    words = []
    if quant == "sabbesaṃ":
        words.append(B.QUANT[quant])
    words.append(PEOPLE)
    if quant == "itaresaṃ":
        words.append(B.QUANT[quant])
    if attr:
        words.append(ATTR[attr])
    if part:
        pv, case, prep = B.PARTICIPLES[part]
        words.append(pv)
        if plane_keys:
            words.append(f"{prep} {B.join_and(PLANES[k][0] for k in plane_keys)}")
    elif plane_keys:
        raise ValueError(f"planes without a participle: {plane_keys!r}")
    return " ".join(words)


def head_items(words):
    """Pāli head words (before the resumptive) → list of (kind, Vietnamese, conj): kind 'P' person group,
    'Y' a 'Ye' clause, 'T' time phrase, 'L' place, 'R' an inner tesaṃ. Raises on any word it cannot place."""
    return _head_items(words)[0]


def _head_items(words):
    """head_items + the start index of each item in `words` (one item per step)."""
    lw = [_lc(w) for w in words]
    items, starts, i = [], [], 0
    for k, v in YE_HEADS.items():                                 # Ye … opening the head
        n = len(k.split())
        if " ".join(lw[:n]) == k:
            starts.append(0)
            items.append(("Y", v, False))
            i = n
            break
    while i < len(lw):
        if len(starts) != len(items):
            raise AssertionError("one item per step")
        starts.append(i)
        t = lw[i]
        hit = None
        for pat, fn in T_PATTERNS:                                # time phrases (longest match)
            if r := _match_at(lw, i, pat):
                if hit is None or r[1] > hit[1]:
                    hit = (fn(r[0]), r[1])
        if hit:
            items.append(("T", hit[0], False))
            i = hit[1]
            continue
        for k, (v, conj) in YE_GROUPS.items():                    # ye ca / ye caññe / yassa cittassa anantarā …
            n = len(k.split())
            if " ".join(lw[i:i + n]) == k:
                if "paṭilabhissānti" in k:
                    SLIPS_SEEN.append(("paṭilabhissānti (spelling slip; termbase variant)", " ".join(words)[:70]))
                items.append(("P", v, conj))
                i += n
                break
        else:
            n = 0
        if n:
            continue
        if t == "pavatte":
            if i + 1 >= len(lw):
                raise ValueError(f"pavatte at the end of {words!r}")
            items.append(("V", PAVATTE, False))                   # its own item, before a time phrase (9-01)
            i += 1
            continue
        if t == "tesaṃ" and i + 1 < len(lw) and " ".join(lw[i:i + 2]) in INNER_TESAM:
            items.append(("R", INNER_TESAM[" ".join(lw[i:i + 2])], False))
            i += 2
            continue
        if t == "tesaṃ":
            items.append(("R", INNER_TESAM["tesaṃ"], False))
            i += 1
            continue
        if t == "avasese":                                        # Avasese <loc planes> (place heads)
            keys, j = [], i + 1
            while j < len(lw) and (pt := B.plane_tok(lw[j], PLANES)) and pt[1] == "loc":
                keys.append(pt[0])
                j += 1
            if not keys:
                raise ValueError(f"Avasese without a plane in {words!r}")
            items.append(("L", f"{C.AT} {B.join_and(PLANES[k][0] for k in keys)} {AVASESE}", False))
            i = j
            continue
        if t in PERSON_GEN:
            items.append(("P", PERSON_GEN[t], False))
            i += 1
            continue
        quant = attr = None
        j = i
        if lw[j] in B.QUANT:
            quant = lw[j]
            j += 1
        if j < len(lw) and lw[j] in ATTR:
            attr = lw[j]
            j += 1
        planes = []
        while j < len(lw) and (pt := B.plane_tok(lw[j], PLANES)) and pt[1] in ("acc", "abl"):
            planes.append(pt)
            j += 1
        if j < len(lw) and lw[j] in B.PARTICIPLES:
            part = lw[j]
            case = B.PARTICIPLES[part][1]
            if any(c != case for _, c in planes):
                raise ValueError(f"plane case does not fit {part!r} in {words!r}")
            for k, _ in planes:
                if k in PLANE_SLIPS:
                    SLIPS_SEEN.append((f"{k}ā (slip for {PLANE_SLIPS[k]}ā)", " ".join(words)[:70]))
            items.append(("P", person_group(quant, attr, part, [k for k, _ in planes]), False))
            i = j + 1
            continue
        if planes:
            raise ValueError(f"plane {planes!r} without a participle in {words!r}")
        if quant == "itaresaṃ" and j < len(lw) and (pt := B.plane_tok(lw[j], PLANES)) and pt[1] == "gen":
            run = []
            while j < len(lw) and (pt := B.plane_tok(lw[j], PLANES)) and pt[1] == "gen":
                run.append(pt[0])
                j += 1
            items.append(("P", B.being_run(run, quant, PLANES), False))
            i = j
            continue
        if attr:                                                  # Anabhisametāvīnaṃ (alone)
            if quant:
                raise ValueError(f"{quant!r} before {attr!r} in {words!r}")
            items.append(("P", f"{PEOPLE} {ATTR[attr]}", False))
            i = j
            continue
        if quant == "itaresaṃ":
            items.append(("P", D.PERSON["itaresaṃ"], False))      # «những người khác»
            i = j
            continue
        if quant == "sabbesaṃ":
            items.append(("P", ALL_PEOPLE, False))
            i = j
            continue
        if (pt := B.plane_tok(t, PLANES)) and pt[1] == "gen":     # beings of a plane (a run)
            run = []
            while i < len(lw) and (pt := B.plane_tok(lw[i], PLANES)) and pt[1] == "gen":
                run.append(pt[0])
                i += 1
            items.append(("P", B.being_run(run, None, PLANES), False))
            continue
        if (pt := B.plane_tok(t, PLANES)) and pt[1] == "loc":     # a place (each its own «ở»)
            items.append(("L", f"{C.AT} {PLANES[pt[0]][0]}", False))
            i += 1
            continue
        raise ValueError(f"unknown word {words[i]!r} in answer head {' '.join(words)!r}")
    if len(starts) != len(items):
        raise AssertionError("one item per step")
    return items, starts


def head_vi(words):
    """Head words → «Ở <persons>, vào khoảnh khắc …, ở cõi X, …» (without the resumptive). One «ở» for a run of
    person groups (joined «A, B và C»); a group after a time phrase or place keeps its own «ở»; a 'ye ca' run after
    a time phrase opens with «và»; pavatte «trong đời sống» is its own item (9-01). A protected variant
    bracket ⟦k⟧ inside the head goes after the Vietnamese item whose Pāli it follows."""
    marks, plain = [], []
    for w in words:
        if re.fullmatch(r"⟦\d+⟧", w):
            if not plain:
                raise ValueError(f"variant opening a head: {words!r}")
            marks.append((len(plain) - 1, w))
        else:
            plain.append(w)
    items, starts = _head_items(plain)
    items = [list(x) for x in items]
    for pos, mk in marks:
        k = max(n for n, s in enumerate(starts) if s <= pos)
        if starts[k] == pos and plain[pos].lower() == "ye" and k:
            k -= 1          # '… paṭilabhissanti ye [variant] caññe …': the variant ends the previous group
        items[k][1] += f" {mk}"
    out, k = [], 0
    while k < len(items):
        kind, vi, conj = items[k]
        if kind == "P":
            run = [vi]
            first_conj = conj
            k += 1
            while k < len(items) and items[k][0] == "P":
                run.append(items[k][1])
                k += 1
            txt = f"{C.AT} {B.join_and(run)}"
            if first_conj and out:
                txt = f"{C.AND} {txt}"
            elif first_conj:
                raise ValueError(f"'ye ca' opening a head: {words!r}")
            out.append(txt)
            continue
        if kind == "V" and (k + 1 >= len(items) or items[k + 1][0] != "T"):
            raise ValueError(f"pavatte not before a time phrase: {words!r}")
        if kind == "Y" and k:
            raise ValueError(f"'Ye' clause inside a head: {words!r}")
        out.append(vi)
        k += 1
    return cap(", ".join(out))


def _is_member(w, M):
    try:
        M.key(w)
        return True
    except ValueError:
        return False


def b_sentence(s, M=SACCA_B):
    """'<head> <tesaṃ|tattha|tesaṃ tattha> A V1, no ca <same> B V2.' (B.b_noca) and
    '<head> <res> Añca V1 Bñca V2.' (B.b_both), or None if the sentence has no member word."""
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
        raise ValueError(f"no resumptive before the member: {s!r}")
    head = w[:h]
    for k, x in enumerate(head):
        if x.endswith(","):
            SLIPS_SEEN.append(("comma inside an answer head (absorbed by the list commas)", s[:80]))
            head[k] = x[:-1]
    if loc == "tattha" and not all((pt := B.plane_tok(_lc(x), PLANES)) and pt[1] == "loc"
                                   for x in head if _lc(x) != "avasese"):
        raise ValueError(f"'tattha' after a non-place head: {s!r}")
    head_txt = head_vi(head)
    clause = " ".join(w[i:])
    if f", no ca {loc} " in clause:
        c1, c2 = clause.split(f", no ca {loc} ")
        a, v1 = B.split_mv(c1, M)
        b, v2 = B.split_mv(c2, M)
        return B.b_noca(head_txt, loc, a, v1, b, v2)
    if " no ca " in clause:
        raise ValueError(f"'no ca' shape not placed: {s!r}")
    t = clause.split()
    j = next((k for k, x in enumerate(t) if k > 0 and _is_member(x, M)), None)
    if j is None or not t[0].endswith("ñca") or not t[j].endswith("ñca"):
        raise ValueError(f"unknown both-frame: {s!r}")
    a, v1 = M.subj(t[0]), B.verb(" ".join(t[1:j]))
    b, v2 = M.subj(t[j]), B.verb(" ".join(t[j + 1:]))
    return B.b_both(head_txt, loc, a, v1, b, v2)


PQ_RE = re.compile(r"(?:\((Ka|Kha)\) )?([Yy])(assa|attha)( vā pana)?( yattha)? (.+?) (tassa tattha|tassa|tattha) "
                   r"(.+?)\?")
CUTQ_RE = re.compile(r"\((Ka|Kha)\) (yassa|yattha)( vā pana)?( yattha)?(?: (.+?))?…pe…(?: (\S+))?\?")


def b_question(q, M=SACCA_B):
    """A full pavattivāra question piece (ends with «?»), labelled or not → C.pair_q, or None."""
    m = PQ_RE.fullmatch(q.strip())
    if not m:
        return None
    label, y, rel, vapana, y2, c1, then, c2 = m.groups()
    who = ("y" + rel) + (y2 or "")
    if C.Q_COR[who] != then:
        raise ValueError(f"relative {who!r} with correlative {then!r}: {q!r}")
    if label and (label == "Kha") != bool(vapana):
        raise ValueError(f"label / vā pana mismatch: {q!r}")
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {q!r}")
    a, v1 = B.split_mv(c1, M)
    b, v2 = B.split_mv(c2, M)
    return C.pair_q(who, f"{a} {v1[0]}", f"{b} {v2[0]}", label, bool(vapana))


def b_cut_question(body, M=SACCA_B):
    """'(Kha) yassa vā pana[ yattha][ A V]…pe…[ V2]?' at the start of a line → (Vietnamese, rest) or None:
    «(b) Còn ở người nào[, ở nơi nào] mà[ A V]…[ V2] không?» (coordinator: a cut question keeps «… không?»)."""
    m = CUTQ_RE.match(body)
    if not m:
        return None
    label, rel, vapana, y2, pre, tail = m.groups()
    who = rel + (y2 or "")
    if (label == "Kha") != bool(vapana):
        raise ValueError(f"label / vā pana mismatch: {body!r}")
    opening = f"{C.VA_PANA} {C.AT}" if vapana else cap(C.AT)
    s = f"{opening} {C.Q_REL[who][0]} mà"
    if pre:
        a, v = B.split_mv(pre, M)
        s += f" {a} {v[0]}"
    s += PE
    if tail:
        s += f" {B.verb(tail)[0]}"
    return f"{LABEL[label]} {s} không?", body[m.end():]


def b_cut_line(body, M=SACCA_B):
    """'Yattha A V…pe… (<note>).' → «Ở nơi nào mà A V… (<note>).»; 'Yattha A V…pe….' → 2-02 b_cut."""
    if (c := E.b_cut(body, M)) is not None:
        return c
    m = re.fullmatch(r"(Yattha|Yassa) (.+?)…pe… (\(.+?\))\.", body)
    if not m or m.group(3) not in NOTES_PALI:
        return None
    a, v = B.split_mv(m.group(2), M)
    return f"{cap(C.AT)} {C.Q_REL[m.group(1).lower()][0]} mà {a} {v[0]}{PE} {NOTES_PALI[m.group(3)]}."


# ===============================================================================================================
# 6. Line translator: questions, answers and …pe… cuts on one line
# ===============================================================================================================
PE_SPLIT = re.compile(r"( ?)…[Pp]e…(\.?)")


def piece(p):
    """One piece of a line (a question «…?», a sentence «….», or a cut piece) → Vietnamese."""
    core = p.strip()
    if core.endswith("?"):
        for f in (a_question, b_question):
            if (r := f(core)) is not None:
                return r
        raise ValueError(f"unknown question {core!r}")
    if core.endswith("."):
        if core in C.EXACT:
            return C.EXACT[core]
        if core in B.SHORT:
            return B.SHORT[core]
        if core in CLOSING:
            return CLOSING[core]
        for f in (a_sentence, b_sentence):
            if (r := f(core)) is not None:
                return r
        raise ValueError(f"unknown sentence {core!r}")
    if (r := a_partial(core)) is not None:
        return r
    raise ValueError(f"unknown cut piece {core!r}")


def chunk_vi(chunk):
    """A run of pieces without …pe… → Vietnamese, keeping the leading / trailing spaces of the chunk."""
    lead = chunk[:len(chunk) - len(chunk.lstrip())]
    trail = chunk[len(chunk.rstrip()):]
    body = chunk.strip()
    if not body:
        return chunk
    parts = [x for x in re.split(r"(?<=[?.]) ", body) if x]
    return lead + " ".join(piece(x) for x in parts) + trail


def line_vi(body):
    """A line body (no block ID; variants protected as ⟦k⟧) → Vietnamese."""
    if body in FIXED:
        return FIXED[body]
    if (c := b_cut_line(body)) is not None:
        return c
    pre = ""
    if (cq := b_cut_question(body)) is not None:
        pre, body = cq
        if not body.strip():
            return pre
    pieces = PE_SPLIT.split(body)                # [chunk, space, dot, chunk, …]
    out = []
    for k in range(0, len(pieces), 3):
        vi = chunk_vi(pieces[k])
        if k + 1 < len(pieces):
            if vi.endswith("."):                 # «Đúng vậy.» before …pe…: the «.» is absorbed (never «.…»)
                SLIPS_SEEN.append(("«.» right before …pe… (absorbed: never «.…»)", body[:60]))
                vi = vi[:-1]
            vi += pieces[k + 1] + PE             # the space before …pe… kept; a «.» after it absorbed
        out.append(vi)
    return pre + "".join(out)


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    else:
        brs = VAR_RE.findall(body)
        for k, br in enumerate(brs):
            body = body.replace(br, f"⟦{k}⟧", 1)
        out = line_vi(body)
        for k, br in enumerate(brs):
            if br not in VARIANTS:
                raise ValueError(f"undeclared variant {br!r}")
            if out.count(f"⟦{k}⟧") != 1:
                raise ValueError(f"variant {br!r} lost in {p!r}")
            out = out.replace(f"⟦{k}⟧", VARIANTS[br])
        if "⟦" in out or KC_TOKEN in out:
            raise ValueError(f"unplaced token in {p!r}")
    return f"{out} {bid}" if bid else out


def build(name=CH):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln))
            except (ValueError, KeyError) as e:
                raise ValueError(f"{name}: cannot place line {ln[:160]!r}: {e!r}") from None
        segs.append(out)
    return segs


# ===============================================================================================================
# 7. Assertions: termbase entries used verbatim, reused pi-N strings, agreement with the setters
# ===============================================================================================================
TERMBASE_USED = [
    ("Saccayamakaṃ", S.yamaka_title(YAMAKA)), ("dukkhasaccaṃ", TRUTH["dukkhasacca"]),
    ("samudayasaccaṃ", TRUTH["samudayasacca"]), ("nirodhasaccaṃ", TRUTH["nirodhasacca"]),
    ("maggasaccaṃ", TRUTH["maggasacca"]), ("dukkhaṃ", TRUTH["dukkha"]), ("samudayo", TRUTH["samudaya"]),
    ("nirodho", TRUTH["nirodha"]), ("maggo", TRUTH["magga"]), ("saccaṃ", TRUTH["sacca"]), ("saccā", X_PL),
    ("Kāyikaṃ dukkhaṃ", KAYIKA), ("cetasikaṃ dukkhaṃ", CETASIKA), ("Suddhasaccavāro", "mục về các sự thật thuần túy"),
    ("Suddhasaccamūlacakkavāro", "mục về vòng luân chuyển dựa trên các sự thật thuần túy"),
    ("Paṇṇattivāra", "mục về sự định danh"), ("pavatte", "đời sống"), ("Apāye", "cõi khổ"),
    ("āpāyikānaṃ", PLANES["apāy"][1]), ("Avasese", AVASESE), ("Anabhisametāvīnaṃ", "người chưa thấu hiểu"),
    ("Abhisametāvīnaṃ", "người đã thấu hiểu"), ("Aggamaggasamaṅgīnaṃ", "người có được con đường tối thượng"),
    ("arahantānaṃ", "bậc A-la-hán"), ("aggamaggaṃ paṭilabhissanti", f"{WILL_ATTAIN} {AGGAMAGGAM}"),
    ("anantarā", "ngay sau"), ("caññe", "khác"), ("vattamāne", "khi … đang diễn ra"), ("citte", MIND),
    ("akusale citte", CITTE_KIND["akusale"]), ("taṇhāvippayuttacitte", MIND_KIND["taṇhāvippayutta"]),
    ("taṇhāvippayuttacittassa uppādakkhaṇe", f"khoảnh khắc sinh khởi của {MIND_KIND['taṇhāvippayutta']}"),
    ("maggavippayuttacittassa uppādakkhaṇe", f"khoảnh khắc sinh khởi của {MIND_KIND['maggavippayutta']}"),
    ("taṇhāvippayuttamaggavippayuttacittassa uppādakkhaṇe",
     f"khoảnh khắc sinh khởi của {MIND_KIND['taṇhāvippayuttamaggavippayutta']}"),
    ("maggavippayuttataṇhāvippayuttacittassa uppādakkhaṇe",
     f"khoảnh khắc sinh khởi của {MIND_KIND['maggavippayuttataṇhāvippayutta']}"),
    ("Taṇhāya uppādakkhaṇe", "khoảnh khắc sinh khởi của khao khát"),
    ("taṇhāya bhaṅgakkhaṇe", "khoảnh khắc tan rã của khao khát"),
    ("upapatticittassa uppādakkhaṇe", f"khoảnh khắc sinh khởi của {MIND_KIND['upapatti']}"),
    ("cittassa bhaṅgakkhaṇe", "khoảnh khắc tan rã của tâm"), ("cittassa uppādakkhaṇe", "khoảnh khắc sinh khởi của tâm"),
    ("maggassa", MAGGAM), ("phalassa", OWNER["phalassa"]), ("Aggamaggassa", AGGAMAGGAM),
    ("nirodhasamāpannānaṃ", "người nhập thành tựu thiền chấm dứt"), ("Pacchimacittasamaṅgīnaṃ", "người có được tâm cuối cùng"),
    ("yatthakasadisaṃ", f"giống như {P_PLACE}"), ("yassayatthakasadisaṃ", f"giống như {P_PERSON_PLACE}"),
    ("Yassakampi", P_PERSON), ("yassayatthakampi", P_PERSON_PLACE), ("yatthakampi", P_PLACE), ("yatthakā", P_PLACE),
    ("asaññattā", "cõi Vô Tưởng"), ("aggamaggaṃ paṭilabhissānti", f"{WILL_ATTAIN} {AGGAMAGGAM}"),
    ("Itaresaṃ", "người khác"), ("puthujjanā", "người phàm phu"), ("maggaṃ paṭilabhissanti", E.MAGGAM_PATILABHISSANTI),
    ("nirodhavārepi", B.NIRODHAVARO), ("avasesaṃ", "còn lại"), ("avaseso", "còn lại"),
]
REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("Cattāri saccāni (pi-2 4-saccavibhango)", f"{CATTARI_SACCANI} –", "2"),
    ("dukkhasaccaṃ (pi-2 18-dhammahadayavibhango)", TRUTH["dukkhasacca"], "2"),
    ("Samudayasaccaṃ (pi-2 18-dhammahadayavibhango)", TRUTH["samudayasacca"], "2"),
    ("kāyikaṃ dukkhaṃ (pi-1 2-05)", KAYIKA, "1"),
    ("kusalābyākate citte vattamāne (pi-5)", "đang diễn ra", "5"),
    ("evaṃ sabbaṃ vitthāretabbaṃ (pi-5)", VITTHARETABBAM, "5"),
    ("nānākaraṇaṃ (pi-5)", "sự khác biệt", "5"),
    ("āpāyikaṃ dukkhaṃ (pi-5)", "cõi khổ", "5"),
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
    # the head parser reproduces 2-01's person heads and place heads (family B setter) byte for byte
    for hd in ("Asaññasattaṃ upapajjantānaṃ", "Itaresaṃ catuvokāraṃ pañcavokāraṃ upapajjantānaṃ",
               "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ", "Suddhāvāsānaṃ asaññasattānaṃ", "Sabbesaṃ cavantānaṃ"):
        assert head_vi(hd.split()) == B.answer_head(hd, "tesaṃ"), (hd, head_vi(hd.split()), B.answer_head(hd, "tesaṃ"))
    assert head_vi("Catuvokāre pañcavokāre".split()) == B.place_head("Catuvokāre pañcavokāre")
    # 8's persons and the ye heads of 2-02 / 2-01
    assert head_vi(["nirodhasamāpannānaṃ", "asaññasattānaṃ"]) == cap(f"{D.AT} {D.PERSON['nirodhasamāpannānaṃ']} "
                                                                       f"{D.AND} {D.PERSON['asaññasattānaṃ']}")
    assert YE_HEADS["ye maggaṃ paṭilabhissanti"] == E.e_head("Ye maggaṃ paṭilabhissanti te x")[0].rsplit(",", 1)[0]
    assert OTHERS == D.PERSON["itaresaṃ"]
    # identical Pāli heads in the Dhammayamaka (9-01, coordinator): byte for byte
    for hd in ("Sabbesaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe", "Sabbesaṃ cittassa bhaṅgakkhaṇe",
               "Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe",
               "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ", "Suddhāvāsānaṃ dutiye akusale citte vattamāne",
               "Aggamaggasamaṅgīnaṃ arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti asaññasattānaṃ",
               "Aggamaggassa bhaṅgakkhaṇe arahantānaṃ yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa "
               "cittassa bhaṅgakkhaṇe asaññasattānaṃ", "Pacchimacittasamaṅgīnaṃ", "Itaresaṃ",
               "Itaresaṃ catuvokārānaṃ pañcavokārānaṃ", "Suddhāvāsaṃ upapajjantānaṃ", "Catuvokāre pañcavokāre"):
        loc = "tattha" if hd == "Catuvokāre pañcavokāre" else "tesaṃ"
        assert head_vi(hd.split()) == T9.answer_head(hd, loc), (hd, head_vi(hd.split()), T9.answer_head(hd, loc))
    # the question shell is 7-01's
    assert b_question("(Ka) yassa dukkhasaccaṃ uppajjati tassa samudayasaccaṃ uppajjatīti?") == C.pair_q(
        "yassa", f"{TRUTH['dukkhasacca']} sinh khởi", f"{TRUTH['samudayasacca']} sinh khởi", "Ka")
    # parsers raise on unknown words
    for bad_s in ("Brahmānaṃ tesaṃ dukkhasaccaṃ uppajjati, no ca tesaṃ samudayasaccaṃ uppajjati.",
                  "Arūpe tesaṃ dukkhasaccañca uppajjati samudayasaccaṃ uppajjati."):
        try:
            b_sentence(bad_s)
        except ValueError:
            continue
        raise AssertionError(f"no error on {bad_s!r}")


# ===============================================================================================================
# 8. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    out = [f"# pi-6 rails {N} (Saccayamaka 1): the four truths in families A and B; new answer-head frames", "",
           "Builder: build_rails_5-01_vi.py (import with importlib; 5-02 / 5-03 take from it: `TRUTH`, `SACCA_A` "
           "(paṇṇattivāra members), `SACCA_B` (pavattivāra members), `KC_VI`, `PLANES`, `PERSON_GEN`, `ATTR`, "
           "`YE_GROUPS`, `YE_HEADS`, `INNER_TESAM`, `MIND_KIND`, `OWNER`, `T_PATTERNS`, `moment`, `head_items`, "
           "`head_vi`, `a_sentence`, `a_question`, `a_partial`, `b_sentence`, `b_question`, `b_cut_question`, "
           "`b_cut_line`, `VARIANTS`, `FIXED`, `NOTES_PALI`, `line_vi`, `tr_line`, `build`). Families A / B from "
           "build_rails_2-01_vi, shapes from build_rails_7-01_vi, moments from build_rails_8_vi, cut lines and ye "
           "heads from build_rails_2-02_vi, all unchanged. Format: Pāli = tiếng Việt.", ""]

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    h("Members (termbase; pi-2)")
    for k, v in TRUTH.items():
        row(k, v)
    row("saccā (subject / predicate)", f"{SACCA_PL} / {X_PL}")
    row(KC_PALI, KC_VI)
    row(UDDESA_PALI, UDDESA_VI + "  (comma after samudayasaccaṃ added: missing punctuation)")
    h("Headings and fixed lines")
    for p in ("Saccayamakaṃ", "Paṇṇattivāra", "Suddhasaccavāro", "Suddhasaccamūlacakkavāro"):
        row(p, heading(p))
    for p, v in {**FIXED, **NOTES_PALI}.items():
        if p != UDDESA_PALI:
            row(p, v)
    row("Uppādavāro.", UPPADAVARO_CLOSE)
    h("Family A: questions and answers (2-01 slot functions)")
    for q in ("(Ka) dukkhaṃ dukkhasaccaṃ?", "(Kha) saccā samudayasaccaṃ?", "(Ka) na dukkhaṃ na saccaṃ?",
              "Samudayo saccaṃ?", "Na saccā na dukkhaṃ?"):
        row(q, a_question(q))
    for s in ("Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ dukkhasaccaṃ, na dukkhaṃ.",
              "Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ dukkhañceva dukkhasaccañca.",
              "Samudayasaccaṃ ṭhapetvā avaseso samudayo, na samudayasaccaṃ.",
              "Samudayasaccaṃ samudayo ceva samudayasaccañca.",
              "Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ ṭhapetvā avasesaṃ na dukkhaṃ, dukkhasaccaṃ.",
              "Dukkhañca dukkhasaccañca ṭhapetvā avasesaṃ na ceva dukkhaṃ na ca dukkhasaccaṃ.",
              "Samudayasaccaṃ ṭhapetvā avaseso na samudayasaccaṃ, samudayo.",
              "Samudayasaccaṃ saccañceva samudayasaccañca.", "Avasesā saccā na samudayasaccaṃ.",
              "Dukkhaṃ ṭhapetvā avasesā saccā na dukkhaṃ, saccā.",
              "Dukkhañca saccañca ṭhapetvā avasesaṃ na ceva dukkhaṃ na ca saccā."):
        row(s, a_sentence(s))
    row("Samudayaṃ ṭhapetvā…pe… nirodhaṃ ṭhapetvā…pe….", line_vi("Samudayaṃ ṭhapetvā…pe… nirodhaṃ ṭhapetvā…pe…."))
    row("Samudayo saccanti? Āmantā…pe…. / Āmantā.…Pe….", line_vi("Samudayo saccanti? Āmantā…pe…."))
    row("Saccā nirodhasaccanti?…Pe…. Saccā maggasaccanti?", line_vi("Saccā nirodhasaccanti?…Pe…. Saccā maggasaccanti?"))
    h("Family B: question shells and cuts (7-01 pair_q)")
    for q in ("(Ka) yassa dukkhasaccaṃ uppajjati tassa samudayasaccaṃ uppajjatīti?",
              "(Ka) yassa yattha dukkhasaccaṃ nuppajjittha tassa tattha maggasaccaṃ nuppajjitthāti?"):
        row(q, b_question(q))
    for q in ("(Kha) yattha vā pana…pe…?", "(Kha) yassa vā pana…pe… uppajjitthāti?",
              "(Kha) yassa vā pana yattha…pe… uppajjitthāti?",
              "(Kha) yassa vā pana yattha samudayasaccaṃ uppajjissati…pe… uppajjissatīti?"):
        row(q, b_cut_question(q)[0])
    for b in ("Yattha dukkhasaccaṃ uppajjittha…pe….", "Yattha dukkhasaccaṃ uppajjati…pe… (yatthakā sadisā sabbe).",
              "Yattha dukkhasaccaṃ uppajjati…pe… (yatthakampi yassayatthakasadisaṃ kātabbaṃ)."):
        row(b, b_cut_line(b))
    h("Family B: answer-head items (new; one «ở» per run of persons, each place / time phrase its own item)")
    row("pavatte <time phrase>", f"{PAVATTE}, <vào khoảnh khắc …>  (9-01: its own item)")
    for k, v in MIND_KIND.items():
        row(f"{k}cittassa uppādakkhaṇe / bhaṅgakkhaṇe", f"{moment('uppādakkhaṇe', v)} / {moment('bhaṅgakkhaṇe', v)}")
    for k, v in OWNER.items():
        row(f"{k} uppādakkhaṇe", moment("uppādakkhaṇe", v))
    row("maggassa ca phalassa ca uppādakkhaṇe", moment("uppādakkhaṇe", f"{MAGGAM} {C.AND} {OWNER['phalassa']}"))
    row("aggamaggassa ca phalassa ca uppādakkhaṇe", moment("uppādakkhaṇe", f"{AGGAMAGGAM} {C.AND} {OWNER['phalassa']}"))
    row("yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe / bhaṅgakkhaṇe",
        f"{moment('uppādakkhaṇe', ANANTARA_MIND)} / … tan rã …")
    for p in ("dutiye citte vattamāne", "dutiye akusale citte vattamāne", "taṇhāvippayuttacitte vattamāne"):
        row(p, head_items(p.split())[0][1])
    row("yassa cittassa anantarā aggamaggaṃ paṭilabhissanti (person group)", ANANTARA_PERSON)
    for k, (v, conj) in YE_GROUPS.items():
        if "ānti" not in k and not k.startswith("yassa"):
            row(f"{k} (in a person run)", f"{v}  (after a time phrase / place: «và ở {v}»)")
    for k, v in YE_HEADS.items():
        row(f"{cap(k)} … (opening the head)", f"{v}, …")
    for k, v in INNER_TESAM.items():
        row(f"{k} (inside a head)", v)
    for k, v in PERSON_GEN.items():
        row(k, v)
    for k, v in ATTR.items():
        row(f"{k} / {k} upapajjantānaṃ", f"{PEOPLE} {v} / {PEOPLE} {v} {B.PARTICIPLES['upapajjantānaṃ'][0]}")
    row("Sabbesaṃ (bare, before a time phrase)", ALL_PEOPLE)
    row("Apāye / Avasese catuvokāre pañcavokāre (place heads)",
        f"{head_vi(['Apāye'])} / {head_vi('Avasese catuvokāre pañcavokāre'.split())}")
    h("Family B: whole answers built by the module (examples)")
    for s in ("Sabbesaṃ upapajjantānaṃ pavatte taṇhāvippayuttacittassa uppādakkhaṇe tesaṃ dukkhasaccaṃ uppajjati, "
              "no ca tesaṃ samudayasaccaṃ uppajjati.",
              "Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe arūpe maggassa ca phalassa ca uppādakkhaṇe tesaṃ "
              "samudayasaccañca nuppajjati dukkhasaccañca nuppajjati.",
              "Avasese catuvokāre pañcavokāre tattha dukkhasaccañca uppajjati maggasaccañca uppajjati.",
              "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ tesaṃ tattha dukkhasaccaṃ uppajjittha, no ca tesaṃ "
              "tattha samudayasaccaṃ uppajjittha.",
              "Aggamaggasamaṅgīnaṃ arahantānaṃ ye ca puthujjanā maggaṃ na paṭilabhissanti tesaṃ dukkhasaccaṃ "
              "uppajjissati, no ca tesaṃ maggasaccaṃ uppajjissati.",
              "Ye puthujjanā maggaṃ na paṭilabhissanti tesaṃ taṇhāya uppādakkhaṇe tesaṃ samudayasaccaṃ uppajjati, no "
              "ca tesaṃ maggasaccaṃ uppajjissati.",
              "Aggamaggassa uppādakkhaṇe arahantānaṃ cittassa uppādakkhaṇe ye ca puthujjanā maggaṃ na paṭilabhissanti "
              "tesaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe tesaṃ dukkhasaccaṃ uppajjati, no ca tesaṃ "
              "maggasaccaṃ uppajjissati.",
              "Yassa cittassa anantarā aggamaggaṃ paṭilabhissanti tassa cittassa uppādakkhaṇe ye caññe maggaṃ "
              "paṭilabhissanti tesaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe tesaṃ dukkhasaccañca uppajjati "
              "maggasaccañca uppajjissati."):
        row(s, b_sentence(s))
    h("Variants")
    for p, v in VARIANTS.items():
        row(p, v)
    h("Termbase gaps and choices (for the coordinator)")
    out += [
        "- Bare dukkhaṃ = «khổ đau» throughout (user); Kāyikaṃ dukkhaṃ cetasikaṃ dukkhaṃ (juxtaposed, no ca) = "
        f"«{KC_VI}» (joined «và», as 2-01 joins juxtaposed runs).",
        "- saccā as a subject «các sự thật» (2-01 khandhā «các khối»), as a predicate «sự thật».",
        "- avaseso / avasesaṃ alone = 2-01's «những gì còn lại» (termbase «còn lại»).",
        "- Answer heads: each item (person run, place, time phrase) is its own comma item; one «ở» per run of person "
        "groups; a group after a time phrase or a place keeps its own «ở» (coordinator); pavatte «trong đời sống» "
        "is its own item (9-01).",
        f"- Sabbesaṃ with no participle (before a time phrase) «{ALL_PEOPLE}» (9-01 ALL_BEINGS).",
        f"- yassa cittassa anantarā aggamaggaṃ paṭilabhissanti: as a person group «{ANANTARA_PERSON}»; with tassa "
        f"cittassa <moment> «vào khoảnh khắc … của {ANANTARA_MIND}» (9-01 PERSON_ATTAIN / that_mind_moment, imported).",
        "- ye ca puthujjanā … / ye caññe … in a person run: «những người phàm phu nào …» / «những người khác nào …» "
        "(2-02 «<NP> nào …»); after a time phrase the run opens «và ở …» (the Pāli ca).",
        "- Inner tesaṃ: «ở những người ấy»; tesaṃ upapajjantānaṃ / cavantānaṃ «khi những người ấy đang tái sinh / "
        "đang chết đi» (2-02 KHI_CAVANTA).",
        f"- Avasese catuvokāre pañcavokāre: one place item «{head_vi('Avasese catuvokāre pañcavokāre'.split())}» "
        "(«còn lại» scopes over both planes; the exception to «each place its own ở»).",
        "- maggassa ca phalassa ca «của con đường và thành quả»; dutiye «thứ hai» (no termbase entry: ordinal).",
        "- Editorial notes: sabbattha «ở mọi chỗ» (coordinator); Tantinānākaraṇaṃ «sự khác biệt trong lời văn» (pi-5 "
        "nānākaraṇaṃ «sự khác biệt»; tanti no entry); heṭṭhā «ở trên» (earlier in the text); sadisaṃ / sadisā «giống "
        "nhau»; vitthāretabbaṃ (pi-5) «nên được trình bày chi tiết»; X-sadisaṃ kātabbaṃ «nên được làm cho giống "
        "như X» (4 sadisaṃ kātabbaṃ); sabbattha sadisaṃ «ở mọi chỗ … đều giống nhau» (3-01).",
        "- Variant notes: evaṃ avasesesu tīsu saccesu «cũng vậy ở ba sự thật còn lại»; evaṃ puggalokāsepi "
        "nirodhavārepi «cũng vậy ở phần về người và nơi chốn và ở mục về sự chấm dứt»; puggalokāsavārepi «cũng vậy ở "
        "mục về người và nơi chốn».",
        "",
        "## Slips and punctuation (translated as written or as plainly meant)",
        "",
        "- ^6-5-1 «samudayasaccaṃ nirodhasaccaṃ» without a comma: comma added (missing punctuation).",
        "- ^6-5-11 «avasesaṃ na dukkhaṃ [variant] dukkhasaccaṃ» without the comma before the last word: «, mà là».",
        "- ^6-5-22, ^6-5-26 «Āmantā.…Pe….»: the «.» before …pe… absorbed («Đúng vậy…»; never «.…»).",
        "- ^6-5-51, ^6-5-79 «paṭilabhissanti, ye caññe», ^6-5-77 «arahantānaṃ, āpāyikānaṃ»: the comma inside the "
        "head is absorbed by the list commas.",
        "- ^6-5-74 «paṭilabhissānti» (termbase variant spelling of paṭilabhissanti): rendered as meant.",
        "- ^6-5-76 «asaññattā» (termbase variant spelling of asaññasattā): rendered as meant.",
        "- ^6-5-58 and ^6-5-79: answer on the question's line (kept on that line); ^6-5-63 «Uppajjittha.» on a line "
        "of its own (kept).",
        "- ^6-5-20 (Kha) asks «saccā dukkhasaccanti?» (not «saccā dukkhanti?»): translated as written.",
        "- ^6-5-76 first (Ka) answer, second sentence: «asaññasattā cavantānaṃ» stands twice (also «asaññattā "
        "cavantānaṃ» before it): kept as written (the repeated group stays).",
        "- Variant brackets inside an answer head go after the Vietnamese item whose Pāli they follow (^6-5-33 after "
        "the moment phrase; ^6-5-69 «… paṭilabhissanti ye [variant] caññe …» after the first group, the variant "
        "being about its end).",
        "- Termbase adherence: 4 misses, all 2-01 shapes kept on purpose (Itaresaṃ catuvokārānaṃ pañcavokārānaṃ "
        "«chúng sinh khác trong cõi gồm bốn khối và cõi gồm năm khối»).",
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
