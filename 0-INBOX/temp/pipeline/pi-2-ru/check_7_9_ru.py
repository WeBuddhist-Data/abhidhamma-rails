# -*- coding: utf-8 -*-
"""Extra checks for chapters 7-9: no «ли», no Latin outside variant brackets, no double blank lines, no CR,
no «:-», no comma directly before a dash after a plain noun list is not checked (manual). Writes nothing."""
import os, re

RU = r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\russian\pi-2-russian-plain-zeroshot_split_chapters"
LATIN = re.compile(r"[A-Za-zĀāĪīŪūṬṭḌḍÑñṆṇṄṅṂṃḶḷ]")
bad = 0
for fn in ("7-satipatthanavibhango.md", "8-sammappadhanavibhango.md", "9-iddhipadavibhango.md"):
    raw = open(os.path.join(RU, fn), "rb").read()
    t = raw.decode("utf-8")
    probs = []
    if b"\r" in raw:
        probs.append("CR")
    if "\n\n\n" in t:
        probs.append("double blank line")
    if re.search(r"(?<![А-Яа-яЁё])ли(?![А-Яа-яЁё])", t):
        probs.append("«ли»")
    if ":-" in t or "—" in t:
        probs.append(":- or em dash")
    for i, l in enumerate(t.split("\n"), 1):
        body = re.sub(r"\[[^\]]*\]", "", re.sub(r"\s*\^[0-9A-Za-z-]+\s*$", "", l))
        if LATIN.search(body):
            probs.append(f"Latin l.{i}")
    print(fn, "OK" if not probs else probs)
    bad += bool(probs)
raise SystemExit(bad)
