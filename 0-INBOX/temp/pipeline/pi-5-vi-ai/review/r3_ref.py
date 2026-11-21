"""r3 helper: print the English (and optionally Russian) segment for given block IDs, optionally only
lines containing a substring. Console only.
usage: python -I -X utf8 -B r3_ref.py <ID> [--ru <chapter-stem>] [--grep TEXT]
"""
import re, sys
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
EN = ROOT + r"\AI_translation\english\pi-5-english-plain.md"
RU = ROOT + r"\AI_translation\russian\pi-5-russian-plain-rails_split_chapters\%s.md"
IDRE = re.compile(r"\s\^(5-[0-9-]+)\s*$")


def seg(path, want):
    cur = []
    with open(path, encoding="utf-8") as f:
        for ln in f:
            ln = ln.rstrip("\n")
            if not ln.strip():
                continue
            cur.append(ln)
            m = IDRE.search(ln)
            if m:
                if m.group(1) == want:
                    return cur
                cur = []
    return []


a = sys.argv[1:]
want = a[0]
g = a[a.index("--grep") + 1] if "--grep" in a else None
for l in seg(EN, want):
    if g is None or g.lower() in l.lower():
        print("EN: " + l)
if "--ru" in a:
    for l in seg(RU % a[a.index("--ru") + 1], want):
        if g is None or g.lower() in l.lower():
            print("RU: " + l)
