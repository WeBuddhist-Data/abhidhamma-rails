"""Print the first approved pi-N map line (all pairs) that has the given keyword.
usage: python -I -X utf8 pi1_line_6.py [--book pi-1] [--n 1] kw [kw ...]"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
args = sys.argv[1:]
book, n = "pi-1", 1
while args and args[0].startswith("--"):
    if args[0] == "--book":
        book, args = args[1], args[2:]
    elif args[0] == "--n":
        n, args = int(args[1]), args[2:]
lines = (ROOT / "AI_translation" / "russian" / f"{book}-keywords-by-reference-pali-russian-plain.md").read_text(
    encoding="utf-8").splitlines()
for kw in args:
    hits = [l for l in lines if f", {kw}=" in l or f"] {kw}=" in l][:n]
    print(f"=== {kw}: {len(hits)} shown")
    for h in hits:
        print(" | ".join(h.split(", ")))
