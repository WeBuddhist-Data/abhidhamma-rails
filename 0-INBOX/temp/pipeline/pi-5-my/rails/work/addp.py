"""work helper (authoring only): append layer patches to my_formulas_rails.py from a spec file
(lines «file<TAB>old<TAB>new<TAB>reason»; «#» comments and «== title» section lines allowed). The count of each patch
is the number of occurrences of «old» in the generator source AFTER the patches already in the layer (and the earlier
spec lines) are applied, so the stated counts are exact; a zero count is reported and the line skipped.
usage: addp.py <spec.tsv>"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parents[1]
GEN = HERE.parent
spec = importlib.util.spec_from_file_location("L", HERE / "my_formulas_rails.py")
L = importlib.util.module_from_spec(spec)
spec.loader.exec_module(L)
cur = {}


def src(f):
    if f not in cur:
        s = (GEN / f"{f}.py").read_text(encoding="utf-8")
        for old, new, _, _ in L.PATCHES.get(f, []):
            s = s.replace(old, new)
        cur[f] = s
    return cur[f]


out, bad = [], 0
for line in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    if line.startswith("== "):
        out.append(f"\n# {'-' * 102} {line[3:]}")
        continue
    f, old, new, reason = line.split("\t")
    old, new = old.replace("\\n", "\n"), new.replace("\\n", "\n")
    n = src(f).count(old)
    if n == 0:
        print(f"ZERO {f}: {old[:80]}")
        bad += 1
        continue
    cur[f] = cur[f].replace(old, new)
    out.append(f"p({f!r}, {old!r}, {new!r}, {n},\n  {reason!r})")
    print(f"{n:3d} {f}: {old[:60]} -> {new[:60]}")
with open(HERE / "my_formulas_rails.py", "a", encoding="utf-8") as fh:
    fh.write("\n" + "\n".join(out) + "\n")
print(f"appended {len(out)} lines; {bad} zero")
