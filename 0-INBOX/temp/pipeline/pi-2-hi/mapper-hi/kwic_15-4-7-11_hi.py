"""Keyword-in-context for one segment's Hindi.  usage: python -I -X utf8 kwic_15-4-7-11_hi.py <chapter> <id> word [word ...]"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_hindi  # noqa: E402

ch, bid, words = sys.argv[1], sys.argv[2], sys.argv[3:]
t = read_hindi(ch)[bid]
for w in words:
    i, n = t.find(w), 0
    while i >= 0 and n < 4:
        print(f"[{w}] …{t[max(0, i - 70): i + len(w) + 50]}…")
        i, n = t.find(w, i + 1), n + 1
    if n == 0:
        print(f"[{w}] NOT FOUND")
