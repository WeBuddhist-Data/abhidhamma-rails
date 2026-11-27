"""pi-6 Burmese rails, pi-1 … pi-5 identity: runs pi-6-my/harmonise_pi12345.py (read only, never edited) on a given
pi-6 Burmese folder: its source is read as text, the one line naming the zero-shot folder is replaced in memory by the
folder given here, and the code is executed (as build_rails.py runs the generators). Every Pāli sentence (and
heading) of pi-6 that also occurs in pi-1 … pi-5 must have exactly their FINAL rails Burmese (or a listed explained
difference). Model: pi-5-my/rails/pi1234_identity.py (read only).
usage: python3 -I -X utf8 pi12345_identity.py <pi-6 burmese split dir> [-q]   (exit 1 if any differs unexplained)"""
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / "harmonise_pi12345.py"
LINE = 'P4P, P4M = A / "pali/pi-6_split_chapters", A / "burmese/pi-6-burmese-plain-zeroshot_split_chapters"'
folder = pathlib.Path(sys.argv[1]).resolve()
src = SRC.read_text(encoding="utf-8")
if src.count(LINE) != 1:
    raise SystemExit("harmonise_pi12345.py: folder line not found once")
src = src.replace(LINE, f'P4P, P4M = A / "pali/pi-6_split_chapters", pathlib.Path({str(folder)!r})')
src = src.split('\nif __name__ == "__main__":\n')[0]
ns = {"__name__": "pi12345_identity", "__file__": str(SRC)}
exec(compile(src, str(SRC), "exec"), ns)
sys.exit(1 if ns["main"](sys.argv[2:]) else 0)
