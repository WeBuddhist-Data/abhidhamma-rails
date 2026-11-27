"""Show where keyword values sit in the Burmese: harmonise_ctx.py KEYWORD [chapter-prefix] [stem]
prints sid, value, and the Burmese around the stem (default: value minus a final သည်/သော)."""
import re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
MY = ROOT / "AI_translation/burmese/pi-1-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segments(path):
    out, buf = {}, []
    for l in path.read_text(encoding="utf-8-sig").splitlines():
        if not l.strip(): continue
        buf.append(l)
        m = ID.search(l)
        if m:
            out[m.group(1)] = " ".join(buf); buf = []
    return out
kw = sys.argv[1]; pre = sys.argv[2] if len(sys.argv) > 2 else ""; stem = sys.argv[3] if len(sys.argv) > 3 else None
W = int(sys.argv[4]) if len(sys.argv) > 4 else 25
for f in sorted(HERE.glob(f"{pre}*.mapped.md")):
    ch = f.name[:-len(".mapped.md")]
    segs = None
    for l in f.read_text(encoding="utf-8").splitlines():
        sid, rest = l.split("] ", 1); sid = sid[1:]
        for kv in rest.split(", "):
            k, v = kv.split("=", 1)
            if k == kw:
                segs = segs or segments(MY / f"{ch}.md")
                s = stem or re.sub(r"(သည်|သော)$", "", v.split(" … ")[0].split(" / ")[0])
                t = segs[sid]; i = t.find(s)
                ctx = t[max(0, i - W): i + len(s) + W] if i >= 0 else "(stem not found)"
                print(f"{ch}\t{sid}\t{v}\t«{ctx}»")
