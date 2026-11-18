"""Review helper for 2-04: print Pāli + Vietnamese + keywords of given segment ids.
usage: python -I -X utf8 probe_2-04_vi.py ID [ID ...]"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_vi import read_keywords, read_pali, read_vietnamese  # noqa: E402

PART = "2-04-cittuppadakandam"
pi, vi = read_pali(PART), read_vietnamese(PART)
kw = dict(read_keywords(PART))
for bid in sys.argv[1:]:
    print("=" * 20, bid)
    print("PI:", pi.get(bid))
    print("VI:", vi.get(bid))
    print("KW:", ", ".join(kw.get(bid, [])))
