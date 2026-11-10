"""Build the English plain zero-shot SAMPLE of pi-1 ch.2 opening (^1-1 ... ^1-57).

usage: python -I -X utf8 build_ch2_01_sample.py
All recurring strings are fixed constants below, so every repeat is byte-identical.
Exposes NAMES, STRINGS and FRAMES for build_terms.py.
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
PALI = HERE / "ch2-01-pali-1-122.md"
OUT = HERE / "ch2-01-sample.md"

DASH = "–"  # the en dash used by the Pāli source

# ---- headings ------------------------------------------------------------------------
H_CH2 = "### The Chapter on the Arising of Mind"
H_KAMA_KUSALA = "#### The Wholesome Mind of the Sense Sphere"
H_PADA = "##### The Analysis of the Terms"
END_PADA = "The analysis of the terms."
END_BHANA1 = "The first recitation section."

# ---- names of the factors (Pāli stem = English), used in the list and in Q/A frames ------
NAMES = {
    "phasso": "contact",
    "vedanā": "feeling",
    "saññā": "perception",
    "cetanā": "intention",
    "cittaṃ": "mind",
    "vitakko": "applied thought",
    "vicāro": "sustained thought",
    "pīti": "rapture",
    "sukhaṃ": "happiness",
    "cittassekaggatā": "one-pointedness of mind",
    "saddhindriyaṃ": "the faculty of faith",
    "vīriyindriyaṃ": "the faculty of energy",
    "satindriyaṃ": "the faculty of mindfulness",
    "samādhindriyaṃ": "the faculty of concentration",
    "paññindriyaṃ": "the faculty of wisdom",
    "manindriyaṃ": "the faculty of mind",
    "somanassindriyaṃ": "the faculty of joy",
    "jīvitindriyaṃ": "the faculty of life",
    "sammādiṭṭhi": "right view",
    "sammāsaṅkappo": "right thought",
    "sammāvāyāmo": "right effort",
    "sammāsati": "right mindfulness",
    "sammāsamādhi": "right concentration",
    "saddhābalaṃ": "the power of faith",
    "vīriyabalaṃ": "the power of energy",
    "satibalaṃ": "the power of mindfulness",
    "samādhibalaṃ": "the power of concentration",
    "paññābalaṃ": "the power of wisdom",
    "hiribalaṃ": "the power of moral shame",
    "ottappabalaṃ": "the power of fear of wrongdoing",
    "alobho": "non-greed",
    "adoso": "non-hate",
    "amoho": "non-delusion",
    "anabhijjhā": "non-covetousness",
    "abyāpādo": "non-ill-will",
    "hirī": "moral shame",
    "ottappaṃ": "fear of wrongdoing",
    "kāyapassaddhi": "tranquillity of the mental body",
    "cittapassaddhi": "tranquillity of mind",
    "kāyalahutā": "lightness of the mental body",
    "cittalahutā": "lightness of mind",
    "kāyamudutā": "pliancy of the mental body",
    "cittamudutā": "pliancy of mind",
    "kāyakammaññatā": "workability of the mental body",
    "cittakammaññatā": "workability of mind",
    "kāyapāguññatā": "proficiency of the mental body",
    "cittapāguññatā": "proficiency of mind",
    "kāyujukatā": "uprightness of the mental body",
    "cittujukatā": "uprightness of mind",
    "sati": "mindfulness",
    "sampajaññaṃ": "clear awareness",
    "samatho": "calm",
    "vipassanā": "insight",
    "paggāho": "exertion",
    "avikkhepo": "non-distraction",
}
N = NAMES

# ---- fixed synonym strings (Pāli string = English string) -----------------------------
TAJJA = "born of the contact of the corresponding mind-consciousness element"
G_KAYA = "in the aggregate of feeling, the aggregate of perception and the aggregate of mental formations"
G_CITTA = "in the aggregate of consciousness"
G_JIVITA = "in those immaterial states"
ROOT = "the wholesome root"

STRINGS = {
    "phasso phusanā saṃphusanā saṃphusitattaṃ":
        "contact, touching, coming into contact, the state of having come into contact",
    "cetasikaṃ sātaṃ cetasikaṃ sukhaṃ cetosamphassajaṃ sātaṃ sukhaṃ vedayitaṃ cetosamphassajā sātā sukhā vedanā":
        "mental comfort, mental happiness, the comfortable, pleasant experience born of mind-contact, "
        "the comfortable, pleasant feeling born of mind-contact",
    "saññā sañjānanā sañjānitattaṃ":
        "perception, perceiving, the state of having perceived",
    "cetanā sañcetanā cetayitattaṃ":
        "intention, intending, the state of having intended",
    "cittaṃ mano mānasaṃ hadayaṃ paṇḍaraṃ mano manāyatanaṃ manindriyaṃ viññāṇaṃ viññāṇakkhandho tajjāmanoviññāṇadhātu":
        "mind, intellect, mental activity, heart, radiance, intellect, the mind base, the faculty of mind, "
        "consciousness, the aggregate of consciousness, the corresponding mind-consciousness element",
    "takko vitakko saṅkappo appanā byappanā cetaso abhiniropanā sammāsaṅkappo":
        "thinking, applied thought, thought, fixing, firm fixing, the directing of the mind, right thought",
    "cāro vicāro anuvicāro upavicāro cittassa anusandhānatā anupekkhanatā":
        "exploring, sustained thought, continued exploring, close exploring, the mind's staying connected, "
        "its continued observing",
    "pīti pāmojjaṃ āmodanā pamodanā hāso pahāso vitti odagyaṃ attamanatā cittassa":
        "rapture, gladness, delight, rejoicing, mirth, merriment, satisfaction, elation, contentment of mind",
    "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ sammāsamādhi":
        "the stability of mind, its steadiness, its firmness, non-scattering, non-distraction, "
        "the state of an unscattered mind, calm, the faculty of concentration, the power of concentration, "
        "right concentration",
    "saddhā saddahanā okappanā abhippasādo saddhā saddhindriyaṃ saddhābalaṃ":
        "faith, trusting, confiding, full confidence, faith, the faculty of faith, the power of faith",
    "cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti asithilaparakkamatā "
    "anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ vīriyindriyaṃ vīriyabalaṃ sammāvāyāmo":
        "the mental arousing of energy, setting out, pressing forward, striving, effort, zeal, ardour, strength, "
        "steadfastness, unslackening pressing forward, not putting down desire, not putting down the burden, "
        "firm grasping of the burden, energy, the faculty of energy, the power of energy, right effort",
    "sati anussati paṭissati sati saraṇatā dhāraṇatā apilāpanatā asammussanatā sati satindriyaṃ satibalaṃ sammāsati":
        "mindfulness, recollection, recall, mindfulness, remembering, keeping in mind, not floating away, "
        "not forgetting, mindfulness, the faculty of mindfulness, the power of mindfulness, right mindfulness",
    "paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ kosallaṃ "
    "nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo paññā "
    "paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto paññāratanaṃ "
    "amoho dhammavicayo sammādiṭṭhi":
        "wisdom, understanding, investigation, close investigation, investigation of states, discerning, "
        "distinguishing, differentiating, learning, skill, subtlety, clarity, consideration, examination, "
        "breadth, intelligence, guidance, insight, clear awareness, a goad, wisdom, the faculty of wisdom, "
        "the power of wisdom, the sword of wisdom, the tower of wisdom, the light of wisdom, "
        "the radiance of wisdom, the lamp of wisdom, the jewel of wisdom, non-delusion, "
        "investigation of states, right view",
    "āyu ṭhiti yapanā yāpanā iriyanā vattanā pālanā jīvitaṃ jīvitindriyaṃ":
        "lifespan, persistence, carrying on, keeping going, moving, continuing, protection, life, "
        "the faculty of life",
    "hirīyati hiriyitabbena hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        "being ashamed of what one should be ashamed of, being ashamed of engaging in bad, unwholesome states",
    "ottappati ottappitabbena ottappati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā":
        "fearing what one should fear, fearing engaging in bad, unwholesome states",
    "alobho alubbhanā alubbhitattaṃ asārāgo asārajjanā asārajjitattaṃ anabhijjhā alobho kusalamūlaṃ":
        "non-greed, not being greedy, the state of not being greedy, non-lust, not lusting, "
        "the state of not lusting, non-covetousness, non-greed, " + ROOT,
    "adoso adussanā adussitattaṃ abyāpādo abyāpajjo adoso kusalamūlaṃ":
        "non-hate, not hating, the state of not hating, non-ill-will, absence of malice, non-hate, " + ROOT,
    "passaddhi paṭipassaddhi passambhanā paṭipassambhanā paṭipassambhitattaṃ":
        "tranquillity, full tranquillity, calming, full calming, the state of being fully calmed",
    "lahutā lahupariṇāmatā adandhanatā avitthanatā":
        "lightness, quickness to change, freedom from slowness, freedom from sluggishness",
    "mudutā maddavatā akakkhaḷatā akathinatā":
        "pliancy, softness, freedom from roughness, freedom from hardness",
    "kammaññatā kammaññattaṃ kammaññabhāvo":
        "workability, being workable, the condition of being workable",
    "paguṇatā paguṇattaṃ paguṇabhāvo":
        "proficiency, being proficient, the condition of being proficient",
    "ujutā ujukatā ajimhatā avaṅkatā akuṭilatā":
        "straightness, uprightness, freedom from deviousness, freedom from crookedness, freedom from twistedness",
}
S = {k.split()[0] if not k.startswith("cetasikaṃ sātaṃ") else "sāta": v for k, v in STRINGS.items()}
assert len(S) == len(STRINGS)
# short keys
S_PHASSA = S["phasso"]
S_SUKHA = S["sāta"]
S_SANNA = S["saññā"]
S_CETANA = S["cetanā"]
S_CITTA = S["cittaṃ"]
S_VITAKKA = S["takko"]
S_VICARA = S["cāro"]
S_PITI = S["pīti"]
S_SAMADHI = S["cittassa"]
S_SADDHA = S["saddhā"]
S_VIRIYA = S["cetasiko"]
S_SATI = S["sati"]
S_PANNA = S["paññā"]
S_JIVITA = S["āyu"]
S_HIRI = S["hirīyati"]
S_OTTAPPA = S["ottappati"]
S_ALOBHA = S["alobho"]
S_ADOSA = S["adoso"]
S_PASSADDHI = S["passaddhi"]
S_LAHUTA = S["lahutā"]
S_MUDUTA = S["mudutā"]
S_KAMMANNATA = S["kammaññatā"]
S_PAGUNATA = S["paguṇatā"]
S_UJUTA = S["ujutā"]

# variant-bearing forms (first occurrences in ^1-5, ^1-13, ^1-19, ^1-33, ^1-40)
S_CETANA_V = S_CETANA + " [variant: sañcetayitattaṃ (Syā.)]"
S_VIRIYA_V = S_VIRIYA.replace("the mental arousing of energy,",
                              "the mental arousing of energy [variant: viriyārambho (Sī., Syā.)],"
                              ).replace("ardour,", "ardour [variant: ussoḷhi (Sī.)],")
S_JIVITA_V = S_JIVITA.replace("moving,", "moving [variant: irīyanā (Sī.)],")
S_ADOSA_V = S_ADOSA.replace("the state of not hating,",
                            "the state of not hating [variant: adūsanā adūsitattaṃ (Syā.)],", 1)
S_PASSADDHI_V = (S_PASSADDHI
                 .replace("full tranquillity,", "full tranquillity [variant: paṭippassaddhi (Sī., Syā.)],")
                 .replace("full calming,", "full calming [variant: paṭippassambhanā (Sī., Syā.)],")
                 + " [variant: paṭippassambhitattaṃ (Sī., Syā.)]")
for a, b in ((S_CETANA, S_CETANA_V), (S_VIRIYA, S_VIRIYA_V), (S_JIVITA, S_JIVITA_V),
             (S_ADOSA, S_ADOSA_V), (S_PASSADDHI, S_PASSADDHI_V)):
    assert a != b and b.count("[variant:") >= 1, b

# ---- frames ----------------------------------------------------------------------------
FRAMES = {
    "Katamo/Katamā/Katamaṃ tasmiṃ samaye X hoti?": "What is X at that time?",
    "Yo/Yā/Yaṃ tasmiṃ samaye S – ayaṃ/idaṃ tasmiṃ samaye X hoti.":
        "Whatever at that time is S – this is X at that time.",
    "Yā/Yaṃ tasmiṃ samaye tajjāmanoviññāṇadhātusamphassajā/-jaṃ S – ayaṃ tasmiṃ samaye X hoti.":
        "Whatever at that time, " + TAJJA + ", is S – this is X at that time.",
    "Yā tasmiṃ samaye vedanākkhandhassa saññākkhandhassa saṅkhārakkhandhassa S – ayaṃ tasmiṃ samaye X hoti.":
        "Whatever at that time, " + G_KAYA + ", is S – this is X at that time.",
    "Yā tasmiṃ samaye viññāṇakkhandhassa S – ayaṃ tasmiṃ samaye X hoti.":
        "Whatever at that time, " + G_CITTA + ", is S – this is X at that time.",
    "Yo tesaṃ arūpīnaṃ dhammānaṃ S – idaṃ tasmiṃ samaye X hoti.":
        "Whatever, " + G_JIVITA + ", is S – this is X at that time.",
    "Yaṃ tasmiṃ samaye hirīyati… / ottappati… – idaṃ/ayaṃ tasmiṃ samaye X hoti.":
        "At that time, S – this is X at that time.",
    "Ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā kusalā.":
        "Or whatever other dependently arisen immaterial states there are at that time – these states are wholesome.",
    "Katame dhammā kusalā?": "What states are wholesome?",
    "Yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti somanassasahagataṃ ñāṇasampayuttaṃ":
        "At a time when a wholesome mind of the sense sphere has arisen, accompanied by joy and associated with knowledge",
    "rūpārammaṇaṃ vā saddārammaṇaṃ vā gandhārammaṇaṃ vā rasārammaṇaṃ vā phoṭṭhabbārammaṇaṃ vā dhammārammaṇaṃ vā yaṃ yaṃ vā panārabbha":
        "with a visible form as its object, or a sound as its object, or a smell as its object, or a taste as its object, "
        "or a touch as its object, or a mental object as its object, or whatever it takes up as its object",
    "tasmiṃ samaye X hoti, Y hoti, …": "at that time there is X, there is Y, …",
}
YEVAPANA = "whatever other dependently arisen immaterial states there are at that time " + DASH + " these states are wholesome."


def Q(x):
    return f"What is {x} at that time?"


def A(s, x, pre=""):
    """pre: '' or ', <qualifier>,' inserted after 'Whatever at that time'."""
    return f"Whatever at that time{pre} is {s} {DASH} this is {x} at that time."


def QA(key, s, pre="", end="."):
    x = N[key]
    a = A(s, x, pre)
    if end != ".":
        a = a[:-1] + end
    return Q(x) + " " + a


def T(s, x):
    return A(s, x, ", " + TAJJA + ",")


def KAYA(key, s):
    return Q(N[key]) + " " + A(s, N[key], ", " + G_KAYA + ",")


def CITTA(key, s):
    return Q(N[key]) + " " + A(s, N[key], ", " + G_CITTA + ",")


def SHAME(key, s):
    return Q(N[key]) + f" At that time, {s} {DASH} this is {N[key]} at that time."


# ---- ^1-1 ------------------------------------------------------------------------------
LIST_1_1 = [
    ("phasso", ""), ("vedanā", ""), ("saññā", ""), ("cetanā", ""), ("cittaṃ", ""), ("vitakko", ""),
    ("vicāro", ""), ("pīti", ""), ("sukhaṃ", ""), ("cittassekaggatā", ""), ("saddhindriyaṃ", ""),
    ("vīriyindriyaṃ", " [variant: viriyindriyaṃ (Sī., Syā.)]"), ("satindriyaṃ", ""), ("samādhindriyaṃ", ""),
    ("paññindriyaṃ", ""), ("manindriyaṃ", ""), ("somanassindriyaṃ", ""), ("jīvitindriyaṃ", ""),
    ("sammādiṭṭhi", ""), ("sammāsaṅkappo", ""), ("sammāvāyāmo", ""), ("sammāsati", ""), ("sammāsamādhi", ""),
    ("saddhābalaṃ", ""), ("vīriyabalaṃ", " [variant: viriyabalaṃ (Sī., Syā.)]"), ("satibalaṃ", ""),
    ("samādhibalaṃ", ""), ("paññābalaṃ", ""), ("hiribalaṃ", ""), ("ottappabalaṃ", ""), ("alobho", ""),
    ("adoso", ""), ("amoho", ""), ("anabhijjhā", ""), ("abyāpādo", ""), ("sammādiṭṭhi", ""), ("hirī", ""),
    ("ottappaṃ", ""), ("kāyapassaddhi", " [variant: kāyappassaddhi (Syā.)]"),
    ("cittapassaddhi", " [variant: cittappassaddhi (Syā.)]"), ("kāyalahutā", ""), ("cittalahutā", ""),
    ("kāyamudutā", ""), ("cittamudutā", ""), ("kāyakammaññatā", ""), ("cittakammaññatā", ""),
    ("kāyapāguññatā", ""), ("cittapāguññatā", ""), ("kāyujukatā", " [variant: kāyujjukatā (Sī., Ka.)]"),
    ("cittujukatā", " [variant: cittujjukatā (Sī., Ka.)]"), ("sati", ""), ("sampajaññaṃ", ""), ("samatho", ""),
    ("vipassanā", ""), ("paggāho", ""), ("avikkhepo", ""),
]
SEG_1_1 = (
    "What states are wholesome? At a time when a wholesome mind of the sense sphere has arisen, "
    "accompanied by joy and associated with knowledge, with a visible form as its object, or a sound as its object, "
    "or a smell as its object, or a taste as its object, or a touch as its object, or a mental object as its object, "
    "or whatever it takes up as its object, at that time "
    + ", ".join(f"there is {N[k]}{v}" for k, v in LIST_1_1)
    + "; or " + YEVAPANA
)

# ---- segments in source order --------------------------------------------------------
SEGMENTS = [
    ("1-1-0", [H_CH2]),
    ("1-1-1-0", [H_KAMA_KUSALA]),
    ("1-1-1-1-0", [H_PADA]),
    ("1-1", [SEG_1_1]),
    ("1-2", [QA("phasso", S_PHASSA)]),
    ("1-3", [Q(N["vedanā"]) + " " + T(S_SUKHA, N["vedanā"])]),
    ("1-4", [Q(N["saññā"]) + " " + T(S_SANNA, N["saññā"])]),
    ("1-5", [Q(N["cetanā"]) + " " + T(S_CETANA_V, N["cetanā"])]),
    ("1-6", [QA("cittaṃ", S_CITTA)]),
    ("1-7", [QA("vitakko", S_VITAKKA)]),
    ("1-8", [QA("vicāro", S_VICARA)]),
    ("1-9", [QA("pīti", S_PITI)]),
    ("1-10", [QA("sukhaṃ", S_SUKHA)]),
    ("1-11", [QA("cittassekaggatā", S_SAMADHI)]),
    ("1-12", [QA("saddhindriyaṃ", S_SADDHA)]),
    ("1-13", [QA("vīriyindriyaṃ", S_VIRIYA_V)]),
    ("1-14", [QA("satindriyaṃ", S_SATI)]),
    ("1-15", [QA("samādhindriyaṃ", S_SAMADHI)]),
    ("1-16", [QA("paññindriyaṃ", S_PANNA)]),
    ("1-17", [QA("manindriyaṃ", S_CITTA)]),
    ("1-18", [QA("somanassindriyaṃ", S_SUKHA)]),
    ("1-19", [Q(N["jīvitindriyaṃ"]) + " " + f"Whatever, {G_JIVITA}, is {S_JIVITA_V} {DASH} this is "
              f"{N['jīvitindriyaṃ']} at that time."]),
    ("1-20", [QA("sammādiṭṭhi", S_PANNA)]),
    ("1-21", [QA("sammāsaṅkappo", S_VITAKKA)]),
    ("1-22", [QA("sammāvāyāmo", S_VIRIYA)]),
    ("1-23", [QA("sammāsati", S_SATI)]),
    ("1-24", [QA("sammāsamādhi", S_SAMADHI)]),
    ("1-25", [QA("saddhābalaṃ", S_SADDHA)]),
    ("1-26", [QA("vīriyabalaṃ", S_VIRIYA)]),
    ("1-27", [QA("satibalaṃ", S_SATI)]),
    ("1-28", [QA("samādhibalaṃ", S_SAMADHI)]),
    ("1-29", [QA("paññābalaṃ", S_PANNA)]),
    ("1-30", [SHAME("hiribalaṃ", S_HIRI)]),
    ("1-31", [SHAME("ottappabalaṃ", S_OTTAPPA)]),
    ("1-32", [QA("alobho", S_ALOBHA)]),
    ("1-33", [QA("adoso", S_ADOSA_V, end="?")]),  # the Pāli ends this answer with "?" (source slip)
    ("1-34", [QA("amoho", S_PANNA + ", " + N["amoho"] + ", " + ROOT)]),
    ("1-35", [QA("anabhijjhā", S_ALOBHA)]),
    ("1-36", [QA("abyāpādo", S_ADOSA)]),
    ("1-37", [QA("sammādiṭṭhi", S_PANNA)]),
    ("1-38", [SHAME("hirī", S_HIRI)]),
    ("1-39", [SHAME("ottappaṃ", S_OTTAPPA)]),
    ("1-40", [KAYA("kāyapassaddhi", S_PASSADDHI_V)]),
    ("1-41", [CITTA("cittapassaddhi", S_PASSADDHI)]),
    ("1-42", [KAYA("kāyalahutā", S_LAHUTA)]),
    ("1-43", [CITTA("cittalahutā", S_LAHUTA)]),
    ("1-44", [KAYA("kāyamudutā", S_MUDUTA)]),
    ("1-45", [CITTA("cittamudutā", S_MUDUTA)]),
    ("1-46", [KAYA("kāyakammaññatā", S_KAMMANNATA)]),
    ("1-47", [CITTA("cittakammaññatā", S_KAMMANNATA)]),
    ("1-48", [KAYA("kāyapāguññatā", S_PAGUNATA)]),
    ("1-49", [CITTA("cittapāguññatā", S_PAGUNATA)]),
    ("1-50", [KAYA("kāyujukatā", S_UJUTA)]),
    ("1-51", [CITTA("cittujukatā", S_UJUTA)]),
    ("1-52", [QA("sati", S_SATI)]),
    ("1-53", [QA("sampajaññaṃ", S_PANNA)]),
    ("1-54", [QA("samatho", S_SAMADHI)]),
    ("1-55", [QA("vipassanā", S_PANNA)]),
    ("1-56", [QA("paggāho", S_VIRIYA)]),
    ("1-57", [QA("avikkhepo", S_SAMADHI), "Or " + YEVAPANA, END_PADA, END_BHANA1]),
]


def cap(line):
    return line[0].upper() + line[1:]


def build():
    out = []
    for bid, lines in SEGMENTS:
        lines = [cap(l) for l in lines]
        lines[-1] += f" ^{bid}"
        out.append("\n".join(lines))
    return "\n\n".join(out) + "\n"


TEXT = build()

if __name__ == "__main__":
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT)
