"""Structural checks for a Hindi file against its Pāli source.

usage: python -I -X utf8 verify_hi.py <pali_file> <hindi_file>
Checks: block IDs in order, per-segment non-empty line counts, heading levels, per-line dash
counts and '[' counts, no em dash, no ':-', no CR, no double blank lines, trailing newline.
"""
import re, sys

ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")


def segs(text):
    out, buf = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        buf.append(line)
        m = ID.search(line)
        if m:
            out.append((m.group(1), buf))
            buf = []
    return out, buf


pt = open(sys.argv[1], encoding="utf-8", newline="").read()
ht = open(sys.argv[2], encoding="utf-8", newline="").read()
errs = []
ps, ptail = segs(pt)
hs, htail = segs(ht)
if htail:
    errs.append(f"trailing lines without id: {len(htail)}")
if [i for i, _ in ps] != [i for i, _ in hs]:
    errs.append(f"ID order mismatch: {len(ps)} vs {len(hs)}")
dash = lambda s: s.count("–") + s.count("—")
for (pid, pl), (hid, hl) in zip(ps, hs):
    if len(pl) != len(hl):
        errs.append(f"{pid}: lines {len(pl)} vs {len(hl)}")
        continue
    for a, b in zip(pl, hl):
        if dash(a) != dash(b):
            errs.append(f"{pid}: dash {dash(a)} vs {dash(b)}")
        if a.count("[") != b.count("["):
            errs.append(f"{pid}: brackets {a.count('[')} vs {b.count('[')}")
        la = len(a) - len(a.lstrip("#"))
        lb = len(b) - len(b.lstrip("#"))
        if la != lb:
            errs.append(f"{pid}: heading level {la} vs {lb}")
        # closing statements the Pāli wrongly ends with "?"; the rails Hindi has «।» (bilingual review)
        if pid not in {"1-33", "1-377", "1-765", "1-773", "1-788"} and \
                a.rstrip().endswith("?" + " ^" + pid) != b.rstrip().endswith("?" + " ^" + pid):
            errs.append(f"{pid}: final '?' differs")
if "\r" in ht:
    errs.append("CR found")
if "\n\n\n" in ht:
    errs.append("double blank line")
if "—" in ht:
    errs.append("em dash found")
if ":-" in ht:
    errs.append("':-' found")
if not ht.endswith("\n") or ht.endswith("\n\n"):
    errs.append("bad file ending")
print(sys.argv[2].split("\\")[-1], "segments", len(hs), "OK" if not errs else "ERRORS")
for e in errs[:30]:
    print("  ", e)
sys.exit(1 if errs else 0)
