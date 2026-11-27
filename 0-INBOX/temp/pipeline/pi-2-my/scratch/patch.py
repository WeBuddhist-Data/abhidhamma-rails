"""patch helper: python3 patch.py FILE  (reads REPL list from stdin as python literal: [(old, new, count), ...])"""
import pathlib, sys, ast
p = pathlib.Path(sys.argv[1]); s = p.read_text(encoding="utf-8")
for old, new, n in ast.literal_eval(sys.stdin.read()):
    c = s.count(old)
    if c != n:
        raise SystemExit(f"{p.name}: {c}x (expected {n}): {old[:120]!r}")
    s = s.replace(old, new)
p.write_text(s, encoding="utf-8")
print("patched", p.name)
