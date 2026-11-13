"""Termbase adherence restricted to my segments (^7-50-* .. ^7-58-*), same matching as hindi_termbase_adherence.py.
usage: python -I -B -X utf8 adherence_4-16_5-04.py"""
import collections
import pathlib
import re

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation/pali/pi-7-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation/hindi/pi-7-pali-hindi-termbase-plain.md"
DIR = ROOT / "AI_translation/hindi/pi-7-hindi-plain-rails_split_chapters"
FILES = ["4-16-tikaduka-sappaccayaduka.md", "4-17-tikaduka-asavaduka.md", "4-18-tikaduka-sarammanaduka.md",
         "4-19-tikaduka-kilesaduka.md", "4-20-tikaduka-dassanenapahatabbaduka.md", "4-21-tikaduka-sauttaraduka.md",
         "5-01-anuloma-tikatika.md", "5-02-anuloma-dukaduka.md", "5-03-paccaniya-tika.md", "5-04-paccaniya-duka.md"]
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
for f in FILES:
    buf = []
    for line in (DIR / f).read_text(encoding="utf-8").splitlines():
        buf.append(line)
        m = ID.search(line)
        if m:
            seg[m.group(1)] = " ".join(buf)
            buf = []
tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
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
misses = collections.Counter()
ex = collections.defaultdict(list)
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
                misses[(kk, " | ".join(terms))] += 1
                if len(ex[kk]) < 3:
                    ex[kk].append(i)
print(f"segments {len(seg)}; checked {total}; misses {miss} ({100 * miss / max(total, 1):.1f}%)")
for (k, t), n in misses.most_common():
    print(f"{n:4d}  {k}  ->  {t}   e.g. {', '.join(ex[k])}")
