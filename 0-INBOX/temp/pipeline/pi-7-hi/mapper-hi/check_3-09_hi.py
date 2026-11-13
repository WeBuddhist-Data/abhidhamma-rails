"""The brief's structural verifier for 3-09-mahantaraduka (same logic as the one-liner in hi-mapper-brief.md)."""
import pathlib

d = pathlib.Path(__file__).resolve().parent
ch = "3-09-mahantaraduka"
a = [l.split("] ", 1) for l in (d / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines()]
b = [l.split("] ", 1) for l in (d / f"{ch}.mapped.md").read_text(encoding="utf-8").splitlines()]
assert [x[0] for x in a] == [x[0] for x in b]
bad = [i for i, (x, y) in enumerate(zip(a, b))
       if len(x) > 1 and [k.strip() for k in x[1].split(", ")] != [k.split("=", 1)[0] for k in y[1].split(", ")]]
print(ch, "lines", len(a), "bad", bad)
