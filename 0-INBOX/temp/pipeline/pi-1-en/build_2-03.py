"""Build the English plain zero-shot of pi-1 part 2-03 (the world-transcending wholesome mind).

usage: python -I -X utf8 build_2-03.py
Shared formulas live in const_2_03_2_04.py; every repeat is generated from fixed constants.
"""
import pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from const_2_03_2_04 import *  # noqa: F401,F403
from const_2_03_2_04 import ELL, DASH, N, G_ANNA, tr_string, build_part

PART = "2-03-cittuppadakandam.md"

HEAD = {
    "#### Lokuttarakusalaṃ": "#### The World-Transcending Wholesome Mind",
    "##### Suddhikapaṭipadā": "##### Plain Progress",
    "##### Suññataṃ": "##### Emptiness",
    "##### Suññatamūlakapaṭipadā": "##### Progress Rooted in Emptiness",
    "##### Appaṇihitaṃ": "##### The Desireless",
    "##### Appaṇihitamūlakapaṭipadā": "##### Progress Rooted in the Desireless",
    "##### Vīsati mahānayā": "##### The Twenty Great Methods",
    "##### Adhipati": "##### The Dominant Factors",
}
CLOSE = {
    "Suddhikapaṭipadā.": "Plain progress.",
    "Suññataṃ.": "Emptiness.",
    "Suññatamūlakapaṭipadā.": "Progress rooted in emptiness.",
    "Appaṇihitaṃ.": "The desireless.",
    "Appaṇihitamūlakapaṭipadā.": "Progress rooted in the desireless.",
    "Vīsati mahānayā.": "The twenty great methods.",
    "Adhipati.": "The dominant factors.",
    "Paṭhamo maggo.": "The first path.",
    "Dutiyo maggo.": "The second path.",
    "Tatiyo maggo.": "The third path.",
    "Catuttho maggo.": "The fourth path.",
    "Lokuttaraṃ cittaṃ.": "The world-transcending mind.",
}

# ---- clause pieces ---------------------------------------------------------------------------
LEADS = "which leads to liberation and leads away from accumulation"
DEV_JHANA = f"one develops world-transcending absorption, {LEADS}"
TWENTY_OBJ = [
    "a world-transcending path", "a world-transcending foundation of mindfulness",
    "a world-transcending right striving", "a world-transcending basis of spiritual power",
    "a world-transcending faculty", "a world-transcending power", "a world-transcending awakening factor",
    "a world-transcending truth", "world-transcending calm", "a world-transcending state",
    "a world-transcending aggregate", "a world-transcending sense base", "a world-transcending element",
    "a world-transcending nutriment", "world-transcending contact", "world-transcending feeling",
    "world-transcending perception", "world-transcending intention", "a world-transcending mind",
]
assert len(TWENTY_OBJ) == 19
DEV_TWENTY = ("one develops " + TWENTY_OBJ[0] + "".join(f"{ELL} develops {o}" for o in TWENTY_OBJ[1:])
              + f", {LEADS}")
STAGE = {
    1: "for the abandoning of wrong views, for reaching the first stage",
    2: "for the weakening of sensual lust and ill will, for reaching the second stage",
    3: "for the abandoning without remainder of sensual lust and ill will, for reaching the third stage",
    4: ("for the abandoning without remainder of lust for fine-material existence, lust for immaterial "
        "existence, conceit, restlessness and ignorance, for reaching the fourth stage"),
}
J1 = f"quite secluded from sensual pleasures{ELL} enters and dwells in the first absorption"
J5 = (f"with the stilling of applied thought and sustained thought{ELL} the second absorption{ELL} "
      f"the third absorption{ELL} the fourth absorption{ELL} the first absorption{ELL} "
      "enters and dwells in the fifth absorption")
PP = [
    "with painful progress and slow direct knowledge",
    "with painful progress and quick direct knowledge",
    "with pleasant progress and slow direct knowledge",
    "with pleasant progress and quick direct knowledge",
]
EMPTY = "which is empty"
DESIRELESS = "which is desireless"
ADHI = (ELL + " ").join(f"with {x} as the dominant factor" for x in ("desire", "energy", "mind", "inquiry"))


def CL(qual, jh=J1, stage=1, dev=DEV_JHANA):
    return f"{dev}, {STAGE[stage]}, and {jh}" + (", " + qual if qual else "")


def ALL4(suffix=""):
    return (ELL + " ").join(p + suffix for p in PP)


OPEN = {
    "1-277": CL(PP[0]),
    "1-339": CL(PP[1]),
    "1-340": CL(PP[2]),
    "1-341": CL(PP[3]),
    "1-342": CL(ALL4(), jh=J5),
    "1-343": CL(EMPTY),
    "1-344": CL(EMPTY, jh=J5),
    "1-345": CL(f"{PP[0]}, {EMPTY}"),
    "1-346": CL(f"{PP[1]}, {EMPTY}"),
    "1-347": CL(f"{PP[2]}, {EMPTY}"),
    "1-348": CL(f"{PP[3]}, {EMPTY}"),
    "1-349": CL(ALL4(", " + EMPTY), jh=J5),
    "1-350": CL(DESIRELESS),
    "1-351": CL(DESIRELESS, jh=J5),
    "1-352": CL(f"{PP[0]}, {DESIRELESS}"),
    "1-353": CL(f"{PP[1]}, {DESIRELESS}"),
    "1-354": CL(f"{PP[2]}, {DESIRELESS}"),
    "1-355": CL(f"{PP[3]}, {DESIRELESS}"),
    "1-356": CL(ALL4(", " + DESIRELESS), jh=J5),
    "1-357": CL(PP[0], dev=DEV_TWENTY),
    "1-358": CL(f"{PP[0]}, {ADHI}"),
    "1-359": CL(f"{PP[0]}, {ADHI}", jh=J5),
    "1-360": CL(f"{PP[0]}, {ADHI}", dev=DEV_TWENTY),
    "1-361": CL(PP[0], stage=2),
    "1-362": CL(PP[0], stage=3),
    "1-363": CL(PP[0], stage=4),
}

# ^1-364: the Pāli joins this answer to the elided rest with a comma, not a dash (translated as written)
_PANNA_PI = ("paññā pajānanā vicayo pavicayo dhammavicayo sallakkhaṇā upalakkhaṇā paccupalakkhaṇā paṇḍiccaṃ "
             "kosallaṃ nepuññaṃ vebhabyā cintā upaparikkhā bhūrī medhā pariṇāyikā vipassanā sampajaññaṃ patodo "
             "paññā paññindriyaṃ paññābalaṃ paññāsatthaṃ paññāpāsādo paññāāloko paññāobhāso paññāpajjoto "
             "paññāratanaṃ amoho dhammavicayo sammādiṭṭhi dhammavicayasambojjhaṅgo maggaṅgaṃ maggapariyāpannaṃ")
_X = N["aññindriyaṃ"]
MANUAL = {
    ("1-364", 0): (f"What is {_X} at that time? Whatever, {G_ANNA}, is {tr_string(_PANNA_PI)}, "
                   f"this is {_X} at that time{ELL} there is non-distraction{ELL} or whatever other dependently "
                   f"arisen immaterial states there are at that time {DASH} these states are wholesome."),
}

if __name__ == "__main__":
    build_part(PART, HEAD, CLOSE, OPEN, MANUAL)
