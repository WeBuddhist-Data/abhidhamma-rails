"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-09 (Anusayayamaka: pahīnavāra, anuloma: person, place,
person + place; paṭiloma: person).

Imports (all READ-ONLY; importing writes nothing, outputs are written only under `if __name__ == "__main__":`):
  S  build_rails_sample_vi   labels, «…», var(), checks
  C  build_rails_7-01_vi     family C setter: tendencies, runs (parse_tp / tp_vi), the question shell (Q_RE,
                             question), connectors, EXACT answers, FAMILY_TERMS, headings, MULAKA, write()
  T2 build_rails_7-02_vi     answer heads (parse_head / head_vi with apariyāpanne / sabbattha / cut heads), CUT_RE,
                             cut_question, FIXED (for the 7-02 rebuild check)
  R7 build_rails_7-07_vi     the Verb class (pos / neg / still / Pāli forms) used here for a nominative predicate
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; P9 = importlib.import_module("build_rails_7-09_vi")

NEW FRAME (exposed for 7-10, 7-11 and any chapter whose subject is a tendency in the nominative): 7-01's
anuseti frames (A V; both-frame «A V, B cũng V»; «…, nhưng ở <pron> không có A, cũng không có B V»; a denied
negative «…, nhưng ở <pron> A [và B] <still>») coded ONCE with the predicate as a parameter (R7.Verb):
  ANUSETI   anuseti / anusenti / nānuseti / nānusenti (7-01 / 7-02 strings; check_family() rebuilds 7-01 and 7-02
            with it and asserts both are byte-identical to their chapter files)
  PAHINA    pahīno / pahīnā «đã được dứt bỏ», appahīno / appahīnā «chưa được dứt bỏ» (termbase, C.FAMILY_TERMS);
            a denied appahīno after "no ca" = «đã được dứt bỏ» (as a denied «chưa từng V» = «đã từng V», 2-01:
            «đã được» answers «chưa được»; no «vẫn» before «đã»)
  nv_vi()   na vattabbo / na vattabbā "P"ti vā "N"ti vā = «không nên nói là “P” hay “N”» (user decision
            na vattabbo «không nên nói là …»; pi-5 «không nên nói là X hay Y»); with a subject run
            «<A [và B]> thì không nên nói là “…” hay “…”»; standalone «Không nên nói là “…” hay “…”.»
  parse_clause() / clause_vi() / noca_vi() / core() / sentence() / answers() / question() / tr_line() / build()
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-09_vi.py
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
R7 = importlib.import_module("build_rails_7-07_vi")   # READ-ONLY (Verb class)

CHAPTER = "7-09-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-09.md"
ADH_DIR = RAILS_DIR / "adh-7-09"
cap = S.cap
PE = S.PE
SEEN = {"punct": [], "noca_comma": [], "semi_both": [], "comma_both": [], "slips": [], "bare": [], "var": []}

# ---------------------------------------------------------------------------------------------------------------
# 1. Predicates (nominative subject + finite verb or participle): R7.Verb(pos, neg, still, {Pāli: (negative?, n)})
# ---------------------------------------------------------------------------------------------------------------
ANUSETI = R7.Verb(C.LIE_LATENT, "không " + C.LIE_LATENT, f"{C.STILL} {C.LIE_LATENT}",
                  {"anuseti": (False, 1), "anusenti": (False, 2), "nānuseti": (True, 1), "nānusenti": (True, 2),
                   "anusanti": (False, 2)})                        # anusanti: 7-01 slip for anusenti (C.VERB_SLIPS)
assert ANUSETI.pos == C.VERB["anuseti"][0] and ANUSETI.neg == C.VERB["nānuseti"][0]

PAHINO = C.FAMILY_TERMS["pahīno"]           # «đã được dứt bỏ» (termbase pahīno / pahīnā)
APPAHINO = C.FAMILY_TERMS["appahīno"]       # «chưa được dứt bỏ» (termbase appahīno / appahīnā)
DENIED_APPAHINO = PAHINO                    # "no ca … appahīno": the negative is denied = «đã được dứt bỏ»
PAHINA = R7.Verb(PAHINO, APPAHINO, DENIED_APPAHINO,
                 {"pahīno": (False, 1), "pahīnā": (False, 2), "appahīno": (True, 1), "appahīnā": (True, 2)})
assert (PAHINO, APPAHINO) == ("đã được dứt bỏ", "chưa được dứt bỏ")

NA_VATTABBO = C.FAMILY_TERMS["na vattabbo"]   # «không nên nói là» (user decision)
OR = "hay"                                    # "X"ti vā "Y"ti vā (pi-5 «không nên nói là người ấy hay người khác»)
NV_RE = re.compile(r'(?:(.+?) )?([Nn])a vattabb(o|ā) "(\S+?)"ti vā "(\S+?)"ti vā')


def _lc(t):
    return t[:1].lower() + t[1:]


def _is_tend(w):
    return C.is_anusaya(_lc(w).split("…")[0])


def nv_phrase(V, n):
    """«không nên nói là “P” hay “N”» (P / N = the predicate's positive / negative Vietnamese)."""
    return f"{NA_VATTABBO} “{V.pos}” {OR} “{V.neg}”"


def nv_vi(m, V):
    """NV_RE match → «<subject> thì không nên nói là “P” hay “N”» / «Không nên nói là “P” hay “N”»."""
    subj, big_n, ending, q1, q2 = m.groups()
    n = 1 if ending == "o" else 2
    if V.forms.get(q1) != (False, n) or V.forms.get(q2) != (True, n):
        raise ValueError(f"quoted predicates {q1!r} / {q2!r} do not fit vattabb{ending}: {m.group(0)!r}")
    if subj is None:
        if big_n != "N":
            raise ValueError(f"standalone na vattabbo in lower case: {m.group(0)!r}")
        return cap(nv_phrase(V, n))
    if big_n != "n":
        raise ValueError(f"capital Na after a subject: {m.group(0)!r}")
    tp = C.parse_tp(_lc(subj))
    if tp["pe"]:
        raise ValueError(f"…pe… in a na vattabbo subject: {subj!r}")
    if (n == 2) != (len(tp["names"]) > 1 and tp["conj"]):
        raise ValueError(f"vattabb{ending} does not fit its subject: {m.group(0)!r}")
    return f"{C.tp_vi(tp)} {C.THEN} {nv_phrase(V, n)}"


# ---------------------------------------------------------------------------------------------------------------
# 2. Clauses: '<run> V [<run> V]' (7-01 parse_clause with the predicate as a parameter)
# ---------------------------------------------------------------------------------------------------------------
def parse_clause(text, V):
    """→ [(tp, negative?, number), …] (one or two groups, one polarity); number checked against the run."""
    t = _lc(text.strip())
    if m := V.comma_re.search(t):            # ^6-7-307 «… appahīno, kāmarāgānusayo ca … appahīnā»
        SEEN["comma_both"].append(t[max(0, m.start() - 40):m.end() + 30])
        t = V.comma_re.sub(lambda mm: f" {mm.group(1)} ", t)
    parts = V.re.split(" " + t)
    if parts[-1].strip() or len(parts) < 3:
        raise ValueError(f"clause does not end in a predicate: {text!r}")
    groups = []
    for run, f in zip(parts[0:-1:2], parts[1::2]):
        tp = C.parse_tp(run.strip())
        if f in C.VERB_SLIPS:
            SEEN["slips"].append((f, C.VERB_SLIPS[f]))
        neg, num = V.forms[f]
        plural = len(tp["names"]) > 1 and tp["conj"]
        if (num == 2) != plural:
            raise ValueError(f"predicate number does not fit its subject: {text!r}")
        groups.append((tp, neg, num))
    if len(groups) > 2 or len({g[1] for g in groups}) != 1:
        raise ValueError(f"more than two groups / mixed polarity in {text!r}")
    return groups


def clause_vi(groups, V, sep=", "):
    """«<run> V»; both-frame 'A ca V B ca V' «A V, B cũng V» (7-01 / 7-02; sep = the Pāli's «;» where it has one)."""
    word = V.neg if groups[0][1] else V.pos
    if len(groups) == 1:
        return f"{C.tp_vi(groups[0][0])} {word}"
    (t1, _, _), (t2, _, _) = groups
    if t1["conj"] and t2["conj"]:
        return f"{C.tp_vi(t1)} {word}{sep}{C.tp_vi(t2)} {C.ALSO} {word}"
    raise ValueError("unknown clause shape: " + repr(groups))


def noca_vi(groups, V):
    """After 'no ca <pron>': positive «không có A[, cũng không có B] V» (7-01, user "neither" rule);
    negative (denied) «A [và B] <still>» (7-01 / 7-02; pahīna: «A [và B] đã được dứt bỏ»)."""
    if len(groups) != 1:
        raise ValueError("no ca with more than one predicate: " + repr(groups))
    tp, neg, _ = groups[0]
    if tp["pe"]:
        raise ValueError("…pe… inside a 'no ca' part: " + repr(tp))
    if not neg:
        return f"{C.NEITHER_FIRST} " + f", {C.NEITHER_NEXT} ".join(tp["names"]) + f" {V.pos}"
    if len(tp["names"]) > 1 and not tp["conj"]:
        raise ValueError("no 'ca' in a 'no ca' list: " + repr(tp))
    return f"{C.tp_vi(tp)} {V.still}"


# ---------------------------------------------------------------------------------------------------------------
# 3. Sentences
# ---------------------------------------------------------------------------------------------------------------
NOCA_RE = re.compile(r"(.+?)(,?) no ca (tassa tattha|tesaṃ tattha|tassa|tesaṃ|tattha) (.+)")


def first_part(p, V, sep=", "):
    """'[<head>] <clause>[, no ca <pron> <clause>]' or a na vattabbo part (standalone or with a subject run)."""
    if m := NV_RE.fullmatch(p):
        return nv_vi(m, V)
    mn = NOCA_RE.fullmatch(p)
    main = mn.group(1) if mn else p
    words = main.split()
    i = next((k for k, w in enumerate(words) if _is_tend(w)), None)
    if i is None:
        raise ValueError(f"no tendency in {p!r}")
    groups = parse_clause(" ".join(words[i:]), V)
    if i == 0:                                      # bare answer «Khuynh hướng tiềm ẩn … đã được dứt bỏ»
        if mn:
            raise ValueError(f"bare answer with 'no ca': not decided: {p!r}")
        SEEN["bare"].append(p)
        return cap(clause_vi(groups, V, sep))
    if words[i][0].isupper():
        raise ValueError(f"capital tendency after a head: {p!r}")
    person, places, res = T2.parse_head(" ".join(words[:i]))
    out = T2.head_vi(person, places, res) + clause_vi(groups, V, sep)
    if mn:
        if places == ["sabbattha"]:
            raise ValueError(f"'no ca' after sabbattha: not decided: {p!r}")
        if not mn.group(2):                         # coordinator: a missing comma before "no ca" is added
            SEEN["noca_comma"].append(p)
        pron = mn.group(3)
        want = (res if res and res != "ettha" else
                ("tattha" if not person else ("tassa" if C.PERSON_GEN[person][1] == 1 else "tesaṃ")))
        if pron != want:
            raise ValueError(f"'no ca {pron}' does not fit the head ({want}): {p!r}")
        out += f", {C.BUT} {C.AT} {C.pron_vi(pron)} {noca_vi(parse_clause(mn.group(4), V), V)}"
    return out


def later_part(p, V):
    """A part after the Pāli's «;»: '<run> na vattabbo "P"ti vā "N"ti vā' (lower case, no head)."""
    m = NV_RE.fullmatch(p)
    if not m or m.group(1) is None:
        raise ValueError(f"unknown part after ';': {p!r}")
    return nv_vi(m, V)


def core(s, V):
    """One answer sentence without its final «.» → Vietnamese without the final «.»; parts split at the Pāli's «; »
    (kept as «; »). A part 'A ca V' followed by '; B ca … V' is one both-frame (^6-7-306): «A V; B … cũng V»."""
    if s + "." in C.EXACT:
        return C.EXACT[s + "."][:-1]
    parts = s.split("; ")
    if len(parts) == 2 and "vattabb" not in s and _is_tend(parts[1].split()[0]) and parts[1][:1].islower():
        SEEN["semi_both"].append(s[:90])
        return first_part(parts[0] + " " + parts[1], V, sep="; ")
    out = [first_part(parts[0], V)]
    out += [later_part(p, V) for p in parts[1:]]
    return "; ".join(out)


def sentence(s, V=PAHINA):
    """Āmantā. / No. / Natthi. / <core>. ; '<…>…pe….' / '<…> …pe….' (cut) = «<…>…» / «<…> …» (7-02)."""
    if s in C.EXACT:
        return C.EXACT[s]
    if m := T2.CUT_RE.fullmatch(s):
        body, gap = m.group(1), (" " if m.group(2) else "") + PE
        if not any(C.is_anusaya(w) for w in body.split()):
            if body + "." in C.EXACT:
                return core(body, V) + gap
            person, places, res = T2.parse_head(body)       # a head alone, cut (7-02)
            return T2.head_vi(person, places, res, cut=True) + gap
        return core(body, V) + gap
    if not s.endswith("."):
        raise ValueError(f"sentence without a final «.»: {s!r}")
    return core(s[:-1], V) + "."


def answers(text, V=PAHINA):
    parts = [x for x in re.split(r"(?<=\.) ", text.strip()) if x]
    return " ".join(sentence(x, V) for x in parts)


# ---------------------------------------------------------------------------------------------------------------
# 4. Questions: C's shell (C.Q_RE / C.question) with this module's slot renderer; variant brackets in slot A
# ---------------------------------------------------------------------------------------------------------------
VAR_RE = re.compile(r" (\[[^\]]+\])")
VARIANTS = {   # Pāli bracket → Vietnamese (sigla as the sample / 2-01; "pana sameti" = pi-4 «; nhưng phù hợp với»)
    "[pahīno (sī. ka.) anusayavārena pana na sameti]":
        S.var("Sī., Ka.", f"pahīno; {C.BUT} không phù hợp với {_lc(C.ANUSAYAVARO)}"),
}


def slot_vi(t, V):
    return clause_vi(parse_clause(t, V), V)


def question(body, V=PAHINA):
    m = C.Q_RE.fullmatch(body)
    if not m:
        return None
    rest = m.group(9)
    q = body[:len(body) - len(rest) - 1] if rest else body
    var = None
    if mv := VAR_RE.search(q):
        br = mv.group(1)
        if br not in VARIANTS:
            raise ValueError(f"unknown variant {br!r}")
        q = q[:mv.start()] + q[mv.end():]
        var = (br, VARIANTS[br])
        mq = C.Q_RE.fullmatch(q)
        if not mq or not q[:mv.start()].endswith(mq.group(6)):
            raise ValueError(f"variant not at the end of slot A: {body!r}")
    out = C.question(q, clause=lambda t: slot_vi(t, V))
    if out is None:
        raise ValueError(f"question shell failed: {body!r}")
    if var:
        a_vi = slot_vi(C.Q_RE.fullmatch(q).group(6), V)
        key = f"{a_vi}, {C.THEN} "
        if out.count(key) != 1:
            raise ValueError(f"cannot place the variant in {out!r}")
        out = out.replace(key, f"{a_vi} {var[1]}, {C.THEN} ")
        SEEN["var"].append(var)
    return out + (" " + answers(rest, V) if rest else "")


# ---------------------------------------------------------------------------------------------------------------
# 5. Headings, fixed lines, line translator
# ---------------------------------------------------------------------------------------------------------------
PAHINAVARO = C.HEADINGS["Pahīnavāro"]                 # «Mục về những gì đã được dứt bỏ» (S.LATER_HEADINGS)
assert PAHINAVARO == C.heading("Pahīnavāra") == C.FAMILY_HEADINGS["Pahīnavāra"]
PAHINAVARO_LC = _lc(PAHINAVARO)
FIXED = {   # built as 7-01 «Anusayavāre anulomaṃ.» / 7-05 «Pajahanavāre anulomaṃ.» / 7-07 «Pariññāvāre anulomaṃ.»
    "Pahīnavāre anulomaṃ.": f"{C.HEADINGS['anulomaṃ']} trong {PAHINAVARO_LC}.",
}
assert C.FIXED["Anusayavāre anulomaṃ."] == f"{C.HEADINGS['anulomaṃ']} trong {_lc(C.ANUSAYAVARO)}."
assert R7.FIXED["Pariññāvāre anulomaṃ."] == f"{C.HEADINGS['anulomaṃ']} trong {R7.PARINNAVARO_LC}."


def tr_line(p, V=PAHINA, fixed=None, hooks=()):
    fixed = FIXED if fixed is None else fixed
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
        out = fixed.get(body)
        for h in hooks:
            if out is None:
                out = h(body)
        if out is None:
            out = question(body, V)
        if out is None:
            out = answers(body, V)
        out += label
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER, V=PAHINA, fixed=None, hooks=()):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln, V, fixed, hooks))
            except ValueError as e:
                raise ValueError(f"{name}: cannot place line {ln[:120]!r}: {e}") from None
        segs.append(out)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# 6. Checks
# ---------------------------------------------------------------------------------------------------------------
REUSED = [   # (Pāli, Vietnamese, book): asserted in that book's approved rails
    ("na vattabbaṃ soti vā aññoti vā (pi-5 1-puggalakatha)", f"{NA_VATTABBO} người ấy {OR} người khác", "5"),
    ("rūpasiddhiṭīkāya pana sameti (pi-4 variant note)", f"; {C.BUT} phù hợp với", "4"),
]
TERMBASE_USED = [
    ("pahīno", PAHINO), ("pahīnoti", PAHINO), ("pahīnā", PAHINO), ("pahīnāti", PAHINO),
    ("appahīno", APPAHINO), ("appahīnā", APPAHINO), ("appahīnoti", APPAHINO), ("appahīnāti", APPAHINO),
    ("Pahīnavāro", PAHINAVARO_LC), ("Pahīnavāra", PAHINAVARO_LC), ("Pahīnavāre", PAHINAVARO_LC),
    ("anulomaṃ", "chiều thuận"), ("anulomapuggalo", "chiều thuận theo người"),
    ("anulomaokāso", "chiều thuận theo nơi chốn"), ("anulomapuggalokāsā", "chiều thuận theo người và nơi chốn"),
    ("paṭilomapuggalo", "chiều ngược theo người"), ("Natthi", "không có"), ("arahato", "bậc A-la-hán"),
    ("Anāgāmissa", "bậc không trở lại"), ("Puthujjanassa", "người phàm phu"), ("puggalānaṃ", "hạng người"),
    ("puggalassa", "hạng người"), ("Kāmadhātuyā", "cõi dục lạc"), ("rūpadhātuyā", "cõi hình sắc"),
    ("arūpadhātuyā", "cõi không hình sắc"), ("dvīsu vedanāsu", "hai loại cảm giác"),
    ("tīsu vedanāsu", "ba loại cảm giác"), ("Dukkhāya vedanāya", "cảm giác khó chịu"),
    ("anusayavāro", _lc(C.ANUSAYAVARO)),
]
USER_DECISIONS = ["na vattabbo «không nên nói là …»"]


def check_reused():
    C.check_reused()
    T2.check_reused()
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
    """7-01 and 7-02 rebuilt here with the ANUSETI predicate = their chapter files, byte for byte."""
    saved = {k: list(v) for k, v in SEEN.items()}
    for name, fixed, hooks in (("7-01-anusayayamaka.md", C.FIXED, (C.kattha,)),
                               ("7-02-anusayayamaka.md", T2.FIXED, (T2.cut_question,))):
        mine = unicodedata.normalize("NFC", "\n\n".join("\n".join(s) for s in build(name, ANUSETI, fixed, hooks))
                                     + "\n")
        theirs = (S.OUT_DIR / name).read_text(encoding="utf-8")
        if mine != theirs:
            a, b = mine.splitlines(), theirs.splitlines()
            diff = [(x, y) for x, y in zip(a, b) if x != y]
            raise AssertionError(f"{name} rebuilt differs: {diff[:2]}")
    for k in SEEN:
        SEEN[k][:] = saved[k]


# ---------------------------------------------------------------------------------------------------------------
# 7. Notes
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-09 (Anusayayamaka, pahīnavāra anuloma + paṭiloma by person): frames and fixed strings", "",
         "Generated by build_rails_7-09_vi.py. Imports S, C (7-01, family C setter), 7-02 (answer heads, cuts) and "
         "7-07 (the Verb class): their strings, byte for byte. New: 7-01's nominative-subject frames coded once with "
         "the predicate as a parameter (ANUSETI, PAHINA); the builder rebuilds 7-01 and 7-02 with ANUSETI and asserts "
         "both equal their chapter files. Later chapters import the module "
         "(importlib.import_module(\"build_rails_7-09_vi\")) and pass PAHINA (or their own R7.Verb).", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    V = PAHINA
    h("Predicate (termbase pahīno «đã được dứt bỏ», appahīno «chưa được dứt bỏ»; distinct pair)")
    row("pahīno / pahīnā (pahīnoti / pahīnāti)", V.pos)
    row("appahīno / appahīnā (appahīnoti / appahīnāti)", V.neg)
    row("no ca … appahīno / appahīnā (negative denied)",
        f"{V.still}  (no «vẫn» before «đã», as 2-01's «đã từng V» for a denied «chưa từng V»; for review)")
    h("Clauses (= 7-01 / 7-02 with «đã được dứt bỏ»)")
    row("A pahīno", f"A {V.pos}")
    row("A ca B ca pahīnā", f"A {C.AND} B {V.pos}")
    row("A…pe… B pahīno (cut)", f"A… B {V.pos}")
    row("A ca pahīno B ca [C ca] pahīno / pahīnā (both)", f"A {V.pos}, B [{C.AND} C] {C.ALSO} {V.pos}")
    row("A ca appahīno B ca appahīno (both)", f"A {V.neg}, B {C.ALSO} {V.neg}")
    row("A ca appahīno; B ca … appahīnā (the Pāli's «;», ^6-7-306)", f"A {V.neg}; B … {C.ALSO} {V.neg}")
    row("A ca appahīno, B ca … appahīnā (the Pāli's comma, ^6-7-307)", f"A {V.neg}, B … {C.ALSO} {V.neg}")
    row(", no ca <pron> A [ca B ca] pahīno / pahīnā",
        f", {C.BUT} {C.AT} <pron> {C.NEITHER_FIRST} A[, {C.NEITHER_NEXT} B] {V.pos}")
    row(", no ca <pron> A [ca B ca] appahīno / appahīnā", f", {C.BUT} {C.AT} <pron> A [{C.AND} B] {V.still}")
    h("na vattabbo (new frame; user decision «không nên nói là …»; «hay» = pi-5)")
    row('Na vattabbo "pahīno"ti vā "appahīno"ti vā.', sentence('Na vattabbo "pahīno"ti vā "appahīno"ti vā.'))
    row('Na vattabbā "pahīnā"ti vā "appahīnā"ti vā.', sentence('Na vattabbā "pahīnā"ti vā "appahīnā"ti vā.'))
    row('…; A na vattabbo "pahīno"ti vā "appahīno"ti vā', f"…; A {C.THEN} {nv_phrase(V, 1)}")
    row('…; A ca B ca na vattabbā "pahīnā"ti vā "appahīnā"ti vā', f"…; A {C.AND} B {C.THEN} {nv_phrase(V, 2)}")
    h("Questions (C's shell)")
    a, b = f"A {V.pos}", f"B {V.pos}"
    row("(Ka) yassa A pahīno tassa B pahīnoti?", C.pair_q("yassa", a, b, "Ka"))
    row("(Kha) yattha vā pana B pahīno tattha A pahīnoti?", C.pair_q("yattha", b, a, "Kha", True))
    row("(Ka) yassa yattha A pahīno tassa tattha B pahīnoti?", C.pair_q("yassa yattha", a, b, "Ka"))
    row("(Ka) yassa A appahīno tassa B appahīnoti?", C.pair_q("yassa", f"A {V.neg}", f"B {V.neg}", "Ka"))
    h("Variant, fixed lines")
    for k, v in VARIANTS.items():
        row(k, v + "  (anusayavāra «mục về khuynh hướng tiềm ẩn», termbase; «; nhưng phù hợp với» = pi-4 "
                   "«rūpasiddhiṭīkāya pana sameti»; sameti: no pi-6 termbase entry)")
    for k, v in FIXED.items():
        row(k, v)
    o.append("")
    o.append("Examples (built by the module):")
    for p in ("Anāgāmissa kāmarāgānusayo pahīno, no ca tassa mānānusayo pahīno.",
              "Arahato kāmarāgānusayo ca paṭighānusayo ca pahīnā mānānusayo ca pahīno.",
              'Rūpadhātuyā arūpadhātuyā ettha mānānusayo pahīno; kāmarāgānusayo na vattabbo "pahīno"ti vā '
              '"appahīno"ti vā.',
              'Mānānusayo pahīno; kāmarāgānusayo ca paṭighānusayo ca na vattabbā "pahīnā"ti vā "appahīnā"ti vā.',
              'Tesaññeva puggalānaṃ kāmadhātuyā dvīsu vedanāsu tesaṃ tattha vicikicchānusayo pahīno, no ca tesaṃ '
              'tattha kāmarāgānusayo ca mānānusayo ca pahīnā; paṭighānusayo na vattabbo "pahīno"ti vā "appahīno"ti vā.',
              "Anāgāmissa mānānusayo appahīno, no ca tassa kāmarāgānusayo appahīno.",
              "Anāgāmissa avijjānusayo ca mānānusayo ca appahīnā, no ca tassa kāmarāgānusayo ca paṭighānusayo ca "
              "appahīnā.",
              "Puthujjanassa avijjānusayo ca appahīno; kāmarāgānusayo ca paṭighānusayo ca mānānusayo ca "
              "diṭṭhānusayo ca vicikicchānusayo ca appahīnā."):
        row(p, sentence(p))
    h("Pāli as written / punctuation (reported)")
    for s in sorted(set(SEEN["semi_both"])):
        o.append(f"- «;» inside a both-frame, kept: {s}…")
    for s in sorted(set(SEEN["comma_both"])):
        o.append(f"- comma inside a both-frame: …{s}…: the Vietnamese both-frame has that comma anyway")
    for s in sorted(set(SEEN["bare"])):
        o.append(f"- answer without a head (as written): {s[:90]}")
    for s in sorted(set(SEEN["noca_comma"])):
        o.append(f"- missing comma before no ca, added: {s[:80]}")
    o.append("- ^6-7-267 / ^6-7-278 / ^6-7-289 / ^6-7-300 / ^6-7-305 «Āmantā …pe….», ^6-7-272 / ^6-7-283 / ^6-7-294 "
             "«… …pe….»: «…pe…» → «…» (7-02 cut).")
    o.append("")
    return "\n".join(o)


def main():
    check_reused()
    check_family()
    n0 = len(C.SLIPS_SEEN)                  # slips seen while rebuilding 7-01 / 7-02 are theirs, not this chapter's
    segs = build(CHAPTER)
    C.write(CHAPTER, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for k, v in SEEN.items():
        for x in sorted(set(map(str, v))):
            print(f"{k}: {x[:120]}")
    for p, v in sorted(set(C.SLIPS_SEEN[n0:])):
        print("slip rendered as meant:", p, "→", v)


if __name__ == "__main__":
    main()
