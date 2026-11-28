"""pi-6 Yamaka: Russian RAILS builder for group G7 (Anusayayamaka, 7-01 … 7-11). Frame-setter for the anusaya frames.

Later groups import it read-only; importing writes nothing:
    import sys; sys.path.insert(0, r"D:\\Work\\OpenPecha\\abhidhamma-rails\\0-INBOX\\temp\\pipeline\\pi-6-ru\\rails")
    import importlib; G7 = importlib.import_module("build_rails_G7_ru")
    G7.np_ru(...), G7.vp(...), G7.question(...), G7.answer(...), G7.PERSON, G7.PLACE_RU, G7.REL_RU, G7.CORR_RU ...
Run as a script (python -I -X utf8 -B build_rails_G7_ru.py [ch ...]) to write the chapter files and run the checks.

Termbase (locked): AI_translation/russian/pi-6-pali-russian-termbase-plain.md + pi-6-ru/termbase/APPROVED.md.
Shared strings: build_rails_sample_ru.py (S): LABEL, YAMAKA, NAMO, check_line, segs, check_file.
Translated from the Pāli; English / Hindi pi-6 rails used as a cross-check of structure only.
New recurring frames: notes-rails-G7.md.
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-6-ru\rails")
if str(RAILS) not in sys.path:
    sys.path.insert(0, str(RAILS))
import build_rails_sample_ru as S  # noqa: E402

PALI = S.PALI
OUT = S.OUT
CHAPTERS = [f"7-{i:02d}-anusayayamaka.md" for i in range(1, 12)]
cap = S.cap
SLIPS = []          # (segment id, note)
_CUR = {"id": None, "okasa": False, "ref_pl": False}


def slip(note):
    SLIPS.append((_CUR["id"], note))


# =========================================================================== the seven tendencies (termbase; pi-2, pi-5)
ANU = {  # Pāli stem -> object of «скрытая склонность к …»
    "kāmarāg": "чувственной страсти", "paṭigh": "неприязни", "mān": "самомнению", "diṭṭh": "воззрениям",
    "vicikicch": "колебанию", "bhavarāg": "страсти к существованию", "avijj": "неведению",
}
SPELL = {"kāmārāg": "kāmarāg"}   # spelling slips rendered as meant
HEAD = {"sg": {"nom": "скрытая склонность", "acc": "скрытую склонность", "gen": "скрытой склонности",
               "prep": "скрытой склонности"},
        "pl": {"nom": "скрытые склонности", "acc": "скрытые склонности", "gen": "скрытых склонностей",
               "prep": "скрытых склонностях"}}
GAP = None
AN_STEM = r"(?:kāmarāg|kāmārāg|paṭigh|mān|diṭṭh|vicikicch|bhavarāg|avijj)"
AN = AN_STEM + r"ānusay(?:o|ena|aṃ|añca)"
NP = rf"{AN}(?:\s+ca)?(?:(?:\s*…pe…\s*|\s+){AN}(?:\s+ca)?)*"


class NPh:
    """A tendency phrase: items (stems or GAP), kind single / list / range, has_ca."""

    def __init__(self, text):
        self.items, self.has_ca = [], False
        for m in re.finditer(rf"({AN_STEM})ānusay(o|ena|aṃ|añca)|(…pe…)|(?<!\S)(ca)(?!\S)", text):
            if m.group(1):
                st = m.group(1)
                if st in SPELL:
                    slip(f"spelling {st}ānusaya- for {SPELL[st]}ānusaya- (rendered as meant)")
                    st = SPELL[st]
                self.items.append(st)
                if m.group(2) == "añca":
                    self.has_ca = True
            elif m.group(3):
                self.items.append(GAP)
            else:
                self.has_ca = True
        n = len([i for i in self.items if i is not GAP])
        assert n >= 1, text
        self.kind = "single" if n == 1 and GAP not in self.items else ("list" if self.has_ca and n > 1 else
                                                                        ("range" if GAP in self.items else "single"))
        if n > 1 and not self.has_ca and GAP not in self.items:
            raise ValueError(f"list without ca: {text!r}")

    @property
    def plural(self):
        return self.kind == "list"

    def objs(self):
        return [GAP if i is GAP else f"к {ANU[i]}" for i in self.items]


def join_items(objs, conj="и"):
    """['к A', 'к B', 'к C'] -> 'к A, к B и к C'; GAP (…pe…) -> '…' glued: 'к A… и к F'."""
    real = [i for i, o in enumerate(objs) if o is not GAP]
    out, prev_gap = "", False
    for k, i in enumerate(real):
        o = objs[i]
        if k == 0:
            out = o
        else:
            gap = any(objs[j] is GAP for j in range(real[k - 1] + 1, i))
            last = k == len(real) - 1
            sep = "… " if gap else ", "
            if last and conj and len(real) > 1:
                sep = ("… " if gap else " ") + f"{conj} "
            out += sep + o
    if objs[-1] is GAP:
        out += "…"
    return out


def np_ru(np, case):
    """«скрытая склонность к X» in a case; lists «скрытые склонности к A, к B и к C»; ranges «… к A… к B»."""
    if np.kind == "list":
        return f"{HEAD['pl'][case]} {join_items(np.objs())}"
    if np.kind == "range":
        return f"{HEAD['sg'][case]} {join_items(np.objs(), conj=None)}"
    return f"{HEAD['sg'][case]} {np.objs()[0]}"


# =========================================================================== verbs (termbase)
# mode: anu anuseti «залегать»; upp uppajjati «возникать»; pah pahīno «устранённый»;
#       paj pajahati «устранять»; par parijānāti «полностью понимать»; san sānusaya / niranusaya «иметь / не иметь»
VRU = {
    "anu": {"+": ("залегает", "залегают"), "-": ("не залегает", "не залегают")},
    "upp": {"+": ("возникает", "возникают"), "-": ("не возникает", "не возникают")},
    "pah": {"+": ("устранена", "устранены"), "-": ("не устранена", "не устранены")},
    "paj": {"+": ("устраняет", "устраняют"), "-": ("не устраняет", "не устраняют")},
    "par": {"+": ("полностью понимает", "полностью понимают"), "-": ("не понимает полностью", "не понимают полностью")},
    "san": {"+": ("имеет", "имеют"), "-": ("не имеет", "не имеют")},
}
TRANS = {"paj", "par", "san"}
OBJ_CASE = {("paj", "+"): "acc", ("paj", "-"): "acc", ("par", "+"): "acc", ("par", "-"): "acc",
            ("san", "+"): "acc", ("san", "-"): "gen"}   # negated иметь: genitive
VP = {
    "anuseti": ("anu", "+", "sg"), "anusenti": ("anu", "+", "pl"), "nānuseti": ("anu", "-", "sg"),
    "nānusenti": ("anu", "-", "pl"), "anusanti": ("anu", "+", "pl"),
    "uppajjati": ("upp", "+", "sg"), "uppajjanti": ("upp", "+", "pl"), "nuppajjati": ("upp", "-", "sg"),
    "nuppajjanti": ("upp", "-", "pl"),
    "pahīno": ("pah", "+", "sg"), "pahīnā": ("pah", "+", "pl"), "appahīno": ("pah", "-", "sg"),
    "appahīnā": ("pah", "-", "pl"),
    "pajahati": ("paj", "+", "sg"), "pajahanti": ("paj", "+", "pl"), "nappajahati": ("paj", "-", "sg"),
    "nappajahanti": ("paj", "-", "pl"),
    "parijānāti": ("par", "+", "sg"), "parijānanti": ("par", "+", "pl"), "na parijānāti": ("par", "-", "sg"),
    "na parijānanti": ("par", "-", "pl"),
    "sānusayo": ("san", "+", "sg"), "sānusayā": ("san", "+", "pl"), "niranusayo": ("san", "-", "sg"),
    "niranusayā": ("san", "-", "pl"),
}
VRX = "(?:" + "|".join(sorted(map(re.escape, VP), key=len, reverse=True)) + ")"
TAD = {"sg": "пребывающую вместе с {r}", "pl": "пребывающие вместе с {r}"}   # tadekaṭṭha (pi-2 «пребывающий вместе с ним»)


def verb(mode, pol, num):
    return VRU[mode][pol][0 if num == "sg" else 1]


class Grp:
    def __init__(self, np, tad, v):
        self.np, self.tad = NPh(np), bool(tad)
        if v == "anusanti":
            slip("anusanti for anusenti (spelling, rendered as meant)")
        self.mode, self.pol, self.vnum = VP[v]


GROUP = re.compile(rf"\s*,?\s*(?P<np>{NP})\s+(?P<tad>tadekaṭṭhaṃ\s+)?(?P<v>{VRX})(?=\s|$|,)")


def parse_groups(s):
    s = s.strip()
    gs, pos = [], 0
    while pos < len(s):
        m = GROUP.match(s, pos)
        if not m:
            raise ValueError(f"cannot parse clause {s[pos:]!r} (segment {_CUR['id']})")
        if gs and s[pos:m.start('np')].strip() == "," and not m.group("tad"):
            slip("stray comma between the two members of an «X ca … Y ca …» pair (Russian commas as usual)")
        gs.append(Grp(m.group("np"), m.group("tad"), m.group("v")))
        pos = m.end()
    return gs


def tad_ru(np, ref_pl):
    """participle after the object: «…, пребывающую вместе с ней» (referent = the first tendency of the clause)."""
    return TAD["pl" if np.plural else "sg"].format(r="ними" if ref_pl else "ней")


TAD_ALONE = {("sg", "sg"): "ту, что пребывает вместе с ней", ("sg", "pl"): "ту, что пребывает вместе с ними",
             ("pl", "sg"): "те, что пребывают вместе с ней", ("pl", "pl"): "те, что пребывают вместе с ними"}


def tadekattha(g):
    """Tadekaṭṭhaṃ pajahati / parijānāti (answer alone): «Устраняет ту, что пребывает вместе с ней.»
    «ту / те» = the tendency asked about (second half of the question), «с ней / с ними» = the first half."""
    num = "pl" if _CUR["okasa"] else "sg"
    key = ("pl" if _CUR.get("obj_pl") else "sg", "pl" if _CUR["ref_pl"] else "sg")
    return cap(f"{verb(g[0], g[1], num)} {TAD_ALONE[key]}")


def vp(g, subj_num, pol=None, ref_pl=False):
    """One group: «залегает скрытая склонность к X» / «устраняет скрытую склонность к X» (pol may be flipped)."""
    pol = pol or g.pol
    if g.mode in TRANS:
        out = f"{verb(g.mode, pol, subj_num)} {np_ru(g.np, OBJ_CASE[(g.mode, pol)])}"
    else:
        out = f"{verb(g.mode, pol, 'pl' if g.np.plural else 'sg')} {np_ru(g.np, 'nom')}"
    if g.tad:
        out += ", " + tad_ru(g.np, ref_pl)
    return out


def neither(gs, subj_num):
    """«X ca nānuseti Y ca nānuseti» = «не залегает ни X, ни Y» (coordinator; items flattened, head noun once)."""
    g0 = gs[0]
    trans = g0.mode in TRANS
    case = "gen" if trans else "nom"
    objs = [o for g in gs for o in g.np.objs()]
    if trans:
        num = subj_num
    else:
        num = "pl" if any(g.np.plural or g.vnum == "pl" for g in gs) else "sg"
    first = next(i for i, o in enumerate(objs) if o is not GAP)
    parts, gap = [], False
    for i, o in enumerate(objs):
        if o is GAP:
            gap = True
            continue
        head = f"{HEAD['sg'][case]} " if i == first else ""
        parts.append(("… " if gap and parts else (", " if parts else "")) + f"ни {head}{o}")
        gap = False
    tail = "…" if objs[-1] is GAP else ""
    return f"{verb(g0.mode, '-', num)} {''.join(parts)}{tail}"


def body_ru(gs, subj_num, flip=False):
    """A clause of one or more groups. flip: render the opposite polarity (after «no ca»)."""
    if flip:
        assert len(gs) == 1, "flip of a multi-group clause"
        g = gs[0]
        return vp(g, subj_num, "-" if g.pol == "+" else "+")
    if len(gs) == 1:
        return vp(gs[0], subj_num)
    pols = {g.pol for g in gs}
    assert len(pols) == 1, "mixed polarity in one clause"
    if not any(g.tad for g in gs) and not all(g.np.has_ca for g in gs) and any(g.np.has_ca for g in gs):
        slip("«ca» missing on one member of an «X ca … Y ca …» pair (rendered as the pair)")
    if any(g.np.has_ca for g in gs) and not any(g.tad for g in gs):
        if pols == {"-"}:
            assert not any(g.tad for g in gs)
            return neither(gs, subj_num)
        return ", ".join("и " + vp(g, subj_num) for g in gs)
    if not any(g.tad for g in gs[1:]) or gs[0].tad:
        raise ValueError(f"asyndetic groups without tadekaṭṭhaṃ (segment {_CUR['id']})")
    r = gs[0].np.plural
    joiner = ", и " if all(g.np.has_ca for g in gs) else ", "
    first = "и " if joiner == ", и " else ""
    return first + joiner.join(vp(g, subj_num, ref_pl=r) for g in gs)


# =========================================================================== persons, places
PERSON = {   # Pāli -> (Russian, gender m/f/pl)
    "Anāgāmissa": ("У невозвращающегося", "m"), "Arahato": ("У архата", "m"),
    "Puthujjanassa": ("У обычного человека", "m"), "Aṭṭhamakassa": ("У личности восьмой ступени", "f"),
    "Dvinnaṃ puggalānaṃ": ("У двух личностей", "pl"), "Tiṇṇaṃ puggalānaṃ": ("У трёх личностей", "pl"),
    "Catunnaṃ puggalānaṃ": ("У четырёх личностей", "pl"), "Tesaññeva puggalānaṃ": ("У этих же личностей", "pl"),
    "Tasseva puggalassa": ("У этой же личности", "f"),
    "Anāgāmī": ("Невозвращающийся", "m"), "Arahā": ("Архат", "m"), "Puthujjano": ("Обычный человек", "m"),
    "Aṭṭhamako": ("Личность восьмой ступени", "f"), "Dve puggalā": ("Две личности", "pl"),
    "Tayo puggalā": ("Три личности", "pl"), "Cattāro puggalā": ("Четыре личности", "pl"),
    "Teva puggalā": ("Эти же личности", "pl"), "Sveva puggalo": ("Эта же личность", "f"),
    "Anāgāmimaggasamaṅgī": ("Обладающий путём невозвращения", "m"),
    "Aggamaggasamaṅgī": ("Обладающий высшим путём", "m"),
}
EXCEPT = {   # «X ṭhapetvā avasesā puggalā» = «Кроме X, остальные личности» (pi-2 / pi-5 ṭhapetvā «кроме»; 2-02)
    "Dvinnaṃ maggasamaṅgīnaṃ": "двух обладающих путём",
    "Dvinnaṃ maggasamaṅgīnañca aṭṭhamakañca": "двух обладающих путём и личности восьмой ступени",
    "Aggamaggasamaṅgiñca aṭṭhamakañca": "обладающего высшим путём и личности восьмой ступени",
    "Anāgāmimaggasamaṅgiñca aṭṭhamakañca": "обладающего путём невозвращения и личности восьмой ступени",
    "Aggamaggasamaṅgiṃ": "обладающего высшим путём",
    "Anāgāmimaggasamaṅgiṃ": "обладающего путём невозвращения",
}
for _k, _v in EXCEPT.items():
    PERSON[f"{_k} ṭhapetvā avasesā puggalā"] = (f"Кроме {_v}, остальные личности", "pl")
PERSON_RX = "(?:" + "|".join(sorted(map(re.escape, PERSON), key=len, reverse=True)) + ")"
PLACE_RU = {   # locative places (pi-2 / pi-5; termbase dvīsu / tīsu vedanāsu «два / три вида чувства»)
    "kāmadhātuyā dvīsu vedanāsu": "в мире чувственных желаний в двух видах чувства",
    "kāmadhātuyā tīsu vedanāsu": "в мире чувственных желаний в трёх видах чувства",
    "dukkhāya vedanāya": "в болезненном чувстве",
    "rūpadhātuyā": "в мире форм", "arūpadhātuyā": "в мире без форм",
    "apariyāpanne": "в том, что не принадлежит к кругам существования",
    "sabbasakkāyapariyāpannesu dhammesu": "во всех явлениях, принадлежащих к самости",
}
PLACE_ONE = "(?:" + "|".join("[" + k[0].upper() + k[0] + "]" + re.escape(k[1:])
                             for k in sorted(PLACE_RU, key=len, reverse=True)) + ")"
PLACE_ONE = PLACE_ONE[:-1] + "|ariyāpanne)"   # ^6-7-130: ariyāpanne for apariyāpanne (rendered as meant)
PLACES = rf"{PLACE_ONE}(?:,?\s+{PLACE_ONE})*"


def places_ru(s):
    ps = re.findall(PLACE_ONE, s)
    if "ariyāpanne" in ps:
        slip("ariyāpanne for apariyāpanne (spelling, rendered as meant)")
        ps = ["apariyāpanne" if p == "ariyāpanne" else p for p in ps]
    if "," in s:
        slip("comma between two places (joined as usual)")
    rus = [PLACE_RU[p[0].lower() + p[1:]] for p in ps]
    return rus[0] if len(rus) == 1 else ", ".join(rus[:-1]) + " и " + rus[-1]


def pron(word, gender):
    """resumptive pronouns: tassa «у него / у неё», tesaṃ «у них», so «он / она», te «они»; tattha / tato / ettha «там»."""
    g = {"m": ("у него", "он"), "f": ("у неё", "она"), "pl": ("у них", "они")}[gender]
    parts = []
    for w in word.split():
        parts.append({"tassa": g[0], "tesaṃ": "у них", "so": g[1], "te": "они",
                      "tattha": "там", "tato": "там", "ettha": "там"}[w])
    return " ".join(parts)


RES = r"(?:tassa tattha|tesaṃ tattha|so tato|te tato|ettha|tato|sabbattha)"
NOCA_PRON = r"(?:tassa tattha|tesaṃ tattha|so tato|te tato|tassa|tesaṃ|tattha|tato|so|te)"
ANS = re.compile(rf"^(?:(?P<person>{PERSON_RX})\s+)?(?:(?P<places>{PLACES})\s+)?(?:(?P<res>{RES})(?:\s+|(?=…)|$))?(?P<body>.*)$")


def answer(s):
    """An answer sentence without its final punctuation."""
    m = ANS.match(s)
    person, places, res, body = m.group("person"), m.group("places"), m.group("res"), m.group("body").strip()
    gender = PERSON[person][1] if person else "m"
    if person:
        subj_num = "pl" if gender == "pl" else "sg"
    else:
        subj_num = "pl" if _CUR["okasa"] else "sg"   # subjectless verb in the place sections: indefinite 3rd pl
    if res and res.split()[0] in ("tassa", "tesaṃ", "so", "te") and person:
        want = {"tassa": ("m", "f"), "so": ("m", "f"), "tesaṃ": ("pl",), "te": ("pl",)}[res.split()[0]]
        if gender not in want:
            slip(f"pronoun {res.split()[0]} does not agree with {person} (rendered as written)")
    # body
    if body == "":
        assert res == "sabbattha", s
        b = ""
    elif body == "…pe…":
        b = "…"
    else:
        mm = re.match(rf"^(?P<a>.+?),?\s+no ca\s+(?:(?P<p>{NOCA_PRON})\s+)?(?P<b>.+)$", body)
        if mm:
            if not re.search(r",\s+no ca", body):
                slip("missing comma before «no ca» (rendered with the comma)")
            a = body_ru(parse_groups(mm.group("a")), subj_num)
            p2 = (pron(mm.group("p"), gender) + " ") if mm.group("p") else ""
            b = f"{a}, но {p2}{body_ru(parse_groups(mm.group('b')), subj_num, flip=True)}"
        else:
            b = body_ru(parse_groups(body), subj_num)
    if res == "sabbattha":
        assert b.startswith("не ") or b in ("…", ""), b
        b = "нигде" + ("" if b in ("…", "") else " ") + b
        res = None
    lead = []
    if person:
        lead.append(PERSON[person][0])
    if places:
        lead.append(places_ru(places))
    lead = " ".join(lead)
    if places and lead.endswith((PLACE_RU["apariyāpanne"], PLACE_RU["sabbasakkāyapariyāpannesu dhammesu"])):
        lead += ","                            # close the relative / participle clause of the place
    if lead and places:
        # aligned with G2: after a place intro the resumptive ettha / tattha / tato is not rendered; after a person
        # + place intro the pronoun (tassa / tesaṃ / so / te) is not rendered and tattha / tato = «там»
        assert res, f"places without a resumptive word: {s!r}"
        return cap(f"{lead} там {b}" if person else f"{lead} {b}")
    assert not res or res == "sabbattha", s
    return cap(f"{lead} {b}" if lead else b)


# =========================================================================== questions
REL_RU = {"yassa": "у кого", "yattha": "где", "yassa yattha": "у кого где", "yo": "кто", "yato": "где",
          "yo yato": "кто где"}
CORR_RU = {"tassa": "у того", "tattha": "там", "tassa tattha": "у того там", "so": "тот", "tato": "там",
           "so tato": "тот там"}
QRX = re.compile(r"^(?:(?P<lab>\((?:Ka|Kha)\))\s+)?(?P<r1>[Yy]assa|[Yy]attha|[Yy]o|[Yy]ato)\s+(?P<vp>vā pana\s+)?"
                 r"(?P<r2>yattha\s+|yato\s+)?(?P<b1>.+?)\s+(?P<c>tassa tattha|so tato|tassa|tattha|so|tato)\s+(?P<b2>.+)$")


def unti(s):
    """drop the quotation -ti of the final verb: anusetīti -> anuseti, pahīnoti -> pahīno, sānusayāti -> sānusayā."""
    if s.endswith("īti"):
        return s[:-3] + "i"
    if s.endswith(("oti", "āti")):
        return s[:-2]
    raise ValueError(f"no -ti in {s!r}")


def question(s):
    """A question without its «?»."""
    m = re.match(rf"^Kattha (?P<b>{NP} {VRX})$", s)
    if m:
        return f"Где {body_ru(parse_groups(m.group('b')), 'sg')}"
    note = ""
    nb = re.search(r"\s*(\[[^\]]*\])\s+(?=(?:tassa|tattha|so|tato)\s)", s)
    if nb:
        note = " " + bracket_ru(nb.group(1))
        s = s[:nb.start()] + " " + s[nb.end():]
    m = QRX.match(s)
    if not m:
        raise ValueError(f"no question frame for {s!r} (segment {_CUR['id']})")
    r1 = m.group("r1").lower() + (" " + m.group("r2").strip() if m.group("r2") else "")
    rel = {"yassa yattha": "yassa yattha", "yo yato": "yo yato"}.get(r1, r1)
    subj = "pl" if rel == "yato" else "sg"     # yato … tato …: no subject in the Pāli = indefinite 3rd pl
    g1 = parse_groups(m.group("b1"))
    _CUR["ref_pl"] = g1[0].np.plural or len(g1) > 1
    g2 = parse_groups(unti(m.group("b2")))
    _CUR["obj_pl"] = g2[0].np.plural or len(g2) > 1
    if g1[0].pol != g2[0].pol:
        slip(f"question halves differ in negation ({m.group('b1')!r} / {m.group('b2')!r}); kept as written")
    b1 = body_ru(g1, subj)
    if note:                                   # the variant is on the verb: put it right after the Russian verb
        v = verb(g1[0].mode, g1[0].pol, subj if g1[0].mode in TRANS else ("pl" if g1[0].np.plural else "sg"))
        assert b1.startswith(v + " "), b1
        b1 = v + note + b1[len(v):]
    q = f"{REL_RU[rel]} {b1}, {CORR_RU[m.group('c')]} {body_ru(g2, subj)}"
    q = ("А " + q) if m.group("vp") else cap(q)
    return (S.LABEL[m.group("lab")] + " " + q) if m.group("lab") else q


# =========================================================================== na vattabbo (pahīna paṭiloma)
NAV = re.compile(rf'^(?:(?P<np>{NP})\s+)?[Nn]a vattabb(?P<n>o|ā) "pahīn[oā]"ti vā "appahīn[oā]"ti vā$')


def na_vattabbo(s):
    """X na vattabbo "pahīno"ti vā "appahīno"ti vā = о X не следует говорить ни «устранена», ни «не устранена»."""
    m = NAV.match(s)
    np = NPh(m.group("np")) if m.group("np") else None
    pl = np.plural if np else m.group("n") == "ā"
    if np and np.plural != (m.group("n") == "ā"):
        slip("number of vattabbo / vattabbā differs from its subject (Russian agreement)")
    p = "устранены" if pl else "устранена"
    tail = f"не следует говорить ни «{p}», ни «не {p}»"
    return f"о {np_ru(np, 'prep')} {tail}" if np else tail


# =========================================================================== dhātu sections (user: «мирах»)
DH = {"kāma": "в мире чувственных желаний", "rūpa": "в мире форм", "arūpa": "в мире без форм"}
DH1 = r"(?:kāma|rūpa|arūpa)"


def dh_ru(s, case):
    """'Na kāmadhātuyā na arūpadhātuyā' -> 'не в мире чувственных желаний и не в мире без форм'."""
    parts = re.findall(rf"(?:(na) )?({DH1})dhātu(?:yā|ṃ)", s, re.I)
    assert " ".join(("na " if n else "") + d + "dhātu" + case for n, d in parts).lower() == s.lower(), (s, parts)
    return " и ".join(("не " if n else "") + DH[d.lower()] for n, d in parts)


FROM = rf"(?P<fr>(?:[Nn]a )?{DH1}dhātuyā(?: na {DH1}dhātuyā)?|[Kk]āmadhātuyā|[Rr]ūpadhātuyā|[Aa]rūpadhātuyā)"
TO = rf"(?P<to>(?:na )?{DH1}dhātuṃ(?: na {DH1}dhātuṃ)?)"
KATI = "kati anusayā anusenti, kati anusayā nānusenti, kati anusayā bhaṅgā"
KATI_RU = ("сколько скрытых склонностей залегает, сколько скрытых склонностей не залегает, "
           "сколько скрытых склонностей подлежит разделению")
NUM = {"satta": ("семь", "скрытых склонностей"), "pañca": ("пять", "скрытых склонностей"),
       "tayo": ("три", "скрытые склонности")}
SOME = ["в одних случаях", "в других случаях", "в третьих случаях"]   # kassaci … kassaci … kassaci …
SATTEVA = "залегают именно семь скрытых склонностей"                  # satteva anusayā anusenti
NOTHING = "скрытых склонностей, подлежащих разделению, нет"             # anusayā bhaṅgā natthi
UPAPATTI = "перерождения {to} вообще нет, перерождаясь ниже, он перерождается только в мире чувственных желаний"


def dhatu(s):
    """dhātupucchā / dhātuvisajjanā sentences (without final punctuation); None if not one."""
    if s == "anusayā bhaṅgā natthi":
        return NOTHING
    def frm(fr):
        f = fr[0].lower() + fr[1:]
        return dh_ru(f, "yā")
    m = re.match(rf"^{FROM} cutassa {TO} upapajjantassa (?P<t>.+)$", s)
    if m:
        intro = f"У того, кто, умерев {frm(m.group('fr'))}, перерождается {dh_ru(m.group('to'), 'ṃ')}"
        t = m.group("t")
        if t == KATI:
            return f"{intro}, {KATI_RU}"
        if t == "satteva anusayā anusenti":
            return f"{intro}, {SATTEVA}"
        ks = re.findall(r"kassaci (satta|pañca|tayo) anusayā anusenti", t)
        assert ", ".join(f"kassaci {k} anusayā anusenti" for k in ks) == t, t
        return intro + ", " + ", ".join(f"{SOME[i]} залегают {NUM[k][0]} {NUM[k][1]}" for i, k in enumerate(ks))
    m = re.match(rf"^{FROM} cutassa (?P<to>(?:na )?{DH1}dhātuyā(?: na {DH1}dhātuyā)?) upapatti ?nāma natthi, "
                 r"heṭṭhā upapajjamāno kāmadhātuṃyeva upapajjati, satteva anusayā anusenti$", s)
    if m:
        if "upapattināma" in s:
            slip("upapattināma written together (rendered as upapatti nāma)")
        return (f"У того, кто умер {frm(m.group('fr'))}, " + UPAPATTI.format(to=dh_ru(m.group("to"), "yā"))
                + f", {SATTEVA}")
    return None


# =========================================================================== fixed lines, headings, labels
NUMLAB = {"Eka": "одной", "Duka": "двух", "Tika": "трёх", "Catukka": "четырёх", "Pañcaka": "пяти", "Chakka": "шести"}
LABELS = {f"({k}mūlakaṃ)": f"(На основе {v})" for k, v in NUMLAB.items()}
LABELS["(Ekamūlakaṃ )"] = LABELS["(Ekamūlakaṃ)"]
DHLAB = {"Kāma": "мира чувственных желаний", "Rūpa": "мира форм", "Arūpa": "мира без форм",
         "Nakāma": "не мира чувственных желаний", "Narūpa": "не мира форм", "Naarūpa": "не мира без форм",
         "Nakāmanaarūpa": "не мира чувственных желаний и не мира без форм",
         "Narūpanaarūpa": "не мира форм и не мира без форм",
         "Nakāmanarūpa": "не мира чувственных желаний и не мира форм"}   # termbase «на основе …»
LABELS.update({f"({k}dhātumūlakaṃ)": f"(На основе {v})" for k, v in DHLAB.items()})
VARA = {   # section names (ru-zeroshot-terms, user-approved; termbase)
    "Uppattiṭṭhāna": "Раздел о месте возникновения", "Anusaya": "Раздел о скрытых склонностях",
    "Sānusaya": "Раздел об имеющих скрытые склонности", "Pajahana": "Раздел об устранении",
    "Pariññā": "Раздел о полном понимании", "Pahīna": "Раздел об устранённом",
    "Uppajjana": "Раздел о возникновении",
    "Dhātupucchā": "Раздел вопросов о мирах", "Dhātuvisajjanā": "Раздел ответов о мирах",
    "Dhātuvisajja": "Раздел ответов о мирах",
}
FORM = {"anulomaṃ": "Утвердительная форма", "paṭilomaṃ": "Отрицательная форма"}
SUBHEAD = {"anulomapuggalo": "утвердительная форма по личности", "anulomaokāso": "утвердительная форма по месту",
           "anulomapuggalokāsā": "утвердительная форма по личности и месту",
           "paṭilomapuggalo": "отрицательная форма по личности", "paṭilomaokāso": "отрицательная форма по месту",
           "paṭilomapuggalokāsā": "отрицательная форма по личности и месту",
           "dhātupucchāvāro": "раздел вопросов о мирах", "dhātuvisajjanāvāro": "раздел ответов о мирах"}
SEVEN = ("Семь скрытых склонностей – " + ", ".join(f"скрытая склонность к {v}" for v in ANU.values()) + ".")


def in_section(ru):
    """«Раздел о X» -> «в разделе о X»."""
    return "в разделе" + ru[len("Раздел"):]


def fixed(s):
    """Exact Pāli sentence (with its punctuation) -> Russian, or None."""
    f = {
        "Āmantā.": S.YES, "No.": "Нет.", "Natthi.": "Такого нет.",
        "Āmantā …pe….": "Да…", "Āmantā…pe….": "Да…",
        "Namo tassa bhagavato arahato sammāsambuddhassa": S.NAMO,
        "Anusayayamakaṃ niṭṭhitaṃ.": S.yamaka_done("Anusayayamakaṃ"),
        "Sattānusayā – kāmarāgānusayo, paṭighānusayo, mānānusayo, diṭṭhānusayo, vicikicchānusayo, "
        "bhavarāgānusayo, avijjānusayo.": SEVEN,
        "(Vitthāretabbaṃ).": "(Следует развернуть).",
        "9": "9",
        "(Kha) yattha vā pana…pe…?": f"{S.LABEL['(Kha)']} А где…?",
    }
    if s in f:
        return f[s]
    if s in LABELS:
        return LABELS[s]
    m = re.fullmatch(r"(\w+)vāre (anulomaṃ|paṭilomaṃ)\.", s)
    if m:
        k = m.group(1)
        if k == "Pajahanā":
            slip("Pajahanāvāre for Pajahanavāre (spelling, rendered as meant)")
            k = "Pajahana"
        return f"{FORM[m.group(2)]} {in_section(VARA[k])}."
    m = re.fullmatch(r"(\w+)vāro\.", s)
    if m and m.group(1) in VARA:
        return VARA[m.group(1)] + "."
    return None


def heading(text):
    hashes, body = text.split(" ", 1)
    if body == "Anusayayamakaṃ":
        return f"{hashes} {S.YAMAKA[body]}"
    if body == "Mahāvāro 1. anusayavāro":
        return f"{hashes} Большой раздел 1. {VARA['Anusaya']}"
    m = re.fullmatch(r"(\([^)]+\)) (\w+)", body)
    if m:
        return f"{hashes} {S.LABEL[m.group(1)]} {cap(SUBHEAD[m.group(2)])}"
    m = re.fullmatch(r"(\w+?)vār[oa]", body)
    if m and m.group(1) in VARA:
        return f"{hashes} {VARA[m.group(1)]}"
    raise ValueError(f"no heading for {text!r}")


def bracket_ru(b):
    if b == "[pahīno (sī. ka.) anusayavārena pana na sameti]":
        return "[вариант чтения (Sī., Ka.): pahīno; но с разделом о скрытых склонностях это не согласуется]"
    raise ValueError(f"no bracket rendering for {b!r}")


# =========================================================================== sentences and lines
def split_sentences(line):
    """Split after . ? ; followed by a space, never inside [...]."""
    out, cur, depth = [], "", 0
    i = 0
    while i < len(line):
        ch = line[i]
        cur += ch
        depth += (ch == "[") - (ch == "]")
        if depth == 0 and ch in ".?;" and i + 1 < len(line) and line[i + 1] == " ":
            out.append(cur.strip())
            cur = ""
        i += 1
    if cur.strip():
        out.append(cur.strip())
    return out


VIT = " (vitthāretabbaṃ)"


def translate_sentence(s):
    f = fixed(s)
    if f is not None:
        return f
    core, end = s, ""
    if core.endswith(VIT + "."):
        core, end = core[:-len(VIT) - 1], " (следует развернуть)."
    elif core[-1:] in ".?;":
        core, end = core[:-1], core[-1]
        if core.endswith("bhaṅgā") and end == ".":
            slip("a dhātupucchā question ends with «.» (kept as written)")
    if core.endswith("…pe…"):                   # «…pe….» / « …pe….» at the end = «…»
        core = core[:-len("…pe…")].rstrip()
        end = "…" if end == "." else "…" + end
    if core.endswith("?") and end == "":
        core, end = core[:-1], "?"
    d = dhatu(core)
    if d is not None:
        return d + end
    if re.match(AN_STEM.replace("(?:", "(?:(?i:") + ")", core) and core[0].isupper():
        core = core[0].lower() + core[1:]          # a sentence that starts with a tendency (no person, no place)
    if end == "?":
        return question(core) + end
    if NAV.match(core):
        r = na_vattabbo(core)
        return (cap(r) if s[0].isupper() else r) + end
    m = re.fullmatch(rf"Tadekaṭṭhaṃ ({VRX})", core)
    if m:
        g = VP[m.group(1)]
        return tadekattha(g) + end
    r = answer(core)
    if not s[0].isupper():
        r = r[0].lower() + r[1:]
    return r + end


def translate_line(pali):
    if pali.startswith("#"):
        h = heading(pali)
        _CUR["okasa"] = pali.endswith("okāso")
        return h
    f = fixed(pali)
    if f is not None:
        return f
    return " ".join(translate_sentence(s) for s in split_sentences(pali))


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


def check_shared():
    """Shared strings must equal the sample's and G2's (frame-setter for the pavatti / pariññā frames)."""
    import importlib
    assert S.YES == "Да." and S.LABEL["(Gha)"] == "(г)"
    try:
        G2 = importlib.import_module("build_rails_G2_ru")
    except Exception as e:   # G2 still being written: report, do not fail
        return [f"G2 not importable ({e.__class__.__name__}); shared strings not cross-checked"]
    out = []
    pairs = [(G2.NO, "Нет."), (G2.NATTHI, "Такого нет."),
             (G2.PERSONS["arahā"][0], PERSON["Arahā"][0]),
             (G2.PERSONS["aggamaggasamaṅgī"][0], PERSON["Aggamaggasamaṅgī"][0]),
             (G2.tru(("parijānāti", False), "sg"), VRU["par"]["+"][0]),
             (G2.tru(("parijānāti", True), "sg"), VRU["par"]["-"][0]),
             (G2.tru(("parijānāti", True), "pl"), VRU["par"]["-"][1]),
             (G2.EXCEPT, "Кроме"),
             (G2.QREL["yassa yattha"], (REL_RU["yassa yattha"], CORR_RU["tassa tattha"]))]
    for a, b in pairs:
        if a != b:
            out.append(f"differs from G2: {a!r} vs {b!r}")
    return out


def main(chs):
    problems = check_shared()
    for p in problems:
        print("shared:", p)
    for ch in chs:
        pt = (PALI / ch).read_text(encoding="utf-8")
        _CUR["okasa"] = False
        ru, pr = render(pt)
        problems += pr
        e, n = S.check_file(pt, ru)
        problems += [f"{ch}: {x}" for x in e]
        (OUT / ch).write_text(ru, encoding="utf-8", newline="\n")
        print(f"wrote {ch}: {n} segments")
    seen = set()
    for sid, note in SLIPS:
        if (sid, note) not in seen:
            seen.add((sid, note))
            print("slip", sid, note)
    print("per-line problems:", len(problems))
    for p in problems:
        print("  ", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or CHAPTERS))
