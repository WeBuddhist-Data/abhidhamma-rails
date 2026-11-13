"""Look up Pāli headwords in the pi-7 Hindi termbase (exact, case-insensitive; '*' suffix = prefix match)."""
import sys

TB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md"
entries = []
for ln in open(TB, encoding="utf-8"):
    if ": {" in ln:
        h, _, rest = ln.partition(": {")
        entries.append((h.strip(), rest.rstrip().rstrip("}")))
for w in sys.argv[1:]:
    wl = w.lower()
    hits = [(h, r) for h, r in entries if (h.lower().startswith(wl[:-1]) if wl.endswith("*") else h.lower() == wl)]
    if not hits:
        print(f"{w}: --")
    for h, r in hits[:12]:
        print(f"{h}: {r}")
