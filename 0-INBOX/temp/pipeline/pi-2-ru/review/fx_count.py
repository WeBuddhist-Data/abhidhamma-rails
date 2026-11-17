"""Count literal strings per Russian chapter file, with block IDs of the lines (read-only).
usage: python -I -X utf8 fx_count.py [--dir backup] "<literal>" ["<literal>" ...]"""
import pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
RU = ROOT / "AI_translation/russian/pi-2-russian-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
args = sys.argv[1:]
if args and args[0] == "--dir":
    RU = ROOT / "0-INBOX/temp/pipeline/pi-2-ru/review/backup-pre-fixes"
    args = args[1:]
for s in args:
    tot = 0
    print(f"--- «{s}»")
    for p in sorted(RU.glob("*.md")):
        lines = p.read_text(encoding="utf-8").splitlines()
        hits = []
        for n, line in enumerate(lines):
            c = line.count(s)
            if c:
                j = n
                while j < len(lines) and not ID.search(lines[j]):
                    j += 1
                sid = ID.search(lines[j]).group(1) if j < len(lines) else "?"
                hits.append(f"{sid}:L{n+1}x{c}")
                tot += c
        if hits:
            print(f"  {p.name}: {sum(int(h.split('x')[-1]) for h in hits)}  {' '.join(hits[:40])}")
    print(f"  TOTAL {tot}")
