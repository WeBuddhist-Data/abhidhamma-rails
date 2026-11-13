"""Dry run of build_rails_sample on any Pāli file (nothing is written): counts lines with no formula and prints
the first failures, plus the Hindi of lines whose block ID is listed (to read later frames).

usage: python -I -X utf8 coverage_sample.py <pali_file> [from_line] [to_line] [--show id,id,...]
"""
import sys, re, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import build_rails_sample as S

args = [a for a in sys.argv[1:] if not a.startswith("--")]
show = set()
if "--show" in sys.argv:
    show = set(sys.argv[sys.argv.index("--show") + 1].split(","))
    args = [a for a in args if a not in sys.argv[sys.argv.index("--show") + 1:sys.argv.index("--show") + 2]]
lines = pathlib.Path(args[0]).read_text(encoding="utf-8").splitlines()
a = int(args[1]) - 1 if len(args) > 1 else 0
b = int(args[2]) if len(args) > 2 else len(lines)
fails, n, buf = [], 0, []
for i in range(a, b):
    line = lines[i]
    if not line.strip():
        continue
    n += 1
    try:
        hi = S.translate_line(line)
    except Exception as e:  # noqa
        fails.append((i + 1, str(e)[:160]))
        hi = "!!"
    buf.append((line, hi))
    m = re.search(r"\^([0-9-]+)\s*$", line)
    if m:
        if m.group(1) in show:
            for p, h in buf:
                print("P:", p)
                print("H:", h)
            print()
        buf = []
print(f"{n} lines, {len(fails)} without a formula")
for f in fails[:25]:
    print("  line", f[0], f[1])
