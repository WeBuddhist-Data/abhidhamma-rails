"""Read-only: the lemma-level scan of the pi-3 Burmese keyword mapping (map-harmonise decision 3, the instrumental /
dative rule). Keywords that differ only by their case / number ending (Arūpino, Arūpīhi; hetukā dhammā, hetukehi
dhammehi; sampayutto, sampayuttā …) are grouped by a crude stem (every word without its case ending, first letter
lower case) and every group with more than one value is printed with the keywords and segments of each value.
usage: python3 -I -X utf8 harmonise_lemma_scan.py [out.txt]"""
import sys, re, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
ENDS = sorted(["ehi", "ena", "āya", "iyā", "uyā", "ūhi", "īhi", "esu", "ato", "ino", "uno", "āni", "ānaṃ", "aṃ", "o",
               "ā", "a", "ī", "i", "u", "ū", "e", "yo"], key=len, reverse=True)


def stem(w):
    w = w[:1].lower() + w[1:]
    if w in ("dhammā", "dhammehi", "dhamma"):
        return "dhamm"
    for e in ENDS:
        if w.endswith(e) and len(w) - len(e) >= 3:
            return w[: -len(e)]
    return w


groups = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
for f in sorted(HERE.glob("*.mapped.md")):
    ch = f.name.split("-", 1)[0].split(".", 1)[0]
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1)
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            key = " ".join(stem(w) for w in k.split())
            groups[key][v][k].append(f"{ch}:{sid[1:]}")
out = []
for key in sorted(groups, key=str.lower):
    if len(groups[key]) > 1:
        out.append(f"== {key}")
        for v, ks in sorted(groups[key].items(), key=lambda x: -sum(len(s) for s in x[1].values())):
            out.append(f"   {v}\t" + " · ".join(f"{k} ({len(s)}: {' '.join(s[:6])})" for k, s in ks.items()))
txt = "\n".join(out) + "\n"
if len(sys.argv) > 1:
    pathlib.Path(sys.argv[1]).write_text(txt, encoding="utf-8")
print(f"lemma groups {len(groups)} | with >1 value {sum(1 for x in out if x.startswith('=='))}")
if len(sys.argv) == 1:
    print(txt)
