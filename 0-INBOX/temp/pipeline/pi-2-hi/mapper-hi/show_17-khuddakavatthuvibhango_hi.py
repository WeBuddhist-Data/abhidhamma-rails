"""Compact view of chapter 17: keywords + Hindi (long known formula strings abbreviated as {NAME}).

usage: python -I -X utf8 show_17-khuddakavatthuvibhango_hi.py <from-index> <to-index> [pali]
       python -I -X utf8 show_17-khuddakavatthuvibhango_hi.py ids <id> [<id> ...]
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from map_sample_hi import read_keywords, read_hindi, read_pali  # noqa: E402
import khuddaka17_f as F  # noqa: E402  (read-only: formula strings of the builder)

CH = "17-khuddakavatthuvibhango"
SUBS = []
for name in dir(F):
    v = getattr(F, name)
    if name.isupper() and isinstance(v, str) and len(v) > 60 and "{" not in v:
        SUBS.append((v, "{" + name + "}"))
SUBS.sort(key=lambda x: -len(x[0]))


def abbrev(t):
    for v, tag in SUBS:
        t = t.replace(v, tag)
    return t


if __name__ == "__main__":
    kws = read_keywords(CH)
    hi = read_hindi(CH)
    pi = read_pali(CH) if "pali" in sys.argv else {}
    if sys.argv[1] == "ids":
        sel = [x for x in kws if x[0] in sys.argv[2:]]
    else:
        sel = kws[int(sys.argv[1]):int(sys.argv[2])]
    for bid, k in sel:
        print(f"[{bid}] KW: {', '.join(k)}")
        if pi:
            print("  PI:", pi.get(bid))
        print("  HI:", abbrev(hi.get(bid, "???")))
