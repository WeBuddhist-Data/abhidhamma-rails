"""Build the English plain zero-shot of pi-1 part 4-02-nikkhepakandam.md (^1-3-2-6-0 ... ^1-1302).

usage: python -I -X utf8 build_4-02.py
Matrix item names come from build_matika.MATRIX_ITEMS (never retyped); every recurring
formula is a constant below, so every repeat is byte-identical. Runs self-checks and
writes the English split chapter.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_matika as M  # noqa: E402  (importing does not write anything)

ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "4-02-nikkhepakandam.md"
OUT = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters" / "4-02-nikkhepakandam.md"

DASH = "–"
D = DASH

# ---- matrix items -------------------------------------------------------------------------
VAR = re.compile(r"\s*\[[^\]]*\]")


def _norm(p):
    p = VAR.sub("", p).strip().rstrip(".")
    p = " ".join(w for w in p.split() if w != "dhammā")
    p = p.replace(" kho pana", "")
    return re.sub(r"pi$", "", p)


ITEM = {}
_first = {}
for bid, letter, pali, eng in sorted(M.MATRIX_ITEMS, key=lambda t: t[0].startswith("1-M2")):
    e = VAR.sub("", eng).rstrip(".")
    e = e[0].lower() + e[1:]
    key = _norm(pali)
    if letter == "a":
        _first[bid] = pali.split()[0]
    elif "kho pana" in [x for x in M.MATRIX_ITEMS if x[0] == bid and x[1] == "a"][0][2]:
        key = _first[bid] + " " + key
    ITEM[key] = e  # M2 entries come last and win


def I(p):
    assert p in ITEM, p
    return ITEM[p]


def Q(p):
    return f"What are {I(p)}?"


def E(p):
    return f"{D} these are {I(p)}."


def L(p):
    return f"These are {I(p)}."


# ---- fixed phrases ---------------------------------------------------------------------
GROUP_H = {bid.replace("1-M-2-", "1-3-2-"): v for bid, v in M.GROUPS.items()}
H_OGHA = GROUP_H["1-3-2-6-0"][0]
H_YOGA = GROUP_H["1-3-2-7-0"][0]
H_NIV = GROUP_H["1-3-2-8-0"][0]
H_PARA = GROUP_H["1-3-2-9-0"][0]
H_MAHA = GROUP_H["1-3-2-10-0"][0]
H_UPA = GROUP_H["1-3-2-11-0"][0]
H_KIL = GROUP_H["1-3-2-12-0"][0]
H_PITTHI = GROUP_H["1-3-2-13-0"][0]
END_BHANA2 = "The second recitation section of the chapter of summaries."
END_ABHI = "The Abhidhamma pairs."

VV = "the aggregate of feeling… the aggregate of consciousness"            # vedanākkhandho…pe… viññāṇakkhandho
RV = "the aggregate of material form… the aggregate of consciousness"      # rūpakkhandho…pe… viññāṇakkhandho
FEEL3 = "the aggregate of feeling, the aggregate of perception, the aggregate of mental formations"
FOUR = FEEL3 + ", the aggregate of consciousness"
PERC3 = "the aggregate of perception, the aggregate of mental formations, the aggregate of consciousness"
RA = "all material form and the unconditioned element"                   # sabbañca rūpaṃ, asaṅkhatā ca dhātu
LOKUT = "the paths not included in the spheres of existence, the fruits of the paths, and the unconditioned element"
KUA = "wholesome, unwholesome and indeterminate"   # kusalākusalābyākatā
KA = "wholesome and indeterminate"                 # kusalābyākatā
KU = "wholesome and unwholesome"                   # kusalākusalā
SPH_KRAP = ("those of the sense sphere, of the fine-material sphere, of the immaterial sphere, "
            "and those not included in the spheres of existence")
SPH_KRA = "those of the sense sphere, of the fine-material sphere and of the immaterial sphere"
LOC_KRP = "the sense sphere, the fine-material sphere and what is not included in the spheres of existence"
LOC_KRAP = ("the sense sphere, the fine-material sphere, the immaterial sphere and what is not included "
            "in the spheres of existence")
TADEKA = "the defilements that stand together with them"                  # tadekaṭṭhā ca kilesā
TAMSAMP = VV + " associated with them"                                     # taṃsampayutto vedanākkhandho…pe…
TAMSAM = "the bodily action, verbal action and mental action arising from them"  # taṃsamuṭṭhānaṃ kāyakammaṃ…
ROOT_TAIL = f"{TADEKA}, {TAMSAMP}, and {TAMSAM}"
ROOTS3 = "the three unwholesome roots"
GHD = "greed, hate, delusion"
FETTERS3 = "the three fetters"
REMAINING_GHD = "the remaining greed, hate and delusion"


def cap(s):
    return s[0].upper() + s[1:] if s[0].isalpha() else s[0] + cap(s[1:]) if s[0] in "\"'" else s


# ---- answer frames ---------------------------------------------------------------------
def F_NO(p):
    """Te dhamme ṭhapetvā avasesā kusalākusalābyākatā … apariyāpannā; vedanā…viññāṇa; sabbañca rūpaṃ, asaṅkhatā ca dhātu"""
    return (f"{Q(p)} Leaving those states aside, the remaining {KUA} states: {SPH_KRAP}; {VV}; {RA} {E(p)}")


def F_SAS(p, kus=KUA):
    """Sāsavā kusalākusalābyākatā dhammā kāmāvacarā, rūpāvacarā, arūpāvacarā; rūpa…viññāṇa"""
    return f"{Q(p)} The {kus} states subject to taints: {SPH_KRA}; {RV} {E(p)}"


def F_LOKUT(p):
    """Apariyāpannā maggā ca, maggaphalāni ca, asaṅkhatā ca dhātu"""
    return f"{Q(p)} {cap(LOKUT)} {E(p)}"


def F_SAMP(p):
    """Tehi dhammehi ye dhammā sampayuttā vedanā…viññāṇa"""
    return f"{Q(p)} The states associated with those states: {VV} {E(p)}"


def F_VIPP(p):
    """Tehi dhammehi ye dhammā vippayuttā vedanā…viññāṇa; sabbañca rūpaṃ, asaṅkhatā ca dhātu"""
    return f"{Q(p)} The states dissociated from those states: {VV}; {RA} {E(p)}"


def F_NIYA_NOT(p, rel):
    """Tehi dhammehi ye dhammā X-niyā, te dhamme ṭhapetvā avasesā sāsavā kusalākusalābyākatā …; rūpa…viññāṇa"""
    return (f"{Q(p)} Among the states {rel} those states, leaving those states aside, the remaining {KUA} "
            f"states subject to taints: {SPH_KRA}; {RV} {E(p)}")


def F_SAMP_NOT(p):
    """Tehi dhammehi ye dhammā sampayuttā, te dhamme ṭhapetvā vedanā…viññāṇa"""
    return f"{Q(p)} Among the states associated with those states, leaving those states aside, {VV} {E(p)}"


def F_VIPP_NIYA(p, kus):
    """Tehi dhammehi ye dhammā vippayuttā sāsavā kusal(ākusal)ābyākatā …; rūpa…viññāṇa"""
    return (f"{Q(p)} Among the states dissociated from those states, the {kus} states subject to taints: "
            f"{SPH_KRA}; {RV} {E(p)}")


def F_LIST(p, body):
    return f"{Q(p)} {cap(body)} {E(p)}"


def TQ(x):
    """Tattha katamo/katamā/katamaṃ X?"""
    return f"Of these, what is {x}?"


def CALLED(x):
    return f"{D} this is called {x}."


def EVA(first, rest):
    """yo/yā/yaṃ evarūpo … : 'whatever <first> of this kind there is, <rest>'"""
    return f"whatever {first} of this kind there is, {rest}"


# ---- definition strings ----------------------------------------------------------------
# Yo kāmesu kāmacchando kāmarāgo kāmanandī kāmataṇhā kāmasineho kāmapariḷāho kāmamucchā kāmajjhosānaṃ
S_KAMA = ("Whatever, with regard to sensual pleasures, is sensual desire, sensual lust, sensual delight, "
          "sensual craving, sensual affection, sensual fever, sensual infatuation, sensual attachment")

# Anatthaṃ me acarīti āghāto jāyati … aṭṭhāne vā pana āghāto jāyati.
AGHATA = ('Resentment arises at the thought "He has done me harm"; resentment arises at the thought '
          '"He is doing me harm"; resentment arises at the thought "He will do me harm"; resentment arises '
          'at the thought "He has done harm to someone dear and pleasing to me… he is doing harm… he will do '
          'harm"; resentment arises at the thought "He has done good to someone not dear and not pleasing to '
          'me… he is doing good… he will do good"; or resentment arises without reason.')
# Yo evarūpo cittassa āghāto paṭighāto paṭighaṃ … anattamanatā cittassa
S_DOSA = cap(EVA("resentment of mind",
                 "repugnance, aversion, hostility, anger, rising anger, intense anger, hate, rising hate, "
                 "intense hate, malice of mind, mental hatred, wrath, being wrathful, the state of being "
                 "wrathful, hate, hating, the state of hating, malice, being malicious, the state of being "
                 "malicious, opposition, hostility, fierceness, rudeness, discontent of mind"))
DOSA = AGHATA + " " + S_DOSA

# Yā cittassa akallatā akammaññatā olīyanā sallīyanā līnaṃ līyanā līyitattaṃ thinaṃ thiyanā thiyitattaṃ cittassa
S_THINA = ("Whatever is indisposition of mind, unworkability, drooping, sagging, sluggishness, being sluggish, "
           "the state of being sluggish, sloth, being slothful, the slothful state of mind")
# Yā kāyassa akallatā akammaññatā onāho pariyonāho antosamorodho middhaṃ soppaṃ pacalāyikā soppaṃ supanā supitattaṃ
S_MIDDHA = ("Whatever is indisposition of the mental body, unworkability, enveloping, full enveloping, "
            "inner confinement, torpor, sleep, drowsiness, sleep, sleeping, the state of being asleep")
# Yaṃ cittassa uddhaccaṃ avūpasamo cetaso vikkhepo bhantattaṃ cittassa
S_UDDHACCA = "Whatever is restlessness of mind, unsettledness, distraction of mind, the mind's whirling"
# Akappiye kappiyasaññitā … Yaṃ evarūpaṃ kukkuccaṃ kukkuccāyanā kukkuccāyitattaṃ cetaso vippaṭisāro manovilekho
KUKKUCCA = ("Perceiving what is not allowable as allowable, perceiving what is allowable as not allowable, "
            "perceiving what is blameless as blameworthy, perceiving what is blameworthy as blameless. "
            + cap(EVA("remorse", "being remorseful, the state of being remorseful, regret of mind, mental scratching")))

# Satthari kaṅkhati vicikicchati, …
VICI_HEAD = "One is uncertain and in doubt about the Teacher"
VICI_INTRO = (VICI_HEAD + ", uncertain and in doubt about the Teaching, uncertain and in doubt about the "
              "Community, uncertain and in doubt about the training, uncertain and in doubt about the past, "
              "uncertain and in doubt about the future, uncertain and in doubt about both the past and the "
              "future, uncertain and in doubt about specific conditionality and dependently arisen states")
# yā evarūpā kaṅkhā kaṅkhāyanā kaṅkhāyitattaṃ vimati vicikicchā … thambhitattaṃ cittassa manovilekho
VICI_TAIL = "stiffness of mind, mental scratching"
VICI_STR = EVA("uncertainty", "being uncertain, the state of being uncertain, perplexity, doubt, being in two "
               "minds, a forked path, hesitation, not settling on one side, faltering, wavering, not plunging in, "
               + VICI_TAIL)

# Dukkhe aññāṇaṃ, … idappaccayatā paṭiccasamuppannesu dhammesu aññāṇaṃ
MOHA_INTRO = ("Lack of knowledge about suffering, lack of knowledge about the arising of suffering, lack of "
              "knowledge about the cessation of suffering, lack of knowledge about the way leading to the "
              "cessation of suffering, lack of knowledge about the past, lack of knowledge about the future, "
              "lack of knowledge about both the past and the future, lack of knowledge about specific "
              "conditionality and dependently arisen states")
# yaṃ evarūpaṃ aññāṇaṃ adassanaṃ … avijjālaṅgī moho akusalamūlaṃ
MOHA_STR = EVA("lack of knowledge",
               "lack of vision, non-realisation, not understanding, not awakening, non-penetration, not "
               "grasping, not plunging in, not examining, not reviewing, not making it directly evident, "
               "stupidity, foolishness, lack of clear awareness, delusion, deep delusion, utter delusion, "
               "ignorance, the flood of ignorance, the yoke of ignorance, the underlying tendency to ignorance, "
               "the obsession of ignorance, the bar of ignorance, delusion, the unwholesome root")

# Sassato lokoti vā, … neva hoti na na hoti tathāgato paraṃ maraṇāti vā
VIEWS10 = ('"The world is eternal", or "The world is not eternal", or "The world has an end", or "The world '
           'has no end", or "The soul is the same as the body", or "The soul is one thing and the body '
           'another", or "The Tathāgata exists after death", or "The Tathāgata does not exist after death", '
           'or "The Tathāgata both exists and does not exist after death", or "The Tathāgata neither exists '
           'nor does not exist after death"')
# yā evarūpā diṭṭhi diṭṭhigataṃ … vipariyāsaggāho
DITTHI_HEAD = "being caught in views"
DITTHI_TAIL = "inverted grasping"
DITTHI_STR = EVA("view", DITTHI_HEAD + ", the thicket of views, the wilderness of views, the contortion of "
                 "views, the writhing of views, the fetter of views, grasping, taking a stand, adherence, "
                 "misapprehension, a wrong road, a wrong path, wrongness, a sectarian doctrine, " + DITTHI_TAIL)
DITTHI_SHORT = EVA("view", DITTHI_HEAD + "… " + DITTHI_TAIL)  # diṭṭhigataṃ…pe… vipariyāsaggāho

# Natthi dinnaṃ, … pavedentīti
NATTHI = ('"There is nothing given, there is nothing offered, there is nothing sacrificed, there is no fruit '
          'or result of good and bad actions, this world does not exist, the other world does not exist, there '
          'is no mother, there is no father, there are no spontaneously born beings, there are no ascetics and '
          'brahmins in the world who have gone rightly [variant: samaggatā (Ka.)] and practise rightly, who '
          'have realised this world and the other world by their own direct knowledge and make it known"')
# Ito bahiddhā samaṇabrāhmaṇānaṃ sīlena suddhi, vatena suddhi, sīlabbatena suddhīti
SILABBATA = ('Ascetics and brahmins outside this Teaching hold that "Purification comes through rules, '
             'purification comes through observances, purification comes through rules and observances"')
# Idha assutavā puthujjano … rūpasmiṃ vā attānaṃ. Vedanaṃ…pe… saññaṃ…pe… saṅkhāre…pe… viññāṇaṃ …
SAKKAYA = ("Here an uninstructed ordinary person, who does not see the noble ones, is unskilled in the teaching "
           "of the noble ones and undisciplined in the teaching of the noble ones, who does not see good people, "
           "is unskilled in the teaching of good people and undisciplined in the teaching of good people, "
           "regards material form as self, or self as possessing material form, or material form as in self, "
           "or self as in material form. He regards feeling… perception… mental formations… consciousness as "
           "self, or self as possessing consciousness, or consciousness as in self, or self as in consciousness.")

# Yo rāgo sārāgo … abhijjhā lobho akusalamūlaṃ
S_LOBHA = ("Whatever is lust, passion, favouring, compliance, delight, delight and lust, passion of mind, "
           "wishing, infatuation, attachment, hunger, deep hunger, sticking, a swamp, stirring, deception, the "
           "begetter, the producer, the seamstress, the ensnarer, the stream, the entangler, a thread, the "
           "spreading one, the striver, the companion, aspiration, the guide to existence, a forest, "
           "undergrowth, intimacy, affection, concern, kinship, longing, yearning, the state of yearning, "
           "longing for visible forms, longing for sounds, longing for smells, longing for tastes, longing for "
           "touches, longing for gain, longing for wealth, longing for children, longing for life, hankering, "
           "strong hankering, intense hankering, hankering, hankering after things, the state of hankering, "
           "voracity, being voracious, the state of being voracious, fawning, wanting the best, unrighteous "
           "lust, unjust greed, liking, wanting, desiring, envying, strong desiring, sensual craving, craving "
           "for continued existence, craving for non-existence, craving for fine-material existence, craving "
           "for immaterial existence, craving for cessation, craving for visible forms, craving for sounds, "
           "craving for smells, craving for tastes, craving for touches, craving for mental objects, a flood, "
           "a yoke, a tie, clinging, an obstruction, a hindrance, a covering, a bond, an impurity, an "
           "underlying tendency, an obsession, a creeper, avarice, the root of suffering, the source of "
           "suffering, the origin of suffering, Māra's snare, Māra's hook, Māra's domain, the river of craving, "
           "the net of craving, the leash of craving, the ocean of craving, covetousness, greed, the "
           "unwholesome root")
# Seyyohamasmīti māno, … ketukamyatā cittassa
MANA = ('The conceit "I am better", the conceit "I am equal", the conceit "I am worse"; '
        + EVA("conceit", "conceiving, the state of conceiving, haughtiness, loftiness, a flag, self-exaltation, "
              "the mind's desire to be a banner"))
# Yaṃ na hirīyati hiriyitabbena, na hirīyati pāpakānaṃ akusalānaṃ dhammānaṃ samāpattiyā
AHIRIKA = ("Not being ashamed of what one should be ashamed of, not being ashamed of engaging in bad, "
           "unwholesome states")
ANOTTAPPA = "Not fearing what one should fear, not fearing engaging in bad, unwholesome states"

# ---- names --------------------------------------------------------------------------------
N_NIV = {  # nīvaraṇa names, nominative and instrumental keys
    "kāmacchandanīvaraṇa": "the hindrance of sensual desire",
    "byāpādanīvaraṇa": "the hindrance of ill will",
    "thinamiddhanīvaraṇa": "the hindrance of sloth and torpor",
    "uddhaccakukkuccanīvaraṇa": "the hindrance of restlessness and remorse",
    "vicikicchānīvaraṇa": "the hindrance of doubt",
    "avijjānīvaraṇa": "the hindrance of ignorance",
    "uddhaccanīvaraṇa": "the hindrance of restlessness",
    "kukkuccanīvaraṇa": "the hindrance of remorse",
}
N_UPA = {
    "kāmupādāna": "clinging to sensual pleasures",
    "diṭṭhupādāna": "clinging to views",
    "sīlabbatupādāna": "clinging to rules and observances",
    "attavādupādāna": "clinging to a doctrine of self",
}
N_KIL = {  # nominative / instrumental stems
    "lobh": "greed", "dos": "hate", "moh": "delusion", "mān": "conceit", "diṭṭhi": "view",
    "vicikicchā": "doubt", "thin": "sloth", "uddhacc": "restlessness", "ahirik": "shamelessness",
    "anottapp": "fearlessness of wrongdoing",
}
SAKKAYADITTHI = "identity view"
SILABBATAPARAMASA = "misapprehension of rules and observances"
DITTHIPARAMASA = "misapprehension through views"
THINA, MIDDHA, UDDHACCA, KUKKUCCA_N, VICIKICCHA = "sloth", "torpor", "restlessness", "remorse", "doubt"


def kil_name(w):
    w = w.strip()
    for stem in sorted(N_KIL, key=len, reverse=True):
        if w.startswith(stem):
            return N_KIL[stem]
    raise KeyError(w)


def pairs_sentence(body, names, kind):
    """'A B-ena X ceva Y-sampayutto ca, …' -> 'A with B is both <kind> and associated with <kind>; …'"""
    out = []
    for part in body.split(", "):
        w = part.split()
        a, b = names(w[0][0].lower() + w[0][1:]), names(w[1])
        out.append(f"{a} with {b} is both {kind} and associated with {kind}")
    return cap("; ".join(out))


def niv_name(w):
    w = re.sub(r"ena$", "a", re.sub(r"ṃ$", "", w))
    return N_NIV[w]


def upa_name(w):
    w = re.sub(r"ena$", "a", re.sub(r"ṃ$", "", w))
    return N_UPA[w]


# ---- segments -----------------------------------------------------------------------------
P = {}  # filled from the Pāli for the long pair lists


def build_segments(pali):
    seg = {}
    seg["1-3-2-6-0"] = [H_OGHA]
    seg["1-1156"] = [f"{Q('oghā')} The four floods… {E('oghavippayuttā oghaniyā')[2:]}"]
    seg["1-3-2-7-0"] = [H_YOGA]
    seg["1-1157"] = [f"{Q('yogā')} The four yokes… {E('yogavippayuttā yoganiyā')[2:]}"]

    # hindrances
    seg["1-3-2-8-0"] = [H_NIV]
    seg["1-1158"] = [f"{Q('nīvaraṇā')} The six hindrances [variant: nīvaraṇāni (Syā.)] {D} "
                     + ", ".join(N_NIV[k] for k in list(N_NIV)[:6]) + "."]
    n = N_NIV
    seg["1-1159"] = [f"{TQ(n['kāmacchandanīvaraṇa'])} {S_KAMA} {CALLED(n['kāmacchandanīvaraṇa'])}"]
    seg["1-1160"] = [f"{TQ(n['byāpādanīvaraṇa'])} {DOSA} {CALLED(n['byāpādanīvaraṇa'])}"]
    seg["1-1161"] = [f"{TQ(n['thinamiddhanīvaraṇa'])} There is {THINA}, and there is {MIDDHA}."]
    seg["1-1162"] = [f"{TQ(THINA)} {S_THINA} {CALLED(THINA)}"]
    seg["1-1163"] = [f"{TQ(MIDDHA)} {S_MIDDHA} {CALLED(MIDDHA)} So this {THINA} and this {MIDDHA} "
                     f"{CALLED(n['thinamiddhanīvaraṇa'])}"]
    seg["1-1164"] = [f"{TQ(n['uddhaccakukkuccanīvaraṇa'])} There is {UDDHACCA}, and there is {KUKKUCCA_N}."]
    seg["1-1165"] = [f"{TQ(UDDHACCA)} {S_UDDHACCA} {CALLED(UDDHACCA)}"]
    seg["1-1166"] = [f"{TQ(KUKKUCCA_N)} {KUKKUCCA} {CALLED(KUKKUCCA_N)} So this {UDDHACCA} and this "
                     f"{KUKKUCCA_N} {CALLED(n['uddhaccakukkuccanīvaraṇa'])}"]
    seg["1-1167"] = [f"{TQ(n['vicikicchānīvaraṇa'])} {VICI_INTRO}. {cap(VICI_STR)} "
                     f"{CALLED(n['vicikicchānīvaraṇa'])}"]
    seg["1-1168"] = [f"{TQ(n['avijjānīvaraṇa'])} {MOHA_INTRO}; {MOHA_STR} {CALLED(n['avijjānīvaraṇa'])}",
                     L("nīvaraṇā")]
    seg["1-1169"] = [F_NO("no nīvaraṇā")]
    seg["1-1170"] = [F_SAS("nīvaraṇiyā")]
    seg["1-1171"] = [F_LOKUT("anīvaraṇiyā")]
    seg["1-1172"] = [F_SAMP("nīvaraṇasampayuttā")]
    seg["1-1173"] = [F_VIPP("nīvaraṇavippayuttā")]
    seg["1-1174"] = [f"{Q('nīvaraṇā ceva nīvaraṇiyā ca')} Those same hindrances are both hindrances and "
                     f"subject to hindrances."]
    seg["1-1175"] = [F_NIYA_NOT("nīvaraṇiyā ceva no ca nīvaraṇā", "subject to")]
    seg["1-1176"] = [f"{Q('nīvaraṇā ceva nīvaraṇasampayuttā ca')} "
                     f"{pairs_sentence(P['1-1176'], niv_name, 'a hindrance')} "
                     f"{E('nīvaraṇā ceva nīvaraṇasampayuttā ca')}"]
    seg["1-1177"] = [F_SAMP_NOT("nīvaraṇasampayuttā ceva no ca nīvaraṇā")]
    seg["1-1178"] = [F_VIPP_NIYA("nīvaraṇavippayuttā nīvaraṇiyā", KA)]
    seg["1-1179"] = [F_LOKUT("nīvaraṇavippayuttā anīvaraṇiyā")]

    # misapprehension
    seg["1-3-2-9-0"] = [H_PARA]
    seg["1-1180"] = [f"{Q('parāmāsā')} {cap(DITTHIPARAMASA)}."]
    seg["1-1181"] = [f"{TQ(DITTHIPARAMASA)} {VIEWS10}; {DITTHI_STR} {CALLED(DITTHIPARAMASA)} "
                     f"All wrong view is {DITTHIPARAMASA}.",
                     L("parāmāsā")]
    seg["1-1182"] = [F_NO("no parāmāsā")]
    seg["1-1183"] = [F_SAS("parāmaṭṭhā")]
    seg["1-1184"] = [F_LOKUT("aparāmaṭṭhā")]
    seg["1-1185"] = [F_SAMP("parāmāsasampayuttā")]
    seg["1-1186"] = [F_VIPP("parāmāsavippayuttā")]
    seg["1-1187"] = [f"{Q('parāmāsā ceva parāmaṭṭhā ca')} That same misapprehension is both a "
                     f"misapprehension and misapprehended."]
    seg["1-1188"] = [F_NIYA_NOT("parāmaṭṭhā ceva no ca parāmāsā", "misapprehended by")]
    seg["1-1189"] = [F_VIPP_NIYA("parāmāsavippayuttā parāmaṭṭhā", KUA)]
    seg["1-1190"] = [F_LOKUT("parāmāsavippayuttā aparāmaṭṭhā")]

    # long intermediate pairs
    seg["1-3-2-10-0"] = [H_MAHA]
    seg["1-1191"] = [F_LIST("sārammaṇā", FOUR)]
    seg["1-1192"] = [F_LIST("anārammaṇā", RA)]
    seg["1-1193"] = [F_LIST("cittā", "eye-consciousness, ear-consciousness, nose-consciousness, "
                                     "tongue-consciousness, body-consciousness, the mind element, "
                                     "the mind-consciousness element")]
    seg["1-1194"] = [F_LIST("no cittā", f"{FEEL3}, {RA}")]
    seg["1-1195"] = [F_LIST("cetasikā", FEEL3)]
    seg["1-1196"] = [F_LIST("acetasikā", f"mind, {RA}")]
    seg["1-1197"] = [F_LIST("cittasampayuttā", FEEL3)]
    seg["1-1198"] = [F_LIST("cittavippayuttā", RA) + f' Mind should not be described {D} either as "associated '
                     f'with mind" or as "dissociated from mind".']
    seg["1-1199"] = [F_LIST("cittasaṃsaṭṭhā", FEEL3)]
    seg["1-1200"] = [F_LIST("cittavisaṃsaṭṭhā", RA) + f' Mind should not be described {D} either as "joined '
                     f'with mind" or as "not joined with mind".']
    seg["1-1201"] = [F_LIST("cittasamuṭṭhānā",
                            f"{FEEL3}; bodily intimation, verbal intimation; or whatever other material form "
                            f"there is that is born of mind, caused by mind, arising from mind: the visible-form "
                            f"base, the sound base, the smell base, the taste base, the touch base, the space "
                            f"element, the water element, lightness of material form, pliancy of material form, "
                            f"workability of material form, growth of material form, continuity of material "
                            f"form, edible food")]
    REM = "mind, the remaining material form and the unconditioned element"
    seg["1-1202"] = [F_LIST("no cittasamuṭṭhānā", REM)]
    EXPR = f"{FEEL3}, bodily intimation, verbal intimation"
    seg["1-1203"] = [F_LIST("cittasahabhuno", EXPR)]
    seg["1-1204"] = [F_LIST("no cittasahabhuno", REM)]
    seg["1-1205"] = [F_LIST("cittānuparivattino", EXPR)]
    seg["1-1206"] = [F_LIST("no cittānuparivattino", REM)]
    for bid, key in (("1-1207", "cittasaṃsaṭṭhasamuṭṭhānā"), ("1-1209", "cittasaṃsaṭṭhasamuṭṭhānasahabhuno"),
                     ("1-1211", "cittasaṃsaṭṭhasamuṭṭhānānuparivattino")):
        seg[bid] = [F_LIST(key, FEEL3)]
        nb = "1-" + str(int(bid[2:]) + 1)
        seg[nb] = [F_LIST("no " + key, f"mind, {RA}")]
    seg["1-1213"] = [F_LIST("ajjhattikā", "the eye base… the mind base")]
    seg["1-1214"] = [F_LIST("bāhirā", "the visible-form base… the mental-object base")]
    seg["1-1215"] = [F_LIST("upādā", "the eye base… edible food")]
    seg["1-1216"] = [F_LIST("no upādā", "the aggregate of feeling, the aggregate of perception, the aggregate "
                                        "of mental formations, the aggregate of consciousness, the four great "
                                        "elements and the unconditioned element")]
    seg["1-1217"] = [F_LIST("upādiṇṇā", f"the results, subject to taints, of {KU} states: {SPH_KRA}; {VV}; "
                                        f"and whatever material form is due to past action")]
    seg["1-1218"] = [F_LIST("anupādiṇṇā", f"the {KU} states subject to taints: {SPH_KRA}; {VV}; the states "
                                          f"that are functional, neither wholesome nor unwholesome nor results "
                                          f"of action; whatever material form is not due to past action; "
                                          f"{LOKUT}")]

    # clinging
    u = N_UPA
    seg["1-3-2-11-0"] = [H_UPA]
    seg["1-1219"] = [f"{Q('upādānā')} The four kinds of clinging {D} " + ", ".join(u.values())
                     + " [variant: kāmūpādānaṃ diṭṭhūpādānaṃ sīlabbatūpādānaṃ attavādūpādānaṃ (Sī.)]."]
    seg["1-1220"] = [f"{TQ(u['kāmupādāna'])} {S_KAMA} {CALLED(u['kāmupādāna'])}"]
    seg["1-1221"] = [f"{TQ(u['diṭṭhupādāna'])} {NATTHI} {D} {DITTHI_STR} {CALLED(u['diṭṭhupādāna'])} "
                     f"Leaving aside {u['sīlabbatupādāna']} and {u['attavādupādāna']}, all wrong view is "
                     f"{u['diṭṭhupādāna']}."]
    seg["1-1222"] = [f"{TQ(u['sīlabbatupādāna'])} {SILABBATA} {D} {DITTHI_STR} {CALLED(u['sīlabbatupādāna'])}"]
    seg["1-1223"] = [f"{TQ(u['attavādupādāna'])} {SAKKAYA} {cap(DITTHI_STR)} {CALLED(u['attavādupādāna'])}",
                     L("upādānā")]
    seg["1-1224"] = [F_NO("no upādānā")]
    seg["1-1225"] = [F_SAS("upādāniyā")]
    seg["1-1226"] = [F_LOKUT("anupādāniyā")]
    seg["1-1227"] = [F_SAMP("upādānasampayuttā")]
    seg["1-1228"] = [F_VIPP("upādānavippayuttā")]
    seg["1-1229"] = [f"{Q('upādānā ceva upādāniyā ca')} Those same kinds of clinging are both kinds of "
                     f"clinging and subject to clinging."]
    seg["1-1230"] = [F_NIYA_NOT("upādāniyā ceva no ca upādānā", "subject to")]
    seg["1-1231"] = [f"{Q('upādānā ceva upādānasampayuttā ca')} "
                     f"{pairs_sentence(P['1-1231'], upa_name, 'a kind of clinging').replace('associated with a kind of clinging', 'associated with clinging')} "
                     f"{E('upādānā ceva upādānasampayuttā ca')}"]
    seg["1-1232"] = [F_SAMP_NOT("upādānasampayuttā ceva no ca upādānā")]
    seg["1-1233"] = [F_VIPP_NIYA("upādānavippayuttā upādāniyā", KUA)]
    seg["1-1234"] = [F_LOKUT("upādānavippayuttā anupādāniyā"), END_BHANA2]

    # defilements
    seg["1-3-2-12-0"] = [H_KIL]
    seg["1-1235"] = [f"{Q('kilesā')} The ten bases of defilement {D} "
                     + ", ".join(N_KIL.values()) + "."]
    k = N_KIL
    seg["1-1236"] = [f"{TQ(k['lobh'])} {S_LOBHA} {CALLED(k['lobh'])}"]
    seg["1-1237"] = [f"{TQ(k['dos'])} {DOSA} {CALLED(k['dos'])}"]
    seg["1-1238"] = [f"{TQ(k['moh'])} {MOHA_INTRO}. {cap(MOHA_STR)} {CALLED(k['moh'])}"]
    seg["1-1239"] = [f"{TQ(k['mān'])} {MANA} {CALLED(k['mān'])}"]
    seg["1-1240"] = [f"{TQ(k['diṭṭhi'])} {VIEWS10}; {DITTHI_STR} {CALLED(k['diṭṭhi'])} "
                     f"All wrong view is {k['diṭṭhi']}."]
    seg["1-1241"] = [f"{TQ(k['vicikicchā'])} {VICI_INTRO}; {VICI_STR} {CALLED(k['vicikicchā'])}"]
    seg["1-1242"] = [f"{TQ(k['thin'])} {S_THINA} {CALLED(k['thin'])}"]
    seg["1-1243"] = [f"{TQ(k['uddhacc'])} {S_UDDHACCA} {CALLED(k['uddhacc'])}"]
    seg["1-1244"] = [f"{TQ(k['ahirik'])} {AHIRIKA} {CALLED(k['ahirik'])}"]
    seg["1-1245"] = [f"{TQ(k['anottapp'])} {ANOTTAPPA} {CALLED(k['anottapp'])}", L("kilesā")]
    seg["1-1246"] = [F_NO("no kilesā")]
    seg["1-1247"] = [F_SAS("saṃkilesikā")]
    seg["1-1248"] = [F_LOKUT("asaṃkilesikā")]
    seg["1-1249"] = [F_LIST("saṃkiliṭṭhā", f"{ROOTS3} {D} {GHD}; {ROOT_TAIL}")]
    seg["1-1250"] = [F_LIST("asaṃkiliṭṭhā", f"the {KA} states: {SPH_KRAP}; {VV}; {RA}")]
    seg["1-1251"] = [F_SAMP("kilesasampayuttā")]
    seg["1-1252"] = [F_VIPP("kilesavippayuttā")]
    seg["1-1253"] = [f"{Q('kilesā ceva saṃkilesikā ca')} Those same defilements are both defilements and "
                     f"subject to defilement."]
    seg["1-1254"] = [F_NIYA_NOT("saṃkilesikā ceva no ca kilesā", "subject to")]
    seg["1-1255"] = [f"{Q('kilesā ceva saṃkiliṭṭhā ca')} Those same defilements are both defilements and "
                     f"defiled."]
    seg["1-1256"] = [f"{Q('saṃkiliṭṭhā ceva no ca kilesā')} Among the states defiled by those states, leaving "
                     f"those states aside, {VV} {E('saṃkiliṭṭhā ceva no ca kilesā')}"]
    seg["1-1257"] = [f"{Q('kilesā ceva kilesasampayuttā ca')} "
                     f"{pairs_sentence(P['1-1257'], kil_name, 'a defilement')} "
                     f"{E('kilesā ceva kilesasampayuttā ca')}"]
    seg["1-1258"] = [F_SAMP_NOT("kilesasampayuttā ceva no ca kilesā")]
    seg["1-1259"] = [F_VIPP_NIYA("kilesavippayuttā saṃkilesikā", KA)]
    seg["1-1260"] = [F_LOKUT("kilesavippayuttā asaṃkilesikā")]

    # closing pairs
    seg["1-3-2-13-0"] = [H_PITTHI]
    THREE_F = f"{FETTERS3} {D} {SAKKAYADITTHI}, {VICIKICCHA}, {SILABBATAPARAMASA}"
    SAKK = f"{TQ(SAKKAYADITTHI)} {SAKKAYA} {cap(DITTHI_SHORT)} {CALLED(SAKKAYADITTHI)}"
    VICI_SHORT = f"{TQ(VICIKICCHA)} {VICI_HEAD}… {VICI_TAIL} {CALLED(VICIKICCHA)}"
    SILA = f"{TQ(SILABBATAPARAMASA)} {SILABBATA} {D} {DITTHI_SHORT} {CALLED(SILABBATAPARAMASA)}"
    seg["1-1261"] = [f"{Q('dassanena pahātabbā')} {cap(THREE_F)}."]
    seg["1-1262"] = [SAKK]
    seg["1-1263"] = [VICI_SHORT]
    seg["1-1264"] = [f"{SILA} These three fetters, {ROOT_TAIL} {E('dassanena pahātabbā')}"]
    seg["1-1265"] = [F_NO("na dassanena pahātabbā")]
    seg["1-1266"] = [F_LIST("bhāvanāya pahātabbā", f"{REMAINING_GHD}, {ROOT_TAIL}")]
    seg["1-1267"] = [F_NO("na bhāvanāya pahātabbā")]
    seg["1-1268"] = [f"{Q('dassanena pahātabbahetukā')} {cap(THREE_F)}."]
    seg["1-1269"] = [SAKK]
    seg["1-1270"] = [VICI_SHORT]
    seg["1-1271"] = [f"{SILA} These three fetters, {ROOT_TAIL} {E('dassanena pahātabbahetukā')} "
                     f"{cap(THREE_F)} {E('dassanena pahātabbā')} The greed, hate and delusion that stand "
                     f"together with them {D} these are the roots to be abandoned by seeing. {cap(ROOT_TAIL)} "
                     f"{E('dassanena pahātabbahetukā')}"]
    seg["1-1272"] = [F_NO("na dassanena pahātabbahetukā")]
    seg["1-1273"] = [f"{Q('bhāvanāya pahātabbahetukā')} {cap(REMAINING_GHD)} {D} these are the roots to be "
                     f"abandoned by development. {cap(ROOT_TAIL)} {E('bhāvanāya pahātabbahetukā')}"]
    seg["1-1274"] = [F_NO("na bhāvanāya pahātabbahetukā")]

    def with_(p, plane, loc, factor, assoc=VV):
        return F_LIST(p, f"in {plane}, in {loc}, leaving {factor} aside, {assoc} associated with it")

    def without(p, plane, loc, factor):
        return F_LIST(p, f"in {plane}, in {loc}: {VV}; {factor}, {RA}")

    seg["1-1275"] = [with_("savitakkā", "the plane with applied thought", LOC_KRP, "applied thought")]
    seg["1-1276"] = [without("avitakkā", "the plane without applied thought", LOC_KRAP, "applied thought")]
    seg["1-1277"] = [with_("savicārā", "the plane with sustained thought", LOC_KRP, "sustained thought", FOUR)]
    seg["1-1278"] = [without("avicārā", "the plane without sustained thought", LOC_KRAP, "sustained thought")]
    seg["1-1279"] = [with_("sappītikā", "the plane with rapture", LOC_KRP, "rapture")]
    seg["1-1280"] = [without("appītikā", "the plane without rapture", LOC_KRAP, "rapture")]
    seg["1-1281"] = [with_("pītisahagatā", "the plane of rapture", LOC_KRP, "rapture")]
    seg["1-1282"] = [without("na pītisahagatā", "what is not the plane of rapture", LOC_KRAP, "rapture")]
    seg["1-1283"] = [with_("sukhasahagatā", "the plane of happiness", LOC_KRP, "happiness", PERC3)]
    seg["1-1284"] = [without("na sukhasahagatā", "what is not the plane of happiness", LOC_KRAP, "happiness")]
    seg["1-1285"] = [with_("upekkhāsahagatā", "the plane of equanimity", LOC_KRAP, "equanimity", PERC3)]
    seg["1-1286"] = [without("na upekkhāsahagatā", "what is not the plane of equanimity", LOC_KRP, "equanimity")]

    MOVE = "move within this range and are included in it"
    WHO = ("of one who has entered meditative attainment, or of one who has been reborn there, or of one who "
           "dwells happily in this very life")
    seg["1-1287"] = [F_LIST("kāmāvacarā",
                            f"taking the Avīci hell as the boundary below, and including above the gods who wield "
                            f"power over the creations of others [variant: paranimmitavasavattideve (Sī., Ka.)], "
                            f"whatever aggregates, elements and sense bases {MOVE}: material form, feeling, "
                            f"perception, mental formations, consciousness")]
    seg["1-1288"] = [F_LIST("na kāmāvacarā", f"{I('rūpāvacarā')}, {I('arūpāvacarā')}, {I('apariyāpannā')}")]
    seg["1-1289"] = [F_LIST("rūpāvacarā",
                            f"taking the Brahma world as the boundary below, and including above the Akaniṭṭha "
                            f"gods [variant: akaniṭṭhadeve (Sī., Ka.)], whatever states of mind and mental factors "
                            f"{MOVE}, of one who has entered meditative attainment, or of one who has been reborn "
                            f"there, or of one who dwells happily in this very life [variant: "
                            f"diṭṭhadhammasukhavihārassa (Ka.)]")]
    seg["1-1290"] = [F_LIST("na rūpāvacarā", f"{I('kāmāvacarā')}, {I('arūpāvacarā')}, {I('apariyāpannā')}")]
    seg["1-1291"] = [F_LIST("arūpāvacarā",
                            f"taking as the boundary below the gods who have reached the base of infinite space, "
                            f"and including above the gods who have reached the base of neither perception nor "
                            f"non-perception, whatever states of mind and mental factors {MOVE}, {WHO}")]
    seg["1-1292"] = [F_LIST("na arūpāvacarā", f"{I('kāmāvacarā')}, {I('rūpāvacarā')}, {I('apariyāpannā')}")]
    seg["1-1293"] = [F_SAS("pariyāpannā")]
    seg["1-1294"] = [F_LIST("apariyāpannā", "the paths, the fruits of the paths, and the unconditioned element")]
    PATHS4 = "the four paths not included in the spheres of existence"
    seg["1-1295"] = [F_LIST("niyyānikā", PATHS4)]
    seg["1-1296"] = [F_NO("aniyyānikā")]
    seg["1-1297"] = [F_LIST("niyatā", f"the five actions with immediate result, the wrong view that is fixed, "
                                      f"and {PATHS4}")]
    seg["1-1298"] = [F_NO("aniyatā")]
    seg["1-1299"] = [F_SAS("sauttarā")]
    seg["1-1300"] = [F_LOKUT("anuttarā")]
    seg["1-1301"] = [F_LIST("saraṇā", f"{ROOTS3}: {GHD}; {ROOT_TAIL}")]
    seg["1-1302"] = [F_LIST("araṇā", f"the {KA} states: {SPH_KRAP}; {VV}; {RA}"), END_ABHI]
    return seg


ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def pali_segments():
    segs, buf = [], []
    for line in PALI.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = ID.search(line)
        if m:
            buf.append(line[:m.start()])
            segs.append((m.group(1), buf))
            buf = []
        else:
            buf.append(line)
    assert not buf
    return segs


def pair_body(line):
    body = line.split("? ", 1)[1].rsplit(f" {D} ime dhammā", 1)[0]
    return body


def ell(t, pali):
    return t.count("…pe…") if pali else t.count("…")


def build():
    segs = pali_segments()
    pd = dict((b, l) for b, l in segs)
    for b in ("1-1176", "1-1231", "1-1257"):
        P[b] = pair_body(pd[b][0])
    eng = build_segments(pd)
    assert set(eng) == set(pd), (set(pd) - set(eng), set(eng) - set(pd))
    out, problems = [], []
    for bid, plines in segs:
        elines = [cap(x) for x in eng[bid]]
        if len(elines) != len(plines):
            problems.append((bid, "line count", len(plines), len(elines)))
        for p, e in zip(plines, elines):
            dp = p.count("–") + p.count("—")
            de = e.count("–") + e.count("—")
            if dp != de:
                problems.append((bid, "dash", dp, de))
            if p.count("?") != e.count("?"):
                problems.append((bid, "?", p.count("?"), e.count("?")))
            if ell(p, True) != ell(e, False):
                problems.append((bid, "ellipsis", ell(p, True), ell(e, False)))
            if p.count("[") != e.count("[variant:"):
                problems.append((bid, "variant", p.count("["), e.count("[variant:")))
            ip = len(re.findall(r"\b[Ii]me dhammā\b", p))
            ie = len(re.findall(r"\b[Tt]hese are\b", e))
            if ip != ie:
                problems.append((bid, "ime dhammā", ip, ie))
            m = re.match(r"Katame dhammā (.+?)\?", p)
            if m:
                key = re.sub(r"\s+", " ", m.group(1))
                if not e.startswith(Q(key)):
                    problems.append((bid, "question", key, e[:80]))
            for bad in ("—", ":-", "outline", "\r", "  "):
                if bad in e:
                    problems.append((bid, "forbidden", bad))
        elines[-1] += f" ^{bid}"
        out.append("\n".join(elines))
    text = "\n\n".join(out) + "\n"
    return text, problems


if __name__ == "__main__":
    text, problems = build()
    for pr in problems:
        print("PROBLEM", pr)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", OUT, "segments", text.count(" ^"), "problems", len(problems))
