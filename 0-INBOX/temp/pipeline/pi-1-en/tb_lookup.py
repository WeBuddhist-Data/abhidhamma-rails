"""Look up headwords in the English termbases pi-3..pi-6.

usage: python -I -X utf8 tb_lookup.py <patterns_file> [max_per_pattern]
patterns_file: one regex per line, matched against the headword (start of line up to ':').
"""
import re, sys, pathlib

root = pathlib.Path(__file__).resolve().parents[4] / "AI_translation" / "english"
files = [root / f"pi-{n}-pali-english-termbase-plain.md" for n in (3, 4, 5, 6)]
entries = []
for f in files:
    for line in f.read_text(encoding="utf-8").splitlines():
        if ":" in line:
            head, rest = line.split(":", 1)
            entries.append((f.name[:4], head.strip(), rest.strip()))

pats = [p.strip() for p in pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").splitlines() if p.strip()]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 4
for p in pats:
    rx = re.compile(p)
    hits = [e for e in entries if rx.search(e[1])]
    seen = set()
    out = []
    for book, h, r in hits:
        k = (h, r)
        if k in seen:
            continue
        seen.add(k)
        out.append(f"  {book} {h}: {r[:160]}")
    print(f"## {p} ({len(hits)})")
    print("\n".join(out[:mx]))
