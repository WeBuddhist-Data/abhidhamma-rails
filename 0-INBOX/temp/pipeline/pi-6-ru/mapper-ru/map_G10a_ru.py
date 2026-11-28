"""G10a indriya: Pāli->Russian keyword maps for pi-6 10-01 … 10-04-indriyayamaka.

usage:  python -I -X utf8 -B map_G10a_ru.py [PART ...]   (writes <part>.mapped.md and verifies it; default: all four)
import: importing writes nothing. G10b (10-05 … 10-13) imports the tables:

    import importlib, sys; sys.path.insert(0, r"...\\pi-6-ru\\mapper-ru"); G10a = importlib.import_module("map_G10a_ru")
    G10a.IN_FACULTY   the 22 faculties (cakkhundriyaṃ … aññātāvindriyaṃ), indriyaṃ / indriyā / indriye, and the
                      (X-indriyamūlakaṃ) tails «(На основе способности глаза)»; -nti / -ñca / -ñceva fold to these
    G10a.IN_BARE      the bare paṇṇatti words (cakkhu глаз … itthī женщина, puriso мужчина, sukhaṃ удовольствие …),
                      every case form listed in 10-01 / 10-02; plus the Āyatana qualifiers (Dibbacakkhu …)
    G10a.IN_PERSON    person attributes and person verbs of the pavatti frame (itthīnaṃ женщина, purisānaṃ мужчина,
                      somanassena радость, upekkhāya невозмутимость, ñāṇasampayuttānaṃ со знанием,
                      ñāṇavippayuttānaṃ без знания, sahetukānaṃ с корнями, sa-X-ka / a-X-ka с глазом / без глаза …,
                      upapajjantīnaṃ перерождаться, uppajjantīnaṃ (^6-10-206 slip) возникать)
    G10a.IN_MOMENT    every «X-sampayutta / -vippayutta (two members) cittassa uppādakkhaṇe / bhaṅgakkhaṇe» moment
                      (also pacchimacittassa), built by moment_value(); members IN_ASSOC (somanassa, upekkhā, saddhā,
                      ñāṇa); G10b can call moment_value(kw) for a combination not in the table
    G10a.IN_HEAD      Indriyayamakaṃ, Suddhindriyavāro, Suddhindriyamūlacakkavāro
    G10a.G10A_TABLE   = YM + G2_FRAME + G3 planes / sa-X-ka + G8 TIME / PERSONS + all of the above

Imports (not retyped): map_G2_ru G2_FRAME / frame_value() / frame_exceptions() / _fold_ti (pavatti verbs, answers,
planes, persons, vāra headings); map_G8_ru TIME and PERSONS (cittassa uppādakkhaṇe / bhaṅgakkhaṇe,
nirodhasamāpannānaṃ, asaññasattānaṃ); map_G3_ru AY_PLANES, AY_HAVE (sacakkhukānaṃ «с глазом» pattern) and the
qualifiers. G2_KHANDHA is NOT imported. map_G6_ru was read: its plane / person values are the same as G2 / G3.
Resolution per keyword: OVERRIDES[bid][kw] -> G2.frame_value() -> G10A_TABLE (-ti / -nti / -ñca / -ñceva folded)
-> moment_value() -> CORE -> value() (pi-2 KH, pi-1 CH2 / MATRIX).  See notes-map-G10a.md.
"""
import importlib
import pathlib
import re
import sys

sys.dont_write_bytecode = True
_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
from map_common_pi6_ru import CORE, NDE, YM, build_part, lc, value, verify  # noqa: E402

G2 = importlib.import_module("map_G2_ru")
G3 = importlib.import_module("map_G3_ru")
G8 = importlib.import_module("map_G8_ru")

PARTS = [f"10-0{i}-indriyayamaka" for i in range(1, 5)]

# =============================================================================================== faculties
# the 22 faculties (pi-2 ^2-221 Russian, build_10-01_ru IN_K): «способность + genitive»; jīvita = жизненная способность
IN_ORDER = ["cakkhu", "sota", "ghāna", "jivhā", "kāya", "mana", "itthī", "purisa", "jīvita", "sukha", "dukkha",
            "somanassa", "domanassa", "upekkhā", "saddhā", "vīriya", "sati", "samādhi", "paññā",
            "anaññātaññassāmīti", "añña", "aññātāvī"]
IN_STEM = dict(zip(IN_ORDER, [        # Pāli faculty stem (+ "ṃ" = the keyword, + "mūlakaṃ" = the closing tail)
    "cakkhundriya", "sotindriya", "ghānindriya", "jivhindriya", "kāyindriya", "manindriya", "itthindriya",
    "purisindriya", "jīvitindriya", "sukhindriya", "dukkhindriya", "somanassindriya", "domanassindriya",
    "upekkhindriya", "saddhindriya", "vīriyindriya", "satindriya", "samādhindriya", "paññindriya",
    "anaññātaññassāmītindriya", "aññindriya", "aññātāvindriya"]))
IN_GEN = {
    "cakkhu": "глаза", "sota": "уха", "ghāna": "носа", "jivhā": "языка", "kāya": "тела", "mana": "ума",
    "itthī": "женственности", "purisa": "мужественности", "sukha": "удовольствия", "dukkha": "боли",
    "somanassa": "радости", "domanassa": "уныния", "upekkhā": "невозмутимости", "saddhā": "веры",
    "vīriya": "усердия", "sati": "осознанности", "samādhi": "сосредоточения", "paññā": "мудрости",
    "anaññātaññassāmīti": "познания непознанного", "añña": "окончательного знания",
    "aññātāvī": "обладателя окончательного знания",
}
IN_NAME = {m: "способность " + g for m, g in IN_GEN.items()}
IN_NAME["jīvita"] = "жизненная способность"
IN_NAME_GEN = {m: "способности " + g for m, g in IN_GEN.items()}
IN_NAME_GEN["jīvita"] = "жизненной способности"

IN_FACULTY = {"indriyaṃ": "способность", "indriyā": "способности", "indriye": "способности"}
for _m in IN_ORDER:
    IN_FACULTY[IN_STEM[_m] + "ṃ"] = IN_NAME[_m]
    # (Cakkhundriyamūlakaṃ) = «(На основе способности глаза)» (G3 X-āyatanamūlakaṃ = на основе сферы X)
    IN_FACULTY[IN_STEM[_m] + "mūlakaṃ"] = "на основе " + IN_NAME_GEN[_m]

# =============================================================================================== bare words
# paṇṇattivāra bare words (build_10-01_ru IN_X; the six sense words as G3): every listed case form = nominative
_BARE = {
    "cakkhu": ("глаз", ["cakkhu", "cakkhū", "cakkhuṃ"]), "sota": ("ухо", ["sotaṃ"]),
    "ghāna": ("нос", ["ghānaṃ"]), "jivhā": ("язык", ["jivhā", "jivhaṃ"]), "kāya": ("тело", ["kāyo", "kāyaṃ"]),
    "mana": ("ум", ["mano", "manaṃ"]), "itthī": ("женщина", ["itthī", "itthiṃ"]),
    "purisa": ("мужчина", ["puriso", "purisaṃ"]), "jīvita": ("жизнь", ["jīvitaṃ"]),
    "sukha": ("удовольствие", ["sukhaṃ"]),          # as in «способность удовольствия» (not «счастье»)
    "dukkha": ("боль", ["dukkhaṃ"]), "somanassa": ("радость", ["somanassaṃ"]),
    "domanassa": ("уныние", ["domanassaṃ"]), "upekkhā": ("невозмутимость", ["upekkhā", "upekkhaṃ"]),
    "saddhā": ("вера", ["saddhā", "saddhaṃ"]), "vīriya": ("усердие", ["vīriyaṃ"]),
    "sati": ("осознанность", ["sati", "satī", "satiṃ"]),
    "samādhi": ("сосредоточение", ["samādhi", "samādhī", "samādhiṃ"]),
    "paññā": ("мудрость", ["paññā", "paññaṃ"]),
    "anaññātaññassāmīti": ("познание непознанного", ["anaññātaññassāmīti", "anaññātaññassāmītiṃ"]),
    "añña": ("окончательное знание", ["aññaṃ"]),
    "aññātāvī": ("обладатель окончательного знания", ["aññātāvī", "aññātāviṃ"]),
}
IN_BARE = {f: v for v, forms in _BARE.values() for f in forms}
IN_BARE.update({
    "anaññātaññāssāmīti": "познание непознанного",     # ^6-10-3 spelling slip (rendered as meant)
    # Āyatana qualifiers (G3 / 3-01): «Божественный глаз, глаз мудрости …», «Божественное ухо, поток жажды …»
    **{k: G3.AY_MEMBERS[k] for k in ("dibbacakkhu", "paññācakkhu", "dibbasotaṃ", "taṇhāsotaṃ")},
    "ṭhapetvā": "кроме", "avasesā": "остальной", "avasesaṃ": "остальной", "avaseso": "остальной",
})

# =============================================================================================== persons
# G3 pattern: the prepositional phrase that carries sa- / a- (sacakkhukānaṃ «с глазом», acakkhukānaṃ «без глаза»);
# -sampayutta / -vippayutta persons the same («со знанием» / «без знания»). The instrumental somanassena /
# upekkhāya («с радостью», after vinā «без радости») = the nominative noun (conventions-pi6 §3: a «с …» phrase of
# an instrumental keyword goes to the nominative noun; vinā carries «без»). Gender nouns: nominative.
IN_PERSON = dict(G3.AY_HAVE)
IN_PERSON.update({
    "sajivhakānaṃ": "с языком", "ajivhakānaṃ": "без языка",          # build_10-02_ru IN_HAVE2 (prepared)
    "sakāyakānaṃ": "с телом", "akāyakānaṃ": "без тела",
    "itthīnaṃ": "женщина", "purisānaṃ": "мужчина",                  # «перерождается (не) женщиной / мужчиной»
    "somanassena": "радость", "upekkhāya": "невозмутимость",         # «с радостью» / «без радости»
    "sahetukānaṃ": "с корнями", "ahetukānaṃ": "без корней",
    "ñāṇasampayuttānaṃ": "со знанием", "ñāṇavippayuttānaṃ": "без знания",
    "upapajjantīnaṃ": "перерождаться",                              # feminine of upapajjantānaṃ (G2 перерождаться)
    "uppajjantīnaṃ": "возникать",            # ^6-10-206 «Itthīnaṃ … uppajjantīnaṃ» = «кто возникает женщиной» (as written)
    "pavatte": "течение жизни",              # «в течение жизни» (as G45 MOMENTS)
})

# =============================================================================================== moments
# «в момент возникновения ума, связанного с радостью и не связанного с верой» -> nominative noun phrase without
# «в», comma dropped (G8 TIME / G45 MOMENTS rule): момент возникновения ума связанного с радостью и …
IN_ASSOC = {"somanassa": "с радостью", "upekkhā": "с невозмутимостью", "saddhā": "с верой", "ñāṇa": "со знанием"}
KHANA = {"uppādakkhaṇe": "момент возникновения", "bhaṅgakkhaṇe": "момент распада"}
MOMENT_RE = re.compile(r"((?:(?:" + "|".join(IN_ASSOC) + r")(?:sampayutta|vippayutta)){1,2})(pacchima)?cittassa"
                       r" (uppādakkhaṇe|bhaṅgakkhaṇe)")
ASSOC_RE = re.compile(r"(" + "|".join(IN_ASSOC) + r")(sampayutta|vippayutta)")


def moment_value(kw):
    """X-sampayutta / -vippayutta (one or two members) [pacchima]cittassa uppādakkhaṇe / bhaṅgakkhaṇe -> Russian;
    None if the keyword is not such a moment."""
    m = MOMENT_RE.fullmatch(lc(kw))
    if not m:
        return None
    assoc = [("связанного " if k == "sampayutta" else "не связанного ") + IN_ASSOC[a]
             for a, k in ASSOC_RE.findall(m.group(1))]
    mind = "последнего ума" if m.group(2) else "ума"
    return f"{KHANA[m.group(3)]} {mind} " + " и ".join(assoc)


IN_MOMENT = {}
_pairs = [a + k for a in IN_ASSOC for k in ("sampayutta", "vippayutta")]
for _p1 in _pairs:
    for _p2 in [""] + [p for p in _pairs if not p.startswith(_p1[:-len("sampayutta")])]:
        for _pc in ("", "pacchima"):
            for _kh in KHANA:
                _k = f"{_p1}{_p2}{_pc}cittassa {_kh}"
                IN_MOMENT[_k] = moment_value(_k)

# =============================================================================================== headings
IN_HEAD = {
    "indriyayamakaṃ": "парные вопросы о способностях",
    "suddhindriyavāro": "раздел о способностях как таковых",
    "suddhindriyamūlacakkavāro": "круговой раздел на основе способностей как таковых",
}

G10A_TABLE = {**YM, **G2.G2_FRAME, **G3.AY_PLANES, **G8.TIME, **G8.PERSONS,
              **IN_FACULTY, **IN_BARE, **IN_PERSON, **IN_MOMENT, **IN_HEAD}

# per-segment readings {block id: {keyword exactly as listed: Russian}} (none needed: the chapters are formulaic)
OVERRIDES = {}


def resolver_for(part, table=None):
    t = G10A_TABLE if table is None else table
    pa, ru = G2.read_pali(part), G2.read_russian(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        v = G2.frame_value(kw, pa.get(bid, ""), ru.get(bid, ""))
        if v is not None:
            return v
        for k in G2._fold_ti(lc(kw)):
            if k in t:
                return t[k]
        v = moment_value(kw)
        if v is not None:
            return v
        if lc(kw) in CORE:
            return CORE[lc(kw)]
        return value(kw, kws, t)
    return resolve


def exceptions_for(part):
    return G2.frame_exceptions(part)


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=300, allowed=exceptions_for(p))
