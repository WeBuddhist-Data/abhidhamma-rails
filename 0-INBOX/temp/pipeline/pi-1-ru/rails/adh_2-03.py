"""Termbase adherence restricted to the segments of 2-03.
Same matching rules as 0-INBOX/temp/pipeline/termbase_adherence.py (functions copied).
usage: python -I -X utf8 adh_2-03.py"""
import collections
import re
from pathlib import Path

ROOT = Path(r"D:\Work\OpenPecha\abhidhamma-rails")
KW = ROOT / "AI_translation" / "pali" / "pi-1-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation" / "russian" / "pi-1-pali-russian-termbase-plain.md"
RU = ROOT / "AI_translation" / "russian" / "pi-1-russian-plain-rails_split_chapters" / "2-03-cittuppadakandam.md"
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
WORD = re.compile(r"[А-Яа-яЁё]+")
STOP = {"и", "в", "с", "к", "по", "из", "на", "не", "ни", "о", "об", "как", "его", "что", "те", "кто", "тот"}


def fold(s):
    return s.lower().replace("ё", "е")


def stem(w):
    w = fold(w)
    if len(w) <= 3:
        return w
    cut = 3 if len(w) < 7 else 5
    return w[: max(3, len(w) - cut)]


def found(term, words):
    parts = [x for x in WORD.findall(term) if fold(x) not in STOP and len(x) >= 3]
    return all(any(fw.startswith(stem(x)) or stem(fw) == stem(x) for fw in words) for x in parts)


seg = {}
buf = []
for line in RU.read_text(encoding="utf-8").splitlines():
    buf.append(line)
    m = ID.search(line)
    if m:
        seg[m.group(1)] = " ".join(buf)
        buf = []
tb = {}
for line in TB.read_text(encoding="utf-8").splitlines():
    w, body = line.split(": {", 1)
    tb[w] = [s.rsplit(": ", 1)[1] for s in body[:-1].split("; ")]
tb_ci = {fold(k): v for k, v in tb.items()}
total = miss = 0
misses = collections.Counter()
ex = collections.defaultdict(list)
for line in KW.read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1)
    i = i[1:]
    if i not in seg:
        continue
    words = [fold(x) for x in WORD.findall(seg[i])]
    for k in body.split(", "):
        for kk in k.split(" / "):
            terms = tb.get(kk) or tb_ci.get(fold(kk))
            if not terms:
                continue
            total += 1
            if not any(found(t, words) for t in terms):
                miss += 1
                misses[(kk, " | ".join(terms))] += 1
                if len(ex[kk]) < 4:
                    ex[kk].append(i)
print(f"segments {len(seg)}; checked {total} keyword occurrences; {miss} misses ({100 * miss / max(total, 1):.1f}%)")
for (k, t), n in misses.most_common():
    print(f"{n:4d}  {k}  ->  {t}   e.g. {', '.join(ex[k])}")
