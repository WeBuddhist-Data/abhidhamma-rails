"""Inspection helper (read only; model pi-4-my/rails/ctx.py): for each adherence miss of the given keyword(s), the
keyword-map form and a window of the Pāli (around the keyword) and of the Burmese (around the map form).
usage: ctx.py <keyword regex> [--rails] [--w N]"""
import pathlib
import re
import sys
import unicodedata

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import adherence_my as A  # noqa: E402

N = lambda s: unicodedata.normalize("NFC", s)  # noqa: E731
w = int(sys.argv[sys.argv.index("--w") + 1]) if "--w" in sys.argv else 70
rails = "--rails" in sys.argv
P = A.segments(ROOT / "AI_translation/pali/pi-5_split_chapters")
Z = A.segments(ROOT / ("AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters" if rails else
                       "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters"))
kv = {}
for l in open(ROOT / "AI_translation/burmese/pi-5-keywords-by-reference-pali-burmese-plain.md", encoding="utf-8"):
    m = re.match(r"^\[([^\]]+)\] (.*)$", N(l.strip()))
    if m:
        for x in m.group(2).split(", "):
            if "=" in x:
                k, v = x.split("=", 1)
                kv[(m.group(1), k)] = v
rx = re.compile(sys.argv[1])
for l in open(HERE / ("adherence-rails.txt" if rails else "adherence-zeroshot.txt"), encoding="utf-8"):
    f = N(l).strip().split("\t")
    if len(f) != 3 or not f[0][:1].isdigit() or not rx.fullmatch(f[1]):
        continue
    i, kw, term = f
    p, z, form = P[i], Z[i], kv.get((i, kw), "")
    k = p.lower().find(kw.lower())
    first = form.split(" … ")[0] if form and not form.startswith("(") else ""
    j = z.find(first) if first else -1
    print(f"[{i}] {kw} «{form}» → «{term}»")
    print("   P: …" + p[max(0, k - w):k + len(kw) + w] + "…")
    print("   B: …" + (z[max(0, j - w):j + len(first) + w] if j >= 0 else z[:2 * w]) + "…")
