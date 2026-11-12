# -*- coding: utf-8 -*-
"""Extra checks for chapters 16 and 9: Latin words outside [...], double blank lines, CR, dash counts, '—', ':-'.

usage: python -I -X utf8 check_16_9_extra.py <pali_file> <hindi_file>
"""
import re, sys

p = open(sys.argv[1], encoding="utf-8", newline="").read()
h = open(sys.argv[2], encoding="utf-8", newline="").read()
errs = []
if "\r" in h:
    errs.append("CR")
if "\n\n\n" in h:
    errs.append("double blank line")
if "—" in h or ":-" in h:
    errs.append("em dash or ':-'")
for n, line in enumerate(h.split("\n"), 1):
    body = re.sub(r"\[[^\]]*\]", "", line)
    body = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", body)
    latin = re.findall(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}", body)
    if latin:
        errs.append(f"line {n}: Latin {latin[:5]}")
pl = [l for l in p.splitlines() if l.strip()]
hl = [l for l in h.splitlines() if l.strip()]
dash = lambda s: s.count("–") + s.count("—")
if len(pl) != len(hl):
    errs.append(f"non-empty lines {len(pl)} vs {len(hl)}")
bad = [i + 1 for i, (a, b) in enumerate(zip(pl, hl)) if dash(a) != dash(b)]
if bad:
    errs.append(f"dash mismatch at non-empty lines {bad[:10]}")
print(sys.argv[2].split("\\")[-1], "lines", len(pl), len(hl), "OK" if not errs else "ERRORS")
for e in errs[:30]:
    print("  ", e)
sys.exit(1 if errs else 0)
