"""English->Pali keyword map for pi-1 chapters `2-05-cittuppadakandam` and `4-03-nikkhepakandam`.

usage: python -I -X utf8 map_2-05_4-03.py [--review]
Writes <ch>.mapped.md next to <ch>.keywords.md. Conventions: map-conventions.md (incl. section 8).

2-05 is formulaic: every keyword has a rule = one or more lemma groups of (regex, value) candidates that
are searched in THAT segment's Pali (brackets removed). Within a group the earliest match wins (same lemma:
first occurrence); several matching groups (different lemmas) are joined with " / " in text order.
The candidate patterns only cover the Pali that the English keyword actually renders (e.g. "contact" does
not take the samphassa of "body-contact", "empty" does not take the suññata of the heading "emptiness").
Headings have fixed tables. 4-03 is mostly non-formulaic: explicit per-segment tables built from shared
pieces (the panna, ditthi, moha, samadhi, viriya and sila strings).

Quotative iti: dropped when the rest is the word letter for letter (Saṃvegoti -> Saṃvego, Vijjāti -> Vijjā);
kept as written when the sandhi changed letters (suññatanti, padhānanti, Vimuttīti, ñāṇanti), as with fused
ca in section 1.5.
"""
import pathlib, re, sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
NDE = "(no direct equivalent)"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def segments(ch):
    segs, buf = {}, []
    for line in (PALI / f"{ch}.md").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        mm = ID.search(line)
        buf.append(line[:mm.start()] if mm else line)
        if mm:
            t = " ".join(buf)
            t = re.sub(r"\[[^\]]*\]", " ", t)
            t = re.sub(r"^#+\s*|\s#+\s", " ", t)
            segs[mm.group(1)] = re.sub(r"\s+", " ", t).strip()
            buf = []
    return segs


# ===================================================================== 2-05 rules
def R(*cands):
    """one lemma group"""
    return [list(cands)]


def J(*groups):
    """several lemma groups (different lemmas, joined with ' / ')"""
    return [list(g) for g in groups]


A1 = lambda m: "a" + m.group(0)[1:]  # sandhi-lengthened initial written in its own form (ābhiññaṃ -> abhiññaṃ)

VIT = [(r"\bvitakko\b", None), (r"\bvitakka(?=vicār)", "vitakka")]
VIC = [(r"\bvicāro\b", None), (r"(?<=vitakka)vicārānaṃ", "vicārānaṃ")]
DIRKN = [(r"(?<=dandh|khipp)ābhiññ(?:aṃ|anti)", A1)]
ANNA = [(r"\baññ(?=indriy)", "aññā"), (r"\baññātāv(?=indriy)", "aññātāvī"), (r"\baññātāvīnaṃ\b", None),
        (r"\baññā\b", None)]
NANA = [(r"\bñāṇa(?=sampayutt|vippayutt)", "ñāṇa")]
G_CITTA = [(r"\bcittaṃ\b", None), (r"\bcittass(?=ekaggatā)", "cittassa"), (r"\bcittassa\b", None),
           (r"\bcitt(?=ādhipateyy)", "citta"), (r"Citt(?=uppāda)", "Citta")]
G_MANO = [(r"\bmano(?=dhātu)", "mano"), (r"\bman(?=indriy)", "mano")]
G_MANASA = [(r"mānasatā", None)]
DOMINANT = [(r"ādhipateyy(?:aṃ|anti)", A1)]
BOJJH = [(r"(?:sam)?bojjhaṅg(?:aṃ|o)\b", None), (r"(?<=magg)aṅgaṃ", "aṅgaṃ")]

RULES = {
    "abandoning": R((r"pahānāya", None), (r"\bpahānā\b", None)),
    "abandoning of pleasure": R((r"sukhassa ca pahānā", None)),
    "abandoning of wrong": R((r"diṭṭhigatānaṃ pahānāya", None)),
    "abiding": R((r"(?<=sukha)vihāraṃ", None)),
    "absorption": R((r"\bjhān(?:aṃ|assa)\b", None)),
    "accompanied": R((r"sahagat(?:ā|aṃ)\b", None)),
    "accompanied by equanimity": R((r"\bupekkhāsahagat(?:ā|aṃ)\b", None)),
    "accompanied by joy": R((r"\bsomanassasahagat(?:ā|aṃ)\b", None)),
    "accumulated": R((r"\bupacitattā\b", None)),
    "accumulation": R((r"(?<=apa)caya(?=gām)", None)),
    "aggregate": R((r"khandh(?:o|aṃ)\b", None)),
    "aggregate of consciousness": R((r"viññāṇakkhandhaṃ", None)),
    "aggregate of feeling": R((r"vedanākkhandhaṃ", None)),
    "aggregate of mental": R((r"saṅkhārakkhandho", None)),
    "aggregate of perception": R((r"saññākkhandhaṃ", None)),
    "aggregates": R((r"\bkhandhā\b", None)),
    "applied": [VIT], "applied thought": [VIT],
    "sustained": [VIC], "sustained thought": [VIC],
    "thought": J(VIT, VIC),
    "ardour": R((r"\bussoḷhī\b", None)),
    "arisen": R((r"\buppann(?:aṃ|ā)\b", None), (r"(?<=paṭicca)samuppannā", None)),
    "arisen immaterial": R((r"samuppannā arūpino", None)),
    "arisen immaterial states": R((r"samuppannā arūpino dhammā", None)),
    "arising": R((r"(?<=Citt)uppāda", None)),
    "arising of mind": R((r"Cittuppāda", None)),
    "arousing": R((r"(?<=vīriy)ārambho", None)),
    "associated": R((r"(?<=ñāṇa)sampayuttā", None)),
    "attending": R((r"(?<=\ba)manasikārā", None)),
    "awakening": R(*BOJJH[:1]),
    "awakening factor": R(*BOJJH[:1]),
    "awareness": R((r"\bsampajaññaṃ\b", None)),
    "away": R((r"\bapacaya(?=gām)", None)),
    "base of infinite": R((r"(?<=ākās)ānañcāyatana(?:ṃ)?", None), (r"\bviññāṇañcāyatana(?:ṃ)?", None)),
    "bases": R((r"(?<=dv)āyatanāni", None)),
    "beyond": R((r"\bsamatikkam(?:ā|ma)\b", None)),
    "bodily": R((r"\bkāyikaṃ\b", None)),
    "body-consciousness": R((r"\bkāyaviññāṇaṃ", None), (r"kāyaviññāṇa(?=dhātu)", None)),
    "body-consciousness element": R((r"kāyaviññāṇadhātu", None)),
    "body-contact": R((r"\bkāyasamphassa", None)),
    "born": R((r"samphassaj(?:aṃ|ā)\b", None)),
    "born of body-contact": R((r"\bkāyasamphassaj(?:aṃ|ā)\b", None)),
    "breadth": R((r"\bbhūrī\b", None)),
    "burden": R((r"(?<=nikkhitta)dhuratā", None), (r"\bdhura(?=sampaggāh)", None)),
    "calm": R((r"\bsamath(?:o|aṃ)\b", None)),
    "chapter": R((r"(?<=Cittuppāda)kaṇḍaṃ", None)),
    "clarity": R((r"\bvebhabyā\b", None)),
    "clear": R((r"\bsampajaññaṃ\b", None)),
    "clear awareness": R((r"\bsampajaññaṃ\b", None)),
    "close investigation": R((r"\bpavicayo\b", None)),
    "coming": R((r"\bsaṃphusanā\b", None)),
    "coming into contact": R((r"\bsaṃphusanā\b", None)),
    "complete": R((r"\bniṭṭhitaṃ\b", None)),
    "completely": R((r"\bsabbaso\b", None)),
    "conceit": R((r"(?<=rāga)māna", None)),
    "concentration": R((r"\bsamādhi(?=ndriy|bal)", None)),
    "consciousness": R((r"\bviññāṇa(?=kkhandh)", None), (r"(?<=pañca)viññāṇāni", None),
                       (r"\bviññāṇañc(?=ā)", "viññāṇañca")),
    "consciousness resulting": R((r"vipākapañcaviññāṇāni", None)),
    "consideration": R((r"\bcintā\b", None)),
    "contact": R((r"\b[Pp]hass(?:o|aṃ)\b", None), (r"(?<=dhātu)samphassa", None)),
    "corresponding": R((r"\btajjā(?=kāya)", None)),
    "dependently": R((r"\bpaṭicca(?=samuppannā)", None)),
    "dependently arisen": R((r"\bpaṭiccasamuppannā\b", None)),
    "dependently arisen immaterial": R((r"\bpaṭiccasamuppannā arūpino", None)),
    "desire": R((r"\b[Cc]hand(?=ādhipateyy)", lambda m: m.group(0) + "a"), (r"(?<=nikkhitta)chandatā", None)),
    "desireless": R((r"\bappaṇihit(?:aṃ|anti)", None)),
    "developed": R((r"\bbhāvitattā\b", None)),
    "develops": R((r"\bbhāveti\b", None)),
    "develops a world-transcending": R((r"\blokuttaraṃ satipaṭṭhānaṃ bhāveti\b", None)),
    "develops absorption": R((r"\bjhānaṃ bhāveti\b", None)),
    "develops world-transcending": R((r"\blokuttaraṃ jhānaṃ bhāveti\b", None)),
    "develops world-transcending absorption": R((r"\blokuttaraṃ jhānaṃ bhāveti\b", None)),
    "device": R((r"(?<=pathavī)kasiṇaṃ", None)),
    "differentiating": R((r"\bpaccupalakkhaṇā\b", None)),
    "direct": [DIRKN], "direct knowledge": [DIRKN],
    "disappearance": R((r"\batthaṅgamā\b", None)),
    "discerning": R((r"\bsallakkhaṇā\b", None)),
    "discomfort": R((r"\basātaṃ\b", None)),
    "dissociated": R((r"(?<=ñāṇa)vippayuttā", None)),
    "dissociated from knowledge": R((r"\bñāṇavippayuttā", None)),
    "distinguishing": R((r"\bupalakkhaṇā\b", None)),
    "diversity": R((r"\bnānatta(?=saññ)", None)),
    "dominant": [DOMINANT], "dominant factor": [DOMINANT],
    "done": R((r"\bkatattā\b", None)),
    "dwells": R((r"\bviharati\b", None)),
    "ear-consciousness": R((r"\bsotaviññāṇaṃ", None)),
    "earth": R((r"\bpathavī(?=kasiṇ)", None)),
    "effort": R((r"\bvāyāmo\b", None)),
    "element": R((r"\bdhātuṃ\b", None), (r"dhātu(?!yo|ṃ)", None)),
    "element accompanied": R((r"(?<=viññāṇa)dhātu (?:somanassa|upekkhā)sahagatā", None)),
    "element has arisen": R((r"dhātu uppannā", None)),
    "element resulting": R((r"vipākā mano(?:viññāṇa)?dhātu", None)),
    "elements": R((r"\bdhātuyo\b", None)),
    "emptiness": R((r"(?<=Suddhika)suññataṃ", None), (r"\bSuññata(?=paṭipadā)", None),
                   (r"(?<=suddhika)suññatā", None)),
    "empty": R((r"\bsuññat(?:aṃ|anti)", None)),
    "enters": R((r"\bupasampajja\b", None)),
    "enters and dwells": R((r"\bupasampajja viharati\b", None)),
    "equanimity": R((r"\bupekkhā", None), (r"\bupekkh(?=indriy)", "upekkhā")),
    "examination": R((r"\bupaparikkhā\b", None)),
    "except": R((r"\bṭhapetvā\b", None)),
    "existence": NDE,  # "lust for fine-material existence": added in English (rūparāga)
    "experience": R((r"\bvedayitaṃ\b", None)),
    "experience born": R((r"samphassajaṃ asātaṃ dukkhaṃ vedayitaṃ", None)),
    "eye-consciousness": R((r"\bcakkhuviññāṇaṃ", None)),
    "factor": J(BOJJH, DOMINANT),
    "factor of investigation": R((r"vicayasambojjhaṅgo", None)),
    "faculties": R((r"indriyāni\b", None)),
    "faculty": R((r"indriyaṃ", None)),
    "faculty of concentration": R((r"\bsamādhindriyaṃ", None)),
    "faculty of energy": R((r"\bvīriyindriyaṃ", None)),
    "faculty of equanimity": R((r"\bupekkhindriyaṃ", None)),
    "faculty of final": R((r"\baññindriyaṃ", None)),
    "faculty of joy": R((r"\bsomanassindriyaṃ", None)),
    "faculty of life": R((r"\bjīvitindriyaṃ", None)),
    "faculty of mind": R((r"\bmanindriyaṃ", None)),
    "faculty of pain": R((r"\bdukkhindriyaṃ", None)),
    "faculty of wisdom": R((r"\bpaññindriyaṃ", None)),
    "feeling": R((r"\bvedan(?:ā|aṃ)", None)),
    "feeling born": R((r"samphassajā asātā dukkhā vedanā", None)),
    "fifth": R((r"\bpañcamaṃ\b", None)),
    "final knowledge": [ANNA],
    "fine-material": R((r"\brūpa(?=rāga)", None), (r"\brūp(?=āvacar)", "rūpa")),
    "fine-material sphere": R((r"\brūpāvacaraṃ", None)),
    "firmness": R((r"\bavaṭṭhiti\b", None)),
    "form": R((r"\brūp(?=ārammaṇ)", "rūpa"), (r"\brūpa(?=saññ)", None)),
    "formations": R((r"\bsaṅkhāra(?=kkhandh)", None)),
    "forward": R((r"\bparakkamo\b", None)),
    "foundation": R((r"(?<=sati)paṭṭhānaṃ", None)),
    "fourth absorption": R((r"\bcatutthaṃ jhānaṃ", None)),
    "functional": R((r"\b[Kk]iriy(?:ā|aṃ)\b", None), (r"(?<=vacara)kiriyā", None)),
    "functional indeterminate": R((r"\b[Kk]iriyā abyākatā", None)),
    "functional indeterminate minds": R((r"\b[Kk]iriyā abyākatā", None)),
    "functional mind": R((r"\bKiriyā mano", None)),
    "functional mind element": R((r"\bKiriyā manodhātu", None)),
    "functional mind-consciousness": R((r"\bKiriyā manoviññāṇa", None)),
    "functional mind-consciousness element": R((r"\bKiriyā manoviññāṇadhātu", None)),
    "functional minds": R((r"(?<=vacara)kiriyā", None)),
    "goad": R((r"\bpatodo\b", None)),
    "grasping": R((r"(?<=dhura)sampaggāho", None)),
    "guidance": R((r"\bpariṇāyikā\b", None)),
    "happiness": R((r"\bsukhaṃ\b", None)),
    "having": NDE,  # auxiliary ("having come into contact", "having passed beyond")
    "ignorance": R((r"(?<=uddhacca)avijjāya", None)),
    "ill": R((r"(?<=rāga)byāpādānaṃ", None)),
    "immaterial": R((r"\barūpino\b", None), (r"(?<=rāga)arūpa", None), (r"\barūp(?=āvacar)", "arūpa")),
    "immaterial sphere": R((r"\barūpāvacaraṃ", None)),
    "immaterial states": R((r"\barūpino dhammā", None)),
    "indeterminate": R((r"\babyākat(?:ā|aṃ)\b", None)),
    "indeterminate minds": R((r"(?<=iriyā )abyākatā", None)),
    "indeterminate results": R((r"\bVipākā abyākatā", None)),
    "indeterminate root": R((r"\babyākatamūlaṃ", None)),
    "indeterminate states": R((r"\bdhammā abyākatā", None)),
    "infinite": R((r"(?<=ākās)ānañc(?=ā)", "ānañca"), (r"\bviññāṇañc(?=ā)", "viññāṇañca")),
    "inquiry": R((r"\bvīmaṃsā(?=dhipateyy)", None)),
    "insight": R((r"\bvipassanā\b", None)),
    "intelligence": R((r"\bmedhā\b", None)),
    "intention": R((r"\bcetan(?:ā|aṃ)\b", None)),
    "investigation": R((r"\bvicayo\b", None)),
    "investigation of states": R((r"\bdhammavicayo\b", None)),
    "jewel": R((r"(?<=paññā)ratanaṃ", None)),
    "jewel of wisdom": R((r"\bpaññāratanaṃ", None)),
    "joy": R((r"\bsomanass(?=asahagat|indriy)", "somanassa")),
    "kinds": R((r"(?<=pañca)viññāṇāni", None)),
    "knowledge": J(DIRKN, ANNA, NANA),
    "lamp": R((r"(?<=paññā)pajjoto", None)),
    "lamp of wisdom": R((r"\bpaññāpajjoto", None)),
    "leads": J([(r"\bniyyānikaṃ", None)], [(r"(?<=apacaya)gāmiṃ", None)]),
    "leads to liberation": R((r"\bniyyānikaṃ", None)),
    "learning": R((r"\bpaṇḍiccaṃ\b", None)),
    "liberation": R((r"\bniyyānikaṃ", None)),
    "liberation and leads": R((r"\bniyyānikaṃ apacayagāmiṃ", None)),
    "life": R((r"\bjīvit(?=indriy)", "jīvita")),
    "light": R((r"(?<=paññā)āloko", None)),
    "light of wisdom": R((r"\bpaññāāloko", None)),
    "lust": R((r"(?<=kāma)rāga", None)),
    "material": R((r"\brūpa(?=saññ)", None)),
    "material form": R((r"\brūpa(?=saññ)", None)),
    "meditation": R((r"(?<=pathavī)kasiṇaṃ", None)),
    "meditation device": R((r"(?<=pathavī)kasiṇaṃ", None)),
    "mental": J([(r"\bsaṅkhāra(?=kkhandh)", None)], [(r"\bdhamm(?=ārammaṇ)", "dhamma")], [(r"\bcetasiko\b", None)]),
    "mental arousing": R((r"\bcetasiko vīriyārambho", None)),
    "mental formations": R((r"\bsaṅkhāra(?=kkhandh)", None)),
    "mental object": R((r"\bdhamm(?=ārammaṇ)", "dhamma")),
    "mental-object": R((r"\bdhamma(?=dhātu)", None), (r"\bdhamm(?=āyatan)", "dhamma")),
    "mental-object base": R((r"\bdhammāyatanaṃ", None)),
    "mental-object element": R((r"\bdhammadhātu", None)),
    "methods": R((r"(?<=mahā)nayā", None)),
    "mind": J(G_CITTA, G_MANO, G_MANASA),
    "mind element": R((r"\bmanodhātu", None)),
    "mind element resulting": R((r"vipākā manodhātu", None)),
    "mind-consciousness": R((r"\bmanoviññāṇa", None)),
    "mind-consciousness element": R((r"\bmanoviññāṇadhātu", None)),
    "mind-consciousness element accompanied": R((r"\bmanoviññāṇadhātu (?:somanassa|upekkhā)sahagatā", None)),
    "mind-consciousness element resulting": R((r"vipākā manoviññāṇadhātu", None)),
    "mindfulness": R((r"\bsati(?=paṭṭhān)", None)),
    "minds": J([(r"(?<=vacara)kiriyā", None)], [(r"(?<=iriyā )abyākatā", None)]),
    "non-delusion": R((r"\bamoho\b", None)),
    "non-distraction": R((r"\bavikkhepo\b", None)),
    "non-greed": R((r"\balobho\b", None)),
    "non-hate": R((r"\badoso\b", None)),
    "non-perception": R((r"(?<=n)āsaññā", A1)),
    "non-scattering": R((r"\bavisāhāro\b", None)),
    "nose-consciousness": R((r"\bghānaviññāṇaṃ", None)),
    "nothingness": R((r"\bākiñcaññ(?=āyatan)", "ākiñcañña")),
    "nutriment": R((r"\bāhāraṃ\b", None)),
    "nutriments": R((r"\bāhārā\b", None)),
    "object": R((r"ārammaṇ(?:aṃ|ā)\b", None)),
    "one-pointedness": R((r"(?<=cittass)ekaggatā", None)),
    "one-pointedness of mind": R((r"\bcittassekaggatā", None)),
    "pain": R((r"\bdukkha(?=sahagat)", None), (r"\bdukkh(?=indriy)", "dukkha"), (r"\bdukkhaṃ\b", None)),
    "painful": R((r"\bdukkha(?=paṭipad)", None), (r"(?<=asātaṃ )dukkhaṃ", None)),
    "painful feeling": R((r"\bdukkhā vedanā", None)),
    "painful progress": R((r"\bdukkhapaṭipadaṃ", None)),
    "passed": R((r"\bsamatikkamma\b", None)),
    "passing": R((r"\bsamatikkamā\b", None)),
    "path": R((r"\bmaggaṃ\b", None), (r"\bmagga(?=ṅgaṃ|pariyāpann)", None)),
    "path factor": R((r"\bmaggaṅgaṃ", None)),
    "paths": R((r"(?<=Dutiyādi)magga", None)),
    "perception": R((r"\bsaññ(?:ā|aṃ)\b", None), (r"saññā(?=kkhandh|sahagat)", None), (r"(?<=neva)saññā", None)),
    "perceptions": R((r"saññānaṃ", None)),
    "plain": R((r"[Ss]uddhika", None)),
    "plain desireless": R((r"Suddhikaappaṇihitaṃ", None)),
    "plain progress": R((r"[Ss]uddhikapaṭipadā", None)),
    "pleasant": R((r"\bsukha(?=paṭipad)", None), (r"(?<=dhamma)sukha(?=vihār)", None)),
    "pleasant progress": R((r"\bsukhapaṭipadaṃ", None)),
    "pleasure": R((r"\bsukhassa\b", None)),
    "pleasures": R((r"\bkāmehi\b", None)),
    "power": J([(r"\biddhi(?=pād)", None)], [(r"balaṃ", None)]),
    "power of concentration": R((r"\bsamādhibalaṃ", None)),
    "power of energy": R((r"\bvīriyabalaṃ", None)),
    "power of wisdom": R((r"\bpaññābalaṃ", None)),
    "pressing": R((r"\bparakkamo\b", None)),
    "pressing forward": R((r"\bparakkamo\b", None)),
    "progress": R((r"(?<=kha)paṭipadaṃ", None), (r"paṭipadā\b", None)),
    "progress and quick": R((r"paṭipadaṃ khipp(?=ā)", lambda m: m.group(0) + "a")),
    "progress and slow": R((r"paṭipadaṃ dandh(?=ā)", lambda m: m.group(0) + "a")),
    "prompting": R((r"(?<=\bsa)saṅkhārena", None)),
    "putting": R((r"(?<=\ba)nikkhitta", None)),
    "quick": R((r"\bkhipp(?=ābhiññ)", "khippa")),
    "quick direct": R((r"\bkhippābhiññ(?:aṃ|anti)", None)),
    "quick direct knowledge": R((r"\bkhippābhiññ(?:aṃ|anti)", None)),
    "quite": R((r"(?<=vivicc)eva\b", None)),
    "radiance": R((r"(?<=paññā)obhāso", None)),
    "radiance of wisdom": R((r"\bpaññāobhāso", None)),
    "rapture": R((r"\bpīti\b", None)),
    "reaching": R((r"\bpattiyā\b", None)),
    "remainder": R((r"(?<=\ban)avasesa", None)),
    "restlessness": R((r"(?<=māna)uddhacca", None)),
    "result of action": R((r"\bkammavipāk(?:ā|aṃ)\b", None)),
    "resulting": R((r"(?<=Akusala)vipāk(?:ā|a)", None)),
    "right": R((r"\bsamm(?=appadhān)", "sammā"), (r"\bsammā(?=diṭṭhi)", None)),
    "root": R((r"(?<=abyākata)mūlaṃ", None)),
    "roots": R((r"(?:(?<=\b[Aa])|(?<=Sa))hetukā\b", None)),
    "secluded": R((r"\bvivicc(?=eva\b)", "vivicca")),
    "secluded from sensual": R((r"\bvivicceva kāmehi\b", None)),
    "sense": R((r"(?<=dv)āyatanāni", None), (r"(?<=lokuttaraṃ )āyatanaṃ", None), (r"\bkām(?=āvacar)", "kāma")),
    "sense bases": R((r"(?<=dv)āyatanāni", None)),
    "sense sphere": R((r"\bkāmāvacara", None)),
    "sensual": R((r"\bkāma(?=rāga)", None), (r"\bkāmehi\b", None)),
    "sensual lust": R((r"\bkāmarāga", None)),
    "sensual pleasures": R((r"\bkāmehi\b", None)),
    "setting": R((r"\bnikkamo\b", None)),
    "signless": R((r"\banimitt(?:aṃ|anti)", None)),
    "skill": R((r"\bkosallaṃ\b", None)),
    "slow": R((r"\bdandh(?=ābhiññ)", "dandha")),
    "slow direct": R((r"\bdandhābhiññ(?:aṃ|anti)", None)),
    "slow direct knowledge": R((r"\bdandhābhiññ(?:aṃ|anti)", None)),
    "smell": R((r"\bgandh(?=ārammaṇ)", "gandha")),
    "sound": R((r"\bsadd(?=ārammaṇ)", "sadda")),
    "space": R((r"\bākās(?=ānañc)", "ākāsa")),
    "sphere": R((r"(?<=rūp)āvacaraṃ", A1), (r"(?<=kām)āvacara", A1)),
    "spiritual": R((r"\biddhi(?=pād)", None)),
    "stability": R((r"(?<=cittassa )ṭhiti\b", None)),
    "stability of mind": R((r"\bcittassa ṭhiti\b", None)),
    "stage": R((r"\bbhūmiyā\b", None)),
    "steadfastness": R((r"\bdhiti\b", None)),
    "steadiness": R((r"\bsaṇṭhiti\b", None)),
    "stilling": R((r"\bvūpasamā\b", None)),
    "strength": R((r"\bthāmo\b", None)),
    "striving": R((r"(?<=sammap)padhānaṃ", None), (r"\buyyāmo\b", None)),
    "subtlety": R((r"\bnepuññaṃ\b", None)),
    "sword": R((r"(?<=paññā)satthaṃ", None)),
    "sword of wisdom": R((r"\bpaññāsatthaṃ", None)),
    "takes": R((r"(?<=pan)ārabbha\b", None)),
    "taste": R((r"\bras(?=ārammaṇ)", "rasa")),
    "time is bodily": R((r"\bsamaye kāyikaṃ", None)),
    "time is contact": R((r"\bsamaye phasso", None)),
    "tongue-consciousness": R((r"\bjivhāviññāṇaṃ", None)),
    "touch": R((r"\bphoṭṭhabb(?=ārammaṇ)", "phoṭṭhabba")),
    "touching": R((r"\bphusanā\b", None)),
    "tower": R((r"(?<=paññā)pāsādo", None)),
    "tower of wisdom": R((r"\bpaññāpāsādo", None)),
    "truth": R((r"\bsaccaṃ\b", None)),
    "twenty": R((r"\bVīsati\b", None)),
    "uncomfortable": R((r"\basāt(?:aṃ|ā)\b", None)),
    "understanding": R((r"\bpajānanā\b", None)),
    "unscattered": R((r"\bavisāhaṭa(?=mānas)", None)),
    "unscattered mind": R((r"\bavisāhaṭamānasatā", None)),
    "unslackening": R((r"\basithila(?=parakkam)", None)),
    "unwholesome": R((r"\bakusalassa\b", None), (r"(?<=\bn)ākusal(?:ā|aṃ)\b", A1), (r"\bAkusala(?=vipāk)", None)),
    "unwholesome action": R((r"\bakusalassa kammassa\b", None)),
    "using": NDE,  # "using earth as the meditation device": construction word (pathavīkasiṇaṃ)
    "view": R((r"(?<=sammā)diṭṭhi\b", None)),
    "views": R((r"\bdiṭṭhigatānaṃ\b", None)),
    "visible": R((r"\brūp(?=ārammaṇ)", "rūpa")),
    "visible form": R((r"\brūp(?=ārammaṇ)", "rūpa")),
    "weakening": R((r"\btanubhāvāya\b", None)),
    "whatever": R((r"\byaṃ yaṃ\b", None), (r"\b(?:Yo|Yā|Yaṃ|ye)\b", None)),
    "wholesome": R((r"\bkusal(?:ā|assa|aṃ)\b", None)),
    "wholesome absorption": R((r"\bkusalassa jhānassa\b", None)),
    "wholesome nor unwholesome": R((r"\bkusal(?:ā|aṃ) nākusal(?:ā|aṃ)\b", None)),
    "wholesome states": R((r"\bdhammā kusalā\b", None)),
    "wisdom": R((r"\bpaññā\b", None)),
    "world-transcending": R((r"\blokuttar(?:aṃ|assa)\b", None), (r"\bLokuttara", None)),
    "world-transcending absorption": R((r"\blokuttaraṃ jhānaṃ\b", None)),
    "world-transcending wholesome": R((r"\blokuttarassa kusalassa\b", None)),
    "world-transcending wholesome absorption": R((r"\blokuttarassa kusalassa jhānassa\b", None)),
    "wrong": R((r"\bdiṭṭhigatānaṃ\b", None)),
    "wrong views": R((r"\bdiṭṭhigatānaṃ\b", None)),
    "zeal": R((r"\bussāho\b", None)),
}
# the twenty great methods: "a world-transcending X" = lokuttaraṃ X
for en, pi in {"aggregate": "khandhaṃ", "awakening": "bojjhaṅgaṃ", "awakening factor": "bojjhaṅgaṃ",
               "basis": "iddhipādaṃ", "calm": "samathaṃ", "contact": "phassaṃ", "element": "dhātuṃ",
               "faculty": "indriyaṃ", "feeling": "vedanaṃ", "foundation": "satipaṭṭhānaṃ", "intention": "cetanaṃ",
               "mind": "cittaṃ", "nutriment": "āhāraṃ", "path": "maggaṃ", "perception": "saññaṃ",
               "power": "balaṃ", "sense": "āyatanaṃ", "state": "dhammaṃ", "truth": "saccaṃ"}.items():
    RULES[f"world-transcending {en}"] = R((rf"\blokuttaraṃ {pi}", None))

# fixed tables for the 2-05 headings (single compounds; cut per sections 1-2 and 8)
HEAD_205 = {
    "1-1-8-0": {"path": "magga", "world-transcending": "Lokuttara"},
    "1-1-8-1-0": {"plain": "Suddhika", "plain progress": "Suddhikapaṭipadā", "progress": "paṭipadā"},
    "1-1-8-2-0": {"emptiness": "suññataṃ", "plain": "Suddhika"},
    "1-1-8-3-0": {"emptiness": "Suññata", "progress": "paṭipadā"},
    "1-1-8-4-0": {"desireless": "appaṇihitaṃ", "plain": "Suddhika", "plain desireless": "Suddhikaappaṇihitaṃ"},
    "1-1-8-5-0": {"desireless": "Appaṇihita", "progress": "paṭipadā"},
    "1-1-8-6-0": {"methods": "nayā", "twenty": "Vīsati"},
    "1-1-8-7-0": {"desire": "Chanda", "dominant": "adhipateyya", "dominant factor": "adhipateyya",
                  "factor": "adhipateyya", "plain": "suddhika", "plain progress": "suddhikapaṭipadā",
                  "progress": "paṭipadā"},
    "1-1-8-8-0": {"desire": "Chanda", "dominant": "adhipateyya", "dominant factor": "adhipateyya",
                  "emptiness": "suññatā", "factor": "adhipateyya", "plain": "suddhika"},
    "1-1-8-9-0": {"paths": "magga"},
    "1-1-9-0": {"indeterminate": "abyākataṃ", "indeterminate results": "vipākaabyākataṃ", "unwholesome": "Akusala"},
    "1-1-9-1-0": {"consciousness": "viññāṇāni", "consciousness resulting": "vipākapañcaviññāṇāni",
                  "kinds": "viññāṇāni", "resulting": "vipāka", "unwholesome": "Akusala"},
    "1-1-9-2-0": {"element": "dhātu", "element resulting": "vipākamanodhātu", "mind": "mano",
                  "mind element": "manodhātu", "mind element resulting": "vipākamanodhātu", "resulting": "vipāka",
                  "unwholesome": "Akusala"},
    "1-1-9-3-0": {"element": "dhātu", "element resulting": "vipākamanoviññāṇadhātu",
                  "mind-consciousness": "manoviññāṇa", "mind-consciousness element": "manoviññāṇadhātu",
                  "mind-consciousness element resulting": "vipākamanoviññāṇadhātu", "resulting": "vipāka",
                  "unwholesome": "Akusala"},
    "1-1-10-0": {"functional": "kiriyā", "functional indeterminate": "kiriyāabyākataṃ",
                 "functional indeterminate minds": "kiriyāabyākataṃ", "indeterminate": "abyākataṃ",
                 "indeterminate minds": "abyākataṃ", "minds": "abyākataṃ", "roots": "hetuka"},
    "1-1-10-1-0": {"element": "dhātu", "functional": "Kiriyā", "functional mind": "Kiriyāmano",
                   "functional mind element": "Kiriyāmanodhātu", "mind": "mano", "mind element": "manodhātu"},
    "1-1-10-4-0": {"functional": "kiriyā", "functional minds": "kiriyā", "minds": "kiriyā", "roots": "hetuka",
                   "sense": "kāma", "sense sphere": "kāmāvacara", "sphere": "avacara"},
    "1-1-10-5-0": {"fine-material": "Rūpa", "fine-material sphere": "Rūpāvacara", "functional": "kiriyā",
                   "functional minds": "kiriyā", "minds": "kiriyā", "sphere": "avacara"},
    "1-1-10-6-0": {"functional": "kiriyā", "functional minds": "kiriyā", "immaterial": "Arūpa",
                   "immaterial sphere": "Arūpāvacara", "minds": "kiriyā", "sphere": "avacara"},
}
for hid, stem in (("1-1-10-2-0", "somanassa"), ("1-1-10-3-0", "upekkhā")):
    nm = "joy" if stem == "somanassa" else "equanimity"
    HEAD_205[hid] = {"accompanied": "sahagatā", f"accompanied by {nm}": f"{stem}sahagatā", "element": "dhātu",
                     "element accompanied": f"dhātu{stem}sahagatā", "functional": "Kiriyā",
                     "functional mind": "Kiriyāmano", "functional mind-consciousness": "Kiriyāmanoviññāṇa",
                     "functional mind-consciousness element": "Kiriyāmanoviññāṇadhātu", nm: stem,
                     "mind-consciousness": "manoviññāṇa", "mind-consciousness element": "manoviññāṇadhātu",
                     "mind-consciousness element accompanied": f"manoviññāṇadhātu{stem}sahagatā"}

_CACHE = {}


def rule_value(kw, text):
    rule = RULES.get(kw)
    if rule is None:
        return None
    if isinstance(rule, str):
        return rule
    hits = []
    for group in rule:
        best = None
        for pat, val in group:
            rx = _CACHE.setdefault(pat, re.compile(pat))
            m = rx.search(text)
            if m and (best is None or m.start() < best[0]):
                v = m.group(0) if val is None else (val(m) if callable(val) else val)
                best = (m.start(), v)
        if best:
            hits.append(best)
    if not hits:
        return None
    vals = []
    for _, v in sorted(hits):
        if v not in vals:
            vals.append(v)
    return " / ".join(vals)


def table_205():
    segs = segments("2-05-cittuppadakandam")

    def lookup(bid, kw):
        if bid in HEAD_205:
            return HEAD_205[bid].get(kw)
        return rule_value(kw, segs[bid])
    return lookup


# ===================================================================== 4-03 tables
PANNA = {"investigation": "vicayo", "investigation of states": "dhammavicayo", "non-delusion": "amoho",
         "right": "sammā", "understanding": "pajānanā", "view": "diṭṭhi", "wisdom": "paññā"}
DITTHI = {"distorted": "vipariyāsa", "distorted grasp": "vipariyāsaggāho", "grasp": "gāho",
          "holding views": "diṭṭhigataṃ", "views": "diṭṭhigataṃ", "kind": "evarūpā"}
MOHA = {"bar": "laṅgī", "delusion": "moho", "ignorance": "avijjā", "knowledge": "ñāṇaṃ",
        "lack of knowledge": "aññāṇaṃ", "root": "mūlaṃ", "unwholesome": "akusala",
        "unwholesome root": "akusalamūlaṃ", "vision": "dassanaṃ", "whatever": "Yaṃ"}
SAMADHI = {"concentration": "samādhi", "mind": "cittassa", "right": "sammā", "stability": "ṭhiti",
           "stability of mind": "cittassa ṭhiti", "whatever": "Yā"}
VIRIYA = {"arousing": "ārambho", "effort": "vāyāmo", "mental": "cetasiko",
          "mental arousing": "cetasiko vīriyārambho", "right": "sammā", "whatever": "Yo"}
SILA = {"body": "kāyiko", "morality": "sīla", "restraint": "saṃvaro", "speech": "vācasiko", "whatever": "Yo"}
AHIRI = {"fearlessness": "anottappañca", "fearlessness of wrongdoing": "anottappañca",
         "shamelessness": "Ahirīkañca", "wrongdoing": "anottappañca", "unwholesome": "akusalā",
         "unwholesome states": "akusalā dhammā"}
HIRI = {"fear": "ottappañca", "fear of wrongdoing": "ottappañca", "moral": "Hirī", "moral shame": "Hirī",
        "shame": "Hirī", "wrongdoing": "ottappañca", "wholesome": "kusalā", "wholesome states": "kusalā dhammā"}
NAMING = {"appellation": "nāmadheyyaṃ", "designation": "paññatti", "expression": "nirutti", "label": "samaññā",
          "naming": "nāmakammaṃ", "pathways": "pathā", "reckoning": "saṅkhā", "usage": "vohāro",
          "utterance": "abhilāpo", "whatever": "Yā"}
VIEW10 = dict(DITTHI, therein="Tattha", self="attā", view="diṭṭhi", whatever="yā")
ENGAGE = {"bad": "pāpakānaṃ", "engaging": "samāpattiyā", "therein": "Tattha", "unwholesome": "akusalānaṃ",
          "unwholesome states": "akusalānaṃ dhammānaṃ"}
SPOKEN = {"accordance": "Sahadhammike", "teaching": "Sahadhammike", "spoken": "vuccamāne", "correct": "vacassatā",
          "taking": "gāhitā", "things": NDE, "therein": "Tattha", "opposing": "vipaccanīka"}
ASSOC = {"associating": "sevanā", "frequenting": "nisevanā", "keeping": "saṃsevanā", "resorting": "bhajanā",
         "closely": "sambhajanā", "devotion": "bhatti", "leaning": "sampavaṅkatā", "towards": "sampavaṅkatā",
         "friends": "mittatā", "having": NDE, "persons": "puggalā", "faith": "saddhā", "learning": "sutā",
         "therein": "Tattha", "whatever": "yā"}
SENSES = {"bad": "pāpakā", "body": "kāyena", "cognising": "viññāya", "covetousness": "abhijjhā",
          "doors": "dvāratā", "ear": "Sotena", "eye": "cakkhunā", "faculties": "indriyānaṃ", "faculty": "indriyaṃ",
          "faculty of mind": "manindriyaṃ", "features": "nimitta", "flow": "anvāssaveyyuṃ", "form": "rūpaṃ",
          "guarding": "gutta", "hearing": "sutvā", "leaves": "viharantaṃ", "mental": "dhammaṃ",
          "mental object": "dhammaṃ", "mind": "manasā", "nose": "ghānena", "object": "dhammaṃ",
          "restraint": "saṃvarāya", "sadness": "domanassā", "seeing": "disvā", "senses": "indriyesu",
          "smell": "gandhaṃ", "smelling": "ghāyitvā", "someone": "ekacco",
          "sound": "saddaṃ", "states of covetousness": "abhijjhādomanassā pāpakā akusalā dhammā", "taste": "rasaṃ",
          "tasting": "sāyitvā", "therein": "Tattha", "tongue": "jivhāya", "touch": "phoṭṭhabbaṃ",
          "touching": "phusitvā", "unrestrained": "asaṃvutaṃ", "unwholesome": "akusalā",
          "unwholesome states": "akusalā dhammā", "visible": "rūpaṃ", "visible form": "rūpaṃ", "whatever": "Yā",
          "grasp": "gāhī", "grasps": "gāhī"}
EATING = {"adornment": "maṇḍanāya", "amusement": "davāya", "beautification": "vibhūsanāya",
          "content": "santuṭṭhitā", "eating": "bhojane", "food": "āhāraṃ", "intoxication": "madāya",
          "knowing": "mattaññutā", "knowing moderation": "mattaññutā", "moderation": "mattaññutā",
          "reflecting": "paṭisaṅkhā", "reflection": "paṭisaṅkhā", "someone": "ekacco", "takes": "āhāreti",
          "therein": "Tattha", "whatever": "Yā"}
VIEWWORLD = {"actions": "kammānaṃ", "ascetics": "samaṇa", "bad": "dukkaṭānaṃ", "beings": "sattā",
             "brahmins": "brāhmaṇā", "direct": "abhiññā", "direct knowledge": "abhiññā", "father": "pitā",
             "fruit": "phalaṃ", "gone": "gatā", "having": NDE, "knowledge": "abhiññā", "known": "pavedentīti",
             "mother": "mātā", "practise": "paṭipannā", "realised": "sacchikatvā", "reborn": "opapātikā",
             "rightly": "sammā", "sacrificed": "hutaṃ", "spontaneously": "opapātikā", "therein": "Tattha",
             "kind": "evarūpā", "whatever": "yā"}


def T(*parts, **kw):
    d = {}
    for p in parts:
        d.update(p)
    d.update(kw)
    return d


def skill(word):
    return {"called skill": f"vuccati {word}", "skill": "kusalatā", "therein": "Tattha", "whatever": "Yā"}


M403 = {
    "1-3-3-0": {"discourse": "Suttantika", "pairs": "duka", "summary": "nikkhepaṃ"},
    "1-1303": {"associated": "sampayuttakā", "knowledge": "vijjā", "states that share": "dhammā vijjābhāgino",
               "true": "vijjā", "true knowledge": "vijjā"},
    "1-1304": {"associated": "sampayuttakā", "ignorance": "avijjā", "states that share": "dhammā avijjābhāgino"},
    "1-1305": {"lightning": "vijju", "like": "upamā", "noble": "ariya", "paths": "maggesu",
               "states like lightning": "dhammā vijjūpamā", "wisdom": "paññā"},
    "1-1306": {"arahantship": "arahatta", "diamond": "vajira", "highest": "Upariṭṭhime", "like": "upamā",
               "path": "magge", "wisdom": "paññā"},
    "1-1307": T(AHIRI, {"foolish": "bālā", "foolish states": "dhammā bālā"}),
    "1-1308": T(HIRI, {"wise": "paṇḍitā", "wise states": "dhammā paṇḍitā"}),
    "1-1309": T(AHIRI, {"dark": "kaṇhā", "dark states": "dhammā kaṇhā"}),
    "1-1310": T(HIRI, {"bright": "sukkā", "bright states": "dhammā sukkā"}),
    "1-1311": {"bodily": "Kāya", "cause": "tapanīyā", "mental": "mano", "misconduct": "duccaritaṃ",
               "torment": "tapanīyā", "unwholesome": "akusalā", "unwholesome states": "akusalā dhammā",
               "verbal": "vacī"},
    "1-1312": {"bodily": "Kāya", "cause": "tapanīyā", "conduct": "caritaṃ", "mental": "mano",
               "states are states": "dhammā atapanīyā", "torment": "tapanīyā", "verbal": "vacī",
               "wholesome": "kusalā", "wholesome states": "kusalā dhammā"},
    "1-1313": T(NAMING, {"names": "adhivacanā", "states are pathways": "dhammā adhivacanapathā"}),
    "1-1314": T(NAMING, {"expressions": "nirutti", "states are pathways": "dhammā niruttipathā"}),
    "1-1315": T(NAMING, {"designations": "paññatti", "states are pathways": "dhammā paññattipathā"}),
    "1-1316": {"aggregate": "khandho", "aggregate of consciousness": "viññāṇakkhandho",
               "aggregate of feeling": "Vedanākkhandho", "aggregate of mental": "saṅkhārakkhandho",
               "aggregate of perception": "saññākkhandho", "consciousness": "viññāṇa", "element": "dhātu",
               "feeling": "Vedanā", "formations": "saṅkhāra", "mental": "saṅkhāra", "mental formations": "saṅkhāra",
               "mentality": "nāmaṃ", "perception": "saññā", "therein": "Tattha", "unconditioned": "asaṅkhatā",
               "unconditioned element": "asaṅkhatā ca dhātu"},
    "1-1317": {"called material": "vuccati rūpaṃ", "called material form": "vuccati rūpaṃ", "derived": "upādāya",
               "elements": "bhūtā", "form": "rūpaṃ", "form derived": "upādāya rūpaṃ", "great elements": "mahābhūtā",
               "material": "rūpaṃ", "material form": "rūpaṃ", "material form derived": "upādāya rūpaṃ",
               "therein": "Tattha"},
    "1-1318": T(MOHA, {"lack": "aññāṇaṃ / adassanaṃ", "therein": "Tattha"}),
    "1-1319": {"continued existence": "bhava", "craving": "taṇhā", "desire": "chando", "existence": "bhava",
               "regard": NDE, "therein": "Tattha", "whatever": "Yo"},
    "1-1320": T(VIEW10, {"called the view": "vuccati bhavadiṭṭhi", "continued existence": "bhava",
                         "exist": "Bhavissati", "existence": "bhava"}),
    "1-1321": T(VIEW10, {"called the view": "vuccati vibhavadiṭṭhi", "exist": "bhavissati",
                         "non-existence": "vibhava"}),
    "1-1322": T(VIEW10, {"eternal": "Sassato", "eternalist": "sassata", "eternalist view": "sassatadiṭṭhi"}),
    "1-1323": T(VIEW10, {"annihilated": "Ucchijjissati", "annihilationist": "uccheda",
                         "annihilationist view": "ucchedadiṭṭhi"}),
    "1-1324": T(VIEW10, {"called the view": "vuccati antavā diṭṭhi"}),
    "1-1325": T(VIEW10, {"called the view": "vuccati anantavā diṭṭhi"}),
    "1-1326": T(VIEW10, {"arises": "uppajjati", "called the view": "vuccati pubbantānudiṭṭhi",
                         "concerning": "anudiṭṭhi / ārabbha", "view arises": "uppajjati diṭṭhi"}),
    "1-1327": T(VIEW10, {"arises": "uppajjati", "called the view": "vuccati aparantānudiṭṭhi",
                         "concerning": "anudiṭṭhi / ārabbha", "view arises": "uppajjati diṭṭhi"}),
    "1-1328": T(ENGAGE, {"ashamed": "hirīyati", "shamelessness": "ahirikaṃ"}),
    "1-1329": T(ENGAGE, {"fear": "ottappitabbena", "fearing": "ottappati", "fearlessness": "anottappaṃ",
                         "fearlessness of wrongdoing": "anottappaṃ", "wrongdoing": "anottappaṃ"}),
    "1-1330": T(ENGAGE, {"ashamed": "hirīyati", "moral": "hirī", "moral shame": "hirī", "shame": "hirī"}),
    "1-1331": T(ENGAGE, {"fear": "ottappaṃ", "fear of wrongdoing": "ottappaṃ", "fearing": "ottappati",
                         "wrongdoing": "ottappaṃ"}),
    "1-1332": T(SPOKEN, {"deference": "paṭissavatā", "delight": "sātatā", "disregard": "anādariyaṃ",
                         "disregarding": "anādaratā", "disrespect": "agāravatā", "hard": "dovacassatā",
                         "intractability": "dovacassāyaṃ", "lack": "appaṭissavatā", "opposite": "vippaṭikūla",
                         "unruliness": "dovacassiyaṃ"}),
    "1-1333": T(ASSOC, {"bad": "pāpa", "immoral": "dussīlā", "stingy": "maccharino", "unwise": "duppaññā"}),
    "1-1334": T(SPOKEN, {"compliance": "sovacassiyaṃ", "deference": "sappaṭissavatā", "delighting": "sātatā",
                         "easy": "sovacassatā", "opposite": "paṭikūla", "regard": "sādariyaṃ",
                         "regarding": "sādaratā", "respect": "sagāravatā", "tractability": "sovacassāyaṃ"}),
    "1-1335": T(ASSOC, {"generous": "cāgavanto", "moral": "sīlavanto", "wise": "paññavanto"}),
    "1-1336": T(PANNA, skill("āpattikusalatā"), {"classes": "khandhā", "offences": "āpatti", "regarding": NDE,
                                                 "respect": NDE}),
    "1-1337": T(PANNA, skill("āpattivuṭṭhānakusalatā"), {"emerging": "vuṭṭhāna", "offences": "āpatti",
                                                         "skill in emerging": "vuṭṭhānakusalatā"}),
    "1-1338": T(PANNA, skill("samāpattikusalatā"), {"applied": "vitakka", "applied thought": "vitakka",
                                                    "attainment": "samāpatti", "attainments": "samāpatti",
                                                    "meditative": "samāpatti", "meditative attainments": "samāpatti",
                                                    "respect": NDE, "sustained": "vicārā",
                                                    "sustained thought": "vicārā", "thought": "vitakka / vicārā"}),
    "1-1339": T(PANNA, skill("samāpattivuṭṭhānakusalatā"), {"attainments": "samāpatti", "emerging": "vuṭṭhāna",
                                                            "meditative": "samāpatti",
                                                            "meditative attainments": "samāpatti",
                                                            "skill in emerging": "vuṭṭhānakusalatā"}),
    "1-1340": T(PANNA, skill("dhātukusalatā"), {
        "body": "kāya", "body element": "kāyadhātu", "body-consciousness": "kāyaviññāṇa",
        "body-consciousness element": "kāyaviññāṇadhātu", "ear": "sota", "ear element": "sotadhātu",
        "ear-consciousness": "sotaviññāṇa", "eighteen": "Aṭṭhārasa", "element": "dhātu", "elements": "dhātu",
        "eye": "cakkhu", "eye element": "cakkhudhātu", "eye-consciousness": "cakkhuviññāṇa",
        "eye-consciousness element": "cakkhuviññāṇadhātu", "mental": "dhamma", "mind": "mano",
        "mind element": "manodhātu", "mind-consciousness": "manoviññāṇa",
        "mind-consciousness element": "manoviññāṇadhātu", "nose": "ghāna", "nose element": "ghānadhātu",
        "nose-consciousness": "ghānaviññāṇa", "objects": "dhamma", "respect": NDE, "smell": "gandha",
        "smell element": "gandhadhātu", "sound": "sadda", "sound element": "saddadhātu", "taste": "rasa",
        "taste element": "rasadhātu", "tongue": "jivhā", "tongue element": "jivhādhātu",
        "tongue-consciousness": "jivhāviññāṇa", "touch": "phoṭṭhabba", "touch element": "phoṭṭhabbadhātu",
        "visible-form": "rūpa", "visible-form element": "rūpadhātu"}),
    "1-1341": T(PANNA, skill("manasikārakusalatā"), {"attention": "manasikāra", "elements": "dhātūnaṃ",
                                                     "respect": NDE, "skill in attention": "manasikārakusalatā"}),
    "1-1342": T(PANNA, skill("āyatanakusalatā"), {
        "bases": "āyatana", "body": "kāya", "body base": "kāyāyatanaṃ", "ear": "sota", "ear base": "sotāyatanaṃ",
        "eye": "cakkhu", "eye base": "cakkhāyatanaṃ", "mental-object": "dhamma",
        "mental-object base": "dhammāyatanaṃ", "mind": "mano", "mind base": "manāyatanaṃ", "nose": "ghāna",
        "nose base": "ghānāyatanaṃ", "respect": NDE, "sense": "āyatana", "sense bases": "āyatana",
        "smell": "gandha", "smell base": "gandhāyatanaṃ", "sound": "sadda", "sound base": "saddāyatanaṃ",
        "taste": "rasa", "taste base": "rasāyatanaṃ", "tongue": "jivhā", "tongue base": "jivhāyatanaṃ",
        "touch": "phoṭṭhabba", "touch base": "phoṭṭhabbāyatanaṃ", "twelve": "Dvādasa", "visible-form": "rūpa",
        "visible-form base": "rūpāyatanaṃ"}),
    "1-1343": T(PANNA, skill("paṭiccasamuppādakusalatā"), {
        "ageing": "jarā", "arising": "samudayo", "bases": "āyatanaṃ", "birth": "jāti", "clinging": "upādānaṃ",
        "condition": "paccayā", "consciousness": "viññāṇaṃ", "contact": "phasso", "craving": "taṇhā",
        "death": "maraṇaṃ", "dependent": "paṭicca", "despair": "upāyāsā", "existence": "bhavo",
        "feeling": "vedanā", "form": "rūpaṃ", "formations": "saṅkhārā", "ignorance": "Avijjā",
        "lamentation": "parideva", "mass": "khandhassa", "material": "rūpaṃ", "material form": "rūpaṃ",
        "mental": "saṅkhārā", "mental formations": "saṅkhārā", "mentality": "nāma", "origination": "samuppāda",
        "pain": "dukkha", "sadness": "domanassa", "sense": "āyatanaṃ", "sense bases": "āyatanaṃ",
        "sorrow": "soka", "suffering": "dukkha", "whole": "kevalassa"}),
    "1-1344": T(PANNA, skill("ṭhānakusalatā"), {"arising": "uppādāya", "case": "taṃ taṃ", "roots": "hetū",
                                                "variant": NDE, "whatever": "Ye ye"}),
    "1-1345": T(PANNA, skill("aṭṭhānakusalatā"), {"arising": "uppādāya", "case": "taṃ taṃ", "impossible": "aṭṭhāna",
                                                  "roots": "hetū", "whatever": "Ye ye"}),
    "1-1346": {"crookedness": "vaṅkatā", "deviousness": "jimhatā", "freedom": "ajimhatā / avaṅkatā / akuṭilatā",
               "straightforwardness": "ajjavo", "therein": "Tattha", "twistedness": "kuṭilatā", "whatever": "Yā"},
    "1-1347": {"freedom": "akakkhaḷatā / akathinatā", "hardness": "kakkhaḷatā", "humility": "nīca",
               "mildness": "maddavo", "mind": "cittatā", "pliancy": "mudutā", "rigidity": "kathinatā",
               "softness": "maddavatā", "therein": "Tattha", "whatever": "Yā"},
    "1-1348": {"contentment": "attamanatā", "endurance": "adhivāsanatā", "forbearance": "khamanatā",
               "mind": "cittassa", "non-abusiveness": "anasuropo", "non-ferocity": "acaṇḍikkaṃ",
               "patience": "khanti", "therein": "Tattha", "whatever": "Yā"},
    "1-1349": T(SILA, {"gentleness": "soraccaṃ", "non-transgression": "avītikkamo", "therein": "Tattha"}),
    "1-1350": {"anger": "kodha", "blameless": "neḷā", "bordering": "sāmantā", "concentration": "samādhi",
               "conducive": "saṃvattanikā", "courteous": "sakhila", "courtesy": "sākhalyaṃ", "ear": "kaṇṇa",
               "going": "gamā", "harsh": "kakkasā", "having": NDE, "heart": "hadaya", "hurtful": "kaṭukā",
               "kind": "tathārūpiṃ", "liked": "kantā", "lovable": "pemanīyā", "non-harsh": "apharusa",
               "offensive": "abhisajjanī", "others": "para", "pleasing": "sukhā / manāpā", "polite": "porī",
               "rough": "aṇḍakā", "smooth": "saṇha", "speaks": "bhāsitā hoti", "speech": "vācā",
               "therein": "Tattha", "whatever": "yā"},
    "1-1351": {"hospitable": "paṭisanthārako", "hospitality": "paṭisanthāro", "kinds": "paṭisanthārā",
               "material": "āmisa", "someone": "ekacco", "teaching": "dhamma", "therein": "Tattha",
               "things": "āmisa"},
    "1-1352": T(SENSES, {"guard": "rakkhati", "non-guarding": "agutti", "non-protection": "agopanā",
                         "non-restraint": "asaṃvaro", "non-watching": "anārakkho", "practise": "paṭipajjati",
                         "undertake": "āpajjati"}),
    "1-1353": T(EATING, {"lack": "appaṭisaṅkhā", "unwisely": "ayoniso"}),
    "1-1354": T(SENSES, {"guards": "rakkhati", "practises": "paṭipajjati", "protection": "gopanā",
                         "undertakes": "āpajjati", "watching": "ārakkho"}),
    "1-1355": T(EATING, {"assisting": "anuggahāya", "blamelessness": "anavajjatā", "body": "kāyassa",
                         "discomfort": "vihiṃsā", "ease": "phāsu", "feeling": "vedanaṃ", "holy": "brahmacariya",
                         "life": "brahmacariya / yātrā", "living": "vihāro", "maintenance": "yāpanāya",
                         "old": "purāṇañca", "thinking": "cāti", "wisely": "yoniso"}),
    "1-1356": {"away": "pilāpanatā", "floating": "pilāpanatā", "forgetfulness": "muṭṭhasaccaṃ",
               "forgetting": "sammusanatā", "keeping": "dhāraṇatā", "lack": "asati / ananussati / appaṭissati",
               "mind": "dhāraṇatā", "mindfulness": "sati", "recall": "paṭissati", "recollection": "anussati",
               "remembering": "saraṇatā", "therein": "Tattha", "whatever": "Yā"},
    "1-1357": T(MOHA, {"awareness": "sampajaññaṃ", "clear": "sampajaññaṃ", "clear awareness": "sampajaññaṃ",
                       "lack": "asampajaññaṃ / aññāṇaṃ / adassanaṃ", "therein": "Tattha"}),
    "1-1358": {"away": "pilāpanatā", "faculty": "indriyaṃ", "faculty of mindfulness": "satindriyaṃ",
               "floating": "pilāpanatā", "forgetting": "sammusanatā", "keeping": "dhāraṇatā", "mind": "dhāraṇatā",
               "mindfulness": "sati", "power": "balaṃ", "power of mindfulness": "satibalaṃ", "recall": "paṭissati",
               "recollection": "anussati", "remembering": "saraṇatā", "right": "sammā", "therein": "Tattha",
               "whatever": "Yā"},
    "1-1359": T(PANNA, {"awareness": "sampajaññaṃ", "clear": "sampajaññaṃ", "clear awareness": "sampajaññaṃ",
                        "therein": "Tattha", "whatever": "Yā"}),
    "1-1360": T(PANNA, {"power": "balaṃ", "reflection": "paṭisaṅkhāna", "therein": "Tattha", "whatever": "Yā"}),
    "1-1361": {"awakening": "bojjhaṅgā", "factors": "bojjhaṅgā", "power": "balaṃ", "practice": "āsevanā",
               "repeated": "bahulīkammaṃ", "therein": "Tattha", "whatever": "Yā", "wholesome": "kusalānaṃ",
               "wholesome states": "kusalānaṃ dhammānaṃ"},
    "1-1362": T(SAMADHI, {"calm": "samatho", "therein": "Tattha"}),
    "1-1363": T(PANNA, {"insight": "vipassanā", "therein": "Tattha", "whatever": "Yā"}),
    "1-1364": T(SAMADHI, {"calm": "samatha", "sign": "nimittaṃ", "therein": "Tattha"}),
    "1-1365": T(VIRIYA, {"exertion": "paggāha", "sign": "nimittaṃ", "therein": "Tattha"}),
    "1-1366": T(VIRIYA, {"exertion": "paggāho", "therein": "Tattha"}),
    "1-1367": T(SAMADHI, {"non-distraction": "avikkhepo", "therein": "Tattha"}),
    "1-1368": T(SILA, {"failure": "vipatti", "immorality": "dussilyaṃ", "therein": "Tattha",
                       "transgression": "vītikkamo"}),
    "1-1369": T(VIEWWORLD, DITTHI, {"exist": "atthi", "failure": "vipatti", "nothing": "natthi", "view": "diṭṭhi",
                                    "wrong": "micchā", "wrong view": "micchādiṭṭhi"}),
    "1-1370": T(SILA, {"accomplishment": "sampadā", "non-transgression": "avītikkamo", "therein": "Tattha"}),
    "1-1371": T(VIEWWORLD, PANNA, {"accomplishment": "sampadā", "view": "diṭṭhi"}),
    "1-1372": T(SILA, {"non-transgression": "avītikkamo", "purification": "visuddhi", "therein": "Tattha"}),
    "1-1373": {"conformity": "anulomika", "fruit": "phala", "knowledge": "ñāṇaṃ", "ownership": "Kammassakata",
               "path": "magga", "possesses": "samaṅgissa", "purification": "visuddhi", "therein": "Tattha",
               "truths": "sacca", "view": "diṭṭhi"},
    "1-1374": T(PANNA, {"purification": "visuddhi", "view": "Diṭṭhi", "whatever": "yā"}),
    "1-1375": T(VIRIYA, {"effort": "padhānanti / vāyāmo", "keeping": "Yathā", "view": "diṭṭhissa",
                         "whatever": "yo"}),
    "1-1376": {"ageing": "jarā", "birth": "jāti", "death": "maraṇa", "fear": "bhayaṃ", "sense": "Saṃvego",
               "sickness": "byādhi", "stir": "Saṃvejaniyaṃ", "things": "ṭhānanti", "urgency": "Saṃvego",
               "variant": NDE},
    "1-1377": {"abandoning": "pahānāya", "abundance": "vepullāya", "arisen": "uppannānaṃ", "arising": "uppādāya",
               "arouses": "ārabhati", "bad": "pāpakānaṃ", "bhikkhu": "bhikkhu", "continuance": "ṭhitiyā",
               "desire": "chandaṃ", "effort": "padhānanti / vāyamati", "exerts": "paggaṇhāti",
               "exerts the mind": "cittaṃ paggaṇhāti", "fulfilment": "pāripūriyā", "generates": "janeti",
               "makes": "vāyamati", "mind": "cittaṃ", "mind and strives": "cittaṃ paggaṇhāti padahati",
               "non-arising": "anuppādāya", "non-decline": "asammosāya", "stirred": "Saṃviggassa",
               "strives": "padahati", "unwholesome": "akusalānaṃ", "unwholesome states": "akusalānaṃ dhammānaṃ",
               "wholesome": "kusalānaṃ", "wholesome states": "kusalānaṃ dhammānaṃ", "wise": "yoniso"},
    "1-1378": {"content": "santuṭṭhitā", "whatever": "yā", "wholesome": "kusalesu",
               "wholesome states": "kusalesu dhammesūti", "wish": "kamyatā"},
    "1-1379": {"acting": "kiriyatā", "burden": "dhuratā", "carefully": "sakkacca", "desire": "chandatā",
               "effort": "padhānasminti", "persistently": "sātacca", "practice": "āsevanā", "putting": "nikkhitta",
               "repeated": "bahulīkammaṃ", "sluggish": "olīna", "stopping": "ṭhita", "whatever": "yā",
               "wholesome": "kusalānaṃ", "wholesome states": "kusalānaṃ dhammānaṃ"},
    "1-1380": {"away": "cuti", "beings": "sattānaṃ", "destruction": "khaye", "kinds": "vijjā",
               "knowledge": "Vijjā / ñāṇaṃ", "lives": "nivāsa", "passing": "cuti", "reappearance": "upapāte",
               "recollection": "anussati", "taints": "āsavānaṃ", "true": "Vijjā", "true knowledge": "Vijjā"},
    "1-1381": {"cittassa": NDE, "kinds": "vimuttiyo", "liberation": "Vimuttīti", "mind": "cittassa",
               "release": "adhimutti", "variant": NDE},
    "1-1382": {"destruction": "Khaye", "knowledge": "ñāṇanti", "path": "magga", "possesses": "samaṅgissa"},
    "1-1383": {"chapter": "kaṇḍaṃ", "complete": "niṭṭhitaṃ", "fruit": "phala", "knowledge": "ñāṇanti",
               "non-arising": "Anuppāde", "possesses": "samaṅgissa", "summaries": "Nikkhepa"},
}
# shared-piece overrides that the shared tables would get wrong
M403["1-1333"]["whatever"] = "yā"
M403["1-1335"]["whatever"] = "yā"
M403["1-1371"]["whatever"] = "yā"
M403["1-1371"]["right"] = "sammā"


def table_403():
    return lambda bid, kw: M403[bid].get(kw)


# ===================================================================== build
def build(ch, lookup):
    src = (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()
    out, missing, used = [], [], defaultdict(set)
    for line in src:
        bid, rest = line.split("] ", 1)
        bid = bid[1:]
        kws = [k.strip() for k in rest.split(", ")]
        pairs = []
        for k in kws:
            v = lookup(bid, k.lower())
            if v is None:
                missing.append((bid, k))
                v = "???"
            assert ", " not in v, (bid, k, v)
            used[bid].add(k.lower())
            pairs.append(f"{v}={k}")
        out.append(f"[{bid}] " + ", ".join(pairs))
    (HERE / f"{ch}.mapped.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(ch, "lines", len(out), "missing", missing)
    return out, used


def review(ch, out):
    """per keyword (lowercased): the distinct values used across the chapter, with counts"""
    agg = defaultdict(Counter)
    for line in out:
        for p in line.split("] ", 1)[1].split(", "):
            v, k = p.rsplit("=", 1)
            agg[k.lower()][v] += 1
    for k in sorted(agg):
        print(f"  {k}: " + " | ".join(f"{v} x{n}" for v, n in agg[k].most_common()))


if __name__ == "__main__":
    o1, u1 = build("2-05-cittuppadakandam", table_205())
    o2, u2 = build("4-03-nikkhepakandam", table_403())
    unused = [(b, k) for b, d in M403.items() for k in d if k not in u2[b]]
    unused += [(b, k) for b, d in HEAD_205.items() for k in d if k not in u1[b]]
    print("unused table keys", unused)
    if "--review" in sys.argv:
        review("2-05", o1)
        review("4-03", o2)
