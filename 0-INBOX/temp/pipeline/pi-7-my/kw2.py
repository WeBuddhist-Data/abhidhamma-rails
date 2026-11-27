"""KWIC with a window: show the Pāli match context and the whole aligned Burmese line (read-only)."""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]; AI = ROOT / "AI_translation"
rx = re.compile(sys.argv[1]); mx = int(sys.argv[2]) if len(sys.argv) > 2 else 2
n = 0
for b in "123456":
    for pf in sorted((AI / f"pali/pi-{b}_split_chapters").glob("*.md")):
        mf = AI / f"burmese/pi-{b}-burmese-plain-rails_split_chapters" / pf.name
        if not mf.exists(): continue
        pl = pf.read_text(encoding="utf-8-sig").splitlines(); ml = mf.read_text(encoding="utf-8-sig").splitlines()
        for i, l in enumerate(pl):
            m = rx.search(l)
            if m and i < len(ml):
                a = max(0, m.start() - 80)
                print(f"[pi-{b} {pf.name}:{i+1}] ...{l[a:m.end()+120]}...")
                print("   MY:", ml[i][:1500]); n += 1
                if n >= mx: sys.exit()
