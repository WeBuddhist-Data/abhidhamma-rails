"""Show Pāli / Hindi / keywords (and current mapping) for segments.
usage: python -I -B -X utf8 show_5-05_5-20_hi.py <file> <id> [<id> …]
"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_hindi, read_pali

f = sys.argv[1]
hi, pa = read_hindi(f), read_pali(f)
kw = dict(read_keywords(f))
for bid in sys.argv[2:]:
    print("==", bid)
    print("PA:", pa.get(bid))
    print("HI:", hi.get(bid))
    print("KW:", ", ".join(kw.get(bid, [])))
