"""H14 survey (read-only): sentences with «evaṃ» but no «yathā»: the Burmese adverb used (ဤသို့ / ထိုနည်းတူ)."""
import re, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent; R = HERE.parents[3]
pd = R / "AI_translation/pali/pi-7_split_chapters"; md = R / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
c = collections.Counter(); ex = {}
for p in sorted(pd.glob("*.md")):
    for i, (x, y) in enumerate(zip(p.read_text(encoding="utf-8-sig").split("\n"), (md / p.name).read_text(encoding="utf-8").split("\n")), 1):
        for m in re.finditer(r"\(([^()]*\bevaṃ\b[^()]*)\)", x):
            s = m[1]
            yat = bool(re.search(r"[Yy]athā|seyyathā", s))
            words = re.findall(r"evaṃ \w+", s)
            n1, n2 = y.count("ဤသို့"), y.count("ထိုနည်းတူ")
            k = ("yathā" if yat else "bare", " ".join(words), "ဤသို့" if n1 and not n2 else "ထိုနည်းတူ" if n2 and not n1 else f"mixed{n1}/{n2}")
            c[k] += 1; ex.setdefault(k, []).append(f"{p.name[:4]}:{i}")
for k, v in sorted(c.items()):
    print(v, k, ex[k][:6], sorted(set(e[:4] for e in ex[k])))
