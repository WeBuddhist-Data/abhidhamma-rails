"""Probe 2-02-cittuppadakandam: keywords not covered by CH2 (count, segments)."""
import pathlib
import sys
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import read_keywords, ch2_value  # noqa: E402

PART = "2-02-cittuppadakandam"
miss = defaultdict(list)
allk = defaultdict(int)
for bid, kws in read_keywords(PART):
    for kw in kws:
        allk[kw] += 1
        try:
            ch2_value(kw, kws)
        except KeyError:
            miss[kw].append(bid)
for kw, bids in sorted(miss.items(), key=lambda x: -len(x[1])):
    print(f"{kw}\t{len(bids)}\t{' '.join(bids[:6])}")
print("unique", len(allk), "uncovered", len(miss))
