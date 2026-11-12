"""Viewer: python -I -X utf8 rv_view.py HINDI_RX [PALI_RX] [FILE_SUBSTR] [--pali-only] [--bak]
Prints file, non-empty line n (1-based), segment ID, Pāli line, Hindi line for matching aligned lines."""
import pathlib, re, sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PDIR = ROOT / r"AI_translation\pali\pi-2_split_chapters"
HDIR = ROOT / r"AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
if "--bak" in sys.argv:
    HDIR = ROOT / r"0-INBOX\temp\pipeline\pi-2-hi\review\backup-pre-fixes"
if "--pi1" in sys.argv:
    PDIR = ROOT / r"AI_translation\pali\pi-1_split_chapters"
    HDIR = ROOT / r"AI_translation\hindi\pi-1-hindi-plain-rails_split_chapters"
CTX = HEAD = 0
for a in sys.argv:
    if a.startswith("--head="):
        HEAD = int(a[7:])
    if a.startswith("--ctx="):
        CTX = int(a[6:])
args = [a for a in sys.argv[1:] if not a.startswith("--")]
hrx = re.compile(args[0]) if args and args[0] else None
prx = re.compile(args[1], re.I) if len(args) > 1 and args[1] else None
fsub = args[2] if len(args) > 2 else ""
IDRX = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def nl(p):
    return [l for l in p.read_text(encoding="utf-8-sig").split("\n") if l.strip()]


tot = 0
for hp in sorted(HDIR.glob("*.md"), key=lambda p: (len(p.stem.split("-")[0]), p.name)):
    if fsub and fsub not in hp.name:
        continue
    pp = PDIR / hp.name
    if not pp.exists():
        continue
    P, H = nl(pp), nl(hp)
    ids, cur = [None] * len(P), None
    for i in range(len(P) - 1, -1, -1):
        m = IDRX.search(P[i])
        if m:
            cur = m.group(1)
        ids[i] = cur
    for i, (p, h) in enumerate(zip(P, H)):
        if hrx and not hrx.search(h):
            continue
        if prx and not prx.search(p):
            continue
        tot += 1
        if HEAD:
            print(f"{hp.name[:3]} L{i+1} ^{ids[i]} | {p[:HEAD]} | {h[:HEAD]}")
        elif CTX and hrx:
            m = hrx.search(h)
            hs = "…" + h[max(0, m.start() - CTX):m.end() + CTX] + "…"
            if prx:
                m2 = prx.search(p)
                ps = "…" + p[max(0, m2.start() - CTX):m2.end() + CTX] + "…"
            else:
                ps = p[:CTX * 2]
            print(f"== {hp.name} L{i+1} ^{ids[i]}\nP: {ps}\nH: {hs}")
        else:
            print(f"== {hp.name} L{i+1} ^{ids[i]}\nP: {p}\nH: {h}")
print("total", tot)
