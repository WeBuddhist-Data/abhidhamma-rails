# -*- coding: utf-8 -*-
"""Extra checks for chapters 4, 5: no «ли», no Latin outside variant brackets, no double blank lines, no CR,
no «—», no ":-"."""
import re, os
D = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters"
for fn in ("4-saccavibhango.md", "5-indriyavibhango.md"):
    raw = open(os.path.join(D, fn), encoding="utf-8", newline="").read()
    probs = []
    if "\r" in raw: probs.append("CR")
    if "\n\n\n" in raw: probs.append("double blank")
    if "—" in raw: probs.append("em dash")
    if ":-" in raw: probs.append(":-")
    for i, line in enumerate(raw.split("\n"), 1):
        if re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", line): probs.append(f"ли at {i}")
        t = re.sub(r"\[вариант [^\]]*\]", "", line)
        t = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", t)
        lat = re.findall(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]+", t)
        if lat: probs.append(f"Latin at {i}: {lat[:5]}")
    print(fn, "OK" if not probs else probs)
