"""Outline: id, number of keywords, first chars of Pāli. usage: outline_1-03_2-01_hi.py <file> [width]"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import read_keywords, read_pali

f = sys.argv[1]
w = int(sys.argv[2]) if len(sys.argv) > 2 else 70
pa = read_pali(f)
for bid, kws in read_keywords(f):
    print(bid, len(kws), (pa.get(bid) or "-").replace("\n", " | ")[:w])
