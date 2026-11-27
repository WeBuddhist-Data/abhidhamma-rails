"""Sentence index of the FINAL Burmese of pi-1 … pi-6 (rails texts), read-only.

A Pāli line and its aligned Burmese line are split into sentences (Pāli «. ? !» + space, Burmese «။» + space);
when both give the same number of sentences, sentence i of the Pāli is paired with sentence i of the Burmese.
index() -> {normalised Pāli sentence: {Burmese sentence: count}} (block IDs and «…pe…» normalised).

usage: python3 -I -X utf8 reuse_index.py <pali chapter file> ...   (prints the sample sentences found in pi-1 … pi-6)
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
AI = ROOT / "AI_translation"
ID_RE = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
PSPLIT = re.compile(r"(?<=[.?!])\s+(?=\S)")
MSPLIT = re.compile(r"(?<=။)\s+(?=\S)")


def norm(s):
    s = ID_RE.sub("", s).strip()
    s = s.replace("…pe…", "…").replace("…Pe…", "…")
    s = re.sub(r"\s*\{[^{}]*\}", "", s)       # variants
    s = re.sub(r"\s*\[[^\[\]]*\]", "", s)
    return s[:1].lower() + s[1:]


def mnorm(s):
    s = ID_RE.sub("", s).strip()
    return s


def index(books=("1", "2", "3", "4", "5", "6")):
    idx = {}
    for b in books:
        pd = AI / f"pali/pi-{b}_split_chapters"
        md = AI / f"burmese/pi-{b}-burmese-plain-rails_split_chapters"
        for pf in sorted(pd.glob("*.md")):
            mf = md / pf.name
            if not mf.exists():
                continue
            pl = pf.read_text(encoding="utf-8-sig").splitlines()
            ml = mf.read_text(encoding="utf-8-sig").splitlines()
            if len(pl) != len(ml):
                continue
            for p, m in zip(pl, ml):
                if not p.strip() or p.startswith("#") or p.startswith("---"):
                    continue
                ps = PSPLIT.split(ID_RE.sub("", p).strip())
                ms = MSPLIT.split(mnorm(m))
                if len(ps) != len(ms):
                    continue
                for a, c in zip(ps, ms):
                    k = norm(a)
                    d = idx.setdefault(k, {})
                    d[c] = d.get(c, 0) + 1
    return idx


def sentences(text):
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        for s in PSPLIT.split(ID_RE.sub("", line).strip()):
            yield s


if __name__ == "__main__":
    idx = index()
    for f in sys.argv[1:]:
        seen = set()
        for s in sentences(pathlib.Path(f).read_text(encoding="utf-8-sig")):
            k = norm(s)
            if k in idx and k not in seen:
                seen.add(k)
                print(f"P: {s}")
                for m, n in idx[k].items():
                    print(f"   [{n}] {m}")
