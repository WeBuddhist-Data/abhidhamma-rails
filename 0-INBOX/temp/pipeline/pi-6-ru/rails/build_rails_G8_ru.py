"""pi-6 Yamaka: Russian RAILS builder, group G8 (8-cittayamaka). Frame-setter for the cittayamaka frames.

Later groups import it read-only; importing writes nothing:
    import sys, importlib; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru\\rails")
    G8 = importlib.import_module("build_rails_G8_ru")
    G8.pred_ru("uppajjati na nirujjhati"), G8.q_puggala(...), G8.translate_line(pali_line) ...
Run as a script (python -I -X utf8 -B build_rails_G8_ru.py) to write
AI_translation/russian/pi-6-russian-plain-rails_split_chapters/8-cittayamaka.md and run the per-line and whole-file checks.

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
Sample strings imported from build_rails_sample_ru (S). New recurring formulas: notes-rails-G8.md.
"""
import pathlib
import re
import sys

sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
import build_rails_sample_ru as S  # noqa: E402

CH = "8-cittayamaka.md"
cap = S.cap

# =========================================================================== verbs and predicates
# pali: (sg, pl, copular participle?)  termbase: uppajjati возникать, uppajjittha возникать (past), uppajjissati
# возникнуть; nirujjhati / nirujjhittha прекращаться, nirujjhissati прекратиться; uppannaṃ возникший,
# uppajjamānaṃ возникающий, nirujjhamānaṃ прекращающийся, niruddhaṃ прекратившийся.
# Participles are said with «является» (sample: «является благим»), so uppanna stays apart from the past tense.
VERB = {
    "uppajjati": ("возникает", "возникают", False),
    "nirujjhati": ("прекращается", "прекращаются", False),
    "uppajjittha": ("возникал", "возникали", False),
    "nirujjhittha": ("прекращался", "прекращались", False),
    "uppajjissati": ("возникнет", "возникнут", False),
    "nirujjhissati": ("прекратится", "прекратятся", False),
    "uppannaṃ": ("является возникшим", "являются возникшими", True),
    "uppajjamānaṃ": ("является возникающим", "являются возникающими", True),
    "nirujjhamānaṃ": ("является прекращающимся", "являются прекращающимися", True),
    "niruddhaṃ": ("является прекратившимся", "являются прекратившимися", True),
}
_V = "|".join(sorted(VERB, key=len, reverse=True))
P_RX = rf"(?:na )?(?:{_V})(?: (?:na )?(?:{_V}))?"   # one predicate or a «X na Y» pair


def vform(v, pl=False, neg=False):
    """'uppajjati' -> 'возникает'; neg -> 'не возникает'."""
    s = VERB[v][1 if pl else 0]
    return ("не " + s) if neg else s


def parse_pred(p):
    """'uppajjati na nirujjhati' -> [(False,'uppajjati'), (True,'nirujjhati')]"""
    toks, out, neg = p.split(), [], False
    for t in toks:
        if t == "na":
            neg = True
            continue
        assert t in VERB, (t, p)
        out.append((neg, t))
        neg = False
    return out


def pred_ru(p, pl=False, flip=False):
    """Predicate phrase -> Russian. A pair with one negated member is joined with «, но» (uppajjati na nirujjhati
    = «возникает, но не прекращается»). flip=True negates a single predicate (the «no ca» clause)."""
    items = parse_pred(p)
    if flip:
        assert len(items) == 1, p
        items = [(not items[0][0], items[0][1])]
    r = [vform(v, pl, n) for n, v in items]
    if len(r) == 2:
        assert items[0][0] != items[1][0], p
        return f"{r[0]}, но {r[1]}"
    return r[0]


def both_ru(x, y, pl=False):
    """«X ceva Y ca» (no relative clause) = «и X, и Y», the verb repeated (7-01 / sample rule)."""
    return f"и {pred_ru(x, pl)}, и {pred_ru(y, pl)}"


def neither_ru(x, y, pl=False):
    """«na ceva X na ca Y» = «ни X, ни Y» (coordinator negatives rule); two participles share one
    «не является / не являются ни A, ни B»."""
    vx, vy = VERB[x], VERB[y]
    if vx[2] and vy[2]:
        cop = "являются" if pl else "является"
        strip = lambda s: s.split(" ", 1)[1]  # noqa: E731
        return f"не {cop} ни {strip(vx[1 if pl else 0])}, ни {strip(vy[1 if pl else 0])}"
    return f"ни {vform(x, pl)}, ни {vform(y, pl)}"


# =========================================================================== minds (subjects)
CITTA = "ум"  # citta (pi-1 … pi-5; termbase)
# kinds of mind (termbase; the sixteen of the Suttanta list as pi-2 «понимает ум, охваченный страстью …»)
# (prefix?, Russian nominative): single adjectives before «ум», phrases after it with commas.
MIND = {
    "sarāgaṃ": (False, "охваченный страстью"), "vītarāgaṃ": (False, "свободный от страсти"),
    "sadosaṃ": (False, "охваченный злобой"), "vītadosaṃ": (False, "свободный от злобы"),
    "samohaṃ": (False, "охваченный заблуждением"), "vītamohaṃ": (False, "свободный от заблуждения"),
    "saṃkhittaṃ": (True, "сжатый"), "vikkhittaṃ": (True, "рассеянный"),
    "mahaggataṃ": (True, "возвышенный"), "amahaggataṃ": (True, "невозвышенный"),
    "sauttaraṃ": (False, "имеющий над собой высшее"), "anuttaraṃ": (False, "не имеющий над собой высшего"),
    "samāhitaṃ": (True, "сосредоточенный"), "asamāhitaṃ": (True, "несосредоточенный"),
    "vimuttaṃ": (True, "освобождённый"), "avimuttaṃ": (True, "неосвобождённый"),
    "kusalaṃ": (True, S.A("kusal", "m_nom")), "akusalaṃ": (True, S.A("akusal", "m_nom")),
    "abyākataṃ": (True, S.A("abyākat", "m_nom")),
    "sukhāya vedanāya sampayuttaṃ": (False, "связанный с приятным чувством"),  # pi-1 «связанные с приятным чувством»
    "araṇaṃ": (False, "свободный от борьбы"),
}
_M = "|".join(sorted((re.escape(k) for k in MIND), key=len, reverse=True))


def mind(adj=None):
    """'sarāgaṃ' -> 'ум, охваченный страстью,' ; 'kusalaṃ' -> 'благой ум' ; None -> 'ум'.
    A phrase after «ум» carries its closing comma, so the verb follows directly."""
    if not adj:
        return CITTA
    pre, ru = MIND[adj]
    return f"{ru} {CITTA}" if pre else f"{CITTA}, {ru},"


SARANA_ARANA_GEN = "сопряжённых с борьбой и свободных от борьбы"  # saraṇaaraṇā (termbase), genitive pl. after «вплоть до»

# =========================================================================== question frames (puggala / dhamma / puggaladhamma)
# yassa … tassa … = «У кого …, у того …?» (7-01, coordinator); yaṃ … taṃ … = «Какой ум …, тот ум …?»;
# yassa yaṃ … tassa taṃ … = «У кого какой ум …, у того тот ум …?» (the same correlative shape as 7-01's
# «У кого где …, у того там …?»); vā pana = «А …».
VA_PANA = "А "
KIND = {  # mode: (opening, resuming, the «no ca» resumer)
    "puggala": ("у кого {s}", "у того {s}", "у него {s}"),
    "dhamma": ("какой {s}", "тот {s}", "этот {s}"),
    "pd": ("у кого какой {s}", "у того тот {s}", "у него этот {s}"),
}


def question(mode, p1, p2, vapana=False, adj=None, p0=None):
    """mode puggala / dhamma / pd; p1, p2 Pāli predicates; p0 = the «no ca … P0» clause of the Atītānāgatavāra."""
    o, r, nc = KIND[mode]
    s = mind(adj)
    head = o.format(s=s) + " " + pred_ru(p1)
    if p0:
        head += f", но {nc.format(s=s)} {pred_ru(p0, flip=True)}"
    out = f"{head}, {r.format(s=s)} {pred_ru(p2)}?"
    return (VA_PANA + out) if vapana else cap(out)


def q_bare(p1, p2):
    """(12)/(13) 'uppannaṃ uppajjamānaṃ?' = «То, что является возникшим, является возникающим?»"""
    return f"То, что {pred_ru(p1)}, {pred_ru(p2)}?"


# Atikkantakālavāra: «uppajjamānaṃ khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ» = «миновал момент возникновения,
# этот момент, и время его прошло» (APPROVED: the noun «момент возникновения / прекращения» stays; the second
# khaṇaṃ = «этот момент», aṭṭhakathā «tameva uppādakkhaṇaṃ vītikkantaṃ»; atikkantakāla = «время его прошло»).
MOMENT = {"uppajjamānaṃ": "момент возникновения", "nirujjhamānaṃ": "момент прекращения"}


def passed(part, neg=False):
    if neg:
        return f"не миновал {MOMENT[part]}, этот момент, и время его не прошло"
    return f"миновал {MOMENT[part]}, этот момент, и время его прошло"


TAKOV = {"puggala": "у того ум таков", "dhamma": "тот ум таков", "pd": "у того тот ум таков"}  # tassa / taṃ cittaṃ?


def q_passed(mode, first, second, neg, vapana=False):
    o = KIND[mode][0].format(s=CITTA)
    out = f"{o} {passed(first, neg)}, {passed(second, neg)}, {TAKOV[mode]}?"
    return (VA_PANA + out) if vapana else cap(out)


# =========================================================================== answers
YES = S.YES                     # Āmantā. = Да. (pi-5; user)
NO = "Нет."                     # No. (pi-5; coordinator)
NATTHI = "Такого нет."          # Natthi. (termbase; coordinator)
SHORT = {f"{cap(v)}.": cap(VERB[v][0]) + "." for v in VERB}   # Uppajjittha. = Возникал.  Uppannaṃ. = Является возникшим.
SHORT.update({"Āmantā.": YES, "No.": NO, "Natthi.": NATTHI})

# person / time intros of the puggalavāra (shared phrases: uppādakkhaṇe / bhaṅgakkhaṇe «в момент возникновения /
# распада»; nirodhasamāpanna «вошедшие в медитативное достижение прекращения»; asaññasatta «существа без восприятия»
# pi-5; Itaresaṃ «У остальных»; «у них» only when no person is named: coordinator).
NIRODHA_ASANNA = "у вошедших в медитативное достижение прекращения и у существ без восприятия"
INTRO = {  # pali intro (before «tesaṃ»): (Russian, names a person?)
    "Pacchimacittassa uppādakkhaṇe": ("в момент возникновения последнего ума", False),
    "Pacchimacittassa bhaṅgakkhaṇe": ("в момент распада последнего ума", False),
    "Cittassa uppādakkhaṇe": ("в момент возникновения ума", False),
    "Cittassa bhaṅgakkhaṇe": ("в момент распада ума", False),
    "Itaresaṃ cittassa uppādakkhaṇe": ("у остальных в момент возникновения ума", True),
    "Itaresaṃ cittassa bhaṅgakkhaṇe": ("у остальных в момент распада ума", True),
    "Nirodhasamāpannānaṃ asaññasattānaṃ": (NIRODHA_ASANNA, True),
    "Cittassa bhaṅgakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ": (f"в момент распада ума, {NIRODHA_ASANNA}", True),
    "Cittassa uppādakkhaṇe nirodhasamāpannānaṃ asaññasattānaṃ": (f"в момент возникновения ума, {NIRODHA_ASANNA}", True),
    "Pacchimacittasamaṅgīnaṃ": ("у обладающих последним умом", True),
    "Itaresaṃ": ("у остальных", True),
    "Cittasamaṅgīnaṃ": ("у обладающих умом", True),
    "Itaresaṃ cittasamaṅgīnaṃ": ("у остальных обладающих умом", True),
    "Sarāgapacchimacittassa uppādakkhaṇe": ("в момент возникновения последнего ума, охваченного страстью,", False),
    "Itaresaṃ sarāgacittassa uppādakkhaṇe": ("у остальных в момент возникновения ума, охваченного страстью", True),
    "Pacchimakusalacittassa uppādakkhaṇe": (f"в момент возникновения последнего {S.A('kusal', 'mn_gen')} ума", False),
    "Itaresaṃ kusalacittassa uppādakkhaṇe": (f"у остальных в момент возникновения {S.A('kusal', 'mn_gen')} ума", True),
}
_I = "|".join(sorted((re.escape(k) for k in INTRO), key=len, reverse=True))
THEY = "у них"     # tesaṃ (no person named)

# dhammavāra subjects (times of the mind): Russian nominative, plural?
TIME_NP = {
    "Bhaṅgakkhaṇe cittaṃ": ("ум в момент распада", False),
    "Uppādakkhaṇe cittaṃ": ("ум в момент возникновения", False),
    "Atītaṃ cittaṃ": ("прошлый ум", False),
    "Anāgataṃ cittaṃ": ("будущий ум", False),
    "Paccuppannaṃ cittaṃ": ("настоящий ум", False),
    "Atītānāgataṃ cittaṃ": ("прошлый и будущий ум", False),
    "Bhaṅgakkhaṇe anāgataṃ ca cittaṃ": ("ум в момент распада и будущий ум", True),
    "Bhaṅgakkhaṇe atītaṃ ca cittaṃ": ("ум в момент распада и прошлый ум", True),
    "Uppādakkhaṇe anāgataṃ ca cittaṃ": ("ум в момент возникновения и будущий ум", True),
    "Bhaṅgakkhaṇe": ("в момент распада оно", False),         # (12)/(13): no subject in the Pāli
    "Uppādakkhaṇe": ("в момент возникновения оно", False),
}
_T = "|".join(sorted((re.escape(k) for k in TIME_NP), key=len, reverse=True))
RESUME = {"tesaṃ cittaṃ": ("у них ум", "у них ум"), "taṃ cittaṃ": ("этот ум", "эти умы"),
          "tassa taṃ cittaṃ": ("у него этот ум", "у него эти умы"), "": ("", "")}


# =========================================================================== headings (ru-zeroshot-terms.md, user-approved)
HEAD = {
    "Cittayamakaṃ": S.YAMAKA["Cittayamakaṃ"],
    "uddeso": S.UDDESO, "niddeso": S.NIDDESO,
    "Suddhacittasāmaññaṃ": "Ум вообще", "Suddhacittasāmañña": "Ум вообще",
    "Puggalavāro": "Раздел о личности", "Dhammavāro": "Раздел о явлениях",
    "Puggaladhammavāro": "Раздел о личности и явлениях",
    "Uppādanirodhakālasambhedavāro": "Раздел о смешении времени возникновения и прекращения",
    "Uppāduppannavāro": "Раздел о возникновении и возникшем",
    "Nirodhuppannavāro": "Раздел о прекращении и возникшем",
    "Uppādavāro": "Раздел о возникновении", "Nirodhavāro": "Раздел о прекращении",
    "Uppādanirodhavāro": "Раздел о возникновении и прекращении",
    "Uppajjamāna-nanirodhavāro": "Раздел о возникающем и непрекращающемся",
    "Uppajjamānananirodhavāro": "Раздел о возникающем и непрекращающемся",
    "Uppajjamānuppannavāro": "Раздел о возникающем и возникшем",
    "Nirujjhamānuppannavāro": "Раздел о прекращающемся и возникшем",
    "Uppannuppādavāro": "Раздел о возникшем и возникновении",
    "Atītānāgatavāro": "Раздел о прошлом и будущем",
    "Uppannuppajjamānavāro": "Раздел о возникшем и возникающем",
    "Niruddhanirujjhamānavāro": "Раздел о прекратившемся и прекращающемся",
    "Atikkantakālavāro": "Раздел о прошедшем времени",
    "Suttantacittamissakaviseso": "Особенность ума из наставлений в смешении",
    "Abhidhammacittamissakaviseso": "Особенность ума из Абхидхаммы в смешении",
}


def head_body(body):
    """'(Ka) uddeso' -> '(а) Перечень'; '(7) Uppajjamāna-nanirodhavāro' -> '(7) Раздел о …' (capital after a label)."""
    out = []
    for p in re.split(r"(\([^)]+\))", body):
        p = p.strip()
        if not p:
            continue
        if p in S.LABEL:
            out.append(S.LABEL[p])
        elif re.fullmatch(r"\(\d+\)", p):
            out.append(p)
        else:
            out.append(cap(HEAD[p]))
    return " ".join(out)


def heading(text):
    hashes, body = text.split(" ", 1)
    return f"{hashes} {head_body(body)}"


# =========================================================================== one-off lines and sentences
_PASSED_A = ("Ум в момент распада миновал момент возникновения, но не миновал момент распада, прошлый ум "
             "и миновал момент возникновения, и миновал момент распада.")
FIXED = {
    # (14) answers; ^6-8-83 writes «vītakkantaṃ» for vītikkantaṃ (spelling slip, rendered as meant)
    "Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītakkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca "
    "vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ.": _PASSED_A,
    "Bhaṅgakkhaṇe cittaṃ uppādakkhaṇaṃ vītikkantaṃ bhaṅgakkhaṇaṃ avītikkantaṃ, atītaṃ cittaṃ uppādakkhaṇañca "
    "vītikkantaṃ bhaṅgakkhaṇañca vītikkantaṃ.": _PASSED_A,
    "Atītaṃ cittaṃ.": "Прошлый ум.",
    # «Uppādakkhaṇe anāgataṃ cittaṃ.» without «ca» (as written: an asyndetic pair, the comma rendered)
    "Uppādakkhaṇe anāgataṃ cittaṃ.": "Ум в момент возникновения, будущий ум.",
    # missing comma before «no ca» rendered (missing punctuation); denied negative said plainly (coordinator)
    "Bhaṅgakkhaṇe cittaṃ bhaṅgakkhaṇaṃ avītikkantaṃ no ca uppādakkhaṇaṃ avītikkantaṃ, uppādakkhaṇe anāgatañca "
    "cittaṃ bhaṅgakkhaṇañca avītikkantaṃ uppādakkhaṇañca avītikkantaṃ.":
        "Ум в момент распада не миновал момент распада, но миновал момент возникновения, ум в момент возникновения "
        "и будущий ум не миновали ни момент распада, ни момент возникновения.",
    "(14) Atikkantakālavāro": "(14) " + HEAD["Atikkantakālavāro"],   # not a heading in the source (^6-8-82)
    "(Etena upāyena yāva saraṇaaraṇā uddharitabbā.)":
        f"(Этим способом их следует излагать вплоть до {SARANA_ARANA_GEN}.)",
    "(Yassa cittake sakabhāvena niddiṭṭhe, yaṃ cittake ca yassa yaṃ cittake ca ekattena niddiṭṭhe.)":
        "(В разделе с «у кого ум» разъяснено по собственной природе, а в разделе с «какой ум» и в разделе "
        "с «у кого какой ум» разъяснено как одно.)",
    "(Mūlayamakaṃ cittayamakaṃ dhammayamakanti tīṇi yamakāni yāva saraṇaaraṇā gacchanti.)":
        f"(«{S.YAMAKA['Mūlayamakaṃ']}», «{S.YAMAKA['Cittayamakaṃ']}» и «{S.YAMAKA['Dhammayamakaṃ']}»: "
        f"эти три части доходят вплоть до {SARANA_ARANA_GEN}.)",
    "Cittayamakaṃ niṭṭhitaṃ.": f"{S.YAMAKA['Cittayamakaṃ']} {S.DONE_PL}.",
}
FIXED_S = {  # single sentences of abbreviated lines
    "Yassa vā pana…pe…?": "А у кого…?",
    "Āmantā …pe….": "Да…",
}

# =========================================================================== sentence translator
SLIPS = []
_CUR = {"id": None}


def norm(s):
    """Quotation -ti dropped before «?» (uppajjatīti? -> uppajjati?, uppannanti? -> uppannaṃ?,
    uppajjitthāti? -> uppajjittha?); -ñceva / -ñca split (uppannañceva -> uppannaṃ ceva)."""
    s = re.sub(r"īti\?$", "i?", s)
    s = re.sub(r"āti\?$", "a?", s)
    s = re.sub(r"nti\?$", "ṃ?", s)
    s = re.sub(r"ñ(ceva|ca)\b", r"ṃ \1", s)
    return s


def pred_any(pr, pl=False):
    """Any answer predicate: single, «X na Y» pair, «X ceva Y ca», «na ceva X na ca Y», or two joined by a comma."""
    m = re.fullmatch(rf"na ceva ({_V}) na ca ({_V})", pr)
    if m:
        return neither_ru(m.group(1), m.group(2), pl)
    m = re.fullmatch(rf"((?:na )?(?:{_V})) ceva ({_V}) ca", pr)
    if m:
        return both_ru(m.group(1), m.group(2), pl)
    if ", " in pr:
        a, b = pr.split(", ", 1)
        return f"{pred_any(a, pl)}, {pred_any(b, pl)}"
    assert re.fullmatch(P_RX, pr), pr
    return pred_ru(pr, pl)


ANS = re.compile(
    rf"^(?:(?P<intro>{_I}) tesaṃ (?:(?P<adj>{_M}) )?cittaṃ|(?P<time>{_T})) (?P<pr>.+?)"
    rf"(?:, no ca (?P<res>(?:tesaṃ cittaṃ|tassa taṃ cittaṃ|taṃ cittaṃ) )?(?P<p0>{P_RX}))?\.$")
Q_ROW = re.compile(  # puggala / dhamma / puggaladhamma questions, incl. the Atītānāgatavāra «no ca» clause
    rf"^(?P<y>yassa|yaṃ) (?P<vp>vā pana )?(?P<yam>yaṃ )?(?:(?P<adj>{_M}) )?cittaṃ (?P<p1>{P_RX})"
    rf"(?: no ca (?:tassa |taṃ |tassa taṃ )?cittaṃ (?P<p0>{P_RX}),)?"
    rf" (?:tassa |taṃ |tassa taṃ )(?:(?P<adj2>{_M}) )?cittaṃ (?P<p2>{P_RX})\?$", re.I)
Q_BARE = re.compile(rf"^((?:na )?(?:{_V})) ((?:na )?(?:{_V}))\?$")
_KK = "khaṇaṃ khaṇaṃ vītikkantaṃ atikkantakālaṃ"
Q_PASSED = re.compile(
    rf"^(?P<y>yassa|yaṃ) (?P<vp>vā pana )?(?P<yam>yaṃ )?cittaṃ (?P<n1>na )?(?P<a>uppajjamānaṃ|nirujjhamānaṃ) {_KK}, "
    rf"(?P<n2>na )?(?P<b>uppajjamānaṃ|nirujjhamānaṃ) {_KK} (?:tassa cittaṃ|taṃ cittaṃ|tassa taṃ cittaṃ)\?$")
Q_LIST = re.compile(rf"^[Yy]assa (?P<adj>{_M}) cittaṃ uppajjati$")
ABBR = re.compile(rf"^Yassa (?P<adj>{_M}) cittaṃ (?P<p>{P_RX})…pe…\.$")
INTRO_PE = re.compile(rf"^(?P<intro>{_I}) tesaṃ…pe…\.$")


def _mode(g):
    if g["y"].lower() == "yaṃ":
        return "dhamma"
    return "pd" if g["yam"] else "puggala"


def np_ru(g):
    """Answer subject -> (Russian, plural?)."""
    if g["intro"]:
        ru, person = INTRO[g["intro"]]
        return (f"{ru} {mind(g['adj'])}" if person else f"{ru} {THEY} {mind(g['adj'])}"), False
    return TIME_NP[g["time"]]


def answer(s):
    m = ANS.match(s)
    if not m:
        return None
    g = m.groupdict()
    subj, pl = np_ru(g)
    out = f"{subj} {pred_any(g['pr'], pl)}"
    if g["p0"]:
        res = RESUME[(g["res"] or "").strip()][1 if pl else 0]
        out += ", но " + (f"{res} " if res else "") + pred_ru(g["p0"], pl, flip=True)
    return cap(out) + "."


def q_list(line):
    """Uddesa lists «Yassa sarāgaṃ cittaṃ uppajjati…pe… yassa … uppajjati…?»"""
    if not line.endswith("…?"):
        return None
    pieces = [p for p in re.split(r"\s*…(?:pe…)?\s*", line[:-1]) if p]
    ms = [Q_LIST.match(p) for p in pieces]
    if not all(ms):
        return None
    if re.search(r" …", line):
        SLIPS.append((_CUR["id"], "a space before «…» in the Pāli; «…» glued to the word (house rule)"))
    return cap("… ".join(f"у кого {mind(m['adj'])} {vform('uppajjati')}" for m in ms) + "…?")


def translate_sentence(s):
    if s in FIXED_S:
        return FIXED_S[s]
    if s in SHORT:
        return SHORT[s]
    lab = ""
    m = re.match(r"^(\((?:Ka|Kha)\)) (.*)$", s)
    if m:
        lab, s = S.LABEL[m.group(1)] + " ", m.group(2)
    n = norm(s)
    m = Q_ROW.match(n)
    if m:
        g = m.groupdict()
        assert (g["adj"] or "") == (g["adj2"] or ""), s
        return lab + question(_mode(g), g["p1"], g["p2"], bool(g["vp"]), g["adj"], g["p0"])
    m = Q_PASSED.match(n)
    if m:
        g = m.groupdict()
        assert bool(g["n1"]) == bool(g["n2"]) and g["a"] != g["b"], s
        return lab + q_passed(_mode(g), g["a"], g["b"], bool(g["n1"]), bool(g["vp"]))
    m = Q_BARE.match(n)
    if m:
        return lab + q_bare(m.group(1), m.group(2))
    r = answer(n)
    if r:
        return lab + r
    m = ABBR.match(s)
    if m:
        return lab + f"У кого {mind(m['adj'])} {pred_ru(m['p'])}…"
    m = INTRO_PE.match(s)
    if m:
        ru, person = INTRO[m["intro"]]
        return lab + cap(ru if person else f"{ru} {THEY}") + "…"
    raise ValueError(f"no formula for: {s!r} (segment {_CUR['id']})")


def translate_line(pali):
    """One Pāli line (without its ^id) -> Russian."""
    if pali.startswith("#"):
        return heading(pali)
    if pali in FIXED:
        if "vītakkantaṃ" in pali:
            SLIPS.append((_CUR["id"], "vītakkantaṃ for vītikkantaṃ: spelling slip, rendered as meant"))
        if pali.startswith("Bhaṅgakkhaṇe cittaṃ bhaṅgakkhaṇaṃ avītikkantaṃ no ca"):
            SLIPS.append((_CUR["id"], "missing comma before «no ca»: rendered with the comma"))
        if pali == "Uppādakkhaṇe anāgataṃ cittaṃ.":
            SLIPS.append((_CUR["id"], "«Uppādakkhaṇe anāgataṃ cittaṃ» lacks the «ca» of the parallel answers "
                                      "(aṭṭhakathā: «uppādakkhaṇe cittaṃ anāgataṃ cittaṃ», two minds): as written, "
                                      "an asyndetic pair with a comma"))
        return FIXED[pali]
    r = q_list(pali)
    if r:
        return r
    return " ".join(translate_sentence(x) for x in re.split(r"(?<=[.?])\s+(?=[(A-ZĀĪŪṬḌṆÑṄa-zāīūṭḍṇñṅ])", pali.strip()))


# =========================================================================== build + checks
def render(pali_text):
    blocks, problems = [], []
    for sid, plines in S.segs(pali_text):
        _CUR["id"] = sid
        ru = []
        for i, pl in enumerate(plines):
            body = S.ID.sub("", pl) if i == len(plines) - 1 else pl
            r = translate_line(body.strip())
            problems += S.check_line(sid, body.strip(), r)
            ru.append(r)
        ru[-1] = f"{ru[-1]} ^{sid}"
        blocks.append("\n".join(ru))
    return "\n\n".join(blocks) + "\n", problems


PI_STRINGS = {  # strings reused unchanged from earlier approved Russian rails (asserted in main)
    "pi-2": ["ум, охваченный страстью", "ум, свободный от страсти", "ум, охваченный злобой", "ум, свободный от злобы",
             "ум, охваченный заблуждением", "ум, свободный от заблуждения", "сжатый ум", "рассеянный ум",
             "возвышенный ум", "невозвышенный ум", "ум, имеющий над собой высшее", "ум, не имеющий над собой высшего",
             "сосредоточенный ум", "несосредоточенный ум", "освобождённый ум", "неосвобождённый ум"],
    "pi-1": ["связанные с приятным чувством"],
    "pi-5": ["В момент возникновения", "в момент распада", "вошёл в медитативное достижение прекращения",
             "У существ без восприятия", "? Да.", "? Нет."],
}


def main():
    probe = "--probe" in sys.argv
    for book, lst in PI_STRINGS.items():
        txt = (S.RU / f"{book}-russian-plain.md").read_text(encoding="utf-8")
        miss = [x for x in lst if x not in txt]
        assert not miss, f"{book} strings not found: {miss}"
    pt = (S.PALI / CH).read_text(encoding="utf-8")
    ru, problems = render(pt)
    e, n = S.check_file(pt, ru)
    problems += [f"{CH}: {x}" for x in e]
    if not probe:
        (S.OUT / CH).write_text(ru, encoding="utf-8", newline="\n")
        print(f"wrote {CH}: {n} segments")
    for sid, note in dict.fromkeys(SLIPS):
        print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
