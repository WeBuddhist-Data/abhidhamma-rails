"""Helper for build_4-01_hi.py: align the Pāli lobha string (^1-1141) with the Hindi LOBHA list."""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
src = (HERE.parents[3] / "AI_translation" / "pali" / "pi-1_split_chapters" / "4-01-nikkhepakandam.md").read_text(encoding="utf-8")
line = [l for l in src.splitlines() if l.endswith("^1-1141")][0]
words = line.split("? Yo ", 1)[1].split(" – ", 1)[0].split()
print(len(words))
try:
    import build_4_01 as B  # noqa
except ImportError:
    pass
import importlib.util
spec = importlib.util.spec_from_file_location("b", HERE / "build_4-01_hi.py")
txt = (HERE / "build_4-01_hi.py").read_text(encoding="utf-8")
start = txt.index("LOBHA = [")
end = txt.index("]\nassert len(LOBHA)")
hi = eval(txt[start + len("LOBHA = "):end + 1])
for i in range(max(len(words), len(hi))):
    print(i, words[i] if i < len(words) else "-", "=", hi[i] if i < len(hi) else "-")
