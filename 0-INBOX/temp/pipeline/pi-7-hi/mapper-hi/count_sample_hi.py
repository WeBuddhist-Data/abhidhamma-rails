"""Helper for the pi-7 sample: count literal Hindi strings across the whole pi-7 Hindi translation.
usage: python -I -B -X utf8 count_sample_hi.py "string1" "string2" ...
"""
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
HI = ROOT / "AI_translation" / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters"

texts = {p.stem: p.read_text(encoding="utf-8") for p in sorted(HI.glob("*.md"))}
for s in sys.argv[1:]:
    tot = sum(t.count(s) for t in texts.values())
    files = [f for f, t in texts.items() if s in t]
    print(f"{tot:6} {s} | {', '.join(files[:6])}{' …' if len(files) > 6 else ''}")
