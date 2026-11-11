"""Look up headwords in the Hindi termbases pi-3..pi-5 (helper for part 2-05).

usage: python -I -X utf8 tb_lookup_2-05_hi.py <patterns_file> [max_per_pattern]
"""
import re, sys, pathlib

root = pathlib.Path(__file__).resolve().parents[4] / "AI_translation" / "hindi"
files = [root / f"pi-{n}-pali-hindi-termbase-plain.md" for n in (3, 4, 5)]
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
        out.append(f"  {book} {h}: {r[:200]}")
    print(f"## {p} ({len(hits)})")
    print("\n".join(out[:mx]))
