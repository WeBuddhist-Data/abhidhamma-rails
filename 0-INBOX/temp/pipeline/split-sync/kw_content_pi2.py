import pathlib, re, unicodedata
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
ID = re.compile(r"\s\^([0-9A-Za-z-]+)\s*$"); KW = re.compile(r"^\[([^\]]+)\]\s*(.*)$")
norm = lambda s: unicodedata.normalize("NFC", s).lower()
for n in (2,):
    text = (B / f"1-SOURCES/Text/pi-{n}.md").read_text(encoding="utf-8")
    blocks, buf = {}, []
    for l in text.splitlines():
        if not l.strip():
            continue
        buf.append(l)
        m = ID.search(l)
        if m:
            blocks[m.group(1)] = norm(" ".join(buf)); buf = []
    tot = hit = 0; worst = []
    for l in (B / f"AI_translation/pali/pi-{n}-keywords-by-reference-pali-plain.md").read_text(encoding="utf-8-sig").splitlines():
        m = KW.match(l)
        if not m: continue
        kws = [k.strip() for k in m.group(2).split(",") if k.strip()]
        b = blocks.get(m.group(1), "")
        # a keyword counts as found if its stem (minus the last 2 letters) occurs in the block
        f = sum(1 for k in kws if norm(k)[:max(3, len(k) - 2)] in b or all(w[:max(3, len(w) - 2)] in b for w in norm(k).split()))
        tot += len(kws); hit += f
        if kws and f / len(kws) < 0.5:
            worst.append((m.group(1), f, len(kws)))
    print(f"pi-{n}: keywords found in their block {hit}/{tot} ({100*hit/max(tot,1):.1f}%); lines under 50%: {len(worst)} {worst[:8]}")
    if False:
        for u in ['7-U292', '7-U300', '7-U432']:
            print("   ", u, blocks[u][:120])

