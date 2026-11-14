"""Build the English plain zero-shot of pi-1 part 2-05 (end of the consciousness chapter).

usage: python -I -X utf8 build_2-05.py
Each Pāli line is split at '…pe…'; every chunk is translated by fixed rules / fixed strings
below (same Pāli chunk = same English), then the chunks are re-joined with '…'.
Shared constants come from the approved sample builder (build_ch2_01_sample.py).
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_ch2_01_sample as C  # noqa: E402  (importing does not rebuild the sample)

ROOT = HERE.parents[3]
PART = "2-05-cittuppadakandam.md"
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / PART
OUT = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters" / PART

DASH = C.DASH
PE = "…"

# ---- headings and closing lines --------------------------------------------------------
HEAD = {
    "Lokuttaravipāka-paṭhamamaggavipākā": "World-Transcending Results: The Results of the First Path",
    "Suddhikapaṭipadā": "The Simple Modes of Practice",
    "Suddhikasuññataṃ": "Simple Emptiness",
    "Suññatapaṭipadā": "Emptiness with the Modes of Practice",
    "Suddhikaappaṇihitaṃ": "Simple Desirelessness",
    "Appaṇihitapaṭipadā": "Desirelessness with the Modes of Practice",
    "Vīsati mahānayā": "The Twenty Great Methods",
    "Chandādhipateyyasuddhikapaṭipadā": "Desire as the Dominant Factor: The Simple Modes of Practice",
    "Chandādhipateyyasuddhikasuññatā": "Desire as the Dominant Factor: Simple Emptiness",
    "Dutiyādimaggavipāko": "The Result of the Second and Later Paths",
    "Akusalavipākaabyākataṃ": "Indeterminate Results of the Unwholesome",
    "Akusalavipākapañcaviññāṇāni": "The Five Kinds of Consciousness Resulting from the Unwholesome",
    "Akusalavipākamanodhātu": "The Mind Element Resulting from the Unwholesome",
    "Akusalavipākamanoviññāṇadhātu": "The Mind-Consciousness Element Resulting from the Unwholesome",
    "Ahetukakiriyāabyākataṃ": "Functional Indeterminate Minds without Roots",
    "Kiriyāmanodhātu": "The Functional Mind Element",
    "Kiriyāmanoviññāṇadhātusomanassasahagatā": "The Functional Mind-Consciousness Element Accompanied by Joy",
    "Kiriyāmanoviññāṇadhātuupekkhāsahagatā": "The Functional Mind-Consciousness Element Accompanied by Equanimity",
    "Sahetukakāmāvacarakiriyā": "Functional Minds of the Sense Sphere with Roots",
    "Rūpāvacarakiriyā": "Functional Minds of the Fine-Material Sphere",
    "Arūpāvacarakiriyā": "Functional Minds of the Immaterial Sphere",
}
CLOSE = {
    "Suddhikapaṭipadā.": "The simple modes of practice.",
    "Suddhikasuññataṃ.": "Simple emptiness.",
    "Suññatapaṭipadā.": "Emptiness with the modes of practice.",
    "Suddhikaappaṇihitaṃ.": "Simple desirelessness.",
    "Appaṇihitapaṭipadā.": "Desirelessness with the modes of practice.",
    "Vīsati mahānayā.": "The twenty great methods.",
    "Chandādhipateyyasuddhikapaṭipadā.": "Desire as the dominant factor: the simple modes of practice.",
    "Chandādhipateyyasuddhikasuññatā.": "Desire as the dominant factor: simple emptiness.",
    "Paṭhamamaggavipāko.": "The result of the first path.",
    "Dutiyādimaggavipāko.": "The result of the second and later paths.",
    "Lokuttaravipāko.": "The world-transcending result.",
    "Akusalavipākapañcaviññāṇāni.": "The five kinds of consciousness resulting from the unwholesome.",
    "Akusalavipākā manodhātu.": "The mind element resulting from the unwholesome.",
    "Akusalavipākā manoviññāṇadhātu.": "The mind-consciousness element resulting from the unwholesome.",
    "Vipākā abyākatā.": "Indeterminate results.",
    "Kiriyā manodhātu.": "The functional mind element.",
    "Kiriyā manoviññāṇadhātu somanassasahagatā.": "The functional mind-consciousness element accompanied by joy.",
    "Kiriyā manoviññāṇadhātu upekkhāsahagatā.": "The functional mind-consciousness element accompanied by equanimity.",
    "Ahetukā kiriyā abyākatā.": "Functional indeterminate minds without roots.",
    "Sahetukā kāmāvacarakiriyā.": "Functional minds of the sense sphere with roots.",
    "Rūpāvacarakiriyā.": "Functional minds of the fine-material sphere.",
    "Arūpāvacarakiriyā.": "Functional minds of the immaterial sphere.",
    "Kiriyā abyākatā.": "Functional indeterminate minds.",
    "Cittuppādakaṇḍaṃ niṭṭhitaṃ.": "The chapter on the arising of mind is complete.",
}

# ---- factor names (approved sample + new ones) -----------------------------------------
N = dict(C.NAMES)
N.update({
    "dukkhaṃ": "pain",
    "dukkhindriyaṃ": "the faculty of pain",
    "upekkhā": "equanimity",
    "upekkhindriyaṃ": "the faculty of equanimity",
    "aññindriyaṃ": "the faculty of final knowledge",
    "aññātāvindriyaṃ": "the faculty of one who has final knowledge",
    "saṅkhārakkhandho": "the aggregate of mental formations",
})

# ---- fixed formula strings -------------------------------------------------------------
Q_ABY = "What states are indeterminate?"
YEVA_ABY = ("whatever other dependently arisen immaterial states there are at that time "
            + DASH + " these states are indeterminate.")
NIY = "that leads to liberation and leads away from accumulation"
STAGE = {
    1: "for the abandoning of wrong views, for reaching the first stage",
    2: "for the weakening of sensual lust and ill will, for reaching the second stage",
    3: "for the abandoning without remainder of sensual lust and ill will, for reaching the third stage",
    4: ("for the abandoning without remainder of lust for the fine-material, lust for the immaterial, "
        "conceit, restlessness and ignorance, for reaching the fourth stage"),
}
VIV = "quite secluded from sensual pleasures"
VUP = "with the stilling of applied thought and sustained thought"
LOK_KUS = "At a time when one develops world-transcending absorption " + NIY
VIPAKA_OPEN = ("because that same world-transcending wholesome absorption has been done and developed, "
               "as its result one, " + VIV)
AKUS_KAMMA = "At a time when, because unwholesome action has been done and accumulated,"
KIRIYA = "functional, neither wholesome nor unwholesome nor a result of action"
KIRIYA_JH = KIRIYA + ", for a pleasant abiding here and now"
OBJ = {
    "rūpārammaṇā vā": "with a visible form as its object",
    "phoṭṭhabbārammaṇā vā": "or a touch as its object",
    "dhammārammaṇā vā": "or a mental object as its object",
}
YAM_YAM = "or whatever it takes up as its object"
ORD = {"paṭhamaṃ": "first", "dutiyaṃ": "second", "tatiyaṃ": "third", "catutthaṃ": "fourth",
       "pañcamaṃ": "fifth"}
ATTR = {
    "dukkhapaṭipadaṃ dandhābhiññaṃ": "with difficult practice and slow direct knowledge",
    "dukkhapaṭipadaṃ khippābhiññaṃ": "with difficult practice and quick direct knowledge",
    "sukhapaṭipadaṃ dandhābhiññaṃ": "with easy practice and slow direct knowledge",
    "sukhapaṭipadaṃ khippābhiññaṃ": "with easy practice and quick direct knowledge",
    "suññataṃ": "empty",
    "animittaṃ": "signless",
    "appaṇihitaṃ": "desireless",
    "chandādhipateyyaṃ": "with desire as the dominant factor",
    "vīriyādhipateyyaṃ": "with energy as the dominant factor",
    "cittādhipateyyaṃ": "with mind as the dominant factor",
    "vīmaṃsādhipateyyaṃ": "with inquiry as the dominant factor",
    "pathavīkasiṇaṃ": "using the earth meditation device",
}
LABEL = {"kusalaṃ": " (wholesome)", "vipāko": " (result)"}
THERE_CONTACT = "at that time there is contact"
TWENTY = {  # lokuttaraṃ X bhāveti
    "maggaṃ": "the world-transcending path",
    "satipaṭṭhānaṃ": "a world-transcending foundation of mindfulness",
    "sammappadhānaṃ": "a world-transcending right striving",
    "iddhipādaṃ": "a world-transcending basis of spiritual power",
    "indriyaṃ": "a world-transcending faculty",
    "balaṃ": "a world-transcending power",
    "bojjhaṅgaṃ": "a world-transcending awakening factor",
    "saccaṃ": "a world-transcending truth",
    "samathaṃ": "a world-transcending calm",
    "dhammaṃ": "a world-transcending state",
    "khandhaṃ": "a world-transcending aggregate",
    "āyatanaṃ": "a world-transcending sense base",
    "dhātuṃ": "a world-transcending element",
    "āhāraṃ": "a world-transcending nutriment",
    "phassaṃ": "a world-transcending contact",
    "vedanaṃ": "a world-transcending feeling",
    "saññaṃ": "a world-transcending perception",
    "cetanaṃ": "a world-transcending intention",
    "cittaṃ": "a world-transcending mind",
}
ARUPA = {
    "sabbaso rūpasaññānaṃ samatikkamā paṭighasaññānaṃ atthaṅgamā nānattasaññānaṃ amanasikārā ākāsānañcāyatanasaññāsahagataṃ":
        "with the complete surmounting of perceptions of material form, with the disappearance of perceptions "
        "of impact, with non-attention to perceptions of diversity, accompanied by the perception of the base "
        "of infinite space",
    "sabbaso ākāsānañcāyatanaṃ samatikkamma viññāṇañcāyatanasaññāsahagataṃ":
        "completely surmounting the base of infinite space, accompanied by the perception of the base of "
        "infinite consciousness",
    "sabbaso viññāṇañcāyatanaṃ samatikkamma ākiñcaññāyatanasaññāsahagataṃ":
        "completely surmounting the base of infinite consciousness, accompanied by the perception of the base "
        "of nothingness",
    "sabbaso ākiñcaññāyatanaṃ samatikkamma nevasaññānāsaññāyatanasaññāsahagataṃ":
        "completely surmounting the base of nothingness, accompanied by the perception of the base of neither "
        "perception nor non-perception",
}
SUKHA_PAHANA = "with the abandoning of happiness"
CITTA_KIND = {  # sahetuka kiriyā
    "somanassasahagatā ñāṇasampayuttā": "accompanied by joy and associated with knowledge",
    "somanassasahagatā ñāṇasampayuttā sasaṅkhārena": "accompanied by joy, associated with knowledge and with prompting",
    "somanassasahagatā ñāṇavippayuttā": "accompanied by joy and dissociated from knowledge",
    "somanassasahagatā ñāṇavippayuttā sasaṅkhārena": "accompanied by joy, dissociated from knowledge and with prompting",
    "upekkhāsahagatā ñāṇasampayuttā": "accompanied by equanimity and associated with knowledge",
    "upekkhāsahagatā ñāṇasampayuttā sasaṅkhārena": "accompanied by equanimity, associated with knowledge and with prompting",
    "upekkhāsahagatā ñāṇavippayuttā": "accompanied by equanimity and dissociated from knowledge",
    "upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena": "accompanied by equanimity, dissociated from knowledge and with prompting",
}
# body-pain string (the painful counterpart of the sample's sāta/sukha string)
S_KAYA_DUKKHA = ("bodily discomfort, bodily pain, the uncomfortable, painful experience born of body-contact, "
                 "the uncomfortable, painful feeling born of body-contact")
P_KAYA_DUKKHA = ("kāyikaṃ asātaṃ kāyikaṃ dukkhaṃ kāyasamphassajaṃ asātaṃ dukkhaṃ vedayitaṃ "
                 "kāyasamphassajā asātā dukkhā vedanā")
TAJJA_KAYA = "born of the contact of the corresponding body-consciousness element"
# shortened strings (functional mind without the path factor at the end)
assert C.S_SAMADHI.endswith(", right concentration") and C.S_VIRIYA.endswith(", right effort")
S_SAMADHI_SHORT = C.S_SAMADHI[: -len(", right concentration")]
S_VIRIYA_SHORT = C.S_VIRIYA[: -len(", right effort")]
P_SAMADHI_SHORT = "cittassa ṭhiti saṇṭhiti avaṭṭhiti avisāhāro avikkhepo avisāhaṭamānasatā samatho samādhindriyaṃ samādhibalaṃ"
P_VIRIYA_SHORT = ("cetasiko vīriyārambho nikkamo parakkamo uyyāmo vāyāmo ussāho ussoḷhī thāmo dhiti "
                  "asithilaparakkamatā anikkhittachandatā anikkhittadhuratā dhurasampaggāho vīriyaṃ "
                  "vīriyindriyaṃ vīriyabalaṃ")
P_PANNA = [k for k in C.STRINGS if k.startswith("paññā ")][0]
PATH_TAIL = "the awakening factor of investigation of states, a factor of the path, included in the path"
P_PATH_TAIL = "dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ"
APART = ("apart from the aggregate of feeling, apart from the aggregate of perception, "
         "apart from the aggregate of consciousness")
KOT_AGGR = ("Now at that time there are four aggregates, there are two sense bases, there are two elements, "
            "there are three nutriments, there are {n} faculties, there is one contact")
KOT_TAIL = "there is one {e}, there is one mental-object base, there is one mental-object element; or "
ELEM = {"kāyaviññāṇadhātu": "body-consciousness element", "manodhātu": "mind element",
        "manoviññāṇadhātu": "mind-consciousness element"}


def strip_dot(s):
    assert s.endswith("."), s
    return s[:-1]


def A_plain(key, s):
    return C.Q(N[key]) + " " + C.A(s, N[key])


EXACT = {
    ".": ".",
    "avikkhepo hoti": "there is non-distraction",
    "aññindriyaṃ hoti": "there is the faculty of final knowledge",
    "aññātāvindriyaṃ hoti": "there is the faculty of one who has final knowledge",
    "ime dhammā abyākatā.": "these states are indeterminate.",
    "ime dhammā abyākatā": "these states are indeterminate",
    "ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā.":
        "or " + YEVA_ABY,
    "alobho abyākatamūlaṃ": "non-greed, the indeterminate root",
    "adoso abyākatamūlaṃ": "non-hate, the indeterminate root",
    "amoho abyākatamūlaṃ": "non-delusion, the indeterminate root",
    # world-transcending openers
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā vivicceva kāmehi":
        f"{Q_ABY} {LOK_KUS}, {STAGE[1]}, and, {VIV}",
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā vitakkavicārānaṃ vūpasamā":
        f"{Q_ABY} {LOK_KUS}, {STAGE[1]}, and, {VUP}",
    "ime dhammā kusalā. Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi":
        "these states are wholesome. " + VIPAKA_OPEN[0].upper() + VIPAKA_OPEN[1:],
    # ^1-528: the Pāli has no full stop after kusalā (translated as written)
    "ime dhammā kusalā tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ vivicceva kāmehi":
        "these states are wholesome; " + VIPAKA_OPEN,
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ maggaṃ bhāveti":
        f"{Q_ABY} At a time when one develops {TWENTY['maggaṃ']}",
    "lokuttaraṃ cittaṃ bhāveti niyyānikaṃ apacayagāmiṃ diṭṭhigatānaṃ pahānāya paṭhamāya bhūmiyā pattiyā vivicceva kāmehi":
        f"develops {TWENTY['cittaṃ']} {NIY}, {STAGE[1]}, and, {VIV}",
    "Katame dhammā abyākatā? Yasmiṃ samaye lokuttaraṃ jhānaṃ bhāveti niyyānikaṃ apacayagāmiṃ kāmarāgabyāpādānaṃ tanubhāvāya dutiyāya bhūmiyā pattiyā":
        f"{Q_ABY} {LOK_KUS}, {STAGE[2]}",
    # "kāmarā gabyāpādānaṃ": broken word in the source, read as kāmarāgabyāpādānaṃ
    "kāmarā gabyāpādānaṃ anavasesappahānāya tatiyāya bhūmiyā pattiyā": STAGE[3],
    "rūparāgaarūparāgamānauddhaccaavijjāya anavasesappahānāya catutthāya bhūmiyā pattiyā vivicceva kāmehi":
        f"{STAGE[4]}, and, {VIV}",
    # Q/A
    "Katamo tasmiṃ samaye phasso hoti? Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – ayaṃ tasmiṃ samaye phasso hoti":
        strip_dot(A_plain("phasso", C.S_PHASSA)),
    "Katamo tasmiṃ samaye phasso hoti? Yo tasmiṃ samaye phasso phusanā saṃphusanā saṃphusitattaṃ – ayaṃ tasmiṃ samaye phasso hoti.":
        A_plain("phasso", C.S_PHASSA),
    "Katamaṃ tasmiṃ samaye aññātāvindriyaṃ hoti? Yā tesaṃ aññātāvīnaṃ dhammānaṃ aññā " + P_PANNA + " "
    + P_PATH_TAIL + " – idaṃ tasmiṃ samaye aññātāvindriyaṃ hoti":
        C.Q(N["aññātāvindriyaṃ"]) + " Whatever, in those states of one who has final knowledge, is final knowledge, "
        + C.S_PANNA + ", " + PATH_TAIL + " " + DASH + " this is " + N["aññātāvindriyaṃ"] + " at that time",
    # unwholesome results: the five kinds of consciousness
    "Katame dhammā abyākatā? Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākaṃ cakkhuviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ rūpārammaṇaṃ":
        f"{Q_ABY} {AKUS_KAMMA} eye-consciousness has arisen as its result, accompanied by equanimity, "
        "with a visible form as its object",
    "sotaviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ saddārammaṇaṃ":
        "ear-consciousness has arisen, accompanied by equanimity, with a sound as its object",
    "ghānaviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ gandhārammaṇaṃ":
        "nose-consciousness has arisen, accompanied by equanimity, with a smell as its object",
    "jivhāviññāṇaṃ uppannaṃ hoti upekkhāsahagataṃ rasārammaṇaṃ":
        "tongue-consciousness has arisen, accompanied by equanimity, with a taste as its object",
    "Katamā tasmiṃ samaye vedanā hoti? Yaṃ tasmiṃ samaye tajjākāyaviññāṇadhātusamphassajaṃ " + P_KAYA_DUKKHA
    + " – ayaṃ tasmiṃ samaye vedanā hoti":
        strip_dot(C.Q(N["vedanā"]) + " " + C.A(S_KAYA_DUKKHA, N["vedanā"], ", " + TAJJA_KAYA + ",")),
    "Katamaṃ tasmiṃ samaye dukkhaṃ hoti? Yaṃ tasmiṃ samaye " + P_KAYA_DUKKHA + " – idaṃ tasmiṃ samaye dukkhaṃ hoti":
        strip_dot(A_plain("dukkhaṃ", S_KAYA_DUKKHA)),
    "Katamaṃ tasmiṃ samaye dukkhindriyaṃ hoti? Yaṃ tasmiṃ samaye " + P_KAYA_DUKKHA
    + " – idaṃ tasmiṃ samaye dukkhindriyaṃ hoti":
        strip_dot(A_plain("dukkhindriyaṃ", S_KAYA_DUKKHA)),
    "ekā kāyaviññāṇadhātu hoti, ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti; ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā":
        KOT_TAIL.format(e=ELEM["kāyaviññāṇadhātu"]) + strip_dot(YEVA_ABY),
    "ekā manodhātu hoti, ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti; ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā":
        KOT_TAIL.format(e=ELEM["manodhātu"]) + strip_dot(YEVA_ABY),
    "ekā manoviññāṇadhātu hoti, ekaṃ dhammāyatanaṃ hoti, ekā dhammadhātu hoti; ye vā pana tasmiṃ samaye aññepi atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā":
        KOT_TAIL.format(e=ELEM["manoviññāṇadhātu"]) + strip_dot(YEVA_ABY),
    "Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, tīṇindriyāni honti, eko phasso hoti":
        KOT_AGGR.format(n="three"),
    "Tasmiṃ kho pana samaye cattāro khandhā honti, dvāyatanāni honti, dve dhātuyo honti, tayo āhārā honti, pañcindriyāni honti, eko phasso hoti":
        KOT_AGGR.format(n="five"),
    # unwholesome results: mind element, mind-consciousness element
    "Katame dhammā abyākatā? Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākā manodhātu uppannā hoti upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} {AKUS_KAMMA} the mind element has arisen as its result, accompanied by equanimity, "
        + OBJ["rūpārammaṇā vā"],
    "Katame dhammā abyākatā? Yasmiṃ samaye akusalassa kammassa katattā upacitattā vipākā manoviññāṇadhātu uppannā hoti upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} {AKUS_KAMMA} the mind-consciousness element has arisen as its result, accompanied by equanimity, "
        + OBJ["rūpārammaṇā vā"],
    # functional
    "Katame dhammā abyākatā? Yasmiṃ samaye manodhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} At a time when the mind element has arisen, {KIRIYA}, accompanied by equanimity, "
        + OBJ["rūpārammaṇā vā"],
    "Katame dhammā abyākatā? Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā somanassasahagatā rūpārammaṇā vā":
        f"{Q_ABY} At a time when the mind-consciousness element has arisen, {KIRIYA}, accompanied by joy, "
        + OBJ["rūpārammaṇā vā"],
    "Katame dhammā abyākatā? Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā upekkhāsahagatā rūpārammaṇā vā":
        f"{Q_ABY} At a time when the mind-consciousness element has arisen, {KIRIYA}, accompanied by equanimity, "
        + OBJ["rūpārammaṇā vā"],
    "Katamā tasmiṃ samaye cittassekaggatā hoti? Yā tasmiṃ samaye " + P_SAMADHI_SHORT
    + " – ayaṃ tasmiṃ samaye cittassekaggatā hoti.":
        A_plain("cittassekaggatā", S_SAMADHI_SHORT),
    "Katamaṃ tasmiṃ samaye vīriyindriyaṃ hoti? Yo tasmiṃ samaye " + P_VIRIYA_SHORT
    + " – idaṃ tasmiṃ samaye vīriyindriyaṃ hoti.":
        A_plain("vīriyindriyaṃ", S_VIRIYA_SHORT),
    "Katamaṃ tasmiṃ samaye samādhindriyaṃ hoti? Yā tasmiṃ samaye " + P_SAMADHI_SHORT
    + " – idaṃ tasmiṃ samaye samādhindriyaṃ hoti":
        strip_dot(A_plain("samādhindriyaṃ", S_SAMADHI_SHORT)),
    "Katame dhammā abyākatā? Yasmiṃ samaye manoviññāṇadhātu uppannā hoti kiriyā neva kusalā nākusalā na ca kammavipākā somanassasahagatā ñāṇasampayuttā":
        f"{Q_ABY} At a time when the mind-consciousness element has arisen, {KIRIYA}, "
        + CITTA_KIND["somanassasahagatā ñāṇasampayuttā"],
    "upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena rūpārammaṇā vā":
        CITTA_KIND["upekkhāsahagatā ñāṇavippayuttā sasaṅkhārena"] + ", " + OBJ["rūpārammaṇā vā"],
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha, tasmiṃ samaye phasso hoti":
        f"{OBJ['dhammārammaṇā vā']}, {YAM_YAM}, {THERE_CONTACT}",
    # fine-material and immaterial functional absorption
    "Katame dhammā abyākatā? Yasmiṃ samaye rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ vivicceva kāmehi":
        f"{Q_ABY} At a time when one develops absorption of the fine-material sphere, {KIRIYA_JH}, and, {VIV}",
    "Katame dhammā abyākatā? Yasmiṃ samaye rūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca kammavipākaṃ diṭṭhadhammasukhavihāraṃ vitakkavicārānaṃ vūpasamā":
        f"{Q_ABY} At a time when one develops absorption of the fine-material sphere, {KIRIYA_JH}, and, {VUP}",
}
for k, v in CITTA_KIND.items():
    EXACT.setdefault(k, v)
for k, v in TWENTY.items():
    EXACT.setdefault(f"lokuttaraṃ {k} bhāveti", "develops " + v)
for k, v in ARUPA.items():
    EXACT["Katame dhammā abyākatā? Yasmiṃ samaye arūpāvacaraṃ jhānaṃ bhāveti kiriyaṃ neva kusalaṃ nākusalaṃ na ca "
          "kammavipākaṃ diṭṭhadhammasukhavihāraṃ " + k + " sukhassa ca pahānā"] = \
        f"{Q_ABY} At a time when one develops absorption of the immaterial sphere, {KIRIYA_JH}, and, {v}, {SUKHA_PAHANA}"

RE_PATH = re.compile(r"^(?:(?P<ord>paṭhamaṃ|dutiyaṃ|tatiyaṃ|catutthaṃ|pañcamaṃ) jhānaṃ"
                     r"(?P<enter> upasampajja viharati)?,?)?\s*(?P<attrs>.*?)"
                     r"(?P<tail>,? ?tasmiṃ samaye phasso hoti)?$")
RE_LIST = re.compile(r"^(?P<pre>.*?), tasmiṃ samaye (?P<list>(?:\S+ hoti,? ?)+); ye vā pana tasmiṃ samaye aññepi "
                     r"atthi paṭiccasamuppannā arūpino dhammā – ime dhammā abyākatā(?P<dot>\.?)$")
RE_SANKHARA = re.compile(r"^Katamo tasmiṃ samaye saṅkhārakkhandho hoti\? (?P<list>[^;]+); ye vā pana tasmiṃ samaye "
                         r"aññepi atthi paṭiccasamuppannā arūpino dhammā ṭhapetvā vedanākkhandhaṃ ṭhapetvā "
                         r"saññākkhandhaṃ ṭhapetvā viññāṇakkhandhaṃ – ayaṃ tasmiṃ samaye saṅkhārakkhandho hoti$")
PRE = {
    "kāyaviññāṇaṃ uppannaṃ hoti dukkhasahagataṃ phoṭṭhabbārammaṇaṃ":
        "body-consciousness has arisen, accompanied by pain, with a touch as its object",
    "phoṭṭhabbārammaṇā vā yaṃ yaṃ vā panārabbha": OBJ["phoṭṭhabbārammaṇā vā"] + ", " + YAM_YAM,
    "dhammārammaṇā vā yaṃ yaṃ vā panārabbha": OBJ["dhammārammaṇā vā"] + ", " + YAM_YAM,
}


def attrs_en(s):
    """Translate a run of path attributes, e.g. 'dukkhapaṭipadaṃ dandhābhiññaṃ suññataṃ'."""
    words, out, i = s.split(), [], 0
    while i < len(words):
        two = " ".join(words[i:i + 2])
        if two in ATTR:
            out.append(ATTR[two]); i += 2
        elif words[i] in ATTR:
            out.append(ATTR[words[i]]); i += 1
        else:
            raise KeyError(f"attr? {words[i]!r} in {s!r}")
    return ", ".join(out)


def tr_chunk(c):
    if c in EXACT:
        return EXACT[c]
    m = RE_LIST.match(c)
    if m:
        names = [w for w in re.split(r"\s*hoti,?\s*", m["list"]) if w]
        return (PRE[m["pre"]] + ", at that time " + ", ".join("there is " + N[w] for w in names)
                + "; or " + (YEVA_ABY if m["dot"] else strip_dot(YEVA_ABY)))
    m = RE_SANKHARA.match(c)
    if m:
        names = [N[w[0].lower() + w[1:]] for w in m["list"].split()]
        return (C.Q(N["saṅkhārakkhandho"]) + " " + ", ".join(names)[0].upper() + ", ".join(names)[1:]
                + "; or whatever other dependently arisen immaterial states there are at that time, " + APART
                + " " + DASH + " this is " + N["saṅkhārakkhandho"] + " at that time")
    m = RE_PATH.match(c)
    if m and (m["ord"] or m["attrs"] or m["tail"]):
        attrs, label = m["attrs"].strip(), ""
        for lab in LABEL:
            if attrs.endswith("nti " + lab):
                attrs = attrs[: -len("nti " + lab)] + "ṃ"
                label = LABEL[lab]
        parts = []
        if m["ord"]:
            ab = f"the {ORD[m['ord']]} absorption"
            parts.append(("enters and dwells in " + ab) if m["enter"] else ab)
        if attrs:
            parts.append(attrs_en(attrs))
        out = ", ".join(parts) + label
        if m["tail"]:
            out += ", " + THERE_CONTACT
        return out
    raise KeyError(f"no rule for chunk: {c!r}")


def tr_line(line):
    if line in CLOSE:
        return CLOSE[line]
    chunks = [c.strip() for c in line.split("…pe…")]
    en = [tr_chunk(c) for c in chunks]
    out = en[0]
    for e in en[1:]:
        out += PE + ("" if e == "." else " ") + e
    return out[0].upper() + out[1:]


def build():
    out_lines = []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            out_lines.append("")
            continue
        m = re.match(r"^(.*?)(\s*\^[0-9A-Za-z-]+)?$", line)
        body, bid = m.group(1), m.group(2) or ""
        if body.startswith("#"):
            hashes, title = body.split(" ", 1)
            out_lines.append(f"{hashes} {HEAD[title]}{bid}")
        else:
            out_lines.append(tr_line(body) + bid)
    return "\n".join(out_lines).rstrip("\n") + "\n"


if __name__ == "__main__":
    text = build()
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT)
