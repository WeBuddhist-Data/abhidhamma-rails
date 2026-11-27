"""pi-5 rails: runs pi-5-my/harmonise_align_explained.py (read only) on the RAILS align outputs (rails/align-rails.txt,
rails/align-hidden-rails.txt) instead of pi-5-my/align-after.txt / align-hidden-after.txt: the two file names are
replaced in memory. Every difference left must be one the zero-shot harmonise explained (its EXPLAINED tables, 1:426);
none new. Model: pi-4-my/rails/align_kept.py.
usage: python3 -I -X utf8 align_explained.py   (after regen_rails.sh step 4 wrote both align files; exit 1 on a new one)"""
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / "harmonise_align_explained.py"
src = SRC.read_text(encoding="utf-8")
for old, new in (('(HERE / "align-after.txt")', f'(pathlib.Path({str(HERE / "align-rails.txt")!r}))'),
                 ('(HERE / "align-hidden-after.txt")', f'(pathlib.Path({str(HERE / "align-hidden-rails.txt")!r}))')):
    if src.count(old) != 1:
        raise SystemExit(f"harmonise_align_explained.py: {old} not found once")
    src = src.replace(old, new)
src = src.split('\nif __name__ == "__main__":\n')[0]
ns = {"__name__": "align_explained", "__file__": str(SRC)}
exec(compile(src, str(SRC), "exec"), ns)
sys.exit(ns["main"]())
