"""User decision 2026-11-17: sati = «sự tỉnh thức» (plain), not «chánh niệm".
Rewrites the two builders; idempotent."""
import pathlib, sys

HERE = pathlib.Path(__file__).parent
RULES = [
    ("chánh niệm đúng đắn", "tỉnh thức đúng đắn"),
    ("năng lực chánh niệm", "năng lực tỉnh thức"),
    ("sức mạnh chánh niệm", "sức mạnh tỉnh thức"),
    ("sự mất chánh niệm", "sự mất tỉnh thức"),
    ("chánh niệm", "sự tỉnh thức"),
]
for name in ("build_ch2_01_sample_vi.py", "build_matika_vi.py"):
    p = HERE / name
    t = p.read_text(encoding="utf-8")
    for old, new in RULES:
        n = t.count(old)
        if n:
            print(f"{name}: {old!r} -> {new!r} x{n}")
        t = t.replace(old, new)
    p.write_text(t, encoding="utf-8", newline="\n")
    assert "chánh niệm" not in t
print("done")
