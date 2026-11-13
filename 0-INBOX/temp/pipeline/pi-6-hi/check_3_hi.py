r"""Extra checks for 3-0x-ayatanayamaka Hindi: Latin words outside variant brackets,
double blank lines, CR, odd punctuation.  usage: python -I -X utf8 check_3_hi.py"""
import pathlib
import re

HI = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-6-hindi-plain-zeroshot_split_chapters")
for n in range(1, 7):
    f = HI / f"3-0{n}-ayatanayamaka.md"
    raw = f.read_bytes().decode("utf-8")
    probs = []
    if "\r" in raw:
        probs.append("CR")
    if "\n\n\n" in raw:
        probs.append("double blank line")
    for i, line in enumerate(raw.split("\n"), 1):
        body = re.sub(r"\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+$", "", line))
        lat = re.findall(r"[A-Za-zāīūṃñṭḍṅṇḷĀĪŪ]{2,}", body)
        if lat:
            probs.append(f"{i}: latin {lat[:5]}")
        for pat in (r" [,।?]", r"।।", r"\?\?", r"  ", r"और और", r"में में", r"\bके के\b"):
            if re.search(pat, body):
                probs.append(f"{i}: pattern {pat!r}: {body[:120]}")
    print(f.name, "OK" if not probs else probs[:20])
