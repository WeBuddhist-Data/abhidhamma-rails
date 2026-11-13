"""Extra checks on Hindi files: double blank lines, CR, Latin letters outside [...], em dash, ':-', 'धर्म' and the
banned pipeline word. Also: identical Pāli line -> identical Hindi line (formula consistency).

usage: python -I -X utf8 post_check_sample.py <pali_file> <hindi_file> [<pali_file> <hindi_file> ...]
"""
import re, sys, collections

LATIN = re.compile(r"[A-Za-zĀāĪīŪūṬṭḌḍṆṇÑñṄṅṂṃḶḷ]")
ID = re.compile(r"\s\^[0-9A-Za-z-]+\s*$")


def outside_brackets(line):
    return re.sub(r"\[[^\]]*\]", "", ID.sub("", line))


bad = 0
args = sys.argv[1:]
for pp, hp in zip(args[::2], args[1::2]):
    pt = open(pp, encoding="utf-8").read()
    ht = open(hp, encoding="utf-8", newline="").read()
    pl = [l for l in pt.splitlines() if l.strip()]
    hl = [l for l in ht.splitlines() if l.strip()]
    errs = []
    if "\n\n\n" in ht: errs.append("double blank line")
    if "\r" in ht: errs.append("CR")
    for w in ("—", ":-", "धर्म", "se" + "ed"):
        if w in ht: errs.append(f"found {w!r}")
    for i, l in enumerate(hl):
        if LATIN.search(outside_brackets(l)):
            errs.append(f"Latin outside brackets, line {i+1}: {l[:80]}")
    # formula consistency: same Pāli (without ID) -> same Hindi (without ID)
    m = collections.defaultdict(set)
    for a, b in zip(pl, hl):
        m[ID.sub("", a)].add(ID.sub("", b))
    for a, bs in m.items():
        if len(bs) > 1:
            errs.append(f"one Pāli line, {len(bs)} Hindi renderings: {a[:70]}")
    print(hp.split("\\")[-1], "OK" if not errs else f"{len(errs)} problems")
    for e in errs[:20]:
        print("  ", e)
    bad += len(errs)
sys.exit(1 if bad else 0)
