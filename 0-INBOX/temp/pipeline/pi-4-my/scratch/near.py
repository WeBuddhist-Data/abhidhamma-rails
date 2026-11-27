"""near.py: Pāli clauses (split on . ; ? – and the Burmese on ။ – where counts match per line; else on sentences)
that are identical after normalising (brackets, punctuation, case) but whose Burmese differs (after removing
brackets and ၊ ။). Shows the shared material that align_check cannot see. usage: near.py [MINLEN]"""
import pathlib, re, sys, collections
R = pathlib.Path(__file__).resolve().parents[5]
P = R / "AI_translation/pali/pi-4_split_chapters"
M = R / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
MIN = int(sys.argv[1]) if len(sys.argv) > 1 else 30
ID = re.compile(r"\s*\^[0-9A-Za-z-]+\s*$")
BR = re.compile(r"\s*\[[^\]]*\]")
SP = re.compile(r"(?:(?<=[.?;!])\s+| – )")
SM = re.compile(r"(?:(?<=[။])\s+| – )")
SP2 = re.compile(r"(?:(?<=[.?;,!])\s+| – )")
SM2 = re.compile(r"(?:(?<=[။၊])\s+| – )")
normp = lambda s: re.sub(r"[\s,;.?!\"“”'‘’–…]+", " ", BR.sub("", s)).strip().lower()
normm = lambda s: re.sub(r"[\s၊။“”–…]+", " ", BR.sub("", s)).strip()
seen = collections.defaultdict(lambda: collections.defaultdict(list))
for p in sorted(P.glob("*.md")):
    a = [l for l in p.read_text(encoding="utf-8-sig").split("\n") if l.strip()]
    b = [l for l in (M / p.name).read_text(encoding="utf-8").split("\n") if l.strip()]
    for i, (x, y) in enumerate(zip(a, b), 1):
        if x.startswith("#"): continue
        x, y = ID.sub("", x).strip(), ID.sub("", y).strip()
        for sp, sm in ((SP2, SM2), (SP, SM)):
            xs, ys = sp.split(x), sm.split(y)
            if len(xs) == len(ys):
                for s, t in zip(xs, ys):
                    k = normp(s)
                    if len(k) >= MIN: seen[k][normm(t)].append(f"{p.name.split('-')[0]}:{i}")
for k, v in sorted(seen.items()):
    if len(v) > 1:
        print("\nPĀLI:", k)
        for t, l in v.items(): print("  ", sorted(set(l))[:8], t)
print("\nnear-identical Pāli with differing Burmese:", sum(1 for v in seen.values() if len(v) > 1))
