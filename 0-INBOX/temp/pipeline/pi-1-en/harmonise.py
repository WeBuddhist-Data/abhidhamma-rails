"""Consistency (harmonise) pass for the pi-1 English plain zero-shot.

Applies fixed old -> new strings (a few fixed regex patterns, marked re=True) to the English parts. A rule
touches an English line ONLY when the aligned Pāli line (non-empty line i <-> non-empty line i) matches the
rule's Pāli pattern. Line counts, block IDs, heading levels and dashes are never touched (checked at the end).
Backup of the pre-pass files: backup-pre-harmonise/. Log: harmonise-log.tsv (rule, part, replacements, lines).

usage: python -I -X utf8 harmonise.py [--dry]
"""
import os, re, sys, collections

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
EDIR = os.path.join(ROOT, r"AI_translation\english\pi-1-english-plain-zeroshot_split_chapters")
HERE = os.path.join(ROOT, r"0-INBOX\temp\pipeline\pi-1-en")
PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam", "2-02-cittuppadakandam", "2-03-cittuppadakandam",
         "2-04-cittuppadakandam", "2-05-cittuppadakandam", "3-01-rupakandam", "3-02-rupakandam", "3-03-rupakandam",
         "4-01-nikkhepakandam", "4-02-nikkhepakandam", "4-03-nikkhepakandam", "5-atthakathakandam"]

R = []  # (id, pali_regex, old, new, is_regex, parts_prefixes or None)


def rule(rid, pali, old, new, rx=False, parts=None):
    R.append((rid, pali, old, new, rx, parts))


# ---- N. ellipsis spacing: Pāli 'X…pe… Y' -> English 'X… Y' (only on lines whose Pāli has no spaced ' …pe…')
ELL = "N-ellipsis"

# ---- A. matrix question frame in chapter 2 (coordinator)
for p, en in [("kusalā", "wholesome"), ("akusalā", "unwholesome"), ("abyākatā", "indeterminate")]:
    rule("A-katame", rf"Katame dhammā {p}\?", f"What states are {en}?", f"What are {en} states?")
    rule("A-ime", rf"ime dhammā {p}\b", f"these states are {en}", f"these are {en} states")

# ---- O. 4-02 Nikkhepa list frames -> 4-01 / 4-03 frames (agent tie; 4-01/4-03 builder covers two of three parts)
O_ALL4 = ("Leaving those states aside, the remaining wholesome, unwholesome and indeterminate states: those of the sense "
          "sphere, of the fine-material sphere, of the immaterial sphere, and those not included in the spheres of existence")
O_ALL4_NEW = ("Except those states, the remaining wholesome, unwholesome and indeterminate states, whether of the sense "
              "sphere, of the fine-material sphere, of the immaterial sphere or not included in the spheres of existence")
rule("O-remaining", r"hapetvā,? avasesā", O_ALL4, O_ALL4_NEW, parts=["4-02"])
rule("O-three-spheres", r"kāmāvacarā, rūpāvacarā, arūpāvacarā",
     ": those of the sense sphere, of the fine-material sphere and of the immaterial sphere",
     ", whether of the sense sphere, of the fine-material sphere or of the immaterial sphere", parts=["4-02"])
rule("O-dissociated-sasava", r"vippayuttā sāsavā kusal",
     "Among the states dissociated from those states, the wholesome", "The states that are dissociated from those states and are wholesome", parts=["4-02"])
rule("O-sasava-start", r"Sāsavā kusal", "The wholesome, unwholesome and indeterminate states subject to taints",
     "Wholesome, unwholesome and indeterminate states subject to taints", parts=["4-02"])
rule("O-sasava-start", r"Sāsavā kusal", "The wholesome and unwholesome states subject to taints",
     "Wholesome and unwholesome states subject to taints", parts=["4-02"])
rule("O-assoc", r"Tehi dhammehi ye dhammā sampayuttā", "The states associated with those states:",
     "The states that are associated with those states:", parts=["4-02"])
rule("O-assoc", r"Tehi dhammehi ye dhammā vippayuttā", "The states dissociated from those states:",
     "The states that are dissociated from those states:", parts=["4-02"])
rule("O-assoc-except", r"Tehi dhammehi ye dhammā sampayuttā,? te dhamme",
     "Among the states associated with those states, leaving those states aside,",
     "Among the states that are associated with those states, except those states,", parts=["4-02"])
for pal, en_old, en_new in [
        ("nīvaraṇiyā", "Among the states subject to those states, leaving those states aside,",
         "Among the states that, in relation to those states, are subject to hindrances, except those states,"),
        ("upādāniyā", "Among the states subject to those states, leaving those states aside,",
         "Among the states that, in relation to those states, are subject to clinging, except those states,"),
        ("saṃkilesikā", "Among the states subject to those states, leaving those states aside,",
         "Among the states that, in relation to those states, are subject to defilement, except those states,"),
        ("parāmaṭṭhā", "Among the states misapprehended by those states, leaving those states aside,",
         "Among the states that, in relation to those states, are misapprehended, except those states,"),
        ("saṃkiliṭṭhā", "Among the states defiled by those states, leaving those states aside,",
         "Among the states that, in relation to those states, are defiled, except those states,")]:
    rule("O-relation-except", rf"Tehi dhammehi ye dhammā {pal},? te dhamme", en_old, en_new, parts=["4-02"])
rule("O-tadekattha", r"[Tt]adekaṭṭh", "stand together with them", "occur together with them", parts=["4-02"])
for old, new in [
        ("the aggregate of feeling… the aggregate of consciousness associated with them", "the associated aggregate of feeling… aggregate of consciousness"),
        ("the aggregate of feeling… the aggregate of consciousness associated with it", "the associated aggregate of feeling… aggregate of consciousness"),
        ("the aggregate of feeling, the aggregate of perception, the aggregate of mental formations, the aggregate of consciousness associated with it",
         "the associated aggregate of feeling, aggregate of perception, aggregate of mental formations, aggregate of consciousness"),
        ("the aggregate of perception, the aggregate of mental formations, the aggregate of consciousness associated with it",
         "the associated aggregate of perception, aggregate of mental formations, aggregate of consciousness")]:
    rule("O-tamsampayutto", r"[Tt]aṃsampayutt", old, new, parts=["4-02"])
rule("O-bhumi-spheres", r"bhūmiyaṃ", ", in the sense sphere, the fine-material sphere and what is not included in the spheres of existence, ",
     ", whether of the sense sphere, of the fine-material sphere or not included in the spheres of existence, ", parts=["4-02"])
rule("O-bhumi-spheres", r"bhūmiyaṃ", ", in the sense sphere, the fine-material sphere, the immaterial sphere and what is not included in the spheres of existence, ",
     ", whether of the sense sphere, of the fine-material sphere, of the immaterial sphere or not included in the spheres of existence, ", parts=["4-02"])
rule("O-avaseso", r"Avaseso lobho", "The remaining greed, hate and delusion", "The remaining greed, hate, delusion", parts=["4-02"])
rule("O-sabbanca", r"sabbañca rūpaṃ", "all material form, and the unconditioned element", "all material form and the unconditioned element")
for nm in ["hindrances", "kinds of clinging", "defilements"]:
    rule("O-teva", r"^Katame dhammā .* (Tāneva|Teva) ", f"Those same {nm} are both ", f"Those same {nm} are states that are both ", parts=["4-02"])
rule("O-sveva", r"Sveva parāmāso|So eva parāmāso", "That same misapprehension is both a misapprehension and misapprehended.",
     "That same misapprehension is one of the states that are both misapprehensions and misapprehended.", parts=["4-02"])
rule("O-pahatabbahetu", r"pahātabbahetū\.", "these are the roots to be abandoned by", "these are roots to be abandoned by", parts=["4-02"])

# ---- B. ṭhapetvā = except (build_2-01_2-02)
rule("B-thapetva", r"hapetvā", "apart from ", "except ", parts=["2-05"])
rule("B-thapetva", r"hapetvā", "Except for ", "Except ")
rule("B-thapetva", r"hapetvā", "except for ", "except ")
rule("B-thapetva", r"hapetvā", "Leaving those states aside, ", "Except those states, ")
rule("B-thapetva", r"hapetvā", r"leaving ((?:\w+ ){0,3}?\w+) aside", r"except \1", rx=True)
rule("B-thapetva", r"hapetvā", "Leaving aside ", "Except ")
rule("B-thapetva", r"hapetvā", "leaving aside ", "except ")

# ---- C. tattha = Therein (majority 4-01/4-03)
rule("C-tattha", r"\bTattha\b", "Of these, ", "Therein, ", parts=["4-02"])
rule("C-tattha", r"\bTattha\b", "Among these, ", "Therein, ", parts=["3-01"])

# ---- D. paṭipadā / suddhika headings in 2-05 -> 2-01 builder and 2-03
rule("D-patipada", r"paṭipadaṃ", "with difficult practice", "with painful progress", parts=["2-05"])
rule("D-patipada", r"paṭipadaṃ", "with easy practice", "with pleasant progress", parts=["2-05"])
for old, new in [
        ("Desire as the Dominant Factor: The Simple Modes of Practice", "Desire as the Dominant Factor: Plain Progress"),
        ("Desire as the dominant factor: the simple modes of practice.", "Desire as the dominant factor: plain progress."),
        ("Desire as the Dominant Factor: Simple Emptiness", "Desire as the Dominant Factor: Plain Emptiness"),
        ("Desire as the dominant factor: simple emptiness.", "Desire as the dominant factor: plain emptiness."),
        ("The Simple Modes of Practice", "Plain Progress"), ("The simple modes of practice.", "Plain progress."),
        ("Simple Emptiness", "Plain Emptiness"), ("Simple emptiness.", "Plain emptiness."),
        ("Emptiness with the Modes of Practice", "Progress with Emptiness"), ("Emptiness with the modes of practice.", "Progress with emptiness."),
        ("Simple Desirelessness", "The Plain Desireless"), ("Simple desirelessness.", "The plain desireless."),
        ("Desirelessness with the Modes of Practice", "Progress with the Desireless"),
        ("Desirelessness with the modes of practice.", "Progress with the desireless.")]:
    rule("D-headings", r"^#*\s*\S*(paṭipadā|suññat|appaṇihit)\S*\.? \^|^\S*(paṭipadā|suññat|appaṇihit)\S*\.?$", old, new, parts=["2-05"])

# ---- E. 2-05 world-transcending, result and functional formulas -> 2-02 / 2-03 / 2-04
rule("E-niyyanika", r"niyyānikaṃ apacayagāmiṃ", "absorption that leads to liberation and leads away from accumulation",
     "absorption, which leads to liberation and leads away from accumulation", parts=["2-05"])
rule("E-niyyanika", r"niyyānikaṃ apacayagāmiṃ", "mind that leads to liberation and leads away from accumulation",
     "mind, which leads to liberation and leads away from accumulation", parts=["2-05"])
rule("E-stage-and", r"bhūmiyā pattiyā", r"(stage), and, ", r"\1, and ", rx=True, parts=["2-05"])
rule("E-tasseva", r"Tasseva lokuttarassa kusalassa jhānassa katattā bhāvitattā vipākaṃ",
     "Because that same world-transcending wholesome absorption has been done and developed, as its result one, ",
     "As a result of that same world-transcending wholesome absorption that has been done and developed, when one, ", parts=["2-05"])
rule("E-sunnata", r"bhāveti.*(suññat|animitt|appaṇihit)", r"(?<!which is )\b(empty|signless|desireless)\b", r"which is \1",
     rx=True, parts=["2-05"])
rule("E-pathavi", r"pathavīkasiṇaṃ", "using the earth meditation device", "using earth as the meditation device")
rule("E-maggangam", r"maggaṅgaṃ maggapariyāpannaṃ", "a factor of the path, included in the path", "a path factor, included in the path")
rule("E-ruparaga", r"rūparāgaarūparāga", "lust for the fine-material, lust for the immaterial,",
     "lust for fine-material existence, lust for immaterial existence,")
rule("E-samatikkama", r"sabbaso rūpasaññānaṃ samatikkamā",
     "with the complete surmounting of perceptions of material form, with the disappearance of perceptions of impact, with non-attention to perceptions of diversity",
     "by completely passing beyond perceptions of material form, by the disappearance of perceptions of impact, by not attending to perceptions of diversity")
rule("E-samatikkama", r"samatikkamma", "completely surmounting ", "having completely passed beyond ")
rule("E-sukhassa", r"sukhassa ca pahānā", "with the abandoning of happiness", "with the abandoning of pleasure")
rule("E-sasankharena", r"sasaṅkhārena", r"accompanied by (joy|equanimity), (associated with|dissociated from) knowledge and with prompting",
     r"accompanied by \1 and \2 knowledge, with prompting", rx=True)
rule("E-akusalavipaka", r"akusalassa kammassa katattā upacitattā",
     r"because unwholesome action has been done and accumulated, (eye-consciousness|the mind element|the mind-consciousness element) has arisen as its result",
     r"as a result of unwholesome action that has been done and accumulated, \1 has arisen", rx=True)
rule("E-kiriya", r"kiriy", "merely functional", "functional")

# ---- G. kakkhaḷa = hard (coordinator); akathina then = rigidity
rule("G-mudu", r"akakkhaḷatā akathinatā", "freedom from roughness, freedom from hardness", "freedom from hardness, freedom from rigidity")

# ---- P. long synonym strings (item-level vote of the three agents; tie -> chapter-2 version, 2-way 4-01 vs 4-02 tie -> 4-01/4-03)
# P1 diṭṭhi string
for old, new in [("holding a view", "holding views"), ("being caught in views", "holding views"),
                 ("the writhing of views", "the vacillation of views"), ("grasping, holding firmly,", "grasping, fixation,"),
                 ("grasping, taking a stand,", "grasping, fixation,"), ("a wrong path, a false way", "a wrong road, a wrong path"),
                 ("the ground of sectarian views", "a basis for sectarian doctrines"),
                 ("wrongness, a sectarian doctrine,", "wrongness, a basis for sectarian doctrines,"),
                 ("grasping things the wrong way round", "a distorted grasp"), ("inverted grasping", "a distorted grasp")]:
    rule("P1-ditthi", r"diṭṭhigataṃ", old, new)
# P2 moha / aññāṇa string
for old, new in [("lack of breakthrough", "non-realisation"), ("deep delusion, confusion,", "deep delusion, utter delusion,"),
                 ("non-realisation, non-understanding, non-awakening, non-penetration, failure to grasp, failure to plunge in, failure to examine, failure to reflect, failure to perceive directly",
                  "non-realisation, lack of understanding, lack of awakening, non-penetration, failure to take in, failure to fathom, failure to consider, failure to review, failure to see for oneself"),
                 ("non-realisation, not understanding, not awakening, non-penetration, not grasping, not plunging in, not examining, not reviewing, not making it directly evident",
                  "non-realisation, lack of understanding, lack of awakening, non-penetration, failure to take in, failure to fathom, failure to consider, failure to review, failure to see for oneself")]:
    rule("P2-moha", r"adassanaṃ", old, new)
rule("P2-moha", r"adassanaṃ", "lack of awakening, lack of penetration,", "lack of awakening, non-penetration,")
rule("P2-moha", r"aññāṇaṃ", "lack of knowledge about ", "lack of knowledge of ", parts=["4-02"])
# P3 kaṅkhā string
for old, new in [("a fork in the road", "a forked path"), ("scratching of the mind", "mental scratching"),
                 ("doubt, wavering, a forked path, indecision, failure to take a definite stand, hesitation, vacillation, failure to plunge in, rigidity of mind",
                  "doubt, indecision, a forked path, wavering, failure to take a definite stand, hesitation, faltering, failure to fathom, stiffness of mind"),
                 ("doubt, being in two minds, a forked path, hesitation, not settling on one side, faltering, wavering, not plunging in, stiffness of mind",
                  "doubt, indecision, a forked path, wavering, failure to take a definite stand, hesitation, faltering, failure to fathom, stiffness of mind")]:
    rule("P3-kankha", r"kaṅkhāyanā", old, new)
# P4 dosa string (tail = 2-04 string; head: 4-01 version with byāpatti = malice and 'of mind')
DOSA = ("annoyance of mind of this kind there is, resentment, aversion, antagonism, irritation, exasperation, fury, hate, hatred, "
        "intense hatred, malice of mind, mental hatred, anger, being angry, the state of being angry, hate, hating, the state of "
        "hating, malice, being malicious, the state of being malicious, hostility, antagonism, fierceness, abusiveness, discontent of mind")
rule("P4-dosa", r"āghāto paṭighāto", "annoyance of the mind of this kind there is, resentment, aversion, opposition, irritation, exasperation, fury, hate, hatred, intense hatred, malevolence of the mind, mental hatred, anger, being angry, the state of being angry, hate, hating, the state of hating, malevolence, being malicious, the state of being malicious, conflict, opposition, ferocity, abusiveness, displeasure of the mind", DOSA)
rule("P4-dosa", r"āghāto paṭighāto", "resentment of mind of this kind there is, repugnance, aversion, hostility, anger, rising anger, intense anger, hate, rising hate, intense hate, malice of mind, mental hatred, wrath, being wrathful, the state of being wrathful, hate, hating, the state of hating, malice, being malicious, the state of being malicious, opposition, hostility, fierceness, rudeness, discontent of mind", DOSA)
rule("P4-dosa", r"āghāto jāyati", "Resentment arises at the thought", "Annoyance arises at the thought", parts=["4-02"])
rule("P4-dosa", r"āghāto jāyati", "\"; resentment arises at the thought", "\", annoyance arises at the thought", parts=["4-02"])
rule("P4-dosa", r"āghāto jāyati", "; or resentment arises without reason", ", or annoyance arises without reason", parts=["4-02"])
rule("P4-dosa", r"āghāto jāyati", "Whatever resentment of mind of this kind", "Whatever annoyance of mind of this kind", parts=["4-02"])
# P5 lobha long string (4-02 -> 4-01; 'of mind' pattern of the approved list)
LOBHA_02 = ("lust, passion, favouring, compliance, delight, delight and lust, passion of mind, wishing, infatuation, attachment, hunger, deep hunger, sticking, a swamp, stirring, deception, the begetter, the producer, the seamstress, the ensnarer, the stream, the entangler, a thread, the spreading one, the striver, the companion, aspiration, the guide to existence, a forest, undergrowth, intimacy, affection, concern, kinship, longing, yearning, the state of yearning, longing for visible forms, longing for sounds, longing for smells, longing for tastes, longing for touches, longing for gain, longing for wealth, longing for children, longing for life, hankering, strong hankering, intense hankering, hankering, hankering after things, the state of hankering, voracity, being voracious, the state of being voracious, fawning, wanting the best, unrighteous lust, unjust greed, liking, wanting, desiring, envying, strong desiring, sensual craving, craving for continued existence, craving for non-existence, craving for fine-material existence, craving for immaterial existence, craving for cessation, craving for visible forms, craving for sounds, craving for smells, craving for tastes, craving for touches, craving for mental objects, a flood, a yoke, a tie, clinging, an obstruction, a hindrance, a covering, a bond, an impurity, an underlying tendency, an obsession, a creeper, avarice,")
LOBHA_01 = ("lust, passion, compliance, accommodation, delight, delight and lust, passion of mind, wanting, infatuation, holding on, eagerness, intense eagerness, attachment, the mire, agitation, deceit, the begetter, the producer, the seamstress, the net-maker, the stream, the entangler, the thread, the spreading one, the accumulator, the companion, aspiration, the conduit to existence, the forest, the undergrowth, intimacy, affection, concern, kinship, hope, hoping, the state of hoping, hope for visible forms, hope for sounds, hope for smells, hope for tastes, hope for touches, hope for gain, hope for wealth, hope for children, hope for life, hankering, intense hankering, extreme hankering, hankering, the act of hankering, the state of hankering, voracity, being voracious, the state of voracity, fawning, the wish for fine things, unrighteous lust, lawless greed, liking, desiring, longing, envying, earnest longing, sensual craving, craving for continued existence, craving for non-existence, craving for fine-material existence, craving for immaterial existence, craving for cessation, craving for visible forms, craving for sounds, craving for smells, craving for tastes, craving for touches, craving for mental objects, the flood, the yoke, the tie, clinging, the obstruction, the hindrance, the covering, the bond, the corruption, the underlying tendency, the obsession, the creeper, meanness,")
rule("P5-lobha", r"cittassa sārāgo", "passion of the mind", "passion of mind")
rule("P5-lobha", r"cittassa sārāgo", LOBHA_02, LOBHA_01)
# P6 māna string (4-02 -> 4-01)
rule("P6-mana", r"Seyyohamasmīti", "The conceit \"I am better\", the conceit \"I am equal\", the conceit \"I am worse\"; whatever conceit of this kind there is, conceiving, the state of conceiving, haughtiness, loftiness, a flag, self-exaltation, the mind's desire to be a banner",
     "Conceit that \"I am better\", conceit that \"I am equal\", conceit that \"I am inferior\"; whatever conceit of this kind there is, conceiving, the state of having conceived, loftiness, haughtiness, flag-raising, self-exaltation, the mind's wish to fly its banner")
# P7 ten views (4-02 -> 4-01)
rule("P7-views", r"Sassato lokoti", "\", or \"", "\" or \"", parts=["4-02"])
rule("P7-views", r"Sassato lokoti", "\"The soul is the same as the body\"", "\"The soul and the body are the same\"", parts=["4-02"])
# P8 natthi dinnaṃ (4-02 -> 4-03)
rule("P8-natthi", r"[Nn]atthi dinnaṃ", "there is no fruit or result of good and bad actions, this world does not exist, the other world does not exist, there is no mother, there is no father, there are no spontaneously born beings, there are no ascetics and brahmins in the world who have gone rightly [variant: samaggatā (Ka.)] and practise rightly, who have realised this world and the other world by their own direct knowledge and make it known",
     "there is no fruit or result of good and bad actions, there is no this world, there is no other world, there is no mother, there is no father, there are no beings spontaneously reborn, there are in the world no ascetics and brahmins who have gone rightly [variant: samaggatā (Ka.)] and practise rightly and who, having realised this world and the other world by their own direct knowledge, make them known")
# P9 sīlena suddhi (4-01 -> 4-02: suddhi = purification, as visuddhi in the approved list)
rule("P9-suddhi", r"sīlena suddhi", "outside this teaching hold that \"purity comes through rules, purity comes through observances, purity comes through rules and observances\"",
     "outside this Teaching hold that \"Purification comes through rules, purification comes through observances, purification comes through rules and observances\"")
# P10 kāmajjhosānaṃ (tie -> 4-01)
rule("P10-kama", r"kāmajjhosānaṃ", "sensual attachment", "sensual holding on")
# P11 puthujjano (4-02 majority)
rule("P11-puthujjana", r"assutavā puthujjano", "is not skilled in the teaching of the noble ones and not trained in the teaching of the noble ones",
     "is unskilled in the teaching of the noble ones and undisciplined in the teaching of the noble ones")
rule("P11-puthujjana", r"assutavā puthujjano", "is not skilled in the teaching of good people and not trained in the teaching of good people",
     "is unskilled in the teaching of good people and undisciplined in the teaching of good people")
# P12 uddhacca string (2-04 vs 4-02 tie -> chapter-2 version)
rule("P12-uddhacca", r"uddhaccaṃ avūpasamo", "restlessness of mind, unsettledness, distraction of mind, the mind's whirling",
     "restlessness of mind, disquiet, distraction of the mind, agitation of mind")

# ---- Q/R/S/M. ch3-5 items
rule("Q-katatta", r"kammassa katattā", "due to action having been done", "due to past action")
rule("R-kabalikara", r"kabaḷīkār", "the nutriment of solid food", "edible food")
rule("S-hyphen", r"viññāṇ", r"\b([Ee]ye|[Ee]ar|[Nn]ose|[Tt]ongue|[Bb]ody) consciousness\b", r"\1-consciousness", rx=True)
rule("M-vattabba", r"Cittaṃ na vattabbaṃ", "Mind is not to be described – as associated with mind, nor as dissociated from mind.",
     "Mind should not be described – either as \"associated with mind\" or as \"dissociated from mind\".", parts=["5-"])
rule("M-vattabba", r"Cittaṃ na vattabbaṃ", "Mind is not to be described – as joined with mind, nor as not joined with mind.",
     "Mind should not be described – either as \"joined with mind\" or as \"not joined with mind\".", parts=["5-"])
rule("T-tayo-hetu", r"Tayo kusalahetū, tayo akusalahetū, tayo abyākatahetū",
     "Three wholesome roots, three unwholesome roots, three indeterminate roots.",
     "The three wholesome roots, the three unwholesome roots, the three indeterminate roots.", parts=["5-"])
rule("J-heṭṭhimāni", r"apariyāpannā, heṭṭhimāni", "spheres of existence and the three lower fruits", "spheres of existence, and the three lower fruits", parts=["5-"])


def nonempty_idx(lines):
    return [i for i, l in enumerate(lines) if l.strip()]


def dashes(t):
    return t.count("—") + t.count("–")


def main(dry=False):
    log = collections.defaultdict(lambda: [0, 0])  # (rid, part) -> [replacements, lines]
    changed_lines = collections.Counter()
    hit_idx = set()
    comp = [(rid, re.compile(p), old, new, rx, parts) for rid, p, old, new, rx, parts in R]
    for part in PARTS:
        pl = [l for l in open(os.path.join(PDIR, part + ".md"), encoding="utf-8-sig").read().splitlines() if l.strip()]
        raw = open(os.path.join(EDIR, part + ".md"), encoding="utf-8").read()
        bom = raw.startswith("\ufeff")
        text = raw.lstrip("\ufeff")
        assert "\r" not in text, part
        el = text.split("\n")
        idx = nonempty_idx(el)
        assert len(idx) == len(pl), (part, len(idx), len(pl))
        for k, li in enumerate(idx):
            p, e0 = pl[k], el[li]
            e = e0
            # N: ellipsis spacing
            if "…pe…" in p and not re.search(r"\s…pe…", p):
                n_e = re.subn(r"(?<=[^\s…]) …", "…", e)
                if n_e[1]:
                    e = n_e[0]
                    log[(ELL, part)][0] += n_e[1]; log[(ELL, part)][1] += 1
            for ri, (rid, pr, old, new, rx, parts) in enumerate(comp):
                if parts and not any(part.startswith(x) for x in parts):
                    continue
                if not pr.search(p):
                    continue
                if rx:
                    e2, n = re.subn(old, new, e)
                else:
                    n = e.count(old)
                    e2 = e.replace(old, new)
                if n:
                    e = e2
                    hit_idx.add(ri)
                    log[(rid, part)][0] += n
                    log[(rid, part)][1] += 1
            if e != e0:
                assert dashes(e) == dashes(e0), (part, k, "dash count changed")
                assert re.findall(r"\^[\w-]+\s*$", e) == re.findall(r"\^[\w-]+\s*$", e0), (part, k, "block id")
                assert re.match(r"#*", e).group(0) == re.match(r"#*", e0).group(0), (part, k, "heading")
                el[li] = e
                changed_lines[part] += 1
        if not dry:
            out = ("\ufeff" if bom else "") + "\n".join(el)
            open(os.path.join(EDIR, part + ".md"), "w", encoding="utf-8", newline="\n").write(out)
    with open(os.path.join(HERE, "harmonise-log.tsv"), "w", encoding="utf-8") as f:
        f.write("rule\tpart\treplacements\tlines\n")
        for (rid, part), (n, l) in sorted(log.items()):
            f.write(f"{rid}\t{part}\t{n}\t{l}\n")
    tot = collections.defaultdict(lambda: [0, 0])
    for (rid, part), (n, l) in log.items():
        tot[rid][0] += n; tot[rid][1] += l
    for rid in sorted(tot):
        print(f"{rid:24s} repl={tot[rid][0]:5d} lines={tot[rid][1]:5d}")
    print("lines changed per part:", dict(changed_lines), "total", sum(changed_lines.values()))
    for ri, r in enumerate(R):
        if ri not in hit_idx:
            print("NO HIT:", r[0], "|", r[2][:90])


if __name__ == "__main__":
    main(dry="--dry" in sys.argv)
