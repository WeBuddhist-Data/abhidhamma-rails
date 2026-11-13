import sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S  # noqa: E402

FILES = ["5-05-paccaniya-dukatika.md", "5-06-paccaniya-tikaduka.md", "5-07-paccaniya-tikatika.md",
         "5-08-paccaniya-dukaduka.md", "5-09-anulomapaccaniya-tika.md", "5-10-anulomapaccaniya-duka.md",
         "5-11-anulomapaccaniya-dukatika.md", "5-12-anulomapaccaniya-tikaduka.md"]
bad = S.check([(S.PALI_DIR / f, S.HI_DIR / f) for f in FILES])
for f in FILES:
    t = (S.HI_DIR / f).read_text(encoding="utf-8")
    for n, l in enumerate(t.splitlines(), 1):
        if "FAIL" in l or "  " in l or l != l.strip() and l.strip():
            print(f, n, "suspicious:", l[:100])
sys.exit(1 if bad else 0)
