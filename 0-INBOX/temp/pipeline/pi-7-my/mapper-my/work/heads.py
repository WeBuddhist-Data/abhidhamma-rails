"""heads.py: distinct (Pāli heading part, Burmese heading part) pairs over the whole book (read-only helper)."""
import re, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[6]
PI = ROOT / "AI_translation/pali/pi-7_split_chapters"; MY = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")
_LABEL = re.compile(r"\((?:[A-ZĀĪŪṄÑṬḌṆḶa-zāīūṅñṭḍṇḷṃ]{1,4}|[က-အ]|\d+)\)|\b\d+(?:-\d+)?\.|[0-9၀-၉]+(?:-[0-9၀-၉]+)?\.")
def parts(t):
    t = re.sub(r"^#+\s*", "", t.strip()).replace("*", "")
    return [p.strip(" .။") for p in _LABEL.split(t) if p.strip(" .။")]
pairs = collections.Counter(); bad = 0
for f in sorted(MY.glob("*.md")):
    pl = {ID.search(l).group(1): l for l in (PI / f.name).read_text(encoding="utf-8-sig").splitlines() if l.startswith("#") and ID.search(l)}
    for l in f.read_text(encoding="utf-8-sig").splitlines():
        if l.startswith("#") and ID.search(l):
            sid = ID.search(l).group(1); p = pl.get(sid)
            if not p: continue
            a, b = parts(ID.sub("", p)), parts(ID.sub("", l))
            if len(a) == len(b):
                for x, y in zip(a, b): pairs[(x, y)] += 1
            else:
                bad += 1
print("mismatched", bad)
for (x, y), n in sorted(pairs.items(), key=lambda t: -t[1]):
    print(n, x, "=", y)
