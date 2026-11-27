"""H13 survey (read-only): Pāli runs of bare locative conditions sharing one count («… atthiyā avigate ekaṃ»):
whether the Burmese puts «၊» after the last condition before the count."""
import re, sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import my7_formulas as F
HERE = pathlib.Path(__file__).resolve().parent; R = HERE.parents[3]
pd = R / "AI_translation/pali/pi-7_split_chapters"; md = R / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
CNTW = "|".join(sorted(F.COUNT, key=len, reverse=True))
LOC = r"(?:na|no)?[a-zāīūṃ]+(?:yā|e)"
rx = re.compile(r"(?:" + LOC + r" ){1,}(?:" + LOC + r") (" + CNTW + r")\b")
c = collections.Counter(); ex = collections.defaultdict(list)
for p in sorted(pd.glob("*.md")):
    for i, (x, y) in enumerate(zip(p.read_text(encoding="utf-8-sig").split("\n"), (md / p.name).read_text(encoding="utf-8").split("\n")), 1):
        if not rx.search(x): continue
        a = len(re.findall(r"အကြောင်း(?: မဟုတ်ခြင်း)?၌၊ (?:" + "|".join(F.COUNT.values()) + r")", y))
        b = len(re.findall(r"အကြောင်း(?: မဟုတ်ခြင်း)?၌ (?:" + "|".join(F.COUNT.values()) + r")", y))
        k = "comma" if a and not b else "nocomma" if b and not a else f"mixed" if a else "?"
        c[k] += 1; ex[k].append(f"{p.name[:4]}:{i}")
for k, v in c.items(): print(v, k, sorted(set(e[:4] for e in ex[k])), ex[k][:5])
