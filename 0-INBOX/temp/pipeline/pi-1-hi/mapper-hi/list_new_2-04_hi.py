"""List 2-04 keywords not covered by CH2 (helper; prints only)."""
import pathlib
import sys
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import CH2, ch2_value, read_keywords  # noqa: E402

PART = "2-04-cittuppadakandam"
miss = defaultdict(list)
for bid, kws in read_keywords(PART):
    for kw in kws:
        try:
            ch2_value(kw, kws)
        except KeyError:
            miss[kw].append(bid)
for kw, bids in sorted(miss.items()):
    print(kw, "|", len(bids), "|", " ".join(bids[:6]))
