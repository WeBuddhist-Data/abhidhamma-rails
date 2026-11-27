"""scratch (read only): find rails segments of pi-1 … pi-5 whose Pāli has REGEX and whose Burmese has STRING.
usage: findw.py 'pali regex' 'burmese' [N]"""
import re, sys, pathlib, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[5]
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
def blocks(t):
    res, cur = {}, []
    for l in t.splitlines():
        if not l.strip():
            continue
        cur.append(l)
        m = ID_RE.search(l)
        if m:
            res[m.group(1)] = cur; cur = []
    return res
rx, my = re.compile(sys.argv[1], re.I), sys.argv[2]
n = int(sys.argv[3]) if len(sys.argv) > 3 else 2
found = 0
for b in "12345":
    pd = ROOT / f"AI_translation/pali/pi-{b}_split_chapters"
    bd = ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters"
    for f in sorted(pd.glob("*.md")):
        if not (bd / f.name).exists():
            continue
        pb = blocks(f.read_text(encoding="utf-8-sig"))
        bb = blocks(unicodedata.normalize("NFC", (bd / f.name).read_text(encoding="utf-8-sig")))
        for k, v in pb.items():
            if rx.search(" ".join(v)) and my in " ".join(bb.get(k, [])):
                found += 1
                if found <= n:
                    print(f"pi-{b} {k} {f.name}: {rx.search(' '.join(v)).group(0)}")
print(f"[{found} segments]")
