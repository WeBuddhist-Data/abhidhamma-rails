"""Inspection helper (read only): a STRICTER adherence view than adherence_my.py. For every keyword use of the Pāli
keyword file, the termbase terms are tested unstemmed: a term passes if its « … »-separated pieces occur as exact
substrings, in order, in the segment. Prints per keyword: uses, strict misses, and the segment ids of the misses.
usage: strict_scan.py <burmese split dir> [--ids]"""
import collections
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402

KW = ROOT / "AI_translation/pali/pi-3-keywords-by-reference-pali-plain.md"
TB = ROOT / "AI_translation/burmese/pi-3-pali-burmese-termbase-plain.md"
N = lambda s: unicodedata.normalize("NFC", s)


def strict(term, text):
    pos = 0
    for piece in [p.strip() for p in term.split("…") if p.strip()]:
        k = text.find(piece, pos)
        if k < 0:
            return False
        pos = k + len(piece)
    return True


tb, segs = A.parse_termbase(TB), A.segments(sys.argv[1])
uses, miss = collections.Counter(), collections.defaultdict(list)
for l in open(KW, encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if not m or m.group(1) not in segs:
        continue
    for kw in m.group(2).split(", "):
        terms = tb.get(kw.strip().lower())
        if not terms:
            continue
        uses[kw] += 1
        if not any(strict(t, segs[m.group(1)]) for t in terms):
            miss[kw].append(m.group(1))
print(f"strict misses: {sum(len(v) for v in miss.values())} in {len(miss)} keywords")
for kw, ids in sorted(miss.items(), key=lambda x: -len(x[1])):
    print(f"{len(ids)}/{uses[kw]}\t{kw}\t{' | '.join(tb[kw.lower()])}" + (f"\t{' '.join(ids[:12])}" if "--ids" in sys.argv else ""))
