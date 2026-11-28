"""pi-6 Yamaka, G10a (Indriyayamaka 10-01 … 10-04): Russian RAILS builder.

Built on the frame-setters G2 (paṇṇatti / pavatti frames) and G8 (moment phrases), and on the finished groups
G3 (sa-/a-X-ka persons «с глазом / без глаза», mūlaka labels, abbreviated «…pe…» questions, place lists) and
G45 (intro_ru(): person / time / place intros with «в течение жизни в момент …»; paṇṇatti answers with
«остальное»). Importing this module writes nothing:
    import sys, importlib
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru\\rails")
    G10a = importlib.import_module("build_rails_G10a_ru")
    G10a.translate_line(pali_line)
Exposes for G10b (10-05 … 10-13):
    FACULTIES   the 22 faculties (Pāli key, bare-word key, Russian nominative; pi-2 Indriyavibhaṅga = termbase)
    faculty_cases(nom) -> (nom, gen, ins, acc);  BARE (bare words: глаз, женщина, радость …)
    ATTR / GENDER  person attributes («с глазом», «без радости», «со знанием», «женщиной», «не мужчиной» …)
    attrs_ru("sacakkhukānaṃ na itthīnaṃ") -> «не женщиной, с глазом»;  person_unit(...) / UNITS_G10a (intro units,
    prepended to G45.UNITS), MOM_G10a (moments «ума, связанного с радостью и не связанного с верой,»)
    core(sentence), translate_sentence(sentence), translate_line(line), render(text)
Run as a script (python -I -X utf8 -B build_rails_G10a_ru.py) to write 10-01 … 10-04 + notes-rails-G10a.md and
run the per-line checks; `--probe <ch> …` prints the sentences without a formula (writes nothing).

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
"""
import importlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_sample_ru as S  # noqa: E402

G2 = importlib.import_module("build_rails_G2_ru")
G8 = importlib.import_module("build_rails_G8_ru")     # moment phrases (via G45, which takes G8's wording)
G3 = importlib.import_module("build_rails_G3_ru")     # import before G45: G45 copies G2's plane tables
G45 = importlib.import_module("build_rails_G45_ru")

ROOT, PALI, OUT = S.ROOT, S.PALI, S.OUT
CHAPTERS = [f"10-0{i}-indriyayamaka.md" for i in range(1, 5)]
cap = S.cap
TERMS = G2.TERMS
_CUR = G2._CUR
SLIPS = []


def slip(note):
    SLIPS.append((_CUR["id"], note))


def low1(s):
    return s[:1].lower() + s[1:]


# =========================================================================== the 22 faculties (termbase = pi-2)
FACULTIES = [  # (Pāli key, bare-word key, Russian nominative), in the order of the Pāli list (^6-10-1; pi-2 ^2-219)
    ("cakkhundriyaṃ", "cakkhu", "способность глаза"),
    ("sotindriyaṃ", "sotaṃ", "способность уха"),
    ("ghānindriyaṃ", "ghānaṃ", "способность носа"),
    ("jivhindriyaṃ", "jivhā", "способность языка"),
    ("kāyindriyaṃ", "kāyo", "способность тела"),
    ("manindriyaṃ", "mano", "способность ума"),
    ("itthindriyaṃ", "itthī", "способность женственности"),
    ("purisindriyaṃ", "puriso", "способность мужественности"),
    ("jīvitindriyaṃ", "jīvitaṃ", "жизненная способность"),
    ("sukhindriyaṃ", "sukhaṃ", "способность удовольствия"),
    ("dukkhindriyaṃ", "dukkhaṃ", "способность боли"),
    ("somanassindriyaṃ", "somanassaṃ", "способность радости"),
    ("domanassindriyaṃ", "domanassaṃ", "способность уныния"),
    ("upekkhindriyaṃ", "upekkhā", "способность невозмутимости"),
    ("saddhindriyaṃ", "saddhā", "способность веры"),
    ("vīriyindriyaṃ", "vīriyaṃ", "способность усердия"),
    ("satindriyaṃ", "sati", "способность осознанности"),
    ("samādhindriyaṃ", "samādhi", "способность сосредоточения"),
    ("paññindriyaṃ", "paññā", "способность мудрости"),
    ("anaññātaññassāmītindriyaṃ", "anaññātaññassāmīti", "способность познания непознанного"),
    ("aññindriyaṃ", "aññaṃ", "способность окончательного знания"),
    ("aññātāvindriyaṃ", "aññātāvī", "способность обладателя окончательного знания"),
]
FACULTY_LIST_HEAD = "Двадцать две способности"   # Bāvīsatindriyāni (pi-2 ^2-219)


def faculty_cases(nom):
    """«способность глаза» -> (nom, gen, ins, acc); «жизненная способность» declines its adjective."""
    if nom == "жизненная способность":
        return nom, "жизненной способности", "жизненной способностью", "жизненную способность"
    rest = nom[len("способность "):]
    return nom, f"способности {rest}", f"способностью {rest}", nom


def register_faculties():
    for key, _, nom in FACULTIES:
        n, gen, ins, acc = faculty_cases(nom)
        st = key[:-1]
        G2.register_term(key, n, gen, ins, "f", acc=acc, forms=[st + "ñca", st + "ñceva", st + "nti"])


# bare words of the term-analysis questions (termbase: cakkhu глаз, sotaṃ ухо, ghānaṃ нос, jivhā язык, kāyo тело,
# mano ум, itthī женщина, puriso мужчина, jīvitaṃ жизнь, sukhaṃ удовольствие, dukkhaṃ боль (faculties chapter),
# somanassaṃ радость, domanassaṃ уныние, upekkhā невозмутимость, saddhā вера, sati осознанность, samādhi
# сосредоточение, paññā мудрость, anaññātaññassāmīti познание непознанного, aññaṃ окончательное знание, aññātāvī
# обладатель окончательного знания, indriyaṃ способность, indriyā / indriye способности; vīriyaṃ has no bare entry:
# «усердие» from vīriyindriyaṃ «способность усердия» and the style sheet vīriya = усердие)
BARE = [  # key, nom, gen, ins, gender, other Pāli forms
    ("cakkhu", "глаз", "глаза", "глазом", "m", ["cakkhū", "cakkhuṃ", "cakkhuñca", "cakkhuñceva", "cakkhūti"]),
    ("sotaṃ", "ухо", "уха", "ухом", "n", ["sotañca", "sotañceva", "sotanti"]),
    ("ghānaṃ", "нос", "носа", "носом", "m", ["ghānañca", "ghānañceva", "ghānanti"]),
    ("jivhā", "язык", "языка", "языком", "m", ["jivhaṃ", "jivhañca", "jivhañceva", "jivhāti"]),
    ("kāyo", "тело", "тела", "телом", "n", ["kāyaṃ", "kāyañca", "kāyañceva", "kāyoti"]),
    ("mano", "ум", "ума", "умом", "m", ["manaṃ", "manañca", "manañceva", "manoti"]),
    ("itthī", "женщина", "женщины", "женщиной", "f", ["itthiṃ", "itthiñca", "itthiñceva", "itthīti"]),
    ("puriso", "мужчина", "мужчины", "мужчиной", "m", ["purisaṃ", "purisañca", "purisañceva", "purisoti"]),
    ("jīvitaṃ", "жизнь", "жизни", "жизнью", "f", ["jīvitañca", "jīvitañceva", "jīvitanti"]),
    ("sukhaṃ", "удовольствие", "удовольствия", "удовольствием", "n", ["sukhañca", "sukhañceva", "sukhanti"]),
    ("dukkhaṃ", "боль", "боли", "болью", "f", ["dukkhañca", "dukkhañceva", "dukkhanti"]),
    ("somanassaṃ", "радость", "радости", "радостью", "f", ["somanassañca", "somanassañceva", "somanassanti"]),
    ("domanassaṃ", "уныние", "уныния", "унынием", "n", ["domanassañca", "domanassañceva", "domanassanti"]),
    ("upekkhā", "невозмутимость", "невозмутимости", "невозмутимостью", "f",
     ["upekkhaṃ", "upekkhañca", "upekkhañceva", "upekkhāti"]),
    ("saddhā", "вера", "веры", "верой", "f", ["saddhaṃ", "saddhañca", "saddhañceva", "saddhāti"]),
    ("vīriyaṃ", "усердие", "усердия", "усердием", "n", ["vīriyañca", "vīriyañceva", "vīriyanti"]),
    ("sati", "осознанность", "осознанности", "осознанностью", "f", ["satiṃ", "satiñca", "satiñceva", "satīti"]),
    ("samādhi", "сосредоточение", "сосредоточения", "сосредоточением", "n",
     ["samādhiṃ", "samādhiñca", "samādhiñceva", "samādhīti"]),
    ("paññā", "мудрость", "мудрости", "мудростью", "f", ["paññaṃ", "paññañca", "paññañceva", "paññāti"]),
    ("anaññātaññassāmīti", "познание непознанного", "познания непознанного", "познанием непознанного", "n",
     ["anaññātaññassāmītiṃ", "anaññātaññassāmītiñca"]),
    ("aññaṃ", "окончательное знание", "окончательного знания", "окончательным знанием", "n",
     ["aññañca", "aññañceva", "aññanti"]),
    ("aññātāvī", "обладатель окончательного знания", "обладателя окончательного знания",
     "обладателем окончательного знания", "m", ["aññātāviṃ", "aññātāviñca", "aññātāviñceva", "aññātāvīti"]),
    ("indriyaṃ", "способность", "способности", "способностью", "f", ["indriyañca", "indriyañceva", "indriyanti"]),
    ("indriyā", "способности", "способностей", "способностями", "pl", ["indriye"]),
]
ACC = {"itthī": "женщину", "puriso": "мужчину", "saddhā": "веру", "paññā": "мудрость", "upekkhā": "невозмутимость"}


def register_bare():
    for k, n, gen, ins, g, forms in BARE:
        G2.register_term(k, n, gen, ins, g, acc=ACC.get(k), forms=forms)
    # ^6-10-3 «anaññātaññāssāmīti»: spelling slip (termbase entry anaññātaññāssāmīti), rendered as meant
    G2.FORMS["anaññātaññāssāmīti"] = "anaññātaññassāmīti"
    G2.SPELL_SLIPS["anaññātaññāssāmīti"] = "spelling slip for anaññātaññassāmīti, rendered as meant (termbase entry)"


register_faculties()
register_bare()   # after G45: dukkhaṃ = «боль» here (termbase sense for the faculties chapter), not «страдание»

# =========================================================================== persons (intro units for G45.intro_ru)
ATTR = {  # sa-/a-X-kānaṃ and the other rebirth attributes (termbase)
    "sacakkhukānaṃ": "с глазом", "acakkhukānaṃ": "без глаза",          # G3 (termbase)
    "sasotakānaṃ": "с ухом", "asotakānaṃ": "без уха",
    "saghānakānaṃ": "с носом", "aghānakānaṃ": "без носа",
    "sacittakānaṃ": "с умом", "acittakānaṃ": "без ума",
    "sahetukānaṃ": "с корнями", "ahetukānaṃ": "без корней",           # no -ānaṃ entry: Sahetukaṃ «имеющий корни»,
    #                                                                   Ahetukaṃ «не имеющий корней», as sa-/a-cakkhuka
    "ñāṇasampayuttānaṃ": "со знанием", "ñāṇavippayuttānaṃ": "без знания",   # termbase
    "somanassena": "с радостью", "vinā somanassena": "без радости",          # termbase somanassena «радость»
    "upekkhāya": "с невозмутимостью", "vinā upekkhāya": "без невозмутимости",  # termbase upekkhāya
}
GENDER = {  # termbase itthīnaṃ «женщина», purisānaṃ «мужчина»; coordinator «перерождается женщиной / мужчиной»
    "itthīnaṃ": "женщиной", "na itthīnaṃ": "не женщиной",
    "purisānaṃ": "мужчиной", "na purisānaṃ": "не мужчиной",
}
WHO_VERB = {  # upapajjantānaṃ / upapajjantīnaṃ «перерождаться»; cavantānaṃ / cavantīnaṃ «умирать» (termbase)
    "upapajjantānaṃ": G2.REBORN, "upapajjantīnaṃ": G2.REBORN,
    "cavantānaṃ": G2.DIES, "cavantīnaṃ": G2.DIES,
    "uppajjantīnaṃ": "возникает",   # ^6-10-206 one-letter slip for upapajjantīnaṃ, a real word: kept as written
}


def _split_attrs(s):
    """'sacakkhukānaṃ na itthīnaṃ' -> ['sacakkhukānaṃ', 'na itthīnaṃ'] (greedy, two-word keys first)."""
    toks, out, i = s.split(), [], 0
    while i < len(toks):
        two = " ".join(toks[i:i + 2])
        if two in ATTR or two in GENDER:
            out.append(two)
            i += 2
        elif toks[i] in ATTR or toks[i] in GENDER:
            out.append(toks[i])
            i += 1
        else:
            return None
    return out


def attrs_ru(s):
    """Russian attribute phrase after «перерождается»: the gender word first («женщиной с глазом»; negated with a
    comma: «не женщиной, с глазом»; two: «не женщиной и не мужчиной»), the rest in the Pāli order joined
    «A и B» as G3 («с глазом и без уха»)."""
    ws = _split_attrs(s)
    if ws is None:
        return None
    gs = [GENDER[w] for w in ws if w in GENDER]
    os_ = [ATTR[w] for w in ws if w in ATTR]
    g = " и ".join(gs)
    o = " и ".join(os_)
    if g and o:
        return g + (", " if g.startswith("не ") else " ") + o
    return g or o


_AT = G2._alt(list(ATTR) + list(GENDER))
UNIT_RX = (rf"(?P<pre>itaresaṃ |itarāsaṃ |pacchimabhavikānaṃ )?(?P<a>(?:{_AT} )+)"
           r"(?P<w>upapajjantānaṃ|upapajjantīnaṃ|uppajjantīnaṃ|cavantānaṃ|cavantīnaṃ)")


def person_unit(m):
    """Intro unit «(itaresaṃ / pacchimabhavikānaṃ) ATTR… upapajjantānaṃ» -> («у тех, кто перерождается …», True)."""
    pre = (m.group("pre") or "").strip()
    w = m.group("w")
    if w == "uppajjantīnaṃ":
        slip("uppajjantīnaṃ for upapajjantīnaṃ: a one-letter slip that makes another word; kept as written "
             "(«кто возникает»)")
    verb = WHO_VERB[w]
    if pre == "pacchimabhavikānaṃ" and w.startswith("upapajj"):
        verb = G2.LAST_REBORN   # APPROVED: «у тех, кто в последний раз перерождается (женщиной …)»
    who = "у остальных, кто" if pre in ("itaresaṃ", "itarāsaṃ") else "у тех, кто"
    if pre == "pacchimabhavikānaṃ" and not w.startswith("upapajj"):
        return None
    return f"{who} {verb} {attrs_ru(m.group('a'))}", True


UNITS_G10a = [(UNIT_RX, "P", person_unit)]

# moments: «pavatte X-sampayutta-Y-vippayutta-cittassa uppādakkhaṇe» (termbase: «момент возникновения ума
# связанного с радостью и не связанного с верой»; G45 punctuation «ума, не связанного с жаждой,»)
QUAL = {"somanassa": "с радостью", "upekkhā": "с невозмутимостью", "saddhā": "с верой", "ñāṇa": "со знанием"}
KIND = {"sampayutta": "связанного", "vippayutta": "не связанного"}
MOM_G10a = {}
for _a in QUAL:
    for _ka in KIND:
        MOM_G10a[f"{_a}{_ka}cittassa"] = (f"ума, {KIND[_ka]} {QUAL[_a]}", True)
        for _b in QUAL:
            if _b != _a:
                for _kb in KIND:
                    MOM_G10a[f"{_a}{_ka}{_b}{_kb}cittassa"] = (
                        f"ума, {KIND[_ka]} {QUAL[_a]} и {KIND[_kb]} {QUAL[_b]}", True)


def install_units():
    """Extend G45's intro tables (planes from G2 incl. G3's -āvacara planes, moments) and prepend the G10a units."""
    for d, src in ((G45.PL_ACC, G2.PL_ACC), (G45.PL_LOC, G2.PL_LOC), (G45.PL_ABL, G2.PL_ABL),
                   (G45.BEINGS, G2.BEINGS)):
        for k, v in src.items():
            d.setdefault(k, v)
    G45.MOM_GEN.update(MOM_G10a)
    G45._MG = "(?P<g>" + "|".join(sorted(map(re.escape, G45.MOM_GEN), key=len, reverse=True)) + ")"
    G45.UNITS = None
    G45.units("")
    G45.UNITS[:0] = UNITS_G10a


install_units()
THEY = G45.THEY   # «у них»


def person_answer(s):
    """INTRO tesaṃ / tāsaṃ (tattha) <partial | pair> (G45.person_answer; the feminine tāsaṃ is «у них» too)."""
    return G45.person_answer(s.replace(" tāsaṃ ", " tesaṃ "))


# =========================================================================== paṇṇatti additions
G2.HEAD.update({k.lower(): v for k, v in {   # termbase
    "Suddhindriyavāro": "раздел о способностях как таковых",
    "Suddhindriyamūlacakkavāro": "круговой раздел на основе способностей как таковых",
}.items()})
REL = {"m": "который", "f": "которая", "n": "которое"}
REST_ADJ = {"m": "Остальной", "f": "Остальная", "n": "Остальное"}


def which_answer(s):
    """«Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca.» = «Ухо, которое является способностью, является и ухом, и
    способностью.» (coordinator: a relative clause before «A ceva B ca» takes one main verb, then «и A, и B»)."""
    m = re.match(r"^(?:Yaṃ|Yo|Yā) (\S+) indriyaṃ (?:taṃ|so|sā) (\S+?ñceva|\S+ ceva) indriyañca\.$", s)
    if not m:
        return None
    x, x2 = G2.term(m.group(1)), G2.term(m.group(2).replace(" ceva", ""))
    if not x or x != x2:
        return None
    X, I = TERMS[x], TERMS["indriyaṃ"]
    return f"{cap(X['nom'])}, {REL[X['g']]} является {I['ins']}, является и {X['ins']}, и {I['ins']}."


def rest_answer(s):
    """«Avasesaṃ sotaṃ na indriyaṃ.» = «Остальное ухо не является способностью.» (avaseso «остальной», termbase)."""
    m = re.match(r"^(?:Avasesaṃ|Avaseso|Avasesā) (\S+) na (indriyaṃ|indriyā)\.$", s)
    if not m or not G2.term(m.group(1)) or G2.term(m.group(1)) in ("indriyā", "indriyaṃ"):
        return None
    x = G2.term(m.group(1))
    X = TERMS[x]
    if X["g"] not in REST_ADJ:
        return None
    if m.group(2) == "indriyā":
        slip("«avaseso kāyo na indriyā»: plural indriyā where the parallels have indriyaṃ; kept as written "
             "(«не является способностями»)")
    return f"{REST_ADJ[X['g']]} {X['nom']} не является {TERMS[G2.term(m.group(2))]['ins']}."


def rest_sg_answer(s):
    """«Upekkhindriyaṃ ṭhapetvā avasesā upekkhā, na upekkhindriyaṃ.»: avasesā agrees with the singular upekkhā, so
    «Кроме способности невозмутимости, остальное является невозмутимостью, но не является …» (as G3 / G45
    «avaseso kāyo» = «остальное является телом»); likewise «… avasesā na upekkhindriyaṃ, upekkhā.»"""
    m = re.match(r"^(\S+) ṭhapetvā avasesā (?:(\S+), na (\S+)|na (\S+), (\S+))\.$", s)
    if not m:
        return None
    x = G2.term(m.group(1))
    b = G2.term(m.group(2) or m.group(5))
    c = G2.term(m.group(3) or m.group(4))
    if not (x and b and c) or TERMS[b]["g"] == "pl":
        return None
    head = f"{G2.EXCEPT} {TERMS[x]['gen']}, {G3.REST_SG}"
    if m.group(2):
        return f"{head} является {TERMS[b]['ins']}, но не является {TERMS[c]['ins']}."
    return f"{head} не является {TERMS[c]['ins']}, но является {TERMS[b]['ins']}."


# =========================================================================== sentence translator
LABEL_NOTES = {  # exact Pāli sentence -> slip note (the sentence is translated as written)
    "(Ka) indriyā domanassindriyanti?": "label (Ka) on the second question of a pair (Kha expected); kept as written",
    "(Kha) indriyaṃ saddhindriyanti?": "«indriyaṃ» (sg.) where the parallels have «indriyā»; kept as written "
                                       "(«Способность является способностью веры?»)",
}


def core(s):
    """One complete Pāli sentence -> Russian, or None."""
    if s in LABEL_NOTES:
        slip(LABEL_NOTES[s])
    for fn in (G3.mulaka, which_answer, rest_answer, rest_sg_answer, person_answer):
        r = fn(s)
        if r:
            return r
    r = G45.translate_sentence(s)
    if r:
        return r
    for fn in (G3.place_answer, G3.abbr_pv):
        r = fn(s)
        if r:
            return r
    return None


SEP = re.compile(r"(…(?:pe|Pe)…\.?|…\.?)")


def fragment(p):
    """A piece between two «…» -> Russian, or None."""
    for end in ("", "?", "."):
        if end and p.endswith(("?", ".")):
            break
        r = core(p + end)
        if r:
            return r[:-1] if end else r
    toks = p.split()
    k, i = G2.take_term(toks, 0)
    if k and i == len(toks):
        return TERMS[k]["nom"]
    return None


def abbreviated(s):
    """Split at «…pe…» / «…» and translate every piece; «…pe…» = «…» glued to the word before it, a final «…pe….»
    = «…» (never «….»); the Pāli space after «?» / «.» is kept (G3)."""
    parts = SEP.split(s)
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append("…")
            continue
        if not p.strip():
            out.append(p)
            continue
        lead = p[:len(p) - len(p.lstrip())]
        body = p.strip()
        r = fragment(body)
        if r is None:
            raise ValueError(f"no formula for piece {body!r} of {s!r} (segment {_CUR['id']})")
        r = cap(r) if body[:1].isupper() else low1(r) if body[:1].islower() else r
        out.append(lead + r)
    return "".join(out)


def translate_sentence(s):
    s = s.strip()
    r = core(s)
    if r:
        return r
    if "…" in s:
        return abbreviated(s)
    raise ValueError(f"no formula for: {s!r} (segment {_CUR['id']})")


# =========================================================================== line translator
LINE_SLIPS = {  # Pāli as found -> (as meant, note): plain spelling slips and missing punctuation only
    "avaseso kāyo na kāyindriyaṃ.": ("avaseso kāyo, na kāyindriyaṃ.",
                                     "missing comma before «na kāyindriyaṃ» (the parallel lines have it); "
                                     "rendered as meant"),
}
FIXED = {}


def _fixed():
    f = {}
    keys = [k for k, _, _ in FACULTIES]
    pali = ("Bāvīsatindriyāni – " + ", ".join(keys) + ".").replace(
        "vīriyindriyaṃ,", "vīriyindriyaṃ [viriyindiyaṃ (sī. syā.)],")
    ru = (FACULTY_LIST_HEAD + " – " + ", ".join(TERMS[k]["nom"] for k in keys) + ".").replace(
        "способность усердия,", "способность усердия " + G2.var_br("viriyindiyaṃ", "sī. syā.", kind="написания") + ",")
    f[pali] = ru   # pi-2 ^2-219 has the same bracket «[вариант написания (Sī., Syā.): viriyindriyaṃ]»
    a = ("Kāyindriyaṃ ṭhapetvā avaseso kāyo, na kāyindriyaṃ. Kāyindriyaṃ kāyo ceva kāyindriyañca.")
    r = " ".join(translate_sentence(x) for x in G3.split_sentences(a))
    f["Kāyindriyaṃ ṭhapetvā avaseso kāyo [avasesā kāyo (sī. syā. ka.)], na kāyindriyaṃ. "
      "Kāyindriyaṃ kāyo ceva kāyindriyañca."] = G45.ins_after(r, "является телом",
                                                            G2.var_br("avasesā kāyo", "sī. syā. ka."))
    return f


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian."""
    global FIXED
    if not FIXED:
        FIXED = {"__building__": None}
        FIXED = _fixed()
    if pali.startswith("#"):
        return G2.heading(pali)
    if pali in FIXED:
        return FIXED[pali]
    for a, (b, note) in LINE_SLIPS.items():
        if a in pali:
            slip(note)
            pali = pali.replace(a, b)
    if re.search(r"\w …(?:pe|Pe)…", pali):
        slip("a space between a word and «…pe…» in the Pāli: «…» glued to the word (brief)")
    return " ".join(translate_sentence(x) for x in G3.split_sentences(pali))


# =========================================================================== build + checks
def render(pali_text):
    blocks, problems = [], []
    for sid, plines in S.segs(pali_text):
        _CUR["id"] = G45._CUR["id"] = sid
        ru = []
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            r = translate_line(body)
            # «? …Pe…» spaced so in the Pāli keeps its space (brief: as the Pāli spaces it); « …» after a word is
            # never produced
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
            if body.startswith("#") or body in FIXED:
                continue
            for a, (b, _) in LINE_SLIPS.items():
                body = body.replace(a, b)
            for x in G3.split_sentences(body):
                try:
                    translate_sentence(x)
                except (ValueError, KeyError, AssertionError, TypeError) as e:
                    bad += 1
                    print(sid, "|", x, "|", e)
    print(ch, "sentences without a formula:", bad)


# =========================================================================== notes (frames for G10b)
def notes_md():
    tl = translate_line
    L = ["# notes-rails-G10a: Indriyayamaka (10-01 … 10-04) frames", "",
         "Format: Pāli = Russian, one per line. Builder: build_rails_G10a_ru.py (importlib.import_module(",
         "\"build_rails_G10a_ru\"); importing writes nothing). Built on G2 (paṇṇatti / pavatti frames), G3 (sa-/a-X-ka",
         "persons, mūlaka labels, «…pe…» questions, place lists) and G45 (intro_ru: person / time / place intros).",
         "For G10b: FACULTIES, faculty_cases(), BARE, ATTR, GENDER, attrs_ru(), person_unit / UNITS_G10a (already",
         "prepended to G45.UNITS on import), MOM_G10a, core(), translate_sentence(), translate_line(), render().",
         "", "## The 22 faculties (termbase = pi-2 Indriyavibhaṅga; nom / gen / ins)", ""]
    for key, _, nom in FACULTIES:
        n, gen, ins, acc = faculty_cases(nom)
        L.append(f"{key} = {n} / {gen} / {ins}" + (f" (acc. {acc})" if acc != n else ""))
    L += ["", "## Bare words (term-analysis questions)", ""]
    L += [f"{k} = {n} / {gen} / {ins}" for k, n, gen, ins, _, _ in BARE]
    L += ["dukkhaṃ = боль in this chapter (termbase sense for dukkhindriya), not «страдание» (Saccayamaka)",
          "vīriyaṃ (no bare entry) = усердие (vīriyindriyaṃ «способность усердия»; style sheet vīriya = усердие)",
          "", "## Person attributes (after «перерождается»)", ""]
    L += [f"{k} = {v}" for k, v in {**ATTR, **GENDER}.items()]
    L += ["order: the gender word first («женщиной с глазом»; negated with a comma «не женщиной, с глазом»;",
          "  «не женщиной и не мужчиной»), the other attributes in the Pāli order joined «A и B» (G3);",
          "  ahetukānaṃ / sahetukānaṃ: no entry, «без корней / с корнями» built from Ahetukaṃ / Sahetukaṃ",
          "  «не имеющий / имеющий корни» on the pattern of sa-/a-cakkhuka «с глазом / без глаза»",
          "tāsaṃ (feminine of tesaṃ) = у них (not rendered after a named person, as tesaṃ: G2)",
          "uppajjantīnaṃ (^6-10-206, for upapajjantīnaṃ) = «кто возникает»: a one-letter slip, kept as written", ""]
    ex = ["Sacakkhukānaṃ asotakānaṃ upapajjantānaṃ", "Sacakkhukānaṃ na itthīnaṃ upapajjantānaṃ",
          "Sacakkhukānaṃ itthīnaṃ upapajjantīnaṃ", "Itthīnaṃ acakkhukānaṃ upapajjantīnaṃ",
          "Purisānaṃ vinā somanassena upapajjantānaṃ", "Sahetukānaṃ na purisānaṃ upapajjantānaṃ",
          "Upekkhāya ñāṇasampayuttānaṃ upapajjantānaṃ",
          "Sabbesaṃ cavantānaṃ na itthīnaṃ na purisānaṃ upapajjantānaṃ",
          "Vinā somanassena upapajjantānaṃ pavatte somanassavippayuttacittassa uppādakkhaṇe",
          "Pavatte somanassasampayuttasaddhāvippayuttacittassa uppādakkhaṇe",
          "Ahetukānaṃ upekkhāya upapajjantānaṃ pavatte saddhāvippayuttaupekkhāsampayuttacittassa uppādakkhaṇe",
          "Sacittakānaṃ upapajjantānaṃ pavatte cittassa uppādakkhaṇe",
          "Sabbesaṃ cavantānaṃ pavatte cittassa bhaṅgakkhaṇe",
          "Sabbesaṃ cittassa bhaṅgakkhaṇe ñāṇavippayuttacittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ",
          "Itaresaṃ sacakkhukānaṃ upapajjantānaṃ", "Pacchimabhavikānaṃ itthīnaṃ upapajjantīnaṃ"]
    L += [f"{p} tesaṃ = {G45.intro_ru(p)}" for p in ex]
    L += ["", "## Moments", "",
          "X-sampayutta-cittassa = ума, связанного с X,; X-vippayutta- = ума, не связанного с X,; two members:",
          "  «ума, связанного с радостью и не связанного с верой,» (X: somanassa с радостью, upekkhā с невозмутимостью,",
          "  saddhā с верой, ñāṇa со знанием; termbase phrases, G45 punctuation)", "",
          "## Pavatti answers", ""]
    ex = ["Sacakkhukānaṃ na itthīnaṃ upapajjantānaṃ tesaṃ cakkhundriyaṃ uppajjati, no ca tesaṃ itthindriyaṃ uppajjati.",
          "Sacakkhukānaṃ itthīnaṃ upapajjantīnaṃ tāsaṃ cakkhundriyañca uppajjati itthindriyañca uppajjati.",
          "Itthīnaṃ acakkhukānaṃ upapajjantīnaṃ tāsaṃ itthindriyaṃ uppajjati, no ca tāsaṃ cakkhundriyaṃ uppajjati.",
          "Vinā somanassena upapajjantānaṃ pavatte somanassavippayuttacittassa uppādakkhaṇe tesaṃ jīvitindriyaṃ "
          "uppajjati, no ca tesaṃ somanassindriyaṃ uppajjati.",
          "Pavatte somanassasampayuttasaddhāvippayuttacittassa uppādakkhaṇe tesaṃ somanassindriyaṃ uppajjati, no ca "
          "tesaṃ saddhindriyaṃ uppajjati.",
          "Acittakānaṃ upapajjantānaṃ tesaṃ jīvitindriyaṃ uppajjati, no ca tesaṃ manindriyaṃ uppajjati.",
          "Rūpāvacare arūpāvacare tattha jīvitindriyaṃ uppajjati, no ca tattha ghānindriyaṃ uppajjati.",
          "Asaññasatte arūpe tattha jīvitindriyaṃ uppajjati, no ca tattha cakkhundriyaṃ uppajjati.",
          "(Cakkhundriyamūlakaṃ)"]
    L += [f"{p} = {tl(p)}" for p in ex]
    L += ["", "## Paṇṇatti", ""]
    ex = ["(Ka) cakkhu cakkhundriyaṃ?", "(Kha) indriyā sotindriyaṃ?", "(Ka) na cakkhu na indriyaṃ?",
          "(Kha) na indriyā na aññātāvī?", "(Ka) jīvitaṃ jīvitindriyanti?",
          "Dibbacakkhu paññācakkhu cakkhu, na cakkhundriyaṃ.", "Cakkhundriyaṃ cakkhu ceva cakkhundriyañca.",
          "Sotindriyaṃ indriyañceva sotindriyañca.", "Avasesā indriyā na sotindriyaṃ.",
          "Itthindriyaṃ na itthī, itthindriyaṃ.",
          "Itthiñca itthindriyañca ṭhapetvā avasesā na ceva itthī na ca itthindriyaṃ.",
          "Upekkhindriyaṃ ṭhapetvā avasesā upekkhā, na upekkhindriyaṃ.",
          "Upekkhindriyaṃ ṭhapetvā avasesā na upekkhindriyaṃ, upekkhā.",
          "Kāyindriyaṃ ṭhapetvā avaseso na kāyindriyaṃ, kāyo.",
          "Cakkhuṃ ṭhapetvā avasesā indriyā na cakkhu, indriyā.",
          "Cakkhuñca indriye ca ṭhapetvā avasesā na ceva cakkhu na ca indriyā.",
          "Yaṃ sotaṃ indriyaṃ taṃ sotañceva indriyañca.", "Avasesaṃ sotaṃ na indriyaṃ.",
          "Yo kāyo indriyaṃ so kāyo ceva indriyañca.", "Yā upekkhā indriyaṃ sā upekkhā ceva indriyañca.",
          "Avasesā upekkhā na indriyaṃ.",
          "Sotaṃ sotindriyaṃ? Indriyā cakkhundriyaṃ?…Pe….",
          "(Kha) na indriyā na cakkhundriyaṃ? …Pe… na indriyā na aññātāvindriyaṃ?",
          "Sukhaṃ sukhindriyanti? Āmantā …pe….",
          "Cakkhundriyaṃ indriyañceva cakkhundriyañca. Avasesā indriyā na cakkhundriyaṃ…pe…."]
    L += [f"{p} = {tl(p)}" for p in ex]
    L += ["Yaṃ X indriyaṃ taṃ Xñceva indriyañca = «X, который / которая / которое является способностью, является и X,",
          "  и способностью» (coordinator: one main verb after a relative clause); Avasesaṃ / Avaseso / Avasesā X =",
          "  «Остальное / Остальной / Остальная X»; X ṭhapetvā avasesā + a singular noun (upekkhā) = «остальное» (sg.)",
          "", "## Headings, lists", ""]
    ex = ["### Indriyayamakaṃ", "#### Suddhindriyavāro", "#### Suddhindriyamūlacakkavāro", "#### Pavattivāro",
          "#### Uppādavāro", "##### (Ga) anulomapuggalokāsā", "##### (Ṅa) paccanīkaokāso"]
    L += [f"{p} = {G2.heading(p)}" for p in ex]
    L.append("Bāvīsatindriyāni – cakkhundriyaṃ, … = " + FIXED[[k for k in FIXED if k.startswith("Bāvīs")][0]])
    return "\n".join(L) + "\n"


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        translate_line("#")
        for ch in sys.argv[2:]:
            probe(ch)
        return
    txt = (S.RU / "pi-2-russian-plain.md").read_text(encoding="utf-8")
    miss = [nom for _, _, nom in FACULTIES if nom not in txt] + ([FACULTY_LIST_HEAD] if FACULTY_LIST_HEAD not in txt
                                                                  else [])
    assert not miss, f"pi-2 strings not found: {miss}"
    problems = []
    for ch in CHAPTERS:
        pt = (PALI / ch).read_text(encoding="utf-8")
        ru, pr = render(pt)
        problems += pr
        e, n = S.check_file(pt, ru)
        problems += [f"{ch}: {x}" for x in e]
        (OUT / ch).write_text(ru, encoding="utf-8", newline="\n")
        print(f"wrote {ch}: {n} segments")
    slips = list(SLIPS) + list(G2.SLIPS) + list(G45.SLIPS)
    (S.RAILS / "notes-rails-G10a.md").write_text(notes_md(), encoding="utf-8", newline="\n")
    print("wrote notes-rails-G10a.md")
    for sid, note in dict.fromkeys(slips):
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()