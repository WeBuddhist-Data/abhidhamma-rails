"""Extra checks for the Hindi files 3-03..3-08: Latin left, odd spacing, CR, double blank lines."""
import re, pathlib
H = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-7-hindi-plain-zeroshot_split_chapters")
FILES = ["3-03-asavagocchaka.md", "3-04-sannojanagocchaka.md", "3-05-ganthagocchaka.md",
         "3-06-oghayogagocchaka.md", "3-07-nivaranagocchaka.md", "3-08-paramasagocchaka.md"]
LAT = re.compile(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]{2,}")
ODD = re.compile(r"  |\s[,;।]|,,|और और|\.\s|@@| \)|\( |,।|।।")
for f in FILES:
    t = (H / f).read_bytes().decode("utf-8")
    bad = []
    if "\r" in t or "\n\n\n" in t:
        bad.append("CR/double blank")
    for n, l in enumerate(t.splitlines(), 1):
        body = re.sub(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]", "", re.sub(r"\s*\^\S+$", "", l))
        if LAT.search(body):
            bad.append(f"{n}: Latin {LAT.search(body).group(0)}")
        m = ODD.search(body)
        if m:
            bad.append(f"{n}: odd {m.group(0)!r} …{body[max(0, m.start()-30):m.end()+30]}…")
    print(f, "OK" if not bad else f"{len(bad)} issues")
    for b in bad[:12]:
        print("   ", b)
