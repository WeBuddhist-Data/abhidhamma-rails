"""Termbase adherence restricted to segments 1-1156 .. 1-1383 (chapters 4-02, 4-03); same matching as hindi_termbase_adherence.py.

usage: python -I -X utf8 build_rails_4-02_4-03_misses.py
"""
import collections
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
HD = ROOT / "AI_translation" / "hindi"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
WORD = re.compile(r"[ऀ-ॣ०-ॿ]+")
STOP = {"का", "की", "के", "को", "से", "में", "ने", "पर", "और", "या", "न", "है", "हैं", "भी", "ही", "तक", "वाला", "वाली", "वाले", "होना", "करना", "जो", "वह", "यह", "एक"}
ENDS = sorted(["ियों", "ियाँ", "ाओं", "ाएँ", "ाइयाँ", "ों", "ें", "एँ", "ओं", "ईं", "ाँ", "ा", "े", "ी", "ो", "ँ", "ं", "ि", "ु"], key=len, reverse=True)


def stem(w):
    for e in ENDS:
        if w.endswith(e) and len(w) - len(e) >= 2:
            return w[: -len(e)]
    return w


seg = {}
for ch in ("4-02-nikkhepakandam.md", "4-03-nikkhepakandam.md"):
    buf = []
    for line in (HD / "pi-1-hindi-plain-rails_split_chapters" / ch).read_text(encoding="utf-8").splitlines():
        buf.append(line)
        m = ID.search(line)
        if m:
            seg[m.group(1)] = " ".join(buf)
            buf = []
tb = {}
for line in (HD / "pi-1-pali-hindi-termbase-plain.md").read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    tb[w] = [s.rsplit(": ", 1)[1] for s in body[:-1].split("; ")]
ci = {k.lower(): v for k, v in tb.items()}


def found(term, words):
    parts = [x for x in WORD.findall(term) if x not in STOP and len(x) >= 2]
    stems = [stem(w) for w in words]
    return not parts or all(any(s.startswith(stem(x)) or stem(x).startswith(s) and len(s) >= 3 for s in stems) for x in parts)


total = 0
mis = collections.defaultdict(list)
for line in (ROOT / "AI_translation" / "pali" / "pi-1-keywords-by-reference-pali-plain.md").read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    i = i[1:]
    if i not in seg:
        continue
    words = WORD.findall(seg[i])
    for k in body.split(", "):
        for kk in k.split(" / "):
            terms = tb.get(kk) or ci.get(kk.lower())
            if terms:
                total += 1
                if not any(found(t, words) for t in terms):
                    mis[(kk, " | ".join(terms))].append(i)
print("checked", total, "misses", sum(len(v) for v in mis.values()))
for (k, t), v in sorted(mis.items(), key=lambda x: -len(x[1])):
    print(f"{len(v):3d} {k} -> {t}  {' '.join(v[:6])}")
