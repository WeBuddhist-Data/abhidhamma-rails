"""Extra checks for parts 2-05 and 3-01 (real en/em dash counts, '?' counts, banned strings, layout).

usage: python -I -X utf8 check_2-05_3-01.py
(dashcheck.py in this folder counts '?' characters: its dash literals were saved as '?'.)
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[4]
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
ENG = ROOT / "AI_translation" / "english" / "pi-1-english-plain-zeroshot_split_chapters"
bad = 0
for part in ("2-05-cittuppadakandam.md", "3-01-rupakandam.md"):
    raw = (ENG / part).read_bytes()
    text = raw.decode("utf-8")
    p = [l for l in (PALI / part).read_text(encoding="utf-8").splitlines() if l.strip()]
    e = [l for l in text.splitlines() if l.strip()]
    errs = []
    if len(p) != len(e):
        errs.append(f"line count {len(p)} vs {len(e)}")
    for i, (a, b) in enumerate(zip(p, e)):
        if a.count("–") + a.count("—") != b.count("–") + b.count("—"):
            errs.append(f"dash mismatch line {i}")
        if a.count("—") != b.count("—"):
            errs.append(f"em dash mismatch line {i}")
        if a.count("?") != b.count("?"):
            errs.append(f"'?' mismatch line {i}")
        if a.count("…pe…") != b.count("…"):
            errs.append(f"ellipsis mismatch line {i}: {a.count('…pe…')} vs {b.count('…')}")
        if a.startswith("#") != b.startswith("#") or (a.startswith("#") and a.split()[0] != b.split()[0]):
            errs.append(f"heading level line {i}")
    for bad_s in (":-", "outline", "Outline", "\r", "\n\n\n", "…pe…", "Dhamma "):
        if bad_s in text:
            errs.append(f"contains {bad_s!r}")
    if raw.startswith(b"\xef\xbb\xbf"):
        errs.append("BOM")
    if not text.endswith("\n") or text.endswith("\n\n"):
        errs.append("file end")
    print(part, "OK" if not errs else errs[:10])
    bad += bool(errs)
raise SystemExit(1 if bad else 0)
