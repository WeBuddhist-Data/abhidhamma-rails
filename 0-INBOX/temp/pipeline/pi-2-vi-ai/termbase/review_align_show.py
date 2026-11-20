"""Show segments of the current pi-2 vi rails text (and, with --pre, the pre-review backup), whole or as snippets
around a regex. Also the Pāli keywords of each segment.

usage: python -I -X utf8 review_align_show.py <id,id,...|all> [--rx regex] [--w 80] [--pre] [--kw]"""
import pathlib, re, sys

sys.dont_write_bytecode = True
ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation/pali/pi-2-keywords-by-reference-pali-plain.md"
POST = ROOT / "AI_translation/vietnamese/pi-2-vietnamese-plain-rails_split_chapters"
PRE = ROOT / "0-INBOX/temp/pipeline/pi-2-vi-ai/rails/backup-pre-review"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(d):
    seg = {}
    for p in sorted(pathlib.Path(d).glob("*.md")):
        buf = []
        for line in p.read_text(encoding="utf-8").splitlines():
            buf.append(line)
            m = ID.search(line)
            if m:
                seg[m.group(1)] = " ".join(buf)
                buf = []
    return seg


a = sys.argv[1:]
seg = segs(PRE if "--pre" in a else POST)
ids = list(seg) if a[0] == "all" else a[0].split(",")
rx = re.compile(a[a.index("--rx") + 1], re.I) if "--rx" in a else None
w = int(a[a.index("--w") + 1]) if "--w" in a else 80
kws = {}
if "--kw" in a:
    for line in KW.read_text(encoding="utf-8").splitlines():
        if line.strip():
            i, body = line.split("] ", 1)
            kws[i[1:]] = body
for i in ids:
    t = seg.get(i)
    if t is None:
        print(f"{i}: (none)")
        continue
    if "--kw" in a:
        print(f"{i} KW: {kws.get(i, '')[:400]}")
    if rx:
        for m in rx.finditer(t):
            print(f"{i}: …{t[max(0, m.start() - w):m.end() + w]}…")
    else:
        print(f"{i}: {t}")
