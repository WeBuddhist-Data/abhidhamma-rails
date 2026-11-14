"""Probe for part 2-04: list keywords not covered by CH2 (with the segments they occur in)."""
import pathlib
import sys
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_ru import CH2, lc, read_keywords  # noqa: E402

PART = "2-04-cittuppadakandam"
miss = defaultdict(list)
for bid, kws in read_keywords(PART):
    for kw in kws:
        k = lc(kw)
        if k.startswith("samaye "):
            k = k[7:]
        if k not in CH2 and k != "dhamma":
            miss[kw].append(bid)
for kw, ids in miss.items():
    print(kw, "|", len(ids), "|", " ".join(ids[:12]))
