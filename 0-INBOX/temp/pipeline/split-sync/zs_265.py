import pathlib, re, difflib
B = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails")
for f in ["AI_translation/english/pi-2-english-plain-zeroshot.md", "3-TRANSFORMATIONS/Translations/en-Contemporary-English-Abhidhamma/pi-2-english-plain-zeroshot.md", "1-SOURCES/Text/pi-2.md"]:
    for l in (B / f).read_text(encoding="utf-8").splitlines():
        if re.search(r"\^2-265\s*$", l) or re.search(r"\^2-265\s*$", l):
            print(f.split("/")[-2][:12], "|", l[:70], "...", l[-60:])
