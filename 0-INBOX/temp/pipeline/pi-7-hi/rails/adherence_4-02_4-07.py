"""Termbase adherence restricted to 4-02..4-07 (same matching as hindi_termbase_adherence.py), all misses listed.
usage (repo root): python -I -B -X utf8 0-INBOX\\temp\\pipeline\\pi-7-hi\\rails\\adherence_4-02_4-07.py"""
import collections
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
FILES = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md"]
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
WORD = re.compile(r"[ऀ-ॣ०-ॿ]+")
STOP = {"का", "की", "के", "को", "से", "में", "ने", "पर", "और", "या", "न", "है", "हैं", "भी", "ही", "तक", "वाला",
        "वाली", "वाले", "होना", "करना", "जो", "वह", "यह", "एक"}
ENDS = sorted(["ियों", "ियाँ", "ाओं", "ाएँ", "ाइयाँ", "ों", "ें", "एँ", "ओं", "ईं", "ाँ", "ा", "े", "ी", "ो", "ँ", "ं",
               "ि", "ु"], key=len, reverse=True)


def stem(w):
    for e in ENDS:
        if w.endswith(e) and len(w) - len(e) >= 2:
            return w[: -len(e)]
    return w


seg = {}
for f in FILES:
    buf = []
    for line in (ROOT / "AI_translation/hindi/pi-7-hindi-plain-rails_split_chapters" / f).read_text(
            encoding="utf-8").splitlines():
        buf.append(line)
        m = ID.search(line)
        if m:
            seg[m.group(1)] = " ".join(buf)
            buf = []
tb = {}
for line in (ROOT / "AI_translation/hindi/pi-7-pali-hindi-termbase-plain.md").read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    tb[w] = [s.split(": ", 1)[1] for s in body[:-1].split("; ")]
tb_ci = {k.lower(): v for k, v in tb.items()}


def found(term, words):
    parts = [x for x in WORD.findall(term) if x not in STOP and len(x) >= 2]
    if not parts:
        return True
    stems = [stem(w) for w in words]
    return all(any(sw.startswith(stem(x)) or stem(x).startswith(sw) and len(sw) >= 3 for sw in stems) for x in parts)


total = miss = 0
misses = collections.defaultdict(list)
for line in (ROOT / "AI_translation/pali/pi-7-keywords-by-reference-pali-plain.md").read_text(
        encoding="utf-8").splitlines():
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
                misses[(kk, " | ".join(terms))].append(i)
print(f"segments {len(seg)}; checked {total} keyword occurrences; {miss} misses ({100 * miss / max(total, 1):.1f}%)")
for (k, t), ids in sorted(misses.items(), key=lambda x: -len(x[1])):
    print(f"{len(ids):4d}  {k}  ->  {t}   {', '.join(ids[:6])}")
