"""Keywords of 4-01 segments with their termbase entries (read-only helper)."""
import re
import sys
from collections import Counter

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
KW = ROOT + r"\AI_translation\pali\pi-7-keywords-by-reference-pali-plain.md"
TB = ROOT + r"\AI_translation\hindi\pi-7-pali-hindi-termbase-plain.md"
SRC = ROOT + r"\AI_translation\pali\pi-7_split_chapters\4-01-kilesagocchaka.md"

ids = set(re.findall(r"\^([0-9A-Za-z-]+)\s*$", open(SRC, encoding="utf-8").read(), re.M))
cnt = Counter()
for ln in open(KW, encoding="utf-8"):
    m = re.match(r"\[([^\]]+)\] (.*)", ln.rstrip("\n"))
    if m and m.group(1) in ids:
        for w in m.group(2).split(", "):
            cnt[w] += 1
tb = {}
for ln in open(TB, encoding="utf-8"):
    k, _, v = ln.rstrip("\n").partition(": ")
    tb[k] = v
mode = sys.argv[1] if len(sys.argv) > 1 else "all"
skip = re.compile(r"paccay|^(Na|na|no|No)?[A-Za-zāīūṅñṭḍṇḷṃ]*(yā|e)$") if mode == "nocond" else None
for w, n in sorted(cnt.items(), key=lambda x: -x[1]):
    if skip and "paccay" in w:
        continue
    print(f"{n}\t{w}\t{tb.get(w, '??')}")
