import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402
# usage: peek2_5-05_5-12.py <file-prefix> <nonempty line> ...   (prints Pāli and Hindi)
pre = sys.argv[1]
f = next(p.name for p in S.PALI_DIR.iterdir() if p.name.startswith(pre))
pl = S.nonempty((S.PALI_DIR / f).read_text(encoding="utf-8"))
hl = S.nonempty((S.HI_DIR / f).read_text(encoding="utf-8"))
for a in sys.argv[2:]:
    n = int(a)
    print(f"--- {f} {n}\nP: {pl[n - 1]}\nH: {hl[n - 1]}")
