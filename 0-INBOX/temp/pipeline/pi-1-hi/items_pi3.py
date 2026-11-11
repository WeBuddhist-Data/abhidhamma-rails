"""Collect matrix-item renderings from the Hindi pi-3 (rails) by splitting aligned lines on '…'.

usage: python -I -X utf8 items_pi3.py
"""
import re, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[4]
P = ROOT / "AI_translation" / "pali" / "pi-3_split_chapters"
H = ROOT / "AI_translation" / "hindi" / "pi-3-hindi-plain-rails_split_chapters"
ID = re.compile(r"\s*\^([0-9A-Za-z-]+)\s*$")


def segs(p):
    out, buf = [], []
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        buf.append(ID.sub("", line))
        if ID.search(line):
            out.append(buf)
            buf = []
    return out


pairs = collections.OrderedDict()
for pf in sorted(P.glob("*.md")):
    hf = H / pf.name
    if not hf.exists():
        continue
    for sa, sb in zip(segs(pf), segs(hf)):
        for x, y in zip(sa, sb):
            xs, ys = x.split("…"), y.split("…")
            if len(xs) != len(ys) or len(xs) < 2:
                continue
            for a, b in zip(xs[:-1], ys[:-1]):
                a, b = a.strip(" .,"), b.strip(" .,")
                if a.endswith("dhammā") and len(a.split()) <= 6 and " ye " not in f" {a} ":
                    # drop leading question-words from the first piece
                    pairs.setdefault(a.lower(), b)
for a, b in pairs.items():
    print(a, "=", b)
