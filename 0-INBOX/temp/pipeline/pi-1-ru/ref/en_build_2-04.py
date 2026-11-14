"""Build the English plain zero-shot of pi-1 part 2-04 (the twelve unwholesome minds; indeterminate results).

usage: python -I -X utf8 build_2-04.py
Shared formulas live in const_2_03_2_04.py; every repeat is generated from fixed constants.
"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from const_2_03_2_04 import (ELL, ARAM_FULL, ARAM_ABBR, ARAM_ABBR_TOUCH, ARAM_ABBR_ANY, PROMPTED,
                             ABBR_LIST, build_part)

PART = "2-04-cittuppadakandam.md"

HEAD = {
    "#### Dvādasa akusalāni": "#### The Twelve Unwholesome Minds",
    "#### Abyākatavipāko": "#### Indeterminate Results",
    "##### Kusalavipākapañcaviññāṇāni": "##### The Five Kinds of Consciousness Resulting from Wholesome Action",
    "##### Kusalavipākamanodhātu": "##### The Mind Element Resulting from Wholesome Action",
    "##### Kusalavipākamanoviññāṇadhātusomanassasahagatā":
        "##### The Mind-Consciousness Element Resulting from Wholesome Action, Accompanied by Joy",
    "##### Kusalavipākamanoviññāṇadhātuupekkhāsahagatā":
        "##### The Mind-Consciousness Element Resulting from Wholesome Action, Accompanied by Equanimity",
    "##### Aṭṭhamahāvipākā": "##### The Eight Great Results",
    "##### Rūpāvacaravipākā": "##### Results of the Fine-Material Sphere",
    "##### Arūpāvacaravipākā": "##### Results of the Immaterial Sphere",
}
CLOSE = {
    "Dvādasa akusalacittāni.": "The twelve unwholesome minds.",
    "Kusalavipākāni pañcaviññāṇāni.": "The five kinds of consciousness resulting from wholesome action.",
    "Kusalavipākā manodhātu.": "The mind element resulting from wholesome action.",
    "Kusalavipākā manoviññāṇadhātu somanassasahagatā.":
        "The mind-consciousness element resulting from wholesome action, accompanied by joy.",
    "Kusalavipākā upekkhāsahagatā manoviññāṇadhātu.":
        "The mind-consciousness element resulting from wholesome action, accompanied by equanimity.",
    "Aṭṭhamahāvipākā.": "The eight great results.",
    "Rūpāvacaravipākā.": "Results of the fine-material sphere.",
    "Arūpāvacaravipākā.": "Results of the immaterial sphere.",
}

# ---- unwholesome minds ---------------------------------------------------------------------------
UNW = "an unwholesome mind has arisen, "
JOY = "accompanied by joy"
EQU = "accompanied by equanimity"
SAD = "accompanied by sadness"
W_ASSOC = "associated with wrong view"
W_DISS = "dissociated from wrong view"


def U(acc, assoc, aram, prompted=False):
    return UNW + f"{acc} and {assoc}, " + (PROMPTED + ", " if prompted else "") + aram


# ---- results of the wholesome -------------------------------------------------------------------------
RES_KAMA = ", as a result of wholesome action of the sense sphere that has been done and accumulated, "
KNOW_A = "associated with knowledge"
KNOW_D = "dissociated from knowledge"
EIGHT = (ELL + " ").join(
    f"{acc} and {kn}" + (", " + PROMPTED if pr else "")
    for acc in (JOY, EQU) for kn in (KNOW_A, KNOW_D) for pr in (False, True))

OPEN = {
    "1-365": U(JOY, W_ASSOC, ARAM_FULL),
    "1-399": U(JOY, W_ASSOC, ARAM_ABBR, True),
    "1-400": U(JOY, W_DISS, ARAM_FULL),
    "1-402": U(JOY, W_DISS, ARAM_ABBR, True),
    "1-403": U(EQU, W_ASSOC, ARAM_FULL),
    "1-409": U(EQU, W_ASSOC, ARAM_ABBR, True),
    "1-410": U(EQU, W_DISS, ARAM_FULL),
    "1-412": U(EQU, W_DISS, ARAM_ABBR, True),
    "1-413": U(SAD, "associated with aversion", ARAM_FULL),
    "1-421": U(SAD, "associated with aversion", ARAM_ABBR, True),
    "1-422": U(EQU, "associated with doubt", ARAM_FULL),
    "1-427": U(EQU, "associated with restlessness", ARAM_ABBR_ANY),
    "1-431": RES_KAMA + f"eye-consciousness has arisen, {EQU}, with a visible form as its object",
    "1-443": (RES_KAMA + f"ear-consciousness has arisen, {EQU}, with a sound as its object{ELL} "
              f"nose-consciousness has arisen, {EQU}, with a smell as its object{ELL} "
              f"tongue-consciousness has arisen, {EQU}, with a taste as its object{ELL} "
              "body-consciousness has arisen, accompanied by happiness, with a touch as its object"),
    "1-455": RES_KAMA + f"the mind element has arisen, {EQU}, " + ARAM_ABBR_TOUCH,
    "1-469": RES_KAMA + f"the mind-consciousness element has arisen, {JOY}, " + ARAM_ABBR,
    "1-484": RES_KAMA + f"the mind-consciousness element has arisen, {EQU}, " + ARAM_ABBR,
    "1-498": RES_KAMA + f"the mind-consciousness element has arisen, {EIGHT}, " + ARAM_ABBR,
}

# ---- results of the fine-material and immaterial spheres (two sentences on one line) --------------------
FM_PATH = "one develops the path to rebirth in the fine-material sphere"
IM_PATH = "one develops the path to rebirth in the immaterial sphere"
EARTH = "using earth as the meditation device"
J1 = f"quite secluded from sensual pleasures{ELL} enters and dwells in the first absorption"
J5 = (f"with the stilling of applied thought and sustained thought{ELL} the second absorption{ELL} "
      f"the third absorption{ELL} the fourth absorption{ELL} the first absorption{ELL} "
      "enters and dwells in the fifth absorption")
J5_PLEASURE = f"with the abandoning of pleasure{ELL} enters and dwells in the fifth absorption"
J4_PLEASURE = f"with the abandoning of pleasure{ELL} enters and dwells in the fourth absorption"
WHOLESOME_END = f", at that time there is contact{ELL} there is non-distraction{ELL} these states are wholesome."
assert ABBR_LIST.startswith(WHOLESOME_END[2:-len("wholesome.")])
RESULT_END = f", at that time there is contact{ELL} there is non-distraction{ELL} these states are indeterminate."


def RES_OF(sphere):
    return f"As a result of that same wholesome action of the {sphere} that has been done and accumulated, when one, "


def FM(jh_kusala, jh_result):
    return ("What states are indeterminate? At a time when " + FM_PATH + " and " + jh_kusala + ", " + EARTH
            + WHOLESOME_END + " " + RES_OF("fine-material sphere") + jh_result + ", " + EARTH + RESULT_END)


SURMOUNT_FORM = ("by completely passing beyond perceptions of material form, by the disappearance of perceptions of "
                 "impact, by not attending to perceptions of diversity")
ARUPA = {
    1: SURMOUNT_FORM + ", accompanied by the perception of the base of infinite space",
    2: ("having completely passed beyond the base of infinite space, accompanied by the perception of the base "
        "of infinite consciousness"),
    3: ("having completely passed beyond the base of infinite consciousness, accompanied by the perception of "
        "the base of nothingness"),
    4: ("having completely passed beyond the base of nothingness, accompanied by the perception of the base of "
        "neither perception nor non-perception"),
}


def IM(n):
    jh = ARUPA[n] + ", " + J4_PLEASURE
    return ("What states are indeterminate? At a time when " + IM_PATH + " and " + jh + WHOLESOME_END + " "
            + RES_OF("immaterial sphere") + jh + RESULT_END)


MANUAL = {
    ("1-499", 0): FM(J1, J1),
    ("1-500", 0): FM(J5, J5_PLEASURE),
    ("1-501", 0): IM(1),
    ("1-502", 0): IM(2),
    ("1-503", 0): IM(3),
    ("1-504", 0): IM(4),
}

if __name__ == "__main__":
    build_part(PART, HEAD, CLOSE, OPEN, MANUAL)
