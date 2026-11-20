"""Review helper: values the approved pi-1 Vietnamese map gives a keyword, and the pi-1 table value.
usage: python -I -X utf8 pi1_lookup_vi.py kw [kw ...]"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import pi1_map_values, pi1_value  # noqa: E402

for kw in sys.argv[1:]:
    try:
        t = pi1_value(kw, [kw])
    except KeyError:
        t = "-"
    print(f"{kw}: table={t} | map={dict(pi1_map_values(kw).most_common(6))}")
