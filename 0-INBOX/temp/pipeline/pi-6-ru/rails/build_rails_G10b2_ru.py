"""pi-6 Yamaka, G10b2 (Indriyayamaka 10-09 … 10-13): Russian RAILS builder.

10-09 … 10-12: the mixed-tense pavatti sections (paccuppannānāgata, atītānāgata); 10-13: the pariññāvāra, which
ends the whole book («Yamakapakaraṇaṃ niṭṭhitaṃ.» = «Парные вопросы завершены.»).

Built on G10a (faculties, persons «с глазом / женщиной …», moments; build_rails_G10a_ru.py), which stands on the
frame-setters G2 (paṇṇatti / pavatti / pariññā frames, mixed tenses) and G8 (moments), and on G3 (sa-/a-X-ka
persons, -āvacara planes, «ye … upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ / cavantānaṃ», editorial
notes), G45 (intro_ru, pajahati «устраняет / устранил / устранит», pj_question) and G9 (bhāveti «развивает»).
G9 is imported first (it resets G45.UNITS; G10a then re-installs its units). The intro shapes G10b1 (10-05 …
10-08) set at the same time are copied verbatim (SAME_STATE, ATTR_NOM, «у тех, у кого сразу после данного ума
возникнет последний ум, связанный с X,», ATTR + plane persons) so the two groups agree.
Importing this module writes nothing:
    import sys, importlib
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru\\rails")
    G10b2 = importlib.import_module("build_rails_G10b2_ru")
    G10b2.translate_line(pali_line)
Exposes: UNITS_G10b2 (intro units, prepended to G45.UNITS on import), distribute() (a participle «tesaṃ
upapajjantānaṃ» after a run of «ye … parinibbāyissanti» groups goes to each group), PR_VERBS / pr_verb() (the four
pariññā verbs in every tense, number and gender), PR_PERSONS, pr_answer(), translate_line(), render().
Run: python -I -X utf8 -B build_rails_G10b2_ru.py              (writes 10-09 … 10-13 + notes-rails-G10b2.md)
     python -I -X utf8 -B build_rails_G10b2_ru.py --probe <ch>  (sentences without a formula; writes nothing)
     python -I -X utf8 -B build_rails_G10b2_ru.py --regress     (G10a's chapters re-rendered here must be unchanged)

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
"""
import importlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_sample_ru as S  # noqa: E402

G9 = importlib.import_module("build_rails_G9_ru")       # first: it resets G45.UNITS, G10a re-installs its units
G10a = importlib.import_module("build_rails_G10a_ru")
G2, G3, G45, G8 = G10a.G2, G10a.G3, G10a.G45, G10a.G8

ROOT, PALI, OUT = S.ROOT, S.PALI, S.OUT
CHAPTERS = [f"10-{i:02d}-indriyayamaka.md" for i in range(9, 14)]
cap, low1 = S.cap, G10a.low1
TERMS = G2.TERMS
_CUR = G2._CUR
SLIPS = []


def slip(note):
    SLIPS.append((_CUR["id"], note))


# =========================================================================== person intros (G45 units)
# --- copied verbatim from G10b1 (10-05 … 10-08, same Pāli; coordinator shape for eteneva bhāvena …)
SAME_STATE = "пройдя в этом же состоянии несколько существований"   # eteneva bhāvena katici bhave dassetvā
WHO_PL = {"purisā": "мужчин", "itthiyo": "женщин"}                    # termbase purisā «мужчины», itthiyo «женщины»
PARINIB_FUT_PL = "достигнут окончательного угасания"                  # parinibbāyissanti, plural after «которые»
ATTR_NOM = {  # nominative attributes before «upapajjitvā» (termbase sacakkhukā «с глазом»; saghānakā as G3)
    "sacakkhukā": "с глазом", "saghānakā": "с носом",
    "somanassena": "с радостью", "upekkhāya": "с невозмутимостью",
}
ANANTARA = "сразу после данного ума"     # yassa cittassa anantarā (G6; termbase anantarā «сразу после»)
LAST_MIND = "последний ум"               # pacchimacittaṃ (termbase)
LAST_MIND_Q = {  # X-sampayuttapacchimacittaṃ (termbase «последний ум связанный с X»; G45 comma punctuation)
    "upekkhāsampayuttapacchimacittaṃ": f"{LAST_MIND}, связанный с невозмутимостью",
    "somanassasampayuttapacchimacittaṃ": f"{LAST_MIND}, связанный с радостью",
}
# --- new here
PART = {  # «tesaṃ upapajjantānaṃ / cavantānaṃ» after a ye-group: «у тех перерождающихся / умирающих …» (G3, G45)
    "upapajjantānaṃ": G45.WHO_PART["upapajjantānaṃ"], "upapajjantīnaṃ": G45.WHO_PART["upapajjantānaṃ"],
    "cavantānaṃ": G45.WHO_PART["cavantānaṃ"], "cavantīnaṃ": G45.WHO_PART["cavantānaṃ"],
}
_PART = "(?:tesaṃ|tāsaṃ) (?P<w>upapajjantānaṃ|upapajjantīnaṃ|cavantānaṃ|cavantīnaṃ)"
# moments and persons of the last mind (termbase: Somanassasampayuttapacchimacittassa uppādakkhaṇe «момент
# возникновения последнего ума связанного с радостью»; upekkhāsampayuttapacchimacittasamaṅgīnaṃ «обладающий
# последним умом связанным с невозмутимостью»; G45 commas around the participle phrase)
MOM_G10b2 = {
    "somanassasampayuttapacchimacittassa": (f"последнего ума, связанного с радостью", True),
    "upekkhāsampayuttapacchimacittassa": (f"последнего ума, связанного с невозмутимостью", True),
}
LAST_MIND_HOLDERS = {
    "somanassasampayuttapacchimacittasamaṅgīnaṃ": "у обладающих последним умом, связанным с радостью",
    "upekkhāsampayuttapacchimacittasamaṅgīnaṃ": "у обладающих последним умом, связанным с невозмутимостью",
}


def _attr_nom(s):
    return " и ".join(ATTR_NOM[w] for w in s.split())


def _abs_phrase(a, p):
    """«переродившись с глазом и с невозмутимостью в мире форм» (G10b1: attributes in the Pāli order, then planes)."""
    r = G2.REBORN_ABS
    if a and a.strip():
        r += " " + _attr_nom(a.strip())
    if p and p.strip():
        r += " " + G2._places(p.strip(), G2.PL_ACC)
    return r


def _check_rel(m):
    if m.group("rel") == "yā" and m.group("who") != "itthiyo" or m.group("rel") == "ye" and m.group("who") != "purisā":
        slip("ye / yā does not agree with purisā / itthiyo; kept as written")


def _who_noun(m):
    """«у тех (перерождающихся) мужчин» (G45 «у тех перерождающихся обычных людей, которые …»)."""
    part = f"{PART[m.group('w')]} " if m.group("w") else ""
    return f"у тех {part}{WHO_PL[m.group('who')]}"


def _same_state(m):
    """ye ca purisā eteneva bhāvena katici bhave dassetvā (ATTR upapajjitvā) parinibbāyissanti (tesaṃ PART)."""
    _check_rel(m)
    a = m.group("a")
    mid = f"{SAME_STATE}, " + (f"{_abs_phrase(a, '')}, " if a else "")
    return f"{_who_noun(m)}, которые, {mid}{PARINIB_FUT_PL}", True


def _who_abs(m):
    """ye ca purisā / yā ca itthiyo ATTR… PLANE… upapajjitvā parinibbāyissanti (tesaṃ PART)."""
    _check_rel(m)
    return f"{_who_noun(m)}, которые, {_abs_phrase(m.group('a'), m.group('p'))}, {PARINIB_FUT_PL}", True


def _ye_abs(m):
    """ye ca ATTR… PLANE… upapajjitvā parinibbāyissanti (tesaṃ PART): G3 «у тех перерождающихся, кто, …»."""
    who = f"у тех {PART[m.group('w')]}" if m.group("w") else "у тех"
    return f"{who}, кто, {_abs_phrase(m.group('a'), m.group('p'))}, {G2.PARINIB_FUT}", True


def _attr_place(m):
    """ATTR… PLANE… upapajjantānaṃ / cavantānaṃ (G10b1)."""
    who = "у остальных, кто" if m.group("pre") else "у тех, кто"
    verb = G2.REBORN if m.group("w") == "upapajjantānaṃ" else G2.DIES
    table = G2.PL_ACC if m.group("w") == "upapajjantānaṃ" else G2.PL_ABL
    return f"{who} {verb} {G10a.attrs_ru(m.group('a').strip())} {G2._places(m.group('p').strip(), table)}", True


def _units():
    A, B, G = G2._alt(G2.PL_ACC), G2._alt(G2.PL_ABL), G2._alt(G2.BEINGS)
    AN, AT = G2._alt(ATTR_NOM), G10a._AT
    return [
        (rf"(?P<rel>ye|yā) (?:ca )?(?P<who>purisā|itthiyo) eteneva bhāvena katici bhave dassetvā "
         rf"(?:(?P<a>(?:{AN} ?)+) upapajjitvā )?parinibbāyissanti(?: {_PART})?", "P", _same_state),
        (rf"(?P<rel>ye|yā) (?:ca )?(?P<who>purisā|itthiyo) (?P<a>(?:{AN} )*)(?P<p>(?:{A} )*)upapajjitvā "
         rf"parinibbāyissanti(?: {_PART})?", "P", _who_abs),
        (rf"ye (?:ca )?(?P<a>(?:{AN} )*)(?P<p>(?:{A} )*)upapajjitvā parinibbāyissanti(?: {_PART})?", "P", _ye_abs),
        (rf"yassa cittassa anantarā (?P<q>{G2._alt(LAST_MIND_Q)}) uppajjissati", "P",
         lambda m: (f"у тех, у кого {ANANTARA} возникнет {LAST_MIND_Q[m.group('q')]}", True)),
        (rf"(?P<h>{G2._alt(LAST_MIND_HOLDERS)})", "P", lambda m: (LAST_MIND_HOLDERS[m.group("h")], True)),
        (rf"(?P<pre>itaresaṃ )?(?P<a>(?:{AT} )+)(?P<p>(?:{A} )+)(?P<w>upapajjantānaṃ)", "P", _attr_place),
        (rf"(?P<pre>itaresaṃ )?(?P<a>(?:{AT} )+)(?P<p>(?:{B} )+)(?P<w>cavantānaṃ)", "P", _attr_place),
        (rf"({G}) upapajjantānaṃ", "P", lambda m: (f"у {G45.WHO_PART['upapajjantānaṃ']} {G2.BEINGS[m.group(1)]}", False)),
        (rf"pacchimabhavikānaṃ (?P<a>(?:{AT} )+)uppajjantānaṃ", "P", _last_arising),
    ]


def _last_arising(m):
    """^6-10-398 «Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ»: uppajjantānaṃ (termbase «возникать») for
    upapajjantānaṃ, a one-letter slip that makes another word: kept as written («кто в последний раз возникает
    мужчиной»; G10a ^6-10-206 uppajjantīnaṃ «кто возникает»)."""
    slip("uppajjantānaṃ for upapajjantānaṃ: a one-letter slip that makes another word; kept as written "
         "(«кто в последний раз возникает мужчиной»)")
    return f"у тех, кто в последний раз {G10a.WHO_VERB['uppajjantīnaṃ']} {G10a.attrs_ru(m.group('a').strip())}", True


UNITS_G10b2 = None


def install_units():
    """Prepend the G10b2 units to G45.UNITS (before G10a's), add the last-mind moments, and append G2's person
    groups (with G3's) as a fallback (as G10b1)."""
    global UNITS_G10b2
    G45.MOM_GEN.update(MOM_G10b2)
    G45._MG = "(?P<g>" + "|".join(sorted(map(re.escape, G45.MOM_GEN), key=len, reverse=True)) + ")"
    G45.UNITS = None
    G45.units("")
    G45.UNITS[:0] = G10a.UNITS_G10a
    UNITS_G10b2 = _units()
    G45.UNITS[:0] = UNITS_G10b2
    G2.GROUP_RULES = None                    # G6 (imported by G9) reset it: rebuild with G3's shapes first, as G3 does
    G2.intro_groups("")
    G2.GROUP_RULES[:0] = G3._g3_rules()
    G45.UNITS += [(rx, "P", fn) for rx, fn in G2.GROUP_RULES]


install_units()


def distribute(s):
    """«ye … parinibbāyissanti ye ca … parinibbāyissanti tesaṃ upapajjantānaṃ»: the participle of the last group
    goes to every ye-group of the run («у тех перерождающихся, кто, …, и у тех перерождающихся мужчин, которые, …»)."""
    out, pos = [], 0
    for m in re.finditer(r"parinibbāyissanti ((?:tesaṃ|tāsaṃ) (?:upapajjantānaṃ|upapajjantīnaṃ|cavantānaṃ|cavantīnaṃ))"
                         r"(?= |$)", s):
        head = s[pos:m.start()]
        head = re.sub(r"parinibbāyissanti (?=(?:ye|yā) )", f"parinibbāyissanti {m.group(1)} ", head)
        out.append(head)
        out.append(m.group(0))
        pos = m.end()
    out.append(s[pos:])
    r = "".join(out)
    if r != s:
        slip("«tesaṃ upapajjantānaṃ / cavantānaṃ» after a run of «ye … parinibbāyissanti» groups: the participle is "
             "rendered with each group («у тех перерождающихся …»)")
    return r


# =========================================================================== pariññā (10-13)
# termbase: parijānāti «полностью понимать», parijānittha / parijānissati «полностью понять» (G2 / G45; negative «не
# понимает полностью»); pajahati «устранять», pajahittha / pajahissati «устранить» (G45); bhāveti «развивать» (G9),
# bhāvittha / bhāvessati «развить»; sacchikaroti «осуществлять», sacchikarittha / sacchākāsi / sacchikarissati
# «осуществить». Past = perfective (G45 «устранил», G2 «полностью понял»), by the subject's gender.
_NEW_PJ = {
    "parijānanti": G45.PJ["parijānāti"][:4] + ("pl",),
    "parijānissanti": G45.PJ["parijānissati"][:4] + ("pl",),
    "pajahanti": G45.PJ["pajahati"][:4] + ("pl",),
    "bhāventi": G45.PJ["bhāveti"][:4] + ("pl",),
    "bhāvittha": ("развил", "развили", "не развил", "не развили", "any"),
    "bhāvessati": ("разовьёт", "разовьют", "не разовьёт", "не разовьют", "sg"),
    "bhāvessanti": ("разовьёт", "разовьют", "не разовьёт", "не разовьют", "pl"),
    "sacchikaroti": ("осуществляет", "осуществляют", "не осуществляет", "не осуществляют", "sg"),
    "sacchikaronti": ("осуществляет", "осуществляют", "не осуществляет", "не осуществляют", "pl"),
    "sacchikarittha": ("осуществил", "осуществили", "не осуществил", "не осуществили", "any"),
    "sacchikarissati": ("осуществит", "осуществят", "не осуществит", "не осуществят", "sg"),
    "sacchikarissanti": ("осуществит", "осуществят", "не осуществит", "не осуществят", "pl"),
}
for _k, _v in _NEW_PJ.items():
    G45.PJ.setdefault(_k, _v)
PR_VERBS = G45.PJ
PAST_ANY = {"parijānittha", "pajahittha", "bhāvittha", "sacchikarittha"}   # -ittha: both numbers in the Yamaka
VERB_SLIP = {"nappajjahittha": ("nappajahittha", "nappajjahittha for nappajahittha: spelling slip, rendered as meant "
                                                 "(termbase entry nappajahittha)")}


def pr_parse(s):
    for a, (b, note) in VERB_SLIP.items():
        if s == a:
            slip(note)
            s = b
    return G45.pjparse(s)


def pr_verb(v, n, g):
    """(base, neg), number, gender -> Russian; a feminine singular past takes «-ла» («поняла», «развила»)."""
    r = G45.pjru(v, n)
    if n == "sg" and g == "f" and v[0] in PAST_ANY:
        r = re.sub(r"(\w+л)\b", r"\1а", r)
    return r


NUM_PERSONS = {  # numeral + puggalā (G7: «Две / Три / Четыре личности»; termbase puggalā «личности»)
    "dve": "Две личности", "tayo": "Три личности", "cattāro": "Четыре личности", "pañca": "Пять личностей",
    "cha": "Шесть личностей", "satta": "Семь личностей", "aṭṭha": "Восемь личностей",
}
EXC = {  # «X ṭhapetvā avasesā puggalā» = «Кроме X, остальные личности» (G2 / G7; termbase maggasamaṅgino
    #      «обладающий путём», Anāgāmimaggasamaṅgiñca «обладающий путём невозвращения», aṭṭhamakañca «личность
    #      восьмой ступени», arahantañca «архат»)
    "dve maggasamaṅgino": "двух обладающих путём",
    "tayo maggasamaṅgino": "трёх обладающих путём",
    "cattāro maggasamaṅgino": "четырёх обладающих путём",
    "tayo maggasamaṅgino ca arahantañca": "трёх обладающих путём и архата",
    "anāgāmimaggasamaṅgiñca arahantañca": "обладающего путём невозвращения и архата",
    "aṭṭhamakañca arahantañca": "личности восьмой ступени и архата",
    "aggamaggasamaṅgiñca arahantañca": "обладающего высшим путём и архата",
}
PR_PERSONS = {  # lower-case Pāli -> (Russian, number, gender)
    "arahā": (G2.PERSONS["arahā"][0], "sg", "m"),                                  # «Архат»
    "aggamaggasamaṅgī": (G2.PERSONS["aggamaggasamaṅgī"][0], "sg", "m"),            # «Обладающий высшим путём»
    "anāgāmimaggasamaṅgī": ("Обладающий путём невозвращения", "sg", "m"),         # G7 (termbase)
    "aṭṭhamako": ("Личность восьмой ступени", "sg", "f"),                         # G7 (termbase Aṭṭhamako)
    "anāgāmī": ("Невозвращающийся", "sg", "m"),                                   # G7
    "tayo maggasamaṅgino": ("Три обладающих путём", "pl", "pl"),                  # termbase maggasamaṅgino
    "yo aggaphalaṃ sacchikaroti so": ("Тот, кто осуществляет высший плод,", "sg", "m"),   # aggaphalaṃ «высший плод»
    "yo aggaphalaṃ sacchākāsi so": ("Тот, кто осуществил высший плод,", "sg", "m"),       # sacchākāsi «осуществить»
    "ye puthujjanā maggaṃ paṭilabhissanti te": ("Те обычные люди, которые обретут путь,", "pl", "pl"),   # G2
    "ye puthujjanā maggaṃ na paṭilabhissanti te": ("Те обычные люди, которые не обретут путь,", "pl", "pl"),
}
for _k, _v in NUM_PERSONS.items():
    PR_PERSONS[f"{_k} puggalā"] = (_v, "pl", "pl")
for _k, _v in EXC.items():
    PR_PERSONS[f"{_k} ṭhapetvā avasesā puggalā"] = (f"{G2.EXCEPT} {_v}, остальные личности", "pl", "pl")


def _num_check(v, n):
    pn = G45.PJ[v[0]][4]
    if v[0] not in PAST_ANY and pn != "any" and pn != n:
        slip(f"{v[0]}: Pāli verb number differs from the subject's; Russian agreement")


def pr_answer(s):
    """P X V1, no ca Y V2. = «P V1 X, но V2' Y.» (a denied negative said plainly); P Xñca V1 Yñca V2. = «P и V1 X,
    и V2 Y.»; the same negated verb twice: «P не V ни X, ни Y.» (G2 / G45 frames, with the subject's gender)."""
    body = s[:-1]
    for pk in sorted(PR_PERSONS, key=len, reverse=True):
        if body.lower().startswith(pk + " "):
            ru, n, g = PR_PERSONS[pk]
            rest = G45.norm(body[len(pk) + 1:])
            break
    else:
        return None
    m = re.match(r"^(?P<x>\S+) (?P<v1>(?:na )?\S+), no ca (?P<y>\S+) (?P<v2>(?:na )?\S+)$", rest)
    if m:
        x, y = G45.term(m.group("x")), G45.term(m.group("y"))
        v1, v2 = pr_parse(m.group("v1")), pr_parse(m.group("v2"))
        if x and y and v1 and v2:
            _num_check(v1, n)
            _num_check(v2, n)
            return (f"{ru} {pr_verb(v1, n, g)} {TERMS[x]['acc']}, но {pr_verb((v2[0], not v2[1]), n, g)} "
                    f"{TERMS[y]['acc']}.")
    m = re.match(r"^(?P<x>\S+) ca (?P<v1>(?:na )?\S+) (?P<y>\S+) ca (?P<v2>(?:na )?\S+)$", rest)
    if m:
        x, y = G45.term(m.group("x")), G45.term(m.group("y"))
        v1, v2 = pr_parse(m.group("v1")), pr_parse(m.group("v2"))
        if x and y and v1 and v2:
            _num_check(v1, n)
            _num_check(v2, n)
            if v1 == v2 and v1[1]:
                return f"{ru} {pr_verb(v1, n, g)} ни {TERMS[x]['acc']}, ни {TERMS[y]['acc']}."
            return f"{ru} и {pr_verb(v1, n, g)} {TERMS[x]['acc']}, и {pr_verb(v2, n, g)} {TERMS[y]['acc']}."
    return None


def pr_question(s):
    """(Ka) yo X V1 so Y V2? = «(а) Кто V1 X, тот V2 Y?» (G45.pj_question; «.» at the end kept as written)."""
    if not re.match(r"^\((?:Ka|Kha)\) yo ", s):
        return None
    for a, (b, note) in VERB_SLIP.items():
        if re.search(rf"(?<!\S){a}(?!\S)", s):
            slip(note)
            s = s.replace(a, b)
    r = G45.pj_question(s)
    if r and s.endswith("."):
        slip("question ends with «.»; kept as written")
    return r


# =========================================================================== fixed sentences, slips
SAME = "(Так же)"   # (Sadisaṃ ) after an abbreviated question: «the same» (G3 sadisaṃ «одинаков / такой же»)
BOOK_DONE = f"{S.BOOK} {S.DONE_PL}."   # Yamakapakaraṇaṃ niṭṭhitaṃ. = «Парные вопросы завершены.» (sample pattern)


def _bhavissanti():
    """^6-10-452: «…, pañca puggalā aññindriyañca bhavissanti domanassindriyañca pajahissanti.» bhavissanti «будут»
    (for bhāvessanti: a one-letter slip that makes another word, kept as written; the comma before «pañca» as
    written)."""
    a = pr_answer("Dve puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahissanti.")[:-1]
    x, y = TERMS["aññindriyaṃ"], TERMS["domanassindriyaṃ"]
    b = (f"{low1(NUM_PERSONS['pañca'])} и будут {x['ins']}, и {pr_verb(('pajahissanti', False), 'pl', 'pl')} "
         f"{y['acc']}.")
    return f"{a}, {b}"


def _fixed_s():
    q = G45.pj_question
    return {  # exact Pāli sentence -> (Russian, slip note or None)
        "(Sadisaṃ )": (SAME, None),
        "Indriyayamakaṃ niṭṭhitaṃ.": (S.yamaka_done("Indriyayamakaṃ"), None),
        "Yamakapakaraṇaṃ niṭṭhitaṃ.": (BOOK_DONE, None),
        # ^6-10-472: a full stop splits the question; kept as written (two sentences)
        "(Kha) yo vā pana aññindriyaṃ bhāvessati.":
            (q("(Kha) yo vā pana aññindriyaṃ bhāvessati so aññindriyaṃ bhāvessatīti?").split(", тот ")[0] + ".",
             "a full stop inside the question «… bhāvessati. So … bhāvitthāti?»; kept as written (two sentences)"),
        "So anaññātaññassāmītindriyaṃ bhāvitthāti?":
            ("Тот " + q("(Ka) yo aññindriyaṃ bhāveti so anaññātaññassāmītindriyaṃ bhāvitthāti?").split(", тот ")[1],
             None),
        "Dve puggalā aññindriyaṃ bhāvessanti, no ca domanassindriyaṃ pajahissanti, pañca puggalā aññindriyañca "
        "bhavissanti domanassindriyañca pajahissanti.":
            (_bhavissanti(), "«aññindriyañca bhavissanti» (bhāvessanti expected): a one-letter slip that makes another "
                             "word, kept as written («и будут способностью окончательного знания»); the comma before "
                             "«pañca puggalā» (a full stop expected) kept as written"),
        # ^6-10-369: a stray comma before «tassa»; the Russian question has a comma there anyway
        "(Kha) yassa vā pana somanassindriyaṃ uppajjissati, tassa purisindriyaṃ uppajjatīti?":
            (G2.pv_question_line("(Kha) yassa vā pana somanassindriyaṃ uppajjissati tassa purisindriyaṃ "
                                 "uppajjatīti?"),
             "stray comma before «tassa» in the question; the Russian has a comma there anyway"),
    }


FIXED_S = None
LINE_SLIPS = {  # Pāli as found -> (as meant, note): missing punctuation only
    "aññindriyaṃ bhāvessanti no ca": ("aññindriyaṃ bhāvessanti, no ca",
                                      "missing comma before «no ca»; rendered as meant"),
    "itthindriyaṃ na uppajjati no ca": ("itthindriyaṃ na uppajjati, no ca",
                                        "missing comma before «no ca»; rendered as meant"),
    "manindriyaṃ na uppajjissati pacchimacittassa": ("manindriyaṃ na uppajjissati. Pacchimacittassa",
                                                     "missing full stop before «pacchimacittassa bhaṅgakkhaṇe» (a new "
                                                     "answer sentence); rendered as meant"),
    # ^6-10-468: missing full stop before the second answer (as meant); anāgāmimaggasamaṅgi = the termbase's short
    # stem form (as meant, «обладающий путём невозвращения»); the comma after «bhāvessanti» is a stray comma (the
    # Russian «и …, и …» has one there anyway)
    "domanassindriyaṃ pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti.":
        ("domanassindriyaṃ pajahanti. Anāgāmimaggasamaṅgī aññindriyañca bhāvessanti domanassindriyañca pajahanti.",
         "missing full stop before «anāgāmimaggasamaṅgi» (as meant); -samaṅgi for -samaṅgī (termbase short stem, as "
         "meant); stray comma after «bhāvessanti» (the Russian «и …, и …» has one anyway)"),
}
_PL_VERB = re.compile(r"(\S+indriyaṃ) (?:na )?((?:uppajj|nirujjh)\w*anti)\b")


def core(s):
    """One Pāli sentence -> Russian or None (G10b2 first, then G10a's core with the participle distributed)."""
    global FIXED_S
    if FIXED_S is None:
        FIXED_S = {}
        FIXED_S = _fixed_s()
    if s in FIXED_S:
        ru, note = FIXED_S[s]
        if note:
            slip(note)
        return ru
    for fn in (pr_question, pr_answer):
        r = fn(s)
        if r:
            return r
    if "parinibbāyissanti" in s:
        s = distribute(s)
    return _core0(s)


_core0 = G10a.core
G10a.core = core   # G10a.translate_sentence / fragment look «core» up in their module (in memory only, as G10b1)

BRACKET = re.compile(r" \[([^\]]+?) \(([^)]+)\)\]")
BR_ANCHOR = {  # the Pāli word before a variant bracket -> its Russian (the bracket follows it)
    "maggasamaṅgino": "обладающих путём", "aṭṭha": "Восемь", "cha": "Шесть",
}


def brackets(pali):
    """Variant brackets «[tayo puggalā (pī.)]»: translated without them, then each «[вариант чтения (Pī.): …]» goes
    after the Russian of the word before it, in order."""
    found = []
    for m in BRACKET.finditer(pali):
        prev = pali[:m.start()].split()[-1].lower()
        found.append((prev, m.group(1), m.group(2)))
    ru = translate_line(BRACKET.sub("", pali))
    pos = 0
    for prev, text, sig in found:
        anchor = BR_ANCHOR[prev]
        i = ru.find(anchor, pos)
        assert i >= 0, (anchor, ru)
        j = i + len(anchor)
        br = G2.var_br(text, sig)
        ru = ru[:j] + " " + br + ru[j:]
        pos = j + len(br) + 1
    return ru


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian."""
    global FIXED_S
    if FIXED_S is None:
        FIXED_S = {}
        FIXED_S = _fixed_s()
    if "[" in pali:
        return brackets(pali)
    for a, (b, note) in LINE_SLIPS.items():
        if a in pali:
            slip(note)
            pali = pali.replace(a, b)
    for m in _PL_VERB.finditer(pali):
        slip(f"«{m.group(1)} … {m.group(2)}»: plural verb with a singular subject; Russian agreement")
    if re.search(r"\(Sadisaṃ \)", pali):
        slip("«(Sadisaṃ )»: the space before «)» is the source's; not rendered")
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


def probe(ch, limit=400):
    bad, seen = 0, set()
    for sid, plines in S.segs((PALI / ch).read_text(encoding="utf-8")):
        _CUR["id"] = G45._CUR["id"] = sid
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            try:
                translate_line(body)
            except (ValueError, KeyError, AssertionError, TypeError) as e:
                bad += 1
                key = re.sub(r"\w+indriy\w*", "F", str(e))
                if key not in seen and len(seen) < limit:
                    print(sid, "|", str(e)[:400])
                seen.add(key)
    print(ch, "lines without a formula:", bad, "distinct:", len(seen))


def regress():
    """G10a's chapters re-rendered under this module's imports must equal the files G10a wrote."""
    bad = 0
    for ch in G10a.CHAPTERS:
        ru, _ = G10a.render((PALI / ch).read_text(encoding="utf-8"))
        old = (OUT / ch).read_text(encoding="utf-8")
        if ru != old:
            bad += 1
            for i, (a, b) in enumerate(zip(ru.splitlines(), old.splitlines())):
                if a != b:
                    print(ch, i + 1, "\n  NEW", a[:300], "\n  OLD", b[:300])
                    break
    print("regression:", "OK" if not bad else f"{bad} chapter(s) differ")
    return bad


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--regress":
        sys.exit(1 if regress() else 0)
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
    slips = list(SLIPS) + list(G10a.SLIPS) + list(G2.SLIPS) + list(G45.SLIPS)
    (S.RAILS / "notes-rails-G10b2.md").write_text(notes_md(), encoding="utf-8", newline="\n")
    print("wrote notes-rails-G10b2.md")
    for sid, note in dict.fromkeys(slips):
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


def notes_md():
    tl = translate_line
    L = ["# notes-rails-G10b2: Indriyayamaka (10-09 … 10-13) frames", "",
         "Format: Pāli = Russian, one per line. Builder: build_rails_G10b2_ru.py (importlib.import_module(",
         "\"build_rails_G10b2_ru\"); importing writes nothing). Everything else is G10a / G2 / G8 / G3 / G45 / G9 verbatim",
         "(see notes-rails-G10a.md); the eteneva bhāvena / ATTR_NOM / last-mind / ATTR + plane shapes are G10b1's strings,",
         "copied so both groups agree. Import order: G9 first (it resets G45.UNITS; G6 via G9 resets G2.GROUP_RULES, which",
         "install_units() rebuilds with G3's shapes); `--regress` re-renders 10-01 … 10-04 and must report OK.", "",
         "## Person intros (mixed tenses)", ""]
    ex = ["Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
          "upapajjantānaṃ",
          "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca rūpāvacaraṃ arūpāvacaraṃ upapajjitvā "
          "parinibbāyissanti ye ca purisā eteneva bhāvena katici bhave dassetvā parinibbāyissanti tesaṃ upapajjantānaṃ",
          "Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca sacakkhukā upekkhāya upapajjitvā parinibbāyissanti "
          "tesaṃ upapajjantānaṃ",
          "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ yā ca itthiyo upekkhāya upapajjitvā parinibbāyissanti tesaṃ "
          "upapajjantīnaṃ",
          "Pacchimabhavikānaṃ purisānaṃ upapajjantānaṃ ye ca purisā somanassena upapajjitvā parinibbāyissanti tesaṃ "
          "upapajjantānaṃ",
          "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ ye ca upekkhāya upapajjitvā parinibbāyissanti tesaṃ "
          "cavantānaṃ",
          "Kāmāvacare parinibbantānaṃ rūpāvacare arūpāvacare pacchimabhavikānaṃ asaññasattānaṃ yā ca itthiyo "
          "somanassena upapajjitvā parinibbāyissanti tesaṃ cavantīnaṃ",
          "Pacchimabhavikānaṃ kāmāvacaraṃ upapajjantānaṃ rūpāvacaraṃ upapajjantānaṃ",
          "Pacchimacittassa uppādakkhaṇe yassa cittassa anantarā upekkhāsampayuttapacchimacittaṃ uppajjissati tassa "
          "cittassa uppādakkhaṇe",
          "Somanassasampayuttapacchimacittassa uppādakkhaṇe",
          "Somanassasampayuttapacchimacittassa bhaṅgakkhaṇe upekkhāsampayuttapacchimacittasamaṅgīnaṃ yassa cittassa "
          "anantarā somanassasampayuttapacchimacittaṃ uppajjissati tassa cittassa bhaṅgakkhaṇe"]
    L += [f"{p} tesaṃ = {G45.intro_ru(distribute(p.lower()))}" for p in ex]
    L += ["ye (ca) ATTR… PLANE… upapajjitvā parinibbāyissanti tesaṃ upapajjantānaṃ / cavantānaṃ = у тех "
          "перерождающихся / умирающих, кто, переродившись …, достигнет окончательного угасания (G3 shape + G10b1 ATTR_NOM)",
          "ye ca purisā / yā ca itthiyo (…) parinibbāyissanti tesaṃ upapajjantānaṃ / tāsaṃ cavantīnaṃ = у тех "
          "перерождающихся / умирающих мужчин / женщин, которые, …, достигнут окончательного угасания (G45 «у тех",
          "  перерождающихся обычных людей, которые …»)",
          "a participle after a run of ye-groups («ye … parinibbāyissanti ye ca … parinibbāyissanti tesaṃ "
          "upapajjantānaṃ») goes with each group (distribute())",
          "X-sampayuttapacchimacittassa = последнего ума, связанного с X, (moment; termbase)",
          "X-sampayuttapacchimacittasamaṅgīnaṃ = у обладающих последним умом, связанным с X, (termbase)",
          "pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ (^6-10-398, as written) = у тех, кто в последний раз возникает "
          "мужчиной", "",
          "## Pavatti answers", ""]
    ex = ["Pacchimabhavikānaṃ pañcavokāraṃ upapajjantānaṃ ye ca arūpaṃ upapajjitvā parinibbāyissanti tesaṃ "
          "upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ sotindriyaṃ uppajjissati.",
          "Itarāsaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ itthindriyañca uppajjati purisindriyañca uppajjissati.",
          "Pañcavokāre parinibbantānaṃ arūpe pacchimabhavikānaṃ tesaṃ cakkhundriyañca na uppajjati jīvitindriyañca na "
          "uppajjissati.",
          "Somanassasampayuttapacchimacittassa uppādakkhaṇe tesaṃ somanassindriyaṃ uppajjati, no ca tesaṃ "
          "manindriyaṃ uppajjissati.",
          "Yassa cakkhundriyaṃ uppajjati tassa purisindriyaṃ uppajjissatīti? (Sadisaṃ )"]
    L += [f"{p} = {tl(p)}" for p in ex]
    L += ["(Sadisaṃ ) = (Так же)  (sadisaṃ «the same»; no full stop in the Pāli)", "",
          "## Pariññā (10-13)", "",
          "verbs (termbase; G2 / G45 / G9 forms; past perfective by the subject's gender, «-ла» for «личность»):"]
    for k in ("parijānāti", "parijānittha", "parijānissati", "pajahati", "pajahittha", "pajahissati", "bhāveti",
              "bhāvittha", "bhāvessati", "sacchikaroti", "sacchikarittha", "sacchikarissati"):
        f = G45.PJ[k]
        L.append(f"  {k} = {f[0]} / {f[1]}; na {k} = {f[2]} / {f[3]}")
    L.append("  sacchākāsi = осуществил (in «Yo aggaphalaṃ sacchākāsi so»); -ittha serves both numbers (no slip)")
    L += ["persons:"]
    L += [f"  {k} = {v[0]}" for k, v in PR_PERSONS.items()]
    L.append("")
    ex = ["(Ka) yo cakkhundriyaṃ parijānāti so domanassindriyaṃ pajahatīti?",
          "(Kha) yo vā pana anaññātaññassāmītindriyaṃ bhāveti so cakkhundriyaṃ parijānātīti?",
          "(Ka) yo cakkhundriyaṃ parijānittha so aññātāvindriyaṃ sacchikaritthāti?",
          "(Ka) yo domanassindriyaṃ nappajahissati so aññātāvindriyaṃ na sacchikarissatīti?",
          "Dve puggalā aññindriyaṃ bhāventi, no ca cakkhundriyaṃ parijānanti.",
          "Aggamaggasamaṅgī aññindriyañca bhāveti cakkhundriyañca parijānāti.",
          "Dve maggasamaṅgino ṭhapetvā avasesā puggalā cakkhundriyañca na parijānanti domanassindriyañca nappajahanti.",
          "Yo aggaphalaṃ sacchikaroti so cakkhundriyaṃ na parijānāti, no ca aññātāvindriyaṃ na sacchikaroti.",
          "Aṭṭhamako aññindriyaṃ na bhāvittha, no ca anaññātaññassāmītindriyaṃ na bhāveti.",
          "Cattāro maggasamaṅgino ṭhapetvā avasesā puggalā aññindriyañca na bhāventi anaññātaññassāmītindriyañca na "
          "bhāventi.",
          "Ye puthujjanā maggaṃ paṭilabhissanti te cakkhundriyañca parijānissanti anaññātaññassāmītindriyañca "
          "bhāvessanti.",
          "Cha [pañca (sī. syā. ka.)] puggalā aññindriyañca na bhāventi aññātāvindriyañca na sacchikarittha.",
          "Pariññāvāro.", "Indriyayamakaṃ niṭṭhitaṃ.", "Yamakapakaraṇaṃ niṭṭhitaṃ."]
    L += [f"{p} = {tl(p)}" for p in ex]
    L += ["", "## Slips (as written / as meant)", "",
          "^6-10-369 «somanassindriyaṃ uppajjissati, tassa» = stray comma (the Russian question has one anyway)",
          "^6-10-376 «Sacakkhukānaṃ … manindriyaṃ uppajjissati cakkhundriyañca uppajjati» = one «ca» missing: «возникнет "
          "способность ума и возникает способность глаза» (as written, G2 rule)",
          "^6-10-385 «itthindriyaṃ na uppajjissanti» = не возникнет (plural verb, singular subject: Russian agreement)",
          "^6-10-387 / ^6-10-452 / ^6-10-477 missing comma before «no ca» (as meant)",
          "^6-10-393 missing full stop before «pacchimacittassa bhaṅgakkhaṇe» (as meant)",
          "^6-10-398 Pacchimabhavikānaṃ purisānaṃ uppajjantānaṃ = у тех, кто в последний раз возникает мужчиной "
          "(as written)",
          "^6-10-452 «…, pañca puggalā aññindriyañca bhavissanti …» = «…, пять личностей и будут способностью "
          "окончательного знания, и …» (bhavissanti and the comma as written)",
          "^6-10-454 / ^6-10-459 / ^6-10-468 plural verb with a singular subject (Russian agreement)",
          "^6-10-455 questions ending with «.» (as written)",
          "^6-10-468 «… pajahanti anāgāmimaggasamaṅgi aññindriyañca bhāvessanti, domanassindriyañca pajahanti.» = "
          "full stop added, -samaṅgī (as meant), stray comma (Russian «и …, и …»)",
          "^6-10-477 «(Kha) yo vā pana aññindriyaṃ bhāvessati. So …?» = «(б) А кто разовьёт способность окончательного "
          "знания. Тот развил …?» (full stop as written)",
          "^6-10-480 nappajjahittha = не устранил (as meant, nappajahittha)"]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
