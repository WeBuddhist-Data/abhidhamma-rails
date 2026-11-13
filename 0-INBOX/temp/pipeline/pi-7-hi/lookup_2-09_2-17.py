"""Look up Pāli terms in the pi-1/2/5/6 Hindi termbases (helper for build_2-09_2-17_hi.py)."""
import pathlib
import sys

HI = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi")
FILES = ["pi-1-pali-hindi-termbase-plain.md", "pi-2-pali-hindi-termbase-plain.md",
         "pi-5-pali-hindi-termbase-plain.md", "pi-6-pali-hindi-termbase-plain.md",
         "pi-4-pali-hindi-termbase-plain.md"]
terms = sys.argv[1:]
lines = {}
for f in FILES:
    lines[f] = (HI / f).read_text(encoding="utf-8").splitlines()
for t in terms:
    print("==", t)
    n = 0
    for f, ls in lines.items():
        for l in ls:
            if l.lower().startswith(t.lower()):
                print("  ", f[:4], l[:220])
                n += 1
                if n > 6:
                    break
        if n > 6:
            break
