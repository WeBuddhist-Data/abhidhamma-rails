"""For keywords, show per segment the Pāli words containing them and the mapped value.
usage: python -I -X utf8 ctx_pi2_ru.py PART kw1 kw2 ..."""
import collections
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from map_common_pi2_ru import HERE, read_pali  # noqa: E402

part, kws = sys.argv[1], sys.argv[2:]
pi = read_pali(part)
for line in (HERE / f"{part}.mapped.md").read_text(encoding="utf-8").splitlines():
    bid, rest = line.split("] ", 1)
    bid = bid[1:]
    for pair in rest.split(", "):
        k, v = pair.split("=", 1)
        if k in kws:
            words = collections.Counter(w for w in re.findall(r"[\wāīūṃṅñṭḍṇḷ]+", pi.get(bid, ""))
                                        if k.lower() in w.lower())
            print(f"{bid}\t{k}={v}\t{dict(words)}")
