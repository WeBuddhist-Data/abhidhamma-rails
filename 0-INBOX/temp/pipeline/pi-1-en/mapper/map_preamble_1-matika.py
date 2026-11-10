"""English->Pali keyword map for pi-1 chapters `preamble` and `1-matika` (sample chapters).

usage: python -I -X utf8 map_preamble_1-matika.py
Writes <ch>.mapped.md next to <ch>.keywords.md. Keyword lookup is by lowercased keyword
(case variants such as "States dissociated"/"states dissociated" always share a value here).
NDE marks "(no direct equivalent)". Conventions: map-conventions.md.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
NDE = "(no direct equivalent)"


def m(**kw):
    return kw


# ---------------------------------------------------------------- preamble
PRE = {
    "0": {"abhidhamma": "Abhidhamma", "abhidhamma piṭaka": "Abhidhammapiṭake"},
    "1-0": {"enumeration": "saṅgaṇī", "enumeration of phenomena": "Dhammasaṅgaṇī",
            "phenomena": "Dhamma"},
    "T-1": {"awakened": "sambuddhassa", "awakened buddha": "sambuddhassa", "blessed": "bhagavato",
            "buddha": "sambuddhassa", "fully": "sammā", "fully awakened": "sammāsambuddhassa",
            "fully awakened buddha": "sammāsambuddhassa", "homage": "Namo", "worthy": "arahato"},
}

# ---------------------------------------------------------------- matrix
MAT = {}

# headings
MAT["1-M-0"] = {"matrix": "Mātikā"}
MAT["1-M-1-0"] = {"matrix": "mātikā"}
MAT["1-M-2-0"] = {"matrix": "mātikā", "pairs": "Duka"}
MAT["1-M-2-1-0"] = {"roots": "Hetu"}
MAT["1-M-2-2-0"] = {"intermediate": "antara", "intermediate pairs": "antaradukaṃ", "pairs": "dukaṃ"}
MAT["1-M-2-3-0"] = {"taints": "Āsava"}
MAT["1-M-2-4-0"] = {"fetters": "Saṃyojana"}
MAT["1-M-2-5-0"] = {"ties": "Gantha"}
MAT["1-M-2-6-0"] = {"floods": "Ogha"}
MAT["1-M-2-7-0"] = {"yokes": "Yoga"}
MAT["1-M-2-8-0"] = {"hindrances": "Nīvaraṇa"}
MAT["1-M-2-9-0"] = {"misapprehension": "Parāmāsa"}
MAT["1-M-2-10-0"] = {"intermediate": "antara", "intermediate pairs": "antaradukaṃ", "pairs": "dukaṃ"}
MAT["1-M-2-11-0"] = {"clinging": "Upādāna"}
MAT["1-M-2-12-0"] = {"defilements": "Kilesa"}
MAT["1-M-2-13-0"] = {"closing": "Piṭṭhi", "pairs": "dukaṃ"}
MAT["1-M-2-14-0"] = {"discourse": "Suttantika", "matrix": "mātikā", "pairs": "duka"}

# ---- triads
MAT["1-M1-1"] = {"indeterminate": "abyākatā", "indeterminate states": "abyākatā dhammā",
                 "unwholesome": "akusalā", "unwholesome states": "akusalā dhammā",
                 "wholesome": "kusalā", "wholesome states": "kusalā dhammā"}
MAT["1-M1-2"] = {"associated": "sampayuttā", "feeling": "vedanāya", "painful": "dukkhāya",
                 "painful feeling": "dukkhāya vedanāya", "painful nor pleasant": "adukkhamasukhāya",
                 "pleasant": "sukhāya", "pleasant feeling": "sukhāya vedanāya"}
MAT["1-M1-3"] = {"produce": "vipākadhamma", "produce results": "vipākadhamma",
                 "states that produce": "vipākadhammadhammā"}
MAT["1-M1-4"] = {"action and subject": "upādiṇṇupādāniyā", "action but subject": "anupādiṇṇupādāniyā",
                 "clinging": "upādāniyā", "past action": "upādiṇṇa", "produced": "upādiṇṇa",
                 "produced by past": "upādiṇṇa", "states neither produced": "anupādiṇṇaanupādāniyā dhammā",
                 "states not produced": "anupādiṇṇupādāniyā dhammā", "states produced": "upādiṇṇupādāniyā dhammā",
                 "subject to clinging": "upādāniyā", "variant": NDE}
MAT["1-M1-5"] = {"defiled": "saṃkiliṭṭha", "defilement": "saṃkilesikā", "subject to defilement": "saṃkilesikā",
                 "undefiled": "asaṃkiliṭṭha", "variant": NDE}
MAT["1-M1-6"] = {"applied": "vitakka", "applied thought": "vitakka",
                 "states with applied": "savitakkasavicārā dhammā",
                 "states without applied": "avitakkavicāramattā dhammā",
                 "sustained": "vicāra", "sustained thought": "vicāra", "thought": "vitakka / vicāra",
                 "variant": NDE}
MAT["1-M1-7"] = {"accompanied": "sahagatā", "accompanied by equanimity": "upekkhāsahagatā",
                 "accompanied by happiness": "sukhasahagatā", "accompanied by rapture": "pītisahagatā",
                 "equanimity": "upekkhā", "happiness": "sukha", "rapture": "pīti",
                 "states accompanied": "sahagatā dhammā"}
MAT["1-M1-8"] = {"abandoned": "pahātabbā", "abandoned by development": "bhāvanāya pahātabbā",
                 "seeing": "dassanena"}
MAT["1-M1-9"] = {"abandoned": "pahātabba", "abandoned by development": "bhāvanāya pahātabba",
                 "roots": "hetukā", "seeing": "dassanena", "states whose roots": "hetukā dhammā"}
MAT["1-M1-10"] = {"accumulation": "ācaya", "away": "apacaya", "states leading": "gāmino dhammā",
                  "variant": NDE}
MAT["1-M1-11"] = {"beyond": "asekkhā", "training": "sekkhā", "variant": NDE}
MAT["1-M1-12"] = {"exalted": "mahaggatā", "exalted states": "mahaggatā dhammā",
                  "immeasurable": "appamāṇā", "immeasurable states": "appamāṇā dhammā",
                  "limited": "parittā", "limited states": "parittā dhammā"}
MAT["1-M1-13"] = {"exalted": "mahaggata", "exalted object": "mahaggatārammaṇā",
                  "immeasurable": "appamāṇa", "immeasurable object": "appamāṇārammaṇā",
                  "limited": "paritta", "limited object": "parittārammaṇā", "object": "ārammaṇā"}
MAT["1-M1-14"] = {"inferior": "hīnā", "inferior states": "hīnā dhammā", "middling": "majjhimā",
                  "middling states": "majjhimā dhammā", "superior": "paṇītā",
                  "superior states": "paṇītā dhammā"}
MAT["1-M1-15"] = {"fixed": "niyatā", "rightness": "sammatta", "states fixed": "niyatā dhammā",
                  "wrongness": "micchatta"}
MAT["1-M1-16"] = {"dominant": "adhipatino", "dominant factor": "adhipatino", "factor": "adhipatino",
                  "object": "ārammaṇā", "path": "magga", "root": "hetukā"}
MAT["1-M1-17"] = {"arise": "uppādino", "arisen": "uppannā", "arisen states": "uppannā dhammā",
                  "bound": "uppādino"}
MAT["1-M1-18"] = {"future states": "anāgatā dhammā", "past states": "atītā dhammā",
                  "present states": "paccuppannā dhammā"}
MAT["1-M1-19"] = {"future object": "anāgatārammaṇā", "object": "ārammaṇā",
                  "past object": "atītārammaṇā", "present object": "paccuppannārammaṇā"}
MAT["1-M1-20"] = {"others": "bahiddhā", "others' states": "bahiddhā dhammā"}
MAT["1-M1-21"] = {"object": "ārammaṇā", "others": "bahiddhā", "others' states": "bahiddhā",
                  "states as object": "ārammaṇā"}
MAT["1-M1-22"] = {"invisible": "anidassana", "make impact": "sappaṭighā", "matrix": "mātikā",
                  "variant": NDE, "visible": "sanidassana"}

# ---- roots group
MAT["1-M2-1"] = {"roots": "hetū"}
MAT["1-M2-2"] = {"roots": "hetukā", "states with roots": "sahetukā dhammā",
                 "states without roots": "ahetukā dhammā"}
MAT["1-M2-3"] = {"associated": "sampayuttā", "dissociated": "vippayuttā", "roots": "hetu",
                 "states dissociated": "vippayuttā dhammā"}
MAT["1-M2-4"] = {"roots": "hetū"}
MAT["1-M2-5"] = {"associated": "sampayuttā", "roots": "hetū"}
MAT["1-M2-6"] = {"roots": "hetū"}

# ---- short intermediate pairs
MAT["1-M2-7"] = {"states without conditions": "appaccayā dhammā"}
MAT["1-M2-8"] = {"conditioned": "saṅkhatā", "conditioned states": "saṅkhatā dhammā",
                 "unconditioned": "asaṅkhatā", "unconditioned states": "asaṅkhatā dhammā"}
MAT["1-M2-9"] = {"invisible": "anidassanā", "invisible states": "anidassanā dhammā",
                 "visible": "sanidassanā", "visible states": "sanidassanā dhammā"}
MAT["1-M2-10"] = {"make impact": "sappaṭighā", "states that make": "sappaṭighā dhammā"}
MAT["1-M2-11"] = {"immaterial": "arūpino", "immaterial states": "arūpino dhammā",
                  "material": "rūpino", "material states": "rūpino dhammā"}
MAT["1-M2-12"] = {"states that transcend": "lokuttarā dhammā", "transcend": "uttarā",
                  "worldly": "lokiyā", "worldly states": "lokiyā dhammā"}
MAT["1-M2-13"] = {"cannot": "na", "consciousness": NDE, "intermediate": "antara",
                  "intermediate pairs": "antaradukaṃ", "kinds": NDE, "know": "viññeyyā",
                  "pairs": "dukaṃ"}


# ---- the six-pair groups (taints, fetters, ties, floods, yokes, hindrances, clinging)
def group(start, names, base, plain, subj, nsubj, s1_name_val=None):
    """names: the English keyword(s) for the group noun (e.g. ['taints'] or
    ['clinging', 'kinds', 'kinds of clinging']); the first is the noun used in fragments."""
    n = names[0]
    out = {}
    # s0: X / not X
    out[start] = {k: plain for k in names}
    # s1: subject to X / not subject (free of) X
    d = {k: (s1_name_val or subj) for k in names}
    d.update({f"subject to {n}": subj, "states subject": f"{subj} dhammā",
              "states not subject": f"{nsubj} dhammā",
              "free": nsubj, f"free of {n}": nsubj, "states free": f"{nsubj} dhammā"})
    out[start + 1] = d
    # s2: associated / dissociated
    d = {k: base for k in names}
    d.update({"associated": "sampayuttā", "dissociated": "vippayuttā",
              f"dissociated from {n}": f"{base}vippayuttā", "states dissociated": "vippayuttā dhammā"})
    out[start + 2] = d
    # s3: both X and subject / subject but not X
    d = {k: plain for k in names}
    d.update({f"subject to {n}": subj, f"{n} and subject": f"{plain} ceva dhammā {subj}"})
    out[start + 3] = d
    # s4: both X and associated / associated but not X
    d = {k: plain for k in names}
    d.update({"associated": "sampayuttā"})
    out[start + 4] = d
    # s5: dissociated but subject / dissociated and not subject (free)
    d = {k: base for k in names}
    d.update({"dissociated": "vippayuttā", f"dissociated from {n}": f"{base}vippayuttā",
              f"{n} but subject": f"{base}vippayuttā kho pana dhammā {subj}",
              "states dissociated": "vippayuttā kho pana dhammā", f"subject to {n}": subj,
              "free": nsubj, f"free of {n}": nsubj})
    out[start + 5] = d
    for i, v in out.items():
        MAT[f"1-M2-{i}"] = v


group(14, ["taints"], "āsava", "āsavā", "sāsavā", "anāsavā", s1_name_val="āsavā")
group(20, ["fetters"], "saṃyojana", "saṃyojanā", "saṃyojaniyā", "asaṃyojaniyā")
group(26, ["ties"], "gantha", "ganthā", "ganthaniyā", "aganthaniyā")
group(32, ["floods"], "ogha", "oghā", "oghaniyā", "anoghaniyā")
group(38, ["yokes"], "yoga", "yogā", "yoganiyā", "ayoganiyā")
group(44, ["hindrances"], "nīvaraṇa", "nīvaraṇā", "nīvaraṇiyā", "anīvaraṇiyā")
group(69, ["clinging", "kinds", "kinds of clinging"], "upādāna", "upādānā", "upādāniyā", "anupādāniyā")

# ---- misapprehension (five pairs)
MAT["1-M2-50"] = {"misapprehensions": "parāmāsā"}
MAT["1-M2-51"] = {"misapprehended": "parāmaṭṭhā", "misapprehended states": "parāmaṭṭhā dhammā"}
MAT["1-M2-52"] = {"associated": "sampayuttā", "dissociated": "vippayuttā",
                  "dissociated from misapprehension": "parāmāsavippayuttā", "misapprehension": "parāmāsa",
                  "states dissociated": "vippayuttā dhammā"}
MAT["1-M2-53"] = {"misapprehended": "parāmaṭṭhā", "misapprehensions": "parāmāsā"}
MAT["1-M2-54"] = {"dissociated": "vippayuttā", "dissociated from misapprehension": "parāmāsavippayuttā",
                  "misapprehended": "parāmaṭṭhā", "misapprehension": "parāmāsa",
                  "states dissociated": "vippayuttā kho pana dhammā"}

# ---- long intermediate pairs
MAT["1-M2-55"] = {"object": "ārammaṇā"}
MAT["1-M2-56"] = {"mind": "cittā"}
MAT["1-M2-57"] = {"factors": "cetasikā", "mental": "cetasikā", "mental factors": "cetasikā"}
MAT["1-M2-58"] = {"associated": "sampayuttā", "dissociated": "vippayuttā",
                  "dissociated from mind": "cittavippayuttā", "mind": "citta",
                  "states dissociated": "vippayuttā dhammā"}
MAT["1-M2-59"] = {"joined": "saṃsaṭṭhā", "joined with mind": "cittasaṃsaṭṭhā", "mind": "citta",
                  "states joined": "saṃsaṭṭhā dhammā", "states not joined": "visaṃsaṭṭhā dhammā"}
MAT["1-M2-60"] = {"arising": "samuṭṭhānā", "arising from mind": "cittasamuṭṭhānā", "mind": "citta",
                  "states arising": "samuṭṭhānā dhammā", "states not arising": "no cittasamuṭṭhānā dhammā"}
MAT["1-M2-61"] = {"existing": "bhuno", "mind": "citta", "states existing": "bhuno dhammā",
                  "states not existing": "no cittasahabhuno dhammā", "together": "saha"}
MAT["1-M2-62"] = {"accompanying": "anuparivattino", "accompanying mind": "cittānuparivattino",
                  "mind": "citta", "states accompanying": "anuparivattino dhammā",
                  "states accompanying mind": "cittānuparivattino dhammā",
                  "states not accompanying": "no cittānuparivattino dhammā"}
MAT["1-M2-63"] = {"arising": "samuṭṭhānā", "arising from mind": "cittasaṃsaṭṭhasamuṭṭhānā",
                  "joined": "saṃsaṭṭha", "mind": "citta",
                  "states joined": "saṃsaṭṭhasamuṭṭhānā dhammā",
                  "states not joined": "no cittasaṃsaṭṭhasamuṭṭhānā dhammā"}
MAT["1-M2-64"] = {"arising": "samuṭṭhāna", "existing": "bhuno", "joined": "saṃsaṭṭha", "mind": "citta",
                  "states joined": "saṃsaṭṭhasamuṭṭhānasahabhuno dhammā",
                  "states not joined": "no cittasaṃsaṭṭhasamuṭṭhānasahabhuno dhammā", "together": "saha"}
MAT["1-M2-65"] = {"accompanying": "anuparivattino", "accompanying mind": "cittasaṃsaṭṭhasamuṭṭhānānuparivattino",
                  "arising": "samuṭṭhāna", "joined": "saṃsaṭṭha", "mind": "citta",
                  "states joined": "saṃsaṭṭhasamuṭṭhānānuparivattino dhammā",
                  "states not joined": "no cittasaṃsaṭṭhasamuṭṭhānānuparivattino dhammā"}
MAT["1-M2-66"] = {"external": "bāhirā", "external states": "bāhirā dhammā", "internal": "ajjhattikā",
                  "internal states": "ajjhattikā dhammā"}
MAT["1-M2-67"] = {"derived": "upādā", "derived states": "upādā dhammā"}
MAT["1-M2-68"] = {"intermediate": "antara", "intermediate pairs": "antaradukaṃ", "pairs": "dukaṃ",
                  "past action": "upādiṇṇā", "produced": "upādiṇṇā", "produced by past": "upādiṇṇā",
                  "states not produced": "anupādiṇṇā dhammā", "states produced": "upādiṇṇā dhammā",
                  "variant": NDE}

# ---- defilements (eight pairs)
MAT["1-M2-75"] = {"defilements": "kilesā"}
MAT["1-M2-76"] = {"defilement": "saṃkilesikā", "states not subject": "asaṃkilesikā dhammā",
                  "states subject": "saṃkilesikā dhammā", "subject to defilement": "saṃkilesikā"}
MAT["1-M2-77"] = {"defiled": "saṃkiliṭṭhā", "defiled states": "saṃkiliṭṭhā dhammā",
                  "undefiled": "asaṃkiliṭṭhā", "undefiled states": "asaṃkiliṭṭhā dhammā"}
MAT["1-M2-78"] = {"associated": "sampayuttā", "defilements": "kilesa", "dissociated": "vippayuttā",
                  "dissociated from defilements": "kilesavippayuttā",
                  "states dissociated": "vippayuttā dhammā"}
MAT["1-M2-79"] = {"defilement": "saṃkilesikā", "defilements": "kilesā", "subject to defilement": "saṃkilesikā"}
MAT["1-M2-80"] = {"defiled": "saṃkiliṭṭhā", "defilements": "kilesā"}
MAT["1-M2-81"] = {"associated": "sampayuttā", "defilements": "kilesā"}
MAT["1-M2-82"] = {"defilement": "saṃkilesikā", "defilements": "kilesa",
                  "defilements but subject": "kilesavippayuttā kho pana dhammā saṃkilesikā",
                  "dissociated": "vippayuttā", "dissociated from defilements": "kilesavippayuttā",
                  "states dissociated": "vippayuttā kho pana dhammā", "subject to defilement": "saṃkilesikā"}

# ---- closing pairs
MAT["1-M2-83"] = {"abandoned": "pahātabbā", "seeing": "dassanena"}
MAT["1-M2-84"] = {"abandoned": "pahātabbā", "abandoned by development": "bhāvanāya pahātabbā"}
MAT["1-M2-85"] = {"abandoned": "pahātabba", "roots": "hetukā", "seeing": "dassanena",
                  "states whose roots": "hetukā dhammā"}
MAT["1-M2-86"] = {"abandoned": "pahātabba", "abandoned by development": "bhāvanāya pahātabba",
                  "roots": "hetukā", "states whose roots": "hetukā dhammā"}
MAT["1-M2-87"] = {"applied": "vitakkā", "applied thought": "vitakkā", "states with applied": "savitakkā dhammā",
                  "states without applied": "avitakkā dhammā", "thought": "vitakkā"}
MAT["1-M2-88"] = {"states with sustained": "savicārā dhammā", "states without sustained": "avicārā dhammā",
                  "sustained": "vicārā", "sustained thought": "vicārā", "thought": "vicārā"}
MAT["1-M2-89"] = {"rapture": "pītikā", "states with rapture": "sappītikā dhammā",
                  "states without rapture": "appītikā dhammā"}
for i, (stem, nm) in {90: ("pīti", "rapture"), 91: ("sukha", "happiness"), 92: ("upekkhā", "equanimity")}.items():
    MAT[f"1-M2-{i}"] = {"accompanied": "sahagatā", f"accompanied by {nm}": f"{stem}sahagatā", nm: stem,
                        "states accompanied": "sahagatā dhammā",
                        "states not accompanied": f"na {stem}sahagatā dhammā"}
MAT["1-M2-93"] = {"sense": "kāma", "sense sphere": "kāmāvacarā", "sphere": "avacarā"}
MAT["1-M2-94"] = {"fine-material": "rūpa", "fine-material sphere": "rūpāvacarā", "sphere": "avacarā"}
MAT["1-M2-95"] = {"immaterial": "arūpa", "immaterial sphere": "arūpāvacarā", "sphere": "avacarā"}
MAT["1-M2-96"] = {"existence": NDE, "spheres": NDE, "spheres of existence": NDE,
                  "states included": "pariyāpannā dhammā", "states not included": "apariyāpannā dhammā"}
MAT["1-M2-97"] = {"lead to liberation": "niyyānikā", "liberation": "niyyānikā",
                  "states that lead": "niyyānikā dhammā"}
MAT["1-M2-98"] = {"fixed": "niyatā", "fixed states": "niyatā dhammā"}
MAT["1-M2-99"] = {"surpassable": "sauttarā", "surpassable states": "sauttarā dhammā",
                  "unsurpassable": "anuttarā", "unsurpassable states": "anuttarā dhammā"}
MAT["1-M2-100"] = {"abhidhamma": "Abhidhamma", "closing": "Piṭṭhi", "conflict": "raṇā", "matrix": "mātikā",
                   "pairs": "dukaṃ", "states with conflict": "saraṇā dhammā",
                   "states without conflict": "araṇā dhammā"}

# ---- discourse pairs
MAT["1-M2-101"] = {"ignorance": "avijjā", "knowledge": "vijjā", "states that share": "bhāgino dhammā",
                   "true": "vijjā", "true knowledge": "vijjā"}
MAT["1-M2-102"] = {"diamond": "vajira", "lightning": "vijju", "like": "upamā",
                   "states like lightning": "vijjūpamā dhammā"}
MAT["1-M2-103"] = {"foolish": "bālā", "foolish states": "bālā dhammā", "wise": "paṇḍitā",
                   "wise states": "paṇḍitā dhammā"}
MAT["1-M2-104"] = {"bright": "sukkā", "bright states": "sukkā dhammā", "dark": "kaṇhā",
                   "dark states": "kaṇhā dhammā"}
MAT["1-M2-105"] = {"cause": "tapanīyā", "torment": "tapanīyā"}
MAT["1-M2-106"] = {"names": "adhivacanā", "pathways": "pathā"}
MAT["1-M2-107"] = {"expressions": "nirutti", "pathways": "pathā"}
MAT["1-M2-108"] = {"designations": "paññatti", "pathways": "pathā"}
MAT["1-M2-109"] = {"form": "rūpañca", "material": "rūpañca", "material form": "rūpañca",
                   "mentality": "nāmañca"}
MAT["1-M2-110"] = {"continued existence": "bhava", "craving": "taṇhā", "existence": "bhava",
                   "ignorance": "avijjā"}
MAT["1-M2-111"] = {"continued existence": "bhava", "existence": "bhava", "non-existence": "vibhava",
                   "view": "diṭṭhi"}
MAT["1-M2-112"] = {"annihilationist": "uccheda", "annihilationist view": "ucchedadiṭṭhi",
                   "eternalist": "sassata", "eternalist view": "sassatadiṭṭhi", "view": "diṭṭhi"}
MAT["1-M2-113"] = {"view": "diṭṭhi"}
MAT["1-M2-114"] = {"concerning": "anudiṭṭhi", "view": "diṭṭhi"}
MAT["1-M2-115"] = {"fearlessness": "anottappañca", "fearlessness of wrongdoing": "anottappañca",
                   "shamelessness": "ahirikañca", "wrongdoing": "anottappañca"}
MAT["1-M2-116"] = {"fear": "ottappañca", "fear of wrongdoing": "ottappañca", "moral": "hirī",
                   "moral shame": "hirī", "shame": "hirī", "wrongdoing": "ottappañca"}
MAT["1-M2-117"] = {"bad": "pāpa", "correct": "vacassatā", "friends": "mittatā", "hard": "dovacassatā",
                   "having": NDE}
MAT["1-M2-118"] = {"correct": "vacassatā", "easy": "sovacassatā", "friends": "mittatā", "having": NDE}
MAT["1-M2-119"] = {"emerging": "vuṭṭhāna", "offences": "āpatti", "regarding": NDE, "skill": "kusalatā",
                   "skill in emerging": "vuṭṭhānakusalatā"}
MAT["1-M2-120"] = {"attainments": "samāpatti", "emerging": "vuṭṭhāna", "meditative": "samāpatti",
                   "meditative attainments": "samāpatti", "skill": "kusalatā",
                   "skill in emerging": "vuṭṭhānakusalatā"}
MAT["1-M2-121"] = {"attention": "manasikāra", "elements": "dhātu", "skill": "kusalatā",
                   "skill in attention": "manasikārakusalatā"}
MAT["1-M2-122"] = {"bases": "āyatana", "dependent": "paṭicca", "origination": "samuppāda",
                   "sense": "āyatana", "sense bases": "āyatana", "skill": "kusalatā"}
MAT["1-M2-123"] = {"impossible": "aṭṭhāna", "skill": "kusalatā"}
MAT["1-M2-124"] = {"mildness": "maddavo", "straightforwardness": "ajjavo"}
MAT["1-M2-125"] = {"gentleness": "soraccañca", "patience": "khanti"}
MAT["1-M2-126"] = {"courtesy": "sākhalyañca", "hospitality": "paṭisanthāro", "variant": NDE}
for i in (127, 128):
    MAT[f"1-M2-{i}"] = {"doors": "dvāratā", "eating": "bhojane", "guarding": "gutta", "knowing": "ññutā",
                        "knowing moderation": "mattaññutā", "moderation": "matta", "senses": "indriyesu"}
MAT["1-M2-129"] = {"awareness": "sampajaññañca", "clear": "sampajaññañca", "clear awareness": "sampajaññañca",
                   "forgetfulness": "muṭṭhasaccañca", "lack": "asampajaññañca"}
MAT["1-M2-130"] = {"awareness": "sampajaññañca", "clear": "sampajaññañca", "clear awareness": "sampajaññañca",
                   "mindfulness": "sati"}
MAT["1-M2-131"] = {"power": "balañca", "reflection": "paṭisaṅkhāna"}
MAT["1-M2-132"] = {"calm": "samatho", "insight": "vipassanā"}
MAT["1-M2-133"] = {"calm": "samatha", "exertion": "paggāha", "sign": "nimittañca"}
MAT["1-M2-134"] = {"exertion": "paggāho", "non-distraction": "avikkhepo"}
MAT["1-M2-135"] = {"failure": "vipatti", "morality": "sīla", "view": "diṭṭhi"}
MAT["1-M2-136"] = {"accomplishment": "sampadā", "morality": "sīla", "view": "diṭṭhi"}
MAT["1-M2-137"] = {"morality": "sīla", "purification": "visuddhi", "view": "diṭṭhi"}
MAT["1-M2-138"] = {"effort": "padhānaṃ", "keeping": "yathā", "purification": "visuddhi", "view": "diṭṭhi"}
MAT["1-M2-139"] = {"effort": "padhānaṃ", "sense": "saṃvego", "stir": "saṃvejaniyesu",
                   "stirred": "saṃviggassa", "things": "ṭhānesu", "urgency": "saṃvego", "wise": "yoniso"}
MAT["1-M2-140"] = {"content": "santuṭṭhitā", "effort": "padhānasmiṃ", "wholesome": "kusalesu",
                   "wholesome states": "kusalesu dhammesu"}
MAT["1-M2-141"] = {"knowledge": "vijjā", "liberation": "vimutti", "true": "vijjā", "true knowledge": "vijjā"}
MAT["1-M2-142"] = {"complete": "niṭṭhitā", "destruction": "khaye", "discourse": "Suttantika",
                   "knowledge": "ñāṇaṃ", "matrix": "mātikā", "non-arising": "anuppāde", "pairs": "duka",
                   "variant": NDE}


def build(ch, table):
    src = (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()
    out, missing, unused = [], [], []
    for line in src:
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        d = table[bid]
        kws = [k.strip() for k in rest.split(", ")]
        pairs = []
        for k in kws:
            v = d.get(k.lower())
            if v is None:
                missing.append((bid, k))
                v = "???"
            assert ", " not in v, (bid, k, v)
            pairs.append(f"{v}={k}")
        used = {k.lower() for k in kws}
        unused += [(bid, k) for k in d if k not in used]
        out.append(f"[{bid}] " + ", ".join(pairs))
    assert not missing, missing
    (HERE / f"{ch}.mapped.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(ch, "lines", len(out), "unused table keys", unused)


if __name__ == "__main__":
    build("preamble", PRE)
    build("1-matika", MAT)
