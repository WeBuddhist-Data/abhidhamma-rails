"""Termbase adherence for Hindi: for each segment's Pāli keywords, check that a locked Hindi term shows up
in that segment of the rails translation (stem match, tolerant of Hindi inflection).

usage: python -I -X utf8 hindi_termbase_adherence.py <keywords-pali.md> <termbase.md> <rails_split_dir> [report.md]
A keyword passes if ANY of its termbase senses' terms is found (sense choice is contextual).
A term is found if every content word of it (Devanagari, not a postposition/particle) matches a word in the
segment by stem: trailing inflection (ों ें एँ ओं ाएँ ियाँ ा े ी ो ँ ं …) stripped from both sides, then prefix match.
"""
import re, sys, pathlib, collections

kw_path, tb_path, rails_dir = sys.argv[1:4]
report = sys.argv[4] if len(sys.argv) > 4 else None
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
for p in [pathlib.Path(rails_dir) / n for n in ("3-01-hetugocchaka.md", "3-02-culantaraduka.md", "3-10-upadanagocchaka.md")]:
    buf = []
    for line in p.read_text(encoding="utf-8").splitlines():
        buf.append(line)
        m = ID.search(line)
        if m:
            seg[m.group(1)] = " ".join(buf); buf = []

tb = {}
for line in pathlib.Path(tb_path).read_text(encoding="utf-8").splitlines():
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
examples = collections.defaultdict(list)
for line in pathlib.Path(kw_path).read_text(encoding="utf-8").splitlines():
    i, body = line.split("] ", 1); i = i[1:]
    if i not in seg or not re.match(r"7-(24|25|33)-|7-U3", i):
        continue
    words = WORD.findall(seg[i])
    for k in body.split(", "):
        for kk in k.split(" / "):
            terms = tb.get(kk) or tb_ci.get(kk.lower())
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
