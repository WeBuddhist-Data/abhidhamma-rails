"""H19 survey (read-only): «<condition stem>sadis-» without «paccaya» (bare) vs with «paccaya»: the Burmese form
of the compared condition («N-နှင့် တူ» bare / «Nဟူသော အကြောင်းနှင့် တူ» full)."""
import re, sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
HERE = pathlib.Path(__file__).resolve().parent; R = HERE.parents[3]
pd = R / "AI_translation/pali/pi-7_split_chapters"; md = R / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
import my7_formulas as F
STEMS = sorted(F.STEMS, key=len, reverse=True)
c = collections.Counter(); ex = collections.defaultdict(list)
for p in sorted(pd.glob("*.md")):
    for i, (x, y) in enumerate(zip(p.read_text(encoding="utf-8-sig").split("\n"), (md / p.name).read_text(encoding="utf-8").split("\n")), 1):
        for m in re.finditer(r"(?:na|no)?(" + "|".join(STEMS) + r")(paccaya)?sadis", x):
            st, pc = m[1], bool(m[2])
            n = F.N.get(st)
            if not n: continue
            full = (n + "ဟူသော အကြောင်း") in y and re.search(re.escape(n) + r"ဟူသော အကြောင်း(?: မဟုတ်ခြင်း)?နှင့် တူ", y)
            bare = re.search(re.escape(n) + r"(?: မဟုတ်ခြင်း)?နှင့် တူ", y)
            k = ("paccaya" if pc else "bare-pali", st, "full" if full and not bare else "bare" if bare and not full else "both" if full else "?")
            c[k] += 1; ex[k].append(f"{p.name[:4]}:{i}")
for k, v in sorted(c.items()):
    print(v, k, sorted(set(e[:4] for e in ex[k])), ex[k][:4])
