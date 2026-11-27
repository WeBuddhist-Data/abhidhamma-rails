"""For pi-6 senses with no tag match in pi-5 / pi-4 / pi-3 / pi-2 / pi-1 (SINGLE_NEW / MULTI_NEW in pi12345-match.tsv): show the locked senses of the
same headword (case-insensitive) when the locked term differs from the pi-6 candidate(s). usage: newcheck.py"""
import pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
def parse(p):
    d = collections.defaultdict(list)
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        hw, body = line.split(": {", 1)
        d[hw.lower()] += [tuple(s.rsplit(": ", 1)) for s in body[:-1].split("; ")]
    return d
L = [("pi-5", parse(B / "AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md")), ("pi-4", parse(B / "AI_translation/burmese/pi-4-pali-burmese-termbase-plain.md")), ("pi-3", parse(B / "AI_translation/burmese/pi-3-pali-burmese-termbase-plain.md")), ("pi-2", parse(B / "AI_translation/burmese/pi-2-pali-burmese-termbase-plain.md")),
     ("pi-1", parse(B / "AI_translation/burmese/pi-1-pali-burmese-termbase-plain.md"))]
n = 0
for r in pathlib.Path(__file__).with_name("pi12345-match.tsv").read_text(encoding="utf-8").splitlines():
    cat, key, cands, _, _, _, tag = r.split("\t")
    if cat not in ("SINGLE_NEW", "MULTI_NEW"): continue
    hw = key.rsplit("|", 1)[0]
    cl = cands.split(" / ")
    hits = [(b, tg, tm) for b, d in L for tg, tm in d.get(hw.lower(), [])]
    if not hits: continue
    if all(tm in cl for _, _, tm in hits): continue
    n += 1
    print(f"{key}: {cands}   [{tag[:80]}]")
    for b, tg, tm in hits: print(f"      {b}: {tm}   [{tg[:90]}]")
print(n, "headwords to judge")
