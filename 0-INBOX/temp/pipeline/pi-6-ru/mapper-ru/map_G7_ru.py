"""G7 anusaya: Pāli->Russian keyword maps for 7-01 … 7-11 (Anusayayamaka). Frame-setter for the anusaya keywords.

usage: python -I -X utf8 -B map_G7_ru.py [PART ...]     (writes <part>.mapped.md for the G7 parts and verifies them)
Importing writes nothing. Later groups:  import map_G7_ru as G7;  G7.ANUSAYA_TABLE, G7.NEG_RULES, G7.context_value()

Resolution per keyword: OVERRIDES[bid][kw] -> context_value() (negation in THIS segment's Russian, the Namo line)
-> ANUSAYA_TABLE (= YM + the anusaya keywords) -> value() (pi-2 KH, pi-1 CH2 / MATRIX; -ti / -ñca folded).
Every keyword's value was read off the Russian of the chapter (fixed builder phrases; build_7-0N_ru.py, notes-7-0N.md);
verify() checks each value against its own segment. Decisions: notes-map-G7.md.
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi6_ru import (CORE, NDE, YM, allowed_for, build_part, lc, read_russian,  # noqa: E402,F401
                               value, verify)

PARTS = [f"7-{i:02d}-anusayayamaka" for i in range(1, 12)]

# ---------------------------------------------------------------------------- the seven tendencies
# every case form (-o, -ā, -aṃ, -añca, -ena) = the nominative name (pi-2 / pi-5); the instrumental of
# «X-ena sānusayo / niranusayo» («имеет / не имеет скрытую склонность к X») takes the same value
ANUSAYA_NAMES = {
    "kāmarāga": "скрытая склонность к чувственной страсти",
    "kāmārāga": "скрытая склонность к чувственной страсти",      # source slip ^6-7-21, ^6-7-25 (notes-7-01)
    "paṭigha": "скрытая склонность к неприязни",
    "māna": "скрытая склонность к самомнению",
    "diṭṭha": "скрытая склонность к воззрениям",
    "vicikicchā": "скрытая склонность к колебанию",
    "bhavarāga": "скрытая склонность к страсти к существованию",
    "avijjā": "скрытая склонность к неведению",
}
ANUSAYA_TABLE = {**YM}
for _stem, _v in ANUSAYA_NAMES.items():
    _s = _stem[:-1] if _stem.endswith(("a", "ā")) else _stem
    for _end in ("ānusayo", "ānusayā", "ānusayaṃ", "ānusayañca", "ānusayena", "ānusayassa"):
        ANUSAYA_TABLE[_s + _end] = _v

ANUSAYA_TABLE.update({
    # -- names and the book frame
    "anusaya": "скрытая склонность", "anusayo": "скрытая склонность", "anusayā": "скрытые склонности",
    "sattānusayā": "семь скрытых склонностей",
    "anusayayamakaṃ": "парные вопросы о скрытых склонностях",
    # -- verbs (finite verb in the text -> infinitive; short participle «устранена» -> full form)
    "anuseti": "залегать", "anusenti": "залегать",
    "sānusayo": "иметь", "sānusayā": "иметь",                 # «имеет / имеют скрытую склонность к X»
    "pajahati": "устранять", "pajahanti": "устранять",
    "parijānāti": "полностью понимать", "parijānanti": "полностью понимать",
    "pahīno": "устранённый", "pahīnā": "устранённый",
    "uppajjati": "возникать",
    "upapajjati": "перерождаться", "upapajjantassa": "перерождаться",
    "upapajjamāno": "перерождаясь",                           # gerund the text uses («перерождаясь ниже»)
    "upapatti": "перерождение", "upapattināma": "перерождение",   # nāma has no word («перерождения … не бывает»)
    "bhaṅgā": "подлежать разделению",                         # 7-10 «подлежит разделению» (coordinator, notes-7-10)
    "natthi": "такого нет",                                   # «Такого нет.» (ru-map-conventions-pi6.md §7)
    # -- persons (nominative; pi-5 / 2-02 / notes-7-05)
    "anāgāmissa": "невозвращающийся", "anāgāmī": "невозвращающийся",
    "puthujjanassa": "обычный человек", "puthujjano": "обычный человек",
    "arahato": "архат", "arahā": "архат",
    "puggalassa": "личность", "puggalo": "личность", "puggalānaṃ": "личности", "puggalā": "личности",
    "aggamaggasamaṅgī": "обладающий высшим путём", "aggamaggasamaṅgiṃ": "обладающий высшим путём",
    "anāgāmimaggasamaṅgī": "обладающий путём невозвращения",
    "anāgāmimaggasamaṅgiṃ": "обладающий путём невозвращения",
    "maggasamaṅgīnaṃ": "обладающий путём",       # «Кроме двух обладающих путём» (participle masc. sg., as G8)
    "aṭṭhamako": "личность восьмой ступени", "aṭṭhamakaṃ": "личность восьмой ступени",   # pi-5
    "avasesā": "остальной", "ṭhapetvā": "кроме",
    # -- places (nominative; pi-2 / pi-5)
    "kāmadhātuyā": "мир чувственных желаний", "rūpadhātuyā": "мир форм", "arūpadhātuyā": "мир без форм",
    "kāmadhātuṃ": "мир чувственных желаний", "rūpadhātuṃ": "мир форм", "arūpadhātuṃ": "мир без форм",
    "kāmadhātuṃyeva": "только … мир чувственных желаний",       # «только в мире чувственных желаний»
    "dvīsu vedanāsu": "два вида чувства", "tīsu vedanāsu": "три вида чувства",
    "dukkhāya vedanāya": "болезненное чувство",
    # -- headings and closings (heading phrase, label / number dropped, lower-case first letter)
    "uppattiṭṭhānavāro": "раздел о месте возникновения",
    "mahāvāro": "большой раздел",
    "anusayavāro": "раздел о скрытых склонностях", "anusayavāra": "раздел о скрытых склонностях",
    "anusayavāre": "раздел о скрытых склонностях",
    "sānusayavāro": "раздел об имеющих скрытые склонности", "sānusayavāra": "раздел об имеющих скрытые склонности",
    "sānusayavāre": "раздел об имеющих скрытые склонности",
    "pajahanavāro": "раздел об устранении", "pajahanavāra": "раздел об устранении",
    "pajahanavāre": "раздел об устранении", "pajahanāvāre": "раздел об устранении",   # ^6-7-197 slip
    "pariññāvāro": "раздел о полном понимании", "pariññāvāra": "раздел о полном понимании",
    "pariññāvāre": "раздел о полном понимании",
    "pahīnavāro": "раздел об устранённом", "pahīnavāra": "раздел об устранённом",
    "pahīnavāre": "раздел об устранённом",
    "uppajjanavāro": "раздел о возникновении",
    "dhātupucchāvāro": "раздел вопросов об элементах",
    "dhātuvisajjanāvāro": "раздел ответов об элементах", "dhātuvisajjavāro": "раздел ответов об элементах",
    "anulomapuggalo": "утвердительная форма по личности", "anulomaokāso": "утвердительная форма по месту",
    "anulomapuggalokāsā": "утвердительная форма по личности и месту",
    "paṭilomapuggalo": "отрицательная форма по личности", "paṭilomaokāso": "отрицательная форма по месту",
    "paṭilomapuggalokāsā": "отрицательная форма по личности и месту",
    "anulomaṃ": "утвердительная форма", "paṭilomaṃ": "отрицательная форма",
    "kāmadhātumūlakaṃ": "на основе мира чувственных желаний",
    "rūpadhātumūlakaṃ": "на основе мира форм",
    "arūpadhātumūlakaṃ": "на основе мира без форм",
    "nakāmadhātumūlakaṃ": "на основе не мира чувственных желаний",
    "narūpadhātumūlakaṃ": "на основе не мира форм",
    "naarūpadhātumūlakaṃ": "на основе не мира без форм",
    "nakāmanaarūpadhātumūlakaṃ": "на основе не мира чувственных желаний и не мира без форм",
    "narūpanaarūpadhātumūlakaṃ": "на основе не мира форм и не мира без форм",
    "nakāmanarūpadhātumūlakaṃ": "на основе не мира чувственных желаний и не мира форм",
    # -- the literal placeholder keyword of the Pāli list (no Pāli word of its own; as the hi / mr / my maps)
    NDE: NDE,
})

# ---------------------------------------------------------------------------- context rules
# negated Pāli verb: «не X» where THIS segment's Russian says it negatively; the positive verb where the text only
# says the denied negative plainly («no ca tassa Y nānuseti» = «но у него залегает Y»; coordinator "Negatives")
NEG_RULES = [   # (keyword regex, negated value, positive value, regex for the negated Russian)
    (r"^nānuse", "не залегать", "залегать", r"не\s+залега"),
    (r"^nappajah", "не устранять", "устранять", r"не\s+устраня"),
    (r"^niranusay", "не иметь", "иметь", r"не\s+име"),
    (r"^appahīn", "не устранённый", "устранённый", r"не\s+устранен"),
    (r"^nuppajj", "не возникать", "возникать", r"не\s+возника"),
]
FOLD = re.compile(r"(?<=[āīūo])ti$")       # anusetīti, sānusayoti, appahīnāti -> base form


def context_value(bid, kw, text):
    """Segment-dependent values; None = use the table."""
    k = lc(kw)
    t = (text or "").replace("ё", "е").lower()
    for pat, neg, pos, ru in NEG_RULES:
        if re.match(pat, k):
            return neg if re.search(ru, t) else pos
    if k.startswith("parijān"):
        # G2's pariññā rule (map_G2_ru.PJ_VERB / pj_value): «полностью понимать»; where the segment has the verb
        # only in the negated order «не понимает / понимают полностью», the value follows it («понимать полностью»).
        # Matched on the stem here: the anusaya place sections use the generic plural «Где полностью понимают …»
        # with a singular Pāli verb (7-03 GENERIC_3PL), which a number-specific test would miss.
        return "полностью понимать" if "полностью понима" in t else "понимать полностью"
    if k == "arahato" and "достойн" in t and "архат" not in t:
        return CORE["arahato"]                                  # the Namo line (^6-7-349)
    return None


# per-segment readings: {block id: {keyword exactly as listed: Russian}}
OVERRIDES = {}


def resolver_for(part):
    ru = read_russian(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        c = context_value(bid, kw, ru.get(bid))
        if c is not None:
            return c
        k = lc(kw)
        if k in CORE and k not in ANUSAYA_TABLE:
            return CORE[k]
        if k not in ANUSAYA_TABLE and FOLD.search(k):
            base = FOLD.sub("", k)
            for b in (base, base[:-1] + {"ī": "i", "ā": "a", "ū": "u"}.get(base[-1], base[-1])):
                if b in ANUSAYA_TABLE:
                    return ANUSAYA_TABLE[b]
        return value(kw, kws, ANUSAYA_TABLE)
    return resolve


# presence-check exceptions (value correct; the Russian form is outside present()'s tolerance)
def exceptions_for(part):
    ru = read_russian(part)
    exc = {}
    from map_common_pi6_ru import read_keywords
    for bid, kws in read_keywords(part):
        t = (ru.get(bid) or "").replace("ё", "е").lower()
        for kw in kws:
            k = lc(kw)
            if k == "bhaṅgā" and "подлежит разделению" in t and "подлежащ" not in t:
                exc[(bid, kw)] = "«подлежит разделению» (2nd conjugation -ит, outside present())"
    return exc


if __name__ == "__main__":
    for p in sys.argv[1:] or PARTS:
        build_part(p, resolver_for(p))
        verify(p, show=200, allowed={**allowed_for(p), **exceptions_for(p)})
