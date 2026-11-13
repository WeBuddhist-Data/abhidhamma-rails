"""Aligned Pāli/Hindi lines of the approved rails Hindi (pi-1 .. pi-5) that match a Pāli regex.
usage: python -I -X utf8 kwic_7-03-7-04.py <regex> [books=1,2] [max=10]
"""
import re, sys, pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
pat = re.compile(sys.argv[1])
books = (sys.argv[2] if len(sys.argv) > 2 else "1,2").split(",")
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 10
n = 0
for b in books:
    pdir = ROOT / "pali" / f"pi-{b}_split_chapters"
    hdir = ROOT / "hindi" / f"pi-{b}-hindi-plain-rails_split_chapters"
    for pf in sorted(pdir.glob("*.md")):
        hf = hdir / pf.name
        if not hf.exists():
            continue
        pl = [l for l in pf.read_text(encoding="utf-8").splitlines() if l.strip()]
        hl = [l for l in hf.read_text(encoding="utf-8").splitlines() if l.strip()]
        for i, l in enumerate(pl):
            m = pat.search(l)
            if m and i < len(hl):
                s = max(0, m.start() - 80)
                print(f"pi-{b}/{pf.name}:{i}\n P: {l[s:s+240]}\n H: {hl[i][:400]}")
                n += 1
                if n >= mx:
                    sys.exit()
