"""Inspection helper (read only): show the Pāli, the zero-shot and (when built) the rails Burmese of pi-3 segments.
usage: seg.py <id ...> | seg.py --grep REGEX [--max N] [--my]   (--my: grep the zero-shot Burmese instead of the Pāli)"""
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[5]
A = ROOT / "AI_translation"
DIRS = [("PĀLI", A / "pali/pi-3_split_chapters"), ("ZS", A / "burmese/pi-3-burmese-plain-zeroshot_split_chapters"),
        ("RAILS", A / "burmese/pi-3-burmese-plain-rails_split_chapters")]
ID_RE = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
N = lambda s: unicodedata.normalize("NFC", s)


def segs(d):
    out = {}
    if not d.exists():
        return out
    for f in sorted(d.glob("*.md")):
        buf = []
        for l in N(f.read_text(encoding="utf-8-sig")).splitlines():
            if not l.strip():
                continue
            buf.append(l)
            m = ID_RE.search(l)
            if m:
                out[m.group(1)] = (f.name, buf)
                buf = []
    return out


S = [(k, segs(d)) for k, d in DIRS]
args = sys.argv[1:]
if args and args[0] == "--grep":
    rx = re.compile(N(args[1]))
    mx = int(args[args.index("--max") + 1]) if "--max" in args else 20
    src = S[1][1] if "--my" in args else S[0][1]
    ids = [i for i, (_, b) in src.items() if rx.search(" ".join(b))][:mx]
else:
    ids = args
for i in ids:
    for k, s in S:
        if i in s:
            print(f"[{k} {s[i][0]} ^{i}]")
            for l in s[i][1]:
                print("   " + l)
    print()
