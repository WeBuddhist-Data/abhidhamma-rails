"""Key-word-in-context for a segment's Hindi (ch12 mapper helper).

usage: python -I -X utf8 kwic_12_hi.py <chapter> <bid> <hindi-fragment> [<hindi-fragment> ...]
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_hindi  # noqa

ch, bid = sys.argv[1], sys.argv[2]
t = read_hindi(ch)[bid]
for frag in sys.argv[3:]:
    i, n = t.find(frag), 0
    while i >= 0 and n < 2:
        print(f"[{frag}] …{t[max(0, i - 80): i + len(frag) + 80]}…")
        i, n = t.find(frag, i + 1), n + 1
    if n == 0:
        print(f"[{frag}] NOT FOUND")
