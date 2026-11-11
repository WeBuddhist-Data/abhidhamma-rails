"""Look up how Pāli keywords were mapped in earlier Hindi maps (pi-3/4/5, pi-1 sample maps).

usage: python -I -X utf8 grep_3-01_3-02_hi.py REGEX [REGEX ...]
Writes the hits to grep_3-01_3-02_hi.out.txt (keyword pairs whose Pāli side matches REGEX, with counts).
"""
import collections
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FILES = [ROOT / "AI_translation" / "hindi" / f"pi-{n}-keywords-by-reference-pali-hindi-plain.md" for n in (3, 4, 5)]
FILES += sorted(HERE.glob("*.mapped.md"))

out = []
for rx in sys.argv[1:]:
    pat = re.compile(rx)
    for f in FILES:
        c = collections.Counter()
        for line in f.read_text(encoding="utf-8").splitlines():
            if "] " not in line:
                continue
            for pair in line.split("] ", 1)[1].split(", "):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    if pat.fullmatch(k.strip()):
                        c[(k, v)] += 1
        if c:
            out.append(f"== {rx}  [{f.name}]")
            for (k, v), n in c.most_common(12):
                out.append(f"   {n:4d}  {k} = {v}")
(HERE / "grep_3-01_3-02_hi.out.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
print(len(out), "lines")
