"""Helper for 3-01, 3-02, 3-10: print termbase entries for the given Pāli words (case-insensitive, exact headword).
usage: python -I -B -X utf8 lookup_3-01_3-02_3-10.py word1 word2 ...   (a word ending in * = prefix search)"""
import sys

TB = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md"
tb = {}
for line in open(TB, encoding="utf-8").read().splitlines():
    if ": {" in line:
        w, body = line.split(": {", 1)
        tb.setdefault(w.lower(), []).append(line)
for q in sys.argv[1:]:
    ql = q.lower()
    if ql.endswith("*"):
        hits = [l for k, ls in tb.items() if k.startswith(ql[:-1]) for l in ls][:8]
    else:
        hits = tb.get(ql, [])
    print(f"## {q}: " + (" || ".join(hits) if hits else "-"))
