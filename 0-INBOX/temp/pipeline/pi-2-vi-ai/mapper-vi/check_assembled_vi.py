"""Check the assembled pi-2 Vietnamese map against the Pāli keyword file: same ids, same keywords in order.
usage: python -I -X utf8 check_assembled_vi.py"""
import pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
P = ROOT / "AI_translation/pali/pi-2-keywords-by-reference-pali-plain.md"
V = ROOT / "AI_translation/vietnamese/pi-2-keywords-by-reference-pali-vietnamese-plain.md"
a = [l.split("] ", 1) for l in P.read_text(encoding="utf-8").splitlines() if l.strip()]
b = [l.split("] ", 1) for l in V.read_text(encoding="utf-8").splitlines() if l.strip()]
assert [x[0] for x in a] == [x[0] for x in b], "ids differ"
bad = [x[0] for x, y in zip(a, b) if [k.strip() for k in x[1].split(", ")] != [k.split("=", 1)[0] for k in y[1].split(", ")]]
empty = [y[0] for y in b if any(not k.split("=", 1)[1].strip() for k in y[1].split(", "))]
print("lines", len(a), "bad", bad, "empty values", empty)
