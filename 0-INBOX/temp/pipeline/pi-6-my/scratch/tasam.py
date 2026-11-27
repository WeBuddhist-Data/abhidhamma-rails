import pathlib, re, collections
HERE = pathlib.Path(__file__).resolve().parents[1]; ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"; MD = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
ID = re.compile(r" (\^[0-9A-Za-z-]+)\s*$")
sp = lambda l: [s for s in re.split(r"(?<=[.?]) (?=\S)", ID.sub("", l)) if s]
bs = lambda l: [s for s in re.split(r"(?<=။) ", ID.sub("", l)) if s]
c = collections.Counter()
for p in sorted(PD.glob("*.md")):
    A = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(A, B), 1):
        P, Q = sp(x), bs(y)
        if len(P) != len(Q): continue
        for s, t in zip(P, Q):
            if "tāsaṃ" in s or "tesaṃ" in s:
                k = (p.name[:5], "tāsaṃ" in s, "tesaṃ" in s, "ထိုမိန်းမတို့" in t, t.count("ထိုသူတို့"))
                if ("tāsaṃ" in s and "tesaṃ" not in s and "ထိုသူတို့" in t) or ("tāsaṃ" not in s and "ထိုမိန်းမတို့" in t):
                    c[(p.name[:5], s[:120], t[:200])] += 1
for k, n in list(c.items())[:20]: print(n, k)
print(len(c))
