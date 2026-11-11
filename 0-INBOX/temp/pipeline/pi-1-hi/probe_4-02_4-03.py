"""Probe: find Pāli formulas of 4-02/4-03 in pi-3/4/5 and print the Hindi segment with the same block ID.

usage: python -I -X utf8 probe_4-02_4-03.py <pattern> [<pattern> ...]
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
AI = ROOT / "AI_translation"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(path):
    out, buf = {}, []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            out[m.group(1)] = "\n".join(buf)
            buf = []
    return out


hits = 0
for book in ("pi-3", "pi-4", "pi-5"):
    pdir = AI / "pali" / f"{book}_split_chapters"
    hdir = AI / "hindi" / f"{book}-hindi-plain-zeroshot_split_chapters"
    for pf in sorted(pdir.glob("*.md")):
        hf = hdir / pf.name
        if not hf.exists():
            continue
        ps = segs(pf)
        hs = None
        for bid, txt in ps.items():
            if all(re.search(p, txt) for p in sys.argv[1:]):
                hs = hs or segs(hf)
                print("=" * 20, book, pf.name, bid)
                print("PALI:", txt[:1500])
                print("HI:  ", hs.get(bid, "?")[:2500])
                hits += 1
                if hits >= 4:
                    sys.exit(0)
print("hits", hits)
