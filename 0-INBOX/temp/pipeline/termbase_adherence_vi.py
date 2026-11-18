"""Termbase adherence for Vietnamese: for each segment's Pāli keywords, check the locked Vietnamese term
shows up in that segment of the rails translation.

usage: python -I -X utf8 termbase_adherence_vi.py <keywords-pali.md> <termbase.md> <rails_split_dir> [report.md]
Vietnamese has no inflection, so the match is literal: NFC, case-insensitive, word-bounded; punctuation, quotes,
dashes and variant brackets are ignored. A term with " … " is checked part by part, in order.
A keyword passes if ANY of its termbase senses' terms is found (sense choice is contextual), also in the
citation-form variants the termbase rule allows: without a leading nominaliser (sự / niềm / lòng / trạng thái /
tính chất / loại) and without a leading tense or «có» word (đã / đang / sẽ / có).
(Modelled on termbase_adherence.py, which is Cyrillic-only.)
"""
import collections
import pathlib
import re
import sys
import unicodedata

kw_path, tb_path, rails_dir = sys.argv[1:4]
report = sys.argv[4] if len(sys.argv) > 4 else None
ID = re.compile(r"\^([0-9A-Za-z-]+)\s*$")
GAP = " … "
LEAD = ("sự ", "niềm ", "lòng ", "trạng thái ", "tính chất ", "loại ", "đã ", "đang ", "sẽ ", "có ")


def norm(t):
    t = unicodedata.normalize("NFC", t)
    t = re.sub(r"\s*\[[^\]]*\]", " ", t)
    t = t.lower()
    t = re.sub(r"[,;:.?!“”‘’\"()–—…#*]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def present(term, text):
    pos = 0
    for part in term.split(GAP):
        p = norm(part)
        if not p:
            continue
        m = re.compile(r"(?<!\w)" + re.escape(p) + r"(?!\w)").search(text, pos)
        if not m:
            return False
        pos = m.end()
    return True


def variants(term):
    out, t = [term], term
    changed = True
    while changed:
        changed = False
        low = t.lower()
        for lead in LEAD:
            if low.startswith(lead) and len(t) > len(lead):
                t = t[len(lead):]
                out.append(t)
                changed = True
                break
    return out


seg = {}
for p in pathlib.Path(rails_dir).glob("*.md"):
    buf = []
    for line in p.read_text(encoding="utf-8").splitlines():
        buf.append(line)
        m = ID.search(line)
        if m:
            seg[m.group(1)] = norm(" ".join(buf))
            buf = []

tb = {}
for line in open(tb_path, encoding="utf-8").read().splitlines():
    if ": {" not in line:
        continue
    w, body = line.split(": {", 1)
    tb[w] = [s.rsplit(": ", 1)[1] for s in body[:-1].split("; ")]
tb_ci = {k.lower(): v for k, v in tb.items()}

total = miss = 0
misses = collections.Counter()
examples = collections.defaultdict(list)
for line in open(kw_path, encoding="utf-8").read().splitlines():
    if not line.strip():
        continue
    i, body = line.split("] ", 1)
    i = i[1:]
    if i not in seg:
        continue
    text = seg[i]
    for k in body.split(", "):
        for kk in k.split(" / "):
            terms = tb.get(kk) or tb_ci.get(kk.lower())
            if not terms:
                continue
            total += 1
            if not any(present(v, text) for t in terms for v in variants(t)):
                miss += 1
                misses[(kk, " | ".join(terms))] += 1
                if len(examples[kk]) < 3:
                    examples[kk].append(i)

print(f"checked {total} keyword occurrences in {len(seg)} segments; {miss} without the termbase term "
      f"({100 * miss / max(total, 1):.1f}%)")
out = [f"{n:4d}  {k}  ->  {t}   e.g. {', '.join(examples[k])}" for (k, t), n in misses.most_common()]
print("\n".join(out[:40]))
if report:
    pathlib.Path(report).write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
