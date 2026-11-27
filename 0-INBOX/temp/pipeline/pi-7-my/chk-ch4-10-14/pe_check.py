"""The text check for 4-10 … 4-14: the Pāli «…Pe…»-folded into pi-7-my/chk-pe/ch4-10-14/ (this group's own folder),
then the unchanged pi-3-mr/check_text.py; the folder is deleted afterwards (chk-pe/ only if it is then empty)."""
import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parents[1]
ROOT = HERE.parents[3]
PALI = ROOT / "AI_translation/pali/pi-7_split_chapters"
OUT = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
NAMES = sys.argv[1:] or ["4-10-dukatika-sarammanaduka.md", "4-11-dukatika-upadanaduka.md",
                         "4-12-dukatika-kilesaduka.md", "4-13-dukatika-dassanenapahatabbaduka.md",
                         "4-14-dukatika-saranaduka.md"]
tmp = HERE / "chk-pe" / "ch4-10-14"
tmp.mkdir(parents=True, exist_ok=True)
rc = 0
for n in NAMES:
    folded = tmp / n
    folded.write_text((PALI / n).read_text(encoding="utf-8-sig").replace("…Pe…", "…pe…"), encoding="utf-8")
    r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE.parent / "pi-3-mr/check_text.py"), str(folded),
                        str(OUT / n)])
    rc |= r.returncode
shutil.rmtree(tmp)
try:
    (HERE / "chk-pe").rmdir()
except OSError:
    pass
sys.exit(rc)
