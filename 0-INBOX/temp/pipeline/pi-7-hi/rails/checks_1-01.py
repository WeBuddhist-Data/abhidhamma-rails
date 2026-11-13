"""Brief checks for 1-01 beyond the three pipeline scripts (no files written).
usage (repo root): python -I -B -X utf8 0-INBOX\\temp\\pipeline\\pi-7-hi\\rails\\checks_1-01.py"""
import collections
import pathlib
import re

P = pathlib.Path("AI_translation/pali/pi-7_split_chapters/1-01-kusalattika.md")
H = pathlib.Path("AI_translation/hindi/pi-7-hindi-plain-rails_split_chapters/1-01-kusalattika.md")
t = H.read_text(encoding="utf-8")
p = P.read_text(encoding="utf-8")
print("double blank:", "\n\n\n" in t, "| CR:", "\r" in t, "| em/en dash total:", t.count("—"), t.count("–"),
      "pali:", p.count("–") + p.count("—"))
nob = re.sub(r"\[[^\]]*\]", "", t)
nob = re.sub(r"\^[0-9A-Za-z-]+", "", nob)
latin = re.findall(r"[A-Za-zĀāĪīŪūṂṃṄṅÑñṬṭḌḍṆṇḶḷ]{2,}", nob)
print("latin outside brackets:", collections.Counter(latin).most_common(10))
print("':-' :", ":-" in t, "| …pe… :", "pe…" in t, "| ascii quotes:", '"' in t, "| '!!!':", "!!!" in t,
      "| control chars:", bool(re.search(r"[\x00-\x08\x0b-\x1f]", t)))
hl = [l for l in t.split("\n") if l.strip()]
print("lines:", len(hl), "| double spaces:", sum("  " in l for l in hl), "| space before danda:",
      sum(" ।" in l for l in hl), "| ',,':", sum(",," in l for l in hl), "| ', ।':", sum(", ।" in l for l in hl))
