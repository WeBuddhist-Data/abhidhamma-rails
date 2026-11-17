"""Termbase adherence for chapter 16 only (^2-16-* headings and ^2-751 … ^2-831), same matching rule as
0-INBOX/temp/pipeline/termbase_adherence.py; prints to stdout (no report file).
usage: python -I -X utf8 adherence_16.py
"""
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
sys.argv = ["x", str(ROOT / "AI_translation/pali/pi-2-keywords-by-reference-pali-plain.md"),
            str(ROOT / "AI_translation/russian/pi-2-pali-russian-termbase-plain.md"),
            str(ROOT / "AI_translation/russian/pi-2-russian-plain-rails_split_chapters")]
src = (ROOT / "0-INBOX/temp/pipeline/termbase_adherence.py").read_text(encoding="utf-8")
ns = {}
exec(compile(src.split("total = miss = 0")[0], "termbase_adherence", "exec"), ns)   # helpers only
seg, tb, tb_ci, found, fold, WORD = ns["seg"], ns["tb"], ns["tb_ci"], ns["found"], ns["fold"], ns["WORD"]


def mine(i):
    if i.startswith("2-16-"):
        return True
    m = re.match(r"^2-(\d+)$", i)
    return bool(m) and 751 <= int(m.group(1)) <= 831


total = miss = 0
misses = collections.Counter()
ex = collections.defaultdict(list)
for line in open(sys.argv[1], encoding="utf-8").read().splitlines():
    i, body = line.split("] ", 1)
    i = i[1:]
    if not mine(i):
        continue
    words = [fold(x) for x in WORD.findall(seg.get(i, ""))]
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
print(f"ch. 16: checked {total} keyword occurrences; {miss} without the termbase term ({100 * miss / max(total, 1):.1f}%)")
for (k, t), n in misses.most_common():
    print(f"{n:4d}  {k}  ->  {t}   e.g. {', '.join(ex[k])}")
