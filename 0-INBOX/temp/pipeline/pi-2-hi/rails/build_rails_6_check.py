"""Extra checks for ch6 Hindi: double blank lines, CR, Latin words outside variant brackets, ':-', leftover markers."""
import pathlib
import re

P = pathlib.Path(r"D:\Work\OpenPecha\abhidhamma-rails\AI_translation\hindi\pi-2-hindi-plain-rails_split_chapters"
                 r"\6-paticcasamuppadavibhango.md")
t = P.read_bytes().decode("utf-8")
print("CR:", "\r" in t, "| double blank:", "\n\n\n" in t, "| ':-':", ":-" in t, "| '<<':", "<<" in t,
      "| em-dash:", "—" in t, "| quotes \":", t.count('"'))
bad = 0
for i, line in enumerate(t.split("\n"), 1):
    s = re.sub(r"\[[^\]]*\]", "", line)
    s = re.sub(r"\^[0-9A-Za-z-]+\s*$", "", s)
    w = re.findall(r"[A-Za-zĀāĪīŪūṄṅÑñṬṭḌḍṆṇḶḷṂṃ]+", s)
    if w:
        bad += 1
        print(i, w[:5])
print("latin lines:", bad)
print("open/close quotes:", t.count("“"), t.count("”"))
