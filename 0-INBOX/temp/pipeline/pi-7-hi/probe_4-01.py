import sys, re, pathlib, collections
sys.path.insert(0, r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi")
import build_sample_hi as S
p = S.PALI_DIR / "4-01-kilesagocchaka.md"
lines = [l for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
heads, counts, other = [], [], []
for i, l in enumerate(lines, 1):
    b = S.ID_RX.sub("", l)
    if b.startswith("#"):
        heads.append(b)
        continue
    try:
        S.count_hi(b)
        counts.append((i, b))
        continue
    except Exception:
        pass
    other.append((i, b))
print("heads", len(heads), "unique", len(set(re.sub(r"^#+ ", "", h) for h in heads)))
print("counts", len(counts))
print("other", len(other))
segs = collections.Counter()
for i, b in other:
    for s in re.split(r" – |\. |; |…pe…|…", b):
        s = s.strip(" .,;")
        if s:
            segs[s] += 1
print("unique segs", len(segs), "total", sum(segs.values()))
if len(sys.argv) > 1 and sys.argv[1] == "heads":
    for h in sorted(set(re.sub(r"^#+ ", "", h) for h in heads)):
        print(h)
if len(sys.argv) > 1 and sys.argv[1] == "other":
    for i, b in other:
        print(i, b[:200])
