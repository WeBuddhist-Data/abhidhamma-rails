"""List keywords of chapters 2/3 not covered by KH / CH2 / MATRIX, with the values in the approved maps.
usage: python -I -X utf8 unmapped_2_3.py PART"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from map_common_pi2_ru import CH2, KH, MATRIX, lc, read_keywords  # noqa: E402

ROOT = HERE.parents[4]
MAPS = sorted((ROOT / "AI_translation" / "russian").glob("pi-*-keywords-by-reference-pali-russian-plain.md"))
MAPS.append(HERE / "1-khandhavibhango.mapped.md")

part = sys.argv[1]
extra = set()
if len(sys.argv) > 2:
    import importlib
    mod = importlib.import_module(sys.argv[2])
    extra = set(mod.T)
want = collections.OrderedDict()
for bid, kws in read_keywords(part):
    for k in kws:
        lk = lc(k)
        if lk in KH or lk in CH2 or lk in MATRIX or lk in extra:
            continue
        want.setdefault(lk, bid)
hits = {k: collections.Counter() for k in want}
for m in MAPS:
    tag = m.name.split("-keywords")[0].replace(".mapped.md", "")
    for line in m.read_text(encoding="utf-8").splitlines():
        if "] " not in line:
            continue
        for pair in line.split("] ", 1)[1].split(", "):
            if "=" not in pair:
                continue
            k, v = pair.split("=", 1)
            k = lc(k)
            if k in hits:
                hits[k][f"{tag}:{v}"] += 1
for k, b in want.items():
    top = hits[k].most_common(4)
    print(f"{k} [{b}]: " + (" | ".join(f"{v} ({n})" for v, n in top) if top else "-"))
