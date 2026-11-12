# -*- coding: utf-8 -*-
"""Extra checks for the Hindi chapter 1: Latin words outside variant brackets, CR, double blank lines,
"seed" words, ":-", sample prefix byte-identical."""
import re, sys

ROOT = r"D:\Work\OpenPecha\abhidhamma-rails"
HI = ROOT + r"\AI_translation\hindi\pi-2-hindi-plain-zeroshot_split_chapters\1-khandhavibhango.md"
SAMPLE = ROOT + r"\0-INBOX\temp\pipeline\pi-2-hi\ch1-sample.md"

raw = open(HI, "rb").read()
text = raw.decode("utf-8")
sample = open(SAMPLE, "rb").read()
errs = []
if not raw.startswith(sample):
    errs.append("does not start with ch1-sample.md")
if b"\r" in raw:
    errs.append("CR found")
if "\n\n\n" in text:
    errs.append("double blank line")
if ":-" in text or "—" in text:
    errs.append("':-' or em dash")
if re.search(r"seed", text, re.I):
    errs.append("'seed' found")
for n, line in enumerate(text.splitlines(), 1):
    body = re.sub(r"\[[^\]]*\]", "", line)
    body = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", body)
    latin = re.findall(r"[A-Za-zĀāĪīŪūṚṛṢṣṬṭḌḍṆṇÑñṄṅṂṃḶḷ]+", body)
    if latin:
        errs.append(f"line {n}: Latin {latin[:5]}")
print("extra checks", "OK" if not errs else "ERRORS")
for e in errs[:30]:
    print("  ", e)
sys.exit(1 if errs else 0)
