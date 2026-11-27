"""Inspection helper (read only): where a Burmese string comes from. Prints its occurrences in my5_formulas.py and the
generators (file:line: text) and the zero-shot segments that hold it (id: Pāli excerpt).
usage: where.py <burmese string> [--seg N] [--pali REGEX]"""
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
s = N(sys.argv[1])
mx = int(sys.argv[sys.argv.index("--seg") + 1]) if "--seg" in sys.argv else 8
prx = re.compile(sys.argv[sys.argv.index("--pali") + 1]) if "--pali" in sys.argv else None
for f in ["my5_formulas.py", "make_sample.py", "make_ch2-5.py", "make_ch6-10.py", "make_ch11-12.py", "make_ch13-16.py",
          "make_ch17-20.py", "make_ch21-25.py", "make_ch26-31.py"]:
    for k, l in enumerate((HERE.parent / f).read_text(encoding="utf-8").splitlines(), 1):
        if s in N(l):
            print(f"{f}:{k}: {l.strip()[:220]}")
P = A.segments(ROOT / "AI_translation/pali/pi-5_split_chapters")
Z = A.segments(ROOT / "AI_translation/burmese/pi-5-burmese-plain-zeroshot_split_chapters")
hits = [i for i, t in Z.items() if s in t and (prx is None or prx.search(P.get(i, "")))]
print(f"-- {len(hits)} zero-shot segments, {sum(Z[i].count(s) for i in hits)} occurrences:", " ".join(hits[:60]))
for i in hits[:mx]:
    z = Z[i]
    k = z.find(s)
    print(f"   [{i}] Z: …{z[max(0, k - 120):k + len(s) + 80]}…")
    print(f"   [{i}] P: {P.get(i, '')[:300]}")
