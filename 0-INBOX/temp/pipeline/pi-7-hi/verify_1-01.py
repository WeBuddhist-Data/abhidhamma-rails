"""Extra checks for 1-01-kusalattika.md Hindi: sample lines byte-identical, Latin, CR, double blanks."""
import re, sys
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S

ht = (S.HI_DIR / "1-01-kusalattika.md").read_bytes().decode("utf-8")
H = [l for l in ht.splitlines() if l.strip()]
bad = 0
for name, a, b in (("s2-paticca-anuloma", 1, 128), ("s3-paticca-paccaniya", 129, 190), ("s4-panha", 1235, 1262)):
    smp = [l for l in (S.SAMPLE_DIR / f"{name}.md").read_text(encoding="utf-8").splitlines() if l.strip()]
    mine = H[a - 1:b]
    diff = [i for i, (x, y) in enumerate(zip(smp, mine)) if x != y]
    print(name, len(smp), len(mine), "diffs", len(diff), diff[:5])
    bad += bool(diff) or len(smp) != len(mine)
lat = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")
var = re.compile(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]")
for i, l in enumerate(H, 1):
    body = S.ID_RX.sub("", var.sub("", l))
    m = lat.search(body)
    if m:
        print("Latin", i, m.group(0)); bad += 1
    if "—" in l or ":-" in l or "?" in l and "क्या" not in l:
        print("punct", i, l[:80]); bad += 1
print("CR", "\r" in ht, "double blank", "\n\n\n" in ht, "ends ok", ht.endswith("\n") and not ht.endswith("\n\n"))
print("BAD" if bad else "ALL OK")
