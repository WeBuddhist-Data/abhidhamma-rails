"""(copy of pi-4-my/rails/check_text_pe_rails.py, unchanged) The pi-6-mr/check_text_pe.py wrapper with its «…Pe…»-folded Pāli copies written inside rails/chk-pe/ (not into
pi-6-mr/, so the rails run writes only in its own folder); otherwise identical: the copy folds «…Pe…» to «…pe…»
and the unchanged pi-3-mr/check_text.py runs on the copy and the Burmese file. regen_rails.sh deletes the copies.
usage: python3 -I -X utf8 check_text_pe_rails.py <pali_file> <burmese_file> [...pairs]"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
CHECK = HERE.parents[1] / "pi-3-mr/check_text.py"
TMP = HERE / "chk-pe"
TMP.mkdir(exist_ok=True)
args = sys.argv[1:]
call = []
for src, tgt in zip(args[::2], args[1::2]):
    src = pathlib.Path(src)
    folded = TMP / src.name
    folded.write_text(src.read_text(encoding="utf-8-sig").replace("…Pe…", "…pe…"), encoding="utf-8")
    call += [str(folded), tgt]
r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(CHECK)] + call)
sys.exit(r.returncode)
