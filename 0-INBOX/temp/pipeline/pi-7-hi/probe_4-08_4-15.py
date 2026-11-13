"""Probe for 4-08..4-15: list distinct parentheticals, headings and words (helper, read-only)."""
import collections
import pathlib
import re
import sys

PALI = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\pali\pi-7_split_chapters")
FILES = ["4-08-dukatika-nivaranaduka.md", "4-09-dukatika-paramasaduka.md", "4-10-dukatika-sarammanaduka.md",
         "4-11-dukatika-upadanaduka.md", "4-12-dukatika-kilesaduka.md",
         "4-13-dukatika-dassanenapahatabbaduka.md", "4-14-dukatika-saranaduka.md",
         "4-15-tikaduka-hetuduka.md"]

mode = sys.argv[1] if len(sys.argv) > 1 else "paren"
out = collections.Counter()
for f in FILES:
    for line in (PALI / f).read_text(encoding="utf-8").splitlines():
        line = re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", line)
        if mode == "paren":
            for m in re.findall(r"\([^()]*\)", line):
                out[m] += 1
        elif mode == "head":
            if line.startswith("#"):
                out[re.sub(r"^#+\s*", "", line)] += 1
        elif mode == "words":
            for w in re.findall(r"[A-Za-zāīūṅñṭḍṇḷṃĀĪŪṄÑṬḌṆḶṂ]+", line):
                out[w.lower()] += 1
for k, v in sorted(out.items()):
    print(v, k)
