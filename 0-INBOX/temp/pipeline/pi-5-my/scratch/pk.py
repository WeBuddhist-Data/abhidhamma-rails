"""scratch: pi-5 Pāli regex -> chapter:line, Pāli and Burmese (zero-shot now). usage: pk.py REGEX [--my REGEX] [--max N] [--w N] [--b]  (--b: search the Burmese only)"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]
PD = ROOT / "AI_translation/pali/pi-5_split_chapters"
MD = ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"
a = sys.argv[1:]
def opt(k, d):
    if k in a:
        i = a.index(k); v = a[i + 1]; del a[i:i + 2]; return v
    return d
mx = int(opt("--max", "30")); w = int(opt("--w", "260")); myrx = opt("--my", None)
bonly = "--b" in a
if bonly: a.remove("--b")
rx = re.compile(a[0]) if a else None
key = lambda p: (int(p.name.split("-")[0]) if p.name[0].isdigit() else 0)
n = 0
for p in sorted(PD.glob("*.md"), key=key):
    if p.name == "frontmatter.txt": continue
    P = p.read_text(encoding="utf-8-sig").split("\n"); M = (MD / p.name).read_text(encoding="utf-8").split("\n")
    for i, (x, y) in enumerate(zip(P, M), 1):
        if bonly:
            mm = re.search(a[0], y)
            if not mm: continue
            s = max(0, mm.start() - w // 2)
            n += 1
            if n <= mx: print(f"{p.name.split('-')[0]}:{i}  P: {x[:w]}\n      M: …{y[s:s + w]}")
            continue
        m = rx.search(x) if rx else None
        if rx and not m: continue
        if myrx and not re.search(myrx, y): continue
        n += 1
        if n <= mx:
            s = max(0, m.start() - 60) if m else 0
            print(f"{p.name.split('-')[0]}:{i}  P: {x[s:s + w]}\n      M: {y[:w*2] if not m else y[:w*2]}")
print(f"[{n} lines]")
