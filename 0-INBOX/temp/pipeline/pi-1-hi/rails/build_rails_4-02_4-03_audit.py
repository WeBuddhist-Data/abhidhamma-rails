"""Audit for chapters 4-02 and 4-03: every 'Katame dhammā X?' and 'ime dhammā X' in the Pāli is matched to its pair in the
Pāli matrix, and the Hindi must carry the name of that same pair from the Hindi 1-matika.md verbatim.

usage: python -I -X utf8 build_rails_4-02_4-03_audit.py
"""
import pathlib
import re
import sys

RAILS = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-1-hi\rails")
sys.path.insert(0, str(RAILS))
import build_rails_sample as bs  # noqa: E402

PH = bs.PH
PM, HM = {}, {}


def norm(s):
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = re.sub(r"\bdhammā\b", " ", s.lower())
    s = s.replace("ṇ", "ṇ")
    return " ".join(re.findall(r"[^\W\d_]+", s))


for sid, lines in bs.segments(bs.PALI / "1-matika.md"):
    for line in lines:
        m = re.match(r"\((Ka|Kha|Ga)\) (.+?)\.?(\s*\^.*)?$", line)
        if m and "M2-" in sid:
            PM.setdefault(norm(m.group(2)), []).append((sid, m.group(1)))
for sid, lines in bs.segments(bs.OUT / "1-matika.md"):
    for line in lines:
        m = re.match(r"\((क|ख)\) (.+)", line)
        if m and "M2-" in sid:
            nm = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", m.group(2))
            nm = re.sub(r"\s*\[[^\]]*\]", "", nm).rstrip("।").strip()
            HM[(sid, {"क": "Ka", "ख": "Kha"}[m.group(1)])] = nm

bad = checked = 0
unmatched = []


def frames(nm):
    if nm.startswith("ऐसी "):
        core = re.fullmatch(rf"ऐसी {PH} जो (.+) नहीं हैं", nm).group(1)
        return f"कौन-सी {PH} {core} नहीं हैं?", f"ये {PH} {core} नहीं हैं।"
    return f"{nm} कौन-सी हैं?", f"ये {nm} हैं।"


for ch in ("4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"):
    p = dict(bs.segments(bs.PALI / ch))
    h = dict(bs.segments(bs.OUT / ch))
    for sid, plines in p.items():
        text = " ".join(plines)
        hindi = " ".join(h[sid])
        for kind, pat in (("q", r"Katame dhammā ([^?]+)\?"), ("a", r"[Ii]me dhammā ([^.?^]+)[.?]")):
            for m in re.finditer(pat, text):
                key = norm(m.group(1))
                hits = PM.get(key)
                if not hits:
                    unmatched.append((sid, kind, m.group(1)))
                    continue
                checked += 1
                q, a = frames(HM[hits[-1]])
                want = q if kind == "q" else a
                if sid == "1-1310" and kind == "a":
                    want = a[:-1] + "?"
                if want not in hindi:
                    bad += 1
                    print("MISSING", sid, kind, m.group(1), "=>", want)
print("frames checked", checked, "bad", bad)
print("not in the Pāli matrix:", len(unmatched))
for u in unmatched:
    print("  ", u)
