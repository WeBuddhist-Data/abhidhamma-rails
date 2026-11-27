"""Show Pāli and FINAL (rails) Burmese segments of pi-1 / pi-2 by block ID or Pāli regex (read only).
usage: seg.py <book 1|2> <id ...> | seg.py <book> --grep REGEX [--max N]"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
ID_RE = re.compile(r"\s(\^[\w-]+)\s*$")


def segs(book):
    P = ROOT / f"AI_translation/pali/pi-{book}_split_chapters"
    B = ROOT / f"AI_translation/burmese/pi-{book}-burmese-plain-rails_split_chapters"
    out = {}
    for f in sorted(P.glob("*.md")):
        bf = B / f.name
        if not bf.exists():
            continue
        def blocks(t):
            res, cur = {}, []
            for line in t.splitlines():
                if not line.strip():
                    continue
                cur.append(line)
                m = ID_RE.search(line)
                if m:
                    res[m.group(1)] = cur
                    cur = []
            return res
        pb = blocks(f.read_text(encoding="utf-8-sig"))
        bb = blocks(bf.read_text(encoding="utf-8-sig"))
        for k, v in pb.items():
            out[k] = (f.name, v, bb.get(k))
    return out


if __name__ == "__main__":
    book = sys.argv[1]
    S = segs(book)
    a = sys.argv[2:]
    mx = 5
    if "--max" in a:
        mx = int(a[a.index("--max") + 1])
    if a and a[0] == "--grep":
        rx = re.compile(a[1])
        n = 0
        for k, (f, p, b) in S.items():
            for i, line in enumerate(p):
                if rx.search(line):
                    print(f"{k} {f} L{i}\n P: {line}\n B: {b[i] if b and i < len(b) else None}")
                    n += 1
                    break
            if n >= mx:
                break
    else:
        for k in a:
            f, p, b = S[k]
            print(k, f)
            for x, y in zip(p, b or []):
                print(" P:", x)
                print(" B:", y)
