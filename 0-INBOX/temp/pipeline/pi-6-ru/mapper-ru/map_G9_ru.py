"""G9 dhamma: Pāli->Russian keyword maps for pi-6 9-01-dhammayamaka, 9-02-dhammayamaka, 9-03-dhammayamaka.

usage:  python -I -X utf8 -B map_G9_ru.py [PART ...]   (writes <part>.mapped.md and verifies it; default: all three)
import: importing writes nothing. Later groups:

    import importlib, sys; sys.path.insert(0, r"...\\pi-6-ru\\mapper-ru"); G9 = importlib.import_module("map_G9_ru")
    G9.DH_MEMBERS (kusala / akusala / abyākata in the paṇṇatti and pavatti forms), G9.DH_MOMENTS (the Dhamma moment
    units: kusalānaṃ / kusalavippayuttacittassa / kusalākusalānaṃ uppāda- and bhaṅgakkhaṇe), G9.DH_PERSONS (the
    sacca-type person units: aggamaggaṃ paṭilabhissanti, anantarā, cittassa, vattamāne …), G9.DH_FRAME (headings,
    bhāvanāvāra), G9.citta_moment() (cittassa uppāda- / bhaṅgakkhaṇe: plain vs «этого ума»), G9.G9_TABLE.

Frame values are imported from the frame-setters: map_G2_ru (G2_FRAME, frame_value(), frame_exceptions(); not
G2_KHANDHA) and map_G8_ru (TENSE, TIME, PERSONS, HEADINGS: moments «момент возникновения / распада», «последний ум»,
«обладающий последним умом», «вошедший в медитативное достижение прекращения»). map_G3_ru was read: its paṇṇatti
additions (glued negated nouns nāyatana-, -pi notes, yassaka / yatthaka notes) do not occur in 9-01 … 9-03 (the
Dhamma paṇṇatti has the separate «na»). The sacca person units (aggamaggaṃ paṭilabhissanti, anantarā, cittassa,
vattamāne, pavatte, arahantānaṃ, akusale citte) carry the same values as map_G45_ru MOMENTS (same Russian frames,
build_5-01_ru); they are set here, not imported, because G45 runs at the same time.

Resolution per keyword: OVERRIDES[bid][kw] -> G2.frame_value() (denied negative, pariññā, pacchimabhavika) ->
pj_value() (pajahati / nappajahati of the bhāvanāvāra) -> citta_moment() -> G9_TABLE (-ti / -nti / -ñca / -ñceva
folded) -> CORE (Namo line) -> value() (YM -> pi-2 KH -> pi-1 CH2 / MATRIX).  See notes-map-G9.md.
"""
import importlib
import pathlib
import re
import sys

sys.dont_write_bytecode = True
_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
from map_common_pi6_ru import CORE, NDE, YM, build_part, lc, read_pali, read_russian, value, verify  # noqa: E402

G2 = importlib.import_module("map_G2_ru")
G8 = importlib.import_module("map_G8_ru")

PARTS = ["9-01-dhammayamaka", "9-02-dhammayamaka", "9-03-dhammayamaka"]

# =============================================================================================== members
# pi-1 «благие / неблагие / этически неопределённые явления» (build_9-01_ru DH_K); bare adjectives (paṇṇattivāra
# «Благие являются …», «Кроме благого …») = masculine singular (YM kusalā / kusalaṃ = благой)
MEMBER = {   # stem: (adj, «X явления» nom. pl.)
    "kusala": ("благой", "благие явления"),
    "akusala": ("неблагой", "неблагие явления"),
    "abyākata": ("этически неопределённый", "этически неопределённые явления"),
}
DH_MEMBERS = {}
for _m, (_adj, _pl) in MEMBER.items():
    _a = _m[:-1] + "ā"
    DH_MEMBERS.update({
        _a: _adj, _m + "ṃ": _adj, _m: _adj,
        f"{_a} dhammā": _pl, f"{_a} ca dhammā": _pl,          # «и возникают благие явления, и …» (ca = и)
        # «Кроме благого и явлений» (Kusalañca dhamme ca ṭhapetvā): the whole two-member phrase, nominative
        f"{_m}ñca dhamme": f"{_adj} и явления",
        # bhāvanāvāra «Кто развивает благое явление» (acc. sg. kusalaṃ dhammaṃ, notes-9-03)
        f"{_m}ṃ dhammaṃ": _pl.replace("ые явления", "ое явление").replace("ие явления", "ое явление"),
    })
DH_MEMBERS.update({
    "dhammā": "явления",
    "avasesā": "остальной",       # «Остальные явления», «остальное» (G2 / G3)
    "ṭhapetvā": "кроме",
})

# =============================================================================================== moments
# locative time phrases -> nominative noun phrase without «в», government kept (G8 TIME); the comma of «ума, не
# связанного с благим» dropped (G8 «ума охваченного страстью», G45 «ума не связанного с жаждой»)
KHANA = {"uppādakkhaṇe": "момент возникновения", "bhaṅgakkhaṇe": "момент распада"}
INSTR = {"kusala": "благим", "akusala": "неблагим", "abyākata": "этически неопределённым"}
GEN_PL = {"kusala": "благих явлений", "akusala": "неблагих явлений",
          "abyākata": "этически неопределённых явлений"}
DH_MOMENTS = {}
for _kh, _mo in KHANA.items():
    for _x in MEMBER:
        DH_MOMENTS[f"{_x}vippayuttacittassa {_kh}"] = f"{_mo} ума не связанного с {INSTR[_x]}"
        DH_MOMENTS[f"{_x[:-1]}ānaṃ {_kh}"] = f"{_mo} {GEN_PL[_x]}"          # «в момент возникновения благих явлений»
        for _y in MEMBER:
            if _y != _x:
                DH_MOMENTS[f"{_x}vippayutta{_y}vippayuttacittassa {_kh}"] = (
                    f"{_mo} ума не связанного с {INSTR[_x]} и не связанного с {INSTR[_y]}")
    # notes-9-02 UNITS_9_02: «в момент распада благих и неблагих явлений»
    DH_MOMENTS[f"kusalākusalānaṃ {_kh}"] = f"{_mo} благих и неблагих явлений"
DH_MOMENTS["kusalākusalānaṃ"] = "благие и неблагие явления"   # split keyword (pi-2 kusalākusalā, + явления as kusalānaṃ)


def citta_moment(kw, pali, ru):
    """cittassa uppādakkhaṇe / bhaṅgakkhaṇe: «момент возникновения ума» where the Pāli segment has the plain unit
    (Sabbesaṃ cittassa uppādakkhaṇe …); where it has only «tassa cittassa …» = «в момент возникновения этого ума»
    («этого» renders tassa, not listed): «момент возникновения … ума»."""
    k = lc(kw)
    if k not in ("cittassa uppādakkhaṇe", "cittassa bhaṅgakkhaṇe"):
        return None
    kh = k.split()[1]
    words = [re.sub(r"[^\w]", "", w).lower() for w in pali.split()]
    plain = any(w == "cittassa" and i + 1 < len(words) and words[i + 1] == kh and (i == 0 or words[i - 1] != "tassa")
                for i, w in enumerate(words))
    mo = KHANA[kh]
    if plain:
        return f"{mo} ума"
    assert f"{mo} этого ума" in ru, (kw, ru[:200])
    return f"{mo} … ума"


# =============================================================================================== persons
# the sacca-type person units (build_5-01_ru frames; same values as map_G45_ru MOMENTS)
DH_PERSONS = {
    "pavatte": "течение жизни",                        # «в течение жизни»
    "vattamāne": "присутствовать",                     # «когда присутствует второй ум»
    "citte": "ум", "akusale citte": "неблагой ум",     # «второй (неблагой) ум»
    "cittassa": "ум",                                  # «сразу после данного ума»
    "anantarā": "сразу после",
    "aggamaggaṃ paṭilabhissanti": "обрести высший путь",   # «кто обретёт высший путь»
    "aggamaggassa": "высший путь",                     # «в момент возникновения / распада высшего пути»
    "aggamaggasamaṅgīnaṃ": "обладающий высшим путём",  # «У обладающих высшим путём» (G2 aggamaggasamaṅgī)
    "arahantānaṃ": "архаты",                           # «у архатов» (Pāli and Russian plural)
}

# =============================================================================================== headings / bhāvanā
DH_FRAME = {
    "dhammayamakaṃ": "парные вопросы о явлениях",      # G8 HEADINGS
    "suddhadhammavāro": "раздел о явлениях как таковых",
    "suddhadhammamūlacakkavāro": "круговой раздел на основе явлений как таковых",
    "bhāvanāvāro": "раздел о развитии",                # notes-9-03
    "bhāveti": "развивать",                            # «развивает» (pi-1)
    "pajahati": "устранять",                           # «устраняет» (G7 / G45 pajahati)
}

G9_TABLE = {**YM, **G2.G2_FRAME, **G8.TENSE, **G8.TIME, **G8.PERSONS, **G8.HEADINGS,
            **DH_MEMBERS, **DH_MOMENTS, **DH_PERSONS, **DH_FRAME}
G9_TABLE["natthi"] = "такого нет"      # G2 / G8 (YM still has нет)


def pj_value(kw, ru):
    """nappajahati: «не устраняет» in the Russian = не устранять (glued n-, as G2 nuppajjati / G45 nappajahati);
    else the positive verb the text has (denied negative)."""
    k = lc(kw)
    if k in ("nappajahati", "nappajahatīti"):
        return "не устранять" if re.search(r"не\s+устраня(ет|ют)", ru.lower()) else "устранять"
    return None


# per-segment readings {block id: {keyword exactly as listed: Russian}} (none needed: the chapters are formulaic)
OVERRIDES = {}


def _fold(k):
    out = [k]
    for end, rep in (("ñceva", "ṃ"), ("ñca", "ṃ"), ("nti", "ṃ")):
        if k.endswith(end):
            out.append(k[: -len(end)] + rep)
    if k.endswith(("oti", "āti", "īti", "ūti")):
        out.append(k[:-2])
    if k.endswith("īti"):
        out.append(k[:-3] + "i")              # bhāvetīti -> bhāveti, pajahatīti -> pajahati
    return out


CORE_KW = ("abhidhammapiṭake", "namo", "bhagavato", "arahato", "sammāsambuddhassa")


def resolver_for(part, table=None):
    t = G9_TABLE if table is None else table
    pa, ru = read_pali(part), read_russian(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        p, r = pa.get(bid, ""), ru.get(bid, "")
        for f in (lambda: G2.frame_value(kw, p, r), lambda: pj_value(kw, r), lambda: citta_moment(kw, p, r)):
            v = f()
            if v is not None:
                return v
        k = lc(kw)
        if k in CORE_KW:
            return CORE[k]
        for b in _fold(k):
            if b in t:
                return t[b]
        return value(kw, kws, t)
    return resolve


# presence-check exceptions: G2's self-checking frame-verb exceptions plus the perfective «обрести высший путь»
G9_EXC_RU = {**G2.FRAME_EXC_RU,
             "aggamaggaṃ paṭilabhissanti": (r"обрет(ёт|ут) высший путь", "обрести высший путь ~ обретёт высший путь")}
for _k in ("nirujjhissati", "nirujjhissanti"):     # plural «прекратятся» (stem change outside present())
    G9_EXC_RU[_k] = G9_EXC_RU[G2._ti(_k)] = (r"прекрат(ится|ятся)", "прекратиться ~ прекратится/прекратятся")


def exceptions_for(part):
    return G2.frame_exceptions(part, exc=G9_EXC_RU)


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=300, allowed=exceptions_for(p))
