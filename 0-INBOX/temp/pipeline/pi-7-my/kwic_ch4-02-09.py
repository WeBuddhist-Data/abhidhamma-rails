"""Read-only: Pāli lines of the FINISHED pi-7 Burmese chapters matching a regex, with the aligned Burmese line.
usage: python3 -I -X utf8 kwic_ch4-02-09.py <regex> [max] [chapter-prefix]"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[4] / "AI_translation"
rx = re.compile(sys.argv[1]); mx = int(sys.argv[2]) if len(sys.argv) > 2 else 4
pre = sys.argv[3] if len(sys.argv) > 3 else ""
MINE = ("4-02", "4-03", "4-04", "4-05", "4-06", "4-07", "4-08", "4-09")
n = 0
for pf in sorted((ROOT / "pali/pi-7_split_chapters").glob("*.md")):
    if pf.name.startswith(MINE) or not pf.name.startswith(pre):
        continue
    mf = ROOT / "burmese/pi-7-burmese-plain-zeroshot_split_chapters" / pf.name
    if not mf.exists():
        continue
    pl = [l for l in pf.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    ml = [l for l in mf.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    for i, l in enumerate(pl):
        if rx.search(l) and i < len(ml):
            print(f"[{pf.name}:{i+1}] {l[:700]}\n   MY: {ml[i][:1500]}")
            n += 1
            if n >= mx:
                sys.exit()
