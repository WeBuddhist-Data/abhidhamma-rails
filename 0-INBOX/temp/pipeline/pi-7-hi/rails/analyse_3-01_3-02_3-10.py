"""Helper for 3-01, 3-02, 3-10: list unique lines / pieces with counts (stdout only)."""
import re, sys, collections, os

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI = os.path.join(ROOT, "AI_translation", "pali", "pi-7_split_chapters")
FILES = ["3-01-hetugocchaka.md", "3-02-culantaraduka.md", "3-10-upadanagocchaka.md"]
ID_RE = re.compile(r" \^([0-9A-Za-z-]+)\s*$")

mode = sys.argv[1] if len(sys.argv) > 1 else "lines"
files = sys.argv[2:] or FILES
c = collections.Counter()
for f in files:
    for ln in open(os.path.join(PALI, f), encoding="utf-8").read().split("\n"):
        if not ln.strip():
            continue
        m = ID_RE.search(ln)
        body = ln[: m.start()] if m else ln.rstrip()
        if mode == "lines":
            c[body] += 1
        elif mode == "heads":
            if body.startswith("#"):
                c[body] += 1
        else:
            for p in re.split(r" – |; |\. |…pe…|…|\.$|, ", body):
                p = p.strip()
                if p:
                    c[p] += 1
for k, n in sorted(c.items(), key=lambda x: -x[1]):
    print(f"{n}\t{k}")
