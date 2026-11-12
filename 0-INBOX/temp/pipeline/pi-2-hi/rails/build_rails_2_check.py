"""Helper: no double blank lines, no CR, no Latin-script words outside square brackets (chapters 2 and 4)."""
import pathlib
import re

OUT = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters")
for ch in ("2-ayatanavibhango.md", "4-saccavibhango.md"):
    t = (OUT / ch).read_bytes().decode("utf-8")
    bad = []
    if "\r" in t:
        bad.append("CR")
    if "\n\n\n" in t:
        bad.append("double blank")
    for n, line in enumerate(t.splitlines(), 1):
        s = re.sub(r"\[[^\]]*\]", "", re.sub(r"\^[0-9A-Za-z-]+\s*$", "", line))
        lat = re.findall(r"[A-Za-zĀ-ſḀ-ỿ]+", s)
        if lat:
            bad.append((n, lat[:5]))
    print(ch, "OK" if not bad else bad)
