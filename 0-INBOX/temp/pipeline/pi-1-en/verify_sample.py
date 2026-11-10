"""Verify an English split file against its Pāli counterpart.

usage: python -I -X utf8 verify_sample.py <pali_file> <english_file>
Checks: block IDs equal and in order, same non-empty line count per segment,
same en/em dash count per line, same count of '[' per line, no em dash in English
unless the Pāli line has one, no ':-', no double blank lines, headings keep # level.
"""
import re, sys, pathlib

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(p):
    text = pathlib.Path(p).read_text(encoding="utf-8")
    out, buf = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            out.append((m.group(1), buf))
            buf = []
    return text, out, buf


pt, ps, ptail = segs(sys.argv[1])
et, es, etail = segs(sys.argv[2])
errs = []
if [i for i, _ in ps] != [i for i, _ in es]:
    errs.append("block ID order/content differs")
if etail:
    errs.append(f"trailing lines without ID: {len(etail)}")
for (pid, pl), (eid, el) in zip(ps, es):
    if len(pl) != len(el):
        errs.append(f"{pid}: line count {len(pl)} vs {len(el)}")
        continue
    for a, b in zip(pl, el):
        if a.count("–") + a.count("—") != b.count("–") + b.count("—"):
            errs.append(f"{pid}: dash count differs")
        if b.count("—") > a.count("—"):
            errs.append(f"{pid}: em dash added")
        if a.count("[") != b.count("["):
            errs.append(f"{pid}: bracket count {a.count('[')} vs {b.count('[')}")
        ha = re.match(r"#+", a)
        hb = re.match(r"#+", b)
        if (ha and ha.group()) != (hb and hb.group()):
            errs.append(f"{pid}: heading level differs")
if ":-" in et:
    errs.append("':-' present")
if "\n\n\n" in et:
    errs.append("double blank line present")
if "…pe…" in et or "pe…" in et:
    errs.append("untranslated pe")
print(f"segments pali={len(ps)} english={len(es)}")
print("OK" if not errs else "\n".join(errs[:40]))
sys.exit(1 if errs else 0)
