"""Print the pi-1/3/4/5 Hindi values of given Pāli keywords (exact and NFC-normalised).

usage: python -I -X utf8 prior_15-4-7-11_hi.py kw [kw ...]
"""
import pathlib
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_sample_hi import prior  # noqa: E402

for kw in sys.argv[1:]:
    r = prior(kw) or prior(unicodedata.normalize("NFC", kw)) or prior(unicodedata.normalize("NFD", kw))
    print(kw, "::", "; ".join(f"pi{n}: " + " | ".join(f"{v}({c})" for v, c in cnt.most_common(4)) for n, cnt in r.items()))
