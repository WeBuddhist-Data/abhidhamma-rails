"""Helper for build_4-01_ru.py: count the words of the long Pāli synonym strings of 4-01.
usage: python -I -X utf8 helper_4-01_count.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[4]
P = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters" / "4-01-nikkhepakandam.md"
t = P.read_text(encoding="utf-8")
line = [l for l in t.splitlines() if l.endswith("^1-1065")][0]
body = re.sub(r"\[[^\]]*\]", "", line)
body = body.split("Yo ", 1)[1].split(" –", 1)[0]
w = body.split()
print(len(w))
for i, x in enumerate(w, 1):
    print(i, x)
