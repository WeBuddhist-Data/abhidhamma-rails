"""G9 probe: print the Pāli, the Russian and the keywords of the given segments.

usage: python -I -X utf8 -B probe_G9_ru.py PART id [id ...]
"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi6_ru import read_keywords, read_pali, read_russian  # noqa: E402

if __name__ == "__main__":
    part, ids = sys.argv[1], sys.argv[2:]
    pa, ru, kw = read_pali(part), read_russian(part), dict(read_keywords(part))
    for i in ids:
        print("=" * 20, i)
        print("KW:", ", ".join(kw.get(i, [])))
        print("PA:", pa.get(i, "").strip())
        print("RU:", ru.get(i, "").strip())
