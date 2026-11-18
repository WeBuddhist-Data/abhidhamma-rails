"""Helper for part 2-05: print Pāli / Vietnamese pairs of finished parts.
usage: python -I -X utf8 show_2-05_vi.py <part.md> <id> [<id> ...]   (ids without caret; 'all' prints all)
"""
import importlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
B = importlib.import_module("build_2-01_2-02_vi")

part = sys.argv[1]
ids = sys.argv[2:]
ps = B.segments((B.PALI_DIR / part).read_text(encoding="utf-8"))
vs = B.segments((B.OUT_DIR / part).read_text(encoding="utf-8"))
for (b, pl), (b2, vl) in zip(ps, vs):
    if "all" in ids or b in ids:
        print("=====", b)
        for p, v in zip(pl, vl):
            print("P:", p)
            print("V:", v)
