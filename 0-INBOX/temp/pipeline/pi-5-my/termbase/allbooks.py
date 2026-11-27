"""For every pi-5 sense (or only multi-candidate ones with --multi), the terms of ALL four locked books for the same headword
(case-insensitive) and the same tag (tag) or any tag (other). usage: allbooks.py [--multi] [--diff] [hw|i ...]"""
import sys, pathlib, collections
B = pathlib.Path(__file__).resolve().parents[5]
def parse(p):
    d = collections.defaultdict(list)
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        hw, body = line.split(": {", 1)
        d[hw.lower()] += [tuple(s.rsplit(": ", 1)) for s in body[:-1].split("; ")]
    return d
L = [(f"pi-{n}", parse(B / f"AI_translation/burmese/pi-{n}-pali-burmese-termbase-plain.md")) for n in (4, 3, 2, 1)]
a = sys.argv[1:]; multi = "--multi" in a; diff = "--diff" in a; keys = [x for x in a if not x.startswith("--")]
for line in (B / "AI_translation/burmese/pi-5-pali-word-burmese-senses-plain.md").read_text(encoding="utf-8").splitlines():
    hw, body = line.split(": {", 1)
    for i, s in enumerate(body[:-1].split("; ")):
        tag, c = s.rsplit(": ", 1); cl = c.split(" / ")
        k = f"{hw}|{i}"
        if keys and k not in keys: continue
        if multi and len(cl) < 2: continue
        same = [(b, tm) for b, d in L for tg, tm in d.get(hw.lower(), []) if tg == tag]
        if diff and len(set(tm for _, tm in same)) < 2: continue
        if not same: continue
        print(f"{k}: {c}  ||  " + "  ".join(f"{b}={tm}" for b, tm in same))
