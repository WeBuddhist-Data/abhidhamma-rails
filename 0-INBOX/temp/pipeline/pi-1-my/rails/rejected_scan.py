"""Inspection helper: blind spots of the loose adherence check. For every decided termbase sense
(termbase/termbase-decisions.md «candidates → chosen»), list the segments whose keyword list holds the headword and
whose Burmese still contains a rejected candidate (one that is not part of the chosen term).
usage: rejected_scan.py [--rails]"""
import pathlib, re, sys, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[5]
N = lambda s: unicodedata.normalize("NFC", s)
M = ROOT / ("AI_translation/burmese/pi-1-burmese-plain-rails_split_chapters" if "--rails" in sys.argv
            else "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters")
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
segs = {}
for p in sorted(M.glob("*.md")):
    buf = []
    for l in N(p.read_text(encoding="utf-8")).splitlines():
        if not l.strip(): continue
        buf.append(l); m = ID.search(l)
        if m: segs[m.group(1)] = " ".join(buf); buf = []
kw = {}
for l in open(ROOT / "AI_translation/pali/pi-1-keywords-by-reference-pali-plain.md", encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m:
        for k in m.group(2).split(", "): kw.setdefault(k.strip(), []).append(m.group(1))
for l in open(ROOT / "0-INBOX/temp/pipeline/pi-1-my/termbase/termbase-decisions.md", encoding="utf-8"):
    f = [x.strip() for x in N(l).split(" | ")]
    if len(f) < 4 or "→" not in f[2]: continue
    hw = f[0]; cands, chosen = f[2].split("→"); chosen = chosen.strip()
    cands = [c.strip() for c in cands.replace("candidates:", "").split(" / ")]
    rej = [c for c in cands if c and c != chosen and c not in chosen]
    for i in kw.get(hw, []):
        t = segs.get(i, "")
        hit = [c for c in rej if c in t]
        if hit and chosen.replace(" … ", " ") not in t:
            print(f"{i}\t{hw}\tchosen «{chosen}»\trejected present: {' / '.join('«'+h+'»' for h in hit)}")
