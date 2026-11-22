"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-02 (Anusayayamaka: anusayavāra, paṭiloma).

Family C (set by rails 7-01): imports build_rails_7-01_vi (READ-ONLY) and build_rails_sample_vi (READ-ONLY) and
copies their strings byte for byte. This module adds the negative (paṭiloma) frames and the "…pe…" cuts:
  APARIYAPANNE / SABBATTHA        the place «những gì không nằm trong các cõi tồn tại» (pi-1 / pi-2 apariyāpanna)
                                  and «mọi nơi» (sabbattha, coordinator: every plane; pi-5 «ở mọi nơi»)
  clause_vi()                     both-frame for negative verbs too: «A không nằm sẵn, B cũng không nằm sẵn»
  neg_clause_vi()                 "no ca <pron> A ca B ca nānusenti" = «…, nhưng ở <pron> A và B vẫn nằm sẵn»
  sentence() / answers()          C's answers + apariyāpanne / sabbattha heads + "…pe…." cuts («…», spacing kept)
  cut_question()                  "(Kha) yattha vā pana…pe…?" = «(b) Còn ở nơi nào mà… không?»
  FIXED                           "Anusayavāre paṭilomaṃ." / "Anusayavāro." closing lines
Later chapters import it with importlib.import_module("build_rails_7-02_vi"). Importing writes nothing.
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-02_vi.py
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

C = importlib.import_module("build_rails_7-01_vi")  # family C setter (READ-ONLY)

CHAPTER = "7-02-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-02.md"
ADH_DIR = RAILS_DIR / "adh-7-02"
cap = S.cap
PE = S.PE                                   # …pe… = «…» (a final «.» after …pe… is absorbed)

# ---------------------------------------------------------------------------------------------------------------
# 1. New places
# ---------------------------------------------------------------------------------------------------------------
APARIYAPANNA = "không nằm trong các cõi tồn tại"         # apariyāpanna (pi-1 ^1-M2-96, pi-2 khandhavibhaṅga)
APARIYAPANNE = f"những gì {APARIYAPANNA}"                # apariyāpanne (loc. sg. neuter: "in what is not included")
SABBATTHA = "mọi nơi"                                    # sabbattha: every plane (coordinator; pi-5 «ở mọi nơi»)
PLACE_LOC = {**C.PLACE_LOC, "apariyāpanne": APARIYAPANNE}
PERSON_GEN = C.PERSON_GEN
AT, THEN, BUT, ALSO, AND, STILL = C.AT, C.THEN, C.BUT, C.ALSO, C.AND, C.STILL


# ---------------------------------------------------------------------------------------------------------------
# 2. Clauses (C's for positive verbs; the same shapes for negative verbs)
# ---------------------------------------------------------------------------------------------------------------
def clause_vi(groups):
    """One group: «<run> V». Two groups, each with 'ca', same polarity (A ca V B ca V): «A V, B cũng V»."""
    if len(groups) == 2 and all(tp["conj"] for tp, _ in groups) and not any(v[2] for _, v in groups):
        (t1, v1), (t2, v2) = groups
        return f"{C.tp_vi(t1)} {v1[0]}, {C.tp_vi(t2)} {ALSO} {v2[0]}"
    return C.clause_vi(groups)


def neg_clause_vi(groups):
    """After 'no ca <pron>': C's frames; a negative verb with a list (both denied the negation) =
    «A và B vẫn nằm sẵn» / «A, B và C vẫn nằm sẵn» (coordinator, From rails 7-01)."""
    if len(groups) == 1:
        tp, v = groups[0]
        if not v[2] and len(tp["names"]) > 1:
            if tp["pe"] or not tp["conj"]:
                raise ValueError("…pe… / no 'ca' in a 'no ca' list: " + repr(tp))
            return f"{C.tp_vi(tp)} {STILL} {v[3]}"
    return C.neg_clause_vi(groups)


# ---------------------------------------------------------------------------------------------------------------
# 3. Answer heads (C's rules + apariyāpanne + "<person> sabbattha")
# ---------------------------------------------------------------------------------------------------------------
def parse_head(txt):
    """'<person>? <places>* <resumptive>?' or '<person> sabbattha' → (person | None, [places], resumptive)."""
    person, rest = C._take(txt, PERSON_GEN)
    if person and rest == "sabbattha":
        return person, ["sabbattha"], ""
    places = []
    while rest:
        p, rest2 = C._take(rest, PLACE_LOC, fold=True)
        if not p:
            break
        places.append(p)
        rest = rest2
    if rest not in ("", "ettha", "tassa tattha", "tesaṃ tattha"):
        raise ValueError(f"unknown answer head {txt!r} (left: {rest!r})")
    if person and places and rest not in ("tassa tattha", "tesaṃ tattha"):
        raise ValueError(f"person + place without 'tassa / tesaṃ tattha': {txt!r}")
    if person and not places and rest:
        raise ValueError(f"person head with a resumptive: {txt!r}")
    if not person and places and rest != "ettha":
        raise ValueError(f"place head without 'ettha': {txt!r}")
    if not person and not places:
        raise ValueError(f"empty answer head: {txt!r}")
    if person and rest and rest.split()[0] != ("tassa" if PERSON_GEN[person][1] == 1 else "tesaṃ"):
        raise ValueError(f"resumptive number does not fit the person: {txt!r}")
    return person, places, rest


def head_vi(person, places, resumptive, cut=False):
    """«Ở <person>, ở <place>, …, » + «thì ở đó » / «thì ở người ấy, ở nơi ấy »; a head cut by …pe… ends «…»."""
    parts = ([f"{AT} {PERSON_GEN[person][0]}"] if person else []) + \
            [f"{AT} {SABBATTHA if p == 'sabbattha' else PLACE_LOC[p]}" for p in places]
    out = cap(", ".join(parts))
    if cut:
        if resumptive:
            raise ValueError("cut head with a resumptive")
        return out
    out += ", "
    if resumptive == "ettha":
        out += C.ETTHA + " "
    elif resumptive:
        out += f"{THEN} {AT} {C.pron_vi(resumptive)} "
    return out


# ---------------------------------------------------------------------------------------------------------------
# 4. Sentences
# ---------------------------------------------------------------------------------------------------------------
CUT_RE = re.compile(r"(.+?)( ?)…pe…\.")


def core(s):
    """One answer sentence without its final «.» → Vietnamese without the final «.»."""
    if s + "." in C.EXACT:
        return C.EXACT[s + "."][:-1]
    m = C.SENT_RE.fullmatch(s + ".")
    if not m:
        raise ValueError(f"unknown sentence {s!r}")
    words = m.group(1).split()
    i = next((k for k, w in enumerate(words) if C.is_anusaya(w.split("…")[0])), None)
    if not i:
        raise ValueError(f"no head / no tendency in {s!r}")
    person, places, res = parse_head(" ".join(words[:i]))
    out = head_vi(person, places, res) + clause_vi(C.parse_clause(" ".join(words[i:])))
    if m.group(2):
        if places == ["sabbattha"]:
            raise ValueError(f"'no ca' after sabbattha: not decided: {s!r}")
        pron = m.group(2)
        want = (res if res and res != "ettha" else
                ("tattha" if not person else ("tassa" if PERSON_GEN[person][1] == 1 else "tesaṃ")))
        if pron != want:
            raise ValueError(f"'no ca {pron}' does not fit the head ({want}): {s!r}")
        out += f", {BUT} {AT} {C.pron_vi(pron)} {neg_clause_vi(C.parse_clause(m.group(3)))}"
    return out


def sentence(s):
    """Āmantā. / No. / Natthi. / <head> <clause>[, no ca <pron> <clause>]. ; '<…>…pe….' (cut) = «<…>…»
    (' …pe….' = « …»); '<person> sabbattha…pe….' = «Ở <person>, ở mọi nơi…»."""
    if s in C.EXACT:
        return C.EXACT[s]
    if m := CUT_RE.fullmatch(s):
        body, gap = m.group(1), (" " if m.group(2) else "") + PE
        if C.SENT_RE.fullmatch(body + ".") is None or not any(C.is_anusaya(w) for w in body.split()):
            if body + "." in C.EXACT:
                return core(body) + gap
            person, places, res = parse_head(body)           # a head alone, cut
            return head_vi(person, places, res, cut=True) + gap
        return core(body) + gap
    if not s.endswith("."):
        raise ValueError(f"sentence without a final «.»: {s!r}")
    return core(s[:-1]) + "."


def answers(text):
    parts = [x for x in re.split(r"(?<=\.) ", text.strip()) if x]
    return " ".join(sentence(x) for x in parts)


# ---------------------------------------------------------------------------------------------------------------
# 5. Questions (C's shell); a question cut right after the relative
# ---------------------------------------------------------------------------------------------------------------
CUTQ_RE = re.compile(r"\((Ka|Kha)\) (yassa|yattha|yassa yattha)( vā pana)?…pe…\?(?: (.+))?")


def cut_question(body):
    """'(Kha) yattha vā pana…pe…?' = «(b) Còn ở nơi nào mà… không?» (sample ^6-1-98: «… không?»)."""
    m = CUTQ_RE.fullmatch(body)
    if not m:
        return None
    label, rel, vapana, rest = m.groups()
    if (label == "Kha") != bool(vapana):
        raise ValueError(f"label {label} with vā pana={bool(vapana)}: {body!r}")
    who = C.Q_REL[rel][0]
    s = f"{C.VA_PANA + ' ' + AT if vapana else cap(AT)} {who} mà{PE} không?"
    return f"{S.LABEL[label]} {s}" + (" " + answers(rest) if rest else "")


def question(body):
    m = C.Q_RE.fullmatch(body)
    if not m:
        return None
    rest = m.group(9)
    q = body[:len(body) - len(rest) - 1] if rest else body
    out = C.question(q)
    if out is None:
        raise ValueError(f"question shell failed: {body!r}")
    return out + (" " + answers(rest) if rest else "")


# ---------------------------------------------------------------------------------------------------------------
# 6. Fixed lines, line translator, build
# ---------------------------------------------------------------------------------------------------------------
PATILOMA = cap(C.HEADINGS["paṭiloma"])                   # paṭilomaṃ «chiều ngược» (termbase; S.LATER_HEADINGS)
ANUSAYAVARO_LC = C.ANUSAYAVARO[0].lower() + C.ANUSAYAVARO[1:]
FIXED = {
    "Anusayavāre paṭilomaṃ.": f"{PATILOMA} trong {ANUSAYAVARO_LC}.",   # as C's «Chiều thuận trong mục về …»
    "Anusayavāro.": C.ANUSAYAVARO + ".",                              # closing label, as C's «Mục về nơi sinh khởi.»
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
        elif (q := cut_question(body)) is not None:
            out = q
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


REUSED = [   # (Pāli, Vietnamese, book): asserted in that book's approved rails
    ("apariyāpannā dhammā", "Các hiện tượng " + APARIYAPANNA, "1"),
    ("atthi apariyāpanno", "có loại " + APARIYAPANNA, "2"),
    ("sabbattha", f"{AT} {SABBATTHA}", "5"),
]
TERMBASE_USED = [
    ("nānuseti", "không " + C.LIE_LATENT), ("nānusenti", "không " + C.LIE_LATENT),
    ("nānusentīti", "không " + C.LIE_LATENT), ("paṭilomaṃ", "chiều ngược"),
    ("Anusayavāra", "mục về khuynh hướng tiềm ẩn"), ("Anusayavāre", "mục về khuynh hướng tiềm ẩn"),
    ("anusayavāro", "mục về khuynh hướng tiềm ẩn"),
    ("paṭilomapuggalo", "chiều ngược theo người"), ("paṭilomaokāso", "chiều ngược theo nơi chốn"),
    ("paṭilomapuggalokāsā", "chiều ngược theo người và nơi chốn"), ("arahato", "bậc A-la-hán"),
]


def check_reused():
    C.check_reused()
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    tb = C.TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M)]
    assert not bad, "termbase strings not found: " + repr(bad)


def check_family():
    """The 7-01 strings this chapter shares stay byte-identical (positive frames through C's own code)."""
    for p in ("Anāgāmissa mānānusayo anuseti, no ca tassa kāmarāgānusayo anuseti.",
              "Tiṇṇaṃ puggalānaṃ avijjānusayo ca anuseti kāmarāgānusayo ca paṭighānusayo ca anusenti.",
              "Rūpadhātuyā arūpadhātuyā ettha mānānusayo anuseti, no ca tattha kāmarāgānusayo ca paṭighānusayo ca anusenti.",
              "Tesaññeva puggalānaṃ kāmadhātuyā dvīsu vedanāsu tesaṃ tattha mānānusayo ca anuseti kāmarāgānusayo ca anuseti."):
        assert sentence(p) == C.sentence(p), p


# ---------------------------------------------------------------------------------------------------------------
# 7. Notes
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-02 (Anusayayamaka, anusayavāra paṭiloma): new frames and fixed strings", "",
         "Generated by build_rails_7-02_vi.py. Family C strings come from build_rails_7-01_vi (imported, unchanged; "
         "see notes-rails-7-01.md). Later chapters import this module (importlib.import_module(\"build_rails_7-02_vi\")) "
         "for the negative frames and the …pe… cuts. (pi-N) = taken unchanged from that book's approved rails (asserted).",
         ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    neg = "không " + C.LIE_LATENT
    h("Places")
    row("apariyāpanne … (answer head; its own «ở»)", f"{AT} {APARIYAPANNE}  (apariyāpanna «{APARIYAPANNA}», pi-1 / pi-2)")
    row("<person> sabbattha … (no resumptive)", f"{cap(AT)} <người>, {AT} {SABBATTHA}, …  (pi-5 «ở mọi nơi»)")
    h("Negative (paṭiloma) frames")
    row("A nānuseti / A ca B ca nānusenti", f"A {neg} / A {AND} B {neg}")
    row("A ca nānuseti B ca nānuseti (both)", f"A {neg}, B {ALSO} {neg}")
    row("A ca B ca nānusenti C ca nānuseti", f"A {AND} B {neg}, C {ALSO} {neg}")
    row(", no ca tassa A nānuseti", f", {BUT} {AT} người ấy A {STILL} {C.LIE_LATENT}  (7-01 / coordinator)")
    row(", no ca tesaṃ A ca B ca nānusenti", f", {BUT} {AT} những người ấy A {AND} B {STILL} {C.LIE_LATENT}  (coordinator)")
    row(", no ca tesaṃ A ca B ca C ca nānusenti", f", {BUT} {AT} những người ấy A, B {AND} C {STILL} {C.LIE_LATENT}")
    row("(Ka) yassa A nānuseti tassa B nānusetīti?", C.pair_q("yassa", "A " + neg, "B " + neg, "Ka"))
    h("…pe… cuts")
    row("<sentence>…pe…. / <sentence> …pe….", f"<câu>{PE} / <câu> {PE}")
    row("Āmantā …pe….", f"{C.YES[:-1]} {PE}")
    row("Dvinnaṃ puggalānaṃ sabbattha…pe….", sentence("Dvinnaṃ puggalānaṃ sabbattha…pe…."))
    row("Arahato sabbattha…pe….", sentence("Arahato sabbattha…pe…."))
    row("(Kha) yattha vā pana…pe…?", cut_question("(Kha) yattha vā pana…pe…?"))
    h("Closing lines")
    for k, v in FIXED.items():
        row(k, v)
    o.append("")
    o.append("Examples (built by the module):")
    for p in ("Anāgāmissa kāmarāgānusayo nānuseti, no ca tassa mānānusayo nānuseti.",
              "Arahato kāmarāgānusayo ca paṭighānusayo ca nānusenti mānānusayo ca nānuseti.",
              "Dvinnaṃ puggalānaṃ vicikicchānusayo nānuseti, no ca tesaṃ kāmarāgānusayo ca paṭighānusayo ca nānusenti.",
              "Rūpadhātuyā arūpadhātuyā apariyāpanne ettha kāmarāgānusayo ca nānuseti paṭighānusayo ca nānuseti.",
              "Dvinnaṃ puggalānaṃ sabbattha kāmarāgānusayo ca nānuseti paṭighānusayo ca nānuseti."):
        row(p, sentence(p))
    h("Open for the coordinator")
    row("apariyāpanne (no pi-6 termbase entry)", f"«{APARIYAPANNE}» (built from pi-1 / pi-2 apariyāpanna)")
    row("sabbattha (no pi-6 termbase entry)", f"«{AT} {SABBATTHA}» (coordinator rule)")
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


if __name__ == "__main__":
    main()
