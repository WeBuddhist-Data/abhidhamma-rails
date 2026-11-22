"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-07 (Anusayayamaka: pariññāvāra, anuloma: person, place,
person + place; paṭiloma: person, place).

Imports (all READ-ONLY; importing writes nothing, outputs are written only under `if __name__ == "__main__":`):
  S  build_rails_sample_vi   labels, «…», checks
  C  build_rails_7-01_vi     family C setter: tendencies, places, pronouns, connectors, headings, FAMILY_TERMS, write()
  T3 build_rails_7-03_vi     nominative yo / yato / yo yato shell (Q_RE, yo_q), pe_tail
  P5 build_rails_7-05_vi     pajahati anuloma frames: TADEKATTHA / TAD_JOIN, parse_run (accusative runs), persons
  R6 build_rails_7-06_vi     nappajahati paṭiloma frames: heads, persons, "<X> ṭhapetvā avasesā puggalā", «vẫn …»
  E  build_rails_2-02_vi     family E setter: parijānāti in every tense (E_VERBS, denied), except_head, yo_q
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; R7 = importlib.import_module("build_rails_7-07_vi")

The 7-05 / 7-06 frames are re-implemented here once, parameterised by a verb (Verb: positive, negative, «vẫn»
form, Pāli forms), so the same code builds the pajahati and the parijānāti chapters. check_family() rebuilds the
whole of 7-05 and 7-06 with the pajahati verb and asserts the result is byte-identical to their own builders.
Exposed for 7-08 … (pahīnavāra and later parijānāti / pajahati chapters):
  Verb / PARIJ / PAJ                  the two verbs (PARIJ strings from 2-02's E_VERBS, PAJ from 7-05 / 7-06)
  parse_clause() / pos_vi() / neg_vi() / noca_vi()
  sentence() / question() / body_vi() / tr_line() / build()
New here: a both-frame whose second part carries tadekaṭṭhaṃ ("A-ñca V B-ñca tadekaṭṭhaṃ V") =
«V A, cũng V B, vốn cùng hiện diện với nó».
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-07_vi.py
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
T3 = importlib.import_module("build_rails_7-03_vi")   # READ-ONLY
P5 = importlib.import_module("build_rails_7-05_vi")   # READ-ONLY
R6 = importlib.import_module("build_rails_7-06_vi")   # READ-ONLY
E = importlib.import_module("build_rails_2-02_vi")    # family E setter (READ-ONLY)

CHAPTER = "7-07-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-07.md"
ADH_DIR = RAILS_DIR / "adh-7-07"
cap = S.cap
SEEN = {"punct": [], "noca_comma": [], "mixed_q": [], "both_tad": []}   # reported by main() and the notes


# ---------------------------------------------------------------------------------------------------------------
# 1. Verbs
# ---------------------------------------------------------------------------------------------------------------
class Verb:
    """pos «V», neg «không V», still «vẫn V» (after no ca a negative verb is denied); forms: Pāli → (negative?, number)."""

    def __init__(self, pos, neg, still, forms):
        self.pos, self.neg, self.still, self.forms = pos, neg, still, dict(forms)
        alts = "|".join(sorted((re.escape(f) for f in forms), key=len, reverse=True))
        self.re = re.compile(r" (" + alts + r")(?= |$)")
        self.comma_re = re.compile(r" (" + alts + r"), (?=\S)")


PARIJ = Verb(E.E_VERBS["parijānāti"].vi,                       # «hiểu biết trọn vẹn» (termbase; 2-02)
             E.E_VERBS["na parijānāti"].vi,                    # «không hiểu biết trọn vẹn» (2-02 tense rule)
             E.denied(E.E_VERBS["na parijānāti"]),             # «vẫn hiểu biết trọn vẹn» (user decision 5)
             {"parijānāti": (False, 1), "parijānanti": (False, 2),
              "na parijānāti": (True, 1), "na parijānanti": (True, 2)})
assert PARIJ.pos == C.FAMILY_TERMS["parijānāti"] == E.PARIJANATI == E.E_VERBS["parijānanti"].vi
assert PARIJ.neg == C.FAMILY_TERMS["na parijānāti"] == E.E_VERBS["na parijānanti"].vi
assert PARIJ.still == f"{C.STILL} {PARIJ.pos}"

PAJ = Verb(P5.PAJAHATI, P5.NOT_PAJAHATI, R6.STILL_PAJAHATI,     # for check_family() and the pajahati chapters
           {"pajahati": (False, 1), "pajahanti": (False, 2), "nappajahati": (True, 1), "nappajahanti": (True, 2)})


# ---------------------------------------------------------------------------------------------------------------
# 2. Clauses
# ---------------------------------------------------------------------------------------------------------------
def parse_clause(text, V):
    """'<run> V [<run> V]' → [(tp | None, tadekaṭṭha?, negative?, number), …]; one polarity, one number."""
    t = text.strip()
    t = t[:1].lower() + t[1:]
    if m := V.comma_re.search(t):   # ^6-7-220 «… parijānāti, kāmarāgānusayaṃ tadekaṭṭhaṃ parijānāti»
        SEEN["punct"].append(f"comma inside a two-verb clause: …{t[max(0, m.start() - 30):m.end() + 30]}…")
        t = V.comma_re.sub(lambda mm: f" {mm.group(1)} ", t)
    parts = V.re.split(" " + t)
    if parts[-1].strip() or len(parts) < 3:
        raise ValueError(f"clause does not end in a verb: {text!r}")
    groups = []
    for run, v in zip(parts[0:-1:2], parts[1::2]):
        tp, tad = P5.parse_run(run.strip())
        groups.append((tp, tad) + V.forms[v])
    if len({g[2] for g in groups}) != 1 or len({g[3] for g in groups}) != 1:
        raise ValueError(f"mixed polarity / number in {text!r}")
    if len(groups) > 2:
        raise ValueError(f"more than two groups in {text!r}")
    return groups


def _single_ca(tp):
    return tp["conj"] and len(tp["names"]) == 1


def _obj(tp, tad):
    return P5.TADEKATTHA if tp is None else C.tp_vi(tp) + (P5.TAD_JOIN if tad else "")


def pos_vi(groups, V):
    """Positive (7-05): «V A» / «V A và B» / «V A… B» / «V những gì cùng hiện diện với nó» / «V A, vốn cùng …»;
    both-frame 'A-ñca V B-ñca V' «V A, cũng V B»; 'A V B tadekaṭṭhaṃ V' «V A, V B, vốn cùng …» (7-05);
    new: a single 'X-ñca' in a tadekaṭṭha two-verb clause marks the both-frame: «V A, cũng V B, vốn cùng …»."""
    if len(groups) == 1:
        tp, tad = groups[0][:2]
        if tp is not None and _single_ca(tp):
            raise ValueError("single item with 'ca' outside a both-frame: " + repr(groups))
        return f"{V.pos} {_obj(tp, tad)}"
    (t1, d1), (t2, d2) = groups[0][:2], groups[1][:2]
    if t1 is None or t2 is None or d1:
        raise ValueError("unknown clause shape: " + repr(groups))
    if not d2 and t1["conj"] and t2["conj"]:
        return f"{V.pos} {C.tp_vi(t1)}, {C.ALSO} {V.pos} {C.tp_vi(t2)}"
    if d2 and (_single_ca(t1) or _single_ca(t2)):
        if not (t1["conj"] and t2["conj"]):
            raise ValueError("unknown clause shape: " + repr(groups))
        SEEN["both_tad"].append(1)
        return f"{V.pos} {C.tp_vi(t1)}, {C.ALSO} {V.pos} {_obj(t2, d2)}"
    if d2:
        return f"{V.pos} {C.tp_vi(t1)}, {V.pos} {_obj(t2, d2)}"
    raise ValueError("unknown clause shape: " + repr(groups))


def neg_vi(groups, V):
    """Negative (7-06): «không V A»; lists and the both-frame «không V A, cũng không V B, …» (7-04 rule);
    cut 'A…pe… B' «không V A… B»."""
    if any(g[0] is None or g[1] for g in groups):
        raise ValueError("tadekaṭṭhaṃ in a negative clause: " + repr(groups))
    tps = [g[0] for g in groups]
    if len(tps) == 2 and (not all(t["conj"] for t in tps) or any(t["pe"] for t in tps)):
        raise ValueError("unknown both-frame: " + repr(groups))
    if len(tps) == 1 and _single_ca(tps[0]):
        raise ValueError("single item with 'ca' outside a both-frame: " + repr(groups))
    if len(tps) == 1 and tps[0]["pe"]:
        if tps[0]["conj"]:
            raise ValueError("…pe… inside an 'A ca … ca' list: " + repr(groups))
        return f"{V.neg} {C.tp_vi(tps[0])}"
    return f"{V.neg} " + f", {C.ALSO} {V.neg} ".join(n for t in tps for n in t["names"])


def clause_vi(groups, V):
    return neg_vi(groups, V) if groups[0][2] else pos_vi(groups, V)


def noca_vi(groups, V):
    """After 'no ca': positive verb «không V A[, cũng không V B …]» (7-05, user "neither" rule);
    negative verb denied «vẫn V A [và B]» (7-06; user decision «vẫn hiểu biết trọn vẹn»)."""
    if len(groups) != 1 or groups[0][0] is None or groups[0][1] or groups[0][0]["pe"]:
        raise ValueError("unknown 'no ca' part: " + repr(groups))
    tp, _, negative, _ = groups[0]
    if negative:
        return f"{V.still} {C.tp_vi(tp)}"
    return f"{V.neg} " + f", {C.ALSO} {V.neg} ".join(tp["names"])


# ---------------------------------------------------------------------------------------------------------------
# 3. Sentences
# ---------------------------------------------------------------------------------------------------------------
def sentence(s, V=PARIJ):
    """Āmantā. / No. / Natthi. / [<head>] <clause>[(,) no ca [<pron>] <clause>]. /
    <X> ṭhapetvā avasesā puggalā [sabbattha] <clause>. (+ a «…pe….» tail, 7-03)"""
    if (t := T3.pe_tail(s, lambda x: sentence(x, V))) is not None:
        return t
    if s in C.EXACT:
        return C.EXACT[s]
    if not s.endswith("."):
        raise ValueError(f"sentence without a final '.': {s!r}")
    body = s[:-1]
    if m := R6.EXCEPT_RE.fullmatch(body):              # 7-06 frame
        if " no ca " in body:
            raise ValueError(f"'no ca' after ṭhapetvā: not decided: {s!r}")
        groups = parse_clause(m.group(3), V)
        if groups[0][3] != 2 or not groups[0][2]:
            raise ValueError(f"avasesā puggalā: not a plural negative clause: {s!r}")
        where = f", {R6.SABBATTHA}," if m.group(2) else ""
        return f"{R6.EXCEPT} {R6.excepted_vi(m.group(1))}, {R6.REST_PERSONS}{where} {neg_vi(groups, V)}."
    parts = R6.NOCA_RE.split(body)
    if len(parts) not in (1, 4):
        raise ValueError(f"unknown sentence {s!r}")
    words = parts[0].split()
    i = next((k for k, w in enumerate(words) if P5._is_obj_word(w)), None)
    if i is None:
        raise ValueError(f"no object in {s!r}")
    groups = parse_clause(" ".join(words[i:]), V)
    num = groups[0][3]
    if i == 0:                                         # bare answer «Hiểu biết trọn vẹn A.» (7-05; = 2-02 e_single)
        if len(parts) == 4 or num != 1:
            raise ValueError(f"bare answer with 'no ca' / in the plural: {s!r}")
        return cap(clause_vi(groups, V)) + "."
    if words[i][0].isupper():
        raise ValueError(f"capital object after a head: {s!r}")
    person, places, res = R6.parse_head(" ".join(words[:i]))
    if num != (R6.PERSON_NOM[person][1] if person else 1):
        raise ValueError(f"verb number does not fit the head: {s!r}")
    out = R6.head_vi(person, places, res) + clause_vi(groups, V)
    if len(parts) == 4:
        comma, pron, rest = parts[1], parts[2] or "", parts[3]
        if not comma:                                  # coordinator: a missing comma before "no ca" is added
            SEEN["noca_comma"].append(s)
        want = res or ("so" if person and R6.PERSON_NOM[person][1] == 1 else "te" if person else "tato")
        if pron != want:
            raise ValueError(f"'no ca {pron}' does not fit the head ({want!r}): {s!r}")
        g2 = parse_clause(rest, V)
        if g2[0][3] != num or g2[0][2] != groups[0][2]:
            raise ValueError(f"'no ca' number / polarity does not fit: {s!r}")
        out += f", {C.BUT} " + (f"{R6.pron_vi(pron)} " if pron else "") + noca_vi(g2, V)
    return out + "."


# ---------------------------------------------------------------------------------------------------------------
# 4. Questions: 7-03's shell (T3.Q_RE, T3.yo_q); each slot keeps its own polarity (^6-7-243: as written)
# ---------------------------------------------------------------------------------------------------------------
def slot_vi(text, V):
    groups = parse_clause(text, V)
    if len(groups) != 1 or groups[0][0] is None or groups[0][1] or groups[0][3] != 1:
        raise ValueError(f"question slot must be one singular plain object run: {text!r}")
    return clause_vi(groups, V), groups[0][2]


def question(chunk, V=PARIJ):
    m = T3.Q_RE.fullmatch(chunk)
    if not m:
        return None
    label, y, rel1, vapana, yato, a, cor, b, rest = m.groups()
    if rest:
        raise ValueError(f"question chunk with a tail: {chunk!r}")
    rel = "y" + rel1 + (" yato" if yato else "")
    if yato and rel1 != "o":
        raise ValueError(f"bad relative in {chunk!r}")
    if T3.YO_COR[rel] != cor:
        raise ValueError(f"relative {rel!r} with correlative {cor!r}: {chunk!r}")
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {chunk!r}")
    if label and (label == "Kha") != bool(vapana):
        raise ValueError(f"label {label} with vā pana={bool(vapana)}: {chunk!r}")
    bw = b.split()
    bw[-1] = C.strip_ti(bw[-1])
    (va, na), (vb, nb) = slot_vi(a, V), slot_vi(" ".join(bw), V)
    if na != nb:
        SEEN["mixed_q"].append(chunk)
    out = T3.yo_q(rel, va, vb, label, bool(vapana))
    if rel == "yato":   # the place shell is C's yattha shell word for word
        assert out == C.pair_q("yattha", va, vb, label, bool(vapana)), out
    if rel == "yo":     # = family E's shell (2-02)
        assert out == E.yo_q(va, vb, label, bool(vapana)), out
    return out


CHUNK_RE = re.compile(r"(?<=[.?;]) ")


def body_vi(body, V=PARIJ):
    """A line body: questions and answer sentences in the Pāli order ('.' / '?' / the Pāli's ';', as 7-06)."""
    out, after_semi = [], False
    for ch in CHUNK_RE.split(body.strip()):
        if ch.endswith("?"):
            v = question(ch, V)
            if v is None:
                raise ValueError(f"unknown question {ch!r}")
        elif ch.endswith(";"):
            SEEN["punct"].append(f"«;» between answer sentences (kept): {ch[-40:]}")
            v = sentence(ch[:-1] + ".", V)[:-1] + ";"
        else:
            v = sentence(ch, V)
        if after_semi and ch[:1].islower():
            v = v[:1].lower() + v[1:]
        after_semi = ch.endswith(";")
        out.append(v)
    return " ".join(out)


# ---------------------------------------------------------------------------------------------------------------
# 5. Headings, fixed lines, line translator
# ---------------------------------------------------------------------------------------------------------------
PARINNAVARO = C.HEADINGS["Pariññāvāro"]           # «Mục về sự hiểu biết trọn vẹn» (S.LATER_HEADINGS, termbase)
assert PARINNAVARO == C.FAMILY_HEADINGS["Pariññāvāra"] == C.heading("Pariññāvāra")
PARINNAVARO_LC = PARINNAVARO[0].lower() + PARINNAVARO[1:]
FIXED = {   # built as 7-05 «Pajahanavāre anulomaṃ.» / 7-01 «Anusayavāre anulomaṃ.»
    "Pariññāvāre anulomaṃ.": f"{C.HEADINGS['anulomaṃ']} trong {PARINNAVARO_LC}.",
}
assert P5.FIXED["Pajahanavāre anulomaṃ."] == f"{C.HEADINGS['anulomaṃ']} trong {R6.PAJAHANAVARO_LC}."


def tr_line(p, V=PARIJ, fixed=None):
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
        out = fixed[body] if body in fixed else body_vi(body, V)
        out += label
    return f"{out} {bid}" if bid else out


def build(name=CHAPTER, V=PARIJ, fixed=None):
    segs = []
    for seg in S.segments_of(name):
        out = []
        for ln in seg:
            try:
                out.append(tr_line(ln, V, fixed))
            except ValueError as e:
                raise ValueError(f"{name}: cannot place line {ln[:120]!r}: {e}") from None
        segs.append(out)
    return segs


# ---------------------------------------------------------------------------------------------------------------
# 6. Checks
# ---------------------------------------------------------------------------------------------------------------
REUSED = [   # (Pāli, Vietnamese, book): asserted in that book's approved rails
    ("parijānāti (pi-5 12-catutthavaggo)", PARIJ.pos, "5"),
    ("tadekaṭṭhā ca kilesā", "cùng hiện diện với", "1"),
    ("Aṭṭhamako puggalo", "người thứ tám", "5"),
    ("sabbattha / ṭhapetvā", R6.EXCEPT.lower(), "1"),
]
TERMBASE_USED = [
    ("parijānāti", PARIJ.pos), ("parijānātīti", PARIJ.pos), ("parijānanti", PARIJ.pos),
    ("Pariññāvāro", PARINNAVARO_LC), ("Pariññāvāra", PARINNAVARO_LC), ("Pariññāvāre", PARINNAVARO_LC),
    ("Aggamaggasamaṅgī", R6.PERSON_NOM["Aggamaggasamaṅgī"][0]), ("Aggamaggasamaṅgiñca", E.AGGAMAGGASAMANGI),
    ("Anāgāmimaggasamaṅgī", R6.ANAGAMIMAGGA), ("Anāgāmimaggasamaṅgiñca", R6.ANAGAMIMAGGA),
    ("Aṭṭhamako", "người thứ tám"), ("aṭṭhamakañca", "người thứ tám"),
    ("maggasamaṅgīnaṃ", R6.MAGGASAMANGI), ("maggasamaṅgīnañca", R6.MAGGASAMANGI),
    ("ṭhapetvā", R6.EXCEPT.lower()), ("Avasesā", R6.REMAINING), ("puggalā", R6.PUGGALA), ("puggalo", R6.PUGGALA),
    ("anulomaṃ", "chiều thuận"), ("anulomapuggalo", "chiều thuận theo người"),
    ("anulomaokāso", "chiều thuận theo nơi chốn"), ("anulomapuggalokāsā", "chiều thuận theo người và nơi chốn"),
    ("paṭilomapuggalo", "chiều ngược theo người"), ("paṭilomaokāso", "chiều ngược theo nơi chốn"),
    ("kāmarāgānusayaṃ", C.ANUSAYA["kāmarāg"]), ("avijjānusayaṃ", C.ANUSAYA["avijj"]),
    ("Kāmadhātuyā", "cõi dục lạc"), ("rūpadhātuyā", "cõi hình sắc"), ("arūpadhātuyā", "cõi không hình sắc"),
    ("dvīsu vedanāsu", "hai loại cảm giác"), ("tīsu vedanāsu", "ba loại cảm giác"),
    ("Dukkhāya vedanāya", "cảm giác khó chịu"),
]
USER_DECISIONS = ["tadekaṭṭha «" + P5.TADEKATTHA + "»", "Aṭṭhamako «Người thứ tám»",
                  "«vẫn dứt bỏ / vẫn hiểu biết trọn vẹn» after no ca"]


def check_reused():
    P5.check_reused()   # 7-01 / 7-02 / 7-03 / 7-05 strings
    R6.check_reused()   # 7-06 strings
    texts = {b: unicodedata.normalize("NFC", "\n".join(p.read_text(encoding="utf-8") for p in sorted(d.glob("*.md"))))
             for b, d in S.RAILS.items()}
    bad = [(p, v, b) for p, v, b in REUSED if unicodedata.normalize("NFC", v).lower() not in texts[b].lower()]
    assert not bad, "reused strings not found in their rails: " + repr(bad)
    tb = C.TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M)]
    assert not bad, "termbase strings not found: " + repr(bad)
    ap = unicodedata.normalize("NFC", P5.APPROVED.read_text(encoding="utf-8"))
    bad = [d for d in USER_DECISIONS if d not in ap]
    assert not bad, "user decisions not found in APPROVED.md: " + repr(bad)


def check_family():
    """1) 7-05 and 7-06 rebuilt here with the pajahati verb = their own builders, byte for byte.
    2) The strings shared with 2-02 (family E) are 2-02's."""
    saved = {k: list(v) for k, v in SEEN.items()}
    for name, mod in (("7-05-anusayayamaka.md", P5), ("7-06-anusayayamaka.md", R6)):
        mine, theirs = build(name, PAJ, mod.FIXED), mod.build(name)
        bad = [(a, b) for sa, sb in zip(mine, theirs) for a, b in zip(sa, sb) if a != b]
        assert len(mine) == len(theirs) and not bad, (name, bad[:2])
    for k in SEEN:
        SEEN[k][:] = saved[k]
    # family E (2-02)
    v_neg = E.E_VERBS["na parijānāti"]
    assert E.denied(v_neg) == PARIJ.still and E.denied(E.E_VERBS["parijānāti"]) == PARIJ.neg
    assert E.except_head(["X", "Y"]) == f"{R6.EXCEPT} X {C.AND} Y, {R6.REST_PERSONS}"
    assert E.AVASESA_PUGGALA == R6.REST_PERSONS and E.EXCEPT == R6.EXCEPT
    assert E.PERSONS.nom["Aggamaggasamaṅgī"][0] == R6.PERSON_NOM["Aggamaggasamaṅgī"][0] == E.AGGAMAGGASAMANGI
    assert E.PERSONS.acc["Aggamaggasamaṅgiṃ"] == R6.EXC_PERSON["aggamaggasamaṅgi"]
    a, b = C.ANUSAYA["kāmarāg"], C.ANUSAYA["mān"]
    head = cap(R6.PERSON_NOM["Aggamaggasamaṅgī"][0])
    assert sentence("Mānānusayaṃ parijānāti.") == E.e_single(None, b, PARIJ.pos)
    assert sentence("Aggamaggasamaṅgī kāmarāgānusayaṃ na parijānāti, no ca so mānānusayaṃ na parijānāti.") == \
        E.e_noca(head, a, PARIJ.neg, f"{R6.pron_vi('so')} {PARIJ.still} {b}")   # + «người ấy» for the Pāli's so
    assert sentence("Dvinnaṃ maggasamaṅgīnaṃ ṭhapetvā avasesā puggalā kāmarāgānusayañca na parijānanti "
                    "mānānusayañca na parijānanti.") == \
        E.e_both(E.except_head([R6.EXC_PERSON["dvinnaṃ maggasamaṅgīna"]]), a, PARIJ.neg, b, PARIJ.neg)
    assert question("(Ka) yo kāmarāgānusayaṃ parijānāti so mānānusayaṃ parijānātīti?") == \
        E.yo_q(f"{PARIJ.pos} {a}", f"{PARIJ.pos} {b}", "Ka")


# ---------------------------------------------------------------------------------------------------------------
# 7. Notes
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-07 (Anusayayamaka, pariññāvāra anuloma + paṭiloma): frames and fixed strings", "",
         "Generated by build_rails_7-07_vi.py. Imports S, C (7-01, family C setter), 7-03 (yo / yato / yo yato shell), "
         "7-05 (pajahati anuloma frames, tadekaṭṭha), 7-06 (nappajahati paṭiloma frames, persons, ṭhapetvā avasesā "
         "puggalā) and 2-02 (family E: parijānāti in every tense): their strings, byte for byte. The 7-05 / 7-06 "
         "frames are coded once with a verb parameter; the builder rebuilds 7-05 and 7-06 with it and asserts they "
         "are identical. Later chapters import the module (importlib.import_module(\"build_rails_7-07_vi\")).", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    V = PARIJ
    h("Verb (termbase parijānāti «hiểu biết trọn vẹn»; 2-02 tense rule; user decision «vẫn …»)")
    row("parijānāti / parijānanti", V.pos)
    row("na parijānāti / na parijānanti", V.neg)
    row("no ca … na parijānāti (negative denied)", V.still)
    h("Anuloma (= 7-05 with «hiểu biết trọn vẹn»)")
    row("A parijānāti", f"{V.pos} A")
    row("A ca B ca parijānāti", f"{V.pos} A {C.AND} B")
    row("A ca parijānāti B ca parijānāti (both)", f"{V.pos} A, {C.ALSO} {V.pos} B")
    row("Tadekaṭṭhaṃ parijānāti.", sentence("Tadekaṭṭhaṃ parijānāti."))
    row("A tadekaṭṭhaṃ parijānāti", f"{V.pos} A{P5.TAD_JOIN}")
    row("A parijānāti[,] B tadekaṭṭhaṃ parijānāti", f"{V.pos} A, {V.pos} B{P5.TAD_JOIN}")
    row("A ca parijānāti B ca [C ca] tadekaṭṭhaṃ parijānāti (new: both-frame with tadekaṭṭha)",
        f"{V.pos} A, {C.ALSO} {V.pos} B [{C.AND} C]{P5.TAD_JOIN}")
    row("A ca B ca parijānāti C ca tadekaṭṭhaṃ parijānāti (new)", f"{V.pos} A {C.AND} B, {C.ALSO} {V.pos} C{P5.TAD_JOIN}")
    row("A ca B ca parijānāti C ca D ca tadekaṭṭhaṃ parijānāti (= 7-05 ^6-7-162)",
        f"{V.pos} A {C.AND} B, {V.pos} C {C.AND} D{P5.TAD_JOIN}")
    row(", no ca <pron> A [ca B ca] parijānāti", f", {C.BUT} <pron> {V.neg} A[, {C.ALSO} {V.neg} B]")
    h("Paṭiloma (= 7-06 with «hiểu biết trọn vẹn»)")
    row("A na parijānāti", f"{V.neg} A")
    row("A ca B ca na parijānāti / A ca na parijānāti B ca na parijānāti",
        f"{V.neg} A, {C.ALSO} {V.neg} B")
    row("A…pe… B na parijānāti (cut)", f"{V.neg} A… B")
    row(", no ca so / tato A [ca B ca] na parijānāti", f", {C.BUT} người ấy / ở nơi ấy {V.still} A [{C.AND} B]")
    row("<X> ṭhapetvā avasesā puggalā …", f"{R6.EXCEPT} <X>, {R6.REST_PERSONS} …")
    h("Questions (7-03 shell = 2-02 yo_q)")
    a, b = f"{V.pos} A", f"{V.pos} B"
    row("(Ka) yo A parijānāti so B parijānātīti?", T3.yo_q("yo", a, b, "Ka"))
    row("(Ka) yato A parijānāti tato B parijānātīti?", T3.yo_q("yato", a, b, "Ka"))
    row("(Ka) yo yato A parijānāti so tato B parijānātīti?", T3.yo_q("yo yato", a, b, "Ka"))
    row("(Ka) yo A na parijānāti so B na parijānātīti?", T3.yo_q("yo", f"{V.neg} A", f"{V.neg} B", "Ka"))
    o.append("")
    o.append("Examples (built by the module):")
    for p in ("Rūpadhātuyā arūpadhātuyā tato mānānusayaṃ parijānāti, no ca tato kāmarāgānusayaṃ parijānāti.",
              "Kāmadhātuyā dvīsu vedanāsu tato mānānusayañca parijānāti kāmarāgānusayañca parijānāti.",
              "Diṭṭhānusayaṃ parijānāti kāmarāgānusayañca paṭighānusayañca mānānusayañca tadekaṭṭhaṃ parijānāti …pe….",
              "Sveva puggalo kāmadhātuyā dvīsu vedanāsu so tato vicikicchānusayaṃ parijānāti, kāmarāgānusayaṃ "
              "tadekaṭṭhaṃ parijānāti.",
              "Sveva puggalo kāmadhātuyā dvīsu vedanāsu so tato vicikicchānusayañca parijānāti kāmarāgānusayañca "
              "tadekaṭṭhaṃ parijānāti, no ca so tato paṭighānusayaṃ parijānāti.",
              "Aggamaggasamaṅgī kāmarāgānusayaṃ na parijānāti, no ca so mānānusayaṃ na parijānāti.",
              "Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca ṭhapetvā avasesā puggalā vicikicchānusayañca na parijānanti "
              "kāmarāgānusayañca paṭighānusayañca mānānusayañca na parijānanti.",
              "Dukkhāya vedanāya tato bhavarāgānusayañca kāmarāgānusayañca na parijānāti, no ca tato paṭighānusayaṃ "
              "na parijānāti."):
        row(p, sentence(p))
    h("Fixed lines")
    for k, v in FIXED.items():
        row(k, v)
    h("Pāli as written / punctuation (reported)")
    for q in sorted(set(SEEN["mixed_q"])):
        row(q, question(q) + "  (^6-7-243: the second slot has no «na»; translated as written)")
    for p in sorted(set(SEEN["punct"])):
        o.append(f"- {p}: the Vietnamese two-verb frame has that comma anyway (= 7-05 / 7-06)")
    for s in sorted(set(SEEN["noca_comma"])):
        o.append(f"- missing comma before no ca, added: {s[:80]}")
    h("Strings that cannot align with 2-02 (family E), and why")
    o.append("- «no ca so …» = «, nhưng người ấy vẫn …»: 2-02's no-ca frame has no pronoun because its Pāli has none; "
             "here the Pāli has so / tato / so tato, rendered with family C's pronouns (7-03 / 7-06). Everything else "
             "(verb forms, «vẫn», both-frame, «không V B, cũng không V C», ṭhapetvā head, yo_q) is asserted equal.")
    o.append("- the both-frame with tadekaṭṭhaṃ («V A, cũng V B, vốn cùng hiện diện với nó») has no 2-02 counterpart "
             "(no tadekaṭṭha in the Khandhayamaka); it is 2-02's / 7-05's both-frame plus 7-05's TAD_JOIN.")
    o.append("")
    return "\n".join(o)


def main():
    check_reused()
    check_family()
    segs = build(CHAPTER)
    C.write(CHAPTER, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for k, v in SEEN.items():
        if k != "both_tad":
            for x in sorted(set(v)):
                print(f"{k}: {x[:110]}")
    print("both-frame with tadekaṭṭha:", len(SEEN["both_tad"]))
    for p, v in sorted(set(C.SLIPS_SEEN)):
        print("slip rendered as meant:", p, "→", v)


if __name__ == "__main__":
    main()
