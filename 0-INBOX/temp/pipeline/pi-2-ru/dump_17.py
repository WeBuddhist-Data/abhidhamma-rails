"""Chapter-17 helper: dump aligned Pāli/Russian non-empty lines of one split file into a text file.
usage: python -I -X utf8 dump_17.py <book> <file.md> <out.txt> [first_line] [last_line]
"""
import os, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation"
PAIRS = {
    "1": ("pi-1_split_chapters", "pi-1-russian-plain-rails_split_chapters"),
    "2": ("pi-2_split_chapters", "pi-2-russian-plain-zeroshot_split_chapters"),
    "3": ("pi-3_split_chapters", "pi-3-russian-plain-rails_split_chapters"),
    "4": ("pi-4_split_chapters", "pi-4-russian-plain-rails_split_chapters"),
    "5": ("pi-5_split_chapters", "pi-5-russian-plain-rails_split_chapters"),
}
b, name, out = sys.argv[1], sys.argv[2], sys.argv[3]
a = int(sys.argv[4]) if len(sys.argv) > 4 else 1
z = int(sys.argv[5]) if len(sys.argv) > 5 else 10 ** 9
pd, rd = PAIRS[b]
pl = open(os.path.join(ROOT, "pali", pd, name), encoding="utf-8").read().split("\n")
rl = open(os.path.join(ROOT, "russian", rd, name), encoding="utf-8").read().split("\n")
with open(out, "w", encoding="utf-8") as f:
    for i, line in enumerate(pl):
        if a <= i + 1 <= z and line.strip():
            f.write(f"[{i+1}] PI: {line}\n[{i+1}] RU: {rl[i] if i < len(rl) else '?'}\n\n")
