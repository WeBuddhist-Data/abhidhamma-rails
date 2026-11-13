"""Test present(value, text): python -I -B -X utf8 pres_2-02_2-08_hi.py "value" "text" …(pairs)"""
import sys, pathlib
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import present  # noqa
a = sys.argv[1:]
for v, t in zip(a[::2], a[1::2]):
    print(present(v, t), "|", v, "|", t)
