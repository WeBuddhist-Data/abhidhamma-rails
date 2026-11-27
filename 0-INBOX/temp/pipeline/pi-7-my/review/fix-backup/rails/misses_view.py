"""Inspection helper (read only; model pi-5-my/rails/misses_view.py): the adherence misses grouped by keyword, with the
keyword-map (zero-shot) forms, the termbase senses and the termbase decision reasons; --seg prints each segment.
usage: misses_view.py <adherence report> [keyword-regex] [--seg] [--max N]"""
import collections
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402

N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
KMAP = ROOT / "AI_translation/burmese/pi-7-keywords-by-reference-pali-burmese-plain.md"
TB = ROOT / "AI_translation/burmese/pi-7-pali-burmese-termbase-plain.md"
DEC = HERE.parent / "termbase/decisions-A.tsv"
P = A.segments(ROOT / "AI_translation/pali/pi-7_split_chapters")
Z = A.segments(ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters")
kv = {}
for l in open(KMAP, encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m:
        for x in m.group(2).split(", "):
            if "=" in x:
                k, v = x.split("=", 1)
                kv[(m.group(1), k)] = v
tbl = {}
for l in open(TB, encoding="utf-8"):
    m = re.match(r"^(.*?): \{(.*)\}\s*$", N(l.rstrip("\n")))
    if m:
        tbl[m.group(1).lower()] = m.group(2)
dec = collections.defaultdict(list)
for l in open(DEC, encoding="utf-8"):
    if l.startswith("#") or "\t" not in l:
        continue
    f = N(l).rstrip("\n").split("\t")
    dec[f[0].split("|")[0].lower()].append(f"{f[0]} «{f[1]}»: {f[2] if len(f) > 2 else ''}")
args = [a for a in sys.argv[1:] if not a.startswith("--")]
mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 99
if "--max" in sys.argv:
    args.remove(str(mx))
rx = re.compile(args[1]) if len(args) > 1 else None
groups = collections.defaultdict(list)
for l in open(args[0], encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) != 3 or not f[0][:1].isdigit():
        continue
    if rx and not rx.fullmatch(f[1]):
        continue
    groups[f[1]].append(f[0])
for kw, ids in sorted(groups.items(), key=lambda x: -len(x[1])):
    forms = collections.Counter(kv.get((i, kw)) for i in ids)
    print(f"=== {kw} ×{len(ids)}  TB: {tbl.get(kw.lower())}")
    print("   map:", "; ".join(f"«{k}» ×{v}" for k, v in forms.most_common()))
    for d in dec.get(kw.lower(), [])[:4]:
        print("   DEC:", d[:400])
    print("   ids:", " ".join(ids[:40]))
    if "--seg" in sys.argv:
        for i in ids[:mx]:
            print(f"   [{i}] P:", P[i][:500])
            print(f"   [{i}] Z:", Z[i][:700])
