"""Extra checks for the Russian pi-1 outputs.

usage: python -I -X utf8 verify_ru.py <pali_file> <russian_file> [<pali_file> <russian_file> ...]
Per pair: block IDs equal and in the same order; per-segment non-empty line counts equal;
no CR; no double blank lines; no «ли» as a word; no Latin letters outside [...] brackets
(Latin inside variant brackets is allowed); no em dash.
"""
import re, sys

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(text):
    out, n = [], 0
    for line in text.splitlines():
        if not line.strip():
            continue
        n += 1
        m = ID.search(line)
        if m:
            out.append((m.group(1), n))
            n = 0
    return out


bad = 0
args = sys.argv[1:]
for p, r in zip(args[::2], args[1::2]):
    pt = open(p, encoding="utf-8").read()
    rb = open(r, "rb").read()
    rt = rb.decode("utf-8")
    errs = []
    ps, rs = segs(pt), segs(rt)
    if [i for i, _ in ps] != [i for i, _ in rs]:
        errs.append("block IDs differ")
    elif [n for _, n in ps] != [n for _, n in rs]:
        errs.append("line counts differ")
    if b"\r" in rb:
        errs.append("CR found")
    if "\n\n\n" in rt:
        errs.append("double blank line")
    if re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", rt):
        errs.append("«ли» found")
    if "—" in rt:
        errs.append("em dash found")
    body = re.sub(r"\[[^\]]*\]", "", rt)
    body = re.sub(r"\^[0-9A-Za-z-]+", "", body)
    latin = sorted(set(re.findall(r"[A-Za-zÀ-ɏḀ-ỿ]+", body)))
    if latin:
        errs.append(f"Latin outside brackets: {latin[:10]}")
    if errs:
        bad += 1
    print(r, "->", "; ".join(errs) if errs else f"OK ({len(rs)} segments, IDs identical in order)")
sys.exit(1 if bad else 0)
