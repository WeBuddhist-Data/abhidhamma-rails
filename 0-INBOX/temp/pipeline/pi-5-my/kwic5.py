"""Read-only lookup: search the FINAL pi-1 … pi-4 Burmese (rails texts) by Pāli regex; prints Pāli line + Burmese line.

usage: python3 -I -X utf8 kwic5.py REGEX [--books 1234] [--max N] [--seg]
Alignment by block ID and line index inside the segment (equal line counts are a hard rule of the track).
Scratch helper only: the generator never uses it.
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
    books, mx, seg = "1234", 8, False
    if "--books" in a:
        i = a.index("--books"); books = a[i + 1]; del a[i:i + 2]
    if "--max" in a:
        i = a.index("--max"); mx = int(a[i + 1]); del a[i:i + 2]
    if "--seg" in a:
        a.remove("--seg"); seg = True
    global FULL
    FULL = "--full" in a
    if FULL:
        a.remove("--full")
    rx = re.compile(a[0], re.I)
    n = 0
    for b in books:
        pdir = ROOT / f"AI_translation/pali/pi-{b}_split_chapters"
        bdir = ROOT / f"AI_translation/burmese/pi-{b}-burmese-plain-rails_split_chapters"
        for f in sorted(pdir.glob("*.md")):
            bf = bdir / f.name
            if not bf.exists():
                continue
            pb = blocks(f.read_text(encoding="utf-8-sig"))
            bb = blocks(unicodedata.normalize("NFC", bf.read_text(encoding="utf-8-sig")))
            for k, pl in pb.items():
                for i, line in enumerate(pl):
                    if rx.search(line):
                        n += 1
                        if n > mx:
                            continue
                        my = bb.get(k, [""] * len(pl))
                        if seg:
                            print(f"== pi-{b} {k} {f.name}\n" + "\n".join(pl) + "\n--\n" + "\n".join(my) + "\n")
                        else:
                            ml = my[i] if i < len(my) else '?'
                            ps = re.split(r"(?<=[.?!])\s+(?=[A-ZĀĪŪṬḌÑ\"“‘(\[])", line)
                            ms = re.split(r"(?<=။)\s+", ml)
                            if len(ps) == len(ms) and not FULL:
                                for x, y in zip(ps, ms):
                                    if rx.search(x):
                                        print(f"== pi-{b} {k} L{i} (sentence)\n{x}\n{y}\n")
                                        break
                            else:
                                m = rx.search(line); lo = max(0, m.start() - 120)
                                print(f"== pi-{b} {k} L{i} [{len(ps)}/{len(ms)}]\n{line[lo:m.end() + 120]}\n{ml if FULL else ml[:900]}\n")
    print(f"[{n} hits]")


main()
