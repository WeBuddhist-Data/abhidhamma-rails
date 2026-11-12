"""Extra checks for chapters 9 and 16: double blank lines, CR, Latin outside brackets, ':-', 'seed'."""
import pathlib
import re

OUT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters")
for f in ("9-iddhipadavibhango.md", "16-nanavibhango.md"):
    t = (OUT / f).read_bytes().decode("utf-8")
    print(f, "CR" if "\r" in t else "noCR", "double-blank" if "\n\n\n" in t else "no-double-blank",
          ":-" in t, "seed" in t.lower())
    for i, line in enumerate(t.splitlines(), 1):
        s = re.sub(r"\[[^\]]*\]", "", line)
        s = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", s)
        lat = re.findall(r"[A-Za-zĀ-ž]+", s)
        if lat:
            print(" latin", i, lat[:5])
