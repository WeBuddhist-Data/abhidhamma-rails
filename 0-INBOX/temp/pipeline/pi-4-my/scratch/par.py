"""par.py PALI_REGEX [MY_REGEX] [-c chapters-prefix] : show Pāli / Burmese line pairs (pi-4) matching."""
import pathlib, re, sys
R = pathlib.Path(__file__).resolve().parents[5]
P = R / "AI_translation/pali/pi-4_split_chapters"
M = R / "AI_translation/burmese/pi-4-burmese-plain-zeroshot_split_chapters"
a = [x for x in sys.argv[1:] if not x.startswith("-")]
pr = re.compile(a[0]) if a and a[0] else None
mr = re.compile(a[1]) if len(a) > 1 else None
full = "-f" in sys.argv
for p in sorted(P.glob("*.md")):
    x = p.read_text(encoding="utf-8-sig").split("\n"); y = (M / p.name).read_text(encoding="utf-8").split("\n")
    for i, (s, t) in enumerate(zip(x, y), 1):
        if (pr is None or pr.search(s)) and (mr is None or mr.search(t)):
            print(f"{p.name.split('-')[0]}:{i}\n  P: {s}\n  M: {t}")
