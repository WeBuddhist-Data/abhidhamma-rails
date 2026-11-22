"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-10 (Anusayayamaka: pahīnavāra paṭiloma by place and by person +
place; uppajjanavāra; dhātupucchāvāra).

Imports (all READ-ONLY; importing writes nothing, outputs are written only under `if __name__ == "__main__":`):
  S   build_rails_sample_vi   labels, «…», checks
  C   build_rails_7-01_vi     family C setter: tendencies, shell, heads, connectors, EXACT, headings, MULAKA, write()
  T2  build_rails_7-02_vi     PATILOMA (for «Pahīnavāre paṭilomaṃ.»)
  R7  build_rails_7-07_vi     the Verb class
  P9  build_rails_7-09_vi     PAHINA, nv_vi, sentence, question (the nominative-subject frames, predicate as parameter)
  B   build_rails_2-01_vi     family B: uppajjati / nuppajjati, denied_vi, PARTICIPLES (cavantānaṃ / upapajjantānaṃ)
  T5  build_rails_5-01_vi     VITTHARETABBAM «nên được trình bày chi tiết» (pi-5)
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; P10 = importlib.import_module("build_rails_7-10_vi")

NEW FRAMES (exposed for 7-11 and any chapter with the dhātu-as-plane person):
  UPPAJJ               R7.Verb for uppajjati / nuppajjati in 7-09's frames (2-01 strings: «sinh khởi» /
                       «không sinh khởi», after no ca «vẫn sinh khởi»)
  DHATU / parse_planes() / dhatu_phrase()
                       planes in the ablative (-dhātuyā) or accusative (-dhātuṃ), plain or negated with "na":
                       «cõi dục lạc»; na X «nơi không phải là cõi X»; na X na Y «nơi không phải là cõi X cũng không
                       phải là cõi Y» (the termbase's -dhātumūlakaṃ labels)
  dhatu_person(fr, to) "<fr> cutassa <to> upapajjantassa" = «người đã chết đi khỏi <fr> và đang tái sinh vào <to>»
  dhatu_head(pali)     → («Ở người …, », rest of the Pāli) for 7-11's answers
  KATI_Q / dhatu_question()
                       "kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā?" = «bao nhiêu khuynh
                       hướng tiềm ẩn nằm sẵn, bao nhiêu khuynh hướng tiềm ẩn không nằm sẵn, bao nhiêu khuynh hướng
                       tiềm ẩn phải phân chia?» (pi-2 kati «bao nhiêu <noun> …»)
  DLABEL_RE / dhatu_label()
                       (Kāmadhātumūlakaṃ) … (Nakāmanarūpadhātumūlakaṃ) = «(Phần dựa trên <dhatu_phrase>)»
  vitth()              "(vitthāretabbaṃ)" / "(Vitthāretabbaṃ)." = «(nên được trình bày chi tiết)» / «(Nên …).»
  answers() / line_vi() / tr_line() / build()   (7-09's sentence / question; a capital Pāli sentence start whose
                       Vietnamese would start in lower case is capitalised)
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-10_vi.py
"""
import importlib
import pathlib
import re
import sys
import unicodedata

RAILS_DIR = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-vi-ai\rails")
if str(RAILS_DIR) not in sys.path:
    sys.path.insert(0, str(RAILS_DIR))
import build_rails_sample_vi as S  # noqa: E402  (READ-ONLY)

C = importlib.import_module("build_rails_7-01_vi")    # family C setter (READ-ONLY)
T2 = importlib.import_module("build_rails_7-02_vi")   # READ-ONLY
R7 = importlib.import_module("build_rails_7-07_vi")   # READ-ONLY (Verb)
P9 = importlib.import_module("build_rails_7-09_vi")   # READ-ONLY (PAHINA, nv_vi, sentence, question)
B = importlib.import_module("build_rails_2-01_vi")    # family B setter (READ-ONLY)
T5 = importlib.import_module("build_rails_5-01_vi")   # READ-ONLY (VITTHARETABBAM)

CHAPTER = "7-10-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-10.md"
ADH_DIR = RAILS_DIR / "adh-7-10"
cap = S.cap
PAHINA = P9.PAHINA
SEEN = {"capped": [], "q_dot": [], "bare": [], "digit": [], "vitth": []}


def _lc(t):
    return t[:1].lower() + t[1:]


# ---------------------------------------------------------------------------------------------------------------
# 1. uppajjati in the nominative-subject frames (2-01 VERB_TABLE strings; 7-01 FAMILY_TERMS)
# ---------------------------------------------------------------------------------------------------------------
UPPAJJ = R7.Verb(B.VERB["uppajjati"][0], B.VERB["nuppajjati"][0], B.denied_vi(B.VERB["nuppajjati"][2]),
                 {"uppajjati": (False, 1), "nuppajjati": (True, 1)})
assert UPPAJJ.pos == C.FAMILY_TERMS["uppajjati"] == "sinh khởi"
assert UPPAJJ.neg == "không sinh khởi" and UPPAJJ.still == f"{C.STILL} sinh khởi"

# ---------------------------------------------------------------------------------------------------------------
# 2. The dhātu-as-plane person and the kati question (new; for 7-11)
# ---------------------------------------------------------------------------------------------------------------
DHATU = {   # kāma- / rūpa- / arūpadhātu = cõi … (termbase Kāmadhātuyā / kāmadhātuṃ, rūpadhātuyā, arūpadhātuyā / -ṃ)
    "kāma": "cõi dục lạc",
    "rūpa": C.PLACE_LOC["rūpadhātuyā"],
    "arūpa": C.PLACE_LOC["arūpadhātuyā"],
}
assert DHATU["rūpa"] == "cõi hình sắc" and DHATU["arūpa"] == B.PLANES["arūp"][0] == "cõi không hình sắc"
NOT_PLANE = "nơi"                    # na X «nơi không phải là X» (termbase -dhātumūlakaṃ labels)
NOT_IS = "không phải là"
NOT_ALSO = "cũng"                    # na X na Y «nơi không phải là X cũng không phải là Y» (termbase labels)
CASE = {"abl": "yā", "acc": "ṃ"}
PLANE_TOK = re.compile(r"(kāma|rūpa|arūpa)dhātu(yā|ṃ)")


def parse_planes(text, case):
    """'Kāmadhātuyā' / 'Na kāmadhātuyā na arūpadhātuyā' / 'kāmadhātuṃ' / 'na kāmadhātuṃ na rūpadhātuṃ' →
    (negated?, [keys]). One polarity; a plain plane is a single plane; raises on anything else."""
    toks = text.split()
    neg, keys, i = None, [], 0
    while i < len(toks):
        n = toks[i].lower() == "na"
        if n:
            i += 1
            if i == len(toks):
                raise ValueError(f"'na' without a plane: {text!r}")
        m = PLANE_TOK.fullmatch(_lc(toks[i]))
        if not m or m.group(2) != CASE[case]:
            raise ValueError(f"not a {case} plane: {toks[i]!r} in {text!r}")
        if neg is not None and neg != n:
            raise ValueError(f"mixed plain / negated planes: {text!r}")
        neg = n
        keys.append(m.group(1))
        i += 1
    if not keys or (not neg and len(keys) != 1) or len(set(keys)) != len(keys):
        raise ValueError(f"unknown plane run: {text!r}")
    return neg, keys


def dhatu_phrase(neg, keys):
    """«cõi dục lạc» / «nơi không phải là cõi dục lạc» / «nơi không phải là cõi dục lạc cũng không phải là …»."""
    if not neg:
        return DHATU[keys[0]]
    return f"{NOT_PLANE} " + f" {NOT_ALSO} ".join(f"{NOT_IS} {DHATU[k]}" for k in keys)


CAV_VI, _, CAV_PREP = B.PARTICIPLES["cavantānaṃ"]        # «đang chết đi», «khỏi» (2-01)
UPA_VI, _, UPA_PREP = B.PARTICIPLES["upapajjantānaṃ"]    # «đang tái sinh», «vào» (2-01; termbase upapajjantassa)
assert CAV_VI.startswith("đang ") and UPA_VI == "đang " + C.FAMILY_TERMS["upapajjati"]
CUTASSA = "đã " + CAV_VI[len("đang "):] + " " + CAV_PREP   # cutassa (past participle): «đã chết đi khỏi»
UPAPAJJANTASSA = f"{UPA_VI} {UPA_PREP}"                     # upapajjantassa «đang tái sinh vào»
PERSON_SG = "người"                                         # genitive singular person (= the shell «ở người nào»)


def dhatu_person(fr, to):
    """«người đã chết đi khỏi <fr> và đang tái sinh vào <to>» (fr / to: Vietnamese plane phrases)."""
    return f"{PERSON_SG} {CUTASSA} {fr} {C.AND} {UPAPAJJANTASSA} {to}"


DHEAD_RE = re.compile(r"(.+?) cutassa (.+?) upapajjantassa(?= |$)")


def dhatu_head(text):
    """'<fr> cutassa <to> upapajjantassa <rest>' → («Ở người … vào <to>, », '<rest>') (for 7-11)."""
    m = DHEAD_RE.match(text)
    if not m:
        raise ValueError(f"no dhātu person head: {text!r}")
    if not m.group(1)[:1].isupper():
        raise ValueError(f"dhātu head in lower case: {text!r}")
    fr = dhatu_phrase(*parse_planes(m.group(1), "abl"))
    to = dhatu_phrase(*parse_planes(m.group(2), "acc"))
    return f"{cap(C.AT)} {dhatu_person(fr, to)}, ", text[m.end():].strip()


KATI = "bao nhiêu"                                          # kati (pi-2 «bao nhiêu khối là thiện, …»)
ANUSAYA_PL = "khuynh hướng tiềm ẩn"                         # anusayā (termbase)
KATI_PALI = "kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā"
KATI_Q = ", ".join((f"{KATI} {ANUSAYA_PL} {C.VERB['anusenti'][0]}",
                    f"{KATI} {ANUSAYA_PL} {C.VERB['nānusenti'][0]}",
                    f"{KATI} {ANUSAYA_PL} {C.FAMILY_TERMS['bhaṅgā']}"))
DQ_RE = re.compile(r"(.+?) cutassa (.+?) upapajjantassa " + re.escape(KATI_PALI) + r"([?.])")


def dhatu_question(m):
    """DQ_RE match → «Ở người đã chết đi khỏi X và đang tái sinh vào Y, bao nhiêu … phải phân chia?»."""
    head, rest = dhatu_head(f"{m.group(1)} cutassa {m.group(2)} upapajjantassa")
    assert rest == ""
    if m.group(3) == ".":                           # ^6-7-335: plainly a question (kati …), the Pāli ends «.»
        SEEN["q_dot"].append(m.group(0)[:70])
    return f"{head}{KATI_Q}?"


def dhatu_line(body):
    """A line of kati questions separated by single spaces; every question must parse."""
    out, pos = [], 0
    while pos < len(body):
        m = DQ_RE.match(body, pos)
        if not m:
            raise ValueError(f"not a dhātu question at {body[pos:pos + 80]!r}")
        out.append(dhatu_question(m))
        pos = m.end()
        if pos < len(body):
            if body[pos] != " ":
                raise ValueError(f"no space after a dhātu question: {body[pos:pos + 40]!r}")
            pos += 1
    if not out:
        raise ValueError(f"empty dhātu line: {body!r}")
    return " ".join(out)


MULAKA_BASED = "Phần dựa trên"                              # -mūlakaṃ «phần dựa trên …» (termbase; 3-01 / 10-01)
DLABEL_RE = re.compile(r" \((?:(Na)(kāma|rūpa|arūpa)(?:na(kāma|rūpa|arūpa))?|(Kāma|Rūpa|Arūpa))dhātumūlakaṃ\)$")


def dhatu_label(m):
    """(Kāmadhātumūlakaṃ) «(Phần dựa trên cõi dục lạc)»; (Nakāmanaarūpadhātumūlakaṃ) «(Phần dựa trên nơi không
    phải là cõi dục lạc cũng không phải là cõi không hình sắc)» (termbase)."""
    if m.group(4):
        return f"({MULAKA_BASED} {dhatu_phrase(False, [_lc(m.group(4))])})"
    return f"({MULAKA_BASED} {dhatu_phrase(True, [k for k in m.group(2, 3) if k])})"


DLABEL_PALI = ["Kāma", "Rūpa", "Arūpa", "Nakāma", "Narūpa", "Naarūpa", "Nakāmanaarūpa", "Narūpanaarūpa",
               "Nakāmanarūpa"]

# ---------------------------------------------------------------------------------------------------------------
# 3. vitthāretabbaṃ, answers, lines
# ---------------------------------------------------------------------------------------------------------------
VITTHARETABBAM = T5.VITTHARETABBAM                           # «nên được trình bày chi tiết» (pi-5)
VITTH_RE = re.compile(r"(.+?) \(([Vv])itthāretabbaṃ\)\.")


def answers(text, V):
    """Answer sentences (7-09 sentence); a sentence the Pāli starts in capitals starts in capitals (^6-7-325
    'Paṭighānusayo na vattabbo …': 7-09 renders a subject before na vattabbo in lower case)."""
    out = []
    for s in [x for x in re.split(r"(?<=\.) ", text.strip()) if x]:
        v = P9.sentence(s, V)
        if s[:1].isupper() and v[:1].islower():
            SEEN["capped"].append(s[:70])
            v = cap(v)
        if C.is_anusaya(_lc(s.split()[0]).split("…")[0]) and "vattabb" not in s.split(";")[0]:
            SEEN["bare"].append(s[:80])
        out.append(v)
    return " ".join(out)


def line_vi(body, V):
    """A question line (7-09 question, + its answers) or a line of answers."""
    m = C.Q_RE.fullmatch(body)
    if m:
        rest = m.group(9)
        q = body[:len(body) - len(rest) - 1] if rest else body
        out = P9.question(q, V)
        return out + (" " + answers(rest, V) if rest else "")
    return answers(body, V)


def vitth(body, V):
    """'… V (vitthāretabbaṃ).' «… V (nên được trình bày chi tiết).»; '…. (Vitthāretabbaṃ).' «…. (Nên …).»."""
    m = VITTH_RE.fullmatch(body)
    if not m:
        return None
    pre, big = m.group(1), m.group(2) == "V"
    SEEN["vitth"].append(body[-40:])
    if pre.endswith("."):                           # a sentence of its own after the answer
        if not big:
            raise ValueError(f"lower-case vitthāretabbaṃ after «.»: {body!r}")
        return f"{line_vi(pre, V)} ({cap(VITTHARETABBAM)})."
    if big:
        raise ValueError(f"capital Vitthāretabbaṃ inside a sentence: {body!r}")
    return f"{line_vi(pre + '.', V)[:-1]} ({VITTHARETABBAM})."


PAHINAVARO = P9.PAHINAVARO                                   # «Mục về những gì đã được dứt bỏ»
UPPAJJANAVARO = C.HEADINGS["Uppajjanavāro"]                  # «Mục về sự sinh khởi» (termbase)
DHATUPUCCHAVARO = C.HEADINGS["dhātupucchāvāro"]              # «Mục hỏi theo các cõi» (user decision, S)
assert DHATUPUCCHAVARO == "Mục hỏi theo các cõi"
FIXED = {
    "Pahīnavāre paṭilomaṃ.": f"{T2.PATILOMA} trong {P9.PAHINAVARO_LC}.",   # = 7-06 «Pajahanāvāre paṭilomaṃ.»
    "Pahīnavāro.": PAHINAVARO + ".",                                       # closing labels (= 7-01 Uppattiṭṭhānavāro.)
    "Uppajjanavāro.": UPPAJJANAVARO + ".",
    "Dhātupucchāvāro.": DHATUPUCCHAVARO + ".",
    "9": "9",                                                              # ^6-7-311: a bare digit line, kept
}
R6 = importlib.import_module("build_rails_7-06_vi")         # READ-ONLY (assert only)
assert R6.FIXED["Pajahanāvāre paṭilomaṃ."] == f"{T2.PATILOMA} trong {R6.PAJAHANAVARO_LC}."
assert C.FIXED["Uppattiṭṭhānavāro."] == C.UPPATTITTHANAVARO + "."
MODE_BY_HEADING = {"Uppajjanavāro": UPPAJJ, "(Ka) dhātupucchāvāro": "dhatu"}   # other headings: PAHINA


def tr_line(p, mode, fixed=None):
    """→ (Vietnamese line, mode for the following lines)."""
    fixed = FIXED if fixed is None else fixed
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out, mode = f"{hashes} {C.heading(text)}", MODE_BY_HEADING.get(text, PAHINA)
    else:
        label = ""
        if mm := C.MULAKA_RE.search(body):
            label = " " + C.mulaka_label(mm)
            body = body[:mm.start()]
        elif mm := DLABEL_RE.search(body):
            label = " " + dhatu_label(mm)
            body = body[:mm.start()]
        if body in fixed:
            out = fixed[body]
            if body == "9":
                SEEN["digit"].append(bid or "")
        elif mode == "dhatu":
            out = dhatu_line(body)
        elif (v := vitth(body, mode)) is not None:
            out = v
        else:
            out = line_vi(body, mode)
        out += label
    return (f"{out} {bid}" if bid else out), mode


def build(name=CHAPTER, fixed=None):
    segs, mode = [], PAHINA
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                v, mode = tr_line(ln, mode, fixed)
            except ValueError as e:
                raise ValueError(f"{name}: cannot place line {ln[:120]!r}: {e}") from None
            out.append(v)
        segs.append(out)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# 4. Checks
# ---------------------------------------------------------------------------------------------------------------
REUSED = [   # (Pāli, Vietnamese, book): asserted in that book's approved rails
    ("kati kusalā, kati akusalā (pi-2 ^2-151)", f", {KATI} khối là bất thiện, {KATI} khối", "2"),
    ("vitthāretabbaṃ (pi-5)", VITTHARETABBAM, "5"),
    ("rūpadhātuyā cuto arūpadhātuṃ upapajjati (pi-5 ^5-65; plane + tái sinh vào)", "tái sinh vào cõi không hình sắc",
     "5"),
]
TERMBASE_USED = [
    ("uppajjati", UPPAJJ.pos), ("uppajjatīti", UPPAJJ.pos), ("nuppajjati", UPPAJJ.neg), ("nuppajjatīti", UPPAJJ.neg),
    ("Uppajjanavāro", _lc(UPPAJJANAVARO)), ("dhātupucchāvāro", _lc(DHATUPUCCHAVARO)),
    ("paṭilomaokāso", "chiều ngược theo nơi chốn"), ("paṭilomapuggalokāsā", "chiều ngược theo người và nơi chốn"),
    ("paṭilomaṃ", _lc(T2.PATILOMA)), ("Pahīnavāro", _lc(PAHINAVARO)), ("Pahīnavāre", _lc(PAHINAVARO)),
    ("Kāmadhātuyā", DHATU["kāma"]), ("kāmadhātuṃ", DHATU["kāma"]), ("rūpadhātuyā", DHATU["rūpa"]),
    ("arūpadhātuyā", DHATU["arūpa"]), ("arūpadhātuṃ", DHATU["arūpa"]),
    ("upapajjantassa", C.FAMILY_TERMS["upapajjati"]), ("anusayā", ANUSAYA_PL), ("anusenti", C.LIE_LATENT),
    ("nānusenti", C.VERB["nānusenti"][0]), ("bhaṅgā", C.FAMILY_TERMS["bhaṅgā"]),
    ("Anāgāmissa", "bậc không trở lại"), ("Puthujjanassa", "người phàm phu"), ("arahato", "bậc A-la-hán"),
    ("puggalānaṃ", "hạng người"), ("puggalassa", "hạng người"), ("Natthi", "không có"),
    ("pahīno", PAHINA.pos), ("appahīno", PAHINA.neg),
    ("dvīsu vedanāsu", "hai loại cảm giác"), ("tīsu vedanāsu", "ba loại cảm giác"),
    ("Dukkhāya vedanāya", "cảm giác khó chịu"),
] + [(f"{x}dhātumūlakaṃ", _lc(dhatu_label(DLABEL_RE.search(f" ({x}dhātumūlakaṃ)"))[1:-1])) for x in DLABEL_PALI]
USER_DECISIONS = ["dhātupucchāvāro «mục hỏi theo các cõi»", "bhaṅgā «phải phân chia»",
                  "na vattabbo «không nên nói là …»"]


def check_reused():
    P9.check_reused()
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    tb = C.TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M)]
    assert not bad, "termbase strings not found: " + repr(bad)
    ap = unicodedata.normalize("NFC", R7.P5.APPROVED.read_text(encoding="utf-8"))
    bad = [d for d in USER_DECISIONS if d not in ap]
    assert not bad, "user decisions not found in APPROVED.md: " + repr(bad)


def check_family():
    """7-09 rebuilt with this module's line translator = its chapter file, byte for byte (so the wrappers here
    change nothing 7-09 decided); 7-01-style uppajjati frames = 2-01's verb strings."""
    saved = {k: list(v) for k, v in SEEN.items()}
    name = "7-09-anusayayamaka.md"
    mine = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in build(name, P9.FIXED)) + "\n")
    theirs = (S.OUT_DIR / name).read_text(encoding="utf-8")
    if mine != theirs:
        diff = [(x, y) for x, y in zip(mine.splitlines(), theirs.splitlines()) if x != y]
        raise AssertionError(f"{name} rebuilt differs: {diff[:2]}")
    for k in SEEN:
        SEEN[k][:] = saved[k]
    a, b = C.ANUSAYA["mān"], C.ANUSAYA["kāmarāg"]
    assert P9.sentence("Anāgāmissa kāmarāgānusayo nuppajjati, no ca tassa mānānusayo nuppajjati.", UPPAJJ) == \
        f"Ở {C.PERSON_GEN['Anāgāmissa'][0]}, {b} {UPPAJJ.neg}, {C.BUT} {C.AT} {C.PRON['tassa']} {a} " \
        f"{B.noca_vi('', B.VERB['nuppajjati']).strip()}."


# ---------------------------------------------------------------------------------------------------------------
# 5. Notes
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-10 (Anusayayamaka: pahīnavāra paṭiloma by place / person + place, uppajjanavāra, "
         "dhātupucchāvāra): frames and fixed strings", "",
         "Generated by build_rails_7-10_vi.py. Imports S, 7-01 (family C), 7-02, 7-06, 7-07 (Verb), 7-09 (PAHINA, "
         "nv_vi, sentence, question), 2-01 (uppajjati strings, PARTICIPLES) and 5-01 (VITTHARETABBAM): their strings, "
         "byte for byte; the builder rebuilds 7-09 with its own line translator and asserts it equals the 7-09 "
         "chapter file. New, for 7-11: the dhātu-as-plane person and the kati question (parameterised; import the "
         "module with importlib.import_module(\"build_rails_7-10_vi\")).", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    h("Pahīnavāra paṭiloma (= 7-09 PAHINA frames)")
    for p in ('Na vattabbo "pahīno"ti vā "appahīno"ti vā.',
              "Kāmadhātuyā dvīsu vedanāsu ettha mānānusayo ca appahīno kāmarāgānusayo ca appahīno.",
              'Rūpadhātuyā arūpadhātuyā ettha mānānusayo appahīno; kāmarāgānusayo na vattabbo "pahīno"ti vā '
              '"appahīno"ti vā.',
              "Tasseva puggalassa kāmadhātuyā dvīsu vedanāsu tassa tattha mānānusayo appahīno, no ca tassa tattha "
              "kāmarāgānusayo appahīno.",
              'Paṭighānusayo na vattabbo "pahīno"ti vā "appahīno"ti vā.'):
        row(p, answers(p, PAHINA))
    row("(Ka) yattha A appahīno tattha B appahīnoti?",
        C.pair_q("yattha", f"A {PAHINA.neg}", f"B {PAHINA.neg}", "Ka"))
    row("(Kha) yassa vā pana yattha B appahīno tassa tattha A appahīnoti?",
        C.pair_q("yassa yattha", f"B {PAHINA.neg}", f"A {PAHINA.neg}", "Kha", True))
    h("Uppajjanavāra (UPPAJJ in 7-09's frames; 2-01 strings)")
    row("uppajjati / nuppajjati", f"{UPPAJJ.pos} / {UPPAJJ.neg}")
    row("no ca … nuppajjati (negative denied)", UPPAJJ.still)
    for p in ("(Ka) yassa kāmarāgānusayo uppajjati tassa paṭighānusayo uppajjatīti?",
              "(Ka) yassa kāmarāgānusayo nuppajjati tassa mānānusayo nuppajjatīti?"):
        row(p, line_vi(p, UPPAJJ))
    for p in ("Anāgāmissa mānānusayo uppajjati, no ca tassa kāmarāgānusayo uppajjati.",
              "Anāgāmissa kāmarāgānusayo nuppajjati, no ca tassa mānānusayo nuppajjati.",
              "Arahato kāmarāgānusayo ca nuppajjati mānānusayo ca nuppajjati.",
              "Tiṇṇaṃ puggalānaṃ mānānusayo ca uppajjati kāmarāgānusayo ca uppajjati (vitthāretabbaṃ).",
              "(Kha) yassa vā pana mānānusayo nuppajjati tassa kāmarāgānusayo nuppajjatīti? Āmantā. "
              "(Vitthāretabbaṃ)."):
        row(p, vitth(p, UPPAJJ) or answers(p, UPPAJJ))
    h("Dhātupucchāvāra (new, parameterised for 7-11)")
    row("Kāmadhātuyā / kāmadhātuṃ", DHATU["kāma"] + "  (termbase)")
    row("rūpadhātuyā / rūpadhātuṃ", DHATU["rūpa"] + "  (rūpadhātuṃ: no termbase entry, sibling rūpadhātuyā)")
    row("arūpadhātuyā / arūpadhātuṃ", DHATU["arūpa"] + "  (termbase)")
    row("na X (ablative or accusative)", dhatu_phrase(True, ["kāma"]) + "  (termbase Nakāmadhātumūlakaṃ)")
    row("na X na Y", dhatu_phrase(True, ["kāma", "arūpa"]) + "  (termbase Nakāmanaarūpadhātumūlakaṃ)")
    row("<fr> cutassa", f"{PERSON_SG} {CUTASSA} <fr>  (cutassa: no termbase entry; 2-01 cavantānaṃ «đang chết đi "
                        f"khỏi» with «đã» for the past participle)")
    row("<to> upapajjantassa", f"{C.AND} {UPAPAJJANTASSA} <to>  (termbase upapajjantassa «tái sinh»; 2-01 «đang "
                               f"tái sinh vào»)")
    row(KATI_PALI + "?", KATI_Q + "?  (kati «bao nhiêu», pi-2 ^2-151; anusayā «khuynh hướng tiềm ẩn», "
                                  "bhaṅgā «phải phân chia»: termbase / user decision)")
    for p in ("Kāmadhātuyā cutassa kāmadhātuṃ upapajjantassa " + KATI_PALI + "?",
              "Kāmadhātuyā cutassa na rūpadhātuṃ upapajjantassa " + KATI_PALI + "?",
              "Na kāmadhātuyā na arūpadhātuyā cutassa na kāmadhātuṃ na rūpadhātuṃ upapajjantassa " + KATI_PALI + "?"):
        row(p, dhatu_line(p))
    row("dhatu_head('Kāmadhātuyā cutassa rūpadhātuṃ upapajjantassa …') (for 7-11)",
        dhatu_head("Kāmadhātuyā cutassa rūpadhātuṃ upapajjantassa X")[0] + "…")
    for x in DLABEL_PALI:
        row(f"({x}dhātumūlakaṃ)", dhatu_label(DLABEL_RE.search(f" ({x}dhātumūlakaṃ)")))
    h("Fixed lines, notes")
    for k, v in FIXED.items():
        row(k, v)
    row("(vitthāretabbaṃ) inside a sentence", f"({VITTHARETABBAM})  (pi-5; 5-01 VITTHARETABBAM)")
    row("(Vitthāretabbaṃ). after a sentence", f"({cap(VITTHARETABBAM)}).")
    h("Pāli as written / punctuation (reported)")
    for s in sorted(set(SEEN["capped"])):
        o.append(f"- a sentence of its own (as written; parallel lines have «; paṭighānusayo …»), capitalised: {s}…")
    for s in sorted(set(SEEN["bare"])):
        o.append(f"- answer without a head (as written): {s}…")
    for s in sorted(set(SEEN["q_dot"])):
        o.append(f"- kati question ending «.» in the Pāli (^6-7-335, plainly a question): rendered «?»: {s}…")
    for s in sorted(set(SEEN["digit"])):
        o.append(f"- a bare «9» line ({s}), kept as a digit (as the English rails)")
    o.append("- ^6-7-311 / ^6-7-322 «Āmantā …pe….», ^6-7-316 / ^6-7-327 «… vā …pe….»: «…pe…» → «…» (7-02 cut).")
    o.append("")
    return "\n".join(o)


def main():
    check_reused()
    check_family()
    n0 = len(C.SLIPS_SEEN)
    for k in P9.SEEN:                       # entries from the 7-09 rebuild are 7-09's, not this chapter's
        P9.SEEN[k][:] = []
    segs = build(CHAPTER)
    C.write(CHAPTER, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for k, v in SEEN.items():
        for x in sorted(set(map(str, v))):
            print(f"{k}: {x[:120]}")
    for k, v in P9.SEEN.items():
        for x in sorted(set(map(str, v))):
            print(f"7-09 {k}: {x[:120]}")
    for p, v in sorted(set(C.SLIPS_SEEN[n0:])):
        print("slip rendered as meant:", p, "→", v)


if __name__ == "__main__":
    main()
