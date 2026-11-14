"""Build the English plain zero-shot of pi-1 chapter 1 (the matrix, 1-matika.md).

usage: python -I -X utf8 build_matika.py
Reads the Pāli split chapter, attaches each block ID to the English segment with the
same ID, checks line counts, and writes the English split chapter.
Also exposes MATRIX_ITEMS (block id, letter, Pāli, English) for build_terms.py.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "1-matika.md"
OUT = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters" / "1-matika.md"

# ---- fixed names reused by later chapters -------------------------------------------
H_MATIKA = "### The Matrix"
H_TIKA = "#### The Matrix of Sets of Three"
H_DUKA = "#### The Matrix of Pairs"
END_TIKA = "The matrix of sets of three."
END_ABHI_DUKA = "The matrix of the Abhidhamma pairs."
END_MATIKA = "The matrix is complete."

GROUPS = {
    # heading id: (heading, closing line)
    "1-M-2-1-0": ("##### The Group on Roots", "The group on roots."),
    "1-M-2-2-0": ("##### The Short Intermediate Pairs", "The short intermediate pairs."),
    "1-M-2-3-0": ("##### The Group on Taints", "The group on taints."),
    "1-M-2-4-0": ("##### The Group on Fetters", "The group on fetters."),
    "1-M-2-5-0": ("##### The Group on Ties", "The group on ties."),
    "1-M-2-6-0": ("##### The Group on Floods", "The group on floods."),
    "1-M-2-7-0": ("##### The Group on Yokes", "The group on yokes."),
    "1-M-2-8-0": ("##### The Group on Hindrances", "The group on hindrances."),
    "1-M-2-9-0": ("##### The Group on Misapprehension", "The group on misapprehension."),
    "1-M-2-10-0": ("##### The Long Intermediate Pairs", "The long intermediate pairs."),
    "1-M-2-11-0": ("##### The Group on Clinging", "The group on clinging."),
    "1-M-2-12-0": ("##### The Group on Defilements", "The group on defilements."),
    "1-M-2-13-0": ("##### The Closing Pairs", "The closing pairs."),
    "1-M-2-14-0": ("##### The Matrix of the Discourse Pairs",
                   "The matrix of the discourse pairs [variant: suttantamātikā (Syā.)]."),
}

# ---- the triads -----------------------------------------------------------------------
TRIADS = {
    1: ["Wholesome states.", "Unwholesome states.", "Indeterminate states."],
    2: ["States associated with pleasant feeling.", "States associated with painful feeling.",
        "States associated with feeling that is neither painful nor pleasant."],
    3: ["States that are results.", "States that produce results.",
        "States that neither are results nor produce results."],
    4: ["States produced by past action and subject to clinging [variant: upādinnupādāniyā (Syā.)].",
        "States not produced by past action but subject to clinging.",
        "States neither produced by past action nor subject to clinging [variant: anupādinnānupādāniyā (Syā.)]."],
    5: ["States that are defiled and subject to defilement.",
        "States that are undefiled but subject to defilement.",
        "States that are undefiled and not subject to defilement [variant: asaṃkiliṭṭhāsaṃkilesikā (Syā.)]."],
    6: ["States with applied thought and sustained thought.",
        "States without applied thought but with sustained thought only.",
        "States without applied thought and without sustained thought [variant: avitakkāvicārā (Syā.)]."],
    7: ["States accompanied by rapture.", "States accompanied by happiness.", "States accompanied by equanimity."],
    8: ["States to be abandoned by seeing.", "States to be abandoned by development.",
        "States to be abandoned neither by seeing nor by development."],
    9: ["States whose roots are to be abandoned by seeing.",
        "States whose roots are to be abandoned by development.",
        "States whose roots are to be abandoned neither by seeing nor by development."],
    10: ["States leading to accumulation.", "States leading away from accumulation.",
         "States leading neither to nor away from accumulation [variant: nevācayagāmino nāpacayagāmino (Syā.)]."],
    11: ["States of one in training.", "States of one beyond training.",
         "States of one neither in training nor beyond training [variant: nevasekkhānāsekkhā (Sī., Syā.)]."],
    12: ["Limited states.", "Exalted states.", "Immeasurable states."],
    13: ["States with a limited object.", "States with an exalted object.", "States with an immeasurable object."],
    14: ["Inferior states.", "Middling states.", "Superior states."],
    15: ["States fixed in wrongness.", "States fixed in rightness.", "States that are not fixed."],
    16: ["States with the path as their object.", "States with the path as their root.",
         "States with the path as their dominant factor."],
    17: ["Arisen states.", "States that have not arisen.", "States that are bound to arise."],
    18: ["Past states.", "Future states.", "Present states."],
    19: ["States with a past object.", "States with a future object.", "States with a present object."],
    20: ["One's own states.", "Others' states.", "States both one's own and others'."],
    21: ["States with one's own states as object.", "States with others' states as object.",
         "States with both one's own and others' states as object."],
    22: ["States that are visible and make impact.", "States that are invisible but make impact.",
         "States that are invisible and make no impact [variant: anidassanāppaṭighā (Syā.)]."],
}


def group6(plural, subj, nsubj, free):
    """The six pairs of a group (taints, fetters, ...).
    plural: 'taints'; subj: 'subject to taints'; nsubj: 'not subject to taints' or 'free of taints'."""
    return [
        [f"States that are {plural}.", f"States that are not {plural}."],
        [f"States {subj}.", f"States {nsubj}."],
        [f"States associated with {free}.", f"States dissociated from {free}."],
        [f"States that are both {plural} and {subj}.", f"States that are {subj} but are not {plural}."],
        [f"States that are both {plural} and associated with {free}.",
         f"States that are associated with {free} but are not {plural}."],
        [f"States dissociated from {free} but {subj}.", f"States dissociated from {free} and {nsubj}."],
    ]


PAIRS = {}
# roots
PAIRS.update({
    1: ["States that are roots.", "States that are not roots."],
    2: ["States with roots.", "States without roots."],
    3: ["States associated with roots.", "States dissociated from roots."],
    4: ["States that are both roots and have roots.", "States that have roots but are not roots."],
    5: ["States that are both roots and associated with roots.",
        "States that are associated with roots but are not roots."],
    6: ["States that are not roots but have roots.", "States that are not roots and are without roots."],
})
# short intermediate pairs
PAIRS.update({
    7: ["States that have conditions.", "States without conditions."],
    8: ["Conditioned states.", "Unconditioned states."],
    9: ["Visible states.", "Invisible states."],
    10: ["States that make impact.", "States that make no impact."],
    11: ["Material states.", "Immaterial states."],
    12: ["Worldly states.", "States that transcend the world."],
    13: ["States that some kinds of consciousness can know.", "States that some kinds of consciousness cannot know."],
})
for start, g in ((14, group6("taints", "subject to taints", "free of taints", "taints")),
                 (20, group6("fetters", "subject to fetters", "not subject to fetters", "fetters")),
                 (26, group6("ties", "subject to ties", "not subject to ties", "ties")),
                 (32, group6("floods", "subject to floods", "not subject to floods", "floods")),
                 (38, group6("yokes", "subject to yokes", "not subject to yokes", "yokes")),
                 (44, group6("hindrances", "subject to hindrances", "not subject to hindrances", "hindrances"))):
    for i, p in enumerate(g):
        PAIRS[start + i] = p
# misapprehension (five pairs)
PAIRS.update({
    50: ["States that are misapprehensions.", "States that are not misapprehensions."],
    51: ["Misapprehended states.", "States that are not misapprehended."],
    52: ["States associated with misapprehension.", "States dissociated from misapprehension."],
    53: ["States that are both misapprehensions and misapprehended.",
         "States that are misapprehended but are not misapprehensions."],
    54: ["States dissociated from misapprehension but misapprehended.",
         "States dissociated from misapprehension and not misapprehended."],
})
# long intermediate pairs
PAIRS.update({
    55: ["States that have an object.", "States without an object."],
    56: ["States that are mind.", "States that are not mind."],
    57: ["States that are mental factors.", "States that are not mental factors."],
    58: ["States associated with mind.", "States dissociated from mind."],
    59: ["States joined with mind.", "States not joined with mind."],
    60: ["States arising from mind.", "States not arising from mind."],
    61: ["States existing together with mind.", "States not existing together with mind."],
    62: ["States accompanying mind.", "States not accompanying mind."],
    63: ["States joined with and arising from mind.", "States not joined with and arising from mind."],
    64: ["States joined with, arising from and existing together with mind.",
         "States not joined with, arising from and existing together with mind."],
    65: ["States joined with, arising from and accompanying mind.",
         "States not joined with, arising from and accompanying mind."],
    66: ["Internal states.", "External states."],
    67: ["Derived states.", "States that are not derived."],
    68: ["States produced by past action [variant: upādinnā (Sī., Syā.)].", "States not produced by past action."],
})
# clinging
for i, p in enumerate(group6("kinds of clinging", "subject to clinging", "not subject to clinging", "clinging")):
    PAIRS[69 + i] = p
# defilements (eight pairs)
PAIRS.update({
    75: ["States that are defilements.", "States that are not defilements."],
    76: ["States subject to defilement.", "States not subject to defilement."],
    77: ["Defiled states.", "Undefiled states."],
    78: ["States associated with defilements.", "States dissociated from defilements."],
    79: ["States that are both defilements and subject to defilement.",
         "States that are subject to defilement but are not defilements."],
    80: ["States that are both defilements and defiled.", "States that are defiled but are not defilements."],
    81: ["States that are both defilements and associated with defilements.",
         "States that are associated with defilements but are not defilements."],
    82: ["States dissociated from defilements but subject to defilement.",
         "States dissociated from defilements and not subject to defilement."],
})
# closing pairs
PAIRS.update({
    83: ["States to be abandoned by seeing.", "States not to be abandoned by seeing."],
    84: ["States to be abandoned by development.", "States not to be abandoned by development."],
    85: ["States whose roots are to be abandoned by seeing.", "States whose roots are not to be abandoned by seeing."],
    86: ["States whose roots are to be abandoned by development.",
         "States whose roots are not to be abandoned by development."],
    87: ["States with applied thought.", "States without applied thought."],
    88: ["States with sustained thought.", "States without sustained thought."],
    89: ["States with rapture.", "States without rapture."],
    90: ["States accompanied by rapture.", "States not accompanied by rapture."],
    91: ["States accompanied by happiness.", "States not accompanied by happiness."],
    92: ["States accompanied by equanimity.", "States not accompanied by equanimity."],
    93: ["States of the sense sphere.", "States not of the sense sphere."],
    94: ["States of the fine-material sphere.", "States not of the fine-material sphere."],
    95: ["States of the immaterial sphere.", "States not of the immaterial sphere."],
    96: ["States included in the spheres of existence.", "States not included in the spheres of existence."],
    97: ["States that lead to liberation.", "States that do not lead to liberation."],
    98: ["Fixed states.", "States that are not fixed."],
    99: ["Surpassable states.", "Unsurpassable states."],
    100: ["States with conflict.", "States without conflict."],
})
# discourse pairs
PAIRS.update({
    101: ["States that share in true knowledge.", "States that share in ignorance."],
    102: ["States like lightning.", "States like a diamond."],
    103: ["Foolish states.", "Wise states."],
    104: ["Dark states.", "Bright states."],
    105: ["States that cause torment.", "States that do not cause torment."],
    106: ["States that are names.", "States that are pathways for names."],
    107: ["States that are expressions.", "States that are pathways for expressions."],
    108: ["States that are designations.", "States that are pathways for designations."],
    109: ["Mentality.", "Material form."],
    110: ["Ignorance.", "Craving for continued existence."],
    111: ["The view of continued existence.", "The view of non-existence."],
    112: ["The eternalist view.", "The annihilationist view."],
    113: ["The view that there is an end.", "The view that there is no end."],
    114: ["The view concerning the past.", "The view concerning the future."],
    115: ["Shamelessness.", "Fearlessness of wrongdoing."],
    116: ["Moral shame.", "Fear of wrongdoing."],
    117: ["Being hard to correct.", "Having bad friends."],
    118: ["Being easy to correct.", "Having good friends."],
    119: ["Skill regarding offences.", "Skill in emerging from offences."],
    120: ["Skill in meditative attainments.", "Skill in emerging from meditative attainments."],
    121: ["Skill in the elements.", "Skill in attention."],
    122: ["Skill in the sense bases.", "Skill in dependent origination."],
    123: ["Skill in what is possible.", "Skill in what is impossible."],
    124: ["Straightforwardness.", "Mildness."],
    125: ["Patience.", "Gentleness."],
    126: ["Courtesy.", "Hospitality [variant: paṭisandhāro ca (Ka.)]."],
    127: ["Not guarding the doors of the senses.", "Not knowing moderation in eating."],
    128: ["Guarding the doors of the senses.", "Knowing moderation in eating."],
    129: ["Forgetfulness.", "Lack of clear awareness."],
    130: ["Mindfulness.", "Clear awareness."],
    131: ["The power of reflection.", "The power of development."],
    132: ["Calm.", "Insight."],
    133: ["The sign of calm.", "The sign of exertion."],
    134: ["Exertion.", "Non-distraction."],
    135: ["Failure in morality.", "Failure in view."],
    136: ["Accomplishment in morality.", "Accomplishment in view."],
    137: ["Purification of morality.", "Purification of view."],
    138: ["Purification of view.", "And effort in keeping with one's view."],
    139: ["A sense of urgency about the things that should stir it.", "And the wise effort of one so stirred."],
    140: ["Not being content with wholesome states.", "Not holding back in effort."],
    141: ["True knowledge.", "Liberation."],
    142: ["Knowledge of destruction.", "Knowledge of non-arising."],
})

LETTERS = "abc"
PALI_LETTERS = ["(Ka)", "(Kha)", "(Ga)"]

# closing lines that follow the last item of a group, keyed by the block id that carries them
TAILS = {
    "1-M1-22": [END_TIKA],
    "1-M2-6": [GROUPS["1-M-2-1-0"][1]],
    "1-M2-13": [GROUPS["1-M-2-2-0"][1]],
    "1-M2-19": [GROUPS["1-M-2-3-0"][1]],
    "1-M2-25": [GROUPS["1-M-2-4-0"][1]],
    "1-M2-31": [GROUPS["1-M-2-5-0"][1]],
    "1-M2-37": [GROUPS["1-M-2-6-0"][1]],
    "1-M2-43": [GROUPS["1-M-2-7-0"][1]],
    "1-M2-49": [GROUPS["1-M-2-8-0"][1]],
    "1-M2-54": [GROUPS["1-M-2-9-0"][1]],
    "1-M2-68": [GROUPS["1-M-2-10-0"][1]],
    "1-M2-74": [GROUPS["1-M-2-11-0"][1]],
    "1-M2-82": [GROUPS["1-M-2-12-0"][1]],
    "1-M2-100": [GROUPS["1-M-2-13-0"][1], END_ABHI_DUKA],
    "1-M2-142": [GROUPS["1-M-2-14-0"][1], END_MATIKA],
}

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
    assert not buf, "trailing lines without id"
    return segs


def english_segment(bid):
    if bid == "1-M-0":
        return [H_MATIKA]
    if bid == "1-M-1-0":
        return [H_TIKA]
    if bid == "1-M-2-0":
        return [H_DUKA]
    if bid in GROUPS:
        return [GROUPS[bid][0]]
    m = re.fullmatch(r"1-M([12])-(\d+)", bid)
    assert m, bid
    items = (TRIADS if m.group(1) == "1" else PAIRS)[int(m.group(2))]
    lines = [f"({LETTERS[i]}) {t}" for i, t in enumerate(items)]
    return lines + TAILS.get(bid, [])


MATRIX_ITEMS = []  # (block id, letter, pali, english)


def build():
    out = []
    for bid, plines in pali_segments():
        elines = english_segment(bid)
        assert len(elines) == len(plines), (bid, plines, elines)
        for p, e in zip(plines, elines):
            for i, pl in enumerate(PALI_LETTERS):
                if p.startswith(pl + " "):
                    assert e.startswith(f"({LETTERS[i]}) "), (bid, p, e)
                    MATRIX_ITEMS.append((bid, LETTERS[i], p[len(pl) + 1:], e[4:]))
            assert ("[" in p) == ("[" in e), (bid, p, e)
        elines = elines[:-1] + [elines[-1] + f" ^{bid}"]
        out.append("\n".join(elines))
    return "\n\n".join(out) + "\n"


TEXT = build()

if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEXT, encoding="utf-8", newline="\n")
    print("wrote", OUT, "items", len(MATRIX_ITEMS))
