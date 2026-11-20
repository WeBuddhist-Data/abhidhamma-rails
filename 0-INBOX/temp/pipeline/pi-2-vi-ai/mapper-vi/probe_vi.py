"""Review helper: print the Pāli, Vietnamese and keywords of segments.
usage: python -I -X utf8 probe_vi.py PART id [id ...]   (add -k to skip the keywords, -p to skip the Pāli)"""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import read_keywords, read_pali, read_vietnamese  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("-")]
part, ids = args[0], args[1:]
pi, vi, kw = read_pali(part), read_vietnamese(part), dict(read_keywords(part))
for i in ids:
    print(f"=== {i}")
    if "-p" not in sys.argv:
        print("PI:", pi.get(i))
    print("VI:", vi.get(i))
    if "-k" not in sys.argv:
        print("KW:", ", ".join(kw.get(i, [])))
