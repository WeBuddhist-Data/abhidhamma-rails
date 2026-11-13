r"""Helper: Latin words outside variant brackets, double blank lines, CR, for the 10-01..10-06 Hindi files."""
import pathlib, re, sys
D = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters")
for n in sys.argv[1:] or [f"10-{i:02d}" for i in range(1, 7)]:
    f = D / f"{n}-indriyayamaka.md"
    raw = f.read_bytes()
    t = raw.decode("utf-8")
    bad = []
    for i, l in enumerate(t.split("\n"), 1):
        s = re.sub(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]", "", l)
        s = re.sub(r"\^[0-9A-Za-z-]+", "", s)
        if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]{2,}", s):
            bad.append(i)
    print(f.name, "CR" if b"\r" in raw else "noCR", "double-blank" if "\n\n\n" in t else "ok-blanks",
          "latin lines:", bad[:10])
