"""pi-7 KWIC: Pāli lines (finished Burmese pi-7 chapters only) matching a regex + the aligned Burmese line."""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]; AI = ROOT / "AI_translation"
rx = re.compile(sys.argv[1]); mx = int(sys.argv[2]) if len(sys.argv) > 2 else 3
skip = {"3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md", "3-10-upadanagocchaka.md"}
n = 0
for pf in sorted((AI / "pali/pi-7_split_chapters").glob("*.md")):
    mf = AI / "burmese/pi-7-burmese-plain-zeroshot_split_chapters" / pf.name
    if not mf.exists() or pf.name in skip: continue
    pl = [l for l in pf.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    ml = [l for l in mf.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    if len(pl) != len(ml): continue
    for i, l in enumerate(pl):
        m = rx.search(l)
        if m:
            a = max(0, m.start() - 60)
            print(f"[{pf.name}:{i+1}] ...{l[a:m.end()+100]}...")
            print("   MY:", ml[i][:700]); n += 1
            if n >= mx: sys.exit()
