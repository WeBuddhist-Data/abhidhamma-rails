"""Inspection helper (read only): for each adherence miss, the Pāli words holding the keyword and the zero-shot
(or rails, --rails) Burmese around the keyword map's form.  usage: ctx.py <adherence report> [kw-regex] [--rails]"""
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
KMAP = ROOT / "AI_translation/burmese/pi-4-keywords-by-reference-pali-burmese-plain.md"
P = A.segments(ROOT / "AI_translation/pali/pi-4_split_chapters")
Z = A.segments(ROOT / ("AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters" if "--rails" in sys.argv
                       else "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"))
kv = {}
for l in open(KMAP, encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m:
        for x in m.group(2).split(", "):
            if "=" in x:
                k, v = x.split("=", 1)
                kv[(m.group(1), k)] = v
args = [a for a in sys.argv[2:] if not a.startswith("--")]
rx = re.compile(args[0]) if args else None
for l in open(sys.argv[1], encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) != 3 or not f[0][:1].isdigit():
        continue
    i, kw, t = f
    if rx and not rx.fullmatch(kw):
        continue
    last = kw.split()[-1].lower()
    words = sorted({w for w in re.findall(r"[\w’']+", P[i]) if last[:max(4, len(last) - 2)] in w.lower()})
    v = kv.get((i, kw), "")
    cs = A.chunks(v) if v and not v.startswith("(") else []
    z = Z[i]
    spots = []
    for c in cs[:1]:
        for m in re.finditer(re.escape(c), z):
            spots.append(z[max(0, m.start() - 40):m.end() + 50])
    print(f"=== {i} {kw} | TB «{t}» | map «{v}» | Pāli {words}")
    for s in spots[:3]:
        print("     …" + s + "…")
