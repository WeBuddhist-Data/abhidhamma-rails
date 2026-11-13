"""Check 4-02..4-07 Hindi: Latin words outside variant brackets / block IDs, CR, double blank lines."""
import pathlib, re

H = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters")
FILES = ["4-02-dukatika-hetuduka.md", "4-03-dukatika-sahetukaduka.md", "4-04-dukatika-sappaccayaduka.md",
         "4-05-dukatika-asavaduka.md", "4-06-dukatika-sannojanaduka.md", "4-07-dukatika-ganthaduka.md"]
for f in FILES:
    raw = (H / f).read_bytes()
    t = raw.decode("utf-8")
    bad = []
    for n, line in enumerate(t.splitlines(), 1):
        x = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", line)
        x = re.sub(r"\[[^\]]*\]", "", x)
        if re.search(r"[A-Za-zāīūṃṅñṭḍṇḷ]", x):
            bad.append(n)
    print(f, "latin:", bad[:10], "CR:", b"\r" in raw, "double-blank:", "\n\n\n" in t,
          "em-dash:", "—" in t, "':-':", ":-" in t, "'?':", t.count("?"))
