"""G10a probe: print Pāli + Russian (+ keywords) of segments.  python -I -X utf8 -B probe_G10a_ru.py PART id [id ...]
PART may be the short form 10-01. id 'all' prints every segment (use with care)."""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi6_ru import read_keywords, read_pali, read_russian  # noqa: E402

part = sys.argv[1]
if not part.endswith("yamaka"):
    part += "-indriyayamaka"
pa, ru = read_pali(part), read_russian(part)
kws = dict(read_keywords(part))
ids = sys.argv[2:]
if ids == ["all"]:
    ids = list(kws)
for i in ids:
    print("=" * 30, i)
    print("KW:", ", ".join(kws.get(i, [])))
    print("PA:", pa.get(i, "<none>"))
    print("RU:", ru.get(i, "<none>"))
