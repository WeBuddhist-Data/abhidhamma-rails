"""Show Pāli lines matching a regex in pi-1/pi-2 split chapters with the aligned rails Hindi line.
usage: python -I -X utf8 kwic_7-05-7-06.py <regex> [max]
"""
import re, sys, pathlib

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation")
pat = re.compile(sys.argv[1])
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 12
n = 0
for book in ("pi-1", "pi-2", "pi-3", "pi-4", "pi-5"):
    pdir = ROOT / "pali" / f"{book}_split_chapters"
    hdir = ROOT / "hindi" / f"{book}-hindi-plain-rails_split_chapters"
    if not hdir.exists():
        continue
    for pf in sorted(pdir.glob("*.md")):
        hf = hdir / pf.name
        if not hf.exists():
            continue
        pl = [l for l in pf.read_text(encoding="utf-8").splitlines() if l.strip()]
        hl = [l for l in hf.read_text(encoding="utf-8").splitlines() if l.strip()]
        for i, l in enumerate(pl):
            if pat.search(l):
                print(f"[{book}/{pf.name}:{i}] {l[:300]}")
                print(f"   HI: {hl[i][:300] if i < len(hl) else '??'}")
                n += 1
                if n >= mx:
                    sys.exit()
