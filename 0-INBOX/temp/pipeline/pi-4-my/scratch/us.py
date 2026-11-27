"""us.py REGEX : unit pairs whose Pāli CONTAINS REGEX (uneven lines shown whole)."""
import sys, re, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent)); import units
rx = re.compile(sys.argv[1]); w = int(sys.argv[2]) if len(sys.argv) > 2 else 100000
for ch, i, s, t, ok in units.search(rx):
    print(f"{ch}:{i}{'' if ok else ' UNEVEN'}\n  P: {s[:w]}\n  M: {t[:w]}")
