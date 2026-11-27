"""KWIC over the pi-7 zero-shot (read-only): lines whose Pāli matches -p REGEX and/or whose Burmese matches -m REGEX.
usage: python3 -I -X utf8 kw7.py [-p REGEX] [-m REGEX] [-n MAX] [-c] [-w WIDTH] [-f chapter-prefix]
  -c: counts per chapter only."""
import pathlib, re, sys, collections
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-7_split_chapters"
MD = ROOT / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
a = sys.argv[1:]
def opt(k, d=None):
    return a[a.index(k) + 1] if k in a else d
pr = re.compile(opt("-p")) if opt("-p") else None
mr = re.compile(opt("-m")) if opt("-m") else None
mx = int(opt("-n", "20")); w = int(opt("-w", "400")); fp = opt("-f", "")
cnt = collections.Counter(); n = 0
for p in sorted(PD.glob("*.md")):
    if not p.name.startswith(fp) or not (MD / p.name).exists():
        continue
    pl = p.read_text(encoding="utf-8-sig").split("\n"); ml = (MD / p.name).read_text(encoding="utf-8").split("\n")
    for i, (x, y) in enumerate(zip(pl, ml), 1):
        if (pr is None or pr.search(x)) and (mr is None or mr.search(y)):
            cnt[p.name[:5]] += 1
            if "-c" not in a and n < mx:
                n += 1
                def win(s, r):
                    if r is None or len(s) <= w:
                        return s[:w]
                    m = r.search(s); s0 = max(0, m.start() - w // 3)
                    return ("…" if s0 else "") + s[s0:s0 + w]
                print(f"[{p.name[:5]}:{i}] {win(x, pr)}\n   MY: {win(y, mr)}")
print("counts:", dict(cnt), "total", sum(cnt.values()))
