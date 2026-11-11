"""List unique keywords of part 5 with counts (helper)."""
import collections
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_hi import read_keywords  # noqa: E402

c = collections.Counter()
for bid, kws in read_keywords("5-atthakathakandam"):
    for k in kws:
        c[k] += 1
print(len(c))
print(" | ".join(f"{k}:{n}" for k, n in sorted(c.items(), key=lambda x: x[0].lower())))
