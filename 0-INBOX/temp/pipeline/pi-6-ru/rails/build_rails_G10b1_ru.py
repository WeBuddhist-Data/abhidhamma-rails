"""pi-6 Yamaka, G10b1 (Indriyayamaka 10-05 … 10-08): Russian RAILS builder.

Built on G10a (faculties, persons, moments, pavatti answers: build_rails_G10a_ru.py), which stands on the
frame-setters G2 (paṇṇatti / pavatti frames, mixed tenses) and G8 (moments), and on G3 (sa-/a-X-ka persons,
-āvacara planes, «ye … upapajjitvā parinibbāyissanti» with several planes, mūlaka labels, «…pe…» questions) and
G45 (intro_ru: person / time / place intros). Importing this module writes nothing:
    import sys, importlib
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru\\rails")
    G10b1 = importlib.import_module("build_rails_G10b1_ru")
    G10b1.translate_line(pali_line)
New here (exposed for later groups): UNITS_G10b1 (intro units, prepended to G45.UNITS on import):
    ye / yā (ca) purisā / itthiyo eteneva bhāvena katici bhave dassetvā (ATTR upapajjitvā) parinibbāyissanti
      = «у тех мужчин / женщин, которые, пройдя в этом же состоянии несколько существований, (переродившись …,)
         достигнут окончательного угасания»  (coordinator shape)
    ye (ca) ATTR… PLANE… upapajjitvā parinibbāyissanti = «у тех, кто, переродившись с глазом и с невозмутимостью
      (в мире форм), достигнет окончательного угасания»  (G2 / G3 frame with the G10a attributes)
    yassa cittassa anantarā X-sampayuttapacchimacittaṃ uppajjissati = «у тех, у кого сразу после данного ума
      возникнет последний ум, связанный с X,» (G6 frame)
    ATTR… PLANE… upapajjantānaṃ / cavantānaṃ = «у тех, кто перерождается без глаза в мире чувственных желаний»
    X-ānaṃ upapajjantānaṃ (beings + participle) = «у перерождающихся существ X»
  then G2's person groups (incl. G3's) as a fallback unit list (pacchimabhavikānaṃ, X-e parinibbantānaṃ …).
Run as a script (python -I -X utf8 -B build_rails_G10b1_ru.py) to write 10-05 … 10-08 + notes-rails-G10b1.md
and run the per-line checks; `--probe <ch> …` prints the sentences without a formula (writes nothing).

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
"""
import importlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_sample_ru as S  # noqa: E402

G10a = importlib.import_module("build_rails_G10a_ru")
G2, G8, G3, G45 = G10a.G2, G10a.G8, G10a.G3, G10a.G45

ROOT, PALI, OUT = S.ROOT, S.PALI, S.OUT
CHAPTERS = [f"10-0{i}-indriyayamaka.md" for i in range(5, 9)]
cap = S.cap
TERMS = G2.TERMS
_CUR = G2._CUR
SLIPS = []


def slip(note):
    SLIPS.append((_CUR["id"], note))


# =========================================================================== person intros (units for G45.intro_ru)
SAME_STATE = "пройдя в этом же состоянии несколько существований"   # eteneva bhāvena katici bhave dassetvā (coordinator)
WHO_PL = {"purisā": "у тех мужчин", "itthiyo": "у тех женщин"}         # termbase purisā «мужчины», itthiyo «женщины»
PARINIB_FUT_PL = "достигнут окончательного угасания"                    # parinibbāyissanti (termbase), plural «которые»
ATTR_NOM = {  # nominative attributes before «upapajjitvā» (termbase sacakkhukā «с глазом»; somanassena «радость»,
    #           upekkhāya «невозмутимость» as G10a; saghānakā: no entry, built as sacakkhukā / G3 saghānakānaṃ)
    "sacakkhukā": "с глазом", "saghānakā": "с носом",
    "somanassena": "с радостью", "upekkhāya": "с невозмутимостью",
}
ANANTARA = "сразу после данного ума"     # yassa cittassa anantarā (G6; termbase anantarā «сразу после»)
LAST_MIND = "последний ум"               # pacchimacittaṃ (termbase)
LAST_MIND_Q = {  # X-sampayuttapacchimacittaṃ (termbase «последний ум связанный с X»; G45 comma punctuation)
    "upekkhāsampayuttapacchimacittaṃ": f"{LAST_MIND}, связанный с невозмутимостью",
    "somanassasampayuttapacchimacittaṃ": f"{LAST_MIND}, связанный с радостью",
}


def _attr_nom(s):
    return " и ".join(ATTR_NOM[w] for w in s.split())


def _abs_phrase(a, p):
    """«переродившись с глазом и с невозмутимостью в мире форм» (attributes in the Pāli order, then the planes)."""
    r = G2.REBORN_ABS
    if a and a.strip():
        r += " " + _attr_nom(a.strip())
    if p and p.strip():
        r += " " + G2._places(p.strip(), G2.PL_ACC)
    return r


def _same_state(m):
    a = m.group("a")
    mid = f"{SAME_STATE}, " + (f"{_abs_phrase(a, '')}, " if a else "")
    if m.group("rel") == "yā" and m.group("who") != "itthiyo" or m.group("rel") == "ye" and m.group("who") != "purisā":
        slip("ye / yā does not agree with purisā / itthiyo; kept as written")
    return f"{WHO_PL[m.group('who')]}, которые, {mid}{PARINIB_FUT_PL}", True


def _attr_place(m):
    who = "у остальных, кто" if m.group("pre") else "у тех, кто"
    verb = G2.REBORN if m.group("w") == "upapajjantānaṃ" else G2.DIES
    table = G2.PL_ACC if m.group("w") == "upapajjantānaṃ" else G2.PL_ABL
    return f"{who} {verb} {G10a.attrs_ru(m.group('a').strip())} {G2._places(m.group('p').strip(), table)}", True


def _cavantana(m):
    slip("cavantāna for cavantānaṃ: spelling slip, rendered as meant (termbase entry)")
    return f"у тех, кто {G2.DIES} {G2._places(m.group(1).strip(), G2.PL_ABL)}", True


def _samangina(m):
    slip("Pacchimacittasamaṅgīna for -samaṅgīnaṃ: spelling slip, rendered as meant (termbase entry)")
    return "у обладающих последним умом", False


def _units():
    A, B, G = G2._alt(G2.PL_ACC), G2._alt(G2.PL_ABL), G2._alt(G2.BEINGS)
    AN = G2._alt(ATTR_NOM)
    AT = G10a._AT
    return [
        (rf"(?P<rel>ye|yā) (?:ca )?(?P<who>purisā|itthiyo) eteneva bhāvena katici bhave dassetvā "
         rf"(?:(?P<a>(?:{AN} ?)+) upapajjitvā )?parinibbāyissanti", "P", _same_state),
        (rf"ye (?:ca )?(?P<a>(?:{AN} )*)(?P<p>(?:{A} )*)upapajjitvā parinibbāyissanti(?! tesaṃ (?:cavantānaṃ|upapajjantānaṃ))",
         "P", lambda m: (f"у тех, кто, {_abs_phrase(m.group('a'), m.group('p'))}, {G2.PARINIB_FUT}", True)),
        (rf"yassa cittassa anantarā (?P<q>{G2._alt(LAST_MIND_Q)}) uppajjissati", "P",
         lambda m: (f"у тех, у кого {ANANTARA} возникнет {LAST_MIND_Q[m.group('q')]}", True)),
        (rf"(?P<pre>itaresaṃ )?(?P<a>(?:{AT} )+)(?P<p>(?:{A} )+)(?P<w>upapajjantānaṃ)", "P", _attr_place),
        (rf"(?P<pre>itaresaṃ )?(?P<a>(?:{AT} )+)(?P<p>(?:{B} )+)(?P<w>cavantānaṃ)", "P", _attr_place),
        (rf"({G}) upapajjantānaṃ", "P", lambda m: (f"у {G45.WHO_PART['upapajjantānaṃ']} {G2.BEINGS[m.group(1)]}", False)),
        (rf"((?:{B} )+)cavantāna", "P", _cavantana),
        (r"pacchimacittasamaṅgīna", "P", _samangina),
    ]


UNITS_G10b1 = None


def install_units():
    """Prepend the G10b1 units to G45.UNITS (after G10a's) and append G2's person groups (with G3's) as a fallback."""
    global UNITS_G10b1
    UNITS_G10b1 = _units()
    G45.UNITS[:0] = UNITS_G10b1
    G2.intro_groups("")
    G45.UNITS += [(rx, "P", fn) for rx, fn in G2.GROUP_RULES]


install_units()

# =========================================================================== sentences and lines
FIXED_S = {  # exact Pāli sentences kept as written (slips reported)
    # ^6-10-240: «yassa … tattha» (tassa expected): another real word, kept as written
    "Yassa vā pana purisindriyaṃ uppajjittha tattha cakkhundriyaṃ uppajjitthāti?":
        ("А у кого возникала способность мужественности, там возникала способность глаза?",
         "«yassa … tattha» where the frame has «yassa … tassa»; kept as written («у кого …, там …»)"),
    # ^6-10-301: a full stop splits «X ca uppajjissati Y ca uppajjissati»; wrong punctuation stays as written
    "Itaresaṃ kāmāvacarānaṃ tesaṃ tattha itthindriyañca uppajjissati.":
        ("У остальных существ мира чувственных желаний там и возникнет способность женственности.",
         "a full stop inside «itthindriyañca uppajjissati. Somanassindriyañca uppajjissati.»; kept as written "
         "(two sentences, «и возникнет …. И возникнет …»)"),
    "Somanassindriyañca uppajjissati.": ("И возникнет способность радости.", None),
}
_core0 = G10a.core


def core(s):
    if s in FIXED_S:
        ru, note = FIXED_S[s]
        if note:
            slip(note)
        return ru
    return _core0(s)


G10a.core = core   # G10a.translate_sentence / fragment look «core» up in their module (in memory only)

LINE_SLIPS = {  # Pāli as found -> (as meant, note): plain spelling slips and missing punctuation only
    "(Ghānandriyamūlakaṃ)": ("(Ghānindriyamūlakaṃ)",
                             "Ghānandriyamūlakaṃ for Ghānindriyamūlakaṃ: spelling slip, rendered as meant (termbase)"),
    "ghānindriyaṃ na uppajjissati no ca tattha": ("ghānindriyaṃ na uppajjissati, no ca tattha",
                                                  "missing comma before «no ca tattha»; rendered as meant"),
}
WORD_NOTES = {  # Pāli kept as written, reported
    "na upapajjissati": "«no ca tesaṃ somanassindriyaṃ na upapajjissati»: upapajjati for uppajjati, a one-letter slip "
                        "that makes another real word; kept as written («но у них переродится …», as G3 ^6-3-212)",
}


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian."""
    for a, (b, note) in LINE_SLIPS.items():
        if a in pali:
            slip(note)
            pali = pali.replace(a, b)
    for a, note in WORD_NOTES.items():
        if a in pali:
            slip(note)
    return G10a.translate_line(pali)


# =========================================================================== build + checks
def render(pali_text):
    blocks, problems = [], []
    for sid, plines in S.segs(pali_text):
        _CUR["id"] = G45._CUR["id"] = sid
        ru = []
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            r = translate_line(body)
            problems += [x for x in S.check_line(sid, body, r)
                         if not (": ellipsis:" in x and re.search(r"[?.] …", body) and "…." not in r
                                 and not re.search(r"[^?.] …", r))]
            ru.append(r)
        ru[-1] = f"{ru[-1]} ^{sid}"
        blocks.append("\n".join(ru))
    return "\n\n".join(blocks) + "\n", problems


def probe(ch):
    bad = 0
    for sid, plines in S.segs((PALI / ch).read_text(encoding="utf-8")):
        _CUR["id"] = G45._CUR["id"] = sid
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            try:
                translate_line(body)
            except (ValueError, KeyError, AssertionError, TypeError) as e:
                bad += 1
                print(sid, "|", body, "|", e)
    print(ch, "lines without a formula:", bad)


def notes_md():
    tl = translate_line
    L = ["# notes-rails-G10b1: Indriyayamaka (10-05 … 10-08) frames", "",
         "Format: Pāli = Russian, one per line. Builder: build_rails_G10b1_ru.py (importlib.import_module(",
         "\"build_rails_G10b1_ru\"); importing writes nothing). Everything else is G10a / G2 / G8 / G3 / G45 verbatim",
         "(see notes-rails-G10a.md). New: the intro units UNITS_G10b1 (prepended to G45.UNITS on import), G2's person",
         "groups (with G3's) appended to G45.UNITS as a fallback, and the slips below.", "",
         "## Person intros", ""]
    ex = ["Ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
          "Yā itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
          "Yā itthiyo eteneva bhāvena katici bhave dassetvā upekkhāya upapajjitvā parinibbāyissanti",
          "Ye rūpāvacaraṃ upapajjitvā parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā "
          "somanassena upapajjitvā parinibbāyissanti",
          "Rūpāvacarānaṃ arūpāvacarānaṃ yā ca itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti",
          "Ye rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti",
          "Ye sacakkhukā upekkhāya upapajjitvā parinibbāyissanti",
          "Ye saghānakā somanassena upapajjitvā parinibbāyissanti",
          "Pacchimabhavikānaṃ ye ca somanassena rūpāvacaraṃ upapajjitvā parinibbāyissanti",
          "Yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati",
          "Yassa cittassa anantarā somanassasampayuttapacchimacittaṃ uppajjissati asaññasattānaṃ",
          "Pañcavokārā cavantānaṃ acakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ arūpānaṃ",
          "Kāmāvacarā cavantānaṃ na itthīnaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacarānaṃ arūpāvacarānaṃ",
          "Sacakkhukānaṃ kāmāvacaraṃ upapajjantānaṃ",
          "Suddhāvāsānaṃ upapajjantānaṃ asaññasattānaṃ",
          "Kāmāvacare pacchimabhavikānaṃ rūpāvacarānaṃ arūpāvacarānaṃ",
          "Suddhāvāse parinibbantānaṃ asaññasattānaṃ arūpānaṃ"]
    L += [f"{p} tesaṃ = {G45.intro_ru(p)}" for p in ex]
    L += [f"eteneva bhāvena katici bhave dassetvā = {SAME_STATE}"
          " (coordinator shape; no termbase entry); «у тех мужчин / женщин, которые, …, достигнут» (plural verb)",
          "  a following «ATTR upapajjitvā» is a second absolutive after a comma: «…, переродившись с радостью, …»",
          "ye ATTR-ā (PLANE-aṃ) upapajjitvā = «переродившись с глазом и с невозмутимостью (в мире форм)»: sacakkhukā с глазом,",
          "  saghānakā с носом (no entry; as G3 saghānakānaṃ), somanassena с радостью, upekkhāya с невозмутимостью",
          "X-ānaṃ upapajjantānaṃ (beings + participle, as written) = у перерождающихся существ X", "",
          "## Answers", ""]
    ex = ["Ye purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ ghānindriyaṃ uppajjissati, no ca "
          "tesaṃ itthindriyaṃ uppajjissati.",
          "Yā itthiyo eteneva bhāvena katici bhave dassetvā parinibbāyissanti tāsaṃ tattha itthindriyaṃ uppajjissati, "
          "no ca tāsaṃ tattha purisindriyaṃ uppajjissati.",
          "Yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tesaṃ somanassindriyaṃ na "
          "uppajjissati, no ca tesaṃ jīvitindriyaṃ na uppajjissati.",
          "Pacchimabhavikānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ ghānindriyañca na uppajjissati "
          "cakkhundriyañca na uppajjissati.",
          "Pacchimacittasamaṅgīnaṃ tesaṃ upekkhindriyañca na uppajjissati manindriyañca na uppajjissati."]
    L += [f"{p} = {tl(p)}" for p in ex]
    L += ["", "## Slips (as written / as meant)", "",
          "^6-10-240 Yassa vā pana purisindriyaṃ uppajjittha tattha cakkhundriyaṃ uppajjitthāti? = "
          + FIXED_S["Yassa vā pana purisindriyaṃ uppajjittha tattha cakkhundriyaṃ uppajjitthāti?"][0]
          + " (yassa … tattha, as written)",
          "^6-10-301 Itaresaṃ kāmāvacarānaṃ tesaṃ tattha itthindriyañca uppajjissati. Somanassindriyañca uppajjissati. = "
          + FIXED_S["Itaresaṃ kāmāvacarānaṃ tesaṃ tattha itthindriyañca uppajjissati."][0] + " "
          + FIXED_S["Somanassindriyañca uppajjissati."][0] + " (full stop as written)",
          "^6-10-309 no ca tesaṃ somanassindriyaṃ na upapajjissati = но у них переродится способность радости (as written; G3)",
          "^6-10-314 Pacchimacittasamaṅgīna = у обладающих последним умом (as meant)",
          "^6-10-318 «na uppajjissati no ca tattha» = «…, но там …» (missing comma, as meant)",
          "^6-10-336 (Ghānandriyamūlakaṃ) = (На основе способности носа) (as meant)",
          "^6-10-361 asaññasattā cavantāna = у тех, кто умирает среди существ без восприятия (as meant)"]
    return "\n".join(L) + "\n"


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        for ch in sys.argv[2:]:
            probe(ch)
        return
    problems = []
    for ch in CHAPTERS:
        pt = (PALI / ch).read_text(encoding="utf-8")
        ru, pr = render(pt)
        problems += pr
        e, n = S.check_file(pt, ru)
        problems += [f"{ch}: {x}" for x in e]
        (OUT / ch).write_text(ru, encoding="utf-8", newline="\n")
        print(f"wrote {ch}: {n} segments")
    slips = list(SLIPS) + list(G10a.SLIPS) + list(G2.SLIPS) + list(G45.SLIPS) + list(getattr(G3, "SLIPS", []))
    (S.RAILS / "notes-rails-G10b1.md").write_text(notes_md(), encoding="utf-8", newline="\n")
    print("wrote notes-rails-G10b1.md")
    for sid, note in dict.fromkeys(slips):
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
