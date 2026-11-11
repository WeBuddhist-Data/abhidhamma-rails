"""Termbase lookup helper for chapters 4-02 and 4-03: lists every termbase entry whose headword is a word,
or a run of consecutive words, of the two Pāli chapters. Also lists chapter words without an entry.

usage: python -I -X utf8 build_rails_4-02_4-03_lookup.py
"""
import pathlib
import re
import collections

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
PALI = ROOT / "AI_translation" / "pali" / "pi-1_split_chapters"
TB = ROOT / "AI_translation" / "hindi" / "pi-1-pali-hindi-termbase-plain.md"
OUT = ROOT / "0-INBOX" / "temp" / "pipeline" / "pi-1-hi" / "rails" / "notes-4-02_4-03-lookup.txt"

tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    if ": {" in line:
        k, body = line.split(": {", 1)
        tb[k.lower()] = (k, body[:-1])

toks = []
for ch in ("4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"):
    t = (PALI / ch).read_text(encoding="utf-8")
    t = re.sub(r"\^[0-9A-Za-z-]+", " ", t)
    toks.append([w.lower() for w in re.findall(r"[^\W\d_]+", t.replace("ः", " "))])

hit = collections.Counter()
missing = collections.Counter()
for seq in toks:
    for i, w in enumerate(seq):
        got = False
        for n in range(1, 7):
            phrase = " ".join(seq[i:i + n])
            if phrase in tb:
                hit[phrase] += 1
                got = True
        if not got:
            missing[w] += 1

out = []
for k in sorted(hit):
    out.append(f"{tb[k][0]}: {tb[k][1]}")
out.append("")
out.append("=== words without an entry ===")
for w, n in sorted(missing.items()):
    out.append(f"{w} ({n})")
OUT.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print(len(hit), "entries;", len(missing), "words without entry")
