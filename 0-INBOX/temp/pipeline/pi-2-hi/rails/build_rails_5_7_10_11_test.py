"""Print the Pañhāpucchaka translator output for given chapter lines (for review).

usage: python -I -X utf8 build_rails_5_7_10_11_test.py <chapter.md> <form> <lineno> [<lineno> ...]
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_rails_5_7_10_11_common as C  # noqa: E402

name, form = sys.argv[1], sys.argv[2]
lines = (C.PALI / name).read_text(encoding="utf-8").splitlines()
for n in sys.argv[3:]:
    pl = lines[int(n) - 1]
    pl = C.re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", pl)
    print(f"== {n}")
    print(C.pq_line(pl, form))
print("UNKNOWN:", C.UNKNOWN)
