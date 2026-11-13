import re, pathlib
d = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters")
for i in range(7, 14):
    f = d / f"10-{i:02d}-indriyayamaka.md"
    b = f.read_bytes(); t = b.decode("utf-8")
    lat = set()
    for l in t.splitlines():
        l2 = re.sub(r"\[[^\]]*\]", "", l)
        l2 = re.sub(r"\^[0-9A-Za-z-]+", "", l2)
        lat |= set(re.findall(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", l2))
    print(f.name, "CR" if b"\r" in b else "noCR", "double-blank" if "\n\n\n" in t else "ok", sorted(lat)[:10], ":-" in t, "seed" in t.lower())
