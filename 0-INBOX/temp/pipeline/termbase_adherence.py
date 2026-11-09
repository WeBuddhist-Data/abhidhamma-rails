"""Termbase adherence: for each segment's Pāli keywords, check the locked Russian term shows up
in that segment of the rails translation (stem match, tolerant of case endings).

usage: python -I -X utf8 termbase_adherence.py <keywords-pali.md> <termbase.md> <rails_split_dir> [report.md]
A keyword passes if ANY of its termbase senses' terms is found (sense choice is contextual).
A term is found if every content word (>=3 letters) of it matches a word in the segment by a
shared stem: first max(3, len-3) letters (min 3), case-insensitive; ё folded to е.
"""
import re, sys, pathlib, collections

kw_path, tb_path, rails_dir = sys.argv[1:4]
report = sys.argv[4] if len(sys.argv) > 4 else None
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


seg = {}
for p in pathlib.Path(rails_dir).glob("*.md"):
    buf = []
    for line in p.read_text(encoding="utf-8").splitlines():
        buf.append(line)
        m = ID.search(line)
        if m:
            seg[m.group(1)] = " ".join(buf); buf = []

tb = {}
for line in open(tb_path, encoding="utf-8").read().splitlines():
    w, body = line.split(": {", 1)
    terms = [s.rsplit(": ", 1)[1] for s in body[:-1].split("; ")]
    tb[w] = terms
tb_ci = {fold(k): v for k, v in tb.items()}


def found(term, words):
    parts = [x for x in WORD.findall(term) if fold(x) not in STOP and len(x) >= 3]
    if not parts:
        return True
    return all(any(fw.startswith(stem(x)) or stem(fw) == stem(x) for fw in words) for x in parts)


total = miss = 0
misses = collections.Counter()
examples = collections.defaultdict(list)
for line in open(kw_path, encoding="utf-8").read().splitlines():
    i, body = line.split("] ", 1); i = i[1:]
    words = [fold(x) for x in WORD.findall(seg.get(i, ""))]
    for k in body.split(", "):
        for kk in k.split(" / "):
            terms = tb.get(kk) or tb_ci.get(fold(kk))
            if not terms:
                continue
            total += 1
            if not any(found(t, words) for t in terms):
                miss += 1; misses[(kk, " | ".join(terms))] += 1
                if len(examples[kk]) < 3:
                    examples[kk].append(i)

print(f"checked {total} keyword occurrences; {miss} without the termbase term ({100*miss/max(total,1):.1f}%)")
out = [f"{n:4d}  {k}  ->  {t}   e.g. {', '.join(examples[k])}" for (k, t), n in misses.most_common()]
print("\n".join(out[:40]))
if report:
    pathlib.Path(report).write_text("\n".join(out) + "\n", encoding="utf-8")
