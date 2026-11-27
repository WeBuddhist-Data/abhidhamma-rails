"""pi-3 rails, sense-level cross-check (stricter than the loose adherence test): every value of the zero-shot keyword
map (the zero-shot's own form of each keyword in each segment) must be a term of that keyword's termbase entry, or
else be (a) a non-chosen candidate of one of the multi-candidate decisions (termbase/decisions-A.tsv, candidates from the
table of termbase/termbase-decisions.md; the fragments / gaps the decision reasons name) or (b) «(no direct equivalent)» of a keyword without an entry. Anything else would be
a GENUINE difference the loose test could hide.
usage: python3 -I -X utf8 map_vs_termbase.py   (exit 1 on an unexplained value)"""
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

N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
TB = ROOT / "AI_translation/burmese/pi-3-pali-burmese-termbase-plain.md"
KMAP = ROOT / "AI_translation/burmese/pi-3-keywords-by-reference-pali-burmese-plain.md"
DEC = HERE.parent / "termbase/decisions-A.tsv"
REP = HERE.parent / "termbase/termbase-decisions.md"
tb = A.parse_termbase(TB)
cands = collections.defaultdict(set)          # decided headword (lower) -> candidates (termbase-decisions.md table)
decided = {N(l).split("\t")[0].split("|")[0].lower() for l in open(DEC, encoding="utf-8") if "|" in l.split("\t")[0]
           and not l.startswith("#")}
for l in open(REP, encoding="utf-8"):
    f = [x.strip() for x in N(l).split(" | ")]
    if len(f) == 4 and " → " in f[2] and f[0].lower() in decided:
        cands[f[0].lower()].update(x.strip() for x in f[2].split(" → ")[0].split(" / "))
if set(cands) != decided:
    raise SystemExit(f"decision table: {sorted(cands)} vs decisions-A {sorted(decided)}")
n, c, bad = 0, collections.Counter(), []
for l in open(KMAP, encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if not m:
        continue
    for x in m.group(2).split(", "):
        if "=" not in x:
            continue
        k, v = x.split("=", 1)
        n += 1
        t = tb.get(k.lower())
        if t is not None and v in t:
            continue
        if t is None and v.startswith("(no direct"):
            c["no entry, (no direct equivalent)"] += 1
        elif t is not None and v in cands.get(k.lower(), ()):
            c[f"decided {k}: non-chosen «{v}»"] += 1
        else:
            bad.append(f"{m.group(1)} {k}={v} | termbase: {' | '.join(t or ['(no entry)'])}")
print(f"keyword-map values: {n}; = a termbase term: {n - sum(c.values()) - len(bad)}; explained: {sum(c.values())}; "
      f"unexplained: {len(bad)}")
for k, v in sorted(c.items()):
    print(f"   {v}\t{k}")
for b in bad:
    print("UNEXPLAINED", b)
sys.exit(1 if bad else 0)
