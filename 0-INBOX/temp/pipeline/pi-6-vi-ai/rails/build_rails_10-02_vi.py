"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-02 (Indriyayamaka 2: suddhindriyamūlacakkavāra + pavattivāra,
uppādavāra, paccuppanna) and the INDRIYA PERSON-HEAD module that 10-03 … 10-13 import.

Setters (all imported READ-ONLY with importlib; every shared string comes from their functions):
  build_rails_10-01_vi  (I)   Indriya members, PART_KEYS / is_part, ind_mulaka, the paṇṇattivāra line translator
  build_rails_3-01_vi   (A)   attribute beings (AY_ATTRS, ATTR_JOIN), PLANES_AY, question_vi / split_mv, cuts
  build_rails_3-02_vi   (A2)  person heads with planes / nested runs (ay_persons), Ye heads (answer_head)
  build_rails_2-01_vi   (B)   family B: b_q, b_noca, b_both, place_head, VERB_TABLE, SHORT, L, PERSON, QUANT
  build_rails_9-01_vi   (DY)  answer heads with pavatte / moments (PAVATTE, moment_vi, mind_gen, SECTION_HEAD)
  build_rails_7-01_vi   (C)   shared connectors (AT, THEN, AND …)     build_rails_8_vi (D8): MOMENT, MIND

New here (named constants; 10-03 … 10-13 import them):
  IND_ATTRS                     sahetukānaṃ «có gốc rễ», ahetukānaṃ «không có gốc rễ» (pi-2), ñāṇasampayuttānaṃ
                                «gắn liền với hiểu biết», ñāṇavippayuttānaṃ «không gắn liền với hiểu biết» (termbase)
  SEX / REBORN_AS / sex_vi      itthīnaṃ / purisānaṃ upapajjantānaṃ «… đang tái sinh làm người nữ / người nam» (user);
                                na itthīnaṃ «… đang tái sinh không làm người nữ»
  FEEL / feel_vi                somanassena / upekkhāya «có niềm vui / có sự bình thản đi kèm» (termbase);
                                vinā somanassena «không có niềm vui đi kèm»
  FAC_MIND / faculty_mind_gen   somanassasampayuttasaddhāvippayuttacittassa «tâm gắn liền với niềm vui và không gắn
                                liền với niềm tin» (two-part citta «tâm <A> và <B>», coordinator; = termbase)
  ind_group / ind_persons       person groups with these words (else 3-02 ay_persons, byte-identical)
  ind_head_parts / ind_answer_head   heads with pavatte / moments in 9-01's shape («Ở …, trong đời sống, vào …»)
  PRON_FEM                      tāsaṃ (feminine) = tesaṃ «những người ấy»
  pv_sentence / pv_unit / pv_line / tr_line / build   the pavattivāra line translator (paṇṇatti lines: 10-01's)
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

    I2 = importlib.import_module("build_rails_10-02_vi"); segs = I2.build("10-03-indriyayamaka.md", fixed={...})

usage: python -I -X utf8 -B build_rails_10-02_vi.py
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
I = importlib.import_module("build_rails_10-01_vi")    # READ-ONLY: Indriya module (setter)
A = importlib.import_module("build_rails_3-01_vi")     # READ-ONLY: attribute beings, questions, cuts
A2 = importlib.import_module("build_rails_3-02_vi")    # READ-ONLY: person heads with planes, Ye heads
B = importlib.import_module("build_rails_2-01_vi")     # READ-ONLY: family B frames
C = importlib.import_module("build_rails_7-01_vi")     # READ-ONLY: shared connectors
D8 = importlib.import_module("build_rails_8_vi")       # READ-ONLY: moments, mind
DY = importlib.import_module("build_rails_9-01_vi")    # READ-ONLY: pavatte / moment heads

cap = S.cap
CH = "10-02-indriyayamaka.md"
N = "10-02"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
TERMBASE = S.ROOT / "AI_translation/vietnamese/pi-6-pali-vietnamese-termbase-plain.md"
M_IND = I.INDRIYA
PLANES = A.PLANES_AY
HEADS_SEEN = []        # (Pāli head, Vietnamese)
MINDS_SEEN = set()     # mind genitives built here (checked against the termbase)
CHECKED = {"10-01": 0, "3-01/3-02": 0}


def lc(w):
    return w[:1].lower() + w[1:]


# ===============================================================================================================
# 1. Person words new in the Indriya pavattivāra
# ===============================================================================================================
# pre-verbal attributes (joined with 3-01's ATTR_JOIN, like sacakkhukānaṃ «có mắt»)
IND_ATTRS = {
    "sahetukānaṃ": "có gốc rễ",                     # pi-2 18-dhammahadayavibhango (identical Pāli); sibling Sahetukaṃ
    "ahetukānaṃ": "không có gốc rễ",                # pi-2 (identical Pāli); sibling Ahetukaṃ
    "ñāṇasampayuttānaṃ": "gắn liền với hiểu biết",   # termbase (user: ñāṇasampayutta «gắn liền với hiểu biết»); pi-2
    "ñāṇavippayuttānaṃ": "không gắn liền với hiểu biết",   # termbase; pi-2
}
PRE_ATTRS = {**A.AY_ATTRS, **IND_ATTRS}
# itthīnaṃ / purisānaṃ upapajjantānaṃ = «… tái sinh làm người nữ / người nam» (user decision 2026-11-22)
SEX = {"itthīnaṃ": I.INDRIYA.subj("itthī"), "purisānaṃ": I.INDRIYA.subj("puriso")}   # «người nữ» / «người nam»
REBORN_AS = "làm"
NOT = "không"                                       # na itthīnaṃ «không làm người nữ»; vinā «không có …»
# the feeling that accompanies the rebirth (termbase somanassena / upekkhāya «có … đi kèm»)
FEEL = {"somanassena": "có niềm vui đi kèm", "upekkhāya": "có sự bình thản đi kèm"}
FEEL_JOIN = ", "                                    # after «làm người nữ»: «…, có niềm vui đi kèm»
PART_FEM = {"upapajjantīnaṃ": "upapajjantānaṃ"}     # feminine participle (termbase «đang tái sinh») = 2-01's
REBIRTH_PARTS = ("upapajjantānaṃ",)                 # participles the SEX / FEEL words are set for (user / termbase)
QUANT_FEM = {"itarāsaṃ": "itaresaṃ"}                # termbase Itarāsaṃ «người khác» (= Itaresaṃ)
PRON_FEM = {"tāsaṃ": "tesaṃ", "tāsaṃ tattha": "tesaṃ tattha"}   # «những người ấy» (Vietnamese has no gender)
NEW_WORDS = set(IND_ATTRS) | set(SEX) | set(FEEL) | set(PART_FEM) | set(QUANT_FEM) | {"na", "vinā"}


def sex_vi(key, neg=False):
    """itthīnaṃ «làm người nữ»; na itthīnaṃ «không làm người nữ»."""
    return f"{NOT + ' ' if neg else ''}{REBORN_AS} {SEX[key]}"


def feel_vi(key, vina=False):
    """somanassena «có niềm vui đi kèm»; vinā somanassena «không có niềm vui đi kèm»."""
    return f"{NOT + ' ' if vina else ''}{FEEL[key]}"


def ind_group(quant, pre, part, sex=None, feel=None):
    """One person group: «những người <attr, attr> đang tái sinh [làm người nữ][, có niềm vui đi kèm]».
    Without sex / feel words = 3-01's ay_group (asserted in check_frames)."""
    words = []
    if quant == "sabbesaṃ":
        words.append(B.QUANT[quant])
    words.append(B.PERSON)
    if quant == "itaresaṃ":
        words.append(B.QUANT[quant])
    if pre:
        words.append(A.ATTR_JOIN.join(pre))
    words.append(B.PARTICIPLES[part][0])
    if (sex or feel) and part not in REBIRTH_PARTS:
        raise ValueError(f"sex / feeling words with {part!r} are not set (only upapajjantānaṃ)")
    out = " ".join(words)
    if sex:
        out += f" {sex}"
    if feel:
        out += (FEEL_JOIN if sex else " ") + feel
    return out


def ind_persons(head):
    """Genitive person phrase → Vietnamese groups (no «Ở»). Without this module's words: 3-02 ay_persons."""
    toks = head.split()
    if not any(lc(t) in NEW_WORDS for t in toks):
        out = A2.ay_persons(head, PLANES)
        HEADS_SEEN.append((head, out))
        return out
    groups = []
    quant, pre, sex, feel, neg, vina = None, [], None, None, False, False

    def dangling():
        if quant or pre or sex or feel or neg or vina:
            raise ValueError(f"dangling words in person phrase {head!r}")

    for t in toks:
        tl = lc(t)
        tl = QUANT_FEM.get(tl, tl)
        if tl == "na":
            if neg:
                raise ValueError(f"double na in {head!r}")
            neg = True
        elif tl == "vinā":
            vina = True
        elif tl in B.QUANT:
            dangling()
            quant = tl
        elif tl in PRE_ATTRS:
            if neg or vina:
                raise ValueError(f"na / vinā before an attribute in {head!r}")
            pre.append(PRE_ATTRS[tl])
        elif tl in SEX:
            if sex or vina:
                raise ValueError(f"misplaced {t!r} in {head!r}")
            sex, neg = sex_vi(tl, neg), False
        elif tl in FEEL:
            if feel or neg:
                raise ValueError(f"misplaced {t!r} in {head!r}")
            feel, vina = feel_vi(tl, vina), False
        elif tl in B.PARTICIPLES or tl in PART_FEM:
            if neg or vina:
                raise ValueError(f"dangling na / vinā in {head!r}")
            groups.append(ind_group(quant, pre, PART_FEM.get(tl, tl), sex, feel))
            quant, pre, sex, feel = None, [], None, None
        elif B.plane_tok(tl, PLANES):
            raise ValueError(f"plane with this module's words not set: {head!r}")
        else:
            raise ValueError(f"unknown word {t!r} in person phrase {head!r}")
    dangling()
    out = B.join_and(groups)
    HEADS_SEEN.append((head, out))
    return out


# ===============================================================================================================
# 2. Kinds of mind (faculty-associated) and answer heads with pavatte / moments (9-01 shape)
# ===============================================================================================================
FAC_MIND = {"somanassa": I.IND_NAME["somanassa"].replace("năng lực ", ""),     # niềm vui
            "upekkhā": "sự bình thản", "saddhā": "niềm tin", "ñāṇa": "hiểu biết"}  # termbase -sampayuttacittassa
SAMPAYUTTA = "gắn liền với"                        # -sampayutta (pi-1; termbase)
VIPPAYUTTA = DY.VIPPAYUTTA                         # -vippayutta «không gắn liền với» (9-01)
ASSOC = {"sampayutta": SAMPAYUTTA, "vippayutta": VIPPAYUTTA}
FAC_RE = re.compile(r"(somanassa|upekkhā|saddhā|ñāṇa)(sampayutta|vippayutta)")


def faculty_mind_gen(word):
    """cittassa «tâm»; kusala… kinds: 9-01 mind_gen; somanassasampayuttasaddhāvippayuttacittassa «tâm gắn liền với
    niềm vui và không gắn liền với niềm tin» (two-part «tâm <A> và <B>», coordinator)."""
    w = lc(word)
    if not w.endswith("cittassa"):
        raise ValueError(f"not a mind genitive {word!r}")
    stem = w[:-len("cittassa")]
    parts = FAC_RE.findall(stem)
    if not stem or not parts:
        return DY.mind_gen(word)
    if "".join(a + b for a, b in parts) != stem:
        raise ValueError(f"unknown kind of mind {word!r}")
    out = f"{D8.MIND} " + f" {C.AND} ".join(f"{ASSOC[b]} {FAC_MIND[a]}" for a, b in parts)
    MINDS_SEEN.add((w, out))
    return out


def ind_head_parts(head):
    """Answer head → parts: person runs «ở …» (ind_persons), pavatte «trong đời sống», <mind> uppādakkhaṇe
    «vào khoảnh khắc sinh khởi của tâm …» (9-01 head_parts shape: parts joined «, »)."""
    toks = head.split()
    parts, run, i = [], [], 0

    def flush():
        if run:
            parts.append(f"{C.AT} {ind_persons(' '.join(run))}")
            run.clear()

    while i < len(toks):
        t = toks[i]
        if lc(t) == "pavatte":
            flush()
            parts.append(DY.PAVATTE)
            i += 1
        elif i + 1 < len(toks) and lc(toks[i + 1]) in D8.MOMENT:
            flush()
            parts.append(DY.moment_vi(toks[i + 1], faculty_mind_gen(t)))
            i += 2
        else:
            run.append(t)
            i += 1
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts


def ind_answer_head(head, loc):
    """tattha: 2-01 place_head (PLANES_AY); Ye … heads: 3-02 answer_head; else ind_head_parts joined «, »."""
    if loc == "tattha":
        return B.place_head(head, PLANES)
    if head.startswith("Ye ") or f" {A2.D.YE_CA} " in head:
        return A2.answer_head(head, loc, PLANES)
    return cap(", ".join(ind_head_parts(head)))


# ===============================================================================================================
# 3. Sentences, units, lines (pavattivāra)
# ===============================================================================================================
LOCP = r"(tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ|tattha)"
NOCA_RE = re.compile(r"(.+?) " + LOCP + r" (.+?), no ca \2 (.+?)\.")
BOTH_RE = re.compile(r"(.+?) " + LOCP + r" (\S+?ñca) (\S+) (\S+?ñca) (\S+)\.")
CUT_ANS_RE = re.compile(r"(\S+?)( ?)…pe…\.?")


def pv_sentence(s, M=None):
    """Family B answer (2-01 b_noca / b_both) with this module's heads; None if it is not one."""
    M = M or M_IND
    if m := NOCA_RE.fullmatch(s):
        head, loc, c1, c2 = m.groups()
        a, v1 = A.split_mv(c1, M)
        b, v2 = A.split_mv(c2, M)
        return B.b_noca(ind_answer_head(head, loc), PRON_FEM.get(loc, loc), a, v1, b, v2)
    if m := BOTH_RE.fullmatch(s):
        head, loc, c1, v1, c2, v2 = m.groups()
        return B.b_both(ind_answer_head(head, loc), PRON_FEM.get(loc, loc), M.subj(c1), B.verb(v1),
                        M.subj(c2), B.verb(v2))
    return None


def pv_unit(u, M=None):
    M = M or M_IND
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if u.endswith("?"):
        return A.question_vi(u[:-1], M)                 # 3-01 (2-01 b_q shell; member lists cut by …pe… / …)
    if u in B.SHORT:
        return B.SHORT[u]
    if (m := CUT_ANS_RE.fullmatch(u)) and m.group(1) + "." in B.SHORT:   # Āmantā …pe…. «Đúng vậy …» (10-01)
        return B.SHORT[m.group(1) + "."][:-1] + (" " if m.group(2) else "") + S.PE
    if (out := pv_sentence(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def pv_line(body, M=None):
    body, label = body.strip(), None
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)\.?)", body):     # trailing (Xindriyamūlakaṃ) label
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    if label:
        units.append(label)
    return " ".join(pv_unit(x, M) for x in units)


def heading(text):
    """9-01 SECTION_HEAD (Pavattivāro, Uppādavāro …), else 10-01 heading (2-01 time / order headings)."""
    if text in DY.SECTION_HEAD:
        return DY.SECTION_HEAD[text]
    return I.heading(text)


def tr_line(p, pavatti, M=None, fixed=None):
    """One Pāli line. pavatti=False: 10-01's translator (paṇṇattivāra); True: this module (asserted equal to 10-01 /
    3-02 wherever those parse the line)."""
    M = M or M_IND
    if not pavatti:
        return I.tr_line(p, M, fixed)
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if "[" in body:
        raise ValueError(f"variant bracket not handled: {p!r}")
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {heading(text)}"
    elif fixed and body in fixed:
        out = fixed[body]
    else:
        out = pv_line(body, M)
        for name, f in (("10-01", lambda: I.line_vi(body, M)),
                        ("3-01/3-02", lambda: A2.line_vi(body, M, PLANES))):
            try:
                old = f()
            except (ValueError, KeyError, AssertionError):
                continue
            if old != out:
                raise AssertionError(f"{name} differs:\n{old}\n{out}")
            CHECKED[name] += 1
    return f"{out} {bid}" if bid else out


def build(name, M=None, fixed=None):
    segs, pavatti = [], False
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            if re.match(r"#+ Pavattivāro ", ln):
                pavatti = True
            out.append(tr_line(ln, pavatti, M, fixed))
        segs.append(out)
    return segs


# ===============================================================================================================
# 4. Checks
# ===============================================================================================================
REUSED = [   # (Pāli, Vietnamese, book): asserted to occur in that book's Vietnamese rails
    ("sahetukānaṃ ñāṇasampayuttānaṃ (^2-1012 block)", "có gốc rễ, gắn liền với hiểu biết", "2"),
    ("sahetukānaṃ ñāṇavippayuttānaṃ", "có gốc rễ, không gắn liền với hiểu biết", "2"),
    ("ahetukānaṃ", "không có gốc rễ", "2"),
]
TERMBASE_USED = [   # pi-6 termbase entries used verbatim («Pāli: {…: Vietnamese}»)
    ("ñāṇavippayuttānaṃ", IND_ATTRS["ñāṇavippayuttānaṃ"]), ("ñāṇasampayuttānaṃ", IND_ATTRS["ñāṇasampayuttānaṃ"]),
    ("itthīnaṃ", SEX["itthīnaṃ"]), ("purisānaṃ", SEX["purisānaṃ"]),
    ("somanassena", FEEL["somanassena"]), ("upekkhāya", FEEL["upekkhāya"]),
    ("upapajjantīnaṃ", B.PARTICIPLES["upapajjantānaṃ"][0]), ("upapajjantānaṃ", B.PARTICIPLES["upapajjantānaṃ"][0]),
    ("Sacittakānaṃ", A.AY_ATTRS["sacittakānaṃ"]), ("Acittakānaṃ", A.AY_ATTRS["acittakānaṃ"]),
    ("pavatte", "đời sống"), ("Itarāsaṃ", "người khác"),
]


def termbase_text():
    return unicodedata.normalize("NFC", TERMBASE.read_text(encoding="utf-8"))


def check_termbase():
    tb = termbase_text()
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(rf"^{re.escape(p)}: {{.*: {re.escape(v)}}}$", tb, re.M)]
    for w, vi in sorted(MINDS_SEEN):   # every faculty kind of mind built = its termbase entry
        if not re.search(rf"^{re.escape(w)} uppādakkhaṇe: {{.*: khoảnh khắc sinh khởi của {re.escape(vi)}}}$", tb, re.M):
            bad.append((w, vi))
    assert not bad, "termbase entries not matched: " + repr(bad)


def check_reused():
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)


def check_frames():
    """The shared strings are the setters': 3-01 groups without the new words; 9-01 moment / pavatte shape."""
    for hd in ("Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ", "Acittakānaṃ upapajjantānaṃ", "Sacakkhukānaṃ upapajjantānaṃ"):
        assert ind_persons(hd) == A.ay_persons(hd), hd
    assert ind_group(None, [A.AY_ATTRS["sacakkhukānaṃ"]], "upapajjantānaṃ") == A.ay_group(
        None, ["sacakkhukānaṃ"], "upapajjantānaṃ")
    assert ind_answer_head("Sacakkhukānaṃ upapajjantānaṃ", "tesaṃ") == A.answer_head("Sacakkhukānaṃ upapajjantānaṃ",
                                                                                     "tesaṃ")
    assert faculty_mind_gen("cittassa") == D8.MIND
    assert faculty_mind_gen("kusalavippayuttacittassa") == DY.mind_gen("kusalavippayuttacittassa")
    assert DY.answer_head("Sabbesaṃ upapajjantānaṃ pavatte kusalavippayuttacittassa uppādakkhaṇe", "tesaṃ") == cap(
        ", ".join([f"{C.AT} {B.persons('Sabbesaṃ upapajjantānaṃ')}", DY.PAVATTE,
                   DY.moment_vi("uppādakkhaṇe", DY.mind_gen("kusalavippayuttacittassa"))]))
    assert ind_answer_head("Ye arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ") == A2.answer_head(
        "Ye arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ", PLANES)
    assert B.L[PRON_FEM["tāsaṃ"]] == f"{C.AT} {C.pron_vi('tesaṃ')}"
    assert FAC_MIND["somanassa"] == "niềm vui"
    assert sex_vi("itthīnaṃ") == "làm người nữ" and sex_vi("purisānaṃ", True) == "không làm người nam"


# ===============================================================================================================
# 5. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = M_IND
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    out += [f"# pi-6 rails {N} (Indriyayamaka 2): person heads of the Indriya pavattivāra (for 10-03 … 10-13)", "",
            "Builder: build_rails_10-02_vi.py (import with importlib). Paṇṇattivāra lines: 10-01's tr_line unchanged. "
            "Pavattivāra: 2-01 b_q / b_noca / b_both, 3-01 question_vi / split_mv / AY_ATTRS / ATTR_JOIN, 3-02 "
            "ay_persons / answer_head, 9-01 PAVATTE / moment_vi / mind_gen / SECTION_HEAD, 10-01 INDRIYA / ind_mulaka, "
            "all READ-ONLY; every pavatti line that 10-01 or 3-02 can also parse is asserted byte-identical. Exposed: "
            "`IND_ATTRS`, `PRE_ATTRS`, `SEX`, `REBORN_AS`, `NOT`, `sex_vi`, `FEEL`, `FEEL_JOIN`, `feel_vi`, `PART_FEM`, "
            "`REBIRTH_PARTS`, `QUANT_FEM`, `PRON_FEM`, `ind_group`, `ind_persons`, `FAC_MIND`, `SAMPAYUTTA`, "
            "`VIPPAYUTTA`, `faculty_mind_gen`, `ind_head_parts`, `ind_answer_head`, `pv_sentence`, `pv_unit`, "
            "`pv_line`, `heading`, `tr_line`, `build`. Format: Pāli = tiếng Việt.", ""]
    h("Headings")
    for t in ("Suddhindriyamūlacakkavāro", "Pavattivāro", "Uppādavāro", "(1) Paccuppannavāro", "(Ka) anulomapuggalo",
              "(Kha) anulomaokāso"):
        row(t, heading(t))
    row("Paṇṇattiniddesavāro.", B.CLOSING["Paṇṇattiniddesavāro."])
    h("Person words new here")
    for k, v in IND_ATTRS.items():
        row(k, f"{B.PERSON} {v} … (attribute, joined «{A.ATTR_JOIN}» as 3-01)")
    for k in SEX:
        row(f"{k} … upapajjantānaṃ / na {k} … upapajjantānaṃ",
            f"{B.PERSON} … đang tái sinh {sex_vi(k)} / … đang tái sinh {sex_vi(k, True)}")
    for k in FEEL:
        row(f"{k} … upapajjantānaṃ / vinā {k} …", f"… đang tái sinh {feel_vi(k)} / … đang tái sinh {feel_vi(k, True)}")
    row("upapajjantīnaṃ (feminine) / Itarāsaṃ / tāsaṃ", f"{B.PARTICIPLES['upapajjantānaṃ'][0]} / = Itaresaṃ / "
        f"= tesaṃ «{C.pron_vi('tesaṃ')}»")
    row("order inside a group", "«những người» + attributes (Pāli order, «, ») + «đang tái sinh» + «làm người nữ / nam» "
        "+ («, » after a sex word) the feeling; the Pāli order of sex / feeling words does not change the Vietnamese")
    for hd in ("Sacakkhukānaṃ na itthīnaṃ upapajjantānaṃ", "Sacakkhukānaṃ itthīnaṃ upapajjantīnaṃ",
               "Itthīnaṃ acakkhukānaṃ upapajjantīnaṃ", "Na purisānaṃ upapajjantānaṃ",
               "Sacakkhukānaṃ vinā somanassena upapajjantānaṃ", "Somanassena aghānakānaṃ upapajjantānaṃ",
               "Upekkhāya sacakkhukānaṃ upapajjantānaṃ", "Sacakkhukānaṃ ahetukānaṃ upapajjantānaṃ",
               "Sahetukānaṃ na itthīnaṃ upapajjantānaṃ", "Ñāṇasampayuttānaṃ acakkhukānaṃ upapajjantānaṃ",
               "Itthīnaṃ vinā somanassena upapajjantīnaṃ", "Somanassena na itthīnaṃ upapajjantānaṃ",
               "Upekkhāya itthīnaṃ upapajjantīnaṃ", "Sacittakānaṃ na purisānaṃ upapajjantānaṃ"):
        row(hd, ind_persons(hd))
    h("Kinds of mind (termbase; two-part «tâm <A> và <B>», coordinator)")
    for w in ("somanassavippayuttacittassa", "upekkhāsampayuttacittassa", "ñāṇavippayuttacittassa",
              "somanassasampayuttasaddhāvippayuttacittassa", "saddhāsampayuttaupekkhāvippayuttacittassa",
              "ñāṇasampayuttasomanassasampayuttacittassa"):
        row(f"{w} uppādakkhaṇe", DY.moment_vi("uppādakkhaṇe", faculty_mind_gen(w)))
    h("Answer heads (9-01 shape: parts joined «, »)")
    for hd in ("Vinā somanassena upapajjantānaṃ pavatte somanassavippayuttacittassa uppādakkhaṇe",
               "Sacittakānaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe",
               "Pavatte somanassasampayuttasaddhāvippayuttacittassa uppādakkhaṇe",
               "Ñāṇasampayuttānaṃ vinā somanassena upapajjantānaṃ pavatte "
               "ñāṇasampayuttasomanassavippayuttacittassa uppādakkhaṇe"):
        row(f"{hd} tesaṃ …", f"{ind_answer_head(hd, 'tesaṃ')}, {C.THEN} {B.L['tesaṃ']} …")
    for hd in ("Asaññasatte arūpe", "Rūpāvacare arūpāvacare", "Catuvokāre pañcavokāre"):
        row(f"{hd} tattha …", f"{ind_answer_head(hd, 'tattha')}, {C.THEN} {B.L['tattha']} …")
    h("Sample lines")
    for s in ("Sacakkhukānaṃ na itthīnaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ itthindriyaṃ "
              "uppajjati. Sacakkhukānaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ cakkhundriyañca uppajjati itthindriyañca uppajjati.",
              "Somanassena na itthīnaṃ upapajjantānaṃ tesaṃ somanassindriyaṃ uppajjati, no ca tesaṃ itthindriyaṃ "
              "uppajjati.",
              "Vinā somanassena upapajjantānaṃ pavatte somanassavippayuttacittassa uppādakkhaṇe tesaṃ jīvitindriyaṃ "
              "uppajjati, no ca tesaṃ somanassindriyaṃ uppajjati.",
              "Pavatte somanassasampayuttasaddhāvippayuttacittassa uppādakkhaṇe tesaṃ somanassindriyaṃ uppajjati, no ca "
              "tesaṃ saddhindriyaṃ uppajjati.",
              "(Ka) yattha cakkhundriyaṃ uppajjati tattha itthindriyaṃ…pe… purisindriyaṃ uppajjatīti?",
              "Yattha cakkhundriyaṃ uppajjati tattha saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ uppajjatīti? Āmantā.",
              "(Kha) yattha vā pana purisindriyaṃ uppajjati tattha itthindriyaṃ uppajjatīti? Āmantā …pe….",
              "Asaññasatte arūpe tattha jīvitindriyaṃ uppajjati, no ca tattha cakkhundriyaṃ uppajjati. Pañcavokāre "
              "tattha jīvitindriyañca uppajjati cakkhundriyañca uppajjati.",
              "(Ka) yassa itthindriyaṃ uppajjati tassa purisindriyaṃ uppajjatīti? No."):
        row(s, pv_line(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- itthīnaṃ / purisānaṃ upapajjantānaṃ «… đang tái sinh làm người nữ / người nam» (user); the negative "
        "«na itthīnaṃ upapajjantānaṃ» has no decision: «… đang tái sinh không làm người nữ». Please confirm.",
        "- vinā somanassena / vinā upekkhāya: no vinā entry; built on the termbase somanassena «có niềm vui đi kèm»: "
        "«không có niềm vui đi kèm» / «không có sự bình thản đi kèm».",
        "- somanassena / upekkhāya placed after «đang tái sinh» (the termbase sense: the feeling that accompanies the "
        "rebirth), after a sex word with «, »: «những người đang tái sinh làm người nữ, có niềm vui đi kèm».",
        "- sahetukānaṃ / ahetukānaṃ (persons): no genitive-plural entry; pi-2 18-dhammahadayavibhango has the identical "
        "Pāli «có gốc rễ» / «không có gốc rễ» (siblings Sahetukaṃ / Ahetukaṃ); used as 3-01 attributes.",
        "- ñāṇa in the kinds of mind «hiểu biết» (termbase ñāṇasampayutta «gắn liền với hiểu biết», user).",
        "- tāsaṃ (feminine of tesaṃ): «những người ấy» (= tesaṃ; Vietnamese has no gender).",
        "- Not set (the builder raises): sex / feeling words with cavantānaṃ / cavantīnaṃ or with a plane in the same "
        "group; a later chapter that meets them must decide the shape.",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-142 «(Kha) indriyaṃ saddhindriyanti?» (singular indriyaṃ; the parallels have indriyā): «(b) Năng lực có "
        "phải là năng lực niềm tin không?».",
        "- ^6-10-169 / ^6-10-180 question and partial answer on one line «(Ka) na mano na indriyanti? Manaṃ ṭhapetvā …» "
        "(the parallels have two lines): kept on one line.",
        "- ^6-10-146 the last answer is split over two lines: kept.",
        "- ^6-10-163 / ^6-10-185 the aññātāvī series ends with aññindriyaṃ (not aññātāvindriyaṃ): as written.",
        "- ^6-10-186 (Kha) somanassindriyaṃ … cakkhundriyaṃ «Āmantā.» (the ghāna parallel ^6-10-187 has a partial "
        "answer): as written. ^6-10-186 last answer «Sacakkhukānaṃ upapajjantānaṃ …» (no sacittakānaṃ): as written.",
        "- ^6-10-191 / ^6-10-192 «Pavatte …cittassa uppādakkhaṇe tesaṃ …» (a head with no person group): «Trong đời "
        "sống, vào khoảnh khắc …, thì ở những người ấy …».",
        "- ^6-10-188, ^6-10-189 «Somanassena na itthīnaṃ upapajjantānaṃ tesaṃ …» (masculine) beside «… itthīnaṃ "
        "upapajjantīnaṃ tāsaṃ …» (feminine): same Vietnamese participle and pronoun.",
        "- ^6-10-195, ^6-10-196, ^6-10-198 … unlabelled questions «Yattha …» among labelled ones: kept unlabelled.",
        "- ^6-10-198, ^6-10-199 a sentence and the next question (and answer) on one line: kept on one line.",
        "- «Āmantā …pe….» (space before the cut) = «Đúng vậy …» (10-01).",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    A.check_reused()
    I.check_reused()
    I.check_frames()
    check_reused()
    check_frames()
    segs = build(CH)
    check_termbase()
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("pavatti lines checked equal:", CHECKED, "; heads built:", len(HEADS_SEEN), "; minds:", len(MINDS_SEEN))


if __name__ == "__main__":
    main()
