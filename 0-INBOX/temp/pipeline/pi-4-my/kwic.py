"""Search the FINAL pi-1 / pi-2 / pi-3 Burmese (rails texts) by Pāli: prints the Pāli line and the aligned Burmese line.

usage: python3 -I -X utf8 kwic.py REGEX [--books 123] [--max N] [--seg] [--file NAME]
Read only. Alignment by block ID and line index within the segment (equal line counts are a hard rule of the track).
"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ID_RE = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")


def blocks(text):
    res, cur = {}, []
    for line in text.splitlines():
        if not line.strip():
            continue
        cur.append(line)
        m = ID_RE.search(line)
        if m:
            res[m.group(1)] = cur
            cur = []
    return res


def main():
    a = sys.argv[1:]
    books = "123"
    mx = 40
    W = 600
    if "--w" in a:
        i = a.index("--w"); W = int(a[i + 1]); del a[i:i + 2]
    seg = False
    only = None
    if "--books" in a:
        i = a.index("--books"); books = a[i + 1]; del a[i:i + 2]
    if "--max" in a:
        i = a.index("--max"); mx = int(a[i + 1]); del a[i:i + 2]
    if "--file" in a:
        i = a.index("--file"); only = a[i + 1]; del a[i:i + 2]
    if "--seg" in a:
        a.remove("--seg"); seg = True
    rx = re.compile(a[0])
    n = 0
    for b in books:
        pdir = ROOT / f"AI_translation/pali/pi-{b}_split_chapters"
        bdir = ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters"
        for f in sorted(pdir.glob("*.md")):
            if only and only not in f.name:
                continue
            bf = bdir / f.name
            if not bf.exists():
                continue
            pb = blocks(f.read_text(encoding="utf-8-sig"))
            bb = blocks(unicodedata.normalize("NFC", bf.read_text(encoding="utf-8-sig")))
            for k, pl in pb.items():
                ml = bb.get(k, [])
                for i, p in enumerate(pl):
                    if rx.search(p):
                        n += 1
                        if n > mx:
                            print("... more")
                            return
                        if seg:
                            print(f"== pi-{b} {f.name} {k}")
                            for x, y in zip(pl, ml):
                                print("P:", x)
                                print("M:", y)
                        else:
                            print(f"== pi-{b} {f.name} {k} [{i}]")
                            print("P:", p[:W])
                            print("M:", (ml[i] if i < len(ml) else "<none>")[:W])
                        break


main()
