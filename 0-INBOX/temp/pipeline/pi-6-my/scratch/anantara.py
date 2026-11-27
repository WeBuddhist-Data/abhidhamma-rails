import pathlib, re, collections, sys
HERE = pathlib.Path(__file__).resolve().parents[1]; ROOT = HERE.parents[3]
PD = ROOT / "AI_translation/pali/pi-6_split_chapters"; MD = ROOT / "AI_translation/burmese/pi-6-burmese-plain-zeroshot_split_chapters"
rx = re.compile(r"[Yy]assa cittassa anantarā \S+ \S+(?: tassa cittassa \S+)?")
c = collections.defaultdict(collections.Counter)
for p in sorted(PD.glob("*.md")):
    A = [l for l in p.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    B = [l for l in (MD / p.name).read_text(encoding="utf-8").splitlines() if l.strip()]
    for i, (x, y) in enumerate(zip(A, B), 1):
        for m in rx.finditer(x):
            for q in re.findall(r"(?:မိမိ |အကြင်)?စိတ်၏ ချက်ချင်း နောက်၌ [^၊။]*?(?:သူတို့|၊ ထိုစိတ်၏ \S+ ခဏ၌|ခဏ၌ ရှိသူတို့)", y):
                c[m[0]][q] += 1
for k, v in sorted(c.items()):
    print(k); [print("   ", n, q) for q, n in v.most_common()]
