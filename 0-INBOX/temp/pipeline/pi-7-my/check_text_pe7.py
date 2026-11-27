"""Both-case wrapper for pi-3-mr/check_text.py, writing its folded Pāli copy into pi-7-my/chk-pe/ (not pi-6-mr/).

usage: python3 -I -X utf8 check_text_pe7.py <pali_file> <burmese_file> [...pairs]
Same as pi-6-mr/check_text_pe.py («…Pe…» folded to «…pe…» in a copy of the Pāli, then the unchanged
check_text.py), but the copy goes to pi-7-my/chk-pe/ and the folder is deleted afterwards.
"""
import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
CHECK = HERE.parent / "pi-3-mr/check_text.py"
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
shutil.rmtree(TMP)
sys.exit(r.returncode)
