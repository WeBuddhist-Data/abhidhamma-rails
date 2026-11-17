"""Print Pāli + Russian of segments. usage: python -I -X utf8 probe_pi2_ru.py PART id [id ...]"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi2_ru import read_pali, read_russian  # noqa: E402

part, ids = sys.argv[1], sys.argv[2:]
pi, ru = read_pali(part), read_russian(part)
for i in ids:
    print(f"=== {i} PALI\n{pi.get(i)}\n=== {i} RU\n{ru.get(i)}\n")
