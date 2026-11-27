import pathlib, re, sys, unicodedata
H = pathlib.Path(__file__).resolve().parents[1]; ROOT = H.parents[4]
sys.path.insert(0, str(H)); sys.dont_write_bytecode = True
import adherence_my as A
N = lambda s: unicodedata.normalize("NFC", s)
P = A.segments(ROOT / "AI_translation/pali/pi-5_split_chapters")
R = A.segments(ROOT / "AI_translation/burmese/pi-5-burmese-plain-rails_split_chapters")
tb = A.parse_termbase(ROOT / "AI_translation/burmese/pi-5-pali-burmese-termbase-plain.md")
w = int(sys.argv[1]) if len(sys.argv) > 1 else 25
for l in open(H / "adherence-classified.tsv", encoding="utf-8"):
    f = N(l).rstrip("\n").split("\t")
    if len(f) < 8 or f[4] != "UNVERIFIED": continue
    i, kw, old = f[0], f[1], f[3]
    p = P[i]; k = p.lower().find(kw.lower().split()[0][:6])
    b = R[i]; first = old.split(" … ")[0] if old and not old.startswith("(") else ""
    j = b.find(first) if first else -1
    print(f"[{i}] {kw} «{old}» TB {' | '.join(tb.get(kw.lower(), []))}\n  P …{p[max(0,k-w):k+len(kw)+w]}…\n  B …{b[max(0,j-w):j+len(first)+w] if j>=0 else '(form not found)'}…")
