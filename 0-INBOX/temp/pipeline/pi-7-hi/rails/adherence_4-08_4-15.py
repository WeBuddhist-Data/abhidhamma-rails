"""Termbase adherence for 4-08 .. 4-15 only: copies the eight files to a scratch folder next to this script,
runs hindi_termbase_adherence.py on it, then removes the folder.
usage: python -I -B -X utf8 adherence_4-08_4-15.py
"""
import pathlib, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
HI = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-rails_split_chapters"
TMP = pathlib.Path(__file__).resolve().parent / "adh-4-08_4-15"
FILES = ["4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md", "4-10-dukatika-sarammanaduka.md",
         "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md", "4-13-dukatika-dassanenapahatabbaduka.md",
         "4-14-dukatika-saranaduka.md", "4-15-tikaduka-hetuduka.md"]
TMP.mkdir(exist_ok=True)
try:
    for f in FILES:
        shutil.copy(HI / f, TMP / f)
    r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(ROOT / "0-INBOX/temp/pipeline/hindi_termbase_adherence.py"),
                        str(ROOT / "AI_translation/pali/pi-7-keywords-by-reference-pali-plain.md"),
                        str(ROOT / "AI_translation/hindi/pi-7-pali-hindi-termbase-plain.md"), str(TMP)],
                       capture_output=True, text=True, encoding="utf-8")
    print(r.stdout, r.stderr)
finally:
    shutil.rmtree(TMP)
