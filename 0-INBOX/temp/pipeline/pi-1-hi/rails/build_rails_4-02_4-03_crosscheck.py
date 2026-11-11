"""Compare identical Pāli sentences between chapters 4-02/4-03 and every other finished Hindi rails chapter.

usage: python -I -X utf8 build_rails_4-02_4-03_crosscheck.py
"""
import collections
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample as bs  # noqa: E402

MINE = {"4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"}
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")


def psent(text):
    text = re.sub(r"\[[^\]]*\]", "", ID.sub("", text)).replace("ः", ".")
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.?])\s+", text) if s.strip()]


def hsent(text):
    text = ID.sub("", text)
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[।?])\s+", text) if s.strip()]


def table(names):
    out = {}
    for name in names:
        ph = bs.PALI / name
        hh = bs.OUT / name
        if not hh.exists():
            continue
        p, h = dict(bs.segments(ph)), dict(bs.segments(hh))
        for sid in p:
            ps = psent(" ".join(p[sid]))
            hs = hsent(" ".join(h[sid]))
            if len(ps) == len(hs):
                for a, b in zip(ps, hs):
                    out.setdefault(a, set()).add((name, sid, b))
    return out


names = [p.name for p in bs.PALI.glob("*.md")]
mine = table(MINE)
others = table([n for n in names if n not in MINE])
shared = diff = 0
seen = collections.Counter()
for s, vals in mine.items():
    if len(s) < 15 or s not in others:
        continue
    shared += 1
    a = {b for _, _, b in vals}
    o = {b for _, _, b in others[s]}
    if a != o:
        diff += 1
        print("PALI:", s[:150])
        for x in sorted(a):
            print("  MINE :", x[:400])
        for n, sid, b in sorted(others[s])[:3]:
            print(f"  {n[:6]} {sid}:", b[:400])
print("shared sentences", shared, "differing", diff)
