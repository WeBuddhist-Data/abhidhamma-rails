"""work helper: for every miss group (keyword, zero-shot map form) the source lines holding that form."""
import collections, pathlib, re, sys, unicodedata
HERE = pathlib.Path(__file__).resolve().parents[1]
ROOT = HERE.parents[4]
N = lambda s: unicodedata.normalize("NFC", s)
kv = {}
for l in open(ROOT / "AI_translation/burmese/pi-5-keywords-by-reference-pali-burmese-plain.md", encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m:
        for x in m.group(2).split(", "):
            if "=" in x:
                k, v = x.split("=", 1); kv[(m.group(1), k)] = v
SRC = {}
for f in ["my5_formulas.py", "make_sample.py", "make_ch2-5.py", "make_ch6-10.py", "make_ch11-12.py", "make_ch13-16.py",
          "make_ch17-20.py", "make_ch21-25.py", "make_ch26-31.py"]:
    SRC[f] = [N(l) for l in (HERE.parent / f).read_text(encoding="utf-8").splitlines()]
g = collections.defaultdict(list)
for l in open(HERE / (sys.argv[1] if len(sys.argv) > 1 else "adherence-zeroshot.txt"), encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) == 3 and f[0][:1].isdigit():
        g[(f[1], kv.get((f[0], f[1]), ""), f[2])].append(f[0])
for (kw, form, term), ids in sorted(g.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f"## {kw} «{form}» → «{term}» ×{len(ids)}: {' '.join(ids[:12])}")
    if not form or form.startswith("("):
        continue
    probe = [c for c in re.split(r" … ", form) if c]
    n = 0
    for f, ls in SRC.items():
        for k, l in enumerate(ls, 1):
            if all(c in l for c in probe):
                n += 1
                if n <= 4:
                    print(f"     {f}:{k}: {l.strip()[:160]}")
    if n > 4:
        print(f"     … {n} source lines")
