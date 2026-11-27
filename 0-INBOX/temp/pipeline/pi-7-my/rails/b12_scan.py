"""Inspection helper for B12: «Q1 Q2 N» stacks of two qualifier phrases without «၊». The qualifier phrases are the
Burmese of the single-term titles «X dhammo Y dhammassa …» = «Q သဘောတရားသည် …» (the book's own term renderings).
usage: b12_scan.py [folder] [--list]"""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
BD = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else HERE / "dev-out"


def qualifiers(folder):
    q = collections.Counter()
    for p in sorted(PD.glob("*.md")):
        pl = N(p.read_text(encoding="utf-8-sig")).split("\n"); bl = N((folder / p.name).read_text(encoding="utf-8")).split("\n")
        for a, b in zip(pl, bl):
            m = re.match(r"(\w+) dhammo \w+ dhammassa ", a)
            if m:
                mb = re.match(r"(.+?) သဘောတရားသည် ", b)
                if mb and mb.group(1).endswith("သော") and "၊" not in mb.group(1):
                    q[mb.group(1)] += 1
    return sorted(q, key=len, reverse=True)


def stack_re(ql):
    alt = "|".join(re.escape(x) for x in ql)
    return re.compile(r"(?:(?<=[ (“၊])|^)(" + alt + r") (?=(" + alt + r") (?!(?:" + alt + r"))\S)")


if __name__ == "__main__":
    ql = qualifiers(BD)
    rx = stack_re(ql)
    c = collections.Counter(); per = collections.Counter(); rows = []
    for p in sorted(PD.glob("*.md")):
        bl = N((BD / p.name).read_text(encoding="utf-8")).split("\n")
        for k, b in enumerate(bl, 1):
            for m in rx.finditer(b):
                c[(m.group(1), m.group(2))] += 1; per[p.name[:4]] += 1
                rows.append((p.name[:-3], k, m.group(1), m.group(2), b[m.end():m.end() + 60]))
    if "--list" in sys.argv:
        for r in rows:
            print("\t".join(map(str, r)))
    for k, v in c.most_common(25):
        print(v, k)
    print(len(ql), "qualifiers;", sum(c.values()), "stacks;", per.most_common(12))
