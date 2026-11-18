"""r3 viewer: print aligned Pali / our Vietnamese / (optional) Tinh Su for segments of a chapter file.
Usage: python -I -X utf8 r3_view.py <chfile.md> [start_idx] [end_idx] [--ts] [--nopv]
Prints to stdout only; writes nothing.
"""
import re, sys, os

BASE = r"D:\Work\OpenPecha\abhidhamma-rails"
PDIR = os.path.join(BASE, r"AI_translation\pali\pi-1_split_chapters")
VDIR = os.path.join(BASE, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
TS = os.path.join(BASE, r"1-SOURCES\Translations\Vietnamese\vi-1-tinh_su.md")
IDRE = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(path):
    txt = open(path, encoding="utf-8").read()
    out = []
    for block in re.split(r"\n\s*\n", txt.strip()):
        lines = [l for l in block.split("\n") if l.strip()]
        if not lines:
            continue
        m = IDRE.search(lines[-1])
        out.append((m.group(1) if m else None, lines))
    return out


def ts_map():
    d = {}
    cur = []
    for l in open(TS, encoding="utf-8"):
        l = l.rstrip("\n")
        if not l.strip() or l.startswith("![["):
            continue
        cur.append(l)
        m = IDRE.search(l)
        if m:
            d[m.group(1)] = cur
            cur = []
    return d


def main():
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    ch = a[0]
    s = int(a[1]) if len(a) > 1 else 0
    e = int(a[2]) if len(a) > 2 else 10**9
    P = segs(os.path.join(PDIR, ch))
    V = segs(os.path.join(VDIR, ch))
    T = ts_map() if "--ts" in sys.argv else {}
    for i, ((pid, pl), (vid, vl)) in enumerate(zip(P, V)):
        if i < s or i > e:
            continue
        print(f"=== [{i}] {pid} {'' if pid == vid else '!!ID MISMATCH ' + str(vid)} P{len(pl)} V{len(vl)}")
        if "--nopv" not in sys.argv:
            for k in range(max(len(pl), len(vl))):
                if k < len(pl) and "--nop" not in sys.argv:
                    print("P:", pl[k])
                if k < len(vl):
                    print("V:", vl[k])
        if T:
            for l in T.get(pid, ["(no TS block)"]):
                print("T:", l)
    if len(P) != len(V):
        print("SEGMENT COUNT MISMATCH", len(P), len(V))


main()
