"""Extra checks for parts 2-03 and 2-04: real dash counts per line, '?' counts, CR, double blanks, banned strings.

usage: python -I -X utf8 verify_2-03_2-04.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
EN = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters"

for part in ("2-03-cittuppadakandam.md", "2-04-cittuppadakandam.md"):
    raw = (EN / part).read_bytes()
    t = raw.decode("utf-8")
    a = [l for l in (PALI / part).read_text(encoding="utf-8").splitlines() if l.strip()]
    b = [l for l in t.splitlines() if l.strip()]
    dash = [i for i, (x, y) in enumerate(zip(a, b)) if x.count("–") + x.count("—") != y.count("–") + y.count("—")]
    q = [i for i, (x, y) in enumerate(zip(a, b)) if x.count("?") != y.count("?")]
    probs = []
    if b"\r" in raw:
        probs.append("CR")
    if "\n\n\n" in t:
        probs.append("double blank")
    if raw.startswith(b"\xef\xbb\xbf"):
        probs.append("BOM")
    for bad in ("—", ":-", "outline", "Outline", "pe…", "  "):
        if bad in t:
            probs.append(f"contains {bad!r}")
    print(part, "lines", len(a), len(b), "dash mismatches", len(dash), dash[:5], "? mismatches", len(q), q[:5],
          "problems", probs or "none")
