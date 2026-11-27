"""Scratch A4: per line, Pāli sentence marks (. ? outside brackets) vs Burmese «။»; Pāli commas vs Burmese «၊» (diff)."""
import pathlib, re, sys, collections
HERE = pathlib.Path(__file__).resolve().parents[1]; ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"
MD = HERE / "harmonise-backup/chapters" if "--bk" in sys.argv else ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
def pm(x):
    x = ID.sub("", x); x = re.sub(r"\[[^\]]*\]", "", x)
    x = x.replace("…pe…", "…").replace("…Pe…", "…")
    return len(re.findall(r"[.?]", x))
def bm(y):
    y = ID.sub("", y); y = re.sub(r"\[[^\]]*\]", "", y)
    return y.count("။")
for p in sorted(PD.glob("*.md")):
    A = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(A, B), 1):
        if x.startswith("#"): continue
        a, b = pm(x), bm(y)
        if a != b:
            print(p.name[:5], i, a, b, "|", x[:170], "\n      |", y[:200])
