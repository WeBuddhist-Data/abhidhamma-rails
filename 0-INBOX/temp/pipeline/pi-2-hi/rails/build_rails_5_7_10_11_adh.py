"""Termbase adherence restricted to chapters 5, 7, 10, 11 (same matching as hindi_termbase_adherence.py),
listing every miss with its segment id.

usage: python -I -X utf8 build_rails_5_7_10_11_adh.py
"""
import collections
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation" / "pali" / "pi-2-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation" / "hindi" / "pi-2-pali-hindi-termbase-plain.md"
OUT = ROOT / "AI_translation" / "hindi" / "pi-2-hindi-plain-rails_split_chapters"
NAMES = ["5-indriyavibhango.md", "7-satipatthanavibhango.md", "10-bojjhangavibhango.md", "11-maggangavibhango.md"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
WORD = re.compile(r"[ऀ-ॣ०-ॿ]+")
STOP = {"का", "की", "के", "को", "से", "में", "ने", "पर", "और", "या", "न", "है", "हैं", "भी", "ही", "तक", "वाला",
        "वाली", "वाले", "होना", "करना", "जो", "वह", "यह", "एक"}
ENDS = sorted(["ियों", "ियाँ", "ाओं", "ाएँ", "ाइयाँ", "ों", "ें", "एँ", "ओं", "ईं", "ाँ", "ा", "े", "ी", "ो", "ँ", "ं", "ि", "ु"],
              key=len, reverse=True)


def stem(w):
    for e in ENDS:
        if w.endswith(e) and len(w) - len(e) >= 2:
            return w[: -len(e)]
    return w


seg = {}
for n in NAMES:
    buf = []
    for line in (OUT / n).read_text(encoding="utf-8").splitlines():
        buf.append(line)
        m = ID.search(line)
        if m:
            seg[m.group(1)] = " ".join(buf)
            buf = []
tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    tb[w] = [s.rsplit(": ", 1)[1] for s in body[:-1].split("; ")]
tb_ci = {k.lower(): v for k, v in tb.items()}


def found(term, words):
    parts = [x for x in WORD.findall(term) if x not in STOP and len(x) >= 2]
    if not parts:
        return True
    stems = [stem(w) for w in words]
    return all(any(sw.startswith(stem(x)) or stem(x).startswith(sw) and len(sw) >= 3 for sw in stems) for x in parts)


total = miss = 0
by = collections.defaultdict(list)
for line in KW.read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    i = i[1:]
    if i not in seg:
        continue
    words = WORD.findall(seg[i])
    for k in body.split(", "):
        for kk in k.split(" / "):
            terms = tb.get(kk) or tb_ci.get(kk.lower())
            if not terms:
                continue
            total += 1
            if not any(found(t, words) for t in terms):
                miss += 1
                by[(kk, " | ".join(terms))].append(i)
print(f"checked {total}; misses {miss} ({100 * miss / max(total, 1):.1f}%)")
for (k, t), ids in sorted(by.items(), key=lambda x: -len(x[1])):
    print(f"{len(ids):3d} {k} -> {t}  [{', '.join(ids[:6])}]")
