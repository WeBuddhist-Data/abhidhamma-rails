"""Print the pi-1..5 Hindi map values of the given Pāli keywords.  usage: python -I -X utf8 prior_3_hi.py kw ..."""
import pathlib
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_sample_hi import prior  # noqa: E402

for k in sys.argv[1:]:
    print(k, {n: dict(c.most_common(3)) for n, c in prior(k).items()})
