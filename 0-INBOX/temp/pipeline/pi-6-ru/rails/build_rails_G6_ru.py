"""pi-6 Yamaka, G6 (Saṅkhārayamaka 6-01, 6-02): Russian RAILS builder.

Built on the frame-setters G2 (build_rails_G2_ru: paṇṇatti, pavatti, pariññā frames, person groups, headings)
and G8 (build_rails_G8_ru: moment phrases, «у вошедших в медитативное достижение прекращения»). Importing this
module writes nothing:
    import sys, importlib
    sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru\\rails")
    G6 = importlib.import_module("build_rails_G6_ru")
    G6.translate_line(pali_line)
Exposes: the three formations and the bare words (registered in G2.TERMS), the jhāna phrases (jhanas, JH_ACC,
JH_LOC), place lists (place_list), the moment phrases with «vinā …» (moment_ru, MOM_SUBJ, VINA), the
«yassa cittassa anantarā … pacchimacittaṃ uppajjissati» groups, bhūmi levels (BHUMI), the intro parser
(intro_items / join_items: a moment after a person group belongs to that group), person_answer, place_answer,
unlabeled questions, …pe… fragments and the editorial notes (NOTES).
Run as a script (python -I -X utf8 -B build_rails_G6_ru.py) to write 6-01 / 6-02 and notes-rails-G6.md and run the
per-line checks; `--probe <ch> …` prints the sentences without a formula (writes nothing).

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
"""
import importlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_sample_ru as S  # noqa: E402

G2 = importlib.import_module("build_rails_G2_ru")
G8 = importlib.import_module("build_rails_G8_ru")

ROOT, PALI, OUT = S.ROOT, S.PALI, S.OUT
CHAPTERS = ["6-01-sankharayamaka.md", "6-02-sankharayamaka.md"]
cap = S.cap
TERMS = G2.TERMS
SLIPS = G2.SLIPS
_CUR = G2._CUR


def slip(note):
    G2.slip(note)


def lowfirst(s):
    return s[:1].lower() + s[1:]


def join_and(ws):
    """«A», «A и B», «A, B и C»."""
    return ws[0] if len(ws) == 1 else ", ".join(ws[:-1]) + " и " + ws[-1]


# =========================================================================== terms (termbase)
def _sankhara(key, nom, gen, ins, stem):
    G2.register_term(key, nom, gen, ins, "m", forms=[stem + "aṃ", stem + "añca"])


_sankhara("kāyasaṅkhāro", "телесный формирующий фактор", "телесного формирующего фактора",
          "телесным формирующим фактором", "kāyasaṅkhār")                   # termbase kāyasaṅkhāro (pi-5 same)
_sankhara("vacīsaṅkhāro", "речевой формирующий фактор", "речевого формирующего фактора",
          "речевым формирующим фактором", "vacīsaṅkhār")                    # termbase vacīsaṅkhāro (pi-5 same)
_sankhara("cittasaṅkhāro", "формирующий фактор ума", "формирующего фактора ума",
          "формирующим фактором ума", "cittasaṅkhār")                       # termbase (pi-5: умственный …)
G2.register_term("saṅkhāro", "формирующий фактор", "формирующего фактора", "формирующим фактором", "m",
                 forms=["saṅkhāraṃ"])                                       # termbase saṅkhāro (bare word)
G2.register_term("kāyo", "тело", "тела", "телом", "n", forms=["kāyaṃ", "kāyañca"])   # termbase kāyo, Kāyañca
G2.register_term("vacī", "речь", "речи", "речью", "f", forms=["vaciṃ", "vaciñca"])  # termbase vacī, Vaciñca
G2.register_term("cittaṃ", "ум", "ума", "умом", "m", forms=["cittañca"])            # termbase cittaṃ, Cittañca
SANKHARA_KEYS = ["kāyasaṅkhāro", "vacīsaṅkhāro", "cittasaṅkhāro"]
BARE_KEYS = ["kāyo", "vacī", "cittaṃ"]

# subjects of the naming answers: «Телесный формирующий фактор не является телом, но является …» (G2 frame)
for _k in SANKHARA_KEYS + BARE_KEYS:
    G2.SUBJ[_k] = (cap(TERMS[_k]["nom"]), "sg")
G2.SUBJ["avasesā saṅkhārā"] = ("Остальные формирующие факторы", "pl")   # avasesā «остальной», saṅkhārā (termbase)

# =========================================================================== planes (as G3: termbase -āvacara)
for _p, _ru in (("kāmāvacar", "мире чувственных желаний"), ("rūpāvacar", "мире форм"),
                ("arūpāvacar", "мире без форм")):
    G2.PL_ACC[_p + "aṃ"] = f"в {_ru}"
    G2.PL_LOC[_p + "e"] = f"в {_ru}"
    G2.PL_ABL[_p + "ā"] = f"в {_ru}"
G2.BEINGS["kāmāvacarānaṃ"] = "существ мира чувственных желаний"
G2.BEINGS["rūpāvacarānaṃ"] = "существ мира форм"
G2.BEINGS["arūpāvacarānaṃ"] = "существ мира без форм"
G2.GROUP_RULES = None

# =========================================================================== jhānas and places
# termbase Catutthajjhānaṃ / Catutthajjhāne «четвёртое медитативное погружение» (jhāna «медитативное погружение»);
# the other ordinals have no entry: built the same way (pi-5 «первое погружение»: the pi-6 termbase adds «медитативное»).
JH = {"paṭhamajjhān": ("первое", "первом"), "dutiyajjhān": ("второе", "втором"),
      "tatiyajjhān": ("третье", "третьем"), "catutthajjhān": ("четвёртое", "четвёртом")}
JH_ACC = {k + "aṃ": k for k in JH}
JH_LOC = {k + "e": k for k in JH}
JH_NOUN = ("медитативное погружение", "медитативном погружении")


def _v(word):
    return "во" if word.startswith("втор") else "в"


def jhanas(stems, case):
    """['dutiyajjhān', 'tatiyajjhān'], 0 -> «во второе и в третье медитативное погружение» (case 0 acc., 1 loc.)."""
    return join_and([f"{_v(JH[s][case])} {JH[s][case]}" for s in stems]) + " " + JH_NOUN[case]


def place_list(words):
    """Locative places: consecutive jhānas share one noun; joined «A, B и C» (G2 _places)."""
    items, run = [], []
    for w in words:
        w = w.lower()
        if w in JH_LOC:
            run.append(JH_LOC[w])
            continue
        if run:
            items.append(jhanas(run, 1))
            run = []
        items.append(G2.PL_LOC[w])
    if run:
        items.append(jhanas(run, 1))
    return join_and(items)


# levels (termbase Savitakkasavicārabhūmiyaṃ «уровень с направленной мыслью и удержанием мысли», Avitakka… «без …»)
BHUMI = {"savitakkasavicārabhūmiyaṃ": "на уровне с направленной мыслью и удержанием мысли",
         "avitakkaavicārabhūmiyaṃ": "на уровне без направленной мысли и без удержания мысли"}

# =========================================================================== moments (G8 shared phrases)
# uppādakkhaṇe / bhaṅgakkhaṇe «в момент возникновения / распада» (G8, pi-5); subjects in the genitive (termbase):
MOM_SUBJ = {
    "cittassa": "ума",
    "pacchimacittassa": "последнего ума",
    "assāsapassāsānaṃ": "вдохов и выдохов",
    "vitakkavicārānaṃ": "направленной мысли и удержания мысли",
    "avitakkaavicāracittassa": "ума без направленной мысли и без удержания мысли",
    "savitakkasavicārapacchimacittassa": "последнего ума с направленной мыслью и удержанием мысли",
    "avitakkaavicārapacchimacittassa": "последнего ума без направленной мысли и без удержания мысли",
}
KHANA = {"uppādakkhaṇe": "в момент возникновения", "bhaṅgakkhaṇe": "в момент распада"}
VINA = {"assāsapassāsehi": "без вдохов и выдохов",                       # vinā «без»; assāsapassāsa (termbase)
        "vitakkavicārehi": "без направленной мысли и удержания мысли"}    # vitakkavicāra (termbase)


def moment_ru(subj, khana, vina=None):
    """'vinā assāsapassāsehi cittassa uppādakkhaṇe' -> «в момент возникновения ума без вдохов и выдохов»;
    after a subject that already has «без …» the «vinā» phrase follows a comma."""
    s = MOM_SUBJ[subj]
    r = f"{KHANA[khana]} {s}"
    if vina:
        r += (", " if "без" in s else " ") + VINA[vina]
    return r


ANANTARA = "сразу после данного ума"        # yassa cittassa anantarā (coordinator shared phrase; termbase anantarā)
LAST_MIND = "последний ум"                  # pacchimacittaṃ (termbase)
AVV = "без направленной мысли и без удержания мысли"   # avitakkaavicāra- (termbase)
SAMANGI_LAST = "у обладающих последним умом"           # Pacchimacittasamaṅgīnaṃ (G8; termbase)
ENTERED = "у вошедших"                                  # samāpannānaṃ «вошедший» (termbase; pi-5 «у вошедшего в …»)
NIRODHA = "у вошедших в медитативное достижение прекращения"   # nirodhasamāpannānaṃ (G8)
SAME_THEY = "у них же"                      # tesaṃyeva (termbase «они же»)
ALL = "у всех"                              # sabbesaṃ
SECOND_MIND = "когда присутствует второй ум"   # dutiye citte vattamāne (coordinator: citte vattamāne «когда присутствует … ум»)
THEY = "у них"                              # tesaṃ when no person is named (G8 / coordinator)


def _it(ru, k="P", rel=False, place=False):
    return {"ru": ru, "k": k, "rel": rel, "place": place}


def _rules():
    G, A, L = G2._alt(G2.BEINGS), G2._alt(G2.PL_ACC), G2._alt(G2.PL_LOC)
    J, BH = G2._alt(JH_ACC), G2._alt(BHUMI)
    MS, VN = G2._alt(MOM_SUBJ), G2._alt(VINA)
    MOM = rf"(?:vinā ({VN}) )?({MS}) (uppādakkhaṇe|bhaṅgakkhaṇe)"
    return [
        (rf"yassa cittassa anantarā ({G}) pacchimacittaṃ uppajjissati",
         lambda m: _it(f"у {G2.BEINGS[m.group(1)]}, у которых {ANANTARA} возникнет {LAST_MIND}", rel=True)),
        (rf"yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati",
         lambda m: _it(f"у тех, у кого {ANANTARA} возникнет {LAST_MIND} {AVV}", rel=True)),
        (rf"((?:{L} )+)pacchimabhavikānaṃ",
         lambda m: _it(f"у тех, кто {G2.LAST_LIFE} {place_list(m.group(1).split())}", rel=True, place=True)),
        (rf"ye ca ((?:{A} )+)upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ",
         lambda m: _it(f"у тех умирающих, кто, {G2.REBORN_ABS} {G2._places(m.group(1).strip(), G2.PL_ACC)}, "
                       f"{G2.PARINIB_FUT}", rel=True)),
        (rf"((?:{L} )+)pacchimacittasamaṅgīnaṃ",
         lambda m: _it(f"{SAMANGI_LAST} {place_list(m.group(1).split())}", place=True)),
        (rf"({BH}) pacchimacittasamaṅgīnaṃ", lambda m: _it(f"{SAMANGI_LAST} {BHUMI[m.group(1)]}", place=True)),
        (r"avitakkaavicārapacchimacittasamaṅgīnaṃ", lambda m: _it(f"{SAMANGI_LAST} {AVV}")),
        (r"pacchimacittasamaṅgīnaṃ", lambda m: _it(SAMANGI_LAST)),
        (rf"((?:{J} )+)samāpannānaṃ", lambda m: _it(f"{ENTERED} {jhanas([JH_ACC[w] for w in m.group(1).split()], 0)}")),
        (r"nirodhasamāpannānaṃ", lambda m: _it(NIRODHA)),
        (r"tesaṃyeva", lambda m: _it(SAME_THEY)),
        (r"sabbesaṃ(?! cavantānaṃ| upapajjantānaṃ)", lambda m: _it(ALL)),
        (rf"itaresaṃ ({BH})", lambda m: _it(f"у остальных {BHUMI[m.group(1)]}", place=True)),
        (rf"((?:{L} )+){MOM}",
         lambda m: _it(f"{place_list(m.group(1).split())} {moment_ru(m.group(3), m.group(4), m.group(2))}", "M",
                       place=True)),
        (rf"({BH}) {MOM}",
         lambda m: _it(f"{BHUMI[m.group(1)]} {moment_ru(m.group(3), m.group(4), m.group(2))}", "M", place=True)),
        (MOM, lambda m: _it(moment_ru(m.group(2), m.group(3), m.group(1)), "M")),
        (r"dutiye citte vattamāne", lambda m: _it(SECOND_MIND, "M", rel=True)),
        (rf"({BH})", lambda m: _it(BHUMI[m.group(1)], "L", place=True)),
    ]


RULES = None   # built lazily (after the tables are complete)


def intro_items(pali):
    """Pāli intro (before «tesaṃ») -> list of items {ru, k: P person / M moment / L level, rel, place}; G6 shapes
    first, then G2's person groups."""
    global RULES
    if RULES is None:
        RULES = _rules()
    if G2.GROUP_RULES is None:
        G2.intro_groups("")
    s, out = pali.strip().lower(), []
    while s:
        for rx, fn in RULES:
            m = re.match(rx + r"(?= |$)", s)
            if m:
                out.append(fn(m))
                break
        else:
            for rx, fn in G2.GROUP_RULES:
                m = re.match(rx + r"(?= |$)", s)
                if m:
                    ru, rel = fn(m)
                    out.append(_it(ru, rel=rel))
                    break
            else:
                return None
        s = s[m.end():].strip()
    return out


def join_items(items):
    """A moment right after person groups belongs to them: the persons since the last moment (up to a relative
    clause) form one unit, joined «A и B», then the moment: «у вошедших в первое медитативное погружение и у существ
    мира чувственных желаний в момент возникновения вдохов и выдохов»; a clause moment («, когда присутствует второй
    ум,») belongs to the last person only. Units are joined as G2 does: «A, B и C» in the Pāli order, a relative
    clause closed by a comma, capitalised."""
    units, run = [], []
    for it in items:
        if it["k"] == "P":
            run.append(it)
            continue
        tail = []
        while run and not run[-1]["rel"] and not (it["rel"] and tail):
            tail.insert(0, run.pop())
        units += run
        run = []
        if tail:
            ru = join_and([t["ru"] for t in tail]) + (", " if it["rel"] else " ") + it["ru"]
            units.append(_it(ru, rel=it["rel"]))
        else:
            units.append(it)
    units += run
    return G2.join_groups([(x["ru"], x["rel"]) for x in units])


def intro(pali):
    items = intro_items(pali)
    return join_items(items) if items else None


def person_answer(s):
    """INTRO tesaṃ (tattha) <partial | pair>. «у них» only when no person is named; «tesaṃ tattha» after a person
    intro = «… там» (G2); after an intro that names only a level / moment with a place, «tattha» is not rendered."""
    body = s[:-1]
    for m in re.finditer(r" tesaṃ(?P<t> tattha)? ", body):
        items = intro_items(body[:m.start()])
        if not items:
            continue
        toks = body[m.end():].split()
        p = G2.parse_partial(toks)
        q = None if p else G2.parse_pair(toks)
        if not (p or q):
            continue
        head = join_items(items)
        has_p = any(i["k"] == "P" for i in items)
        has_place = any(i["place"] for i in items)
        if not has_p:
            head += f" {THEY}"
        there = " там" if m.group("t") and (has_p or not has_place) else ""
        clause = G2.partial(*p) if p else G2.pair(*q)
        return f"{head}{there} {clause}."
    return None


def _ploc():
    return G2._alt({**G2.PL_LOC, **JH_LOC})


def place_answer(s):
    """PLACES tattha <partial | pair> (okāsa): «Во втором и в третьем медитативном погружении возникает …, но там
    не возникает …» (the resumptive «tattha» after the named places is not rendered: G2)."""
    m = re.match(rf"^((?:{_ploc()} )+)tattha (.+)\.$", s, re.I)
    if not m:
        return None
    place = cap(place_list(m.group(1).split()))
    toks = m.group(2).split()
    p = G2.parse_partial(toks, place=True)
    if p:
        return f"{place} {G2.partial(*p, who=None)}."
    p = G2.parse_pair(toks)
    if p:
        return f"{place} {G2.pair(*p)}."
    return None


# =========================================================================== questions and …pe… fragments
def _strip_label(r):
    return re.sub(r"^\([а-я]\) ", "", r)


def pv_question(s):
    """Unlabeled pavatti question: «Yassa X V tassa Y V?» = «У кого V X, у того V Y?» (as G2's labeled frame)."""
    if not re.match(r"^(Yassa|Yattha) ", s):
        return None
    lab = "(Kha)" if s.startswith(("Yassa vā pana", "Yattha vā pana")) else "(Ka)"
    r = G2.pv_question_line(f"{lab} {lowfirst(s)}")
    return cap(_strip_label(r)) if r else None


REL_RU = {"yassa": "у кого", "yattha": "где", "yassa yattha": "у кого где"}   # G2 QREL
FRAG = re.compile(r"^(?:\((?P<lab>Ka|Kha)\) )?(?P<rel>[Yy]assa vā pana yattha|[Yy]assa yattha|[Yy]assa vā pana|"
                  r"[Yy]assa|[Yy]attha vā pana|[Yy]attha)(?: (?P<body>[^…]+?))?…pe…(?P<end>[?.]?)$")


def fragment(s):
    """«(Kha) yassa vā pana…pe…?» = «(б) А у кого…?»; «Yattha X V…pe….» = «Где V X…»; «(Kha) yassa vā pana X…pe…?»
    = «(б) А у кого X…?»; a final «…pe….» = «…» (never «….»)."""
    m = FRAG.match(s)
    if not m:
        return None
    rel = m.group("rel").lower()
    vp = " vā pana" in rel
    lead = REL_RU[rel.replace(" vā pana", "")]
    lead = f"А {lead}" if vp else lead
    if m.group("body"):
        sv = G2.parse_sv(m.group("body"))
        if sv:
            X = TERMS[sv[0]]
            lead += f" {G2.vru(*sv[1], X['g'])} {X['nom']}"
        else:
            k, i = G2.take_term(m.group("body").split(), 0)
            if not k or i != len(m.group("body").split()):
                return None
            lead += f" {TERMS[k]['nom']}"
    end = "…" + ("?" if m.group("end") == "?" else "")
    if m.group("lab"):
        if (m.group("lab") == "Kha") != vp:
            slip(f"label ({m.group('lab')}) on a fragment {'with' if vp else 'without'} «vā pana»; kept as written")
        if m.group("end") == ".":
            slip("abbreviated question «…pe….» ends with «.» instead of «?»; rendered «…» (the …pe…. rule)")
        return f"{S.LABEL['(' + m.group('lab') + ')']} {lead}{end}"
    return f"{cap(lead)}{end}"


def place_fragment(s):
    """«Dutiyajjhāne tatiyajjhāne tattha…pe…» = «Во втором и в третьем медитативном погружении…»."""
    m = re.match(rf"^((?:{_ploc()} )+)tattha…pe…$", s, re.I)
    return cap(place_list(m.group(1).split())) + "…" if m else None


# =========================================================================== editorial notes
YASSAKA = "раздел с «у кого»"           # Yassakampi (termbase)
YY = "раздел с «у кого где»"            # yassayatthakampi (termbase)
YY_LOC = "в разделе с «у кого где»"     # yassayatthake (termbase)
YATTHAKA = "раздел с «где»"             # Yatthakampi (termbase)
NIRODHA_WORD = "слова «у вошедших в медитативное достижение прекращения»"   # nirodhasamāpannānanti (-ti: quoted)
SAME = "тоже такие же"                  # -pi … sadisaṃ
EXPAND_SAME = "тоже следует развернуть так же"   # -pi … sadisaṃ vitthāretabbaṃ (G7 vitthāretabbaṃ «следует развернуть»)
NOT_FOUND = "не применяются"            # na labbhati
NOT_TO_USE = "использовать не следует"  # na kātabbaṃ
BOTH_FORMS = "и в утвердительной, и в отрицательной форме"   # anulomampi paccanīkampi (termbase)
NO_DIFF = "различий нет"                # natthi nānākaraṇaṃ
UPP, NIR = "в разделе о возникновении", "в разделе о прекращении"   # uppādavāre, nirodhavāre (termbase)
UPPNIR = "в разделе о возникновении и прекращении"                 # uppādanirodhavāre(pi), uppādavāranirodhavārepi
Q_PAST, Q_PP, Q_PF = "вопросы о прошлом", "вопросы о настоящем и прошлом", "вопросы о прошлом и будущем"  # pucchā
YY_PAIR = f"{cap(YASSAKA)} и {YY}"

NOTES = {
    "(Yassakampi yassayatthakampi sadisaṃ.)": f"({YY_PAIR} {SAME}.)",
    "(yassakampi yassayatthakampi sadisaṃ).": f"({YASSAKA} и {YY} {SAME}).",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na labbhati.)":
        f"({YY_PAIR} {EXPAND_SAME}, {YY_LOC} {NIRODHA_WORD} {NOT_FOUND}.)",
    "(Yassakampi yassayatthakampi sadisaṃ vitthāretabbaṃ, yassayatthake nirodhasamāpannānanti na kātabbaṃ.)":
        f"({YY_PAIR} {EXPAND_SAME}, {YY_LOC} {NIRODHA_WORD} {NOT_TO_USE}.)",
    "(Yassakampi yassayatthakampi sadisaṃ, yassayatthake nirodhasamāpannānanti na labbhati).":
        f"({YY_PAIR} {SAME}, {YY_LOC} {NIRODHA_WORD} {NOT_FOUND}).",
    "(Yatthakampi sabbattha ekasadisaṃ).": f"({cap(YATTHAKA)} тоже везде одинаков).",
    "(itaresaṃ yatthakānaṃ sadisaṃ).": "(так же, как в остальных разделах с «где»).",
    "(Atītā pucchā uppādavārepi nirodhavārepi uppādanirodhavārepi sadisaṃ vitthāretabbā).":
        f"({cap(Q_PAST)} и {UPP}, и {NIR}, и {UPPNIR} следует развернуть так же).",
    "(Yathā uppādavāre atītā pucchā yassakampi yassayatthakampi anulomampi paccanīkampi vibhattaṃ evaṃ "
    "nirodhavārepi vibhajitabbaṃ, natthi nānākaraṇaṃ.)":
        f"(Как {UPP} разобраны {Q_PAST} и в разделе с «у кого», и {YY_LOC}, {BOTH_FORMS}, так и {NIR} "
        f"следует разобрать, {NO_DIFF}.)",
    "(Yathā uppādavāre paccuppannātītā pucchā anulomampi paccanīkampi vibhattā evaṃ uppādavāranirodhavārepi "
    "paccuppannātītā pucchā anulomampi paccanīkampi vibhajitabbā.)":
        f"(Как {UPP} разобраны {Q_PP} {BOTH_FORMS}, так и {UPPNIR} следует разобрать {Q_PP} {BOTH_FORMS}.)",
    "(Yathā nirodhavāre atītānāgatā pucchā anulomampi paccanīkampi evaṃ uppādanirodhavārepi atītānāgatā pucchā "
    "anulomampi paccanīkampi vibhajitabbaṃ asammohantena nirodhavārena sadisaṃ, natthi nānākaraṇaṃ.)":
        f"(Как {NIR} {Q_PF} {BOTH_FORMS}, так и {UPPNIR} {Q_PF} {BOTH_FORMS} следует разобрать, не путаясь, "
        f"так же, как {NIR}, {NO_DIFF}.)",
    "(Yathā khandhayamake pariññāvāraṃ vibhattaṃ evaṃ saṅkhārayamakepi pariññāvāraṃ vibhajitabbaṃ.)":
        f"(Как в «{S.YAMAKA['Khandhayamakaṃ'].replace('Парные вопросы', 'Парных вопросах')}» разобран раздел о полном "
        f"понимании, так и в «{S.YAMAKA['Saṅkhārayamakaṃ'].replace('Парные вопросы', 'Парных вопросах')}» следует "
        f"разобрать раздел о полном понимании.)",
}

# =========================================================================== headings and closing labels
G2.HEAD.update({
    "suddhasaṅkhāravāro": "раздел о формирующих факторах как таковых",   # termbase Suddhasaṅkhāravāro
    "paccanīkaokāsā": "отрицательная форма по месту",                     # termbase paccanīkaokāsā
    "paccuppannavārādi": "раздел о настоящем и другие",                   # termbase Paccuppannavārādi
})
G2.COLO["paṇṇattivāro"] = cap("раздел об обозначениях")                 # Paṇṇattivāro (user heading)


# =========================================================================== fixed lines
def _fixed():
    ks = [TERMS[k]["nom"] for k in SANKHARA_KEYS]
    f = {
        "Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO,
        "Saṅkhārayamakaṃ niṭṭhitaṃ.": f"{S.YAMAKA['Saṅkhārayamakaṃ']} {S.DONE_PL}.",
        # uddesa (^6-6-1): tayo «три»; Assāsapassāsā, vitakkavicārā, saññā, vedanā, cittasampayuttakā (termbase)
        "Tayo saṅkhārā – kāyasaṅkhāro, vacīsaṅkhāro, cittasaṅkhāroti. Assāsapassāsā kāyasaṅkhāro, vitakkavicārā "
        "vacīsaṅkhāro, saññā ca vedanā ca cittasaṅkhāro. Ṭhapetvā vitakkavicāre sabbepi cittasampayuttakā dhammā "
        "cittasaṅkhāro.":
            f"Три формирующих фактора – {', '.join(ks)}. Вдохи и выдохи являются {TERMS['kāyasaṅkhāro']['ins']}, "
            f"направленная мысль и удержание мысли являются {TERMS['vacīsaṅkhāro']['ins']}, восприятие и чувство "
            f"являются {TERMS['cittasaṅkhāro']['ins']}. {G2.EXCEPT} направленной мысли и удержания мысли, все "
            f"явления, связанные с умом, являются {TERMS['cittasaṅkhāro']['ins']}.",
        # «(Kha) paccanīkaṃ» standing as a line (not a heading) at the end of ^6-6-2 / ^6-6-4
        "(Kha) paccanīkaṃ": f"{S.LABEL['(Kha)']} {cap(G2.HEAD['paccanīkaṃ'])}",
        # ^6-6-65: «4 (Ṅa) paccanīkaokāso» stands as a line (the heading marks «####» appear as «4»): as written
        "4 (Ṅa) paccanīkaokāso": f"4 {S.LABEL['(Ṅa)']} {cap(G2.HEAD['paccanīkaokāso'])}",
    }
    # ^6-6-10: variant after «avasesā saṅkhārā»
    a = translate_sentence("Vacīsaṅkhāro saṅkhāro ceva vacīsaṅkhāro ca.")
    b = translate_sentence("Avasesā saṅkhārā na vacīsaṅkhāro.")
    b = b.replace("Остальные формирующие факторы", "Остальные формирующие факторы "
                  + G2.var_br("avasesā saṅkhārā saṅkhārā", "sī. syā. kaṃ."), 1)
    f["Vacīsaṅkhāro saṅkhāro ceva vacīsaṅkhāro ca. Avasesā saṅkhārā [avasesā saṅkhārā saṅkhārā (sī. syā. kaṃ.)] "
      "na vacīsaṅkhāro."] = f"{a} {b}"
    # ^6-6-130 / ^6-6-131: fragment + note
    f["Dutiyajjhāne tatiyajjhāne tattha…pe… (itaresaṃ yatthakānaṃ sadisaṃ)."] = \
        place_fragment("Dutiyajjhāne tatiyajjhāne tattha…pe…") + " " + NOTES["(itaresaṃ yatthakānaṃ sadisaṃ)."]
    f["Yassa yattha kāyasaṅkhāro uppajjati…pe… (yassakampi yassayatthakampi sadisaṃ)."] = \
        fragment("Yassa yattha kāyasaṅkhāro uppajjati…pe…") + " " + NOTES["(yassakampi yassayatthakampi sadisaṃ)."]
    return f


FIXED = {}

# =========================================================================== sentence / line translator
G6_RULES = [fragment, pv_question, place_answer, person_answer]


def translate_sentence(s):
    s = s.strip()
    if s in NOTES:
        return NOTES[s]
    m = re.match(r"^(.+\?)…[Pp]e…\.?$", s)   # «…?…Pe….» = «…?…»
    if m:
        return translate_sentence(m.group(1)) + "…"
    for fn in G6_RULES:
        r = fn(s)
        if r:
            return r
    return G2.translate_sentence(s)


def split_sentences(pali):
    return re.split(r"(?<=[.?])\s+", pali.strip())


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian."""
    global FIXED
    if not FIXED:
        FIXED = _fixed()
    if pali.startswith("#"):
        return G2.heading(pali)
    if pali in FIXED:
        return FIXED[pali]
    return " ".join(translate_sentence(x) for x in split_sentences(pali))


# =========================================================================== build + checks
def render(pali_text):
    blocks, problems = [], []
    for sid, plines in S.segs(pali_text):
        _CUR["id"] = sid
        ru = []
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            r = translate_line(body)
            problems += S.check_line(sid, body, r)
            ru.append(r)
        ru[-1] = f"{ru[-1]} ^{sid}"
        blocks.append("\n".join(ru))
    return "\n\n".join(blocks) + "\n", problems


def probe(ch):
    bad = 0
    for sid, plines in S.segs((PALI / ch).read_text(encoding="utf-8")):
        _CUR["id"] = sid
        for i, pl in enumerate(plines):
            body = (S.ID.sub("", pl) if i == len(plines) - 1 else pl).strip()
            try:
                translate_line(body)
            except (ValueError, KeyError, AssertionError, TypeError) as e:
                bad += 1
                print(sid, "|", e)
    print(ch, "lines without a formula:", bad)


# strings reused unchanged from approved earlier Russian rails (asserted in main)
PI5_STRINGS = ["телесный формирующий фактор", "речевой формирующий фактор", "вдохи и выдохи",
               "направленная мысль и удержание мысли", "у вошедшего в первое погружение", "присутствует"]

# =========================================================================== notes (new recurring formulas)
NOTE_EXAMPLES = [
    "#### Suddhasaṅkhāravāro", "##### 1-6. Paccuppannavārādi", "##### (Ṅa) paccanīkaokāsā",
    "(Ka) kāyo kāyasaṅkhāro?", "(Kha) saṅkhārā vacīsaṅkhāro?", "(Ka) na cittaṃ na cittasaṅkhāro?",
    "Kāyasaṅkhāro na kāyo, kāyasaṅkhāro.", "Kāyañca kāyasaṅkhārañca ṭhapetvā avasesā na ceva kāyo na ca kāyasaṅkhāro.",
    "Vacīsaṅkhāro saṅkhāro ceva vacīsaṅkhāro ca.", "Avasesā saṅkhārā na vacīsaṅkhāro.",
    "Paṇṇattivāro.",
    "Vinā vitakkavicārehi assāsapassāsānaṃ uppādakkhaṇe tesaṃ kāyasaṅkhāro uppajjati, no ca tesaṃ vacīsaṅkhāro uppajjati.",
    "Paṭhamajjhānaṃ samāpannānaṃ kāmāvacarānaṃ assāsapassāsānaṃ uppādakkhaṇe tesaṃ kāyasaṅkhāro ca uppajjati "
    "vacīsaṅkhāro ca uppajjati.",
    "Sabbesaṃ cittassa bhaṅgakkhaṇe vinā assāsapassāsehi avitakkaavicāracittassa uppādakkhaṇe nirodhasamāpannānaṃ "
    "asaññasattānaṃ tesaṃ kāyasaṅkhāro ca nuppajjati vacīsaṅkhāro ca nuppajjati.",
    "Dutiyajjhāne tatiyajjhāne tattha kāyasaṅkhāro uppajjati, no ca tattha vacīsaṅkhāro uppajjati.",
    "Catutthajjhāne rūpāvacare arūpāvacare tattha cittasaṅkhāro uppajjati, no ca tattha kāyasaṅkhāro uppajjati.",
    "Dutiyajjhānaṃ tatiyajjhānaṃ catutthajjhānaṃ samāpannānaṃ suddhāvāsānaṃ dutiye citte vattamāne tesaṃ tattha "
    "cittasaṅkhāro uppajjittha, no ca tesaṃ tattha vacīsaṅkhāro uppajjittha.",
    "Yassa cittassa anantarā kāmāvacarānaṃ pacchimacittaṃ uppajjissati rūpāvacare arūpāvacare pacchimabhavikānaṃ ye ca "
    "rūpāvacaraṃ arūpāvacaraṃ upapajjitvā parinibbāyissanti tesaṃ cavantānaṃ tesaṃ vacīsaṅkhāro uppajjissati, no ca "
    "tesaṃ kāyasaṅkhāro uppajjissati.",
    "Yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati tesaṃ cittasaṅkhāro uppajjissati, no ca "
    "tesaṃ vacīsaṅkhāro uppajjissati.",
    "Pacchimacittasamaṅgīnaṃ yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati tesaṃ "
    "kāyasaṅkhāro ca nuppajjissati vacīsaṅkhāro ca nuppajjissati.",
    "Paṭhamajjhānaṃ samāpannānaṃ kāmāvacarānaṃ assāsapassāsānaṃ bhaṅgakkhaṇe tesaṃyeva vinā assāsapassāsehi cittassa "
    "uppādakkhaṇe rūpāvacarānaṃ arūpāvacarānaṃ tesaṃ tattha vacīsaṅkhāro uppajjittha, no ca tesaṃ tattha "
    "kāyasaṅkhāro uppajjati.",
    "Savitakkasavicārapacchimacittassa bhaṅgakkhaṇe avitakkaavicārapacchimacittasamaṅgīnaṃ tesaṃ vacīsaṅkhāro ca "
    "nuppajjati cittasaṅkhāro ca nuppajjissati.",
    "Kāmāvacare pacchimacittasamaṅgīnaṃ dutiyajjhānaṃ tatiyajjhānaṃ samāpannānaṃ tesaṃ tattha kāyasaṅkhāro "
    "uppajjittha, no ca tesaṃ tattha vacīsaṅkhāro uppajjissati.",
    "Savitakkasavicārabhūmiyaṃ pacchimacittasamaṅgīnaṃ tesaṃ tattha vacīsaṅkhāro uppajjittha, no ca tesaṃ tattha "
    "cittasaṅkhāro uppajjissati.",
    "Itaresaṃ savitakkasavicārabhūmiyaṃ tesaṃ tattha vacīsaṅkhāro ca uppajjittha cittasaṅkhāro ca uppajjissati.",
    "Avitakkaavicārabhūmiyaṃ tesaṃ tattha cittasaṅkhāro uppajjissati, no ca tesaṃ tattha vacīsaṅkhāro uppajjittha.",
    "Kāmāvacarānaṃ pacchimacittassa uppādakkhaṇe tesaṃ vacīsaṅkhāro nirujjhissati, no ca tesaṃ kāyasaṅkhāro "
    "nirujjhissati.",
    "Rūpāvacare arūpāvacare pacchimacittassa bhaṅgakkhaṇe asaññasattānaṃ tesaṃ tattha kāyasaṅkhāro ca na nirujjhittha "
    "cittasaṅkhāro ca na nirujjhissati.",
    "Yassa kāyasaṅkhāro uppajjittha tassa vacīsaṅkhāro nirujjhitthāti?",
    "Yassa yattha kāyasaṅkhāro uppajjati…pe….", "(Kha) yassa vā pana…pe…?", "(Kha) yassa vā pana yattha…pe…?",
    "(Kha) yattha vā pana…pe…?", "(Kha) yassa vā pana cittasaṅkhāro…pe…?",
    "(Ka) yo kāyasaṅkhāraṃ parijānāti so vacīsaṅkhāraṃ parijānātīti?",
]


def notes_md():
    L = ["# notes-rails-G6: Saṅkhārayamaka frames (6-01, 6-02)", "",
         "Format: Pāli = Russian, one per line. Builder: build_rails_G6_ru.py (importlib; importing writes nothing).",
         "Built on G2 (frames, person groups, headings) and G8 (moment phrases, nirodhasamāpanna). New here:",
         "the three formations, jhāna phrases, moment phrases with «vinā …», «yassa cittassa anantarā …», levels",
         "(bhūmi), «tesaṃyeva», «sabbesaṃ», «dutiye citte vattamāne», the intro joiner and the editorial notes.", "",
         "## Terms (termbase)", "",
         "kāyasaṅkhāro = телесный формирующий фактор (pi-5 same)",
         "vacīsaṅkhāro = речевой формирующий фактор (pi-5 same)",
         "cittasaṅkhāro = формирующий фактор ума (pi-6 termbase; pi-5 had «умственный формирующий фактор»)",
         "saṅkhāro / kāyo / vacī / cittaṃ (bare words) = формирующий фактор / тело / речь / ум",
         "X-jjhānaṃ samāpannānaṃ = у вошедших в первое / во второе / в третье / в четвёртое медитативное погружение;",
         "  several ordinals share one noun: «во второе и в третье медитативное погружение» (pi-5 «первое погружение»:",
         "  the pi-6 termbase jhāna = «медитативное погружение»); locative «в первом … медитативном погружении»",
         "vinā assāsapassāsehi / vitakkavicārehi = без вдохов и выдохов / без направленной мысли и удержания мысли",
         "  (after a moment; after a subject that already has «без …» it follows a comma)",
         f"yassa cittassa anantarā X-ānaṃ pacchimacittaṃ uppajjissati = у X(gen), у которых {ANANTARA} возникнет {LAST_MIND}",
         f"yassa cittassa anantarā avitakkaavicāraṃ pacchimacittaṃ uppajjissati = у тех, у кого {ANANTARA} возникнет "
         f"{LAST_MIND} {AVV}",
         f"tesaṃyeva = {SAME_THEY}; sabbesaṃ = {ALL}; dutiye citte vattamāne = {SECOND_MIND} (between commas)",
         "Savitakkasavicārabhūmiyaṃ / Avitakkaavicārabhūmiyaṃ = " + " / ".join(BHUMI.values()),
         "Intro joiner: a moment belongs to the person groups right before it (since the last moment, up to a",
         "  relative clause), joined «A и B» + moment («у вошедших в первое … и у существ … в момент …»); a clause",
         "  moment («, когда присутствует второй ум,») belongs to the last person only; units joined as G2 «A, B и C»;",
         "  «у них» only when no person is named; «tesaṃ tattha» after a person = «… там» (G2); after an intro naming",
         "  only a level or a placed moment, «tattha» is not rendered.", "",
         "## Lines", ""]
    L += [f"{p} = {translate_line(p)}" for p in NOTE_EXAMPLES]
    L += ["", "## Editorial notes", ""]
    L += [f"{p} = {r}" for p, r in NOTES.items()]
    L += [f"{p} = {r}" for p, r in _fixed().items() if p.startswith(("Dutiyajjhāne tatiyajjhāne tattha…pe…",
                                                                     "Yassa yattha kāyasaṅkhāro uppajjati…pe… ("))]
    return "\n".join(L) + "\n"


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--probe":
        for ch in sys.argv[2:]:
            probe(ch)
        return
    txt = (S.RU / "pi-5-russian-plain.md").read_text(encoding="utf-8")
    miss = [x for x in PI5_STRINGS if x not in txt]
    assert not miss, f"pi-5 strings not found: {miss}"
    problems = []
    for ch in CHAPTERS:
        pt = (PALI / ch).read_text(encoding="utf-8")
        ru, pr = render(pt)
        problems += pr
        e, n = S.check_file(pt, ru)
        problems += [f"{ch}: {x}" for x in e]
        (OUT / ch).write_text(ru, encoding="utf-8", newline="\n")
        print(f"wrote {ch}: {n} segments")
    slips = list(SLIPS)
    (S.RAILS / "notes-rails-G6.md").write_text(notes_md(), encoding="utf-8", newline="\n")
    print("wrote notes-rails-G6.md")
    for sid, note in dict.fromkeys(slips):
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
