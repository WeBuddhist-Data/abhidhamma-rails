"""Check pi-7 mapped files: same ids/keywords as the keyword files, no Latin / ", " / dash in values.

usage: python -I -B -X utf8 verify_map7.py <part> [<part> …]   (or 'all')
"""
import pathlib, re, sys

D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-7-hi\mapper-hi")
LATIN = re.compile(r"[A-Za-zāīūṃṅñṭḍṇḷ]")
NDE = "(no direct equivalent)"
parts = sys.argv[1:]
if parts == ["all"]:
    parts = sorted(p.name[:-len(".keywords.md")] for p in D.glob("*.keywords.md"))
tot_nde = 0
for part in parts:
    kf, mf = D / f"{part}.keywords.md", D / f"{part}.mapped.md"
    if not mf.exists():
        print(part, "MISSING"); continue
    a = [l.split("] ", 1) for l in kf.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    b = [l.split("] ", 1) for l in mf.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    bad, vals, nde = [], [], 0
    if [x[0] for x in a] != [x[0] for x in b]:
        print(part, "ID ORDER DIFFERS"); continue
    for x, y in zip(a, b):
        kws = [k.strip() for k in x[1].split(", ")] if len(x) > 1 else []
        pairs = [q.split("=", 1) for q in y[1].split(", ")] if len(y) > 1 else []
        if kws != [p[0] for p in pairs] or any(len(p) != 2 for p in pairs):
            bad.append(x[0]); continue
        for k, v in pairs:
            if v == NDE:
                nde += 1
            elif LATIN.search(v) or "—" in v or "–" in v or not v.strip():
                vals.append((x[0], k, v))
    tot_nde += nde
    print(part, "lines", len(a), "bad", bad[:5], "bad values", vals[:5], "NDE", nde)
print("total NDE", tot_nde)
