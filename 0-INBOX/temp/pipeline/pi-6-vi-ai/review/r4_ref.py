"""Print a block (by ID) from the English and/or the Tinh Su reference, to the console only.
usage: r4_ref.py en|ts|both ID[,ID...] [lineFilterRegex]"""
import sys, re, unicodedata
ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
SRC = {"en": ROOT + r"\AI_translation\english\pi-6-english-plain.md",
       "ts": ROOT + r"\1-SOURCES\Translations\Vietnamese\vi-6-tinh_su.md",
       "pi": ROOT + r"\AI_translation\pali\pi-6-pali.md"}
which = sys.argv[1]
ids = sys.argv[2].split(",")
flt = sys.argv[3] if len(sys.argv) > 3 else None
_cache = {}


def blocks(path):
    if path in _cache:
        return _cache[path]
    with open(path, encoding="utf-8") as fh:
        t = unicodedata.normalize("NFC", fh.read())
    d = {}
    for b in re.split(r"\n\s*\n", t):
        m = re.search(r"\^([0-9a-z-]+)\s*$", b.strip())
        if m:
            d[m.group(1)] = b.strip()
    _cache[path] = d
    return d


for k in (["en", "ts"] if which == "both" else [which]):
    d = blocks(SRC[k])
    for i in ids:
        b = d.get(i)
        print(f"== {k} {i} ==")
        if b is None:
            print("  (missing)")
            continue
        for j, line in enumerate(b.split("\n")):
            if flt is None or re.search(flt, line):
                print(f"  [{j}] {line}")
