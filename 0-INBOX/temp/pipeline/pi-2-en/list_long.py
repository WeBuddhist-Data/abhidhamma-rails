import pathlib, collections
M = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\0-INBOX\temp\pipeline\pi-2-en\mapper")
c = collections.Counter()
for p in M.glob("*.mapped.md"):
    for l in p.read_text(encoding="utf-8-sig").splitlines():
        if "] " not in l: continue
        for q in l.split("] ", 1)[1].split(", "):
            pv, en = q.rsplit("=", 1)
            if pv != "(no direct equivalent)" and any(len(x.split()) >= 4 for x in pv.split(" / ")):
                c[(pv, en)] += 1
for (pv, en), n in sorted(c.items(), key=lambda x: -x[1]):
    print(n, "|", pv, "=", en)
