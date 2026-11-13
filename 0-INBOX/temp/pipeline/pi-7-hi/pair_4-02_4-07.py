"""Print Pāli/Hindi non-empty lines side by side.
usage: pair_4-02_4-07.py <file> <first> <last>        (1-based non-empty line range)
       pair_4-02_4-07.py <file> --grep <regex>         (lines whose Pāli matches)
"""
import pathlib, re, sys

R = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
f = sys.argv[1]
p = [l for l in (R / "pali" / "pi-7_split_chapters" / f).read_text(encoding="utf-8").splitlines() if l.strip()]
h = [l for l in (R / "hindi" / "pi-7-hindi-plain-zeroshot_split_chapters" / f).read_text(encoding="utf-8").splitlines() if l.strip()]
if sys.argv[2] == "--grep":
    idx = [i for i, l in enumerate(p) if re.search(sys.argv[3], l)]
else:
    idx = range(int(sys.argv[2]) - 1, min(int(sys.argv[3]), len(p)))
seen = set()
for i in idx:
    key = re.sub(r"\^\S+$", "", p[i])
    if "--uniq" in sys.argv and key in seen:
        continue
    seen.add(key)
    print(f"P{i+1}: {p[i]}")
    print(f"H{i+1}: {h[i]}")
