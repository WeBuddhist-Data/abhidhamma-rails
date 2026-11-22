"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 10-12 (Indriyayamaka 12: uppādavāra, (6) atītānāgatavāro (past +
future), (Ka) … (Ca), the closing «Pavattivāro niṭṭhito.» and the heading «Pariññāvāro»).

Setters (all imported READ-ONLY with importlib; every shared string comes from their functions):
  build_rails_10-11_vi  (J11) head_parts11 / person_items11 / ye_head11 (person runs, Ye heads, final minds, samaṅgī
                              persons, the anantarā group: 10-10 / 10-05 / 6-01 / 9-01 shapes, asserted there)
  build_rails_10-10_vi  (J10) coordinator-accepted frames (pacchima_gen, samangi_person, that_mind_moment_x,
                              ye_head, answer_head, tr_line: asserted equal wherever they parse)
  build_rails_10-05_vi  (J5)  the time phrase "Suddhāvāsānaṃ dutiye citte vattamāne" (head_parts12: «Ở chúng sinh
                              trong cõi Tịnh Cư, khi tâm thứ hai đang diễn ra»), anantara_group «… ngay sau tâm này»
                              (6-01 smooth form), ye_clause12 (eteneva bhāvena, katici bhave dassetvā), answer_head12
  build_rails_10-09_vi  (J9)  answer_head13 / pv_sentence13 / tr_line (asserted equal wherever they parse)
  build_rails_10-08_vi  (J8)  question12 (whole and cut pair questions, separate na), CUT_AFTER_Q, answer_head12,
                              tr_line; through it 10-04 … 10-01, 9-01, 3-02, 3-01, 2-01, 7-01, 8, 5-01
  build_rails_2-02_vi   (D2)  HEADINGS["Pariññāvāro"] «Mục về sự hiểu biết trọn vẹn» (= sample LATER_HEADINGS)
  build_rails_2-01_vi   (B)   CLOSING["Pavattivāro niṭṭhito."], SHORT (Uppajjittha. / Uppajjissati. / Natthi. /
                              Āmantā.), b_noca / b_both, VERB_TABLE (through 10-03 verb: «đã sinh khởi / chưa từng sinh
                              khởi», «sẽ sinh khởi / sẽ không sinh khởi»; after no ca «đã từng sinh khởi», «vẫn sẽ sinh
                              khởi»)

New here (named constants; nothing else depends on them yet):
  TIME_PHRASE / time_part      "<ordinal> citte vattamāne" «khi tâm thứ <n> đang diễn ra» (10-05 head_parts12 string,
                               asserted)
  head_parts / answer_head     10-11 head_parts11 around the time phrase (parts joined «, », 9-01 shape)
  LOCP12 / NOCA_RE / BOTH_RE / pv_sentence   person (tesaṃ) and person-place (tesaṃ tattha) answers in one parser
  LABEL_RE / label_unit        "(Xindriyamūlakaṃ)…pe…." «(Phần dựa trên năng lực X)…» (10-01 ind_mulaka + S.PE)
  HEAD_EXTRA / heading         Pariññāvāro (2-02), else 10-02 heading
  unit / line / tr_line / build
A line, unit or word the parsers cannot place raises ValueError (no silent fallback). Importing writes nothing.

usage: python -I -X utf8 -B build_rails_10-12_vi.py   (probe: … build_rails_10-12_vi.py probe)
"""
import importlib
import re
import sys
import unicodedata

RAILS_DIR = r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails"
if RAILS_DIR not in sys.path:
    sys.path.insert(0, RAILS_DIR)
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)
J11 = importlib.import_module("build_rails_10-11_vi")  # READ-ONLY: person runs, Ye heads, final minds (10-10 frames)
J10 = importlib.import_module("build_rails_10-10_vi")  # READ-ONLY: coordinator-accepted frames
J5 = importlib.import_module("build_rails_10-05_vi")   # READ-ONLY: time phrase, anantarā group, ye clauses
J9 = importlib.import_module("build_rails_10-09_vi")   # READ-ONLY: parallel uppādavāra chapter (asserted)
J8 = importlib.import_module("build_rails_10-08_vi")   # READ-ONLY: question12, CUT_AFTER_Q
assert J11.J8 is J8 and J11.J5 is J5 and J11.J10 is J10 and J10.J8 is J8 and J9.M8 is J8 and J9.M5 is J5
assert J9.J10 is J10
I4, I3, I2, I, A, A2, B, C, DY, D8 = J8.I4, J8.I3, J8.I2, J8.I, J8.A, J8.A2, J8.B, J8.C, J8.DY, J8.D8
Q6, A3, P92, D2 = J11.Q6, J11.A3, J11.P92, J11.D2
assert J5.I2 is I2 and J5.DY is DY and J5.B is B and J5.D8 is D8 and J5.S6 is Q6 and J5.A3 is A3

cap = S.cap
lc = I2.lc
CH = "10-12-indriyayamaka.md"
N = "10-12"
NOTES_MD = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/notes-rails-{N}.md"
ADH_DIR = S.ROOT / f"0-INBOX/temp/pipeline/pi-6-vi-ai/rails/adh-{N}"
M_IND = I.INDRIYA
PLANES = A.PLANES_AY
CHECKED = {"10-11 head": 0, "10-10 head": 0, "10-09 head": 0, "10-08 head": 0, "10-05 head": 0,
           "10-11 sentence": 0, "10-10 sentence": 0, "10-09 sentence": 0, "10-08 sentence": 0, "10-05 sentence": 0,
           "10-11 line": 0, "10-10 line": 0, "10-09 line": 0, "10-08 line": 0, "10-05 line": 0}
HEADS_SEEN = {}          # Pāli head -> Vietnamese
NEW_HEADS = {}           # heads no setter parses
OWN_READING = {}         # head -> (setter, string): read differently on purpose (10-11's one-group rule)
SETTER_FAIL = {}         # a setter's own internal assertion failed on an input (listed, not used)
SLIPS = {}               # none found in this chapter (Pāli as written)

# ===============================================================================================================
# 1. Time phrase "<ordinal> citte vattamāne" (10-05 head_parts12; 9-01 WHILE / ORDINAL / OCCURRING)
# ===============================================================================================================
TIME_PHRASE = ["citte", "vattamāne"]


def time_part(ordinal):
    """dutiye citte vattamāne «khi tâm thứ hai đang diễn ra» (the very string of 10-05 head_parts12)."""
    if lc(ordinal) not in DY.ORDINAL:
        raise ValueError(f"unknown ordinal {ordinal!r}")
    return f"{DY.WHILE} {D8.MIND} {DY.ORDINAL[lc(ordinal)]} {DY.OCCURRING}"


# ===============================================================================================================
# 2. Answer heads: 10-11 head_parts11 / ye_head11 (10-10 frames) + the time phrase as its own part
# ===============================================================================================================
def head_parts(head):
    """Parts joined «, » (9-01 shape); a person run after the time phrase keeps its own «ở» (coordinator)."""
    toks = head.split()
    low = [lc(t) for t in toks]
    parts, own, chunk, i = [], False, [], 0

    def flush():
        nonlocal own
        if chunk:
            p, o = J11.head_parts11(" ".join(chunk))
            parts.extend(p)
            own = own or o
            chunk.clear()

    while i < len(toks):
        if low[i] in DY.ORDINAL and low[i + 1:i + 3] == TIME_PHRASE:
            flush()
            parts.append(time_part(toks[i]))
            i += 3
            continue
        chunk.append(toks[i])
        i += 1
    flush()
    if not parts:
        raise ValueError(f"empty answer head {head!r}")
    return parts, own


ITARA = ("itaresaṃ",)                     # «Ở những người khác» / «Ở chúng sinh khác trong cõi X» (10-10 answer_head)


def answer_head(head, loc):
    if loc == "tattha":
        return B.place_head(head, PLANES)
    if J11.is_ye_head(head):
        out, own = J11.ye_head11(head), head in J11.OWN_READING
    elif lc(head.split()[0]) in ITARA:
        out, own = J10.answer_head(head, loc), False       # Itaresaṃ [plane-beings] (10-10 → 3-02 persons strings)
    else:
        parts, own = head_parts(head)
        out = cap(", ".join(parts))
    parsed = False
    for name, f in (("10-11 head", lambda: J11.answer_head11(head, loc)),
                    ("10-10 head", lambda: J10.answer_head(head, loc)),
                    ("10-09 head", lambda: J9.answer_head13(head, loc)),
                    ("10-08 head", lambda: J8.answer_head12(head, loc)),
                    ("10-05 head", lambda: J5.answer_head12(head, loc))):
        try:
            old = f()
        except (ValueError, KeyError):
            continue
        except AssertionError as e:            # the setter's own cross-check fails on this head: listed, skipped
            SETTER_FAIL.setdefault(head, (name, str(e)[:200]))
            continue
        parsed = True
        if own:
            if old != out:
                OWN_READING[head] = (name, old)
            continue
        assert old == out, (name, head, old, out)
        CHECKED[name] += 1
    if not parsed:
        NEW_HEADS.setdefault(head, out)
    HEADS_SEEN[head] = out
    return out


# ===============================================================================================================
# 3. Sentences (family B, 2-01 b_noca / b_both): person answers "tesaṃ" and person-place answers "tesaṃ tattha"
# ===============================================================================================================
LOCP12 = r"(tesaṃ tattha|tāsaṃ tattha|tesaṃ|tāsaṃ)"
_MEM = r"(?=\S+ndriya(?:ṃ|ñca) )"              # the pronoun that opens the member clause (10-09)
NOCA_RE = re.compile(r"(.+?) " + LOCP12 + " " + _MEM + r"(.+?), no ca \2 (.+?)\.")
BOTH_RE = re.compile(r"(.+?) " + LOCP12 + " " + _MEM + r"(\S+?ñca) ((?:na )?\S+) (\S+?ñca) ((?:na )?\S+)\.")


def pv_sentence(s, M=None):
    M = M or M_IND
    if m := NOCA_RE.fullmatch(s):
        head, loc, c1, c2 = m.groups()
        a, v1 = I3.split_mv(c1, M)
        b, v2 = I3.split_mv(c2, M)
        out = B.b_noca(answer_head(head, loc), I2.PRON_FEM.get(loc, loc), a, v1, b, v2)
    elif m := BOTH_RE.fullmatch(s):
        head, loc, c1, v1, c2, v2 = m.groups()
        out = B.b_both(answer_head(head, loc), I2.PRON_FEM.get(loc, loc), M.subj(c1), I3.verb(v1), M.subj(c2),
                       I3.verb(v2))
    else:
        return None
    for name, f in (("10-11 sentence", J11.pv_sentence11), ("10-10 sentence", J10.pv_sentence),
                    ("10-09 sentence", J9.pv_sentence13), ("10-08 sentence", J8.pv_sentence12),
                    ("10-05 sentence", J5.pv_sentence12)):
        try:
            old = f(s, M)
        except (ValueError, KeyError):
            continue
        except AssertionError as e:
            SETTER_FAIL.setdefault(s[:80], (name, str(e)[:200]))
            continue
        if old is None:
            continue
        if old != out and any(h in s for h in OWN_READING):
            continue
        assert old == out, (name, s, old, out)
        CHECKED[name] += 1
    return out


# ===============================================================================================================
# 4. Units, lines, headings
# ===============================================================================================================
LABEL_RE = re.compile(r"(\(\w+mūlakaṃ\))…pe…\.")       # "(Paññindriyamūlakaṃ)…pe…." (end of the pavattivāra)


def label_unit(u, M=None):
    """«(Phần dựa trên năng lực trí tuệ)…» (10-01 ind_mulaka + "…pe…" → "…")."""
    m = LABEL_RE.fullmatch(u)
    if not m:
        return None
    lab = I.ind_mulaka(m.group(1), M or M_IND)
    if lab is None:
        raise ValueError(f"unknown label {u!r}")
    return lab + S.PE


def unit(u, M=None):
    M = M or M_IND
    if (lab := I.ind_mulaka(u, M)) is not None:
        return lab
    if (lab := label_unit(u, M)) is not None:
        return lab
    if u.endswith(J8.CUT_AFTER_Q):
        return J8.question12(u[:-len(J8.CUT_AFTER_Q)], M) + S.PE
    if u.endswith("?"):
        return J8.question12(u[:-1], M)
    if u in B.SHORT:
        return B.SHORT[u]
    if u in B.CLOSING:
        return B.CLOSING[u]
    if "…" in u:
        raise ValueError(f"cut not set in this chapter: {u!r}")
    if (out := pv_sentence(u, M)) is not None:
        return out
    raise ValueError(f"unknown unit {u!r}")


def line(body, M=None):
    body, label = body.strip(), None
    if m := re.fullmatch(r"(.+?) (\(\w+mūlakaṃ\)(?:…pe…)?\.?)", body):    # trailing label (10-02), with a cut here
        body, label = m.group(1), m.group(2)
    units = [x for x in re.split(r"(?<=[.?]) (?=\S)", body) if x]
    if label:
        units.append(label)
    return " ".join(unit(x, M) for x in units)


HEAD_EXTRA = {"Pariññāvāro": D2.HEADINGS["Pariññāvāro"]}       # «Mục về sự hiểu biết trọn vẹn» (2-02)
assert dict((k, v) for k, v, *_ in S.LATER_HEADINGS)["Pariññāvāro"] == HEAD_EXTRA["Pariññāvāro"]   # approved sample


def heading(text):
    if text in HEAD_EXTRA:
        return HEAD_EXTRA[text]
    return I2.heading(text)


def tr_line(p, M=None, fixed=None):
    M = M or M_IND
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
        out = line(body, M)
    full = f"{out} {bid}" if bid else out
    for name, f in (("10-11 line", J11.tr_line), ("10-10 line", J10.tr_line), ("10-09 line", J9.tr_line),
                    ("10-08 line", J8.tr_line), ("10-05 line", J5.tr_line)):
        try:
            old = f(p, M, fixed)
        except (ValueError, KeyError):
            continue
        except AssertionError as e:
            SETTER_FAIL.setdefault(p[:80], (name, str(e)[:200]))
            continue
        if old != full and any(h in p for h in OWN_READING):
            continue
        assert old == full, (name, p, old, full)
        CHECKED[name] += 1
    return full


def build(name, M=None, fixed=None):
    return [[tr_line(ln, M, fixed) for ln in seg] for seg in S.segments_of(name)]


# ===============================================================================================================
# 5. Checks
# ===============================================================================================================
TERMBASE_USED = [   # pi-6 termbase entries used verbatim (10-13's looser match: «Pāli: {…: Vietnamese…}»)
    ("Pariññāvāro", "mục về sự hiểu biết trọn vẹn"),
    ("Pacchimacittassa", J10.pacchima_gen("Pacchimacittassa")),
    ("upekkhāsampayuttapacchimacittaṃ", J5.pacchima_mind("upekkhāsampayuttapacchimacittaṃ")),
    ("somanassasampayuttapacchimacittaṃ", J5.pacchima_mind("somanassasampayuttapacchimacittaṃ")),
    ("purisā", J5.YE_NOUN["purisā"]), ("itthiyo", J5.YE_NOUN["itthiyo"]),
    ("sacakkhukā", A.AY_ATTRS["sacakkhukānaṃ"]), ("anantarā", DY.ANANTARA),
    ("Pañcavokāre", PLANES["pañcavokār"][0]), ("Kāmāvacare", PLANES["kāmāvacar"][0]),
]


def check_termbase():
    tb = I2.termbase_text()
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M | re.I)]
    assert not bad, "termbase entries not matched: " + repr(bad)
    J10.check_termbase()
    J11.check_termbase()


def check_frames():
    hd = "Suddhāvāsānaṃ dutiye citte vattamāne asaññasattānaṃ"          # 10-05's own head (identical Pāli shape)
    assert answer_head(hd, "tesaṃ tattha") == J5.answer_head12(hd, "tesaṃ tattha"), hd
    assert answer_head("Suddhāvāsānaṃ dutiye citte vattamāne", "tesaṃ tattha") == \
        f"{cap(C.AT)} {PLANES['suddhāvās'][1]}, {time_part('dutiye')}"
    hd = "Pacchimacittasamaṅgīnaṃ yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati"
    assert answer_head(hd, "tesaṃ") == J5.answer_head12(hd, "tesaṃ"), hd   # 10-05 notes: built for 10-12
    assert J5.anantara_group("upekkhāsampayuttapacchimacittaṃ", "uppajjissati").endswith(
        f" {DY.ANANTARA} {DY.THIS_MIND}")                                    # 6-01 smooth form, not «Vào tâm mà …»
    assert Q6.anantara_group(None, False).endswith(f" {DY.ANANTARA} {DY.THIS_MIND}")
    assert I3.verb("uppajjittha")[0] == "đã sinh khởi" and I3.verb("na uppajjittha")[0] == "chưa từng sinh khởi"
    assert B.noca_vi("B", I3.verb("na uppajjittha")) == "B đã từng sinh khởi"   # coordinator: past after no ca
    assert B.noca_vi("B", I3.verb("na uppajjissati")) == "B vẫn sẽ sinh khởi"
    assert B.SHORT["Uppajjittha."] == "Đã sinh khởi." and B.SHORT["Uppajjissati."] == "Sẽ sinh khởi."
    assert B.CLOSING["Pavattivāro niṭṭhito."] == "Mục về sự diễn tiến đã hoàn tất."
    assert heading("(6) Atītānāgatavāro") == "(6) Mục về quá khứ và tương lai"
    assert label_unit("(Paññindriyamūlakaṃ)…pe….") == "(Phần dựa trên năng lực trí tuệ)…"


# ===============================================================================================================
# 6. Notes file (Pāli = tiếng Việt)
# ===============================================================================================================
def notes():
    M = M_IND
    out = []

    def row(p, v):
        out.append(f"{p} = {v}")

    def h(t):
        out.extend(["", f"## {t}", ""])

    def hrow(hd, loc="tesaṃ"):
        row(f"{hd} {loc} …", f"{answer_head(hd, loc)}, {C.THEN} {B.L[I2.PRON_FEM.get(loc, loc)]} …")

    out += [f"# pi-6 rails {N} (Indriyayamaka 12): (6) atītānāgatavāro, Pavattivāro niṭṭhito, Pariññāvāro", "",
            "Builder: build_rails_10-12_vi.py (import with importlib). Setters: build_rails_10-11_vi (head_parts11, "
            "ye_head11, person_items11), build_rails_10-10_vi (pacchima_gen, samangi_person, that_mind_moment_x, "
            "ye_head, answer_head, tr_line), build_rails_10-05_vi (time phrase, anantara_group = 6-01 smooth form, "
            "ye_clause12, answer_head12), build_rails_10-09_vi (answer_head13, pv_sentence13, tr_line), "
            "build_rails_10-08_vi (question12, CUT_AFTER_Q; through it 10-04 … 10-01, 9-01, 3-02, 3-01, 2-01, 7-01, 8, "
            "5-01), build_rails_2-02_vi (HEADINGS), build_rails_2-01_vi (CLOSING, SHORT, b_noca, b_both); all "
            "READ-ONLY. Every line, sentence and head that 10-11 / 10-10 / 10-09 / 10-08 / 10-05 parse is asserted "
            "byte-identical. Exposed: `TIME_PHRASE`, `time_part`, `head_parts`, `answer_head`, `LOCP12`, `NOCA_RE`, "
            "`BOTH_RE`, `pv_sentence`, `LABEL_RE`, `label_unit`, `unit`, `line`, `HEAD_EXTRA`, `heading`, `tr_line`, "
            "`build`. Format: Pāli = tiếng Việt.", ""]
    h("Headings")
    for t in ("(6) Atītānāgatavāro", "(Ka) anulomapuggalo", "(Kha) anulomaokāso", "(Ga) anulomapuggalokāsā",
              "(Gha) paccanīkapuggalo", "(Ṅa) paccanīkaokāso", "(Ca) paccanīkapuggalokāsā", "Pariññāvāro"):
        row(t, heading(t))
    h("Verbs (2-01 VERB_TABLE via 10-03; coordinator: past after no ca «đã từng», future «vẫn sẽ»)")
    for v in ("uppajjittha", "uppajjissati", "na uppajjittha", "na uppajjissati"):
        row(v, I3.verb(v)[0])
    for v in ("uppajjittha", "uppajjissati", "na uppajjittha", "na uppajjissati"):
        row(f"no ca tesaṃ tattha B {v}", "nhưng ở những người ấy, ở nơi ấy " + (
            B.noca_vi("B", I3.verb(v)) if v.startswith("na ") else f"không có B {I3.verb(v)[0]}"))
    for u in ("Uppajjittha.", "Uppajjissati.", "Natthi.", "Āmantā."):
        row(u, B.SHORT[u])
    h("Questions (10-08 question12)")
    for q in ("(Ka) yassa cakkhundriyaṃ uppajjittha tassa sotindriyaṃ uppajjissatīti",
              "(Kha) yassa vā pana sotindriyaṃ uppajjissati tassa cakkhundriyaṃ uppajjitthāti",
              "Yassa cakkhundriyaṃ uppajjittha tassa saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ uppajjissatīti",
              "(Ka) yassa yattha cakkhundriyaṃ na uppajjittha tassa tattha sotindriyaṃ na uppajjissatīti",
              "Yassa ghānindriyaṃ…pe… itthindriyaṃ… purisindriyaṃ… jīvitindriyaṃ… somanassindriyaṃ… "
              "upekkhindriyaṃ… saddhindriyaṃ… paññindriyaṃ na uppajjittha tassa manindriyaṃ na uppajjissatīti"):
        row(q + "?", J8.question12(q, M))
    row("Yattha cakkhundriyaṃ uppajjittha tattha sotindriyaṃ uppajjissatīti?…Pe….",
        unit("Yattha cakkhundriyaṃ uppajjittha tattha sotindriyaṃ uppajjissatīti?…Pe….", M))
    h("New here: the time phrase in a person-place head (10-05 string), the cut label, the closing")
    hrow("Suddhāvāsānaṃ dutiye citte vattamāne", "tesaṃ tattha")
    row("(Paññindriyamūlakaṃ)…pe….", label_unit("(Paññindriyamūlakaṃ)…pe…."))
    row("Pavattivāro niṭṭhito.", B.CLOSING["Pavattivāro niṭṭhito."])
    h("Heads (setter strings)")
    for hd, loc in (("Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti", "tesaṃ"),
                    ("Pacchimabhavikānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti ye ca purisā "
                     "eteneva bhāvena katici bhave dassetvā parinibbāyissanti", "tesaṃ"),
                    ("Pacchimabhavikānaṃ ye ca upekkhāya upapajjitvā parinibbāyissanti", "tesaṃ"),
                    ("Pacchimacittasamaṅgīnaṃ yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati",
                     "tesaṃ"),
                    ("Pacchimacittasamaṅgīnaṃ yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati "
                     "asaññasattānaṃ", "tesaṃ tattha"),
                    ("Itaresaṃ", "tesaṃ"), ("Itaresaṃ pañcavokārānaṃ", "tesaṃ tattha"),
                    ("Itaresaṃ catuvokārānaṃ pañcavokārānaṃ", "tesaṃ tattha"),
                    ("Kāmāvacare pacchimabhavikānaṃ rūpāvacarānaṃ ye ca purisā eteneva bhāvena katici bhave dassetvā "
                     "parinibbāyissanti", "tesaṃ tattha"),
                    ("Pañcavokāre pacchimabhavikānaṃ ye ca sacakkhukā upekkhāya upapajjitvā parinibbāyissanti",
                     "tesaṃ tattha"),
                    ("Suddhāvāsaṃ upapajjantānaṃ", "tesaṃ tattha"),
                    ("Suddhāvāsānaṃ asaññasattānaṃ arūpānaṃ", "tesaṃ tattha"),
                    ("Suddhāvāsānaṃ arūpe pacchimabhavikānaṃ asaññasattānaṃ", "tesaṃ tattha"),
                    ("Rūpāvacare arūpāvacare pacchimabhavikānaṃ asaññasattānaṃ", "tesaṃ tattha"),
                    ("Rūpāvacare pacchimabhavikānaṃ asaññasattānaṃ arūpānaṃ", "tesaṃ tattha")):
        hrow(hd, loc)
    h("Sample lines")
    for s in ("Pacchimabhavikānaṃ tesaṃ cakkhundriyaṃ uppajjittha, no ca tesaṃ jīvitindriyaṃ uppajjissati.",
              "Itaresaṃ tesaṃ cakkhundriyañca uppajjittha jīvitindriyañca uppajjissati.",
              "Pañcavokāre pacchimabhavikānaṃ tesaṃ tattha sotindriyaṃ na uppajjissati, no ca tesaṃ tattha "
              "cakkhundriyaṃ na uppajjittha.",
              "Suddhāvāsānaṃ dutiye citte vattamāne tesaṃ tattha upekkhindriyaṃ uppajjissati, no ca tesaṃ tattha "
              "somanassindriyaṃ uppajjittha."):
        row(s, line(s, M))
    h("Termbase misfits and gaps (for the coordinator)")
    out += [
        "- No new term. All heads come from 10-11 / 10-10 / 10-05 / 3-02 / 3-03 strings; the only new piece is the "
        f"time phrase in a head without a following person group: «{answer_head('Suddhāvāsānaṃ dutiye citte vattamāne', 'tesaṃ tattha')}» "
        "(10-05's string for the same words, there followed by «, ở chúng sinh Vô Tưởng»).",
        "- (Paññindriyamūlakaṃ)…pe…. at the end of the pavattivāra: the label as 10-01 plus «…» (dash rule: "
        "«…pe…» → «…», never «….»).",
        "- Kept as the setters print it (6-01 open item, «và» inside an inner plane list): «Rūpāvacare arūpāvacare "
        "pacchimabhavikānaṃ asaññasattānaṃ» = «những người thuộc kiếp sống cuối cùng trong cõi hình sắc và cõi không "
        "hình sắc và chúng sinh Vô Tưởng».",
        "",
        "## Pāli as written (reported)",
        "",
        "- ^6-10-430 (Ca) jīvita / somanassa: «… tassa tattha somanassindriyaṃ na uppajjissatīti? Uppajjissati.» and "
        "«… na uppajjitthāti? Uppajjittha.»: short answers as written («Sẽ sinh khởi.» / «Đã sinh khởi.»).",
        "- ^6-10-424 first slot cut with bare «…» after «…pe…» («ghānindriyaṃ…pe… itthindriyaṃ… purisindriyaṃ… …»): "
        "each cut «…» kept at its spot; the pair answers «Natthi.» / «Uppajjittha.» as written.",
        "- ^6-10-434 the label is followed by «…pe….» and «Pavattivāro niṭṭhito.» on its own line: kept as two lines.",
        "- Unlabelled cut-list pairs («Yassa … saddhindriyaṃ…pe… paññindriyaṃ…pe… manindriyaṃ …ti?» / «Yassa vā pana …») "
        "and whole unlabelled sections (^6-10-410, 411, 420, 421, 432, 433) among labelled ones: kept as written.",
        "- ^6-10-413 / ^6-10-425 «Yattha …ti?…Pe….» = «… không?…» (9-01 / 10-08).",
        "- No spelling slips found; no emendation.",
        "",
        "## Setter cross-checks",
        "",
        "- Asserted equal: " + ", ".join(f"{k} {v}" for k, v in CHECKED.items()) + ".",
        f"- Heads no setter parses (built here): {len(NEW_HEADS)}" + (
            ": " + "; ".join(f"«{k}» = «{v}»" for k, v in NEW_HEADS.items()) if NEW_HEADS else "") + ".",
        f"- Read differently from a setter on purpose: {len(OWN_READING)}.",
        f"- Setter self-check failures (skipped, listed): {len(SETTER_FAIL)}"
        + (": " + "; ".join(f"{k[:60]} ({v[0]})" for k, v in SETTER_FAIL.items()) if SETTER_FAIL else "") + ".",
        "",
    ]
    return "\n".join(out)


def main():
    S.check_reused()
    B.check_reused()
    A.check_reused()
    I.check_reused()
    I.check_frames()
    I2.check_reused()
    I2.check_frames()
    I3.check_frames()
    I4.check_frames()
    J8.check_frames()
    J5.check_frames()
    check_frames()
    segs = build(CH)
    check_termbase()
    note_text = notes()
    S.write(CH, segs)
    text = (S.OUT_DIR / CH).read_text(encoding="utf-8")
    ADH_DIR.mkdir(parents=True, exist_ok=True)
    (ADH_DIR / CH).write_text(text, encoding="utf-8", newline="\n")
    print("wrote", ADH_DIR / CH)
    NOTES_MD.write_text(unicodedata.normalize("NFC", note_text), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    print("checked equal:", CHECKED, "; heads:", len(HEADS_SEEN), "; new heads:", len(NEW_HEADS),
          "; own:", len(OWN_READING), "; setter self-check failures:", len(SETTER_FAIL))
    for k, v in SETTER_FAIL.items():
        print("setter fail:", k, v)


def probe(name=CH):
    for seg in S.segments_of(name):
        for ln in seg:
            try:
                print("OK  ", tr_line(ln))
            except Exception as e:  # noqa: BLE001
                print("FAIL", ln[:200], "\n    ", type(e).__name__, str(e)[:400])


if __name__ == "__main__":
    if sys.argv[1:] == ["probe"]:
        probe()
    else:
        main()
