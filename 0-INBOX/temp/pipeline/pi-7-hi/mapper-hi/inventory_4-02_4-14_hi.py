"""Helper: distinct keyword -> value pairs (with counts) of mapped files, for reading by eye.
usage: python -I -B -X utf8 inventory_4-02_4-14_hi.py <file> [<file> ...]
"""
import collections, pathlib, sys
sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
inv = collections.defaultdict(collections.Counter)
for f in sys.argv[1:]:
    for line in (HERE / f"{f}.mapped.md").read_text(encoding="utf-8").splitlines():
        _, _, rest = line.partition("] ")
        if rest:
            for pair in rest.split(", "):
                k, v = pair.split("=", 1)
                inv[k[:1].lower() + k[1:]][v] += 1
for k in sorted(inv):
    print(k, "=", " | ".join(f"{v} ({c})" for v, c in inv[k].most_common()))
