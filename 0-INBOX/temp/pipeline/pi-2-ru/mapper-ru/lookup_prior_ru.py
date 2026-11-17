"""Look up how the approved Russian maps (pi-1, 3, 4, 5) render given Pāli keywords (exact match, case-insensitive first letter).
usage: python -I -X utf8 lookup_prior_ru.py kw1 "kw two" ...      (or: --file PATH with one keyword per line)"""
import collections
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[5]
MAPS = sorted((ROOT / "AI_translation" / "russian").glob("pi-*-keywords-by-reference-pali-russian-plain.md"))
args = sys.argv[1:]
if args[:1] == ["--file"]:
    args = [l.strip() for l in pathlib.Path(args[1]).read_text(encoding="utf-8").splitlines() if l.strip()]
want = {a[:1].lower() + a[1:]: a for a in args}
hits = {k: collections.Counter() for k in want}
for m in MAPS:
    tag = m.name.split("-keywords")[0]
    for line in m.read_text(encoding="utf-8").splitlines():
        if "] " not in line:
            continue
        for pair in line.split("] ", 1)[1].split(", "):
            if "=" not in pair:
                continue
            k, v = pair.split("=", 1)
            k = k[:1].lower() + k[1:]
            if k in hits:
                hits[k][f"{tag}:{v}"] += 1
for k in want:
    top = hits[k].most_common(5)
    print(f"{k}: " + (" | ".join(f"{v} ({n})" for v, n in top) if top else "-"))
