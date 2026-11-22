"""pi-6 Yamaka, Vietnamese plain RAILS: chapter 7-04 (Anusayayamaka: sānusayavāra, paṭiloma: niranusayo).

Imports (READ-ONLY): build_rails_sample_vi (S) and the family-C setter build_rails_7-01_vi (C). Importing this module
writes nothing; outputs are written only under `if __name__ == "__main__":`.
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-vi-ai\\rails")
    import importlib; R = importlib.import_module("build_rails_7-04_vi")

Frames set here (nominative person yo / so, place yato / tato, person + place yo yato / so tato; the
"-ena niranusayo" predicate; "no ca … niranusayo" = «vẫn có …»; sabbattha; apariyāpanne):
  PERSON_NOM / PLACE_LOC_NOM / pair_q_nom()   persons (nominative), places, the yo / yo yato question shell
  without_vi() / still_has_vi()               «không có A, cũng không có B» / «vẫn có A và B»
  sentence() / answers() / question()         answer sentences and question lines
A line the parsers cannot place raises ValueError: there is no silent fallback.

usage: python -I -X utf8 -B build_rails_7-04_vi.py
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
T2 = importlib.import_module("build_rails_7-02_vi")  # negative frames, apariyāpanne, sabbattha (READ-ONLY)
T3 = importlib.import_module("build_rails_7-03_vi")  # nominative yo / so shell and person heads (READ-ONLY)

CHAPTER = "7-04-anusayayamaka.md"
NOTES_MD = RAILS_DIR / "notes-rails-7-04.md"
ADH_DIR = RAILS_DIR / "adh-7-04"
cap = S.cap
SLIPS_SEEN = []

# ---------------------------------------------------------------------------------------------------------------
# 1. Predicate: "<tendencies>-ena niranusayo" (termbase niranusayo «không có»; sānusayo «có»)
# ---------------------------------------------------------------------------------------------------------------
NIRANUSAYO = C.FAMILY_TERMS["niranusayo"]        # «không có»
SANUSAYO = C.FAMILY_TERMS["sānusayo"]            # «có» (after "no ca" the negative niranusayo is denied)
STILL_HAS = f"{C.STILL} {SANUSAYO}"              # «vẫn có» (coordinator: «vẫn» after no ca + negative)
NEITHER_NEXT = C.NEITHER_NEXT                    # «cũng không có»
ADJ = {"niranusayo": 1, "niranusayā": 2}         # number agrees with the person (not with the tendencies)
ADJ_RE = re.compile(r" (niranusayo|niranusayā)(?= |$)")


def without_vi(tp):
    """'A' «không có A»; 'A ca B ca' (neither) «không có A, cũng không có B»; 'A…pe… B' «không có A… B»."""
    if tp["pe"]:
        if tp["conj"]:
            raise ValueError("…pe… inside an 'A ca … ca' list: " + repr(tp))
        return f"{NIRANUSAYO} {C.tp_vi(tp)}"
    return f"{NIRANUSAYO} " + f", {NEITHER_NEXT} ".join(tp["names"])


def still_has_vi(tp):
    """After 'no ca': «vẫn có A» / «vẫn có A và B» / «vẫn có A, B và C» (coordinator, 7-01)."""
    if tp["pe"]:
        raise ValueError("…pe… inside a 'no ca' part: " + repr(tp))
    return f"{STILL_HAS} {C.tp_vi(tp)}"


def parse_groups(text, allow_missing_ca=False):
    """'<run> niranusayo|niranusayā [<run> niranusayo|niranusayā]' → ([tp, …], number)."""
    parts = ADJ_RE.split(" " + text.strip())
    if parts[-1].strip():
        raise ValueError(f"clause does not end in niranusayo / niranusayā: {text!r}")
    groups, nums = [], set()
    for run, adj in zip(parts[0:-1:2], parts[1::2]):
        groups.append(C.parse_tp(run.strip()))
        nums.add(ADJ[adj])
    if len(nums) != 1:
        raise ValueError(f"mixed number in {text!r}")
    if len(groups) == 2:
        g1, g2 = groups
        if not g2["conj"] or g1["pe"] or g2["pe"]:
            raise ValueError(f"unknown both-frame {text!r}")
        if not g1["conj"]:
            if not (allow_missing_ca and len(g1["names"]) == 1):
                raise ValueError(f"both-frame without 'ca' in {text!r}")
            SLIPS_SEEN.append((text.split()[0] + " niranusayo (no ca)", text.split()[0] + " ca niranusayo"))
    elif len(groups) != 1:
        raise ValueError(f"more than two groups in {text!r}")
    return groups, nums.pop()


def clause_vi(groups):
    """One group: «không có A[, cũng không có B]». Both-frame 'A ca niranusayo B ca niranusayo'
    (coordinator «A V, B cũng V») = «không có A, cũng không có B» (lists: one «cũng không có» per item)."""
    names = [n for tp in groups for n in tp["names"]]
    if len(groups) == 1:
        return without_vi(groups[0])
    return f"{NIRANUSAYO} " + f", {NEITHER_NEXT} ".join(names)


# ---------------------------------------------------------------------------------------------------------------
# 2. Answer heads: persons (nominative), places, resumptives (tato «ở nơi ấy» = tattha, commentary ^6-113)
# ---------------------------------------------------------------------------------------------------------------
PERSON_NOM = {**T3.PERSON_NOM,                  # 7-03 nominative persons (Vietnamese = C.PERSON_GEN)
              "Arahā": C.PERSON_GEN["Arahato"]}  # not in 7-03: termbase Arahā «bậc A-la-hán» (= C's Arahato)
APARIYAPANNE = T2.APARIYAPANNE                   # «những gì không nằm trong các cõi tồn tại» (7-02; pi-1 / pi-2)
PLACE_LOC_NOM = T2.PLACE_LOC                     # C.PLACE_LOC + apariyāpanne (7-02)
PLACE_SLIPS = {"ariyāpanne": "apariyāpanne"}   # ^6-7-130 «Sveva puggalo dukkhāya vedanāya ariyāpanne»: slip
AT, THEN, BUT = C.AT, C.THEN, C.BUT
SABBATTHA = f"{AT} {T2.SABBATTHA}"               # «ở mọi nơi» (7-02; pi-5)
pron_nom = T3.pron_vi      # 'tato' «ở nơi ấy»; 'so tato' «người ấy, ở nơi ấy»; 'te tato' «những người ấy, ở nơi ấy»


def parse_head(txt):
    """'<person>? sabbattha? <places>* <resumptive>?' → (person | None, sabbattha?, [places], resumptive)."""
    person, rest = C._take(txt, PERSON_NOM)
    sabb = False
    if rest == "sabbattha" or rest.startswith("sabbattha "):
        sabb, rest = True, rest[len("sabbattha"):].strip()
    places = []
    while rest:
        w = rest.split()[0]
        if w in PLACE_SLIPS:
            SLIPS_SEEN.append((w, PLACE_SLIPS[w]))
            rest = PLACE_SLIPS[w] + rest[len(w):]
        p, rest2 = C._take(rest, PLACE_LOC_NOM, fold=True)
        if not p:
            break
        places.append(p)
        rest = rest2
    if rest not in ("", "tato", "so tato", "te tato"):
        raise ValueError(f"unknown answer head {txt!r} (left: {rest!r})")
    if not person and not places:
        raise ValueError(f"empty answer head {txt!r}")
    if sabb and (not person or places or rest):
        raise ValueError(f"sabbattha out of place: {txt!r}")
    if person and places and rest != ("so tato" if PERSON_NOM[person][1] == 1 else "te tato"):
        raise ValueError(f"person + place without a fitting 'so / te tato': {txt!r}")
    if person and not places and rest:
        raise ValueError(f"person head with a resumptive: {txt!r}")
    if not person and rest != "tato":
        raise ValueError(f"place head without 'tato': {txt!r}")
    return person, sabb, places, rest


def head_vi(person, sabb, places, res):
    """«Bậc không trở lại …» / «Hai hạng người, ở mọi nơi, …» / «Ở <nơi>, ở <nơi>, thì ở nơi ấy …» /
    «Ba hạng người, ở <nơi>, thì những người ấy, ở nơi ấy …»."""
    where = ", ".join(f"{AT} {PLACE_LOC_NOM[p]}" for p in places)
    if person and sabb:
        return f"{cap(PERSON_NOM[person][0])}, {SABBATTHA}, "
    if person and places:
        return f"{cap(PERSON_NOM[person][0])}, {where}, {THEN} {pron_nom(res)} "
    if person:
        return f"{cap(PERSON_NOM[person][0])} "
    return f"{cap(where)}, {THEN} {pron_nom(res)} "


# ---------------------------------------------------------------------------------------------------------------
# 3. Answer sentences
# ---------------------------------------------------------------------------------------------------------------
NOCA_RE = re.compile(r"(,?) no ca (?:(so tato|te tato|tato) )?")
PE_END_RE = re.compile(r"(.*?)( ?)…pe…\.")
EXACT = C.EXACT                                  # Āmantā. / No. / Natthi.


def sentence(s, allow_missing_ca=False):
    if s in EXACT:
        return EXACT[s]
    if m := PE_END_RE.fullmatch(s):              # '… …pe….' / 'Āmantā…pe….': «…» at the same spot, «.» absorbed
        return sentence(m.group(1) + ".", allow_missing_ca)[:-1] + (" …" if m.group(2) else "…")
    if not s.endswith("."):
        raise ValueError(f"sentence without a final '.': {s!r}")
    body = s[:-1]
    parts = NOCA_RE.split(body)
    if len(parts) not in (1, 4):
        raise ValueError(f"unknown sentence {s!r}")
    words = parts[0].split()
    i = next((k for k, w in enumerate(words) if C.is_anusaya(w.split("…")[0])), None)
    if not i:
        raise ValueError(f"no head / no tendency in {s!r}")
    person, sabb, places, res = parse_head(" ".join(words[:i]))
    groups, num = parse_groups(" ".join(words[i:]), allow_missing_ca)
    want_num = PERSON_NOM[person][1] if person else 1
    if num != want_num:
        raise ValueError(f"niranusayo / niranusayā does not fit the head: {s!r}")
    out = head_vi(person, sabb, places, res) + clause_vi(groups)
    if len(parts) == 4:
        comma, pron, rest = parts[1], parts[2] or "", parts[3]
        if not comma:
            SLIPS_SEEN.append(("… niranusayo no ca … (no comma)", "… niranusayo, no ca …"))
        if pron != res:
            raise ValueError(f"'no ca {pron}' does not fit the head ({res!r}): {s!r}")
        g2, num2 = parse_groups(rest)
        if len(g2) != 1 or num2 != num:
            raise ValueError(f"unknown 'no ca' part in {s!r}")
        out += f", {BUT} " + (f"{pron_nom(pron)} " if pron else "") + still_has_vi(g2[0])
    return out + "."


def answers(text):
    parts = [x for x in re.split(r"(?<=\.) ", text.strip()) if x]
    # ^6-7-127 «Arahā sabbattha bhavarāgānusayena niranusayo kāmarāgānusayena ca …»: the first 'ca' is missing
    return " ".join(sentence(x, allow_missing_ca=x.startswith("Arahā sabbattha ")) for x in parts)


# ---------------------------------------------------------------------------------------------------------------
# 4. Questions: yo / so (person), yato / tato (place = yattha / tattha, commentary ^6-113), yo yato / so tato
# ---------------------------------------------------------------------------------------------------------------
Q_RE = re.compile(r"(?:\((Ka|Kha)\) )?([Yy])(o|ato)( vā pana)?( yato)? (.+?) (so tato|so|tato) (.+?)\?(?: (.+))?")
Q_COR = T3.YO_COR                                # yo → so, yato → tato, yo yato → so tato
# (Ka) yo A so B ti? = «(a) Người nào mà A, thì người ấy có phải B không?»; (Kha) «(b) Còn người nào mà …»;
# yato = C's yattha shell «Ở nơi nào mà …, thì ở nơi ấy …»; yo yato «Người nào, ở nơi nào mà …, thì người ấy, ở nơi ấy …»
pair_q_nom = T3.yo_q                             # 7-03 (byte for byte)


def slot(text):
    groups, num = parse_groups(text)
    if num != 1 or len(groups) != 1:
        raise ValueError(f"question slot {text!r}")
    return clause_vi(groups)


def question(body):
    m = Q_RE.fullmatch(body)
    if not m:
        return None
    label, y, rel1, vapana, yato, a, cor, b, rest = m.groups()
    rel = "y" + rel1 + (" yato" if yato else "")
    if yato and rel1 != "o":
        raise ValueError(f"bad relative in {body!r}")
    if Q_COR[rel] != cor:
        raise ValueError(f"relative {rel!r} with correlative {cor!r}: {body!r}")
    if bool(label) != (y == "y"):
        raise ValueError(f"label / capital mismatch: {body!r}")
    if label and (label == "Kha") != bool(vapana):
        raise ValueError(f"label {label} with vā pana={bool(vapana)}: {body!r}")
    bw = b.split()
    bw[-1] = C.strip_ti(bw[-1])
    av, bv = slot(a), slot(" ".join(bw))
    out = pair_q_nom(rel, av, bv, label, bool(vapana))
    if rel == "yato":   # the place shell is C's yattha shell word for word (as 7-03)
        assert out == C.pair_q("yattha", av, bv, label, bool(vapana)), out
    return out + (" " + answers(rest) if rest else "")


# ---------------------------------------------------------------------------------------------------------------
# 5. Fixed lines, line translator
# ---------------------------------------------------------------------------------------------------------------
SANUSAYAVARO = C.FAMILY_HEADINGS["Sānusayavāro"]          # «Mục về sự có khuynh hướng tiềm ẩn»
FIXED = {
    "Sānusayavāre paṭilomaṃ.": f"{cap(S.LATER_HEADINGS[1][1])} trong {SANUSAYAVARO[0].lower()}{SANUSAYAVARO[1:]}.",
    "Sānusayavāro.": SANUSAYAVARO + ".",
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
# 6. Reuse assertions
# ---------------------------------------------------------------------------------------------------------------
REUSED = [
    ("apariyāpanna", "không nằm trong các cõi tồn tại", "2"),
    ("apariyāpannā dhammā", "không nằm trong các cõi tồn tại", "1"),
    ("sabbattha", SABBATTHA, "5"),
    ("Tayo puggalā", "ba hạng người", "4"),
    ("Cattāro puggalā", "bốn hạng người", "4"),
    ("Dve puggalā", "hai hạng người", "4"),
]
TERMBASE_USED = [
    ("niranusayo", NIRANUSAYO), ("niranusayoti", NIRANUSAYO), ("niranusayā", NIRANUSAYO),
    ("sānusayo", SANUSAYO), ("Anāgāmī", PERSON_NOM["Anāgāmī"][0]), ("Arahā", PERSON_NOM["Arahā"][0]),
    ("Puthujjano", PERSON_NOM["Puthujjano"][0]), ("puggalā", "hạng người"), ("puggalo", "hạng người"),
    ("paṭilomaṃ", "chiều ngược"), ("Sānusayavāre", "mục về sự có khuynh hướng tiềm ẩn"),
    ("Sānusayavāra", "mục về sự có khuynh hướng tiềm ẩn"), ("paṭilomaokāso", "chiều ngược theo nơi chốn"),
    ("paṭilomapuggalokāsā", "chiều ngược theo người và nơi chốn"),
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
    # heads shared with 7-03 stay byte-identical
    for h in ("Anāgāmī", "Dve puggalā", "Dukkhāya vedanāya tato", "Rūpadhātuyā arūpadhātuyā tato",
              "Tayo puggalā kāmadhātuyā dvīsu vedanāsu te tato", "Sveva puggalo dukkhāya vedanāya so tato",
              "Teva puggalā rūpadhātuyā arūpadhātuyā te tato"):
        p, sabb, pl, r = parse_head(h)
        assert head_vi(p, sabb, pl, r) == T3.head_vi(*T3.parse_head(h)), h


# ---------------------------------------------------------------------------------------------------------------
# 7. Notes
# ---------------------------------------------------------------------------------------------------------------
def notes():
    o = ["# Rails 7-04 (Anusayayamaka, sānusayavāra paṭiloma): frames and fixed strings", "",
         "Generated by build_rails_7-04_vi.py. Imports S (sample), C (build_rails_7-01_vi, family C setter), "
         "build_rails_7-02_vi (apariyāpanne, sabbattha) and build_rails_7-03_vi (yo / yato / yo yato shell, "
         "nominative person heads, tato / so tato / te tato): those strings are theirs, byte for byte. New here: "
         "the -ena niranusayo predicate and «nhưng vẫn có …» after no ca.", ""]

    def row(p, v):
        o.append(f"{p} = {v}")

    def h(t):
        o.extend(["", f"## {t}", ""])

    h("Predicate")
    row("A-ena niranusayo", f"{NIRANUSAYO} A")
    row("A-ena ca B-ena ca niranusayo (neither, coordinator rule)", f"{NIRANUSAYO} A, {NEITHER_NEXT} B")
    row("A-ena…pe… B-ena niranusayo (cut)", f"{NIRANUSAYO} A… B")
    row("A-ena ca niranusayo B-ena ca niranusayo (both-frame «A V, B cũng V»)", f"{NIRANUSAYO} A, {NEITHER_NEXT} B")
    row("A ca niranusayo B ca C ca niranusayo", f"{NIRANUSAYO} A, {NEITHER_NEXT} B, {NEITHER_NEXT} C")
    row(", no ca A-ena niranusayo (negative denied: «vẫn»)", f", {BUT} {STILL_HAS} A")
    row(", no ca A-ena ca B-ena ca niranusayo", f", {BUT} {STILL_HAS} A {C.AND} B")
    row(", no ca tato … / no ca so tato … / no ca te tato …",
        f", {BUT} {pron_nom('tato')} {STILL_HAS} … / , {BUT} {pron_nom('so tato')} {STILL_HAS} … / "
        f", {BUT} {pron_nom('te tato')} {STILL_HAS} …")
    h("Questions")
    row("(Ka) yo A niranusayo so B niranusayoti?", pair_q_nom("yo", "không có A", "không có B", "Ka"))
    row("(Kha) yo vā pana B … so A …ti?", pair_q_nom("yo", "không có B", "không có A", "Kha", True))
    row("Yo … so …ti? (no label)", pair_q_nom("yo", "không có A", "không có B"))
    row("(Ka) yato … tato …ti? (= yattha / tattha, commentary ^6-113)",
        C.pair_q("yattha", "không có A", "không có B", "Ka"))
    row("(Ka) yo yato … so tato …ti?", pair_q_nom("yo yato", "không có A", "không có B", "Ka"))
    row("(Kha) yo vā pana yato … so tato …ti?", pair_q_nom("yo yato", "không có B", "không có A", "Kha", True))
    h("Answer heads (nominative persons; each place its own «ở»)")
    for k, (v, n) in PERSON_NOM.items():
        row(f"{k} … (person only)", f"{cap(v)} …")
    row("apariyāpanne (place)", f"{AT} {APARIYAPANNE}")
    row("ariyāpanne (slip, ^6-7-130)", f"{AT} {APARIYAPANNE}")
    row("<person> sabbattha …", f"<Người>, {SABBATTHA}, …")
    row("<places> tato …", f"{cap(AT)} <nơi>, {AT} <nơi>, {THEN} {pron_nom('tato')} …")
    row("<person sg> <places> so tato …", f"<Người>, {AT} <nơi>, {THEN} {pron_nom('so tato')} …")
    row("<person pl> <places> te tato …", f"<Người>, {AT} <nơi>, {THEN} {pron_nom('te tato')} …")
    o.append("")
    o.append("Examples (built by the module):")
    for p in ("Anāgāmī kāmarāgānusayena niranusayo, no ca mānānusayena niranusayo.",
              "Arahā kāmarāgānusayena ca paṭighānusayena ca niranusayo mānānusayena ca niranusayo.",
              "Dukkhāya vedanāya tato kāmarāgānusayena niranusayo, no ca tato paṭighānusayena niranusayo.",
              "Rūpadhātuyā arūpadhātuyā apariyāpanne tato kāmarāgānusayena ca niranusayo paṭighānusayena ca niranusayo.",
              "Tayo puggalā kāmadhātuyā dvīsu vedanāsu te tato bhavarāgānusayena ca paṭighānusayena ca niranusayā, "
              "no ca te tato kāmarāgānusayena ca mānānusayena ca niranusayā.",
              "Dve puggalā sabbattha kāmarāgānusayena ca niranusayā paṭighānusayena ca niranusayā.",
              "Arahā vicikicchānusayena ca niranusayo kāmarāgānusayena ca paṭighānusayena ca mānānusayena ca "
              "diṭṭhānusayena ca niranusayo …pe…."):
        row(p, sentence(p))
    h("Fixed lines")
    row("Āmantā …pe…. / Āmantā…pe….", f"{C.YES[:-1]} … / {C.YES[:-1]}…")
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
    for p, v in sorted(set(SLIPS_SEEN + C.SLIPS_SEEN)):
        print("slip rendered as meant:", p, "→", v)


if __name__ == "__main__":
    main()
