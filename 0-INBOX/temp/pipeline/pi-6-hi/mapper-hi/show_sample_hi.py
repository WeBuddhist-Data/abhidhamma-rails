"""Print the Pāli, the Hindi, the keywords and (if built) the mapped line of pi-6 segments.
usage: python -I -X utf8 show_sample_hi.py <file> <id> [<id> ...]"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import HERE, read_keywords, read_hindi, read_pali  # noqa: E402

f, ids = sys.argv[1], sys.argv[2:]
pi, hi, kw = read_pali(f), read_hindi(f), dict(read_keywords(f))
mp = {}
if (HERE / f"{f}.mapped.md").exists():
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        mp[line.split("] ", 1)[0][1:]] = line
for i in ids:
    print(f"=== {i}\n--- PI\n{pi.get(i)}\n--- HI\n{hi.get(i)}\n--- KW {kw.get(i)}\n--- MAP {mp.get(i)}\n")
