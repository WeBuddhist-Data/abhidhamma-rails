"""r1 helper: dump Pali / our Vietnamese / Tinh Su side by side per block ID.
Usage: python -I -X utf8 r1_align.py <chapter.md> <out.txt> [--no-ts]
"""
import re, sys, os

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
PALI = os.path.join(ROOT, r"AI_translation\pali\pi-1_split_chapters")
VI = os.path.join(ROOT, r"AI_translation\vietnamese\pi-1-vietnamese-plain-rails_split_chapters")
TS = os.path.join(ROOT, r"1-SOURCES\Translations\Vietnamese\vi-1-tinh_su.md")

IDRE = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$")
TRANS = re.compile(r"!\[\[1-SOURCES/Text/pi-1\.md#\^([0-9A-Za-z-]+)\]\]")


def segments(path):
    segs, cur = [], []
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.strip():
            cur.append(line)
            m = IDRE.search(line)
            if m:
                segs.append((m.group(1), cur))
                cur = []
    return segs


def ts_map():
    out, cur, pend = {}, [], []
    text = open(TS, encoding="utf-8").read()
    body = text.split("\n---\n", 1)[1] if text.startswith("---") else text
    for line in body.split("\n"):
        t = TRANS.search(line)
        if t:
            pend.append(t.group(1))
            continue
        if not line.strip():
            continue
        cur.append(line)
        m = IDRE.search(line)
        if m:
            ids = set(pend) | {m.group(1)}
            joined = "\n".join(cur)
            for i in ids:
                tag = "" if len(ids) == 1 else " [merged: " + ",".join(sorted(ids)) + "]"
                out[i] = joined + tag
            cur, pend = [], []
    return out


def main():
    ch, outp = sys.argv[1], sys.argv[2]
    p = segments(os.path.join(PALI, ch))
    v = dict(segments(os.path.join(VI, ch)))
    ts = {} if "--no-ts" in sys.argv else ts_map()
    with open(outp, "w", encoding="utf-8") as f:
        for i, lines in p:
            f.write("=" * 20 + " " + i + "\n")
            f.write("PI: " + "\n    ".join(lines) + "\n")
            f.write("VI: " + "\n    ".join(v.get(i, ["<MISSING>"])) + "\n")
            if ts:
                f.write("TS: " + ts.get(i, "<none>").replace("\n", "\n    ") + "\n")
    print(len(p), "segments")


if __name__ == "__main__":
    main()
