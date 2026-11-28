"""G10b indriya: Pāli->Russian keyword maps for pi-6 10-05 … 10-13-indriyayamaka.

usage:  python -I -X utf8 -B map_G10b_ru.py [PART ...]   (writes <part>.mapped.md and verifies it; default: all nine)
import: importing writes nothing (the MIXED pacchimabhavika warning goes to stderr only while building).
    G10b.OWN          this group's new values (future-unit persons purisā / itthiyo, last-mind units, bhāveti /
                      sacchikaroti in all tenses, 10-13 persons, slips); G10b.G10B_TABLE = the whole table
    G10b.pacchima_value() G2's rule extended to upapajjantīnaṃ and the ^6-10-398 slip uppajjantānaṃ
    G10b.citta_moment()   cittassa uppāda- / bhaṅgakkhaṇe: plain vs «этого ума» (same rule as map_G9_ru)
    G10b.exceptions_for(part)

Imports (not retyped): map_G10a_ru G10A_TABLE (= YM + G2_FRAME + G3 AY_PLANES + G8 TIME / PERSONS + IN_FACULTY,
IN_BARE, IN_PERSON, IN_MOMENT, IN_HEAD) and moment_value(); map_G2_ru frame_value() (denied negative, pariññā word
order), _fold_ti, _ti, FRAME_EXC_RU; map_G45_ru MOMENTS (anantarā, cittassa, citte, vattamāne, upapatticittassa …),
PJ3_FRAME / pj3_value() (pajahati in all tenses, nappajah- rule), G45_EXC_RU; map_G7_ru five person keys (anāgāmī,
anāgāmimaggasamaṅgī / -iṃ, aṭṭhamako / -aṃ). G2_KHANDHA not imported. map_G9_ru read only (bhāveti = развивать,
citta_moment rule; G9 runs in parallel, so its rule is copied, not imported).
Resolution per keyword: OVERRIDES[bid][kw] -> pacchima_value() -> citta_moment() -> G2.frame_value() ->
G45.pj3_value() -> G10B_TABLE (-ti / -nti / -ñca / -ñceva folded) -> G10a.moment_value() -> CORE -> value().
Every chapter's segments were compared through the builders' notes (notes-10-05 … notes-10-13) and probes
(probe_G10b_ru.py); decisions in notes-map-G10b.md.
"""
import importlib
import pathlib
import re
import sys

sys.dont_write_bytecode = True
_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
from map_common_pi6_ru import CORE, NDE, YM, build_part, lc, value, verify  # noqa: E402,F401

G2 = importlib.import_module("map_G2_ru")
G10a = importlib.import_module("map_G10a_ru")
G45 = importlib.import_module("map_G45_ru")

PARTS = [f"10-{i:02d}-indriyayamaka" for i in range(5, 14)]

G7 = importlib.import_module("map_G7_ru")

OWN = {
    # persons of the future units
    "purisā": "мужчины", "itthiyo": "женщины",
    "sacakkhukā": "с глазом", "saghānakā": "с носом",
    "somanassasampayuttapacchimacittaṃ": "последний ум связанный с радостью",
    "upekkhāsampayuttapacchimacittaṃ": "последний ум связанный с невозмутимостью",
    "somanassasampayuttapacchimacittasamaṅgīnaṃ": "обладающий последним умом связанным с радостью",
    "upekkhāsampayuttapacchimacittasamaṅgīnaṃ": "обладающий последним умом связанным с невозмутимостью",
    "pacchimacittasamaṅgīna": "обладающий последним умом",
    "upapatticittassa": "ум перерождения",          # split keyword «в момент возникновения ума перерождения»
    "cavantīnaṃ": "умирать", "cavantāna": "умирать",
    "itarāsaṃ": "остальной",
    "uppajjantānaṃ": "возникать",
    "ghānandriyamūlakaṃ": "на основе способности носа",
    # 10-13 verbs
    "bhāveti": "развивать", "bhāventi": "развивать",
    "bhāvittha": "развить", "bhāvessati": "развить", "bhāvessanti": "развить",
    "sacchikaroti": "осуществлять", "sacchikaronti": "осуществлять",
    "sacchikarittha": "осуществить", "sacchikarissati": "осуществить", "sacchikarissanti": "осуществить",
    "sacchākāsi": "осуществить",
    "aggaphalaṃ": "высший плод", "maggaṃ": "путь",
    "anāgāmimaggasamaṅgi": "обладающий путём невозвращения",
    "maggasamaṅgino": "обладающий путём",
    "yamakapakaraṇaṃ": "парные вопросы",
}
for _f in ("bhāveti", "bhāvittha", "bhāvessati", "sacchikaroti", "sacchikarittha", "sacchikarissati"):
    OWN[G2._ti(_f)] = OWN[_f]                       # quoted -īti / -āti forms
_G7_KEYS = ("anāgāmī", "anāgāmimaggasamaṅgī", "anāgāmimaggasamaṅgiṃ", "aṭṭhamako", "aṭṭhamakaṃ")
G10B_TABLE = {**G10a.G10A_TABLE, **G45.MOMENTS, **G45.PJ3_FRAME,
              **{k: G7.ANUSAYA_TABLE[k] for k in _G7_KEYS}, **OWN}
# per-segment readings {block id: {keyword exactly as listed: Russian}}
OVERRIDES = {
    # «no ca tesaṃ somanassindriyaṃ na upapajjissati» (upapajjati for uppajjati, kept as written, notes-10-06):
    # «но у них переродится способность радости» = the positive verb the text has
    "6-10-309": {"upapajjissati": "переродиться"},
}

# presence exceptions: perfective infinitive vs the future form in the text (self-checking, as G2.FRAME_EXC_RU)
G10B_EXC_RU = {
    "bhāvessati": (r"разовь(ёт|ют)", "развить ~ разовьёт/разовьют"),
    "bhāvessanti": (r"разовь(ёт|ют)", "развить ~ разовьёт/разовьют"),
    "bhāvessatīti": (r"разовь(ёт|ют)", "развить ~ разовьёт/разовьют"),
}


def exceptions_for(part):
    return G2.frame_exceptions(part, exc={**G2.FRAME_EXC_RU, **G45.G45_EXC_RU, **G10B_EXC_RU})


def pacchima_value(kw, pali, ru):
    k = lc(kw)
    if k != "pacchimabhavikānaṃ":
        return None
    kinds = set()
    for m in re.finditer(r"(?<!\w)" + re.escape(kw) + r"(?!\w)((?: \S+){0,2})", pali):
        nxt = m.group(1).split()
        reb = ("upapajjantānaṃ", "upapajjantīnaṃ", "uppajjantānaṃ")
        last = bool(nxt) and nxt[0] in reb
        last = last or (len(nxt) == 2 and nxt[1] in reb)
        kinds.add("раз" if last else "жизнь")
    if len(kinds) > 1:
        print("   MIXED pacchimabhavika", kw, file=sys.stderr)
    if kinds == {"раз"}:
        assert "в последний раз" in ru, (kw, ru)
        return "в последний раз"
    assert "последней жизнью" in ru, (kw, ru)
    return "жить последней жизнью"


KHANA = {"uppādakkhaṇe": "момент возникновения", "bhaṅgakkhaṇe": "момент распада"}


def citta_moment(kw, pali, ru):
    """cittassa uppādakkhaṇe / bhaṅgakkhaṇe (same rule as map_G9_ru.citta_moment): «момент возникновения ума» where
    the Pāli segment has the plain unit (Sabbesaṃ cittassa bhaṅgakkhaṇe …); where it has only «tassa cittassa …»
    = «в момент распада этого ума» («этого» renders tassa, not listed): «момент распада … ума»."""
    k = lc(kw)
    if k not in ("cittassa uppādakkhaṇe", "cittassa bhaṅgakkhaṇe"):
        return None
    kh = k.split()[1]
    words = [re.sub(r"[^\w]", "", w).lower() for w in pali.split()]
    plain = any(w == "cittassa" and i + 1 < len(words) and words[i + 1] == kh and (i == 0 or words[i - 1] != "tassa")
                for i, w in enumerate(words))
    mo = KHANA[kh]
    if plain:
        assert f"{mo} ума" in ru, (kw, ru[:200])
        return f"{mo} ума"
    assert f"{mo} этого ума" in ru, (kw, ru[:200])
    return f"{mo} … ума"


def resolver_for(part, table=None):
    t = G10B_TABLE if table is None else table
    pa, ru = G2.read_pali(part), G2.read_russian(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        p, r = pa.get(bid, ""), ru.get(bid, "")
        for f in (pacchima_value, citta_moment):
            v = f(kw, p, r)
            if v is not None:
                return v
        v = G2.frame_value(kw, p, r)
        if v is not None:
            return v
        v = G45.pj3_value(kw, r)
        if v is not None:
            return v
        for k in G2._fold_ti(lc(kw)):
            if k in t:
                return t[k]
        v = G10a.moment_value(kw)
        if v is not None:
            return v
        if lc(kw) in CORE:
            return CORE[lc(kw)]
        return value(kw, kws, t)
    return resolve


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=300, allowed=exceptions_for(p))
