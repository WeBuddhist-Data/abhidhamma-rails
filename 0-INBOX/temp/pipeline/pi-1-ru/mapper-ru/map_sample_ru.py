"""Build the SAMPLE Pāli->Russian keyword maps for pi-1: preamble, 1-matika, 2-01-cittuppadakandam.

usage: python -I -X utf8 map_sample_ru.py          (writes the three <part>.mapped.md and verifies them)

Resolution order per keyword: OVERRIDES[bid][kw]  ->  the part's table  ->  (2-01) ch2_value.
The tables live in map_common_ru.py (CORE, MATRIX, CH2); the overrides below are the per-segment
readings found when comparing each segment's Russian (see ru-map-conventions.md).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_ru import CH2, CORE, MATRIX, build_part, ch2_value, lc, verify  # noqa: E402

PARTS = ["preamble", "1-matika", "2-01-cittuppadakandam"]

OVERRIDES = {
    # ---- 1-matika: the same Pāli item read differently by its Russian
    "1-M1-4": {"upādāniyā": "служащий его объектом"},          # «…и служащие его объектом»
    "1-M1-16": {"ārammaṇā": "имеющий объектом",               # «имеющие объектом путь»
                "hetukā": "имеющий корнем"},                   # «имеющие корнем путь»
    "1-M2-2": {"hetukā": "имеющий корни"},                     # «имеющие корни / не имеющие корней»
    "1-M2-55": {"ārammaṇā": "имеющий объект"},                 # «имеющие объект»
    "1-M2-119": {"vuṭṭhāna": "избавление",                    # «избавлении от проступков»
                 "vuṭṭhānakusalatā": "умение разбираться в избавлении"},
    "1-M2-120": {"vuṭṭhāna": "выход",                          # «выходе из медитативных достижений»
                 "vuṭṭhānakusalatā": "умение разбираться в выходе"},
    # ---- 2-01: «Paṭhamaṃ / Tatiyaṃ / Pañcamaṃ / Sattamaṃ cittaṃ» is the only cittaṃ in these segments
    "1-145": {"cittaṃ": "вид ума"},
    "1-148": {"cittaṃ": "вид ума"},
    "1-155": {"cittaṃ": "вид ума"},
    "1-158": {"cittaṃ": "вид ума"},
}


def resolver_for(part):
    def resolve(bid, kw, kws):
        ov = OVERRIDES.get(bid, {})
        if kw in ov:
            return ov[kw]
        if part == "preamble":
            return CORE[lc(kw)]
        if part == "1-matika":
            return MATRIX[lc(kw)]
        return ch2_value(kw, kws, CH2)
    return resolve


if __name__ == "__main__":
    for p in PARTS:
        build_part(p, resolver_for(p))
        verify(p)
