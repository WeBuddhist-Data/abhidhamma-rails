"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-03 (Anusayayamaka: sānusayavāra, anuloma: person, place,
person + place). Family C: imports build_rails_7-01_vi (READ-ONLY) and copies its strings byte for byte.

New frames (exposed for 7-04 … 7-11, which share the yo / yato shape with other predicates):
  YO_REL / yo_q()        (Ka) yo A so B ti? / yato … tato … / yo yato … so tato … (nominative person shell)
  PERSON_NOM             nominative persons (Anāgāmī, Puthujjano, Tayo puggalā, Teva puggalā, Sveva puggalo …),
                         Vietnamese taken from C.PERSON_GEN
  pred_vi() / neg_vi()   «có A» / «có A, cũng có B» / «không có A, cũng không có B» (user "neither" rule)
  sentence() / answers() one answer sentence (person / places + tato / person + places + so | te tato / bare)
  pe_tail()              «…pe….» at a sentence end → «…» (final «.» absorbed)
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-03_vi.py
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

CHAPTER = "7-03-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-03.md"
ADH_DIR = RAILS_DIR / "adh-7-03"
cap = S.cap

# ---------------------------------------------------------------------------------------------------------------
# 1. Predicate: sānusayo / sānusayā «có» (+ the tendency), termbase; number checked against the subject
# ---------------------------------------------------------------------------------------------------------------
HAVE = C.FAMILY_TERMS["sānusayo"]            # «có»
PRED = {"sānusayo": 1, "sānusayā": 2}
PRED_RE = re.compile(r" (sānusayo|sānusayā)(?= |$)")


def parse_pred(text):
    """'<run> sānusayo [<run> sānusayo]' → [(tp, number), …] (tendencies in the instrumental, C.parse_tp)."""
    parts = PRED_RE.split(" " + text.strip())
    if parts[-1].strip() or len(parts) < 3:
        raise ValueError(f"clause does not end in sānusayo / sānusayā: {text!r}")
    groups = [(C.parse_tp(run.strip()), PRED[v]) for run, v in zip(parts[0:-1:2], parts[1::2])]
    if len({n for _, n in groups}) != 1:
        raise ValueError(f"mixed number in {text!r}")
    return groups


def pred_vi(groups):
    """One group «có <run>»; both-frame 'A ca sānusayo B ca sānusayo' = «có A, cũng có B» (C both-frame)."""
    if len(groups) == 1:
        return f"{HAVE} {C.tp_vi(groups[0][0])}"
    if len(groups) == 2 and all(tp["conj"] for tp, _ in groups):
        (t1, _), (t2, _) = groups
        return f"{HAVE} {C.tp_vi(t1)}, {C.ALSO} {HAVE} {C.tp_vi(t2)}"
    raise ValueError("unknown clause shape: " + repr(groups))


def neg_vi(groups):
    """After 'no ca': «không có A[, cũng không có B …]» (user rule: "neither", termbase decision 4, 7-03)."""
    if len(groups) != 1:
        raise ValueError("no ca with more than one predicate: " + repr(groups))
    tp = groups[0][0]
    if tp["pe"]:
        raise ValueError("…pe… inside a 'no ca' part: " + repr(tp))
    return f"{C.NEITHER_FIRST} " + f", {C.NEITHER_NEXT} ".join(tp["names"])


# ---------------------------------------------------------------------------------------------------------------
# 2. Answer heads: nominative persons (Vietnamese from C.PERSON_GEN), places (C.PLACE_LOC), pronouns
# ---------------------------------------------------------------------------------------------------------------
PERSON_NOM = {   # Pāli nominative → the C.PERSON_GEN key it shares its Vietnamese with
    "Anāgāmī": "Anāgāmissa", "Puthujjano": "Puthujjanassa",
    "Dve puggalā": "Dvinnaṃ puggalānaṃ", "Tayo puggalā": "Tiṇṇaṃ puggalānaṃ", "Cattāro puggalā": "Catunnaṃ puggalānaṃ",
    "Teva puggalā": "Tesaññeva puggalānaṃ", "Sveva puggalo": "Tasseva puggalassa",
}
PERSON_NOM = {k: C.PERSON_GEN[v] for k, v in PERSON_NOM.items()}   # → (Vietnamese, number)
PRON_NOM = {"so": C.PRON["tassa"], "te": C.PRON["tesaṃ"], "tato": C.PRON["tattha"]}   # người ấy / những người ấy / nơi ấy


def pron_vi(pron):
    """'tato' → «ở nơi ấy»; 'so tato' → «người ấy, ở nơi ấy»; 'te tato' → «những người ấy, ở nơi ấy»."""
    w = pron.split()
    if w == ["tato"]:
        return f"{C.AT} {PRON_NOM['tato']}"
    if len(w) == 2 and w[0] in ("so", "te") and w[1] == "tato":
        return f"{PRON_NOM[w[0]]}, {C.AT} {PRON_NOM['tato']}"
    raise ValueError(f"unknown pronoun {pron!r}")


def parse_head(txt):
    """'<person>? <places>* <so tato | te tato | tato>?' → (person | None, [places], resumptive | '')."""
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
    return out + (f", {C.THEN} {pron_vi(res)} " if res else " ")


SENT_RE = re.compile(r"(.+?)(?:, no ca (?:(so tato|te tato|tato) )?(.+))?\.")


def pe_tail(s, fn):
    """'<sentence>…pe….' / '<sentence> …pe….' → fn('<sentence>.') with its «.» replaced by «…» (same spot)."""
    m = re.fullmatch(r"(.+?)( ?)…pe…\.", s)
    if not m:
        return None
    vi = fn(m.group(1) + ".")
    assert vi.endswith("."), vi
    return vi[:-1] + m.group(2) + S.PE


def sentence(s):
    """Āmantā. / No. / Natthi. / [<head>] <clause>[, no ca [<pron>] <clause>]. (+ a «…pe….» tail)"""
    if (t := pe_tail(s, sentence)) is not None:
        return t
    if s in C.EXACT:
        return C.EXACT[s]
    m = SENT_RE.fullmatch(s)
    if not m:
        raise ValueError(f"unknown sentence {s!r}")
    words = m.group(1).split()
    i = next((k for k, w in enumerate(words) if C.is_anusaya(w.split("…")[0][:1].lower() + w.split("…")[0][1:])),
             None)
    if i is None:
        raise ValueError(f"no tendency in {s!r}")
    groups = parse_pred(" ".join([words[i][:1].lower() + words[i][1:]] + words[i + 1:]))
    num = groups[0][1]
    if i == 0:                                   # bare answer: «Có A.»
        person, places, res = None, [], ""
        out = cap(pred_vi(groups))
        if num != 1:
            raise ValueError(f"bare answer in the plural: {s!r}")
    else:
        if words[i][0].isupper():
            raise ValueError(f"capital tendency after a head: {s!r}")
        person, places, res = parse_head(" ".join(words[:i]))
        want = PERSON_NOM[person][1] if person else 1
        if num != want:
            raise ValueError(f"predicate number does not fit the head: {s!r}")
        out = head_vi(person, places, res) + pred_vi(groups)
    if m.group(3):
        pron = m.group(2) or ""
        if pron != res:
            raise ValueError(f"'no ca {pron}' does not fit the head ({res!r}): {s!r}")
        ng = parse_pred(m.group(3))
        if ng[0][1] != num:
            raise ValueError(f"'no ca' number does not fit: {s!r}")
        out += f", {C.BUT} " + (pron_vi(pron) + " " if pron else "") + neg_vi(ng)
    return out + "."


def answers(text):
    parts = [x for x in re.split(r"(?<=\.) ", text.strip()) if x]
    return " ".join(sentence(x) for x in parts)


# ---------------------------------------------------------------------------------------------------------------
# 3. Questions: yo / so (nominative person), yato / tato (place: = C's yattha / tattha wording), yo yato / so tato
# ---------------------------------------------------------------------------------------------------------------
YO_REL = {   # relative → (who / where, that one / there)
    "yo": ("người nào", "người ấy"),
    "yato": (f"{C.AT} nơi nào", f"{C.AT} nơi ấy"),
    "yo yato": (f"người nào, {C.AT} nơi nào", f"người ấy, {C.AT} nơi ấy"),
}
YO_COR = {"yo": "so", "yato": "tato", "yo yato": "so tato"}


def yo_q(rel, a, b, label=None, vapana=False):
    """(Ka) yo A so B ti? = «(a) Người nào mà A, thì người ấy có phải B không?»; (Kha) «(b) Còn người nào mà …»;
    yato «Ở nơi nào mà …, thì ở nơi ấy …» (= C.pair_q('yattha')); yo yato «Người nào, ở nơi nào mà …,
    thì người ấy, ở nơi ấy …». A / B = «có …»."""
    who, that = YO_REL[rel]
    s = f"{C.VA_PANA + ' ' if vapana else ''}{who} mà {a}, {C.THEN} {that} có phải {b} không?"
    s = cap(s)
    return f"{S.LABEL[label]} {s}" if label else s


Q_RE = re.compile(r"(?:\((Ka|Kha)\) )?([Yy])(o|ato)( vā pana)?( yato)? (.+?) (so tato|so|tato) (.+?)\?(?: (.+))?")


def question(body):
    m = Q_RE.fullmatch(body)
    if not m:
        return None
    label, y, rel1, vapana, yato, a, cor, b, rest = m.groups()
    rel = "y" + rel1 + (" yato" if yato else "")
    if yato and rel1 != "o":
        raise ValueError(f"bad relative in {body!r}")
    if YO_COR[rel] != cor:
        raise ValueError(f"relative {rel!r} with correlative {cor!r}: {body!r}")
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {body!r}")
    if label and (label == "Kha") != bool(vapana):
        raise ValueError(f"label {label} with vā pana={bool(vapana)}: {body!r}")
    bw = b.split()
    bw[-1] = C.strip_ti(bw[-1])
    ga, gb = parse_pred(a), parse_pred(" ".join(bw))
    if ga[0][1] != 1 or gb[0][1] != 1 or len(ga) != 1 or len(gb) != 1:
        raise ValueError(f"question slots must be one singular predicate: {body!r}")
    out = yo_q(rel, pred_vi(ga), pred_vi(gb), label, bool(vapana))
    if rel == "yato":   # the place shell is C's yattha shell word for word
        assert out == C.pair_q("yattha", pred_vi(ga), pred_vi(gb), label, bool(vapana)), out
    return out + (" " + answers(rest) if rest else "")


# ---------------------------------------------------------------------------------------------------------------
# 4. Headings and fixed lines
# ---------------------------------------------------------------------------------------------------------------
SANUSAYAVARO = C.FAMILY_HEADINGS["Sānusayavāro"]   # «Mục về sự có khuynh hướng tiềm ẩn» (termbase)
FIXED = {   # Sānusayavāre anulomaṃ. built as C's «Anusayavāre anulomaṃ.»
    "Sānusayavāre anulomaṃ.": f"{C.HEADINGS['anulomaṃ']} trong {SANUSAYAVARO[0].lower()}{SANUSAYAVARO[1:]}.",
}
assert C.FIXED["Anusayavāre anulomaṃ."] == f"{C.HEADINGS['anulomaṃ']} trong {C.ANUSAYAVARO[0].lower()}{C.ANUSAYAVARO[1:]}."


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


TERMBASE_USED = [   # pi-6 termbase entries used verbatim (asserted as C does)
    ("sānusayo", HAVE), ("sānusayoti", HAVE), ("sānusayā", HAVE), ("Sānusayavāro", "mục về sự có khuynh hướng tiềm ẩn"),
    ("Sānusayavāre", "mục về sự có khuynh hướng tiềm ẩn"), ("Anāgāmī", "bậc không trở lại"),
    ("Puthujjano", "người phàm phu"), ("puggalā", "hạng người"), ("puggalo", "hạng người"),
    ("anulomapuggalo", "chiều thuận theo người"), ("anulomaokāso", "chiều thuận theo nơi chốn"),
    ("anulomapuggalokāsā", "chiều thuận theo người và nơi chốn"), ("anulomaṃ", "chiều thuận"),
    ("kāmarāgānusayena", C.ANUSAYA["kāmarāg"]), ("paṭighānusayena", C.ANUSAYA["paṭigh"]),
    ("mānānusayena", C.ANUSAYA["mān"]), ("diṭṭhānusayena", C.ANUSAYA["diṭṭh"]),
    ("vicikicchānusayena", C.ANUSAYA["vicikicch"]), ("bhavarāgānusayena", C.ANUSAYA["bhavarāg"]),
    ("avijjānusayena", C.ANUSAYA["avijj"]), ("dvīsu vedanāsu", "hai loại cảm giác"),
    ("tīsu vedanāsu", "ba loại cảm giác"), ("Dukkhāya vedanāya", "cảm giác khó chịu"),
]


def check_reused():
    C.check_reused()   # 7-01's (pi-N) strings and termbase strings (all reused here through C)
    tb = C.TERMBASE.read_text(encoding="utf-8")
    bad = [(p, v) for p, v in TERMBASE_USED
           if not re.search(r"^" + re.escape(p) + r": \{[^\n]*: " + re.escape(v) + r"[};]", tb, re.M)]
    assert not bad, "termbase strings not found: " + repr(bad)


# ---------------------------------------------------------------------------------------------------------------
# 5. Notes file
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-03 (Anusayayamaka, sānusayavāra anuloma): frames and fixed strings", "",
         "Generated by build_rails_7-03_vi.py. Family C (setter 7-01): tendencies, places, pronouns, "
         "«không có A, cũng không có B», both-frame «…, cũng …», (Xmūlakaṃ) labels and headings are imported from "
         "build_rails_7-01_vi unchanged. New here: the nominative yo / yato shell and nominative person heads "
         "(7-04 niranusayo, 7-05 … pajahati share the shape). Later chapters import the module "
         "(importlib.import_module(\"build_rails_7-03_vi\")).", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    h("Predicate (termbase sānusayo «có»)")
    row("A-ena sānusayo / sānusayā", f"{HAVE} A")
    row("A-ena ca B-ena ca sānusayo", f"{HAVE} A {C.AND} B")
    row("A-ena ca sānusayo B-ena ca sānusayo (both)", f"{HAVE} A, {C.ALSO} {HAVE} B")
    row("no ca A-ena sānusayo", f"{C.BUT} {C.NEITHER_FIRST} A")
    row("no ca A-ena ca B-ena ca sānusayo (neither; user rule)", f"{C.BUT} {C.NEITHER_FIRST} A, {C.NEITHER_NEXT} B")
    row("Mānānusayena sānusayo. (bare answer)", sentence("Mānānusayena sānusayo."))
    row("<sentence>…pe…. / Āmantā …pe….", f"<câu>… / {C.YES[:-1]} …")
    h("Questions (yo / so, yato / tato, yo yato / so tato)")
    a, b = f"{HAVE} A", f"{HAVE} B"
    row("(Ka) yo A sānusayo so B sānusayoti?", yo_q("yo", a, b, "Ka"))
    row("(Kha) yo vā pana B sānusayo so A sānusayoti?", yo_q("yo", b, a, "Kha", True))
    row("Yo … so …ti? / Yo vā pana … (no label)", yo_q("yo", a, b) + " / " + yo_q("yo", b, a, None, True))
    row("(Ka) yato … tato …ti? (= 7-01 yattha shell)", yo_q("yato", a, b, "Ka"))
    row("(Kha) yato vā pana … tato …ti?", yo_q("yato", b, a, "Kha", True))
    row("(Ka) yo yato … so tato …ti?", yo_q("yo yato", a, b, "Ka"))
    row("(Kha) yo vā pana yato … so tato …ti?", yo_q("yo yato", b, a, "Kha", True))
    h("Answer heads (nominative persons; Vietnamese = 7-01 PERSON_GEN without «Ở»)")
    for k, (v, n) in PERSON_NOM.items():
        row(f"{k} …", f"{cap(v)} …")
    row("<places> tato …", f"{cap(C.AT)} <nơi>, {C.AT} <nơi>, {C.THEN} {pron_vi('tato')} …")
    row("<person sg> <places> so tato …", f"<Người>, {C.AT} <nơi>, {C.THEN} {pron_vi('so tato')} …")
    row("<person pl> <places> te tato …", f"<Người>, {C.AT} <nơi>, {C.THEN} {pron_vi('te tato')} …")
    row(", no ca tato / so tato / te tato …", f", {C.BUT} {pron_vi('tato')} / {pron_vi('so tato')} / "
        f"{pron_vi('te tato')} {C.NEITHER_FIRST} …")
    o.append("")
    o.append("Examples (built by the module):")
    for p in ("Anāgāmī mānānusayena sānusayo, no ca kāmarāgānusayena ca paṭighānusayena ca sānusayo.",
              "Tayo puggalā mānānusayena ca sānusayā kāmarāgānusayena ca sānusayā.",
              "Rūpadhātuyā arūpadhātuyā tato mānānusayena sānusayo, no ca tato kāmarāgānusayena sānusayo.",
              "Teva puggalā kāmadhātuyā dvīsu vedanāsu te tato mānānusayena ca kāmarāgānusayena ca sānusayā, "
              "no ca te tato paṭighānusayena sānusayā."):
        row(p, sentence(p))
    h("Fixed lines")
    for k, v in FIXED.items():
        row(k, v)
    o.append("")
    return "\n".join(o)


def main():
    check_reused()
    segs = build(CHAPTER)
    C.write(CHAPTER, segs, extra_dirs=(ADH_DIR,))
    NOTES_MD.write_text(unicodedata.normalize("NFC", notes()), encoding="utf-8", newline="\n")
    print("wrote", NOTES_MD)
    for p, v in sorted(set(C.SLIPS_SEEN)):
        print("slip rendered as meant:", p, "→", v)


if __name__ == "__main__":
    main()
