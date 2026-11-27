"""Look up headwords in the locked pi-1/2/3 termbases (read only). usage: tb.py WORD|/REGEX/ ..."""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
TB = {b: (ROOT / f"AI_translation/burmese/pi-{b}-pali-burmese-termbase-plain.md").read_text(encoding="utf-8").splitlines() for b in "123"}
for w in sys.argv[1:]:
    rx = re.compile(w[1:-1]) if w.startswith("/") else None
    for b, L in TB.items():
        for l in L:
            hw = l.split(":", 1)[0]
            if (rx and rx.search(hw)) or (not rx and hw.lower() == w.lower()):
                print(f"pi-{b} {l[:300]}")
