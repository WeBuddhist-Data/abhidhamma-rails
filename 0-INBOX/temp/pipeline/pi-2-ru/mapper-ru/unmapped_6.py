"""List chapter-6 keywords and how the inherited table resolves them (before map_6_ru.py additions).
usage: python -I -X utf8 unmapped_6.py [--all]   (default: only unresolved keywords, one per line)"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import map_4_5_ru as M45  # noqa: E402
from map_common_pi2_ru import read_keywords, value  # noqa: E402

seen = {}
for bid, kws in read_keywords("6-paticcasamuppadavibhango"):
    for k in kws:
        if k in seen:
            continue
        try:
            seen[k] = value(k, kws, M45.T)
        except KeyError:
            seen[k] = None
for k, v in seen.items():
    if v is None:
        print(k)
    elif "--all" in sys.argv:
        print(f"{k}\t{v}")
