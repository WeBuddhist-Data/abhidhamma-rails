"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-06 (Anusayayamaka: pajahanavāra, paṭiloma: nappajahati;
person, place, person + place).

Imports (READ-ONLY; importing writes nothing, outputs are written only under `if __name__ == "__main__":`):
  S  build_rails_sample_vi   labels, «…», checks
  C  build_rails_7-01_vi     family C setter: tendencies, places, pronouns, labels, headings, family terms, write()
  T2 build_rails_7-02_vi     apariyāpanne, sabbattha, «Chiều ngược»
  T3 build_rails_7-03_vi     nominative yo / yato / yo yato shell (yo_q, Q_RE), persons, tato / so tato, «…pe….» tail
  T4 build_rails_7-04_vi     negative list rule («không có A, cũng không có B, …»), «vẫn» after no ca, sabbattha head
  P5 build_rails_7-05_vi     pajahati frames: PAJAHATI / NOT_PAJAHATI, parse_run (accusative runs), neg_vi, persons
  A  build_rails_2-01_vi     EXCEPT «Ngoại trừ» (ṭhapetvā)
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; R = importlib.import_module("build_rails_7-06_vi")

Frames set here (exposed for the later pajahati / parijānāti paṭiloma chapters):
  not_vi()            "<run> nappajahati" = «không dứt bỏ A[, cũng không dứt bỏ B …]» (P5.neg_vi), cut «không dứt bỏ A… B»
  still_vi()          "no ca <pron> A [ca B ca] nappajahati" = «nhưng <pron> vẫn dứt bỏ A [và B]»
  PERSON_NOM          P5's persons + Anāgāmimaggasamaṅgī «người có được con đường không trở lại» (termbase)
  excepted_vi()       "<X> ṭhapetvā avasesā puggalā [sabbattha] …" = «Ngoại trừ <X>, những hạng người còn lại[, ở mọi nơi,] …»
  sentence() / question() / body_vi() / tr_line() / build()
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-06_vi.py
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
T3 = importlib.import_module("build_rails_7-03_vi")   # READ-ONLY
T4 = importlib.import_module("build_rails_7-04_vi")   # READ-ONLY
P5 = importlib.import_module("build_rails_7-05_vi")   # pajahati frames (READ-ONLY)
A = importlib.import_module("build_rails_2-01_vi")    # EXCEPT (READ-ONLY)

CHAPTER = "7-06-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-06.md"
ADH_DIR = RAILS_DIR / "adh-7-06"
cap = S.cap
PUNCT_SEEN = []    # Pāli punctuation kept / normalised (reported)

# ---------------------------------------------------------------------------------------------------------------
# 1. The verb (termbase nappajahati / nappajahanti «không dứt bỏ»; P5's PAJAHATI / NOT_PAJAHATI)
# ---------------------------------------------------------------------------------------------------------------
PAJAHATI = P5.PAJAHATI                          # «dứt bỏ»
NOT_PAJAHATI = P5.NOT_PAJAHATI                  # «không dứt bỏ»
STILL_PAJAHATI = f"{C.STILL} {PAJAHATI}"        # «vẫn dứt bỏ»: after "no ca" a negative verb is denied (coordinator)
NOT_NEXT = f"{C.ALSO} {NOT_PAJAHATI}"           # «cũng không dứt bỏ» (one per item, 7-04 / 7-05)
VERB_NUM = {"nappajahati": 1, "nappajahanti": 2}
VERB_RE = re.compile(r" (nappajahati|nappajahanti)(?= |$)")
assert NOT_PAJAHATI == C.FAMILY_TERMS["nappajahati"] and PAJAHATI == C.FAMILY_TERMS["pajahati"]


def parse_clause(text):
    """'<run> nappajahati|nappajahanti [<run> nappajahati|nappajahanti]' → ([tp, …], number).
    Two groups = the both-frame 'A ca V B ca V' (each run with 'ca'); a run may be a list or a …pe… cut."""
    t = text.strip()
    if m := re.search(r" (nappajahati|nappajahanti), (?=\S)", t):   # ^6-7-193 «…nappajahati, vicikicchānusayañca …»
        PUNCT_SEEN.append(("… nappajahati, X-añca nappajahati (comma inside the both-frame)",
                           "the Vietnamese both-frame has that comma anyway"))
        t = t[:m.start()] + f" {m.group(1)} " + t[m.end():]
    parts = VERB_RE.split(" " + t)
    if parts[-1].strip() or len(parts) < 3:
        raise ValueError(f"clause does not end in nappajahati / nappajahanti: {text!r}")
    groups, nums = [], set()
    for run, v in zip(parts[0:-1:2], parts[1::2]):
        tp, tad = P5.parse_run(run.strip())
        if tp is None or tad:
            raise ValueError(f"tadekaṭṭhaṃ in a nappajahati clause: {text!r}")
        groups.append(tp)
        nums.add(VERB_NUM[v])
    if len(nums) != 1:
        raise ValueError(f"mixed number in {text!r}")
    if len(groups) == 2:
        if not all(g["conj"] for g in groups) or any(g["pe"] for g in groups):
            raise ValueError(f"unknown both-frame {text!r}")
    elif len(groups) != 1:
        raise ValueError(f"more than two groups in {text!r}")
    elif groups[0]["conj"] and len(groups[0]["names"]) == 1:
        raise ValueError(f"single item with 'ca' outside a both-frame: {text!r}")
    return groups, nums.pop()


def not_vi(groups):
    """«không dứt bỏ A» / list or both-frame «không dứt bỏ A, cũng không dứt bỏ B, …» (P5.neg_vi, 7-04 rule) /
    cut 'A…pe… B' «không dứt bỏ A… B»."""
    if len(groups) == 1 and groups[0]["pe"]:
        if groups[0]["conj"]:
            raise ValueError("…pe… inside an 'A ca … ca' list: " + repr(groups))
        return f"{NOT_PAJAHATI} {C.tp_vi(groups[0])}"
    merged = {"names": [n for g in groups for n in g["names"]], "conj": True, "pe": {}}
    out = P5.neg_vi([(merged, False)])
    assert out == f"{NOT_PAJAHATI} " + f", {NOT_NEXT} ".join(merged["names"]), out
    return out


def still_vi(groups):
    """After 'no ca' (negative denied): «vẫn dứt bỏ A» / «vẫn dứt bỏ A và B» / «vẫn dứt bỏ A, B và C»."""
    if len(groups) != 1 or groups[0]["pe"]:
        raise ValueError("unknown 'no ca' part: " + repr(groups))
    return f"{STILL_PAJAHATI} {C.tp_vi(groups[0])}"


# ---------------------------------------------------------------------------------------------------------------
# 2. Answer heads (P5 / 7-03 persons and heads; 7-02 places incl. apariyāpanne)
# ---------------------------------------------------------------------------------------------------------------
ANAGAMIMAGGA = "người có được con đường không trở lại"      # Anāgāmimaggasamaṅgī (termbase)
PERSON_NOM = {**P5.PERSON_NOM, "Anāgāmimaggasamaṅgī": (ANAGAMIMAGGA, 1)}
PLACE_LOC = T2.PLACE_LOC                                    # C.PLACE_LOC + apariyāpanne (7-02)
AT, THEN, BUT, AND = C.AT, C.THEN, C.BUT, C.AND


def pron_vi(pron):
    """'so' «người ấy»; 'tato' «ở nơi ấy»; 'so tato' «người ấy, ở nơi ấy» (7-03)."""
    if pron == "so":
        return T3.PRON_NOM["so"]
    return T3.pron_vi(pron)


def parse_head(txt):
    """'<person>? <places>* <so tato | tato>?' → (person | None, [places], resumptive) (7-03 / 7-05 rules)."""
    person, rest = C._take(txt, PERSON_NOM)
    places = []
    while rest:
        p, rest2 = C._take(rest, PLACE_LOC, fold=True)
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
    """«Người có được con đường tối thượng …» / «Ở <nơi>, ở <nơi>, thì ở nơi ấy …» /
    «Chính hạng người ấy, ở <nơi>, thì người ấy, ở nơi ấy …» (= 7-03 / 7-05 head_vi)."""
    parts = ([PERSON_NOM[person][0]] if person else []) + [f"{AT} {PLACE_LOC[p]}" for p in places]
    return cap(", ".join(parts)) + (f", {THEN} {T3.pron_vi(res)} " if res else " ")


# "<X> ṭhapetvā avasesā puggalā [sabbattha] …"
EXCEPT = A.EXCEPT                                # «Ngoại trừ» (2-01; termbase ṭhapetvā)
PUGGALA = "hạng người"                           # puggalā (termbase)
REMAINING = "còn lại"                            # avasesā (termbase Avasesā)
REST_PERSONS = f"những {PUGGALA} {REMAINING}"    # avasesā puggalā «những hạng người còn lại»
SABBATTHA = T4.SABBATTHA                         # «ở mọi nơi» (7-02 / 7-04)
MAGGASAMANGI = "người có được con đường"         # maggasamaṅgīnaṃ (termbase; pi-1 maggasamaṅgissa)
EXC_PERSON = {   # accusative / genitive stem (before -ṃ / -ñca) → Vietnamese (termbase)
    "anāgāmimaggasamaṅgi": ANAGAMIMAGGA,
    "aggamaggasamaṅgi": PERSON_NOM["Aggamaggasamaṅgī"][0],
    "aṭṭhamaka": PERSON_NOM["Aṭṭhamako"][0],
    "dvinnaṃ maggasamaṅgīna": f"hai {MAGGASAMANGI}",   # Dvinnaṃ … «hai …» (7-01 Dvinnaṃ puggalānaṃ «hai hạng người»)
}
EXCEPT_RE = re.compile(r"(.+?) ṭhapetvā avasesā puggalā( sabbattha)? (.+)")


def excepted_vi(txt):
    """'Dvinnaṃ maggasamaṅgīnaṃ' / 'Anāgāmimaggasamaṅgiṃ' / 'Xñca Yñca' → «hai người có được con đường» /
    «người có được con đường không trở lại» / «X và Y»."""
    w = txt.split()
    toks = []
    while w:
        if w[0] == "Dvinnaṃ":
            if len(w) < 2:
                raise ValueError(f"unknown excepted persons {txt!r}")
            toks.append(w[0] + " " + w[1])
            w = w[2:]
        else:
            toks.append(w[0])
            w = w[1:]
    names, ends = [], []
    for t in toks:
        m = re.fullmatch(r"(.+?)(ṃ|ñca)", t)
        stem = m and (m.group(1)[:1].lower() + m.group(1)[1:])
        if not m or stem not in EXC_PERSON:
            raise ValueError(f"unknown excepted person {t!r} in {txt!r}")
        names.append(EXC_PERSON[stem])
        ends.append(m.group(2))
    if (len(toks) == 1) != (ends == ["ṃ"]) or (len(toks) > 1 and set(ends) != {"ñca"}):
        raise ValueError(f"unknown excepted list {txt!r}")
    return names[0] if len(names) == 1 else ", ".join(names[:-1]) + f" {AND} " + names[-1]


# ---------------------------------------------------------------------------------------------------------------
# 3. Sentences
# ---------------------------------------------------------------------------------------------------------------
NOCA_RE = re.compile(r"(,?) no ca (?:(so tato|te tato|tato|so) )?")


def sentence(s):
    """Āmantā. / <head> <clause>[, no ca <pron> <clause>]. / <X> ṭhapetvā avasesā puggalā [sabbattha] <clause>.
    (+ a «…pe….» tail, 7-03)"""
    if (t := T3.pe_tail(s, sentence)) is not None:
        return t
    if s in C.EXACT:
        return C.EXACT[s]
    if not s.endswith("."):
        raise ValueError(f"sentence without a final '.': {s!r}")
    body = s[:-1]
    if m := EXCEPT_RE.fullmatch(body):
        if " no ca " in body:
            raise ValueError(f"'no ca' after ṭhapetvā: not decided: {s!r}")
        groups, num = parse_clause(m.group(3))
        if num != 2:
            raise ValueError(f"avasesā puggalā with a singular verb: {s!r}")
        where = f", {SABBATTHA}," if m.group(2) else ""
        return f"{EXCEPT} {excepted_vi(m.group(1))}, {REST_PERSONS}{where} {not_vi(groups)}."
    parts = NOCA_RE.split(body)
    if len(parts) not in (1, 4):
        raise ValueError(f"unknown sentence {s!r}")
    words = parts[0].split()
    i = next((k for k, w in enumerate(words) if C.is_anusaya(w.split("…")[0])), None)
    if not i:
        raise ValueError(f"no head / no tendency in {s!r}")
    person, places, res = parse_head(" ".join(words[:i]))
    groups, num = parse_clause(" ".join(words[i:]))
    if num != (PERSON_NOM[person][1] if person else 1):
        raise ValueError(f"verb number does not fit the head: {s!r}")
    out = head_vi(person, places, res) + not_vi(groups)
    if len(parts) == 4:
        comma, pron, rest = parts[1], parts[2] or "", parts[3]
        if not comma:   # coordinator: a missing comma before "no ca" is added (7-04, 7-05)
            PUNCT_SEEN.append((f"… no ca (no comma): {s[:60]}", "comma added"))
        want = res or ("so" if person and PERSON_NOM[person][1] == 1 else "te" if person else "tato")
        if pron != want:
            raise ValueError(f"'no ca {pron}' does not fit the head ({want!r}): {s!r}")
        g2, n2 = parse_clause(rest)
        if n2 != num:
            raise ValueError(f"'no ca' number does not fit: {s!r}")
        out += f", {BUT} {pron_vi(pron)} {still_vi(g2)}"
    return out + "."


# ---------------------------------------------------------------------------------------------------------------
# 4. Questions: 7-03's shell (T3.Q_RE, T3.yo_q) with nappajahati slots
# ---------------------------------------------------------------------------------------------------------------
def slot_vi(text):
    groups, num = parse_clause(text)
    if num != 1:
        raise ValueError(f"question slot in the plural: {text!r}")
    return not_vi(groups)


def question(body):
    m = T3.Q_RE.fullmatch(body)
    if not m:
        return None
    label, y, rel1, vapana, yato, a, cor, b, rest = m.groups()
    if rest:
        raise ValueError(f"question chunk with a tail: {body!r}")
    rel = "y" + rel1 + (" yato" if yato else "")
    if yato and rel1 != "o":
        raise ValueError(f"bad relative in {body!r}")
    if T3.YO_COR[rel] != cor:
        raise ValueError(f"relative {rel!r} with correlative {cor!r}: {body!r}")
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {body!r}")
    if label and (label == "Kha") != bool(vapana):
        raise ValueError(f"label {label} with vā pana={bool(vapana)}: {body!r}")
    bw = b.split()
    bw[-1] = C.strip_ti(bw[-1])
    va, vb = slot_vi(a), slot_vi(" ".join(bw))
    out = T3.yo_q(rel, va, vb, label, bool(vapana))
    if rel == "yato":   # the place shell is C's yattha shell word for word
        assert out == C.pair_q("yattha", va, vb, label, bool(vapana)), out
    return out


CHUNK_RE = re.compile(r"(?<=[.?;]) ")


def body_vi(body):
    """A line body: questions ('…ti?') and answer sentences ('.' or the Pāli's ';'), in the Pāli order; a line may
    hold several questions (^6-7-178, ^6-7-182)."""
    out, after_semi = [], False
    for ch in CHUNK_RE.split(body.strip()):
        if ch.endswith("?"):
            q = question(ch)
            if q is None:
                raise ValueError(f"unknown question {ch!r}")
            v = q
        elif ch.endswith(";"):
            PUNCT_SEEN.append((f"«;» between answer sentences: {ch[-40:]}", "kept"))
            v = sentence(ch[:-1] + ".")[:-1] + ";"
        else:
            v = sentence(ch)
        if after_semi and ch[:1].islower():
            v = v[:1].lower() + v[1:]
        after_semi = ch.endswith(";")
        out.append(v)
    return " ".join(out)


# ---------------------------------------------------------------------------------------------------------------
# 5. Headings, fixed lines, line translator
# ---------------------------------------------------------------------------------------------------------------
PAJAHANAVARO = C.HEADINGS["Pajahanavāro"]        # «Mục về sự dứt bỏ» (S.LATER_HEADINGS, termbase)
PAJAHANAVARO_LC = PAJAHANAVARO[0].lower() + PAJAHANAVARO[1:]
FIXED = {   # built as 7-02 «Anusayavāre paṭilomaṃ.» / 7-04 «Sānusayavāre paṭilomaṃ.»
    "Pajahanāvāre paṭilomaṃ.": f"{T2.PATILOMA} trong {PAJAHANAVARO_LC}.",   # Pajahanāvāre: variant spelling (termbase)
    "Pajahanavāro.": PAJAHANAVARO + ".",
}
assert T2.FIXED["Anusayavāre paṭilomaṃ."] == f"{T2.PATILOMA} trong {T2.ANUSAYAVARO_LC}."
assert T4.FIXED["Sānusayavāre paṭilomaṃ."].startswith(T2.PATILOMA + " trong ")
assert P5.FIXED["Pajahanavāre anulomaṃ."] == f"{C.HEADINGS['anulomaṃ']} trong {PAJAHANAVARO_LC}."


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
        out = FIXED[body] if body in FIXED else body_vi(body)
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
# 6. Checks
# ---------------------------------------------------------------------------------------------------------------
REUSED = [   # (Pāli, Vietnamese, book): asserted in that book's approved rails
    ("maggasamaṅgissa ñāṇaṃ", f"của {MAGGASAMANGI}", "1"),
    ("Aṭṭhamako puggalo", "người thứ tám", "5"),
    ("sabbattha", SABBATTHA, "5"),
    ("ṭhapetvā", EXCEPT.lower(), "1"),
]
TERMBASE_USED = [
    ("nappajahati", NOT_PAJAHATI), ("nappajahanti", NOT_PAJAHATI), ("nappajahatīti", NOT_PAJAHATI),
    ("pajahati", PAJAHATI), ("Aggamaggasamaṅgī", PERSON_NOM["Aggamaggasamaṅgī"][0]),
    ("Anāgāmimaggasamaṅgī", ANAGAMIMAGGA), ("Anāgāmimaggasamaṅgiṃ", ANAGAMIMAGGA),
    ("Anāgāmimaggasamaṅgiñca", ANAGAMIMAGGA), ("Aggamaggasamaṅgiṃ", EXC_PERSON["aggamaggasamaṅgi"]),
    ("Aggamaggasamaṅgiñca", EXC_PERSON["aggamaggasamaṅgi"]), ("Aṭṭhamako", "người thứ tám"),
    ("aṭṭhamakañca", "người thứ tám"), ("maggasamaṅgīnaṃ", MAGGASAMANGI), ("maggasamaṅgīnañca", MAGGASAMANGI),
    ("ṭhapetvā", EXCEPT.lower()), ("Avasesā", REMAINING), ("puggalā", PUGGALA), ("puggalo", PUGGALA),
    ("Pajahanavāra", PAJAHANAVARO_LC), ("Pajahanavāro", PAJAHANAVARO_LC), ("Pajahanāvāre", PAJAHANAVARO_LC),
    ("paṭilomaṃ", "chiều ngược"), ("paṭilomapuggalo", "chiều ngược theo người"),
    ("paṭilomaokāso", "chiều ngược theo nơi chốn"), ("paṭilomapuggalokāsā", "chiều ngược theo người và nơi chốn"),
]


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


def check_family():
    """Strings shared with 7-03 / 7-04 / 7-05 stay byte-identical."""
    for k, v in P5.PERSON_NOM.items():
        assert PERSON_NOM[k] == v
    for h in (("Sveva puggalo", ["kāmadhātuyā dvīsu vedanāsu"], "so tato"),
              (None, ["rūpadhātuyā", "arūpadhātuyā"], "tato"),
              ("Aggamaggasamaṅgī", ["dukkhāya vedanāya"], "so tato"), ("Aṭṭhamako", [], "")):
        assert head_vi(*h) == P5.head_vi(*h) == T3.head_vi(*h) if h[0] in T3.PERSON_NOM or not h[0] \
            else head_vi(*h) == P5.head_vi(*h), h
    for h in ("Sveva puggalo dukkhāya vedanāya apariyāpanne so tato", "Apariyāpanne tato",
              "Rūpadhātuyā arūpadhātuyā apariyāpanne tato"):
        assert head_vi(*parse_head(h)) == T4.head_vi(*T4.parse_head(h)), h
    for s in ("Āmantā.", "Āmantā …pe…."):
        assert sentence(s) == P5.sentence(s) == T4.sentence(s), s
    # the negative list frame is 7-04's with «dứt bỏ» for «có»
    assert T4.without_vi({"names": ["A", "B", "C"], "conj": True, "pe": {}}) == \
        not_vi([{"names": ["A", "B", "C"], "conj": True, "pe": {}}]).replace(NOT_PAJAHATI, C.FAMILY_TERMS["niranusayo"])
    # 7-05's question shell with the negative slot
    q = "(Ka) yo kāmarāgānusayaṃ nappajahati so paṭighānusayaṃ nappajahatīti?"
    assert question(q) == T3.yo_q("yo", f"{NOT_PAJAHATI} {C.ANUSAYA['kāmarāg']}",
                                  f"{NOT_PAJAHATI} {C.ANUSAYA['paṭigh']}", "Ka")


# ---------------------------------------------------------------------------------------------------------------
# 7. Notes
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-06 (Anusayayamaka, pajahanavāra paṭiloma): frames and fixed strings", "",
         "Generated by build_rails_7-06_vi.py. Imports S, C (7-01, family C setter), 7-02 (apariyāpanne, cuts, "
         "«Chiều ngược»), 7-03 (yo / yato / yo yato shell, heads), 7-04 (negative list rule, sabbattha), 7-05 "
         "(PAJAHATI / NOT_PAJAHATI, accusative runs, neg_vi, persons) and 2-01 (EXCEPT): their strings, byte for "
         "byte. New here: nappajahati as the predicate, «vẫn dứt bỏ» after no ca, Anāgāmimaggasamaṅgī, the "
         "ṭhapetvā avasesā puggalā frame. Later chapters import the module "
         "(importlib.import_module(\"build_rails_7-06_vi\")).", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    h("Predicate (termbase nappajahati / nappajahanti «không dứt bỏ»)")
    row("A nappajahati / nappajahanti", f"{NOT_PAJAHATI} A")
    row("A ca B ca nappajahati (neither, 7-04 rule)", f"{NOT_PAJAHATI} A, {NOT_NEXT} B")
    row("A ca nappajahati B ca nappajahati (both-frame)", f"{NOT_PAJAHATI} A, {NOT_NEXT} B")
    row("A ca nappajahati B ca C ca nappajahati", f"{NOT_PAJAHATI} A, {NOT_NEXT} B, {NOT_NEXT} C")
    row("A…pe… B nappajahati (cut)", f"{NOT_PAJAHATI} A… B")
    row(", no ca so / tato / so tato A nappajahati (negative denied)",
        f", {BUT} {pron_vi('so')} / {pron_vi('tato')} / {pron_vi('so tato')} {STILL_PAJAHATI} A")
    row(", no ca so A ca B ca nappajahati", f", {BUT} {pron_vi('so')} {STILL_PAJAHATI} A {AND} B")
    h("Questions (7-03 shell)")
    a, b = f"{NOT_PAJAHATI} A", f"{NOT_PAJAHATI} B"
    row("(Ka) yo A nappajahati so B nappajahatīti?", T3.yo_q("yo", a, b, "Ka"))
    row("(Kha) yo vā pana B … so A …ti?", T3.yo_q("yo", b, a, "Kha", True))
    row("Yo … so …ti? (no label)", T3.yo_q("yo", a, b))
    row("(Ka) yato … tato …ti?", T3.yo_q("yato", a, b, "Ka"))
    row("Yato vā pana … tato …ti? (no label)", T3.yo_q("yato", b, a, None, True))
    row("(Ka) yo yato … so tato …ti?", T3.yo_q("yo yato", a, b, "Ka"))
    row("(Kha) yo vā pana yato … so tato …ti?", T3.yo_q("yo yato", b, a, "Kha", True))
    h("Answer heads")
    row("Anāgāmimaggasamaṅgī …", f"{cap(ANAGAMIMAGGA)} …")
    for k in ("Aggamaggasamaṅgī", "Aṭṭhamako", "Sveva puggalo"):
        row(f"{k} … (7-05 / 7-03)", f"{cap(PERSON_NOM[k][0])} …")
    row("<X> ṭhapetvā avasesā puggalā …", f"{EXCEPT} <X>, {REST_PERSONS} …")
    row("<X> ṭhapetvā avasesā puggalā sabbattha …", f"{EXCEPT} <X>, {REST_PERSONS}, {SABBATTHA}, …")
    for k, v in EXC_PERSON.items():
        row(f"{k}ṃ / {k}ñca (after ṭhapetvā)", v)
    o.append("")
    o.append("Examples (built by the module):")
    for p in ("Aggamaggasamaṅgī kāmarāgānusayaṃ nappajahati, no ca so mānānusayaṃ nappajahati.",
              "Dvinnaṃ maggasamaṅgīnaṃ ṭhapetvā avasesā puggalā kāmarāgānusayañca nappajahanti mānānusayañca nappajahanti.",
              "Anāgāmimaggasamaṅgī vicikicchānusayañca mānānusayañca nappajahati, no ca so kāmarāgānusayañca "
              "paṭighānusayañca nappajahati.",
              "Dukkhāya vedanāya tato kāmarāgānusayaṃ nappajahati, no ca tato paṭighānusayaṃ nappajahati.",
              "Rūpadhātuyā arūpadhātuyā apariyāpanne tato kāmarāgānusayañca nappajahati paṭighānusayañca nappajahati.",
              "Anāgāmimaggasamaṅgī dukkhāya vedanāya so tato kāmarāgānusayaṃ nappajahati, no ca so tato "
              "paṭighānusayaṃ nappajahati.",
              "Anāgāmimaggasamaṅgiñca aṭṭhamakañca ṭhapetvā avasesā puggalā sabbattha kāmarāgānusayañca nappajahanti "
              "vicikicchānusayañca nappajahanti."):
        row(p, sentence(p))
    h("Fixed lines")
    for k, v in FIXED.items():
        row(k, v)
    h("Pāli punctuation")
    for p, v in sorted(set(PUNCT_SEEN)):
        row(p, v)
    o.append("")
    return "\n".join(o)


def main():
    check_reused()
    check_family()
    segs = build(CHAPTER)
    C.write(CHAPTER, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for p, v in sorted(set(C.SLIPS_SEEN + PUNCT_SEEN)):
        print("punctuation / slip:", p, "→", v)


if __name__ == "__main__":
    main()
