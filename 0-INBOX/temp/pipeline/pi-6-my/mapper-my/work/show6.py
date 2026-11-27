"""read-only helper: show keywords, Pāli and Burmese of segments. usage: show6.py CH [sid-regex] [maxn]"""
import sys, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
ROOT = HERE.parents[4]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def seg(p):
    out, buf = {}, []
    for l in pathlib.Path(p).read_text(encoding="utf-8-sig").splitlines():
        if not l.strip(): continue
        buf.append(l)
        m = ID.search(l)
        if m:
            out[m.group(1)] = "\n    ".join(buf); buf = []
    return out
ch = sys.argv[1]; rx = re.compile(sys.argv[2]) if len(sys.argv) > 2 else None
n = int(sys.argv[3]) if len(sys.argv) > 3 else 10**6
my = seg(ROOT / f"AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters/{ch}.md")
pa = seg(ROOT / f"AI_translation/pali/pi-6_split_chapters/{ch}.md")
k = 0
for l in (HERE / f"{ch}.keywords.md").read_text(encoding="utf-8").splitlines():
    sid, kws = l[1:].split("] ", 1)
    if rx and not rx.search(sid): continue
    print(f"[{sid}] KW: {kws}\n  PA: {pa.get(sid)}\n  MY: {my.get(sid)}")
    k += 1
    if k >= n: break
