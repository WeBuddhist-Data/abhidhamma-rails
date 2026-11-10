"""English->Pali keyword map for pi-1 chapter `2-02-cittuppadakandam`.

usage: python -I -X utf8 map_2-02-cittuppadakandam.py [--report]
Writes 2-02-cittuppadakandam.mapped.md next to the keywords file. Conventions: map-conventions.md.

Method. The English of 2-02 was built from the Pali by fixed phrase tables (build_2-01_2-02.py: PH,
N, KOTTHASA_*, EXACT), so every English keyword has a fixed set of possible Pali sources. CAND lists
them per keyword (lowercased; case variants share a value): (pattern, value). For each segment the
candidate whose pattern occurs FIRST in that segment's Pali wins (ties: the longer pattern), which
implements map-conventions §4 (first occurrence) and keeps identical formulaic segments identical.
A keyword whose list ends with NDE falls back to "(no direct equivalent)" when no pattern occurs;
any other keyword without a source raises an error (nothing is guessed silently).
"""
import pathlib, re, sys, collections

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
CH = "2-02-cittuppadakandam"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / f"{CH}.md"
NDE = "(no direct equivalent)"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def segments():
    """Same cleaning as check_preamble_1-matika.py: variant brackets, labels, heading marks removed."""
    segs, buf = {}, []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        mm = ID.search(line)
        buf.append(line[:mm.start()] if mm else line)
        if mm:
            t = " ".join(buf)
            t = re.sub(r"\[[^\]]*\]", " ", t)
            t = re.sub(r"\((Ka|Kha|Ga)\)", " ", t)
            t = re.sub(r"^#+\s*|\s#+\s", " ", t)
            segs[mm.group(1)] = re.sub(r"\s+", " ", t).strip()
            buf = []
    return segs


def same(*ps):
    """candidates whose value is the pattern itself"""
    return [(p, p) for p in ps]


THOUGHT = [("savitakkaṃ savicāraṃ", "vitakkaṃ / vicāraṃ"),        # 1st absorption, full
           ("vitakkavicārānaṃ", "vitakka / vicārānaṃ"),            # "with the stilling of ..."
           ("avitakkaṃ vicāramattaṃ", "vitakkaṃ / vicāra"),        # 2nd absorption of the fivefold method
           ("vicāro", "vicāro"),                                   # "sustained thought" (list item)
           ("subhanti", "subhanti")]                               # 'with the thought "beautiful"'
APPLIED = [("savitakkaṃ", "vitakkaṃ"), ("vitakkavicārānaṃ", "vitakka"), ("avitakkaṃ", "vitakkaṃ")]
SUSTAINED = [("savicāraṃ", "vicāraṃ"), ("vitakkavicārānaṃ", "vicārānaṃ"), ("vicāramattaṃ", "vicāra"),
             ("vicāro", "vicāro")]
FORM = [("arūpasaññī", "rūpa"), ("rūpī", "rūpī"), ("rūpasaññānaṃ", "rūpa")]
LIMITED = [("parittaṃ", "parittaṃ"), ("parittārammaṇaṃ", "paritta"), ("parittāni", "parittāni")]
IMMEAS = [("appamāṇaṃ", "appamāṇaṃ"), ("appamāṇārammaṇaṃ", "appamāṇa"), ("appamāṇāni", "appamāṇāni"),
          ("Appamāṇāni", "Appamāṇāni")]
DOMINANT = [("ādhipateyyaṃ", "adhipateyyaṃ")]
SIXTEEN = same("Soḷasakkhattukaṃ", "soḷasakkhattukaṃ", "soḷasakkhattukāni")
EIGHT = same("Aṭṭhakkhattukaṃ", "aṭṭhakkhattukaṃ")
SPHERE_FM = [("rūpūpapattiyā", "rūpa"), ("Rūpāvacara", "Rūpāvacara")]
SPHERE_IM = [("arūpūpapattiyā", "arūpa"), ("Arūpāvacara", "Arūpāvacara")]
BASE_INF = [("ākāsānañcāyatanaṃ", "ānañcāyatanaṃ"), ("ākāsānañcāyatanasaññā", "ānañcāyatana"),
            ("viññāṇañcāyatanaṃ", "viññāṇañcāyatanaṃ"), ("viññāṇañcāyatanasaññā", "viññāṇañcāyatana")]

CAND = {
    # ---- question / answer frame and tails
    "wholesome": same("kusalā", "kusalaṃ"),
    "wholesome states": [("dhammā kusalā", "dhammā kusalā")],
    "unwholesome": same("akusalehi"),
    "unwholesome states": same("akusalehi dhammehi"),
    "wholesome mind": same("kusalaṃ cittaṃ", "kusalaṃ"),
    # "mind": a real source (cetaso / cittaṃ / cittassa / citta-), else the English noun supplied with
    # the neuter kusalaṃ in "the wholesome mind of ..." (headings, closing lines) -> nde (§5)
    "mind": [("cetaso", "cetaso"), ("cittaṃ", "cittaṃ"), ("cittassekaggatā", "cittassa"),
             ("cittādhipateyyaṃ", "citta"), NDE],
    "contact": same("phasso", "Phasso"),
    "non-distraction": same("avikkhepo"),
    "whatever": [("ye vā pana", "ye")],
    "dependently": [("paṭiccasamuppannā", "paṭicca")],
    "dependently arisen": same("paṭiccasamuppannā"),
    "dependently arisen immaterial": same("paṭiccasamuppannā arūpino"),
    "arisen": [("paṭiccasamuppannā", "samuppannā"), ("uppannaṃ", "uppannaṃ")],
    "arisen immaterial": [("paṭiccasamuppannā arūpino", "samuppannā arūpino")],
    "arisen immaterial states": [("paṭiccasamuppannā arūpino dhammā", "samuppannā arūpino dhammā")],
    "immaterial states": same("arūpino dhammā"),
    "except": same("ṭhapetvā"),
    # ---- intro "develops the path to rebirth in the fine-material / immaterial sphere"
    "develops": same("bhāveti"),
    "develops the path": same("maggaṃ bhāveti"),
    "path": same("maggaṃ"),
    "path to rebirth": [("ūpapattiyā maggaṃ", "upapattiyā maggaṃ")],
    "rebirth": [("ūpapattiyā", "upapattiyā")],
    "fine-material": [("rūpūpapattiyā", "rūpa"), ("Rūpāvacara", "Rūpa")],
    "fine-material sphere": SPHERE_FM,
    "immaterial": [("arūpūpapattiyā", "arūpa"), ("arūpino", "arūpino"), ("Arūpāvacara", "Arūpa"),
                   ("arūpajhānāni", "arūpa")],
    "immaterial sphere": SPHERE_IM,
    # "sphere": a real source (-āvacara) where the segment has one, else supplied (rūpūpapatti) -> nde
    "sphere": [("Rūpāvacara", "avacara"), ("Arūpāvacara", "avacara"), ("Kāmāvacara", "avacara"),
               ("kāmāvacaraṃ", "avacaraṃ"), NDE],
    "sense": [("dvāyatanāni", "āyatanāni"), ("Kāmāvacara", "Kāma"), ("kāmāvacaraṃ", "kāma")],
    "sense sphere": same("Kāmāvacara", "kāmāvacaraṃ"),
    "sphere has arisen": [("āvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti", "avacaraṃ kusalaṃ cittaṃ uppannaṃ hoti")],
    "planes": [("Tebhūmaka", "bhūmaka")],
    # ---- absorption formulas
    "quite": same("vivicceva"),
    "secluded": same("vivicceva"),
    "secluded from sensual": same("vivicceva kāmehi"),
    "sensual": same("kāmehi"),
    "sensual pleasures": same("kāmehi"),
    "pleasures": same("kāmehi"),
    "applied": APPLIED,
    "applied thought": APPLIED,
    "sustained": SUSTAINED,
    "sustained thought": SUSTAINED,
    "thought": THOUGHT,
    "seclusion": same("vivekajaṃ"),
    "born": same("vivekajaṃ", "samādhijaṃ"),
    "rapture": [("pītiyā", "pītiyā"), ("pīti", "pīti")],
    "happiness": [("pītisukhaṃ", "sukhaṃ"), ("sukhañca", "sukhañca"), ("sukhaṃ hoti", "sukhaṃ")],
    "absorption": same("jhānaṃ"),
    "absorptions": same("jhānāni"),
    "enters": same("upasampajja"),
    "dwells": same("viharati"),
    "enters and dwells": same("upasampajja viharati"),
    "stilling": same("vūpasamā"),
    "inner": same("ajjhattaṃ"),
    "confidence": same("sampasādanaṃ"),
    "unification": same("ekodibhāvaṃ"),
    "concentration": [("samādhijaṃ", "samādhijaṃ"), ("samādhindriyaṃ", "samādhi")],
    "fading": same("virāgā"),
    "away": same("virāgā"),
    "dwells equanimous": same("upekkhako ca viharati"),
    "equanimous": same("upekkhako"),
    "mindful": [("sato ca", "sato")],
    "clearly": same("sampajāno"),
    "aware": same("sampajāno"),
    "experiences": same("paṭisaṃvedeti"),
    "body": same("kāyena"),
    "noble": same("ariyā"),
    "declare": same("ācikkhanti"),
    "abandoning": same("pahānā"),
    "abandoning of pleasure": same("sukhassa ca pahānā"),
    "pleasure": same("sukhassa"),
    "pain": same("dukkhassa"),
    "disappearance": same("atthaṅgamā"),
    "sadness": same("domanassānaṃ"),
    "painful nor pleasant": same("adukkhamasukhaṃ"),
    "purity": same("pārisuddhiṃ"),
    "fourth absorption": same("catutthaṃ jhānaṃ"),
    "fifth": same("pañcamaṃ"),
    # ---- list of factors (absorptions in full)
    "feeling": same("vedanā"),
    "perception": same("saññā"),
    "intention": same("cetanā"),
    "joy": [("somanassa", "somanassa"), ("somanass", "somanassa"), ("muditā", "muditā")],
    "equanimity": same("upekkhā"),
    "one-pointedness": [("cittassekaggatā", "ekaggatā")],
    "one-pointedness of mind": same("cittassekaggatā"),
    "faculty": same("indriyaṃ"),
    "faculties": same("indriyāni"),
    "faculty of faith": same("saddhindriyaṃ"),
    "faith": [("saddhindriyaṃ", "saddhā")],
    "faculty of energy": same("vīriyindriyaṃ"),
    "faculty of mindfulness": same("satindriyaṃ"),
    "mindfulness": [("satipārisuddhiṃ", "sati"), ("satindriyaṃ", "sati")],
    "faculty of concentration": same("samādhindriyaṃ"),
    "faculty of wisdom": same("paññindriyaṃ"),
    "wisdom": [("paññindriyaṃ", "paññā")],
    "faculty of mind": same("manindriyaṃ"),
    "faculty of joy": same("somanassindriyaṃ"),
    "faculty of equanimity": same("upekkhindriyaṃ"),
    "faculty of life": same("jīvitindriyaṃ"),
    "life": [("jīvitindriyaṃ", "jīvita")],
    "right": [("sammādiṭṭhi", "sammā")],
    "view": [("sammādiṭṭhi", "diṭṭhi")],
    "effort": [("sammāvāyāmo", "vāyāmo")],
    "exertion": same("paggāho"),
    # ---- Koṭṭhāsa summary
    "aggregates": same("khandhā"),
    "sense bases": [("dvāyatanāni", "āyatanāni")],
    "bases": [("āyatanāni", "āyatanāni"), NDE],
    "elements": same("dhātuyo"),
    "nutriments": same("āhārā"),
    "three-factored": same("tivaṅgikaṃ"),
    "two-factored": same("duvaṅgikaṃ"),
    "two-factored absorption": same("duvaṅgikaṃ jhānaṃ"),
    "four-factored": same("caturaṅgikaṃ", "caturaṅgiko"),
    "four-factored path": same("caturaṅgiko maggo"),
    "powers": same("balāni"),
    "roots": same("hetū"),
    "mental-object": [("dhammāyatanaṃ", "dhamma")],
    "mental-object base": same("dhammāyatanaṃ"),
    "mental-object element": same("dhammadhātu"),
    "element": [("dhammadhātu", "dhātu")],
    # ---- aggregate of mental formations (Q/A)
    "aggregate": same("khandho", "khandhaṃ"),
    "aggregate of mental": same("saṅkhārakkhandho"),
    "mental": [("saṅkhārakkhandho", "saṅkhāra")],
    "mental formations": [("saṅkhārakkhandho", "saṅkhāra")],
    "formations": [("saṅkhārakkhandho", "saṅkhāra")],
    "aggregate of feeling": same("vedanākkhandhaṃ"),
    "aggregate of perception": same("saññākkhandhaṃ"),
    "aggregate of consciousness": same("viññāṇakkhandhaṃ"),
    "consciousness": [("viññāṇakkhandhaṃ", "viññāṇa"), ("viññāṇañcāyatana", "viññāṇañca")],
    # ---- methods, headings
    "fourfold": [("Catukkanayo", "Catukka")],
    "fourfold method": same("Catukkanayo"),
    "fivefold": [("Pañcakanayo", "Pañcaka")],
    "fivefold method": same("Pañcakanayo"),
    "method": [("Catukkanayo", "nayo"), ("Pañcakanayo", "nayo")],
    "modes": same("paṭipadā"),
    "kinds": same("ārammaṇāni"),
    "sixteenfold": SIXTEEN,
    "eightfold": EIGHT,
    "eightfold set": EIGHT,
    # ---- earth device and the eight devices
    "using": [NDE],
    "earth": [("pathavīkasiṇaṃ", "pathavī")],
    "meditation": same("kasiṇaṃ"),
    "device": same("kasiṇaṃ"),
    "meditation device": same("kasiṇaṃ"),
    "devices": same("kasiṇaṃ"),
    "meditation devices": same("kasiṇaṃ"),
    "water": [("āpokasiṇaṃ", "āpo")],
    "fire": [("tejokasiṇaṃ", "tejo")],
    "air": [("vāyokasiṇaṃ", "vāyo")],
    "blue": [("nīlāni", "nīlāni"), ("nīlakasiṇaṃ", "nīla")],
    "yellow": [("pītāni", "pītāni"), ("pītakasiṇaṃ", "pīta")],
    "red": [("lohitakāni", "lohitakāni"), ("lohitakasiṇaṃ", "lohita")],
    "white": [("odātāni", "odātāni"), ("odātakasiṇaṃ", "odāta")],
    # ---- modes of progress
    "painful": [("dukkhapaṭipadaṃ", "dukkha"), ("adukkhamasukhaṃ", "dukkha")],
    "pleasant": [("sukhapaṭipadaṃ", "sukha"), ("adukkhamasukhaṃ", "sukhaṃ")],
    "painful progress": same("dukkhapaṭipadaṃ"),
    "pleasant progress": same("sukhapaṭipadaṃ"),
    "progress": same("paṭipadaṃ", "paṭipadā"),
    "slow": [("dandhābhiññaṃ", "dandha")],
    "quick": [("khippābhiññaṃ", "khippa")],
    "slow direct": same("dandhābhiññaṃ"),
    "slow direct knowledge": same("dandhābhiññaṃ"),
    "quick direct": same("khippābhiññaṃ"),
    "quick direct knowledge": same("khippābhiññaṃ"),
    "progress and slow": [("paṭipadaṃ dandhābhiññaṃ", "paṭipadaṃ dandha")],
    "progress and quick": [("paṭipadaṃ khippābhiññaṃ", "paṭipadaṃ khippa")],
    "direct": [("ābhiññaṃ", "abhiññaṃ")],
    "direct knowledge": [("ābhiññaṃ", "abhiññaṃ")],
    "knowledge": [("ābhiññaṃ", "abhiññaṃ"), ("ñāṇasampayuttaṃ", "ñāṇa"), ("ñāṇavippayuttaṃ", "ñāṇa")],
    "editions": [NDE],
    "variant": [NDE],
    # ---- the absorption and its object
    "limited": LIMITED,
    "limited object": same("parittārammaṇaṃ"),
    "immeasurable": IMMEAS,
    "immeasurable object": same("appamāṇārammaṇaṃ"),
    "object": same("ārammaṇaṃ", "ārammaṇāni"),
    # ---- bases of mastery
    "perceiving": [("arūpasaññī", "saññī")],
    "perceiving material": [("arūpasaññī", "rūpasaññī")],
    "perceiving material form": [("arūpasaññī", "rūpasaññī")],
    "material": FORM,
    "material form": FORM,
    "form": FORM,
    "form in oneself": [("ajjhattaṃ arūpasaññī", "ajjhattaṃ arūpa")],
    "oneself": same("ajjhattaṃ"),
    "visible": same("rūpāni"),
    "visible forms": same("rūpāni"),
    # "forms" in the headings "... over Limited / Immeasurable Forms" is supplied -> nde
    "forms": [("rūpāni", "rūpāni"), NDE],
    "outside": same("bahiddhā"),
    "ones": same("ariyā", "parittāni", "appamāṇāni", "nīlāni", "pītāni"),
    "having": [NDE],
    "mastered": same("abhibhuyya"),
    "know": same("jānāmi"),
    "thinks": same("passāmīti"),
    "beautiful": [("suvaṇṇa", "suvaṇṇa"), ("subhanti", "subhanti")],
    "ugly": [("dubbaṇṇāni", "dubbaṇṇāni")],
    "colour": [("vaṇṇāni", "vaṇṇāni")],
    "appearance": [("nidassanāni", "nidassanāni")],
    "shining": [("nibhāsāni", "nibhāsāni")],
    "bases of mastery": same("Abhibhāyatanāni", "abhibhāyatanāni") + [NDE],
    "mastery": [("Abhibhāyatanāni", "Abhibhu"), ("abhibhāyatanāni", "abhibhu"), NDE],
    "limited forms": same("parittāni"),
    # ---- liberations
    "possessing": same("rūpī"),
    "possessing material form": same("rūpī"),
    "liberations": same("vimokkhāni"),
    # ---- divine abidings
    "accompanied": same("sahagataṃ"),
    "accompanied by loving-kindness": same("mettāsahagataṃ"),
    "loving-kindness": [("mettāsahagataṃ", "mettā")],
    "compassion": [("karuṇāsahagataṃ", "karuṇā")],
    "sympathetic": [("muditāsahagataṃ", "muditā")],
    "accompanied by equanimity": same("upekkhāsahagataṃ"),
    "divine": [("brahmavihāra", "brahma")],
    "abidings": [("brahmavihāra", "vihāra")],
    # ---- the unattractive
    "unattractive": [("Asubha", "Asubha")],
    "corpse": [("uddhumātakasaññā", "uddhumātaka"), ("vinīlakasaññā", "vinīlaka")],
    "bloated": [("uddhumātakasaññā", "uddhumātaka")],
    "discoloured": [("vinīlakasaññā", "vinīlaka")],
    "festering": [("vipubbakasaññā", "vipubbaka")],
    "apart": [("vicchiddakasaññā", "vicchiddaka")],
    "gnawed": [("vikkhāyitakasaññā", "vikkhāyitaka")],
    "scattered": [("vikkhittakasaññā", "vikkhittaka")],
    "hacked": [("hatavikkhittaka", "hata")],
    "bleeding": [("lohitakasaññā", "lohitaka")],
    "worm-infested": [("puḷavakasaññā", "puḷavaka")],
    "skeleton": [("aṭṭhikasaññā", "aṭṭhika")],
    # ---- immaterial absorptions
    "completely": same("sabbaso"),
    "passing": same("samatikkamā"),
    "passed": same("samatikkamma"),
    "beyond": same("samatikkamā", "samatikkamma"),
    "perceptions": same("saññānaṃ"),
    "attending": [("amanasikārā", "manasikārā")],
    "diversity": [("nānattasaññānaṃ", "nānatta")],
    "base of infinite": BASE_INF,
    "infinite": [("ākāsānañcāyatana", "ānañca"), ("viññāṇañcāyatana", "viññāṇañca")],
    "space": [("ākāsānañcāyatana", "ākāsa")],
    "nothingness": [("ākiñcaññāyatana", "ākiñcañña")],
    "non-perception": [("nāsaññāyatana", "nāsaññā")],
    # ---- three planes: sense sphere
    "accompanied by joy": same("somanassasahagataṃ"),
    "associated": [("ñāṇasampayuttaṃ", "sampayuttaṃ")],
    "dissociated": [("ñāṇavippayuttaṃ", "vippayuttaṃ")],
    "dissociated from knowledge": same("ñāṇavippayuttaṃ"),
    "prompting": [("sasaṅkhārena", "saṅkhārena")],
    "inferior": same("hīnaṃ"),
    "middling": same("majjhimaṃ"),
    "superior": same("paṇītaṃ"),
    "desire": [("chandādhipateyyaṃ", "chanda")],
    "inquiry": [("vīmaṃsādhipateyyaṃ", "vīmaṃsā")],
    "dominant": DOMINANT,
    "dominant factor": DOMINANT,
    "factor": DOMINANT,
}


def resolve(kw, text):
    cands = CAND[kw]
    best = None
    for c in cands:
        if c == NDE:
            continue
        pat, val = c
        i = text.find(pat)
        if i < 0:
            continue
        key = (i, -len(pat))
        if best is None or key < best[0]:
            best = (key, val)
    if best:
        return best[1]
    if NDE in cands:
        return NDE
    raise KeyError(kw)


def build(report=False):
    segs = segments()
    out, errors = [], []
    seen = collections.defaultdict(collections.Counter)
    used = set()
    for line in (HERE / f"{CH}.keywords.md").read_text(encoding="utf-8").splitlines():
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        text = segs[bid]
        pairs = []
        for k in [k.strip() for k in rest.split(", ")]:
            kl = k.lower()
            used.add(kl)
            try:
                v = resolve(kl, text)
            except KeyError:
                errors.append((bid, k))
                v = "???"
            assert ", " not in v and "=" not in v, (bid, k, v)
            seen[kl][v] += 1
            pairs.append(f"{v}={k}")
        out.append(f"[{bid}] " + ", ".join(pairs))
    assert not errors, errors
    unused = sorted(set(CAND) - used)
    (HERE / f"{CH}.mapped.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(CH, "lines", len(out), "unused table keys", unused)
    if report:
        for k in sorted(seen):
            print(f"  {k}: " + "; ".join(f"{v} x{n}" for v, n in seen[k].most_common()))


if __name__ == "__main__":
    build("--report" in sys.argv)
