"""pi-3 rails: every repeated Pāli sentence that align_check_my.py reports with differing Burmese in the RAILS text must
be one of the zero-shot's accepted differences, explained by the subject's number (pi-3-my/harmonise_align_kept.py,
read only, run here on the rails folder: its source is read as text and the line naming the zero-shot folder is
replaced in memory), and the set of differing sentences must be the zero-shot's (the rails introduce none, lose none
silently): compared on the «PĀLI:» lines of rails/align-zeroshot.txt and rails/align-rails.txt.
usage: python3 -I -X utf8 align_kept.py   (after regen_rails.sh step 4 wrote both align files; exit 1 if unexplained)"""
import contextlib
import io
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SRC = HERE.parent / "harmonise_align_kept.py"
LINE = 'MD = ROOT / "AI_translation/burmese/pi-3-burmese-plain-zeroshot_split_chapters"'
RL = ROOT / "AI_translation/burmese/pi-3-burmese-plain-rails_split_chapters"
src = SRC.read_text(encoding="utf-8")
if src.count(LINE) != 1:
    raise SystemExit("harmonise_align_kept.py: folder line not found once")
src = src.replace(LINE, f"MD = pathlib.Path({str(RL)!r})")
buf, code = io.StringIO(), 0
with contextlib.redirect_stdout(buf):
    try:
        exec(compile(src, str(SRC), "exec"), {"__name__": "align_kept_rails", "__file__": str(SRC)})
    except SystemExit as e:
        code = e.code or 0
out = buf.getvalue().strip().splitlines()


def diffs(name):
    return {l[len("PĀLI: "):] for l in (HERE / name).read_text(encoding="utf-8").splitlines() if l.startswith("PĀLI: ")}


r, z = diffs("align-rails.txt"), diffs("align-zeroshot.txt")
new, gone = sorted(r - z), sorted(z - r)
print(f"rails align differences: {len(r)} (zero-shot {len(z)}); new in the rails: {len(new)}; no longer differing: "
      f"{len(gone)}; harmonise_align_kept on the rails: {out[-1] if out else '?'}")
for s in new:
    print("  NEW:", s[:140])
for l in out:
    if l.startswith("NOT EXPLAINED"):
        print("  " + l)
sys.exit(1 if code or new else 0)
