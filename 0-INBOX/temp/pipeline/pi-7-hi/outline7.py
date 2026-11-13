"""Print headings of a pi-7 Pāli file with their NON-EMPTY line numbers (and the total).

usage: python -I -B -X utf8 outline7.py <file.md> [max_headings]
"""
import pathlib, sys

f = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters") / sys.argv[1]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 60
n, shown = 0, 0
for line in f.read_text(encoding="utf-8-sig").splitlines():
    if not line.strip():
        continue
    n += 1
    if line.startswith("#") and shown < mx:
        print(n, line[:110]); shown += 1
print("non-empty lines:", n)
