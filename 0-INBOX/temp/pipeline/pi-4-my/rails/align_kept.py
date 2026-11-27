"""pi-4 rails: the repeated Pāli sentences that align_check_my.py reports with differing Burmese in the RAILS text must
be exactly the zero-shot's accepted set (the pi-4 zero-shot has 0: «with differing Burmese: 0»), compared on the
«PĀLI:» lines of rails/align-zeroshot.txt and rails/align-rails.txt: the rails introduce none and lose none silently.
Model: pi-3-my/rails/align_kept.py (pi-4 has no harmonise_align_kept.py: no accepted difference to explain).
usage: python3 -I -X utf8 align_kept.py   (after regen_rails.sh step 4 wrote both align files; exit 1 on a new one)"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent


def diffs(name):
    t = (HERE / name).read_text(encoding="utf-8").splitlines()
    return t[0], {l[len("PĀLI: "):] for l in t if l.startswith("PĀLI: ")}


(hz, z), (hr, r) = diffs("align-zeroshot.txt"), diffs("align-rails.txt")
new, gone = sorted(r - z), sorted(z - r)
print(f"rails align differences: {len(r)} (zero-shot {len(z)}); new in the rails: {len(new)}; no longer differing: "
      f"{len(gone)}")
for s in new:
    print("  NEW:", s[:140])
ok = not new and "with differing Burmese: 0;" in hr and "with differing Burmese: 0;" in hz
sys.exit(0 if ok else 1)
