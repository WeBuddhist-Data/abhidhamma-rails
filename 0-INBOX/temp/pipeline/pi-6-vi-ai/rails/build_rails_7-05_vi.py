"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-05 (Anusayayamaka: pajahanavāra, anuloma: person, place,
person + place).

Family C: imports build_rails_7-01_vi (tendencies, places, pronouns, labels, headings, family terms),
build_rails_7-03_vi (the nominative yo / so, yato / tato, yo yato / so tato shell, nominative persons, heads,
the «…pe….» tail) and build_rails_7-02_vi (cuts), all READ-ONLY, and copies their strings byte for byte.

New frames (exposed for 7-06 pajahanavāra paṭiloma and the other pajahati / tadekaṭṭha chapters):
  PAJAHATI / NOT_PAJAHATI    pajahati «dứt bỏ» / its "no ca" denial «không dứt bỏ» (termbase nappajahati)
  TADEKATTHA / TAD_ATTR      standalone Tadekaṭṭhaṃ «những gì cùng hiện diện với nó» (user decision); tadekaṭṭha
                             qualifying A (modifier form) «vốn cùng hiện diện với nó": "A tadekaṭṭhaṃ pajahati"
                             = «dứt bỏ A, vốn cùng hiện diện với nó» (one item or a list; coordinator)
  PERSON_NOM                 7-03's persons + Aṭṭhamako «người thứ tám», Aggamaggasamaṅgī «người có được con đường
                             tối thượng» (termbase)
  parse_clause() / clause_vi() / neg_vi()   "<accusative run> [tadekaṭṭhaṃ] pajahati" (one or two groups)
  sentence() / answers() / question() / tr_line() / build()
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-05_vi.py
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

C = importlib.import_module("build_rails_7-01_vi")   # family C setter (READ-ONLY)
C2 = importlib.import_module("build_rails_7-02_vi")  # cuts (READ-ONLY)
C3 = importlib.import_module("build_rails_7-03_vi")  # nominative person frame (READ-ONLY)

CHAPTER = "7-05-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-05.md"
ADH_DIR = RAILS_DIR / "adh-7-05"
APPROVED = S.ROOT / "0-INBOX/temp/pipeline/pi-6-vi-ai/termbase/APPROVED.md"
cap = S.cap

# ---------------------------------------------------------------------------------------------------------------
# 1. The verb and tadekaṭṭha
# ---------------------------------------------------------------------------------------------------------------
PAJAHATI = C.FAMILY_TERMS["pajahati"]            # «dứt bỏ» (termbase)
NOT_PAJAHATI = C.FAMILY_TERMS["nappajahati"]     # «không dứt bỏ»: "no ca … pajahati" (termbase nappajahati)
TADEKATTHA = "những gì cùng hiện diện với nó"    # standalone Tadekaṭṭhaṃ (user decision, APPROVED.md 5; pi-1 «cùng hiện diện với»)
TAD_ATTR = "vốn cùng hiện diện với nó"           # tadekaṭṭha qualifying A: bare modifier form (coordinator, 2026-11-22)
TAD_JOIN = f", {TAD_ATTR}"                       # "A tadekaṭṭhaṃ pajahati" = «dứt bỏ A, vốn cùng hiện diện với nó» (one or more)
assert TADEKATTHA.endswith(TAD_ATTR.split(" ", 1)[1])
TAD = "tadekaṭṭhaṃ"
assert C.NEITHER_NEXT == f"{C.ALSO} {C.NEITHER_FIRST}"   # «cũng không có» = ALSO + «không có»: the same build here
VERB_RE = re.compile(r" (pajahati)(?= |$)")


def is_acc(word):
    """An accusative tendency word ('kāmarāgānusayaṃ'); the -añca forms are split before parsing."""
    return C.is_anusaya(word) and word.endswith("ānusayaṃ")


def parse_run(run):
    """'<tendencies> [tadekaṭṭhaṃ]' → (tp | None, tadekaṭṭha?). 'Xañca' = 'Xaṃ ca' (C.parse_tp)."""
    w = run.split()
    tad = bool(w) and w[-1] == TAD
    if tad:
        w = w[:-1]
    if not w:
        if tad:
            return None, True
        raise ValueError(f"empty object before pajahati: {run!r}")
    txt = re.sub(r"ānusayañca(?=[\s…]|$)", "ānusayaṃ ca", " ".join(w))
    return C.parse_tp(txt, subject=is_acc), tad


def parse_clause(text):
    """'<run> pajahati [<run> pajahati]' → [(tp | None, tad), …]."""
    t = text.strip()
    t = t[:1].lower() + t[1:]
    parts = VERB_RE.split(" " + t)
    if parts[-1].strip() or len(parts) < 3:
        raise ValueError(f"clause does not end in pajahati: {text!r}")
    return [parse_run(run.strip()) for run in parts[0:-1:2]]


def _obj(tp, tad):
    if tp is None:
        return TADEKATTHA
    return C.tp_vi(tp) + (TAD_JOIN if tad else "")


def clause_vi(groups):
    """One group: «dứt bỏ A» / «dứt bỏ A, là …» / «dứt bỏ những gì …» (bare Tadekaṭṭhaṃ pajahati).
    Two groups: both-frame 'A ca pajahati B ca pajahati' = «dứt bỏ A, cũng dứt bỏ B» (7-01 / 7-03);
    'A pajahati B tadekaṭṭhaṃ pajahati' = «dứt bỏ A, dứt bỏ B, là những gì cùng hiện diện với nó»."""
    if len(groups) == 1:
        return f"{PAJAHATI} {_obj(*groups[0])}"
    if len(groups) == 2:
        (t1, d1), (t2, d2) = groups
        if t1 is None or t2 is None or d1:
            raise ValueError("unknown clause shape: " + repr(groups))
        if not d2 and t1["conj"] and t2["conj"]:
            return f"{PAJAHATI} {C.tp_vi(t1)}, {C.ALSO} {PAJAHATI} {C.tp_vi(t2)}"
        if d2 and not (len(t1["names"]) == 1 and t1["conj"]):
            return f"{PAJAHATI} {C.tp_vi(t1)}, {PAJAHATI} {_obj(t2, d2)}"
    raise ValueError("unknown clause shape: " + repr(groups))


def neg_vi(groups):
    """After 'no ca': «không dứt bỏ A[, cũng không dứt bỏ B …]» (user "neither" rule, 7-03's build)."""
    if len(groups) != 1 or groups[0][0] is None or groups[0][1]:
        raise ValueError("unknown 'no ca' part: " + repr(groups))
    tp = groups[0][0]
    if tp["pe"]:
        raise ValueError("…pe… inside a 'no ca' part: " + repr(tp))
    return f"{NOT_PAJAHATI} " + f", {C.ALSO} {NOT_PAJAHATI} ".join(tp["names"])


# ---------------------------------------------------------------------------------------------------------------
# 2. Answer heads (7-03's heads; two more persons from the termbase)
# ---------------------------------------------------------------------------------------------------------------
PERSON_NOM = {**C3.PERSON_NOM,
              "Aṭṭhamako": ("người thứ tám", 1),                            # termbase; user «Người thứ tám»; pi-5
              "Aggamaggasamaṅgī": ("người có được con đường tối thượng", 1)}  # termbase


def parse_head(txt):
    """'<person>? <places>* <so tato | te tato | tato>' → (person | None, [places], resumptive) (7-03's rules)."""
    person, rest = C._take(txt, PERSON_NOM)
    places = []
    while rest:
        p, rest2 = C._take(rest, C.PLACE_LOC, fold=True)
        if not p:
            break
        places.append(p)
        rest = rest2
    if rest not in ("", "tato", "so tato", "te tato"):
        raise ValueError(f"unknown answer head {txt!r} (left: {rest!r})")
    if person and places and rest != ("so tato" if PERSON_NOM[person][1] == 1 else "te tato"):
        raise ValueError(f"person + place without a fitting 'so / te tato': {txt!r}")
    if person and not places and rest:
        raise ValueError(f"person head with a resumptive: {txt!r}")
    if not person and places and rest != "tato":
        raise ValueError(f"place head without 'tato': {txt!r}")
    if not person and not places:
        raise ValueError(f"empty answer head: {txt!r}")
    return person, places, rest


def head_vi(person, places, res):
    parts = ([PERSON_NOM[person][0]] if person else []) + [f"{C.AT} {C.PLACE_LOC[p]}" for p in places]
    out = cap(", ".join(parts))
    return out + (f", {C.THEN} {C3.pron_vi(res)} " if res else " ")


SENT_RE = re.compile(r"(.+?)(?:(,?) no ca (?:(so tato|te tato|tato) )?(.+))?\.")
NO_COMMA_SEEN = []   # "… pajahati no ca …" without the Pāli comma (^6-7-148): missing comma rendered as meant
#                      (coordinator, as 7-04 at ^6-7-122)


def _is_obj_word(w):
    w = w.split("…")[0]
    w = w[:1].lower() + w[1:]
    return w == TAD or C.is_anusaya(w)


def sentence(s):
    """Āmantā. / No. / Natthi. / [<head>] <clause>[(,) no ca [<pron>] <clause>]. (+ a «…pe….» tail, 7-03)"""
    if (t := C3.pe_tail(s, sentence)) is not None:
        return t
    if s in C.EXACT:
        return C.EXACT[s]
    m = SENT_RE.fullmatch(s)
    if not m:
        raise ValueError(f"unknown sentence {s!r}")
    words = m.group(1).split()
    i = next((k for k, w in enumerate(words) if _is_obj_word(w)), None)
    if i is None:
        raise ValueError(f"no object in {s!r}")
    groups = parse_clause(" ".join(words[i:]))
    if i == 0:                                   # bare answer: «Dứt bỏ A.» / «Dứt bỏ những gì …»
        if m.group(4):
            raise ValueError(f"bare answer with 'no ca': {s!r}")
        return cap(clause_vi(groups)) + "."
    if words[i][0].isupper():
        raise ValueError(f"capital object after a head: {s!r}")
    person, places, res = parse_head(" ".join(words[:i]))
    out = head_vi(person, places, res) + clause_vi(groups)
    if m.group(4):
        pron = m.group(3) or ""
        if pron != res:
            raise ValueError(f"'no ca {pron}' does not fit the head ({res!r}): {s!r}")
        if not m.group(2):
            NO_COMMA_SEEN.append(s)
        out += ", " + f"{C.BUT} " + (C3.pron_vi(pron) + " " if pron else "") + \
            neg_vi(parse_clause(m.group(4)))
    return out + "."


def answers(text):
    parts = [x for x in re.split(r"(?<=\.) ", text.strip()) if x]
    return " ".join(sentence(x) for x in parts)


# ---------------------------------------------------------------------------------------------------------------
# 3. Questions: 7-03's shell (C3.Q_RE, C3.yo_q) with the pajahati slots
# ---------------------------------------------------------------------------------------------------------------
def slot_vi(text):
    groups = parse_clause(text)
    if len(groups) != 1 or groups[0][0] is None or groups[0][1]:
        raise ValueError(f"question slot must be one plain object run: {text!r}")
    return clause_vi(groups)


def question(body):
    m = C3.Q_RE.fullmatch(body)
    if not m:
        return None
    label, y, rel1, vapana, yato, a, cor, b, rest = m.groups()
    rel = "y" + rel1 + (" yato" if yato else "")
    if yato and rel1 != "o":
        raise ValueError(f"bad relative in {body!r}")
    if C3.YO_COR[rel] != cor:
        raise ValueError(f"relative {rel!r} with correlative {cor!r}: {body!r}")
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {body!r}")
    if label and (label == "Kha") != bool(vapana):
        raise ValueError(f"label {label} with vā pana={bool(vapana)}: {body!r}")
    bw = b.split()
    bw[-1] = C.strip_ti(bw[-1])
    va, vb = slot_vi(a), slot_vi(" ".join(bw))
    out = C3.yo_q(rel, va, vb, label, bool(vapana))
    if rel == "yato":   # the place shell is C's yattha shell word for word
        assert out == C.pair_q("yattha", va, vb, label, bool(vapana)), out
    return out + (" " + answers(rest) if rest else "")


# ---------------------------------------------------------------------------------------------------------------
# 4. Headings and fixed lines
# ---------------------------------------------------------------------------------------------------------------
PAJAHANAVARO = C.HEADINGS["Pajahanavāro"]        # «Mục về sự dứt bỏ» (S.LATER_HEADINGS, termbase)
assert PAJAHANAVARO == C.FAMILY_HEADINGS["Pajahanavāra"]
FIXED = {   # built as C's «Anusayavāre anulomaṃ.» / C3's «Sānusayavāre anulomaṃ.»
    "Pajahanavāre anulomaṃ.": f"{C.HEADINGS['anulomaṃ']} trong {PAJAHANAVARO[0].lower()}{PAJAHANAVARO[1:]}.",
}


def tr_line(p):
    m = re.search(r" (\^\S+)$", p)
    bid = m.group(1) if m else None
    body = p[:m.start()] if m else p
    if body.startswith("#"):
        hashes, text = body.split(" ", 1)
        out = f"{hashes} {C.heading(text)}"
    else:
        label = ""
        if mm := C.MULAKA_RE.search(body):
            label = " " + C.mulaka_label(mm)
            body = body[:mm.start()]
        if body in FIXED:
            out = FIXED[body]
        elif (q := question(body)) is not None:
            out = q
        else:
            out = answers(body)
        out += label
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln))
            except ValueError as e:
                raise ValueError(f"{name}: cannot place line {ln[:120]!r}: {e}") from None
        segs.append(out)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# 5. Checks: reused strings, termbase, user decisions, family agreement
# ---------------------------------------------------------------------------------------------------------------
REUSED = [   # (Pāli, Vietnamese, book): asserted in that book's approved rails
    ("tadekaṭṭhā ca kilesā", "cùng hiện diện với", "1"),
    ("Aṭṭhamako puggalo", "người thứ tám", "5"),
    ("pahātabbā", f"cần {PAJAHATI}", "1"),
]
TERMBASE_USED = [
    ("pajahati", PAJAHATI), ("pajahatīti", PAJAHATI), ("Aṭṭhamako", "người thứ tám"),
    ("Aggamaggasamaṅgī", "người có được con đường tối thượng"), ("Pajahanavāro", "mục về sự dứt bỏ"),
    ("Pajahanavāre", "mục về sự dứt bỏ"), ("puggalo", "hạng người"), ("anulomaṃ", "chiều thuận"),
    ("anulomapuggalo", "chiều thuận theo người"), ("anulomaokāso", "chiều thuận theo nơi chốn"),
    ("anulomapuggalokāsā", "chiều thuận theo người và nơi chốn"),
    ("kāmarāgānusayaṃ", C.ANUSAYA["kāmarāg"]), ("paṭighānusayaṃ", C.ANUSAYA["paṭigh"]),
    ("mānānusayaṃ", C.ANUSAYA["mān"]), ("diṭṭhānusayaṃ", C.ANUSAYA["diṭṭh"]),
    ("vicikicchānusayaṃ", C.ANUSAYA["vicikicch"]), ("bhavarāgānusayaṃ", C.ANUSAYA["bhavarāg"]),
    ("avijjānusayaṃ", C.ANUSAYA["avijj"]), ("kāmarāgānusayañca", C.ANUSAYA["kāmarāg"]),
    ("Kāmadhātuyā", "cõi dục lạc"), ("rūpadhātuyā", "cõi hình sắc"), ("arūpadhātuyā", "cõi không hình sắc"),
    ("dvīsu vedanāsu", "hai loại cảm giác"), ("tīsu vedanāsu", "ba loại cảm giác"),
    ("Dukkhāya vedanāya", "cảm giác khó chịu"),
]
USER_DECISIONS = ["tadekaṭṭha «" + TADEKATTHA + "»", "Aṭṭhamako «Người thứ tám»"]


def check_reused():
    C3.check_reused()   # 7-01's and 7-03's (pi-N) and termbase strings
    C2.check_reused()
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    tb = C.TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M)]
    assert not bad, "termbase strings not found: " + repr(bad)
    ap = unicodedata.normalize("NFC", APPROVED.read_text(encoding="utf-8"))
    bad = [d for d in USER_DECISIONS if d not in ap]
    assert not bad, "user decisions not found in APPROVED.md: " + repr(bad)


def check_family():
    """Strings shared with 7-02 / 7-03 stay byte-identical."""
    for k in C3.PERSON_NOM:
        assert PERSON_NOM[k] == C3.PERSON_NOM[k]
    for h in (("Sveva puggalo", ["kāmadhātuyā dvīsu vedanāsu"], "so tato"),
              (None, ["rūpadhātuyā", "arūpadhātuyā"], "tato"),
              ("Teva puggalā", ["dukkhāya vedanāya"], "te tato")):
        assert head_vi(*h) == C3.head_vi(*h), h
    for s in ("Āmantā …pe….", "Āmantā…pe…."):
        assert sentence(s) == C3.sentence(s) == C2.sentence(s), s
    assert C3.yo_q("yo", "A", "B", "Ka") == "(a) Người nào mà A, thì người ấy có phải B không?"


# ---------------------------------------------------------------------------------------------------------------
# 6. Notes file
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-05 (Anusayayamaka, pajahanavāra anuloma): frames and fixed strings", "",
         "Generated by build_rails_7-05_vi.py. Family C (setter 7-01), the nominative yo / yato shell and heads (7-03) "
         "and the cuts (7-02) are imported unchanged. New here: the pajahati predicate, tadekaṭṭhaṃ, two persons. "
         "Later chapters (7-06 pajahanavāra paṭiloma …) import the module "
         "(importlib.import_module(\"build_rails_7-05_vi\")).", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    h("Predicate (termbase pajahati «dứt bỏ»; user decision tadekaṭṭha)")
    row("A pajahati", f"{PAJAHATI} A")
    row("A ca B ca pajahati", f"{PAJAHATI} A {C.AND} B")
    row("A ca pajahati B ca pajahati (both)", f"{PAJAHATI} A, {C.ALSO} {PAJAHATI} B")
    row("Tadekaṭṭhaṃ pajahati.", sentence("Tadekaṭṭhaṃ pajahati."))
    row("A tadekaṭṭhaṃ pajahati", f"{PAJAHATI} A{TAD_JOIN}")
    row("A ca B ca C ca tadekaṭṭhaṃ pajahati", f"{PAJAHATI} A, B {C.AND} C{TAD_JOIN}")
    row("A pajahati B tadekaṭṭhaṃ pajahati", f"{PAJAHATI} A, {PAJAHATI} B{TAD_JOIN}")
    row(", no ca <pron> A pajahati", f", {C.BUT} <pron> {NOT_PAJAHATI} A")
    row(", no ca <pron> A ca B ca pajahati (neither; user rule)",
        f", {C.BUT} <pron> {NOT_PAJAHATI} A, {C.ALSO} {NOT_PAJAHATI} B")
    row("Mānānusayaṃ pajahati. (bare answer)", sentence("Mānānusayaṃ pajahati."))
    h("Questions (7-03 shell)")
    a, b = f"{PAJAHATI} A", f"{PAJAHATI} B"
    row("(Ka) yo A pajahati so B pajahatīti?", C3.yo_q("yo", a, b, "Ka"))
    row("(Kha) yo vā pana B pajahati so A pajahatīti?", C3.yo_q("yo", b, a, "Kha", True))
    row("(Ka) yato A pajahati tato B pajahatīti?", C3.yo_q("yato", a, b, "Ka"))
    row("(Ka) yo yato A pajahati so tato B pajahatīti?", C3.yo_q("yo yato", a, b, "Ka"))
    h("Answer heads (new persons; the rest as 7-03)")
    for k in ("Aṭṭhamako", "Aggamaggasamaṅgī"):
        row(f"{k} …", f"{cap(PERSON_NOM[k][0])} …")
    o.append("")
    o.append("Examples (built by the module):")
    for p in ("Rūpadhātuyā arūpadhātuyā tato mānānusayaṃ pajahati, no ca tato kāmarāgānusayaṃ pajahati.",
              "Kāmadhātuyā dvīsu vedanāsu tato mānānusayañca pajahati kāmarāgānusayañca pajahati.",
              "Dukkhāya vedanāya tato vicikicchānusayañca paṭighānusayañca pajahati, no ca tato kāmarāgānusayañca "
              "mānānusayañca pajahati.",
              "Diṭṭhānusayaṃ pajahati kāmarāgānusayañca paṭighānusayañca mānānusayañca tadekaṭṭhaṃ pajahati …pe….",
              "Aṭṭhamako rūpadhātuyā arūpadhātuyā so tato vicikicchānusayaṃ pajahati mānānusayaṃ tadekaṭṭhaṃ pajahati, "
              "no ca so tato kāmarāgānusayañca paṭighānusayañca pajahati.",
              "Aggamaggasamaṅgī dukkhāya vedanāya so tato avijjānusayaṃ pajahati, no ca so tato mānānusayaṃ pajahati."):
        row(p, sentence(p))
    h("Fixed lines")
    for k, v in FIXED.items():
        row(k, v)
    h("Missing punctuation rendered as meant")
    for s in sorted(set(NO_COMMA_SEEN)):
        row(s, sentence(s) + "  (^6-7-148: comma before no ca added, as 7-04 at ^6-7-122)")
    o.append("")
    return "\n".join(o)


def main():
    check_reused()
    check_family()
    segs = build(CHAPTER)
    C.write(CHAPTER, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for p, v in sorted(set(C.SLIPS_SEEN)):
        print("slip rendered as meant:", p, "→", v)
    for s in sorted(set(NO_COMMA_SEEN)):
        print("missing comma before 'no ca' rendered as meant:", s[:100])


if __name__ == "__main__":
    main()
