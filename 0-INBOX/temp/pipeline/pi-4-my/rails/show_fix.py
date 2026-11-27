"""Inspection helper (read only) for the review fixes: Pāli line / rails line pairs with line numbers.
usage: show_fix.py ID [ID ...] [--re REGEX]   (REGEX filters on the Pāli line)"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[5]
PA = ROOT / "AI_translation/pali/pi-4_split_chapters"
RA = ROOT / "AI_translation/burmese/pi-4-burmese-plain-rails_split_chapters"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
def segs(lines):
    out, buf = {}, []
    for k, l in enumerate(lines):
        if not l.strip():
            continue
        buf.append(k)
        m = ID.search(l)
        if m:
            out[m.group(1)] = buf; buf = []
    return out
args = sys.argv[1:]; rx = None
if "--re" in args:
    i = args.index("--re"); rx = re.compile(args[i + 1]); args = args[:i] + args[i + 2:]
for f in sorted(PA.glob("*.md")):
    p = f.read_text(encoding="utf-8-sig").split("\n"); r = (RA / f.name).read_text(encoding="utf-8").split("\n")
    ps, rs = segs(p), segs(r)
    for i in args:
        if i in ps:
            for a, b in zip(ps[i], rs[i]):
                if rx and not rx.search(p[a]):
                    continue
                print(f"[{f.name[:-3]} ^{i} l.{b+1}]\n  P: {p[a]}\n  M: {r[b]}")
