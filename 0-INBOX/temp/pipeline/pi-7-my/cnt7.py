"""Count Burmese regex matches per chapter (pi-7 zero-shot; read-only). usage: cnt7.py REGEX [REGEX ...]"""
import pathlib, re, sys, collections
HERE = pathlib.Path(__file__).resolve().parent
MD = HERE.parents[3] / "AI_translation/burmese/pi-7-burmese-plain-zeroshot_split_chapters"
for r in sys.argv[1:]:
    c = collections.Counter(); forms = collections.Counter()
    for p in sorted(MD.glob("*.md")):
        for m in re.finditer(r, p.read_text(encoding="utf-8")):
            c[p.name[:4]] += 1; forms[m[0]] += 1
    print(f"«{r}»: {sum(c.values())} {dict(c)}")
    if len(forms) > 1:
        for f, n in forms.most_common(12): print(f"     {n} «{f}»")
