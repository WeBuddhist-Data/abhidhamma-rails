import pathlib, re, collections, sys
HERE = pathlib.Path(__file__).resolve().parents[1]; ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"; MD = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
nobr = lambda s: re.sub(r"\[[^\]]*\]", "", s)
RULES = [("kāma", r"(?i)kāmāvacar|kāmadhātu", "ကာမဘုံ"),
         ("rūpa", r"(?i)(?<![Aa])rūpāvacar|(?<![Aa])rūpadhātu", "သိမ်မွေ့သော ရုပ်ဘုံ"),
         ("arūpa", r"(?i)arūpāvacar|arūpadhātu|\barūp(?:e|aṃ|ānaṃ|ā|abhav\w*)\b", "ရုပ်မရှိသော ဘုံ")]
c = collections.Counter(); ex = collections.defaultdict(list)
for p in sorted(PD.glob("*.md")):
    A = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(A, B), 1):
        x, y = nobr(x), nobr(y)
        for k, rx, my in RULES:
            a, b = len(re.findall(rx, x)), y.count(my)
            if k == "kāma": b = b  # adjectival «ကာမဘုံနှင့် ဆိုင်သော» also contains it
            if a != b:
                c[(p.name[:5], k, a - b)] += 1; ex[(p.name[:5], k, a - b)].append((i, x[:150], y[:220]))
for k, n in sorted(c.items()):
    print(n, k); [print("    ", e) for e in ex[k][:2]]
