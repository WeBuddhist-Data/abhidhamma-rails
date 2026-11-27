"""Locked pi-3 / pi-2 / pi-1 entries for headwords (case-insensitive; with --sub: every headword containing the string).
usage: lk.py [--sub] hw [hw ...]"""
import sys, pathlib
B = pathlib.Path(__file__).resolve().parents[5]
F = [(n, B / f"AI_translation/burmese/pi-{n[-1]}-pali-burmese-termbase-plain.md") for n in ("pi-4", "pi-3", "pi-2", "pi-1")]
D = {}
for n, p in F:
    D[n] = [l.split(": {", 1) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
a = sys.argv[1:]; sub = "--sub" in a; a = [x for x in a if x != "--sub"]
for hw in a:
    for n in D:
        for h, body in D[n]:
            if (hw.lower() in h.lower()) if sub else (h.lower() == hw.lower()):
                print(f"{n} {h}: {body[:-1][:300]}")
