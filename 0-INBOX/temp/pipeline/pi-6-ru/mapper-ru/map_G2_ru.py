"""G2 khandha: Pāli->Russian keyword maps for pi-6 2-01-khandhayamaka and 2-02-khandhayamaka.

usage:  python -I -X utf8 -B map_G2_ru.py          (writes the two <part>.mapped.md and verifies them)
import: importing writes nothing. FRAME-SETTER for the paṇṇatti, pavatti and pariññā frames: later groups import

    import importlib, sys; sys.path.insert(0, r"...\\pi-6-ru\\mapper-ru"); G2 = importlib.import_module("map_G2_ru")
    table = {**G2.YM, **G2.G2_FRAME, **own_members}
    v = G2.frame_value(kw, pali_text, ru_text)      # context rules (denied negative, word order, pacchimabhavika)
    allowed = G2.frame_exceptions(part)             # presence-check exceptions of the frame verbs (self-checking)

Exposed constants
  PV_FRAME     pavatti verbs (uppajjati / nirujjhati, all tenses, sg / pl, -ti, glued n-), answers (Āmantā, No, Natthi)
  PJ_FRAME     pariññā verbs (parijānāti … parijānissanti) and its persons (Arahā, Aggamaggasamaṅgī, puthujjanā …)
  PLANE_KW     planes (pañca- / catu- / eka-vokāra, arūpa, asaññasatta, suddhāvāsa) in every case form of the frames
  PERSON_KW    person units (upapajjantānaṃ, cavantānaṃ, parinibbantānaṃ, itaresaṃ, sabbesaṃ …)
  HEAD_KW      vāra headings / colophons shared by all yamakas (paṇṇatti, padasodhana, pavatti, uppāda, nirodha …)
  G2_FRAME     = PV_FRAME + PJ_FRAME + PLANE_KW + PERSON_KW + HEAD_KW   (import this, not G2_KHANDHA)
  G2_KHANDHA   the Khandhayamaka members (rūpaṃ = «форма» here only: paṇṇattivāra «Форма является …»)
  G2           = YM + G2_FRAME + G2_KHANDHA (this group's table)
Resolution per keyword: OVERRIDES[bid][kw] -> frame_value() context rules -> CORE (frame words) -> G2 -> value()
(pi-2 KH, pi-1 CH2 / MATRIX).  See notes-map-G2.md for every value.
"""
import pathlib
import re
import sys

sys.dont_write_bytecode = True
_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
from map_common_pi6_ru import (CORE, EXCEPTIONS, NDE, YM, build_part, lc, present,  # noqa: E402,F401
                               read_keywords, read_pali, read_russian, value, verify)

PARTS = ["2-01-khandhayamaka", "2-02-khandhayamaka"]


def _ti(form):
    """Quoted form at the end of a question: uppajjati -> uppajjatīti, uppajjittha -> uppajjitthāti."""
    return form[:-1] + ("īti" if form.endswith("i") else "āti")


# =============================================================================================== pavatti frame
# Russian verb in the text -> infinitive. Tenses: present «возникает» -> возникать; past (-ittha) «возникала»
# (imperfective) -> возникать; future (-issati) «возникнет» (perfective) -> возникнуть.
PV_VERB = {
    "uppajjati": "возникать", "uppajjanti": "возникать", "uppajjittha": "возникать",
    "uppajjissati": "возникнуть", "uppajjissanti": "возникнуть",
    "nirujjhati": "прекращаться", "nirujjhanti": "прекращаться", "nirujjhittha": "прекращаться",
    "nirujjhissati": "прекратиться", "nirujjhissanti": "прекратиться",
}
PV_FRAME = {}
for _f, _v in PV_VERB.items():
    PV_FRAME[_f] = PV_FRAME[_ti(_f)] = _v
    if _f.startswith("upp"):                               # glued negation: nuppajjati … (see pv_neg_value)
        PV_FRAME["n" + _f] = PV_FRAME[_ti("n" + _f)] = "не " + _v
PV_FRAME.update({
    "nirujjhattha": "прекращаться",                        # ^6-2-111 slip for nirujjhittha (rendered as meant)
    "āmantā": "да", "no": "нет", "natthi": "такого нет",   # ru-map-conventions-pi6.md §7 (YM still has natthi = нет)
    "na": "не",
    "yattha": "где", "yatthakaṃ": "раздел с «где»",       # «(раздел с «где» следует изложить полностью)»
})

# Denied negative (coordinator "Negatives"): «no ca tesaṃ Y nuppajjati» = «но у них возникает Y». A glued n-form maps
# to «не V» where that tense occurs negated in the segment's Russian, else to the positive verb the text has.
PV_NEG_RU = {"nuppajjati": r"не возника(ет|ют)", "nuppajjanti": r"не возника(ет|ют)", "nuppajjittha": r"не возникал",
             "nuppajjissati": r"не возникн", "nuppajjissanti": r"не возникн"}


def pv_neg_value(kw, ru):
    k = lc(kw)
    base = next((b for b in PV_NEG_RU if k in (b, _ti(b))), None)
    if base is None:
        return None
    return PV_FRAME[base] if re.search(PV_NEG_RU[base], ru.lower()) else PV_VERB[base[1:]]


# =============================================================================================== pariññā frame
# pi-5: parijānāti = полностью понимать. Past «полностью понял» and future «полностью поймёт» = полностью понять.
# The negated question / answer has the order «не понимает полностью»: where a segment has the verb only in that
# order, the value follows it («понимать полностью»). The negation «na» is a separate word: the keyword is positive.
PJ_VERB = {"parijānāti": "полностью понимать", "parijānanti": "полностью понимать",
           "parijānittha": "полностью понять", "parijānissati": "полностью понять",
           "parijānissanti": "полностью понять"}
PJ_POS_RU = {"parijānāti": r"полностью понимает", "parijānanti": r"полностью понимают",
             "parijānittha": r"полностью понял", "parijānissati": r"полностью поймёт",
             "parijānissanti": r"полностью поймут"}
PJ_FRAME = {}
for _f, _v in PJ_VERB.items():
    PJ_FRAME[_f] = PJ_FRAME[_ti(_f)] = _v
PJ_FRAME.update({
    "arahā": "архат", "arahantaṃ": "архат",                                # pi-5; arahantañca folds to arahantaṃ
    "aggamaggasamaṅgī": "обладающий высшим путём", "aggamaggasamaṅgiṃ": "обладающий высшим путём",
    "puggalā": "личности",                                                 # «остальные личности»
    "puthujjanā": "обычные люди",                                          # «те обычные люди, которые …»
    "maggaṃ paṭilabhissanti": "обрести путь", "paṭilabhissanti": "обрести",  # «обретёт / обретут путь»
})


def pj_value(kw, ru):
    k = lc(kw)
    base = next((b for b in PJ_VERB if k in (b, _ti(b))), None)
    if base is None:
        return None
    if re.search(PJ_POS_RU[base], ru.lower()):
        return PJ_VERB[base]
    return " ".join(reversed(PJ_VERB[base].split()))                      # «не понимает полностью»


# =============================================================================================== planes and persons
# plane forms (-aṃ «перерождается в …», -e «В …: там», -ā «умирает в …») = the plane; -ānaṃ = its beings
PLANE_RU = {
    "pañcavokār": ("существование с пятью составляющими", "существа с пятью составляющими"),
    "catuvokār": ("существование с четырьмя составляющими", "существа с четырьмя составляющими"),
    "ekavokār": ("существование с одной составляющей", "существа с одной составляющей"),
    "arūp": ("мир без форм", "существа мира без форм"),
    "asaññasatt": ("существа без восприятия", "существа без восприятия"),   # «среди существ без восприятия»
    "suddhāvās": ("Чистые обители", "существа Чистых обителей"),
}
PLANE_KW = {}
for _s, (_in, _beings) in PLANE_RU.items():
    for _e in ("aṃ", "e", "ā"):
        PLANE_KW[_s + _e] = _in
    PLANE_KW[_s + "ānaṃ"] = _beings

PERSON_KW = {
    "upapajjantānaṃ": "перерождаться", "upapajjitvā": "переродившись",   # «кто перерождается», «переродившись»
    "cavantānaṃ": "умирать",                                             # «кто умирает» / «когда они умирают»
    "parinibbantānaṃ": "достигать окончательного угасания",
    "parinibbāyissanti": "достигнуть окончательного угасания",           # «достигнет окончательного угасания»
    "itaresaṃ": "остальной",                                             # «у остальных» (as avasesā = остальной)
    "sabbesaṃ": "все",                                                   # «у всех, кто …»
    "pacchimabhavikānaṃ": "жить последней жизнью",                       # see pacchima_value
}


def pacchima_value(kw, pali, ru):
    """pacchimabhavikānaṃ: «тех, кто живёт последней жизнью» = жить последней жизнью; in «pacchimabhavikānaṃ
    [Xaṃ] upapajjantānaṃ» = «кто (в последний раз) перерождается (в последний раз)» = в последний раз.
    Decided by the exact-case occurrences of the keyword in the Pāli segment."""
    if lc(kw) != "pacchimabhavikānaṃ":
        return None
    kinds = set()
    for m in re.finditer(r"(?<!\w)" + re.escape(kw) + r"(?!\w)((?: \S+){0,2})", pali):
        nxt = m.group(1).split()
        last = nxt[0] == "upapajjantānaṃ" if nxt else False
        last = last or (len(nxt) == 2 and nxt[0].endswith("aṃ") and nxt[1] == "upapajjantānaṃ")
        kinds.add("раз" if last else "жизнь")
    if kinds == {"раз"}:
        assert "в последний раз" in ru, (kw, ru)
        return "в последний раз"
    assert "последней жизнью" in ru, (kw, ru)
    return "жить последней жизнью"


# =============================================================================================== headings
HEAD_KW = {
    "paṇṇattivāro": "раздел об обозначениях", "paṇṇattivāraniddesa": "разъяснение раздела об обозначениях",
    "paṇṇattiuddesavāro": "раздел перечня обозначений", "paṇṇattiniddesavāro": "раздел разъяснения обозначений",
    "padasodhanavāro": "раздел уточнения слов",
    "padasodhanamūlacakkavāro": "круговой раздел на основе уточнения слов",
    "anulomaṃ": "утвердительная форма", "paccanīkaṃ": "отрицательная форма",
    "anulomapuggalo": "утвердительная форма по личности", "anulomaokāso": "утвердительная форма по месту",
    "anulomapuggalokāsā": "утвердительная форма по личности и месту",
    "paccanīkapuggalo": "отрицательная форма по личности", "paccanīkaokāso": "отрицательная форма по месту",
    "paccanīkapuggalokāsā": "отрицательная форма по личности и месту",
    "pavattivāro": "раздел о протекании", "pavatti": "протекание",
    "uppādavāro": "раздел о возникновении", "uppādavāre": "раздел о возникновении",
    "nirodhavāro": "раздел о прекращении", "uppādanirodhavāro": "раздел о возникновении и прекращении",
    "atītānāgatavāro": "раздел о прошлом и будущем", "pariññāvāro": "раздел о полном понимании",
    NDE: NDE,     # the keyword lists carry the literal token "(no direct equivalent)": kept as it is
}

G2_FRAME = {**PV_FRAME, **PJ_FRAME, **PLANE_KW, **PERSON_KW, **HEAD_KW}

# =============================================================================================== Khandha members
KH_GEN = {"rūpa": "материальной формы", "vedanā": "чувств", "saññā": "восприятия",
          "saṅkhāra": "формирующих факторов", "viññāṇa": "сознания"}
G2_KHANDHA = {
    "khandhayamakaṃ": "парные вопросы о совокупностях", "khandhayamakapāḷi": "парные вопросы о совокупностях",
    "suddhakhandhavāro": "раздел о совокупностях как таковых",
    "suddhakhandhamūlacakkavāro": "круговой раздел на основе совокупностей как таковых",
    "pañcakkhandhā": "пять совокупностей",
    "khandho": "совокупность", "khandhaṃ": "совокупность", "khandhā": "совокупности", "khandhe": "совокупности",
    "avasesā khandhā": "остальные совокупности",
    # paṇṇattivāra bare words (build_2-01_ru KH_X): rūpa = «форма» (piyarūpa …), the aggregate keeps pi-2
    "rūpaṃ": "форма", "vedanā": "чувство", "vedanaṃ": "чувство", "saññā": "восприятие", "saññaṃ": "восприятие",
    "saṅkhārā": "формирующие факторы", "saṅkhāre": "формирующие факторы", "viññāṇaṃ": "сознание",
    "diṭṭhisaññā": "восприятие-воззрение", "ṭhapetvā": "кроме", "avasesā": "остальной",
    "vadanākkhandho": "совокупность чувств",                  # ^6-2-185 slip for vedanākkhandho
}
for _m, _g in KH_GEN.items():
    for _e in ("kkhandho", "kkhandhaṃ"):
        G2_KHANDHA[_m + _e] = "совокупность " + _g

G2 = {**YM, **G2_FRAME, **G2_KHANDHA}

# per-segment readings {block id: {keyword exactly as listed: Russian}} (none needed: the frames are formulaic)
OVERRIDES = {}


def _fold_ti(k):
    """-ti / -nti / -oti quotation endings and -ñca / -ñceva: candidate base keys."""
    out = [k]
    if k.endswith("ñceva"):
        out.append(k[:-5] + "ṃ")
    if k.endswith("ñca"):
        out.append(k[:-3] + "ṃ")
    if k.endswith("nti"):
        out.append(k[:-3] + "ṃ")
    if k.endswith(("oti", "āti", "īti", "ūti")):
        out.append(k[:-2])
    return out


def frame_value(kw, pali, ru):
    """Context rules of the frames; None if the keyword is not one of them."""
    for f in (pv_neg_value, pj_value):
        v = f(kw, ru)
        if v is not None:
            return v
    return pacchima_value(kw, pali, ru)


def resolver_for(part, table=None):
    t = G2 if table is None else table
    pa, ru = read_pali(part), read_russian(part)

    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        v = frame_value(kw, pa.get(bid, ""), ru.get(bid, ""))
        if v is not None:
            return v
        for k in _fold_ti(lc(kw)):
            if k in t:
                return t[k]
        if lc(kw) in CORE:
            return CORE[lc(kw)]
        return value(kw, kws, t)
    return resolve


# =============================================================================================== presence exceptions
# Perfective infinitive vs the future form in the text (stem change outside present()'s tolerance). Each exception is
# accepted only if the stated Russian form is really in the segment (self-checking).
FRAME_EXC_RU = {
    "uppajjissati": (r"возникн(ет|ут)", "возникнуть ~ возникнет/возникнут"),
    "uppajjissanti": (r"возникн(ет|ут)", "возникнуть ~ возникнет/возникнут"),
    "nuppajjissati": (r"не возникн(ет|ут)", "не возникнуть ~ не возникнет/возникнут"),
    "nuppajjissanti": (r"не возникн(ет|ут)", "не возникнуть ~ не возникнет/возникнут"),
    "parijānissati": (r"(полностью пойм(ёт|ут)|пойм(ёт|ут) полностью)", "понять ~ поймёт/поймут"),
    "parijānissanti": (r"(полностью пойм(ёт|ут)|пойм(ёт|ут) полностью)", "понять ~ поймёт/поймут"),
    "parinibbāyissanti": (r"достигн(ет|ут) окончательного угасания", "достигнуть ~ достигнет/достигнут"),
    "paṭilabhissanti": (r"обрет(ёт|ут)", "обрести ~ обретёт/обретут"),
    "maggaṃ paṭilabhissanti": (r"обрет(ёт|ут) путь", "обрести путь ~ обретёт/обретут путь"),
}
for _k in list(FRAME_EXC_RU):
    if " " not in _k:
        FRAME_EXC_RU[_ti(_k)] = FRAME_EXC_RU[_k]


def frame_exceptions(part, exc=FRAME_EXC_RU):
    """{(bid, kw): reason} for the pairs of <part>.mapped.md whose value present() misses although the stated
    Russian form is in the segment (frame verbs), plus inherited pi-2 EXCEPTIONS that are really needed."""
    ru = read_russian(part)
    allowed = {}
    for line in (_HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        text = ru.get(bid, "")
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            k = lc(kw)
            if v == NDE or present(v, text):
                continue
            if k in exc and re.search(exc[k][0], text.lower()):
                allowed[(bid, kw)] = exc[k][1]
            elif k in EXCEPTIONS:
                allowed[(bid, kw)] = EXCEPTIONS[k]
    return allowed


if __name__ == "__main__":
    for p in (sys.argv[1:] or PARTS):
        build_part(p, resolver_for(p))
        verify(p, show=200, allowed=frame_exceptions(p))
