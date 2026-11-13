"""pi-6 Anusayayamaka (7-01 … 7-11) Pāli->Hindi keyword maps: the shared Anusaya table.

Importing this module writes nothing and prints nothing. It imports map_sample_hi read-only.

    import sys, pathlib; sys.dont_write_bytecode = True
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from map_7_common_hi import *        # T7, TABLE7 (= {**PI6, **T7}), present7, verify7, + all of map_sample_hi
    T = {...}                             # your chapter entries (lower-case first letter keys)
    build_part(f, make_resolver(f, {**TABLE7, **T}, OVR))
    verify7(f, allowed={(bid, kw): reason})

Decisions (Hindi from notes-7a.md / the translation files; pi-1/2/6 conventions):
- the seven anusayas, every case form (-o, -ena, -aṃ, -añca via the module's -ñca strip, -ā): «X की सुप्त प्रवृत्ति»
  (pi-2 ^2-949); anusaya / anusayo / anusayā = सुप्त प्रवृत्ति (pi-2, singular rule); Sattānusayā = सात सुप्त
  प्रवृत्ति (numeral + singular, as pi-2 Sattarasindriyā = सत्रह क्षमता, pi-6 Pañcakkhandhā = पाँच समूह).
- anuseti / anusenti = सोया रहना (pi-2 anuseti = सोया रहना on «सोई रहती है»); fused negative nānuseti / nānusenti =
  सोया नहीं रहना (pi-6 nuppajjati rule). The text has the feminine «सोई» (subject सुप्त प्रवृत्ति): present7 accepts
  सोया ~ सोई / सोए (the same kind of tolerance as the module's हुआ था ~ हुई थी).
- sānusayo / -ā = सुप्त प्रवृत्ति वाला (heading Sānusayavāro «सुप्त प्रवृत्ति वाला होने का खंड»), niranusayo / -ā =
  सुप्त प्रवृत्ति से मुक्त (text «X की सुप्त प्रवृत्ति वाला है / से मुक्त है»); masc. sg.
- pajahati / pajahanti = छोड़ना, nappajahati / nappajahanti = नहीं छोड़ना (text «को नहीं छोड़ता»);
  parijānāti / parijānanti = पूरी तरह समझना; pahīno / pahīnā = छोड़ा जा चुका, appahīno / appahīnā = छोड़ा नहीं गया
  (text «छोड़ी जा चुकी है», «छोड़ी नहीं गई है»; the pi-1 check already accepts these feminine forms).
- persons, direct case: Anāgāmī / Anāgāmissa = फिर न लौटने वाला, Puthujjano / -assa = साधारण व्यक्ति, Arahā /
  Arahato = अर्हत्, puggalo / puggalā / puggalānaṃ / puggalassa = व्यक्ति, Aṭṭhamako = आठवें स्तर का व्यक्ति (pi-5),
  X-maggasamaṅgī (any case) = «X मार्ग से युक्त व्यक्ति» (pi-5 maggasamaṅgī = मार्ग से युक्त व्यक्ति).
- places, direct case: Kāmadhātuyā = इंद्रिय-सुखों का लोक, rūpadhātuyā = सूक्ष्म भौतिक लोक, arūpadhātuyā = अभौतिक
  लोक (pi-2); dvīsu / tīsu vedanāsu = दो / तीन अनुभूति (numeral + singular); dukkhāya vedanāya = दुःखद अनुभूति (PI2).
- headings: notes-7a.md and the Hindi headings; X-vāre (in «X-vāre anulomaṃ / paṭilomaṃ») = the vāra name.
- Natthi = ऐसा कोई नहीं (PI6; harmonise I4 made it «ऐसा कोई नहीं है।» in 7-01 … 7-11).
- RULE (coordinator, all pi-6 Hindi mappers): the keyword «(no direct equivalent)» in the Pāli keyword lists is an
  artefact (an English keyword that had no Pāli), not a Pāli word. Keep it in place and map it as
  `(no direct equivalent)=(no direct equivalent)`, never to a Hindi word (not «व्यक्ति», even where the Hindi has
  «जो व्यक्ति»; not «स्थान»). T7 does this; do not override it.
"""
import itertools
import pathlib
import re
import sys

sys.dont_write_bytecode = True
_HERE = pathlib.Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))
from map_sample_hi import *  # noqa: F401,F403,E402  (read-only import)
from map_sample_hi import PI6, NDE, HERE, read_hindi, present  # noqa: E402

T7 = {NDE: NDE}                             # the «(no direct equivalent)» keyword: an artefact, never a Hindi word

# --- the seven anusayas (pi-2 ^2-949)
ANUSAYA = {"kāmarāg": "इंद्रिय-सुखों के राग", "kāmārāg": "इंद्रिय-सुखों के राग",   # kāmārāga: source slip
           "paṭigh": "चिढ़", "mān": "अहंकार", "diṭṭh": "दृष्टि", "vicikicch": "संशय",
           "bhavarāg": "अस्तित्व के राग", "avijj": "अज्ञान"}
for _st, _h in ANUSAYA.items():
    for _e in ("o", "ena", "aṃ", "ā", "assa", "ānaṃ", "a", "e"):
        T7[f"{_st}ānusay{_e}"] = f"{_h} की सुप्त प्रवृत्ति"
T7.update({
    "anusaya": "सुप्त प्रवृत्ति", "anusayo": "सुप्त प्रवृत्ति", "anusayā": "सुप्त प्रवृत्ति",
    "anusayaṃ": "सुप्त प्रवृत्ति", "anusayena": "सुप्त प्रवृत्ति", "anusayānaṃ": "सुप्त प्रवृत्ति",
    "sattānusayā": "सात सुप्त प्रवृत्ति",
})

# --- predicates
T7.update({
    "anuseti": "सोया रहना", "anusenti": "सोया रहना", "anusanti": "सोया रहना",          # anusanti: source slip
    "nānuseti": "सोया नहीं रहना", "nānusenti": "सोया नहीं रहना",
    "sānusayo": "सुप्त प्रवृत्ति वाला", "sānusayā": "सुप्त प्रवृत्ति वाला", "sānusaya": "सुप्त प्रवृत्ति वाला",
    "niranusayo": "सुप्त प्रवृत्ति से मुक्त", "niranusayā": "सुप्त प्रवृत्ति से मुक्त",
    "niranusaya": "सुप्त प्रवृत्ति से मुक्त",
    "pajahati": "छोड़ना", "pajahanti": "छोड़ना", "nappajahati": "नहीं छोड़ना", "nappajahanti": "नहीं छोड़ना",
    "parijānāti": "पूरी तरह समझना", "parijānanti": "पूरी तरह समझना",
    "pahīno": "छोड़ा जा चुका", "pahīnā": "छोड़ा जा चुका",
    "appahīno": "छोड़ा नहीं गया", "appahīnā": "छोड़ा नहीं गया",
})

# --- persons (direct case; the text's «… में» / «… को» are postpositions)
T7.update({
    "anāgāmī": "फिर न लौटने वाला", "anāgāmissa": "फिर न लौटने वाला", "anāgāmino": "फिर न लौटने वाला",
    "anāgāmiṃ": "फिर न लौटने वाला",
    "puthujjano": "साधारण व्यक्ति", "puthujjanassa": "साधारण व्यक्ति", "puthujjanaṃ": "साधारण व्यक्ति",
    "puthujjanānaṃ": "साधारण व्यक्ति",
    "arahā": "अर्हत्", "arahato": "अर्हत्", "arahantaṃ": "अर्हत्",
    "puggalo": "व्यक्ति", "puggalā": "व्यक्ति", "puggalānaṃ": "व्यक्ति", "puggalassa": "व्यक्ति",
    "puggalaṃ": "व्यक्ति",
    "aṭṭhamako": "आठवें स्तर का व्यक्ति", "aṭṭhamakaṃ": "आठवें स्तर का व्यक्ति",
    "aṭṭhamakassa": "आठवें स्तर का व्यक्ति",
})
for _p, _h in (("", "मार्ग से युक्त व्यक्ति"), ("agga", "सर्वोच्च मार्ग से युक्त व्यक्ति"),
               ("anāgāmi", "फिर न लौटने के मार्ग से युक्त व्यक्ति")):
    for _e in ("ī", "iṃ", "issa", "īnaṃ", "ino"):
        T7[f"{_p}maggasamaṅg{_e}"] = _h

# --- places (direct case)
T7.update({
    "kāmadhātuyā": "इंद्रिय-सुखों का लोक", "kāmadhātuṃ": "इंद्रिय-सुखों का लोक", "kāmadhātu": "इंद्रिय-सुखों का लोक",
    "rūpadhātuyā": "सूक्ष्म भौतिक लोक", "rūpadhātuṃ": "सूक्ष्म भौतिक लोक", "rūpadhātu": "सूक्ष्म भौतिक लोक",
    "arūpadhātuyā": "अभौतिक लोक", "arūpadhātuṃ": "अभौतिक लोक", "arūpadhātu": "अभौतिक लोक",
    "dvīsu vedanāsu": "दो अनुभूति", "tīsu vedanāsu": "तीन अनुभूति", "vedanāsu": "अनुभूति",
    "dukkhāya vedanāya": "दुःखद अनुभूति", "sabbattha": "सब जगह",
})

# --- headings (notes-7a.md; the Hindi headings of 7-01 … 7-11)
_VARA = {"uppattiṭṭhāna": "उत्पन्न होने के स्थान का खंड", "mahā": "बड़ा खंड",
         "anusaya": "सुप्त प्रवृत्तियों का खंड", "sānusaya": "सुप्त प्रवृत्ति वाला होने का खंड",
         "pajahana": "छोड़ने का खंड", "pajahanā": "छोड़ने का खंड", "pariññā": "पूरी तरह समझने का खंड",
         "pahīna": "छोड़ा जा चुका होने का खंड", "uppajjana": "उत्पन्न होने का खंड",
         "dhātupucchā": "लोकों के बारे में प्रश्नों का खंड",
         "dhātuvisajjanā": "लोकों के बारे में उत्तरों का खंड", "dhātuvisajja": "लोकों के बारे में उत्तरों का खंड"}
for _p, _h in _VARA.items():
    for _e in ("vāro", "vāra", "vāre"):
        T7[f"{_p}{_e}"] = _h

TABLE7 = {**PI6, **T7}

# ---------------------------------------------------------------------------- presence check
# feminine / plural forms of masculine participles that the pi-1 check does not model (सोया ~ सोई / सोए)
_GENDER = {"सोया": ("सोई", "सोए")}


def present7(value, text):
    """map_sample_hi.present + सोया ~ सोई / सोए (the text agrees with the feminine सुप्त प्रवृत्ति)."""
    if present(value, text):
        return True
    toks = value.split(" ")
    opts = [(t,) + _GENDER.get(t, ()) for t in toks]
    if all(len(o) == 1 for o in opts):
        return False
    return any(present(" ".join(c), text) for c in itertools.product(*opts))


def verify7(f, show=60, allowed=None):
    """map_sample_hi.verify with present7. allowed: {(bid, kw): reason} listed, not counted."""
    allowed = allowed or {}
    a = [l.split("] ", 1) for l in (HERE / f"{f}.keywords.md").read_text(encoding="utf-8").splitlines()]
    b = [l.split("] ", 1) for l in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines()]
    assert [x[0] for x in a] == [x[0] for x in b]
    bad = [i for i, (x, y) in enumerate(zip(a, b))
           if len(x) > 1 and [k.strip() for k in x[1].split(", ")] != [k.split("=", 1)[0] for k in y[1].split(", ")]]
    hi = read_hindi(f)
    nde, miss, exc = 0, [], []
    for x in b:
        if len(x) < 2:
            continue
        bid, rest = x[0][1:], x[1]
        text = hi.get(bid)
        for pair in rest.split(", "):
            kw, v = pair.split("=", 1)
            if v == NDE:
                nde += 1
            elif text is None or not present7(v, text):
                (exc if (bid, kw) in allowed else miss).append((bid, kw, v))
    print(f, "lines", len(a), "bad", bad, "| no-direct-equivalent", nde, "| presence misses", len(miss),
          "| listed exceptions", len(exc))
    for m in miss[:show]:
        print("   MISS", *m)
    for e in exc:
        print("   EXC ", *e, "--", allowed[(e[0], e[1])])
    return bad, nde, miss
