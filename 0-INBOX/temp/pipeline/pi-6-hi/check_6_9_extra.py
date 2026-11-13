r"""Extra checks for 6-01/6-02/9-01/9-02/9-03 Hindi: Latin words outside variant brackets,
double blank lines, CR characters, ":-", "seed"."""
import pathlib
import re

HI = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters")
for f in ["6-01-sankharayamaka.md", "6-02-sankharayamaka.md", "9-01-dhammayamaka.md",
          "9-02-dhammayamaka.md", "9-03-dhammayamaka.md"]:
    raw = (HI / f).read_bytes()
    t = raw.decode("utf-8")
    probs = []
    if b"\r" in raw:
        probs.append("CR")
    if "\n\n\n" in t:
        probs.append("double blank")
    if ":-" in t or "seed" in t.lower():
        probs.append(":- or seed")
    for i, line in enumerate(t.splitlines(), 1):
        s = re.sub(r"\[(?:पाठभेद|वर्तनी-भेद) \([^)]*\): [^\]]*\]", "", line)
        s = re.sub(r"\^[0-9A-Za-z-]+$", "", s)
        if re.search(r"[A-Za-zĀ-ſḀ-ỿ]", s):
            probs.append(f"latin@{i}: {line[:80]}")
    print(f, "OK" if not probs else probs[:10])
