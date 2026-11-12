"""Quick presence test: python -I -X utf8 ptest_10_12_13_14_hi.py <chapter> <bid> <value> [<value> ...]"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import present, read_hindi  # noqa

ch, bid = sys.argv[1], sys.argv[2]
t = read_hindi(ch)[bid]
for v in sys.argv[3:]:
    print(present(v, t), v)
