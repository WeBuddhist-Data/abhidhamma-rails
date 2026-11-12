"""Helper (read-only): print pi-1 Pāli line || pi-1 rails Hindi line for a chapter file, line range.

usage: python -I -X utf8 build_rails_16_pair.py <file.md> [start] [end]
"""
import pathlib
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PA = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
HI = ROOT / "AI_translation" / "hindi" / "pi-1-hindi-plain-rails_split_chapters"
f = sys.argv[1]
a = int(sys.argv[2]) if len(sys.argv) > 2 else 0
b = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 9
pl = [x for x in (PA / f).read_text(encoding="utf-8").splitlines() if x.strip()]
hl = [x for x in (HI / f).read_text(encoding="utf-8").splitlines() if x.strip()]
for i in range(a, min(b, len(pl))):
    print(f"{i}| {pl[i]}\n {hl[i]}")
