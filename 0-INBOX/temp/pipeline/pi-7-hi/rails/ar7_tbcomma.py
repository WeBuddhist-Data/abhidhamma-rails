"""Termbase terms (written without commas) that occur in the Hindi with a comma inside (pi-1 internal commas).
usage: python -I -B -X utf8 ar7_tbcomma.py [--bak]"""
import os, re, sys, collections, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ar7_common as C

TB = os.path.join(C.ROOT, r"AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md")
hdir = C.BAK if "--bak" in sys.argv else C.HDIR
terms = set()
for line in open(TB, encoding="utf-8"):
    if ": {" not in line:
        continue
    body = line.split(": {", 1)[1].rstrip().rstrip("}")
    for s in body.split("; "):
        if ": " in s:
            t = s.split(": ", 1)[1].strip()
            if len(t.split()) >= 3:
                terms.add(t)


def rx_of(t):
    ws = t.split()
    out = []
    for w in ws:
        e = re.escape(w)
        e = re.sub(r"वाला$", "वा(?:ला|ली|ले)", e)
        e = re.sub(r"^(का|की|के)$", "क[ाीे]", e)
        e = re.sub(r"(जुड़ा|हुआ|समाया)$", lambda m: m.group(1)[:-1] + "[ाीे]", e)
        out.append(e)
    return re.compile(r"(?<![ऀ-ॿ])" + "(?:,? )".join(out) + r"(?![ऀ-ॿ])")


cnt = collections.Counter()
files = collections.defaultdict(set)
ex = {}
texts = {os.path.basename(p)[:-3]: open(p, encoding="utf-8").read() for p in glob.glob(os.path.join(hdir, "*.md"))}
for t in sorted(terms, key=len, reverse=True):
    if "," in t:
        continue
    r = rx_of(t)
    for part, tx in texts.items():
        for m in r.finditer(tx):
            if "," in m.group(0):
                cnt[t] += 1
                files[t].add(part[:4])
                ex.setdefault(t, m.group(0))
for t, n in cnt.most_common():
    print(f"[{n}] {t}  ::  {ex[t]}  ::  {' '.join(sorted(files[t]))}")
