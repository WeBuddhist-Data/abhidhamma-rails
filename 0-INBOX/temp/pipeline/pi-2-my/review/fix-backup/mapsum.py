"""Inspection helper: adherence misses grouped by (keyword, termbase term, keyword-map value of the zero-shot).
usage: mapsum.py adherence.txt"""
import pathlib, re, sys, unicodedata, collections
ROOT = pathlib.Path(__file__).resolve().parents[5]
N = lambda s: unicodedata.normalize("NFC", s)
KM = ROOT / "AI_translation/burmese/pi-2-keywords-by-reference-pali-burmese-plain.md"
KV = {}
for l in open(KM, encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m:
        for kv in m.group(2).split(", "):
            if "=" in kv:
                k, v = kv.split("=", 1); KV[(m.group(1), k)] = v
G = collections.defaultdict(list)
for l in open(sys.argv[1], encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) == 3 and f[0][:1].isdigit():
        G[(f[1], f[2], KV.get((f[0], f[1]), "-"))].append(f[0])
for (k, t, v), ids in sorted(G.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"{len(ids)}\t{k}\t{t}\tMAP {v}\t{' '.join(ids[:8])}{' …' if len(ids) > 8 else ''}")
