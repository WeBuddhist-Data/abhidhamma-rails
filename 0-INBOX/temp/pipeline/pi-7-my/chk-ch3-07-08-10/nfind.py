import sys, re, pathlib, subprocess
ROOT = pathlib.Path(sys.argv[1]).resolve().parents[3]; AI = ROOT / "AI_translation"
notes = [l.split(") ", 1)[1] for l in open(sys.argv[2], encoding="utf-8") if l.startswith("('")]
skip = {"3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md", "3-10-upadanagocchaka.md"}
pairs = []
for pf in sorted((AI / "pali/pi-7_split_chapters").glob("*.md")):
    mf = AI / "burmese/pi-7-burmese-plain-zeroshot_split_chapters" / pf.name
    if not mf.exists() or pf.name in skip: continue
    pl = [l for l in pf.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    ml = [l for l in mf.read_text(encoding="utf-8-sig").splitlines() if l.strip()]
    if len(pl) == len(ml): pairs += [(pf.name, a, b) for a, b in zip(pl, ml)]
for n in notes:
    norm = lambda s: re.sub(r"\s+", " ", re.sub(r"\{[^{}]*\}", "", s)).lower()
    hits = [(f, a, b) for f, a, b in pairs if norm(n) in norm(a)]
    if hits:
        f, a, b = hits[0]
        pa = re.findall(r"\([^()]*\)", re.sub(r"\{[^{}]*\}", "", a)); pb = re.findall(r"\([^()]*\)", re.sub(r"\{[^{}]*\}", "", b))
        i = [norm(x) for x in pa].index(norm(n)) if norm(n) in [norm(x) for x in pa] else None
        print(f"{n}\n   [{f}] {pb[i] if i is not None and len(pa)==len(pb) else b[:300]}")
