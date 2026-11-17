"""For the keywords of PART that map_10_12_ru.py cannot resolve (or whose value is not in the Russian), print the
values the approved pi-1/3/4/5 maps and the finished pi-2 maps give them.
usage: python -I -X utf8 lookup_10_12.py PART [--all]"""
import collections
import pathlib
import sys

sys.dont_write_bytecode = True
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import map_10_12_ru as M  # noqa: E402
from map_common_pi2_ru import NDE, lc, present, read_keywords, read_russian  # noqa: E402

part = sys.argv[1]
show_all = "--all" in sys.argv
ROOT = HERE.parents[4]
MAPS = sorted((ROOT / "AI_translation" / "russian").glob("pi-*-keywords-by-reference-pali-russian-plain.md"))
MAPS += sorted(p for p in HERE.glob("*.mapped.md") if not p.name.startswith(part))
ru, res = read_russian(part), M.resolver_for(part)
want = set()
for bid, kws in read_keywords(part):
    for kw in kws:
        try:
            v = res(bid, kw, kws)
        except KeyError:
            v = None
        if show_all or v is None or not (v == NDE or present(v, ru.get(bid, ""))):
            want.add(lc(kw))
hits = {k: collections.Counter() for k in want}
for m in MAPS:
    tag = m.name.split("-keywords")[0].split(".mapped")[0][:12]
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
for k in sorted(want):
    top = hits[k].most_common(4)
    print(f"{k}: " + (" | ".join(f"{v} ({n})" for v, n in top) if top else "-"))
